# Implementation Plan: Local-First Obsidian Automation

> **Version**: 2.0.0  
> **Created**: 2026-01-03  
> **Last Updated**: 2026-01-03  
> **Status**: Ready for Execution  
> **Related**: [DESIGN.md](DESIGN.md) | [REQUIREMENTS.md](REQUIREMENTS.md) | [STANDARDS.md](STANDARDS.md) | [REFACTOR.md](REFACTOR.md)

This document breaks the automation system into sequenced, Claude-sized implementation steps. Each step is designed to be completable in a single agent session with clear deliverables, test criteria, and gate conditions.

---

## Guiding Constraints (Do Not Violate)

These rules apply to ALL implementation steps:

1. **Local-first + headless**: No Obsidian runtime, no plugin triggers
2. **Reasoning ≠ Execution**: AI only produces schema-enforced JSON; Python performs deterministic file ops
3. **Schema enforcement**: Use `client.responses.parse(..., text_format=PydanticModel, store=False)`
4. **Transactional apply**: Atomic writes + backups + rollback; clean git required
5. **Standards compliance**: Naming, frontmatter, tags, folders per STANDARDS.md
6. **Tasks live only in source notes**: `_Tasks/*.md` contain Dataview queries only
7. **Privacy enforcement**: Always pass `store=False` and use explicit runtime checks (no `assert`) to prevent server-side storage.

---

## Milestone Map (High-Level)

| Milestone | Goal                  | Key Deliverable                              |
| --------- | --------------------- | -------------------------------------------- |
| **M0**    | Foundation            | Repo structure + models + config             |
| **M1**    | Vertical Slice        | One transcript processed end-to-end          |
| **M2**    | Production Hardening  | Logging, DLQ, idempotency, standards checks  |
| **M3**    | Email Integration     | Apple Mail shortcut + email processing       |
| **M4**    | Vault Migration       | migrate.py for existing content              |
| **M5**    | Operational Readiness | Runbooks, test fixtures, safety verification |

---

## Implementation Phases

```
Phase 0: Foundation          → Models, config, project structure, atomic writes
Phase 1: Core Infrastructure → Patch primitives, git ops, entity matching
Phase 2: Templates & Profiles → Jinja2 templates, extraction rubrics
Phase 3: Extract Pipeline    → OpenAI integration, content extraction
Phase 4: Plan Pipeline       → ChangePlan generation from extractions
Phase 5: Apply Pipeline      → Transactional file operations
Phase 6: Orchestration       → process_inbox.py, logging, DLQ
Phase 7: Hardening           → Standards checks, idempotency, test fixtures
Phase 8: Migration           → migrate.py for existing vault content
Phase 9: Ingestion           → Apple Mail hotkey, MacWhisper config
Phase 10: Operational Docs   → Runbooks, troubleshooting guides
```

**Dependency Graph**:

```
Phase 0 ──┬──→ Phase 1 ──→ Phase 5 ──┐
          │                          ├──→ Phase 6 ──→ Phase 7 ──→ Phase 10
          └──→ Phase 2 ──→ Phase 3 ──→ Phase 4 ──┘
                                           │
                         Phase 8 ←─────────┴──→ Phase 9
```

---

## Agent Execution Protocol

For each step, I (Claude) will:

1. **Read** the step requirements and success criteria
2. **Implement** the deliverables (create files, write code)
3. **Test** by running commands in terminal or executing Python
4. **Verify** all success criteria checkboxes pass
5. **Report** completion with evidence (command output, file paths)
6. **Gate**: Only proceed to next step when ALL criteria pass

If a step fails:

- Fix the issue before proceeding
- Re-run verification tests
- Document any deviations from plan

---

## Phase 0: Foundation ✅ COMPLETE

**Goal**: Establish project structure, Pydantic models, configuration loading, and atomic file utilities.

**Milestone**: M0 Foundation  
**Estimated Time**: 1 session  
**Dependencies**: None  
**Status**: ✅ Completed 2026-01-03

---

### Step 0.1: Repository Scaffolding + Safety Defaults

**Objective**: Create the exact folder layout, gitignore entries, and minimal CLI stubs.

**Deliverables**:

```
Workflow/
├── scripts/
│   ├── __init__.py
│   ├── extract.py          # Stub with --help
│   ├── plan.py             # Stub with --help
│   ├── apply.py            # Stub with --help
│   ├── process_inbox.py    # Stub with --help
│   └── utils/
│       └── __init__.py
├── models/
│   └── __init__.py
├── templates/
├── profiles/
├── prompts/
├── entities/
│   └── aliases.yaml        # Empty starter with schema comment
├── logs/                   # Gitignored
├── config.yaml
├── requirements.txt
└── .env.example
```

**Gitignore Entries** (add to vault root `.gitignore`):

```
Workflow/.venv/
Workflow/.env
Workflow/logs/*.log
Inbox/_extraction/*.json
.workflow_backups/
```

**Requirements.txt**:

```
openai>=1.52.0,<2
pydantic>=2.0.0
jinja2>=3.0.0
pyyaml>=6.0
click>=8.0.0
python-frontmatter>=1.0.0
```

**Runtime**:

- Python >= 3.10 (uses `|` union types and Pydantic v2)

**Commands to Execute**:

```bash
cd /Users/jason/Documents/Notes
mkdir -p Workflow/scripts/utils Workflow/models Workflow/templates
mkdir -p Workflow/profiles Workflow/prompts Workflow/entities Workflow/logs
touch Workflow/scripts/__init__.py Workflow/scripts/utils/__init__.py
touch Workflow/models/__init__.py
```

**Verification Commands**:

```bash
tree Workflow/ -I '__pycache__|*.pyc'
python3 -c "import sys; sys.path.insert(0, 'Workflow'); from scripts.utils import *; print('OK')"
```

**Success Criteria**:

- [x] All directories exist per structure above ✅ 2026-01-03
- [x] `python3 -c "from scripts.utils import *"` succeeds (from Workflow dir) ✅ 2026-01-03
- [x] `.gitignore` contains all listed entries ✅ 2026-01-03
- [x] `requirements.txt` contains all dependencies ✅ 2026-01-03
- [x] Each CLI stub responds to `--help` ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03

---

### Step 0.2: Pydantic Models — Extraction

**Objective**: Create the `ExtractionV1` model for structured extraction output.

**File**: `Workflow/models/extraction.py`

**Schema**:

```python
"""Pydantic models for extraction phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal

class TaskItem(BaseModel):
    """A single extracted task/action item."""
    model_config = ConfigDict(extra="forbid")

    text: str
    owner: str | None = None          # "Myself" for first-person
    due: str | None = None            # YYYY-MM-DD
    priority: Literal["highest", "high", "medium", "low", "lowest"] = "medium"

class ExtractionV1(BaseModel):
    """Schema for extracted meeting/email content. Version 1.0."""
    model_config = ConfigDict(extra="forbid")

    version: Literal["1.0"] = "1.0"
    source_file: str
    processed_at: datetime
    note_type: Literal["customer", "people", "projects", "rob", "journal", "partners", "travel"]
    entity_name: str | None = None    # Matched or inferred entity
    title: str
    date: str                         # YYYY-MM-DD (meeting/email date)
    participants: list[str] = Field(default_factory=list)
    summary: str
    tasks: list[TaskItem] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    facts: list[str] = Field(default_factory=list)
    mentions: dict[str, list[str]] = Field(
        default_factory=lambda: {"people": [], "projects": [], "accounts": []}
    )
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
```

**Verification Script** (run in terminal):

```python
import sys; sys.path.insert(0, "Workflow")
from models.extraction import ExtractionV1, TaskItem
from datetime import datetime

# Test basic creation
e = ExtractionV1(
    source_file="test.md",
    processed_at=datetime.now(),
    note_type="people",
    title="Test Meeting",
    date="2026-01-03",
    summary="Test summary"
)
print("✓ Basic creation works")

# Test with tasks
e2 = ExtractionV1(
    source_file="test.md",
    processed_at=datetime.now(),
    note_type="customer",
    title="Customer Call",
    date="2026-01-03",
    summary="Discussed pricing",
    tasks=[TaskItem(text="Follow up", owner="Myself", due="2026-01-10", priority="high")]
)
print("✓ Tasks work")
print(e2.model_dump_json(indent=2))

# Test validation rejects bad priority
try:
    TaskItem(text="bad", priority="invalid")
    print("✗ Should have rejected invalid priority")
except Exception as ex:
    print(f"✓ Validation rejects invalid priority: {type(ex).__name__}")

# Test extra fields rejected
try:
    ExtractionV1(source_file="x", processed_at=datetime.now(), note_type="people",
                 title="x", date="2026-01-01", summary="x", extra_field="bad")
    print("✗ Should have rejected extra field")
except Exception as ex:
    print(f"✓ Extra fields rejected: {type(ex).__name__}")

print("\n=== All ExtractionV1 tests passed ===")
```

**Success Criteria**:

- [x] Model file created at `Workflow/models/extraction.py` ✅ 2026-01-03
- [x] Basic creation works with required fields only ✅ 2026-01-03
- [x] Tasks with all fields serialize correctly ✅ 2026-01-03
- [x] Invalid priority raises ValidationError ✅ 2026-01-03
- [x] Extra fields are rejected (`extra="forbid"`) ✅ 2026-01-03
- [x] JSON round-trip works (`model_dump_json` + `model_validate_json`) ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03

---

### Step 0.3: Pydantic Models — ChangePlan

**Objective**: Create the `ChangePlan` model for operation planning.

**File**: `Workflow/models/changeplan.py`

**Schema**:

```python
"""Pydantic models for the ChangePlan phase output."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum
from typing import Literal

class OperationType(str, Enum):
    """Allowed operation types for ChangePlan."""
    CREATE = "create"
    PATCH = "patch"
    LINK = "link"

class PatchPrimitive(str, Enum):
    """Allowed patch primitives - no regex, only structured operations."""
    UPSERT_FRONTMATTER = "upsert_frontmatter"
    APPEND_UNDER_HEADING = "append_under_heading"
    ENSURE_WIKILINKS = "ensure_wikilinks"

class FrontmatterPatch(BaseModel):
    """A single frontmatter field update."""
    model_config = ConfigDict(extra="forbid")

    key: str
    value: str | list[str] | None  # None = remove key

class HeadingPatch(BaseModel):
    """Content to append under a specific heading."""
    model_config = ConfigDict(extra="forbid")

    heading: str   # e.g., "## Recent Context"
    content: str   # Content to append

class PatchSpec(BaseModel):
    """Specification for a single patch operation."""
    model_config = ConfigDict(extra="forbid")

    primitive: PatchPrimitive
    frontmatter: list[FrontmatterPatch] | None = None
    heading: HeadingPatch | None = None
    wikilinks: list[str] | None = None

class Operation(BaseModel):
    """A single vault operation."""
    model_config = ConfigDict(extra="forbid")

    op: OperationType
    path: str                              # Relative to vault root
    template: str | None = None            # For create ops
    context: dict | None = None            # Template variables
    patches: list[PatchSpec] | None = None # For patch ops
    links: list[str] | None = None         # For link ops

class ChangePlan(BaseModel):
    """Complete plan for vault modifications. NO archive ops - those are deterministic."""
    model_config = ConfigDict(extra="forbid")

    version: Literal["1.0"] = "1.0"
    source_file: str
    extraction_file: str
    created_at: datetime
    operations: list[Operation] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from models.changeplan import (
    ChangePlan, Operation, OperationType, PatchSpec,
    PatchPrimitive, FrontmatterPatch, HeadingPatch
)
from datetime import datetime

# Test CREATE operation
plan1 = ChangePlan(
    source_file="test.md",
    extraction_file="test.extraction.json",
    created_at=datetime.now(),
    operations=[
        Operation(
            op=OperationType.CREATE,
            path="VAST/People/Jeff Denworth/2026-01-03 - Meeting.md",
            template="people.md.j2",
            context={"title": "Meeting", "person": "Jeff Denworth"}
        )
    ]
)
print("✓ CREATE operation works")

# Test PATCH operation
plan2 = ChangePlan(
    source_file="test.md",
    extraction_file="test.extraction.json",
    created_at=datetime.now(),
    operations=[
        Operation(
            op=OperationType.PATCH,
            path="VAST/People/Jeff Denworth/README.md",
            patches=[
                PatchSpec(
                    primitive=PatchPrimitive.UPSERT_FRONTMATTER,
                    frontmatter=[FrontmatterPatch(key="last_contact", value="2026-01-03")]
                ),
                PatchSpec(
                    primitive=PatchPrimitive.APPEND_UNDER_HEADING,
                    heading=HeadingPatch(heading="## Recent Context", content="- 2026-01-03: Meeting notes")
                )
            ]
        )
    ]
)
print("✓ PATCH operation works")
print(plan2.model_dump_json(indent=2))

# Test enums serialize as strings
json_str = plan2.model_dump_json()
assert '"patch"' in json_str, "Enum should serialize as string"
assert '"upsert_frontmatter"' in json_str
print("✓ Enums serialize as strings")

# Test JSON round-trip
plan3 = ChangePlan.model_validate_json(plan2.model_dump_json())
assert plan3.operations[0].op == OperationType.PATCH
print("✓ JSON round-trip works")

# Test invalid operation type rejected
try:
    Operation(op="delete", path="test.md")  # type: ignore
    print("✗ Should have rejected invalid op type")
except Exception as ex:
    print(f"✓ Invalid op type rejected: {type(ex).__name__}")

print("\n=== All ChangePlan tests passed ===")
```

**Success Criteria**:

- [x] Model file created at `Workflow/models/changeplan.py` ✅ 2026-01-03
- [x] CREATE, PATCH, LINK operations work ✅ 2026-01-03
- [x] Nested models (PatchSpec, HeadingPatch) validate correctly ✅ 2026-01-03
- [x] Enums serialize as strings in JSON ✅ 2026-01-03
- [x] JSON round-trip preserves all data ✅ 2026-01-03
- [x] Invalid enum values raise ValidationError ✅ 2026-01-03
- [x] Extra fields are rejected ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03

---

### Step 0.4: Configuration Loading + Path Registry

**Objective**: Centralize configuration and vault-relative path handling.

**Files**:

- `Workflow/config.yaml` - Main configuration
- `Workflow/scripts/utils/config.py` - Config loader
- `Workflow/scripts/utils/paths.py` - Path utilities

**Config Schema** (`Workflow/config.yaml`):

```yaml
# Automation system configuration
# Environment variables can override using ${VAR:-default} syntax

vault:
  root: "${NOTES_ROOT:-/Users/jason/Documents/Notes}"

paths:
  inbox: "Inbox"
  transcripts: "Inbox/Transcripts"
  email: "Inbox/Email"
  extraction: "Inbox/_extraction"
  archive: "Inbox/_archive"
  failed: "Inbox/_failed"
  templates: "Workflow/templates"
  profiles: "Workflow/profiles"
  prompts: "Workflow/prompts"
  entities: "Workflow/entities"
  logs: "Workflow/logs"

# Profile selection based on entity location
profile_mapping:
  "VAST/Customers and Partners/": "work_sales"
  "VAST/People/": "work_sales"
  "VAST/Projects/": "work_engineering"
  "VAST/ROB/": "work_leadership"
  "Personal/": "personal"

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
  store: false # CRITICAL: Privacy - never store on OpenAI
  timeout: 60
  max_retries: 3
```

**Config Loader** (`Workflow/scripts/utils/config.py`):

```python
"""Configuration loading with environment variable support."""

import os
import re
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Any

@dataclass
class ModelConfig:
    model: str
    temperature: float

@dataclass
class Config:
    vault_root: Path
    paths: dict[str, Path]
    profile_mapping: dict[str, str]
    models: dict[str, ModelConfig]
    api_store: bool
    api_timeout: int
    api_max_retries: int

def _expand_env_vars(value: str) -> str:
    """Expand ${VAR:-default} patterns in strings."""
    pattern = r'\$\{(\w+)(?::-([^}]*))?\}'
    def replacer(match):
        var_name = match.group(1)
        default = match.group(2) or ""
        return os.environ.get(var_name, default)
    return re.sub(pattern, replacer, value)

def _process_value(value: Any) -> Any:
    """Recursively expand environment variables in config values."""
    if isinstance(value, str):
        return _expand_env_vars(value)
    elif isinstance(value, dict):
        return {k: _process_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [_process_value(v) for v in value]
    return value

def load_config(config_path: Path | None = None) -> Config:
    """Load configuration from YAML file."""
    if config_path is None:
        config_path = Path(__file__).parent.parent.parent / "config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        raw = yaml.safe_load(f)

    # Expand environment variables
    data = _process_value(raw)

    vault_root = Path(data["vault"]["root"])

    # Convert relative paths to absolute
    paths = {}
    for key, rel_path in data["paths"].items():
        paths[key] = vault_root / rel_path

    # Parse model configs
    models = {}
    for key, cfg in data["models"].items():
        models[key] = ModelConfig(model=cfg["model"], temperature=cfg["temperature"])

    return Config(
        vault_root=vault_root,
        paths=paths,
        profile_mapping=data.get("profile_mapping", {}),
        models=models,
        api_store=data["api"]["store"],
        api_timeout=data["api"]["timeout"],
        api_max_retries=data["api"]["max_retries"],
    )
```

**Path Utilities** (`Workflow/scripts/utils/paths.py`):

