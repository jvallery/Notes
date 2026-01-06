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

---

## 1) Prevent empty `participants` in generated notes

**Goal:** Ensure extracted notes always include at least one participant and avoid blank `**Attendees**:` headers.

**Status: ✅ COMPLETED** (2026-01-05)

**Discovery:**
`audit_import.py` flagged multiple notes with `participants: []` and empty `**Attendees**:` during manual vault cleanup.

**Impact:** Medium - Missing participants reduces context quality and makes audits noisy.

**Effort:** 2–4 hours

**Tasks**
- [ ] Update extraction to infer participants from source metadata (email headers, transcript metadata, or explicit “With/Attendees” lines).
- [ ] Decide a safe fallback (e.g., include `Jason Vallery` when source implies the note was captured by the user).
- [ ] Add a regression test with a fixture that previously produced `participants: []`.

**Success Criteria**
- New imports do not generate `participants: []` for transcript/meeting notes.
- `Workflow/scripts/audit_import.py` reports zero `participants` warnings for newly ingested items.

## 2) Avoid placeholder entity links like `**Account**: [[]]`

**Goal:** Stop emitting placeholder entity header links and ensure account/project headers match the entity.

**Status: ✅ COMPLETED** (2026-01-06)

**Discovery:**
Dozens of notes were created with `**Account**: [[]]` / `**Project**: [[]]` even when the note lived inside an entity folder.

**Impact:** Medium - Placeholder headers break link graph and reduce note readability.

**Effort:** 2–3 hours

**Tasks**
- [ ] In patch/template generation, omit header entity lines when the entity is unknown instead of emitting `[[]]`.
- [ ] Ensure entity keys are always populated for notes created inside entity folders.
- [ ] Add tests that assert generated markdown contains no `[[]]` placeholders.

**Success Criteria**
- Grep across newly generated notes finds zero `**Account**: [[]]` and zero `**Project**: [[]]`.

## 3) Fix README frontmatter duplication / YAML escaping bugs

**Goal:** Ensure entity `README.md` files always have a single valid YAML frontmatter block and safe quoting.

**Status: ✅ COMPLETED** (2026-01-05)

**Discovery:**
At least one People README contained two YAML frontmatter blocks and invalid quoting in fields (breaking manifest scan expectations).

**Impact:** Medium - Invalid README frontmatter breaks manifests and entity resolution.

**Effort:** 2–4 hours

**Tasks**
- [ ] Identify the code path that can create duplicated frontmatter blocks (likely apply/patch README writes).
- [ ] Add a regression test for a README containing quotes (e.g., organization names) and ensure YAML remains valid.
- [ ] Add an audit check: README must start with exactly one frontmatter block.

**Success Criteria**
- `manifest_sync.py sync` succeeds without skipping any README due to YAML errors.
- No README contains multiple frontmatter blocks.

## 4) Improve entity resolution for similar names (e.g., Kanchan vs Akanksha)

**Goal:** Prevent cross-contamination of facts/tasks between similarly named people and stabilize alias handling.

**Status: ✅ COMPLETED** (2026-01-05)

**Discovery:**
Facts/tasks for Akanksha Mehrotra were mistakenly attributed in Kanchan Mehrotra context during import/README generation.

**Impact:** Medium - Misattribution reduces trust in entity READMEs and prompts.

**Effort:** 1–2 hours

**Tasks**
- [ ] Add/extend alias mappings for nicknames/transcript variants.
- [ ] Add a unit test demonstrating correct resolution for both names.

**Success Criteria**
- Imports referencing “Akanksha” map to `Akanksha Mehrotra`; “Kanchan/Koncha” maps to `Kanchan Mehrotra`.
- No People README contains facts belonging to the other person.

## 5) Integrate post-import normalization into the pipeline

**Goal:** Make post-import cleanup automatic and idempotent as part of the ingest flow.

**Status: ✅ COMPLETED** (2026-01-05)

**Discovery:**
Multiple cleanup passes were required after import (frontmatter normalization, header placeholders cleanup).

