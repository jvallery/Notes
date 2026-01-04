# Standards: File Management & Conventions

> **Version**: 1.0.0 (Final)  
> **Last Updated**: 2026-01-03  
> **Status**: Locked  
> **Related**: [REQUIREMENTS.md](REQUIREMENTS.md) | [DESIGN.md](DESIGN.md)

This document defines the **Source of Truth** for file management in the Notes vault. All automation scripts and human contributors must follow these conventions.

---

## 1. Directory Hierarchy

### 1.1 Top-Level Structure

| Directory   | Purpose                                       | Ownership           |
| ----------- | --------------------------------------------- | ------------------- |
| `Inbox/`    | Landing zone for all incoming content         | Automation + Manual |
| `Personal/` | Personal life: tasks, projects, relationships | Manual primary      |
| `VAST/`     | Work context (VAST Data employment)           | Automation + Manual |
| `Workflow/` | Automation system (scripts, config, logs)     | Developers only     |

### 1.2 Inbox Structure (Processing Queue)

```
Inbox/
├── Email/                  # Captured emails (.eml + .md pairs)
├── Transcripts/            # Meeting recordings (MacWhisper output)
├── Voice/                  # Voice memos, dictation
├── Attachments/            # Manual file drops
├── _extraction/            # AI-generated JSON (gitignored)
│   ├── *.extraction.json   # Structured data from content
│   └── *.changeplan.json   # Operations to apply
├── _archive/               # Processed source files
│   └── YYYY-MM-DD/         # Organized by processing date
└── _failed/                # Dead letter queue
    └── YYYY-MM-DD/         # Failed files with error logs
```

### 1.3 Entity Folder Structure

All entities (People, Projects, Accounts) follow the same pattern:

```
{Domain}/{EntityType}/{EntityName}/
├── README.md              # Root doc (source of truth)
└── YYYY-MM-DD - {Title}.md  # Historical notes
```

**Examples**:

```
VAST/People/Jeff Denworth/
├── README.md
├── 2026-01-03 - Weekly 1-1.md
└── 2025-12-15 - Q4 Review.md

Personal/Projects/Greenhouse/
├── README.md
├── 2026-01-02 - Sensor Installation.md
└── 2025-12-20 - Materials List.md
```

### 1.4 Task Dashboards

```
{Domain}/_Tasks/
└── {Scope} Tasks.md        # Dataview queries ONLY (not task storage)
```

**Critical**: Tasks live in their source notes. Dashboard files contain only queries.

---

## 2. File Naming Conventions

### 2.1 Date Formats

All dates use **ISO-8601** format.

| Context                   | Format                 | Example                         |
| ------------------------- | ---------------------- | ------------------------------- |
| Frontmatter               | `YYYY-MM-DD`           | `2026-01-03`                    |
| File prefix (notes)       | `YYYY-MM-DD`           | `2026-01-03 - Title.md`         |
| File prefix (emails)      | `YYYY-MM-DD_HHMMSS`    | `2026-01-03_143022_Subject.md`  |
| File prefix (transcripts) | `YYYY-MM-DD HH MM`     | `2026-01-03 14 30 - Meeting.md` |
| Archive folders           | `YYYY-MM-DD`           | `Inbox/_archive/2026-01-03/`    |
| Timestamps in JSON        | ISO-8601 with timezone | `2026-01-03T14:30:00-07:00`     |

### 2.2 File Name Patterns

| File Type        | Pattern                                  | Example                                             |
| ---------------- | ---------------------------------------- | --------------------------------------------------- |
| Historical note  | `YYYY-MM-DD - {Title}.md`                | `2026-01-03 - Weekly 1-1.md`                        |
| Email (source)   | `YYYY-MM-DD_HHMMSS_{NNNN}_{Subject}.eml` | `2026-01-03_143022_4365_RE-Meeting-followup.eml`    |
| Email (markdown) | `YYYY-MM-DD_HHMMSS_{NNNN}_{Subject}.md`  | `2026-01-03_143022_4365_RE-Meeting-followup.md`     |
| Transcript       | `YYYY-MM-DD HH MM - {Title}.md`          | `2026-01-03 14 30 - Google GDC RFP.md`              |
| Extraction JSON  | `{SourceStem}.extraction.json`           | `2026-01-03 14 30 - Google GDC RFP.extraction.json` |
| ChangePlan JSON  | `{SourceStem}.changeplan.json`           | `2026-01-03 14 30 - Google GDC RFP.changeplan.json` |
| Root document    | `README.md`                              | Always this name                                    |
| Template         | `{type}.md.j2`                           | `people.md.j2`, `customer.md.j2`                    |

