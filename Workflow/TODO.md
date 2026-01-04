# TODO – Remediation Plan (Sequenced)

This list is ordered by risk and dependency. Each task includes success criteria so a reviewer can verify completion.

---

## 🤖 Agent Instructions

> **Multi-Agent Workflow**: Multiple agents can work on this list simultaneously.
> See `AGENTS.md#todo-workflow` for full protocol.

### Quick Reference

| Status        | Meaning                 | Marker                                                           |
| ------------- | ----------------------- | ---------------------------------------------------------------- |
| `NOT STARTED` | Available for any agent | `**Status: NOT STARTED**`                                        |
| `IN PROGRESS` | Claimed by an agent     | `**Status: IN PROGRESS** (@agent-id, started: YYYY-MM-DD HH:MM)` |
| `COMPLETED`   | Finished and verified   | `**Status: ✅ COMPLETED** (YYYY-MM-DD)`                          |
| `BLOCKED`     | Waiting on dependency   | `**Status: ⏸️ BLOCKED** (reason)`                                |

### Prompts for Agents

<details>
<summary><strong>📥 PROMPT 1: Add New Work Item</strong></summary>

```
Read Workflow/TODO.md and add a new work item following this protocol:

1. Find the highest existing item number: `grep "^## [0-9]*)" Workflow/TODO.md | tail -1`
2. Create new item with next sequential number
3. Use this exact template:

## {N}) {Title}

**Goal:** {One-line goal statement}

**Status: NOT STARTED**

**Discovery:**
{How was this issue found? What evidence?}

**Impact:** {Critical|High|Medium|Low} - {brief reason}

**Effort:** {estimated time}

**Tasks**
- [ ] {specific action 1}
- [ ] {specific action 2}

**Success Criteria**
- {Verifiable outcome 1}
- {Verifiable outcome 2}

4. Commit: `git add Workflow/TODO.md && git commit -m "[todo] Add item {N}: {Title}"`
```

</details>

<details>
<summary><strong>🔍 PROMPT 2: Find and Claim Work</strong></summary>

```
Read Workflow/TODO.md and claim an available work item:

1. Search for available items:
   grep -n "Status: NOT STARTED" Workflow/TODO.md | head -10

2. Pick ONE item matching your capabilities (prefer lower numbers = higher priority)

3. ATOMICALLY claim it by replacing:
   **Status: NOT STARTED**
   with:
   **Status: IN PROGRESS** (@{agent-id}, started: {YYYY-MM-DD HH:MM})

   Where {agent-id} is a unique identifier (e.g., "copilot-1", "claude-a", "agent-xyz")

4. Commit IMMEDIATELY before starting work:
   git add Workflow/TODO.md && git commit -m "[todo] Claim item {N}: {Title}"

5. Now perform the work described in the item's Tasks section

6. After completing work, update status (see PROMPT 3)

CONFLICT PREVENTION:
- Always `git pull --rebase` before claiming
- If commit fails (conflict), abort claim and retry with different item
- Never hold a claim for more than 2 hours without progress commits
- Stale claims (>4 hours) can be reclaimed by other agents
```

</details>

<details>
<summary><strong>✅ PROMPT 3: Complete or Release Work</strong></summary>

```
After finishing work on a TODO item:

COMPLETE (success):
1. Replace status line:
   **Status: IN PROGRESS** (@{agent-id}, started: {timestamp})
   with:
   **Status: ✅ COMPLETED** ({YYYY-MM-DD})

2. Add completion note if needed (what was done, any caveats)

3. Commit:
   git add -A && git commit -m "[fix] {Description of fix} (item {N})"

RELEASE (cannot complete):
1. Replace status line back to:
   **Status: NOT STARTED**

2. Add a note explaining why:
   **Note:** Released by @{agent-id} on {date} - {reason}

3. Commit:
   git add Workflow/TODO.md && git commit -m "[todo] Release item {N}: {reason}"

BLOCKED (waiting on dependency):
1. Replace status line:
   **Status: ⏸️ BLOCKED** (waiting on item {X} / {external dependency})

2. Commit:
   git add Workflow/TODO.md && git commit -m "[todo] Block item {N}: {reason}"
```

</details>

<details>
<summary><strong>🧹 PROMPT 4: Clean Up Completed Items</strong></summary>

```
Remove all completed items from TODO.md and renumber remaining items:

1. Run the cleanup script:
   cd ~/Documents/Notes/Workflow && source .venv/bin/activate
   python scripts/cleanup_todo.py

2. Review what was removed (script prints summary)

3. Commit the cleanup:
   git add Workflow/TODO.md && git commit -m "[todo] Clean up: remove completed items, renumber to {N}"

WHAT THE SCRIPT REMOVES:
- Items with "Status: ✅ COMPLETED" in content
- Items with ✅ in the header (e.g., "## 42) ✅ FIXED: ...")
- Meta sections: Priority Matrix, Summary Statistics, Notes, etc.
- Unnumbered completed sections (Post-Run Cleanup, etc.)

WHAT THE SCRIPT DOES:
- Parses all ## sections
- Filters out completed/meta sections
- Renumbers remaining items sequentially (1, 2, 3...)
- Preserves the header/instructions section
- Cleans up excess blank lines

RUN PERIODICALLY:
- After completing several items
- Before starting a new work session
- When the file becomes cluttered with completed work
```

</details>

---

### How to Use These Prompts

**For Humans**: Copy the prompt text and paste it into a new chat with an AI agent (Copilot, Claude, etc.). The agent will execute the workflow.

**For Agents**: Reference the prompt by number when given a task:

- "Follow PROMPT 1 to add this issue..."
- "Use PROMPT 2 to find work"
- "Complete this item per PROMPT 3"
- "Run PROMPT 4 to clean up the file"

**Quick Commands** (paste into chat):
| Task | Prompt |
|------|--------|
| Add new issue | "Read Workflow/TODO.md and add item: {description}" |
| Find work | "Read Workflow/TODO.md, claim an available item, and complete it" |
| Mark complete | "Mark item {N} as completed in Workflow/TODO.md" |
| Clean up | "Run the cleanup script for Workflow/TODO.md" |

---

## Work Item Index

| Status      | Count                                             | Command to list                                    |
| ----------- | ------------------------------------------------- | -------------------------------------------------- |
| Available   | `grep -c "Status: NOT STARTED" Workflow/TODO.md`  | `grep -B5 "Status: NOT STARTED" Workflow/TODO.md`  |
| In Progress | `grep -c "Status: IN PROGRESS" Workflow/TODO.md`  | `grep -B5 "Status: IN PROGRESS" Workflow/TODO.md`  |
| Completed   | `grep -c "Status: ✅ COMPLETED" Workflow/TODO.md` | `grep -B5 "Status: ✅ COMPLETED" Workflow/TODO.md` |
| Blocked     | `grep -c "Status: ⏸️ BLOCKED" Workflow/TODO.md`   | `grep -B5 "Status: ⏸️ BLOCKED" Workflow/TODO.md`   |

---

---

## 1) Privacy + API Compliance (Blocker)

**Goal:** Align all OpenAI usage with documented privacy requirements and a single API surface.

**Status: ✅ COMPLETED** (2026-01-04)

**Note:** Standardized Structured Outputs on `client.responses.parse(...)` + enforced privacy via `models.privacy.*` config.

**Tasks**

- Unify on one API pattern (`responses.parse` preferred) across core pipeline and backfill.
- Ensure `store=False` is passed on all API calls (extract/plan/backfill/audits).
- Fix privacy config source: code should read `models.privacy.store` (or update config to match code).

**Success Criteria**

- All OpenAI calls include `store=False`.
- No direct `chat.completions.create` usage for structured outputs.
- Privacy check reads the correct config field and fails fast if violated.

---

---

## 2) Fix Backup + Git Staging Safety (Blocker)

**Goal:** Prevent data loss and dirty repos during Apply/Migration/Backfill.

**Status: ✅ COMPLETED** (2026-01-04)

**Tasks**

- [x] Update `backup_file()` to preserve vault-relative structure for all callers.
- [x] Switch staging to `git add -A -- Inbox/ VAST/ Personal/` (or `add_content_dirs_all`).
- [x] Ensure migration/backfill apply flows use same staging strategy.

**Completion Notes:**

- Fixed `migration/executor.py` to pass `vault_root` to `backup_file()` (was missing)
- Replaced `add_files()` with `stage_content_dirs()` in migration executor
- `apply.py` already had correct implementations
- `backfill/applier.py` has its own inline implementation that already preserves structure
- Added test: two README.md files in different folders backup to distinct paths

**Success Criteria**

- ✅ Running Apply on multiple README.md files produces distinct backups.
- ✅ Git commits capture renames/deletions with a clean working tree.

---

---

## 3) Standards Consistency (Docs + Templates + Validators)

**Goal:** Resolve conflicts between `STANDARDS.md`, templates, and validators.

**Status: ✅ COMPLETED** (2026-01-04)

**Completion Notes:**

- Fixed `readme-migration.md.j2`: Changed `type: "readme"` to `type: "{{ entity_type }}"` so it renders correct type per entity
- Standardized all 7 note templates to use unquoted type values (per STANDARDS.md)
- Fixed `VAST/Projects/Cloud Marketplace MVP/README.md`: Changed `type: project` to `type: projects`
- Fixed 2 misclassified notes in `VAST/People/Shachar Feinblit/`: Changed `type: rob` to `type: people`
- Verified scanner EXPECTED_TYPES already matches STANDARDS.md
- Scanner reports 0 wrong_type issues for People scope

**Tasks**

- [x] Choose one README root schema (`person-root` vs `people`) and update:
  - `STANDARDS.md`
  - README templates (`readme-*.md.j2`)
  - Migration checks (`migration/scanner.py` expected types)
- [x] Update tag taxonomy rules if nested tags are ever allowed.

**Success Criteria**

- ✅ README templates produce frontmatter that matches `STANDARDS.md`.
- ✅ Migration scanner reports no false positives for correct README types.

---

---

## 4) Schema Alignment (JSON Schema vs Pydantic Models)

**Goal:** Ensure JSON schemas match actual Pydantic models.

**Status: ✅ COMPLETED** (2026-01-04)

**Tasks**

- Update `schemas/changeplan.schema.json` to match `PatchSpec` shape
  - `append_under_heading` should match nested `heading` object.
