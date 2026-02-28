#!/usr/bin/env python3
"""v2.7 Portfolio Field Contract Test

Tests that portfolio field exists in version.json for fleet organization.
Part of AGET framework v2.7 portfolio governance standards.

Validates: CAP-TPL-002 (version.json fields), CAP-SUP-001 (fleet oversight)
"""

import pytest
import json
from pathlib import Path


def test_portfolio_field_exists():
    """version.json must have portfolio field (may be null for templates/coordinators). [CAP-TPL-002]"""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "portfolio" in data, "version.json missing 'portfolio' field (required in v2.7+)"


def test_portfolio_field_valid_value():
    """portfolio field must be null or valid portfolio name."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        portfolio = data.get("portfolio")

        # Valid values: null, "main", "example", "legalon", or other string
        # (null is valid for templates and coordinators)
        assert portfolio is None or isinstance(portfolio, str), \
            f"portfolio must be null or string, got {type(portfolio)}"


def test_supervisor_portfolio_coordination():
    """Supervisors typically have portfolio=null (cross-portfolio coordination)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Check if this is a supervisor (domain="supervision" or instance_type includes "super")
        domain = data.get("domain", "")
        instance_type = data.get("instance_type", "")

        is_supervisor = (
            domain == "supervision" or
            "supervisor" in instance_type.lower() or
            "coordinator" in instance_type.lower()
        )

        if is_supervisor:
            portfolio = data.get("portfolio")
            # Supervisors typically have null portfolio (coordinate across portfolios)
            # This is informational, not a hard requirement
            if portfolio is not None:
                # If supervisor has a portfolio, it's managing single-portfolio fleet
                assert isinstance(portfolio, str), "Supervisor portfolio must be string if not null"