### 2.3 Character Rules

| Rule                 | Details                                      |
| -------------------- | -------------------------------------------- |
| Allowed characters   | `a-z`, `A-Z`, `0-9`, `-`, `_`, ` `, `.`      |
| Forbidden characters | `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `\|` |
| Spaces               | Allowed in titles, use `-` in slugs          |
| Case                 | Preserve original case (names, titles)       |
| Max length           | 200 characters                               |

### 2.4 Slug Generation

```python
def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')
```

**Examples**:

- `Jeff Denworth` → `jeff-denworth`
- `AI Pipelines Collateral` → `ai-pipelines-collateral`

---

## 3. Frontmatter Schema

### 3.1 Required Fields (All Notes)

```yaml
---
type: "customer|people|projects|rob|journal|partners|travel|task-dashboard"
title: "Human-readable title"
date: "YYYY-MM-DD"
tags:
  - "type/{type}"
  - "{entity_type}/{entity-slug}"
---
```

### 3.2 Automation-Added Fields

Notes created by the automation pipeline include these additional fields:

```yaml
---
source: "transcript|email|manual"
source_ref: "Inbox/_archive/YYYY-MM-DD/{original-filename}"
---
```

The `source_ref` field provides traceability back to the archived original source.

### 3.3 Note-Type Specific Fields

**People Notes**:

```yaml
---
type: "people"
person: "Full Name"
participants: ["Name 1", "Name 2"]
source: "transcript"
source_ref: "Inbox/_archive/2026-01-03/2026-01-03 14 30 - Meeting.md"
---
```

**Customer Notes**:

```yaml
---
type: "customer"
account: "Company Name"
participants: ["Name 1", "Name 2"]
---
```

**Project Notes**:

```yaml
---
type: "projects"
project: "Project Name"
participants: ["Name 1", "Name 2"]
---
```

### 3.4 Root Document Fields

**Person Root** (`README.md`):

```yaml
---
type: "people"
title: "Full Name"
created: "YYYY-MM-DD"
last_contact: "YYYY-MM-DD"
tags:
  - "type/people"
  - "company/{company-slug}" # optional
---
```

**Project Root** (`README.md`):

```yaml
---
type: "projects"
title: "Project Name"
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
status: "active|on-hold|completed|cancelled"
tags:
  - "type/projects"
  - "status/{status}" # optional
---
```

**Account Root** (`README.md`):

```yaml
---
type: "customer"
title: "Company Name"
created: "YYYY-MM-DD"
last_contact: "YYYY-MM-DD"
status: "active|prospect|churned"
tags:
  - "type/customer"
  - "industry/{industry-slug}" # optional
