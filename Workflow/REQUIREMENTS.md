# Requirements: Local-First Obsidian Automation System

> **Version**: 1.0.0 (Final)  
> **Last Updated**: 2026-01-03  
> **Status**: Locked  
> **Related**: [DESIGN.md](DESIGN.md) | [STANDARDS.md](STANDARDS.md)

## 1. Problem Statement

Managing professional and personal knowledge across multiple input channels (meetings, emails, texts, voice notes) requires significant manual effort to organize, cross-reference, and keep current. The goal is to build a **local-first, headless automation pipeline** that:

1. **Captures** raw context from multiple sources into a unified inbox
2. **Extracts** structured information using AI with schema-enforced outputs
3. **Plans** explicit, auditable change operations via Pydantic models
4. **Applies** updates deterministically via Python with transactional rollback
5. **Maintains** cross-links between people, projects, and historical context

### 1.1 Key Architectural Principles

| Principle                   | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **Local-first**             | All processing runs on-device; no cloud storage of raw content        |
| **Headless operation**      | Pipeline runs without Obsidian open; no plugin dependencies           |
| **Separation of concerns**  | Reasoning (AI) is strictly separated from execution (Python)          |
| **Schema-enforced outputs** | Use Pydantic models with `responses.parse()` for guaranteed structure |
| **Transactional apply**     | Batch operations succeed or fail atomically with rollback             |
| **Privacy by default**      | All API calls explicitly disable training (`store=False`)             |

---

## 2. Functional Requirements

### 2.1 Ingestion Layer (Raw Context → Inbox)

| ID     | Requirement                                                                           | Priority | Implementation         |
| ------ | ------------------------------------------------------------------------------------- | -------- | ---------------------- |
| ING-01 | Capture email threads from Apple Mail via global hotkey → `Inbox/Email/`              | P0       | Shortcut + AppleScript |
| ING-02 | **Save raw .eml source** alongside Markdown conversion (HTML fidelity)                | P0       | AppleScript export     |
| ING-03 | Record Zoom/Meet calls via MacWhisper with speaker diarization → `Inbox/Transcripts/` | P0       | MacWhisper             |
| ING-04 | Voice memos/dictation via MacWhisper → `Inbox/Voice/`                                 | P1       | MacWhisper             |
| ING-05 | Manual file drops (screenshots, PDFs, notes) → `Inbox/Attachments/`                   | P2       | Finder                 |
| ING-06 | Preserve original source files in `Inbox/_archive/` after processing                  | P0       | Python script          |

### 2.2 Extraction Layer (Raw Context → Structured JSON)

| ID     | Requirement                                                                          | Priority | Implementation                |
| ------ | ------------------------------------------------------------------------------------ | -------- | ----------------------------- |
| EXT-01 | **Schema-enforced extraction** using `client.responses.parse()` with Pydantic models | P0       | OpenAI Structured Outputs     |
| EXT-02 | Extract tasks, decisions, facts, and participants from transcripts                   | P0       | ExtractionV1 model            |
| EXT-03 | Extract action items and key info from emails                                        | P0       | ExtractionV1 model            |
| EXT-04 | Classify note type using profile-based rubrics (not personas)                        | P0       | Profiles in `profiles/*.yaml` |
| EXT-05 | Identify existing entities (people, projects, accounts) to link against              | P1       | Local fuzzy match + aliases   |
| EXT-06 | **All API calls must use `store=False`**                                             | P0       | Privacy requirement           |
| EXT-07 | Output extraction to `Inbox/_extraction/{source}.extraction.json`                    | P0       | Python script                 |

### 2.3 Planning Layer (Extraction → ChangePlan)

| ID     | Requirement                                                                                                  | Priority | Implementation           |
| ------ | ------------------------------------------------------------------------------------------------------------ | -------- | ------------------------ |
| PLN-01 | **Schema-enforced ChangePlan** using `client.responses.parse()` with Pydantic models                         | P0       | ChangePlan model         |
| PLN-02 | LLM plans only: `create`, `patch`, `link` operations                                                         | P0       | No archive in LLM output |
| PLN-03 | **Structured patch primitives** (no regex): `upsert_frontmatter`, `append_under_heading`, `ensure_wikilinks` | P0       | Safe, deterministic ops  |
| PLN-04 | **No direct file modifications by AI** — planning only                                                       | P0       | Architecture             |
| PLN-05 | Archive operation is deterministic post-step, not LLM-generated                                              | P0       | Apply phase              |
| PLN-06 | Output plan to `Inbox/_extraction/{source}.changeplan.json`                                                  | P0       | Python script            |

### 2.4 Apply Layer (ChangePlan → File Updates)

