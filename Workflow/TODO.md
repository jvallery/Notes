# TODO: Notes Vault Automation Remediation

> **Created**: 2026-01-03  
> **Status**: Active  
> **Source**: Code review from `claude/REVIEW-BUNDLE.md` and `codex/FULL-REVIEW.md`

This document contains the complete task list to address all identified issues, organized by priority and dependency sequence.

---

## Overview

| Priority | Category | Tasks | Est. Effort |
|----------|----------|-------|-------------|
| 🔴 Critical | API & Safety | 6 | 4-6 hours |
| 🟠 High | Config & Standards | 6 | 3-4 hours |
| 🟡 Medium | Content & Features | 6 | 4-6 hours |
| 🟢 Low | Polish & Docs | 4 | 2-3 hours |
| **Total** | | **22 tasks** | **13-19 hours** |

---

## Phase 1: Critical Fixes (Must Do First)

These issues affect data integrity, privacy, or will cause runtime failures.

### T1: Fix OpenAI API Method and Privacy Enforcement

**Problem**: Code uses `client.beta.chat.completions.parse()` but docs specify `client.responses.parse()`. Privacy flag `store=False` is not enforced.

**Files**:
- `Workflow/scripts/utils/openai_client.py`
- `Workflow/config.yaml` (privacy config path)

**Tasks**:
- [ ] T1.1: Update `parse_structured()` to use `client.responses.parse()` 
- [ ] T1.2: Ensure `store=False` is explicitly passed in all API calls
- [ ] T1.3: Fix config path: `models.privacy.store` → `api.store` or standardize lookup

**Success Criteria**:
- All OpenAI calls use Responses API endpoint
- `store=False` verified in API call kwargs
- Privacy test: intercept call and confirm `store` parameter

**Sequence**: Do first — other fixes depend on working API calls

---

### T2: Fix Config Model Names

**Problem**: `config.yaml` references `gpt-5.2-2025-12-11` which doesn't exist.

**Files**:
- `Workflow/config.yaml` (lines 68-110)

**Tasks**:
- [ ] T2.1: Replace all `gpt-5.2-*` with valid model names:
  - `classify`: `gpt-4o-mini`
  - `extract_transcript`: `gpt-4o`
  - `extract_email`: `gpt-4o`
  - `planning`: `gpt-4o`
  - `backfill`: `gpt-4o-mini`
- [ ] T2.2: Add comment noting model selection rationale

**Success Criteria**:
- `python scripts/extract.py --dry-run` completes without API errors
- Config matches docs (README, REQUIREMENTS)

**Sequence**: Do after T1

---

### T3: Fix Backup Collision Bug

**Problem**: `backup_file()` uses only filename, causing overwrites when multiple files share the same name (e.g., multiple `README.md` files).

**Files**:
- `Workflow/scripts/utils/fs.py` (~line 32)
- `Workflow/scripts/apply.py` (backup calls)

**Tasks**:
- [ ] T3.1: Modify `backup_file(source, backup_dir, vault_root)` to preserve relative path:
  ```python
  rel_path = source.resolve().relative_to(vault_root.resolve())
  backup_path = backup_dir / rel_path
  backup_path.parent.mkdir(parents=True, exist_ok=True)
  ```
- [ ] T3.2: Update all callers to pass `vault_root`

**Success Criteria**:
- Backup of `VAST/People/Jeff/README.md` goes to `.workflow_backups/{run}/VAST/People/Jeff/README.md`
- Batch apply with multiple README patches creates distinct backups

**Sequence**: Do before any batch processing

---

### T4: Fix Git Staging for Deletes/Renames

**Problem**: `add_files()` only stages existing paths; moves/deletes/renames remain unstaged.

**Files**:
- `Workflow/scripts/utils/git_ops.py`
- `Workflow/scripts/apply.py` (staging calls)

**Tasks**:
- [ ] T4.1: Add `stage_content_dirs(repo)` function:
  ```python
  def stage_content_dirs(repo: git.Repo):
      """Stage all changes in content directories."""
      repo.git.add("-A", "--", "Inbox/", "VAST/", "Personal/")
  ```
- [ ] T4.2: Replace individual `add_files()` call in Apply with `stage_content_dirs()`
- [ ] T4.3: Verify archives are staged (moved files)

