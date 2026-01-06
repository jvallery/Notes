"""
Output Generation - Create draft replies, calendar invites, and task files.

This module handles the output generation phase of the unified pipeline,
producing actionable outputs from extracted knowledge.

Outputs:
- Draft email replies → Outbox/
- Calendar invites → Outbox/_calendar/
- Task aggregations → TASKS_INBOX.md or entity README

Usage:
    generator = OutputGenerator(vault_root)
    draft_path = generator.generate_reply(extraction, context)
    ics_path = generator.generate_calendar_invite(extraction)
"""

import json
import sys
import re
import yaml
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from .models import UnifiedExtraction, SuggestedOutputs, CalendarSuggestion
from scripts.utils import get_model_config, workflow_root


def _load_persona() -> dict:
    """Load the communication persona from profiles/jason_persona.yaml."""
    persona_path = workflow_root() / "profiles" / "jason_persona.yaml"
    if persona_path.exists():
        with open(persona_path) as f:
            return yaml.safe_load(f)
    return {}


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
        self.outbox_dir = vault_root / "Outbox"
        self.replies_dir = self.outbox_dir
        self.calendar_dir = self.outbox_dir / "_calendar"
        self.prompts_dir = self.outbox_dir / "_prompts"
        
        if not dry_run:
            self.outbox_dir.mkdir(parents=True, exist_ok=True)
            self.calendar_dir.mkdir(parents=True, exist_ok=True)
            self.prompts_dir.mkdir(parents=True, exist_ok=True)

    def _as_vault_relative(self, path: Path) -> str:
        """Return a vault-relative path string when possible."""
        try:
            return str(path.relative_to(self.vault_root))
        except Exception:
            return str(path)
    
    def generate_all(
        self, 
        extraction: UnifiedExtraction, 
        context_bundle: Optional[object] = None,
        source_content: str = "",
        force_reply: bool = False
    ) -> dict:
        """Generate all outputs based on extraction.
        
        Args:
            extraction: The UnifiedExtraction with suggested_outputs
            context_bundle: Optional ContextBundle for reply generation
            source_content: Original content for reply generation
            force_reply: If True, generate reply regardless of needs_reply
        
        Returns:
            Dict with paths to generated files:
            {
                "reply": Path or None,
                "calendar": Path or None,
                "reminder": Path or None,
                "tasks": list of task lines or []
            }
        """
        outputs = {
            "reply": None,
            "calendar": None,
            "reminder": None,
            "tasks": [],
        }
        
        suggested = extraction.suggested_outputs
        
        # Generate reply if needed (or forced for emails)
        if suggested.needs_reply or force_reply:
            outputs["reply"] = self.generate_reply(extraction, context_bundle, source_content)
        
        # Generate calendar invite if suggested
        if suggested.calendar_invite:
            outputs["calendar"] = self.generate_calendar_invite(extraction)
        
        # Generate reminder if suggested
        if suggested.follow_up_reminder:
            outputs["reminder"] = self.generate_reminder(extraction)
        
        # Emit all tasks from extraction to TASKS_INBOX.md
        if extraction.tasks:
            outputs["tasks"] = self.emit_tasks(extraction)
        
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
        
        # Note: needs_reply check is handled by caller (generate_all)
        # This method generates a reply unconditionally when called
        
        # Determine recipient from extraction
        # For emails, the sender is in contacts[0] (not participants which includes "Myself")
        sender = "Unknown"
        sender_email = ""
        if extraction.contacts:
            first_contact = extraction.contacts[0]
            sender = first_contact.name if first_contact.name else "Unknown"
            sender_email = first_contact.email or ""
        elif extraction.participants:
            # Fallback to first non-self participant
            for p in extraction.participants:
                if p.lower() not in ("myself", "jason vallery", "jason"):
                    sender = p
                    break
            if sender == "Unknown" and extraction.participants:
                sender = extraction.participants[0]
        
        # Generate filename
        today = datetime.now().strftime("%Y-%m-%d")
        subject_slug = re.sub(r"[^\w\s-]", "", extraction.title or "email")
        subject_slug = re.sub(r"\s+", "-", subject_slug).strip("-")[:40] or "email"

        filename = f"{today}_Reply-To_{subject_slug}.md"
        output_path = self.replies_dir / filename

        # Avoid overwriting
        counter = 1
        while output_path.exists():
            filename = f"{today}_Reply-To_{subject_slug}_{counter}.md"
            output_path = self.replies_dir / filename
            counter += 1

        prompt_path = self.prompts_dir / f"{output_path.stem}.prompt.json"
        prompt_ref = self._as_vault_relative(prompt_path)
        model_config = get_model_config("draft_responses")
        
        # Build draft content
        # Use LLM with persona for high-quality replies
        draft_body = self._build_reply_body(
            extraction,
            suggested.reply_context or "",
            source_content,
            prompt_path=prompt_path,
            draft_path=output_path,
        )
        
        # Include email if available
        to_field = f"{sender} <{sender_email}>" if sender_email else sender
        
        content = f"""---
	type: draft-reply
	status: pending
	created: "{datetime.now().isoformat()}"
	urgency: "{suggested.reply_urgency}"
	to: "{to_field}"
	subject: "Re: {extraction.title}"
	source_file: "{extraction.source_file}"
	ai_model: "{model_config.get('model', '')}"
	ai_temperature: {float(model_config.get('temperature', 0.7))}
	prompt_file: "{prompt_ref}"
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
    
    def _build_reply_body(
        self,
        extraction: UnifiedExtraction,
        reply_context: str,
        source_content: str = "",
        *,
        prompt_path: Optional[Path] = None,
        draft_path: Optional[Path] = None,
    ) -> str:
        """Build the draft reply body using LLM with persona.
        
        Uses the jason_persona.yaml to generate impact-driven, persona-aligned responses.
        Falls back to a simple template if LLM call fails.
        """
        # Try LLM-based generation
        try:
            return self._generate_llm_reply(
                extraction,
                reply_context,
                source_content,
                prompt_path=prompt_path,
                draft_path=draft_path,
            )
        except Exception as e:
            if self.verbose:
                print(f"  [WARN] LLM reply generation failed: {e}, using template fallback")
            return self._build_template_reply(extraction, reply_context)
    
    def _generate_llm_reply(
        self,
        extraction: UnifiedExtraction,
        reply_context: str,
        source_content: str = "",
        *,
        prompt_path: Optional[Path] = None,
        draft_path: Optional[Path] = None,
    ) -> str:
        """Generate reply body using LLM with persona."""
        from scripts.utils.ai_client import get_openai_client
        
        model_config = get_model_config("draft_responses")
        persona = _load_persona()
        
        # Build persona context
        identity = persona.get("identity", {})
        style = persona.get("style", {})
        
        # Determine sender
        sender = "Unknown"
        if extraction.contacts:
            sender = extraction.contacts[0].name or "Unknown"
        elif extraction.participants:
            for p in extraction.participants:
                if p.lower() not in ("myself", "jason vallery", "jason"):
                    sender = p
                    break
        first_name = sender.split()[0] if sender != "Unknown" else "there"
        
        # Build questions and commitments
        questions = extraction.questions if hasattr(extraction, 'questions') else []
        commitments = extraction.commitments if hasattr(extraction, 'commitments') else []
        
        system_prompt = f"""You are {identity.get('name', 'Jason Vallery')}, {identity.get('role', 'VP of Product Management for Cloud')} at {identity.get('company', 'VAST Data')}.