- Update `schemas/extraction.schema.json` to align with ExtractionV1 (or explicitly document system-set fields).

**Success Criteria**

- `scripts/validate.py` passes on artifacts that Pydantic accepts.
- No “valid by schema / invalid by model” discrepancy.

---

---

## 5) Backfill Extractor Hardening

**Goal:** Make backfill extraction deterministic, privacy‑safe, and schema‑enforced.

**Status: ✅ COMPLETED** (2026-01-04)

**Completion Notes:**

- Web enrichment uses Responses API + Pydantic schemas (no regex JSON parsing).
- Added config gate `features.backfill_web_enrichment` (default false) and disk cache under `Workflow/_cache/backfill_web_enrichment` (gitignored).
- `backfill.py enrich` fails fast when disabled; added unit tests for caching + gating.

**Tasks**

- Replace backfill chat extraction with Responses API + Pydantic schema.
- Remove brittle JSON code-fence parsing and duplicate `decisions` fallback bug.
- Gate web enrichment behind config flag + caching (if kept).

**Success Criteria**

- Backfill extractor returns valid typed objects without manual JSON parsing.
- Web search enrichment can be disabled centrally; no unbounded API calls.

---

---

## 6) Classification & Profile Selection Reliability

**Goal:** Ensure correct profile selection for Inbox sources.

**Status: ✅ COMPLETED** (2026-01-04)

**Decision:** Heuristic-only classification (no LLM).

**Rationale:**

- Current `scripts/classify.py` uses regex pattern matching, no API calls
- Faster (no latency), cheaper (no tokens), deterministic (same input = same output)
- DESIGN.md already specified "no LLM classification step" - code matches design
- Patterns cover common cases: ROB, customer, people, projects

**Documentation Updated:**

- `README.md`: Changed "Classify (AI)" to "Classify (Heuristics)", added pattern list
- `REQUIREMENTS.md`: Updated model table to show "Heuristics" not "gpt-4o-mini"
- `config.yaml`: Added note that classify config is reserved for future use

**Tasks**

- [x] Decide on heuristic vs LLM classification; update docs to match.
- [x] If heuristic-only: document explicitly in README/Design.

**Success Criteria**

- ✅ Extract runs select correct profile for transcripts vs customer vs projects in test cases.
- ✅ Documentation reflects actual behavior.

---

---

## 7) Planner Context Quality

**Goal:** Avoid ambiguous entities and improve plan accuracy.

**Status: ✅ COMPLETED** (2026-01-04)

**Completion Notes:**

- `entity_paths` now preserves multiple folders per name (VAST + Personal) instead of overwriting.
- Planner prompt includes `mentioned_entities` plus explicit disambiguation guidance.

**Tasks**

- Provide full entity folder paths to planner (not just names).
- Include aliases from `entities/aliases.yaml` in planner prompt.
- Disambiguate Personal vs VAST entities in context.

**Success Criteria**

- Planner can generate correct `path` for known entities without guessing.
- Fewer warnings about ambiguous entity names.

---

---

## 8) Archive Collision & Idempotency

**Goal:** Prevent overwriting archives and duplicate patches.

**Status: ✅ COMPLETED** (2026-01-05)

**Completion Notes:**

- Archive strategy: `get_archive_path()` now preserves source subfolder (Transcripts/, Email/, Voice/) in archive path
- Idempotency: `append_under_heading()` already had dedup logic (checks if text exists in section, checks for duplicate wikilinks)
- Rollback: `apply.py._rollback()` already restores archived sources via `moved_sources` tracking

**Tasks**

- [x] Update archive strategy to preserve relative paths or add unique suffixes.
- [x] Make `append_under_heading` idempotent (dedupe or marker).
- [x] Ensure apply rollback restores archived sources (if moved).

**Success Criteria**

- ✅ Two sources with same filename can be archived without overwrite.
- ✅ Re-running Apply does not duplicate appended content.

---

---

## 9) README Coverage in Vault

**Goal:** Bring vault to SOT compliance for entity roots.

**Status: NOT STARTED**

**Tasks**

- Run migration to create missing READMEs (People, Projects, Customers).
- Decide on Personal READMEs strategy and either create or explicitly exempt.

**Success Criteria**

- All entity folders have README.md, or exemptions are documented.

---

---

## 10) Documentation Cleanup

**Goal:** Remove stale/duplicate docs and align all references.

**Status: NOT STARTED**

**Tasks**

- Remove or mark archived docs as outdated.
- Update `Workflow/README.md`, `REQUIREMENTS.md`, `DESIGN.md`, `BACKFILL-DESIGN.md` to match code.
- Align config path references (`Inbox/_bins` vs `Workflow/*`).

**Success Criteria**

- All docs agree on API usage, model policy, and paths.
- No contradictory instructions remain.

---

---

## 11) Test Coverage Gaps

**Goal:** Catch regressions in core pipeline.

**Status: NOT STARTED**

**Tasks**

- Add unit test for `apply.py` path validation + rollback.
- Add plan/apply round‑trip test using fixture extraction JSON.
- Add schema vs Pydantic consistency tests.

**Success Criteria**

- Tests fail when paths are unsafe or schema drift exists.
- CI passes with new tests.

---

---

## 12) Operational Runbooks

**Goal:** Ensure safe execution and recovery steps are documented.

**Status: NOT STARTED**

**Tasks**

- Document rollback steps for Apply/Backfill/Migration.
- Add checklist for daily run (pre-flight, post-run review).

**Success Criteria**

- Operator can recover from a failed run without guesswork.

---

---

## 13) Parallel Execution for process_inbox.py

**Goal:** Speed up EXTRACT and PLAN phases with concurrent execution.

**Status: NOT STARTED**

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

---

## 14) Enhanced Verbose Output

**Goal:** Show extraction richness, not just task counts.

**Status: NOT STARTED**

**Tasks**

- Update verbose output format to show: `✓ customer, 3 tasks, 5 facts, 2 decisions, 4 topics`.
- Add `--summary` flag to show aggregate stats at end of each phase.
- Include mentions breakdown in verbose mode: `mentions: 5 people, 2 projects, 3 accounts`.

**Success Criteria**

- User can see extraction quality without reading JSON files.
- Summary shows total tasks/facts/decisions/topics extracted.

---

---

## 15) CONTRACTS.md Alignment Fixes

**Goal:** Resolve specification inconsistencies identified in CONTRACTS review.

**Status: NOT STARTED**

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

---

## 16) Multi-Entity Attribution

**Goal:** Support notes that span multiple entities (customer + project + people).

**Status: NOT STARTED**

**Tasks**

- Add `related_entities` array to ExtractionV1: `[{type, name, role, confidence}]`.
- Update planner to generate patch ops for ALL related entities, not just primary.
- Display related entities in verbose output.
- Consider cross-linking notes (e.g., customer note links to project note).

**Success Criteria**

- A meeting about Microsoft + Neo project + Kanchan creates/updates 3 entity READMEs.
- `related_entities` captured in extraction JSON with roles (e.g., "discussed", "action owner").

---

---

## 17) Post‑Import README Template Fixes

**Goal:** Ensure README task queries and timestamps render correctly after import.

**Status: NOT STARTED**

Re-scan results (current vault):

- `rg -l -g 'README.md' 'FROM ""' VAST Personal` → **0** READMEs (good)
- `rg -l -g 'README.md' 'FROM this.file.folder' VAST Personal` → **179** READMEs
- `rg -l -g 'README.md' 'FROM "' VAST Personal` → **36** READMEs (hard-coded scopes)
- `rg -l -g 'README.md' '^last_updated: ""$' VAST Personal` → **15** READMEs
- `rg -l -g 'README.md' "^last_updated: ''$" VAST Personal` → **34** READMEs
- `rg --files-without-match -g 'README.md' '^last_updated:' VAST Personal` → **181** READMEs

This indicates `last_updated` is frequently missing/blank, and `TASK FROM ...` scopes are not standardized.

**Tasks**

- [ ] Standardize README task query scopes:
  - Default: `FROM this.file.folder`
  - Allow explicit multi-folder scopes only when intentional (documented exceptions)
- [ ] Ensure `last_updated` is always set and updated (frontmatter field; no body-level placeholder).
- [ ] Backfill existing READMEs to normalize task scopes + populate `last_updated`.
- [ ] Add an audit gate to fail runs when README queries/timestamps are blank (see item 21).

**Success Criteria**

- `rg -l -g 'README.md' '^last_updated: ""$' VAST Personal` returns 0.
- `rg -l -g 'README.md' "^last_updated: ''$" VAST Personal` returns 0.
- `rg --files-without-match -g 'README.md' '^last_updated:' VAST Personal` returns 0.

---

---

## 18) Title → Path Sanitization (Slashes, Nested Folders)

**Goal:** Prevent title text (e.g., `A/B`) from creating unintended nested directories.

**Status: NOT STARTED**

**Tasks**

- Centralize a path‑safe slug function (replace `/`, `\\`, `:` with `-`, normalize whitespace).
- Use sanitized names for folder/file paths while preserving full `title` in frontmatter.
- Migrate existing nested folders created by `/` in titles and update backlinks.

**Success Criteria**

- New notes with `/` in titles are created in a single folder path.
- No project/people/customer folder names are partial segments of a `title` split by `/`.

---

---

## 19) `_NEW_` Entity Triage + Duplicate Merge

**Goal:** Eliminate `_NEW_*` placeholders and dedupe mis‑typed entities.

**Status: NOT STARTED**

**Tasks**

- Block empty entity names; route unknowns to a triage list instead of `_NEW_`.
- Add alias/fuzzy matching to resolve near‑matches (e.g., Maneesh vs Manish).
- Merge existing `_NEW_*` folders into canonical entities and update links.

**Success Criteria**

- `find VAST -type d -name "_NEW_*"` returns 0.
- Known duplicates are consolidated (e.g., `_NEW_Jeff Denworth`, `_NEW_Jai Menon`).

---

---

## 20) Note Naming + Missing Metadata Cleanup

**Goal:** Avoid `Untitled.md` and missing date/title fields in created notes.

**Status: NOT STARTED**

**Tasks**

- Enforce `title` in extraction (fallback to source filename/ID if missing).
- Guarantee filename format `YYYY-MM-DD - Title.md` (use source date or processed_at).
- Rename existing `Untitled*.md` and any date‑less notes; update backlinks.

**Success Criteria**

