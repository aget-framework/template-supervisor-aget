#!/usr/bin/env python3
"""
Update GitHub issues
Part of Phase 1: GitHub Issues Foundation
"""

import subprocess
import json
import sys
from typing import List, Optional
from datetime import datetime

class IssueUpdater:
    """Update GitHub issues with state changes and labels"""

    def __init__(self, repo: Optional[str] = None):
        """Initialize with optional repo override"""
        self.repo = repo or "aget-framework/aget"

    def update_state(self, issue_number: int, state: str) -> bool:
        """Update issue state"""
        if state in ["closed", "close"]:
            return self.close_issue(issue_number)
        elif state == "open":
            return self.reopen_issue(issue_number)
        else:
            # State is a label like "in-progress"
            return self.add_label(issue_number, f"state:{state}")

    def close_issue(self, issue_number: int, comment: Optional[str] = None) -> bool:
        """Close an issue"""
        cmd = ["gh", "issue", "close", str(issue_number), "--repo", self.repo]

        if comment:
            cmd.extend(["--comment", comment])

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Closed issue #{issue_number}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to close issue: {e.stderr}")
            return False

    def reopen_issue(self, issue_number: int) -> bool:
        """Reopen a closed issue"""
        cmd = ["gh", "issue", "reopen", str(issue_number), "--repo", self.repo]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Reopened issue #{issue_number}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to reopen issue: {e.stderr}")
            return False

    def add_label(self, issue_number: int, label: str) -> bool:
        """Add a label to an issue"""
        cmd = ["gh", "issue", "edit", str(issue_number), "--repo", self.repo,
               "--add-label", label]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Added label '{label}' to issue #{issue_number}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to add label: {e.stderr}")
            return False

    def remove_label(self, issue_number: int, label: str) -> bool:
        """Remove a label from an issue"""
        cmd = ["gh", "issue", "edit", str(issue_number), "--repo", self.repo,
               "--remove-label", label]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Removed label '{label}' from issue #{issue_number}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to remove label: {e.stderr}")
            return False

    def add_comment(self, issue_number: int, comment: str) -> bool:
        """Add a comment to an issue"""
        cmd = ["gh", "issue", "comment", str(issue_number), "--repo", self.repo,
               "--body", comment]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Added comment to issue #{issue_number}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to add comment: {e.stderr}")
            return False

    def assign_issue(self, issue_number: int, assignee: str) -> bool:
        """Assign issue to user"""
        cmd = ["gh", "issue", "edit", str(issue_number), "--repo", self.repo,
               "--add-assignee", assignee]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Assigned issue #{issue_number} to {assignee}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to assign issue: {e.stderr}")
            return False

    def update_severity(self, issue_number: int, new_severity: str) -> bool:
        """Update issue severity"""
        # Remove old severity labels
        for old_sev in ["critical", "high", "medium", "low"]:
            if old_sev != new_severity:
                self.remove_label(issue_number, f"severity:{old_sev}")

        # Add new severity
        return self.add_label(issue_number, f"severity:{new_severity}")

    def mark_resolved(self, issue_number: int, solution: str) -> bool:
        """Mark issue as resolved with solution"""
        # Add resolved comment
        comment = f"""## Resolution

{solution}

---
*Resolved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"""

        # Update labels
        self.remove_label(issue_number, "route:needs-triage")
        self.add_label(issue_number, "route:resolved")
        self.add_label(issue_number, "state:ready-to-close")

        # Add comment
        self.add_comment(issue_number, comment)

        return True

    def mark_blocked(self, issue_number: int, blocked_by: List[int]) -> bool:
        """Mark issue as blocked by other issues"""
        # Add blocked label
        self.add_label(issue_number, "state:blocked")

        # Add comment about blocking
        blocking_refs = ", ".join([f"#{n}" for n in blocked_by])
        comment = f"⚠️ Blocked by: {blocking_refs}"
        self.add_comment(issue_number, comment)

        return True


def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description="Update GitHub issue")
    parser.add_argument("issue", type=int, help="Issue number")
    parser.add_argument("--state", choices=["open", "closed", "in-progress", "blocked",
                                           "investigating", "needs-review", "ready-to-close"],
                       help="Update issue state")
    parser.add_argument("--severity", choices=["critical", "high", "medium", "low"],
                       help="Update severity")
    parser.add_argument("--add-label", dest="add_labels", action="append",
                       help="Add label(s)")
    parser.add_argument("--remove-label", dest="remove_labels", action="append",
                       help="Remove label(s)")
    parser.add_argument("--comment", help="Add comment")
    parser.add_argument("--assign", help="Assign to user")
    parser.add_argument("--resolve", help="Mark as resolved with solution")
    parser.add_argument("--blocked-by", type=int, nargs="+", help="Mark as blocked by issue(s)")
    parser.add_argument("--repo", help="Repository (defaults to hub)")

    args = parser.parse_args()

    # Create updater
    updater = IssueUpdater(args.repo)

    # Process updates
    success = True

    if args.state:
        success &= updater.update_state(args.issue, args.state)

    if args.severity:
        success &= updater.update_severity(args.issue, args.severity)

    if args.add_labels:
        for label in args.add_labels:
            success &= updater.add_label(args.issue, label)

    if args.remove_labels:
        for label in args.remove_labels:
            success &= updater.remove_label(args.issue, label)

    if args.comment:
        success &= updater.add_comment(args.issue, args.comment)

    if args.assign:
        success &= updater.assign_issue(args.issue, args.assign)

    if args.resolve:
        success &= updater.mark_resolved(args.issue, args.resolve)

    if args.blocked_by:
        success &= updater.mark_blocked(args.issue, args.blocked_by)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()