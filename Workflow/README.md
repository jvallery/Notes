# Workflow: Obsidian Vault Automation

> Local-first automation pipeline for processing meeting transcripts, emails, and notes into structured knowledge.

## Quick Start

```bash
# Activate environment
cd ~/Documents/Notes/Workflow
source .venv/bin/activate

# Process all pending inbox items
python scripts/process_inbox.py

# Or run phases individually
python scripts/extract.py --all --dry-run    # Preview extraction
python scripts/plan.py --all                  # Generate change plans
python scripts/apply.py --all                 # Apply changes (transactional)
```

## Architecture Overview

The system follows a **ChangePlan Pattern** separating AI reasoning from execution:

```
Inbox/ (raw sources) → Extract (AI) → Plan (AI) → Apply (deterministic)
                           ↓              ↓             ↓
                     .extraction.json  .changeplan.json  Files + Git commit
```

**Key Principles:**
- AI extracts and plans, Python executes deterministically
- Transactional apply with rollback on failure
- All changes are git-committed for auditability
- `store=False` on all OpenAI calls for privacy

## Documentation

| Document | Purpose |
|----------|---------|
| [DESIGN.md](DESIGN.md) | Core architecture and ChangePlan pattern |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Functional requirements and workflows |
| [STANDARDS.md](STANDARDS.md) | File naming, frontmatter, task format conventions |
| [SOURCES_ARCHITECTURE.md](SOURCES_ARCHITECTURE.md) | Source file storage in `Sources/` folder |
| [BACKFILL-DESIGN.md](BACKFILL-DESIGN.md) | Historical content processing system |

## Directory Structure

```
Workflow/
├── scripts/              # Python automation
│   ├── extract.py        # Phase 1: Content → JSON
│   ├── plan.py           # Phase 2: JSON → ChangePlan
│   ├── apply.py          # Phase 3: Apply changes
│   ├── process_inbox.py  # Orchestrator
│   ├── backfill.py       # Historical processing
│   └── utils/            # Shared utilities
├── templates/            # Jinja2 templates for notes
├── prompts/              # AI extraction prompts
├── profiles/             # Extraction rubrics by context
├── schemas/              # Pydantic models
└── config.yaml           # Runtime configuration
```

## Common Commands

```bash
# Backfill historical content
python scripts/backfill.py scan          # Find existing notes
python scripts/backfill.py extract       # Extract from notes
python scripts/backfill.py aggregate     # Build READMEs
python scripts/backfill.py apply         # Write files

# Maintenance
python scripts/cleanup/readme_normalizer.py --dry-run    # Preview normalization
python scripts/cleanup/source_normalizer.py --dry-run    # Preview file renames
python scripts/migrate.py status                         # Check migration status
```

## Environment Setup

```bash
# First-time setup
cd ~/Documents/Notes/Workflow
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Copy and edit environment file
cp .env.example .env
# Set OPENAI_API_KEY in .env
```

## Vault Structure

```
Notes/
├── Inbox/              # Processing queue
│   ├── Transcripts/    # Meeting recordings
│   ├── Email/          # Imported emails
│   └── _extraction/    # JSON outputs (gitignored)
├── Sources/            # Archived primary sources
│   └── Transcripts/    # By year (2025/, 2026/)
├── VAST/               # Work context
│   ├── People/         # Individual contacts
│   ├── Customers/      # Account folders
│   └── Projects/       # Work initiatives
├── Personal/           # Personal context
└── Workflow/           # This automation system
```

## Related

- [AGENTS.md](../AGENTS.md) - AI agent autonomy configuration
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) - Copilot context
