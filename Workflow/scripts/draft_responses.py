#!/usr/bin/env python3
"""
Email Response Draft Generator with Vault Context

Generates AI-drafted responses using a 3-step process:

1. EXTRACT - Analyze email for topics, people, questions, action items
2. SEARCH - Find relevant notes in vault (people, projects, tasks, history)
3. GENERATE - Draft response using email + vault context

This ensures responses are grounded in existing knowledge and relationships.

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
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, get_model_config, vault_root, workflow_root


console = Console()


def load_persona() -> dict:
    """Load the communication persona from profiles/jason_persona.yaml."""
    persona_path = workflow_root() / "profiles" / "jason_persona.yaml"
    if persona_path.exists():
        with open(persona_path) as f:
            return yaml.safe_load(f)
    return {}


def build_persona_prompt(persona: dict) -> str:
    """Build a prompt section from the persona configuration."""
    if not persona:
        return ""
    
    identity = persona.get("identity", {})
    style = persona.get("style", {})
    patterns = persona.get("patterns", {})
    actions = persona.get("actions", {})
    avoid = persona.get("avoid", [])
    phrases = persona.get("phrases", {})
    
    prompt_parts = []
    
    # Identity
    prompt_parts.append(f"""## YOUR IDENTITY
You are {identity.get('name', 'Jason Vallery')}, {identity.get('role', 'VP of Product Management for Cloud')} at {identity.get('company', 'VAST Data')}.
Scope: {identity.get('scope', 'Cloud products and enterprise storage solutions')}""")
    
    # Communication Style
    if style.get("tone"):
        prompt_parts.append(f"""
## YOUR COMMUNICATION STYLE
Tone:
{chr(10).join('- ' + t for t in style['tone'])}""")
    
    if style.get("principles"):
        prompt_parts.append(f"""
Core Principles:
{chr(10).join('- ' + p for p in style['principles'])}""")
    
    # Impact-Driven Patterns
    prompt_parts.append("""
## IMPACT-DRIVEN COMMUNICATION
You drive for IMPACT in every email. You don't just respond - you ADVANCE the conversation.""")
    
    if patterns.get("requests"):
        prompt_parts.append(f"""
When responding to requests:
{chr(10).join('- ' + r for r in patterns['requests'])}""")
    
    if patterns.get("delegation"):
        prompt_parts.append(f"""
When delegating or making asks:
{chr(10).join('- ' + d for d in patterns['delegation'])}""")
    
    if patterns.get("follow_ups"):
        prompt_parts.append(f"""
When following up:
{chr(10).join('- ' + f for f in patterns['follow_ups'])}""")
    
    # Action Framework
    if actions.get("every_response"):
        prompt_parts.append(f"""
## BEFORE SENDING, ASK YOURSELF:
{chr(10).join('- ' + a for a in actions['every_response'])}""")
    
    if actions.get("proactive_offers"):
        prompt_parts.append(f"""
PROACTIVE VALUE-ADDS to consider:
{chr(10).join('- ' + p for p in actions['proactive_offers'])}""")
    
    if actions.get("delegation_phrases"):
        prompt_parts.append(f"""
Natural delegation phrases you use:
{chr(10).join('- "' + p + '"' for p in actions['delegation_phrases'][:5])}""")
    
    # Anti-patterns
    if avoid:
        prompt_parts.append(f"""
## AVOID THESE PATTERNS:
{chr(10).join('- ' + a for a in avoid)}""")
    
    # Signature phrases
    if phrases.get("action_oriented"):
        prompt_parts.append(f"""
## YOUR SIGNATURE PHRASES:
{chr(10).join('- "' + p + '"' for p in phrases['action_oriented'][:5])}""")
    
    return "\n".join(prompt_parts)


# =============================================================================
# STEP 1: EXTRACT - Analyze email for context
# =============================================================================