**Success Criteria**:
- After Apply, `git status` shows clean tree
- Archived source files appear in commit diff

**Sequence**: Do after T3

---

### T5: Fix Backfill Extractor to Use Structured Outputs

**Problem**: Backfill uses `chat.completions.create` with manual JSON parsing and duplicate keys.

**Files**:
- `Workflow/scripts/backfill/extractor.py` (~lines 178-216)
- `Workflow/models/` (add new model)

**Tasks**:
- [ ] T5.1: Create `BackfillExtractionLite` Pydantic model:
  ```python
  class BackfillExtractionLite(BaseModel):
      summary: str
      key_topics: list[str]
      people_mentioned: list[str]
      projects_mentioned: list[str]
      accounts_mentioned: list[str]
      date_context: str | None
  ```
- [ ] T5.2: Update extractor to use `parse_structured()` with new model
- [ ] T5.3: Remove manual JSON parsing and fallback dict
- [ ] T5.4: Ensure `store=False` is passed

**Success Criteria**:
- Backfill extraction uses Responses API with Pydantic schema
- No regex JSON parsing in extractor
- `store=False` verified

**Sequence**: Do after T1

---

### T6: Fix Archive Path Collision

**Problem**: `get_archive_path()` uses only filename, causing overwrites for same-named files.

**Files**:
- `Workflow/scripts/utils/paths.py`
- `Workflow/scripts/apply.py`

**Tasks**:
- [ ] T6.1: Update `get_archive_path()` to include source folder context:
  ```python
  def get_archive_path(vault_root: Path, source: Path) -> Path:
      date_str = datetime.now().strftime("%Y-%m-%d")
      # Include parent folder for uniqueness
      parent_name = source.parent.name
      unique_name = f"{parent_name}_{source.name}" if parent_name != source.name else source.name
      return vault_root / "Inbox" / "_archive" / date_str / unique_name
  ```
- [ ] T6.2: Update `find_unprocessed()` to check against new archive pattern

**Success Criteria**:
- Two files with same name from different folders archive without overwrite
- Processing detection works correctly

**Sequence**: Do after T4

---

## Phase 2: High Priority (Do This Week)

### T7: Load Aliases in Planner

**Problem**: TODO in `plan.py` — aliases passed as empty dict `{}`.

**Files**:
- `Workflow/scripts/plan.py` (line 122)
- `Workflow/entities/aliases.yaml`

**Tasks**:
- [ ] T7.1: Load aliases in `build_planner_prompt()`:
  ```python
  from scripts.utils.config import workflow_root
  import yaml
  
  aliases_path = workflow_root() / "entities" / "aliases.yaml"
  aliases = yaml.safe_load(aliases_path.read_text()) if aliases_path.exists() else {}
  ```
- [ ] T7.2: Pass to template context: `aliases=aliases`
- [ ] T7.3: Remove TODO comment

**Success Criteria**:
- Planner prompt includes alias mappings (verify in logs)
- "Jeff" resolves to "Jeff Denworth" in entity matching

**Sequence**: Can do independently

---

### T8: Update Config Resource Paths

**Problem**: `config.yaml` references archived paths `Inbox/_bins/*`.

**Files**:
- `Workflow/config.yaml` (lines 33-36)

**Tasks**:
- [ ] T8.1: Update paths:
  ```yaml
  resources:
    prompts: "Workflow/prompts"
    templates: "Workflow/templates"
    profiles: "Workflow/profiles"
  ```
- [ ] T8.2: Remove `subtemplates` key (no longer used)
- [ ] T8.3: Verify `scripts/utils/templates.py` uses these paths OR remove if unused

**Success Criteria**:
- Config paths match actual file locations
- No references to `Inbox/_bins`

**Sequence**: Can do independently

---

### T9: Make Patch Primitives Idempotent

**Problem**: `append_under_heading()` always appends, causing duplicates on re-run.

**Files**:
- `Workflow/scripts/utils/patch_primitives.py`

**Tasks**:
- [ ] T9.1: Add content deduplication to `append_under_heading()`:
  ```python
  def append_under_heading(content: str, heading: str, text: str) -> str:
      # Check if text already exists under heading
      if text.strip() in content:
          return content  # Already present, skip
      # ... existing append logic
  ```
