#!/usr/bin/env python3
"""Agent discovery and routing pattern for AGET v2.0."""

import os
import json
from pathlib import Path
from typing import Dict, List, Any

def discover_agents(base_path: str = None) -> List[Dict[str, Any]]:
    """Discover AGET agents in the system.

    Args:
        base_path: Starting path for discovery (defaults to parent directory)

    Returns:
        List of discovered agents with metadata
    """
    if base_path is None:
        base_path = Path.home() / "github"

    agents = []
    base = Path(base_path)

    # Look for AGET signatures
    for path in base.rglob(".aget"):
        agent_root = path.parent
        agent_info = {
            "name": agent_root.name,
            "path": str(agent_root),
            "version": "unknown"
        }

        # Check for version file
        version_file = path / "version.json"
        if version_file.exists():
            try:
                with open(version_file) as f:
                    version_data = json.load(f)
                    agent_info["version"] = version_data.get("aget_version", "unknown")
                    agent_info["tier"] = version_data.get("tier", "unknown")
            except:
                pass

        # Check for CLAUDE.md
        claude_file = agent_root / "CLAUDE.md"
        agent_info["has_claude_md"] = claude_file.exists()

        agents.append(agent_info)

    return agents

def route_to_hub(message: str, agent_context: Dict[str, Any]) -> Dict[str, Any]:
    """Route messages to AGET hub for coordination.

    Args:
        message: Message to route
        agent_context: Current agent context/metadata

    Returns:
        Routing result
    """
    hub_repo = "aget-framework/aget"
    return {
        "hub": hub_repo,
        "agent": agent_context.get("name", "unknown"),
        "message": message,
        "routing": "Use GitHub issues for cross-agent coordination"
    }

if __name__ == "__main__":
    # Example usage
    print("Agent discovery and routing pattern installed for AGET v2.0")
    agents = discover_agents()
    print(f"Found {len(agents)} agent(s)")