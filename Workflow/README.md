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

# Process all pending Inbox items (emails + transcripts)
python scripts/ingest.py --all --draft-replies --enrich

# Preview without writing changes
python scripts/ingest.py --all --dry-run -v

# Re-process archived sources (e.g., after schema changes)
python scripts/ingest.py --source --type email --force --trace-dir ./logs/ai/traces
```

---

## Pipeline Overview

The system follows a **ChangePlan Pattern** that strictly separates AI reasoning from file execution:

> **Current entry point:** `python scripts/ingest.py --all` wraps normalize → context → extract → plan → apply → outputs.  
> Legacy phase scripts (extract/plan/apply/process_inbox) are deprecated and forward to `ingest.py`; the details below are kept for reference.

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
│  Model:   From config (default gpt-5.2, fallback gpt-4o)                 │
└────────────────────────────────────┬─────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: PLAN              scripts/plan.py                              │
│  ─────────────────────────────────────────────────────────────────────── │
│  Input:   .extraction.json file                                          │
│  AI:      Uses prompts/system-planner.md.j2 with vault context           │
│  Output:  Inbox/_extraction/{filename}.changeplan.json                   │
│  Model:   From config (default gpt-5.2, fallback gpt-4o)                 │
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

| Principle                       | Implementation                               |
| ------------------------------- | -------------------------------------------- |
| **AI reasons, Python executes** | Extract/Plan use AI; Apply is deterministic  |
| **Transactional safety**        | All-or-nothing apply with automatic rollback |
| **Audit trail**                 | Every change is git-committed                |
| **Privacy**                     | `store=False` on all OpenAI API calls        |
| **Schema enforcement**          | Pydantic models + OpenAI Structured Outputs  |

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

Classification uses **heuristics** (pattern matching on filename/content), not LLM:

```
Source File → Classify (Heuristics) → Select Profile → Build Extraction Prompt
                    │
                    ▼
              ┌─────────────────────────────────────┐
              │ profiles/work_sales.yaml            │  Customer/partner meetings
              │ profiles/work_engineering.yaml      │  Technical discussions
              │ profiles/work_leadership.yaml       │  Strategy/planning
              │ profiles/personal.yaml              │  Personal context
              └─────────────────────────────────────┘

Patterns checked (in order):
1. ROB: "office hours", "team sync", "standup", "flight school"
2. Customer: "rfp", "proposal", known account names
3. People: "1-1", "1:1", "weekly with", "sync with"
4. Projects: "sprint", "architecture", "design review"
5. Fallback: Transcripts → people, Emails → customer
```

---

## Scripts Reference

### Core Pipeline Scripts

#### `scripts/ingest.py` — Unified Pipeline Entry Point

- Normalizes Inbox content → loads context → extracts with cached prompts → generates ChangePlans → applies → emits drafts/tasks.
- Defaults to processing Inbox; use `--source` to re-run archived content.

```bash
# Standard run (emails + transcripts, with drafts + enrichment)
python scripts/ingest.py --all --draft-replies --enrich

# Dry run / verbose
python scripts/ingest.py --all --dry-run -v

# Scope by type
python scripts/ingest.py --type email
python scripts/ingest.py --type transcript

# Re-process archived Sources content
python scripts/ingest.py --source --type email --force --trace-dir ./logs/ai/traces

