#!/usr/bin/env python3
"""
Setup GitHub labels for AGET issue management
Creates or updates all required labels
"""

import subprocess
import json
import sys
from typing import Dict, List, Tuple

# Label definitions
LABELS = {
    # Severity labels (Red shades)
    "severity:critical": ("B60205", "Data loss, security, or system failure"),
    "severity:high": ("D93F0B", "Major functionality broken"),
    "severity:medium": ("E99695", "Important but workaroundable"),
    "severity:low": ("FBCA04", "Minor inconvenience"),

    # Type labels (Blue shades)
    "type:bug": ("0E4C92", "Something broken"),
    "type:feature": ("1E88E5", "New capability"),
    "type:improvement": ("64B5F6", "Enhancement to existing"),
    "type:discovery": ("90CAF9", "Finding or insight"),
    "type:question": ("BBDEFB", "Needs clarification"),

    # State labels (Yellow/Orange shades)
    "state:investigating": ("FFF176", "Being analyzed"),
    "state:blocked": ("FFB74D", "Waiting on dependency"),
    "state:in-progress": ("FFD54F", "Actively working"),
    "state:needs-review": ("FFEE58", "Ready for review"),
    "state:ready-to-close": ("FFF59D", "Can be closed"),

    # Agent labels (Purple shades)
    "from:agent": ("7B1FA2", "Filed by an agent"),
    "from:my-AGET-aget": ("8E24AA", "Filed by my-AGET-aget"),
    "from:my-example-aget": ("9C27B0", "Filed by my-example-aget"),
    "from:my-spotify-aget": ("AB47BC", "Filed by spotify agent"),
    "from:my-github-aget": ("BA68C8", "Filed by github agent"),

    # Routing labels (Green shades)
    "route:needs-triage": ("2E7D32", "Needs routing decision"),
    "route:my-AGET-template": ("388E3C", "For template repo"),
    "route:spotify": ("43A047", "For spotify project"),
    "route:resolved": ("66BB6A", "Routing complete"),

    # Project labels (Teal shades)
    "project:aget-framework": ("00695C", "AGET framework issues"),
    "project:spotify": ("00796B", "Spotify project"),
    "project:github-workspace": ("00897B", "GitHub workspace"),
    "project:internal": ("009688", "Internal tooling"),

    # Special labels
    "data-loss-risk": ("B60205", "Can cause data loss"),
}

def get_repo() -> str:
    """Get the repository name from git remote"""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        url = result.stdout.strip()
        # Extract owner/repo from URL
        if "github.com" in url:
            parts = url.split("github.com")[1]
            parts = parts.strip(":/").replace(".git", "")
            return parts
    except:
        return "aget-framework/aget"  # Default

def get_existing_labels(repo: str) -> Dict[str, Tuple[str, str]]:
    """Get existing labels from repository"""
    try:
        result = subprocess.run(
            ["gh", "label", "list", "--repo", repo, "--limit", "100", "--json", "name,color,description"],
            capture_output=True,
            text=True,
            check=True
        )
        labels = json.loads(result.stdout)
        return {label["name"]: (label["color"], label.get("description", "")) for label in labels}
    except Exception as e:
        print(f"Error fetching labels: {e}")
        return {}

def create_or_update_label(repo: str, name: str, color: str, description: str, existing: Dict) -> str:
    """Create or update a single label"""
    if name in existing:
        existing_color, existing_desc = existing[name]
        if existing_color.lower() == color.lower() and existing_desc == description:
            return "exists"

        # Update if different
        result = subprocess.run(
            ["gh", "label", "create", name, "--repo", repo, "--color", color,
             "--description", description, "--force"],
            capture_output=True,
            text=True
        )
        return "updated" if result.returncode == 0 else "failed"
    else:
        # Create new
        result = subprocess.run(
            ["gh", "label", "create", name, "--repo", repo, "--color", color,
             "--description", description],
            capture_output=True,
            text=True
        )
        return "created" if result.returncode == 0 else "failed"

def setup_labels():
    """Main setup function"""
    repo = get_repo()
    print(f"🎯 Setting up labels for repository: {repo}")
    print(f"📋 Total labels to configure: {len(LABELS)}")
    print()

    # Get existing labels
    print("Fetching existing labels...")
    existing = get_existing_labels(repo)
    print(f"Found {len(existing)} existing labels\n")

    # Statistics
    stats = {"created": 0, "updated": 0, "exists": 0, "failed": 0}

    # Process each label
    for name, (color, description) in LABELS.items():
        status = create_or_update_label(repo, name, color, description, existing)
        stats[status] += 1

        # Status icons
        icons = {"created": "✅", "updated": "🔄", "exists": "☑️", "failed": "❌"}
        icon = icons.get(status, "?")

        print(f"{icon} {name}: {status}")

    # Summary
    print(f"\n📊 Summary:")
    print(f"  Created: {stats['created']}")
    print(f"  Updated: {stats['updated']}")
    print(f"  Already correct: {stats['exists']}")
    print(f"  Failed: {stats['failed']}")

    if stats['failed'] > 0:
        print("\n⚠️  Some labels failed to create. Check permissions.")
        return 1

    print("\n✅ Label setup complete!")
    return 0

def cleanup_old_labels():
    """Remove default labels we don't need"""
    repo = get_repo()
    old_labels = ["bug", "documentation", "duplicate", "enhancement", "invalid", "question", "wontfix"]

    print(f"\n🧹 Cleaning up old default labels...")
    for label in old_labels:
        if label not in ["good first issue", "help wanted"]:  # Keep these
            result = subprocess.run(
                ["gh", "label", "delete", label, "--repo", repo, "--yes"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"  ❌ Removed: {label}")
            else:
                print(f"  ⏭️  Skipped: {label}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cleanup":
        cleanup_old_labels()

    sys.exit(setup_labels())