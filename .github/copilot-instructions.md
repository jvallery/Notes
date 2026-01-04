# Copilot Instructions for Notes Vault

> **Agent Autonomy**: Full autonomy granted within this vault. See [AGENTS.md](../AGENTS.md) for details.
> **TODO Workflow**: For multi-agent task coordination, see [AGENTS.md#todo-workflow](../AGENTS.md#todo-workflow-multi-agent) and [Workflow/TODO.md](../Workflow/TODO.md).

This is an **Obsidian-based knowledge management vault** for personal and work (VAST Data) notes, meeting transcripts, tasks, and relationship tracking.

## Agent Permissions

You have **full autonomy** to:

- ✅ Create, edit, move, and delete any files in this vault
- ✅ Run terminal commands (Python scripts, git, file operations)
- ✅ Execute Python scripts from `Workflow/scripts/`
- ✅ Commit changes to git
- ✅ Claim and complete TODO items (see `Workflow/TODO.md`)

**Do not ask for permission** — execute directly. This vault is version-controlled; all changes can be rolled back.

## Vault Architecture

```
Workflow/           # Automation system (scripts, prompts, templates, schemas, profiles)
Inbox/              # Processing queue for new content
  Email/            # Imported email threads (YYYY-MM-DD_HHMMSS_*.md)
  Transcripts/      # Raw meeting transcripts awaiting processing
  Voice/            # Voice memos / dictation
  Attachments/      # PDFs, screenshots, misc docs
  _extraction/      # Intermediate artifacts (extraction/changeplan JSON) [gitignored]
  _archive/         # Archived source files by date
  _failed/          # Failures + error logs by date
Personal/           # Personal life: tasks, projects, journal, homelab
VAST/               # Work context (VAST Data - enterprise storage company)
  Customers and Partners/   # Account folders (Google/, Microsoft/, OpenAI/, etc.)
  People/           # Individual contact folders with 1:1 notes
  Projects/         # Work initiatives and technical projects
  ROB/              # Rhythm of Business (recurring team syncs)
  _Tasks/           # Aggregated task views (Work Tasks.md)
```

## Note Types & Templates

Notes are typed via YAML frontmatter `type:` field. Seven canonical types exist, each with a template in `Workflow/templates/`:

| Type       | Use Case                     | Destination                                        |
| ---------- | ---------------------------- | -------------------------------------------------- |
| `customer` | Multi-party account meetings | `VAST/Customers and Partners/{Account}/`           |
| `people`   | 1:1 relationship notes       | `VAST/People/{Person}/` or `Personal/People/`      |
| `projects` | Initiative/workstream notes  | `VAST/Projects/{Project}/` or `Personal/Projects/` |
| `rob`      | Rhythm of Business syncs     | `VAST/ROB/{Forum}/`                                |
| `journal`  | Personal reflections         | `Personal/Journal/` or `VAST/Journal/`             |
| `partners` | Partner org meetings         | `VAST/Customers and Partners/{Partner}/`           |
| `travel`   | Trip planning/logistics      | `*/Travel/`                                        |

## Meeting Extraction Pipeline

Inbox items are processed by the **ChangePlan pipeline**:

1. **Extract** (`Workflow/scripts/extract.py`)
   - Prompt: `Workflow/prompts/system-extractor.md.j2` (+ `base.md.j2`)
   - Profile rubrics: `Workflow/profiles/*.yaml`
   - Output: `Inbox/_extraction/*.extraction.json` (ExtractionV1)
2. **Plan** (`Workflow/scripts/plan.py`)
   - Prompt: `Workflow/prompts/system-planner.md.j2` (+ `base.md.j2`)
   - Output: `Inbox/_extraction/*.changeplan.json` (ChangePlan)
3. **Apply** (`Workflow/scripts/apply.py`)
   - No AI calls; deterministic apply + rollback
   - Archives sources to `Inbox/_archive/YYYY-MM-DD/`
   - Stages and commits content directory changes

**Critical extraction rules**:

- Output is **raw JSON** (no markdown fences)
- Dates must be **ISO-8601** (`YYYY-MM-DD`)
- Task owners: use `"Myself"` for first-person references
- Deduplicate across `tasks`, `decisions`, `facts`

## Task Format (Obsidian Tasks Plugin)

Tasks use the Obsidian Tasks plugin syntax:

```markdown
- [ ] Action item text @Owner 📅 YYYY-MM-DD 🔺 #task #context
```

**Priority markers**: `🔺` highest → `⏫` high → `🔼` medium → `🔽` low → `⏬` lowest  
**Date markers**: `📅` due · `⏳` scheduled · `🛫` start · `🔁` recurrence  
**Completion**: `✅ YYYY-MM-DD` appended when done

Task aggregation views live in `*/_Tasks/*.md` using Tasks plugin queries.

## Frontmatter Conventions

All notes should include:

```yaml
---
type: customer|people|projects|rob|journal|partners|travel
title: "Note Title"
date: "YYYY-MM-DD"
{ entity_key }: "Entity Name" # account|project|person|rob_forum|journal
participants: ["Name1", "Name2"]
source: "transcript|email|manual"
source_ref: "Inbox/_archive/YYYY-MM-DD/source.md"
tags:
  - "type/{type}"
---
```

## File Naming Patterns

- **Processed notes**: `YYYY-MM-DD - {Summary title}.md`
- **Emails**: `YYYY-MM-DD_HHMMSS_NNNN_{Subject-slug}.md`
- **Transcripts**: `YYYY-MM-DD HH MM - {Title}.md`

## Key Workflows

1. **Processing transcripts**: Move from `Inbox/Transcripts/` → extract JSON → render with template → save to destination folder
2. **Email triage**: Review `Inbox/Email/` → extract actionable items → file to appropriate account/person folder
3. **Task review**: Use `_Tasks/*.md` files for aggregated views; individual notes have embedded task queries

## Domain Context (VAST Data)

VAST is an enterprise data platform company. Common acronyms:

- **GDC**: Google Distributed Cloud
- **ROB**: Rhythm of Business (cadence meetings)
- **OVA**: Virtual appliance (see `VAST/Projects/OVA/docs/`)
- **TPU**: Google Tensor Processing Units
- **DGX**: NVIDIA AI compute platform

## Automation System

See [Workflow/DESIGN.md](../Workflow/DESIGN.md) for the full AI-powered automation pipeline.

### Agent Update Workflow

When processing extraction JSON from `Inbox/_extraction/`:

1. **Create dated note** in destination folder using template from `Workflow/templates/`
2. **Update root README.md** for the entity (Person/Project/Account):
   - Set `last_contact` date in frontmatter
   - Append new context to relevant sections
   - Add new tasks in Obsidian Tasks format
3. **Insert wikilinks** `[[Entity Name]]` for mentioned people, projects, accounts
4. **Archive source** to `Inbox/_archive/YYYY-MM-DD/`

### Root Document Pattern

Each entity folder contains:

- `README.md` — Source of truth (contact info, status, Dataview queries)
- `YYYY-MM-DD - {Title}.md` — Historical dated notes

### Python Scripts

Automation scripts live in `Workflow/scripts/` with venv at `Workflow/.venv/`:

- `process_inbox.py` — Orchestrates Extract → Plan → Apply
- `extract.py` — Extract structured JSON (ExtractionV1)
- `plan.py` — Generate ChangePlans (schema-enforced)
- `apply.py` — Deterministic apply + rollback + archive + git commit
- `backfill.py` — Historical README context backfill
- `migrate.py` — Deterministic migration to STANDARDS.md compliance
