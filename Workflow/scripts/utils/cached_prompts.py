#!/usr/bin/env python3
"""
Cached Prompt System: Optimize OpenAI API calls with prompt caching.

This module provides:
1. A cached glossary of people, projects, and customers
2. Jason's persona for consistent voice
3. Optimized prompt structure for cache hits

OpenAI Prompt Caching Requirements:
- Prompts must be 1024+ tokens for caching
- Static content must be at the BEGINNING of the prompt
- Dynamic/user-specific content at the END
- Cache is automatic, no explicit management needed
- Cache persists 5-10 min (in-memory) or up to 24h (extended)

Usage:
    from utils.cached_prompts import get_system_prompt, get_glossary_context
    
    # For email drafting (includes persona + glossary)
    system_prompt = get_system_prompt(task="email_draft")
    
    # For extraction (glossary only, no persona)  
    system_prompt = get_system_prompt(task="extraction")
    
    # Just get glossary context to append
    glossary = get_glossary_context()
    
    # Use with AI client - static content first, then user message
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},  # Cached prefix
            {"role": "user", "content": user_specific_content}  # Dynamic
        ],
        store=False,
        prompt_cache_retention="24h"  # Extended caching
    )
"""

import json
import yaml
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any
from .config import load_config

# Paths - __file__ is utils/cached_prompts.py
# parent = utils/, parent.parent = scripts/, parent.parent.parent = Workflow/
WORKFLOW_DIR = Path(__file__).parent.parent.parent
CONFIG = load_config()
VAULT_ROOT = Path(CONFIG.get("paths", {}).get("vault_root", WORKFLOW_DIR.parent))
CACHE_DIR = WORKFLOW_DIR / "_cache"
GLOSSARY_CACHE = CACHE_DIR / "glossary.json"
PERSONA_PATH = WORKFLOW_DIR / "profiles" / "jason_persona.yaml"
WORK_PATHS = CONFIG.get("paths", {}).get("work", {})
PEOPLE_MANIFEST = Path(WORK_PATHS.get("people", VAULT_ROOT / "VAST" / "People")) / "_MANIFEST.md"
PROJECTS_MANIFEST = Path(WORK_PATHS.get("projects", VAULT_ROOT / "VAST" / "Projects")) / "_MANIFEST.md"
CUSTOMERS_MANIFEST = Path(WORK_PATHS.get("accounts", VAULT_ROOT / "VAST" / "Customers and Partners")) / "_MANIFEST.md"

# Cache settings
_glossary_cache: Optional[Dict[str, Any]] = None
_glossary_cache_time: Optional[datetime] = None
_persona_cache: Optional[str] = None
_persona_cache_time: Optional[datetime] = None
CACHE_TTL = timedelta(minutes=30)  # Refresh in-memory cache every 30 min


def load_glossary() -> Dict[str, Any]:
    """Load glossary from cache file or manifests."""
    global _glossary_cache, _glossary_cache_time
    
    # Check in-memory cache
    if (_glossary_cache is not None and 
        _glossary_cache_time is not None and
        datetime.now() - _glossary_cache_time < CACHE_TTL):
        return _glossary_cache
    
    # Try loading from JSON cache
    if GLOSSARY_CACHE.exists():
        try:
            data = json.loads(GLOSSARY_CACHE.read_text())
            _glossary_cache = data
            _glossary_cache_time = datetime.now()
            return data
        except json.JSONDecodeError:
            pass
    
    # Fall back to building from manifests
    glossary = build_glossary_from_manifests()
    _glossary_cache = glossary
    _glossary_cache_time = datetime.now()
    return glossary


def parse_manifest_table(content: str) -> list:
    """Parse a markdown table from manifest content."""
    entries = []
    lines = content.split("\n")
    
    in_table = False
    headers = []
    
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            in_table = False
            continue
        
        # Skip separator line
        if line.startswith("|--") or line.startswith("| --"):
            continue
        
        cells = [c.strip() for c in line.split("|")[1:-1]]  # Remove first/last empty
        
        if not in_table:
            # This is the header row
            headers = [h.lower().replace(" ", "_") for h in cells]
            in_table = True
        else:
            # This is a data row
            entry = {}
            for i, val in enumerate(cells):
                if i < len(headers):
                    entry[headers[i]] = val
            if entry:
                entries.append(entry)
    
    return entries