**Impact:** High - Manual cleanup is error-prone and will recur on full reimports.

**Effort:** 1–2 hours

**Tasks**
- [ ] Add a post-apply phase to run normalization helpers (frontmatter + header cleanup) on updated files.
- [ ] Document the post-import cleanup phase in `Workflow/UNIFIED-PIPELINE.md`.

**Success Criteria**
- A fresh ingest run yields entity folders that pass `audit_import.py` without manual intervention.

---

# Pipeline Architecture Review (2026-01-05)

The following items address critical bugs, edge cases, and architectural issues identified in a comprehensive code review of the ingestion pipeline.

---

## 6) PatchGenerator writes to disk during planning (breaks dry-run and transactionality)

**Goal:** Make PatchGenerator pure (no disk writes) so planning phase is side-effect-free.

**Status: NOT STARTED**

**Discovery:**
Code review identified `PatchGenerator._create_entity_folder()` calls `folder.mkdir()` and `readme_path.write_text()` during plan generation, violating the reasoning/execution separation principle.

**Impact:** Critical - Running with `--dry-run` can still create entity folders/READMEs. Parallel mode's extraction-only phase (`apply=False`) creates folders/READMEs. TransactionalApply rollback won't remove those created folders (not tracked by `_created`).

**Effort:** 4–6 hours

**Tasks**
- [ ] Refactor `_create_entity_folder()` to return a planned creation operation instead of performing disk writes.
- [ ] Add `entities_to_create` operations to ChangePlan that TransactionalApply can execute.
- [ ] Track created entity folders in TransactionalApply so rollback can remove them.
- [ ] Add test: `--dry-run` must not create any files or directories.
- [ ] Add test: failed apply must rollback all created entity folders.

**Success Criteria**
- `PatchGenerator.generate()` performs zero disk writes.
- Running `ingest.py --dry-run` creates no files or directories.
- A failed `TransactionalApply.apply()` removes all entity folders created during that run.

---

## 7) Transaction rollback does not undo source archiving/moves

**Goal:** Make source archiving fully transactional (undo on failure).

**Status: NOT STARTED**

**Discovery:**
Code review of `TransactionalApply._archive_source()` shows sources are moved with `shutil.move()` after patching. If exception occurs after moving, `_rollback()` restores modified files but does NOT move sources back.

**Impact:** Critical - Sources can be moved out of Inbox even on failure, leaving a "rolled back" vault but missing inputs.

**Effort:** 3–4 hours

**Tasks**
- [ ] Track source moves in a `_moved_sources: dict[Path, Path]` (original → archive destination).
- [ ] In `_rollback()`, move sources back to original locations.
- [ ] Alternative: use copy + delete-only-on-success pattern.
- [ ] Add test: failed apply after source archiving restores sources to Inbox.

**Success Criteria**
- On apply failure, all sources are restored to their original Inbox locations.
- No sources are lost on pipeline failure.

---

## 8) Source archiving collision risk (possible overwrite)

**Goal:** Prevent source archiving from overwriting existing files with same name.

**Status: NOT STARTED**

**Discovery:**
`TransactionalApply._archive_source()` uses `archive_path = archive_dir/source_path.name`. If two sources share the same filename (common for email exports), the second can overwrite the first or fail on Windows.

**Impact:** Medium - Possible data loss when multiple sources have same filename.

**Effort:** 1–2 hours

**Tasks**
- [ ] Before archiving, check if destination exists.
- [ ] If collision, append counter suffix (`_1`, `_2`) or timestamp suffix.
- [ ] Add test: two sources with identical names are both archived without collision.

**Success Criteria**
- No source file is overwritten during archiving.
- Collision-safe naming is logged when applied.

---

## 9) Parallel execution is not thread-safe (shared mutable state)

**Goal:** Make parallel mode thread-safe by eliminating data races on shared state.

**Status: NOT STARTED**

