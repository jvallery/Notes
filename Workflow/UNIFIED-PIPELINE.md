# Unified Content Pipeline Architecture

> **Status**: Design Draft  
> **Created**: 2026-01-04  
> **Related**: [DESIGN.md](DESIGN.md) | [EMAIL-INGESTION.md](EMAIL-INGESTION.md)

## Vision

A single ETL pipeline that:
1. **Accepts** any content type (email, transcript, document, voice memo, text message)
2. **Extracts** structured knowledge with rich context (manifests, persona, glossary)
3. **Patches** all relevant entities (people, companies, projects)
4. **Triggers** enrichments for new or sparse entities
5. **Generates** appropriate outputs (draft replies, tasks, calendar invites)

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         UNIFIED INGEST PIPELINE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUTS (Content Adapters)                                                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │  Email   │ │Transcript│ │ Document │ │  Voice   │ │   SMS    │          │
│  │ Adapter  │ │ Adapter  │ │ Adapter  │ │ Adapter  │ │ Adapter  │          │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘          │
│       │            │            │            │            │                  │
│       └────────────┴────────────┼────────────┴────────────┘                  │
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    NORMALIZE (ContentEnvelope)                         │  │
│  │  {                                                                     │  │
│  │    content_type: email | transcript | document | voice | sms           │  │
│  │    source_path: "Inbox/Email/2026-01-04_*.md"                          │  │
│  │    raw_content: "..."                                                  │  │
│  │    metadata: { date, participants, subject, thread_id, ... }           │  │
│  │  }                                                                     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                 │                                            │
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      LOAD CONTEXT (ContextBundle)                      │  │
│  │                                                                        │  │
│  │  • Persona: Workflow/prompts/persona.md (my role, priorities, style)   │  │
│  │  • Manifests: People/_MANIFEST.md, Customers/_MANIFEST.md              │  │
│  │  • Glossary: entities/glossary.yaml (acronyms, terms)                  │  │
│  │  • Aliases: entities/aliases.yaml (name normalization)                 │  │
│  │  • Entity READMEs: Relevant entities mentioned in content              │  │
│  │                                                                        │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                 │                                            │
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                           EXTRACT (LLM)                                │  │
│  │                                                                        │  │
│  │  System Prompt includes:                                               │  │
│  │  • Base extraction rules (prompts/base.md.j2)                          │  │
│  │  • Content-type specific guidance                                      │  │
│  │  • Persona context (who I am, what I care about)                       │  │
│  │  • Manifest snippets (known entities for matching)                     │  │
│  │  • Glossary (term definitions)                                         │  │
│  │                                                                        │  │
│  │  Output: UnifiedExtraction                                             │  │
│  │  {                                                                     │  │
│  │    summary: "...",                                                     │  │
│  │    note_type: people | customer | project | rob | journal,             │  │
│  │    primary_entity: { type, name, confidence },                         │  │
│  │    participants: [...],                                                │  │
│  │    facts: [ { text, about_entity, confidence } ],                      │  │
│  │    decisions: [...],                                                   │  │
│  │    tasks: [ { text, owner, due, related_entities } ],                  │  │
│  │    topics: [...],                                                      │  │
│  │    mentioned_entities: [ { type, name, role, facts_about } ],          │  │
│  │    suggested_outputs: {                                                │  │
│  │      draft_reply: true | false,                                        │  │
│  │      calendar_invite: { ... } | null,                                  │  │
│  │      follow_up_reminder: { ... } | null                                │  │
│  │    }                                                                   │  │
│  │  }                                                                     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                 │                                            │
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      GENERATE PATCHES (Deterministic)                  │  │
│  │                                                                        │  │
│  │  For each entity with facts/context:                                   │  │
│  │  • People: patch Key Facts, Topics, Recent Context                     │  │
│  │  • Companies: patch Key Facts, Key Contacts, Recent Context            │  │
│  │  • Projects: patch Key Decisions, Related People, Recent Context       │  │
│  │                                                                        │  │
│  │  Patching Rules:                                                       │  │
│  │  • Existing entity + facts → PATCH                                     │  │
│  │  • New entity + high confidence → CREATE + PATCH                       │  │
│  │  • New entity + low confidence → SKIP + flag for review                │  │
│  │                                                                        │  │
│  │  Output: ChangePlan with all operations                                │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                 │                                            │
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    TRIGGER ENRICHMENTS (Async Queue)                   │  │
│  │                                                                        │  │
│  │  Events:                                                               │  │
│  │  • entity.created[person] → enrich_person(level=2)                     │  │
│  │  • entity.created[company] → enrich_company(level=2)                   │  │
│  │  • entity.sparse[person] → queue_enrichment(person, priority=low)      │  │
│  │                                                                        │  │
│  │  Enrichment runs after apply phase completes                           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                 │                                            │  
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                     GENERATE OUTPUTS (LLM + Context)                   │  │
│  │                                                                        │  │
│  │  If email input + needs reply:                                         │  │
│  │  • Gather related READMEs (sender, mentioned entities)                 │  │
│  │  • Load persona + communication style                                  │  │
│  │  • Generate draft reply → Inbox/_drafts/                               │  │
│  │                                                                        │  │
│  │  If scheduling mentioned:                                              │  │
│  │  • Extract date/time/participants                                      │  │
│  │  • Generate .ics draft → Inbox/_drafts/                                │  │
│  │                                                                        │  │
│  │  If tasks extracted:                                                   │  │
│  │  • Already embedded in meeting notes via extraction                    │  │
│  │  • High-priority tasks → also added to TASKS_INBOX.md                  │  │
│  │                                                                        │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                 │                                            │
│                                 ▼                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                           APPLY (Transactional)                        │  │
│  │                                                                        │  │
│  │  1. Validate git is clean                                              │  │
│  │  2. Apply all patches atomically                                       │  │
│  │  3. Create meeting notes / knowledge artifacts                         │  │
│  │  4. Archive source to Sources/{ContentType}/{Year}/                    │  │
│  │  5. Git commit with summary                                            │  │
│  │  6. Run queued enrichments                                             │  │
│  │                                                                        │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Content Adapters

