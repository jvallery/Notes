#!/usr/bin/env python3
"""
Ingest Transcripts: Unified pipeline for meeting transcripts.

This script mirrors ingest_emails.py but for meeting transcripts (MacWhisper, etc).

Pipeline:
1. EXTRACT - Parse transcript for structured content
2. PLAN - Generate vault patches for READMEs
3. APPLY - Execute patches to vault
4. ARCHIVE - Move source to Sources/Transcripts/YYYY/

Enrichments (matching email pipeline):
- Name normalization via aliases
- Path sanitization for folder names
- Entity discovery for unknown contacts
- Triage queue for low-confidence entities
- Duplicate detection via content hashing
- Structured patches for consistency

Usage:
    python ingest_transcripts.py                    # Process all pending transcripts
    python ingest_transcripts.py --source           # Re-process from Sources/
    python ingest_transcripts.py --file FILE        # Process single file
    python ingest_transcripts.py --dry-run          # Preview without changes
"""

import json
import re
import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Tuple

import click
from pydantic import BaseModel, Field, ConfigDict
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    load_config,
    get_model_config,
    vault_root,
    workflow_root,
    normalize_person_name,
    normalize_task_owner,
)
from utils.templates import sanitize_path_name


# =============================================================================
# PYDANTIC MODELS
# =============================================================================

class ParticipantInfo(BaseModel):
    """Information about a meeting participant."""
    
    model_config = ConfigDict(extra="ignore")
    
    name: str
    title: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    role_in_meeting: Optional[str] = None  # host, attendee, presenter, etc.


class TaskItem(BaseModel):
    """A task or action item from the meeting."""
    
    model_config = ConfigDict(extra="ignore")
    
    text: str
    owner: Optional[str] = None
    due: Optional[str] = None
    priority: str = "medium"
    related_person: Optional[str] = None
    related_project: Optional[str] = None
    related_customer: Optional[str] = None


class KeyFact(BaseModel):
    """A key fact learned during the meeting."""
    
    model_config = ConfigDict(extra="ignore")
    
    fact: str
    about: str  # Person/company/project this is about
    fact_type: str = "general"  # preference, background, technical, relationship, etc.


class TranscriptExtraction(BaseModel):
    """Structured extraction from a meeting transcript."""
    
    model_config = ConfigDict(extra="ignore")
    
    # Source metadata
    source_file: str
    processed_at: datetime
    meeting_date: str  # YYYY-MM-DD
    title: str
    
    # Meeting classification
    meeting_type: str = "1:1"  # 1:1, team, customer, project, rob, etc.
    note_type: str = "people"  # customer, people, projects, rob, journal
    primary_entity: Optional[str] = None  # Main person/customer/project
    
    # Participants
    participants: List[ParticipantInfo] = Field(default_factory=list)
    
    # Content extraction
    summary: str
    topics: List[str] = Field(default_factory=list)
    
    # Actionable items
    tasks: List[TaskItem] = Field(default_factory=list)
    decisions: List[str] = Field(default_factory=list)
    follow_ups: List[str] = Field(default_factory=list)
    
    # Knowledge extraction
    key_facts: List[KeyFact] = Field(default_factory=list)
    
    # Entity mentions for cross-linking
    people_mentioned: List[str] = Field(default_factory=list)
    companies_mentioned: List[str] = Field(default_factory=list)
    projects_mentioned: List[str] = Field(default_factory=list)


class VaultPatch(BaseModel):
    """A single patch operation for the vault."""
    
    model_config = ConfigDict(extra="forbid")
    
    target_path: str  # Relative path in vault
    target_entity: str
    operation: str  # upsert_frontmatter, append_under_heading, add_task, ensure_wikilinks
    
    frontmatter: Optional[dict] = None
    heading: Optional[str] = None
    content: Optional[str] = None
    task: Optional[TaskItem] = None
    wikilinks: Optional[List[str]] = None


class TranscriptChangePlan(BaseModel):
    """A set of patches based on transcript extraction."""
    
    model_config = ConfigDict(extra="forbid")
    
    version: str = "1.0"
    source_file: str
    extraction_file: str
    created_at: datetime
    
    # Meeting note to create
    meeting_note: Optional[dict] = None
    meeting_note_path: Optional[str] = None
    
    # Patches for entity READMEs
    patches: List[VaultPatch] = Field(default_factory=list)
    
    # Entities to create
    entities_to_create: List[dict] = Field(default_factory=list)
    
    # Warnings
    warnings: List[str] = Field(default_factory=list)


console = Console()

# Index caches
_email_index = None
_name_index = None


# =============================================================================
# UTILITIES
# =============================================================================

