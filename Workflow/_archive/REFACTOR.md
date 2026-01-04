# Refactor Plan: migrate.py Implementation Design

> **Version**: 1.0.0 (Final)  
> **Created**: 2026-01-03  
> **Status**: Ready for Implementation  
> **Related**: [STANDARDS.md](STANDARDS.md) | [DESIGN.md](DESIGN.md)

This document provides the technical specification for `migrate.py`, a one-time script to bring existing vault content into compliance with [STANDARDS.md](STANDARDS.md).

---

## 1. Problem Statement

The vault contains 187 files across 53 entity folders with:

- **52 missing README.md** root documents
- **6 different `type:` values** that need normalization
- **~12 files with malformed frontmatter** (`{{DATE}}` placeholders)
- **~25 task aggregation files** mixed with notes
- **~20 files with non-standard naming**

**Goal**: Automate remediation using the same transactional pattern as the main pipeline.

---

## 2. Architecture

The migration script follows the same 4-phase pattern as `process_inbox.py`:

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    scan     │→ │   analyze   │→ │    apply    │→ │   verify    │
│             │  │             │  │             │  │             │
│ Inventory   │  │ Classify    │  │ Execute ops │  │ Compliance  │
│ Parse FM    │  │ Plan ops    │  │ Transactional │ │ Report      │
│ Detect bugs │  │ (No AI)     │  │ Git commit  │  │             │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
       │                │                │                │
       ▼                ▼                ▼                ▼
  manifest.json   changeplan.json   [file changes]   report.md
```

**Key difference from daily pipeline**: Migration uses **no AI calls**. All operations are deterministic based on file analysis.

---

## 3. Module Structure

```
Workflow/scripts/
├── migrate.py              # CLI entry point
└── migration/
    ├── __init__.py
    ├── scanner.py          # Phase 1: Scan vault, build manifest
    ├── analyzer.py         # Phase 2: Classify, plan operations
    ├── executor.py         # Phase 3: Apply changes (transactional)
    ├── verifier.py         # Phase 4: Compliance checking
    └── models.py           # Pydantic models
```

---

## 4. Data Models

### 4.1 Manifest Schema

```python
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class IssueType(str, Enum):
    MISSING_README = "missing_readme"
    BAD_FRONTMATTER = "bad_frontmatter"
    WRONG_TYPE = "wrong_type"
    BAD_FILENAME = "bad_filename"
    PLACEHOLDER = "placeholder"

class Issue(BaseModel):
    type: IssueType
    file: str | None = None
    details: str | None = None

class NoteInfo(BaseModel):
    path: str                       # Relative to vault root
    filename: str
    frontmatter: dict | None
    has_frontmatter: bool
    current_type: str | None
    inferred_date: str | None       # YYYY-MM-DD
    issues: list[Issue] = []

class EntityFolder(BaseModel):
    path: str                       # e.g., "VAST/People/Jeff Denworth"
    entity_type: str                # person, account, project, rob
    entity_name: str                # e.g., "Jeff Denworth"
    has_readme: bool
    notes: list[NoteInfo] = []
    note_count: int = 0
    last_contact: str | None        # YYYY-MM-DD from most recent note
    issues: list[Issue] = []

class Manifest(BaseModel):
    version: str = "1.0"
    scan_date: datetime
    vault_root: str
    statistics: dict
    entities: list[EntityFolder]
```

### 4.2 ChangePlan Schema

```python
class OperationType(str, Enum):
    CREATE_README = "create_readme"
    FIX_FRONTMATTER = "fix_frontmatter"
    RENAME_FILE = "rename_file"
    ARCHIVE_FILE = "archive_file"

class FrontmatterPatch(BaseModel):
    field: str
    action: str                     # "set", "remove"
    old_value: str | None = None
    new_value: str | None = None

class Operation(BaseModel):
    op: OperationType
    path: str                       # Target file (relative)
    new_path: str | None = None     # For rename operations
    template: str | None = None     # For create operations
    context: dict | None = None     # Template variables
    patches: list[FrontmatterPatch] | None = None

class ChangePlan(BaseModel):
    version: str = "1.0"
    source_manifest: str
    scope: str                      # e.g., "VAST/People" or "*"
    created_at: datetime
    operations: list[Operation]
    statistics: dict