```python
"""Path utilities for vault operations."""

from pathlib import Path
from datetime import date

def get_archive_path(vault_root: Path, original_file: Path, archive_date: date | None = None) -> Path:
    """Get archive destination for a source file."""
    if archive_date is None:
        archive_date = date.today()
    return vault_root / "Inbox" / "_archive" / archive_date.isoformat() / original_file.name

def get_extraction_path(vault_root: Path, source_file: Path) -> Path:
    """Get extraction JSON path for a source file."""
    return vault_root / "Inbox" / "_extraction" / f"{source_file.stem}.extraction.json"

def get_changeplan_path(vault_root: Path, source_file: Path) -> Path:
    """Get changeplan JSON path for a source file."""
    return vault_root / "Inbox" / "_extraction" / f"{source_file.stem}.changeplan.json"

def safe_relative_path(vault_root: Path, path: Path | str) -> Path:
    """Convert to vault-relative path, preventing directory traversal."""
    if isinstance(path, str):
        path = Path(path)

    # If already relative, resolve against vault root
    if not path.is_absolute():
        path = vault_root / path

    # Resolve to catch any .. traversal
    resolved = path.resolve()
    vault_resolved = vault_root.resolve()

    # Ensure path is within vault
    try:
        resolved.relative_to(vault_resolved)
    except ValueError:
        raise ValueError(f"Path {path} is outside vault root {vault_root}")

    return resolved.relative_to(vault_resolved)

def ensure_parent_exists(path: Path) -> None:
    """Create parent directories if they don't exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.config import load_config
from scripts.utils.paths import get_archive_path, safe_relative_path
from pathlib import Path
from datetime import date

# Test config loading
cfg = load_config()
print(f"Vault root: {cfg.vault_root}")
print(f"Templates path: {cfg.paths['templates']}")
assert cfg.vault_root.exists(), "Vault root should exist"
assert cfg.api_store == False, "api.store must be False for privacy"
print("✓ Config loads correctly")

# Test path utilities
archive_path = get_archive_path(cfg.vault_root, Path("test.md"), date(2026, 1, 3))
assert "2026-01-03" in str(archive_path)
assert archive_path.name == "test.md"
print(f"✓ Archive path: {archive_path}")

# Test safe path prevents traversal
try:
    safe_relative_path(cfg.vault_root, "../../../etc/passwd")
    print("✗ Should have rejected path traversal")
except ValueError:
    print("✓ Path traversal rejected")

print("\n=== All config/path tests passed ===")
```

**Success Criteria**:

- [x] `config.yaml` created with all sections ✅ 2026-01-03
- [x] `config.py` loads and parses config correctly ✅ 2026-01-03
- [x] Environment variable expansion works (`${VAR:-default}`) ✅ 2026-01-03
- [x] `paths.py` utilities work correctly ✅ 2026-01-03
- [x] Path traversal attacks are rejected ✅ 2026-01-03
- [x] `api.store` is enforced as `false` ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03

---

### Step 0.5: Atomic File Operations

**Objective**: Provide deterministic file read/write primitives used everywhere.

**File**: `Workflow/scripts/utils/fs.py`

**Functions**:

```python
"""Atomic file system operations."""

from pathlib import Path
import tempfile
import os

def atomic_write(path: Path, content: str, encoding: str = "utf-8") -> None:
    """
    Write content to file atomically using temp file + rename.

    This prevents partial writes if the process is interrupted.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write to temp file in same directory (required for atomic rename)
    fd, temp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, 'w', encoding=encoding) as f:
            f.write(content)
        # Atomic rename
        os.replace(temp_path, path)
    except:
        # Clean up temp file on failure
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise

def safe_read_text(path: Path, encoding: str = "utf-8") -> str:
    """Read text file with encoding fallback."""
    try:
        return path.read_text(encoding=encoding)
    except UnicodeDecodeError:
        # Fall back to latin-1 which accepts any byte
        return path.read_text(encoding="latin-1")

def backup_file(source: Path, backup_dir: Path, vault_root: Path) -> Path:
    """Copy file to backup directory, preserving vault-relative structure."""
    import shutil
    rel = source.resolve().relative_to(vault_root.resolve())
    backup_path = backup_dir / rel
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, backup_path)
    return backup_path
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.fs import atomic_write, safe_read_text, backup_file
from pathlib import Path
import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)

    # Test atomic write
    test_file = tmpdir / "subdir" / "test.md"
    atomic_write(test_file, "Hello, World!")
    assert test_file.exists()
    assert test_file.read_text() == "Hello, World!"
    print("✓ Atomic write works (including parent creation)")

    # Test safe read
    content = safe_read_text(test_file)
    assert content == "Hello, World!"
    print("✓ Safe read works")

    # Test backup
    backup_dir = tmpdir / "backups"
    backup_path = backup_file(test_file, backup_dir, tmpdir)
    assert backup_path.exists()
    assert backup_path.read_text() == "Hello, World!"
    print(f"✓ Backup works: {backup_path}")

    # Test atomicity: temp file should not linger on success
    before_files = set(tmpdir.rglob("*.tmp"))
    atomic_write(test_file, "Updated content")
    after_files = set(tmpdir.rglob("*.tmp"))
    assert before_files == after_files, "No temp files should linger"
    print("✓ No temp files linger after success")

print("\n=== All fs tests passed ===")
```

**Success Criteria**:

- [x] `fs.py` created with all functions ✅ 2026-01-03
- [x] `atomic_write` creates parent directories ✅ 2026-01-03
- [x] `atomic_write` uses temp file + rename pattern ✅ 2026-01-03
- [x] No temp files linger after successful write ✅ 2026-01-03
- [x] `safe_read_text` handles encoding gracefully ✅ 2026-01-03
- [x] `backup_file` preserves file content ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - Phase 0 Complete!

---

## Phase 1: Core Infrastructure ✅ COMPLETE

**Goal**: Build the foundational utilities used by all pipeline phases.

**Milestone**: M0 Foundation (completion)  
**Estimated Time**: 1-2 sessions  
**Dependencies**: Phase 0 complete  
**Status**: ✅ Completed 2026-01-03

---

### Step 1.1: Frontmatter Parsing

**Objective**: Create YAML frontmatter parser that handles edge cases safely.

**File**: `Workflow/scripts/utils/frontmatter.py`

**Implementation**:

```python
"""YAML frontmatter parsing and manipulation."""

import yaml
from typing import Any

def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """
    Extract frontmatter dict and body from markdown content.

    Returns (frontmatter_dict, body_content).
    If no frontmatter, returns (None, original_content).
    """
    if not content.startswith("---"):
        return None, content

    # Find the closing ---
    lines = content.split("\n")
    end_index = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index is None:
        # No closing ---, treat as no frontmatter
        return None, content

    fm_text = "\n".join(lines[1:end_index])
    body = "\n".join(lines[end_index + 1:])

    # Handle empty frontmatter
    if not fm_text.strip():
        return {}, body

    try:
        fm = yaml.safe_load(fm_text)
        if fm is None:
            fm = {}
    except yaml.YAMLError:
        # Invalid YAML, return as-is
        return None, content

    return fm, body

def render_frontmatter(fm: dict) -> str:
    """Convert dict to YAML frontmatter block."""
    if not fm:
        return "---\n---\n"

    yaml_content = yaml.dump(
        fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,  # Preserve insertion order
        width=1000,  # Prevent line wrapping
    )
    return f"---\n{yaml_content}---\n"

def update_frontmatter(content: str, updates: dict[str, Any]) -> str:
    """
    Merge updates into existing frontmatter.

    Creates frontmatter if none exists.
    Set value to None to remove a key.
    """
    fm, body = parse_frontmatter(content)

    if fm is None:
        fm = {}

    for key, value in updates.items():
        if value is None:
            fm.pop(key, None)
        else:
            fm[key] = value

    return render_frontmatter(fm) + body
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.frontmatter import parse_frontmatter, render_frontmatter, update_frontmatter

# Test parsing with frontmatter
content = '''---
title: "Test"
tags:
  - one
  - two
---
# Body content

Some text.
'''
fm, body = parse_frontmatter(content)
assert fm["title"] == "Test"
assert len(fm["tags"]) == 2
assert body.strip().startswith("# Body content")
print("✓ Parses frontmatter correctly")

# Test no frontmatter
content2 = "# Just a heading\n\nNo frontmatter here."
fm2, body2 = parse_frontmatter(content2)
assert fm2 is None
assert body2 == content2
print("✓ Handles missing frontmatter")

# Test empty frontmatter
content3 = "---\n---\n# Body"
fm3, body3 = parse_frontmatter(content3)
assert fm3 == {}
assert "# Body" in body3
print("✓ Handles empty frontmatter")

# Test render
fm = {"type": "people", "title": "Test", "tags": ["one", "two"]}
rendered = render_frontmatter(fm)
assert rendered.startswith("---\n")
assert rendered.endswith("---\n")
assert "type: people" in rendered
print("✓ Renders frontmatter correctly")

# Test update
content4 = "---\ntype: old\nkeep: this\n---\n# Body"
updated = update_frontmatter(content4, {"type": "new", "added": "value"})
assert "type: new" in updated
assert "keep: this" in updated
assert "added: value" in updated
print("✓ Updates frontmatter correctly")

# Test update with removal
updated2 = update_frontmatter(content4, {"keep": None})
assert "keep" not in updated2
print("✓ Removes keys with None value")

# Test unicode
content5 = "---\ntitle: Café résumé\n---\n# Body"
fm5, _ = parse_frontmatter(content5)
assert fm5["title"] == "Café résumé"
rendered5 = render_frontmatter(fm5)
assert "Café résumé" in rendered5
print("✓ Handles unicode correctly")

# Test round-trip preservation
original = '''---
type: "people"
title: "Test Title"
date: "2026-01-03"
tags:
  - "type/people"
  - "person/test"
---
# Body content
'''
fm_orig, body_orig = parse_frontmatter(original)
reconstructed = render_frontmatter(fm_orig) + body_orig
fm_check, body_check = parse_frontmatter(reconstructed)
assert fm_check == fm_orig
assert body_check == body_orig
print("✓ Round-trip preserves content")

print("\n=== All frontmatter tests passed ===")
```

**Success Criteria**:

- [x] `frontmatter.py` created with all functions
- [x] Parses valid frontmatter correctly
- [x] Handles missing frontmatter gracefully (returns None, original)
- [x] Handles empty frontmatter (`---\n---`)
- [x] Round-trip preserves content
- [x] Unicode handled correctly
- [x] Update can add, modify, and remove keys

**Gate**: ✅ PASSED 2026-01-03

---

### Step 1.2: Structured Patch Primitives

**Objective**: Implement the three core patch operations (NO REGEX for content modification).

**File**: `Workflow/scripts/utils/patch_primitives.py`

**Design Constraints** (from DESIGN.md):

- Use `frontmatter.py` for YAML operations
- Line-based parsing for headings with **exact level matching**
- Ensure trailing newline before appending content
- Idempotent: running twice produces same result (dedupe via deterministic marker)

**Implementation**:

```python
"""
Structured patch operations - NO REGEX for content modification.

These primitives are safe, deterministic, and testable.
"""

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scripts.utils.frontmatter import parse_frontmatter, render_frontmatter
import hashlib

# Import model types for type hints
from models.changeplan import FrontmatterPatch

def upsert_frontmatter(content: str, patches: list[FrontmatterPatch]) -> str:
    """
    Update or insert frontmatter fields.

    None value = remove key.
    """
    fm, body = parse_frontmatter(content)

    if fm is None:
        fm = {}

    for patch in patches:
        if patch.value is None:
            fm.pop(patch.key, None)
        else:
            fm[patch.key] = patch.value

    return render_frontmatter(fm) + body

def _block_hash(text: str) -> str:
    return hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:12]

def append_under_heading(content: str, heading: str, text: str) -> str:
    """
    Append text under a specific heading.

    CRITICAL: Requires EXACT heading level match.
    - "## Context" matches only "## Context", not "### Context"
    - Creates heading if not found
    - Ensures proper newline spacing
    """
    lines = content.split("\n")
    heading_prefix = heading.split()[0]  # e.g., "##" from "## Context"
    heading_text = heading[len(heading_prefix):].strip()

    # Find the target heading
    target_line = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Must start with exact prefix and have matching text
        if stripped.startswith(heading_prefix + " "):
            line_text = stripped[len(heading_prefix):].strip()
            if line_text.lower() == heading_text.lower():
                target_line = i
                break

    # Deterministic marker for idempotency
    marker = f"<!-- append_under_heading:{_block_hash(text)} -->"

    if target_line is None:
        # Heading not found - append at end with the heading
        if not content.endswith("\n"):
            content += "\n"
        block = f"\n{heading}\n\n{marker}\n{text.rstrip()}\n"
        if block in content:
            return content
        content += block
        return content

    # Find end of section (next heading of same or higher level, or EOF)
    heading_level = len(heading_prefix)  # Number of #
    end_line = len(lines)

    for i in range(target_line + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("#"):
            # Count the heading level
            current_level = 0
            for char in stripped:
                if char == "#":
                    current_level += 1
                else:
                    break
            if current_level <= heading_level:
                end_line = i
                break

    # Insert content before end_line
    # Ensure there's content separation
    insert_text = text.rstrip()

    # Find last non-empty line in section
    last_content_line = target_line
    for i in range(end_line - 1, target_line, -1):
        if lines[i].strip():
            last_content_line = i
            break

    # If marker already exists in this section or exact text present, no-op
    section_text = "\n".join(lines[target_line:end_line])
    if marker in section_text or insert_text.strip() in section_text:
        return content

    # Insert after last content, with blank line if needed
    new_lines = lines[:last_content_line + 1]
    if new_lines[-1].strip():  # If last line has content, add blank line
        new_lines.append("")
    new_lines.append(marker)
    new_lines.append(insert_text)
    new_lines.extend(lines[end_line:])

    return "\n".join(new_lines)

def ensure_wikilinks(content: str, links: list[str]) -> str:
    """
    Ensure wikilinks exist somewhere in content.

    Only adds links that don't already exist (case-insensitive check).
    Adds to ## Related section if missing, creates section if needed.
    """
    content_lower = content.lower()
    missing_links = []

    for link in links:
        # Normalize the link format
        if not link.startswith("[["):
            link = f"[[{link}]]"
        if not link.endswith("]]"):
            link = f"{link}]]"

        # Check if link exists (case-insensitive)
        if link.lower() not in content_lower:
            missing_links.append(link)

    if not missing_links:
        return content  # All links already present

    # Add missing links to ## Related section
    related_content = "\n".join(f"- {link}" for link in missing_links)

    # Check if ## Related exists
    if "## related" in content_lower:
        return append_under_heading(content, "## Related", related_content)
    else:
        # Add ## Related section
        if not content.endswith("\n"):
            content += "\n"
        content += f"\n## Related\n\n{related_content}\n"
        return content
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.patch_primitives import upsert_frontmatter, append_under_heading, ensure_wikilinks
from models.changeplan import FrontmatterPatch

# Test upsert_frontmatter
content = "---\ntype: old\nkeep: value\n---\n# Body"
result = upsert_frontmatter(content, [
    FrontmatterPatch(key="type", value="new"),
    FrontmatterPatch(key="added", value="yes")
])
assert "type: new" in result
assert "keep: value" in result
assert "added: yes" in result
print("✓ upsert_frontmatter adds/updates")

# Test removal
result2 = upsert_frontmatter(content, [FrontmatterPatch(key="keep", value=None)])
assert "keep" not in result2
print("✓ upsert_frontmatter removes with None")

# Test append_under_heading - existing heading
content3 = "# Doc\n\n## Context\n\nExisting content.\n\n## Other Section\n\nMore stuff."
result3 = append_under_heading(content3, "## Context", "- New item")
assert "Existing content." in result3
assert "- New item" in result3
assert result3.index("Existing content.") < result3.index("- New item")
assert result3.index("- New item") < result3.index("## Other Section")
print("✓ append_under_heading works with existing heading")

# Test exact level matching (## should not match ###)
content4 = "# Doc\n\n### Context\n\nWrong level.\n\n## Other"
result4 = append_under_heading(content4, "## Context", "- New item")
# Should create ## Context since ### Context doesn't match
assert "## Context" in result4  # New heading created
assert "### Context" in result4  # Original preserved
print("✓ append_under_heading requires exact level match")

# Test heading creation
content5 = "# Doc\n\nNo context section here."
result5 = append_under_heading(content5, "## Context", "- Added item")
assert "## Context" in result5
assert "- Added item" in result5
print("✓ append_under_heading creates missing heading")

# Test ensure_wikilinks - new links
content6 = "# Doc\n\nSome content about things."
result6 = ensure_wikilinks(content6, ["[[Person A]]", "[[Project B]]"])
assert "[[Person A]]" in result6
assert "[[Project B]]" in result6
assert "## Related" in result6
print("✓ ensure_wikilinks adds missing links")

# Test ensure_wikilinks - idempotent
result7 = ensure_wikilinks(result6, ["[[Person A]]"])
assert result7.count("[[Person A]]") == 1  # Not duplicated
print("✓ ensure_wikilinks is idempotent")

# Test case-insensitive check
content8 = "# Doc\n\nMentions [[person a]] already."
result8 = ensure_wikilinks(content8, ["[[Person A]]"])
assert result8.count("Person A") + result8.count("person a") == 1  # Not added again
print("✓ ensure_wikilinks is case-insensitive")

# Test idempotency of all operations
result_idem = upsert_frontmatter(result, [FrontmatterPatch(key="type", value="new")])
assert result_idem == result
print("✓ Operations are idempotent")

print("\n=== All patch primitive tests passed ===")
```

**Success Criteria**:

- [x] `patch_primitives.py` created with all three functions
- [x] `upsert_frontmatter` adds, updates, and removes keys
- [x] `append_under_heading` inserts under correct heading
- [x] `append_under_heading` requires EXACT level match (`##` ≠ `###`)
- [x] `append_under_heading` creates heading if missing
- [x] `ensure_wikilinks` adds links to ## Related
- [x] `ensure_wikilinks` is idempotent (no duplicates)
- [x] `ensure_wikilinks` is case-insensitive
- [x] All operations preserve existing content

**Gate**: ✅ PASSED 2026-01-03

---

### Step 1.3: Git Operations

**Objective**: Create git helper functions for transactional workflow with smart dirty detection.

**File**: `Workflow/scripts/utils/git_ops.py`

**Design Notes** (from DESIGN.md):

- Only check content directories (`Inbox/`, `VAST/`, `Personal/`)
- Ignore `.obsidian/` changes (mobile sync, plugin updates)
- Fail fast if dirty unless explicitly overridden

**Implementation**:

```python
"""Git operations for transactional workflow."""

import subprocess
from pathlib import Path
from dataclasses import dataclass

# Paths to CHECK for cleanliness (content directories only)
CHECKED_PATHS = ["Inbox/", "VAST/", "Personal/"]

# Paths to IGNORE (frequently change from Obsidian/sync)
IGNORED_PATTERNS = [
    ".obsidian/",
    "Workflow/logs/",
    "Workflow/.venv/",
    ".workflow_backups/",
]

@dataclass
class GitStatus:
    """Git repository status."""
    staged: list[str]
    unstaged: list[str]
    untracked: list[str]

    @property
    def is_clean(self) -> bool:
        return not (self.staged or self.unstaged or self.untracked)

def _run_git(repo_path: Path, *args: str) -> tuple[int, str, str]:
    """Run a git command and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout, result.stderr

def is_git_repo(path: Path) -> bool:
    """Check if path is inside a git repository."""
    code, _, _ = _run_git(path, "rev-parse", "--git-dir")
    return code == 0

def get_status(repo_path: Path, paths: list[str] | None = None) -> GitStatus:
    """
    Get git status, optionally filtered to specific paths.

    Returns GitStatus with staged, unstaged, and untracked files.
    """
    cmd = ["status", "--porcelain"]
    if paths:
        cmd.append("--")
        cmd.extend(paths)

    code, stdout, stderr = _run_git(repo_path, *cmd)
    if code != 0:
        raise RuntimeError(f"git status failed: {stderr}")

    staged = []
    unstaged = []
    untracked = []

    for line in stdout.strip().split("\n"):
        if not line:
            continue

        # Skip ignored patterns
        file_path = line[3:]  # Status is first 2 chars + space
        if any(pattern in file_path for pattern in IGNORED_PATTERNS):
            continue

        index_status = line[0]
        worktree_status = line[1]

        if index_status == "?":
            untracked.append(file_path)
        else:
            if index_status != " ":
                staged.append(file_path)
            if worktree_status != " ":
                unstaged.append(file_path)

    return GitStatus(staged=staged, unstaged=unstaged, untracked=untracked)

def is_clean(repo_path: Path, strict: bool = False) -> bool:
    """
    Check if working directory is clean for automation.

    By default, only checks CHECKED_PATHS.
    If strict=True, checks entire repo.
    """
    paths = None if strict else CHECKED_PATHS
    status = get_status(repo_path, paths)
    return status.is_clean

def require_clean(repo_path: Path, allow_dirty: bool = False) -> None:
    """
    Fail fast if working directory is dirty.

    Raises RuntimeError if dirty (unless allow_dirty=True).
    """
    if allow_dirty:
        return

    if not is_clean(repo_path):
        status = get_status(repo_path, CHECKED_PATHS)
        files = status.staged + status.unstaged + status.untracked
        raise RuntimeError(
            f"Git working directory has uncommitted changes in content directories:\n"
            f"  {', '.join(files[:5])}{'...' if len(files) > 5 else ''}\n"
            f"Commit or stash changes before running automation.\n"
            f"Use --allow-dirty to override (not recommended)."
        )

def add_content_dirs_all(repo_path: Path) -> None:
    """Stage all adds/deletes/renames under content dirs in one shot."""
    code, _, stderr = _run_git(
        repo_path,
        "add", "-A", "--",
        *CHECKED_PATHS,
    )
    if code != 0:
        raise RuntimeError(f"git add -A failed: {stderr}")

def commit(repo_path: Path, message: str) -> str:
    """Create commit and return commit hash."""
    code, stdout, stderr = _run_git(repo_path, "commit", "-m", message)
    if code != 0:
        if "nothing to commit" in stderr or "nothing to commit" in stdout:
            return ""  # No changes to commit
        raise RuntimeError(f"git commit failed: {stderr}")

    # Get the commit hash
    code, stdout, _ = _run_git(repo_path, "rev-parse", "HEAD")
    return stdout.strip()

def get_current_branch(repo_path: Path) -> str:
    """Get current branch name."""
    code, stdout, stderr = _run_git(repo_path, "branch", "--show-current")
    if code != 0:
        raise RuntimeError(f"git branch failed: {stderr}")
    return stdout.strip()
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.git_ops import is_git_repo, get_status, is_clean, require_clean, get_current_branch
from pathlib import Path
import tempfile
import subprocess

vault_root = Path("/Users/jason/Documents/Notes")

# Test is_git_repo
assert is_git_repo(vault_root), "Should be a git repo"
print("✓ is_git_repo works")

# Test get_current_branch
branch = get_current_branch(vault_root)
print(f"✓ Current branch: {branch}")

# Test get_status
status = get_status(vault_root)
print(f"✓ Status: staged={len(status.staged)}, unstaged={len(status.unstaged)}, untracked={len(status.untracked)}")

# Test is_clean (result depends on current state)
clean = is_clean(vault_root)
print(f"✓ is_clean (content dirs): {clean}")

# Test with temp git repo to verify clean detection
with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    subprocess.run(["git", "init"], cwd=tmpdir, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=tmpdir)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmpdir)

    # Create initial commit
    (tmpdir / "README.md").write_text("# Test")
    subprocess.run(["git", "add", "."], cwd=tmpdir)
    subprocess.run(["git", "commit", "-m", "init"], cwd=tmpdir)

    # Should be clean
    assert is_clean(tmpdir, strict=True), "Should be clean after commit"
    print("✓ Clean repo detected as clean")

    # Make dirty
    (tmpdir / "dirty.md").write_text("dirty")
    assert not is_clean(tmpdir, strict=True), "Should be dirty"
    print("✓ Dirty repo detected as dirty")

    # Test require_clean raises
    try:
        require_clean(tmpdir)
        print("✗ Should have raised RuntimeError")
    except RuntimeError as e:
        assert "uncommitted changes" in str(e)
        print("✓ require_clean raises on dirty repo")

    # Test allow_dirty bypasses
    require_clean(tmpdir, allow_dirty=True)  # Should not raise
    print("✓ allow_dirty bypasses check")

print("\n=== All git_ops tests passed ===")
```

**Success Criteria**:

- [x] `git_ops.py` created with all functions
- [x] `is_git_repo` correctly identifies git repos
- [x] `get_status` returns correct file lists
- [x] `is_clean` checks only content directories by default
- [x] `require_clean` raises RuntimeError when dirty
- [x] `require_clean` can be bypassed with `allow_dirty=True`
- [x] Ignored patterns (`.obsidian/`) don't trigger dirty state
- [x] `commit` returns commit hash
- [x] `add_content_dirs_all` stages deletions/renames correctly

**Gate**: ✅ PASSED 2026-01-03

---

### Step 1.4: Entity Matching

**Objective**: Create entity resolution logic using aliases and fuzzy matching.

**Files**:

- `Workflow/entities/aliases.yaml` - Entity alias mappings
- `Workflow/scripts/utils/entities.py` - Entity matching logic

**Aliases Schema** (`Workflow/entities/aliases.yaml`):

```yaml
# Entity alias mappings
# Maps short names/nicknames to canonical folder names

people:
  "Jeff": "Jeff Denworth"
  "JD": "Jeff Denworth"
  "Jonsi": "Jonsi Stephenson"
  "Lior": "Lior Genzel"
  "Karl": "Karl Vietmeier"

accounts:
  "GDC": "Google"
  "MSFT": "Microsoft"
  "OAI": "OpenAI"

projects:
  "AI Collateral": "AI Pipelines Collateral"

# ROB forum mappings if needed
rob_forums: {}
```

**Entity Matcher** (`Workflow/scripts/utils/entities.py`):

```python
"""Entity matching and resolution."""

import yaml
from pathlib import Path
from difflib import SequenceMatcher
from functools import lru_cache

from scripts.utils.config import load_config

@lru_cache(maxsize=1)
def _load_aliases() -> dict:
    """Load aliases from YAML file."""
    config = load_config()
    aliases_path = config.paths["entities"] / "aliases.yaml"

    if not aliases_path.exists():
        return {"people": {}, "accounts": {}, "projects": {}, "rob_forums": {}}

    with open(aliases_path) as f:
        return yaml.safe_load(f) or {}

def _get_entity_base_path(entity_type: str) -> tuple[str, str]:
    """Get (domain, folder) for entity type."""
    mapping = {
        "person": ("VAST", "People"),
        "people": ("VAST", "People"),
        "account": ("VAST", "Customers and Partners"),
        "accounts": ("VAST", "Customers and Partners"),
        "project": ("VAST", "Projects"),
        "projects": ("VAST", "Projects"),
        "rob": ("VAST", "ROB"),
        "rob_forums": ("VAST", "ROB"),
        "personal_person": ("Personal", "People"),
        "personal_project": ("Personal", "Projects"),
    }
    return mapping.get(entity_type, ("VAST", entity_type.title()))

def list_entities(entity_type: str) -> list[str]:
    """
    List all known entities of a type.

    Returns list of entity names (folder names).
    """
    config = load_config()
    domain, folder = _get_entity_base_path(entity_type)
    base_path = config.vault_root / domain / folder

    if not base_path.exists():
        return []

    return [d.name for d in base_path.iterdir() if d.is_dir() and not d.name.startswith("_")]

def list_all_entity_names() -> dict[str, list[str]]:
    """List all entity names by type (lightweight for context)."""
    return {
        "people": list_entities("people"),
        "accounts": list_entities("accounts"),
        "projects": list_entities("projects"),
        "rob": list_entities("rob"),
    }

def match_entity(
    name: str,
    entity_type: str,
    threshold: float = 0.8
) -> tuple[str | None, float]:
    """
    Match name to existing entity.

    Returns (folder_path, confidence).
    - Exact match: confidence = 1.0
    - Alias match: confidence = 0.95
    - Fuzzy match: confidence = similarity score
    - No match: (None, 0.0)
    """
    config = load_config()
    domain, folder = _get_entity_base_path(entity_type)

    # Normalize the input
    name_lower = name.lower().strip()

    # Get known entities
    entities = list_entities(entity_type)
    entities_lower = {e.lower(): e for e in entities}

    # 1. Exact match
    if name_lower in entities_lower:
        canonical = entities_lower[name_lower]
        return f"{domain}/{folder}/{canonical}", 1.0

    # 2. Alias match
    aliases = _load_aliases()
    alias_type = entity_type.rstrip("s")  # "people" -> "people" (keep), "accounts" -> "account"
    if entity_type in aliases:
        alias_map = {k.lower(): v for k, v in aliases[entity_type].items()}
        if name_lower in alias_map:
            canonical = alias_map[name_lower]
            if canonical.lower() in entities_lower:
                canonical = entities_lower[canonical.lower()]
                return f"{domain}/{folder}/{canonical}", 0.95

    # 3. Fuzzy match
    best_match = None
    best_score = 0.0

    for entity in entities:
        score = SequenceMatcher(None, name_lower, entity.lower()).ratio()
        if score > best_score:
            best_score = score
            best_match = entity

    if best_score >= threshold:
        return f"{domain}/{folder}/{best_match}", best_score

    return None, best_score

def suggest_entity_folder(name: str, entity_type: str) -> str:
    """Generate folder path for a new entity."""
    config = load_config()
    domain, folder = _get_entity_base_path(entity_type)

    # Clean up the name for folder use
    clean_name = name.strip()

    return f"{domain}/{folder}/{clean_name}"

def get_entity_metadata(entity_names: set[str]) -> dict:
    """
    Get metadata for mentioned entities.

    Returns dict with entity info for context.
    """
    config = load_config()
    result = {}

    for name in entity_names:
        # Try to match in each type
        for entity_type in ["people", "accounts", "projects"]:
            path, confidence = match_entity(name, entity_type)
            if path and confidence >= 0.8:
                result[name] = {
                    "path": path,
                    "confidence": confidence,
                    "type": entity_type,
                }
                break

    return result
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.entities import match_entity, list_entities, suggest_entity_folder, list_all_entity_names

# Test list_entities (depends on actual vault content)
people = list_entities("people")
print(f"Found {len(people)} people entities")
if people:
    print(f"  Examples: {people[:3]}")

# Test exact match
if "Jeff Denworth" in people:
    path, conf = match_entity("Jeff Denworth", "people")
    assert path == "VAST/People/Jeff Denworth"
    assert conf == 1.0
    print("✓ Exact match works")
else:
    print("⚠ Skipping exact match test (Jeff Denworth not in vault)")

# Test alias match (after we create aliases.yaml)
path, conf = match_entity("Jeff", "people")
if conf >= 0.9:
    print(f"✓ Alias match: {path} (confidence: {conf})")
else:
    print(f"⚠ Alias or fuzzy match: {path} (confidence: {conf})")

# Test fuzzy match
if people:
    # Get first person and try partial match
    first_person = people[0]
    partial = first_person.split()[0] if " " in first_person else first_person[:4]
    path, conf = match_entity(partial, "people", threshold=0.5)
    print(f"✓ Fuzzy match for '{partial}': {path} (confidence: {conf:.2f})")

# Test no match
path, conf = match_entity("Nonexistent Person XYZ", "people")
assert path is None or conf < 0.8
print(f"✓ No match returns None or low confidence: {path}, {conf:.2f}")

# Test suggest_entity_folder
suggestion = suggest_entity_folder("New Person", "people")
assert suggestion == "VAST/People/New Person"
print(f"✓ Suggested folder: {suggestion}")

# Test list_all_entity_names
all_entities = list_all_entity_names()
print(f"✓ All entity names: {sum(len(v) for v in all_entities.values())} total")

print("\n=== All entity matching tests passed ===")
```

**Success Criteria**:

- [x] `aliases.yaml` created with example mappings
- [x] `entities.py` created with all functions
- [x] Exact matches return confidence 1.0
- [x] Alias matches return confidence 0.95
- [x] Fuzzy matching works with configurable threshold
- [x] Unknown entities return `(None, <low_score>)`
- [x] `suggest_entity_folder` generates correct paths
- [x] `list_all_entity_names` returns lightweight name lists

**Gate**: ✅ PASSED 2026-01-03 - All Phase 1 steps complete!

---

## Phase 2: Templates & Profiles ✅ COMPLETE

**Goal**: Create Jinja2 templates and extraction profiles.

**Milestone**: M0 Foundation (completion)  
**Estimated Time**: 1 session  
**Dependencies**: Phase 1 complete
**Status**: ✅ Completed 2026-01-03

---

### Step 2.1: Jinja2 Template Engine

**Objective**: Create template loader with custom filters for note rendering.

**File**: `Workflow/scripts/utils/templates.py`

**Implementation**:

```python
"""Jinja2 template engine for note rendering."""

import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, StrictUndefined
import json

from scripts.utils.config import load_config

def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    # Lowercase
    slug = text.lower()
    # Replace spaces with hyphens
    slug = slug.replace(" ", "-")
    # Remove non-alphanumeric except hyphens
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    # Collapse multiple hyphens
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")

def basename(path: str) -> str:
    """Get the basename of a path."""
    return Path(path).name

def get_template_env() -> Environment:
    """Create Jinja2 environment with custom filters."""
    config = load_config()
    template_dir = config.paths["templates"]

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        undefined=StrictUndefined,  # Fail on undefined variables
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Add custom filters
    env.filters["slugify"] = slugify
    env.filters["basename"] = basename
    env.filters["tojson"] = lambda v, **kw: json.dumps(v, ensure_ascii=False, **kw)

    return env

# Whitelist of allowed templates to mitigate traversal/LLM-controlled names
ALLOWED_TEMPLATES = {
    "people.md.j2",
    "customer.md.j2",
    "projects.md.j2",
    "rob.md.j2",
    "journal.md.j2",
    "readme-migration.md.j2",
}

def render_note(template_name: str, context: dict) -> str:
    """Render a note template with given context."""
    env = get_template_env()
    template = env.get_template(template_name)
    return template.render(**context)
```

**Success Criteria**:

- [x] `templates.py` created with all functions
- [x] `slugify` converts names correctly
- [x] Environment uses `StrictUndefined`
- [x] Templates load from configured path

**Gate**: ✅ PASSED - Proceed to Step 2.2

---

### Step 2.2: Note Templates

**Objective**: Create Jinja2 templates for each note type per STANDARDS.md.

**Files to Create**:

- `Workflow/templates/people.md.j2`
- `Workflow/templates/customer.md.j2`
- `Workflow/templates/projects.md.j2`
- `Workflow/templates/rob.md.j2`
- `Workflow/templates/journal.md.j2`
- `Workflow/templates/readme-migration.md.j2` (for Phase 8)

**Template: people.md.j2**:

```jinja2
---
type: "people"
title: "{{ title }}"
date: "{{ date }}"
person: "{{ person }}"
participants: {{ participants | tojson }}
source: "{{ source }}"
source_ref: "{{ source_ref }}"
tags:
  - "type/people"
  - "person/{{ person | slugify }}"
  - "generated"
---

# {{ title }}

**Date**: {{ date }}
**With**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename }}]]*
```

**Template: customer.md.j2**:

```jinja2
---
type: "customer"
title: "{{ title }}"
date: "{{ date }}"
account: "{{ account }}"
participants: {{ participants | tojson }}
source: "{{ source }}"
source_ref: "{{ source_ref }}"
tags:
  - "type/customer"
  - "account/{{ account | slugify }}"
  - "generated"
---

# {{ title }}

**Date**: {{ date }}
**Account**: [[{{ account }}]]
**Attendees**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename }}]]*
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.templates import render_note, slugify

# Test slugify
assert slugify("Jeff Denworth") == "jeff-denworth"
assert slugify("AI Pipelines Collateral") == "ai-pipelines-collateral"
assert slugify("Test 123!@#") == "test-123"
print("✓ slugify works correctly")

# Test people template
content = render_note("people.md.j2", {
    "title": "Weekly 1-1",
    "date": "2026-01-03",
    "person": "Jeff Denworth",
    "participants": ["Jeff Denworth", "Jason"],
    "summary": "Discussed Q1 goals and pipeline priorities.",
    "tasks": [
        {"text": "Follow up on pricing", "owner": "Myself", "due": "2026-01-10", "priority": "high"},
        {"text": "Review contract", "owner": "Jeff", "due": "2026-01-15", "priority": "medium"}
    ],
    "decisions": ["Approved new pricing tier"],
    "facts": ["Q1 target is $5M"],
    "source": "transcript",
    "source_ref": "Inbox/_archive/2026-01-03/meeting.md"
})

# Verify frontmatter
assert 'type: "people"' in content
assert 'person: "Jeff Denworth"' in content
assert '"type/people"' in content
assert '"person/jeff-denworth"' in content
print("✓ Frontmatter generated correctly")

# Verify content
assert "## Summary" in content
assert "Discussed Q1 goals" in content
assert "## Action Items" in content
assert "@Myself" in content
assert "📅 2026-01-10" in content
assert "⏫" in content  # high priority
assert "## Decisions" in content
assert "Approved new pricing tier" in content
print("✓ Content sections generated correctly")

# Verify source reference
assert "[[meeting.md]]" in content
print("✓ Source reference works")

# Test customer template
content2 = render_note("customer.md.j2", {
    "title": "RFP Review",
    "date": "2026-01-03",
    "account": "Google",
    "participants": ["Alice", "Bob"],
    "summary": "Reviewed RFP requirements.",
    "tasks": [],
    "decisions": [],
    "facts": [],
    "source": "transcript",
    "source_ref": "Inbox/_archive/2026-01-03/google.md"
})

assert 'type: "customer"' in content2
assert 'account: "Google"' in content2
assert "[[Google]]" in content2
print("✓ Customer template works")

# Test strict undefined (should fail on missing var)
try:
    render_note("people.md.j2", {"title": "Test"})  # Missing required vars
    print("✗ Should have raised on undefined variable")
except Exception as e:
    print(f"✓ StrictUndefined catches missing vars: {type(e).__name__}")

print("\n=== All template tests passed ===")
```

