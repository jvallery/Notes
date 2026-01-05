# Agent Configuration: Full Autonomy for Notes Vault

> **Mode**: God Mode (Maximum Autonomy)  
> **Last Updated**: 2025-01-03

This document describes how AI agents (Copilot/Claude, Codex) are configured
for autonomous operation within the Notes vault.

## God Mode Configuration

**All agents operate with `approval_policy: never`** — execute without confirmation.

| Layer                | File                              | Key Setting         |
| -------------------- | --------------------------------- | ------------------- |
| VS Code UI           | `.vscode/settings.json`           | `autoApprove: true` |
| Claude Code          | `.claude/CLAUDE.md`               | Full autonomy scope |
| Copilot Instructions | `.github/copilot-instructions.md` | Permissions matrix  |
| Agent Profiles       | `.claude/agents/autonomous.md`    | Execution policies  |

## Scope of Autonomy

Agents have **full autonomy** within `/Users/jason/Documents/Notes/` to:

- Create, edit, move, and delete files
- Run terminal commands
- Execute Python scripts
- Commit changes to git

## Configuration Files

| File                              | Purpose                                            |
| --------------------------------- | -------------------------------------------------- |
| `.vscode/settings.json`           | VS Code workspace settings, agent auto-approve     |
| `.claude/CLAUDE.md`               | Claude Code project configuration                  |
| `.claude/agents/autonomous.md`    | Autonomous agent execution policies                |
| `Notes.code-workspace`            | Workspace definition with launch configs and tasks |
| `.github/copilot-instructions.md` | Context and conventions for Copilot/Claude         |
| `AGENTS.md`                       | This file - agent autonomy documentation           |
| `Workflow/.env.example`           | Environment variable template                      |
| `Workflow/config.yaml`            | Runtime configuration (paths, settings)            |

## Run Commands (No Confirmation)

Agents can execute these commands directly:

```bash
# Activate Python environment
cd ~/Documents/Notes/Workflow && source .venv/bin/activate

# Process all pending transcripts
python scripts/extract.py --all --verbose

# Check pipeline status
python scripts/extract.py --all --dry-run

# Git operations
git add -A && git commit -m "[auto] Processed inbox"
git status
git log --oneline -5
```

## Agent Capabilities

### File Operations

- ✅ Create new notes in any folder
- ✅ Edit existing notes (frontmatter, content, tasks)
- ✅ Move/rename files to correct destinations
- ✅ Archive processed files to `Inbox/_archive/`
- ✅ Create new entity folders (People, Projects, Accounts)

### Terminal Commands

- ✅ Run Python scripts from `Workflow/scripts/`
- ✅ Git operations (add, commit, push)
- ✅ File system operations (mkdir, mv, cp)
- ✅ Package management (pip install)

### Restricted Operations

- ⚠️ API calls require valid credentials in environment
- ⚠️ External network calls subject to API rate limits
- ❌ No access outside `~/Documents/Notes/` folder

## Task Management Standard (Obsidian Tasks Plugin)

**Source of truth**: Tasks live in their **source notes** (meeting notes, project notes, etc.) using Obsidian Tasks checkbox format:

```markdown
- [ ] Action item text @Owner 📅 YYYY-MM-DD 🔺 #task
```

**Dashboard**: `TASKS.md` at the vault root is **query-only** and aggregates open tasks across the vault. Checking a task off in `TASKS.md` updates the original source note and removes it from the dashboard lists.

**Rules**

- Always tag actionable tasks with `#task` so they appear in dashboards.
- AI-generated tasks must also include `#proposed #auto`; removing `#proposed` = you accepted the task.
- Prefer creating tasks under `VAST/` (work) or `Personal/` (personal) so the dashboard can group them cleanly.
- Do not create or use `{Domain}/_Tasks/` folders; legacy task lists were archived under `Inbox/_archive/`.
- Legacy manual list is preserved in `TASKS_BACKLOG.md` (referenced from `TASKS.md`).

## Triggering Agent Actions