---
```

---

## 4. Tagging Taxonomy

### 4.1 Controlled Tags (Automation-Generated)

| Category  | Pattern                  | Examples                                        |
| --------- | ------------------------ | ----------------------------------------------- |
| Type      | `type/{note-type}`       | `type/people`, `type/customer`, `type/projects` |
| Person    | `person/{name-slug}`     | `person/jeff-denworth`, `person/jason`          |
| Project   | `project/{project-slug}` | `project/ai-pipelines`, `project/greenhouse`    |
| Account   | `account/{account-slug}` | `account/google`, `account/microsoft`           |
| ROB Forum | `rob/{forum-slug}`       | `rob/weekly-standup`, `rob/leadership-sync`     |

### 4.2 Free-Form Tags (Human-Added)

| Category | Pattern     | Examples                                             |
| -------- | ----------- | ---------------------------------------------------- |
| Status   | `status/*`  | `status/urgent`, `status/blocked`, `status/waiting`  |
| Topic    | `topic/*`   | `topic/pricing`, `topic/architecture`, `topic/legal` |
| Action   | `action/*`  | `action/follow-up`, `action/review`, `action/draft`  |
| Context  | `context/*` | `context/confidential`, `context/public`             |

### 4.3 Reserved Tags

| Tag             | Purpose                      | Set By     |
| --------------- | ---------------------------- | ---------- |
| `#task`         | Marks items for Tasks plugin | Automation |
| `#generated`    | Auto-created by pipeline     | Automation |
| `#needs-review` | Flagged for human review     | Automation |
| `#archived`     | Moved to archive             | Automation |

### 4.4 The `#needs-review` Convention

The `#needs-review` tag is used to flag items requiring human attention:

**When applied**:

- Entity match confidence < 0.90
- Task extraction confidence < 0.75
- New entity created with `_NEW_` prefix
- Merge conflict detected
- Uncertain date inference

**How to use**:

```markdown
Search in Obsidian: #needs-review
After resolving: Remove the tag
```

### 4.5 Tag Hygiene Rules

1. **Lowercase only**: All tags must be lowercase
2. **Hyphens for spaces**: Use `multi-word-tag` not `multi_word_tag`
3. **No nested hierarchies**: Use `type/people` not `type/people/work`
4. **Singular nouns**: Use `project/greenhouse` not `projects/greenhouse`
5. **No special characters**: Only `a-z`, `0-9`, `-`, `/`

---

## 5. Wikilink Conventions

### 5.1 Link Targets

| Target   | Pattern                        | Example                                               |
| -------- | ------------------------------ | ----------------------------------------------------- |
| Person   | `[[{Name}]]`                   | `[[Jeff Denworth]]`                                   |
| Project  | `[[{Project}]]`                | `[[AI Pipelines Collateral]]`                         |
| Account  | `[[{Account}]]`                | `[[Google]]`                                          |
| Root doc | `[[{Path}/README\|{Display}]]` | `[[VAST/People/Jeff Denworth/README\|Jeff Denworth]]` |

### 5.2 Link Aliases

Use aliases for cleaner reading:

```markdown
Discussed with [[Jeff Denworth]] about the [[AI Pipelines Collateral|AI collateral]] project.
```

### 5.3 Bidirectional Links

When creating a note about a person, also update that person's root doc:

**In new note**:

```markdown
Met with [[Jeff Denworth]] to discuss...
```

**Patch to person's README.md** (via `append_under_heading` primitive):

```markdown
## Recent Context

- 2026-01-03: Discussed Q1 pipeline priorities
```

---

## 6. Task Format

### 6.1 Obsidian Tasks Plugin Syntax

```markdown
- [ ] Task description @Owner 📅 YYYY-MM-DD 🔺 #task #context-tag
```

### 6.2 Priority Markers

| Marker | Priority | When to Use                    |
| ------ | -------- | ------------------------------ |
| `🔺`   | Highest  | Blocking other work, immediate |
| `⏫`   | High     | Important, this week           |
| `🔼`   | Medium   | Normal priority                |
| `🔽`   | Low      | Nice to have                   |
| `⏬`   | Lowest   | Backlog, someday               |

### 6.3 Date Markers

| Marker | Meaning         | Example         |
| ------ | --------------- | --------------- |
| `📅`   | Due date        | `📅 2026-01-10` |
| `⏳`   | Scheduled date  | `⏳ 2026-01-08` |
| `🛫`   | Start date      | `🛫 2026-01-05` |
| `🔁`   | Recurrence      | `🔁 every week` |
| `✅`   | Completion date | `✅ 2026-01-03` |

### 6.4 Owner Convention

| Owner        | How to Write                | Notes                                    |
| ------------ | --------------------------- | ---------------------------------------- |
| Self         | `@Myself`                   | First-person references from transcripts |
| Named person | `@Jeff` or `@Jeff Denworth` | Short or full name                       |
| Team/Group   | `@Engineering`              | Team assignment                          |
| Unassigned   | (omit owner)                | No `@` marker                            |

### 6.5 Task Examples

```markdown
- [ ] Follow up with Google PM on timeline @Myself 📅 2026-01-06 ⏫ #task
- [ ] Review contract draft @Legal 📅 2026-01-10 🔼 #task #account/google
- [x] Send meeting notes @Myself 📅 2026-01-03 ✅ 2026-01-03 #task
```

---

## 7. Template Conventions

### 7.1 Jinja2 Template Location

All templates live in `Workflow/templates/` with `.md.j2` extension.

### 7.2 Template Variables

| Variable             | Source       | Example Value                     |
| -------------------- | ------------ | --------------------------------- |
| `{{ title }}`        | Extraction   | `"Weekly 1-1"`                    |
| `{{ date }}`         | Extraction   | `"2026-01-03"`                    |
| `{{ person }}`       | Entity match | `"Jeff Denworth"`                 |
| `{{ account }}`      | Entity match | `"Google"`                        |
| `{{ participants }}` | Extraction   | `["Jeff", "Jason"]`               |
| `{{ summary }}`      | Extraction   | `"Discussed Q1..."`               |
| `{{ source_ref }}`   | Archive path | `"Inbox/_archive/2026-01-03/..."` |
| `{{ tasks }}`        | Extraction   | `[{text, owner, due, priority}]`  |
| `{{ decisions }}`    | Extraction   | `["Approved pricing"]`            |
| `{{ tags }}`         | Generated    | `["type/people", "person/jeff"]`  |

### 7.3 Template Example

`Workflow/templates/people.md.j2`:

```jinja
---
type: "people"
title: "{{ title }}"
date: "{{ date }}"
person: "{{ person }}"
participants: {{ participants | tojson }}
source: "transcript"
source_ref: "{{ source_ref }}"
tags:
{% for tag in tags %}
  - "{{ tag }}"
{% endfor %}
---

# {{ title }}

**Date**: {{ date }}
**With**: {{ participants | join(', ') }}

## Summary

{{ summary }}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }} @{{ task.owner }} 📅 {{ task.due }}{% if task.priority == 'highest' %} 🔺{% elif task.priority == 'high' %} ⏫{% endif %} #task
{% endfor %}
{% endif %}

## Notes

{{ notes if notes else '<!-- Add detailed notes here -->' }}

---

*Source*: [[{{ source_ref | basename }}]]
```

---

## 8. Archive Conventions

### 8.1 Archive Location

Processed source files move to:

```
Inbox/_archive/YYYY-MM-DD/{original-filename}
```

### 8.2 Archive Contents

Each archive folder contains:

- Original source files (`.md`, `.eml`)
- Companion extraction JSON (optional, for debugging)

### 8.3 Archive Retention

| Content         | Retention  | Reason                 |
| --------------- | ---------- | ---------------------- |
| Transcripts     | Indefinite | Audit trail            |
| Emails (.eml)   | Indefinite | HTML fidelity recovery |
| Extraction JSON | 30 days    | Debugging only         |
| ChangePlan JSON | 30 days    | Debugging only         |

---

## 9. Git Conventions

### 9.1 Commit Messages

```
[auto] Processed: {file1}, {file2}

- Created: VAST/People/Jeff Denworth/2026-01-03 - Weekly 1-1.md
- Updated: VAST/People/Jeff Denworth/README.md
- Archived: Inbox/Transcripts/2026-01-03 14 30 - Jeff Denworth 1-1.md
```

### 9.2 Ignored Files

`.gitignore` must include:

```
Workflow/.venv/
Workflow/.env
Workflow/logs/*.log
Inbox/_extraction/*.json
.workflow_backups/
```

### 9.3 Branching

| Branch        | Purpose                         |
| ------------- | ------------------------------- |
| `main`        | Production state                |
| (no branches) | Simple linear history preferred |