- `find VAST Personal -name "Untitled*.md"` returns 0.
- All generated notes include a date in filename and frontmatter.

---

---

## 21) Post‑Import QC Audit Script

**Goal:** Automate validation of import outputs before human review.

**Status: NOT STARTED**

**Tasks**

- Add `Workflow/scripts/audit_import.py` (or similar) to scan for:
  - blank `FROM ""` in README dataview blocks
  - missing `last_updated`
  - missing `README.md` in entity folders
  - `_NEW_*` directories
  - `Untitled*.md` files
  - broken `source_ref` targets (including 0-byte archive files)
  - note type ↔ destination mismatches (e.g., `VAST/People/*` notes with `type: customer`)
  - empty `participants: []` when `source` is a transcript/meeting
  - invalid tags (uppercase, punctuation, deep nesting, etc.)
  - unsafe title→path characters or nested folder splits
- Add a Runbook step to execute audit after each full import.

**Success Criteria**

- Audit produces a concise report and exits non‑zero on violations.
- Post‑import remediation reduces audit report to zero findings.

---

---

## 22) Inconsistent Task Owner Names (Normalization Needed)

**Goal:** Normalize @Owner names during extraction to enable reliable task aggregation.

**Status: NOT STARTED**

**Discovery:**

Owner variants in vault (by frequency):

- `@Myself` (309) ← correct first-person
- `@Jason Vallery` (102) ← should be @Myself?
- `@localhost` (80) ← likely extraction error
- `@Jason` (61) ← ambiguous
- `@TBD` (44) ← valid placeholder
- `@Tomer` (33) vs `@Tomer Hagay` (likely)
- `@Jai` (21) vs `@Jai Menon` (17) ← same person, different formats
- `@Jeff` vs `@Jeff Denworth` ← inconsistent

**Impact:** Medium - task queries by owner are fragmented

**Effort:** 15 minutes

**Tasks**

- [ ] Create owner aliases in `entities/aliases.yaml` for common names
- [ ] Normalize during extraction: `Jai` → `Jai Menon`, `Jeff` → `Jeff Denworth`
- [ ] Handle first-person: convert speaker self-references to `@Myself`
- [ ] Flag `@localhost` as extraction error, investigate root cause

**Success Criteria**

- `@Jai` and `@Jai Menon` map to same canonical owner
- Task queries by owner return complete results

---

---

## 23) Duplicate Notes from Same Meeting (Deduplication)

**Goal:** Detect and prevent processing duplicate transcripts of the same meeting.

**Status: NOT STARTED**

**Discovery:**

Same meeting transcribed multiple times creates multiple notes:

- `VAST/People/Jeff Denworth/2025-11-07 - Org landscape and cloud strategy.md`
- `VAST/People/Jeff Denworth/2025-11-07 - Org map and cloud strategy.md`
- `VAST/People/Jeff Denworth/2025-11-07 - Org map and cloud focus.md`

All three are from the same 1:1 meeting, just different MacWhisper exports.

**Impact:** Medium - wastes API tokens, clutters vault, confuses context

**Effort:** 20 minutes

**Tasks**

- [ ] Add pre-processing dedup check: hash first 500 chars of transcript
- [ ] Compare participant list + date + similar title
- [ ] Skip duplicate sources with warning
- [ ] Consider consolidating existing duplicates

**Success Criteria**

- Same audio processed twice creates only one note
- Existing duplicates flagged for manual review

---

---

## 24) 4 Untitled Files Need Proper Names

**Goal:** Rename all Untitled.md files with appropriate titles.

**Status: NOT STARTED**

**Discovery:**

- `VAST/Customers and Partners/Google/Untitled.md` - Contains Google RFP email (valuable)
- `VAST/Projects/OVA/Proxmox/Untitled.md` - Empty file
- `VAST/Projects/OVA/Proxmox/Untitled 1.md` - Support case documentation
- `Personal/Homelab/VMs/Untitled.md` - Contains encryption key

**Impact:** Low - but creates noise and violates naming standards

**Effort:** 10 minutes

**Tasks**

- [ ] Rename Google Untitled → `2025-XX-XX - GDC RFP Technical Questions.md`
- [ ] Delete empty Proxmox Untitled.md
- [ ] Rename Proxmox Untitled 1 → appropriate title
- [ ] Rename Personal VM Untitled → `VM Encryption Keys.md` or similar

**Success Criteria**

- `find . -name "Untitled*.md"` returns 0

---

---

## 25) 33 Customers with No Meeting Notes

**Goal:** Identify customers with READMEs but no associated notes.

**Status: NOT STARTED**

**Discovery:**

33 customer folders have README.md but no meeting notes:

- CoreWeave (mentioned 53x in other notes, but no own notes)
- IBM, Dell, AWS, Anthropic (likely mentioned in other contexts)
- Many one-off mentions that got auto-created folders

**Impact:** Low-Medium - creates false impression of customer coverage

**Effort:** Analysis only (no immediate fix)

**Tasks**

- [ ] Audit which customers have mentions but no notes
- [ ] For heavily-mentioned customers (CoreWeave), check if notes filed elsewhere
- [ ] Consider cleaning up placeholder folders with no real content
- [ ] Add warning to planner: "Creating new customer folder with no prior notes"

**Success Criteria**

- Report of customers with mentions but no notes
- Decision on whether to keep/remove placeholder folders

---

---

## 26) Company-to-Person Cross-Links Missing

**Goal:** Link People entities to their Company in README and vice versa.

**Status: NOT STARTED**

**Discovery:**

From Role fields, we can map:

- **Microsoft** (21 people): Amy Hood, Jack Kabat, Jai Menon, Kanchan Mehrotra, Kushal Datta, Satya Nadella...
- **Google** (6 people): Billy Kettler, Henry Perez, Jan Niemus, John Downey, Muninder Singh Sambi, Olivia Kim
- **VAST internal**: Jeff Denworth, Jonsi Stephenson, etc.

These relationships exist in frontmatter but aren't cross-linked.

**Impact:** Medium - knowledge graph incomplete

**Effort:** 30 minutes (script)

**Tasks**

- [ ] Extract company from person's Role field
- [ ] Add `company:` field to person README frontmatter
- [ ] Add backlinks to company README: "## Key Contacts\n- [[Person Name]]"
- [ ] Update extraction to capture company affiliation

**Success Criteria**

- `VAST/Customers and Partners/Microsoft/README.md` has Key Contacts section
- Person READMEs have `company: Microsoft` frontmatter

---

---

## 27) Frontmatter Type Inconsistency (Quoted vs Unquoted)

**Goal:** Normalize frontmatter type field format.

**Status: NOT STARTED**

**Discovery:**

Mixed formats in vault:

- `type: people` (unquoted)
- `type: "people"` (quoted)
- Some with invalid types

**Impact:** Low - YAML parses both, but inconsistent

**Effort:** 5 minutes (regex replace)

**Tasks**

- [ ] Standardize on unquoted: `type: people`
- [ ] Run replacement across all files
- [ ] Update templates to use unquoted format

**Success Criteria**

- All frontmatter uses `type: typename` (no quotes)

---

---

## 28) Tasks Without Proper ISO Dates

**Goal:** Ensure all tasks have ISO-8601 due dates where applicable.

**Status: NOT STARTED**

**Discovery:**

Current scan (VAST + Personal) shows **806/1226** tasks have `📅 YYYY-MM-DD`, and **0** tasks use a non-ISO `📅` date format.

The real gap is **missing due dates** (and implied dates like “next week” that could be inferred from the meeting date). See item 65 for the open `#task` subset.

**Impact:** Medium - task scheduling/queries don't work properly

**Effort:** Ongoing (fix during extraction)

**Tasks**

- [ ] Preserve ISO format for all `📅` dates (already compliant).
- [ ] Add inference rules: “next week” / “tomorrow” / “by Friday” + `meeting_date` → computed `📅` date.
- [ ] Leave `📅` off tasks with no clear due date (avoid guessed dates).

**Success Criteria**

- All `📅` due dates use `YYYY-MM-DD`.
- Tasks without clear dates have no `📅` marker.

---

---

## 29) Nested Folder Paths from Title Slashes (Major Issue)

**Goal:** Fix project folders that were incorrectly nested due to `/` in titles.

**Status: NOT STARTED**

**Discovery (found 15+ cases):**

Titles with `/` created unintended nested directories:

- `VAST/Projects/Microsoft Comparison Slide (LSv4/LSv5/OEM-ODM/Azure Storage)` ← 4 levels deep!
- `VAST/Projects/Marketplace L-series Offer Complement (SKUs/OEM path)/`
- `VAST/Projects/Cisco POC (DoD/IC)/`
- `VAST/Projects/Alluxio/DAX evaluation/` (legitimate? or from title)
- `VAST/Projects/BlockFuse/C-Store/`, `BlockFuse/BlobFuse/`

Each nested folder has its own README.md, fragmenting the project.

**Impact:** HIGH - breaks folder navigation, fragments related content

**Effort:** 30 minutes (consolidation + wikilink updates)

**Tasks**

- [ ] Audit all nested project folders
- [ ] Consolidate into single flat folders with sanitized names
- [ ] Update wikilinks to point to new locations
- [ ] Fix path sanitization in plan.py (item 18)

**Success Criteria**

- Projects are max 1 level deep: `VAST/Projects/{ProjectName}/`
- No folders with `/` `)` `(` in names

---

---

## 30) Duplicate Email Imports

**Goal:** Prevent duplicate email imports in Inbox.

**Status: NOT STARTED**

**Discovery:**

Same emails imported multiple times with different random IDs:

- `2025-12-14_125503_6117_Your-BetterDisplay-order.md`
- `2025-12-14_125503_6741_Your-BetterDisplay-order.md`
- `2025-12-15_173836_2490_Dont-miss-conversations...`
- `2025-12-15_173836_7937_Dont-miss-conversations...`

Only difference is export timestamp - content is identical.

**Impact:** Low - wastes processing, creates duplicates

**Effort:** 10 minutes (dedup script)

**Tasks**

- [ ] Hash email content before import
- [ ] Skip if hash matches existing file
- [ ] Clean up existing duplicates

**Success Criteria**

- Same email imported only once
- No duplicate content in Inbox/Email/

---

---

## 31) 103 People + 53 Projects with README Only (No Notes)

**Goal:** Identify and handle entity folders that were auto-created but never populated.