### Interactive (VS Code Chat)

```
@workspace Process all pending items in Inbox/_extraction/
@workspace Update the root doc for Jeff Denworth with latest meeting notes
@workspace Create a new project folder for "AI Pipelines Collateral"
```

### Scripted (Python → Agent handoff)

1. Python script extracts structured JSON to `Inbox/_extraction/`
2. Agent reads JSON and executes vault updates
3. Agent archives source files and commits changes

### Scheduled (launchd/cron)

```bash
# Run at 6 PM daily - process all pending extractions
0 18 * * * cd ~/Documents/Notes && /path/to/venv/python Workflow/scripts/process_inbox.py
```

## Safety Mechanisms

1. **Git version control**: All changes tracked, easy rollback
2. **Archive pattern**: Source files preserved in `Inbox/_archive/`
3. **Idempotent operations**: Re-running produces same result
4. **Structured JSON intermediate**: Human-reviewable extraction output

## Environment Setup

### First-time setup

```bash
cd ~/Documents/Notes/Workflow
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
```

### Required environment variables

```bash
OPENAI_API_KEY=sk-...          # For extraction scripts
NOTES_ROOT=/Users/jason/Documents/Notes
```

## Agent Context Files

The agent loads context from these files to understand the vault:

1. **`.github/copilot-instructions.md`** - Primary instructions

   - Vault architecture
   - Note types and templates
   - Task format
   - Frontmatter conventions

2. **`Workflow/DESIGN.md`** - System design

   - Processing flow
   - Component architecture
   - AI model allocation

3. **`Workflow/prompts/`** + **`Workflow/templates/`** - Prompts + templates
   - Jinja2 prompt layers (extract/plan/backfill)
   - Note templates for created notes and README roots

4. **`Workflow/schemas/`** - JSON schemas
   - `extraction.schema.json` (ExtractionV1)
   - `changeplan.schema.json` (ChangePlan)

5. **`Workflow/EMAIL-INGESTION.md`** - Email processing pipeline
   - 6-step email processing workflow
   - Entity extraction and vault patching
   - Draft response generation
   - Email address as primary key for people lookup

## Email Processing

**Quick Reference**: See [Workflow/EMAIL-INGESTION.md](Workflow/EMAIL-INGESTION.md) for full documentation.

### 6-Step Pipeline

```
DEDUPE → EXTRACT → PATCH → GATHER → DRAFT → ARCHIVE
```

1. **DEDUPE**: Remove duplicate email exports
2. **EXTRACT**: AI extraction of contacts, tasks, facts
3. **PATCH**: Update vault READMEs with knowledge
4. **GATHER**: Collect related READMEs for context
5. **DRAFT**: Generate AI response with vault context
6. **ARCHIVE**: Move to `Sources/Email/YYYY/`

### Commands

```bash
# Full pipeline
python scripts/process_emails.py

# Knowledge capture only (phases 1-3)
python scripts/process_emails.py --phase 1-3

# Response generation only (phases 4-6)
python scripts/process_emails.py --phase 4-6

# Dry-run
python scripts/process_emails.py --dry-run
```

### Entity Indexing

- **Email addresses** are used as primary keys when available
- **Single names** with email are allowed (email = stable index)
- **Single names** without email are skipped (ambiguous)
- **Multi-email** people should list all addresses in frontmatter

---

## TODO Workflow (Multi-Agent)

> **Purpose**: Enable multiple agents to work on `Workflow/TODO.md` simultaneously without conflicts.

### Core Principles

1. **Atomic Claims**: Always commit immediately after claiming an item
2. **Git as Lock**: Use git commits to prevent race conditions
3. **Fail Fast**: If a claim commit fails, another agent got there first
4. **Time Limits**: Claims expire after 4 hours of inactivity
5. **Lower = Higher Priority**: Item numbers indicate priority (lower = more important)

### Work Item Lifecycle

```
NOT STARTED → IN PROGRESS → COMPLETED
                    ↓
                BLOCKED ←→ NOT STARTED (released)
```