def build_glossary_from_manifests() -> Dict[str, Any]:
    """Build glossary by parsing manifest files directly."""
    glossary = {
        "version": "1.0",
        "generated_at": datetime.now().isoformat(),
        "people": [],
        "projects": [],
        "customers": []
    }
    
    # Parse People manifest
    if PEOPLE_MANIFEST.exists():
        content = PEOPLE_MANIFEST.read_text()
        glossary["people"] = parse_manifest_table(content)
    
    # Parse Projects manifest
    if PROJECTS_MANIFEST.exists():
        content = PROJECTS_MANIFEST.read_text()
        glossary["projects"] = parse_manifest_table(content)
    
    # Parse Customers manifest
    if CUSTOMERS_MANIFEST.exists():
        content = CUSTOMERS_MANIFEST.read_text()
        glossary["customers"] = parse_manifest_table(content)
    
    return glossary


def load_persona() -> str:
    """Load Jason's persona YAML."""
    global _persona_cache, _persona_cache_time
    
    # Check in-memory cache
    if (_persona_cache is not None and
        _persona_cache_time is not None and
        datetime.now() - _persona_cache_time < CACHE_TTL):
        return _persona_cache
    
    if not PERSONA_PATH.exists():
        return ""
    
    content = PERSONA_PATH.read_text()
    _persona_cache = content
    _persona_cache_time = datetime.now()
    return content


def format_glossary_as_text(glossary: Dict[str, Any], compact: bool = False) -> str:
    """Format glossary as readable text for prompt inclusion.
    
    Args:
        glossary: The glossary data dict
        compact: If True, use minimal formatting for smaller token count
    """
    lines = []
    
    if not compact:
        lines.extend([
            "=== CONTEXT: MY PROFESSIONAL NETWORK ===",
            "",
            "## People I Work With",
            ""
        ])
    else:
        lines.append("PEOPLE:")
    
    for p in glossary.get("people", [])[:80]:  # Limit for token budget
        name = p.get("name", "")
        role = p.get("role", "")
        company = p.get("company", "")
        email = p.get("email", "")
        
        if compact:
            parts = [name]
            if role or company:
                parts.append(f"({role or ''} @ {company or ''})")
            if email:
                parts.append(f"<{email}>")
            lines.append(" ".join(parts))
        else:
            if role and company:
                lines.append(f"- **{name}**: {role} at {company}")
            elif role:
                lines.append(f"- **{name}**: {role}")
            elif company:
                lines.append(f"- **{name}**: at {company}")
            else:
                lines.append(f"- **{name}**")
            if email:
                lines.append(f"  Email: {email}")
    
    if not compact:
        lines.extend([
            "",
            "## Active Projects",
            ""
        ])
    else:
        lines.append("\nPROJECTS:")
    
    for proj in glossary.get("projects", [])[:40]:  # Limit
        name = proj.get("name", "")
        status = proj.get("status", "active")
        desc = proj.get("description", "")[:80]
        
        if compact:
            lines.append(f"{name} [{status}]")
        else:
            if desc:
                lines.append(f"- **{name}** [{status}]: {desc}")
            else:
                lines.append(f"- **{name}** [{status}]")
    
    if not compact:
        lines.extend([
            "",
            "## Customers & Partners",
            ""
        ])
    else:
        lines.append("\nCUSTOMERS:")
    
    for c in glossary.get("customers", []):
        name = c.get("name", "")
        ctype = c.get("type", "")
        industry = c.get("industry", "")
        stage = c.get("stage", "")
        my_role = c.get("my_role", "")
        last_contact = c.get("last_contact", "")
        
        if compact:
            parts = [name]
            meta_parts = [p for p in [ctype, stage] if p]
            if meta_parts:
                parts.append(f"({', '.join(meta_parts)})")
            if my_role:
                parts.append(f"[{my_role}]")
            lines.append(" ".join(parts))
        else:
            parts = [f"**{name}**"]
            if ctype:
                parts.append(f"({ctype})")
            if stage:
                parts.append(f"[{stage}]")
            if industry:
                parts.append(f"- {industry}")
            if my_role:
                parts.append(f"— my role: {my_role}")
            if last_contact:
                parts.append(f"(last: {last_contact})")
            lines.append("- " + " ".join(parts))
    
    if not compact:
        lines.extend([
            "",
            "=== END CONTEXT ===",
            ""
        ])
    
    return "\n".join(lines)