**Discovery:**
Code review identified `_process_paths_parallel()` calls `self.process_file()` concurrently, but shared instances have mutable state:
- `self.extractor` mutates `last_usage`, caches client
- `self.patch_generator` mutates `_created_folders` and writes to disk
- `self.entity_index` mutates caches: `_search_cache`, indices, alias load
- `ai_client.py` uses global client with mutable caller/context via `set_context()`

**Impact:** Critical - Data races can cause wrong entity folder selection, missing patches, corrupt AI logging, or context bleed between files.

**Effort:** 6–8 hours

**Tasks**
- [ ] Option A: Create per-task instances of extractor/patchgen/entity_index in `process_file()`.
- [ ] Option B: Add threading locks around all mutable shared state.
- [ ] Remove or guard `InstrumentedClient.set_context()` usage in parallel mode.
- [ ] Ensure AI logging JSONL writes are atomic (use file locking or separate log files per thread).
- [ ] Add integration test: parallel processing of 10+ files produces consistent results.

**Success Criteria**
- Parallel mode produces identical results to sequential mode for the same inputs.
- No data races or shared state corruption under concurrent load.

---

## 10) Parallel mode behavior differs from sequential mode (output generation)

**Goal:** Unify sequential and parallel output generation logic.

**Status: NOT STARTED**

**Discovery:**
Code review found:
(a) `draft_all_emails` logic differs: sequential uses `force_reply = is_email and self.draft_all_emails`, parallel uses `force_reply=is_email` (always true for emails).
(b) Parallel output loop gates on `if not (is_email or (suggested and suggested.needs_reply)): continue`, potentially skipping tasks for transcripts/documents.

**Impact:** High - Parallel mode generates drafts for all emails regardless of `draft_all_emails` flag. Transcripts with tasks may not emit tasks in parallel mode.

**Effort:** 2–3 hours

**Tasks**
- [ ] Extract output gating logic into shared helper function.
- [ ] Apply identical predicate in both sequential and parallel code paths.
- [ ] Add test: parallel mode with `draft_all_emails=False` should NOT generate drafts for automated/no-reply emails.
- [ ] Add test: transcript with tasks emits tasks in both modes.

**Success Criteria**
- `--draft-all-emails` flag behavior is identical in sequential and parallel modes.
- All content types with tasks emit tasks in both modes.

---

## 11) VOICE content type not supported end-to-end

**Goal:** Complete VOICE content type support or remove it.

**Status: NOT STARTED**

**Discovery:**
- `ContentType.VOICE` exists in `envelope.py`
- CLI supports `--type voice`
- Config validation requires `models.extract_voice`
- BUT: `AdapterRegistry.default()` registers only Email/Transcript/Document adapters

**Impact:** Medium - Voice items in `Inbox/Voice/*.md` are parsed by DocumentAdapter, becoming `ContentType.DOCUMENT`. `extract_voice` model config may never be used.

**Effort:** 3–4 hours

**Tasks**
- [ ] Option A: Implement `VoiceAdapter` that detects voice memos and returns `ContentType.VOICE`.
- [ ] Option B: Remove VOICE type entirely and document that voice memos are processed as documents.
- [ ] Ensure config validation matches actual adapter registry.
- [ ] Add test: voice memos are processed with correct content type and model.

**Success Criteria**
- `Inbox/Voice/*.md` files are processed with consistent, documented behavior.
- Config validation matches actual pipeline capabilities.

---

## 12) Manifest patch flow dead (extractor discards discovered_aliases/acronyms)

**Goal:** Make discovered aliases/acronyms flow through to manifest patches.

**Status: NOT STARTED**

**Discovery:**
- `models.py` defines `discovered_aliases`, `discovered_acronyms` in UnifiedExtraction
- `PatchGenerator._generate_manifest_patches()` consumes them
- BUT: `UnifiedExtractor._build_extraction()` never reads these fields from LLM JSON

**Impact:** Medium - LLM can output alias/acronym discoveries but they never affect manifests, making that prompt guidance wasted.

**Effort:** 2–3 hours

