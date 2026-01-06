from datetime import datetime
from pathlib import Path

from pipeline.pipeline import UnifiedPipeline
from pipeline.envelope import ContentType
from pipeline.models import (
    UnifiedExtraction,
    EntityRef,
    Fact,
    TaskItem,
    MentionedEntity,
    SuggestedOutputs,
)


def _write_templates(vault_root: Path):
    templates_dir = vault_root / "Workflow" / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    (templates_dir / "people.md.j2").write_text(
        """{{ title }}

{{ date }}

## Summary
{{ summary }}

## Tasks
{% for t in tasks %}- [ ] {{ t.text }}
{% endfor %}"""
    )


def _write_readme(vault_root: Path, name: str):
    path = vault_root / "VAST" / "People" / name / "README.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"# {name}\n\n## Key Facts\n\n## Topics\n\n## Key Decisions\n\n## Recent Context\n\n"
    )
    return path


def _fake_extraction(source_path: Path) -> UnifiedExtraction:
    primary = EntityRef(entity_type="person", name="Jeff Denworth", confidence=0.9)
    fact_primary = Fact(text="Jeff needs Azure marketplace SKU update", about_entity=primary, fact_type="task")
    mention = MentionedEntity(
        entity_type="person",
        name="Jason Vallery",
        role="discussed",
        facts_about=["Jason coordinating GDC RFP deck"],
        confidence=0.8,
    )
    task = TaskItem(
        text="Send updated GDC RFP deck to Microsoft",
        owner="Myself",
        due="2026-01-06",
        priority="high",
        related_person="Jeff Denworth",
    )
    return UnifiedExtraction(
        source_file=str(source_path),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=primary,
        date="2026-01-04",
        title="Weekly Status: Azure Marketplace",
        summary="Azure SKU update and GDC RFP deck follow-up",
        participants=["Jeff Denworth", "Jason Vallery"],
        facts=[fact_primary],
        decisions=["Proceed with SKU change by Friday"],
        topics=["Azure marketplace", "GDC RFP"],
        tasks=[task],
        questions=[],
        commitments=[],
        mentioned_entities=[mention],
        suggested_outputs=SuggestedOutputs(needs_reply=False),
        confidence=0.9,
    )


def _fake_extraction_for_env(env) -> UnifiedExtraction:
    """Generate deterministic extraction per content type."""
    if env.content_type == ContentType.TRANSCRIPT:
        primary_name = "Jai Menon"
        title = f"Transcript - {env.source_path.stem}"
        fact_text = "Jai shared latency targets for GPU interconnect"
        task_text = "Follow up with Jai on latency targets"
    else:
        primary_name = "Jeff Denworth"
        title = f"Email - {env.source_path.stem}"
        fact_text = "Jeff needs Azure marketplace SKU update"
        task_text = "Send Azure marketplace SKU update"
    
    primary = EntityRef(entity_type="person", name=primary_name, confidence=0.9)
    fact = Fact(text=fact_text, about_entity=primary, fact_type="relationship")
    mention = MentionedEntity(
        entity_type="person",
        name="Jason Vallery",
        facts_about=["Coordinating follow-up with stakeholders"],
        confidence=0.8,
    )
    task = TaskItem(
        text=task_text,
        owner="Myself",
        due="2026-01-06",
        priority="high",
        related_person=primary_name,
    )
    
    return UnifiedExtraction(
        source_file=str(env.source_path),
        content_type=env.content_type.value,
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=primary,
        date=env.date,
        title=title,
        summary=fact_text,
        participants=env.participants or [primary_name],
        facts=[fact],
        tasks=[task],
        questions=[],
        commitments=[],
        mentioned_entities=[mention],
        suggested_outputs=SuggestedOutputs(needs_reply=False),
        confidence=0.9,
    )


def test_pipeline_processes_email_fixture_end_to_end(monkeypatch, tmp_path):
    # Arrange fixtures
    _write_templates(tmp_path)
    _write_readme(tmp_path, "Jeff Denworth")
    _write_readme(tmp_path, "Jason Vallery")

    email_fixture = Path(__file__).parent / "fixtures" / "email_basic.md"
    inbox_path = tmp_path / "Inbox" / "Email" / email_fixture.name
    inbox_path.parent.mkdir(parents=True, exist_ok=True)
    inbox_path.write_text(email_fixture.read_text())

    pipeline = UnifiedPipeline(tmp_path, dry_run=False, verbose=False, generate_outputs=False, force=True, log_metrics=False)

    # Stub extractor to bypass network/LLM
    monkeypatch.setattr(
        pipeline.extractor,
        "extract",
        lambda env, ctx: _fake_extraction(env.source_path),
    )

    result = pipeline.process_file(inbox_path)

    # Assertions: apply succeeded
    assert result.success is True
    assert result.plan is not None
    assert result.apply_result is not None

    # Meeting note created
    note_path = tmp_path / result.plan.meeting_note_path
    assert note_path.exists()
    content = note_path.read_text()
    assert "Weekly Status" in content
    assert "Send updated GDC RFP deck" in content

    # README patched with facts/topics/decisions/context
    readme = tmp_path / "VAST" / "People" / "Jeff Denworth" / "README.md"
    readme_text = readme.read_text()
    assert "Jeff needs Azure marketplace SKU update" in readme_text
    assert "Azure marketplace" in readme_text
    assert "Proceed with SKU change by Friday" in readme_text

    # Mentioned entity with facts gets patched
    jv_readme = tmp_path / "VAST" / "People" / "Jason Vallery" / "README.md"
    assert "Jason coordinating GDC RFP deck" in jv_readme.read_text()

    # Source archived
    archive_dir = tmp_path / "Sources" / "Email"
    assert any(archive_dir.rglob(email_fixture.name))


