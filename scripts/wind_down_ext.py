#!/usr/bin/env python3
"""
Wind Down Extension Hook — Instance-Specific

This file is an INSTANCE ARTIFACT (not overwritten on framework upgrade).
Add domain-specific wind-down actions here.

Classification: Instance_Artifact (C3+C1 pattern)
Owner: Agent operator (not aget-framework)
Called by: wind_down.py or CLI agent skill after canonical wind-down

Usage:
    python3 scripts/wind_down_ext.py                # Human-readable
    python3 scripts/wind_down_ext.py --json          # JSON output
    python3 scripts/wind_down_ext.py --dir /path     # Specific agent

Examples of domain-specific extensions:
    - Fleet state snapshot (supervisor)
    - Unresolved escalation summary
    - Pending broadcast delivery check
    - Cross-portfolio coordination notes

See: SKILL-002 R-WD-008 (Extension Hook), DEPLOYMENT_SPEC v1.1.0
"""

import argparse
import json
import sys
from pathlib import Path


def get_extension_data(agent_path: Path) -> dict:
    """
    Gather domain-specific data for wind-down summary.

    Customize this function for your agent's domain.
    Return a dict that will be merged into wind-down output.
    """
    # Placeholder — replace with domain-specific logic
    return {
        "extension": "wind_down_ext",
        "status": "placeholder",
        "message": "No domain extensions configured. Edit scripts/wind_down_ext.py to add.",
    }


def main():
    parser = argparse.ArgumentParser(description="Wind-down extension hook")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--dir", type=Path, help="Agent directory")
    args = parser.parse_args()

    agent_path = Path(args.dir) if args.dir else Path.cwd()
    data = get_extension_data(agent_path)

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        msg = data.get("message", "")
        if msg:
            print(f"  Extension: {msg}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
