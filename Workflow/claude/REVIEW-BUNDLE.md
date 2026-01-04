# Code Review Bundle: Notes Vault Automation System

> **Generated**: 2025-01-03  
> **Purpose**: Comprehensive analysis for planning LLM to understand system state, identify gaps, and plan improvements

---

## 1. Executive Summary

This is a **local-first Obsidian automation system** for processing meeting transcripts and emails into structured knowledge. The architecture follows a **ChangePlan Pattern** that strictly separates AI reasoning from file execution.

### System Health: 🟡 Functional with Gaps

| Area | Status | Notes |
|------|--------|-------|
| Core Pipeline | 🟢 Working | Extract → Plan → Apply flow operational |
| Pydantic Models | 🟢 Complete | ExtractionV1, ChangePlan, TaskItem, etc. |
| Templates | 🟢 Complete | 11 Jinja2 templates covering all note types |
| Prompts | 🟡 Functional | 5 prompts, but aliases not loaded in planner |
| Config | 🟡 Stale | References non-existent model `gpt-5.2-2025-12-11` |
| Backfill | 🟡 Complete | Full pipeline but separate from main flow |
| Entity Matching | 🟡 Partial | aliases.yaml exists but TODO in plan.py |
| Documentation | 🟢 Good | README.md recently rewritten, DESIGN.md comprehensive |
| Test Coverage | 🔴 Missing | No tests directory or test files found |
| Inbox Queue | 🟡 Pending | 6 transcripts + 7 emails awaiting processing |

---

## 2. Architecture Overview

### 2.1 Pipeline Flow

```
Inbox/Transcripts/*.md  ──┐
Inbox/Email/*.md        ──┼──▶ extract.py ──▶ plan.py ──▶ apply.py
Inbox/Attachments/*     ──┘
        │                        │             │            │
        │                        ▼             ▼            ▼
        │                   .extraction    .changeplan    Vault
        │                      .json         .json       Updates
        │                                                   │
        └───────────────────────────────────────────────────┘
                              (archived to Inbox/_archive/)
```

### 2.2 Key Design Decisions

1. **ChangePlan Pattern**: AI generates JSON operations; Python executes deterministically
2. **Transactional Apply**: Backup → Execute → Rollback on failure
3. **Schema Enforcement**: Pydantic + OpenAI Structured Outputs
4. **Privacy**: All API calls use `store=False`
5. **Headless Operation**: No Obsidian plugins required

### 2.3 File Counts

| Location | Count | Notes |
|----------|-------|-------|
| VAST/People/ | ~125 folders | Each with README.md + dated notes |
| VAST/Customers and Partners/ | ~39 folders | Account-level organization |
| Personal/Projects/ | ~6 folders | Personal project tracking |
| Inbox/Transcripts/ | 6 pending | Unprocessed transcripts |
| Inbox/Email/ | 7 pending | Unprocessed emails |

---

## 3. Codebase Inventory

### 3.1 Core Scripts (`scripts/`)