def get_openai_client():
    """Get configured OpenAI client with logging."""
    from utils.ai_client import get_openai_client as get_instrumented_client
    return get_instrumented_client("ingest_transcripts")


def get_glossary_context() -> str:
    """Load entity glossary for prompt context."""
    try:
        from utils.cached_prompts import get_glossary_context as _get_glossary
        return _get_glossary(compact=True)
    except ImportError:
        return ""


def _content_hash(file_path: Path) -> str:
    """Generate content hash for duplicate detection."""
    import hashlib
    
    content = file_path.read_text()
    
    # Strip frontmatter
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            content = content[end + 4:]
    
    # Normalize and hash
    normalized = content.strip()[:2000]
    return hashlib.md5(normalized.encode()).hexdigest()[:12]


def _build_content_hash_index(processed_dir: Path) -> dict[str, str]:
    """Build index of processed content hashes."""
    index = {}
    
    if not processed_dir.exists():
        return index
    
    for ext_file in processed_dir.glob("*.transcript_extraction.json"):
        try:
            data = json.loads(ext_file.read_text())
            source = data.get("source_file", "")
            if source:
                source_path = vault_root() / source
                if source_path.exists():
                    content_hash = _content_hash(source_path)
                    index[content_hash] = ext_file.stem.replace(".transcript_extraction", "")
        except Exception:
            pass
    
    return index


def _build_person_index() -> Tuple[dict, dict]:
    """Build index of people by email and name."""
    global _email_index, _name_index
    
    if _email_index is not None and _name_index is not None:
        return _email_index, _name_index
    
    from utils.frontmatter import parse_frontmatter
    
    email_idx = {}
    name_idx = {}
    vault = vault_root()
    
    people_dirs = [
        vault / "VAST" / "People",
        vault / "Personal" / "People"
    ]
    
    for people_dir in people_dirs:
        if not people_dir.exists():
            continue
        
        for folder in people_dir.iterdir():
            if not folder.is_dir():
                continue
            
            readme = folder / "README.md"
            if not readme.exists():
                continue
            
            # Index by folder name
            name_idx[folder.name.lower()] = folder
            
            # Parse frontmatter for email
            try:
                content = readme.read_text()
                fm, _ = parse_frontmatter(content)
                if fm and fm.get("email"):
                    email = fm["email"].strip().lower()
                    if email and email != "''":
                        email_idx[email] = folder
            except Exception:
                pass
    
    _email_index = email_idx
    _name_index = name_idx
    return email_idx, name_idx


def _find_person_folder(name: str, email: Optional[str] = None) -> Optional[Path]:
    """Find existing person folder in vault."""
    email_idx, name_idx = _build_person_index()
    
    # 1. Email match (highest priority)
    if email:
        email_lower = email.strip().lower()
        if email_lower in email_idx:
            return email_idx[email_lower]
    
    # 2. Exact name match
    name_lower = name.lower()
    if name_lower in name_idx:
        return name_idx[name_lower]
    
    # 3. Partial name match (first AND last must match)
    name_parts = name_lower.split()
    if len(name_parts) >= 2:
        for folder_name, folder_path in name_idx.items():
            folder_parts = folder_name.split()
            if len(folder_parts) >= 2:
                if name_parts[0] == folder_parts[0] and name_parts[-1] == folder_parts[-1]:
                    return folder_path
    
    return None


def _find_customer_folder(company: str) -> Optional[Path]:
    """Find existing customer folder in vault."""
    vault = vault_root()
    customers = vault / "VAST" / "Customers and Partners"
    
    if not customers.exists():
        return None
    
    company_lower = company.lower()
    
    for folder in customers.iterdir():
        if folder.is_dir():
            folder_lower = folder.name.lower()
            if company_lower in folder_lower or folder_lower in company_lower:
                return folder
    
    return None


def _find_project_folder(project: str) -> Optional[Path]:
    """Find existing project folder in vault."""
    vault = vault_root()
    projects = vault / "VAST" / "Projects"
    
    if not projects.exists():
        return None
    
    project_lower = project.lower()
    
    for folder in projects.iterdir():
        if folder.is_dir():
            folder_lower = folder.name.lower()
            if project_lower in folder_lower or folder_lower in project_lower:
                return folder
    
    return None


def _add_to_triage_queue(entry: dict):
    """Add entity to triage queue."""
    triage_file = vault_root() / "Inbox" / "_triage" / "entities.yaml"
    triage_file.parent.mkdir(parents=True, exist_ok=True)
    
    import yaml
    
    try:
        entries = yaml.safe_load(triage_file.read_text()) if triage_file.exists() else []
        if entries is None:
            entries = []
    except Exception:
        entries = []
    
    # Check for duplicate by name
    existing = [e.get("name", "").lower() for e in entries if isinstance(e, dict)]
    if entry.get("name", "").lower() not in existing:
        entries.append(entry)
        triage_file.write_text(yaml.dump(entries, allow_unicode=True))


