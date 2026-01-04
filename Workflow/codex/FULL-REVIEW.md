# Full Review Summary (End-to-End)

This document consolidates code + docs + vault state into one handoff for the planning LLM. It is intentionally exhaustive and oriented around mismatches, hidden risks, and workflow drift.

## 1) System Overview (What Exists)

### Core Pipeline (Extract -> Plan -> Apply)

- Extract: `Workflow/scripts/extract.py` uses `scripts/classify.py` + `scripts/utils/openai_client.py` to produce `Inbox/_extraction/*.extraction.json`.
- Plan: `Workflow/scripts/plan.py` turns extractions into ChangePlans via prompt `Workflow/prompts/system-planner.md.j2`.
- Apply: `Workflow/scripts/apply.py` executes ChangePlans transactionally with backup + rollback and archives sources.

### Backfill Pipeline (Historical Content -> README enrichment)

- Scanner: `Workflow/scripts/backfill/scanner.py` discovers notes in entity folders.
- Extractor: `Workflow/scripts/backfill/extractor.py` uses OpenAI (chat) to extract summaries/mentions/details from existing notes.
- Aggregator: `Workflow/scripts/backfill/aggregator.py` merges extractions into README update plans.
- Applier: `Workflow/scripts/backfill/applier.py` applies README updates transactionally.

### Migration + Cleanup

- Migration (Phase 8): `Workflow/scripts/migration/*` scans and patches frontmatter/READMEs for compliance.
- Cleanup: `Workflow/scripts/cleanup/*` normalizes readme structure and source filenames.

### Assets

- Prompts: `Workflow/prompts/*.md.j2`
- Templates: `Workflow/templates/*.md.j2`
- Profiles: `Workflow/profiles/*.yaml`
- Schemas: `Workflow/schemas/*.schema.json`

## 2) Critical Inconsistencies (Docs vs Code)

### 2.1 OpenAI API usage

- Docs (DESIGN/REQUIREMENTS/README) specify `client.responses.parse(..., store=False)`.
- Code uses `client.beta.chat.completions.parse(...)` in `scripts/utils/openai_client.py`.
- `store=False` is not passed anywhere in `openai_client.parse_structured()`.
- Privacy enforcement reads `config.get("api")`, but `config.yaml` stores privacy under `models.privacy.store`.
- Backfill uses `client.chat.completions.create` directly (`scripts/backfill/extractor.py`, `cleanup/readme_auditor.py`).

**Risk:** Privacy requirement is not enforced in code paths. Also API method mismatch could break with OpenAI version changes.

### 2.2 Model policy drift

- README/Requirements describe `gpt-4o`/`gpt-4o-mini` usage.
- `config.yaml` uses `gpt-5.2-2025-12-11` for classify/extract/plan/backfill.
- Backfill design doc specifies `gpt-4o-mini` (~500 tokens) but actual extractor defaults to `gpt-5.2`.

### 2.3 Config paths vs actual assets

- `config.yaml` has `paths.resources.prompts/templates` under `Inbox/_bins/_prompts` / `Inbox/_bins/_templates`.
- Actual prompts and templates are under `Workflow/prompts` and `Workflow/templates`.
- `scripts/utils/templates.py` falls back to `Workflow/templates`, effectively ignoring `paths.resources.*`.

**Risk:** Config is misleading; future refactors could break asset loading.

### 2.4 Standards vs templates (README roots)

- `STANDARDS.md` defines README types as `person-root`, `project-root`, `account-root` with `name`/`project`/`account` keys.
- README templates use `type: people/projects/customer` and `title` rather than `name` for people.
- `STANDARDS.md` also lists allowed types as `customer|people|projects|rob|journal|partners|travel|task-dashboard`, which does not include `*-root` types.

**Risk:** Standards doc is internally inconsistent and does not match templates or migration checks.

### 2.5 JSON schema vs Pydantic models

