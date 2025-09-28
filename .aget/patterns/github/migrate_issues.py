#!/usr/bin/env python3
"""
Migrate YAML issues to GitHub Issues
Part of Phase 1: GitHub Issues Foundation
"""

import yaml
import subprocess
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class IssueMigrator:
    """Migrate YAML issues to GitHub"""

    def __init__(self, repo: Optional[str] = None):
        """Initialize migrator"""
        self.repo = repo or "aget-framework/aget"
        self.migrated = []
        self.failed = []

    def load_yaml_issue(self, file_path: Path) -> Dict:
        """Load a YAML issue file"""
        try:
            with open(file_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"❌ Failed to load {file_path}: {e}")
            return None

    def yaml_to_github_format(self, yaml_issue: Dict) -> Dict:
        """Convert YAML format to GitHub issue format"""
        metadata = yaml_issue.get('metadata', {})
        issue = yaml_issue.get('issue', {})
        status = yaml_issue.get('status', {})
        impact = yaml_issue.get('impact', {})
        resolution = yaml_issue.get('resolution', {})

        # Build title
        title = issue.get('title', 'No title')
        filed_by = metadata.get('filed_by', 'unknown')
        if not title.startswith(f"[{filed_by}]"):
            title = f"[{filed_by}] {title}"

        # Build body
        body_sections = []
        body_sections.append(f"**Original ID**: {metadata.get('id', 'unknown')}")
        body_sections.append(f"**Filed by**: {filed_by}")
        body_sections.append(f"**Original date**: {metadata.get('timestamp', 'unknown')}")

        if issue.get('affected_components'):
            components = []
            for comp in issue['affected_components']:
                if isinstance(comp, dict):
                    components.append(f"{comp.get('file', '')}:{comp.get('lines', '')}")
                else:
                    components.append(str(comp))
            body_sections.append(f"**Affected components**: {', '.join(components)}")

        body_sections.append("")
        body_sections.append("## Description")
        body_sections.append(issue.get('description', 'No description'))

        # Add reproduction steps
        if issue.get('reproduction', {}).get('steps'):
            body_sections.append("")
            body_sections.append("## Reproduction Steps")
            for i, step in enumerate(issue['reproduction']['steps'], 1):
                body_sections.append(f"{i}. {step}")

        # Add evidence
        if issue.get('evidence'):
            body_sections.append("")
            body_sections.append("## Evidence")
            if issue['evidence'].get('logs'):
                body_sections.append("**Logs:**")
                for log in issue['evidence']['logs']:
                    body_sections.append(f"- {log}")

        # Add impact
        if impact:
            body_sections.append("")
            body_sections.append("## Impact")
            body_sections.append(f"- Users affected: {impact.get('users_affected', 'unknown')}")
            body_sections.append(f"- Data loss risk: {impact.get('data_loss_risk', False)}")
            body_sections.append(f"- Security risk: {impact.get('security_risk', False)}")
            if impact.get('workaround'):
                body_sections.append(f"- Workaround: {impact['workaround']}")

        # Add resolution if exists
        if resolution and status.get('state') == 'RESOLVED':
            body_sections.append("")
            body_sections.append("## Resolution")
            body_sections.append(resolution.get('solution', 'No solution provided'))
            if resolution.get('prevention'):
                body_sections.append("")
                body_sections.append("**Prevention:**")
                body_sections.append(resolution['prevention'])

        body_sections.append("")
        body_sections.append("---")
        body_sections.append("*Migrated from YAML issue format*")

        # Build labels
        labels = []

        # Severity
        severity = metadata.get('severity', 'medium').lower()
        labels.append(f"severity:{severity}")

        # Type
        issue_type = metadata.get('type', 'bug').lower()
        labels.append(f"type:{issue_type}")

        # From agent
        labels.append(f"from:{filed_by}")
        labels.append("from:agent")

        # State
        state = status.get('state', 'OPEN')
        if state == 'IN_PROGRESS':
            labels.append("state:in-progress")
        elif state == 'BLOCKED':
            labels.append("state:blocked")
        elif state == 'RESOLVED':
            labels.append("state:ready-to-close")

        # Special labels
        if impact.get('data_loss_risk'):
            labels.append("data-loss-risk")

        # Tags - map to appropriate project labels
        if metadata.get('tags'):
            for tag in metadata['tags']:
                if tag in ['git', 'session']:
                    labels.append("project:github-workspace")
                elif tag in ['patterns', 'efficiency']:
                    labels.append("project:aget-framework")
                elif tag == 'spotify':
                    labels.append("project:spotify")

        return {
            "title": title,
            "body": "\n".join(body_sections),
            "labels": labels,
            "state": "closed" if state == "RESOLVED" else "open"
        }

    def create_github_issue(self, issue_data: Dict) -> Optional[int]:
        """Create a GitHub issue from converted data"""
        cmd = [
            "gh", "issue", "create",
            "--repo", self.repo,
            "--title", issue_data["title"],
            "--body", issue_data["body"],
            "--label", ",".join(issue_data["labels"])
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            output = result.stdout.strip()
            if "issues/" in output:
                issue_num = output.split("issues/")[-1]

                # If state should be closed, close it
                if issue_data["state"] == "closed":
                    close_cmd = ["gh", "issue", "close", issue_num, "--repo", self.repo]
                    subprocess.run(close_cmd, capture_output=True, text=True)

                return int(issue_num)
            return None
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create issue: {e.stderr}")
            return None

    def migrate_file(self, file_path: Path) -> bool:
        """Migrate a single YAML file"""
        print(f"📄 Migrating {file_path.name}...")

        # Load YAML
        yaml_issue = self.load_yaml_issue(file_path)
        if not yaml_issue:
            self.failed.append(file_path)
            return False

        # Convert format
        github_data = self.yaml_to_github_format(yaml_issue)

        # Create on GitHub
        issue_num = self.create_github_issue(github_data)
        if issue_num:
            print(f"   ✅ Created issue #{issue_num}")
            self.migrated.append((file_path, issue_num))

            # Create backup with issue number
            backup_dir = Path(".aget/backups/migration")
            backup_dir.mkdir(parents=True, exist_ok=True)
            backup_file = backup_dir / f"{file_path.stem}_gh{issue_num}.yaml"

            # Add GitHub number to YAML
            yaml_issue['github_issue'] = issue_num
            yaml_issue['migrated_at'] = datetime.now().isoformat()

            with open(backup_file, 'w') as f:
                yaml.dump(yaml_issue, f)

            return True
        else:
            self.failed.append(file_path)
            return False

    def migrate_directory(self, directory: Path) -> None:
        """Migrate all YAML files in directory"""
        yaml_files = list(directory.glob("*.yaml")) + list(directory.glob("*.yml"))

        if not yaml_files:
            print(f"No YAML files found in {directory}")
            return

        print(f"🚀 Migrating {len(yaml_files)} issues to GitHub...")
        print()

        for file_path in yaml_files:
            self.migrate_file(file_path)
            print()

        # Summary
        print("=" * 60)
        print("MIGRATION SUMMARY")
        print("=" * 60)
        print(f"✅ Successfully migrated: {len(self.migrated)}")
        print(f"❌ Failed: {len(self.failed)}")

        if self.migrated:
            print("\nMigrated issues:")
            for file_path, issue_num in self.migrated:
                print(f"  - {file_path.name} → Issue #{issue_num}")
                print(f"    https://github.com/{self.repo}/issues/{issue_num}")

        if self.failed:
            print("\nFailed migrations:")
            for file_path in self.failed:
                print(f"  - {file_path.name}")


def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description="Migrate YAML issues to GitHub")
    parser.add_argument("path", nargs="?", default=".aget/issues",
                       help="Path to YAML file or directory (default: .aget/issues)")
    parser.add_argument("--repo", help="Target repository (defaults to hub)")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be migrated without creating issues")

    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"❌ Path not found: {path}")
        sys.exit(1)

    migrator = IssueMigrator(args.repo)

    if path.is_file():
        success = migrator.migrate_file(path)
        sys.exit(0 if success else 1)
    else:
        migrator.migrate_directory(path)
        sys.exit(0 if not migrator.failed else 1)


if __name__ == "__main__":
    main()