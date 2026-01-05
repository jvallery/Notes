#!/usr/bin/env python3
"""
Email Response Draft Generator

Generates AI-drafted responses for emails that need replies.

When to generate a draft:
- Email has a question directed at the user
- Email requests action or information
- Email is from an important contact (customer, partner)
- Email thread is awaiting response

What NOT to draft:
- Newsletters / automated notifications
- FYI/informational emails with no call to action
- Already-replied threads (user is last sender)
- Spam / marketing emails

Usage:
    python scripts/draft_responses.py                # Generate drafts for pending emails
    python scripts/draft_responses.py --file X.md   # Draft response for specific email
    python scripts/draft_responses.py --dry-run     # Show what would be drafted
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, get_model_config, vault_root, workflow_root


console = Console()


def get_openai_client():
    """Get configured OpenAI client."""
    import os
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(workflow_root() / ".env")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment")

    return OpenAI(api_key=api_key)


def parse_email_metadata(content: str) -> dict:
    """Extract metadata from email file content."""
    
    metadata = {
        "subject": "",
        "sender": "",
        "sender_email": "",
        "date": "",
        "message_count": 1,
        "is_reply": False,
        "has_question": False,
        "has_action_request": False,
        "latest_message": "",
    }
    
    lines = content.split('\n')
    
    # First line is subject (# Subject)
    if lines and lines[0].startswith('# '):
        metadata["subject"] = lines[0][2:].strip()
        metadata["is_reply"] = metadata["subject"].lower().startswith(('re:', 'fwd:'))
    
    # Look for Messages count
    msg_match = re.search(r'Messages:\s*(\d+)', content)
    if msg_match:
        metadata["message_count"] = int(msg_match.group(1))
    
    # Find the first (most recent) message sender
    sender_match = re.search(r'##.*?—\s*(.+?)\s*<(.+?)>', content)
    if sender_match:
        metadata["sender"] = sender_match.group(1).strip()
        metadata["sender_email"] = sender_match.group(2).strip()
    
    # Find date of first message
    date_match = re.search(r'##\s*(\d{4}-\d{2}-\d{2})', content)
    if date_match:
        metadata["date"] = date_match.group(1)
    
    # Extract latest message content (between first ## and second ## or end)
    msg_sections = re.split(r'##\s+\d{4}-\d{2}-\d{2}', content)
    if len(msg_sections) > 1:
        latest = msg_sections[1].split('---')[0] if '---' in msg_sections[1] else msg_sections[1]
        metadata["latest_message"] = latest[:2000]  # Limit size
    
    # Simple heuristics for response detection
    latest_lower = metadata["latest_message"].lower()
    metadata["has_question"] = '?' in metadata["latest_message"]
    metadata["has_action_request"] = any(phrase in latest_lower for phrase in [
        "please", "could you", "can you", "would you", "let me know",
        "get back to me", "follow up", "need your", "waiting for",
        "when can", "respond", "reply", "urgent", "asap"
    ])
    
    return metadata


def should_draft_response(metadata: dict, content: str) -> tuple[bool, str]:
    """Determine if this email needs a draft response.
    
    Returns: (should_draft, reason)
    """
    
    subject_lower = metadata.get("subject", "").lower()
    sender_email = metadata.get("sender_email", "").lower()
    content_lower = content.lower()
    
    # Skip automated/notification emails
    automated_patterns = [
        "noreply@", "no-reply@", "notifications@", "alerts@", 
        "automated@", "system@", "mailer-daemon", "unsubscribe",
        "paddle.com", "expressscripts", "pharmacy",
    ]
    if any(p in sender_email for p in automated_patterns):
        return False, "Automated notification"
    
    # Skip if I'm the sender (already replied)
    my_email = "jason.vallery@vastdata.com"
    if my_email in sender_email:
        return False, "Already responded"
    
    # Skip calendar/meeting notifications
    calendar_patterns = [
        "accepted:", "declined:", "tentative:", 
        "invitation:", "meeting request", "calendar event",
        "just scheduled"
    ]
    if any(p in subject_lower for p in calendar_patterns):
        return False, "Calendar notification"
    
    # Skip order/shipping confirmations
    order_patterns = [
        "order confirmation", "your order", "thanks for your order",
        "shipping", "tracking", "delivery", "invoice", "receipt"
    ]
    if any(p in subject_lower for p in order_patterns):
        return False, "Order/shipping notification"
    
    # Skip newsletters / marketing
    marketing_keywords = [
        "newsletter", "unsubscribe", "view in browser", "privacy policy",
        "sent you this email", "update your preferences"
    ]
    if any(kw in content_lower for kw in marketing_keywords):
        return False, "Marketing/newsletter"
    
    # Skip internal announcements/FYI (no action needed)
    fyi_patterns = [
        "fyi", "for your information", "heads up", "quick recap",
        "update:", "announcement", "team update"
    ]
    if any(p in subject_lower for p in fyi_patterns) and not metadata["has_question"]:
        return False, "FYI/informational"
    
    # Draft if there's a direct question
    if metadata["has_question"]:
        return True, "Contains question"
    
    # Draft if there's an action request directed at user
    action_phrases = [
        "please let me know", "could you", "can you", "would you",
        "waiting for your", "need your input", "get back to me",
        "respond", "reply", "your thoughts", "what do you think"
    ]
    if any(phrase in content_lower for phrase in action_phrases):
        return True, "Action requested"
    
    # Draft if from important domain (customers, partners) AND seems substantive
    important_domains = [
        "microsoft.com", "google.com", "nvidia.com", "openai.com",
        "oracle.com", "amazon.com", "aws.amazon.com"
    ]
    if any(d in sender_email for d in important_domains):
        # Only draft if it seems like it needs a reply
        if metadata["message_count"] >= 2 or "@jason" in content_lower:
            return True, "Important contact - substantive"
    
    return False, "No response needed"


def generate_draft_response(
    email_content: str, 
    metadata: dict,
    client,
    context: Optional[str] = None
) -> str:
    """Generate a draft response using AI."""
    
    model_config = get_model_config("extraction")  # Reuse extraction model config
    
    system_prompt = """You are drafting an email reply for Jason Vallery, VP of Product Management for Cloud at VAST Data.

