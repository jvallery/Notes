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

3. **`Inbox/_bins/_prompts/`** - Extraction prompts
   - JSON schema
   - Type-specific guidance
