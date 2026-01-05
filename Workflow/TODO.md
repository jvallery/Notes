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

**Status: ✅ COMPLETED** (2026-01-05)

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

---

---

## Legacy Backlog Archived

Legacy remediation items (1–93) have been archived; see git history if needed. The list below is the current unified work plan aligned to UNIFIED-PIPELINE.md.

---

## 1) Unified Pipeline Fit-Gap vs Architecture Doc

**Goal:** Align pipeline implementation with UNIFIED-PIPELINE.md (persona/manifest/glossary/aliases context, prompt caching, instrumentation).

**Status: ✅ COMPLETED** (2026-01-05)

**Discovery:** UnifiedExtractor/ContextBundle exist but still hand-roll prompts and skip cached persona/glossary/aliases; instrumentation not surfaced.

**Impact:** Critical

**Effort:** 4 hours

**Tasks**
- [ ] Map architecture components to code and list missing behaviors vs UNIFIED-PIPELINE.md
- [ ] Wire ContextBundle to load persona, manifests, glossary, aliases, README summaries; feed cached prompts into UnifiedExtractor
- [ ] Ensure extractor uses instrumented client (utils.ai_client) with cache-friendly prompt ordering
- [ ] Update UNIFIED-PIPELINE.md/docstrings with the wired context path

**Success Criteria**
- UnifiedExtractor prompt includes cached persona + glossary + aliases and logs via instrumented client
- ContextBundle returns enriched context (persona + manifests + relevant README summaries) verified by tests/fixtures
- Fit-gap notes captured in UNIFIED-PIPELINE.md or code comments

---

## 2) Smart Patch, ChangePlan, and Entity Dedup/Apply

**Goal:** Make patch generation/entity routing match unified models with ChangePlan validation and rollback-ready apply.

**Status: ✅ COMPLETED** (2026-01-04)

**Discovery:** PatchGenerator/TransactionalApply not fully tied to EntityIndex/aliases or facts_about; planner is separate from pipeline run.

**Impact:** High

**Effort:** 4 hours

**Tasks**
- [ ] Drive patches off `facts_about` for all mentioned entities; resolve via EntityIndex + aliases
- [ ] Route UnifiedPipeline through ChangePlan objects (reuse schemas/changeplan + plan.py patterns) before apply
- [ ] Add apply validation + rollback/dry-run hooks; ensure manifest sync safety
- [ ] Document dedupe/alias merge rules in REFACTOR/UNIFIED-PIPELINE

**Success Criteria**
- ChangePlans validate and include patches for every entity with facts
- Apply supports dry-run/rollback and preserves manifest integrity
- Tests cover dedupe/alias resolution on email + transcript fixtures

---

## 3) Unified Outputs: Draft Replies, Calendar, Tasks

**Goal:** Generate downstream outputs from UnifiedPipeline with TASKS-compatible tasks (`?` → `[ ]`/`/`/`R`/`x`).

**Status: ✅ COMPLETED** (2026-01-04)

**Impact:** High

**Effort:** 3 hours

**Tasks**
- [x] Implement outputs module for draft replies and calendar suggestions (persona + context) to `Inbox/_drafts/`
- [x] Standardize task emission to `- [?] ... #task #proposed #auto` with priority/dates; mirror high-priority tasks into TASKS.md views
- [x] Add acceptance flow notes (`?` → accepted/rejected/in-progress/done) to TASKS.md dashboards
- [x] Update EMAIL-INGESTION/README/RUNBOOK to describe output + triage path

**Success Criteria**
- Sample email run yields draft reply + optional .ics suggestion
- Tasks appear in TASKS.md Proposed section sorted priority → created date
- Docs show one-click triage path from Proposed to Accepted/Rejected/Done

---

## 4) Single CLI + Retire Legacy Scripts

**Goal:** Make `scripts/ingest.py` the single entry point that calls UnifiedPipeline; archive legacy process_* and ingest_* scripts.

**Status: ✅ COMPLETED** (2026-01-05)

**Note:** Reclaimed from stale @copilot-b620700 on 2026-01-05 (session unresponsive).

