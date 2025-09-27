"""
Basic setup tests to verify test infrastructure
"""
import pytest
from pathlib import Path

class TestBasicSetup:
    """Verify basic test infrastructure is working."""

    @pytest.mark.unit
    def test_pytest_running(self):
        """Test that pytest is running."""
        assert True

    @pytest.mark.unit
    def test_imports_work(self):
        """Test that we can import standard libraries."""
        import sys
        import os
        assert sys.version_info >= (3, 8)
        assert os.path.exists(".")

    @pytest.mark.unit
    def test_project_structure_exists(self):
        """Test that basic project structure exists."""
        expected_dirs = ["docs", "src", "workspace", "products", "data", "tests", ".aget"]
        for dir_name in expected_dirs:
            assert Path(dir_name).exists(), f"Directory {dir_name} should exist"

    @pytest.mark.unit
    def test_aget_metadata_exists(self):
        """Test that .aget directory exists."""
        aget_dir = Path(".aget")
        assert aget_dir.exists(), ".aget directory should exist"
        assert aget_dir.is_dir(), ".aget should be a directory"

class TestFixtures:
    """Test that our fixtures work correctly."""

    @pytest.mark.unit
    def test_temp_project_dir_fixture(self, temp_project_dir):
        """Test temporary directory fixture."""
        assert temp_project_dir.exists()
        assert temp_project_dir.is_dir()
        test_file = temp_project_dir / "test.txt"
        test_file.write_text("test")
        assert test_file.exists()

    @pytest.mark.unit
    def test_mock_aget_dir_fixture(self, mock_aget_dir):
        """Test mock .aget directory fixture."""
        assert mock_aget_dir.exists()
        assert (mock_aget_dir / "evolution").exists()
        assert (mock_aget_dir / "checkpoints").exists()
        assert (mock_aget_dir / "version.json").exists()

    @pytest.mark.unit
    def test_sample_pattern_fixture(self, sample_pattern_file):
        """Test sample pattern fixture."""
        assert sample_pattern_file.exists()
        content = sample_pattern_file.read_text()
        assert "apply_pattern" in content
        assert "validate_pattern" in content