**Status: NOT STARTED**

**Discovery:**

- **103 people** have README.md but zero meeting notes
- **53 projects** have README.md but zero related notes
- Many are mentioned in other notes but never had direct meetings

Examples:

- `VAST/People/Greg Brockman/` (OpenAI CEO - mentioned, no 1:1)
- `VAST/People/Satya Nadella/` (MS CEO - mentioned, no 1:1)
- `VAST/People/Amy Hood/` (MS CFO - mentioned, no 1:1)

**Impact:** Low - creates false impression of relationship depth

**Effort:** Analysis only

**Tasks**

- [ ] Generate report of empty entity folders
- [ ] Distinguish "mentioned only" vs "direct interaction expected"
- [ ] Consider adding `status: mentioned-only` to README frontmatter
- [ ] Optionally consolidate into company-level contact lists

**Success Criteria**

- Clear distinction between active relationships and mention-only
- Decision on folder cleanup policy

---

---

## 32) Orphan Note: Nidhi Missing README

**Goal:** Create README for person folder with notes but no README.

**Status: NOT STARTED**

**Discovery:**

`VAST/People/Nidhi/` has 1 note but no README.md:

- `2025-10-01 - SC25 small-group meeting planning.md`

**Impact:** Low - single case

**Effort:** 2 minutes

**Tasks**

- [ ] Determine full name (Nidhi who?)
- [ ] Create README.md from person template
- [ ] Check for other orphan notes

**Success Criteria**

- All People folders have README.md

---

---

## 33) 14 READMEs with Hardcoded Dataview Paths

**Goal:** Replace hardcoded paths with `this.file.folder` in Dataview queries.

**Status: NOT STARTED**

**Discovery:**

14 READMEs have hardcoded paths like:

```
FROM "VAST/People/Yogev Vankin"
```

Instead of portable:

```
FROM this.file.folder
```

If files are moved, hardcoded queries break.

**Impact:** Low - only breaks if folders renamed

**Effort:** 5 minutes (regex replace)

**Tasks**

- [ ] Find all hardcoded FROM paths
- [ ] Replace with `this.file.folder`
- [ ] Verify Dataview renders correctly

**Success Criteria**

- All READMEs use `FROM this.file.folder`

---

---

## 34) 37 Tasks in People READMEs Missing Format

**Goal:** Update plain tasks in READMEs to have proper Obsidian Tasks format.

**Status: NOT STARTED**

**Discovery:**

37 tasks in People READMEs have format:

```
- [ ] Define Blob API MVP as AZCopy compatibility...
```

Should be:

```
- [ ] Define Blob API MVP @Owner 📅 2025-01-15 🔼 #task
```

Without dates/tags, these won't appear in task queries.

**Impact:** Medium - tasks not aggregated properly

**Effort:** 20 minutes (script to add tags, dates if inferable)

**Tasks**

- [ ] Extract tasks from READMEs
- [ ] Add `#task` tag to all
- [ ] Infer owner from context if possible
- [ ] Flag tasks needing manual date assignment

**Success Criteria**

- All README tasks have minimum: `#task` tag
- Tasks appear in `_Tasks/Work Tasks.md` queries

---

---

## 35) Folder Names with Special Characters

**Goal:** Sanitize folder names with quotes, parentheses, ampersands.

**Status: NOT STARTED**

**Discovery:**

Problematic folder names:

- `Fort Meade "Gemini as a service" on-prem validation/` ← quotes
- `Microsoft BizDev Education & Intros to Ronnie/` ← ampersand
- `Cloud-in-a-box (Tier-2 clouds)/` ← parentheses
- `VIP/Failover Design (GCP RDMA)/` ← nested + parens

Shell commands, some tools, and sync may have issues with these characters.

**Impact:** Medium - breaks automation, shell scripts

**Effort:** 30 minutes (rename + update links)

**Tasks**

- [ ] Replace `"` with empty or hyphen
- [ ] Replace `&` with `and`
- [ ] Replace `(`, `)` with hyphen or remove
- [ ] Update all wikilinks to new names

**Success Criteria**

- `find VAST -name '*"*' -o -name '*&*'` returns 0
- All folder names are shell-safe

---

---

## 36) 68 Files Without Type Field in Frontmatter

**Goal:** Ensure all notes have proper `type:` frontmatter.

**Status: NOT STARTED**

**Discovery:**

68 files missing `type:` field:

- Most are OVA project docs (technical documentation)
- Some are Untitled files
- A few are archive/legacy files

**Impact:** Low - type field mainly for queries/templates

**Effort:** 15 minutes (add type based on location)

**Tasks**

- [ ] List all files without type
- [ ] Add `type: documentation` for OVA/docs/
- [ ] Add `type: archive` for legacy files
- [ ] Add appropriate type for remaining

**Success Criteria**

- All .md files have `type:` in frontmatter

---

---

## 37) 20 Duplicate Meeting Notes (Same Meeting, Multiple Files)

**Goal:** Deduplicate notes from same meeting that were processed multiple times.

**Status: NOT STARTED**

**Discovery:**

Same transcripts in inbox multiple times → multiple notes created:

| Person        | Date       | Duplicate Count           |
| ------------- | ---------- | ------------------------- |
| Jai Menon     | 2025-09-03 | 4 notes from same meeting |
| Jai Menon     | 2025-09-15 | 3 notes                   |
| Jai Menon     | 2025-09-22 | 2 notes                   |
| Jeff Denworth | 2025-11-07 | 3 notes                   |
| Lior Genzel   | 2025-10-28 | 2 notes                   |
| Rick Haselton | 2025-10-28 | 2 notes                   |
| Others        | Various    | 4+ notes                  |

**Impact:** HIGH - duplicate content, confusing README context, wasted tokens

**Effort:** 30 minutes (manual merge + add pre-processing dedup)

**Tasks**

- [ ] Merge duplicates into single canonical note per meeting
- [ ] Update README Recent Context to point to merged note
- [ ] Add pre-processing dedup in extract.py (hash first 500 chars)
- [ ] Add duplicate detection before planning phase

**Success Criteria**

- Max 1 note per person per date (unless multiple meetings)
- Pre-processing prevents future duplicates

---

---

## 38) 92 Empty Related Projects Sections

**Goal:** Populate Related Projects sections in People READMEs.

**Status: NOT STARTED**

**Discovery:**

All 92 People READMEs have empty `## Related Projects` sections:

```markdown
---
## Related Projects
---

## Related
```

The projects are mentioned in notes but not cross-linked to the person.

**Impact:** Medium - knowledge graph incomplete

**Effort:** 20 minutes (update planner to populate)

**Tasks**

- [ ] Update planner to extract project mentions for each person
- [ ] Add PATCH operation to populate Related Projects
- [ ] Backfill existing READMEs with inferred project links

**Success Criteria**

- Related Projects populated from extraction.mentions.projects
- People involved in projects have wikilinks to those projects

---

---

## 39) September 2025 Has Most Duplicate Transcripts

**Goal:** Investigate and prevent duplicate transcripts at source.

**Status: NOT STARTED**

**Discovery:**

Archive analysis shows clustering of duplicates:

- 2025-09-03: 5 duplicate transcripts
- 2025-09-15: 7 duplicate transcripts
- 2025-10-28: 13 duplicate transcripts
- 2025-10-29: 13 duplicate transcripts
- 2025-10-30: 9 duplicate transcripts

Likely cause: MacWhisper auto-export creating multiple files, or manual re-exports.

**Impact:** Medium - wastes processing, creates confusion

**Effort:** Analysis + workflow change

**Tasks**

- [ ] Review MacWhisper export settings for duplicate prevention
- [ ] Add timestamp-based dedup (same time = same meeting)
- [ ] Consider using audio file hash for identity

**Success Criteria**

- Same audio produces only one transcript
- Pre-processing identifies duplicates before API calls

---

---

## 40) Projects Folder Has Deep Nesting (Subprojects)

**Goal:** Clarify whether subfolders in Projects are intentional or accidents.

**Status: NOT STARTED**

**Discovery:**

Several project folders have sub-projects:

- `BlockFuse/` → `BlobFuse/`, `C-Store/`
- `Alluxio/` → `DAX/`, `DAX evaluation/`
- `VIP/` → `Failover Design (GCP RDMA)/`
- `OVA/` → `Proxmox/`, `docs/`

Some are intentional (OVA docs), some may be title-slash errors.

**Impact:** Low - if intentional; Medium if accidental

**Effort:** Analysis

**Tasks**

- [ ] Audit each nested project folder
- [ ] Consolidate accidental nesting
- [ ] Document allowed nesting patterns (e.g., docs/ ok)

**Success Criteria**

- Clear policy on project folder nesting
- Accidental nesting resolved

---

---

## 41) OVA Project Has 68 Undocumented Files

**Goal:** Add frontmatter to OVA technical docs.

**Status: NOT STARTED**

**Discovery:**

68 files in `VAST/Projects/OVA/` lack `type:` frontmatter:

- `docs/*.md` - Technical documentation
- `docs/archive/*.md` - Old docs
- `Proxmox/*.md` - VM-specific notes

These are technical docs, not meeting notes.

**Impact:** Low - docs work fine without type

**Effort:** 10 minutes (add type: documentation)

**Tasks**

- [ ] Add `type: documentation` to OVA docs
- [ ] Optionally add `project: OVA` tag
- [ ] Consider exempting technical docs from type requirement

**Success Criteria**

- OVA docs have consistent frontmatter
- Or: Explicit exemption documented

---

---

## 42) 57+ Broken First-Name-Only Wikilinks

**Goal:** Resolve wikilinks that reference people by first name only.

**Status: NOT STARTED**

**Discovery:**

Many wikilinks use first names without matching folders:

- `[[Renan]]`, `[[Kui]]`, `[[Krishnan]]`, `[[Qi]]`, `[[Andrew]]`
- `[[Suresh]]`, `[[Pradeep]]`, `[[Nidhi]]`, `[[Harish]]`, `[[Aung]]`
- `[[Nagendra]]`, `[[Lukasz]]`, `[[Girish]]`, `[[Long]]`, `[[Juergen]]`

These appear in Key Contacts sections of customer READMEs.
57 unique first-name-only broken links found.

**Impact:** Medium - broken links in knowledge graph

**Effort:** 30 minutes (identify full names, update or create)

**Tasks**