# Single file (vault-relative paths OK)
python scripts/ingest.py --file Inbox/Email/example.md --dry-run
```

Key flags: `--type {email|transcript|document|voice|all}`, `--source`, `--force`, `--enrich`, `--draft-replies`, `--trace-dir`, `--vault-root`.
Key observability flag: `--show-cache-stats` (prints per-run cache + timing summary).

#### Legacy wrappers

`process_inbox.py`, `process_emails.py`, `ingest_emails.py`, and `ingest_transcripts.py` now emit a deprecation notice and forward to `ingest.py`. Phase-specific scripts (extract/plan/apply) live in `Workflow/_archive/` for reference.

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

| File                       | Used By             | Purpose                                    |
| -------------------------- | ------------------- | ------------------------------------------ |
| `base.md.j2`               | All prompts         | Trust boundary, date standards, task rules |
| `system-extractor.md.j2`   | `extract.py`        | Content extraction with profile injection  |
| `system-planner.md.j2`     | `plan.py`           | ChangePlan generation with vault context   |
| `backfill-extractor.md.j2` | `backfill.py`       | Historical note summarization              |
| `audit-readme.md`          | `readme_auditor.py` | Quality assessment prompts                 |

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

| Template         | Note Type | Creates                      |
| ---------------- | --------- | ---------------------------- |
| `people.md.j2`   | people    | Individual meeting notes     |
| `customer.md.j2` | customer  | Multi-party account meetings |
| `partners.md.j2` | partners  | Partner org meetings         |
| `projects.md.j2` | projects  | Project work notes           |
| `rob.md.j2`      | rob       | Rhythm of Business syncs     |
| `journal.md.j2`  | journal   | Personal reflections         |
| `travel.md.j2`   | travel    | Trip notes                   |

**README Templates (for backfill):**

| Template                | Entity Type | Creates                              |
| ----------------------- | ----------- | ------------------------------------ |
| `readme-person.md.j2`   | Person      | Contact info, relationship, context  |
| `readme-customer.md.j2` | Account     | Company info, stakeholders, activity |
| `readme-project.md.j2`  | Project     | Goals, status, milestones            |

### Profile Files (`profiles/`)

Profiles are **extraction rubrics** (not personas) that control what to prioritize:

| Profile                 | When Used                 | Focus                         |
| ----------------------- | ------------------------- | ----------------------------- |
| `work_sales.yaml`       | Customer/partner meetings | Deals, blockers, next steps   |
| `work_engineering.yaml` | Technical discussions     | Architecture, decisions, code |
| `work_leadership.yaml`  | Strategy/planning         | OKRs, priorities, org changes |
| `personal.yaml`         | Personal context          | Relationships, life events    |

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
# OpenAI models by phase (policy-based; see config.yaml for full list)
models:
  privacy:
    store: false
    api: responses

  extract_transcript:
    model: gpt-5.2
    fallback: gpt-4o
    temperature: 0.0

  extract_email:
    model: gpt-5.2
    fallback: gpt-4o
    temperature: 0.0

  planning:
    model: gpt-5.2
    fallback: gpt-4o
    temperature: 0.0

# Paths
paths:
  inbox:
    transcripts: Inbox/Transcripts
    email: Inbox/Email
    extraction: Inbox/_extraction
    archive: Inbox/_archive

  resources:
    prompts: Workflow/prompts
    templates: Workflow/templates
    profiles: Workflow/profiles
```

**Note:** Failed files are moved to `Inbox/_failed/YYYY-MM-DD/` by the scripts on error.

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
│   ├── ingest.py           # Unified pipeline CLI
│   ├── process_inbox.py    # Deprecated wrapper → ingest.py
│   ├── process_emails.py   # Deprecated wrapper → ingest.py
│   ├── ingest_emails.py    # Deprecated wrapper → ingest.py
│   ├── ingest_transcripts.py # Deprecated wrapper → ingest.py
│   ├── manifest_sync.py    # Manifest scan/enrichment
│   ├── dedupe_emails.py    # Inbox dedupe helper
│   ├── audit_import.py     # Validate imported sources
│   ├── cleanup_todo.py     # TODO maintenance
│   └── utils/              # Shared utilities (ai_client, templates, config)
│
├── pipeline/               # Unified pipeline modules
│   ├── adapters/           # Content adapters
│   ├── context.py          # Persona/manifests/glossary loader
│   ├── extract.py          # Unified extraction (LLM)
│   ├── patch.py            # ChangePlan generator
│   ├── apply.py            # Transactional apply
│   ├── outputs.py          # Drafts, calendar, tasks
│   └── pipeline.py         # Orchestrator
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
└── _archive/               # Archived docs (not canonical; see _archive/README.md)
    ├── README.md
    ├── IMPLEMENTATION.md
    ├── REFACTOR.md
    ├── REVIEW-BUNDLE.md
    ├── config_old.py
    └── personas/