def format_persona_as_text(persona_yaml: str, include_full: bool = True) -> str:
    """Format persona YAML as prompt instructions.
    
    Args:
        persona_yaml: Raw YAML content
        include_full: If True, include full persona; else just key points
    """
    if not persona_yaml:
        return ""
    
    try:
        persona = yaml.safe_load(persona_yaml)
    except yaml.YAMLError:
        return ""
    
    lines = [
        "=== YOUR IDENTITY ===",
        ""
    ]
    
    # Extract identity
    identity = persona.get("identity", {})
    lines.append(f"You are drafting as **{identity.get('name', 'Jason Vallery')}**.")
    lines.append(f"Role: {identity.get('role', 'VP Product Management, Cloud')}")
    lines.append(f"Company: {identity.get('company', 'VAST Data')}")
    
    if identity.get("scope_summary"):
        lines.append(f"Scope: {identity['scope_summary']}")
    
    # Style guidelines
    style = persona.get("style", {})
    if style.get("voice"):
        lines.extend(["", "## Communication Style"])
        for v in style["voice"]:
            lines.append(f"- {v}")
    
    if style.get("formatting"):
        lines.extend(["", "## Formatting Rules"])
        for f in style["formatting"]:
            lines.append(f"- {f}")
    
    # Guardrails
    guardrails = persona.get("guardrails", {})
    if guardrails.get("brand_safety"):
        lines.extend(["", "## Guardrails"])
        for g in guardrails["brand_safety"]:
            lines.append(f"- {g}")
    
    # Calibration
    calibration = persona.get("calibration", {})
    if calibration:
        lines.extend(["", "## Tone Calibration by Recipient"])
        for rtype, rules in calibration.items():
            if isinstance(rules, dict):
                tone = rules.get("tone", "")
                rule = rules.get("rule", "")
                lines.append(f"- **{rtype}**: {tone}. {rule}")
    
    lines.extend(["", "=== END IDENTITY ===", ""])
    
    return "\n".join(lines)


def get_glossary_context(compact: bool = False) -> str:
    """Get formatted glossary context for prompts.
    
    Returns the glossary formatted as text, suitable for inclusion
    in a system prompt to provide context about people/projects.
    """
    glossary = load_glossary()
    return format_glossary_as_text(glossary, compact=compact)


def get_persona_context(include_full: bool = True) -> str:
    """Get formatted persona context for prompts.
    
    Returns Jason's persona formatted for prompt inclusion.
    """
    persona_yaml = load_persona()
    return format_persona_as_text(persona_yaml, include_full=include_full)


def get_system_prompt(
    task: str = "general",
    include_persona: bool = True,
    include_glossary: bool = True,
    compact_glossary: bool = False,
    additional_instructions: str = ""
) -> str:
    """Build a complete system prompt optimized for caching.
    
    The prompt is structured with static content FIRST (for cache hits)
    and any task-specific content at the end.
    
    Args:
        task: Task type - "email_draft", "extraction", "planning", "general"
        include_persona: Whether to include Jason's persona
        include_glossary: Whether to include people/project glossary
        compact_glossary: Use compact format to reduce tokens
        additional_instructions: Task-specific instructions (added last)
    
    Returns:
        Complete system prompt string
    """
    sections = []
    
    # === STATIC CACHED CONTENT (put first for cache hits) ===
    
    # 1. Persona (if drafting)
    if include_persona and task in ("email_draft", "general"):
        persona_text = get_persona_context()
        if persona_text:
            sections.append(persona_text)
    
    # 2. Glossary (people/projects/customers)
    if include_glossary:
        glossary_text = get_glossary_context(compact=compact_glossary)
        if glossary_text:
            sections.append(glossary_text)
    
    # === TASK-SPECIFIC CONTENT (at end, varies per call) ===
    
    # 3. Task-specific base instructions
    task_instructions = get_task_instructions(task)
    if task_instructions:
        sections.append(task_instructions)
    
    # 4. Additional custom instructions
    if additional_instructions:
        sections.append(additional_instructions)
    
    return "\n\n".join(sections)