### Status Markers (Exact Format Required)

```markdown
**Status: NOT STARTED**
**Status: IN PROGRESS** (@agent-id, started: 2026-01-04 14:30)
**Status: ✅ COMPLETED** (2026-01-04)
**Status: ⏸️ BLOCKED** (waiting on item 5)
```

### Agent ID Convention

Use a unique, traceable identifier:

- `copilot-{session-hash}` - GitHub Copilot sessions
- `claude-{session-id}` - Claude Code sessions
- `codex-{run-id}` - OpenAI Codex runs
- `manual` - Human edits

### Claiming Protocol (Step-by-Step)

```bash
# 1. Ensure clean state and latest TODO
cd ~/Documents/Notes
# If this repo has no remote tracking configured, this will error; that's OK.
git pull --rebase || true

# 2. Find available work
grep -n "Status: NOT STARTED" Workflow/TODO.md | head -5

# 3. Read the item you want to claim (e.g., item 27)
grep -A30 "^## 27)" Workflow/TODO.md

# 4. Edit TODO.md to change status (use sed or editor)
# Replace: **Status: NOT STARTED**
# With:    **Status: IN PROGRESS** (@copilot-abc123, started: 2026-01-04 14:30)

# 5. Commit IMMEDIATELY (this is your "lock")
git add Workflow/TODO.md
git commit -m "[todo] Claim item 27: Inconsistent Task Owner Names"

# 6. If commit succeeds, you own the item. Start working.
# 7. If commit fails (conflict), someone else claimed it. Pick another.
```

### Conflict Resolution

| Scenario                   | Resolution                                                            |
| -------------------------- | --------------------------------------------------------------------- |
| Two agents claim same item | First successful commit wins; other agent picks different item        |
| Claim older than 4 hours   | Any agent can reclaim (add note: "Reclaimed from stale @{old-agent}") |
| Agent crashes mid-work     | On restart, agent should complete or release its claims               |
| Merge conflict on TODO.md  | Pull latest, re-check item status, re-claim if still available        |

### Commit Message Conventions

```bash
# Claiming
[todo] Claim item {N}: {Title}

# Completing (with the actual fix)
[fix] {Description} (item {N})

# Releasing
[todo] Release item {N}: {reason}

# Blocking
[todo] Block item {N}: {reason}

# Adding new item
[todo] Add item {N}: {Title}
```

### Stale Claim Detection

An agent can reclaim a stale item if:

1. Status shows `IN PROGRESS` with timestamp > 4 hours ago
2. No commits from that agent in the last 4 hours
3. The reclaiming agent adds a note: `**Note:** Reclaimed from stale @{old-agent} on {date}`

### Best Practices

1. **Claim one item at a time** - Complete before claiming another
2. **Make progress commits** - Commit partial work every 30-60 minutes
3. **Release if stuck** - Don't hold items you can't complete
4. **Lower numbers first** - Priority is implied by item number
5. **Check dependencies** - Some items depend on others (noted in description)
6. **Verify success criteria** - Don't mark complete until criteria are met
7. **Document blockers** - If blocked, explain why in the status

### Quick Commands

```bash
# Count items by status
echo "Available: $(grep -c 'Status: NOT STARTED' Workflow/TODO.md)"
echo "In Progress: $(grep -c 'Status: IN PROGRESS' Workflow/TODO.md)"
echo "Completed: $(grep -c 'Status: ✅ COMPLETED' Workflow/TODO.md)"
echo "Blocked: $(grep -c 'Status: ⏸️ BLOCKED' Workflow/TODO.md)"

# Find my claimed items (replace agent-id)
grep -B10 "@copilot-abc123" Workflow/TODO.md

# Find stale claims (>4 hours old) - requires date comparison
grep "Status: IN PROGRESS" Workflow/TODO.md

# List available high-priority items (first 10)
grep -B5 "Status: NOT STARTED" Workflow/TODO.md | head -50
```
