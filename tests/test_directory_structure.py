#!/usr/bin/env python3
"""v2.5+ Directory Structure Contract Test

Tests that required directories exist for supervisor template.
Part of AGET framework v2.5+ standards.

Validates: CAP-TPL-001 (.aget/ structure), CAP-TPL-002 (version.json),
           CAP-TPL-004 (AGENTS.md)
"""

import pytest
from pathlib import Path


def test_core_directories_exist():
    """Core AGET directories must exist. [CAP-TPL-001]"""
    required_dirs = [
        ".aget",
        "docs",
        "src",
        "workspace",
        "products",
        "data",
        "tests"
    ]

    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        assert dir_path.exists(), f"Required directory missing: {dir_name}"
        assert dir_path.is_dir(), f"{dir_name} should be a directory"


def test_aget_subdirectories_exist():
    """Required .aget subdirectories must exist. [CAP-TPL-001]"""
    required_subdirs = [
        ".aget/evolution",
        ".aget/checkpoints",
        ".aget/docs",
        ".aget/specs"
    ]

    for subdir in required_subdirs:
        subdir_path = Path(subdir)
        assert subdir_path.exists(), f"Required .aget subdirectory missing: {subdir}"
        assert subdir_path.is_dir(), f"{subdir} should be a directory"


def test_version_json_exists():
    """version.json must exist in .aget/. [CAP-TPL-002]"""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found in .aget/"
    assert version_file.is_file(), "version.json should be a file"


def test_agents_md_exists():
    """AGENTS.md must exist at root. [CAP-TPL-004]"""
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), "AGENTS.md not found"
    assert agents_md.is_file(), "AGENTS.md should be a file"


def test_claude_md_symlink():
    """CLAUDE.md must be symlink to AGENTS.md. [CAP-TPL-004]"""
    claude_md = Path("CLAUDE.md")
    assert claude_md.exists(), "CLAUDE.md not found"
    assert claude_md.is_symlink(), "CLAUDE.md must be a symlink to AGENTS.md"

    target = claude_md.resolve()
    agents_md = Path("AGENTS.md").resolve()
    assert target == agents_md, f"CLAUDE.md must link to AGENTS.md (links to {target})"
