import json
from pathlib import Path

import pipeline.extract as extract_mod
from pipeline.envelope import ContentEnvelope, ContentType
from pipeline.context import _cached_persona_context, _cached_glossary_context
from pipeline.extract import UnifiedExtractor


class FakeOpenAIResponse:
    def __init__(self, content: dict):
        self.choices = [type("Choice", (), {"message": type("Msg", (), {"content": json.dumps(content)})})]
        self.usage = type("Usage", (), {"prompt_tokens": 200, "cached_tokens": 50})


class FakeChat:
    def __init__(self, responder):
        self._responder = responder

    def completions_create(self, **kwargs):
        return self._responder(**kwargs)

    # Compatibility with .chat.completions.create signature
    @property
    def completions(self):
        return self

    def create(self, **kwargs):
        return self._responder(**kwargs)


class FakeClient:
    def __init__(self, responder):
        self.chat = FakeChat(responder)


def test_unified_extractor_calls_openai_with_context(monkeypatch, tmp_path):
    # Disable cached prompt helpers so we control context content
    monkeypatch.setattr(extract_mod, "_cached_persona_context", None, raising=False)
    monkeypatch.setattr(extract_mod, "_cached_glossary_context", None, raising=False)

    captured = {}

    def responder(**kwargs):
        captured["messages"] = kwargs["messages"]
        payload = {
            "note_type": "people",
            "primary_entity": {"entity_type": "person", "name": "Alice Example", "confidence": 0.9},
            "title": "Test Title",
            "summary": "Summary",
            "participants": ["Alice Example"],
            "contacts": [],
            "facts": [],
            "decisions": [],
            "topics": [],
            "tasks": [],
            "questions": [],
            "commitments": [],
            "mentioned_entities": [],
            "email_requires_response": False,
            "email_urgency": "medium",
            "email_type": "other",
            "suggested_outputs": {"needs_reply": False},
            "confidence": 0.9,
        }
        return FakeOpenAIResponse(payload)

    fake_client = FakeClient(responder)
    monkeypatch.setattr("pipeline.extract.get_model_config", lambda _: {"model": "gpt-4o"}, raising=False)
    monkeypatch.setattr("scripts.utils.ai_client.get_openai_client", lambda caller=None: fake_client, raising=False)

    extractor = UnifiedExtractor(tmp_path, verbose=True)
    env = ContentEnvelope(
        source_path=tmp_path / "Inbox" / "Email" / "test.md",
        content_type=ContentType.EMAIL,
        raw_content="body",
        date="2026-01-05",
        title="Title",
        participants=["Alice Example"],
    )

    result = extractor.extract(env)

    assert result.note_type == "people"
    assert result.primary_entity and result.primary_entity.name == "Alice Example"
    assert captured["messages"][0]["role"] == "system"
    assert captured["messages"][1]["role"] == "user"
    assert "PERSONA" in captured["messages"][0]["content"]
    assert "Extract knowledge" in captured["messages"][1]["content"]


def test_model_selection_by_content_type(monkeypatch, tmp_path):
    # Verify task-specific model lookup (extract_email, extract_transcript, etc.)
    monkeypatch.setattr(extract_mod, "_cached_persona_context", None, raising=False)
    monkeypatch.setattr(extract_mod, "_cached_glossary_context", None, raising=False)

    captured = {}

    def responder(**kwargs):
        captured["model"] = kwargs.get("model")
        payload = {
            "note_type": "people",
            "primary_entity": {"entity_type": "person", "name": "Alice Example", "confidence": 0.9},
            "title": "Test Title",
            "summary": "Summary",
            "participants": [],
            "contacts": [],
            "facts": [],
            "decisions": [],
            "topics": [],
            "tasks": [],
            "questions": [],
            "commitments": [],
            "mentioned_entities": [],
            "email_requires_response": False,
            "email_urgency": "medium",
            "email_type": "other",
            "suggested_outputs": {"needs_reply": False},
            "confidence": 0.9,
        }
        return FakeOpenAIResponse(payload)

    fake_client = FakeClient(responder)
    # Return a distinct model for the email task key
    monkeypatch.setattr("pipeline.extract.get_model_config", lambda task: {"model": f"model-for-{task}"}, raising=False)
    monkeypatch.setattr("scripts.utils.ai_client.get_openai_client", lambda caller=None: fake_client, raising=False)

    extractor = UnifiedExtractor(tmp_path, verbose=False)
    env = ContentEnvelope(
        source_path=tmp_path / "Inbox" / "Email" / "test.md",
        content_type=ContentType.EMAIL,
        raw_content="body",
        date="2026-01-05",
        title="Title",
        participants=[],
    )

    extractor.extract(env)

    assert captured["model"] == "model-for-extract_email"

