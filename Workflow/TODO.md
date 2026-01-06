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

**Status: IN PROGRESS** (@codex-20260105, started: 2026-01-05 17:12)

**Discovery:**
Multiple cleanup passes were required after import (frontmatter normalization, header placeholders cleanup).

**Impact:** High - Manual cleanup is error-prone and will recur on full reimports.

**Effort:** 1–2 hours

**Tasks**
- [ ] Add a post-apply phase to run normalization helpers (frontmatter + header cleanup) on updated files.
- [ ] Document the post-import cleanup phase in `Workflow/UNIFIED-PIPELINE.md`.

**Success Criteria**
- A fresh ingest run yields entity folders that pass `audit_import.py` without manual intervention.
