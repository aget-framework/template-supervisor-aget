#!/usr/bin/env python3
"""
Official AGET v2.0 Compliance Verification Tool
Validates agent structure, patterns, and protocols
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

class ComplianceChecker:
    """Official v2.0 compliance verification"""

    def __init__(self, agent_path: str = "."):
        """Initialize with agent path"""
        self.agent_path = Path(agent_path)
        self.results = {
            "passed": [],
            "failed": [],
            "warnings": [],
            "score": 0,
            "max_score": 0
        }

    def check_all(self) -> Dict:
        """Run all compliance checks"""
        print("=" * 60)
        print(" " * 20 + "AGET v2.0 Compliance Check")
        print("=" * 60)
        print()

        # Version check
        self._check_version()

        # Directory structure
        self._check_directory_structure()

        # Pattern location and organization
        self._check_patterns()

        # CLAUDE.md protocols
        self._check_protocols()

        # Self-containment (ARCH-001)
        self._check_self_containment()

        # GitHub integration
        self._check_github_integration()

        # Generate report
        return self._generate_report()

    def _check_version(self):
        """Check version.json compliance"""
        print("📋 Checking Version...")

        version_file = self.agent_path / ".aget" / "version.json"
        if not version_file.exists():
            self._fail("No .aget/version.json found")
            return

        try:
            with open(version_file) as f:
                version_data = json.load(f)

            version = version_data.get("aget_version", "")
            if version == "2.0.0":
                self._pass("Version 2.0.0 ✓")
            elif version.startswith("2.0.0"):
                self._warn(f"Version {version} (pre-release)")
            else:
                self._fail(f"Version {version} (not v2.0)")

            # Check required fields
            if "created" in version_data:
                self._pass("Has creation date ✓")
            else:
                self._warn("Missing creation date")

        except Exception as e:
            self._fail(f"Invalid version.json: {e}")

    def _check_directory_structure(self):
        """Check v2.0 directory structure"""
        print("\n📁 Checking Directory Structure...")

        required_dirs = {
            ".aget": "Framework metadata",
            ".aget/patterns": "Pattern storage",
            ".aget/evolution": "Decision tracking",
            ".aget/checkpoints": "State snapshots",
            "sessions": "Session notes",
            "workspace": "Agent workspace",
            "products": "Public products"
        }

        for dir_path, description in required_dirs.items():
            full_path = self.agent_path / dir_path
            if full_path.exists():
                self._pass(f"{dir_path}/ exists ✓")
            else:
                self._fail(f"{dir_path}/ missing ({description})")

        # Check for old structure
        old_patterns = self.agent_path / "patterns"
        if old_patterns.exists():
            self._fail("Root patterns/ still exists (should be in .aget/patterns/)")

    def _check_patterns(self):
        """Check pattern installation and organization"""
        print("\n🔧 Checking Patterns...")

        patterns_dir = self.agent_path / ".aget" / "patterns"

        # Essential patterns
        essential_patterns = {
            "session/wake_up.py": "Session initialization",
            "session/wind_down.py": "Session completion",
            "github/create_issue.py": "Issue creation",
            "github/list_issues.py": "Issue listing",
            "routing/agent_discovery.py": "Agent discovery",
            "documentation/smart_reader.py": "Document reading"
        }

        for pattern_path, description in essential_patterns.items():
            full_path = patterns_dir / pattern_path
            if full_path.exists():
                self._pass(f"{pattern_path} ✓")
            else:
                # Check for alternate names
                alt_name = pattern_path.replace("wake_up", "wake").replace("wind_down_safe", "sign_off")
                alt_path = patterns_dir / alt_name
                if alt_path.exists():
                    self._warn(f"{pattern_path} missing (found {alt_name})")
                else:
                    self._fail(f"{pattern_path} missing ({description})")

        # Count total patterns
        pattern_count = len(list(patterns_dir.rglob("*.py"))) if patterns_dir.exists() else 0
        if pattern_count >= 10:
            self._pass(f"{pattern_count} patterns installed ✓")
        elif pattern_count >= 5:
            self._warn(f"Only {pattern_count} patterns (minimum 10 recommended)")
        else:
            self._fail(f"Only {pattern_count} patterns")

    def _check_protocols(self):
        """Check CLAUDE.md protocols"""
        print("\n📜 Checking Protocols...")

        claude_file = self.agent_path / "CLAUDE.md"
        if not claude_file.exists():
            self._fail("No CLAUDE.md found")
            return

        try:
            content = claude_file.read_text().lower()

            # Required protocols
            protocols = {
                "wake up": "Session wake protocol",
                "wind down": "Session completion protocol",
                "github": "GitHub integration",
                ".aget/patterns": "Pattern location",
                "task tool": "Efficiency rules",
                "substantial change": "Planning protocol"
            }

            for keyword, description in protocols.items():
                if keyword in content:
                    self._pass(f"{description} ✓")
                else:
                    self._fail(f"{description} missing")

        except Exception as e:
            self._fail(f"Cannot read CLAUDE.md: {e}")

    def _check_self_containment(self):
        """Check ARCH-001 self-containment"""
        print("\n🔒 Checking Self-Containment (ARCH-001)...")

        patterns_dir = self.agent_path / ".aget" / "patterns"
        if not patterns_dir.exists():
            self._warn("No patterns to check")
            return

        external_deps = []
        for py_file in patterns_dir.rglob("*.py"):
            try:
                content = py_file.read_text()
                # Check for relative imports outside agent
                if "from .." in content or "import .." in content:
                    if "../.." in content:  # Outside agent directory
                        external_deps.append(str(py_file.relative_to(self.agent_path)))
            except:
                pass

        if external_deps:
            self._fail(f"External dependencies found in {len(external_deps)} files")
            for dep in external_deps[:3]:
                print(f"    - {dep}")
        else:
            self._pass("All patterns self-contained ✓")

    def _check_github_integration(self):
        """Check GitHub integration setup"""
        print("\n🐙 Checking GitHub Integration...")

        # Check for gh CLI
        try:
            result = subprocess.run(["gh", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                self._pass("GitHub CLI available ✓")
            else:
                self._warn("GitHub CLI not working")
        except:
            self._warn("GitHub CLI not installed")

        # Check GitHub patterns
        github_dir = self.agent_path / ".aget" / "patterns" / "github"
        if github_dir.exists():
            pattern_count = len(list(github_dir.glob("*.py")))
            if pattern_count >= 3:
                self._pass(f"{pattern_count} GitHub patterns ✓")
            else:
                self._warn(f"Only {pattern_count} GitHub patterns")
        else:
            self._fail("No GitHub patterns directory")

    def _pass(self, message: str):
        """Record passing check"""
        self.results["passed"].append(message)
        self.results["score"] += 1
        self.results["max_score"] += 1
        print(f"  ✅ {message}")

    def _fail(self, message: str):
        """Record failing check"""
        self.results["failed"].append(message)
        self.results["max_score"] += 1
        print(f"  ❌ {message}")

    def _warn(self, message: str):
        """Record warning"""
        self.results["warnings"].append(message)
        self.results["score"] += 0.5
        self.results["max_score"] += 1
        print(f"  ⚠️  {message}")

    def _generate_report(self) -> Dict:
        """Generate compliance report"""
        print("\n" + "=" * 60)
        print(" " * 20 + "COMPLIANCE REPORT")
        print("=" * 60)

        # Calculate percentage
        percentage = (self.results["score"] / self.results["max_score"] * 100) if self.results["max_score"] > 0 else 0

        # Determine status
        if percentage >= 90:
            status = "✅ FULLY COMPLIANT"
            emoji = "🎉"
        elif percentage >= 70:
            status = "⚠️  MOSTLY COMPLIANT"
            emoji = "👍"
        else:
            status = "❌ NOT COMPLIANT"
            emoji = "🔧"

        print(f"\nScore: {self.results['score']:.1f}/{self.results['max_score']}")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Status: {status} {emoji}")

        print(f"\n✅ Passed: {len(self.results['passed'])}")
        print(f"⚠️  Warnings: {len(self.results['warnings'])}")
        print(f"❌ Failed: {len(self.results['failed'])}")

        if self.results["failed"]:
            print("\n🔧 Required Fixes:")
            for item in self.results["failed"][:5]:
                print(f"  - {item}")

        if self.results["warnings"]:
            print("\n💡 Recommendations:")
            for item in self.results["warnings"][:3]:
                print(f"  - {item}")

        # Save report
        report = {
            "timestamp": datetime.now().isoformat(),
            "version": "2.0.0",
            "agent_path": str(self.agent_path),
            "score": self.results["score"],
            "max_score": self.results["max_score"],
            "percentage": percentage,
            "status": status,
            "passed": len(self.results["passed"]),
            "warnings": len(self.results["warnings"]),
            "failed": len(self.results["failed"]),
            "details": self.results
        }

        report_file = self.agent_path / ".aget" / "compliance_report.json"
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)

        print(f"\n📄 Report saved to: {report_file}")
        print("=" * 60)

        return report


def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description="AGET v2.0 Compliance Checker")
    parser.add_argument("--path", default=".", help="Path to agent directory")
    parser.add_argument("--json", action="store_true", help="Output JSON report")

    args = parser.parse_args()

    checker = ComplianceChecker(args.path)
    report = checker.check_all()

    if args.json:
        print("\nJSON Report:")
        print(json.dumps(report, indent=2))

    # Exit code based on compliance
    if report["percentage"] >= 90:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()