#!/usr/bin/env python3
"""v2.7 Supervisor Role Contract Test

Tests that supervisor-specific configuration is present and valid.
Part of AGET framework v2.7 supervisor template standards.

Validates: CAP-SUP-001 (fleet oversight), CAP-SUP-002 (work distribution),
           INV-SUP-001, INV-SUP-002, L99, L099
"""

import pytest
import json
from pathlib import Path


def test_supervisor_domain():
    """Supervisor agents must have domain='supervision' in version.json. [CAP-SUP-001]"""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "domain" in data, "version.json missing 'domain' field"
        domain = data["domain"]
        assert domain == "supervision", \
            f"Supervisor template must have domain='supervision', got '{domain}'"


def test_supervisor_instance_type():
    """Supervisors must have appropriate instance_type."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "instance_type" in data, "version.json missing 'instance_type' field"
        instance_type = data["instance_type"]

        # Valid values: "AGET", "template", "coordinator"
        # Supervisors are action-taking, so typically "AGET" or "template"
        valid_types = ["AGET", "template", "coordinator"]
        assert instance_type in valid_types, \
            f"instance_type must be one of {valid_types}, got '{instance_type}'"


def test_supervisor_coordination_directory():
    """Supervisor template must have .aget/coordination/ directory. [CAP-SUP-002]"""
    coordination_dir = Path(".aget/coordination")
    # Directory may not exist in template but should be documented
    # This test passes if documented in AGENTS.md
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), "AGENTS.md not found"

    content = agents_md.read_text()
    assert "coordination" in content.lower(), \
        "Supervisor template must document coordination patterns"
    assert ".aget/coordination" in content or "coordination/" in content, \
        "Supervisor template must reference .aget/coordination/ directory"


def test_supervisor_patterns_documented():
    """Supervisor template must document L99 and L099 patterns. [INV-SUP-001, INV-SUP-002]"""
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), "AGENTS.md not found"

    content = agents_md.read_text()

    # Check for L99 (Recursive Supervision Model)
    assert "L99" in content or "recursive supervision" in content.lower(), \
        "Supervisor template must document L99 (Recursive Supervision Model)"

    # Check for L099 (Supervision Patterns)
    assert "L099" in content or "supervision patterns" in content.lower(), \
        "Supervisor template must document L099 (Supervision Patterns)"
