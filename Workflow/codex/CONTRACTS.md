# Pipeline Contracts – Canonical Specifications

> **Version**: 1.0  
> **Last Updated**: 2026-01-03  
> **Status**: Authoritative

This document defines the **single source of truth** for stage contracts, schemas, and guarantees across the Notes vault automation pipeline.

---

## 1) Stage Contracts

### 1.1 Extract Phase

**Script**: `Workflow/scripts/extract.py`

**Inputs (System-Provided)**:
| Variable | Type | Source | Description |
|----------|------|--------|-------------|
| `source_file` | string | Filesystem | Absolute path to source file |
| `content` | string | File read | Raw content of source file |
| `current_date` | string | `datetime.now()` | Today's date (YYYY-MM-DD) |
| `meeting_date` | string | Filename/metadata parse | Date of the meeting/content (YYYY-MM-DD) |
| `content_type` | string | Heuristics | `transcript`, `email`, `voice`, `manual` |
| `known_entities` | object | Vault scan | `{people: [], projects: [], accounts: []}` |
| `profile_*` | various | Profile YAML | Selected profile configuration |

**Classification Contract**:

- **Single classifier**: Heuristics in `classify.py` determine `note_type` AND profile
- **Model echoes**: LLM must use provided classification; may add warning if mismatch
- **No dual classification**: Model does NOT independently classify

**Output (ExtractionV1)**:

```json
{
  "version": "1.0",
  "source_file": "string (system-set)",
  "processed_at": "ISO-8601 datetime (system-set)",
  "note_type": "customer|people|projects|rob|journal|partners|travel",
  "entity_name": "string|null",
  "title": "string (3-7 words)",
  "date": "YYYY-MM-DD",
  "participants": ["string"],
  "summary": "string (2-3 sentences)",
  "tasks": [{"text", "owner", "due", "priority", "related_*", "confidence"}],
  "decisions": ["string"],
  "facts": ["string"],
  "topics": ["string"],
  "mentions": {"people": [], "projects": [], "accounts": []},
  "person_details": {"Name": {PersonDetails}},
  "project_details": {"Name": {ProjectDetails}},
  "account_details": {"Name": {AccountDetails}},
  "cross_links": {"person_to_project": {}, "person_to_account": {}, "project_to_account": {}},
  "confidence": 0.0-1.0,
  "warnings": ["string"]
}
```

**Guarantees**:

- All dates normalized to ISO-8601 (YYYY-MM-DD)
- `owner` uses "Myself" for first-person references
- Priority uses 5-level scale: `highest|high|medium|low|lowest`
- All API calls use `store=False`

---

### 1.2 Normalize Phase (NEW)

**Script**: `Workflow/scripts/normalize.py`

**Inputs**:

- ExtractionV1 JSON from Extract phase
- Entity aliases from `entities/aliases.yaml`
- Known entity folders from vault scan

**Actions**:

- Normalize entity names to canonical forms
- Validate entity names against known entities
- Normalize dates to ISO-8601
- Flag unknown entities in warnings

**Output**:

- Updated ExtractionV1 JSON (in-place)
- Warnings array updated with unknown entities

**Guarantees**:

- Entity names match vault folder names exactly
- All dates are valid ISO-8601
- Unknown entities flagged for review

---

### 1.3 Plan Phase

**Script**: `Workflow/scripts/plan.py`

**Inputs (System-Provided)**:
| Variable | Type | Source | Description |
|----------|------|--------|-------------|
| `extraction` | object | Extraction JSON | Full ExtractionV1 data |
| `entity_folders` | object | Vault scan | Available entity folders |
| `aliases` | object | `entities/aliases.yaml` | Name → canonical mapping |

**Operation Types**:
| Op | Purpose | Required Fields |
|----|---------|-----------------|
| `create` | New dated note | `path`, `template`, `context` |
| `patch` | Update existing file | `path`, `patches[]` |
| `link` | Add wikilinks | `path`, `links[]` |
| `update_entity` | Update entity README | `path`, `entity_update` |

