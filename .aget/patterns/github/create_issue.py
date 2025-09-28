#!/usr/bin/env python3
"""Create GitHub issue pattern for AGET v2.0."""

import subprocess
import json
from typing import Dict, Any

def create_issue(title: str, body: str, labels: list = None, repo: str = "aget-framework/aget") -> Dict[str, Any]:
    """Create a GitHub issue using gh CLI.

    Args:
        title: Issue title
        body: Issue body/description
        labels: Optional list of labels
        repo: Repository (defaults to AGET hub)

    Returns:
        Issue details or error
    """
    cmd = ["gh", "issue", "create",
           "--repo", repo,
           "--title", title,
           "--body", body]

    if labels:
        cmd.extend(["--label", ",".join(labels)])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"success": True, "url": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": e.stderr}

if __name__ == "__main__":
    # Example usage
    print("GitHub issue creation pattern installed for AGET v2.0")