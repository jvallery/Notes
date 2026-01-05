from datetime import datetime
from pathlib import Path

from pipeline.entities import EntityIndex
from pipeline.models import UnifiedExtraction, EntityRef, Fact, MentionedEntity
from pipeline.patch import PatchGenerator


def _setup_entities(vault_root: Path):
    paths = [
        vault_root / "VAST" / "People" / "Alice Example" / "README.md",
        vault_root / "VAST" / "People" / "Bob Example" / "README.md",
    ]
    for p in paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("# README\n\n## Key Facts\n\n")


def _extraction(source_file: Path) -> UnifiedExtraction:
    primary = EntityRef(entity_type="person", name="Alice Example", confidence=0.9)
    fact_primary = Fact(text="Alice fact", about_entity=primary, fact_type="background")
    mention = MentionedEntity(
        entity_type="person",
        name="Bob Example",
        role="mentioned",
        facts_about=["Bob fact"],
        confidence=0.8,
    )
    return UnifiedExtraction(
        source_file=str(source_file),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=primary,
        date="2026-01-05",
        title="Meeting",
        summary="Summary",
        participants=["Alice Example", "Bob Example"],
        facts=[fact_primary],
        decisions=[],
        topics=[],
        tasks=[],
        questions=[],
        commitments=[],
        mentioned_entities=[mention],
        confidence=0.9,
    )


def test_patch_generator_creates_patches_for_primary_and_mentions(tmp_path):
    _setup_entities(tmp_path)
    entity_index = EntityIndex(tmp_path)
    gen = PatchGenerator(tmp_path, entity_index)

    extraction = _extraction(tmp_path / "Inbox" / "Email" / "test.md")
    plan = gen.generate(extraction)

    targets = [p.target_path for p in plan.patches]
    # Primary entity README gets patched
    assert any("Alice Example/README.md" in t for t in targets)
    # Mentioned entity with facts_about gets patched
    assert any("Bob Example/README.md" in t for t in targets)
