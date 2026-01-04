"""
Pytest fixtures and configuration for Workflow tests.
"""

import json
import pytest
from pathlib import Path


@pytest.fixture
def fixtures_dir() -> Path:
    """Path to test fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_transcript(fixtures_dir: Path) -> str:
    """Sample meeting transcript content."""
    return (fixtures_dir / "sample-meeting-transcript.md").read_text()


@pytest.fixture
def sample_readme(fixtures_dir: Path) -> str:
    """Sample README.md content."""
    return (fixtures_dir / "sample-readme.md").read_text()


@pytest.fixture
def sample_extraction(fixtures_dir: Path) -> dict:
    """Sample extraction JSON."""
    return json.loads((fixtures_dir / "sample-extraction.json").read_text())


@pytest.fixture
def sample_changeplan(fixtures_dir: Path) -> dict:
    """Sample changeplan JSON."""
    return json.loads((fixtures_dir / "sample-changeplan.json").read_text())


@pytest.fixture
def temp_vault(tmp_path: Path) -> Path:
    """Create a temporary vault structure for testing."""
    # Create directory structure
    (tmp_path / "Inbox" / "_extraction").mkdir(parents=True)
    (tmp_path / "Inbox" / "_archive").mkdir(parents=True)
    (tmp_path / "Inbox" / "Transcripts").mkdir(parents=True)
    (tmp_path / "VAST" / "People" / "Jeff Denworth").mkdir(parents=True)
    (tmp_path / "VAST" / "Customers and Partners" / "Google").mkdir(parents=True)
    
    return tmp_path
