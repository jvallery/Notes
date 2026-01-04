# TODO – Remediation Plan (Sequenced)

This list is ordered by risk and dependency. Each task includes success criteria so a reviewer can verify completion.

---

## 1) Privacy + API Compliance (Blocker)

**Goal:** Align all OpenAI usage with documented privacy requirements and a single API surface.

**Tasks**
- Unify on one API pattern (`responses.parse` preferred) across core pipeline and backfill.
- Ensure `store=False` is passed on all API calls (extract/plan/backfill/audits).
- Fix privacy config source: code should read `models.privacy.store` (or update config to match code).

**Success Criteria**
- All OpenAI calls include `store=False`.
- No direct `chat.completions.create` usage for structured outputs.
- Privacy check reads the correct config field and fails fast if violated.

---

## 2) Fix Backup + Git Staging Safety (Blocker)

**Goal:** Prevent data loss and dirty repos during Apply/Migration/Backfill.

**Tasks**
- Update `backup_file()` to preserve vault-relative structure for all callers.
- Switch staging to `git add -A -- Inbox/ VAST/ Personal/` (or `add_content_dirs_all`).
- Ensure migration/backfill apply flows use same staging strategy.

**Success Criteria**
- Running Apply on multiple README.md files produces distinct backups.
- Git commits capture renames/deletions with a clean working tree.

---

## 3) Standards Consistency (Docs + Templates + Validators)

**Goal:** Resolve conflicts between `STANDARDS.md`, templates, and validators.

**Tasks**
- Choose one README root schema (`person-root` vs `people`) and update:
  - `STANDARDS.md`
  - README templates (`readme-*.md.j2`)
  - Migration checks (`migration/scanner.py` expected types)
- Update tag taxonomy rules if nested tags are ever allowed.

**Success Criteria**
- README templates produce frontmatter that matches `STANDARDS.md`.
- Migration scanner reports no false positives for correct README types.

---

## 4) Schema Alignment (JSON Schema vs Pydantic Models)

**Goal:** Ensure JSON schemas match actual Pydantic models.

**Tasks**
- Update `schemas/changeplan.schema.json` to match `PatchSpec` shape
  - `append_under_heading` should match nested `heading` object.
- Update `schemas/extraction.schema.json` to align with ExtractionV1 (or explicitly document system-set fields).

**Success Criteria**
- `scripts/validate.py` passes on artifacts that Pydantic accepts.
- No “valid by schema / invalid by model” discrepancy.

---

## 5) Backfill Extractor Hardening

**Goal:** Make backfill extraction deterministic, privacy‑safe, and schema‑enforced.

**Tasks**
- Replace backfill chat extraction with Responses API + Pydantic schema.
- Remove brittle JSON code-fence parsing and duplicate `decisions` fallback bug.
- Gate web enrichment behind config flag + caching (if kept).

**Success Criteria**
- Backfill extractor returns valid typed objects without manual JSON parsing.
- Web search enrichment can be disabled centrally; no unbounded API calls.

---

## 6) Classification & Profile Selection Reliability

**Goal:** Ensure correct profile selection for Inbox sources.

**Tasks**
- Decide on heuristic vs LLM classification; update docs to match.
- If LLM classification: add structured classifier schema and integrate into `extract.py`.
- If heuristic-only: document explicitly in README/Design.

**Success Criteria**
- Extract runs select correct profile for transcripts vs customer vs projects in test cases.
- Documentation reflects actual behavior.

---

## 7) Planner Context Quality

**Goal:** Avoid ambiguous entities and improve plan accuracy.

**Tasks**
- Provide full entity folder paths to planner (not just names).
- Include aliases from `entities/aliases.yaml` in planner prompt.
- Disambiguate Personal vs VAST entities in context.

**Success Criteria**
- Planner can generate correct `path` for known entities without guessing.
- Fewer warnings about ambiguous entity names.

---

## 8) Archive Collision & Idempotency

**Goal:** Prevent overwriting archives and duplicate patches.

**Tasks**
- Update archive strategy to preserve relative paths or add unique suffixes.
- Make `append_under_heading` idempotent (dedupe or marker).
- Ensure apply rollback restores archived sources (if moved).

**Success Criteria**
- Two sources with same filename can be archived without overwrite.
- Re-running Apply does not duplicate appended content.

---

## 9) README Coverage in Vault

**Goal:** Bring vault to SOT compliance for entity roots.

**Tasks**
- Run migration to create missing READMEs (People, Projects, Customers).
- Decide on Personal READMEs strategy and either create or explicitly exempt.

**Success Criteria**
- All entity folders have README.md, or exemptions are documented.

---

## 10) Documentation Cleanup

**Goal:** Remove stale/duplicate docs and align all references.

**Tasks**
- Remove or mark archived docs as outdated.
- Update `Workflow/README.md`, `REQUIREMENTS.md`, `DESIGN.md`, `BACKFILL-DESIGN.md` to match code.
- Align config path references (`Inbox/_bins` vs `Workflow/*`).

**Success Criteria**
- All docs agree on API usage, model policy, and paths.
- No contradictory instructions remain.

---

## 11) Test Coverage Gaps

**Goal:** Catch regressions in core pipeline.

**Tasks**
- Add unit test for `apply.py` path validation + rollback.
- Add plan/apply round‑trip test using fixture extraction JSON.
- Add schema vs Pydantic consistency tests.

**Success Criteria**
- Tests fail when paths are unsafe or schema drift exists.
- CI passes with new tests.

---

## 12) Operational Runbooks

**Goal:** Ensure safe execution and recovery steps are documented.

**Tasks**
- Document rollback steps for Apply/Backfill/Migration.
- Add checklist for daily run (pre-flight, post-run review).

**Success Criteria**
- Operator can recover from a failed run without guesswork.

---

# Notes

- This TODO intentionally prioritizes safety/consistency fixes before quality improvements.
- For each task, update `Workflow/codex/FULL-REVIEW.md` when completed.