- [ ] Identify full names for each first-name reference
- [ ] Create person folders where appropriate
- [ ] Update wikilinks to use full names
- [ ] Add aliases for first names in aliases.yaml

**Success Criteria**

- All wikilinks resolve to existing folders
- First names aliased to full names

---

---

## 43) 15 Typo/Misspelled Person Names in Wikilinks

**Goal:** Fix typos in person name wikilinks.

**Status: NOT STARTED**

**Discovery:**

Typo variants found (correct → wrong):

- `Jason Vallery` → `Jason Valeri`
- `Jonsi Stephenson` → `Jonsi Stemmelsson`, `Yonsi Stephenson`
- `Maneesh Sah` → `Manish Sah`
- `Michael Myrah` → `Michael Myra`
- `Ronnie Booker` → `Ronnie Borker`

These create broken links and fragment the knowledge graph.

**Impact:** Medium - broken links

**Effort:** 15 minutes (find and replace)

**Tasks**

- [ ] Create typo mapping list
- [ ] Global search/replace in vault
- [ ] Add typos to aliases.yaml for future prevention

**Success Criteria**

- All person names spelled correctly
- Aliases prevent future typos

---

---

## 44) 2 READMEs with `last_contact: unknown`

**Goal:** Populate unknown last_contact dates.

**Status: NOT STARTED**

**Discovery:**

Two READMEs have `last_contact: unknown`:

- `VAST/People/Jack Kabat/README.md`
- `VAST/People/Rory Carmichael/README.md`

**Impact:** Low

**Effort:** 5 minutes

**Tasks**

- [ ] Check if these people have notes
- [ ] Set last_contact from most recent note
- [ ] If no notes, set to created date

**Success Criteria**

- All READMEs have valid last_contact dates

---

---

## 45) Jason Vallery README Has 56 Context Entries

**Goal:** Trim excessive Recent Context entries.

**Status: NOT STARTED**

**Discovery:**

`VAST/People/Jason Vallery/README.md` has 56 entries in Recent Context.
This is because Jason appears in most meetings (it's the user's notes).

Other high-count READMEs:

- Lior Genzel: 28 entries
- Jeff Denworth: 23 entries
- Jai Menon: 14 entries

**Impact:** Low - UI clutter but functional

**Effort:** 10 minutes (trim to last N)

**Tasks**

- [ ] Decide on max Recent Context entries (e.g., 20)
- [ ] Implement trimming in planner/apply
- [ ] Trim existing excessive entries

**Success Criteria**

- Recent Context sections have reasonable length
- Oldest entries archived or removed

---

---

## 46) Email Inbox Has Duplicate Exports

**Goal:** Clean up duplicate email exports.

**Status: NOT STARTED**

**Discovery:**

Same emails exported twice with different random IDs:

- `2025-12-14_125503_6117_Your-BetterDisplay-order.md`
- `2025-12-14_125503_6741_Your-BetterDisplay-order.md` (same content)
- `2025-12-15_173836_2490_Dont-miss-conversations...`
- `2025-12-15_173836_7937_Dont-miss-conversations...` (same content)

4 duplicate pairs in current inbox.

**Impact:** Low - processing will create duplicate notes

**Effort:** 5 minutes (delete duplicates)

**Tasks**

- [ ] Identify and delete duplicate email files
- [ ] Fix email export script to dedupe
- [ ] Consider content hash for email identity

**Success Criteria**

- No duplicate emails in inbox

---

---

## 47) Pending Emails Include Low-Value Spam

**Goal:** Triage pending emails before processing.

**Status: NOT STARTED**

**Discovery:**

7 emails pending processing:

- **High value**: Microsoft Ignite follow-up, OpenAI, Google RFP
- **Low value**: BetterDisplay order (personal purchase), LinkedIn notification

Processing all will waste API tokens on spam/personal.

**Impact:** Low - token waste

**Effort:** 5 minutes (manual triage)

**Tasks**

- [ ] Move personal/spam emails to archive or delete
- [ ] Process only work-relevant emails
- [ ] Consider email classification before processing

**Success Criteria**

- Only work-relevant emails processed

---

---

## 48) 15 Empty Folders in Vault

**Goal:** Clean up or populate empty folders.

**Status: NOT STARTED**

**Discovery:**

15 empty folders found:

- `VAST/Journal/` - Never used
- `VAST/ROB/Phase Gate 1/`, `VAST/ROB/SRE/`, `VAST/ROB/VAST on Cloud Office Hours/` - No meetings yet
- `VAST/Projects/Cloud/Tackle/` - Abandoned project?
- `VAST/Customers and Partners/Microsoft/Azure Managed Lustere/` - TYPO (should be Lustre)
- `VAST/Customers and Partners/Microsoft/UK Met/`, `Apollo/` - Subfolders in wrong location
- `Personal/Journal/`, `Personal/Transcripts/`, `Personal/People/` - Never used
- `Personal/Homelab/Synology/` - Never used
- `VAST/Travel/SC25/`, `Personal/Travel/` - Empty travel folders

**Impact:** Low - clutter

**Effort:** 10 minutes

**Tasks**

- [ ] Delete empty folders with no purpose
- [ ] Add README.md to intentionally-empty folders
- [ ] Fix typo: Lustere → Lustre

**Success Criteria**

- No purposeless empty folders

---

---

## 49) 3 Self-Referential Wikilinks

**Goal:** Remove wikilinks that link to themselves.

**Status: NOT STARTED**

**Discovery:**

3 README files contain wikilinks to the person they describe:

- `VAST/People/Liraz Ben Or/README.md`
- `VAST/People/Muninder Singh Sambi/README.md`
- `VAST/People/Vishnu Charan TJ/README.md`

This is likely from extraction including the entity name in mentions.

**Impact:** Low - unnecessary links

**Effort:** 5 minutes

**Tasks**

- [ ] Remove self-referential wikilinks
- [ ] Update planner to filter out entity_name from mentions

**Success Criteria**

- No README links to itself

---

---

## 50) Tasks with Multiple @Owners

**Goal:** Clarify task ownership conventions for multi-owner tasks.

**Status: NOT STARTED**

**Discovery:**

Some tasks have multiple owners:

```
- [ ] **re:Invent**: confirm plan @Myself @Jonsi @Lior #task
- [ ] **Draft pricing proposal** @Myself @Timo @Jonsi @Tomer @Jeff #task
```

This is valid (shared ownership) but may complicate task queries.

**Impact:** Low - valid pattern but needs documentation

**Effort:** Analysis only

**Tasks**

- [ ] Document multi-owner convention
- [ ] Consider primary owner pattern: `@Primary with @Secondary @Tertiary`

**Success Criteria**

- Multi-owner convention documented

---

---

## 51) Tasks Missing Priority Markers

**Goal:** Add priority markers to tasks that have dates but no priority.

**Status: NOT STARTED**

**Discovery:**

5+ tasks have `📅 date` but no priority marker:

```
- [ ] Develop PAYGO offer @Product 📅 2025-11-08 #task  ← no priority
```

Should be:

```
- [ ] Develop PAYGO offer @Product 📅 2025-11-08 🔼 #task  ← with priority
```

**Impact:** Low - tasks still queryable

**Effort:** 10 minutes

**Tasks**

- [ ] Count tasks missing priority
- [ ] Add default priority (🔼 medium) where missing
- [ ] Update extraction to always include priority

**Success Criteria**

- All tasks with dates have priority markers

---

---

## 52) Microsoft Subfolders in Wrong Location

**Goal:** Move subprojects from customer folder to proper location.

**Status: NOT STARTED**

**Discovery:**

Microsoft customer folder has project subfolders:

- `VAST/Customers and Partners/Microsoft/Apollo/` - Should be project
- `VAST/Customers and Partners/Microsoft/UK Met/` - Should be project
- `VAST/Customers and Partners/Microsoft/Azure Managed Lustere/` - Should be project

These should be in `VAST/Projects/` with cross-links to Microsoft.

**Impact:** Medium - confusing structure

**Effort:** 15 minutes

**Tasks**

- [ ] Move Apollo → `VAST/Projects/Apollo/`
- [ ] Move UK Met → `VAST/Projects/UK Met/`
- [ ] Move Azure Managed Lustre → `VAST/Projects/Azure Managed Lustre/`
- [ ] Add [[Microsoft]] wikilink to each
- [ ] Update backlinks

**Success Criteria**

- Customer folders contain only meeting notes
- Projects in Projects/ folder

---

---

## 53) 4 \_Open Topics Files Need Review

**Goal:** Review and standardize \_Open Topics files.

**Status: NOT STARTED**

**Discovery:**

4 people have `_Open Topics.md` files:

- `VAST/People/Jeff Denworth/_Open Topics.md`
- `VAST/People/Jonsi Stephenson/_Open Topics.md`
- `VAST/People/Shachar Feinblit/_Open Topics.md`
- `VAST/People/Alon Horev/_Open Topics.md`

These contain task queries but no standardized structure.

**Impact:** Low - useful but inconsistent

**Effort:** 10 minutes

**Tasks**

- [ ] Standardize format
- [ ] Consider moving to README or deprecating

**Success Criteria**

- Consistent format or removal

---

---

## 54) Only 32/135 People Have Key Facts Populated

**Goal:** Improve Key Facts extraction or document as optional.

**Status: NOT STARTED**

**Discovery:**

Only 24% of people READMEs have Key Facts populated.
Facts require explicit extraction from conversations.

**Impact:** Low - facts are nice-to-have

**Effort:** Ongoing (improve prompt)

**Tasks**

- [ ] Review extraction prompt for facts
- [ ] Consider making facts section optional
- [ ] Add examples of good facts to prompt

**Success Criteria**

- Higher fact capture rate or documented expectation

---

---

## 55) 7 Uncommitted README Changes

**Goal:** Review and commit or revert uncommitted changes.

**Status: NOT STARTED**

**Discovery:**

7 README files have uncommitted changes:

- `VAST/Customers and Partners/Dhammak/README.md`
- `VAST/Customers and Partners/EY/README.md`
- `VAST/People/Aaron Chaisson/README.md`
- `VAST/People/JB/README.md`
- `VAST/People/Lihi Rotchild/README.md`
- `VAST/People/Maneesh Sah/README.md`
- `VAST/Projects/Cloud Marketplace MVP/README.md`

**Impact:** Low - should commit

**Effort:** 5 minutes

**Tasks**

