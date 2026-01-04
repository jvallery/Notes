"""
Tests for planner context assembly and prompt rendering.

Focus: T7 Planner Context Quality (entity paths + aliases).
"""

from datetime import datetime
from pathlib import Path

import pytest

from models.extraction import ExtractionV1


def test_list_entity_paths_preserves_duplicates(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    """list_entity_paths should not overwrite names that exist in multiple domains."""
    # Create duplicate entity name in both VAST and Personal
    (tmp_path / "VAST" / "People" / "Alex Smith").mkdir(parents=True)
    (tmp_path / "Personal" / "People" / "Alex Smith").mkdir(parents=True)

    from scripts.utils import entities as entities_mod

    monkeypatch.setattr(entities_mod, "vault_root", lambda: tmp_path)

    entity_paths = entities_mod.list_entity_paths()

    assert entity_paths["Alex Smith"] == [
        "VAST/People/Alex Smith",
        "Personal/People/Alex Smith",
    ]


def test_build_planner_prompt_includes_paths_and_mentions():
    """Planner prompt should include entity_paths and mentioned_entities sections."""
    from scripts.plan import build_planner_prompt

    extraction = ExtractionV1(
        version="1.0",
        source_file="Inbox/Transcripts/sample.md",
        processed_at=datetime.now(),
        note_type="people",
        entity_name="Alex Smith",
        title="Weekly 1-1",
        date="2026-01-01",
        participants=["Alex Smith", "Myself"],
        summary="Discussed priorities.",
        tasks=[],
        decisions=[],
        facts=[],
        topics=[],
    )

    vault_context = {
        "all_entity_names": {"people": ["Alex Smith"], "accounts": [], "projects": [], "rob": []},
        "entity_paths": {"Alex Smith": ["VAST/People/Alex Smith", "Personal/People/Alex Smith"]},
        "mentioned_entities": {"Alex Smith": {"path": "VAST/People/Alex Smith", "confidence": 1.0, "type": "people"}},
    }

    prompt = build_planner_prompt(vault_context, extraction)

    assert "## Entity Paths (Name → Folder(s))" in prompt
    assert "VAST/People/Alex Smith" in prompt
    assert "Personal/People/Alex Smith" in prompt
    assert "## Mentioned Entities (High-Confidence Matches)" in prompt