**Tasks**
- [ ] Parse `discovered_aliases` and `discovered_acronyms` from LLM response in `_build_extraction()`.
- [ ] Add to UnifiedExtraction model.
- [ ] Verify `_generate_manifest_patches()` creates valid patches.
- [ ] Add test: extraction with discovered alias creates manifest patch.

**Success Criteria**
- New aliases discovered by LLM are patched into `_MANIFEST.md`.
- Acronym discoveries are added to project manifest.

---

## 13) Git commit behavior is risky (commits on any non-dry-run regardless of failures)

**Goal:** Only git commit when batch has zero failures.

**Status: NOT STARTED**

**Discovery:**
`ingest.py` → `_git_commit()` runs on any non-dry-run, even with failures. `git add -A` stages all files at vault root, potentially including unrelated changes (logs, caches, partial artifacts).

**Impact:** Medium - Partial/corrupt state can be committed; unrelated files can be committed.

**Effort:** 1–2 hours

**Tasks**
- [ ] Only call `_git_commit()` when `batch.failed == 0`.
- [ ] Stage only content directories (VAST/, Personal/, Sources/, Outbox/) instead of `-A`.
- [ ] Add `--no-commit` flag to skip git operations entirely.
- [ ] Add test: failed batch does not trigger commit.

**Success Criteria**
- Git commits only occur on fully successful runs.
- Only content directories are staged (no logs, caches, or artifacts).

---

## 14) EmailAdapter recipient parsing can crash on empty parts

**Goal:** Make recipient parsing robust to malformed headers.

**Status: NOT STARTED**

**Discovery:**
If To line includes trailing comma or double commas, `part.strip()` becomes empty, `name_match` is None, then `re.sub(..., name)` throws because `name` is None.

**Impact:** Low - Crash on malformed email headers.

**Effort:** 30 minutes

**Tasks**
- [ ] Guard against None name in `_extract_recipients()`.
- [ ] Set `name = ""` as default when name_match is None.
- [ ] Add test: email with malformed To header (trailing comma) parses without crash.

**Success Criteria**
- Malformed email headers do not cause crashes.

---

## 15) TranscriptAdapter can emit bogus "Speaker 1" entities

**Goal:** Prevent generic speaker labels from being treated as people.

**Status: NOT STARTED**

**Discovery:**
`speakers` can include literal labels like "Speaker 1" when mapping isn't found. These flow into participants, potentially causing folder creation for "Speaker 1".

**Impact:** Medium - Bogus entity folders for generic speaker labels.

**Effort:** 1 hour

**Tasks**
- [ ] Filter out participants matching regex `^Speaker \d+$` (and similar patterns).
- [ ] Treat unmapped speakers as unknown/skip rather than creating entities.
- [ ] Add test: transcript with "Speaker 1", "Speaker 2" labels doesn't create Speaker folders.

**Success Criteria**
- No entity folders are created for generic speaker labels.

---

## 16) ContextBundle nondeterministic dynamic suffix (hurts caching)

**Goal:** Make context bundle deterministic for cache stability.

**Status: NOT STARTED**

**Discovery:**
`enriched` is a `set`; `list(enriched)[:12]` is nondeterministic because set iteration order varies. This affects "relevant readmes" selection, breaking cache stability.

**Impact:** Low - Cache hit rate reduced; debugging harder due to nondeterminism.

**Effort:** 30 minutes

**Tasks**
- [ ] Sort the enriched set before slicing: `sorted(enriched)[:12]`.
- [ ] Add test: same input produces same context bundle hash.

**Success Criteria**
- ContextBundle is deterministic for identical inputs.

---

## 17) ContextBundle glossary typing inconsistency

**Goal:** Fix glossary type to match actual data structure.

**Status: NOT STARTED**

**Discovery:**
`bundle.glossary` is declared `dict[str, str]` but `_extract_acronyms_from_manifest()` inserts dict values like `{"full_name": name, "definition": definition}`. Type mismatch can cause runtime errors.