- [ ] Review changes with `git diff`
- [ ] Commit if appropriate
- [ ] Update apply.py if these are artifacts

**Success Criteria**

- Clean git status

---

---

## 56) 792 Open Tasks Have Overdue Dates (Oct/Nov 2025)

**Goal:** Triage and update overdue tasks or close if stale.

**Status: NOT STARTED**

**Discovery:**

792 tasks have due dates from Oct/Nov 2025 and are still open:

- 172 assigned to "Myself"
- 74 to "Jason Vallery"
- 47 to "Jason" (duplicate of Myself?)
- 38 to "TBD" (unassigned)
- Many others with various owners

**Impact:** HIGH - dashboard noise, stale data

**Effort:** 2+ hours (bulk triage)

**Tasks**

- [ ] Export all overdue tasks to review file
- [ ] Mark completed or update due dates
- [ ] Consider archiving old project task files

**Success Criteria**

- No tasks with due dates > 60 days past

---

---

## 57) 44 Tasks Have @TBD Owner (Unassigned)

**Goal:** Assign owners to unassigned tasks or close.

**Status: NOT STARTED**

**Discovery:**

44 tasks use `@TBD` as owner placeholder:

```
- [ ] Define GA acceptance criteria... @TBD 📅 2025-11-08
- [ ] Assemble pricing and go-to-market package... @TBD 📅 2025-11-08
```

**Impact:** Medium - tasks won't appear in owner-filtered views

**Effort:** 30 minutes

**Tasks**

- [ ] Review each @TBD task and assign real owner
- [ ] Add validation to extraction to require owner

**Success Criteria**

- No @TBD tasks remain

---

---

## 58) 207 Open Tasks Missing Due Dates

**Goal:** Add due dates or mark as backlog.

**Status: NOT STARTED**

**Discovery:**

207 open tasks have `#task` tag but no `📅` due date.

**Impact:** Medium - tasks not appearing in date-filtered views

**Effort:** 1 hour (review + update)

**Tasks**

- [ ] Review tasks and add reasonable due dates
- [ ] Or create #backlog tag for undated items

**Success Criteria**

- All active tasks have due dates

---

---

## 59) Malformed Task Owner Syntax

**Goal:** Fix tasks where extra content follows @Owner.

**Status: NOT STARTED**

**Discovery:**

Many tasks have malformed syntax where additional content follows @Owner:

```
@Aaron ⏫ #task #PMM #enablement
@Adar #task #Uplink #Salesforce 🔼 ✅ 2025-11-08
@Architecture team #task #AI #performance 🔽 ✅ 2025-11-08
```

Correct format: `@Owner` should be followed by priority emoji then `📅` date then `#task` then other tags.

**Impact:** Medium - tasks may not parse correctly

**Effort:** 1 hour

**Tasks**

- [ ] Create regex to find malformed tasks
- [ ] Fix syntax in affected notes

**Success Criteria**

- All tasks follow canonical format

---

---

## 60) 25 Batch Backfill Notes Dated 2025-10-01

**Goal:** Review batch-created notes for accuracy.

**Status: NOT STARTED**

**Discovery:**

25 notes were created on 2025-10-01, suggesting batch backfill:

- Cloud Marketplace MVP checklist
- Pricing vTeam action list
- Multiple 1-1 notes (Andy, Jeff, Jonsi, etc.)
- Customer engagement tasks

These may have placeholder content or inaccurate dates.

**Impact:** Low - historical notes, not ongoing issue

**Effort:** 1 hour (review)

**Tasks**

- [ ] Review notes for accuracy
- [ ] Correct dates if actual meeting date known
- [ ] Add "backfill" tag if keeping synthetic date

**Success Criteria**

- All notes have accurate dates or backfill marker

---

---

## 61) 7 Wikilinks Use 1:1 Instead of 1-1

**Goal:** Fix wikilinks that use colons instead of dashes.

**Status: NOT STARTED**

**Discovery:**

7 unique wikilinks use `1:1` but files are named with `1-1`:

```
2025-10-27 - Jeff 1:1 cloud priorities → file is "Jeff 1-1 cloud priorities.md"
2025-10-28 - Intro 1:1 on pricing
2025-10-28 - Weekly 1:1 and Tel Aviv plan
2025-10-29 - Intro 1:1 on CS ops
2025-10-29 - Intro 1:1 on release process
2025-10-30 - Intro 1:1 on cloud enablement
2025-10-31 - Intro 1:1 on VAST on Cloud
```

**Root Cause:** LLM generated links with colons, but file sanitization converts `:` to `-`

**Impact:** Medium - broken links in READMEs

**Effort:** 10 minutes

**Tasks**

- [ ] Find-replace `1:1` with `1-1` in all READMEs
- [ ] Add colon sanitization rule to LLM prompt or post-processing

**Success Criteria**

- All wikilinks resolve to actual files

---

---

## 62) 10 READMEs Use Old Template (Contact Information)

**Goal:** Migrate old template format to current standard.

**Status: NOT STARTED**

**Discovery:**

10 People READMEs use old template with `## Contact Information` instead of `## Profile`:

- Jack Kabat
- Kanchan Mehrotra
- Kishore Inampudi
- Kurt Niebuhr
- Rick Haselton
- Rob Banga
- Rob Benoit
- Rosanne Kincaid–Smith
- Vishnu Charan TJ
- Yogev Vankin

**Root Cause:** Template changed but existing files not migrated.

**Impact:** Medium - inconsistent structure

**Effort:** 30 minutes

**Tasks**

- [ ] Update readme-person.md.j2 to match current READMEs (Profile format)
- [ ] Create migration script for old-format READMEs
- [ ] Run migration on 10 affected files

**Success Criteria**

- All People READMEs use same template structure

---

---

## 63) ROB Note Filed at Root Instead of Subfolder

**Goal:** Move misplaced ROB note to proper subfolder.

**Status: NOT STARTED**

**Discovery:**

`VAST/ROB/2025-12-16 - VAST and Microsoft Strategic Discussion.md` has:

- `rob_forum: "VAST"`

But there's no `VAST/ROB/VAST/` folder. The note was filed at ROB root instead of in a forum subfolder.

**Root Cause:** Pipeline created note without matching forum folder.

**Impact:** Medium - breaks ROB organization

**Effort:** 10 minutes

**Tasks**

- [ ] Create `VAST/ROB/VAST/` folder
- [ ] Move note to proper location
- [ ] Check pipeline for ROB folder creation logic

**Success Criteria**

- All ROB notes in forum subfolders

---

---

## 64) 112/135 People Need Review (83%)

**Goal:** Triage #needs-review tagged READMEs.

**Status: NOT STARTED**

**Discovery:**

112 out of 135 People READMEs have `#needs-review` tag:

- All were auto-created
- Many have incomplete role/company info
- Many have generic "Microsoft" or "_Unknown_" for Role

Only 23 have been manually reviewed.

**Impact:** Medium - data quality issue

**Effort:** 3+ hours (manual review)

**Tasks**

- [ ] Prioritize high-contact people for review
- [ ] Create review checklist
- [ ] Remove tag after verification

**Success Criteria**

- <50% of People have #needs-review

---

---

## 65) Inconsistent Role Extraction (13 Unknown, 11 Company-Only)

**Goal:** Improve role extraction quality.

**Status: NOT STARTED**

**Discovery:**

Role field quality issues:

- 13 have `_Unknown_` for Role
- 11 have just company name (e.g., "Microsoft") instead of role

Examples:

- `**Role**: Microsoft` (should be "EVP at Microsoft")
- `**Role**: _Unknown_` (should infer from context)

**Root Cause:** LLM not consistently extracting role vs company.

**Impact:** Medium - CRM data quality

**Effort:** 30 minutes (update prompt)

**Tasks**

- [ ] Update extraction prompt to explicitly separate role and company
- [ ] Add examples to prompt
- [ ] Re-run on affected READMEs

**Success Criteria**

- All Role fields have actual job titles

---

---

## 66) Checkbox Semantics: Tasks vs Checklists (OVA Docs Skew Task Audits)

**Goal:** Decide whether checkbox items in documentation (e.g., OVA docs) are “tasks” and how they should appear in dashboards/audits.

**Status: NOT STARTED**

**Discovery:**

Scan results (VAST + Personal):

- `rg -P -g'*.md' -l '^- \\[ \\](?!.*#task\\b)' VAST Personal` → **22** files
- `rg -P -g'*.md' -n '^- \\[ \\](?!.*#task\\b)' VAST Personal | wc -l` → **116** open checkbox items missing `#task`

Most are checklist-style docs under `VAST/Projects/OVA/docs/**`, but a few are in entity READMEs (e.g., `VAST/People/Jeff Denworth/README.md`).

If we treat all `- [ ]` items as tasks, these docs will dominate “missing format” reports; if we don’t, audits must explicitly exclude them.

**Impact:** Medium - either dashboard noise or inconsistent conventions.

**Effort:** 30–60 minutes (policy + audit rules), plus optional backfill

**Tasks**

- [ ] Decide policy:
  - All checkboxes are tasks → enforce `#task` + format everywhere (including docs), OR
  - Checklists are allowed → whitelist paths (e.g., `VAST/Projects/OVA/docs/**`) and exclude them from task-format audits.
- [ ] Update `Workflow/STANDARDS.md` to codify the policy.
- [ ] Update `Workflow/scripts/audit_import.py` to implement the chosen rule.
- [ ] Optional: backfill affected files to conform (add/remove `#task`, add due dates only where appropriate).

**Success Criteria**

- Audit report clearly distinguishes task violations from checklist docs.
- “Tasks missing format” metric is stable and explainable.

---

---

## 67) Deterministic Extraction for Structured `Sources/Transcripts/*` Notes

**Goal:** Avoid expensive LLM extraction when sources are already structured.

**Status: NOT STARTED**

**Discovery:**

- `Sources/Transcripts/**/*.md`: **124** files, all with an `entities:` frontmatter block and structured sections (`## Summary`, `## Key facts learned`, `## Outcomes`, `## Decisions`).
- These sources are not raw “speaker transcript” text; they are already a high-signal intermediate artifact.
- Current pipeline re-extracts them with an LLM, which can degrade fidelity (e.g., completed `[x]` tasks become open `[ ]` tasks).

**Impact:** HIGH - reduces cost and improves accuracy; enables fast iteration without reprocessing raw transcripts.