```

---

## For AI Agents

### Agent Permissions

Agents have **full autonomy** within this vault. See [AGENTS.md](../AGENTS.md) for details.

### Task Management

- Write tasks into the **source note** as checkbox tasks (`- [?] ...`) tagged `#task`. AI/automation adds `#proposed #auto` and starts tasks at status **Proposed (`?`)**; triage by moving to **Not Started (`[ ]`)** or **In Progress (`/`)**, complete with **Done (`x`)**, reject with **Rejected (`R`)**.
- Use `../TASKS.md` as the **query-only dashboard** (Obsidian Tasks plugin). Completing tasks in the dashboard updates the source note. Proposed items and the quick-capture inbox live under the “Proposed”/“Inbox” sections.

### Common Agent Tasks

#### Process New Inbox Items

```bash
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
python scripts/ingest.py --all --draft-replies --enrich
```

#### Check Pending Items

```bash
# List unprocessed transcripts
ls -la ../Inbox/Transcripts/*.md

# List unprocessed emails
ls -la ../Inbox/Email/*.md

# Check extraction status
ls -la ../Inbox/_extraction/
```

#### Manual Single-File Processing

```bash
# Process one file (vault-relative or absolute)
python scripts/ingest.py --file "../Inbox/Transcripts/2026-01-03 Meeting.md" --dry-run -v
```

#### Create Missing READMEs

```bash
# Use the deterministic migration pipeline to bring the vault into STANDARDS.md compliance
python scripts/migrate.py status
python scripts/migrate.py run --scope VAST --dry-run
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

| Issue                 | Check                               | Fix                                      |
| --------------------- | ----------------------------------- | ---------------------------------------- |
| Extraction fails      | API key valid? Content readable?    | Check `.env`, verify file exists         |
| Plan generates no ops | Extraction complete? Entity exists? | Check `.extraction.json`, verify folder  |
| Apply fails           | Git clean? Paths valid?             | Run `git status`, check ChangePlan paths |
| Rollback triggered    | Check error message                 | Review failed file in `Inbox/_failed/`   |

### File Naming Conventions

| Type         | Pattern                       | Example                           |
| ------------ | ----------------------------- | --------------------------------- |
| Source files | `YYYY-MM-DD HH MM - Title.md` | `2026-01-03 14 30 - Team Sync.md` |
| Dated notes  | `YYYY-MM-DD - Title.md`       | `2026-01-03 - Weekly 1-1.md`      |
| Extraction   | `{source}.extraction.json`    | `meeting.extraction.json`         |
| ChangePlan   | `{source}.changeplan.json`    | `meeting.changeplan.json`         |

---

## Related Documentation

| Document                                                      | Purpose                              |
| ------------------------------------------------------------- | ------------------------------------ |
| [DESIGN.md](DESIGN.md)                                        | Full architecture specification      |
| [REQUIREMENTS.md](REQUIREMENTS.md)                            | Functional requirements              |
| [STANDARDS.md](STANDARDS.md)                                  | File naming, frontmatter conventions |
| [SOURCES_ARCHITECTURE.md](SOURCES_ARCHITECTURE.md)            | Source file organization             |
| [BACKFILL-DESIGN.md](BACKFILL-DESIGN.md)                      | Historical processing details        |
| [AGENTS.md](../AGENTS.md)                                     | AI agent autonomy settings           |
| [copilot-instructions.md](../.github/copilot-instructions.md) | Vault context for AI                 |