def _extract_date_from_filename(filename: str) -> str:
    """Extract date from transcript filename."""
    # Patterns: "2025-12-15 16 10 - Title.md" or "2025-12-15 - Title.md"
    date_match = re.match(r'^(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        return date_match.group(1)
    return datetime.now().strftime("%Y-%m-%d")


def _extract_title_from_filename(filename: str) -> str:
    """Extract title from transcript filename."""
    # Remove date and time patterns
    title = re.sub(r'^\d{4}-\d{2}-\d{2}\s*\d*:?\d*\s*-?\s*', '', filename)
    title = title.replace('.md', '').strip()
    return title if title else "Meeting"


# =============================================================================
# STEP 1: EXTRACT
# =============================================================================

def extract_from_transcript(file_path: Path, content: str, client) -> TranscriptExtraction:
    """Extract structured data from a meeting transcript."""
    
    model_config = get_model_config("extraction")
    
    meeting_date = _extract_date_from_filename(file_path.name)
    title = _extract_title_from_filename(file_path.name)
    
    # Get glossary for entity resolution
    glossary = get_glossary_context()
    
    extraction_prompt = """You are extracting structured knowledge from a meeting transcript for a personal knowledge management system.

The speaker is Jason Vallery (me, myself). When extracting tasks owned by Jason, use owner "Myself".

Extract ALL of the following as JSON:

{
    "meeting_type": "1:1 | team | customer | project | rob | other",
    "note_type": "people | customer | projects | rob | journal",
    "primary_entity": "The main person/customer/project this meeting is about",
    "title": "A concise title for this meeting",
    "summary": "2-3 sentence summary of the meeting",
    
    "participants": [
        {
            "name": "Full Name",
            "title": "Job title if mentioned",
            "company": "Company if mentioned",
            "role_in_meeting": "host | attendee | presenter"
        }
    ],
    
    "topics": ["Topic 1", "Topic 2"],
    
    "tasks": [
        {
            "text": "Action item description",
            "owner": "Myself or Person Name",
            "due": "YYYY-MM-DD if mentioned",
            "priority": "high | medium | low",
            "related_person": "Person this relates to",
            "related_project": "Project this relates to",
            "related_customer": "Customer this relates to"
        }
    ],
    
    "decisions": ["Decision 1", "Decision 2"],
    
    "follow_ups": ["Follow-up item 1", "Follow-up item 2"],
    
    "key_facts": [
        {
            "fact": "The fact learned",
            "about": "Person or company name",
            "fact_type": "preference | background | technical | relationship | general"
        }
    ],
    
    "people_mentioned": ["Name 1", "Name 2"],
    "companies_mentioned": ["Company 1", "Company 2"],
    "projects_mentioned": ["Project 1", "Project 2"]
}

IMPORTANT RULES:
- Use "Myself" for first-person task ownership
- Normalize names: use full names where possible
- Date format: YYYY-MM-DD
- Extract facts about people and companies that would be useful to remember
- Identify ALL entities mentioned for cross-linking
- Be thorough but avoid duplicating content across fields
"""

    user_prompt = f"""Filename: {file_path.name}
Meeting Date: {meeting_date}

Transcript:
{content}"""

    # Build system prompt with glossary prefix (for caching)
    if glossary:
        system_prompt = f"""## ENTITY GLOSSARY
{glossary}

{extraction_prompt}"""
    else:
        system_prompt = extraction_prompt

    try:
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.0,
        )
        
        data = json.loads(response.choices[0].message.content)
        
        # Normalize participant names
        if "participants" in data:
            for p in data["participants"]:
                if p.get("name"):
                    p["name"] = normalize_person_name(p["name"])
        
        # Normalize task owners
        if "tasks" in data:
            for task in data["tasks"]:
                if task.get("owner"):
                    task["owner"] = normalize_task_owner(task["owner"])
        
        # Normalize entity mentions
        for field in ["people_mentioned", "companies_mentioned"]:
            if field in data:
                data[field] = [normalize_person_name(n) for n in data[field]]
        
        # Build extraction model
        extraction = TranscriptExtraction(
            source_file=str(file_path.relative_to(vault_root())),
            processed_at=datetime.now(),
            meeting_date=meeting_date,
            title=data.get("title", title),
            meeting_type=data.get("meeting_type", "1:1"),
            note_type=data.get("note_type", "people"),
            primary_entity=data.get("primary_entity"),
            participants=[ParticipantInfo(**p) for p in data.get("participants", [])],
            summary=data.get("summary", ""),
            topics=data.get("topics", []),
            tasks=[TaskItem(**t) for t in data.get("tasks", [])],
            decisions=data.get("decisions", []),
            follow_ups=data.get("follow_ups", []),
            key_facts=[KeyFact(**f) for f in data.get("key_facts", [])],
            people_mentioned=data.get("people_mentioned", []),
            companies_mentioned=data.get("companies_mentioned", []),
            projects_mentioned=data.get("projects_mentioned", [])
        )
        
        return extraction
        
    except json.JSONDecodeError as e:
        console.print(f"[yellow]JSON parse error: {e}[/yellow]")
        return TranscriptExtraction(
            source_file=str(file_path),
            processed_at=datetime.now(),
            meeting_date=meeting_date,
            title=title,
            summary="Failed to extract"
        )
    except Exception as e:
        console.print(f"[red]Extraction failed: {e}[/red]")
        raise