Your tone should be:
- Professional but warm
- Concise and direct
- Helpful and solution-oriented

Guidelines:
- Address the sender's questions/requests directly
- Offer specific next steps or information
- Keep responses focused (2-4 paragraphs typically)
- Sign off with "Best,\\nJason" or similar

Do NOT:
- Include the original email (they have it)
- Use excessive formality or jargon
- Make commitments you can't verify (use "I'll check" or "I believe")
- Include [placeholder] style brackets - write complete text

Return ONLY the email body text (no subject, headers, etc.)."""

    user_prompt = f"""Draft a response to this email:

FROM: {metadata.get('sender', 'Unknown')} <{metadata.get('sender_email', '')}>
SUBJECT: {metadata.get('subject', '')}
DATE: {metadata.get('date', '')}

EMAIL CONTENT:
{email_content[:4000]}
"""

    if context:
        user_prompt += f"\n\nADDITIONAL CONTEXT:\n{context}"

    try:
        response = client.chat.completions.create(
            model=model_config.get("model", "gpt-4o"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,  # Slightly more creative for email writing
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        console.print(f"[red]Draft generation failed: {e}[/red]")
        return f"[Error generating draft: {e}]"


def save_draft(
    original_file: Path,
    metadata: dict,
    draft_body: str,
    reason: str
) -> Path:
    """Save draft response to Outbox folder."""
    
    outbox = vault_root() / "Outbox"
    outbox.mkdir(exist_ok=True)
    
    # Generate filename
    today = datetime.now().strftime("%Y-%m-%d")
    subject_slug = re.sub(r'[^\w\s-]', '', metadata.get('subject', 'email'))
    subject_slug = re.sub(r'\s+', '-', subject_slug)[:40]
    
    filename = f"{today}_Reply-To_{subject_slug}.md"
    output_path = outbox / filename
    
    # Avoid overwriting
    counter = 1
    while output_path.exists():
        filename = f"{today}_Reply-To_{subject_slug}_{counter}.md"
        output_path = outbox / filename
        counter += 1
    
    # Build draft document
    content = f"""---
