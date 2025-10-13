#!/usr/bin/env python3
"""v2.6 Configuration Size Contract Test

Tests that AGENTS.md stays under 40,000 character limit (L146).
Part of AGET framework v2.6+ configuration size management standards.
"""

import pytest
from pathlib import Path


def test_agents_md_size_limit():
    """AGENTS.md must be under 40,000 characters (L146)."""
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), "AGENTS.md not found"

    size = len(agents_md.read_text())
    assert size < 40000, \
        f"AGENTS.md is {size} chars (limit: 40,000). Extract content to .aget/docs/"


def test_template_size_buffer():
    """Template should stay under 25k chars to provide buffer for users."""
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), "AGENTS.md not found"

    size = len(agents_md.read_text())
    # This is a warning, not hard failure
    if size >= 25000:
        pytest.skip(f"Template is {size} chars (target: <25k). Consider extracting content.")


def test_configuration_size_documented():
    """AGENTS.md must document configuration size management (L146)."""
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), "AGENTS.md not found"

    content = agents_md.read_text()
    assert "L146" in content or "Configuration Size Management" in content, \
        "AGENTS.md must document L146 (Configuration Size Management)"

    assert "40,000" in content or "40k" in content.lower(), \
        "AGENTS.md must specify 40k character limit"
