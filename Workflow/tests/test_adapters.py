from pathlib import Path

from pipeline.adapters import AdapterRegistry
from pipeline.adapters.email import EmailAdapter
from pipeline.adapters.transcript import TranscriptAdapter
from pipeline.adapters.document import DocumentAdapter
from pathlib import Path


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
    # Parser captures speaker labels or words; ensure diarization flag set
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


def test_document_adapter_with_fixture(tmp_path):
    fixture = Path(__file__).parent / "fixtures" / "document_basic.md"
    doc_path = tmp_path / "Inbox" / "Attachments" / fixture.name
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(fixture.read_text())

    registry = AdapterRegistry.default()
    env = registry.parse(doc_path)

    assert env.content_type.value == "document"
    assert "Architecture Notes" in env.title or env.title == "document_basic"


def test_adapter_registry_picks_correct_adapter(tmp_path):
    email_path = tmp_path / "Inbox" / "Email" / "2026-01-05_120000_0001_Test.md"
    email_path.parent.mkdir(parents=True, exist_ok=True)
    email_path.write_text("# Subject\n\nFrom: A\nTo: B")

    registry = AdapterRegistry.default()
    adapter = registry.get_adapter(email_path)

    assert isinstance(adapter, EmailAdapter)


def test_email_adapter_with_fixture(tmp_path):
    fixture = Path(__file__).parent / "fixtures" / "email_basic.md"
    inbox_path = tmp_path / "Inbox" / "Email" / fixture.name
    inbox_path.parent.mkdir(parents=True, exist_ok=True)
    inbox_path.write_text(fixture.read_text())

    registry = AdapterRegistry.default()
    env = registry.parse(inbox_path)

    assert env.title.startswith("Weekly Status")
    assert any("Jeff Denworth" in p for p in env.participants)
    assert any("Jason Vallery" in p for p in env.participants)
    assert env.metadata["email"]["is_reply"] is False


def test_transcript_adapter_with_fixture(tmp_path):
    fixture = Path(__file__).parent / "fixtures" / "transcript_basic.md"
    inbox_path = tmp_path / "Inbox" / "Transcripts" / fixture.name
    inbox_path.parent.mkdir(parents=True, exist_ok=True)
    inbox_path.write_text(fixture.read_text())

    registry = AdapterRegistry.default()
    env = registry.parse(inbox_path)

    assert env.content_type.value == "transcript"
    assert any("Jason Vallery" in p for p in env.participants)
    assert "Azure Sync" in env.title or env.title == "transcript_basic"


def test_email_adapter_preserves_addresses(tmp_path):
    fixture = Path(__file__).parent / "fixtures" / "email_basic.md"
    inbox_path = tmp_path / "Inbox" / "Email" / fixture.name
    inbox_path.parent.mkdir(parents=True, exist_ok=True)
    inbox_path.write_text(fixture.read_text())

    env = AdapterRegistry.default().parse(inbox_path)
    email_meta = env.metadata.get("email", {})

    assert email_meta.get("sender_email") == "jeff@vastdata.com"
    assert "jason@vastdata.com" in email_meta.get("recipients_emails", [])
    assert any(rec.get("email") == "lior@vastdata.com" for rec in email_meta.get("recipients_detail", []))
