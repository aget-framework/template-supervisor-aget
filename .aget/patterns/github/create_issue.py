#!/usr/bin/env python3
"""
Create GitHub issues with AGET conventions
Part of Phase 1: GitHub Issues Foundation
"""

import subprocess
import json
import sys
from typing import List, Optional
from pathlib import Path
from datetime import datetime

class IssueCreator:
    """Create GitHub issues with proper labels and formatting"""

    def __init__(self, repo: Optional[str] = None):
        """Initialize with optional repo override"""
        self.repo = repo or self._get_repo()
        self.agent_name = self._get_agent_name()

    def _get_repo(self) -> str:
        """Get repository from git remote or default to hub"""
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=True
            )
            url = result.stdout.strip()
            if "github.com" in url:
                parts = url.split("github.com")[1]
                parts = parts.strip(":/").replace(".git", "")
                # Default to hub repo for agent filing
                return "aget-framework/aget"
        except:
            return "aget-framework/aget"

    def _get_agent_name(self) -> str:
        """Get agent name from current directory"""
        cwd = Path.cwd()
        if "aget" in cwd.name:
            return cwd.name
        return "unknown-agent"

    def detect_severity(self, title: str, body: str) -> str:
        """Auto-detect severity from content"""
        content = f"{title} {body}".lower()

        if any(word in content for word in ["data loss", "security", "critical", "crash"]):
            return "critical"
        elif any(word in content for word in ["broken", "fail", "error", "bug"]):
            return "high"
        elif any(word in content for word in ["slow", "improve", "enhance"]):
            return "medium"
        else:
            return "low"

    def detect_type(self, title: str, body: str) -> str:
        """Auto-detect issue type from content"""
        content = f"{title} {body}".lower()

        if any(word in content for word in ["bug", "broken", "fail", "error"]):
            return "bug"
        elif any(word in content for word in ["feature", "add", "new"]):
            return "feature"
        elif any(word in content for word in ["improve", "enhance", "optimize"]):
            return "improvement"
        elif any(word in content for word in ["discover", "found", "notice"]):
            return "discovery"
        else:
            return "question"

    def build_labels(self, severity: str, issue_type: str, extra_labels: List[str] = None) -> str:
        """Build label string for issue"""
        labels = [
            f"severity:{severity}",
            f"type:{issue_type}",
            f"from:{self.agent_name}",
            "from:agent"
        ]

        # Add special labels
        if severity == "critical":
            if "data loss" in (extra_labels or []):
                labels.append("data-loss-risk")

        # Add routing label
        labels.append("route:needs-triage")

        # Add extra labels
        if extra_labels:
            labels.extend(extra_labels)

        return ",".join(labels)

    def format_body(self, body: str, metadata: dict = None) -> str:
        """Format issue body with metadata"""
        sections = []

        # Header with agent info
        sections.append(f"**Filed by**: {self.agent_name}")
        sections.append(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        if metadata:
            if "affected_files" in metadata:
                sections.append(f"**Affected files**: {', '.join(metadata['affected_files'])}")
            if "environment" in metadata:
                sections.append(f"**Environment**: {metadata['environment']}")

        sections.append("")  # Blank line
        sections.append("## Description")
        sections.append(body)

        if metadata:
            if "reproduction" in metadata:
                sections.append("")
                sections.append("## Reproduction Steps")
                for i, step in enumerate(metadata["reproduction"], 1):
                    sections.append(f"{i}. {step}")

            if "impact" in metadata:
                sections.append("")
                sections.append("## Impact")
                sections.append(metadata["impact"])

        # Footer
        sections.append("")
        sections.append("---")
        sections.append(f"*Automatically filed by {self.agent_name} via AGET issue system*")

        return "\n".join(sections)

    def create(self, title: str, body: str, severity: Optional[str] = None,
               issue_type: Optional[str] = None, labels: Optional[List[str]] = None,
               metadata: Optional[dict] = None) -> Optional[int]:
        """Create a GitHub issue"""

        # Auto-detect if not provided
        if not severity:
            severity = self.detect_severity(title, body)
        if not issue_type:
            issue_type = self.detect_type(title, body)

        # Format body
        formatted_body = self.format_body(body, metadata)

        # Build labels
        label_string = self.build_labels(severity, issue_type, labels)

        # Add agent prefix to title
        if not title.startswith(f"[{self.agent_name}]"):
            title = f"[{self.agent_name}] {title}"

        # Create issue using gh CLI
        cmd = [
            "gh", "issue", "create",
            "--repo", self.repo,
            "--title", title,
            "--body", formatted_body,
            "--label", label_string
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            # Extract issue number from output
            output = result.stdout.strip()
            if "issues/" in output:
                issue_num = output.split("issues/")[-1]
                return int(issue_num)
            return None
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create issue: {e.stderr}")
            return None


def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description="Create GitHub issue")
    parser.add_argument("--title", required=True, help="Issue title")
    parser.add_argument("--body", required=True, help="Issue description")
    parser.add_argument("--severity", choices=["critical", "high", "medium", "low"],
                       help="Issue severity (auto-detected if not provided)")
    parser.add_argument("--type", choices=["bug", "feature", "improvement", "discovery", "question"],
                       help="Issue type (auto-detected if not provided)")
    parser.add_argument("--labels", nargs="+", help="Additional labels")
    parser.add_argument("--repo", help="Repository (defaults to hub)")
    parser.add_argument("--affected-files", nargs="+", help="Affected files")
    parser.add_argument("--reproduction", nargs="+", help="Reproduction steps")
    parser.add_argument("--impact", help="Impact description")

    args = parser.parse_args()

    # Build metadata
    metadata = {}
    if args.affected_files:
        metadata["affected_files"] = args.affected_files
    if args.reproduction:
        metadata["reproduction"] = args.reproduction
    if args.impact:
        metadata["impact"] = args.impact

    # Create issue
    creator = IssueCreator(args.repo)
    issue_num = creator.create(
        title=args.title,
        body=args.body,
        severity=args.severity,
        issue_type=args.type,
        labels=args.labels,
        metadata=metadata
    )

    if issue_num:
        print(f"✅ Created issue #{issue_num}")
        print(f"   View at: https://github.com/{creator.repo}/issues/{issue_num}")
    else:
        print("❌ Failed to create issue")
        sys.exit(1)


if __name__ == "__main__":
    main()