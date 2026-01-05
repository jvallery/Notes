from datetime import datetime
from pathlib import Path

import yaml

from pipeline.entities import EntityIndex
from pipeline.models import UnifiedExtraction, EntityRef, Fact, MentionedEntity
from pipeline.patch import PatchGenerator, ChangePlan, PatchOperation


def _setup_entities(vault_root: Path):
    paths = [
        vault_root / "VAST" / "People" / "Alice Example" / "README.md",
        vault_root / "VAST" / "People" / "Bob Example" / "README.md",
    ]
    for p in paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("# README\n\n## Key Facts\n\n")


def _setup_aliases(vault_root: Path):
    """Set up an aliases.yaml file."""
    aliases_dir = vault_root / "Workflow" / "entities"
    aliases_dir.mkdir(parents=True, exist_ok=True)
    aliases = {
        "Alice Example": ["Alice", "A. Example"],
        "Bob Example": ["Robert Example", "Bob"],
    }
    (aliases_dir / "aliases.yaml").write_text(yaml.dump(aliases))


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


def test_changeplan_validation_passes_for_valid_plan():
    """Test that a well-formed ChangePlan validates successfully."""
    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        meeting_note_path="VAST/People/Alice Example/2026-01-05 - Meeting.md",
        meeting_note={"type": "people", "title": "Meeting"},
        patches=[
            PatchOperation(
                operation="patch",
                target_path="VAST/People/Alice Example/README.md",
                target_entity="Alice Example",
                add_facts=["Alice cares about Azure"],
            )
        ],
    )
    
    issues = plan.validate_plan()
    assert len(issues) == 0
    assert plan.is_valid()


def test_changeplan_validation_catches_missing_source():
    """Test that validation catches missing source_file."""
    plan = ChangePlan(source_file="")
    
    issues = plan.validate_plan()
    assert any("source_file" in issue for issue in issues)
    assert not plan.is_valid()


def test_changeplan_validation_catches_duplicate_patches():
    """Test that validation catches duplicate patch targets."""
    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        patches=[
            PatchOperation(
                operation="patch",
                target_path="VAST/People/Alice Example/README.md",
                target_entity="Alice Example",
                add_facts=["Fact 1"],
            ),
            PatchOperation(
                operation="patch",
                target_path="VAST/People/Alice Example/README.md",
                target_entity="Alice Example",
                add_facts=["Fact 2"],
            ),
        ],
    )
    
    issues = plan.validate_plan()
    assert any("Duplicate" in issue for issue in issues)


def test_changeplan_validation_catches_empty_patch():
    """Test that validation catches patch operations with no changes."""
    plan = ChangePlan(
        source_file="Inbox/Email/test.md",
        patches=[
            PatchOperation(
                operation="patch",
                target_path="VAST/People/Alice Example/README.md",
                target_entity="Alice Example",
                # No facts, topics, decisions, etc.
            ),
        ],
    )
    
    issues = plan.validate_plan()
    assert any("no changes" in issue for issue in issues)


def test_patch_generator_resolves_aliases(tmp_path):
    """Test that PatchGenerator uses alias resolution."""
    _setup_entities(tmp_path)
    _setup_aliases(tmp_path)
    
    # Create extraction with alias "Alice" instead of "Alice Example"
    primary = EntityRef(entity_type="person", name="Alice", confidence=0.9)
    extraction = UnifiedExtraction(
        source_file=str(tmp_path / "Inbox" / "Email" / "test.md"),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=primary,
        date="2026-01-05",
        title="Meeting",
        summary="Summary",
        participants=["Alice"],
        facts=[],
        decisions=[],
        topics=[],
        tasks=[],
        questions=[],
        commitments=[],
        mentioned_entities=[],
        confidence=0.9,
    )
    
    entity_index = EntityIndex(tmp_path)
    gen = PatchGenerator(tmp_path, entity_index)
    plan = gen.generate(extraction)
    
    # Should have a warning about alias resolution
    assert any("alias" in w.lower() for w in plan.warnings)


def test_patch_generator_detects_duplicate_entities(tmp_path):
    """Test that PatchGenerator warns about potential duplicate entities."""
    _setup_entities(tmp_path)
    _setup_aliases(tmp_path)
    
    # Extraction with both "Alice Example" and "Alice" (same person via alias)
    primary = EntityRef(entity_type="person", name="Alice Example", confidence=0.9)
    mention = MentionedEntity(
        entity_type="person",
        name="Alice",  # Alias for Alice Example
        role="mentioned",
        facts_about=["Duplicate fact"],
        confidence=0.8,
    )
    extraction = UnifiedExtraction(
        source_file=str(tmp_path / "Inbox" / "Email" / "test.md"),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=primary,
        date="2026-01-05",
        title="Meeting",
        summary="Summary",
        participants=["Alice Example"],
        facts=[],
        decisions=[],
        topics=[],
        tasks=[],
        questions=[],
        commitments=[],
        mentioned_entities=[mention],
        confidence=0.9,
    )
    
    entity_index = EntityIndex(tmp_path)
    gen = PatchGenerator(tmp_path, entity_index)
    plan = gen.generate(extraction)
    
    # Should have a warning about potential duplicate
    assert any("duplicate" in w.lower() for w in plan.warnings)
