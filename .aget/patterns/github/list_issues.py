#!/usr/bin/env python3
"""
List and display GitHub issues
Part of Phase 1: GitHub Issues Foundation
"""

import subprocess
import json
import sys
from typing import List, Dict, Optional
from datetime import datetime

class IssueLister:
    """List and display GitHub issues with filtering"""

    def __init__(self, repo: Optional[str] = None):
        """Initialize with optional repo override"""
        self.repo = repo or "aget-framework/aget"

    def list_issues(self, state: str = "open", labels: Optional[List[str]] = None,
                   limit: int = 30) -> List[Dict]:
        """Get issues from GitHub"""
        cmd = [
            "gh", "issue", "list",
            "--repo", self.repo,
            "--state", state,
            "--limit", str(limit),
            "--json", "number,title,state,labels,createdAt,updatedAt,author"
        ]

        if labels:
            cmd.extend(["--label", ",".join(labels)])

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to list issues: {e.stderr}")
            return []

    def format_issue(self, issue: Dict) -> str:
        """Format single issue for display"""
        number = issue["number"]
        title = issue["title"]
        state = issue["state"].upper()

        # Extract severity and type from labels
        severity = "?"
        issue_type = "?"
        for label in issue.get("labels", []):
            name = label["name"]
            if name.startswith("severity:"):
                severity = name.split(":")[1].upper()
            elif name.startswith("type:"):
                issue_type = name.split(":")[1]

        # Format line
        return f"#{number:4d} [{severity:8s}] [{issue_type:11s}] {title[:60]}"

    def display_dashboard(self):
        """Display issue dashboard"""
        print("=" * 80)
        print(" " * 30 + "ISSUE DASHBOARD")
        print("=" * 80)
        print()

        # Get different issue categories
        open_issues = self.list_issues(state="open")
        critical = [i for i in open_issues if any(
            l["name"] == "severity:critical" for l in i.get("labels", []))]
        in_progress = [i for i in open_issues if any(
            l["name"] == "state:in-progress" for l in i.get("labels", []))]
        blocked = [i for i in open_issues if any(
            l["name"] == "state:blocked" for l in i.get("labels", []))]
        needs_triage = [i for i in open_issues if any(
            l["name"] == "route:needs-triage" for l in i.get("labels", []))]

        # Display sections
        if critical:
            print("🔴 CRITICAL ISSUES")
            print("-" * 80)
            for issue in critical:
                print(self.format_issue(issue))
            print()

        if in_progress:
            print("🟡 IN PROGRESS")
            print("-" * 80)
            for issue in in_progress:
                print(self.format_issue(issue))
            print()

        if blocked:
            print("🟠 BLOCKED")
            print("-" * 80)
            for issue in blocked:
                print(self.format_issue(issue))
            print()

        if needs_triage:
            print("📥 NEEDS TRIAGE")
            print("-" * 80)
            for issue in needs_triage[:5]:  # Show first 5
                print(self.format_issue(issue))
            if len(needs_triage) > 5:
                print(f"   ... and {len(needs_triage) - 5} more")
            print()

        # Statistics
        closed_issues = self.list_issues(state="closed", limit=100)

        print("📊 STATISTICS")
        print("-" * 80)
        print(f"Open:        {len(open_issues)}")
        print(f"Closed:      {len(closed_issues)}")
        print(f"Critical:    {len(critical)}")
        print(f"In Progress: {len(in_progress)}")
        print(f"Blocked:     {len(blocked)}")
        print(f"Needs Triage:{len(needs_triage)}")
        print()

        # Priority breakdown
        priority_map = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for issue in open_issues:
            for label in issue.get("labels", []):
                if label["name"].startswith("severity:"):
                    sev = label["name"].split(":")[1]
                    priority_map[sev] = priority_map.get(sev, 0) + 1

        print("PRIORITY BREAKDOWN")
        print("-" * 80)
        print(f"P0 Critical: {priority_map['critical']}")
        print(f"P1 High:     {priority_map['high']}")
        print(f"P2 Medium:   {priority_map['medium']}")
        print(f"P3 Low:      {priority_map['low']}")
        print()

        print("=" * 80)

    def display_list(self, issues: List[Dict], title: str = "Issues"):
        """Display a list of issues"""
        if not issues:
            print(f"No {title.lower()} found")
            return

        print(f"\n{title} ({len(issues)} total)")
        print("-" * 80)
        print(f"{'#':>5s} {'Severity':^10s} {'Type':^12s} {'Title'}")
        print("-" * 80)

        for issue in issues:
            print(self.format_issue(issue))

        print()


def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description="List GitHub issues")
    parser.add_argument("--state", choices=["open", "closed", "all"], default="open",
                       help="Issue state to filter")
    parser.add_argument("--labels", nargs="+", help="Filter by labels")
    parser.add_argument("--dashboard", action="store_true", help="Show dashboard view")
    parser.add_argument("--repo", help="Repository (defaults to hub)")
    parser.add_argument("--limit", type=int, default=30, help="Maximum issues to fetch")
    parser.add_argument("--severity", choices=["critical", "high", "medium", "low"],
                       help="Filter by severity")
    parser.add_argument("--type", choices=["bug", "feature", "improvement", "discovery", "question"],
                       help="Filter by type")

    args = parser.parse_args()

    # Build label filters
    labels = args.labels or []
    if args.severity:
        labels.append(f"severity:{args.severity}")
    if args.type:
        labels.append(f"type:{args.type}")

    # Create lister
    lister = IssueLister(args.repo)

    if args.dashboard:
        lister.display_dashboard()
    else:
        issues = lister.list_issues(state=args.state, labels=labels if labels else None,
                                   limit=args.limit)
        title = f"{args.state.title()} Issues"
        if labels:
            title += f" (labels: {', '.join(labels)})"
        lister.display_list(issues, title)


if __name__ == "__main__":
    main()