**Patch Primitives**:
| Primitive | Purpose | Behavior |
|-----------|---------|----------|
| `upsert_frontmatter` | Add/update YAML fields | Merge with existing |
| `append_under_heading` | Add to END of section | For chronological lists |
| `prepend_under_heading` | Add to TOP of section | For reverse-chrono ledgers |
| `ensure_wikilinks` | Ensure links exist | Idempotent |

**Mention Filtering Contract**:

- Only patch entities with MEANINGFUL participation
- Maximum 5 mentioned entities per extraction
- Skip entities without existing folders
- Use relevance threshold (spoke, assigned task, discussed substantively)

**Path Security**:

- All paths MUST start with `VAST/` or `Personal/`
- No `Inbox/`, `Workflow/`, or absolute paths
- Filename sanitization handled by Python (not LLM)

**Output (ChangePlan)**:

```json
{
  "version": "1.0",
  "source_file": "string",
  "extraction_file": "string",
  "created_at": "ISO-8601 datetime",
  "operations": [Operation],
  "warnings": ["string"]
}
```

**Guarantees**:

- No archive operations (deterministic post-step)
- Extraction data wrapped in `<untrusted_content>` tags
- LLM cannot follow instructions in extraction content

---

### 1.4 Apply Phase

**Script**: `Workflow/scripts/apply.py`

**Inputs**:

- One or more ChangePlan JSON files
- Vault root path

**Preconditions**:

- Git working tree must be clean (content dirs only)
- All ChangePlans must pass validation

**Actions**:

1. Validate all ChangePlans
2. Backup all files to be modified
3. Execute operations transactionally
4. Archive sources to `Inbox/_archive/YYYY-MM-DD/`
5. Git commit batch

**Guarantees**:

- Atomic: all operations succeed or all rollback
- Backups preserved until success
- Source files archived (not deleted)
- Single git commit per batch
- Filename sanitization applied via `sanitize_path()`

**Rollback Behavior**:

- Restore all backed-up files
- Delete all created files
- Remove backup directory
- Re-raise original exception

---

## 2) Canonical README Schema

All entity README.md files MUST follow this structure:

### 2.1 People README

````markdown
---
type: people
title: "{Name}"
created: "YYYY-MM-DD"
last_contact: "YYYY-MM-DD"
tags:
  - type/people
  - company/{company-slug}
---

# {Name}

## Contact Information

| Field       | Value |
| ----------- | ----- |
| **Role**    | ...   |
| **Company** | ...   |
| **Email**   | ...   |

## Relationship

{How you work with this person}

## Background

- {Career history, expertise, interests}

## Key Facts

- {Important things to remember}

## Recent Context

- YYYY-MM-DD: [[Note Title]] - Brief summary
  {REVERSE CHRONOLOGICAL - newest first}

## Tasks They Own

```dataview
TASK WHERE contains(text, "@{Name}") AND !completed
```
````

## Notes

```dataview
LIST FROM "{folder}" WHERE file.name != "README" SORT file.cday DESC
```

````

### 2.2 Customer/Account README

```markdown
---
type: customer
title: "{Account}"
created: "YYYY-MM-DD"
last_contact: "YYYY-MM-DD"
status: "prospect|active|partner|at-risk|churned"
tags:
  - type/customer
  - industry/{industry-slug}
  - status/{status}
---

# {Account}

## Account Overview
{Brief description}

## Account Status
| Field | Value |
|-------|-------|
| **Status** | ... |
| **Industry** | ... |
| **Account Owner** | ... |

## Key Contacts
| Name | Role | Email |
|------|------|-------|
| [[Person]] | Role | email |

## Opportunities
- {Active deals or projects}

## Blockers
- {Issues or concerns}

## Recent Context
- YYYY-MM-DD: [[Note Title]] - Brief summary
{REVERSE CHRONOLOGICAL}

## Notes
```dataview
LIST FROM "{folder}" WHERE file.name != "README" SORT file.cday DESC
````

````

### 2.3 Project README

