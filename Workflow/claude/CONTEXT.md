# Context Primer: Notes Vault Automation

> Quick context for AI agents working with this system

---

## What Is This?

A **local-first automation pipeline** for an Obsidian vault that:

1. **Ingests** meeting transcripts and emails into `Inbox/`
2. **Extracts** structured data using OpenAI (tasks, decisions, mentions)
3. **Plans** vault operations as a JSON schema
4. **Applies** changes atomically with git commit

---

## Key Architecture Decisions

| Decision                          | Why                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------- |
| **ChangePlan Pattern**            | AI generates JSON operations; Python executes them. Separates reasoning from execution. |
| **Pydantic + Structured Outputs** | Schema enforcement at generation time, not post-validation                              |
| **Transactional Apply**           | Backup → Execute → Rollback on failure. All-or-nothing.                                 |
| **Privacy: store=False**          | All OpenAI calls explicitly opt out of training                                         |
| **Headless Operation**            | No Obsidian plugins required; pure Python + Jinja2                                      |

---

## Pipeline Phases

```
EXTRACT                    PLAN                      APPLY
─────────                  ────                      ─────
scripts/extract.py         scripts/plan.py           scripts/apply.py

Input: Raw .md            Input: .extraction.json   Input: .changeplan.json
Output: .extraction.json  Output: .changeplan.json  Output: New files, patches

AI: OpenAI gpt-4o         AI: OpenAI gpt-4o         AI: NONE (deterministic)
Schema: ExtractionV1      Schema: ChangePlan
```

---

## Allowed Operations

The LLM can only generate these operations in a ChangePlan:

| Operation | Purpose                | Example             |
| --------- | ---------------------- | ------------------- |
| `create`  | New note from template | Create meeting note |
| `patch`   | Update existing file   | Add to README.md    |
| `link`    | Insert wikilinks       | Add [[Person]] refs |

**NOT allowed** (deterministic post-steps):

- `archive` - Python moves source to `Inbox/_archive/`
- `delete` - Never allowed
- Direct file writes - Always through templates

---

## Patch Primitives

Only these structured operations are allowed (no regex):

| Primitive              | Purpose                            |
| ---------------------- | ---------------------------------- |
| `upsert_frontmatter`   | Add/update YAML frontmatter fields |
| `append_under_heading` | Append content under `## Heading`  |
| `ensure_wikilinks`     | Add links if not already present   |

---

## Entity Types

| Type      | Location                                 | Key Field   |
| --------- | ---------------------------------------- | ----------- |
| People    | `VAST/People/{Name}/`                    | `person`    |
| Customers | `VAST/Customers and Partners/{Account}/` | `account`   |
| Projects  | `VAST/Projects/{Name}/`                  | `project`   |
| ROB       | `VAST/ROB/{Forum}/`                      | `rob_forum` |
| Personal  | `Personal/{Type}/{Name}/`                | varies      |

Each entity folder has:

- `README.md` - Source of truth (contact info, status)
- `YYYY-MM-DD - {Title}.md` - Historical dated notes

---

## Profiles (Not Personas)

Profiles are **extraction rubrics** that tell the AI what to focus on:

| Profile                 | Use Case                                       |
| ----------------------- | ---------------------------------------------- |
| `work_sales.yaml`       | Customer meetings: deals, blockers, next steps |
| `work_engineering.yaml` | Technical: architecture, requirements          |
| `work_leadership.yaml`  | Strategy: decisions, priorities                |
| `personal.yaml`         | Personal: home projects, relationships         |

---

## Task Format

Tasks use Obsidian Tasks plugin syntax:

```markdown
- [ ] Action text @Owner 📅 YYYY-MM-DD ⏫ #task
```

Priority markers: 🔺 highest · ⏫ high · 🔼 medium · 🔽 low · ⏬ lowest

---

## Key Files

| File                       | Purpose                     |
| -------------------------- | --------------------------- |
| `Workflow/config.yaml`     | Runtime configuration       |
| `Workflow/README.md`       | Main documentation          |
| `Workflow/DESIGN.md`       | Architecture details        |
| `models/extraction.py`     | ExtractionV1 Pydantic model |
| `models/changeplan.py`     | ChangePlan Pydantic model   |
| `scripts/process_inbox.py` | Full pipeline orchestrator  |

---

## Safety Guarantees

1. **Git required**: Apply phase requires clean git tree
2. **Atomic writes**: temp file + rename pattern
3. **Rollback**: Any failure restores backups
4. **Validation**: ChangePlans validated before execution
5. **No AI in Apply**: Apply phase has zero AI calls

---

## Known Issues (As of 2025-01-03)

1. **Config has invalid model names** (`gpt-5.2-*` doesn't exist)
2. **Aliases not loaded** in planner (TODO in plan.py#L122)
3. **No test coverage** - zero test files
4. **Stale resource paths** in config.yaml

See `claude/REVIEW-BUNDLE.md` for full analysis.