```

---

## 5. Phase 1: Scanner

### 5.1 Entity Detection Rules

```python
ENTITY_PATTERNS = {
    "person": ["VAST/People/*", "Personal/People/*"],
    "account": ["VAST/Customers and Partners/*"],
    "project": ["VAST/Projects/*", "Personal/Projects/*"],
    "rob": ["VAST/ROB/*"],
}
```

### 5.2 Issue Detection

```python
def detect_issues(folder: EntityFolder, notes: list[NoteInfo]) -> list[Issue]:
    issues = []

    # Missing README
    if not (vault_root / folder.path / "README.md").exists():
        issues.append(Issue(type=IssueType.MISSING_README))

    # Per-note issues
    for note in notes:
        # Placeholder frontmatter
        if note.frontmatter:
            for key, value in note.frontmatter.items():
                if isinstance(value, str) and "{{" in value:
                    issues.append(Issue(
                        type=IssueType.PLACEHOLDER,
                        file=note.filename,
                        details=f"{key}: {value}"
                    ))

        # Wrong type
        expected_type = resolve_type_from_location(folder.path)
        if note.current_type and note.current_type != expected_type:
            issues.append(Issue(
                type=IssueType.WRONG_TYPE,
                file=note.filename,
                details=f"has '{note.current_type}', expected '{expected_type}'"
            ))

    return issues
```

### 5.3 CLI Command

```bash
python scripts/migrate.py scan --scope "VAST/People" --output manifest.json
```

---

## 6. Phase 2: Analyzer

### 6.1 Type Resolution

```python
TYPE_NORMALIZATION = {
    "1-1": "people",
    "People": "people",
    "group-meeting": None,  # Resolve by location
    "Customer": "customer",
    "Partners": "partners",
}

def resolve_type(path: str, current_type: str | None) -> str:
    """Determine canonical type for a note."""

    # Location-based resolution
    if "/People/" in path:
        return "people"
    if "/Customers and Partners/" in path:
        return "customer"
    if "/Projects/" in path:
        return "projects"
    if "/ROB/" in path:
        return "rob"

    # Normalization map
    if current_type and current_type in TYPE_NORMALIZATION:
        return TYPE_NORMALIZATION[current_type] or "unknown"

    return (current_type or "unknown").lower()
```

### 6.2 README Generation

For README.md creation, use a simple template (no AI):

```python
def generate_readme_context(entity: EntityFolder) -> dict:
    """Build template context for README.md."""

    return {
        "entity_type": entity.entity_type,
        "entity_name": entity.entity_name,
        "entity_slug": slugify(entity.entity_name),
        "last_contact": entity.last_contact,
        "note_count": entity.note_count,
        "folder_path": entity.path,
        "created_date": datetime.now().strftime("%Y-%m-%d"),
    }
```

### 6.3 Frontmatter Patch Generation

```python
def generate_frontmatter_patches(
    note: NoteInfo,
    target_type: str,
    entity_name: str
) -> list[FrontmatterPatch]:
    patches = []
    fm = note.frontmatter or {}

    # Type normalization
    if fm.get("type") != target_type:
        patches.append(FrontmatterPatch(
            field="type",
            action="set",
            old_value=fm.get("type"),
            new_value=target_type
        ))

    # Date field
    if "date" not in fm and note.inferred_date:
        patches.append(FrontmatterPatch(
            field="date",
            action="set",
            new_value=note.inferred_date
        ))

    # Entity-specific field
    entity_field = {
        "people": "person",
        "customer": "account",
        "projects": "project",
    }.get(target_type)

    if entity_field and entity_field not in fm:
        patches.append(FrontmatterPatch(
            field=entity_field,
            action="set",
            new_value=entity_name
        ))

    # Fix placeholders
    for field, value in fm.items():
        if isinstance(value, str) and "{{" in value:
            patches.append(FrontmatterPatch(
                field=field,
                action="set",
                old_value=value,
                new_value=note.inferred_date or datetime.now().strftime("%Y-%m-%d")
            ))

    return patches
```

### 6.4 CLI Command

```bash
python scripts/migrate.py analyze --manifest manifest.json --output changeplan.json
```

---

## 7. Phase 3: Executor (Transactional)

Uses the same `TransactionalApply` class from `apply.py` with rollback support:

```python
class MigrationExecutor:
    def __init__(self, vault_root: Path, run_id: str):
        self.vault_root = vault_root
        self.backup_dir = vault_root / ".workflow_backups" / run_id
        self.created_files: list[Path] = []
        self.backed_up: dict[Path, Path] = {}

    def execute(self, changeplan: ChangePlan):
        """Execute migration with rollback on failure."""

        # 1. Require clean git tree
        if not self._git_is_clean():
            raise RuntimeError("Git working directory is dirty.")

        try:
            # 2. Backup files that will be modified
            for op in changeplan.operations:
                target = self.vault_root / op.path
                if target.exists():
                    self._backup(target)

            # 3. Execute operations
            for op in changeplan.operations:
                self._apply_operation(op)

            # 4. Git commit
            self._git_commit(changeplan)

            # 5. Cleanup backups
            shutil.rmtree(self.backup_dir, ignore_errors=True)

        except Exception as e:
            self._rollback()
            raise