**Effort:** 1–2 hours (parser + integration + a few tests)

**Tasks**

- [ ] Implement a parser that converts structured transcript-notes → `ExtractionV1` (summary, facts, decisions, tasks, mentions/entities).
- [ ] Add a content-type detector: if a source matches the structured format, bypass LLM and use parser output.
- [ ] Add fixtures/tests for at least: a People 1:1, a Customer meeting, and a Project note.

**Success Criteria**

- Structured sources ingest with **0** OpenAI calls while producing valid `ExtractionV1`.
- Task completion state in sources (`[x]`) is preserved in extracted tasks.

---

---

## 68) Persist Extraction/Plan Artifacts for Re-Planning Without Re-Extracting

**Goal:** Make iteration cheap: rerun PLAN/APPLY using existing artifacts instead of reprocessing transcripts.

**Status: NOT STARTED**

**Discovery:**

`Inbox/_extraction/` is empty after the import run, so extraction outputs/plans are not available for replay/debugging.

**Impact:** HIGH - forces expensive re-runs and makes debugging difficult.

**Effort:** 30–60 minutes

**Tasks**

- [ ] Persist `extraction.json`, `plan.json`, and an apply log per source under `Workflow/runs/YYYY-MM-DD/<source_id>/`.
- [ ] Generate a stable `source_id` (hash of source content + original path) and store it in meeting note frontmatter.
- [ ] Add CLI modes: `--replan-only` (use existing extraction), `--apply-only` (use existing plan).

**Success Criteria**

- Planner can rerun against a prior run’s extraction artifacts with no LLM calls.
- A failed apply has enough artifacts to reproduce/debug without touching sources.

---

---

## 69) Source Kind Classification (Transcript vs Checklist vs Article) + Template Branching

**Goal:** Handle different inbound context types correctly and avoid forcing everything into a “meeting transcript” shape.

**Status: NOT STARTED**

**Discovery:**

Some imported notes are “tasks/checklists” or “announcements/articles” (participants often empty), but are labeled `source: transcript`.

**Impact:** MED - wrong schemas create missing participants, incorrect note types, and weak planner context.

**Effort:** 30–60 minutes

**Tasks**

- [ ] Add `source_kind` enum to extraction + plan models (`transcript|email|note|checklist|article`).
- [ ] Add classifier (heuristic-first) to route to the right extractor/prompt and meeting-note template.
- [ ] Make `participants` optional for non-transcript kinds; require `source_url` for `article`.

**Success Criteria**

- No “article/checklist” notes are labeled as transcript.
- Meeting notes have non-empty participants unless explicitly exempted by `source_kind`.

---

---

## 70) URL Hygiene: Remove `utm_source=chatgpt.com` and Prevent New Tracking Params

**Goal:** Keep links clean and avoid leaking tool provenance into saved notes.

**Status: NOT STARTED**

**Discovery:**

Some notes include URLs with `utm_source=chatgpt.com`.

**Impact:** Low - cosmetic, but confusing and avoidable.

**Effort:** 10–15 minutes

**Tasks**

- [ ] Add a sanitizer to strip common tracking params (`utm_*`, `gclid`, etc.) during any web enrichment step.
- [ ] Run a one-time cleanup pass over existing notes.

**Success Criteria**

- `rg -n \"utm_source=chatgpt\\.com\" VAST Personal` returns 0.

---

---

## 71) Unprocessed Personal Transcript in Projects Folder

**Goal:** Process or archive raw transcript in wrong location.

**Status: NOT STARTED**

**Discovery:**

`Personal/Projects/NextWave/2025-12-15 1240 - AI Discussion at Longmont Museum.md`:

- 810 lines of raw MacWhisper transcript
- No frontmatter
- Sitting in Projects folder instead of Inbox/Transcripts

**Impact:** Low - personal content, but shows gap in capture workflow

**Effort:** 15 minutes

**Tasks**

- [ ] Decide: process or archive as-is
- [ ] If processing: move to Inbox/Transcripts, run extraction
- [ ] Consider: should Personal transcripts go through pipeline?

**Success Criteria**

- No raw transcripts outside Inbox folder

---

---

## 72) 45 Files Without Frontmatter

**Goal:** Audit and standardize markdown files without frontmatter.

**Status: NOT STARTED**

**Discovery:**

45 markdown files lack frontmatter (excluding OVA docs):

- 3 `_MANIFEST.md` files (auto-generated)
- 4 `_Open Topics.md` files
- 2 `_Tasks/*.md` files (Dataview queries)
- Various homelab/config docs
- 1 unprocessed transcript

Most are intentionally unstructured, but should be documented.

**Impact:** Low - most are utility files

**Effort:** 30 minutes (document or add minimal frontmatter)

**Tasks**

- [ ] Categorize files without frontmatter
- [ ] Add minimal frontmatter to utility files
- [ ] Document exceptions in STANDARDS.md

**Success Criteria**

- All files have frontmatter or documented exemption

---

---

## 73) Nidhi Folder Missing README

**Found**: 2026-01-04

**Status: NOT STARTED**

Only person folder without a README:

- `VAST/People/Nidhi/` - has 1 note but no README.md

**Fix**: Create README from template or determine if folder should be merged elsewhere.

---

---

## 74) Wikilink Name Misspellings (65+ broken links)

**Found**: 2026-01-04

**Status: NOT STARTED**

Misspelled wikilinks pointing to non-existent paths:

| Wrong                   | Correct                | Count |
| ----------------------- | ---------------------- | ----- |
| `[[Tomer Hagey]]`       | `[[Tomer Hagay]]`      | 65    |
| `[[Manish Sah]]`        | `[[Maneesh Sah]]`      | ?     |
| `[[Jonsi Stemmelsson]]` | `[[Jonsi Stephenson]]` | ?     |
| `[[Yonsi Stephenson]]`  | `[[Jonsi Stephenson]]` | ?     |
| `[[Jason Valeri]]`      | `[[Jason Vallery]]`    | ?     |

**Fix**:

1. Add misspellings to `aliases.yaml`
2. Find-replace in source files

---

---

## 75) Short Name Wikilinks (Alias Resolution Needed)

**Found**: 2026-01-04

**Status: NOT STARTED**

Short names used instead of full names:

- `[[Vishnu]]` - 70 times (should be `[[Vishnu Charan TJ]]`)
- `[[Rosanne]]` - 23 times (should be `[[Rosanne Kincaid–Smith]]`)
- `[[Jason]]` - 24 times (ambiguous - me or someone else?)

**Fix**: Add to aliases.yaml and consider find-replace for clarity.

---

---

## 76) Orphan Wikilinks - Notable People Without Folders

**Found**: 2026-01-04

**Status: NOT STARTED**

Real people referenced but no folder exists:

- `[[Scott Guthrie]]` - Microsoft EVP
- `[[Mustafa Suleyman]]` - Microsoft AI CEO
- `[[Brendan Burns]]` - 16 references
- `[[Allison Boerum]]`, `[[Dotan Arnin]]`, `[[Helen Protopapas]]`
- `[[Maxim Dunaivicher]]`, `[[Michael Myra]]`, `[[Pete Eming]]`
- `[[Qiu Ke]]`, `[[Ronnie Borker]]`, `[[Yaniv Sharon]]`

**Decision needed**: Create folders for external notable people, or add to aliases pointing to their org?

---

---

## 77) Template Artifact in Wikilinks

**Found**: 2026-01-04

**Status: NOT STARTED**

- `[[Note Title]]` appears in content - template placeholder not replaced

**Fix**: Search and remove/replace these placeholder artifacts.

---

---

## 78) Project Wikilinks Without Folders

**Found**: 2026-01-04

**Status: NOT STARTED**

Project references without corresponding folders:

- `[[Project Apollo]]`
- `[[Project Stargate]]`
- `[[Platform Learning]]`
- `[[Cloud control plane]]` - 28 references

**Fix**: Create project folders or clarify naming.

---

---

## 79) 33 Customer Folders with Only README (No Notes)

**Found**: 2026-01-04

**Status: NOT STARTED**

Out of 41 customer/partner folders, 33 have only README.md - no meeting notes filed:

- Amazon, Anthropic, Avanade, Cisco, CoreWeave, Crusoe, Databricks, Dell...
- Goldman Sachs, HPE, Intel, Lambda, Leidos, McDonald's, Micron, NBCU...

Only 8 folders have actual notes:

- Microsoft (28), Google (11), OpenAI (4), Silk (3), Walmart (3), EY (1), Dhammak (1)

**Impact**: Low (stubs for future use)

**Action**: Consider marking as "placeholder" in README or pruning unused folders.

---

---

## 80) CRITICAL: Archive Filename Mismatch - Wrong Content Association

**Found**: 2026-01-04

**Status: NOT STARTED**

The archive file `Inbox/_archive/2026-01-04/2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen .md` contains:

- **Actual content**: Strategic Microsoft/VAST discussion (Jason + colleague discussing MAI, Bifrost, etc.)
- **Filename suggests**: "G24 Flight School" training content

The extracted note `VAST/ROB/2025-12-16 - VAST and Microsoft Strategic Discussion.md` has:

- `source_ref` pointing to the Flight School file
- Content extracted from the strategic discussion (correct content, wrong source attribution)

**Root Cause**: Multiple files may have been conflated during archive, or filename was wrong from ingestion.

**Impact**: Critical - source_ref traceability is broken. Can't trust archive file names.

**Investigation Needed**:

1. Check if `Inbox/Transcripts/` had duplicate/misnamed files
2. Verify archive process preserves original filenames
3. May need to re-ingest from MacWhisper exports

---

---

## 81) CRITICAL: MacWhisper Captures App Title, Not Meeting Title

**Found**: 2026-01-04

**Status: NOT STARTED**

Deep investigation of archive reveals **3 additional files with wrong names**:

| Archive Filename                            | Actual Content                                                                        |
| ------------------------------------------- | ------------------------------------------------------------------------------------- |
| `2025-12-17 13:53 - Google Chrome.md`       | Call with Avinash from Welliptic about blockchain agent execution platform            |
| `2025-12-19 09:50 - New Recording.md`       | Detailed Google GDC RFP call with Kamal, Malikarjan, David (encryption, benchmarking) |
| `2025-12-16 08:35 - G24 Flight School...md` | Strategic Microsoft/VAST discussion (MAI, Bifrost, supply chain)                      |