**Impact:** Low - Type confusion; potential runtime errors.

**Effort:** 30 minutes

**Tasks**
- [ ] Change type annotation to `dict[str, Any]` or `dict[str, str | dict]`.
- [ ] Or flatten to string format: `"Full Name — Definition"`.
- [ ] Add type validation in `_extract_acronyms_from_manifest()`.

**Success Criteria**
- Glossary type annotation matches actual runtime data.
- mypy/pyright passes without type errors.

---

## 18) Quick entity scan uses substring matching (false positives)

**Goal:** Improve entity detection to avoid false positives with short names.

**Status: NOT STARTED**

**Discovery:**
`if name.lower() in content_lower` matches "Ann" in "annual", "Dan" in "danger", etc. This pulls irrelevant READMEs into context, increasing token use and confusing extraction.

**Impact:** Medium - Increased token costs; potentially confused extraction.

**Effort:** 2–3 hours

**Tasks**
- [ ] Use word boundary matching: `\b{name}\b` regex.
- [ ] Consider minimum name length threshold (3+ characters).
- [ ] Add test: "Ann" does not match "annual report".

**Success Criteria**
- Short names only match when they appear as whole words.
- Token usage for context loading is reduced.

---

## 19) Extraction JSON parse error treated as success

**Goal:** Treat JSON parse failure as pipeline failure.

**Status: NOT STARTED**

**Discovery:**
On JSON parse error, `_build_minimal_extraction()` returns a minimal extraction with confidence 0. Downstream patch generation may still create meeting notes and archive sources.

**Impact:** Medium - Corrupt/minimal notes created; sources archived despite failure.

**Effort:** 1–2 hours

**Tasks**
- [ ] Raise exception on JSON parse failure instead of returning minimal extraction.
- [ ] Add retry logic (1-2 retries with backoff) before failing.
- [ ] Move source to `_failed/` on extraction failure, not archive.
- [ ] Add test: JSON parse failure does not archive source.

**Success Criteria**
- JSON parse failures result in explicit pipeline errors.
- Sources with failed extraction go to `_failed/`, not `Sources/`.

---

## 20) ChangePlan.validate_plan() doesn't consider add_wikilinks

**Goal:** Fix validation to recognize wikilink-only patches as valid.

**Status: NOT STARTED**

**Discovery:**
Validation can flag a patch as "has no changes" even if it only adds wikilinks, because `add_wikilinks` is not checked in the "has_changes" condition.

**Impact:** Low - Valid patches incorrectly flagged as invalid.

**Effort:** 30 minutes

**Tasks**
- [ ] Add `patch.add_wikilinks` to the `has_changes` check in `validate_plan()`.
- [ ] Add test: patch with only `add_wikilinks` is valid.

**Success Criteria**
- Wikilink-only patches pass validation.

---

## 21) dry-run doesn't report primary source archiving

**Goal:** Make dry-run report complete list of files that would be archived.

**Status: NOT STARTED**

**Discovery:**
`_dry_run_apply()` collects `extra_source_paths` but not `source_path`. Dry-run output lies about what will be archived.

**Impact:** Low - Misleading dry-run output.

**Effort:** 30 minutes

**Tasks**
- [ ] Add `source_path` to `files_archived` in dry-run mode.
- [ ] Add test: dry-run reports all sources that would be archived.

**Success Criteria**
- Dry-run output accurately lists all files that would be created, modified, and archived.

---

## 22) TransactionalApply._atomic_write() weaker than existing utility

**Goal:** Use the robust atomic write from `scripts/utils/fs.py`.

**Status: NOT STARTED**

**Discovery:**
`_atomic_write()` uses deterministic temp filename (`file.md.tmp`), not unique temp file. Rename semantics can fail on Windows when overwriting. `scripts/utils/fs.py` already has a robust implementation.

**Impact:** Low - Potential Windows failures; code duplication.

**Effort:** 30 minutes