```

### 7.1 CLI Command

```bash
python scripts/migrate.py apply --changeplan changeplan.json
```

With dry-run:

```bash
python scripts/migrate.py apply --changeplan changeplan.json --dry-run
```

---

## 8. Phase 4: Verifier

```python
def verify_compliance(vault_root: Path, scope: str) -> dict:
    """Check vault compliance with STANDARDS.md."""

    results = {
        "compliant": 0,
        "non_compliant": 0,
        "issues": []
    }

    for entity in scan_entities(vault_root, scope):
        # Check README exists
        readme_path = vault_root / entity.path / "README.md"
        if not readme_path.exists():
            results["issues"].append(f"Missing README: {entity.path}")
            results["non_compliant"] += 1
            continue

        # Check all notes have valid frontmatter
        for note in entity.notes:
            if not note.has_frontmatter:
                results["issues"].append(f"Missing frontmatter: {note.path}")
                results["non_compliant"] += 1
            elif note.issues:
                for issue in note.issues:
                    results["issues"].append(f"{issue.type}: {note.path}")
                results["non_compliant"] += 1
            else:
                results["compliant"] += 1

    return results
```

### 8.1 CLI Command

```bash
python scripts/migrate.py verify --scope "VAST"
```

---

## 9. README Template

`Workflow/templates/readme-migration.md.j2`:

````jinja
---
type: "{{ entity_type }}-root"
{% if entity_type == "person" %}
name: "{{ entity_name }}"
role: ""
company: ""
{% elif entity_type == "project" %}
project: "{{ entity_name }}"
status: "active"
{% elif entity_type == "account" %}
account: "{{ entity_name }}"
stage: "active"
{% endif %}
last_contact: "{{ last_contact or created_date }}"
tags:
  - "{{ entity_type }}/{{ entity_slug }}"
---

# {{ entity_name }}

## Overview

<!-- Add description here -->

## Recent Context

{% if recent_context %}
{% for item in recent_context %}
- {{ item.date }}: {{ item.summary }}
{% endfor %}
{% else %}
<!-- Recent interactions will be added here -->
{% endif %}

## Open Items

```dataview
TASK
FROM "{{ folder_path }}"
WHERE !completed
SORT due ASC
````

## Notes

```dataview
LIST
FROM "{{ folder_path }}"
WHERE file.name != "README"
SORT date DESC
LIMIT 10
```

````

---

## 10. Execution Plan

### 10.1 Rollout Order

Execute migration in phases to limit blast radius:

1. **VAST/People** (32 folders) — Highest value, good test set
2. **VAST/Customers and Partners** (5 folders)
3. **VAST/Projects** (12 folders)
4. **VAST/ROB** (3 folders)
5. **Personal** (remaining)

### 10.2 Pre-Migration Checklist

- [ ] Commit all pending changes
- [ ] Create backup tag: `git tag pre-migration-$(date +%Y-%m-%d)`
- [ ] Run `migrate.py scan --scope "*"` to generate full manifest
- [ ] Review manifest for unexpected findings
- [ ] Run `migrate.py analyze` with `--dry-run` first

### 10.3 Commands

```bash
# Full workflow for one scope
cd ~/Documents/Notes/Workflow
source .venv/bin/activate

# 1. Scan
python scripts/migrate.py scan --scope "VAST/People" -o manifest-people.json

# 2. Analyze
python scripts/migrate.py analyze -m manifest-people.json -o changeplan-people.json

# 3. Preview
python scripts/migrate.py apply -c changeplan-people.json --dry-run

# 4. Apply (transactional)
python scripts/migrate.py apply -c changeplan-people.json

# 5. Verify
python scripts/migrate.py verify --scope "VAST/People"
````

---

## 11. Implementation Checklist

- [ ] Create `Workflow/scripts/migration/` package
- [ ] Implement `models.py` with Pydantic schemas
- [ ] Implement `scanner.py`
- [ ] Implement `analyzer.py`
- [ ] Implement `executor.py` (reuse `patch_primitives.py`)
- [ ] Implement `verifier.py`
- [ ] Create `readme-migration.md.j2` template
- [ ] Wire up `migrate.py` CLI with Click
- [ ] Test on single folder first
- [ ] Execute rollout plan

---

## Appendix: Statistics from Vault Audit

| Category               | Count |
| ---------------------- | ----- |
| Total entity folders   | 53    |
| Missing README.md      | 52    |
| Total markdown files   | 187   |
| Files with frontmatter | ~160  |
| Malformed frontmatter  | ~12   |
| Distinct `type` values | 6     |
| Pending in Inbox       | 13    |