Each content type has an adapter that normalizes to `ContentEnvelope`:

### Email Adapter
```python
class EmailAdapter:
    """Parse email .md files exported from Apple Mail."""
    
    def parse(self, path: Path) -> ContentEnvelope:
        content = path.read_text()
        # Extract headers (From, To, Subject, Date)
        # Parse thread structure
        # Return normalized envelope
        return ContentEnvelope(
            content_type="email",
            source_path=path,
            raw_content=content,
            metadata={
                "from": sender,
                "to": recipients,
                "subject": subject,
                "date": date,
                "thread_id": thread_id,
                "is_reply": bool,
            }
        )
```

### Transcript Adapter
```python
class TranscriptAdapter:
    """Parse MacWhisper transcripts with speaker diarization."""
    
    def parse(self, path: Path) -> ContentEnvelope:
        content = path.read_text()
        # Parse speaker labels
        # Extract date from filename
        # Identify participants from speaker labels
        return ContentEnvelope(
            content_type="transcript",
            source_path=path,
            raw_content=content,
            metadata={
                "date": date_from_filename,
                "participants": speakers,
                "duration": duration_estimate,
            }
        )
```

### Document Adapter
```python
class DocumentAdapter:
    """Parse PDFs, notes, articles dropped in Inbox."""
    
    def parse(self, path: Path) -> ContentEnvelope:
        # Extract text from PDF/docx/txt
        # Detect document type (article, spec, proposal, etc.)
        return ContentEnvelope(
            content_type="document",
            source_path=path,
            raw_content=extracted_text,
            metadata={
                "document_type": doc_type,
                "title": title,
                "date": date or today,
            }
        )
```

---

## Context Loading

Before extraction, we load relevant context:

```python
class ContextBundle:
    """All context needed for extraction and output generation."""
    
    persona: str              # My role, priorities, communication style
    people_manifest: str      # Compact list of known people
    company_manifest: str     # Compact list of known companies
    project_list: list[str]   # Known project names
    glossary: dict            # Term definitions, acronyms
    aliases: dict             # Name normalization mappings
    
    # Dynamically loaded based on content
    relevant_readmes: dict[str, str]  # Entity name → README summary
    
    @classmethod
    def load(cls, envelope: ContentEnvelope, vault_root: Path) -> "ContextBundle":
        """Load context relevant to this content."""
        
        bundle = cls()
        bundle.persona = load_persona(vault_root)
        bundle.people_manifest = load_manifest(vault_root / "VAST/People/_MANIFEST.md")
        bundle.company_manifest = load_manifest(vault_root / "VAST/Customers and Partners/_MANIFEST.md")
        bundle.project_list = list_projects(vault_root)
        bundle.glossary = load_glossary(vault_root)
        bundle.aliases = load_aliases(vault_root)
        
        # Pre-scan content for likely entity mentions
        # Load those READMEs for richer context
        mentioned = quick_entity_scan(envelope.raw_content, bundle)
        bundle.relevant_readmes = load_entity_readmes(mentioned, vault_root)
        
        return bundle
```

