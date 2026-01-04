# Workflow: Obsidian Vault Automation

> Local-first automation pipeline for processing meeting transcripts, emails, and notes into structured knowledge.

This documentation is for both **human operators** and **AI agents** working with this vault.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Pipeline Overview](#pipeline-overview)
3. [Information Flow](#information-flow)
4. [Scripts Reference](#scripts-reference)
5. [Prompts & Templates](#prompts--templates)
6. [Data Schemas](#data-schemas)
7. [Configuration](#configuration)
8. [Directory Structure](#directory-structure)
9. [For AI Agents](#for-ai-agents)

---

## Quick Start

```bash
# Activate environment
cd ~/Documents/Notes/Workflow
source .venv/bin/activate

# Process all pending inbox items (recommended)
python scripts/process_inbox.py --verbose

# Or run phases individually
python scripts/extract.py --all --dry-run    # Preview what will be extracted
python scripts/plan.py --all                  # Generate change plans
python scripts/apply.py --all                 # Apply changes (transactional)
```

---

## Pipeline Overview

The system follows a **ChangePlan Pattern** that strictly separates AI reasoning from file execution:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           INBOX (Landing Zone)                           │
│  Inbox/Transcripts/*.md    Inbox/Email/*.md    Inbox/Attachments/*       │
└────────────────────────────────────┬─────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: EXTRACT           scripts/extract.py                           │
│  ─────────────────────────────────────────────────────────────────────── │
│  Input:   Raw transcript or email (.md)                                  │
│  AI:      Uses prompts/system-extractor.md.j2 + profile (work_sales etc) │
│  Output:  Inbox/_extraction/{filename}.extraction.json                   │
│  Model:   gpt-4o with Structured Outputs (ExtractionV1 schema)           │
└────────────────────────────────────┬─────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: PLAN              scripts/plan.py                              │
│  ─────────────────────────────────────────────────────────────────────── │
│  Input:   .extraction.json file                                          │
│  AI:      Uses prompts/system-planner.md.j2 with vault context           │
│  Output:  Inbox/_extraction/{filename}.changeplan.json                   │
│  Model:   gpt-4o with Structured Outputs (ChangePlan schema)             │
│  Ops:     create, patch, link (NO archive - that's deterministic)        │
└────────────────────────────────────┬─────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: APPLY             scripts/apply.py                             │
│  ─────────────────────────────────────────────────────────────────────── │
│  Input:   .changeplan.json files                                         │
│  AI:      NONE - purely deterministic Python execution                   │
│  Process: Backup → Execute ops → Archive sources → Git commit            │
│  Output:  New notes, updated READMEs, archived sources                   │
│  Safety:  Transactional - rollback on any failure                        │
└──────────────────────────────────────────────────────────────────────────┘
```

### Key Principles

| Principle | Implementation |
|-----------|----------------|
| **AI reasons, Python executes** | Extract/Plan use AI; Apply is deterministic |
| **Transactional safety** | All-or-nothing apply with automatic rollback |
| **Audit trail** | Every change is git-committed |
| **Privacy** | `store=False` on all OpenAI API calls |
| **Schema enforcement** | Pydantic models + OpenAI Structured Outputs |

---

## Information Flow

### Input → Output Mapping

```
Source File                    Extraction JSON                  ChangePlan JSON                   Vault Changes
─────────────                  ───────────────                  ───────────────                   ─────────────
Inbox/Transcripts/             Inbox/_extraction/               Inbox/_extraction/                VAST/People/{Name}/
  2026-01-03 Meeting.md    →     2026-01-03 Meeting            2026-01-03 Meeting              2026-01-03 - Title.md
                                   .extraction.json          →   .changeplan.json           →  README.md (patched)
                                                                                                 
                                 Contains:                      Contains:                       + archived to:
                                 - note_type                    - create ops                    Inbox/_archive/2026-01-03/
                                 - entity_name                  - patch ops                       original.md
                                 - tasks[]                      - link ops
                                 - decisions[]
                                 - mentions{}
```

### Profile Selection Flow

```
Source File → Classify (AI) → Select Profile → Build Extraction Prompt
                    │
                    ▼
              ┌─────────────────────────────────────┐
              │ profiles/work_sales.yaml            │  Customer/partner meetings
              │ profiles/work_engineering.yaml      │  Technical discussions  
              │ profiles/work_leadership.yaml       │  Strategy/planning
              │ profiles/personal.yaml              │  Personal context
              └─────────────────────────────────────┘
```

---

## Scripts Reference

### Core Pipeline Scripts

#### `scripts/process_inbox.py` — Full Pipeline Orchestrator

```bash
# Process all pending items
python scripts/process_inbox.py

# Options
--scope transcripts|email|all   # Filter by content type
--dry-run                       # Preview without changes
--apply-only                    # Skip extract/plan, apply existing changeplans
--allow-dirty                   # Run even if git tree has changes
--verbose                       # Show detailed progress
```

#### `scripts/extract.py` — Phase 1: Content Extraction

```bash
# Extract single file
python scripts/extract.py --file "Inbox/Transcripts/meeting.md"

# Extract all pending transcripts
python scripts/extract.py --all --scope transcripts

# Extract all pending emails  
python scripts/extract.py --all --scope email

# Dry run
python scripts/extract.py --all --dry-run
```

**Uses:**
- `prompts/system-extractor.md.j2` (includes `base.md.j2`)
- `profiles/*.yaml` for extraction focus
- Outputs: `Inbox/_extraction/*.extraction.json`

#### `scripts/plan.py` — Phase 2: Change Planning

```bash
# Plan all unplanned extractions
python scripts/plan.py --all

# Plan specific extraction
python scripts/plan.py --file "Inbox/_extraction/meeting.extraction.json"

# Dry run
python scripts/plan.py --all --dry-run
```

**Uses:**
- `prompts/system-planner.md.j2` (includes `base.md.j2`)
- `templates/*.md.j2` referenced in plan
- Outputs: `Inbox/_extraction/*.changeplan.json`

#### `scripts/apply.py` — Phase 3: Transactional Apply

```bash
# Apply all pending changeplans
python scripts/apply.py --all

# Dry run (validate without writing)
python scripts/apply.py --all --dry-run

# Allow overwriting existing files
python scripts/apply.py --all --allow-overwrite
```

**Uses:**
- `templates/*.md.j2` for CREATE operations
- `utils/patch_primitives.py` for PATCH operations
- No AI calls - purely deterministic

### Backfill Scripts

#### `scripts/backfill.py` — Historical Content Processing

```bash
# Scan for existing notes
python scripts/backfill.py scan --scope VAST

# Extract metadata from existing notes
python scripts/backfill.py extract --manifest manifest.json

# Aggregate into README updates
python scripts/backfill.py aggregate --extractions extractions.json

# Apply updates
python scripts/backfill.py apply --plan plan.json

# Full pipeline
python scripts/backfill.py run --scope VAST --dry-run
```

**Additional commands:**
```bash
# Sync entity folders with manifests
python scripts/backfill.py sync-manifests

# Enrich entities with web data
python scripts/backfill.py enrich --scope people --limit 10

# Merge duplicate entities
python scripts/backfill.py merge --source "Jon Smith" --target "Jonathan Smith"
```

### Cleanup Scripts

```bash
# Normalize README structure (Profile → Tasks → Context order)
python scripts/cleanup/readme_normalizer.py --dry-run

# Standardize source file names to YYYY-MM-DD format
python scripts/cleanup/source_normalizer.py --dry-run

# AI-powered README quality audit
python scripts/cleanup/readme_auditor.py --file "VAST/People/Name/README.md"
```

---

## Prompts & Templates

### Prompt Files (`prompts/`)

| File | Used By | Purpose |
|------|---------|---------|
| `base.md.j2` | All prompts | Trust boundary, date standards, task rules |
| `system-extractor.md.j2` | `extract.py` | Content extraction with profile injection |
| `system-planner.md.j2` | `plan.py` | ChangePlan generation with vault context |
| `backfill-extractor.md.j2` | `backfill.py` | Historical note summarization |
| `audit-readme.md` | `readme_auditor.py` | Quality assessment prompts |

### Prompt Composition

```
system-extractor.md.j2
├── {% include 'base.md.j2' %}     ← Universal rules (dates, tasks, trust)
├── Profile injection              ← From profiles/*.yaml
├── Classification rules           ← Note type detection
└── ExtractionV1 schema           ← Required JSON structure

system-planner.md.j2  
├── {% include 'base.md.j2' %}     ← Universal rules
├── Path security rules            ← VAST/ and Personal/ only
├── Vault context injection        ← Known entities, folders
├── Operation definitions          ← create, patch, link
└── ChangePlan schema              ← Required JSON structure
```

### Template Files (`templates/`)

| Template | Note Type | Creates |
|----------|-----------|---------|
| `people.md.j2` | people | Individual meeting notes |
| `customer.md.j2` | customer | Multi-party account meetings |
| `partners.md.j2` | partners | Partner org meetings |
| `projects.md.j2` | projects | Project work notes |
| `rob.md.j2` | rob | Rhythm of Business syncs |
| `journal.md.j2` | journal | Personal reflections |
| `travel.md.j2` | travel | Trip notes |

**README Templates (for backfill):**

| Template | Entity Type | Creates |
|----------|-------------|---------|
| `readme-person.md.j2` | Person | Contact info, relationship, context |
| `readme-customer.md.j2` | Account | Company info, stakeholders, activity |
| `readme-project.md.j2` | Project | Goals, status, milestones |

### Profile Files (`profiles/`)

Profiles are **extraction rubrics** (not personas) that control what to prioritize:

| Profile | When Used | Focus |
|---------|-----------|-------|
| `work_sales.yaml` | Customer/partner meetings | Deals, blockers, next steps |
| `work_engineering.yaml` | Technical discussions | Architecture, decisions, code |
| `work_leadership.yaml` | Strategy/planning | OKRs, priorities, org changes |
| `personal.yaml` | Personal context | Relationships, life events |

---

## Data Schemas

### ExtractionV1 (`models/extraction.py`)

```python
class ExtractionV1(BaseModel):
    # Classification
    note_type: Literal["customer", "people", "projects", "rob", "journal", "partners", "travel"]
    entity_name: str | None        # Primary entity (person, account, project)
    
    # Core content
    title: str                     # Brief title (3-7 words)
    date: str                      # YYYY-MM-DD
    participants: list[str]
    summary: str                   # 2-3 sentence summary
    
    # Extracted items
    tasks: list[TaskItem]          # Action items with owner, due, priority
    decisions: list[str]
    facts: list[str]
    mentions: Mentions             # people, projects, accounts
    
    # Confidence
    confidence: float              # 0.0-1.0
    warnings: list[str]            # Flags for review
```

### ChangePlan (`models/changeplan.py`)

```python
class ChangePlan(BaseModel):
    source_file: str               # Original source path
    extraction_file: str           # Path to extraction JSON
    operations: list[Operation]    # create, patch, link ops
    warnings: list[str]

class Operation(BaseModel):
    op: OperationType              # CREATE, PATCH, or LINK
    path: str                      # Target file path
    template: str | None           # For CREATE: template name
    context: CreateContext | None  # For CREATE: template vars
    patches: list[PatchSpec]       # For PATCH: structured patches
    links: list[str]               # For LINK: wikilinks
```

---

## Configuration

### `config.yaml`

```yaml
# OpenAI models by phase
models:
  extract_transcript:
    model: gpt-4o
    temperature: 0.0
  extract_email:
    model: gpt-4o
    temperature: 0.0
  planning:
    model: gpt-4o
    temperature: 0.1

# Paths
paths:
  inbox:
    transcripts: Inbox/Transcripts
    email: Inbox/Email
    extraction: Inbox/_extraction
    archive: Inbox/_archive
    failed: Inbox/_failed

# Privacy
api:
  store: false  # CRITICAL: Never store content in OpenAI
```

### Environment (`.env`)

```bash
OPENAI_API_KEY=sk-...
NOTES_ROOT=/Users/jason/Documents/Notes
```

---

## Directory Structure

```
Workflow/
├── README.md               # This file
├── config.yaml             # Runtime configuration
├── requirements.txt        # Python dependencies
├── .env                    # API keys (gitignored)
│
├── scripts/                # Automation scripts
│   ├── extract.py          # Phase 1: AI extraction
│   ├── plan.py             # Phase 2: AI planning
│   ├── apply.py            # Phase 3: Deterministic apply
│   ├── process_inbox.py    # Full pipeline orchestrator
│   ├── classify.py         # Content classification
│   ├── backfill.py         # Historical processing CLI
│   ├── backfill/           # Backfill submodules
│   │   ├── scanner.py      # Find existing notes
│   │   ├── extractor.py    # Extract from notes
│   │   ├── aggregator.py   # Build update plans
│   │   ├── applier.py      # Apply updates
│   │   └── entities.py     # Entity management
│   ├── cleanup/            # Maintenance scripts
│   │   ├── readme_normalizer.py
│   │   ├── source_normalizer.py
│   │   └── readme_auditor.py
│   └── utils/              # Shared utilities
│       ├── config.py       # Config loading
│       ├── openai_client.py
│       ├── patch_primitives.py
│       ├── templates.py
│       └── ...
│
├── models/                 # Pydantic schemas
│   ├── extraction.py       # ExtractionV1
│   └── changeplan.py       # ChangePlan, Operation
│
├── prompts/                # AI prompts (Jinja2)
│   ├── base.md.j2          # Universal rules
│   ├── system-extractor.md.j2
│   ├── system-planner.md.j2
│   └── backfill-extractor.md.j2
│
├── templates/              # Note templates (Jinja2)
│   ├── people.md.j2
│   ├── customer.md.j2
│   ├── readme-person.md.j2
│   └── ...
│
├── profiles/               # Extraction rubrics
│   ├── work_sales.yaml
│   ├── work_engineering.yaml
│   ├── work_leadership.yaml
│   └── personal.yaml
│
└── _archive/               # Archived documentation
    ├── REFACTOR.md
    └── REVIEW-BUNDLE.md
```

---

## For AI Agents

### Agent Permissions

Agents have **full autonomy** within this vault. See [AGENTS.md](../AGENTS.md) for details.

### Common Agent Tasks

#### Process New Inbox Items

```bash
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
python scripts/process_inbox.py --verbose
```

#### Check Pending Items

```bash
# List unprocessed transcripts
ls -la Inbox/Transcripts/*.md

# List unprocessed emails
ls -la Inbox/Email/*.md

# Check extraction status
ls -la Inbox/_extraction/
```

#### Manual Single-File Processing

```bash
# Extract one file
python scripts/extract.py --file "Inbox/Transcripts/2026-01-03 Meeting.md"

# Generate plan for extraction
python scripts/plan.py --file "Inbox/_extraction/2026-01-03 Meeting.extraction.json"

# Apply the plan
python scripts/apply.py --all
```

#### Create Missing READMEs

```bash
# Use the backfill system to create READMEs for folders without them
python scripts/backfill.py sync-manifests
```

#### Update Stale last_contact Dates

```python
# Find and update from ledger entries
import re
from pathlib import Path

vault = Path('/Users/jason/Documents/Notes')
for readme in vault.rglob('README.md'):
    content = readme.read_text()
    if 'last_contact: unknown' in content:
        # Check for dated entries in Recent Context
        dates = re.findall(r'^\s*-\s*(\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
        if dates:
            latest = sorted(dates, reverse=True)[0]
            # Update frontmatter
```

### Pipeline Troubleshooting

| Issue | Check | Fix |
|-------|-------|-----|
| Extraction fails | API key valid? Content readable? | Check `.env`, verify file exists |
| Plan generates no ops | Extraction complete? Entity exists? | Check `.extraction.json`, verify folder |
| Apply fails | Git clean? Paths valid? | Run `git status`, check ChangePlan paths |
| Rollback triggered | Check error message | Review failed file in `Inbox/_failed/` |

### File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Source files | `YYYY-MM-DD HH MM - Title.md` | `2026-01-03 14 30 - Team Sync.md` |
| Dated notes | `YYYY-MM-DD - Title.md` | `2026-01-03 - Weekly 1-1.md` |
| Extraction | `{source}.extraction.json` | `meeting.extraction.json` |
| ChangePlan | `{source}.changeplan.json` | `meeting.changeplan.json` |

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [DESIGN.md](DESIGN.md) | Full architecture specification |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Functional requirements |
| [STANDARDS.md](STANDARDS.md) | File naming, frontmatter conventions |
| [SOURCES_ARCHITECTURE.md](SOURCES_ARCHITECTURE.md) | Source file organization |
| [BACKFILL-DESIGN.md](BACKFILL-DESIGN.md) | Historical processing details |
| [AGENTS.md](../AGENTS.md) | AI agent autonomy settings |
| [copilot-instructions.md](../.github/copilot-instructions.md) | Vault context for AI |