# =============================================================================
# STEP 2: PLAN
# =============================================================================

def generate_patches(extraction: TranscriptExtraction, client=None) -> TranscriptChangePlan:
    """Generate vault patches from transcript extraction."""
    
    vault = vault_root()
    patches = []
    warnings = []
    entities_to_create = []
    
    # Determine destination folder based on note_type and primary_entity
    note_type = extraction.note_type
    primary_entity = extraction.primary_entity
    
    # Normalize primary entity name
    if primary_entity:
        primary_entity = normalize_person_name(primary_entity)
    
    # Find or determine destination folder
    dest_folder = None
    if note_type == "people" and primary_entity:
        dest_folder = _find_person_folder(primary_entity)
        if not dest_folder:
            # Create new person folder
            safe_name = sanitize_path_name(primary_entity)
            dest_folder = vault / "VAST" / "People" / safe_name
            dest_folder.mkdir(parents=True, exist_ok=True)
            entities_to_create.append({
                "type": "person",
                "name": primary_entity,
                "source": extraction.source_file
            })
    elif note_type == "customer" and primary_entity:
        dest_folder = _find_customer_folder(primary_entity)
        if not dest_folder:
            safe_name = sanitize_path_name(primary_entity)
            dest_folder = vault / "VAST" / "Customers and Partners" / safe_name
            dest_folder.mkdir(parents=True, exist_ok=True)
            entities_to_create.append({
                "type": "customer",
                "name": primary_entity,
                "source": extraction.source_file
            })
    elif note_type == "projects" and primary_entity:
        dest_folder = _find_project_folder(primary_entity)
        if not dest_folder:
            safe_name = sanitize_path_name(primary_entity)
            dest_folder = vault / "VAST" / "Projects" / safe_name
            dest_folder.mkdir(parents=True, exist_ok=True)
            entities_to_create.append({
                "type": "project",
                "name": primary_entity,
                "source": extraction.source_file
            })
    elif note_type == "rob":
        dest_folder = vault / "VAST" / "ROB" / sanitize_path_name(primary_entity or "General")
        dest_folder.mkdir(parents=True, exist_ok=True)
    else:
        # Fallback to journal
        dest_folder = vault / "VAST" / "Journal"
        dest_folder.mkdir(parents=True, exist_ok=True)
    
    # Generate meeting note content
    meeting_note = _generate_meeting_note(extraction)
    safe_title = sanitize_path_name(extraction.title)
    meeting_note_filename = f"{extraction.meeting_date} - {safe_title}.md"
    meeting_note_path = str((dest_folder / meeting_note_filename).relative_to(vault))
    
    # Generate patches for participant READMEs
    for participant in extraction.participants:
        if participant.name.lower() in ["myself", "jason vallery", "jason"]:
            continue  # Skip self
        
        participant_patches = _generate_person_patches(
            participant, 
            extraction, 
            client
        )
        patches.extend(participant_patches["patches"])
        warnings.extend(participant_patches["warnings"])
        if participant_patches.get("create"):
            entities_to_create.append(participant_patches["create"])
    
    # Companies to skip patching (our company, generic mentions)
    skip_companies = {
        "vast", "vast data", "vastdata",  # Our own company
        "the company", "our company", "this company",  # Generic refs
    }
    
    # Only patch companies for customer/partner type meetings
    # For 1:1s (people type), companies are often mentioned in passing
    if note_type in ["customer", "partners"]:
        # Generate patches for mentioned companies (excluding our own)
        for company in extraction.companies_mentioned:
            if company.lower() in skip_companies:
                continue
            company_patches = _generate_customer_patches(company, extraction)
            patches.extend(company_patches["patches"])
            warnings.extend(company_patches["warnings"])
    elif primary_entity and note_type == "people":
        # For 1:1s with a person from a specific company, patch that company only
        for participant in extraction.participants:
            if participant.company and participant.company.lower() not in skip_companies:
                # Only patch the participant's company, not all mentions
                company_folder = _find_customer_folder(participant.company)
                if company_folder:
                    company_patches = _generate_customer_patches(participant.company, extraction)
                    patches.extend(company_patches["patches"])
                    break  # Only patch one company per 1:1
    
    # Build change plan
    plan = TranscriptChangePlan(
        source_file=extraction.source_file,
        extraction_file=extraction.source_file.replace(".md", ".transcript_extraction.json"),
        created_at=datetime.now(),
        meeting_note=meeting_note,
        meeting_note_path=meeting_note_path,
        patches=patches,
        entities_to_create=entities_to_create,
        warnings=warnings
    )
    
    return plan