### Prompt Caching & Instrumentation

- Persona + entity glossary + aliases are loaded first and placed at the top of the system prompt to trigger OpenAI prompt caching (static prefix ≥1024 tokens).
- Dynamic context (relevant READMEs) is appended after the cacheable prefix.
- All extractor calls use the instrumented OpenAI client (`utils.ai_client`) so cache hit/miss and token usage are logged alongside caller/context metadata.

---

## Unified Extraction Schema

A single schema works for all content types:

```python
class UnifiedExtraction(BaseModel):
    """Extraction output for any content type."""
    
    # Core fields (all content types)
    source_file: str
    content_type: Literal["email", "transcript", "document", "voice", "sms"]
    processed_at: datetime
    
    # Classification
    note_type: Literal["people", "customer", "project", "rob", "journal"]
    primary_entity: EntityRef | None  # Main subject of the content
    
    # Participants (for meetings/emails)
    participants: list[str] = []
    
    # Extracted knowledge
    summary: str
    facts: list[Fact]           # { text, about_entity, confidence }
    decisions: list[str] = []
    tasks: list[Task] = []      # { text, owner, due, priority, related_entities }
    topics: list[str] = []
    
    # Entity mentions with context
    mentioned_entities: list[MentionedEntity] = []
    # { type: person|company|project, name, role, facts_about: [...] }
    
    # Content-type specific
    email_metadata: EmailMeta | None = None  # thread_id, needs_reply, urgency
    meeting_metadata: MeetingMeta | None = None  # duration, agenda
    
    # Suggested outputs
    suggested_outputs: SuggestedOutputs = SuggestedOutputs()


class Fact(BaseModel):
    text: str
    about_entity: EntityRef | None  # Who/what is this fact about?
    confidence: float = 0.8


class MentionedEntity(BaseModel):
    entity_type: Literal["person", "company", "project"]
    name: str
    role: str | None = None  # How they relate to the content
    facts_about: list[str] = []  # Facts discovered about this entity


class SuggestedOutputs(BaseModel):
    needs_reply: bool = False
    draft_reply_context: str | None = None  # Key points to address
    calendar_invite: CalendarSuggestion | None = None
    follow_up_reminder: ReminderSuggestion | None = None
```

---

## Smart Patching Logic

Patch entities when we learn something new:

```python
def generate_patches(extraction: UnifiedExtraction, context: ContextBundle) -> list[PatchOp]:
    """Generate patches for all entities with new knowledge."""
    
    patches = []
    
    # 1. Primary entity always gets patched
    if extraction.primary_entity:
        patches.extend(generate_entity_patch(
            extraction.primary_entity,
            extraction.facts,
            extraction.summary,
            extraction.tasks
        ))
    
    # 2. Patch any entity we learned facts about
    for mention in extraction.mentioned_entities:
        if mention.facts_about:
            # We learned something specific about this entity
            entity_path = find_entity_path(mention.name, mention.entity_type, context)
            if entity_path:
                patches.append(PatchOp(
                    target=entity_path,
                    add_facts=mention.facts_about,
                    add_context=f"Mentioned in: {extraction.summary[:100]}..."
                ))
            elif should_create_entity(mention, context):
                patches.append(CreateOp(
                    entity_type=mention.entity_type,
                    name=mention.name,
                    initial_facts=mention.facts_about
                ))
    
    # 3. Participants get context updates (not full patches)
    for participant in extraction.participants:
        person_path = find_person_folder(participant, context)
        if person_path:
            patches.append(PatchOp(
                target=person_path,
                add_context=f"{extraction.date}: {extraction.summary[:100]}..."
            ))
    
    return patches
```

---

## Persona Integration

Create a persona file that guides extraction and output:

```markdown
# Workflow/prompts/persona.md

## About Me

I'm Jason Vallery, working at VAST Data as [role]. 

## My Priorities
- Cloud partnerships (Microsoft, Google, AWS)
- Enterprise customer relationships
- Technical accuracy in all communications

## What I Care About Extracting
- Commitments made (by me or others)
- Blockers and risks
- Technical decisions and rationale
- Relationship dynamics and key contacts
- Competitive intelligence

## Communication Style
- Direct and concise
- Technical when appropriate
- Professional but personable

## Task Assignment Rules
- If I commit to something → owner is "Myself"
- If someone else commits → use their full name
- If unclear → owner is "TBD"

## Follow-up Preferences
- Important external emails: reply within 24 hours
- Meeting follow-ups: send summary same day
- Action items: create tasks with realistic due dates
```

