#!/usr/bin/env python3
"""Update GitHub issue pattern for AGET v2.0."""

import subprocess
from typing import Dict, Any

def update_issue(issue_number: int, comment: str = None, state: str = None, repo: str = "aget-framework/aget") -> Dict[str, Any]:
    """Update or comment on a GitHub issue using gh CLI.

    Args:
        issue_number: Issue number to update
        comment: Optional comment to add
        state: Optional state change (open, closed)
        repo: Repository (defaults to AGET hub)

    Returns:
        Update result or error
    """
    results = []

    if comment:
        cmd = ["gh", "issue", "comment", str(issue_number),
               "--repo", repo,
               "--body", comment]
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            results.append({"comment": "added"})
        except subprocess.CalledProcessError as e:
            results.append({"error": e.stderr})

    if state:
        action = "close" if state == "closed" else "reopen"
        cmd = ["gh", "issue", action, str(issue_number), "--repo", repo]
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            results.append({action: "success"})
        except subprocess.CalledProcessError as e:
            results.append({"error": e.stderr})

    return {"success": len(results) > 0, "actions": results}

if __name__ == "__main__":
    # Example usage
    print("GitHub issue update pattern installed for AGET v2.0")