def _generate_meeting_note(extraction: TranscriptExtraction) -> dict:
    """Generate meeting note content."""
    
    # Build frontmatter
    frontmatter = {
        "type": extraction.note_type,
        "title": extraction.title,
        "date": extraction.meeting_date,
        "participants": [p.name for p in extraction.participants],
        "source": "transcript",
        "tags": [f"type/{extraction.note_type}"]
    }
    
    if extraction.primary_entity:
        frontmatter["entity"] = extraction.primary_entity
    
    # Build content sections
    content_parts = []
    
    # Summary
    if extraction.summary:
        content_parts.append(f"## Summary\n\n{extraction.summary}\n")
    
    # Topics
    if extraction.topics:
        topics_list = "\n".join(f"- {t}" for t in extraction.topics)
        content_parts.append(f"## Topics\n\n{topics_list}\n")
    
    # Key facts
    if extraction.key_facts:
        facts_list = "\n".join(f"- {f.fact} *(about {f.about})*" for f in extraction.key_facts)
        content_parts.append(f"## Key Facts\n\n{facts_list}\n")
    
    # Decisions
    if extraction.decisions:
        decisions_list = "\n".join(f"- {d}" for d in extraction.decisions)
        content_parts.append(f"## Decisions\n\n{decisions_list}\n")
    
    # Tasks with Obsidian Tasks format
    if extraction.tasks:
        tasks_lines = []
        for task in extraction.tasks:
            task_line = f"- [ ] {task.text}"
            if task.owner:
                task_line += f" @{task.owner}"
            if task.due:
                task_line += f" 📅 {task.due}"
            # Priority emoji
            priority_map = {
                "highest": "🔺", "high": "⏫", "medium": "🔼",
                "low": "🔽", "lowest": "⏬"
            }
            task_line += f" {priority_map.get(task.priority, '🔼')} #task"
            tasks_lines.append(task_line)
        content_parts.append(f"## Action Items\n\n" + "\n".join(tasks_lines) + "\n")
    
    # Follow-ups (as tasks without dates)
    if extraction.follow_ups:
        followups_lines = [f"- [ ] {f} @Myself 🔼 #task #followup" for f in extraction.follow_ups]
        content_parts.append(f"## Follow-ups\n\n" + "\n".join(followups_lines) + "\n")
    
    # Companies to skip in related links
    skip_companies = {"vast", "vast data", "vastdata"}
    
    # Related entities
    related = []
    for p in extraction.people_mentioned:
        if p.lower() not in ["myself", "jason vallery", "jason"]:
            related.append(f"[[{p}]]")
    for c in extraction.companies_mentioned:
        if c.lower() not in skip_companies:
            related.append(f"[[{c}]]")
    for p in extraction.projects_mentioned:
        related.append(f"[[{p}]]")
    
    if related:
        related_list = "\n".join(f"- {r}" for r in related)
        content_parts.append(f"## Related\n\n{related_list}\n")
    
    return {
        "frontmatter": frontmatter,
        "content": "\n".join(content_parts)
    }


