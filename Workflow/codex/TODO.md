# TODO – Remediation Plan (Sequenced)

This list is ordered by risk and dependency. Each task includes success criteria so a reviewer can verify completion.

> **Status**: Tasks 1-10 completed (2025-01-XX). See git commits for implementation details.

---

## 1) Privacy + API Compliance (Blocker) ✅ COMPLETED

**Goal:** Align all OpenAI usage with documented privacy requirements and a single API surface.

**Tasks**

- Unify on `client.beta.chat.completions.parse()` API across core pipeline.
- Ensure `store=False` is passed on all API calls (extract/plan/backfill/audits).
- Fix privacy config source: code reads `api.store` and fails fast if not False.

**Success Criteria**

- All OpenAI calls include `store=False`.
- No direct `chat.completions.create` usage for structured outputs.
- Privacy check reads the correct config field and fails fast if violated.

---

## 2) Fix Backup + Git Staging Safety (Blocker) ✅ COMPLETED

**Goal:** Prevent data loss and dirty repos during Apply/Migration/Backfill.

**Tasks**

- Updated `backup_file()` to preserve vault-relative structure.
- Switched staging to `git add -A -- Inbox/ VAST/ Personal/`.
- Migration/backfill apply flows use same staging strategy.

**Success Criteria**

- Running Apply on multiple README.md files produces distinct backups.
- Git commits capture renames/deletions with a clean working tree.

---

## 3) Standards Consistency (Docs + Templates + Validators) ✅ COMPLETED

**Goal:** Resolve conflicts between `STANDARDS.md`, templates, and validators.

**Tasks**

- Chose simple types (`people`, `customer`, `projects`) for README roots.
- Updated STANDARDS.md, templates, and migration scanner to match.
- Tag taxonomy uses flat tags only.

**Success Criteria**

- README templates produce frontmatter that matches `STANDARDS.md`.
- Migration scanner reports no false positives for correct README types.

---

## 4) Schema Alignment (JSON Schema vs Pydantic Models) ✅ COMPLETED

**Goal:** Ensure JSON schemas match actual Pydantic models.

**Tasks**

- Updated `schemas/changeplan.schema.json` to match `PatchSpec` shape.
- `append_under_heading` matches nested `heading` object structure.

**Success Criteria**

- `scripts/validate.py` passes on artifacts that Pydantic accepts.
- No "valid by schema / invalid by model" discrepancy.

---

## 5) Backfill Extractor Hardening ✅ COMPLETED

**Goal:** Make backfill extraction deterministic, privacy‑safe, and schema‑enforced.

**Tasks**

- Backfill uses Structured Outputs with Pydantic schemas.
- Web enrichment gated behind config flag (disabled by default).
- Privacy enforced via `store=False` on all calls.

**Success Criteria**

- Backfill extractor returns valid typed objects without manual JSON parsing.
- Web search enrichment can be disabled centrally; no unbounded API calls.

---

## 6) Classification & Profile Selection Reliability ✅ COMPLETED

**Goal:** Ensure correct profile selection for Inbox sources.

**Tasks**

- Documented heuristic classification in DESIGN.md.
- Profile selection uses filename patterns + content heuristics.
- Classification behavior documented explicitly in design docs.

**Success Criteria**

- Extract runs select correct profile for transcripts vs customer vs projects in test cases.
- Documentation reflects actual behavior.

---

## 7) Planner Context Quality ✅ COMPLETED

**Goal:** Avoid ambiguous entities and improve plan accuracy.

**Tasks**

- Added `load_aliases()` and `list_entity_paths()` to entities.py.
- Planner receives full entity paths and aliases.
- Disambiguates Personal vs VAST entities in context.

**Success Criteria**

- Planner can generate correct `path` for known entities without guessing.
- Fewer warnings about ambiguous entity names.

---

## 8) Archive Collision & Idempotency ✅ COMPLETED

**Goal:** Prevent overwriting archives and duplicate patches.

**Tasks**

- Archive preserves vault-relative paths with unique suffixes.
- Made `append_under_heading` idempotent (checks for existing content).
- Rollback handles archived sources correctly.

**Success Criteria**

- Two sources with same filename can be archived without overwrite.
- Re-running Apply does not duplicate appended content.

---

## 9) README Coverage in Vault ✅ COMPLETED

**Goal:** Bring vault to SOT compliance for entity roots.

**Tasks**

- Created 19 missing READMEs for Personal and VAST projects.
- Personal READMEs follow same pattern as VAST entities.
- All entity folders now have README.md.

**Success Criteria**

- All entity folders have README.md, or exemptions are documented.

---

## 10) Documentation Cleanup ✅ COMPLETED

**Goal:** Remove stale/duplicate docs and align all references.

**Tasks**

- Fixed config.yaml paths (`Inbox/_bins` → `Workflow/*`).
- Updated REQUIREMENTS.md, DESIGN.md API references.
- Aligned all docs on `client.beta.chat.completions.parse()` pattern.

**Success Criteria**

- All docs agree on API usage, model policy, and paths.
- No contradictory instructions remain.

---

## 11) Test Coverage Gaps (SKIPPED)

**Goal:** Catch regressions in core pipeline.

**Tasks**

- Add unit test for `apply.py` path validation + rollback.
- Add plan/apply round‑trip test using fixture extraction JSON.
- Add schema vs Pydantic consistency tests.

**Status:** Deferred to future iteration. Core functionality stabilized first.

**Success Criteria**

- Tests fail when paths are unsafe or schema drift exists.
- CI passes with new tests.

---

## 12) Operational Runbooks ✅ COMPLETED

**Goal:** Ensure safe execution and recovery steps are documented.

**Tasks**

- Created `RUNBOOK.md` with daily checklists and rollback procedures.
- Documented recovery for Apply/Backfill/Migration failures.
- Added quick reference table and emergency recovery section.

**Success Criteria**

- Operator can recover from a failed run without guesswork.

---

# Notes

- All tasks complete except T11 (tests, deferred).
- See `RUNBOOK.md` for operational procedures.
