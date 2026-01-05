from datetime import datetime
from pathlib import Path

from pipeline.pipeline import UnifiedPipeline
from pipeline.envelope import ContentEnvelope, ContentType
from pipeline.models import (
    UnifiedExtraction,
    EntityRef,
    Fact,
    TaskItem,
    MentionedEntity,
    SuggestedOutputs,
)
from pipeline.patch import ChangePlan, PatchOperation
from pipeline.apply import ApplyResult, TransactionalApply


def _fake_envelope(path: Path) -> ContentEnvelope:
    return ContentEnvelope(
        source_path=path,
        content_type=ContentType.EMAIL,
        raw_content="Hello world",
        date="2026-01-05",
        title="Test Email",
        participants=["Alice Example"],
        metadata={},
    )


def _fake_extraction(source_path: Path) -> UnifiedExtraction:
    primary = EntityRef(entity_type="person", name="Alice Example", confidence=0.9)
    fact = Fact(text="Alice cares about Azure", about_entity=primary, fact_type="preference")
    task = TaskItem(text="Follow up with Alice", owner="Myself", priority="high", related_person="Alice Example")
    mention = MentionedEntity(entity_type="person", name="Alice Example", facts_about=["Alice cares about Azure"])
    return UnifiedExtraction(
        source_file=str(source_path),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=primary,
        date="2026-01-05",
        title="Test Email",
        summary="Summary about Alice",
        participants=["Alice Example"],
        facts=[fact],
        tasks=[task],
        mentioned_entities=[mention],
        suggested_outputs=SuggestedOutputs(needs_reply=False),
    )


def _fake_plan() -> ChangePlan:
    return ChangePlan(
        source_file="Inbox/Email/test.md",
        meeting_note_path="VAST/People/Alice Example/2026-01-05 - Test Email.md",
        meeting_note={"type": "people", "title": "Test Email", "date": "2026-01-05"},
        patches=[
            PatchOperation(
                operation="patch",
                target_path="VAST/People/Alice Example/README.md",
                target_entity="Alice Example",
                add_facts=["Alice cares about Azure"],
            )
        ],
    )


def test_process_file_dry_run(monkeypatch, tmp_path):
    inbox_file = tmp_path / "Inbox" / "Email" / "test.md"
    inbox_file.parent.mkdir(parents=True, exist_ok=True)
    inbox_file.write_text("hello")

    pipeline = UnifiedPipeline(tmp_path, dry_run=True, verbose=False, generate_outputs=False)

    monkeypatch.setattr(pipeline.registry, "parse", lambda p: _fake_envelope(p))
    monkeypatch.setattr(pipeline.extractor, "extract", lambda env, ctx: _fake_extraction(env.source_path))
    monkeypatch.setattr(pipeline.patch_generator, "generate", lambda extraction: _fake_plan())

    result = pipeline.process_file(inbox_file)

    assert result.success is True
    assert result.plan is not None
    assert result.apply_result is None  # dry run skips apply
    assert result.plan.meeting_note_path.endswith("Test Email.md")


def test_process_file_with_apply(monkeypatch, tmp_path):
    inbox_file = tmp_path / "Inbox" / "Email" / "test.md"
    inbox_file.parent.mkdir(parents=True, exist_ok=True)
    inbox_file.write_text("hello")

    pipeline = UnifiedPipeline(tmp_path, dry_run=False, verbose=False, generate_outputs=False)

    monkeypatch.setattr(pipeline.registry, "parse", lambda p: _fake_envelope(p))
    monkeypatch.setattr(pipeline.extractor, "extract", lambda env, ctx: _fake_extraction(env.source_path))
    monkeypatch.setattr(pipeline.patch_generator, "generate", lambda extraction: _fake_plan())

    def fake_apply(self, plan, source_path=None):
        res = ApplyResult()
        res.files_created.append(plan.meeting_note_path)
        res.files_modified.extend([p.target_path for p in plan.patches])
        return res

    monkeypatch.setattr(TransactionalApply, "apply", fake_apply)

    result = pipeline.process_file(inbox_file)

    assert result.success is True
    assert result.apply_result is not None
    assert "README.md" in result.apply_result.files_modified[0]
