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
    - Release discovery: check for newer framework versions (CAP-REL-027, L656)

See: SKILL-001 WU-008, CAP-REL-027, L656
"""

import json
import subprocess
from pathlib import Path


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
    Adds release discovery check for upstream framework versions.
    """
    agent_path = Path(data.get('agent_path', '.'))
    lines = []

    # Release discovery (CAP-REL-027, L656)
    config_path = agent_path / '.aget' / 'config.json'
    if config_path.exists():
        try:
            with open(config_path) as f:
                config = json.load(f)
            rd_config = config.get('release_discovery', {})
            if rd_config.get('enabled', False):
                # Get current version
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
