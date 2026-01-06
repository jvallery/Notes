"""Tests for the outputs module."""

import json
from datetime import datetime
from pathlib import Path

from pipeline.models import (
    UnifiedExtraction,
    EntityRef,
    TaskItem,
    SuggestedOutputs,
    CalendarSuggestion,
    ReminderSuggestion,
)
from pipeline.outputs import OutputGenerator


def _create_extraction_with_tasks() -> UnifiedExtraction:
    """Create a test extraction with tasks."""
    return UnifiedExtraction(
        source_file="Inbox/Email/test.md",
        content_type="email",
        processed_at=datetime.now(),
        note_type="people",
        date="2026-01-05",
        title="Weekly Sync",
        summary="Discussed project status and action items",
        participants=["Alice Example"],
        facts=[],
        decisions=[],
        topics=[],
        tasks=[
            TaskItem(
                text="Follow up with Microsoft on pricing",
                owner="Myself",
                due="2026-01-08",
                priority="high",
            ),
            TaskItem(
                text="Review proposal draft",
                owner="Bob Smith",
                due="2026-01-10",
                priority="medium",
            ),
            TaskItem(
                text="Schedule call with Google team",
                priority="low",
            ),
        ],
        questions=[],
        commitments=[],
        mentioned_entities=[],
        confidence=0.9,
    )


def _create_extraction_with_reply_suggestion() -> UnifiedExtraction:
    """Create a test extraction that suggests a reply."""
    extraction = _create_extraction_with_tasks()
    extraction.suggested_outputs = SuggestedOutputs(
        needs_reply=True,
        reply_urgency="normal",
        reply_context="Need to confirm the meeting time for next week",
    )
    return extraction


def _create_extraction_with_calendar_suggestion() -> UnifiedExtraction:
    """Create a test extraction that suggests a calendar invite."""
    extraction = _create_extraction_with_tasks()
    extraction.suggested_outputs = SuggestedOutputs(
        calendar_invite=CalendarSuggestion(
            title="Azure Strategy Review",
            proposed_date="2026-01-10",
            proposed_time="14:00",
            duration_minutes=60,
            attendees=["Alice Example", "Bob Smith"],
            description="Discuss Q1 Azure roadmap",
        )
    )
    return extraction


def test_emit_tasks_creates_proper_format(tmp_path):
    """Test that emit_tasks creates tasks with correct Obsidian format."""
    extraction = _create_extraction_with_tasks()
    generator = OutputGenerator(tmp_path, dry_run=False, verbose=False)
    
    task_lines = generator.emit_tasks(extraction)
    
    # Should emit 3 tasks
    assert len(task_lines) == 3
    
    # Check high priority task format
    high_priority_task = [t for t in task_lines if "Microsoft" in t][0]
    assert "[?]" in high_priority_task  # Proposed status
    assert "📅 2026-01-08" in high_priority_task  # Due date
    assert "⏫" in high_priority_task  # High priority emoji
    assert "#task #proposed #auto" in high_priority_task  # Tags
    
    # Check task with owner
    owner_task = [t for t in task_lines if "Bob Smith" in t][0]
    assert "@Bob Smith" in owner_task
    assert "🔼" in owner_task  # Medium priority
    
    # Check task without owner
    no_owner_task = [t for t in task_lines if "Google" in t][0]
    assert "@" not in no_owner_task.split("#")[0]  # No @ before tags
    assert "🔽" in no_owner_task  # Low priority


def test_emit_tasks_writes_to_tasks_inbox(tmp_path):
    """Test that tasks are written to TASKS_INBOX.md."""
    extraction = _create_extraction_with_tasks()
    generator = OutputGenerator(tmp_path, dry_run=False, verbose=False)
    
    generator.emit_tasks(extraction)
    
    tasks_inbox = tmp_path / "TASKS_INBOX.md"
    assert tasks_inbox.exists()
    
    content = tasks_inbox.read_text()
    assert "## Inbox" in content
    assert "Microsoft" in content
    assert "Bob Smith" in content
    assert "#task #proposed #auto" in content


def test_emit_tasks_dry_run_does_not_write(tmp_path):
    """Test that dry_run=True doesn't write files."""
    extraction = _create_extraction_with_tasks()
    generator = OutputGenerator(tmp_path, dry_run=True, verbose=False)
    
    task_lines = generator.emit_tasks(extraction)
    
    # Should return task lines
    assert len(task_lines) == 3
    
    # But file should not exist
    tasks_inbox = tmp_path / "TASKS_INBOX.md"
    assert not tasks_inbox.exists()


