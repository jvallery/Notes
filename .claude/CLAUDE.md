# Claude Code Configuration

> **Project**: Notes Vault (Obsidian + Automation)
> **Mode**: Autonomous

## Agent Behavior

Claude Code operates with full autonomy in this repository.

### Allowed Without Asking

- All file operations (create, edit, move, delete)
- All terminal commands
- Git operations
- Package installation

### Scope Boundaries

- ✅ `/Users/jason/Documents/Notes/**` — Full access
- ❌ Outside vault — Not permitted

## Key Files

| File                              | Purpose                 |
| --------------------------------- | ----------------------- |
| `AGENTS.md`                       | Autonomy documentation  |
| `.github/copilot-instructions.md` | Vault conventions       |
| `Workflow/DESIGN.md`              | System architecture     |
| `Workflow/IMPLEMENTATION.md`      | Implementation progress |
| `Workflow/config.yaml`            | Runtime configuration   |

## Python Environment

```bash
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
# Python 3.13 with OpenAI, Pydantic, Click, Jinja2
```

## Processing Pipeline

1. **Extract**: `python scripts/extract.py --all`
2. **Plan**: `python scripts/plan.py --all` (Phase 4)
3. **Apply**: `python scripts/apply.py --all` (Phase 5)

## Quick Commands

```bash
# Activate environment
source Workflow/.venv/bin/activate

# Run extraction
python Workflow/scripts/extract.py --all --verbose

# Check for syntax errors
python -m py_compile Workflow/scripts/*.py

# Git status
git status --short
```
