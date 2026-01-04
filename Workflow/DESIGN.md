# Design: Local-First Obsidian Automation System

> **Version**: 1.0.0 (Final)  
> **Last Updated**: 2026-01-03  
> **Status**: Locked  
> **Related**: [REQUIREMENTS.md](REQUIREMENTS.md) | [STANDARDS.md](STANDARDS.md)

## 1. System Architecture

The architecture strictly separates **Reasoning (AI)** from **Execution (Python)** to prevent data loss and ensure auditability.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              INGESTION LAYER                                 │
│                         (Daytime Capture - Manual)                           │
├─────────────────┬─────────────────┬─────────────────┬───────────────────────┤
│   Apple Mail    │   MacWhisper    │   Voice Memo    │   Manual Drop         │
│   (⌃⌥⌘M)        │   (Recording)   │   (Dictation)   │   (Finder)            │
└────────┬────────┴────────┬────────┴────────┬────────┴──────────┬────────────┘
         │                 │                 │                   │
         │ .eml + .md      │ .md             │ .md               │ any
         ▼                 ▼                 ▼                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INBOX (Landing Zone)                               │
├─────────────────┬─────────────────┬─────────────────┬───────────────────────┤
│  Inbox/Email/   │Inbox/Transcripts│  Inbox/Voice/   │ Inbox/Attachments/    │
└─────────────────┴─────────────────┴─────────────────┴───────────────────────┘
                                    │
                                    │ End-of-day trigger (manual)
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          EXTRACT PHASE                                       │
│                 (Python + OpenAI Structured Outputs)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. Scan Inbox/* for unprocessed files                                      │
│  2. Classify note type using profile-based rubrics                          │
│  3. Extract structured data via Pydantic-parsed responses                   │
│  4. Write → Inbox/_extraction/{source}.extraction.json                      │
│                                                                              │
│  API: client.responses.parse(..., store=False)  # Schema-enforced           │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PLAN PHASE                                         │
│                 (Python + OpenAI Structured Outputs)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. Load extraction JSON                                                    │
│  2. Generate ChangePlan with explicit operations via Pydantic parsing       │
│  3. LLM plans: create | patch | link (NOT archive)                          │
│  4. Write → Inbox/_extraction/{source}.changeplan.json                      │
│                                                                              │
│  Archive is deterministic post-step, not LLM-generated                      │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLY PHASE                                         │
│                    (Deterministic Python - Transactional)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. Require clean git tree (fail fast if dirty)                             │
│  2. Backup all files to be touched                                          │
│  3. Execute structured patch primitives (no regex)                          │
│  4. On failure: restore backups, delete new files, stop                     │
│  5. On success: archive sources, git commit batch                           │
│                                                                              │
│  NO AI CALLS - Pure deterministic execution with rollback                   │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     │ Next morning
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          REVIEW PHASE                                        │
│                        (Human + VS Code Agent)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. Review git diff of overnight changes                                    │
│  2. Check _Tasks/*.md dashboards (Dataview queries)                         │
│  3. Query #needs-review tag for flagged items                               │
│  4. VS Code Agent for conflict resolution ONLY                              │
│  5. Manual push to remote                                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The ChangePlan Pattern

### 2.1 Why This Pattern?

The previous design allowed AI agents to modify files directly. This creates risks:

- AI hallucinations can corrupt existing notes
- No audit trail of intended vs. actual changes
- Difficult to rollback partial failures
- Mixing reasoning with execution obscures errors

**The ChangePlan pattern separates concerns:**

1. **AI reasons** about what should change (produces schema-enforced plan)
2. **Python executes** the plan deterministically (no AI calls, with rollback)
3. **Human reviews** the results next morning

### 2.2 Key Design Decisions

| Decision                        | Rationale                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Structured Outputs**          | Use `client.responses.parse()` with Pydantic models to guarantee schema adherence at generation time |
| **No `archive` in LLM ops**     | Archive is deterministic post-step; LLM only plans semantic operations                               |
| **Structured patch primitives** | No regex patching; use `upsert_frontmatter`, `append_under_heading`, etc.                            |
| **Transactional apply**         | Backup → Execute → Rollback on failure; batch succeeds or fails atomically                           |
| **Clean git required**          | Fail fast if working directory is dirty (override with `--allow-dirty`)                              |

### 2.3 Operations (LLM-Planned)

The LLM generates only these operations:

| Operation | Description                                    | Example                       |
| --------- | ---------------------------------------------- | ----------------------------- |
| `create`  | Create new file from template                  | New meeting note              |
| `patch`   | Update existing file via structured primitives | Update README.md last_contact |
| `link`    | Insert wikilinks to related entities           | Add [[Person]] references     |

**Not LLM-generated** (deterministic post-steps):

- `archive` — Move source to `Inbox/_archive/YYYY-MM-DD/`
- `commit` — Git commit with run summary

### 2.4 Pydantic Schemas

```python
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class OperationType(str, Enum):
    CREATE = "create"
    PATCH = "patch"
    LINK = "link"

class PatchPrimitive(str, Enum):
    UPSERT_FRONTMATTER = "upsert_frontmatter"
    APPEND_UNDER_HEADING = "append_under_heading"
    ENSURE_WIKILINKS = "ensure_wikilinks"

class FrontmatterPatch(BaseModel):
    key: str
    value: str | list[str] | None

class HeadingPatch(BaseModel):
    heading: str  # e.g., "## Recent Context"
    content: str  # Content to append

class PatchSpec(BaseModel):
    primitive: PatchPrimitive
    frontmatter: list[FrontmatterPatch] | None = None
    heading: HeadingPatch | None = None
    wikilinks: list[str] | None = None

class Operation(BaseModel):
    op: OperationType
    path: str  # Relative to vault root
    template: str | None = None  # For create ops
    context: dict | None = None  # Template variables
    patches: list[PatchSpec] | None = None  # For patch ops
    links: list[str] | None = None  # For link ops

class ChangePlan(BaseModel):
    version: str = "1.0"
    source_file: str
    extraction_file: str
    created_at: datetime
    operations: list[Operation]
    warnings: list[str] = []

class ExtractionV1(BaseModel):
    source_file: str
    processed_at: datetime
    note_type: str
    entity_name: str | None
    title: str
    date: str  # ISO-8601
    participants: list[str]
    summary: str
    tasks: list[dict]
    decisions: list[str]
    facts: list[str]
    mentions: dict  # people, projects, accounts
    confidence: float
```

### 2.5 Example ChangePlan

```json
{
  "version": "1.0",
  "source_file": "Inbox/Transcripts/2026-01-03 14 30 - Jeff Denworth 1-1.md",
  "extraction_file": "Inbox/_extraction/2026-01-03 14 30 - Jeff Denworth 1-1.extraction.json",
  "created_at": "2026-01-03T18:00:00Z",
  "operations": [
    {
      "op": "create",
      "path": "VAST/People/Jeff Denworth/2026-01-03 - Weekly 1-1.md",
      "template": "people.md.j2",
      "context": {
        "title": "Weekly 1-1",
        "date": "2026-01-03",
        "person": "Jeff Denworth",
        "participants": ["Jeff Denworth", "Jason"],
        "summary": "Discussed Q1 pipeline and Google deal status...",
        "source_ref": "Inbox/_archive/2026-01-03/2026-01-03 14 30 - Jeff Denworth 1-1.md",
        "tasks": [
          {
            "text": "Follow up with Google PM on timeline",
            "owner": "Myself",
            "due": "2026-01-06",
            "priority": "high"
          }
        ],
        "decisions": ["Approved new pricing tier for enterprise"],
        "tags": ["type/people", "person/jeff-denworth"]
      }
    },
    {
      "op": "patch",
      "path": "VAST/People/Jeff Denworth/README.md",
      "patches": [
        {
          "primitive": "upsert_frontmatter",
          "frontmatter": [{ "key": "last_contact", "value": "2026-01-03" }]
        },
        {
          "primitive": "append_under_heading",
          "heading": {
            "heading": "## Recent Context",
            "content": "- 2026-01-03: Discussed Q1 pipeline, approved enterprise pricing\n"
          }
        }
      ]
    },
    {
      "op": "link",
      "path": "VAST/People/Jeff Denworth/2026-01-03 - Weekly 1-1.md",
      "links": ["[[Google]]", "[[Enterprise Pricing]]"]
    }
  ],
  "warnings": ["Entity 'Enterprise Pricing' not found - will create new folder"]
}
```

---

## 3. Folder Structure

```
Notes/
├── .github/
│   └── copilot-instructions.md    # AI agent context
├── AGENTS.md                       # Agent autonomy documentation
│
├── Workflow/                       # Automation system
│   ├── REQUIREMENTS.md             # What we're building
│   ├── DESIGN.md                   # How it works (this file)
│   ├── STANDARDS.md                # File/folder/tag conventions
│   ├── config.yaml                 # Runtime configuration
│   ├── requirements.txt            # Python dependencies
│   │
│   ├── scripts/                    # Python automation
│   │   ├── extract.py              # Phase 1: Content → Pydantic JSON
│   │   ├── plan.py                 # Phase 2: JSON → ChangePlan
│   │   ├── apply.py                # Phase 3: ChangePlan → Files (transactional)
│   │   ├── process_inbox.py        # Orchestrator (all phases)
│   │   └── utils/
│   │       ├── config.py           # Config loading
│   │       ├── entities.py         # Entity matching
│   │       ├── git_ops.py          # Git operations
│   │       ├── frontmatter.py      # YAML frontmatter parsing
│   │       └── patch_primitives.py # Structured patch operations
│   │
│   ├── models/                     # Pydantic schemas
│   │   ├── extraction.py           # ExtractionV1
│   │   └── changeplan.py           # ChangePlan, Operation
│   │
│   ├── templates/                  # Jinja2 templates (headless)
│   │   ├── people.md.j2
│   │   ├── customer.md.j2
│   │   ├── projects.md.j2
│   │   ├── rob.md.j2
│   │   └── journal.md.j2
│   │
│   ├── profiles/                   # Extraction rubrics (not personas)
│   │   ├── work_sales.yaml         # Customer/partner meetings
│   │   ├── work_engineering.yaml   # Technical discussions
│   │   ├── work_leadership.yaml    # Strategy/planning
│   │   └── personal.yaml           # Personal context
│   │
│   ├── prompts/                    # AI prompts (Jinja2 templates)
│   │   ├── base.md.j2              # Universal rules
│   │   └── system-extractor.md.j2  # Main extraction prompt
│   │
│   ├── entities/                   # Entity registry
│   │   └── aliases.yaml            # Name → Folder mapping
│   │
│   └── logs/                       # Automation logs
│
├── Inbox/
│   ├── _extraction/                # JSON outputs (gitignored)
│   ├── _archive/                   # Processed sources
│   │   └── YYYY-MM-DD/
│   ├── _failed/                    # Dead letter queue
│   │   └── YYYY-MM-DD/
│   ├── Email/                      # Raw emails (.eml + .md)
│   ├── Transcripts/                # Meeting transcripts
│   └── Attachments/                # Manual drops
│
├── Personal/
│   ├── _Tasks/Personal Tasks.md    # Dataview queries ONLY
│   ├── People/{Name}/README.md
│   ├── Projects/{Project}/README.md
│   └── Journal/
│
└── VAST/
    ├── _Tasks/Work Tasks.md        # Dataview queries ONLY
    ├── Customers and Partners/{Account}/README.md
    ├── People/{Name}/README.md
    ├── Projects/{Project}/README.md
    └── ROB/{Forum}/README.md
```

---

## 4. Component Design

### 4.1 Ingestion: Apple Mail Hotkey

**Implementation**: Apple Shortcut with embedded AppleScript  
**Hotkey**: `⌃⌥⌘M` (Control + Option + Command + M)

```applescript
tell application "Mail"
    set selectedMessages to selection
    repeat with theMessage in selectedMessages
        -- Export raw source for HTML fidelity
        set rawSource to source of theMessage
        set emlPath to inboxPath & "/" & fileName & ".eml"
        writeTextToFile(rawSource, emlPath)

        -- Also save markdown conversion
        set mdContent to convertToMarkdown(theMessage)
        set mdPath to inboxPath & "/" & fileName & ".md"
        writeTextToFile(mdContent, mdPath)
    end repeat
end tell
```

**Output**: For each email, creates:

- `Inbox/Email/YYYY-MM-DD_HHMMSS_{Subject}.eml` (raw source)
- `Inbox/Email/YYYY-MM-DD_HHMMSS_{Subject}.md` (readable markdown)

### 4.2 Ingestion: MacWhisper

**Settings**:

- Output format: **Markdown** (speaker labels preserved)
- Speaker diarization: **Enabled**
- Auto-export path: `~/Documents/Notes/Inbox/Transcripts/`
- Filename pattern: `%Y-%m-%d %H %M - {title}.md`

### 4.3 Extract Phase

**Script**: `Workflow/scripts/extract.py`

```python
#!/usr/bin/env python3
"""
Extract Phase: Raw content → Pydantic-validated JSON

Uses OpenAI Structured Outputs for guaranteed schema adherence.
"""

from openai import OpenAI
from pathlib import Path
from models.extraction import ExtractionV1

def extract_content(source_file: Path, client: OpenAI, profile: dict) -> ExtractionV1:
    """Extract structured data with Pydantic parsing."""

    content = source_file.read_text()
    system_prompt = build_prompt(profile)

    # Schema-enforced extraction via Pydantic
    response = client.responses.parse(
        model="gpt-4o",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content}
        ],
        text_format=ExtractionV1,  # Pydantic model
        store=False  # CRITICAL: Privacy
    )

    extraction = response.output_parsed
    extraction.source_file = str(source_file)

    return extraction
```

### 4.4 Plan Phase

**Script**: `Workflow/scripts/plan.py`

```python
#!/usr/bin/env python3
"""
Plan Phase: Extraction JSON → ChangePlan JSON

LLM generates create/patch/link operations only.
Archive is handled deterministically in apply phase.
"""

from models.changeplan import ChangePlan

def generate_changeplan(extraction: ExtractionV1, client: OpenAI) -> ChangePlan:
    """Generate ChangePlan with Pydantic parsing."""

    # CRITICAL: Filter context to prevent token explosion
    # Only include metadata for entities mentioned in extraction,
    # plus a lightweight list of all entity names for fuzzy matching
    mentioned = set(extraction.participants)
    for entity_list in extraction.mentions.values():
        mentioned.update(entity_list)

    vault_context = {
        "mentioned_entities": get_entity_metadata(mentioned),  # Full details
        "all_entity_names": list_all_entity_names(),           # Strings only
        "aliases": load_aliases()
    }

    response = client.responses.parse(
        model="gpt-4o",
        input=[
            {"role": "system", "content": PLANNER_PROMPT},
            {"role": "user", "content": json.dumps({
                "extraction": extraction.model_dump(),
                "vault_context": vault_context
            })}
        ],
        text_format=ChangePlan,  # Pydantic model
        store=False
    )

    return response.output_parsed
```

### 4.5 Apply Phase (Transactional)

**Script**: `Workflow/scripts/apply.py`

```python
#!/usr/bin/env python3
"""
Apply Phase: ChangePlan → File Updates

TRANSACTIONAL EXECUTION:
1. Require clean git tree (content dirs only, ignoring .obsidian/)
2. Backup all touched files
3. Execute ALL operations from ALL changeplans
4. On failure: restore backups, delete new files
5. On success: archive sources, single git commit for batch
"""

from pathlib import Path
import shutil

# Paths to check for cleanliness (content directories only)
# Ignores .obsidian/ which changes from mobile sync, plugins, etc.
CHECKED_PATHS = ["Inbox/", "VAST/", "Personal/"]

class TransactionalApply:
    def __init__(self, vault_root: Path, run_id: str):
        self.vault_root = vault_root
        self.backup_dir = vault_root / ".workflow_backups" / run_id
        self.created_files: list[Path] = []
        self.backed_up: dict[Path, Path] = {}

    def execute_batch(self, changeplans: list[ChangePlan], source_files: list[Path]):
        """
        Execute ALL changeplans atomically.

        Either all succeed (single git commit) or all fail (full rollback).
        This prevents partial state from processing 10 emails individually.
        """

        # 1. Require clean git tree (content dirs only)
        if not self._git_is_clean(CHECKED_PATHS):
            raise RuntimeError("Git working directory has uncommitted content changes.")

        try:
            # 2. Backup ALL files that will be modified across ALL plans
            for changeplan in changeplans:
                for op in changeplan.operations:
                    target = self.vault_root / op.path
                    if target.exists() and op.op in ["patch", "link"]:
                        self._backup(target)

            # 3. Execute ALL operations from ALL changeplans
            for changeplan in changeplans:
                for op in changeplan.operations:
                    self._apply_operation(op)

            # 4. Archive ALL sources
            for source_file in source_files:
                self._archive_source(source_file)

            # 5. Single git commit for entire batch
            self._git_commit_batch(changeplans)

            # 6. Cleanup backups on success
            shutil.rmtree(self.backup_dir, ignore_errors=True)

        except Exception as e:
            # ROLLBACK: restore backups, delete new files
            self._rollback()
            raise

    def _apply_operation(self, op: Operation):
        """Apply a single operation using structured primitives."""
        target = self.vault_root / op.path

        match op.op:
            case "create":
                self._create_file(target, op.template, op.context)
                self.created_files.append(target)

            case "patch":
                content = target.read_text()
                for patch in op.patches:
                    content = self._apply_patch_primitive(content, patch)
                self._atomic_write(target, content)

            case "link":
                content = target.read_text()
                content = self._ensure_wikilinks(content, op.links)
                self._atomic_write(target, content)

    def _rollback(self):
        """Restore all backups and delete created files."""
        for original, backup in self.backed_up.items():
            shutil.copy2(backup, original)

        for created in self.created_files:
            created.unlink(missing_ok=True)

        shutil.rmtree(self.backup_dir, ignore_errors=True)
```

### 4.6 Structured Patch Primitives

**File**: `Workflow/scripts/utils/patch_primitives.py`

```python
"""
Structured patch operations - NO REGEX for content modification.

These primitives are safe, deterministic, and testable.
"""

import yaml

def upsert_frontmatter(content: str, patches: list) -> str:
    """Update or insert frontmatter fields."""

    # Parse existing frontmatter
    if content.startswith("---"):
        end = content.find("\n---", 3)
        fm_text = content[4:end]
        body = content[end+4:]
        fm = yaml.safe_load(fm_text) or {}
    else:
        fm = {}
        body = content

    # Apply patches
    for patch in patches:
        if patch.value is None:
            fm.pop(patch.key, None)  # Remove
        else:
            fm[patch.key] = patch.value  # Set/update

    # Reconstruct
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    return f"---\n{new_fm}---\n{body}"


def append_under_heading(content: str, heading: str, text: str) -> str:
    """Append text under a specific heading."""

    lines = content.split("\n")
    heading_level = heading.count("#")
    heading_text = heading.lstrip("# ").strip()

    result = []
    inserted = False

    for i, line in enumerate(lines):
        result.append(line)

        if line.strip().startswith("#" * heading_level) and heading_text in line:
            # Find end of section
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith("#") and next_line.count("#") <= heading_level:
                    break
                j += 1

            result.extend(lines[i+1:j])
            result.append(text.rstrip())
            lines = lines[:i+1] + lines[j:]
            inserted = True
            break

    if not inserted:
        result.append("")
        result.append(heading)
        result.append(text.rstrip())

    return "\n".join(result)


def ensure_wikilinks(content: str, links: list[str]) -> str:
    """Ensure wikilinks exist somewhere in the content."""

    for link in links:
        if link.lower() not in content.lower():
            if "## Related" in content:
                content = append_under_heading(content, "## Related", f"- {link}")
            else:
                content += f"\n\n## Related\n\n- {link}\n"

    return content
```

---

## 5. Profiles vs Personas

### 5.1 Why Profiles, Not Personas

**Personas** ("You are a Sales Executive...") are useful for **writing** but risky for **record-keeping**:

- Increase variance in extraction
- "What's important?" shifts subtly between runs
- Makes debugging harder

**Profiles** are **rubrics** that define stable extraction behavior:

- What to prioritize
- What to ignore
- How to classify ambiguous content
- Confidence thresholds

### 5.2 Profile Structure

```yaml
# Workflow/profiles/work_sales.yaml
name: "Sales/Customer Context"
description: "For customer and partner meetings"

focus:
  - Deal status and stage changes
  - Blockers and objections
  - Competitive mentions
  - Next steps and commitments
  - Budget and timeline signals

ignore:
  - Small talk and pleasantries
  - Technical deep-dives (summarize only)
  - Internal process discussions

task_rules:
  confidence_threshold: 0.75
  owner_inference: "If speaker commits, owner is Myself"
  due_date_inference: "Anchor to meeting date; 'next week' = +7 days"

entity_matching:
  auto_create_threshold: 0.90
  needs_review_threshold: 0.80
```

### 5.3 Profile Selection

| Location Pattern                | Profile                            |
| ------------------------------- | ---------------------------------- |
| `VAST/Customers and Partners/*` | `work_sales`                       |
| `VAST/People/*`                 | `work_sales` or `work_engineering` |
| `VAST/Projects/*`               | `work_engineering`                 |
| `VAST/ROB/*`                    | `work_leadership`                  |
| `Personal/*`                    | `personal`                         |

---

## 6. Daily Loop Workflow

### 6.1 Daytime (Capture)

| Activity                     | Output                   |
| ---------------------------- | ------------------------ |
| Record meetings (MacWhisper) | `Inbox/Transcripts/*.md` |
| Hotkey emails (⌃⌥⌘M)         | `Inbox/Email/*.{eml,md}` |
| Drop files                   | `Inbox/Attachments/*`    |

### 6.2 End of Day (Process)

```bash
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
python scripts/process_inbox.py
```

**What happens**:

1. Check git is clean (fail fast if dirty)
2. For each file in `Inbox/*`:
   - Extract → `*.extraction.json`
   - Plan → `*.changeplan.json`
   - Apply (transactional)
3. Archive sources to `Inbox/_archive/YYYY-MM-DD/`
4. Git commit: `[auto] Processed: file1.md, file2.md`

### 6.3 Morning (Review)

| Activity           | Command                        |
| ------------------ | ------------------------------ |
| Review changes     | `git diff HEAD~1`              |
| Check dashboards   | Open `_Tasks/*.md` in Obsidian |
| Find flagged items | Search for `#needs-review`     |
| Resolve conflicts  | VS Code agent (if needed)      |
| Push to remote     | `git push` (manual)            |

---

## 7. Error Handling

### 7.1 Failure Modes

| Error              | Handling                                   |
| ------------------ | ------------------------------------------ |
| Git dirty          | Fail fast, require clean tree              |
| Extraction fails   | Log, move to `_failed/`, continue batch    |
| ChangePlan invalid | Log, skip apply, continue batch            |
| Apply fails        | **Rollback entire run**, flag for review   |
| Entity not found   | Create `_NEW_` prefix, add `#needs-review` |

### 7.2 Dead Letter Queue

```
Inbox/_failed/
└── YYYY-MM-DD/
    ├── {filename}.md        # Original file
    └── {filename}.error.json # Error details
```

### 7.3 Logging

**Location**: `Workflow/logs/YYYY-MM-DD_HHMMSS.log`

Logged metrics:

- Files processed / failed
- API latency and token usage
- Operations applied
- Git commit hash
- Model and profile used per file

---

## 8. AI Model Configuration

### 8.1 Policy-Based Selection

```yaml
# config.yaml
models:
  classification:
    model: "gpt-4o-mini"
    temperature: 0.1

  extraction:
    model: "gpt-4o"
    temperature: 0.2

  planning:
    model: "gpt-4o"
    temperature: 0.1

api:
  store: false # REQUIRED for privacy
  timeout: 60
  max_retries: 3
```

### 8.2 API Usage

```python
# All API calls MUST use Structured Outputs + store=False

response = client.responses.parse(
    model="gpt-4o",
    input=[...],
    text_format=PydanticModel,  # Schema-enforced
    store=False  # Privacy
)
```

---

## 9. Implementation Checklist

### Phase 1: Foundation

- [ ] Create Pydantic models (`models/extraction.py`, `models/changeplan.py`)
- [ ] Create profile YAML files (`profiles/*.yaml`)
- [ ] Set up Python venv with dependencies
- [ ] Create Jinja2 templates

### Phase 2: Extract + Plan

- [ ] Implement `extract.py` with `responses.parse()`
- [ ] Implement `plan.py` with schema-enforced output
- [ ] Test with 5 existing transcripts

### Phase 3: Apply

- [ ] Implement `patch_primitives.py`
- [ ] Implement transactional `apply.py`
- [ ] Implement `process_inbox.py` orchestrator
- [ ] Test rollback behavior

### Phase 4: Polish

- [ ] Error handling and logging
- [ ] Git integration
- [ ] Apple Mail shortcut for .eml export

---

## Appendix A: Headless Operation Guarantee

The pipeline **must not** require:

- Obsidian to be running
- Any Obsidian plugin
- User interaction during processing
- GUI of any kind

All operations are handled by:

- Python + Pydantic for data models
- Jinja2 for templates
- YAML parsing for frontmatter (no regex)
- Git for version control

---

## Appendix B: Security & Privacy

| Requirement      | Implementation                   |
| ---------------- | -------------------------------- |
| No cloud storage | All processing local             |
| API opt-out      | `store=False` on every call      |
| Minimal context  | Profile-guided extraction        |
| Auditability     | Git tracks all changes           |
| Rollback         | Transactional apply with backups |