| File | Lines | Purpose | Dependencies |
|------|-------|---------|--------------|
| `extract.py` | 386 | Phase 1: Content → ExtractionV1 JSON | openai, profiles, prompts |
| `plan.py` | 274 | Phase 2: Extraction → ChangePlan JSON | openai, entities |
| `apply.py` | 382 | Phase 3: ChangePlan → File Updates | git_ops, templates, patch_primitives |
| `process_inbox.py` | 456 | Full pipeline orchestrator | extract, plan, apply |
| `backfill.py` | 645 | Historical content processing CLI | backfill/* modules |
| `classify.py` | ~100 | Note type classification | openai |
| `validate.py` | ~80 | Schema validation | pydantic |
| `config.py` | ~60 | Config loading | yaml |
| `migrate.py` | ~200 | Migration utilities | - |

### 3.2 Utility Modules (`scripts/utils/`)

| Module | Purpose | Used By |
|--------|---------|---------|
| `config.py` | Load config.yaml, env vars | All scripts |
| `openai_client.py` | API client with structured outputs | extract, plan, backfill |
| `entities.py` | Entity matching, folder resolution | plan, extract |
| `git_ops.py` | Git operations (require_clean, commit) | apply |
| `patch_primitives.py` | upsert_frontmatter, append_under_heading | apply |
| `templates.py` | Jinja2 template rendering | apply |
| `profiles.py` | Load extraction profiles | extract |
| `fs.py` | atomic_write, safe_read_text | all |
| `paths.py` | Path resolution utilities | all |
| `validation.py` | ChangePlan validation | plan, apply |
| `standards_check.py` | Frontmatter/filename validation | apply |
| `logging.py` | Structured logging | all |

### 3.3 Backfill Modules (`scripts/backfill/`)

| Module | Purpose |
|--------|---------|
| `scanner.py` | Find notes needing backfill |
| `extractor.py` | AI extraction for historical notes |
| `aggregator.py` | Build README update plans |
| `applier.py` | Transactional README updates |
| `entities.py` | Entity discovery and enrichment |

### 3.4 Models (`models/`)

| Model | Fields | Notes |
|-------|--------|-------|
| `ExtractionV1` | note_type, entity_name, title, date, participants, summary, tasks, decisions, facts, mentions, confidence, warnings | Schema-enforced output from extraction |
| `ChangePlan` | source_file, extraction_file, operations[], warnings[] | Batch of vault operations |
| `Operation` | op, path, template, context, patches, links | Single vault operation |
| `TaskItem` | text, owner, due, priority, confidence | Extracted task |

### 3.5 Templates (`templates/`)

| Template | Type | Used For |
|----------|------|----------|
| `people.md.j2` | Note | 1:1 meeting notes |
| `customer.md.j2` | Note | Customer meeting notes |
| `partners.md.j2` | Note | Partner meeting notes |
| `projects.md.j2` | Note | Project notes |
| `rob.md.j2` | Note | Rhythm of Business notes |
| `journal.md.j2` | Note | Journal entries |
| `travel.md.j2` | Note | Travel notes |
| `readme-person.md.j2` | README | Person folder root doc |
| `readme-customer.md.j2` | README | Account folder root doc |
| `readme-project.md.j2` | README | Project folder root doc |
| `readme-migration.md.j2` | README | Migration template |

### 3.6 Prompts (`prompts/`)

| Prompt | Purpose | Included By |
|--------|---------|-------------|
| `base.md.j2` | Universal rules (trust boundary, dates, tasks) | All extraction prompts |
| `system-extractor.md.j2` | Main extraction prompt with profile injection | extract.py |
| `system-planner.md.j2` | ChangePlan generation prompt | plan.py |
| `backfill-extractor.md.j2` | Historical note summarization | backfill.py |
| `audit-readme.md` | README quality assessment | manual |

### 3.7 Profiles (`profiles/`)

| Profile | Use Case | Key Focus Areas |
|---------|----------|-----------------|
| `work_sales.yaml` | Customer/partner meetings | Deal status, blockers, next steps |
| `work_engineering.yaml` | Technical discussions | Architecture decisions, requirements |
| `work_leadership.yaml` | Strategy/planning | Decisions, priorities, resources |
| `personal.yaml` | Personal context | Personal priorities, home projects |

---

## 4. Issues and Gaps

### 4.1 Critical Issues 🔴

#### 4.1.1 No Test Coverage

**Problem**: Zero test files in the codebase.

**Impact**: 
- Cannot verify pipeline behavior
- Risky to refactor
- No regression protection

**Files Affected**: All scripts

**Recommendation**: Create `tests/` directory with:
- `test_extraction.py` - Model validation
- `test_changeplan.py` - Operation validation  
- `test_apply.py` - Transactional apply tests
- `test_patch_primitives.py` - Frontmatter/heading operations

#### 4.1.2 Config References Non-Existent Model

**Problem**: `config.yaml` references `gpt-5.2-2025-12-11` which doesn't exist.

**Location**: [config.yaml#L68-L95](../config.yaml#L68-L95)

```yaml
classify:
  model: "gpt-5.2-2025-12-11"  # ← This model doesn't exist
```

**Impact**: Pipeline will fail on OpenAI API calls

**Recommendation**: Update to valid model names:
- `gpt-4o` or `gpt-4o-mini` for current production
- `gpt-4.5-preview` if using preview features

### 4.2 High Priority Issues 🟠

#### 4.2.1 Aliases Not Loaded in Planner

**Problem**: The planner prompt has a TODO for loading aliases.

**Location**: [plan.py#L122](../scripts/plan.py#L122)

```python
aliases={},  # TODO: Load from entities/aliases.yaml
```

**Impact**: Entity matching won't use nickname/abbreviation mappings

**Recommendation**: Load aliases in `build_planner_prompt()`:
```python
from scripts.utils.config import workflow_root
import yaml

aliases_path = workflow_root() / "entities" / "aliases.yaml"
aliases = yaml.safe_load(aliases_path.read_text()) if aliases_path.exists() else {}
```

#### 4.2.2 Config Path Mismatch for Resources

**Problem**: `config.yaml` references legacy paths that were archived.

**Location**: [config.yaml#L33-L36](../config.yaml#L33-L36)

```yaml
resources:
  prompts: "Inbox/_bins/_prompts"        # ← Archived/deleted
  subtemplates: "Inbox/_bins/_prompts/subtemplates"  # ← Archived/deleted
  templates: "Inbox/_bins/_templates"    # ← Archived/deleted
```

**Impact**: Scripts may fail if they use these config paths

**Recommendation**: Update to actual locations:
```yaml
resources:
  prompts: "Workflow/prompts"
  templates: "Workflow/templates"
```

#### 4.2.3 Duplicate Emails in Inbox

**Problem**: Some emails appear twice with different sequence numbers.

**Files**:
- `2025-12-14_125503_6117_Your-BetterDisplay-order.md`
- `2025-12-14_125503_6741_Your-BetterDisplay-order.md`
- `2025-12-15_173836_2490_Dont-miss-conversations...`
- `2025-12-15_173836_7937_Dont-miss-conversations...`

**Impact**: May process same content twice

**Recommendation**: Add deduplication check based on content hash before extraction

### 4.3 Medium Priority Issues 🟡

#### 4.3.1 Non-Standard Transcript Filenames

**Problem**: Some transcripts have colons or emojis in filenames that may cause issues.

**Files**:
- `2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen .md`
- `2025-12-17 13:53 - Google Chrome.md`

**Impact**: May cause filesystem issues on some systems

**Recommendation**: Add filename sanitization in MacWhisper output or post-capture hook

#### 4.3.2 Backfill System Not Integrated with Main Pipeline

**Problem**: `backfill.py` is a separate CLI with its own modules, not integrated with `process_inbox.py`.

**Impact**: 
- Duplicate code between `backfill/applier.py` and `apply.py`
- Different patterns for similar operations

**Recommendation**: Consider refactoring to share common utilities

#### 4.3.3 Inconsistent Schema Validation

**Problem**: JSON schemas exist but may not be in sync with Pydantic models.

**Files**:
- `schemas/extraction.schema.json`
- `schemas/changeplan.schema.json`

**Impact**: Schema drift between JSON schema files and Pydantic models

**Recommendation**: Generate JSON schemas from Pydantic models:
```python
from models.extraction import ExtractionV1
print(ExtractionV1.model_json_schema())
```

### 4.4 Low Priority Issues 🟢

#### 4.4.1 Legacy Files in _archive

**Files in `Workflow/_archive/`**:
- `IMPLEMENTATION.md` (5,289 lines) - Old implementation docs
- `REFACTOR.md` - Old migration design
- `REVIEW-BUNDLE.md` - Previous review artifact
- `personas/` - Unused (system uses profiles)

**Recommendation**: These are correctly archived, no action needed

#### 4.4.2 Empty Placeholder Folders

**Folders**:
- `VAST/Journal/` - Empty
- `Personal/Journal/` - Empty
- `VAST/Travel/` - Empty

**Recommendation**: Intentional placeholders, no action needed

#### 4.4.3 Microsoft Contacts.csv in People Folder

**File**: `VAST/People/Microsoft Contacts.csv`

**Impact**: CSV file mixed with person folders

**Recommendation**: Move to `Workflow/entities/` or `VAST/_data/`

---

## 5. Improvement Opportunities

### 5.1 Testing Infrastructure

**Priority**: High

Create comprehensive test suite:

```
tests/
├── __init__.py
├── conftest.py              # Fixtures (mock client, sample data)
├── test_models/
│   ├── test_extraction.py
│   └── test_changeplan.py
├── test_scripts/
│   ├── test_extract.py
│   ├── test_plan.py
│   └── test_apply.py
├── test_utils/
│   ├── test_patch_primitives.py
│   ├── test_entities.py
│   └── test_validation.py
└── fixtures/
    ├── sample_transcript.md
    ├── sample_extraction.json
    └── sample_changeplan.json
```

### 5.2 Error Handling Improvements

**Current**: Errors move files to `_failed/` with error.txt

**Enhancement**: Add structured error reporting:
```python
{
    "file": "original.md",
    "phase": "extract",
    "error_type": "APIError",
    "message": "Rate limit exceeded",
    "timestamp": "2025-01-03T18:00:00",
    "retry_count": 0
}
```

### 5.3 Observability Dashboard

**Current**: Logs in `Workflow/logs/`

**Enhancement**: Create `Workflow/claude/METRICS.md` with:
- Files processed per day
- Success/failure rates
- Token usage tracking
- Common error patterns

### 5.4 Email Deduplication

**Enhancement**: Add content hashing to detect duplicate emails:
```python
import hashlib

def content_hash(content: str) -> str:
    # Strip headers, normalize whitespace
    normalized = " ".join(content.split())
    return hashlib.md5(normalized.encode()).hexdigest()[:12]
```

### 5.5 Profile Auto-Selection

**Current**: Manual profile selection based on folder

**Enhancement**: Use LLM classification to auto-select profile:
```python
def auto_select_profile(content: str) -> str:
    # Use cheap model for classification
    response = classify(content)
    return profile_mapping[response.note_type]
```

---

## 6. Recommended Next Steps

### Phase 1: Immediate Fixes (This Week)

1. **Fix config.yaml model names** - Change `gpt-5.2-*` to valid models
2. **Update resource paths in config** - Point to `Workflow/` locations
3. **Load aliases in planner** - Fix the TODO in plan.py
4. **Dedupe inbox emails** - Remove duplicate captures

### Phase 2: Testing (Next Week)

1. Create `tests/` directory structure
2. Write unit tests for Pydantic models
3. Write tests for patch_primitives
4. Add integration test for extract → plan → apply

### Phase 3: Polish (Following Week)

1. Regenerate JSON schemas from Pydantic models
2. Add content hashing for email deduplication
3. Create metrics tracking
4. Document common failure modes

---

## 7. File Map for Context

```
Workflow/
├── README.md                 # Main documentation (567 lines)
├── DESIGN.md                 # Architecture design (876 lines)
├── REQUIREMENTS.md           # Functional requirements (310 lines)
├── STANDARDS.md              # File conventions (520 lines)
├── config.yaml               # Runtime configuration (384 lines)
├── requirements.txt          # Python dependencies
│
├── models/                   # Pydantic data models
│   ├── extraction.py         # ExtractionV1 schema
│   └── changeplan.py         # ChangePlan schema
│
├── scripts/                  # Automation scripts
│   ├── extract.py            # Phase 1: Extract
│   ├── plan.py               # Phase 2: Plan
│   ├── apply.py              # Phase 3: Apply
│   ├── process_inbox.py      # Orchestrator
│   ├── backfill.py           # Historical processing
│   ├── backfill/             # Backfill modules
│   └── utils/                # Shared utilities
│
├── templates/                # Jinja2 note templates (11 files)
├── prompts/                  # AI prompt templates (5 files)
├── profiles/                 # Extraction rubrics (4 files)
├── schemas/                  # JSON schemas (2 files)
├── entities/                 # Entity aliases
│   └── aliases.yaml
│
├── _archive/                 # Archived documentation
│   ├── IMPLEMENTATION.md
│   ├── REFACTOR.md
│   ├── REVIEW-BUNDLE.md
│   └── personas/
│
└── claude/                   # AI planning artifacts
    └── REVIEW-BUNDLE.md      # This file
```

---

## 8. Context for Planning LLM

When planning improvements to this system, keep in mind:

1. **Privacy is paramount** - All API calls must use `store=False`
2. **Headless operation** - No Obsidian plugins can be triggered by automation
3. **Transactional safety** - Apply phase must be atomic with rollback
4. **Schema enforcement** - Use Pydantic + Structured Outputs, not regex parsing
5. **Git as safety net** - All changes are committed for easy rollback
6. **Separation of concerns** - AI reasons (JSON), Python executes (files)

The system is functional for the happy path but needs hardening around edge cases, testing, and configuration cleanup.
