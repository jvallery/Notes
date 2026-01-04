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

## 13) Parallel Execution for process_inbox.py

**Goal:** Speed up EXTRACT and PLAN phases with concurrent execution.

**Tasks**

- Port `ThreadPoolExecutor` pattern from `backfill/extractor.py` to `process_inbox.py`.
- Add `--workers N` CLI flag (default 5) for parallel extraction/planning.
- Ensure thread-safe logging and progress reporting.
- Rate-limit API calls to respect OpenAI limits.

**Success Criteria**

- 126 files process in ~20 min instead of ~60 min.
- No race conditions in JSON output or logging.
- Works with `--dry-run` and `--verbose` flags.

---

## 14) Enhanced Verbose Output

**Goal:** Show extraction richness, not just task counts.

**Tasks**

- Update verbose output format to show: `✓ customer, 3 tasks, 5 facts, 2 decisions, 4 topics`.
- Add `--summary` flag to show aggregate stats at end of each phase.
- Include mentions breakdown in verbose mode: `mentions: 5 people, 2 projects, 3 accounts`.

**Success Criteria**

- User can see extraction quality without reading JSON files.
- Summary shows total tasks/facts/decisions/topics extracted.

---

## 15) CONTRACTS.md Alignment Fixes

**Goal:** Resolve specification inconsistencies identified in CONTRACTS review.

**Tasks**

- [ ] Classification policy: Pick heuristics OR LLM reclassification, update docs.
- [ ] Schema scope: ExtractionV1 Pydantic is richer than prompt guidance—align them.
- [ ] Entity creation: Resolve "skip unknown" vs "`_NEW_` prefix" conflict.
- [ ] `meeting_date`: Guarantee injection from filename when present.
- [ ] `task.related_*`: Typed references with confidence (not just strings).
- [ ] Normalize failure handling: Consistent with guarantees.
- [ ] API contract: Use `responses.parse()` everywhere (not mixed with chat.completions).

**Success Criteria**

- Single source of truth: DESIGN.md, schemas, and code all agree.
- No "valid input → surprising output" edge cases.

---

## 16) Multi-Entity Attribution

**Goal:** Support notes that span multiple entities (customer + project + people).

**Tasks**

- Add `related_entities` array to ExtractionV1: `[{type, name, role, confidence}]`.
- Update planner to generate patch ops for ALL related entities, not just primary.
- Display related entities in verbose output.
- Consider cross-linking notes (e.g., customer note links to project note).

**Success Criteria**

- A meeting about Microsoft + Neo project + Kanchan creates/updates 3 entity READMEs.
- `related_entities` captured in extraction JSON with roles (e.g., "discussed", "action owner").

---

# Notes

- This TODO intentionally prioritizes safety/consistency fixes before quality improvements.
- For each task, update `Workflow/codex/FULL-REVIEW.md` when completed.
- Items 13-16 added 2026-01-04 based on pipeline run observations.
- Items 17-22 added 2026-01-04 based on full review of 126-file pipeline run results.

---

# Post-Run Cleanup (2026-01-04 Pipeline)

## 17) Merge _NEW_ Entity Folders into Existing Entities

**Goal:** Consolidate content from incorrectly-created `_NEW_*` folders into existing entity folders.

**Discovered Issues (18 folders):**
```
VAST/Customers and Partners/_NEW_Jai Menon/     → VAST/People/Jai Menon/ (exists!)
VAST/Customers and Partners/_NEW_Jeff Denworth/ → VAST/People/Jeff Denworth/ (exists!)
VAST/Customers and Partners/_NEW_Maneesh Sah/   → VAST/People/Maneesh Sah/ (if exists)
VAST/Customers and Partners/_NEW_Timo Pervane/  → VAST/People/Timo Pervane/ (exists!)
VAST/Customers and Partners/_NEW_Deandre Jackson/ → VAST/People/Deandre Jackson/ (exists!)
VAST/Customers and Partners/_NEW_Yogev Vankin/  → VAST/People/Yogev Vankin/ (if exists)
VAST/Customers and Partners/_NEW_VAST/          → DELETE (invalid - VAST is the company)
VAST/Customers and Partners/_NEW_Pricing/       → VAST/Projects/Pricing/ (if exists)
VAST/Customers and Partners/_NEW_Dhammak/       → NEW ACCOUNT - keep as customer
VAST/Customers and Partners/_NEW_/Asaf Levy/    → VAST/People/Asaf Levy/
VAST/Customers and Partners/_NEW_/Jonsi Stephenson/ → VAST/People/Jonsi Stephenson/
VAST/People/_NEW_Nidhi/                         → VAST/People/Nidhi/ (normalize)
VAST/People/_NEW_JB/                            → VAST/People/JB/ or identify
VAST/People/_NEW_Tomer/                         → VAST/People/Tomer Hagay/ (merge)
VAST/People/_NEW_Roy/                           → Identify or delete
VAST/People/_NEW_John/                          → Identify or delete
VAST/People/_NEW_Cloud Marketplace MVP/         → VAST/Projects/Cloud Marketplace/
VAST/People/_NEW_Longmont Public Media/         → Personal/Projects/ (not VAST)
```

**Tasks**
- [ ] Create script `scripts/cleanup_new_entities.py` to merge content
- [ ] Move notes from `_NEW_*` into correct destination
- [ ] Update wikilinks in moved notes
- [ ] Delete empty `_NEW_*` folders
- [ ] Add `#needs-review` tag to merged READMEs

