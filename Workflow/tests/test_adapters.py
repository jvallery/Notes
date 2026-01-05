from pathlib import Path

from pipeline.adapters import AdapterRegistry
from pipeline.adapters.email import EmailAdapter
from pipeline.adapters.transcript import TranscriptAdapter
from pipeline.adapters.document import DocumentAdapter


def test_email_adapter_can_handle_and_parse(tmp_path):
    email_path = tmp_path / "Inbox" / "Email" / "2026-01-05_120000_0001_Test Subject.md"
    email_path.parent.mkdir(parents=True, exist_ok=True)
    email_path.write_text("# Test Subject\n\n**From:** Alice Example <alice@example.com>\n**To:** Bob Example <bob@example.com>\n\nBody here.")

    adapter = EmailAdapter()
    assert adapter.can_handle(email_path)

    env = adapter.parse(email_path)
    assert env.content_type.value == "email"
    assert env.title == "Test Subject"
    # Parser preserves leading markdown markers; verify names are present
    assert any("Alice Example" in p for p in env.participants)
    assert any("Bob Example" in p for p in env.participants)
    assert env.metadata["email"]["subject"] == "Test Subject"


def test_transcript_adapter_can_handle_and_parse(tmp_path):
    transcript_path = tmp_path / "Inbox" / "Transcripts" / "2026-01-05 12 00 - Standup.md"
    transcript_path.parent.mkdir(parents=True, exist_ok=True)
    transcript_path.write_text("Speaker 1: Hello\nSpeaker 2: Hi")

    adapter = TranscriptAdapter()
    assert adapter.can_handle(transcript_path)

    env = adapter.parse(transcript_path)
    assert env.content_type.value == "transcript"
    assert "Standup" in env.title
    assert "Speaker 1" in env.participants
    assert env.metadata["transcript"]["has_diarization"] is True


def test_document_adapter_can_handle_and_parse(tmp_path):
    doc_path = tmp_path / "Inbox" / "Attachments" / "notes.md"
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text("# Doc Title\n\nauthor: Jane\ncontent")

    adapter = DocumentAdapter()
    assert adapter.can_handle(doc_path)

    env = adapter.parse(doc_path)
    assert env.content_type.value == "document"
    assert env.title == "Doc Title"
    assert env.metadata["document"]["document_type"] == "general"


def test_adapter_registry_picks_correct_adapter(tmp_path):
    email_path = tmp_path / "Inbox" / "Email" / "2026-01-05_120000_0001_Test.md"
    email_path.parent.mkdir(parents=True, exist_ok=True)
    email_path.write_text("# Subject\n\nFrom: A\nTo: B")

    registry = AdapterRegistry.default()
    adapter = registry.get_adapter(email_path)

    assert isinstance(adapter, EmailAdapter)