def get_task_instructions(task: str) -> str:
    """Get base instructions for a specific task type."""
    
    instructions = {
        "email_draft": """
## Your Task: Draft Email Response

You are drafting an email response as Jason Vallery.
- Read the incoming email carefully
- Apply the persona guidelines above
- Use the people/project context to understand references
- Generate a ready-to-send email draft

Output JSON with:
- "subject": The email subject
- "body": The complete email body
- "internal_notes": Any observations for Jason's review
""",
        
        "extraction": """
## Your Task: Extract Structured Data

Extract structured information from the provided content.
Use the glossary above to:
- Match names to known people (use canonical names)
- Identify referenced projects by their full names
- Link customers/partners to known accounts

Be precise and only extract explicitly stated information.
""",
        
        "planning": """
## Your Task: Generate Change Plan

You are planning updates to a knowledge vault based on extracted content.
Use the glossary to:
- Route content to correct entity folders
- Use exact folder names for people/projects/customers
- Create wikilinks with proper names

Generate a structured ChangePlan with create/patch/link operations.
""",
        
        "general": """
## Your Task

You are an AI assistant helping Jason Vallery.
Use the context above to:
- Understand references to people and projects
- Maintain Jason's communication style
- Provide actionable, direct responses
"""
    }
    
    return instructions.get(task, instructions["general"])


def estimate_prompt_tokens(prompt: str) -> int:
    """Rough estimate of token count (4 chars per token average)."""
    return len(prompt) // 4


def get_cache_status() -> Dict[str, Any]:
    """Get status of cached glossary and persona."""
    status = {
        "glossary_cached": GLOSSARY_CACHE.exists(),
        "glossary_cache_age": None,
        "persona_path_exists": PERSONA_PATH.exists(),
        "people_manifest_exists": PEOPLE_MANIFEST.exists(),
        "projects_manifest_exists": PROJECTS_MANIFEST.exists(),
        "customers_manifest_exists": CUSTOMERS_MANIFEST.exists(),
    }
    
    if GLOSSARY_CACHE.exists():
        mtime = datetime.fromtimestamp(GLOSSARY_CACHE.stat().st_mtime)
        status["glossary_cache_age"] = str(datetime.now() - mtime)
    
    # Estimate token counts
    if status["glossary_cached"]:
        glossary_text = get_glossary_context()
        status["glossary_tokens"] = estimate_prompt_tokens(glossary_text)
    
    if status["persona_path_exists"]:
        persona_text = get_persona_context()
        status["persona_tokens"] = estimate_prompt_tokens(persona_text)
    
    # Total cached prefix
    full_prompt = get_system_prompt(task="email_draft")
    status["full_prompt_tokens"] = estimate_prompt_tokens(full_prompt)
    status["caching_eligible"] = status["full_prompt_tokens"] >= 1024
    
    return status


# Convenience function for common use case
def get_email_draft_prompt() -> str:
    """Get optimized system prompt for email drafting."""
    return get_system_prompt(
        task="email_draft",
        include_persona=True,
        include_glossary=True,
        compact_glossary=False
    )


def get_extraction_prompt() -> str:
    """Get optimized system prompt for content extraction."""
    return get_system_prompt(
        task="extraction",
        include_persona=False,
        include_glossary=True,
        compact_glossary=True  # Smaller for extraction
    )


if __name__ == "__main__":
    # Test the module
    print("=== Cache Status ===")
    status = get_cache_status()
    for k, v in status.items():
        print(f"  {k}: {v}")
    
    print("\n=== Sample Prompts ===")
    
    print("\n--- Email Draft Prompt (first 500 chars) ---")
    email_prompt = get_email_draft_prompt()
    print(email_prompt[:500])
    print(f"\n... ({len(email_prompt)} chars, ~{estimate_prompt_tokens(email_prompt)} tokens)")
    
    print("\n--- Extraction Prompt (first 500 chars) ---")
    extract_prompt = get_extraction_prompt()
    print(extract_prompt[:500])
    print(f"\n... ({len(extract_prompt)} chars, ~{estimate_prompt_tokens(extract_prompt)} tokens)")