status: draft
type: email-draft
original: "{original_file.name}"
created: "{datetime.now().isoformat()}"
to: "{metadata.get('sender_email', '')}"
to_name: "{metadata.get('sender', '')}"
subject: "Re: {metadata.get('subject', '')}"
reason: "{reason}"
---

# Draft Reply: {metadata.get('subject', '')}

**To:** {metadata.get('sender', '')} <{metadata.get('sender_email', '')}>
**Subject:** Re: {metadata.get('subject', '')}
**Context:** {reason}

---

{draft_body}

---

## Original Email

> From: {metadata.get('sender', '')} <{metadata.get('sender_email', '')}>
> Date: {metadata.get('date', '')}

"""
    
    output_path.write_text(content)
    return output_path


def find_emails_needing_response() -> list[Path]:
    """Find emails in Inbox/Email that may need responses."""
    
    email_dir = vault_root() / "Inbox" / "Email"
    if not email_dir.exists():
        return []
    
    return list(email_dir.glob("*.md"))


@click.command()
@click.option(
    "--file", "-f", "single_file",
    type=click.Path(exists=True),
    help="Process a single email file"
)
@click.option("--dry-run", is_flag=True, help="Show what would be drafted without generating")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed analysis")
@click.option("--force", is_flag=True, help="Draft even for emails that don't seem to need response")
def main(single_file: Optional[str], dry_run: bool, verbose: bool, force: bool):
    """Generate draft email responses for Inbox emails."""
    
    console.print("[bold blue]Email Response Draft Generator[/bold blue]")
    console.print("=" * 50)
    
    # Find emails to process
    if single_file:
        emails = [Path(single_file)]
    else:
        emails = find_emails_needing_response()
    
    if not emails:
        console.print("[yellow]No emails found to process.[/yellow]")
        return
    
    console.print(f"Found [bold]{len(emails)}[/bold] emails to analyze")
    
    # Analyze and generate drafts
    needs_draft = []
    skipped = []
    
    for email_path in emails:
        content = email_path.read_text()
        metadata = parse_email_metadata(content)
        should_draft, reason = should_draft_response(metadata, content)
        
        if should_draft or force:
            needs_draft.append((email_path, metadata, reason if should_draft else "Forced"))
        else:
            skipped.append((email_path, reason))
    
    console.print(f"\n[bold]Analysis Results:[/bold]")
    console.print(f"  Needs response: {len(needs_draft)}")
    console.print(f"  Skipped: {len(skipped)}")
    
    if verbose and skipped:
        console.print("\n[dim]Skipped emails:[/dim]")
        for path, reason in skipped[:10]:
            console.print(f"  [dim]{path.name[:40]}... - {reason}[/dim]")
        if len(skipped) > 10:
            console.print(f"  [dim]...and {len(skipped) - 10} more[/dim]")
    
    if not needs_draft:
        console.print("\n[green]No emails need responses![/green]")
        return
    
    if dry_run:
        console.print("\n[yellow]Would generate drafts for:[/yellow]")
        for path, metadata, reason in needs_draft:
            console.print(f"  • {metadata.get('subject', path.name)[:50]}")
            console.print(f"    From: {metadata.get('sender', 'Unknown')}")
            console.print(f"    Reason: {reason}")
        return
    
    # Generate drafts
    client = get_openai_client()
    drafts_created = []
    
    console.print("\n[bold]Generating drafts...[/bold]")
    
    for email_path, metadata, reason in needs_draft:
        content = email_path.read_text()
        
        console.print(f"\n[cyan]Drafting reply to: {metadata.get('subject', 'email')[:50]}[/cyan]")
        
        draft_body = generate_draft_response(content, metadata, client)
        
        output_path = save_draft(email_path, metadata, draft_body, reason)
        drafts_created.append(output_path)
        
        console.print(f"  [green]→ {output_path.name}[/green]")
        
        if verbose:
            console.print(Panel(draft_body[:500] + "..." if len(draft_body) > 500 else draft_body, 
                               title="Draft Preview", border_style="dim"))
    
    console.print(f"\n[bold green]Created {len(drafts_created)} draft(s) in Outbox/[/bold green]")


if __name__ == "__main__":
    main()