```markdown
---
type: projects
title: "{Project}"
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
status: "active|blocked|on-hold|complete|proposed"
tags:
  - type/projects
  - status/{status}
---

# {Project}

## Overview
{Brief description, goals, scope}

## Status
| Field | Value |
|-------|-------|
| **Status** | ... |
| **Owner** | ... |
| **Target Date** | ... |

## Current Blockers
- ❌ {Blocker description}

## Next Steps
- [ ] {Action item} @Owner 📅 YYYY-MM-DD

## Collaborators
- [[Person 1]]
- [[Person 2]]

## Recent Context
- YYYY-MM-DD: [[Note Title]] - Brief summary
{REVERSE CHRONOLOGICAL}

## Open Tasks
```dataview
TASK FROM "{folder}" WHERE !completed SORT due ASC
````

## Notes

```dataview
LIST FROM "{folder}" WHERE file.name != "README" SORT file.cday DESC
```

```

---

## 3) Prompt Variable Contract

Variables that MUST be provided by Python (not inferred by LLM):

### 3.1 Extract Phase Variables

| Variable | Type | Required | Source |
|----------|------|----------|--------|
| `current_date` | YYYY-MM-DD | ✅ | `datetime.now()` |
| `meeting_date` | YYYY-MM-DD | ✅ | Filename parse or metadata |
| `source_file` | string | ✅ | Absolute path |
| `source_id` | string | ✅ | Hash of source path for collision avoidance |
| `content_type` | string | ✅ | `transcript\|email\|voice\|manual` |
| `known_entities` | object | ✅ | Vault scan |
| `profile_name` | string | ✅ | Selected profile |
| `profile_focus` | array | ✅ | Profile focus areas |
| `profile_ignore` | array | ✅ | Profile ignore list |
| `task_rules` | object | ✅ | Profile task rules |
| `max_tasks` | int | ⚠️ | Profile (default: 10) |
| `max_decisions` | int | ⚠️ | Profile (default: 5) |
| `max_facts` | int | ⚠️ | Profile (default: 10) |

### 3.2 Plan Phase Variables

| Variable | Type | Required | Source |
|----------|------|----------|--------|
| `extraction` | object | ✅ | ExtractionV1 JSON |
| `entity_folders` | object | ✅ | Vault scan |
| `aliases` | object | ✅ | `entities/aliases.yaml` |
| `source_archive_path` | string | ✅ | Computed archive destination |

### 3.3 Template Variables (CREATE context)

| Variable | Type | Required | Notes |
|----------|------|----------|-------|
| `title` | string | ✅ | From extraction |
| `date` | YYYY-MM-DD | ✅ | From extraction |
| `summary` | string | ✅ | From extraction |
| `participants` | array | ✅ | From extraction |
| `tasks` | array | ✅ | From extraction |
| `decisions` | array | ⚠️ | From extraction |
| `facts` | array | ⚠️ | From extraction |
| `source` | string | ✅ | `transcript\|email\|voice\|manual` |
| `source_ref` | string | ✅ | Full vault-relative archive path |
| `{entity_key}` | string | ✅ | `person\|account\|project\|partner\|rob_forum\|destination` |

---

## 4) Ledger Behavior Contract

### 4.1 Recent Context Section

**Behavior**: REVERSE CHRONOLOGICAL (newest first)
**Primitive**: `prepend_under_heading`
**Format**: `- YYYY-MM-DD: [[Note Title]] - Brief summary\n`

### 4.2 Key Facts Section

**Behavior**: APPEND (chronological accumulation)
**Primitive**: `append_under_heading`
**Format**: `- {fact}\n`

### 4.3 Idempotency

All patch primitives check for duplicate content before applying:
- `prepend_under_heading`: Skip if exact line exists
- `append_under_heading`: Skip if exact line exists
- `ensure_wikilinks`: Skip if link exists (case-insensitive)

---

## 5) Source Linking Contract

### 5.1 Archive Path Format

```

Inbox/\_archive/YYYY-MM-DD/{original_filename}