- [ ] T9.2: Add similar check to `ensure_wikilinks()` (already partially implemented)
- [ ] T9.3: Document idempotency guarantee in docstrings

**Success Criteria**:
- Running same ChangePlan twice produces identical output
- No duplicate entries after re-processing

**Sequence**: Can do independently

---

### T10: Normalize README Frontmatter Types

**Problem**: STANDARDS.md defines `person-root`, `project-root` but templates use `people`, `projects`.

**Files**:
- `Workflow/STANDARDS.md`
- `Workflow/templates/readme-*.md.j2`
- `Workflow/scripts/utils/standards_check.py`

**Tasks**:
- [ ] T10.1: Decide canonical type names (recommend: use `people`, `projects`, `customer` for both notes AND READMEs)
- [ ] T10.2: Update STANDARDS.md Section 3.4 to remove `*-root` types
- [ ] T10.3: Update README templates to use consistent type field
- [ ] T10.4: Update `standards_check.py` to accept README-specific patterns

**Success Criteria**:
- STANDARDS.md, templates, and validation all agree on type names
- Existing READMEs pass validation

**Sequence**: Do after deciding type naming convention

---

### T11: Add Path Safety to Backfill

**Problem**: Backfill modules don't use `safe_relative_path()` before writes.

**Files**:
- `Workflow/scripts/backfill/applier.py`
- `Workflow/scripts/backfill/entities.py`

**Tasks**:
- [ ] T11.1: Import `safe_relative_path` from utils
- [ ] T11.2: Apply to all path construction before file writes
- [ ] T11.3: Reject paths containing `..`, absolute paths, or backslashes

**Success Criteria**:
- Backfill refuses to write outside vault root
- Path traversal attempts raise ValueError

**Sequence**: Can do independently

---

### T12: Add Profile Auto-Selection

**Problem**: Profile selection is folder-based but could use content classification.

**Files**:
- `Workflow/scripts/extract.py`
- `Workflow/scripts/utils/profiles.py`

**Tasks**:
- [ ] T12.1: Use classification result to select profile:
  ```python
  note_type = classify(content)  # Already happening
  profile = select_profile_by_type(note_type)
  ```
- [ ] T12.2: Add `profile_mapping` to config:
  ```yaml
  profile_mapping:
    customer: "work_sales"
    partners: "work_sales"
    people: "work_sales"  # default for 1:1s
    projects: "work_engineering"
    rob: "work_leadership"
  ```
- [ ] T12.3: Update `select_profile()` to use mapping

**Success Criteria**:
- Profile selected based on classified note type, not folder
- Logs show profile selection reasoning

**Sequence**: Can do independently

---

## Phase 3: Medium Priority (This Week/Next)

### T13: Create Missing Project READMEs

**Problem**: 14 project folders lack README.md (VAST/Projects/).

**Folders Missing README**:
- Platform Learning
- VIP
- 5.5 Features
- Alluxio
- Win
- Marketplace L-series Offer Complement (SKUs)
- Microsoft Comparison Slide (LSv4)
- BlockFuse
- Model Builder Turbine
- Cisco POC (DoD)
- AI Talk
- GSI Team
- Pricing
- (verify actual count with updated scan)

**Tasks**:
- [ ] T13.1: Create script or use backfill to generate minimal READMEs
- [ ] T13.2: Run for each missing folder with template `readme-project.md.j2`
- [ ] T13.3: Set `last_updated: unknown` for manual review

**Success Criteria**:
- All project folders have README.md
- `find "VAST/Projects" -name "README.md" | wc -l` equals folder count minus 1

**Sequence**: Can do independently

---

### T14: Create Personal Domain READMEs

**Problem**: Personal domain has no README roots at all.

**Folders to Check**:
- `Personal/People/*`
- `Personal/Projects/*`

**Tasks**:
- [ ] T14.1: Scan Personal/People and Personal/Projects for folders
- [ ] T14.2: Create README.md for each using appropriate template
- [ ] T14.3: Mark as `#needs-review` for human context addition

**Success Criteria**:
- All Personal entity folders have README.md
- READMEs tagged for review

**Sequence**: After T13 (same pattern)

---

### T15: Deduplicate Inbox Emails