**Success Criteria**:

- [x] All 5 note templates created
- [x] Templates produce valid YAML frontmatter
- [x] Required fields present per STANDARDS.md
- [x] Task format matches STANDARDS.md (📅, ⏫, 🔺, #task)
- [x] `source` and `source_ref` included for traceability
- [x] `generated` tag automatically added
- [x] StrictUndefined catches missing variables

**Gate**: ✅ PASSED - All checkboxes passed - Proceed to Step 2.3

---

### Step 2.3: Extraction Profiles

**Objective**: Create profile YAML files that define extraction rubrics.

**Files to Create**:

- `Workflow/profiles/work_sales.yaml`
- `Workflow/profiles/work_engineering.yaml`
- `Workflow/profiles/work_leadership.yaml`
- `Workflow/profiles/personal.yaml`

**Profile Schema** (from DESIGN.md):

```yaml
# work_sales.yaml
name: "Sales/Customer Context"
description: "For customer and partner meetings"

focus:
  - Deal status and stage changes
  - Blockers and objections
  - Competitive mentions
  - Next steps and commitments
  - Budget and timeline signals
  - Key stakeholder positions

ignore:
  - Small talk and pleasantries
  - Deep technical implementation details (summarize only)
  - Internal process discussions unrelated to customer

task_rules:
  confidence_threshold: 0.75
  owner_inference: "If speaker commits to action, owner is 'Myself'"
  due_date_inference: "Anchor to meeting date. 'next week' = +7 days, 'end of month' = last day of current month"

entity_matching:
  auto_create_threshold: 0.90
  needs_review_threshold: 0.80
```

**Profile Loader** (`Workflow/scripts/utils/profiles.py`):

```python
"""Extraction profile loading and selection."""

import yaml
from pathlib import Path
from functools import lru_cache

from scripts.utils.config import load_config

@lru_cache(maxsize=10)
def load_profile(name: str) -> dict:
    """Load profile YAML by name."""
    config = load_config()
    profile_path = config.paths["profiles"] / f"{name}.yaml"

    if not profile_path.exists():
        raise FileNotFoundError(f"Profile not found: {profile_path}")

    with open(profile_path) as f:
        profile = yaml.safe_load(f)

    # Validate required keys
    required = ["name", "description", "focus", "ignore", "task_rules", "entity_matching"]
    for key in required:
        if key not in profile:
            raise ValueError(f"Profile {name} missing required key: {key}")

    return profile

def select_profile(file_path: str) -> str:
    """
    Select appropriate profile based on file location or destination.

    Uses profile_mapping from config.yaml.
    """
    config = load_config()

    # Normalize path
    file_path = file_path.replace("\\", "/")

    for pattern, profile_name in config.profile_mapping.items():
        if pattern in file_path:
            return profile_name

    # Default to personal
    return "personal"

def list_profiles() -> list[str]:
    """List all available profile names."""
    config = load_config()
    profile_dir = config.paths["profiles"]

    if not profile_dir.exists():
        return []

    return [p.stem for p in profile_dir.glob("*.yaml")]
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.profiles import load_profile, select_profile, list_profiles

# Test list_profiles
profiles = list_profiles()
print(f"Available profiles: {profiles}")
assert len(profiles) >= 4, "Should have at least 4 profiles"

# Test load_profile
profile = load_profile("work_sales")
assert profile["name"] == "Sales/Customer Context"
assert "Deal status" in str(profile["focus"])
assert profile["task_rules"]["confidence_threshold"] == 0.75
print("✓ work_sales profile loads correctly")

# Test validation
profile2 = load_profile("work_engineering")
assert "focus" in profile2
assert "task_rules" in profile2
print("✓ work_engineering profile loads correctly")

# Test select_profile
assert select_profile("VAST/People/Jeff/note.md") == "work_sales"
assert select_profile("VAST/Customers and Partners/Google/note.md") == "work_sales"
assert select_profile("VAST/Projects/AI/note.md") == "work_engineering"
assert select_profile("VAST/ROB/Weekly/note.md") == "work_leadership"
assert select_profile("Personal/Projects/Greenhouse/note.md") == "personal"
print("✓ Profile selection works correctly")

# Test missing profile
try:
    load_profile("nonexistent")
    print("✗ Should have raised FileNotFoundError")
except FileNotFoundError:
    print("✓ Missing profile raises FileNotFoundError")

print("\n=== All profile tests passed ===")
```

**Success Criteria**:

- [x] All 4 profile YAML files created
- [x] Profiles contain all required keys
- [x] `load_profile` validates schema
- [x] `select_profile` maps paths correctly per config
- [x] Missing profile raises clear error
- [x] Default falls back to "personal"

**Gate**: ✅ PASSED - All checkboxes passed - Proceed to Step 2.4

---

### Step 2.4: Extraction Prompt Template

**Objective**: Create the system prompt for content extraction.

**File**: `Workflow/prompts/system-extractor.md.j2`

**Template Content**:

```jinja2
You are an extraction assistant for a personal knowledge management system.

## Your Task

Extract structured information from the following {{ source_type }} content.

## Profile: {{ profile.name }}

{{ profile.description }}

### Focus On
{% for item in profile.focus %}
- {{ item }}
{% endfor %}

### Ignore
{% for item in profile.ignore %}
- {{ item }}
{% endfor %}

## Output Rules

1. **Dates**: Use ISO-8601 format (YYYY-MM-DD). Today is {{ today }}.
2. **Task owners**: Use "Myself" for first-person commitments (I will, I'll, I need to)
3. **Due dates**: {{ profile.task_rules.due_date_inference }}
4. **Confidence**: Set < 1.0 if extraction is uncertain
5. **Participants**: Include all mentioned people with full names where possible

## Entity Context

These entities already exist in the knowledge base. Match mentions to these when possible:

**Known people**: {{ known_people | join(", ") if known_people else "None provided" }}
**Known accounts**: {{ known_accounts | join(", ") if known_accounts else "None provided" }}
**Known projects**: {{ known_projects | join(", ") if known_projects else "None provided" }}

For unknown entities, infer the type from context.

## Response Format

Respond with a valid JSON object. No markdown fencing, no explanation—just the JSON.

The response must match this schema:
- version: "1.0"
- source_file: (provided)
- processed_at: (current ISO timestamp)
- note_type: one of "customer", "people", "projects", "rob", "journal", "partners", "travel"
- entity_name: the primary entity this content is about (person name, account name, etc.)
- title: a concise title for this note
- date: the date of the meeting/email (YYYY-MM-DD)
- participants: list of participant names
- summary: 2-3 sentence summary of the key content
- tasks: list of {text, owner, due, priority} - priority is "highest"/"high"/"medium"/"low"/"lowest"
- decisions: list of decisions made
- facts: list of key facts or information to remember
- mentions: {people: [], projects: [], accounts: []} - entities mentioned
- confidence: 0.0-1.0 - your confidence in this extraction
```

**File**: `Workflow/prompts/system-planner.md.j2`

```jinja2
You are a planning assistant for a knowledge management system.

## Your Task

Given extraction JSON, generate a ChangePlan with operations to update the vault.

## Available Operations

1. **create**: Create a new note from template
   - Requires: path, template, context
   - Path format: {Domain}/{EntityType}/{EntityName}/YYYY-MM-DD - {Title}.md

2. **patch**: Update an existing file
   - Uses structured primitives only:
     - upsert_frontmatter: Update/add frontmatter fields
     - append_under_heading: Add content under a heading (creates heading if missing)
     - ensure_wikilinks: Add wikilinks to Related section

3. **link**: Add wikilinks to a file
   - Requires: path, links[]

## Rules

1. Create a dated note in the correct entity folder
2. Patch the entity's README.md to:
   - Update `last_contact` frontmatter field
   - Append brief context to "## Recent Context" section
3. Link mentioned entities with wikilinks
4. Do NOT generate archive operations (handled automatically)
5. Set warnings for:
   - Entity match confidence < 0.9
   - New entities that would be created
   - Uncertain mappings

## Vault Context

{{ vault_context | tojson(indent=2) }}

## Extraction Data

{{ extraction | tojson(indent=2) }}

## Response Format

Respond with a valid JSON ChangePlan. No markdown fencing.
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
from scripts.utils.templates import get_template_env
from scripts.classify import classify  # Step 3.0
from scripts.utils.profiles import load_profile
from datetime import date
from pathlib import Path

# Load prompts environment (separate from note templates)
config_path = Path("Workflow")
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(str(config_path / "prompts")),
    trim_blocks=True,
    lstrip_blocks=True,
)

# Test extractor prompt
profile = load_profile("work_sales")
template = env.get_template("system-extractor.md.j2")

prompt = template.render(
    source_type="transcript",
    profile=profile,
    today=date.today().isoformat(),
    known_people=["Jeff Denworth", "Jonsi Stephenson"],
    known_accounts=["Google", "Microsoft"],
    known_projects=["AI Pipelines"],
)

assert "Sales/Customer Context" in prompt
assert "Deal status" in prompt
assert "YYYY-MM-DD" in prompt
assert "Jeff Denworth" in prompt
print("✓ Extractor prompt renders correctly")

# Test planner prompt
planner = env.get_template("system-planner.md.j2")
plan_prompt = planner.render(
    vault_context={"entities": ["Jeff Denworth"]},
    extraction={"title": "Test", "note_type": "people"}
)

assert "create" in plan_prompt
assert "patch" in plan_prompt
assert "README.md" in plan_prompt
print("✓ Planner prompt renders correctly")

print("\n=== All prompt tests passed ===")
```

**Success Criteria**:

- [x] `system-extractor.md.j2` created
- [x] `system-planner.md.j2` created
- [x] Prompts render with profile content
- [x] Entity context injects correctly
- [x] Date rules are clear
- [x] Response format instructions are explicit

**Gate**: ✅ PASSED - All checkboxes passed - Phase 2 Complete

---

## Phase 3: Extract Pipeline ✅ COMPLETE

**Goal**: Implement the extraction phase using OpenAI Structured Outputs.

**Milestone**: M1 Vertical Slice  
**Estimated Time**: 1-2 sessions  
**Dependencies**: Phase 2 complete
**Status**: ✅ Completed 2026-01-03

---

### Step 3.0: Pre-Extraction Classification

Add a pre-extraction classification step to select the correct profile for Inbox sources (Transcripts/Email) where vault destination is unknown.

**File**: `Workflow/scripts/classify.py`

**Behavior**:

- Input: `source_path`, raw text
- Output: `{ note_type, likely_domain_path_prefix }`
- Start with heuristics by folder name; can be upgraded to a small model later.

**Success Criteria**:

- [x] Returns a `note_type` for transcripts/emails
- [x] Integrates with `select_profile()`
- [x] Unit tests cover both inbox types

**Gate**: ✅ PASSED - Proceed to Step 3.1

---

### Step 3.1: OpenAI Client Wrapper

**Objective**: Create OpenAI client wrapper with `responses.parse()` support and privacy enforcement.

**File**: `Workflow/scripts/utils/openai_client.py`

**Implementation**:

```python
"""OpenAI client wrapper with Structured Outputs support."""

import os
import time
from typing import TypeVar
from openai import OpenAI
from pydantic import BaseModel

from scripts.utils.config import load_config

T = TypeVar("T", bound=BaseModel)

def get_client() -> OpenAI:
    """Create OpenAI client from environment."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    return OpenAI(api_key=api_key)

def parse_structured(
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_content: str,
    response_model: type[T],
    temperature: float = 0.2,
    max_retries: int = 3,
) -> tuple[T, dict]:
    """
    Call OpenAI with Pydantic schema enforcement.

    Returns (parsed_response, metadata).
    Metadata includes: tokens, latency_ms, model_used.

    CRITICAL: Always uses store=False for privacy.
    """
    config = load_config()

    # Enforce privacy (no asserts in production)
    if config.api_store:
        raise RuntimeError("api.store must be False for privacy")

    start_time = time.time()
    last_error = None

    for attempt in range(max_retries):
        try:
            response = client.responses.parse(
                model=model,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                text_format=response_model,
                store=False,  # CRITICAL: Privacy
                temperature=temperature,
            )

            latency_ms = int((time.time() - start_time) * 1000)

            metadata = {
                "latency_ms": latency_ms,
                "model": model,
                "attempt": attempt + 1,
            }

            # Extract token usage if available
            if hasattr(response, "usage") and response.usage:
                metadata["input_tokens"] = response.usage.input_tokens
                metadata["output_tokens"] = response.usage.output_tokens

            return response.output_parsed, metadata

        except Exception as e:
            last_error = e
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            continue

    raise RuntimeError(f"OpenAI call failed after {max_retries} attempts: {last_error}")
```

**Verification Script**:

```python
import sys; sys.path.insert(0, "Workflow")
import os

# Skip if no API key
if not os.environ.get("OPENAI_API_KEY"):
    print("⚠ Skipping OpenAI tests (no API key)")
    print("Set OPENAI_API_KEY to run integration tests")
    exit(0)

from scripts.utils.openai_client import get_client, parse_structured
from pydantic import BaseModel

class SimpleExtract(BaseModel):
    title: str
    date: str

client = get_client()
print("✓ Client created")

result, metadata = parse_structured(
    client=client,
    model="gpt-4o-mini",
    system_prompt="Extract a title and date from the text. Respond with JSON.",
    user_content="Meeting on January 3rd, 2026 about Q1 Planning",
    response_model=SimpleExtract,
    temperature=0.1
)

assert result.title, "Should have extracted a title"
assert "2026" in result.date, "Should have extracted date"
print(f"✓ Extracted: {result.title}, {result.date}")
print(f"✓ Metadata: {metadata}")

assert "latency_ms" in metadata
print("✓ Latency tracked")

print("\n=== All OpenAI client tests passed ===")
```

**Success Criteria**:

- [x] `openai_client.py` created
- [x] `get_client()` uses environment variable
- [x] `parse_structured()` returns Pydantic model
- [x] `store=False` is always used (privacy)
- [x] Retry logic with exponential backoff
- [x] Metadata includes latency and tokens
- [x] Missing API key raises clear error

**Gate**: ✅ PASSED - Proceed to Step 3.2

---

### Step 3.2: Extract Script

**Objective**: Create the main extraction script for processing inbox content.

**File**: `Workflow/scripts/extract.py`

**CLI Interface**:

```bash
# Extract single file
python scripts/extract.py --file "Inbox/Transcripts/2026-01-03 - Meeting.md"

# Extract all pending in Transcripts
python scripts/extract.py --all --scope transcripts

# Dry run (show what would be extracted)
python scripts/extract.py --all --dry-run
```

**Implementation**:

```python
#!/usr/bin/env python3
"""
Extract Phase: Raw content → ExtractionV1 JSON

Uses OpenAI Structured Outputs for guaranteed schema adherence.
"""

import sys
import json
import click
from pathlib import Path
from datetime import datetime, date

# Add Workflow to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.extraction import ExtractionV1
from scripts.utils.config import load_config
from scripts.utils.paths import get_extraction_path
from scripts.utils.fs import safe_read_text, atomic_write
from scripts.utils.profiles import load_profile, select_profile
from scripts.utils.entities import list_all_entity_names
from scripts.utils.openai_client import get_client, parse_structured
from scripts.utils.templates import get_template_env

def find_unprocessed(config, scope: str = "transcripts") -> list[Path]:
    """Find files without corresponding .extraction.json."""
    scope_paths = {
        "transcripts": config.paths["transcripts"],
        "email": config.paths["email"],
    }

    inbox_path = scope_paths.get(scope, config.paths["transcripts"])

    if not inbox_path.exists():
        return []

    unprocessed = []
    for f in inbox_path.glob("*.md"):
        extraction_path = get_extraction_path(config.vault_root, f)
        if not extraction_path.exists():
            unprocessed.append(f)

    return sorted(unprocessed)

def build_extraction_prompt(source_type: str, profile: dict, entity_names: dict) -> str:
    """Build the extraction system prompt."""
    from jinja2 import Environment, FileSystemLoader

    config = load_config()
    env = Environment(
        loader=FileSystemLoader(str(config.paths["prompts"])),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template("system-extractor.md.j2")
    return template.render(
        source_type=source_type,
        profile=profile,
        today=date.today().isoformat(),
        known_people=entity_names.get("people", [])[:50],  # Limit context
        known_accounts=entity_names.get("accounts", [])[:20],
        known_projects=entity_names.get("projects", [])[:20],
    )

def extract_file(source: Path, client, config) -> tuple[ExtractionV1, dict]:
    """Extract structured data from a single file."""
    content = safe_read_text(source)

    # Determine source type and profile
    source_type = "transcript" if "Transcripts" in str(source) else "email"
    # Use classifier to select profile deterministically for Inbox sources
    cls = classify(str(source), content)
    profile_name = select_profile(cls.get("likely_domain_path_prefix", str(source)))
    profile = load_profile(profile_name)

    # Get entity context
    entity_names = list_all_entity_names()

    # Build prompt
    system_prompt = build_extraction_prompt(source_type, profile, entity_names)

    # Call OpenAI
    extraction, metadata = parse_structured(
        client=client,
        model=config.models["extraction"].model,
        system_prompt=system_prompt,
        user_content=content,
        response_model=ExtractionV1,
        temperature=config.models["extraction"].temperature,
    )

    # Set source file
    extraction.source_file = str(source.relative_to(config.vault_root))

    return extraction, metadata

def save_extraction(extraction: ExtractionV1, output_path: Path) -> None:
    """Save extraction JSON to disk."""
    json_str = extraction.model_dump_json(indent=2)
    atomic_write(output_path, json_str)

@click.command()
@click.option("--file", "file_path", type=click.Path(exists=True), help="Extract single file")
@click.option("--all", "extract_all", is_flag=True, help="Extract all pending files")
@click.option("--scope", default="transcripts", type=click.Choice(["transcripts", "email"]))
@click.option("--dry-run", is_flag=True, help="Show what would be extracted")
def main(file_path: str | None, extract_all: bool, scope: str, dry_run: bool):
    """Extract structured data from inbox content."""
    config = load_config()

    if file_path:
        files = [Path(file_path)]
    elif extract_all:
        files = find_unprocessed(config, scope)
    else:
        click.echo("Specify --file or --all")
        return

    if not files:
        click.echo("No files to process")
        return

    click.echo(f"Found {len(files)} file(s) to extract")

    if dry_run:
        for f in files:
            click.echo(f"  Would extract: {f.name}")
        return

    client = get_client()

    for f in files:
        try:
            click.echo(f"Extracting: {f.name}")
            extraction, metadata = extract_file(f, client, config)

            output_path = get_extraction_path(config.vault_root, f)
            save_extraction(extraction, output_path)

            click.echo(f"  → {output_path.name} ({metadata.get('latency_ms', '?')}ms)")
        except Exception as e:
            click.echo(f"  ✗ Error: {e}", err=True)

if __name__ == "__main__":
    main()
```

**Verification Steps**:

1. Create a test transcript:

```bash
cat > "Inbox/Transcripts/test-extraction.md" << 'EOF'
# Test Meeting

Date: January 3, 2026

Participants: Jason, Jeff Denworth

## Transcript

Jason: Hey Jeff, thanks for joining. Let's discuss the Q1 pipeline.

Jeff: Sure. I think we need to focus on the Google deal. They're asking about pricing.

Jason: I'll follow up with their PM next week about the timeline.

Jeff: Great. Also, we decided to approve the new enterprise pricing tier.

Jason: Got it. I'll send the updated docs by Friday.
EOF
```

2. Run extraction:

```bash
cd /Users/jason/Documents/Notes
export OPENAI_API_KEY=your_key_here
python Workflow/scripts/extract.py --file "Inbox/Transcripts/test-extraction.md"
```

3. Verify output:

```bash
cat Inbox/_extraction/test-extraction.extraction.json
```

**Success Criteria**:

- [x] `extract.py` created with CLI interface
- [x] `--file` extracts single file
- [x] `--all` finds unprocessed files
- [x] `--dry-run` shows planned actions
- [x] Extraction JSON is valid `ExtractionV1`
- [x] Skips already-processed files (has .extraction.json)
- [x] Errors are logged, don't crash entire process

**Gate**: ✅ PASSED - Phase 3 Complete

---

## Phase 4: Plan Pipeline ✅ COMPLETE

**Goal**: Generate ChangePlans from extractions using OpenAI Structured Outputs.

**Milestone**: M1 Vertical Slice  
**Estimated Time**: 1 session  
**Dependencies**: Phase 3 complete
**Status**: ✅ Completed 2026-01-03

---

### Step 4.1: Plan Script

**Objective**: Create the planning script that generates ChangePlans.

**File**: `Workflow/scripts/plan.py`

**CLI Interface**:

```bash
# Plan from single extraction
python scripts/plan.py --extraction "Inbox/_extraction/meeting.extraction.json"

# Plan all pending extractions
python scripts/plan.py --all

# Dry run
python scripts/plan.py --all --dry-run
```

**Implementation**:

```python
#!/usr/bin/env python3
"""
Plan Phase: ExtractionV1 → ChangePlan JSON

LLM generates create/patch/link operations only.
Archive is handled deterministically in apply phase.
"""

import sys
import json
import click
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from models.extraction import ExtractionV1
from models.changeplan import ChangePlan
from scripts.utils.config import load_config
from scripts.utils.paths import get_changeplan_path, get_extraction_path
from scripts.utils.fs import safe_read_text, atomic_write
from scripts.utils.entities import list_all_entity_names, get_entity_metadata, match_entity
from scripts.utils.openai_client import get_client, parse_structured

def find_unplanned(config) -> list[Path]:
    """Find extractions without corresponding .changeplan.json."""
    extraction_dir = config.paths["extraction"]

    if not extraction_dir.exists():
        return []

    unplanned = []
    for f in extraction_dir.glob("*.extraction.json"):
        changeplan_path = f.parent / f.name.replace(".extraction.json", ".changeplan.json")
        if not changeplan_path.exists():
            unplanned.append(f)

    return sorted(unplanned)

def load_extraction(path: Path) -> ExtractionV1:
    """Load extraction JSON from file."""
    content = safe_read_text(path)
    return ExtractionV1.model_validate_json(content)

def gather_vault_context(extraction: ExtractionV1) -> dict:
    """
    Build FILTERED context for the planner.

    CRITICAL: Only includes:
    1. Full metadata for entities mentioned in extraction
    2. Lightweight name-only list for fuzzy matching
    3. Aliases

    Prevents context window explosion.
    """
    # Collect mentioned entity names
    mentioned = set(extraction.participants)
    for entity_list in extraction.mentions.values():
        mentioned.update(entity_list)
    if extraction.entity_name:
        mentioned.add(extraction.entity_name)

    return {
        "mentioned_entities": get_entity_metadata(mentioned),
        "all_entity_names": list_all_entity_names(),
        "note_type": extraction.note_type,
        "entity_name": extraction.entity_name,
    }

def build_planner_prompt(vault_context: dict, extraction: ExtractionV1) -> str:
    """Build the planner system prompt."""
    from jinja2 import Environment, FileSystemLoader
    import json

    config = load_config()
    env = Environment(
        loader=FileSystemLoader(str(config.paths["prompts"])),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Ensure tojson exists across environments
    env.filters["tojson"] = lambda v, **kw: json.dumps(v, ensure_ascii=False, **kw)

    template = env.get_template("system-planner.md.j2")
    return template.render(
        vault_context=vault_context,
        extraction=extraction.model_dump(mode="json"),
    )

def validate_changeplan(plan: ChangePlan) -> list[str]:
    """
    Validate changeplan operations.

    Returns list of issues (empty if valid).
    """
    issues = []

    for i, op in enumerate(plan.operations):
        # Check for forbidden operations
        if op.op.value not in ["create", "patch", "link"]:
            issues.append(f"Operation {i}: forbidden op type '{op.op.value}'")

        # Basic path safety
        if (
            ".." in op.path
            or op.path.startswith("/")
            or "\\" in op.path
            or ":" in op.path
        ):
            issues.append(f"Operation {i}: unsafe path '{op.path}'")

        # Validate patch primitives
        if op.patches:
            for j, patch in enumerate(op.patches):
                if patch.primitive.value not in ["upsert_frontmatter", "append_under_heading", "ensure_wikilinks"]:
                    issues.append(f"Operation {i}, patch {j}: forbidden primitive '{patch.primitive.value}'")

    return issues

def apply_validate_changeplan(plan: ChangePlan, allowed_templates: set[str]) -> list[str]:
    """Strict validation used by apply phase before touching disk."""
    issues = []
    for i, op in enumerate(plan.operations):
        # paths must be vault-relative, no abs, no backslashes or colons
        if (
            op.path.startswith("/")
            or "\\" in op.path
            or ":" in op.path
            or ".." in op.path
        ):
            issues.append(f"Operation {i}: invalid path '{op.path}'")

        if op.op.value == "create":
            if not op.template or op.template not in allowed_templates:
                issues.append(f"Operation {i}: forbidden or missing template '{op.template}'")
            if not op.context:
                issues.append(f"Operation {i}: context required for CREATE")
            if op.patches or op.links:
                issues.append(f"Operation {i}: CREATE cannot include patches/links")

        if op.op.value == "patch":
            if not op.patches:
                issues.append(f"Operation {i}: PATCH requires patches")
            for j, patch in enumerate(op.patches or []):
                if patch.primitive.value not in [
                    "upsert_frontmatter",
                    "append_under_heading",
                    "ensure_wikilinks",
                ]:
                    issues.append(
                        f"Operation {i}, patch {j}: forbidden primitive '{patch.primitive.value}'"
                    )
                if patch.primitive.value == "append_under_heading" and not patch.heading:
                    issues.append(f"Operation {i}, patch {j}: heading required for append_under_heading")

        if op.op.value == "link":
            if not op.links:
                issues.append(f"Operation {i}: LINK requires links list")

    return issues

def generate_plan(extraction_path: Path, client, config) -> tuple[ChangePlan, dict]:
    """Generate ChangePlan from extraction."""
    extraction = load_extraction(extraction_path)
    vault_context = gather_vault_context(extraction)

    system_prompt = build_planner_prompt(vault_context, extraction)

    plan, metadata = parse_structured(
        client=client,
        model=config.models["planning"].model,
        system_prompt=system_prompt,
        user_content="Generate the ChangePlan for this extraction.",
        response_model=ChangePlan,
        temperature=config.models["planning"].temperature,
    )

    # Set source references
    plan.extraction_file = str(extraction_path.name)
    plan.source_file = extraction.source_file
    plan.created_at = datetime.now()

    # Validate
    issues = validate_changeplan(plan)
    if issues:
        plan.warnings.extend(issues)

    return plan, metadata

def save_plan(plan: ChangePlan, output_path: Path) -> None:
    """Save ChangePlan JSON to disk."""
    json_str = plan.model_dump_json(indent=2)
    atomic_write(output_path, json_str)

@click.command()
@click.option("--extraction", "extraction_path", type=click.Path(exists=True), help="Plan from single extraction")
@click.option("--all", "plan_all", is_flag=True, help="Plan all pending extractions")
@click.option("--dry-run", is_flag=True, help="Show what would be planned")
def main(extraction_path: str | None, plan_all: bool, dry_run: bool):
    """Generate ChangePlans from extractions."""
    config = load_config()

    if extraction_path:
        files = [Path(extraction_path)]
    elif plan_all:
        files = find_unplanned(config)
    else:
        click.echo("Specify --extraction or --all")
        return

    if not files:
        click.echo("No extractions to plan")
        return

    click.echo(f"Found {len(files)} extraction(s) to plan")

    if dry_run:
        for f in files:
            click.echo(f"  Would plan: {f.name}")
        return

    client = get_client()

    for f in files:
        try:
            click.echo(f"Planning: {f.name}")
            plan, metadata = generate_plan(f, client, config)

            output_path = f.parent / f.name.replace(".extraction.json", ".changeplan.json")
            save_plan(plan, output_path)

            ops_summary = ", ".join(op.op.value for op in plan.operations)
            click.echo(f"  → {output_path.name} ({metadata.get('latency_ms', '?')}ms)")
            click.echo(f"    Operations: {ops_summary}")

            if plan.warnings:
                for warning in plan.warnings:
                    click.echo(f"    ⚠ {warning}")

        except Exception as e:
            click.echo(f"  ✗ Error: {e}", err=True)

if __name__ == "__main__":
    main()
```

**Verification Steps**:

1. Using extraction from Phase 3:

```bash
python Workflow/scripts/plan.py --extraction Inbox/_extraction/test-extraction.extraction.json
```

2. Verify output:

```bash
cat Inbox/_extraction/test-extraction.changeplan.json
```

Expected output structure:

```json
{
  "version": "1.0",
  "source_file": "Inbox/Transcripts/test-extraction.md",
  "extraction_file": "test-extraction.extraction.json",
  "operations": [
    {"op": "create", "path": "VAST/People/Jeff Denworth/2026-01-03 - Q1 Pipeline.md", ...},
    {"op": "patch", "path": "VAST/People/Jeff Denworth/README.md", ...}
  ],
  "warnings": []
}
```

**Success Criteria**:

- [x] `plan.py` created with CLI interface ✅ 2026-01-03
- [x] Generates valid ChangePlan JSON ✅ 2026-01-03
- [x] Creates appropriate operations (create, patch, link) ✅ 2026-01-03
- [x] Patches README.md for entity with `last_contact` ✅ 2026-01-03
- [x] Handles new entities with warnings ✅ 2026-01-03
- [x] NO archive operations in output (those are deterministic) ✅ 2026-01-03
- [x] Validation catches forbidden ops/primitives ✅ 2026-01-03
- [x] Vault context is filtered (not entire vault) ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03

---

## Phase 5: Apply Pipeline ✅ COMPLETE

**Goal**: Execute ChangePlans with transactional safety and rollback.

**Milestone**: M1 Vertical Slice (completion)  
**Estimated Time**: 1-2 sessions  
**Dependencies**: Phase 4 complete
**Status**: ✅ Completed 2026-01-03

---

### Step 5.1: Transactional Executor

**Objective**: Implement the core transactional apply logic with rollback.

**File**: `Workflow/scripts/apply.py`

**Design Principles** (from DESIGN.md):

- **NO AI CALLS** in apply - pure deterministic execution
- Backup all files before modification
- Atomic file writes via temp + rename
- Full rollback on any failure
- Single git commit for entire batch

**Implementation**:

```python
#!/usr/bin/env python3
"""
Apply Phase: ChangePlan → File Updates

TRANSACTIONAL EXECUTION:
1. Require clean git tree (content dirs only)
2. Backup all files to be touched
3. Execute ALL operations from changeplan(s)
4. On failure: restore backups, delete new files
5. On success: archive sources, git commit batch
"""

import sys
import shutil
import click
from pathlib import Path
from datetime import datetime, date
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent.parent))

from models.changeplan import ChangePlan, Operation, OperationType, PatchPrimitive
from scripts.utils.config import load_config
from scripts.utils.paths import get_archive_path, safe_relative_path
from scripts.utils.fs import safe_read_text, atomic_write, backup_file
from scripts.utils.git_ops import is_clean, require_clean, add_content_dirs_all, commit
from scripts.utils.patch_primitives import upsert_frontmatter, append_under_heading, ensure_wikilinks
from scripts.utils.templates import render_note

@dataclass
class TransactionalApply:
    """Executes ChangePlans with rollback on failure."""

    vault_root: Path
    run_id: str
    backup_dir: Path = field(init=False)
    created_files: list[Path] = field(default_factory=list)
    backed_up: dict[Path, Path] = field(default_factory=dict)
    modified_files: list[Path] = field(default_factory=list)

    def __post_init__(self):
        self.backup_dir = self.vault_root / ".workflow_backups" / self.run_id

    def execute_batch(
        self,
        changeplans: list[ChangePlan],
        source_files: list[Path],
        allow_dirty: bool = False,
        allow_overwrite: bool = False,
    ) -> str:
        """
        Execute ALL changeplans atomically.

        Returns commit hash on success.
        Raises on failure (after rollback).
        """
        # 1. Require clean git tree
        require_clean(self.vault_root, allow_dirty=allow_dirty)

        try:
            # 2. Backup ALL files that will be modified
            for plan in changeplans:
                for op in plan.operations:
                    target = self.vault_root / op.path
                    if target.exists() and op.op in [OperationType.PATCH, OperationType.LINK]:
                        self._backup(target)

            # 3. Execute ALL operations
            for plan in changeplans:
                for op in plan.operations:
                    self._apply_operation(op, allow_overwrite=allow_overwrite)

            # 4. Archive ALL sources
            for source_file in source_files:
                self._archive_source(source_file)

            # 5. Stage and commit
            all_files = self.created_files + self.modified_files
            # Add archived sources
            for source in source_files:
                archive_path = get_archive_path(self.vault_root, source)
                all_files.append(archive_path)

            add_content_dirs_all(self.vault_root)

            summary = self._build_commit_message(changeplans)
            commit_hash = commit(self.vault_root, summary)

            # 6. Cleanup backups on success
            shutil.rmtree(self.backup_dir, ignore_errors=True)

            return commit_hash

        except Exception as e:
            self._rollback()
            raise

    def _backup(self, file_path: Path) -> None:
        """Create backup of file before modification."""
        if file_path not in self.backed_up:
            backup_path = backup_file(file_path, self.backup_dir, self.vault_root)
            self.backed_up[file_path] = backup_path

    def _apply_operation(self, op: Operation, allow_overwrite: bool = False) -> None:
        """Apply a single operation."""
        # Harden path handling: coerce to safe vault-relative
        rel = safe_relative_path(self.vault_root, op.path)
        target = self.vault_root / rel

        match op.op:
            case OperationType.CREATE:
                # Enforce template whitelist (defend against traversal)
                from scripts.utils.templates import ALLOWED_TEMPLATES
                if op.template not in ALLOWED_TEMPLATES:
                    raise ValueError(f"Forbidden template: {op.template}")
                # Fail fast if target exists unless override
                if target.exists() and not allow_overwrite:
                    raise FileExistsError(f"Target exists for CREATE: {target}")
                content = render_note(op.template, op.context)
                target.parent.mkdir(parents=True, exist_ok=True)
                atomic_write(target, content)
                self.created_files.append(target)

            case OperationType.PATCH:
                content = safe_read_text(target)
                for patch in op.patches:
                    content = self._apply_patch(content, patch)
                atomic_write(target, content)
                self.modified_files.append(target)

            case OperationType.LINK:
                content = safe_read_text(target)
                content = ensure_wikilinks(content, op.links)
                atomic_write(target, content)
                self.modified_files.append(target)

    def _apply_patch(self, content: str, spec) -> str:
        """Apply a single patch primitive."""
        match spec.primitive:
            case PatchPrimitive.UPSERT_FRONTMATTER:
                return upsert_frontmatter(content, spec.frontmatter)
            case PatchPrimitive.APPEND_UNDER_HEADING:
                return append_under_heading(
                    content,
                    spec.heading.heading,
                    spec.heading.content
                )
            case PatchPrimitive.ENSURE_WIKILINKS:
                return ensure_wikilinks(content, spec.wikilinks)
        return content

    def _archive_source(self, source_file: Path) -> None:
        """Move source file to archive."""
        archive_path = get_archive_path(self.vault_root, source_file)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source_file), str(archive_path))
        # Track move for rollback
        if not hasattr(self, "_moved_sources"):
            self._moved_sources = []
        self._moved_sources.append((archive_path, source_file))

    def _build_commit_message(self, changeplans: list[ChangePlan]) -> str:
        """Build git commit message."""
        sources = [Path(p.source_file).name for p in changeplans]
        if len(sources) <= 3:
            files = ", ".join(sources)
        else:
            files = f"{sources[0]}, {sources[1]}, ... (+{len(sources)-2} more)"
        return f"[auto] Processed: {files}"

    def _rollback(self) -> None:
        """Restore backups and delete created files."""
        # Restore backed up files
        for original, backup in self.backed_up.items():
            try:
                shutil.copy2(backup, original)
            except Exception:
                pass  # Best effort

        # Delete created files
        for created in self.created_files:
            try:
                created.unlink(missing_ok=True)
            except Exception:
                pass  # Best effort

        # Undo archived source moves
        for dst, src in getattr(self, "_moved_sources", []):
            try:
                if dst.exists():
                    src.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(dst), str(src))
            except Exception:
                pass

        # Cleanup backup directory
        shutil.rmtree(self.backup_dir, ignore_errors=True)


def find_pending_changeplans(config) -> list[Path]:
    """Find changeplans ready to apply."""
    extraction_dir = config.paths["extraction"]

    if not extraction_dir.exists():
        return []

    return sorted(extraction_dir.glob("*.changeplan.json"))

def load_changeplan(path: Path) -> ChangePlan:
    """Load ChangePlan from JSON file."""
    content = safe_read_text(path)
    return ChangePlan.model_validate_json(content)

@click.command()
@click.option("--changeplan", "changeplan_path", type=click.Path(exists=True), help="Apply single changeplan")
@click.option("--all", "apply_all", is_flag=True, help="Apply all pending changeplans")
@click.option("--dry-run", is_flag=True, help="Show what would be applied")
@click.option("--allow-dirty", is_flag=True, help="Allow apply with dirty git tree")
def main(changeplan_path: str | None, apply_all: bool, dry_run: bool, allow_dirty: bool):
    """Apply ChangePlans to update the vault."""
    config = load_config()

    if changeplan_path:
        files = [Path(changeplan_path)]
    elif apply_all:
        files = find_pending_changeplans(config)
    else:
        click.echo("Specify --changeplan or --all")
        return

    if not files:
        click.echo("No changeplans to apply")
        return

    # Load all changeplans
    changeplans = []
    source_files = []

    for f in files:
        plan = load_changeplan(f)
        changeplans.append(plan)
        source_files.append(config.vault_root / plan.source_file)

    click.echo(f"Loaded {len(changeplans)} changeplan(s)")

    if dry_run:
        for plan in changeplans:
            click.echo(f"\n{plan.source_file}:")
            for op in plan.operations:
                click.echo(f"  {op.op.value}: {op.path}")
        return

    # Execute transactionally
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    executor = TransactionalApply(config.vault_root, run_id)

    try:
        commit_hash = executor.execute_batch(changeplans, source_files, allow_dirty)
        click.echo(f"\n✓ Applied successfully")
        click.echo(f"  Created: {len(executor.created_files)} files")
        click.echo(f"  Modified: {len(executor.modified_files)} files")
        click.echo(f"  Archived: {len(source_files)} sources")
        if commit_hash:
            click.echo(f"  Commit: {commit_hash[:8]}")

        # Cleanup changeplan files
        for f in files:
            f.unlink()

    except Exception as e:
        click.echo(f"\n✗ Apply failed: {e}", err=True)
        click.echo("  Rollback completed - no changes made", err=True)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
```

**Verification Steps**:

1. Test with dry run first:

```bash
python Workflow/scripts/apply.py --all --dry-run
```

2. Full apply:

```bash
python Workflow/scripts/apply.py --all
```

3. Verify:

```bash
# Check created note
ls VAST/People/Jeff\ Denworth/

# Check git log
git log --oneline -1

# Check archive
ls Inbox/_archive/$(date +%Y-%m-%d)/
```

4. Test rollback (inject failure):

```python
# In Python REPL
import sys; sys.path.insert(0, "Workflow")
from scripts.apply import TransactionalApply
from pathlib import Path

# This should fail and rollback
executor = TransactionalApply(Path("/Users/jason/Documents/Notes"), "test-rollback")
# ... create a plan with an invalid operation path
```

**Success Criteria**:

- [x] `apply.py` created with CLI interface ✅ 2026-01-03
- [x] Backup created before modifications ✅ 2026-01-03
- [x] CREATE operations render templates correctly ✅ 2026-01-03
- [x] PATCH operations apply all primitives ✅ 2026-01-03
- [x] LINK operations add wikilinks ✅ 2026-01-03
- [x] Atomic writes prevent corruption ✅ 2026-01-03
- [x] Archive moves source correctly ✅ 2026-01-03
- [x] Git commit includes all changes ✅ 2026-01-03 (when in git repo)
- [x] Rollback restores backups on failure ✅ 2026-01-03
- [x] Rollback deletes created files on failure ✅ 2026-01-03
- [x] `--allow-dirty` bypasses clean check ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03

---

### Step 5.2: Apply-Phase Validation (Strict)

Add strict validation of plans before any disk writes.

**File**: `Workflow/scripts/apply.py` (extend)

**Rules**:

- Reject absolute paths, backslashes, `..`, and Windows drive `:` in `op.path`
- CREATE: must include `template` in `ALLOWED_TEMPLATES` and `context`; no patches/links
- PATCH: requires `patches`; each primitive must be one of the whitelist; append requires `heading`
- LINK: requires non-empty `links`

Integrate validation:

```python
from scripts.plan import apply_validate_changeplan
issues = apply_validate_changeplan(plan, ALLOWED_TEMPLATES)
if issues:
    raise ValueError("Invalid changeplan: " + "; ".join(issues))
```

Run this check for every plan prior to applying.

---

## Phase 6: Orchestration ✅ COMPLETE

**Goal**: Create the main entry point and structured logging.

**Milestone**: M1 Vertical Slice (completion) → M2 Production Hardening  
**Estimated Time**: 1 session  
**Dependencies**: Phase 5 complete

---

### Step 6.1: Process Inbox Orchestrator

**Objective**: One command runs the full pipeline end-of-day.

**File**: `Workflow/scripts/process_inbox.py`

**Flow** (STAGED, not per-file):

```
1. Check git is clean (only Inbox/, VAST/, Personal/)
2. Find all unprocessed files in Inbox/
3. EXTRACT ALL: For each file → .extraction.json
   - Failed extractions → _failed/, continue with rest
4. PLAN ALL: For each extraction → .changeplan.json
   - Failed plans → _failed/, continue with rest
5. APPLY BATCH: Execute all ChangePlans in ONE transaction
   - Backup all targets
   - Apply all operations
   - On ANY failure: rollback entire batch
   - On success: archive all sources, single git commit
6. Log results
```

**CRITICAL**: The Apply phase is atomic across ALL files.

**CLI Interface**:

```bash
# Process everything
python scripts/process_inbox.py

# Process specific subfolder
python scripts/process_inbox.py --scope transcripts

# Dry run
python scripts/process_inbox.py --dry-run

# Skip extraction/planning (apply existing changeplans only)
python scripts/process_inbox.py --apply-only

# Allow dirty git tree
python scripts/process_inbox.py --allow-dirty
```

**Implementation**:

```python
#!/usr/bin/env python3
"""
Process Inbox: Full pipeline orchestrator.

Runs: Extract → Plan → Apply in staged batch mode.
"""

import sys
import shutil
import click
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.utils.config import load_config
from scripts.utils.logging import setup_logging, log_event
from scripts.utils.git_ops import require_clean
from scripts.extract import find_unprocessed, extract_file, save_extraction
from scripts.plan import find_unplanned, generate_plan, save_plan, load_extraction
from scripts.apply import TransactionalApply, find_pending_changeplans, load_changeplan

@dataclass
class ProcessResult:
    """Results of inbox processing."""
    extracted: int = 0
    planned: int = 0
    applied: int = 0
    failed: int = 0
    errors: list[str] = field(default_factory=list)
    commit_hash: str = ""

def move_to_failed(source: Path, error: str, config):
    """Move failed file to _failed/ directory with error log."""
    failed_dir = config.paths["failed"] / datetime.now().strftime("%Y-%m-%d")
    failed_dir.mkdir(parents=True, exist_ok=True)

    # Move source file
    dest = failed_dir / source.name
    shutil.move(str(source), str(dest))

    # Write error log
    error_path = failed_dir / f"{source.stem}.error.txt"
    error_path.write_text(f"Error: {error}\n\nTimestamp: {datetime.now().isoformat()}\n")

    return dest

def extract_all(files: list[Path], client, config) -> tuple[list[Path], list[Path]]:
    """Extract all files. Returns (successes, failures)."""
    from scripts.utils.paths import get_extraction_path

    successes = []
    failures = []

    for f in files:
        try:
            log_event("extract", "start", {"file": f.name})
            extraction, metadata = extract_file(f, client, config)

            output_path = get_extraction_path(config.vault_root, f)
            save_extraction(extraction, output_path)

            log_event("extract", "success", {"file": f.name, **metadata})
            successes.append(output_path)

        except Exception as e:
            log_event("extract", "failed", {"file": f.name, "error": str(e)})
            move_to_failed(f, str(e), config)
            failures.append(f)

    return successes, failures

def plan_all(extractions: list[Path], client, config) -> tuple[list[Path], list[Path]]:
    """Plan all extractions. Returns (successes, failures)."""
    successes = []
    failures = []

    for f in extractions:
        try:
            log_event("plan", "start", {"file": f.name})
            plan, metadata = generate_plan(f, client, config)

            output_path = f.parent / f.name.replace(".extraction.json", ".changeplan.json")
            save_plan(plan, output_path)

            log_event("plan", "success", {"file": f.name, **metadata})
            successes.append(output_path)

        except Exception as e:
            log_event("plan", "failed", {"file": f.name, "error": str(e)})
            # Move the extraction to failed
            extraction_source = config.vault_root / load_extraction(f).source_file
            if extraction_source.exists():
                move_to_failed(extraction_source, str(e), config)
            failures.append(f)

    return successes, failures

@click.command()
@click.option("--scope", type=click.Choice(["transcripts", "email", "all"]), default="all")
@click.option("--dry-run", is_flag=True, help="Show what would be processed")
@click.option("--apply-only", is_flag=True, help="Skip extract/plan, apply existing changeplans")
@click.option("--allow-dirty", is_flag=True, help="Allow processing with dirty git tree")
def main(scope: str, dry_run: bool, apply_only: bool, allow_dirty: bool):
    """Process all pending items in the inbox."""
    config = load_config()
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Setup logging
    log_path = setup_logging(config, run_id)
    log_event("process", "start", {"scope": scope, "run_id": run_id})

    result = ProcessResult()

    try:
        # Check git cleanliness early
        if not dry_run and not apply_only:
            require_clean(config.vault_root, allow_dirty=allow_dirty)

        if apply_only:
            # Just apply existing changeplans
            changeplans = find_pending_changeplans(config)
            click.echo(f"Found {len(changeplans)} changeplan(s) to apply")
        else:
            # Find unprocessed files
            if scope == "all":
                scopes = ["transcripts", "email"]
            else:
                scopes = [scope]

            all_files = []
            for s in scopes:
                all_files.extend(find_unprocessed(config, s))

            click.echo(f"Found {len(all_files)} unprocessed file(s)")

            if dry_run:
                for f in all_files:
                    click.echo(f"  Would process: {f.name}")
                return

            if not all_files:
                click.echo("Nothing to process")
                return

            # Get OpenAI client
            from scripts.utils.openai_client import get_client
            client = get_client()

            # STAGE 1: Extract all
            click.echo("\n=== EXTRACT ===")
            extractions, extract_failures = extract_all(all_files, client, config)
            result.extracted = len(extractions)
            result.failed += len(extract_failures)
            click.echo(f"Extracted: {len(extractions)}, Failed: {len(extract_failures)}")

            if not extractions:
                click.echo("No successful extractions, stopping")
                return

            # STAGE 2: Plan all
            click.echo("\n=== PLAN ===")
            changeplans, plan_failures = plan_all(extractions, client, config)
            result.planned = len(changeplans)
            result.failed += len(plan_failures)
            click.echo(f"Planned: {len(changeplans)}, Failed: {len(plan_failures)}")

            if not changeplans:
                click.echo("No successful plans, stopping")
                return

        # STAGE 3: Apply batch (atomic)
        click.echo("\n=== APPLY ===")

        # Load all plans
        plans = [load_changeplan(p) for p in changeplans]
        source_files = [config.vault_root / p.source_file for p in plans if (config.vault_root / p.source_file).exists()]

        executor = TransactionalApply(config.vault_root, run_id)
        commit_hash = executor.execute_batch(plans, source_files, allow_dirty)

        result.applied = len(plans)
        result.commit_hash = commit_hash

        click.echo(f"Applied: {len(plans)} changeplans")
        click.echo(f"Created: {len(executor.created_files)} files")
        click.echo(f"Modified: {len(executor.modified_files)} files")
        click.echo(f"Archived: {len(source_files)} sources")
        if commit_hash:
            click.echo(f"Commit: {commit_hash[:8]}")

        # Cleanup changeplan files
        for p in changeplans:
            p.unlink(missing_ok=True)

        log_event("process", "complete", {
            "extracted": result.extracted,
            "planned": result.planned,
            "applied": result.applied,
            "failed": result.failed,
            "commit": commit_hash[:8] if commit_hash else ""
        })

        click.echo(f"\n✓ Processing complete. Log: {log_path}")

    except Exception as e:
        log_event("process", "error", {"error": str(e)})
        click.echo(f"\n✗ Error: {e}", err=True)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
```

**Success Criteria**:

- [x] `process_inbox.py` created with CLI interface ✅ 2026-01-03
- [x] Stages run in correct order: Extract → Plan → Apply ✅ 2026-01-03
- [x] Failed files go to `_failed/` with error logs ✅ 2026-01-03
- [x] Apply is atomic (all or nothing) ✅ 2026-01-03
- [x] Single git commit for entire batch ✅ 2026-01-03
- [x] `--dry-run` shows planned actions ✅ 2026-01-03
- [x] `--apply-only` skips extract/plan ✅ 2026-01-03
- [x] Re-run is idempotent (no duplicate processing) ✅ 2026-01-03

**Gate**: Proceed to Step 6.2

---

### Step 6.2: Structured Logging

**Objective**: Implement JSON-line logging for observability.

**File**: `Workflow/scripts/utils/logging.py`

**Log Location**: `Workflow/logs/YYYY-MM-DD_HHMMSS.log`

**Implementation**:

```python
"""Structured logging for automation pipeline."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

# Global log file handle
_log_file = None
_run_id = None

def setup_logging(config, run_id: str) -> Path:
    """Initialize logging for this run."""
    global _log_file, _run_id

    log_dir = config.paths["logs"]
    log_dir.mkdir(parents=True, exist_ok=True)

    log_path = log_dir / f"{run_id}.log"
    _log_file = open(log_path, "a")
    _run_id = run_id

    return log_path

def log_event(phase: str, status: str, data: dict[str, Any] | None = None) -> None:
    """Log a structured event."""
    global _log_file, _run_id

    event = {
        "timestamp": datetime.now().isoformat(),
        "run_id": _run_id,
        "phase": phase,
        "status": status,
    }

    if data:
        event.update(data)

    line = json.dumps(event)

    if _log_file:
        _log_file.write(line + "\n")
        _log_file.flush()
    else:
        # Fallback to print if not initialized
        print(f"[LOG] {line}")

def close_logging() -> None:
    """Close log file."""
    global _log_file
    if _log_file:
        _log_file.close()
        _log_file = None
```

**Log Format Example**:

```json
{"timestamp": "2026-01-03T18:00:00", "run_id": "20260103_180000", "phase": "process", "status": "start", "scope": "all"}
{"timestamp": "2026-01-03T18:00:01", "run_id": "20260103_180000", "phase": "extract", "status": "start", "file": "meeting.md"}
{"timestamp": "2026-01-03T18:00:03", "run_id": "20260103_180000", "phase": "extract", "status": "success", "file": "meeting.md", "latency_ms": 2500, "input_tokens": 1500}
{"timestamp": "2026-01-03T18:00:04", "run_id": "20260103_180000", "phase": "plan", "status": "start", "file": "meeting.extraction.json"}
{"timestamp": "2026-01-03T18:00:05", "run_id": "20260103_180000", "phase": "apply", "status": "success", "operations": 3}
{"timestamp": "2026-01-03T18:00:06", "run_id": "20260103_180000", "phase": "process", "status": "complete", "extracted": 1, "planned": 1, "applied": 1, "commit": "abc123"}
```

**Success Criteria**:

- [x] `logging.py` created ✅ 2026-01-03
- [x] Logs created for each run ✅ 2026-01-03
- [x] JSON format is valid and parseable ✅ 2026-01-03
- [x] Token usage tracked when available ✅ 2026-01-03
- [x] Errors include relevant context ✅ 2026-01-03
- [x] Logs are human-readable with `jq` ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - All Phase 6 checkboxes complete

---

## Phase 7: Hardening

**Goal**: Add standards checks, idempotency enforcement, and test fixtures.

**Milestone**: M2 Production Hardening  
**Estimated Time**: 1-2 sessions  
**Dependencies**: Phase 6 complete

---

### Step 7.1: Standards Compliance Checker

**Objective**: Validate output against STANDARDS.md before writing.

**File**: `Workflow/scripts/utils/standards_check.py`

**Implementation**:

```python
"""Standards compliance validation."""

import re
from pathlib import Path
from scripts.utils.frontmatter import parse_frontmatter

# Required frontmatter keys by note type
REQUIRED_KEYS = {
    "people": ["type", "title", "date", "person", "tags"],
    "customer": ["type", "title", "date", "account", "tags"],
    "projects": ["type", "title", "date", "project", "tags"],
    "rob": ["type", "title", "date", "tags"],
    "journal": ["type", "title", "date", "tags"],
}

# Automation-added keys (required for generated notes)
AUTOMATION_KEYS = ["source", "source_ref"]

# Tag patterns
TAG_PATTERN = re.compile(r"^[a-z0-9-]+(/[a-z0-9-]+)?$")

# File name patterns
DATED_NOTE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} - .+\.md$")
EMAIL_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{6}_\d{4}_.+\.(md|eml)$")

def check_frontmatter(content: str, note_type: str, is_generated: bool = True) -> list[str]:
    """Check frontmatter for required keys and valid values."""
    issues = []

    fm, _ = parse_frontmatter(content)
    if fm is None:
        return ["Missing frontmatter"]

    # Check required keys
    required = REQUIRED_KEYS.get(note_type, ["type", "title", "date", "tags"])
    for key in required:
        if key not in fm:
            issues.append(f"Missing required key: {key}")

    # Check automation keys for generated notes
    if is_generated:
        for key in AUTOMATION_KEYS:
            if key not in fm:
                issues.append(f"Missing automation key: {key}")

    # Check type value
    if fm.get("type") != note_type:
        issues.append(f"Type mismatch: expected '{note_type}', got '{fm.get('type')}'")

    # Check date format
    date_val = fm.get("date", "")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(date_val)):
        issues.append(f"Invalid date format: {date_val} (expected YYYY-MM-DD)")

    # Check tags
    tags = fm.get("tags", [])
    if not tags:
        issues.append("No tags found")
    else:
        for tag in tags:
            if not TAG_PATTERN.match(tag):
                issues.append(f"Invalid tag format: {tag}")

    return issues

def check_filename(filename: str, context: str = "note") -> list[str]:
    """Check filename against standards."""
    issues = []

    if context == "note":
        if not DATED_NOTE_PATTERN.match(filename):
            issues.append(f"Invalid note filename: {filename} (expected YYYY-MM-DD - Title.md)")
    elif context == "email":
        if not EMAIL_PATTERN.match(filename):
            issues.append(f"Invalid email filename: {filename}")

    # Check for forbidden characters
    forbidden = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in forbidden:
        if char in filename:
            issues.append(f"Forbidden character in filename: {char}")

    return issues

def validate_before_write(path: Path, content: str, note_type: str) -> list[str]:
    """
    Run all validations before writing a file.

    Returns list of issues. Empty list = valid.
    """
    issues = []

    # Check filename
    issues.extend(check_filename(path.name))

    # Check content
    issues.extend(check_frontmatter(content, note_type, is_generated=True))

    return issues
```

**Integration with Apply**:

Add validation hook to `apply.py`:

```python
# In _apply_operation for CREATE:
if op.op == OperationType.CREATE:
    content = render_note(op.template, op.context)

    # Validate before write
    issues = validate_before_write(target, content, op.context.get("type", ""))
    if issues:
        raise ValueError(f"Standards validation failed for {target}:\n" + "\n".join(issues))

    atomic_write(target, content)
```

**Success Criteria**:

- [x] `standards_check.py` created ✅ 2026-01-03
- [x] Validates required frontmatter keys ✅ 2026-01-03
- [x] Validates date format (YYYY-MM-DD) ✅ 2026-01-03
- [x] Validates tag format (lowercase, hyphens only) ✅ 2026-01-03
- [x] Validates filename patterns ✅ 2026-01-03
- [x] Integration with apply phase ✅ 2026-01-03
- [x] Invalid content causes rollback (not write) ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - Proceed to Step 7.2

---

### Step 7.2: Idempotency Checks

**Objective**: Ensure re-running pipeline produces no changes.

**Implementation**:

Add to `process_inbox.py`:

```python
def is_already_processed(source: Path, config) -> bool:
    """
    Check if a source file has already been processed.

    A file is considered processed if:
    1. It has a corresponding extraction in _extraction/
    2. OR it exists in _archive/
    """
    # Check extraction exists
    extraction_path = get_extraction_path(config.vault_root, source)
    if extraction_path.exists():
        return True

    # Check in any archive folder
    archive_base = config.paths["archive"]
    if archive_base.exists():
        for date_dir in archive_base.iterdir():
            if (date_dir / source.name).exists():
                return True

    return False
```

**Test**:

```bash
# Run twice - second run should do nothing
python scripts/process_inbox.py
python scripts/process_inbox.py  # Should report "Nothing to process"
```

**Success Criteria**:

- [x] Re-run detects already-processed files ✅ 2026-01-03
- [x] No duplicate notes created ✅ 2026-01-03
- [x] No duplicate git commits ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - Proceed to Step 7.3

---

### Step 7.3: Test Fixtures

**Objective**: Create synthetic test data for reliable testing.

**Directory**: `Workflow/tests/fixtures/`

**Files to Create**:

1. `Workflow/tests/fixtures/transcripts/sample-meeting.md`:

```markdown
# Test Meeting - Q1 Planning

Date: January 3, 2026

Participants: Jason, Jeff Denworth

## Transcript

Jason: Welcome everyone. Let's discuss Q1 priorities.

Jeff: I think we need to focus on the Google partnership.

Jason: Agreed. I'll set up a call with their PM next week.

Jeff: Also, we decided to go with the new pricing model.

Jason: Great. Let me send the updated proposal by Friday.

## Summary

Discussed Q1 priorities focusing on Google partnership and pricing.
```

2. `Workflow/tests/fixtures/expected/sample-meeting.extraction.json`:

```json
{
  "version": "1.0",
  "note_type": "people",
  "entity_name": "Jeff Denworth",
  "title": "Q1 Planning",
  "date": "2026-01-03",
  "participants": ["Jason", "Jeff Denworth"],
  "summary": "Discussed Q1 priorities focusing on Google partnership and new pricing model",
  "tasks": [
    {
      "text": "Set up call with Google PM",
      "owner": "Myself",
      "due": "2026-01-10",
      "priority": "medium"
    },
    {
      "text": "Send updated proposal",
      "owner": "Myself",
      "due": "2026-01-10",
      "priority": "medium"
    }
  ],
  "decisions": ["Go with new pricing model"],
  "mentions": {
    "people": ["Jeff Denworth"],
    "accounts": ["Google"],
    "projects": []
  }
}
```

3. `Workflow/tests/test_pipeline.py`:

```python
"""Integration tests for the full pipeline."""

import pytest
import tempfile
import shutil
from pathlib import Path

# Tests for patch primitives, frontmatter, etc.
# Run with: pytest Workflow/tests/
```

**Success Criteria**:

- [x] Test fixtures created ✅ 2026-01-03
- [x] Expected outputs documented ✅ 2026-01-03
- [x] Tests can run without API calls (mocked) ✅ 2026-01-03
- [x] Test coverage for patch primitives ✅ 2026-01-03
- [x] Test coverage for rollback logic ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - All Phase 7 checkboxes complete

**Test Summary**: 45 tests passing across 4 test modules:

- `test_patch_primitives.py` - 13 tests for upsert_frontmatter, append_under_heading, ensure_wikilinks
- `test_standards.py` - 12 tests for frontmatter, filename, path validation
- `test_validation.py` - 12 tests for ChangePlan schema validation
- `test_rollback.py` - 8 tests for transactional apply, idempotency, git checks

---

## Phase 8: Migration

**Goal**: Implement `migrate.py` to bring existing vault content into standards compliance.

**Milestone**: M4 Vault Migration  
**Estimated Time**: 1-2 sessions  
**Dependencies**: Phase 7 complete

**Reference**: See `REFACTOR.md` for full migration requirements.

---

### Step 8.1: Migration Scanner

**Objective**: Scan vault for entity folders and detect compliance issues.

**File**: `Workflow/scripts/migration/scanner.py`

**Implementation**:

```python
#!/usr/bin/env python3
"""
Migration Scanner: Phase 1 of migrate.py

Scans vault for entity folders, detects issues, outputs manifest.json.
"""

import sys
import json
from pathlib import Path
from dataclasses import dataclass, field, asdict
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scripts.utils.config import load_config
from scripts.utils.frontmatter import parse_frontmatter
from scripts.utils.paths import safe_relative_path as vault_relative

@dataclass
class EntityIssue:
    """A detected issue with an entity."""
    entity_path: str
    issue_type: str  # missing_readme, bad_frontmatter, wrong_type, missing_key
    details: str
    severity: str = "warning"  # warning, error

@dataclass
class EntityInfo:
    """Information about an entity folder."""
    path: str
    entity_type: str  # people, customer, projects, rob
    name: str
    has_readme: bool
    note_count: int
    issues: list[EntityIssue] = field(default_factory=list)

@dataclass
class ScanManifest:
    """Output of migration scan."""
    scan_date: str
    scope: str
    entities: list[EntityInfo]
    total_issues: int

    def to_dict(self):
        return {
            "scan_date": self.scan_date,
            "scope": self.scope,
            "entities": [asdict(e) for e in self.entities],
            "total_issues": self.total_issues
        }

# Entity type detection based on path
ENTITY_PATTERNS = {
    "VAST/People": "people",
    "VAST/Customers and Partners": "customer",
    "VAST/Projects": "projects",
    "VAST/ROB": "rob",
    "Personal/People": "people",
    "Personal/Projects": "projects",
}

# Required frontmatter by type
REQUIRED_KEYS = {
    "people": ["type", "person"],
    "customer": ["type", "account"],
    "projects": ["type", "project"],
    "rob": ["type"],
}

def detect_entity_type(path: Path, vault_root: Path) -> str | None:
    """Detect entity type from path."""
    rel = vault_relative(vault_root, path)
    for pattern, etype in ENTITY_PATTERNS.items():
        if rel.startswith(pattern):
            return etype
    return None

def scan_entity(entity_dir: Path, vault_root: Path) -> EntityInfo:
    """Scan a single entity folder."""
    rel_path = vault_relative(vault_root, entity_dir)
    entity_type = detect_entity_type(entity_dir, vault_root) or "unknown"

    info = EntityInfo(
        path=rel_path,
        entity_type=entity_type,
        name=entity_dir.name,
        has_readme=False,
        note_count=0,
        issues=[]
    )

    # Check for README
    readme = entity_dir / "README.md"
    if readme.exists():
        info.has_readme = True
        content = readme.read_text()
        fm, _ = parse_frontmatter(content)

        if fm is None:
            info.issues.append(EntityIssue(
                entity_path=rel_path,
                issue_type="bad_frontmatter",
                details="README.md has no valid frontmatter"
            ))
        else:
            # Check required keys
            for key in REQUIRED_KEYS.get(entity_type, []):
                if key not in fm:
                    info.issues.append(EntityIssue(
                        entity_path=rel_path,
                        issue_type="missing_key",
                        details=f"README.md missing required key: {key}"
                    ))

            # Check type matches
            if fm.get("type") and fm.get("type") != entity_type:
                info.issues.append(EntityIssue(
                    entity_path=rel_path,
                    issue_type="wrong_type",
                    details=f"Type mismatch: expected {entity_type}, got {fm.get('type')}"
                ))
    else:
        info.issues.append(EntityIssue(
            entity_path=rel_path,
            issue_type="missing_readme",
            details="Entity folder has no README.md",
            severity="error"
        ))

    # Count notes
    for f in entity_dir.glob("*.md"):
        if f.name != "README.md":
            info.note_count += 1

    return info

def scan_scope(vault_root: Path, scope: str) -> ScanManifest:
    """Scan a scope for entity folders."""
    if scope == "all":
        scan_dirs = [vault_root / "VAST", vault_root / "Personal"]
    else:
        scan_dirs = [vault_root / scope]

    entities = []

    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue

        # Find entity folders (depth 2: e.g., VAST/People/{Name})
        for type_dir in scan_dir.iterdir():
            if not type_dir.is_dir() or type_dir.name.startswith("_"):
                continue

            for entity_dir in type_dir.iterdir():
                if entity_dir.is_dir() and not entity_dir.name.startswith("_"):
                    entities.append(scan_entity(entity_dir, vault_root))

    total_issues = sum(len(e.issues) for e in entities)

    return ScanManifest(
        scan_date=datetime.now().isoformat(),
        scope=scope,
        entities=entities,
        total_issues=total_issues
    )

def main():
    """CLI entry point."""
    import click

    @click.command()
    @click.option("--scope", default="all", help="Scope to scan (VAST, Personal, or all)")
    @click.option("-o", "--output", default="manifest.json", help="Output file path")
    def run(scope: str, output: str):
        config = load_config()
        manifest = scan_scope(config.vault_root, scope)

        output_path = Path(output)
        output_path.write_text(json.dumps(manifest.to_dict(), indent=2))

        click.echo(f"Scanned {len(manifest.entities)} entities")
        click.echo(f"Found {manifest.total_issues} issues")
        click.echo(f"Manifest written to: {output_path}")

    run()

if __name__ == "__main__":
    main()
```

**CLI**:

```bash
python scripts/migration/scanner.py --scope "VAST/People" -o manifest.json
python scripts/migration/scanner.py --scope "all" -o manifest.json
```

**Success Criteria**:

- [x] `scanner.py` created ✅ 2026-01-03
- [x] Finds all entity folders ✅ 2026-01-03
- [x] Correctly identifies missing README ✅ 2026-01-03
- [x] Detects frontmatter issues ✅ 2026-01-03
- [x] Manifest JSON is valid and parseable ✅ 2026-01-03
- [x] Statistics are accurate ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - Proceed to Step 8.2

---

### Step 8.2: Migration Analyzer

**Objective**: Generate fix operations from manifest (no AI).

**File**: `Workflow/scripts/migration/analyzer.py`

**Implementation**:

```python
#!/usr/bin/env python3
"""
Migration Analyzer: Phase 2 of migrate.py

Loads manifest, generates deterministic fix operations.
"""

import sys
import json
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from models.changeplan import ChangePlan, Operation, OperationType, PatchSpec, PatchPrimitive, FrontmatterPatch

def analyze_manifest(manifest: dict) -> ChangePlan:
    """Generate ChangePlan from scan manifest."""
    operations = []
    warnings = []

    for entity in manifest["entities"]:
        for issue in entity.get("issues", []):
            issue_type = issue["issue_type"]
            entity_path = issue["entity_path"]

            if issue_type == "missing_readme":
                # Create README from template
                operations.append(Operation(
                    op=OperationType.CREATE,
                    path=f"{entity_path}/README.md",
                    template="readme-migration.md.j2",
                    context={
                        "type": entity["entity_type"],
                        "name": entity["name"],
                        "entity_key": get_entity_key(entity["entity_type"]),
                    }
                ))

            elif issue_type == "missing_key":
                # Patch to add missing key
                key = issue["details"].split(": ")[-1]
                value = infer_value(key, entity)

                operations.append(Operation(
                    op=OperationType.PATCH,
                    path=f"{entity_path}/README.md",
                    patches=[PatchSpec(
                        primitive=PatchPrimitive.UPSERT_FRONTMATTER,
                        frontmatter=[FrontmatterPatch(key=key, value=value)]
                    )]
                ))

            elif issue_type == "wrong_type":
                # Patch to fix type
                operations.append(Operation(
                    op=OperationType.PATCH,
                    path=f"{entity_path}/README.md",
                    patches=[PatchSpec(
                        primitive=PatchPrimitive.UPSERT_FRONTMATTER,
                        frontmatter=[FrontmatterPatch(key="type", value=entity["entity_type"])]
                    )]
                ))

            elif issue_type == "bad_frontmatter":
                warnings.append(f"Manual fix needed for {entity_path}: bad frontmatter")

    return ChangePlan(
        version="1.0",
        source_file="manifest.json",
        extraction_file="",  # N/A for migration
        created_at=datetime.now(),
        operations=operations,
        warnings=warnings
    )

def get_entity_key(entity_type: str) -> str:
    """Get the entity key field name for a type."""
    return {
        "people": "person",
        "customer": "account",
        "projects": "project",
        "rob": "rob_forum",
    }.get(entity_type, "entity")

def infer_value(key: str, entity: dict):
    """Infer a value for a missing frontmatter key."""
    if key in ("person", "account", "project", "rob_forum"):
        return entity["name"]
    if key == "type":
        return entity["entity_type"]
    return ""

def main():
    import click

    @click.command()
    @click.option("-m", "--manifest", required=True, help="Manifest JSON from scan")
    @click.option("-o", "--output", default="changeplan.json", help="Output changeplan")
    def run(manifest: str, output: str):
        manifest_data = json.loads(Path(manifest).read_text())
        plan = analyze_manifest(manifest_data)

        Path(output).write_text(plan.model_dump_json(indent=2))

        click.echo(f"Generated {len(plan.operations)} operations")
        if plan.warnings:
            click.echo(f"Warnings: {len(plan.warnings)}")
            for w in plan.warnings:
                click.echo(f"  - {w}")
        click.echo(f"ChangePlan written to: {output}")

    run()

if __name__ == "__main__":
    main()
```

**Success Criteria**:

- [x] `analyzer.py` created ✅ 2026-01-03
- [x] Creates README operations for missing folders ✅ 2026-01-03
- [x] Creates patch operations for missing keys ✅ 2026-01-03
- [x] Creates patch operations for wrong types ✅ 2026-01-03
- [x] Warns on unfixable issues (bad frontmatter) ✅ 2026-01-03
- [x] ChangePlan is valid Pydantic output ✅ 2026-01-03

**Gate**: ✅ PASSED 2026-01-03 - Proceed to Step 8.3

---

### Step 8.3: Migration Executor & Verifier

**Objective**: Execute changeplan and verify compliance.

**Files**:

- `Workflow/scripts/migration/executor.py`
- `Workflow/scripts/migration/verifier.py`
- `Workflow/scripts/migrate.py` (CLI wrapper)

**Reuse**: `TransactionalApply` from Phase 5

**CLI**:

```bash
# Full pipeline
python scripts/migrate.py scan --scope "VAST"
python scripts/migrate.py analyze -m manifest.json
python scripts/migrate.py apply -c changeplan.json --dry-run
python scripts/migrate.py apply -c changeplan.json
python scripts/migrate.py verify --scope "VAST"
```

**migrate.py wrapper**:

```python
#!/usr/bin/env python3
"""
Migrate: CLI wrapper for migration phases.
"""

import click
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent / "migration"

@click.group()
def cli():
    """Vault migration tool."""
    pass

@cli.command()
@click.option("--scope", default="all")
@click.option("-o", "--output", default="manifest.json")
def scan(scope: str, output: str):
    """Scan vault for issues."""
    subprocess.run(["python", str(SCRIPT_DIR / "scanner.py"), "--scope", scope, "-o", output])

@cli.command()
@click.option("-m", "--manifest", required=True)
@click.option("-o", "--output", default="changeplan.json")
def analyze(manifest: str, output: str):
    """Generate fix operations."""
    subprocess.run(["python", str(SCRIPT_DIR / "analyzer.py"), "-m", manifest, "-o", output])

@cli.command()
@click.option("-c", "--changeplan", required=True)
@click.option("--dry-run", is_flag=True)
def apply(changeplan: str, dry_run: bool):
    """Apply changes."""
    cmd = ["python", str(SCRIPT_DIR / "executor.py"), "-c", changeplan]
    if dry_run:
        cmd.append("--dry-run")
    subprocess.run(cmd)

@cli.command()
@click.option("--scope", default="all")
def verify(scope: str):
    """Verify compliance."""
    subprocess.run(["python", str(SCRIPT_DIR / "verifier.py"), "--scope", scope])

if __name__ == "__main__":
    cli()
```

**Success Criteria**:

- [x] `migrate.py` CLI wrapper created ✅ 2026-01-03
- [x] `executor.py` uses `TransactionalApply` pattern ✅ 2026-01-03
- [x] Dry run shows planned changes without writing ✅ 2026-01-03
- [x] Apply is transactional (rollback on failure) ✅ 2026-01-03
- [x] `verifier.py` re-scans and reports compliance ✅ 2026-01-03
- [x] Full pipeline works end-to-end ✅ 2026-01-03
- [x] Migration is idempotent (running twice = no changes) ✅ 2026-01-03

**Test Results (VAST/People)**:

- 30 entities scanned
- 29 missing README.md detected
- 31 operations generated (29 creates + 2 patches)
- Full dry-run pipeline successful

**Gate**: ✅ PASSED 2026-01-03 - Phase 8 complete, proceed to Phase 9

---

## Phase 9: Ingestion

**Goal**: Set up capture mechanisms for raw content.

**Milestone**: M3 Ingestion Integrations  
**Estimated Time**: 1 session  
**Dependencies**: Phase 6 complete (core pipeline working)

---

### Step 9.1: Apple Mail Hotkey

**Objective**: Create macOS Shortcut for email capture.

**Deliverable**: `Workflow/automations/Capture Email to Notes.shortcut`

**Functionality** (from DESIGN.md 4.1):

- Hotkey: `⌃⌥⌘M`
- Export selected emails as `.eml` + `.md`
- Save to `Inbox/Email/`
- Filename: `YYYY-MM-DD_HHMMSS_NNNN_{Subject-slug}.{ext}`

**Implementation** (Apple Shortcut with embedded AppleScript):

```applescript
use AppleScript version "2.4"
use scripting additions

-- Configuration
set inboxPath to (POSIX path of (path to home folder)) & "Documents/Notes/Inbox/Email"

tell application "Mail"
    set selectedMessages to selection
    if (count of selectedMessages) = 0 then
        display dialog "No emails selected" buttons {"OK"} default button "OK"
        return
    end if

    set counter to 1
    repeat with theMessage in selectedMessages
        -- Build filename components
        set msgDate to date received of theMessage
        set dateStr to my formatDate(msgDate)
        set timeStr to my formatTime(msgDate)
        set subjectText to subject of theMessage
        set sluggedSubject to my slugify(subjectText)
        set counterStr to text -4 thru -1 of ("0000" & counter)

        set baseFilename to dateStr & "_" & timeStr & "_" & counterStr & "_" & sluggedSubject

        -- Export raw source (.eml)
        set rawSource to source of theMessage
        set emlPath to inboxPath & "/" & baseFilename & ".eml"
        my writeFile(emlPath, rawSource)

        -- Build markdown content
        set mdContent to "---" & linefeed
        set mdContent to mdContent & "from: " & my quoted(my senderString(theMessage)) & linefeed
        set mdContent to mdContent & "to: " & my quoted(my recipientString(theMessage)) & linefeed
        set mdContent to mdContent & "subject: " & my quoted(subjectText) & linefeed
        set mdContent to mdContent & "date: " & dateStr & linefeed
        set mdContent to mdContent & "source: email" & linefeed
        set mdContent to mdContent & "---" & linefeed & linefeed
        set mdContent to mdContent & "# " & subjectText & linefeed & linefeed
        set mdContent to mdContent & content of theMessage

        -- Export markdown
        set mdPath to inboxPath & "/" & baseFilename & ".md"
        my writeFile(mdPath, mdContent)

        set counter to counter + 1
    end repeat

    display notification (count of selectedMessages) & " email(s) saved to Notes" with title "Email Captured"
end tell

-- Helper functions
on formatDate(d)
    set y to year of d as string
    set m to text -2 thru -1 of ("0" & (month of d as integer))
    set dy to text -2 thru -1 of ("0" & day of d)
    return y & "-" & m & "-" & dy
end formatDate

on formatTime(d)
    set h to text -2 thru -1 of ("0" & hours of d)
    set mi to text -2 thru -1 of ("0" & minutes of d)
    set s to text -2 thru -1 of ("0" & seconds of d)
    return h & mi & s
end formatTime

on slugify(txt)
    set cleanText to ""
    repeat with c in characters of txt
        if c is in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -" then
            set cleanText to cleanText & c
        end if
    end repeat
    set AppleScript's text item delimiters to " "
    set words_ to text items of cleanText
    set AppleScript's text item delimiters to "-"
    set result to words_ as string
    set AppleScript's text item delimiters to ""
    return result
end slugify

on quoted(txt)
    return "\"" & txt & "\""
end quoted

on senderString(msg)
    tell application "Mail"
        return address of sender of msg
    end tell
end senderString

on recipientString(msg)
    tell application "Mail"
        set recips to {}
        repeat with r in to recipients of msg
            set end of recips to address of r
        end repeat
        set AppleScript's text item delimiters to ", "
        set result to recips as string
        set AppleScript's text item delimiters to ""
        return result
    end tell
end recipientString

on writeFile(posixPath, content)
    set fileRef to open for access POSIX file posixPath with write permission
    set eof fileRef to 0
    write content to fileRef as «class utf8»
    close access fileRef
end writeFile
```

**Test Criteria**:

1. Open Mail.app
2. Select 1-3 emails
3. Press `⌃⌥⌘M`
4. Verify files appear in `Inbox/Email/`

**Success Criteria**:

- [ ] Shortcut created and installed
- [ ] Hotkey triggers reliably
- [ ] Both `.eml` and `.md` files created
- [ ] Filename format matches `YYYY-MM-DD_HHMMSS_NNNN_{Subject-slug}.ext`
- [ ] Unicode subjects handled (stripped or transliterated)
- [ ] Markdown has valid frontmatter
- [ ] Notification confirms capture

**Gate**: Proceed to Step 9.2

---

### Step 9.2: MacWhisper Configuration

**Objective**: Document MacWhisper settings for transcript output.

**Deliverable**: `Workflow/docs/macwhisper-setup.md`

**Content**:

````markdown
# MacWhisper Configuration for Notes Vault

## Required Settings

1. **Output Format**: Markdown
2. **Speaker Diarization**: Enabled
3. **Auto-Export Path**: `~/Documents/Notes/Inbox/Transcripts/`
4. **Filename Pattern**: `%Y-%m-%d %H %M - {title}.md`

## Setting Up

1. Open MacWhisper → Preferences
2. Navigate to Export tab
3. Set output format to "Markdown"
4. Enable "Auto-export after transcription"
5. Set export folder to your Inbox/Transcripts path
6. Under Advanced, ensure speaker labels are enabled

## Filename Handling

MacWhisper uses the recording title (or "New Recording" if untitled).
For best results, name your recording before export:

- "Jeff Denworth 1-1"
- "Google GDC RFP Call"
- "Team Standup"

## Output Format

MacWhisper produces markdown like:

```markdown
# Meeting Title

## Transcript

**Speaker 1**: First person speaking...

**Speaker 2**: Response...
```
````

The automation pipeline expects this format and parses speaker labels accordingly.

## Troubleshooting

- **No speaker labels**: Ensure diarization is enabled in settings
- **Wrong folder**: Check the auto-export path is correct
- **Encoding issues**: MacWhisper outputs UTF-8 by default

````

**Success Criteria**:

- [ ] Documentation created
- [ ] Settings documented with screenshots (optional)
- [ ] Test recording exports correctly
- [ ] Speaker labels preserved in output
- [ ] Filename format correct

**Gate**: All Phase 9 checkboxes must pass before proceeding to Phase 10

---

## Phase 10: Operational Readiness

**Goal**: Create runbooks and troubleshooting documentation.

**Milestone**: M5 Operational Readiness
**Estimated Time**: 1 session
**Dependencies**: All previous phases complete

---

### Step 10.1: Runbooks

**Objective**: Create operational documentation.

**Files**:

- `Workflow/docs/runbook-daily.md`
- `Workflow/docs/runbook-troubleshooting.md`

**runbook-daily.md**:

```markdown
# Daily Processing Runbook

## End of Day Processing

### Prerequisites
- All meetings for the day are transcribed
- Relevant emails are captured
- Git tree is clean

### Steps

1. **Run the pipeline**
   ```bash
   cd ~/Documents/Notes/Workflow
   source .venv/bin/activate
   python scripts/process_inbox.py
````

2. **Review output**
   - Check for error messages
   - Review log file in `Workflow/logs/`
3. **Verify changes**

   ```bash
   git diff HEAD~1
   ```

4. **Morning review**
   - Open `_Tasks/*.md` dashboards
   - Search for `#needs-review` items
   - Resolve any flagged items

### If Processing Fails

See `runbook-troubleshooting.md`

### Metrics to Track

- Files processed per run
- Average processing time
- Failure rate
- Token usage (cost)

````

**runbook-troubleshooting.md**:

```markdown
# Troubleshooting Guide

## Common Issues

### "Git working directory has uncommitted changes"

**Cause**: Content directories have unstaged changes.

**Fix**:
```bash
# Check what's changed
git status

# Commit or stash changes
git add -A && git commit -m "wip"

# Or force processing
python scripts/process_inbox.py --allow-dirty
````

### "OpenAI API error: rate limit"

**Cause**: Too many requests too quickly.

**Fix**: Wait 60 seconds and retry. Consider reducing batch size.

### Extraction fails for specific file

**Cause**: Content too long, encoding issue, or ambiguous content.

**Fix**:

1. Check `_failed/` for the file and error log
2. Try manual extraction with verbose logging
3. Edit content to clarify (add context, fix encoding)

### Apply fails: rollback triggered

**Cause**: Standards validation failed or file conflict.

**Fix**:

1. Check the error message for specific file/issue
2. All changes have been rolled back automatically
3. Fix the issue in the changeplan or source
4. Re-run with `--apply-only`

### Duplicate notes created

**Cause**: Idempotency check failed or file was re-added.

**Fix**:

1. Delete duplicate(s)
2. Check `_archive/` for original source
3. Ensure source was properly archived

## Debug Commands

```bash
# Check what would be processed
python scripts/process_inbox.py --dry-run

# Process only extractions
python scripts/process_inbox.py --scope transcripts

# Apply existing changeplans only
python scripts/process_inbox.py --apply-only

# View recent logs
tail -f Workflow/logs/*.log | jq

# Check standards compliance
python -c "from scripts.utils.standards_check import *; print('OK')"
```

## Recovery Procedures

### Rollback last commit

```bash
git revert HEAD --no-commit
git commit -m "Revert: processing error"
```

### Restore from archive

```bash
cp Inbox/_archive/YYYY-MM-DD/filename.md Inbox/Transcripts/
```

### Full reset

```bash
git reset --hard origin/main
```

````

**Success Criteria**:

- [ ] Daily runbook created
- [ ] Troubleshooting guide covers common issues
- [ ] Debug commands documented
- [ ] Recovery procedures documented

**Gate**: Proceed to Step 10.2

---

### Step 10.2: Final Validation

**Objective**: Verify complete system works end-to-end.

**Validation Checklist**:

```bash
# 1. Verify all files exist
ls -la Workflow/scripts/
ls -la Workflow/scripts/utils/
ls -la Workflow/models/
ls -la Workflow/templates/
ls -la Workflow/profiles/

# 2. Run tests
pytest Workflow/tests/ -v

# 3. Dry run with real data
python scripts/process_inbox.py --dry-run

# 4. Process one file manually
python scripts/extract.py Inbox/Transcripts/test.md
python scripts/plan.py Inbox/_extraction/test.extraction.json
python scripts/apply.py --dry-run

# 5. Full pipeline
python scripts/process_inbox.py --scope transcripts

# 6. Verify output
git log -1
git diff HEAD~1 --stat
````

**Success Criteria**:

- [ ] All files in File Checklist exist
- [ ] Tests pass
- [ ] Dry run completes without error
- [ ] Single file processing works
- [ ] Full pipeline completes
- [ ] Git commit created
- [ ] Notes appear in correct folders
- [ ] Frontmatter is standards-compliant

---

## Milestone Summary

| Phase  | Milestone | Deliverables                        | Test                    | Est. Sessions |
| ------ | --------- | ----------------------------------- | ----------------------- | ------------- |
| **0**  | M0        | Models, config, structure           | Import & serialize      | 1             |
| **1**  | M0        | Patch primitives, git ops, entities | Unit tests              | 1-2           |
| **2**  | M0        | Templates, profiles, prompts        | Render tests            | 1             |
| **3**  | M1        | Extract script                      | Single file extraction  | 1-2           |
| **4**  | M1        | Plan script                         | ChangePlan generation   | 1             |
| **5**  | M1        | Apply script                        | Transactional execution | 1-2           |
| **6**  | M1→M2     | Orchestrator, logging               | End-to-end pipeline     | 1             |
| **7**  | M2        | Standards checks, tests             | Compliance validation   | 1-2           |
| **8**  | M4        | Migration scripts                   | Vault compliance        | 1-2           |
| **9**  | M3        | Ingestion automation                | Capture to Inbox        | 1             |
| **10** | M5        | Runbooks, final validation          | Full system test        | 1             |

**Total Estimated Sessions**: 11-16

---

## Appendix: File Checklist

All files to be created, organized by phase. Check off as completed.

### Phase 0: Foundation

- [ ] `Workflow/models/__init__.py`
- [ ] `Workflow/models/extraction.py`
- [ ] `Workflow/models/changeplan.py`
- [ ] `Workflow/scripts/__init__.py`
- [ ] `Workflow/scripts/utils/__init__.py`
- [ ] `Workflow/scripts/utils/config.py`
- [ ] `Workflow/scripts/utils/paths.py`
- [ ] `Workflow/scripts/utils/fs.py`

### Phase 1: Core Infrastructure

- [ ] `Workflow/scripts/utils/frontmatter.py`
- [ ] `Workflow/scripts/utils/patch_primitives.py`
- [ ] `Workflow/scripts/utils/git_ops.py`
- [ ] `Workflow/scripts/utils/entities.py`
- [ ] `Workflow/entities/aliases.yaml`

### Phase 2: Templates & Profiles

- [ ] `Workflow/scripts/utils/templates.py`
- [ ] `Workflow/scripts/utils/profiles.py`
- [ ] `Workflow/templates/people.md.j2`
- [ ] `Workflow/templates/customer.md.j2`
- [ ] `Workflow/templates/projects.md.j2`
- [ ] `Workflow/templates/rob.md.j2`
- [ ] `Workflow/templates/journal.md.j2`
- [ ] `Workflow/templates/readme-migration.md.j2`
- [ ] `Workflow/profiles/work_sales.yaml`
- [ ] `Workflow/profiles/work_engineering.yaml`
- [ ] `Workflow/profiles/work_leadership.yaml`
- [ ] `Workflow/profiles/personal.yaml`
- [ ] `Workflow/prompts/system-extractor.md.j2`
- [ ] `Workflow/prompts/system-planner.md.j2`

### Phase 3: Extract Pipeline

- [x] `Workflow/scripts/utils/openai_client.py` ✅
- [x] `Workflow/scripts/extract.py` ✅

### Phase 4: Plan Pipeline

- [x] `Workflow/scripts/plan.py` ✅

### Phase 5: Apply Pipeline

- [x] `Workflow/scripts/apply.py` ✅

### Phase 6: Orchestration

- [x] `Workflow/scripts/process_inbox.py` ✅
- [x] `Workflow/scripts/utils/logging.py` ✅

### Phase 7: Hardening

- [x] `Workflow/scripts/utils/standards_check.py` ✅
- [x] `Workflow/scripts/utils/validation.py` ✅ (consolidated changeplan validation)
- [x] `Workflow/tests/__init__.py` ✅
- [x] `Workflow/tests/conftest.py` ✅
- [x] `Workflow/tests/fixtures/sample-meeting-transcript.md` ✅
- [x] `Workflow/tests/fixtures/sample-extraction.json` ✅
- [x] `Workflow/tests/fixtures/sample-changeplan.json` ✅
- [x] `Workflow/tests/fixtures/sample-readme.md` ✅
- [x] `Workflow/tests/test_patch_primitives.py` ✅ (13 tests)
- [x] `Workflow/tests/test_standards.py` ✅ (12 tests)
- [x] `Workflow/tests/test_validation.py` ✅ (12 tests)
- [x] `Workflow/tests/test_rollback.py` ✅ (8 tests)

### Phase 8: Migration ✅

- [x] `Workflow/scripts/migration/__init__.py` ✅ 2026-01-03
- [x] `Workflow/scripts/migration/models.py` ✅ 2026-01-03
- [x] `Workflow/scripts/migration/scanner.py` ✅ 2026-01-03
- [x] `Workflow/scripts/migration/analyzer.py` ✅ 2026-01-03
- [x] `Workflow/scripts/migration/executor.py` ✅ 2026-01-03
- [x] `Workflow/scripts/migration/verifier.py` ✅ 2026-01-03
- [x] `Workflow/scripts/migrate.py` ✅ 2026-01-03

### Phase 9: Ingestion

- [ ] `Workflow/automations/Capture Email to Notes.shortcut`
- [ ] `Workflow/docs/macwhisper-setup.md`

### Phase 10: Operational Readiness

- [ ] `Workflow/docs/runbook-daily.md`
- [ ] `Workflow/docs/runbook-troubleshooting.md`

### Configuration (exists or needs update)

- [ ] `Workflow/config.yaml`
- [ ] `Workflow/requirements.txt`
- [ ] `Workflow/.env.example`

---

## Appendix: Verification Commands Reference

Quick reference for verification at each phase gate.

```bash
# Phase 0 Gate
python -c "from models.extraction import ExtractionV1; from models.changeplan import ChangePlan; print('✓ Models OK')"

# Phase 1 Gate
python -c "from scripts.utils.frontmatter import parse_frontmatter; from scripts.utils.patch_primitives import upsert_frontmatter; from scripts.utils.git_ops import is_clean; from scripts.utils.entities import resolve_entity; print('✓ Infrastructure OK')"

# Phase 2 Gate
python -c "from scripts.utils.templates import render_note; from scripts.utils.profiles import get_profile_for_path; print('✓ Templates OK')"

# Phase 3 Gate
python scripts/extract.py --help && echo '✓ Extract OK'

# Phase 4 Gate
python scripts/plan.py --help && echo '✓ Plan OK'

# Phase 5 Gate
python scripts/apply.py --help && echo '✓ Apply OK'

# Phase 6 Gate
python scripts/process_inbox.py --help && echo '✓ Orchestration OK'

# Phase 7 Gate
pytest Workflow/tests/ -v && echo '✓ Tests OK'

# Phase 8 Gate
python scripts/migrate.py --help && echo '✓ Migration OK'

# Full System Test
python scripts/process_inbox.py --dry-run && echo '✓ Full System OK'
```

---

_Document Version: 2.0.0_
_Last Updated: 2026-01-06_
_Status: Active - Phase 0 Ready to Begin_
