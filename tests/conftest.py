"""
Shared pytest fixtures and configuration
"""
import pytest
import tempfile
import shutil
from pathlib import Path

@pytest.fixture
def temp_project_dir():
    """Create a temporary directory for testing."""
    temp_dir = tempfile.mkdtemp(prefix="aget_test_")
    yield Path(temp_dir)
    shutil.rmtree(temp_dir, ignore_errors=True)

@pytest.fixture
def mock_aget_dir(temp_project_dir):
    """Create a mock .aget directory structure."""
    aget_dir = temp_project_dir / ".aget"
    aget_dir.mkdir()
    (aget_dir / "evolution").mkdir()
    (aget_dir / "checkpoints").mkdir()
    (aget_dir / "version.json").write_text('{"version": "2.0.0", "framework": "aget"}')
    return aget_dir

@pytest.fixture
def sample_pattern_file(temp_project_dir):
    """Create a sample pattern file for testing."""
    patterns_dir = temp_project_dir / "patterns" / "test"
    patterns_dir.mkdir(parents=True)
    pattern_file = patterns_dir / "sample_pattern.py"
    pattern_file.write_text('''
"""Sample test pattern"""

def apply_pattern(project_root=None):
    """Apply the sample pattern."""
    return {"status": "success", "message": "Pattern applied"}

def validate_pattern(project_root=None):
    """Validate pattern requirements."""
    return True
''')
    return pattern_file