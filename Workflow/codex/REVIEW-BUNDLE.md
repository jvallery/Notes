# Code Review Bundle – Notes Vault (2026-01-03)

This bundle summarizes findings across the vault with prioritized issues, concrete fixes, and references. Use alongside the linked artifacts in this `Workflow/codex/` folder.

## Top Risks (Fix First)

- Backup collisions on modify/rollback
  - File: `Workflow/scripts/utils/fs.py:30`
  - Issue: `backup_file()` saves to `backup_dir / source.name` → collisions (e.g., multiple `README.md`).
  - Fix: Preserve vault-relative structure: `backup_dir / source.relative_to(vault_root)`.

- Git staging misses deletions/renames in Apply
  - File: `Workflow/scripts/apply.py:86, 132`
  - Issue: Uses per-file staging via `add_files`, which won’t stage deletions/renames.
  - Fix: Stage content dirs with `git add -A -- Inbox/ VAST/ Personal/` (or helper `add_content_dirs_all`).

- Backfill extractor uses Chat Completions + ad-hoc JSON parse
  - File: `Workflow/scripts/backfill/extractor.py:178-216`
  - Issues:
    - Uses `client.chat.completions.create(...)` instead of Responses API `responses.parse()`.
    - `store=False` likely ignored on chat endpoint.
    - Brittle JSON parsing with code-fence stripping; duplicate key bug (`decisions`) in fallback.
  - Fix: Move to Responses API with Pydantic schema (BackfillExtraction-like), `store=False`, retries.

- Missing defense-in-depth path checks in backfill flows
  - Files: `Workflow/scripts/backfill/*`
  - Issue: Generally safe (scans vault), but enforce `safe_relative_path()` where composing paths from data.
  - Fix: Wrap any join back to vault with `safe_relative_path(vault, path)`.

## High Impact Gaps

- Classification step for profile selection
  - Context: Extract pipeline still path-heuristic driven. Inbox items lack robust profile selection.
  - Fix: Add `scripts/classify.py` returning `{note_type, path_hint}`; integrate before extraction.

- Prompt JSON serialization hygiene
  - Files: `Workflow/prompts/*.j2`, `scripts/utils/templates.py`
  - Status: tojson filter is registered (utils), but ensure all prompt rendering uses that env.

- Standards checker wiring for README vs dated notes
  - File: `scripts/utils/standards_check.py` integration
  - Need separate validation mode for READMEs vs dated content to avoid false rejections.

- Web search enrichment in backfill/entities
  - File: `Workflow/scripts/backfill/entities.py:600+`
  - Issue: Uses `responses.create(..., tools=[web_search_preview])`; network/tooling may be unavailable; parsing ad-hoc JSON from free-form output.
  - Fix: Gate behind config flag; parse via Responses API with a schema; cache/enforce rate limits.

## Architecture Fit – Observations

- Extract → Plan → Apply pipeline adheres to the ChangePlan pattern; Apply is transactional and uses `safe_relative_path()`.
- Template env uses `StrictUndefined` and an `ALLOWED_TEMPLATES` whitelist.
- Validation: A centralized `scripts/utils/validation.py` performs strict plan checks; ensure Apply imports it (it does via utils).

## Backfill Track – Observations

- Models are thorough (`Workflow/scripts/backfill/__init__.py`).
- Scanner and Aggregator are well-factored; Applier backs up with preserved structure.
- Extractor is the main outlier (chat endpoint + freeform JSON).

## Notable Inconsistencies

- Config paths vs actual locations
  - `config.yaml` has `paths.resources.*` pointing to `Inbox/_bins/...`; active templates/prompts live under `Workflow/templates` and `Workflow/prompts`. Utils default correctly, but the config entries are misleading.

- Duplicated Step titles in docs were fixed in IMPLEMENTATION.md, but ensure consistency across archived copies.

## Recommended Next Actions (Sequenced)

1) Safety patches
   - Fix `backup_file()` (utils/fs.py) + adjust Apply to pass `vault_root`.
   - Stage with `add -A` on content dirs (git_ops + apply).

2) Backfill extractor hardening
   - Swap to Responses API + Pydantic; remove code-fence logic; add retries and `store=False`.

3) Classification for profile selection
   - Add `scripts/classify.py`; inject into extract pipeline.

4) Standards checker modes
   - README vs dated note; wire into Apply CREATE path pre-write.

5) Config/doc cleanups
   - Align `config.yaml` path hints with actual template/prompt dirs; clarify `resources` vs `Workflow/*`.

See DETAILS in `ISSUES.md` and patch steps in `DIFF-PLAN.md`.