def test_generate_reply_creates_draft_file(tmp_path):
    """Test that generate_reply creates a draft file."""
    extraction = _create_extraction_with_reply_suggestion()
    generator = OutputGenerator(tmp_path, dry_run=False, verbose=False)
    
    reply_path = generator.generate_reply(extraction)
    
    assert reply_path is not None
    assert reply_path.exists()
    
    content = reply_path.read_text()
    assert "type: draft-reply" in content
    assert "status: pending" in content
    assert "Alice Example" in content
    assert "meeting time" in content
    assert "prompt_file:" in content

    prompt_path_line = next(line for line in content.splitlines() if line.startswith("prompt_file:"))
    prompt_rel = prompt_path_line.split(":", 1)[1].strip().strip('"')
    prompt_path = tmp_path / prompt_rel
    assert prompt_path.exists()

    payload = json.loads(prompt_path.read_text())
    assert payload.get("operation") == "draft_reply"
    assert payload.get("messages")


def test_generate_calendar_creates_ics_file(tmp_path):
    """Test that generate_calendar_invite creates an .ics file."""
    extraction = _create_extraction_with_calendar_suggestion()
    generator = OutputGenerator(tmp_path, dry_run=False, verbose=False)
    
    ics_path = generator.generate_calendar_invite(extraction)
    
    assert ics_path is not None
    assert ics_path.exists()
    assert ics_path.suffix == ".ics"
    
    content = ics_path.read_text()
    assert "BEGIN:VCALENDAR" in content
    assert "BEGIN:VEVENT" in content
    assert "Azure Strategy Review" in content
    assert "ATTENDEE" in content


def test_generate_all_returns_all_outputs(tmp_path):
    """Test that generate_all returns all generated outputs."""
    extraction = _create_extraction_with_reply_suggestion()
    extraction.suggested_outputs.calendar_invite = CalendarSuggestion(
        title="Follow-up Call",
        proposed_date="2026-01-12",
    )
    extraction.suggested_outputs.follow_up_reminder = ReminderSuggestion(
        text="Check on Azure pricing response",
        remind_date="2026-01-09",
    )
    
    generator = OutputGenerator(tmp_path, dry_run=False, verbose=False)
    outputs = generator.generate_all(extraction)
    
    # Should have all output types
    assert outputs["reply"] is not None
    assert outputs["calendar"] is not None
    assert outputs["reminder"] is not None
    assert len(outputs["tasks"]) == 3  # 3 tasks from extraction


def test_output_generator_creates_directories(tmp_path):
    """Test that OutputGenerator creates required directories."""
    generator = OutputGenerator(tmp_path, dry_run=False)
    
    assert (tmp_path / "Outbox").exists()
    assert (tmp_path / "Outbox" / "_calendar").exists()
    assert (tmp_path / "Outbox" / "_prompts").exists()


def test_generate_reply_prompt_artifact_includes_context(tmp_path):
    extraction = _create_extraction_with_reply_suggestion()
    generator = OutputGenerator(tmp_path, dry_run=False, verbose=False)

    class DummyContext:
        def get_dynamic_suffix(self):
            return "## RELEVANT ENTITY CONTEXT\n\n### Jeff Denworth\nRole: CRO"

    reply_path = generator.generate_reply(
        extraction,
        context_bundle=DummyContext(),
        source_content="From: Alice Example\nSubject: Weekly Sync\n\nBody goes here.",
    )
    assert reply_path is not None

    content = reply_path.read_text()
    prompt_path_line = next(line for line in content.splitlines() if line.startswith("prompt_file:"))
    prompt_rel = prompt_path_line.split(":", 1)[1].strip().strip('"')
    prompt_path = tmp_path / prompt_rel
    payload = json.loads(prompt_path.read_text())

    messages = payload.get("messages") or []
    system_content = next(m.get("content", "") for m in messages if m.get("role") == "system")
    assert "Never invent" in system_content
    assert "phone" in system_content.lower()
    assert any("SOURCE EMAIL (VERBATIM)" in m.get("content", "") for m in messages)
    assert any("Body goes here." in m.get("content", "") for m in messages)
    assert any("RELEVANT CONTEXT FROM MY NOTES" in m.get("content", "") for m in messages)
    assert any("Jeff Denworth" in m.get("content", "") for m in messages)
