# PROMPTS & TEMPLATES REVIEW BUNDLE

> **Generated**: 2026-01-03 (Updated with multi-entity support)
> **Purpose**: External review of all AI prompts and Jinja2 templates before running migration/backfill
> **Files Included**: 4 prompts + 8 templates + 4 profiles + 2 schemas

---

## TABLE OF CONTENTS

1. [Prompts](#prompts)
   - [base.md.j2](#promptsbasemdj2) - Universal rules
   - [system-extractor.md.j2](#promptssystem-extractormdj2) - Content extraction (transcripts/emails)
   - [system-planner.md.j2](#promptssystem-plannermdj2) - ChangePlan generation (UPDATED: multi-entity)
   - [backfill-extractor.md.j2](#promptsbackfill-extractormdj2) - Lightweight extraction for existing notes
2. [Templates](#templates)
   - [people.md.j2](#templatespeoplemdj2) - 1:1 meeting notes
   - [customer.md.j2](#templatescustomermdj2) - Customer meeting notes
   - [partners.md.j2](#templatespartnersmdj2) - Partner meeting notes
   - [projects.md.j2](#templatesprojectsmdj2) - Project meeting notes
   - [rob.md.j2](#templatesrobmdj2) - Rhythm of Business notes
   - [journal.md.j2](#templatesjournalmdj2) - Journal entries
   - [travel.md.j2](#templatestravelmdj2) - Travel notes
   - [readme-migration.md.j2](#templatesreadme-migrationmdj2) - Entity README
3. [Profiles](#profiles)
   - [work_sales.yaml](#profileswork_salesyaml) - Sales/customer extraction rubrics
   - [work_engineering.yaml](#profileswork_engineeringyaml) - Engineering extraction rubrics
   - [work_leadership.yaml](#profileswork_leadershipyaml) - Leadership extraction rubrics
   - [personal.yaml](#profilespersonalyaml) - Personal extraction rubrics
4. [Schemas](#schemas)
   - [extraction.schema.json](#schemasextractionschemajon) - Extraction output schema
   - [changeplan.schema.json](#schemaschangeplanschemajon) - ChangePlan output schema

---

# PROMPTS

---

## prompts/base.md.j2

```jinja
{# Base Prompt Layer - Universal Rules #}
{# Include this in all extraction/planning prompts #}

## Output Format

You MUST return valid JSON only. No markdown fences, no explanations outside the JSON structure.

## Date Standards

- All dates must be **ISO-8601 format**: `YYYY-MM-DD`
- Today's date is: {{ current_date }}
- Resolve relative dates:
  - "tomorrow" → {{ tomorrow }}
  - "next week" → {{ next_week }}
  - "next Monday" → calculate from {{ current_date }}
  - "end of month" → last day of current month
  - If ambiguous, use the next occurrence

## Task Extraction Rules

- Task owners: Use `"Myself"` for first-person references ("I will", "I need to", "my action")
- Use actual names for third-party assignments
- Extract due dates when mentioned; omit if not specified
- Priority mapping:
  - "urgent", "critical", "ASAP" → `"highest"`
  - "important", "priority" → `"high"`
  - "normal", unspecified → `"medium"`
  - "low priority", "when possible" → `"low"`
  - "backlog", "someday" → `"lowest"`

## Entity Linking

Known entities in the vault:
{{ known_entities | tojson(indent=2) }}

When extracting mentions, match against known entities when possible.
For new/unknown entities, include them but mark confidence as lower.

## Deduplication

- Do NOT duplicate items across `tasks`, `follow_ups`, and `decisions`
- If something is a task, it goes in `tasks` only
- Decisions are conclusions reached, not actions to take
```

---

## prompts/system-extractor.md.j2

````jinja
{# System Prompt: Content Extraction #}
{# Assembles: Base Layer + Profile Layer + Extraction Instructions #}

{% include 'base.md.j2' %}

## Extraction Context

**Profile**: {{ profile_name }}
**Description**: {{ profile_description }}

### Focus Areas

When extracting information, prioritize:
{% for focus in profile_focus %}
- {{ focus }}
{% endfor %}

### Content to De-emphasize

{% for ignore in profile_ignore %}
- {{ ignore }}
{% endfor %}

### Task Extraction Rules

{{ task_rules.owner_inference }}

**Due Date Inference**:
{{ task_rules.due_date_inference }}

**Confidence Threshold**: Only extract tasks with confidence ≥ {{ task_rules.confidence_threshold }}

## Content Classification

Based on the content, determine the most appropriate note type:
- **people**: 1-on-1 meetings, personal relationship notes
- **customer**: Multi-party account meetings with external customers
- **partners**: Partner organization meetings
- **projects**: Project work, sprint planning, technical discussions
- **rob**: Rhythm of Business forums (recurring team syncs)
- **journal**: Personal reflections, daily notes

## Required Output Schema

You MUST return valid JSON matching this exact structure:

```json
{
  "note_type": "people|customer|partners|projects|rob|journal",
  "entity_name": "string - Primary entity (person name, account name, project name, etc.)",
  "title": "string - Brief descriptive title (3-7 words)",
  "date": "YYYY-MM-DD - Date of the meeting/content",
  "participants": ["array of participant names"],
  "summary": "string - 2-3 sentence summary of key points",
  "tasks": [
    {
      "text": "string - The action item",
      "owner": "string - Person responsible (use 'Myself' for first-person)",
      "due": "YYYY-MM-DD or null if not specified",
      "priority": "highest|high|medium|low|lowest",
      "confidence": 0.0-1.0
    }
  ],
  "decisions": ["array of decisions made"],
  "facts": ["array of key facts or context to remember"],
  "mentions": {
    "people": ["names of people mentioned"],
    "projects": ["projects referenced"],
    "accounts": ["companies/accounts referenced"]
  },
  "confidence": 0.0-1.0,
  "warnings": ["any concerns or ambiguities"]
}
````

## Content to Extract From

**Source**: {{ source_file }}
**Content Type**: {{ content_type | default('meeting transcript') }}

---

{{ content }}

````

---

## prompts/system-planner.md.j2

> **⚠️ UPDATED**: Now includes multi-entity support - one extraction updates ALL mentioned entity READMEs

```jinja
{# System Prompt: ChangePlan Generation #}
{# Generates structured operations for vault updates #}

{% include 'base.md.j2' %}

## Planning Task

You are generating a **ChangePlan** - a structured list of file operations to update the Obsidian vault based on extracted content.

**CRITICAL**: You generate ONLY semantic operations (`create`, `patch`, `link`). Archive operations are handled deterministically by Python code AFTER your plan executes successfully. Do NOT generate archive operations.

## Vault Context

### Entity Folders
{{ entity_folders | tojson(indent=2) }}

### Entity Aliases
{{ aliases | tojson(indent=2) }}

## Operation Types

### 1. `create` - Create a new dated note

Creates a new file from a template.

```json
{
  "op": "create",
  "path": "VAST/People/Jeff Denworth/2026-01-03 - Weekly 1-1.md",
  "template": "people.md.j2",
  "context": {
    "title": "Weekly 1-1",
    "date": "2026-01-03",
    "person": "Jeff Denworth",
    "participants": ["Jeff Denworth", "Jason"],
    "summary": "...",
    "tasks": [...],
    "decisions": [...],
    "facts": [...],
    "source": "transcript",
    "source_ref": "Inbox/_archive/2026-01-03/original.md"
  }
}
````

Available templates: `people.md.j2`, `customer.md.j2`, `partners.md.j2`, `projects.md.j2`, `rob.md.j2`, `journal.md.j2`

### 2. `patch` - Update an existing file

Uses structured patch primitives (NOT regex):

```json
{
  "op": "patch",
  "path": "VAST/People/Jeff Denworth/README.md",
  "patches": [
    {
      "primitive": "upsert_frontmatter",
      "frontmatter": [{ "key": "last_contact", "value": "2026-01-03" }]
    },
    {
      "primitive": "append_under_heading",
      "heading": "## Recent Context",
      "content": "- 2026-01-03: Discussed Q1 pipeline and priorities\n"
    }
  ]
}
```

Patch primitives:

- `upsert_frontmatter`: Add/update YAML frontmatter fields
- `append_under_heading`: Append text under a markdown heading
- `ensure_wikilinks`: Ensure wikilinks exist in the file

### 3. `link` - Add wikilinks to a file

```json
{
  "op": "link",
  "path": "VAST/People/Jeff Denworth/2026-01-03 - Weekly 1-1.md",
  "links": ["[[Google]]", "[[AI Pipeline Project]]"]
}
```

## Required Workflow

For each extraction, you MUST generate:

1. **CREATE** a dated note in the appropriate entity folder

   - Path format: `{EntityFolder}/{YYYY-MM-DD} - {Title}.md`
   - Template must match note_type (e.g., `people.md.j2` for note_type="people")
   - **CRITICAL: The `context` object MUST include ALL these fields from the extraction**:
     - `title`: Use extraction.title
     - `date`: Use extraction.date
     - `person`/`account`/`project`: Use extraction.entity_name based on note_type
     - `participants`: Use extraction.participants
     - `summary`: Use extraction.summary
     - `tasks`: Use extraction.tasks (array of task objects)
     - `decisions`: Use extraction.decisions
     - `facts`: Use extraction.facts
     - `source`: "transcript" or "email"
     - `source_ref`: Construct from source_file path
   - **DO NOT leave context empty - copy data from the extraction!**

2. **PATCH** the PRIMARY entity's README.md (if it exists)

   - Update `last_contact` frontmatter field to extraction.date
   - Append summary to `## Recent Context`

3. **PATCH** ALL MENTIONED entity READMEs (CRITICAL - multi-entity support)

   - For EACH person in `extraction.mentions.people`:
     - If they have a folder in vault context, generate a PATCH operation
     - Update their README.md with `last_contact` and a cross-reference line
   - For EACH project in `extraction.mentions.projects`:
     - Same: patch their README if folder exists
   - For EACH account in `extraction.mentions.accounts`:
     - Same: patch their README if folder exists
   - The cross-reference format: `- {date}: [[{note title}]] (via {primary entity})`

4. **LINK** mentioned entities as wikilinks in the new note
   - Link people, projects, and accounts from extraction.mentions

**Example multi-entity output**:
If a customer meeting with Google mentions Jeff Denworth and Karl:

```json
{
  "operations": [
    {"op": "create", "path": "VAST/Customers and Partners/Google/2026-01-03 - GDC Alignment.md", ...},
    {"op": "patch", "path": "VAST/Customers and Partners/Google/README.md", ...},
    {"op": "patch", "path": "VAST/People/Jeff Denworth/README.md",
     "patches": [
       {"primitive": "upsert_frontmatter", "frontmatter": [{"key": "last_contact", "value": "2026-01-03"}]},
       {"primitive": "append_under_heading", "heading": "## Recent Context",
        "content": "- 2026-01-03: [[2026-01-03 - GDC Alignment]] (via Google)\n"}
     ]},
    {"op": "patch", "path": "VAST/People/Karl Vietmeier/README.md", ...},
    {"op": "link", "path": "VAST/Customers and Partners/Google/2026-01-03 - GDC Alignment.md", ...}
  ]
}
```

## Output Schema

```json
{
  "version": "1.0",
  "source_file": "path to original source file",
  "extraction_file": "path to extraction JSON",
  "created_at": "ISO-8601 timestamp",
  "operations": [
    { "op": "create|patch|link", ... }
  ],
  "warnings": ["any concerns or issues to flag for human review"]
}
```

## Entity Resolution

- Match extracted `entity_name` to existing folders in vault context
- If no match found, create path with `_NEW_` prefix and add warning
- Use aliases to resolve alternate names to canonical folders

## Extraction Data

{{ extraction | tojson(indent=2) }}

````

---

## prompts/backfill-extractor.md.j2

> **NEW**: Lightweight extraction for populating READMEs from existing notes

```jinja
{# System Prompt: Backfill Extraction #}
{# Lightweight extraction for existing notes - metadata only #}

## Task

You are extracting structured metadata from an existing note for indexing purposes. This is NOT for creating new content - we just need to understand what this note contains so we can update entity README files.

## Output Format

Return valid JSON only. No markdown fences, no explanations.

## Required Output

```json
{
  "summary": "1-2 sentence summary of what this note is about",
  "mentions": {
    "people": ["Full Name 1", "Full Name 2"],
    "projects": ["Project Name"],
    "accounts": ["Company/Account Name"]
  },
  "key_facts": [
    "Important fact 1",
    "Important fact 2",
    "Important fact 3"
  ]
}
````

## Guidelines

### Summary

- Be concise: 1-2 sentences max
- Focus on the outcome or topic, not the process
- Example: "Aligned on GDC integration timeline with Google team. Agreed to share encryption architecture doc."

### Mentions

- **people**: Full names of individuals mentioned (not "the team" or "everyone")
- **projects**: Named initiatives, products, or workstreams
- **accounts**: Companies, customers, or partner organizations
- Only include entities explicitly mentioned, not inferred

### Key Facts

- Up to 3 most important facts worth remembering
- Prioritize: decisions, commitments, deadlines, status changes
- Skip: obvious context, meeting logistics, pleasantries

## Note Context

**Path**: {{ note_path }}
**Date**: {{ note_date | default('Unknown') }}
**Entity**: {{ entity_name | default('Unknown') }}

## Note Content

{{ content }}

````

---

# TEMPLATES

---

## templates/people.md.j2

```jinja
---
type: "people"
title: "{{ title }}"
date: "{{ date }}"
person: "{{ person }}"
participants: {{ participants | tojson }}
source: "{{ source | default('transcript') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/people"
  - "person/{{ person | slugify }}"
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}
**With**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
````

---

## templates/customer.md.j2

```jinja
---
type: "customer"
title: "{{ title }}"
date: "{{ date }}"
account: "{{ account }}"
participants: {{ participants | tojson }}
source: "{{ source | default('transcript') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/customer"
  - "account/{{ account | slugify }}"
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}
**Account**: [[{{ account }}]]
**Attendees**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
```

---

## templates/partners.md.j2

```jinja
---
type: "partners"
title: "{{ title }}"
date: "{{ date }}"
partner: "{{ partner }}"
participants: {{ participants | tojson }}
source: "{{ source | default('transcript') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/partners"
  - "partner/{{ partner | slugify }}"
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}
**Partner**: [[{{ partner }}]]
**Attendees**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
```

---

## templates/projects.md.j2

```jinja
---
type: "projects"
title: "{{ title }}"
date: "{{ date }}"
project: "{{ project }}"
participants: {{ participants | tojson }}
source: "{{ source | default('transcript') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/projects"
  - "project/{{ project | slugify }}"
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}
**Project**: [[{{ project }}]]
**Attendees**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
```

---

## templates/rob.md.j2

```jinja
---
type: "rob"
title: "{{ title }}"
date: "{{ date }}"
rob_forum: "{{ rob_forum }}"
participants: {{ participants | tojson }}
source: "{{ source | default('transcript') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/rob"
  - "rob/{{ rob_forum | slugify }}"
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}
**Forum**: [[{{ rob_forum }}]]
**Attendees**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
```

---

## templates/journal.md.j2

```jinja
---
type: "journal"
title: "{{ title }}"
date: "{{ date }}"
source: "{{ source | default('manual') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/journal"
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Key Information

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}
{% if source_ref %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
{% endif %}
```

---

## templates/travel.md.j2

```jinja
---
type: "travel"
title: "{{ title }}"
date: "{{ date }}"
{% if destination is defined and destination %}
destination: "{{ destination }}"
{% endif %}
participants: {{ participants | tojson }}
source: "{{ source | default('transcript') }}"
source_ref: "{{ source_ref | default('') }}"
tags:
  - "type/travel"
{% if destination is defined and destination %}
  - "destination/{{ destination | slugify }}"
{% endif %}
  - "generated"
{% if extra_tags is defined and extra_tags %}
{% for tag in extra_tags %}
  - "{{ tag }}"
{% endfor %}
{% endif %}
---

# {{ title }}

**Date**: {{ date }}
{% if destination is defined and destination %}
**Destination**: {{ destination }}
{% endif %}
**Travelers**: {{ participants | join(", ") }}

## Summary

{{ summary }}

{% if tasks %}
## Action Items

{% for task in tasks %}
- [ ] {{ task.text }}{% if task.owner %} @{{ task.owner }}{% endif %}{% if task.due %} 📅 {{ task.due }}{% endif %}{% if task.priority == "high" %} ⏫{% elif task.priority == "highest" %} 🔺{% elif task.priority == "low" %} 🔽{% elif task.priority == "lowest" %} ⏬{% endif %} #task
{% endfor %}
{% endif %}

{% if decisions %}
## Decisions

{% for decision in decisions %}
- {{ decision }}
{% endfor %}
{% endif %}

{% if facts %}
## Logistics & Details

{% for fact in facts %}
- {{ fact }}
{% endfor %}
{% endif %}

---

*Source: [[{{ source_ref | basename | strip_extension }}]]*
```

---

## templates/readme-migration.md.j2

````jinja
---
type: "readme"
title: "{{ entity_name }}"
entity_type: "{{ entity_type }}"
created: "{{ created_date }}"
last_contact: "{{ last_contact | default('') }}"
tags:
  - "type/{{ entity_type }}"
  - "{{ entity_type }}/{{ entity_name | slugify }}"
---

# {{ entity_name }}

{% if entity_type == "people" %}
## Contact Information

<!-- Add contact details here -->

{% elif entity_type == "accounts" %}
## Account Overview

<!-- Add account context here -->

{% elif entity_type == "projects" %}
## Project Overview

<!-- Add project description here -->

{% endif %}
## Recent Context

{% if recent_context %}
{% for item in recent_context %}
- {{ item.date }}: {{ item.summary }}
{% endfor %}
{% else %}
<!-- Recent interactions will be added here -->
{% endif %}

## Active Tasks

```dataview
TASK
FROM "{{ folder_path }}"
WHERE !completed
SORT due ASC
````

## Notes

```dataview
TABLE date as "Date", title as "Title"
FROM "{{ folder_path }}"
WHERE type != "readme"
SORT date DESC
LIMIT 10
```

````

---

# PROFILES

---

## profiles/work_sales.yaml

```yaml
# Profile: Sales/Customer Context
# For customer and partner meetings, deal discussions, pipeline reviews

name: "Sales/Customer Context"
description: "For customer and partner meetings with revenue-focused outcomes"

# What to prioritize during extraction
focus:
  - Deal status and stage changes
  - Blockers and objections raised
  - Competitive mentions (products, vendors)
  - Next steps and explicit commitments
  - Budget and timeline signals
  - Decision makers and influencers identified
  - Pain points and requirements expressed
  - Pricing discussions and proposals
  - Contract and legal topics

# What to de-emphasize or skip
ignore:
  - Small talk and pleasantries
  - Deep technical implementation details (summarize at high level)
  - Internal process discussions not relevant to deal
  - Off-topic tangents

# Rules for task extraction
task_rules:
  # Only extract tasks with this confidence or higher
  confidence_threshold: 0.75

  # How to infer task owner from speaker context
  owner_inference: |
    If the speaker (user) commits to an action, owner is "Myself".
    If a named participant commits, use their first name.
    If ownership is ambiguous, use "TBD".

  # How to calculate due dates from relative references
  due_date_inference: |
    Anchor all relative dates to the meeting date.
    "tomorrow" = meeting_date + 1 day
    "next week" = meeting_date + 7 days
    "end of week" = next Friday from meeting_date
    "next month" = first of next month
    If no date mentioned, leave due_date empty.

# Rules for entity matching
entity_matching:
  # Auto-create new entity folder if confidence >= this threshold
  auto_create_threshold: 0.90

  # Flag for human review if confidence between these thresholds
  needs_review_threshold: 0.80

  # Prefer these entity types for ambiguous matches
  preferred_types:
    - account
    - partner
    - person

# Note type hints based on context
type_hints:
  # If these patterns appear, suggest these note types
  patterns:
    - pattern: "1-1|one-on-one|1:1"
      suggests: "people"
    - pattern: "RFP|proposal|deal|pipeline"
      suggests: "customer"
    - pattern: "partner|alliance|integration"
      suggests: "partners"

# Extraction behavior
extraction:
  # Include quotes for key statements
  include_quotes: true
  quote_threshold: 0.85  # Only include high-confidence quotes

  # Max items per section
  max_tasks: 10
  max_decisions: 5
  max_facts: 10
````

---

## profiles/work_engineering.yaml

```yaml
# Profile: Engineering/Technical Context
# For technical discussions, architecture reviews, project work

name: "Engineering/Technical Context"
description: "For technical discussions, code reviews, architecture, and project work"

# What to prioritize during extraction
focus:
  - Technical decisions and rationale
  - Architecture choices and trade-offs
  - API design and interface contracts
  - Performance considerations and benchmarks
  - Security and compliance requirements
  - Integration points and dependencies
  - Bug reports and issue resolution
  - Code review feedback and action items
  - Documentation needs
  - Testing strategy and coverage

# What to de-emphasize or skip
ignore:
  - Off-topic personal discussions
  - Scheduling logistics
  - Administrative topics not related to technical work
  - Repeated explanations of known concepts

# Rules for task extraction
task_rules:
  confidence_threshold: 0.70 # Lower threshold for technical tasks

  owner_inference: |
    If the speaker commits to implementation, owner is "Myself".
    If a specific engineer is assigned, use their name.
    For team tasks, use "Team" as owner.
    If ownership unclear, use "TBD".

  due_date_inference: |
    Anchor to meeting date.
    "by EOD" = meeting_date
    "tomorrow" = meeting_date + 1 day
    "next sprint" = meeting_date + 14 days
    "next release" = next Friday from meeting_date
    If no date, leave empty.

# Rules for entity matching
entity_matching:
  auto_create_threshold: 0.85
  needs_review_threshold: 0.70

  preferred_types:
    - project
    - person

# Note type hints
type_hints:
  patterns:
    - pattern: "sprint|backlog|standup|retro"
      suggests: "projects"
    - pattern: "1-1|sync|check-in"
      suggests: "people"
    - pattern: "architecture|design|review"
      suggests: "projects"

# Extraction behavior
extraction:
  include_quotes: true
  quote_threshold: 0.80

  # Include code references if mentioned
  include_code_refs: true

  max_tasks: 15 # More tasks typical in technical discussions
  max_decisions: 10
  max_facts: 15
```

---

## profiles/work_leadership.yaml

```yaml
# Profile: Leadership/Strategy Context
# For ROB forums, planning sessions, all-hands, executive discussions

name: "Leadership/Strategy Context"
description: "For ROB forums, strategic planning, all-hands, and executive discussions"

# What to prioritize during extraction
focus:
  - Strategic decisions and direction changes
  - Organizational announcements
  - Priority shifts and resource allocation
  - Cross-team dependencies and coordination
  - Metrics and KPI discussions
  - Quarterly/annual planning items
  - Headcount and hiring plans
  - Process changes and new initiatives
  - Escalations and blockers requiring leadership attention
  - Recognition and team highlights

# What to de-emphasize or skip
ignore:
  - Detailed technical implementation
  - Individual task-level items (capture at summary level)
  - Scheduling details
  - Administrative logistics

# Rules for task extraction
task_rules:
  confidence_threshold: 0.80 # Higher bar for leadership tasks

  owner_inference: |
    If a leader commits to action, use their name.
    If speaker commits, owner is "Myself".
    For org-wide actions, use "Leadership" or team name.
    If delegated to a team, use team name.

  due_date_inference: |
    Anchor to meeting date.
    "by EOQ" = end of current quarter
    "next week" = meeting_date + 7 days
    "next quarter" = first of next quarter
    "by EOY" = December 31 of current year
    If no date, leave empty.

# Rules for entity matching
entity_matching:
  auto_create_threshold: 0.90
  needs_review_threshold: 0.85

  preferred_types:
    - rob_forum
    - person
    - project

# Note type hints
type_hints:
  patterns:
    - pattern: "office hours|sync|standup|weekly"
      suggests: "rob"
    - pattern: "1-1|one-on-one"
      suggests: "people"
    - pattern: "all-hands|town hall|QBR"
      suggests: "rob"
    - pattern: "planning|roadmap|strategy"
      suggests: "projects"

# Extraction behavior
extraction:
  include_quotes: true
  quote_threshold: 0.90 # Only highest confidence quotes

  # Capture metrics mentioned
  include_metrics: true

  max_tasks: 8 # Fewer but higher-impact tasks
  max_decisions: 10
  max_facts: 10
```

---

## profiles/personal.yaml

```yaml
# Profile: Personal Context
# For personal notes, journal entries, non-work content

name: "Personal Context"
description: "For personal notes, journal entries, home projects, and non-work content"

# What to prioritize during extraction
focus:
  - Personal goals and commitments
  - Health and wellness notes
  - Family and relationship items
  - Home projects and tasks
  - Personal learning and development
  - Travel and event planning
  - Financial and administrative items
  - Creative projects and hobbies
  - Reflections and insights

# What to de-emphasize or skip
ignore:
  - Work-related content (route to work profiles)
  - Sensitive personal information (minimize extraction)
  - Detailed financial figures

# Rules for task extraction
task_rules:
  confidence_threshold: 0.65 # Lower threshold for personal reminders

  owner_inference: |
    Default owner is "Myself" for personal tasks.
    If involving family member, use their first name.
    For shared tasks, use "Us" or "Family".

  due_date_inference: |
    Anchor to meeting/note date.
    "tomorrow" = date + 1 day
    "this weekend" = next Saturday
    "next week" = date + 7 days
    If no date, leave empty.

# Rules for entity matching
entity_matching:
  auto_create_threshold: 0.85
  needs_review_threshold: 0.75

  preferred_types:
    - person
    - project

# Note type hints
type_hints:
  patterns:
    - pattern: "journal|reflect|thoughts"
      suggests: "journal"
    - pattern: "project|build|create"
      suggests: "projects"
    - pattern: "trip|travel|vacation"
      suggests: "travel"
    - pattern: "meet|coffee|dinner|call with"
      suggests: "people"

# Extraction behavior
extraction:
  include_quotes: false # Less formal for personal

  # Be more lenient with structure
  allow_freeform: true

  max_tasks: 10
  max_decisions: 5
  max_facts: 10
```

---

# SCHEMAS

---

## schemas/extraction.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "extraction.schema.json",
  "title": "Extraction Output",
  "description": "Structured data extracted from transcripts/emails",
  "type": "object",
  "required": ["source_file", "processed_at", "classification", "extraction"],
  "properties": {
    "source_file": {
      "type": "string",
      "description": "Path to original source file"
    },
    "processed_at": {
      "type": "string",
      "format": "date-time",
      "description": "ISO-8601 timestamp of extraction"
    },
    "classification": {
      "type": "object",
      "required": ["note_type"],
      "properties": {
        "note_type": {
          "type": "string",
          "enum": [
            "customer",
            "people",
            "projects",
            "rob",
            "journal",
            "partners",
            "travel"
          ]
        },
        "entity_name": {
          "type": "string",
          "description": "Primary entity (person, project, account)"
        },
        "confidence": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "sub_type": {
          "type": "string",
          "description": "Optional sub-classification (e.g., technical, leadership)"
        }
      }
    },
    "extraction": {
      "type": "object",
      "required": ["title", "date", "participants"],
      "properties": {
        "title": {
          "type": "string",
          "description": "Generated note title"
        },
        "date": {
          "type": "string",
          "format": "date",
          "description": "Meeting/email date (YYYY-MM-DD)"
        },
        "participants": {
          "type": "array",
          "items": { "type": "string" },
          "description": "List of people involved"
        },
        "summary": {
          "type": "string",
          "description": "Brief summary of content"
        },
        "tasks": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["text"],
            "properties": {
              "text": { "type": "string" },
              "owner": { "type": "string", "default": "Myself" },
              "due": { "type": "string", "format": "date" },
              "priority": {
                "type": "string",
                "enum": ["highest", "high", "medium", "low", "lowest"]
              }
            }
          }
        },
        "decisions": {
          "type": "array",
          "items": { "type": "string" }
        },
        "facts": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Key facts or context to remember"
        },
        "mentions": {
          "type": "object",
          "properties": {
            "people": { "type": "array", "items": { "type": "string" } },
            "projects": { "type": "array", "items": { "type": "string" } },
            "accounts": { "type": "array", "items": { "type": "string" } }
          }
        },
        "notes": {
          "type": "string",
          "description": "Additional notes or raw content"
        }
      }
    }
  }
}
```

---

## schemas/changeplan.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "changeplan.schema.json",
  "title": "ChangePlan",
  "description": "Schema for deterministic file operations",
  "type": "object",
  "required": ["version", "source", "operations"],
  "properties": {
    "version": {
      "const": "1.0",
      "description": "Schema version"
    },
    "source": {
      "type": "object",
      "required": ["file", "extraction", "processed_at"],
      "properties": {
        "file": {
          "type": "string",
          "description": "Original source file path"
        },
        "extraction": {
          "type": "string",
          "description": "Path to extraction JSON"
        },
        "processed_at": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "operations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["op", "path"],
        "properties": {
          "op": {
            "type": "string",
            "enum": ["create", "append", "patch", "link", "archive"],
            "description": "Operation type"
          },
          "path": {
            "type": "string",
            "description": "Target file path (relative to vault root)"
          },
          "template": {
            "type": "string",
            "description": "Jinja2 template name (for create)"
          },
          "context": {
            "type": "object",
            "description": "Template variables (for create)"
          },
          "content": {
            "type": "string",
            "description": "Raw content (for append)"
          },
          "patches": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "section": {
                  "type": "string",
                  "description": "YAML key or ## heading to target"
                },
                "find": {
                  "type": ["string", "null"],
                  "description": "Regex pattern to find (null = append to section)"
                },
                "replace": {
                  "type": "string",
                  "description": "Replacement text"
                }
              },
              "required": ["replace"]
            },
            "description": "Patch operations (for patch)"
          },
          "links": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Wikilinks to insert (for link)"
          },
          "destination": {
            "type": "string",
            "description": "Archive destination folder (for archive)"
          }
        }
      }
    },
    "validation": {
      "type": "object",
      "properties": {
        "schema_valid": {
          "type": "boolean"
        },
        "conflicts": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Files with potential conflicts"
        },
        "warnings": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Non-blocking issues"
        }
      }
    }
  }
}
```

---

# REVIEW CHECKLIST

## Key Questions for External Review

### Prompts (LLM Guidance)

1. **Clarity**: Is the expected output format crystal clear?
2. **Completeness**: Are all edge cases addressed (empty meetings, no tasks, etc.)?
3. **Constraints**: Are there enough guardrails to prevent hallucination?
4. **Examples**: Would adding more concrete examples improve extraction quality?
5. **Deduplication**: Is the logic for separating tasks/decisions/facts clear enough?
6. **Multi-entity**: Is the new multi-entity update logic in system-planner clear?

### Templates (Output Rendering)

1. **Frontmatter**: Are all required fields present for each note type?
2. **Consistency**: Do all templates follow the same structural pattern?
3. **Dataview Queries**: Are the README queries correct for each entity type?
4. **Wikilinks**: Is the `[[entity]]` linking correct in all templates?
5. **Source Attribution**: Is the source linking consistent?

### Profiles (Extraction Rubrics)

1. **Coverage**: Do the 4 profiles cover all likely meeting types?
2. **Thresholds**: Are confidence thresholds appropriate for each context?
3. **Type Hints**: Are the regex patterns for note type classification accurate?
4. **Owner Inference**: Is the task owner logic clear and consistent?

### Schemas (Validation)

1. **Required Fields**: Are the mandatory fields correct?
2. **Enums**: Do the allowed values match actual usage?
3. **Extensibility**: Is there room for future additions?

---

## Known Gaps / Issues to Address

1. **New Entity Creation**: Currently, if a person is extracted who doesn't exist, the planner uses `_NEW_` prefix. Consider tiered approach based on confidence thresholds from profiles.

2. **`travel` type**: Not included in the main extraction type hints - may need profile/detection rules.

3. **Missing `slugify` filter**: The templates reference `| slugify` but this is a custom Jinja filter - need to verify it's registered.

4. **`source_ref` format**: Templates expect a path but use `| basename | strip_extension` - verify these custom filters exist.

5. **Empty arrays**: Templates use `{% if tasks %}` guards but should also handle `tasks: []` vs `tasks: null`.

6. **Multi-entity deduplication**: If someone is both the primary entity AND in mentions, avoid duplicate patches.

7. **Cross-reference format**: The new `(via {entity})` format needs testing to ensure it renders correctly.

---

_End of Review Bundle_
