#!/usr/bin/env python3
"""
Agent Discovery System
Scans workspace for AGET projects and builds registry
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class AgentDiscovery:
    """Discover and catalog AGET agents in workspace"""

    def __init__(self, workspace_path: str = None):
        """Initialize discovery with workspace path"""
        if workspace_path is None:
            # Default to parent directory
            workspace_path = Path(__file__).parent.parent.parent.parent.parent

        self.workspace = Path(workspace_path)
        self.agents = {}
        self.scan_results = []

    def scan(self, verbose: bool = False) -> Dict:
        """
        Scan workspace for AGET projects

        Returns:
            Dictionary of discovered agents
        """
        if verbose:
            print(f"Scanning workspace: {self.workspace}")

        # Look for directories with .aget folder
        for item in self.workspace.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                aget_dir = item / '.aget'
                if aget_dir.exists():
                    agent_info = self._analyze_agent(item)
                    if agent_info:
                        self.agents[item.name] = agent_info
                        if verbose:
                            print(f"  ✓ Found: {item.name}")

        # Save scan results
        self._save_registry()

        return self.agents

    def _analyze_agent(self, project_path: Path) -> Optional[Dict]:
        """Analyze an AGET project to extract metadata"""
        info = {
            "path": str(project_path),
            "name": project_path.name,
            "discovered": datetime.now().isoformat(),
            "type": "aget-project",
            "capabilities": [],
            "version": None,
            "status": "unknown"
        }

        # Check for CLAUDE.md
        claude_file = project_path / "CLAUDE.md"
        if claude_file.exists():
            info["has_claude_md"] = True
            # Extract capabilities from CLAUDE.md
            try:
                content = claude_file.read_text()
                if "session" in content.lower():
                    info["capabilities"].append("session-management")
                if "git" in content.lower():
                    info["capabilities"].append("git")
                if "python" in content.lower():
                    info["capabilities"].append("python")
                if "template" in content.lower():
                    info["capabilities"].append("template")
            except:
                pass

        # Check for agents.md (version info)
        agents_file = project_path / ".aget" / "agents.md"
        if agents_file.exists():
            try:
                content = agents_file.read_text()
                # Extract version from first line like "aget-aget v2.0.0-beta"
                lines = content.strip().split('\n')
                if lines:
                    parts = lines[0].split()
                    for part in parts:
                        if part.startswith('v'):
                            info["version"] = part
                            break
            except:
                pass

        # Check for specific patterns
        patterns_dir = project_path / ".aget" / "patterns"
        if patterns_dir.exists():
            info["has_patterns"] = True
            pattern_dirs = [d.name for d in patterns_dir.iterdir() if d.is_dir()]
            info["pattern_types"] = pattern_dirs

            # Add capabilities based on patterns
            if "github" in pattern_dirs:
                info["capabilities"].append("github-integration")
            if "documentation" in pattern_dirs:
                info["capabilities"].append("documentation")
            if "routing" in pattern_dirs:
                info["capabilities"].append("routing-hub")

        # Check repository (if git)
        try:
            result = subprocess.run(
                ["git", "config", "--get", "remote.origin.url"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=2
            )
            if result.returncode == 0:
                repo_url = result.stdout.strip()
                # Extract repo name
                if "github.com" in repo_url:
                    parts = repo_url.split("/")
                    if len(parts) >= 2:
                        owner = parts[-2].split(":")[-1]
                        repo = parts[-1].replace(".git", "")
                        info["repository"] = f"{owner}/{repo}"
        except:
            pass

        # Determine status
        if info.get("repository"):
            info["status"] = "active"
        elif info["capabilities"]:
            info["status"] = "local"
        else:
            info["status"] = "inactive"

        return info

    def _save_registry(self):
        """Save agent registry to file"""
        registry_file = Path(__file__).parent / "agent_registry.json"

        registry = {
            "version": "1.0.0",
            "last_scan": datetime.now().isoformat(),
            "workspace": str(self.workspace),
            "agents": self.agents,
            "statistics": {
                "total": len(self.agents),
                "active": len([a for a in self.agents.values() if a["status"] == "active"]),
                "with_patterns": len([a for a in self.agents.values() if a.get("has_patterns")]),
                "hub_capable": len([a for a in self.agents.values() if "routing-hub" in a["capabilities"]])
            }
        }

        with open(registry_file, "w") as f:
            json.dump(registry, f, indent=2)

        return registry_file

    def get_capabilities_map(self) -> Dict:
        """Build map of capabilities to agents"""
        cap_map = {}

        for agent_name, agent_info in self.agents.items():
            for capability in agent_info.get("capabilities", []):
                if capability not in cap_map:
                    cap_map[capability] = []
                cap_map[capability].append(agent_name)

        return cap_map

    def find_agents_with_capability(self, capability: str) -> List[str]:
        """Find all agents with specific capability"""
        matches = []

        for agent_name, agent_info in self.agents.items():
            if capability in agent_info.get("capabilities", []):
                matches.append(agent_name)

        return matches


def main():
    """CLI interface for agent discovery"""
    import argparse

    parser = argparse.ArgumentParser(description="Agent Discovery System")
    parser.add_argument("--scan", action="store_true", help="Scan for agents")
    parser.add_argument("--list", action="store_true", help="List discovered agents")
    parser.add_argument("--capabilities", action="store_true", help="Show capability map")
    parser.add_argument("--find", help="Find agents with capability")
    parser.add_argument("--workspace", help="Workspace path to scan")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    discovery = AgentDiscovery(args.workspace)

    if args.scan:
        print("=== Agent Discovery Scan ===\n")
        agents = discovery.scan(verbose=args.verbose)
        print(f"\nDiscovered {len(agents)} agents")

        # Show summary
        for name, info in agents.items():
            status = "🟢" if info["status"] == "active" else "🟡" if info["status"] == "local" else "⚫"
            caps = len(info.get("capabilities", []))
            print(f"{status} {name:30} {caps} capabilities")

    elif args.list:
        # Load from registry
        registry_file = Path(__file__).parent / "agent_registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                registry = json.load(f)

            print("=== Agent Registry ===\n")
            print(f"Last scan: {registry['last_scan']}")
            print(f"Total agents: {registry['statistics']['total']}\n")

            for name, info in registry["agents"].items():
                print(f"Agent: {name}")
                print(f"  Path: {info['path']}")
                print(f"  Status: {info['status']}")
                print(f"  Capabilities: {', '.join(info.get('capabilities', []))}")
                if info.get("repository"):
                    print(f"  Repository: {info['repository']}")
                print()
        else:
            print("No registry found. Run --scan first.")

    elif args.capabilities:
        discovery.scan()
        cap_map = discovery.get_capabilities_map()

        print("=== Capability Map ===\n")
        for capability, agents in sorted(cap_map.items()):
            print(f"{capability}:")
            for agent in agents:
                print(f"  - {agent}")
            print()

    elif args.find:
        discovery.scan()
        matches = discovery.find_agents_with_capability(args.find)

        if matches:
            print(f"Agents with capability '{args.find}':")
            for agent in matches:
                print(f"  - {agent}")
        else:
            print(f"No agents found with capability '{args.find}'")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()