## COMMUNICATION STYLE
- Direct but Empathetic: Respect their time while acknowledging their effort
- Bias for Action: Use active voice with specific next steps  
- Confident & Expert: No hedging on technical facts
- BLUF: Bottom Line Up Front - the answer goes in the first 2 sentences

## FORMATTING RULES
- Short paragraphs (1-2 sentences)
- Use specific dates/times, not "soon" or "when you can"
- Professional warmth without emojis
- Keep response to 2-4 paragraphs total

## YOUR TASK
Write a complete, ready-to-send email reply. Do NOT include placeholders like [TODO] or [Add answer].
If you don't have enough information to answer something, either:
1. Make a reasonable assumption and answer
2. Acknowledge you'll need to check and get back to them with a specific timeframe

	Return ONLY the email body text (no subject line, no markdown headers, no frontmatter)."""

        user_prompt = f"""Write a reply to {sender} about: {extraction.title}

## EMAIL SUMMARY
{extraction.summary}

## KEY POINTS TO ADDRESS
{reply_context or "No specific points identified"}

## QUESTIONS ASKED
{json.dumps(questions) if questions else "None"}

## COMMITMENTS MADE
{json.dumps(commitments) if commitments else "None"}

## CONTEXT
- Recipient first name: {first_name}
- Urgency: {extraction.suggested_outputs.reply_urgency if extraction.suggested_outputs else "normal"}

	Write the complete email body now (greeting through signature):"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        if prompt_path and not self.dry_run:
            try:
                prompt_payload = {
                    "created": datetime.now().isoformat(),
                    "operation": "draft_reply",
                    "model": model_config.get("model", ""),
                    "temperature": model_config.get("temperature", 0.7),
                    "source_file": extraction.source_file,
                    "draft_path": str(draft_path) if draft_path else None,
                    "messages": messages,
                }
                prompt_path.write_text(json.dumps(prompt_payload, indent=2))
            except Exception as exc:
                if self.verbose:
                    print(f"  [WARN] Failed to write prompt artifact: {exc}")

        client = get_openai_client("pipeline.outputs.generate_reply")
        if draft_path:
            client.set_context(
                {
                    "source_file": extraction.source_file,
                    "draft_path": str(draft_path),
                    "prompt_path": str(prompt_path) if prompt_path else None,
                }
            )

        response = client.chat.completions.create(
            model=model_config["model"],
            messages=messages,
            temperature=model_config.get("temperature", 0.7),
        )
        
        return response.choices[0].message.content.strip()
    
    def _build_template_reply(self, extraction: UnifiedExtraction, reply_context: str) -> str:
        """Build a simple template-based reply (fallback)."""
        questions = extraction.questions if hasattr(extraction, 'questions') else []
        commitments = extraction.commitments if hasattr(extraction, 'commitments') else []
        
        body_parts = []
        
        # Determine the sender's first name
        sender = "there"
        if extraction.contacts:
            sender = extraction.contacts[0].name or "there"
        elif extraction.participants:
            for p in extraction.participants:
                if p.lower() not in ("myself", "jason vallery", "jason"):
                    sender = p
                    break
        first_name = sender.split()[0] if sender != "there" else "there"
        body_parts.append(f"Hi {first_name},")
        body_parts.append("")
        
        if reply_context:
            body_parts.append("Thank you for your email. Here's my response:")
            body_parts.append("")
            for point in reply_context.split(". "):
                if point.strip():
                    body_parts.append(f"- {point.strip()}")
            body_parts.append("")
        
        if questions:
            body_parts.append("To answer your questions:")
            for q in questions[:3]:
                body_parts.append(f"- {q}: [TODO: Add answer]")
            body_parts.append("")
        
        if commitments:
            body_parts.append("I'll follow up on:")
            for c in commitments[:3]:
                body_parts.append(f"- {c}")
            body_parts.append("")
        
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
        self._append_task_to_inbox(task_line)
        
        if self.verbose:
            print(f"  Added reminder to TASKS_INBOX.md")
        
        return tasks_inbox
    
    def emit_tasks(self, extraction: UnifiedExtraction) -> list[str]:
        """Emit all tasks from extraction to TASKS_INBOX.md.
        
        Formats tasks with Obsidian Tasks plugin syntax:
        - [?] Task text @Owner 📅 YYYY-MM-DD 🔺 #task #proposed #auto
        
        Priority markers: 🔺 highest → ⏫ high → 🔼 medium → 🔽 low → ⏬ lowest
        
        Args:
            extraction: UnifiedExtraction with tasks
        
        Returns:
            List of task lines emitted
        """
        if not extraction.tasks:
            return []
        
        # Priority emoji mapping
        priority_emoji = {
            "highest": "🔺",
            "high": "⏫",
            "medium": "🔼",
            "low": "🔽",
            "lowest": "⏬",
        }
        
        task_lines = []
        
        for task in extraction.tasks:
            # Build task line with Obsidian Tasks format
            parts = [f"- [?] {task.text}"]
            
            # Add owner if specified (not myself)
            if task.owner and task.owner.lower() not in ["myself", "me", "i"]:
                parts.append(f"@{task.owner}")
            
            # Add due date if specified
            if task.due:
                parts.append(f"📅 {task.due}")
            
            # Add priority marker
            priority = task.priority.lower() if task.priority else "medium"
            if priority in priority_emoji:
                parts.append(priority_emoji[priority])
            
            # Add tags
            parts.append("#task #proposed #auto")
            
            task_line = " ".join(parts) + "\n"
            task_lines.append(task_line)
            
            if not self.dry_run:
                self._append_task_to_inbox(task_line)
            elif self.verbose:
                print(f"  [DRY RUN] Would emit task: {task_line.strip()}")
        
        if self.verbose and not self.dry_run:
            print(f"  Emitted {len(task_lines)} tasks to TASKS_INBOX.md")
        
        return task_lines
    
    def _append_task_to_inbox(self, task_line: str):
        """Append a task line to TASKS_INBOX.md.
        
        Creates the file with proper structure if it doesn't exist.
        """
        tasks_inbox = self.vault_root / "TASKS_INBOX.md"
        
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
