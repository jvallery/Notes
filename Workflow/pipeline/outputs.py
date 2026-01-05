"""
Output Generation - Create draft replies, calendar invites, and task files.

This module handles the output generation phase of the unified pipeline,
producing actionable outputs from extracted knowledge.

Outputs:
- Draft email replies → Inbox/_drafts/replies/
- Calendar invites → Inbox/_drafts/calendar/
- Task aggregations → TASKS_INBOX.md or entity README

Usage:
    generator = OutputGenerator(vault_root)
    draft_path = generator.generate_reply(extraction, context)
    ics_path = generator.generate_calendar_invite(extraction)
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from .models import UnifiedExtraction, SuggestedOutputs, CalendarSuggestion


class OutputGenerator:
    """Generate output files from extraction results.
    
    Generates:
    - Draft email replies with frontmatter metadata
    - Calendar .ics files for suggested meetings
    - Follow-up reminder tasks
    """
    
    def __init__(self, vault_root: Path, dry_run: bool = False, verbose: bool = False):
        self.vault_root = vault_root
        self.dry_run = dry_run
        self.verbose = verbose
        
        # Ensure output directories exist
        self.drafts_dir = vault_root / "Inbox" / "_drafts"
        self.replies_dir = self.drafts_dir / "replies"
        self.calendar_dir = self.drafts_dir / "calendar"
        
        if not dry_run:
            self.replies_dir.mkdir(parents=True, exist_ok=True)
            self.calendar_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_all(
        self, 
        extraction: UnifiedExtraction, 
        context_bundle: Optional[object] = None,
        source_content: str = ""
    ) -> dict:
        """Generate all outputs based on extraction.
        
        Args:
            extraction: The UnifiedExtraction with suggested_outputs
            context_bundle: Optional ContextBundle for reply generation
            source_content: Original content for reply generation
        
        Returns:
            Dict with paths to generated files:
            {
                "reply": Path or None,
                "calendar": Path or None,
                "reminder": Path or None
            }
        """
        outputs = {
            "reply": None,
            "calendar": None,
            "reminder": None,
        }
        
        suggested = extraction.suggested_outputs
        
        # Generate reply if needed
        if suggested.needs_reply:
            outputs["reply"] = self.generate_reply(extraction, context_bundle, source_content)
        
        # Generate calendar invite if suggested
        if suggested.calendar_invite:
            outputs["calendar"] = self.generate_calendar_invite(extraction)
        
        # Generate reminder if suggested
        if suggested.follow_up_reminder:
            outputs["reminder"] = self.generate_reminder(extraction)
        
        return outputs
    
    def generate_reply(
        self,
        extraction: UnifiedExtraction,
        context_bundle: Optional[object] = None,
        source_content: str = ""
    ) -> Optional[Path]:
        """Generate a draft email reply.
        
        Creates a markdown file with frontmatter metadata and draft body.
        The user can review, edit, and send from their email client.
        
        Args:
            extraction: UnifiedExtraction with email metadata
            context_bundle: Optional ContextBundle for LLM generation
            source_content: Original email content for context
        
        Returns:
            Path to generated draft file, or None if not generated
        """
        suggested = extraction.suggested_outputs
        
        if not suggested.needs_reply:
            return None
        
        # Determine recipient from extraction
        # For emails, participants[0] is typically the sender
        sender = extraction.participants[0] if extraction.participants else "Unknown"
        
        # Generate filename
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        safe_sender = "".join(c if c.isalnum() or c in "- " else "_" for c in sender)[:30]
        filename = f"{date_str}_reply_to_{safe_sender}.md"
        
        output_path = self.replies_dir / filename
        
        # Build draft content
        # If we have a context bundle and source content, we could call LLM here
        # For now, use the reply_context from extraction as a starting point
        draft_body = self._build_reply_body(extraction, suggested.reply_context or "")
        
        content = f"""---
type: draft-reply
status: pending
created: "{datetime.now().isoformat()}"
urgency: "{suggested.reply_urgency}"
to: "{sender}"
subject: "Re: {extraction.title}"
source_file: "{extraction.source_file}"
---

# Draft Reply to {sender}

**Regarding**: {extraction.title}
**Urgency**: {suggested.reply_urgency}

---

## Key Points to Address

{suggested.reply_context or "No specific points identified"}

---

## Draft Response

{draft_body}

---

## Original Summary

{extraction.summary}

---