**Impact:** Medium

**Effort:** 2 hours

**Tasks**
- [x] Update `scripts/ingest.py` to wrap UnifiedPipeline with flags: type/all, dry-run, verbose, outputs, enrich
- [x] Convert legacy scripts to thin wrappers or move to `_archive/` with deprecation notice
- [x] Refresh README/RUNBOOK/UNIFIED-PIPELINE and automations/SETUP-CHECKLIST with the single-command workflow
- [x] Add smoke test over fixture Inbox content

**Success Criteria**
- `python scripts/ingest.py --all` processes email + transcript fixtures end-to-end
- Legacy scripts emit deprecation notice or are archived
- Docs/checklists reference only the unified CLI

---

## 5) Observability + Prompt Cache Metrics

**Goal:** Apply instrumentation and cache metrics across pipeline phases.

**Status: ✅ COMPLETED** (2026-01-05)

**Impact:** Medium

**Effort:** 2 hours

**Tasks**
- [x] Wrap adapter/extract/patch/apply/output phases with structured logging + timings; print run summary
- [x] Surface prompt cache hit/miss and token savings; add `--show-cache-stats` flag
- [x] Persist metrics to `logs/ai` and human-readable logs; document how to view stats
- [x] Add unit/fixture test to ensure metrics fields populate

**Success Criteria**
- Logs show phase timings and cache hit/miss data; summary emitted at run end
- `logs/ai/YYYY-MM-DD/summary.json` includes `unified_pipeline` stats
- Cache stats flag works without errors

---

## 6) Context Search, Entity Index, and Aliases

**Goal:** Strengthen entity discovery (search + aliases) for context loading and dedupe.

**Status: IN PROGRESS** (@codex-20260105, started: 2026-01-05 00:30)

**Impact:** Medium

**Effort:** 3 hours

**Tasks**
- [ ] Extend EntityIndex with fuzzy search + alias resolution (people/company/project) and caching
- [ ] Add pre-extraction context enrichment: search vault for relevant READMEs/notes (VAST + Personal) and feed summaries into ContextBundle
- [ ] Add duplicate detection on apply with merge guidance in changeplans
- [ ] Document search/alias rules in UNIFIED-PIPELINE.md and ENTITY-DISCOVERY.md

**Success Criteria**
- Extraction loads relevant READMEs even with aliases/variants (verified on fixture)
- Apply flags potential dupes and suggests merge target
- Docs updated with search/alias flow

---

## 7) Email-First Person Matching

**Goal:** Use email as the primary key for person lookup with name fallback.

**Status: NOT STARTED**

**Impact:** High

**Effort:** 45 minutes

**Tasks**
- [ ] Build email→folder index from People READMEs; cache on first call
- [ ] Lookup order: email match → exact full name → alias/partial match via EntityIndex
- [ ] Ensure extraction preserves sender/recipient emails; changeplan uses email when available
- [ ] Add tests for email-first matching in UnifiedPipeline adapters/extractor

**Success Criteria**
- Person with `email:` in frontmatter is resolved by email
- Fallbacks work when email missing; tests cover email/name/alias cases

---

## 8) Re-Ingest Sources to Populate Empty README Sections

**Goal:** Replay ingestion to fix past misrouted patches and fill empty Key Facts/Topics/Decisions.

**Status: NOT STARTED**

**Impact:** High

**Effort:** 1 hour

**Tasks**
- [ ] Re-run email pipeline via unified CLI on Sources/Email and Inbox (dry-run first)
- [ ] Spot-check 5 high-contact people (Jeff Denworth, Jai Menon, Lior Genzel, etc.)
- [ ] Decide if transcript re-run is needed; document outcome

**Success Criteria**
- Key people READMEs show populated Key Facts/Topics/Decisions
- No new patches target wrong folders

---

## 9) Full Vault Reimport (Optional Reset)

**Goal:** If remediation is insufficient, rebuild People/Projects/Customers from Sources/.

**Status: NOT STARTED**

**Impact:** Critical (destructive; last resort)

**Effort:** 2–4 hours