def _generate_person_patches(
    participant: ParticipantInfo,
    extraction: TranscriptExtraction,
    client=None
) -> dict:
    """Generate patches for a person's README.
    
    NOTE: This function does NOT create folders - only generates patches
    for existing entities.
    """
    
    patches = []
    warnings = []
    create_info = None
    
    # Find existing folder
    person_folder = _find_person_folder(participant.name)
    
    if person_folder is None:
        # Person doesn't exist - log and skip (don't auto-create for participants)
        warnings.append(f"Person '{participant.name}' not found - skipping patches")
        return {"patches": patches, "warnings": warnings, "create": None}
    
    # Generate patches for README
    readme_path = person_folder / "README.md"
    if not readme_path.exists():
        warnings.append(f"README not found for {participant.name}")
        return {"patches": patches, "warnings": warnings, "create": create_info}
    
    target_path = str(readme_path.relative_to(vault_root()))
    
    # Patch: Update last_contact
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=participant.name,
        operation="upsert_frontmatter",
        frontmatter={"last_contact": extraction.meeting_date}
    ))
    
    # Patch: Add to Recent Context
    context_entry = f"- {extraction.meeting_date}: {extraction.title}"
    if extraction.summary:
        context_entry += f" - {extraction.summary[:100]}"
    
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=participant.name,
        operation="append_under_heading",
        heading="## Recent Context",
        content=context_entry
    ))
    
    # Patch: Add key facts about this person
    person_facts = [f for f in extraction.key_facts if f.about.lower() == participant.name.lower()]
    for fact in person_facts:
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=participant.name,
            operation="append_under_heading",
            heading="## Key Facts",
            content=f"- {fact.fact} ({extraction.meeting_date})"
        ))
    
    # Patch: Add topics discussed
    if extraction.topics:
        topics_entry = f"- {extraction.meeting_date}: " + ", ".join(extraction.topics[:5])
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=participant.name,
            operation="append_under_heading",
            heading="## Topics",
            content=topics_entry
        ))
    
    # Patch: Add decisions
    if extraction.decisions:
        decisions_entry = f"- {extraction.meeting_date}: " + "; ".join(extraction.decisions[:3])
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=participant.name,
            operation="append_under_heading",
            heading="## Key Decisions",
            content=decisions_entry
        ))
    
    return {"patches": patches, "warnings": warnings, "create": create_info}


def _generate_customer_patches(company: str, extraction: TranscriptExtraction) -> dict:
    """Generate patches for a customer README.
    
    NOTE: This function does NOT create folders - it only generates patches.
    Folder creation happens in the apply phase.
    """
    
    patches = []
    warnings = []
    create_info = None
    
    customer_folder = _find_customer_folder(company)
    
    if customer_folder is None:
        # Mark for creation (don't actually create here - that's for apply phase)
        warnings.append(f"Customer '{company}' not found - will skip (no auto-create for customers)")
        return {"patches": patches, "warnings": warnings, "create": None}
    
    readme_path = customer_folder / "README.md"
    if not readme_path.exists():
        warnings.append(f"README not found for {company}")
        return {"patches": patches, "warnings": warnings, "create": None}
    
    target_path = str(readme_path.relative_to(vault_root()))
    
    # Patch: Update last_contact
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=company,
        operation="upsert_frontmatter",
        frontmatter={"last_contact": extraction.meeting_date}
    ))
    
    # Patch: Add to Recent Context
    context_entry = f"- {extraction.meeting_date}: {extraction.title}"
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=company,
        operation="append_under_heading",
        heading="## Recent Context",
        content=context_entry
    ))
    
    return {"patches": patches, "warnings": warnings}


def _create_person_readme(participant: ParticipantInfo) -> str:
    """Create a new person README."""
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    frontmatter = f"""---
type: people
title: "{participant.name}"
created: {today}
last_contact: {today}
last_updated: {today}
tags:
  - type/people
  - "#needs-review"
---

"""
    
    content = f"""# {participant.name}

## Profile

**Role**: {participant.title or "_Unknown_"}
**Company**: {participant.company or "_Unknown_"}

---

## Key Facts

---

## Topics

---

## Key Decisions

---

## Recent Context

---

## Related Customers

---

## Related Projects

---

## Tasks

```tasks
not done
path includes {{{{this.file.folder}}}}
```
"""
    
    return frontmatter + content


def _create_customer_readme(company: str) -> str:
    """Create a new customer README."""
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    return f"""---
type: customer
title: "{company}"
created: {today}
last_contact: {today}
last_updated: {today}
status: active
tags:
  - type/customer
  - "#needs-review"
---

# {company}

## Overview

_Customer added via transcript processing._

---

## Key Contacts

---

## Recent Context

---

## Tasks

```tasks
not done
path includes {{{{this.file.folder}}}}
```
"""


# =============================================================================
# STEP 3: APPLY
# =============================================================================

