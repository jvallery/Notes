# Autonomous Agent Configuration

> **Mode**: Full Autonomy (God Mode)
> **Scope**: `/Users/jason/Documents/Notes/` and subdirectories

## Execution Policy

This agent operates with **no confirmation required** for:

### File Operations

- ✅ Create files anywhere in the vault
- ✅ Edit any file (markdown, YAML, JSON, Python)
- ✅ Move/rename files
- ✅ Delete files (with git safety net)
- ✅ Create directories

### Terminal Commands

- ✅ Execute Python scripts from `Workflow/scripts/`
- ✅ Run git commands (add, commit, status, diff)
- ✅ Install packages via pip
- ✅ File operations (mkdir, mv, cp, rm)
- ✅ Any shell command within vault scope

### API Calls

- ✅ OpenAI API (extraction, planning)
- ✅ Local HTTP servers (if applicable)

## Behavioral Directives

1. **Execute, don't ask** — If a task is clear, do it immediately
2. **Fail fast, report clearly** — If something fails, stop and explain
3. **Use git as safety net** — All changes are tracked; commit frequently
4. **Follow DESIGN.md** — The source of truth for system architecture
5. **Preserve existing structure** — Don't reorganize without explicit request

## Common Tasks (Execute Without Confirmation)

```bash
# Process all pending transcripts
cd ~/Documents/Notes/Workflow && source .venv/bin/activate && python scripts/extract.py --all

# Check for errors in Python code
python -m py_compile scripts/*.py

# Git operations
git add -A && git commit -m "[auto] Processed inbox items"
git status
git diff HEAD~1
```

## Context Loading Priority

1. `AGENTS.md` — Autonomy scope and capabilities
2. `.github/copilot-instructions.md` — Vault conventions
3. `Workflow/DESIGN.md` — System architecture
4. `Workflow/IMPLEMENTATION.md` — Current phase and progress

## Rollback Protocol

If something goes wrong:

1. `git stash` to save uncommitted changes
2. `git checkout -- <file>` to restore specific file
3. `git reset --hard HEAD~1` to undo last commit
4. Check `Inbox/_archive/` for original source files