*This draft was auto-generated. Edit and send via your email client.*
"""
        
        if self.dry_run:
            if self.verbose:
                print(f"  [DRY RUN] Would generate reply: {output_path}")
            return output_path
        
        output_path.write_text(content)
        
        if self.verbose:
            print(f"  Generated draft reply: {output_path.name}")
        
        return output_path
    
    def _build_reply_body(self, extraction: UnifiedExtraction, reply_context: str) -> str:
        """Build the draft reply body.
        
        This is a simple version that provides a template.
        A more advanced version would call the LLM with persona + context.
        """
        # Extract questions/requests from the extraction
        questions = extraction.questions if hasattr(extraction, 'questions') else []
        commitments = extraction.commitments if hasattr(extraction, 'commitments') else []
        
        body_parts = []
        
        # Opener
        sender = extraction.participants[0] if extraction.participants else "there"
        first_name = sender.split()[0] if sender != "Unknown" else "there"
        body_parts.append(f"Hi {first_name},")
        body_parts.append("")
        
        # Address key points
        if reply_context:
            body_parts.append("Thank you for your email. Here's my response:")
            body_parts.append("")
            
            # Convert reply_context to bullet points if not already
            for point in reply_context.split(". "):
                if point.strip():
                    body_parts.append(f"- {point.strip()}")
            body_parts.append("")
        
        # Address questions
        if questions:
            body_parts.append("To answer your questions:")
            for q in questions[:3]:
                body_parts.append(f"- {q}: [TODO: Add answer]")
            body_parts.append("")
        
        # Note any commitments
        if commitments:
            body_parts.append("I'll follow up on:")
            for c in commitments[:3]:
                body_parts.append(f"- {c}")
            body_parts.append("")
        
        # Closer
        body_parts.append("Let me know if you have any questions.")
        body_parts.append("")
        body_parts.append("Best,")
        body_parts.append("Jason")
        
        return "\n".join(body_parts)
    
    def generate_calendar_invite(self, extraction: UnifiedExtraction) -> Optional[Path]:
        """Generate a calendar .ics file from suggested calendar invite.
        
        Creates a standard iCalendar file that can be imported into
        any calendar application.
        
        Args:
            extraction: UnifiedExtraction with calendar_invite suggestion
        
        Returns:
            Path to generated .ics file, or None if not generated
        """
        cal_suggest = extraction.suggested_outputs.calendar_invite
        
        if not cal_suggest:
            return None
        
        # Generate filename
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        safe_title = "".join(c if c.isalnum() or c in "- " else "_" for c in cal_suggest.title)[:30]
        filename = f"{date_str}_mtg_{safe_title}.ics"
        
        output_path = self.calendar_dir / filename
        
        # Parse proposed date
        try:
            if cal_suggest.proposed_date:
                start_date = datetime.strptime(cal_suggest.proposed_date, "%Y-%m-%d")
                # Default to 10 AM if no time specified
                start_dt = start_date.replace(hour=10, minute=0)
            else:
                # Default to tomorrow at 10 AM
                start_dt = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0) + timedelta(days=1)
        except ValueError:
            start_dt = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0) + timedelta(days=1)
        
        duration = cal_suggest.duration_minutes or 30
        end_dt = start_dt + timedelta(minutes=duration)
        
        # Format for iCal
        dtstart = start_dt.strftime("%Y%m%dT%H%M%S")
        dtend = end_dt.strftime("%Y%m%dT%H%M%S")
        dtstamp = datetime.now().strftime("%Y%m%dT%H%M%SZ")
        uid = f"{date_str}-{extraction.source_file.replace('/', '-')}"
        
        # Build attendee list
        attendees = cal_suggest.attendees or []
        attendee_lines = "\n".join(
            f"ATTENDEE;ROLE=REQ-PARTICIPANT:mailto:{a}@example.com"
            for a in attendees if a
        )
        
        # Build iCal content
        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//VAST Notes Pipeline//Calendar Generator//EN
CALSCALE:GREGORIAN
METHOD:REQUEST
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
DTSTART:{dtstart}
DTEND:{dtend}
SUMMARY:{cal_suggest.title}
DESCRIPTION:Auto-generated from email/meeting notes.\\nSource: {extraction.source_file}
{attendee_lines}
STATUS:TENTATIVE
END:VEVENT
END:VCALENDAR
"""
        
        if self.dry_run:
            if self.verbose:
                print(f"  [DRY RUN] Would generate calendar: {output_path}")
            return output_path
        
        output_path.write_text(ics_content)
        
        if self.verbose:
            print(f"  Generated calendar invite: {output_path.name}")
        
        return output_path
    
    def generate_reminder(self, extraction: UnifiedExtraction) -> Optional[Path]:
        """Generate a reminder task entry.
        
        Instead of a separate file, appends to TASKS_INBOX.md with
        the proposed [?] status for triage.
        
        Args:
            extraction: UnifiedExtraction with follow_up_reminder suggestion
        
        Returns:
            Path to TASKS_INBOX.md if modified, or None
        """
        reminder = extraction.suggested_outputs.follow_up_reminder
        
        if not reminder:
            return None
        
        tasks_inbox = self.vault_root / "TASKS_INBOX.md"
        
        # Format task with proposed status
        reminder_text = reminder.text
        remind_date = reminder.remind_date or (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
        
        task_line = f"- [?] {reminder_text} 📅 {remind_date} #task #proposed #auto\n"
        
        if self.dry_run:
            if self.verbose:
                print(f"  [DRY RUN] Would add reminder: {task_line.strip()}")
            return tasks_inbox
        
        # Append to TASKS_INBOX.md
        if tasks_inbox.exists():
            existing = tasks_inbox.read_text()
            # Add under "## Inbox" section if it exists, or at end
            if "## Inbox" in existing:
                existing = existing.replace("## Inbox\n", f"## Inbox\n{task_line}")
            else:
                existing += f"\n{task_line}"
            tasks_inbox.write_text(existing)
        else:
            tasks_inbox.write_text(f"# Tasks Inbox\n\n## Inbox\n{task_line}")
        
        if self.verbose:
            print(f"  Added reminder to TASKS_INBOX.md")
        
        return tasks_inbox


def generate_outputs_from_extraction(
    extraction: UnifiedExtraction,
    vault_root: Path,
    dry_run: bool = False,
    verbose: bool = False,
) -> dict:
    """Convenience function to generate all outputs from an extraction.
    
    Args:
        extraction: UnifiedExtraction result
        vault_root: Path to vault root
        dry_run: If True, don't write files
        verbose: If True, log output generation
    
    Returns:
        Dict with paths to generated files
    """
    generator = OutputGenerator(vault_root, dry_run=dry_run, verbose=verbose)
    return generator.generate_all(extraction)