**Tasks**
- [ ] Replace `_atomic_write()` with import from `scripts/utils/fs.atomic_write()`.
- [ ] Or copy the robust implementation (unique temp, proper error handling).
- [ ] Add test: concurrent writes to same file don't corrupt.

**Success Criteria**
- Single atomic write implementation used throughout.
- Windows compatibility verified.

---

## 23) Patch application silently skips missing target files

**Goal:** Log warning when patch target file doesn't exist.

**Status: NOT STARTED**

**Discovery:**
`_apply_patch()` returns early if target doesn't exist. This can hide real issues (e.g., plan refers to file that should have been created but wasn't).

**Impact:** Low - Silent failures; harder debugging.

**Effort:** 30 minutes

**Tasks**
- [ ] Add warning log when target file not found.
- [ ] Optionally add to `ApplyResult.warnings`.
- [ ] Add test: missing patch target produces warning.

**Success Criteria**
- Missing patch targets are logged for debugging.

---

## 24) OutputGenerator calendar invite formatting invalid

**Goal:** Generate valid ICS calendar invites.

**Status: NOT STARTED**

**Discovery:**
Calendar generation uses `mailto:{a}@example.com` where `{a}` is a human name (not email). ICS formatting typically needs CRLF and proper escaping.

**Impact:** Low - Generated calendar invites don't work in real calendar apps.

**Effort:** 2–3 hours

**Tasks**
- [ ] Look up attendee emails from contacts/entity index.
- [ ] Use proper ICS CRLF line endings.
- [ ] Escape special characters per ICS RFC.
- [ ] Add test: generated ICS validates against ICS parser.

**Success Criteria**
- Calendar invites can be imported into Google Calendar/Outlook.

---

## 25) OutputGenerator dry_run still creates directories

**Goal:** Prevent directory creation in dry-run mode.

**Status: NOT STARTED**

**Discovery:**
`OutputGenerator.__init__()` creates `Outbox/`, `_calendar/`, `_prompts/` directories even when `dry_run=True` (the `if not dry_run:` guard may not cover all paths).

**Impact:** Low - Dry-run has side effects.

**Effort:** 30 minutes

**Tasks**
- [ ] Move all `mkdir()` calls inside `if not dry_run:` blocks.
- [ ] Add test: dry-run creates no directories.

**Success Criteria**
- `--dry-run` creates no files or directories.

---

## 26) Tasks inbox writing not safe for parallelism

**Goal:** Make TASKS_INBOX.md writes atomic and safe for parallel execution.

**Status: NOT STARTED**

**Discovery:**
Multiple tasks are appended by repeated read/replace/write cycles without locking. Parallel runs or concurrent edits can interleave and lose updates.

**Impact:** Medium - Task loss in parallel mode.

**Effort:** 1–2 hours

**Tasks**
- [ ] Use file locking (fcntl/msvcrt) for TASKS_INBOX.md writes.
- [ ] Or batch all tasks and write once at end of parallel run.
- [ ] Add test: concurrent task writes don't lose data.

**Success Criteria**
- Parallel task emission doesn't lose tasks.

---

## 27) Duplicate detection probably doesn't work

**Goal:** Fix or remove duplicate detection.

**Status: NOT STARTED**

**Discovery:**
`_is_duplicate()` looks for artifacts in `Inbox/_extraction`, but pipeline doesn't write extraction artifacts there (only optional `trace_dir`). Also keys by stem, not content hash.

**Impact:** Medium - Duplicates not detected; or wrong content skipped.

**Effort:** 2–3 hours

**Tasks**
- [ ] Option A: Write extraction artifacts to `Inbox/_extraction` and check there.
- [ ] Option B: Use content hash-based dedup (hash stored in manifest or separate index).
- [ ] Add test: reprocessing same file is correctly detected as duplicate.
- [ ] Add test: different content with same filename is NOT skipped.

**Success Criteria**
- Duplicate detection correctly identifies already-processed content.
- Different content with same filename is processed.

---

## 28) Rate limiting config is unused

**Goal:** Implement rate limiting for parallel API calls.

