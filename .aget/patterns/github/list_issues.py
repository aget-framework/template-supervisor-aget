#!/usr/bin/env python3
"""List GitHub issues pattern for AGET v2.0."""

import subprocess
import json
from typing import List, Dict, Any

def list_issues(repo: str = "aget-framework/aget", state: str = "open", limit: int = 10) -> List[Dict[str, Any]]:
    """List GitHub issues using gh CLI.

    Args:
        repo: Repository (defaults to AGET hub)
        state: Issue state (open, closed, all)
        limit: Maximum number of issues to return

    Returns:
        List of issues or error
    """
    cmd = ["gh", "issue", "list",
           "--repo", repo,
           "--state", state,
           "--limit", str(limit),
           "--json", "number,title,state,labels,url"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return [{"error": e.stderr}]

if __name__ == "__main__":
    # Example usage
    print("GitHub issue listing pattern installed for AGET v2.0")