| ID     | Requirement                                                                   | Priority | Implementation       |
| ------ | ----------------------------------------------------------------------------- | -------- | -------------------- |
| APL-01 | **Require clean git tree** before processing (fail fast if dirty)             | P0       | Git check            |
| APL-02 | **Backup all files to be modified** before applying changes                   | P0       | `.workflow_backups/` |
| APL-03 | **Transactional execution**: on failure, restore backups and delete new files | P0       | Rollback logic       |
| APL-04 | All file operations are atomic (temp file + rename)                           | P0       | Prevent corruption   |
| APL-05 | Create new notes using Jinja2 templates (not Obsidian plugins)                | P0       | Python + Jinja2      |
| APL-06 | Include `source_ref` in created notes pointing to archived source             | P0       | Auditability         |
| APL-07 | Move processed sources to `Inbox/_archive/{date}/` after success              | P0       | Deterministic        |
| APL-08 | Git commit all changes in batch with run summary                              | P1       | Python + git         |

### 2.5 Review Layer (Conflict Resolution)

| ID     | Requirement                                                                | Priority | Implementation  |
| ------ | -------------------------------------------------------------------------- | -------- | --------------- |
| REV-01 | **VS Code Agent** used only for conflict resolution, not primary execution | P0       | Manual trigger  |
| REV-02 | Human review of changes next morning via git diff                          | P0       | Git integration |
| REV-03 | Flag uncertain items with `#needs-review` tag                              | P0       | Automation      |
| REV-04 | Easy rollback via git revert if changes are incorrect                      | P1       | Git workflow    |

### 2.6 Source of Truth Documents

| ID     | Requirement                                                                     | Priority |
| ------ | ------------------------------------------------------------------------------- | -------- |
| SOT-01 | Each **Person** has a root doc: `{People}/{Name}/README.md`                     | P0       |
| SOT-02 | Each **Project** has a root doc: `{Projects}/{Name}/README.md`                  | P0       |
| SOT-03 | Each **Account** has a root doc: `{Customers and Partners}/{Account}/README.md` | P1       |
| SOT-04 | Historical notes stored as dated entries within entity folders                  | P0       |
| SOT-05 | **Tasks live in source notes only** — no duplication to `_Tasks/*.md` files     | P0       |
| SOT-06 | `_Tasks/*.md` files contain **Dataview queries only** (dashboards, not storage) | P0       |

### 2.7 Obsidian Usage (Read-Only for Automation)

| ID     | Requirement                                                    | Notes                      |
| ------ | -------------------------------------------------------------- | -------------------------- |
| OBS-01 | **No plugin dependencies for automation** — headless operation | Critical                   |
| OBS-02 | Templater, Linter, etc. are for human use only                 | Not triggered by pipeline  |
| OBS-03 | All formatting handled by Python + Jinja2 templates            | `Workflow/templates/`      |
| OBS-04 | Dataview queries for dynamic dashboards (read-only)            | Task rollups, recent notes |

---

## 3. Non-Functional Requirements

### 3.1 Performance

- Extraction latency: < 30 seconds per transcript (up to 60 min recording)
- ChangePlan generation: < 10 seconds per extraction
- Apply execution: < 2 seconds per file operation
- Daily batch processing: Complete within 5 minutes for typical day's input

### 3.2 Cost Management

- OpenAI API budget: ~$50/month cap
- Model selection policy-based (see AI Model Policy below)
- Use `gpt-4o-mini` for classification, `gpt-4o` for extraction/planning

### 3.3 Reliability (ETL Best Practices)

| Principle                 | Implementation                                           |
| ------------------------- | -------------------------------------------------------- |
| **Idempotency**           | Re-running on same input produces same result            |
| **Atomic operations**     | No partial writes; temp file + rename pattern            |
| **Schema enforcement**    | Pydantic models guarantee structure at generation time   |
| **Transactional batches** | Entire apply phase succeeds or rolls back                |
| **Dead letter queue**     | Failed files move to `Inbox/_failed/`, don't block queue |
| **Observability**         | Structured logs with metrics and error details           |

### 3.4 Privacy & Security

| Requirement                     | Implementation                                        |
| ------------------------------- | ----------------------------------------------------- |
| All processing runs locally     | No cloud storage of raw content                       |
| **API calls use `store=False`** | Responses API, explicit opt-out of training           |
| Minimal context to APIs         | Profile-guided extraction focuses on relevant content |
| Sensitive content flagged       | `#needs-review` for human review                      |
| API keys in environment         | Never in config files or git                          |

---

## 4. AI Model Policy

### 4.1 Model Selection Strategy

Models are selected **policy-based** rather than hardcoded.

| Task           | Model          | Fallback | Notes                       |
| -------------- | -------------- | -------- | --------------------------- |
| Classification | `gpt-4o-mini`  | `gpt-4o` | Fast, cheap routing         |
| Extraction     | `gpt-4o`       | —        | Structured outputs required |
| Planning       | `gpt-4o`       | —        | Structured outputs required |
| Review         | VS Code `auto` | —        | Human-in-the-loop           |

### 4.2 API Configuration

```python
# All OpenAI API calls MUST use Structured Outputs:
response = client.responses.parse(
    model="gpt-4o",
    input=[...],
    text_format=PydanticModel,  # Schema-enforced
    store=False  # CRITICAL: Disable training
)
```

### 4.3 Configuration Management