**Root Cause**: MacWhisper picks up the **foreground app window title** when recording starts, not the meeting title.

- "Google Chrome" = browser was active
- "New Recording" = default placeholder
- "G24 Flight School" = Zoom window title from previous meeting?

**Impact**: CRITICAL

- Archive filenames are unreliable as source_ref
- Content-filename mismatch breaks traceability
- ~3/132 (2.3%) of archive files confirmed wrong
- Unknown how many more have subtle mismatches

**Fix**:

1. **Immediate**: Manually audit and rename problematic archives
2. **Process**: Configure MacWhisper to prompt for title after recording ends
3. **Fallback**: Have LLM propose corrected filename during extraction phase
4. **Validation**: Add content-vs-filename sanity check to pipeline

---

---

## 82) Source Attribution Chain Is Broken

**Found**: 2026-01-04

**Status: NOT STARTED**

The `source_ref` field in extracted notes links to archive files, but:

- Archive filenames can be wrong (item 96, 97)
- No verification that source_ref file content matches extracted note content
- Cannot reliably trace back from a note to its source material

**Example**:
`VAST/ROB/2025-12-16 - VAST and Microsoft Strategic Discussion.md` has:

```yaml
source_ref: "Inbox/_archive/2026-01-04/2025-12-16 08:35 - G24 Flight School...md"
```

This points to a file whose NAME suggests Flight School training, but whose CONTENT is the Microsoft discussion.

**Impact**: Medium-High

- Audit/provenance trail is broken
- Cannot regenerate notes from source if needed
- Compliance/legal discovery scenarios compromised

**Fix**:

1. Store content hash of source at extraction time
2. Add `source_hash` field to frontmatter
3. Validation can compare archive file hash to stored hash

---

---

## 83) `type: "projects"` Never Used - 3 Project Notes Have Wrong Types

**Found**: 2026-01-04

**Status: NOT STARTED**

Schema defines 7 types: `customer`, `people`, `projects`, `rob`, `journal`, `partners`, `travel`

But scanning all notes in vault:

```
72 type: "customer"
48 type: "people"
 3 type: "rob"
 0 type: "projects"  ← NEVER USED!
```

3 notes in `**/Projects/` folders have wrong types:

- `VAST/Projects/Cloud Marketplace MVP/2025-10-01 - Cloud Marketplace MVP checklist.md` → `type: "people"`
- `VAST/Projects/Pricing/2025-10-01 - Pricing vTeam action list.md` → `type: "customer"`
- `Personal/Projects/LPM/2025-10-27 - LPM board AI discussion.md` → `type: "people"`

**Root Cause**: LLM extraction classifies by participant relationship, not destination folder.

**Fix**:

1. Add to extraction prompt: "Notes about project work use type=projects, not people/customer"
2. Alternatively: derive type from destination folder path in plan phase
3. Fix 3 existing notes

---

---

## 84) 3 Empty ROB Subfolders

**Found**: 2026-01-04

**Status: NOT STARTED**

All ROB subfolders are empty (no notes, no READMEs):

- `VAST/ROB/Phase Gate 1/` - empty
- `VAST/ROB/SRE/` - empty
- `VAST/ROB/VAST on Cloud Office Hours/` - empty

Only note is misplaced at ROB root level (item 71).

**Root Cause**: No ROB meetings processed yet, or all filed incorrectly.

**Fix**:

1. Add README.md to each ROB forum folder
2. Re-file any ROB notes that ended up elsewhere
3. Consider whether these forums are still active

---

---

## 85) Participant Name Inconsistencies

**Found**: 2026-01-04

**Status: NOT STARTED**

Participant names have multiple variations across notes:

| Canonical        | Variations                                    |
| ---------------- | --------------------------------------------- |
| Jason Vallery    | "Jason" (4x), "Jason Valleri", "Jason Valeri" |
| Jonsi Stephenson | "Jonsi Stefansson" (3x), "Jonsi Stemmelsson"  |
| Tomer Hagay      | "Tomer" (4x)                                  |
| Jeff Denworth    | "Jeff" (3x)                                   |
| Lior Genzel      | "Lior" (multiple)                             |

Also many first-name-only entries that can't be resolved: "Leo", "Tom", "Paul", "Chris", "John"

**Impact**: Medium

- Can't aggregate meetings by participant reliably
- Dataview queries won't group correctly
- Graph view links will be fragmented

**Fix**:

1. Add name normalization to extraction output validation
2. Maintain canonical name list in `Workflow/entities/aliases.yaml`
3. Post-process participants to resolve to full names

---

---

## 86) Duplicate Files Across Personal/VAST

**Found**: 2026-01-04

**Status: NOT STARTED**

Content hash analysis found exact duplicate files:

| Hash          | File 1                                    | File 2                                          |
| ------------- | ----------------------------------------- | ----------------------------------------------- |
| `cda0dbf7...` | `Personal/Projects/AI Talk/Outline.md`    | `VAST/Projects/AI Talk/Outline.md`              |
| `d41d8cd9...` | `Personal/Homelab/VMs/Frigate.md` (empty) | `VAST/Projects/OVA/Proxmox/Untitled.md` (empty) |

**Impact**: Low

- Confusion about canonical location
- Risk of divergent edits
- Wasted space

**Fix**:

1. Determine canonical location for AI Talk project (Personal or VAST?)
2. Delete empty placeholder files

---

---

## 87) Archive Files Have Colons in Filenames (macOS Quirk)

**Found**: 2026-01-04

**Status: NOT STARTED**

macOS allows colons in filenames (internally stored as `/`). Archive has files with colons:

```
2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen .md
```

This file was created by MacWhisper from a Zoom meeting title.

**Impact**: Low-Medium

- Colons display as `:` but are stored as `/` internally
- May cause issues when copying to non-macOS systems
- Git handles it fine but could confuse tools

**Fix**:

1. Rename archive files to remove colons
2. Configure MacWhisper to sanitize output filenames
3. Already handled in `sanitize_path()` for new files

---

---

## 88) Vault-Wide Statistics Summary

**Snapshot**: 2026-01-04

| Metric                  | Count              |
| ----------------------- | ------------------ |
| Total items in TODO.md  | 107                |
| CRITICAL priority items | 11                 |
| HIGH priority items     | 9                  |
| MEDIUM priority items   | 22                 |
| LOW priority items      | 18                 |
| Notes with `source_ref` | 123                |
| Broken source_refs      | 100                |
| People folders          | 136                |
| Customer folders        | 41                 |
| Project folders         | 59                 |
| ROB forums              | 3 (all empty)      |
| Pending transcripts     | 3                  |
| Pending emails          | 7 (4 dupe, 2 spam) |

**Audit Coverage**:

- ✅ Folder structure
- ✅ Wikilinks (broken, misspelled, orphan)
- ✅ Task format consistency
- ✅ Frontmatter fields
- ✅ Archive integrity
- ✅ Pipeline logs analysis
- ✅ Schema/model validation
- ✅ Template variable checks
- ✅ Participant name variations
- ✅ Duplicate content detection

- Consider symlinks or redirects for multi-context items

---

---

## 89) README Frontmatter Gaps (2 files)

**Found**: 2026-01-04

**Status: NOT STARTED**

Two entity READMEs have frontmatter that does not match standards/templates (missing required keys like `type`, `title`, `created`, `tags`):

- `VAST/People/Jonsi Stephenson/README.md`
- `VAST/Projects/Fort Meade "Gemini as a service" on-prem validation/README.md`

**Impact**: Medium - standards checks and queries become unreliable; template drift risk.

**Tasks**

- [ ] Migrate both READMEs onto the current templates (preserve any unique content).
- [ ] Add audit rule: fail if an entity README is missing required keys (`type`, `title`, `created`, `tags`).
- [ ] Decide whether `last_updated` is required in frontmatter and backfill accordingly.

**Success Criteria**

- `Workflow/scripts/audit_import.py` reports 0 entity READMEs with missing required frontmatter keys.

---

---

## 90) Tag Hygiene (Invalid Characters + Deep Paths)

**Found**: 2026-01-04

**Status: NOT STARTED**

Observed tags that violate normalization / conventions (uppercase, punctuation, or multi-level nesting), e.g.:

- `company/ssi-(safe-superintelligence-inc.)`
- `entity/Sam Hopewell`
- `industry/automotive-/-technology`
- `industry/semiconductors-/-ai-infrastructure`

**Impact**: Low-Medium - taxonomy inconsistency; validators/queries can break if tag grammar tightens.

**Tasks**

- [ ] Confirm allowed tag grammar in `Workflow/STANDARDS.md` (slash depth, allowed chars).
- [ ] Add a `normalize_tag()` step during extraction/apply (lowercase, strip punctuation, collapse separators).
- [ ] Run a cleanup pass to rewrite existing invalid tags to canonical forms.

**Success Criteria**

- `rg -n \"company/ssi-\\(safe-superintelligence-inc\\.\\)\" VAST Personal` returns 0.
- `rg -n \"industry/.*-/-\" VAST Personal` returns 0.

---

---

## 91) Meeting Notes with Empty `participants: []` (5 files)

**Found**: 2026-01-04

**Status: NOT STARTED**

5 generated notes have `participants: []` and render an empty “Attendees” line; most appear to be checklist/article-style sources mislabeled as transcripts:

- `VAST/Customers and Partners/Google/2025-10-01 - Confirm GCP GA timing.md`
- `VAST/Customers and Partners/Google/2025-11-13 - GDC RFP security and ops.md`
- `VAST/Customers and Partners/Microsoft/2025-11-12 - Microsoft AI capacity and VAST.md`
- `VAST/Customers and Partners/Microsoft/2025-12-18 - VAST Azure integration outline.md`
- `VAST/Projects/Cloud Marketplace MVP/2025-10-01 - Cloud Marketplace MVP checklist.md`

**Impact**: Medium - weak context, poor people graph, and likely indicates `source_kind` misclassification (see item 77).

**Tasks**

- [ ] If `source_kind=transcript`, require non-empty participants (or explicitly mark unknown).
- [ ] If `source_kind=checklist|article`, omit participants and omit “Attendees” line in templates.
- [ ] Backfill the 5 affected notes to set correct `source_kind` and/or participants.

**Success Criteria**

- `Workflow/scripts/audit_import.py` reports 0 transcript-kind notes with empty participants.
- Generated notes never render an empty `**Attendees**:` line.