- JSON schema in `Workflow/schemas/changeplan.schema.json` expects patch fields `heading` + `content` at top-level.
- Pydantic model `PatchSpec` expects a nested `heading: {heading, content}`.
- Extraction JSON schema does not include `source_file` or `processed_at`, but `ExtractionV1` requires those fields (though set post-parse).

**Risk:** `scripts/validate.py` may accept files that Pydantic would reject (or vice versa).

## 3) Core Pipeline Logic Issues

### 3.1 Backup collisions

- `scripts/utils/fs.py:backup_file()` uses `backup_dir / source.name`.
- If multiple `README.md` (or any repeated filenames) are modified in a batch, backups overwrite each other.

### 3.2 Git staging misses deletes/renames

- `scripts/apply.py` calls `add_files()` with only existing paths.
- Renames/moves/deletes are not staged, leaving dirty working tree and incomplete commits.

### 3.3 Patch idempotency not implemented

- `scripts/utils/patch_primitives.append_under_heading()` always appends content.
- The design and docs claim primitives are idempotent, but this implementation duplicates content on re-run.

### 3.4 Path safety in archive

- `scripts/utils/paths.get_archive_path()` uses only `original_file.name` (no subdir).
- If two sources share the same filename on the same day, archive collision will overwrite.
- `extract.find_unprocessed()` uses archive by filename only, which can mark unrelated files as processed.

### 3.5 Planner context ambiguity

- `list_all_entity_names()` returns names only, not full paths.
- Planner prompt labels these as `Entity Folders`, implying full paths.
- Aliases are passed as `{}` in `plan.build_planner_prompt()` despite existing `Workflow/entities/aliases.yaml`.
- Personal + VAST names are merged without domain context; LLM can’t disambiguate path base.

## 4) Backfill Pipeline Issues

### 4.1 Extraction endpoint + parsing

- Backfill extractor uses `client.chat.completions.create` and manual JSON parsing.
- Contains a duplicate `decisions` key in fallback dictionary (bug).
- `store=False` may not be enforced.

### 4.2 Web enrichment risks

- `scripts/backfill/entities.py` calls OpenAI `web_search_preview` with no config gate or caching.
- Uses regex to scrape JSON from freeform output.

### 4.3 Template environment inconsistency

- Backfill rendering uses a raw `Environment(...)` without the shared filters (`tojson`, `StrictUndefined`).

## 5) Documentation Gaps and Drift

- README claims extract/plan models use `gpt-4o` and `responses.parse`; code uses other endpoints.
- Backfill design says “no new files” but backfill logic can create new READMEs if missing.
- Standards doc for root README types does not match templates or migration rules.

## 6) Vault Content Observations

- VAST People folders: 133; READMEs present: 132
- VAST Projects folders: 59; READMEs present: 45
- VAST Customers folders: 40; READMEs present: 39
- Personal READMEs: 0
- Inbox extractions present: 54

**Gap:** Many entities lack README.md despite SOT requirement.

## 7) Recommendations (Doc-Only, No Code Changes)

Prioritize:

1) Align docs with current code OR update code to match docs:
   - Decide on Responses API vs Chat API.
   - Enforce `store=False` centrally.
   - Normalize model names in docs vs config.

2) Repair standards inconsistencies:
   - Pick a single README frontmatter schema (either `person-root` or `people`).
   - Update `STANDARDS.md`, README templates, migration expectations accordingly.

3) Harden pipeline safety:
   - Fix backup collisions and git staging strategy.
   - Make patch primitives idempotent.
   - Prevent archive collisions by preserving relative paths or disambiguating names.

4) Backfill reliability:
   - Use Structured Outputs for backfill extractor.
   - Gate web enrichment by config and cache results.

5) Context clarity in planner:
   - Provide actual folder paths and alias mappings to the planner prompt.
   - Distinguish VAST vs Personal entities explicitly.

---

This review complements: `Workflow/codex/REVIEW-BUNDLE.md` and `Workflow/codex/ISSUES.md`.