def extract_email_context(email_content: str, metadata: dict, client) -> dict:
    """
    Step 1: Extract structured context from the email.
    
    Returns dict with:
    - topics: List of topics/subjects being discussed
    - people: List of people mentioned or involved
    - companies: List of companies/organizations mentioned
    - questions: Specific questions being asked
    - action_items: Requested actions or commitments
    - urgency: low/medium/high
    - summary: Brief summary of what the email is about
    """
    
    model_config = get_model_config("extraction")
    
    system_prompt = """You are analyzing an email to extract structured context for drafting a response.

Extract the following as JSON:
{
    "topics": ["list of main topics/subjects discussed"],
    "people": ["list of people mentioned by name"],
    "companies": ["list of companies/organizations mentioned"],
    "questions": ["specific questions being asked that need answers"],
    "action_items": ["requested actions or commitments"],
    "urgency": "low|medium|high",
    "summary": "1-2 sentence summary of what this email needs"
}

Be specific - extract actual names, companies, and concrete topics.
Return ONLY valid JSON, no markdown fences."""

    user_prompt = f"""Analyze this email:

FROM: {metadata.get('sender', 'Unknown')} <{metadata.get('sender_email', '')}>
SUBJECT: {metadata.get('subject', '')}

{email_content[:6000]}"""

    try:
        response = client.chat.completions.create(
            model=model_config.get("model", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
        )
        
        result = response.choices[0].message.content.strip()
        
        # Parse JSON
        if result.startswith("```"):
            result = re.sub(r'^```\w*\n?', '', result)
            result = re.sub(r'\n?```$', '', result)
        
        return json.loads(result)
    
    except json.JSONDecodeError as e:
        console.print(f"[yellow]JSON parse error in extraction: {e}[/yellow]")
        return {
            "topics": [],
            "people": [metadata.get("sender", "")],
            "companies": [],
            "questions": [],
            "action_items": [],
            "urgency": "medium",
            "summary": metadata.get("subject", "Email requiring response")
        }
    except Exception as e:
        console.print(f"[red]Extraction failed: {e}[/red]")
        return {
            "topics": [],
            "people": [metadata.get("sender", "")],
            "companies": [],
            "questions": [],
            "action_items": [],
            "urgency": "medium",
            "summary": metadata.get("subject", "Email requiring response")
        }


# =============================================================================
# STEP 2: SEARCH - Find relevant vault context
# =============================================================================

def search_vault_context(extracted: dict, max_results: int = 10) -> dict:
    """
    Step 2: Search the vault for relevant notes based on extracted context.
    
    Searches for:
    - People READMEs and recent notes
    - Customer/Partner READMEs
    - Project READMEs
    - Related open tasks
    
    Returns dict with discovered context organized by type.
    """
    
    vault = vault_root()
    context = {
        "people": [],
        "customers": [],
        "projects": [],
        "tasks": [],
        "recent_notes": []
    }
    
    # Normalize search terms
    people_names = [p.lower().strip() for p in extracted.get("people", []) if p]
    company_names = [c.lower().strip() for c in extracted.get("companies", []) if c]
    topics = [t.lower().strip() for t in extracted.get("topics", []) if t]
    
    # Search People
    people_dir = vault / "VAST" / "People"
    if people_dir.exists():
        for person_folder in people_dir.iterdir():
            if not person_folder.is_dir():
                continue
            person_name = person_folder.name.lower()
            
            # Check if this person matches any extracted names
            if any(name in person_name or person_name in name for name in people_names):
                readme = person_folder / "README.md"
                if readme.exists():
                    content = readme.read_text()
                    # Extract key sections
                    context["people"].append({
                        "name": person_folder.name,
                        "path": str(readme.relative_to(vault)),
                        "summary": _extract_section(content, "## Profile", 500)
                            or _extract_section(content, "## About", 500)
                            or content[:500],
                        "recent_context": _extract_section(content, "## Recent Context", 800),
                        "key_facts": _extract_section(content, "## Key Facts", 500)
                    })
                    
                    # Also get most recent note
                    notes = sorted([f for f in person_folder.glob("*.md") 
                                  if f.name != "README.md"], 
                                  key=lambda x: x.name, reverse=True)
                    if notes:
                        recent_note = notes[0]
                        context["recent_notes"].append({
                            "path": str(recent_note.relative_to(vault)),
                            "name": recent_note.name,
                            "preview": recent_note.read_text()[:1000]
                        })
    
    # Search Customers and Partners
    customers_dir = vault / "VAST" / "Customers and Partners"
    if customers_dir.exists():
        for customer_folder in customers_dir.iterdir():
            if not customer_folder.is_dir():
                continue
            customer_name = customer_folder.name.lower()
            
            if any(name in customer_name or customer_name in name for name in company_names):
                readme = customer_folder / "README.md"
                if readme.exists():
                    content = readme.read_text()
                    context["customers"].append({
                        "name": customer_folder.name,
                        "path": str(readme.relative_to(vault)),
                        "summary": _extract_section(content, "## Overview", 500)
                            or _extract_section(content, "## About", 500)
                            or content[:500],
                        "key_contacts": _extract_section(content, "## Key Contacts", 500),
                        "recent_context": _extract_section(content, "## Recent Context", 800)
                    })
    
    # Search Projects
    projects_dir = vault / "VAST" / "Projects"
    if projects_dir.exists():
        for project_folder in projects_dir.iterdir():
            if not project_folder.is_dir():
                continue
            project_name = project_folder.name.lower()
            
            # Match projects by topic or company name
            if any(topic in project_name or project_name in topic for topic in topics + company_names):
                readme = project_folder / "README.md"
                if readme.exists():
                    content = readme.read_text()
                    context["projects"].append({
                        "name": project_folder.name,
                        "path": str(readme.relative_to(vault)),
                        "summary": _extract_section(content, "## Overview", 500)
                            or _extract_section(content, "## About", 500)
                            or content[:500],
                        "status": _extract_section(content, "## Status", 300),
                        "open_tasks": _extract_section(content, "## Open Tasks", 500)
                    })
    
    # Search for related open tasks across vault
    # Look for tasks mentioning extracted people or topics
    all_search_terms = people_names + company_names + topics
    if all_search_terms:
        context["tasks"] = _search_open_tasks(vault, all_search_terms, max_tasks=5)
    
    return context


def _extract_section(content: str, heading: str, max_chars: int) -> Optional[str]:
    """Extract content under a specific heading."""
    
    lines = content.split('\n')
    heading_level = heading.count('#')
    heading_text = heading.lstrip('# ').strip().lower()
    
    in_section = False
    section_lines = []
    
    for line in lines:
        if line.strip().lower().startswith('#'):
            # Check if this is our heading
            if heading_text in line.lower():
                in_section = True
                continue
            # Check if we hit another heading of same or higher level
            elif in_section:
                current_level = len(line) - len(line.lstrip('#'))
                if current_level <= heading_level:
                    break
        
        if in_section:
            section_lines.append(line)
    
    if section_lines:
        result = '\n'.join(section_lines).strip()
        return result[:max_chars] if len(result) > max_chars else result
    
    return None


def _search_open_tasks(vault: Path, search_terms: List[str], max_tasks: int = 5) -> List[dict]:
    """Search for open tasks mentioning search terms."""
    
    tasks = []
    
    # Look in key locations for tasks
    search_paths = [
        vault / "VAST" / "People",
        vault / "VAST" / "Customers and Partners", 
        vault / "VAST" / "Projects"
    ]
    
    for search_path in search_paths:
        if not search_path.exists():
            continue
            
        for md_file in search_path.rglob("*.md"):
            try:
                content = md_file.read_text()
                lines = content.split('\n')
                
                for i, line in enumerate(lines):
                    # Find open task lines
                    if line.strip().startswith('- [ ]'):
                        task_text = line.strip()
                        task_lower = task_text.lower()
                        
                        # Check if task mentions any search term
                        if any(term in task_lower for term in search_terms):
                            tasks.append({
                                "file": str(md_file.relative_to(vault)),
                                "task": task_text,
                            })
                            
                            if len(tasks) >= max_tasks:
                                return tasks
            except Exception:
                continue
    
    return tasks


def format_vault_context(context: dict) -> str:
    """Format discovered vault context for the LLM prompt."""
    
    sections = []
    
    if context.get("people"):
        sections.append("## People Context")
        for person in context["people"][:3]:  # Limit to top 3
            sections.append(f"\n### {person['name']}")
            if person.get("summary"):
                sections.append(person["summary"])
            if person.get("recent_context"):
                sections.append(f"\n**Recent interactions:**\n{person['recent_context']}")
            if person.get("key_facts"):
                sections.append(f"\n**Key facts:**\n{person['key_facts']}")
    
    if context.get("customers"):
        sections.append("\n## Customer/Partner Context")
        for customer in context["customers"][:3]:
            sections.append(f"\n### {customer['name']}")
            if customer.get("summary"):
                sections.append(customer["summary"])
            if customer.get("key_contacts"):
                sections.append(f"\n**Key contacts:**\n{customer['key_contacts']}")
            if customer.get("recent_context"):
                sections.append(f"\n**Recent context:**\n{customer['recent_context']}")
    
    if context.get("projects"):
        sections.append("\n## Related Projects")
        for project in context["projects"][:3]:
            sections.append(f"\n### {project['name']}")
            if project.get("summary"):
                sections.append(project["summary"])
            if project.get("status"):
                sections.append(f"\n**Status:**\n{project['status']}")
    
    if context.get("tasks"):
        sections.append("\n## Related Open Tasks")
        for task in context["tasks"]:
            sections.append(f"- {task['task']} (from {task['file']})")
    
    if context.get("recent_notes"):
        sections.append("\n## Recent Related Notes")
        for note in context["recent_notes"][:2]:
            sections.append(f"\n### {note['name']}")
            sections.append(note["preview"][:500])
    
    return '\n'.join(sections) if sections else ""


def get_openai_client():
    """Get configured OpenAI client with logging instrumentation."""
    from utils.ai_client import get_openai_client as get_instrumented_client
    return get_instrumented_client("draft_responses")


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
    extracted_context: Optional[dict] = None,
    vault_context: Optional[str] = None
) -> str:
    """
    Step 3: Generate a draft response using email + vault context + persona.
    
    This combines:
    - The original email content
    - Extracted email analysis (topics, questions, people)
    - Discovered vault context (people history, project status, open tasks)
    - Communication persona (tone, style, impact-driven patterns)
    """
    
    model_config = get_model_config("extraction")  # Reuse extraction model config
    
    # Load persona for impact-driven communication
    persona = load_persona()
    persona_prompt = build_persona_prompt(persona)
    
    system_prompt = f"""You are drafting an email reply. Your goal is to write an IMPACT-DRIVEN response that advances the conversation, not just answers it.

{persona_prompt}

## CONTEXT AVAILABLE
1. The original email requiring a response
2. Analysis of the email (topics, questions, people involved)  
3. Relevant context from notes (relationship history, project status, open tasks)

## YOUR MISSION
Write a response that:
1. **ANSWERS** - Address questions/requests directly and completely
2. **ADVANCES** - Propose specific next steps, don't leave things hanging
3. **ASKS** - Make proactive requests of others when appropriate (delegate, request info, set deadlines)
4. **ADDS VALUE** - Offer introductions, share relevant resources, connect dots they might miss

## STRUCTURE YOUR RESPONSE
- **Opening**: Brief acknowledgment, show you understood the context
- **Core Response**: Answer their questions, address their needs
- **Proactive Ask**: What do you need from them? What should they do next?
- **Offer/Next Step**: What will YOU do? When will you follow up?
- **Close**: Warm, action-oriented sign-off

## MAKE ASKS NATURALLY
When making requests or delegating, be direct but collegial:
- "Could you take the lead on X? I can support with Y."
- "I'd like to get this wrapped up by [date] - is that doable?"
- "If you can get me X, I can turn around Y by Z."
- "Let me know what you need from me to move forward."
- "I'm looping in [person] who can help with [specific thing]."

## FORMATTING
- Keep it concise (2-4 paragraphs)
- Use specific dates/times, not "soon" or "when you can"
- Sign off with "Best,\\nJason" or "Thanks,\\nJason"
- Return ONLY the email body (no subject line or headers)

## AVOID
- Passive voice that obscures who's doing what
- Vague commitments without timelines
- Over-apologizing or excessive hedging
- Ending with "let me know your thoughts" when you should propose a path
- Generic responses that could apply to anyone"""

    user_prompt = f"""Draft an IMPACT-DRIVEN response to this email:

FROM: {metadata.get('sender', 'Unknown')} <{metadata.get('sender_email', '')}>
SUBJECT: {metadata.get('subject', '')}
DATE: {metadata.get('date', '')}

EMAIL CONTENT:
{email_content[:4000]}
"""

    if extracted_context:
        user_prompt += f"""

--- EMAIL ANALYSIS ---
Topics: {', '.join(extracted_context.get('topics', []))}
Questions to answer: {json.dumps(extracted_context.get('questions', []))}
Action items requested: {json.dumps(extracted_context.get('action_items', []))}
People involved: {', '.join(extracted_context.get('people', []))}
Companies: {', '.join(extracted_context.get('companies', []))}
Urgency: {extracted_context.get('urgency', 'medium')}
Summary: {extracted_context.get('summary', '')}
"""

    if vault_context:
        user_prompt += f"""

--- RELEVANT CONTEXT FROM MY NOTES ---
Use this to personalize your response and reference relevant history:
{vault_context}
"""

    # Add specific guidance for this email
    user_prompt += """

--- YOUR TASK ---
1. Write a response that ANSWERS their questions completely
2. Include at least ONE proactive ask or clear next step for them
3. State what YOU will do and by when (if applicable)
4. Keep it concise but impactful - quality over length
"""

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
    reason: str,
    extracted_context: Optional[dict] = None,
    vault_context_summary: Optional[str] = None
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
    
    # Build context summary for frontmatter
    topics = extracted_context.get("topics", []) if extracted_context else []
    people = extracted_context.get("people", []) if extracted_context else []
    
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
topics: {json.dumps(topics)}
people_mentioned: {json.dumps(people)}
vault_context_used: {bool(vault_context_summary)}
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

    # Add vault context summary if we used it
    if vault_context_summary:
        content += f"""
---

## Vault Context Used

<details>
<summary>Context from notes that informed this draft</summary>

{vault_context_summary[:2000]}

</details>
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
@click.option("--no-context", is_flag=True, help="Skip vault context search (faster, less informed)")
def main(single_file: Optional[str], dry_run: bool, verbose: bool, force: bool, no_context: bool):
    """Generate draft email responses using 3-step context-aware process."""
    
    console.print(Panel.fit(
        "[bold blue]Email Response Draft Generator[/bold blue]\n"
        "[dim]3-step process: Extract → Search → Generate[/dim]",
        border_style="blue"
    ))
    
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
    
    # Generate drafts using 3-step process
    client = get_openai_client()
    drafts_created = []
    
    console.print("\n[bold]Generating context-aware drafts...[/bold]")
    
    for email_path, metadata, reason in needs_draft:
        content = email_path.read_text()
        subject = metadata.get('subject', 'email')[:50]
        
        console.print(f"\n[cyan]━━━ {subject} ━━━[/cyan]")
        
        # STEP 1: Extract email context
        console.print("  [dim]Step 1: Extracting email context...[/dim]")
        extracted = extract_email_context(content, metadata, client)
        
        if verbose:
            table = Table(show_header=False, box=None, padding=(0, 1))
            table.add_column("Key", style="dim")
            table.add_column("Value")
            table.add_row("Topics", ", ".join(extracted.get("topics", [])[:3]))
            table.add_row("People", ", ".join(extracted.get("people", [])[:3]))
            table.add_row("Questions", str(len(extracted.get("questions", []))))
            table.add_row("Urgency", extracted.get("urgency", "medium"))
            console.print(table)
        
        # STEP 2: Search vault for context
        vault_context_str = ""
        if not no_context:
            console.print("  [dim]Step 2: Searching vault for context...[/dim]")
            vault_context = search_vault_context(extracted)
            vault_context_str = format_vault_context(vault_context)
            
            # Count what we found
            people_found = len(vault_context.get("people", []))
            customers_found = len(vault_context.get("customers", []))
            projects_found = len(vault_context.get("projects", []))
            tasks_found = len(vault_context.get("tasks", []))
            
            if verbose or (people_found + customers_found + projects_found > 0):
                console.print(f"    Found: {people_found} people, {customers_found} customers, "
                            f"{projects_found} projects, {tasks_found} tasks")
        else:
            console.print("  [dim]Step 2: Skipped (--no-context)[/dim]")
        
        # STEP 3: Generate draft with all context
        console.print("  [dim]Step 3: Generating draft response...[/dim]")
        draft_body = generate_draft_response(
            content, 
            metadata, 
            client,
            extracted_context=extracted,
            vault_context=vault_context_str if vault_context_str else None
        )
        
        output_path = save_draft(
            email_path, 
            metadata, 
            draft_body, 
            reason,
            extracted_context=extracted,
            vault_context_summary=vault_context_str if vault_context_str else None
        )
        drafts_created.append(output_path)
        
        console.print(f"  [green]✓ Saved: {output_path.name}[/green]")
        
        if verbose:
            console.print(Panel(
                draft_body[:500] + "..." if len(draft_body) > 500 else draft_body,
                title="Draft Preview", 
                border_style="dim"
            ))
    
    console.print(f"\n[bold green]━━━ Created {len(drafts_created)} context-aware draft(s) in Outbox/ ━━━[/bold green]")


if __name__ == "__main__":
    main()
