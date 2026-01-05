from datetime import datetime
from pathlib import Path

from pipeline.envelope import ContentType, ContentEnvelope
from pipeline.models import UnifiedExtraction, EntityRef, SuggestedOutputs
from pipeline.patch import ChangePlan
from pipeline.pipeline import UnifiedPipeline


def test_pipeline_collects_metrics(monkeypatch, tmp_path):
    inbox_file = tmp_path / "Inbox" / "Email" / "metric.md"
    inbox_file.parent.mkdir(parents=True, exist_ok=True)
    inbox_file.write_text("body")

    pipeline = UnifiedPipeline(
        tmp_path,
        dry_run=True,
        verbose=False,
        generate_outputs=False,
        force=True,
        log_metrics=False,
    )

    envelope = ContentEnvelope(
        source_path=inbox_file,
        content_type=ContentType.EMAIL,
        raw_content="body",
        date="2026-01-05",
        title="Metrics Test",
        participants=["Alice Example"],
    )

    extraction = UnifiedExtraction(
        source_file=str(inbox_file),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=EntityRef(entity_type="person", name="Alice Example", confidence=0.9),
        date="2026-01-05",
        title="Metrics Test",
        summary="Summary",
        participants=["Alice Example"],
        facts=[],
        tasks=[],
        mentioned_entities=[],
        suggested_outputs=SuggestedOutputs(needs_reply=False),
        confidence=0.9,
    )

    monkeypatch.setattr(pipeline.registry, "parse", lambda p: envelope)

    def fake_extract(env, ctx):
        pipeline.extractor.last_usage = {
            "model": "gpt-4o",
            "prompt_tokens": 120,
            "completion_tokens": 20,
            "total_tokens": 140,
            "cached_tokens": 60,
            "cache_hit": True,
            "latency_ms": 50,
        }
        return extraction

    monkeypatch.setattr(pipeline.extractor, "extract", fake_extract)
    monkeypatch.setattr(pipeline.patch_generator, "generate", lambda ext: ChangePlan(source_file=str(inbox_file)))

    batch = pipeline.process_all()

    assert batch.metrics["cache"]["hits"] == 1
    assert batch.metrics["cache"]["cached_tokens"] == 60
    assert batch.metrics["phase_ms_avg"]["extract_ms"] >= 0
    result_metrics = batch.results[0].metrics
    assert result_metrics["timings"]["adapter_ms"] >= 0
    assert result_metrics["cache"]["cache_hit"] is True


def test_pipeline_adds_header_contacts(monkeypatch, tmp_path):
    inbox_file = tmp_path / "Inbox" / "Email" / "mail.md"
    inbox_file.parent.mkdir(parents=True, exist_ok=True)
    inbox_file.write_text("body")

    pipeline = UnifiedPipeline(
        tmp_path,
        dry_run=True,
        verbose=False,
        generate_outputs=False,
        force=True,
        log_metrics=False,
    )

    email_meta = {
        "sender_name": "Sender Name",
        "sender_email": "sender@example.com",
        "recipients": ["Recipient Name"],
        "recipients_emails": ["recipient@example.com"],
        "recipients_detail": [{"name": "Recipient Name", "email": "recipient@example.com"}],
    }
    envelope = ContentEnvelope(
        source_path=inbox_file,
        content_type=ContentType.EMAIL,
        raw_content="body",
        date="2026-01-05",
        title="Metrics Test",
        participants=["Sender Name", "Recipient Name"],
        metadata={"email": email_meta},
    )

    extraction = UnifiedExtraction(
        source_file=str(inbox_file),
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        primary_entity=None,
        date="2026-01-05",
        title="Metrics Test",
        summary="Summary",
        participants=[],
        contacts=[],
        facts=[],
        tasks=[],
        mentioned_entities=[],
        suggested_outputs=SuggestedOutputs(needs_reply=False),
        confidence=0.9,
    )

    monkeypatch.setattr(pipeline.registry, "parse", lambda p: envelope)

    captured = {}

    def fake_extract(env, ctx):
        pipeline.extractor.last_usage = {}
        return extraction

    def fake_generate(extraction_input):
        captured["contacts"] = [c.email for c in extraction_input.contacts if c.email]
        captured["participants"] = extraction_input.participants
        return ChangePlan(source_file=str(inbox_file))

    monkeypatch.setattr(pipeline.extractor, "extract", fake_extract)
    monkeypatch.setattr(pipeline.patch_generator, "generate", fake_generate)

    pipeline.process_all()

    assert "sender@example.com" in captured["contacts"]
    assert "recipient@example.com" in captured["contacts"]
    assert captured["participants"] == ["Sender Name", "Recipient Name"]