def apply_changeplan(plan: TranscriptChangePlan, dry_run: bool = False) -> bool:
    """Apply the changeplan to the vault."""
    
    from utils.frontmatter import parse_frontmatter
    import yaml
    
    vault = vault_root()
    success = True
    
    # 1. Create meeting note
    if plan.meeting_note and plan.meeting_note_path:
        note_path = vault / plan.meeting_note_path
        
        if dry_run:
            console.print(f"  [dim]Would create: {plan.meeting_note_path}[/dim]")
        elif not note_path.exists():
            note_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Build note content
            fm = plan.meeting_note["frontmatter"]
            content = plan.meeting_note["content"]
            
            fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
            note_content = f"---\n{fm_yaml}---\n\n{content}"
            
            note_path.write_text(note_content)
            console.print(f"  [green]Created: {plan.meeting_note_path}[/green]")
    
    # 2. Apply patches
    for patch in plan.patches:
        target = vault / patch.target_path
        
        if not target.exists():
            console.print(f"  [yellow]Target not found: {patch.target_path}[/yellow]")
            continue
        
        if dry_run:
            console.print(f"  [dim]Would patch: {patch.target_entity} ({patch.operation})[/dim]")
            continue
        
        try:
            content = target.read_text()
            
            if patch.operation == "upsert_frontmatter":
                content = _apply_frontmatter_patch(content, patch.frontmatter or {})
            
            elif patch.operation == "append_under_heading":
                content = _apply_heading_patch(content, patch.heading or "", patch.content or "")
            
            target.write_text(content)
            
        except Exception as e:
            console.print(f"  [red]Patch failed: {patch.target_path} - {e}[/red]")
            success = False
    
    return success


def _apply_frontmatter_patch(content: str, updates: dict) -> str:
    """Update frontmatter in content."""
    import yaml
    
    if not content.startswith("---"):
        # No frontmatter - add it
        fm_yaml = yaml.dump(updates, default_flow_style=False, allow_unicode=True)
        return f"---\n{fm_yaml}---\n\n{content}"
    
    end = content.find("\n---", 3)
    if end == -1:
        return content
    
    fm_text = content[4:end]
    body = content[end + 4:]
    
    try:
        fm = yaml.safe_load(fm_text) or {}
    except:
        fm = {}
    
    fm.update(updates)
    
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    return f"---\n{new_fm}---{body}"


def _apply_heading_patch(content: str, heading: str, text: str) -> str:
    """Append text under a heading."""
    
    lines = content.split("\n")
    heading_level = heading.count("#")
    heading_text = heading.lstrip("# ").strip().lower()
    
    # Find the heading
    for i, line in enumerate(lines):
        if line.strip().lower().startswith(heading.lower()) or \
           (line.strip().startswith("#" * heading_level + " ") and 
            heading_text in line.strip().lower()):
            
            # Find end of section (next heading of same or higher level, or "---")
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith("---"):
                    break
                if next_line.startswith("#"):
                    # Check heading level
                    next_level = len(next_line) - len(next_line.lstrip("#"))
                    if next_level <= heading_level:
                        break
                j += 1
            
            # Insert before the end marker or next section
            # Skip blank lines at end of section
            insert_at = j
            while insert_at > i + 1 and not lines[insert_at - 1].strip():
                insert_at -= 1
            
            lines.insert(insert_at, text)
            return "\n".join(lines)
    
    # Heading not found - add at end
    lines.append("")
    lines.append(heading)
    lines.append("")
    lines.append(text)
    return "\n".join(lines)


# =============================================================================
# STEP 4: ARCHIVE
# =============================================================================

def archive_source(source_path: Path, extraction: TranscriptExtraction) -> Path:
    """Move source file to Sources/Transcripts/YYYY/."""
    
    vault = vault_root()
    year = extraction.meeting_date[:4]
    
    archive_dir = vault / "Sources" / "Transcripts" / year
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    dest = archive_dir / source_path.name
    
    # Handle duplicates
    counter = 1
    while dest.exists():
        stem = source_path.stem
        suffix = source_path.suffix
        dest = archive_dir / f"{stem}_{counter}{suffix}"
        counter += 1
    
    source_path.rename(dest)
    
    return dest


# =============================================================================
# MAIN CLI
# =============================================================================

def find_pending_transcripts() -> List[Path]:
    """Find unprocessed transcripts in Inbox."""
    
    inbox = vault_root() / "Inbox" / "Transcripts"
    extraction_dir = vault_root() / "Inbox" / "_extraction"
    
    if not inbox.exists():
        return []
    
    # Build content hash index
    hash_index = _build_content_hash_index(extraction_dir)
    
    pending = []
    duplicates = []
    
    for file in inbox.glob("*.md"):
        # Check if already extracted
        extraction_file = extraction_dir / f"{file.stem}.transcript_extraction.json"
        if extraction_file.exists():
            continue
        
        # Check for content duplicate
        content_hash = _content_hash(file)
        if content_hash in hash_index:
            duplicates.append((file, hash_index[content_hash]))
            continue
        
        pending.append(file)
    
    if duplicates:
        console.print(f"[yellow]Skipping {len(duplicates)} duplicate transcripts[/yellow]")
    
    return sorted(pending, key=lambda p: p.name)