**Problem**: Duplicate email captures with different sequence numbers.

**Files**:
- `Inbox/Email/2025-12-14_125503_6117_Your-BetterDisplay-order.md`
- `Inbox/Email/2025-12-14_125503_6741_Your-BetterDisplay-order.md`
- (and others)

**Tasks**:
- [ ] T15.1: Create content hash utility
- [ ] T15.2: Scan inbox for duplicates by content hash
- [ ] T15.3: Archive duplicates with `.duplicate` suffix
- [ ] T15.4: Add dedup check to email capture workflow

**Success Criteria**:
- No duplicate emails in Inbox
- Future captures detect and skip duplicates

**Sequence**: Can do independently

---

### T16: Fix Template Environment in Backfill

**Problem**: Backfill uses raw Jinja2 Environment without shared filters.

**Files**:
- `Workflow/scripts/backfill/entities.py` (~line 520)

**Tasks**:
- [ ] T16.1: Replace local `Environment(...)` with `get_template_env()` from utils
- [ ] T16.2: Ensure `tojson`, `slugify`, `basename` filters available
- [ ] T16.3: Enable `StrictUndefined` to catch missing variables

**Success Criteria**:
- Backfill templates render identically to main pipeline
- Missing variables raise error instead of silent empty

**Sequence**: Can do independently

---

### T17: Regenerate JSON Schemas from Pydantic

**Problem**: JSON schemas may be out of sync with Pydantic models.

**Files**:
- `Workflow/schemas/extraction.schema.json`
- `Workflow/schemas/changeplan.schema.json`
- `Workflow/models/extraction.py`
- `Workflow/models/changeplan.py`

**Tasks**:
- [ ] T17.1: Create `scripts/generate_schemas.py`:
  ```python
  from models.extraction import ExtractionV1
  from models.changeplan import ChangePlan
  import json
  
  schemas_dir.joinpath("extraction.schema.json").write_text(
      json.dumps(ExtractionV1.model_json_schema(), indent=2)
  )
  ```
- [ ] T17.2: Run and commit updated schemas
- [ ] T17.3: Add to CI/pre-commit hook

**Success Criteria**:
- JSON schemas match Pydantic models exactly
- Validation with JSON schema == Pydantic validation

**Sequence**: Can do independently

---

### T18: Gate Web Enrichment in Backfill

**Problem**: Web enrichment calls OpenAI with no config flag or caching.

**Files**:
- `Workflow/scripts/backfill/entities.py` (~lines 600-700)
- `Workflow/config.yaml`

**Tasks**:
- [ ] T18.1: Add config flag:
  ```yaml
  backfill:
    web_enrichment: false  # Enable with caution
    enrichment_cache: "Workflow/entities/.enrichment_cache"
  ```
- [ ] T18.2: Check flag before web search calls
- [ ] T18.3: Implement simple file-based cache for results
- [ ] T18.4: Log when using cached vs fresh results

**Success Criteria**:
- Web enrichment disabled by default
- Cache prevents duplicate API calls for same entity

**Sequence**: Can do independently

---

## Phase 4: Low Priority (Polish)

### T19: Add Core Pipeline Tests

**Problem**: No test coverage for extract/plan/apply.

**Tasks**:
- [ ] T19.1: Create `tests/` directory structure
- [ ] T19.2: Create `tests/fixtures/` with sample transcript, extraction, changeplan
- [ ] T19.3: Write `test_models.py` for Pydantic validation
- [ ] T19.4: Write `test_patch_primitives.py` for idempotency
- [ ] T19.5: Write `test_apply.py` for transactional behavior

**Success Criteria**:
- `pytest tests/` runs and passes
- Coverage for critical path functions

**Sequence**: After Phase 1-2 fixes stabilize code

---

### T20: Clean Up Stale Extraction Files

**Problem**: 54 extraction files in `_extraction/` may be orphaned.

**Tasks**:
- [ ] T20.1: List all `.extraction.json` and `.changeplan.json`
- [ ] T20.2: Check if source files still exist or are archived
- [ ] T20.3: Archive orphaned extractions to `_extraction/_archive/`
- [ ] T20.4: Document retention policy

**Success Criteria**:
- `_extraction/` contains only files for pending sources
- Orphaned files archived with date