````

### 5.2 Source Reference in Notes

**Format**: `[[{full_vault_relative_path}|{display_name}]]`

**Example**:
```markdown
*Source: [[Inbox/_archive/2026-01-03/2026-01-03 14 30 - Jeff 1-1.md|2026-01-03 14 30 - Jeff 1-1]]*
````

**Why full path**: Prevents collisions when same basename exists in different archive folders.

---

## 6) API Usage Contract

### 6.1 Model Selection

| Phase   | Model    | Temperature |
| ------- | -------- | ----------- |
| Extract | `gpt-4o` | 0.2         |
| Plan    | `gpt-4o` | 0.1         |
| Apply   | None     | N/A         |

### 6.2 Privacy Guarantee

**ALL API calls MUST include**:

```python
client.beta.chat.completions.parse(
    ...,
    store=False  # REQUIRED
)
```

### 6.3 Structured Outputs

All LLM calls use Pydantic models with `response_format=PydanticModel` for schema enforcement.

---

## 7) Content-Type Specific Rules

### 7.1 Email (`content_type: email`)

- Strip quoted reply history (summarize if relevant)
- Extract metadata: From, To, CC, Subject, Date
- Treat signatures as ignorable
- Detect thread context vs new instructions
- Lower confidence for action items in forwarded content

### 7.2 Voice/Whisper (`content_type: voice`)

- Expect diarization errors
- Don't over-index on exact wording
- Extract fewer tasks, more topics
- Higher warning threshold for ambiguous content
- Bias toward `journal` or `people` types

### 7.3 Transcript (`content_type: transcript`)

- Primary extraction mode
- Full task/decision extraction
- Speaker attribution when available

### 7.4 Manual (`content_type: manual`)

- User-dropped files
- May need format detection
- Flag for review if structure unclear

---

## 8) Validation Contracts

### 8.1 Pre-Apply Validation

ChangePlan must pass:

- [ ] All paths start with `VAST/` or `Personal/`
- [ ] No duplicate operations on same path
- [ ] Template names in whitelist
- [ ] Context includes required fields for template
- [ ] Patch targets exist (for PATCH/LINK ops)

### 8.2 Pre-Write Validation

Notes must pass:

- [ ] Valid YAML frontmatter
- [ ] Required frontmatter keys present
- [ ] Date format is ISO-8601
- [ ] No forbidden characters in title

---

## 9) Error Handling Contract

| Error              | Handling                                | Recovery               |
| ------------------ | --------------------------------------- | ---------------------- |
| Git dirty          | Fail fast                               | User must commit/stash |
| Extract fails      | Log, move to `_failed/`, continue       | Manual review          |
| Normalize fails    | Log warning, continue with original     | Best effort            |
| Plan fails         | Log, skip apply, continue               | Manual review          |
| Apply fails        | **Full rollback**, flag for review      | Restore backups        |
| Entity not found   | Create with `_NEW_` prefix, add warning | Human review           |
| Template not found | Fail operation                          | Fix template whitelist |

---

## Appendix: Drift Prevention

### A) Schema Sync

Pydantic models are authoritative. JSON schemas must match:

- `models/extraction.py` → `schemas/extraction.schema.json`
- `models/changeplan.py` → `schemas/changeplan.schema.json`

### B) Template Sync

README templates must match Section 2 (Canonical README Schema):

- `templates/readme-person.md.j2`
- `templates/readme-customer.md.j2`
- `templates/readme-project.md.j2`

### C) Prompt Sync

Prompts must reference current schema and contracts:

- `prompts/system-extractor.md.j2` - Uses ExtractionV1 schema
- `prompts/system-planner.md.j2` - Uses ChangePlan schema + patch primitives

### D) Profile Enforcement

If profile YAML defines a constraint, prompt MUST enforce it:

- `max_tasks` → Prompt says "pick top N by impact"
- `confidence_threshold` → Prompt says "only extract if confidence ≥ X"
- `type_hints` → Code applies, model does not re-classify
