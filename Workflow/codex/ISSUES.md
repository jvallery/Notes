# Detailed Issues, Challenges, Gaps

Use these items to guide patching. File references include approximate line anchors.

## Critical

1) Backup collisions on apply rollback
   - File: `Workflow/scripts/utils/fs.py:32`
   - Symptom: `backup_dir / source.name` → overwrites when multiple files share a basename.
   - Fix: `backup_file(source, backup_dir, vault_root)`; use `source.resolve().relative_to(vault_root.resolve())` under backup dir.

2) Staging deletions/renames
   - Files: `Workflow/scripts/apply.py:120-150`, `Workflow/scripts/utils/git_ops.py`
   - Symptom: `add_files(repo, files)` stages existing paths only; deletions/renames remain unstaged.
   - Fix: Add `add_content_dirs_all(repo)` → `git add -A -- Inbox/ VAST/ Personal/`; use it in Apply.

3) Backfill extractor endpoint + parsing
   - File: `Workflow/scripts/backfill/extractor.py:178-216`
   - Issues:
     - Uses `chat.completions.create`; should use `responses.parse` with schema.
     - `store=False` likely ignored by chat endpoint.
     - Fallback dict repeats `decisions` key; JSON fallback bug.
   - Fix: Define `BackfillExtractionLite` Pydantic model and `responses.parse(..., text_format=BackfillExtractionLite, store=False)`.

4) Web enrichment loose parsing
   - File: `Workflow/scripts/backfill/entities.py:600-700`
   - Issue: `responses.create(... tools=[web_search_preview])` and regex JSON scrape.
   - Fix: Schema-parse via Responses API; add config flag and caching.

## High

5) Path safety defense-in-depth in backfill
   - Files: `Workflow/scripts/backfill/*`
   - Action: Apply `safe_relative_path(vault, path)` before writes/moves; reject absolute/backslash/colon.

6) Standards checker mode for README
   - Files: `Workflow/scripts/utils/standards_check.py`, `scripts/apply.py`
   - Action: Add `context="readme"` mode; skip dated-note filename rules when target is `README.md`.

7) Profile selection for Inbox sources
   - Files: `Workflow/scripts/extract.py`, `Workflow/scripts/utils/profiles.py`
   - Action: Add light classifier and pass `note_type` into `select_profile()`; avoid wrong rubric.

## Medium

8) Template env parity in backfill entities
   - File: `Workflow/scripts/backfill/entities.py:520`
   - Issue: Jinja `Environment(...)` without `StrictUndefined` or custom `tojson`/helpers.
   - Fix: Reuse `scripts/utils/templates.get_template_env()`.

9) Config path confusion
   - File: `Workflow/config.yaml`
   - Issue: `paths.resources.*` points to `Inbox/_bins`; live assets are under `Workflow/*`.
   - Fix: Clarify/align; or teach utils to honor `resources` keys if moved later.

10) Test coverage gaps beyond backfill
    - Backfill tests exist; core Extract/Plan/Apply tests appear lighter.
    - Action: Add minimal plan/apply round-trip test with a fixture extraction.

## Low / Docs

11) Small doc inconsistencies (dates, headings)
    - IMPLEMENTATION.md fixed; ensure `_archive/IMPLEMENTATION.md` not used by devs.

12) Logging noise scale
    - Many `.log` files; confirm retention policy and log directory ignores.