def find_source_transcripts(year: Optional[str] = None) -> List[Path]:
    """Find transcripts in Sources/ for reprocessing."""
    
    sources = vault_root() / "Sources" / "Transcripts"
    
    if not sources.exists():
        return []
    
    transcripts = []
    
    if year:
        year_dir = sources / year
        if year_dir.exists():
            transcripts.extend(year_dir.glob("*.md"))
    else:
        for year_dir in sources.iterdir():
            if year_dir.is_dir():
                transcripts.extend(year_dir.glob("*.md"))
    
    return sorted(transcripts, key=lambda p: p.name)


@click.command()
@click.option("--file", "-f", "single_file", type=click.Path(exists=True),
              help="Process a single file")
@click.option("--source", "-s", is_flag=True,
              help="Reprocess from Sources/ instead of Inbox/")
@click.option("--year", "-y", type=str,
              help="Year to process from Sources/ (e.g., 2025)")
@click.option("--limit", "-l", type=int, default=0,
              help="Maximum files to process")
@click.option("--dry-run", is_flag=True,
              help="Preview without making changes")
@click.option("--verbose", "-v", is_flag=True,
              help="Show detailed output")
def main(single_file, source, year, limit, dry_run, verbose):
    """Ingest meeting transcripts into the vault."""
    
    console.print("[bold blue]Ingest Transcripts[/bold blue]")
    console.print("=" * 50)
    
    # Find files to process
    if single_file:
        files = [Path(single_file)]
    elif source:
        files = find_source_transcripts(year)
        console.print(f"Processing from Sources/ ({len(files)} files)")
    else:
        files = find_pending_transcripts()
    
    if not files:
        console.print("[yellow]No transcripts to process.[/yellow]")
        return
    
    if limit > 0:
        files = files[:limit]
    
    console.print(f"Found [bold]{len(files)}[/bold] transcripts to process")
    
    if dry_run:
        console.print("[dim](dry-run mode)[/dim]")
    
    # Initialize OpenAI client
    client = get_openai_client()
    
    # Process each file
    results = {"success": [], "failed": []}
    
    for file in files:
        console.print(f"\n[bold]{file.name}[/bold]")
        
        try:
            content = file.read_text()
            
            # EXTRACT
            if verbose:
                console.print("  Extracting...")
            extraction = extract_from_transcript(file, content, client)
            
            if verbose:
                console.print(f"    Type: {extraction.note_type}")
                console.print(f"    Entity: {extraction.primary_entity}")
                console.print(f"    Participants: {len(extraction.participants)}")
                console.print(f"    Tasks: {len(extraction.tasks)}")
            
            # Save extraction
            extraction_dir = vault_root() / "Inbox" / "_extraction"
            extraction_dir.mkdir(parents=True, exist_ok=True)
            extraction_file = extraction_dir / f"{file.stem}.transcript_extraction.json"
            
            if not dry_run:
                extraction_file.write_text(extraction.model_dump_json(indent=2))
            
            # PLAN
            if verbose:
                console.print("  Planning...")
            plan = generate_patches(extraction, client)
            
            if verbose:
                console.print(f"    Patches: {len(plan.patches)}")
                console.print(f"    New entities: {len(plan.entities_to_create)}")
            
            # Save changeplan
            changeplan_file = extraction_dir / f"{file.stem}.transcript_changeplan.json"
            if not dry_run:
                changeplan_file.write_text(plan.model_dump_json(indent=2))
            
            # APPLY
            if verbose:
                console.print("  Applying...")
            apply_success = apply_changeplan(plan, dry_run=dry_run)
            
            # ARCHIVE (only for Inbox files, not --source)
            if not source and not dry_run and apply_success:
                if verbose:
                    console.print("  Archiving...")
                archive_path = archive_source(file, extraction)
                
                # Update extraction with archive path
                extraction_data = json.loads(extraction_file.read_text())
                extraction_data["archived_to"] = str(archive_path.relative_to(vault_root()))
                extraction_file.write_text(json.dumps(extraction_data, indent=2))
            
            results["success"].append(str(file))
            console.print(f"  [green]✓ Complete[/green]")
            
        except Exception as e:
            results["failed"].append({"file": str(file), "error": str(e)})
            console.print(f"  [red]✗ Failed: {e}[/red]")
            if verbose:
                import traceback
                traceback.print_exc()
    
    # Summary
    console.print("\n" + "=" * 50)
    console.print(f"[green]Success: {len(results['success'])}[/green]")
    console.print(f"[red]Failed: {len(results['failed'])}[/red]")


if __name__ == "__main__":
    main()
