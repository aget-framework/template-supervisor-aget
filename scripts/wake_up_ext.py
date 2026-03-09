#!/usr/bin/env python3
"""
Wake Up Extension — Instance_Artifact for supervisor agents.

Domain-specific wake-up augmentations. Called by canonical wake_up.py
via the C1 extension hook (WU-008 per SKILL-001 v1.1.0).

This file is an Instance_Artifact: owned by the agent operator,
NOT overwritten on framework upgrade.

Contract:
    post_wake(data: dict) -> dict
    - Receives wake data from canonical script
    - Returns augmented data dict (additive-only per L464)
    - Must not remove or override framework keys

Domain extensions:
    - Fleet version delta: compare supervisor vs fleet version (L465)
    - Active projects: scan planning/ for in-progress work
    - Release discovery: check for newer framework versions (CAP-REL-027, L656)

See: SKILL-001 WU-008, CAP-REL-027, L656
"""

import json
import re
import subprocess
from pathlib import Path


def _get_version_delta(agent_path: Path, supervisor_version: str) -> dict:
    """Compare supervisor version to fleet version (L465).

    Reads FLEET_STATE.yaml for fleet_version. Returns delta info
    for display in wake-up output.
    """
    fleet_file = agent_path / '.aget' / 'fleet' / 'FLEET_STATE.yaml'
    result = {
        'supervisor_version': supervisor_version,
        'fleet_version': 'unknown',
        'has_delta': False,
        'explanation': '',
    }
    if not fleet_file.exists():
        return result
    try:
        content = fleet_file.read_text()
        for line in content.split('\n'):
            if line.strip().startswith('fleet_version:'):
                match = re.search(r'(\d+\.\d+\.\d+)', line)
                if match:
                    result['fleet_version'] = match.group(1)
                    break
    except (IOError, UnicodeDecodeError):
        pass
    if result['fleet_version'] != 'unknown':
        sv = supervisor_version.lstrip('v')
        fv = result['fleet_version']
        if sv != fv:
            result['has_delta'] = True
            result['explanation'] = f"Fleet at v{fv} — upgrade in progress"
    return result


def _get_active_projects(agent_path: Path) -> list:
    """Scan planning/ for active PROJECT_PLANs.

    Returns list of dicts with name and current_phase.
    Active = status is not Complete or COMPLETE.
    """
    planning_dir = agent_path / 'planning'
    if not planning_dir.is_dir():
        return []
    projects = []
    for f in sorted(planning_dir.glob('PROJECT_PLAN_*.md')):
        try:
            content = f.read_text(errors='replace')
            # Check if complete
            if '**Status**: COMPLETE' in content or '**Status**: Complete' in content:
                continue
            # Extract status
            status = 'unknown'
            for line in content.split('\n')[:20]:
                if line.startswith('**Status**:'):
                    status = line.split(':', 1)[1].strip()
                    break
            projects.append({
                'name': f.stem.replace('PROJECT_PLAN_', ''),
                'current_phase': status,
            })
        except (IOError, UnicodeDecodeError):
            continue
    return projects


def _check_latest_release(upstream_repo: str, current_version: str) -> dict:
    """Check if a newer AGET framework version is available on GitHub.

    Uses gh CLI (ADR-004 tier_rich). Non-blocking per C-WU-002:
    10s timeout, silent on failure.

    Returns dict with: available (bool), latest (str), message (str).
    """
    try:
        result = subprocess.run(
            ["gh", "release", "view", "--repo", upstream_repo,
             "--json", "tagName", "-q", ".tagName"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            return {"available": False, "latest": None, "message": ""}

        latest = result.stdout.strip().lstrip("v")
        if latest != current_version:
            return {
                "available": True,
                "latest": latest,
                "message": (
                    f"Framework v{latest} available (you are at v{current_version}). "
                    f"Review DEPLOYMENT_SPEC before upgrading."
                ),
            }
        return {"available": False, "latest": latest, "message": ""}
    except (FileNotFoundError, subprocess.TimeoutExpired, Exception):
        return {"available": False, "latest": None, "message": ""}


def post_wake(data: dict) -> dict:
    """C1 Extension Hook: Augment wake data with supervisor-specific content.

    Called by canonical wake_up.py after gathering framework data.
    Adds fleet version delta, active projects, and release discovery.
    """
    agent_path = Path(data.get('agent_path', '.'))
    lines = []

    # Fleet version delta (L465)
    supervisor_version = data.get('aget_version', '0.0.0')
    delta = _get_version_delta(agent_path, supervisor_version)
    if delta.get('has_delta'):
        lines.append(f"Fleet: {delta['explanation']}")
        data['version_delta'] = delta

    # Active projects
    projects = _get_active_projects(agent_path)
    if projects:
        names = [f"{p['name']} ({p['current_phase']})" for p in projects]
        lines.append(f"Active: {', '.join(names)}")
        data['active_projects'] = projects

    # Release discovery (CAP-REL-027, L656)
    config_path = agent_path / '.aget' / 'config.json'
    if config_path.exists():
        try:
            with open(config_path) as f:
                config = json.load(f)
            rd_config = config.get('release_discovery', {})
            if rd_config.get('enabled', False):
                version_path = agent_path / '.aget' / 'version.json'
                current_version = "0.0.0"
                if version_path.exists():
                    with open(version_path) as f:
                        current_version = json.load(f).get('aget_version', '0.0.0')

                upstream_repo = rd_config.get('upstream_repo', 'aget-framework/aget')
                release_info = _check_latest_release(upstream_repo, current_version)

                if release_info.get('available'):
                    lines.append(f"Release: {release_info['message']}")
                    data['release_discovery'] = release_info
        except Exception:
            pass  # Non-blocking per C-WU-002

    if lines:
        existing = data.get('extension_output', '')
        if existing:
            lines.insert(0, existing)
        data['extension_output'] = "\n".join(lines)

    return data