**Sequence**: Can do independently

---

### T21: Move Microsoft Contacts.csv

**Problem**: CSV file in `VAST/People/` folder among person folders.

**Files**:
- `VAST/People/Microsoft Contacts.csv`

**Tasks**:
- [ ] T21.1: Move to `Workflow/entities/` or `VAST/_data/`
- [ ] T21.2: Update any scripts that reference it
- [ ] T21.3: Commit with explanation

**Success Criteria**:
- No non-folder items in People directory
- CSV accessible if needed

**Sequence**: Can do independently

---

### T22: Document Logging and Retention

**Problem**: Log files accumulate without documented retention policy.

**Files**:
- `Workflow/logs/`
- `Workflow/.gitignore`

**Tasks**:
- [ ] T22.1: Add retention policy to README:
  ```markdown
  ## Logging
  - Logs: `Workflow/logs/YYYY-MM-DD_HHMMSS.log`
  - Retention: 30 days
  - Cleanup: Manual or scheduled
  ```
- [ ] T22.2: Verify `.gitignore` excludes logs
- [ ] T22.3: Add log rotation/cleanup script (optional)

**Success Criteria**:
- Logging behavior documented
- Logs excluded from git

**Sequence**: Can do independently

---

## Dependency Graph

```
Phase 1 (Critical):
T1 (API Fix) ─────┬──▶ T2 (Config Models)
                  │
                  └──▶ T5 (Backfill Extractor)

T3 (Backup Fix) ──▶ T4 (Git Staging) ──▶ T6 (Archive Fix)

Phase 2 (High):
T7, T8, T9, T10, T11, T12 ─── (Independent, parallel OK)

Phase 3 (Medium):
T13, T14 ─── (Sequential: Projects then Personal)
T15, T16, T17, T18 ─── (Independent)

Phase 4 (Low):
T19 ─── (After Phase 1-2 stabilizes)
T20, T21, T22 ─── (Independent)
```

---

## Quick Reference: Files by Task

| Task | Primary Files |
|------|---------------|
| T1 | `scripts/utils/openai_client.py`, `config.yaml` |
| T2 | `config.yaml` |
| T3 | `scripts/utils/fs.py`, `scripts/apply.py` |
| T4 | `scripts/utils/git_ops.py`, `scripts/apply.py` |
| T5 | `scripts/backfill/extractor.py`, `models/` |
| T6 | `scripts/utils/paths.py` |
| T7 | `scripts/plan.py` |
| T8 | `config.yaml` |
| T9 | `scripts/utils/patch_primitives.py` |
| T10 | `STANDARDS.md`, `templates/readme-*.md.j2` |
| T11 | `scripts/backfill/*.py` |
| T12 | `scripts/extract.py`, `scripts/utils/profiles.py` |
| T13 | Script + `VAST/Projects/*/README.md` |
| T14 | Script + `Personal/*/README.md` |
| T15 | `Inbox/Email/` |
| T16 | `scripts/backfill/entities.py` |
| T17 | `schemas/*.json`, `models/*.py` |
| T18 | `scripts/backfill/entities.py`, `config.yaml` |
| T19 | `tests/` (new) |
| T20 | `Inbox/_extraction/` |
| T21 | `VAST/People/Microsoft Contacts.csv` |
| T22 | `Workflow/logs/`, `README.md` |

---

## Completion Tracking

| Task | Status | Completed | Notes |
|------|--------|-----------|-------|
| T1 | ⬜ | | |
| T2 | ⬜ | | |
| T3 | ⬜ | | |
| T4 | ⬜ | | |
| T5 | ⬜ | | |
| T6 | ⬜ | | |
| T7 | ⬜ | | |
| T8 | ⬜ | | |
| T9 | ⬜ | | |
| T10 | ⬜ | | |
| T11 | ⬜ | | |
| T12 | ⬜ | | |
| T13 | ⬜ | | |
| T14 | ⬜ | | |
| T15 | ⬜ | | |
| T16 | ⬜ | | |
| T17 | ⬜ | | |
| T18 | ⬜ | | |
| T19 | ⬜ | | |
| T20 | ⬜ | | |
| T21 | ⬜ | | |
| T22 | ⬜ | | |