**Tasks**
- [ ] Only proceed after items 1–8 are complete and validated
- [ ] Tag current state, back up entity folders, then delete and re-ingest Sources/Email + Sources/Transcripts
- [ ] Run audit/validation scripts post-import; compare stats before/after

**Success Criteria**
- Clean reimport with no empty sections or misrouted patches
- Audit passes with zero critical findings

---

## 10) Customer/Account Manifest and Enrichment

**Goal:** Extend manifest + enrichment to Customers/Partners and wire into unified pipeline context.

**Status: NOT STARTED**

**Impact:** Medium

**Effort:** 2 hours

**Tasks**
- [ ] Create/refresh `VAST/Customers and Partners/_MANIFEST.md` with key columns
- [ ] Add sync + enrichment functions (or extend enrich pattern) and include in ContextBundle
- [ ] Include customer manifest in draft/reply context gathering

**Success Criteria**
- Customer manifest available to extractor and outputs
- Drafts include relevant customer context

---

## 11) Manifest Enrichment Documentation Complete

**Goal:** Finish MANIFEST-ENRICHMENT.md to match current CLIs and levels.

**Status: NOT STARTED**

**Impact:** Low

**Effort:** 30 minutes

**Tasks**
- [ ] Align doc with enrich_person/customer CLIs and L0–L4 examples
- [ ] Add troubleshooting and common workflows

**Success Criteria**
- MANIFEST-ENRICHMENT.md enables a new user to run enrichment end-to-end without assistance

---

## 12) Magic Strings Audit

**Goal:** Externalize all hardcoded strings (config, mappings, aliases, keys) into configuration or manifest systems.

**Status: NOT STARTED**

**Impact:** Medium

**Effort:** 2-3 hours

**Tasks**
- [ ] Audit all Python scripts for hardcoded paths, entity names, API keys, model names
- [ ] Audit prompt templates for hardcoded domain terms or mappings
- [ ] Move discovered magic strings to config.yaml, entities/aliases.yaml, or manifests
- [ ] Add validation that required config keys exist at startup

**Success Criteria**
- No hardcoded paths or entity names in Python scripts (except test fixtures)
- All configurable values loaded from config.yaml or manifests
- Startup fails fast with clear error if required config missing

---

## 🗒️ Agent Session Notes (2026-01-04)

**Session Summary:** Copilot agent session became unresponsive. Documenting progress for handoff.

**Completed This Session (uncommitted):**

1. **Item 1 (Fit-Gap)** - Marked complete. ContextBundle wired with cached prompts, glossary, aliases.

2. **Legacy Script Archival (partial Item 4):**
   - Moved to `Workflow/_archive/`:
     - `process_inbox_legacy.py`
     - `process_emails_legacy.py`
     - `ingest_emails_legacy.py`
     - `ingest_transcripts_legacy.py`
     - `extract_legacy.py`
     - `plan_legacy.py`
     - `apply_legacy.py`

3. **Code Changes (uncommitted in working tree):**
   - `pipeline/context.py` - Added `get_cached_prompt_prefix()`, `get_dynamic_context()`, relationship extraction
   - `pipeline/extract.py` - Added VERBOSITY RULES section with examples
   - `pipeline/outputs.py` - Created OutputGenerator for draft replies + calendar
   - `pipeline/pipeline.py` - Integrated OutputGenerator
   - `scripts/manifest_sync.py` - Added my_relationship, my_role columns
   - `UNIFIED-PIPELINE.md` - Updated with fit-gap notes

**Next Steps for New Agent:**

1. Run `git status` to see all uncommitted changes
2. Review changes with `git diff` 
3. Commit with: `git add -A && git commit -m "[wip] Pipeline improvements: cached prompts, outputs, verbosity rules"`
4. Continue with Item 4 (update VS Code tasks.json to use ingest.py)
5. Then Item 5 (observability), Item 6 (entity search), Item 7 (email-first matching)

**Files to Review Before Continuing:**
- `Workflow/pipeline/context.py` - Verify cached prompt logic
- `Workflow/pipeline/outputs.py` - New file, verify it's complete
- `Workflow/_archive/` - Verify legacy scripts archived correctly