| Configuration    | Location                           | Notes                        |
| ---------------- | ---------------------------------- | ---------------------------- |
| Model selection  | `config.yaml` → `models:`          | Policy-based with fallbacks  |
| Profile mapping  | `config.yaml` → `profile_mapping:` | Folder → profile             |
| Path definitions | `config.yaml` → `paths:`           | All folder paths centralized |
| Prompts          | `Workflow/prompts/*.md.j2`         | Jinja2 templates             |
| Entity aliases   | `Workflow/entities/aliases.yaml`   | Name → folder resolution     |

---

## 5. Agent Mode Clarification

### 5.1 Mode A: Local Automation (PRIMARY)

| Component       | Tool                | Purpose                     |
| --------------- | ------------------- | --------------------------- |
| Extraction      | Python + OpenAI API | Pydantic-parsed JSON        |
| Planning        | Python + OpenAI API | Pydantic-parsed ChangePlan  |
| Execution       | Python              | Deterministic with rollback |
| Templating      | Jinja2              | Note formatting             |
| Version control | Git                 | Rollback capability         |

**This is our target architecture.**

### 5.2 Mode B: VS Code Interactive Agent

| Component | Tool                     | Purpose               |
| --------- | ------------------------ | --------------------- |
| Trigger   | Manual in VS Code        | Human initiates       |
| Agent     | Copilot (Claude)         | Local reasoning       |
| Scope     | Conflict resolution only | Not primary execution |

**Used only when:**

- Apply phase encounters conflicts
- Human review flags issues
- Complex multi-file reasoning needed

### 5.3 Mode C: GitHub Copilot Coding Agent (NOT USED)

| Status                  | Reason                                        |
| ----------------------- | --------------------------------------------- |
| ❌ Not for this project | Cloud/PR-based workflow                       |
|                         | Designed for code repos, not knowledge vaults |
|                         | Latency and privacy concerns                  |

---

## 6. Daily Workflow Integration

### 6.1 Daytime Capture (Throughout Day)

```
User → Record meeting (MacWhisper) → Inbox/Transcripts/
User → Hotkey email (⌃⌥⌘M) → Inbox/Email/
User → Drop files → Inbox/Attachments/
```

### 6.2 End-of-Day Processing (Manual Trigger ~6PM)

```bash
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
python scripts/process_inbox.py
```

**What happens**:

1. Verify git is clean (fail if dirty)
2. Extract all pending files → JSON
3. Plan all extractions → ChangePlans
4. Apply all plans (transactional)
5. Archive sources
6. Git commit batch

### 6.3 Morning Review (Next Day)

```
User → git diff HEAD~1 (review changes)
User → Search for #needs-review
User → Resolve any flagged conflicts
User → git push (manual)
```

---

## 7. Constraints

| Constraint             | Rationale                                                         |
| ---------------------- | ----------------------------------------------------------------- |
| macOS only             | Primary workstation; leverages AppleScript, Shortcuts, MacWhisper |
| No Docker              | Self-contained on laptop; avoid server dependencies               |
| Local Python venv      | `/Notes/Workflow/.venv/` for scripts                              |
| **No new software**    | Only Obsidian, MacWhisper, and macOS automations                  |
| **Headless operation** | Cannot require Obsidian to be running                             |
| **No plugin triggers** | Templater/Linter for human use only                               |
| Markdown-first         | All outputs must be valid Obsidian markdown                       |
| Git-tracked vault      | Version control for rollback and history                          |

---

## 8. Success Criteria

1. **Zero-touch meeting processing**: Record with MacWhisper → trigger script → notes appear in correct folders
2. **Auditable changes**: Every update traced through extraction → plan → apply chain
3. **No AI-caused data loss**: Transactional apply with rollback prevents corruption
4. **Tasks in source notes**: Dashboards query tasks, never duplicate them
5. **Privacy preserved**: All API calls have `store=False`
6. **Weekly review time reduced**: From 2+ hours to < 30 minutes

---

## Appendix A: Dependencies

| Category          | Dependencies                                                  |
| ----------------- | ------------------------------------------------------------- |
| External Software | Obsidian, MacWhisper                                          |
| macOS Features    | Shortcuts, Quick Actions, AppleScript                         |
| Python Packages   | openai, pydantic, jinja2, pyyaml, gitpython                   |
| Obsidian Plugins  | Dataview (for dashboards), Tasks (for manual task management) |

---

## Appendix B: Migration from v0.1

| Old Approach                  | New Approach                      |
| ----------------------------- | --------------------------------- |
| Agent updates files directly  | Python applies ChangePlans        |
| JSON mode + post-validation   | Structured Outputs with Pydantic  |
| Regex patching                | Structured patch primitives       |
| Per-file apply                | Transactional batch apply         |
| Persona injection             | Profile-based rubrics             |
| Tasks duplicated to `_Tasks/` | Tasks stay in source notes        |
| Relied on Templater triggers  | Jinja2 templates, headless        |
| No `store: false`             | All API calls opt out of training |