---

## Implementation Plan

### Phase 1: Shared Foundation (Refactor)
1. Create `pipeline/` module with shared components
2. Move adapters to `pipeline/adapters/`
3. Create `ContextBundle` loader
4. Create unified extraction prompt with context injection

### Phase 2: Unified Extraction
1. Single extraction function that accepts `ContentEnvelope`
2. Persona + manifest injection into system prompt
3. Enhanced `mentioned_entities` with `facts_about`

### Phase 3: Smart Patching
1. Patch entities when facts are discovered (not just primary)
2. Conservative creation policy with review flags
3. Enrichment triggers for new entities

### Phase 4: Output Generation
1. Draft reply generation for emails
2. Calendar invite generation
3. High-priority task surfacing

### Phase 5: Unified CLI
```bash
# Process everything
python scripts/ingest.py --all

# Process specific type
python scripts/ingest.py --type email
python scripts/ingest.py --type transcript

# Process single file
python scripts/ingest.py --file Inbox/Email/example.md

# With outputs + enrichment
python scripts/ingest.py --all --draft-replies --enrich

# Re-process archived sources (after prompt/schema change)
python scripts/ingest.py --source --type email --force --trace-dir ./logs/ai/traces
```

---

## File Structure

```
Workflow/
├── pipeline/
│   ├── __init__.py
│   ├── adapters/
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── transcript.py
│   │   ├── document.py
│   │   └── base.py          # ContentEnvelope, BaseAdapter
│   ├── context.py            # ContextBundle loader
│   ├── extract.py            # Unified extraction
│   ├── patch.py              # Patch generation
│   ├── enrich.py             # Enrichment triggers
│   ├── outputs.py            # Draft generation
│   └── apply.py              # Transactional apply
├── prompts/
│   ├── persona.md            # My context and preferences
│   ├── base.md.j2            # Universal extraction rules
│   ├── extract-unified.md.j2 # Main extraction prompt
│   └── draft-reply.md.j2     # Reply generation prompt
├── scripts/
│   └── ingest.py             # Unified CLI entry point
└── models/
    ├── envelope.py           # ContentEnvelope
    ├── extraction.py         # UnifiedExtraction
    └── changeplan.py         # PatchOp, CreateOp
```

---

## Migration Path

1. **Keep existing scripts working** during transition
2. **New `ingest.py`** calls into `pipeline/` module
3. **Deprecate** `ingest_emails.py` and `ingest_transcripts.py` (wrappers now forward to `ingest.py` with a notice)
4. **Shared code** in `pipeline/` used by both old and new

---

## ChangePlan Validation and Alias Resolution

### ChangePlan Validation

Before applying changes, the `ChangePlan.validate_plan()` method checks:

1. **Required fields**: `source_file` must be set
2. **Path safety**: No `..` path traversal in target paths
3. **Duplicate targets**: Warns if multiple patches target the same file
4. **Non-empty patches**: Patch operations must have at least one change

```python
plan = ChangePlan(source_file="Inbox/Email/test.md", patches=[...])
issues = plan.validate_plan()
if issues:
    print(f"Validation issues: {issues}")
else:
    applier.apply(plan)
```

### Alias Resolution

The `PatchGenerator` uses `EntityIndex` to normalize names via aliases:

1. **Alias lookup**: `"Jeff"` → `"Jeff Denworth"` via `entities/aliases.yaml`
2. **Warnings**: Logs when an alias is resolved to help debugging
3. **Duplicate detection**: Warns if the same entity appears under multiple names

```yaml
# Workflow/entities/aliases.yaml
Jeff Denworth:
  - Jeff
  - Denworth
  - JD
```

When generating patches, if `"Jeff"` and `"Jeff Denworth"` both appear, 
only one patch is created and a warning is logged.

### Dry-Run and Rollback

The `TransactionalApply` class supports:

- **`dry_run=True`**: Reports what would be changed without modifying files
- **Rollback on failure**: Backs up files before modification, restores on error
- **Atomic writes**: Uses temp files + rename to prevent partial writes

---

## Success Criteria

- [x] Single CLI processes all content types
- [x] Extraction has access to persona, manifests, glossary
- [x] Facts about any entity trigger patches (not just primary)
- [x] ChangePlan validation catches common errors
- [x] Alias resolution prevents duplicate patches
- [x] Dry-run mode available for testing
- [ ] New entities trigger enrichment
- [ ] Emails generate draft replies when appropriate
- [ ] All shared logic in `pipeline/` module (no duplication)