**Success Criteria**
- Zero `_NEW_*` folders remain
- All notes accessible via correct entity folders
- Wikilinks updated to correct paths

---

## 18) Delete Invalid VAST/Accounts Folder

**Goal:** Remove incorrectly-created `VAST/Accounts/` path (should be `VAST/Customers and Partners/`).

**Discovered Issues (3 stub READMEs):**
```
VAST/Accounts/Google/README.md    → Already exists at VAST/Customers and Partners/Google/
VAST/Accounts/Microsoft/README.md → Already exists at VAST/Customers and Partners/Microsoft/
VAST/Accounts/OpenAI/README.md    → Already exists at VAST/Customers and Partners/OpenAI/
```

**Tasks**
- [ ] Delete `VAST/Accounts/` folder entirely
- [ ] Fix planner prompt to use `Customers and Partners` not `Accounts`

**Success Criteria**
- No `VAST/Accounts/` folder
- Planner generates correct paths

---

## 19) Fix Person Entities Misplaced in Customers Folder

**Goal:** Move person entities incorrectly placed under `Customers and Partners/`.

**Discovered Issues:**
```
VAST/Customers and Partners/Jack Kabat/  → VAST/People/Jack Kabat/
VAST/Customers and Partners/EY/          → Legitimate customer, keep
```

**Tasks**
- [ ] Move `Jack Kabat/` to `VAST/People/`
- [ ] Review planner logic for entity type detection
- [ ] People are never "customers" - add validation

**Success Criteria**
- People always placed in `People/` folder
- Planner correctly distinguishes person vs customer

---

## 20) Fix README Task Format (Missing Dates/Priorities)

**Goal:** Tasks in entity READMEs should have full Obsidian Tasks format.

**Discovered Issues:**
- Meeting notes have proper format: `@Owner 📅 YYYY-MM-DD 🔺 #task`
- Entity READMEs have plain format: `- [ ] Task text` (no dates, no priorities)

**Example (Jeff Denworth README):**
```
- [ ] Define Blob API MVP as AZCopy compatibility...  ← MISSING: @Owner 📅 date 🔺 #task
```

**Tasks**
- [ ] Update entity README patch template to include task metadata
- [ ] Propagate owner, due date, priority from extraction to README patches
- [ ] Add `#task` tag to all task lines

**Success Criteria**
- All tasks in READMEs have: owner, due date (if known), priority, `#task` tag
- Tasks plugin can query READMEs same as notes

---

## 21) Remove Duplicate Context Entries

**Goal:** Prevent duplicate lines in `## Recent Context` section.

**Discovered Issues:**
- Jeff Denworth README has duplicate context entries
- `append_under_heading` is not idempotent

**Example:**
```
- 2025-11-07: [[2025-11-07 - Org map and cloud strategy]]
- 2025-11-07: [[2025-11-07 - Org map and cloud focus]]     ← Similar note, should merge?
- 2025-11-07: [[2025-11-07 - Org landscape and cloud strategy]]  ← Third variant
```

**Tasks**
- [ ] Add deduplication logic to `append_under_heading` primitive
- [ ] Consider using date as key for context entries
- [ ] Review duplicate source transcripts that generated similar notes

**Success Criteria**
- No duplicate context lines for same date/note
- Re-running apply on same sources is idempotent

---

## 22) Review and Clean 24 Auto-Stub READMEs

**Goal:** Replace auto-generated stub READMEs with proper templates.

**Discovered Issues (24 stubs):**
- All marked with `> ⚠️ Auto-created stub - needs review`
- Have minimal frontmatter and empty sections
- Located in: `VAST/Accounts/`, `VAST/Customers and Partners/_NEW_*/`, `VAST/People/_NEW_*/`, etc.

**Tasks**
- [ ] List all stubs: `grep -l "Auto-created stub" VAST/*/*/README.md`
- [ ] For each stub: either populate from template or delete folder
- [ ] Remove stubs for entities that don't exist (e.g., `Lihi Rotchild` typo for existing person)

**Success Criteria**
- Zero "Auto-created stub" READMEs remain
- All entity READMEs use proper templates with real content

---

# Planner Improvements (Prevent Future Issues)

## 23) Improve Entity Matching in Planner

**Goal:** Planner should match existing entities before creating `_NEW_*` folders.

**Root Causes:**
- Planner doesn't have full visibility into existing entity folders
- People classified as "customer" note type go to wrong folder
- Aliases not being used for matching

**Tasks**
- [ ] Pass complete entity folder list to planner context
- [ ] Add fuzzy matching for names (Jai Menon, Jai, etc.)
- [ ] Validate note_type matches destination (people → People/, customer → Customers/)
- [ ] Use `entities/aliases.yaml` for normalization

**Success Criteria**
- Zero `_NEW_*` folders created for known entities
- Entity name variations (Jai vs Jai Menon) resolve correctly

---

## 24) Add Post-Plan Validation for Path Correctness

**Goal:** Catch invalid paths before apply phase.

**Discovered Issues:**
- `VAST/Accounts/` path should never exist
- Person names in `Customers and Partners/` path
- Colons in filenames (fixed, but should prevent at plan time)

**Tasks**
- [ ] Add path pattern validation in `plan.py`
- [ ] Reject plans with `VAST/Accounts/` path
- [ ] Warn if person name appears in customer path
- [ ] Sanitize filenames at plan generation, not apply time

**Success Criteria**
- Invalid paths caught at PLAN phase, not APPLY phase
- Clear warnings in plan output for suspicious paths