**Status: NOT STARTED**

**Discovery:**
`requests_per_minute` is read from config but never used. Parallel mode blasts requests without throttling.

**Impact:** Medium - Risk of API rate limit errors in high-volume runs.

**Effort:** 2–3 hours

**Tasks**
- [ ] Implement token bucket or sliding window rate limiter.
- [ ] Apply rate limit in parallel extraction loop.
- [ ] Add config option to disable rate limiting.
- [ ] Add test: rate limiter respects configured RPM.

**Success Criteria**
- Parallel mode respects `requests_per_minute` config.
- No rate limit errors from OpenAI API.

---

## 29) Config paths vs hard-coded paths inconsistency

**Goal:** Respect config paths throughout pipeline.

**Status: NOT STARTED**

**Discovery:**
Some components use config paths, others hard-code:
- `_is_duplicate()` uses `vault_root/Inbox/_extraction`
- `_archive_source()` always archives to `vault_root/Sources/...`
- `_create_meeting_note()` uses `vault_root/Workflow/templates`
- `OutputGenerator` uses `Outbox/` fixed location

**Impact:** Medium - "Works on my vault" behavior; config less trustworthy.

**Effort:** 3–4 hours

**Tasks**
- [ ] Audit all hard-coded paths in pipeline modules.
- [ ] Replace with config lookups (with sensible defaults).
- [ ] Document required config paths in `config.yaml`.
- [ ] Add test: pipeline works with non-standard vault layout.

**Success Criteria**
- All paths are configurable.
- Pipeline works with custom vault layouts.

---

## 30) sys.path manipulation in multiple modules

**Goal:** Clean up import graph and eliminate sys.path hacks.

**Status: NOT STARTED**

**Discovery:**
Many modules do `sys.path.insert(...)` to reach `scripts.*`. This causes confusing import graphs, duplicate module loads, and `isinstance` failures.

**Impact:** Low - Maintenance burden; subtle bugs.

**Effort:** 4–6 hours

**Tasks**
- [ ] Create proper package structure with `__init__.py` files.
- [ ] Use relative imports within packages.
- [ ] Remove all `sys.path.insert()` calls.
- [ ] Add `pyproject.toml` or `setup.py` for editable install.
- [ ] Verify imports work from any working directory.

**Success Criteria**
- No `sys.path` manipulation in source files.
- `import pipeline` and `import scripts.utils` work correctly.

---

## 31) Utility functions duplicated across modules

**Goal:** Consolidate utility functions to single source of truth.

**Status: NOT STARTED**

**Discovery:**
- `slugify/basename/strip_extension` redefined in `TransactionalApply._create_meeting_note()` but exist in `scripts/utils/templates.py`
- `atomic_write` in Apply vs `scripts/utils/fs.py`
- Path handling for archive/extraction exists in `scripts/utils/paths.py` but pipeline uses hard-coded paths

**Impact:** Low - Fixes in one place don't propagate; behavior diverges.

**Effort:** 2–3 hours

**Tasks**
- [ ] Audit all utility function definitions in pipeline modules.
- [ ] Replace with imports from `scripts/utils/`.
- [ ] Remove duplicate implementations.
- [ ] Add test: utility functions are not duplicated.

**Success Criteria**
- Each utility function has single implementation.
- All pipeline code imports from shared utils.

---

## 32) Config validation mismatch (extract_voice required, extract_document not)

**Goal:** Align config validation with actual pipeline requirements.

**Status: NOT STARTED**

**Discovery:**
`_validate_config()` requires `extract_voice` but not `extract_document`. Yet DocumentAdapter exists and processes documents.

**Impact:** Low - Config validation doesn't match reality.

**Effort:** 30 minutes

**Tasks**
- [ ] Add `extract_document` to required config if documents are processed.
- [ ] Or make all `extract_*` configs optional with fallbacks.
- [ ] Document which model configs are required vs optional.

**Success Criteria**
- Config validation matches actual pipeline model usage.