def test_pipeline_processes_all_inbox_types(monkeypatch, tmp_path):
    _write_templates(tmp_path)
    for name in ["Jeff Denworth", "Jason Vallery", "Jai Menon"]:
        _write_readme(tmp_path, name)

    email_fixture = Path(__file__).parent / "fixtures" / "email_basic.md"
    transcript_fixture = Path(__file__).parent / "fixtures" / "transcript_basic.md"

    inbox_email = tmp_path / "Inbox" / "Email" / email_fixture.name
    inbox_email.parent.mkdir(parents=True, exist_ok=True)
    inbox_email.write_text(email_fixture.read_text())

    inbox_transcript = tmp_path / "Inbox" / "Transcripts" / transcript_fixture.name
    inbox_transcript.parent.mkdir(parents=True, exist_ok=True)
    inbox_transcript.write_text(transcript_fixture.read_text())

    pipeline = UnifiedPipeline(tmp_path, dry_run=False, verbose=False, generate_outputs=False, force=True, log_metrics=False)
    monkeypatch.setattr(
        pipeline.extractor,
        "extract",
        lambda env, ctx: _fake_extraction_for_env(env),
    )

    batch = pipeline.process_all()

    assert batch.total == 2
    assert batch.success == 2

    # Both sources archived into Sources/{type}
    archive_email = tmp_path / "Sources" / "Email"
    archive_transcripts = tmp_path / "Sources" / "Transcripts"
    assert any(archive_email.rglob(email_fixture.name))
    assert any(archive_transcripts.rglob(transcript_fixture.name))

    # People READMEs patched
    jeff_readme = tmp_path / "VAST" / "People" / "Jeff Denworth" / "README.md"
    jai_readme = tmp_path / "VAST" / "People" / "Jai Menon" / "README.md"
    assert "Azure marketplace SKU update" in jeff_readme.read_text()
    assert "latency targets for GPU interconnect" in jai_readme.read_text()


def test_pipeline_parallel_mode_generates_outbox_drafts(monkeypatch, tmp_path):
    _write_templates(tmp_path)
    for name in ["Jeff Denworth", "Jason Vallery", "Jai Menon"]:
        _write_readme(tmp_path, name)

    email_fixture = Path(__file__).parent / "fixtures" / "email_basic.md"
    transcript_fixture = Path(__file__).parent / "fixtures" / "transcript_basic.md"
    inbox_email = tmp_path / "Inbox" / "Email" / email_fixture.name
    inbox_email.parent.mkdir(parents=True, exist_ok=True)
    inbox_email.write_text(email_fixture.read_text())

    inbox_transcript = tmp_path / "Inbox" / "Transcripts" / transcript_fixture.name
    inbox_transcript.parent.mkdir(parents=True, exist_ok=True)
    inbox_transcript.write_text(transcript_fixture.read_text())

    pipeline = UnifiedPipeline(tmp_path, dry_run=False, verbose=False, generate_outputs=True, force=True, log_metrics=False)
    monkeypatch.setattr(
        pipeline.extractor,
        "extract",
        lambda env, ctx: _fake_extraction_for_env(env),
    )

    batch = pipeline.process_all()

    assert batch.total == 2
    assert batch.success == 2

    outbox = tmp_path / "Outbox"
    assert outbox.exists()
    assert any(outbox.glob("*_Reply-To_*.md"))


def test_pipeline_apply_archives_source(monkeypatch, tmp_path):
    # Arrange fixtures
    _write_templates(tmp_path)
    _write_readme(tmp_path, "Jeff Denworth")
    _write_readme(tmp_path, "Jason Vallery")

    email_fixture = Path(__file__).parent / "fixtures" / "email_basic.md"
    inbox_path = tmp_path / "Inbox" / "Email" / email_fixture.name
    inbox_path.parent.mkdir(parents=True, exist_ok=True)
    inbox_path.write_text(email_fixture.read_text())

    pipeline = UnifiedPipeline(tmp_path, dry_run=False, verbose=False, generate_outputs=False, force=True, log_metrics=False)

    monkeypatch.setattr(
        pipeline.extractor,
        "extract",
        lambda env, ctx: _fake_extraction(env.source_path),
    )

    result = pipeline.process_file(inbox_path)

    assert result.success is True
    archive_dir = tmp_path / "Sources" / "Email"
    assert any(archive_dir.rglob(email_fixture.name))
