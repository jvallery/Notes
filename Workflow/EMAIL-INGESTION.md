# Email Ingestion Pipeline

> **Version**: 2.0  
> **Last Updated**: 2026-01-04  
> **Entry Point**: `Workflow/scripts/process_emails.py`

## Overview

The email ingestion pipeline processes emails from the Inbox through knowledge extraction to draft responses. It's designed to:

1. **Capture knowledge** - Extract contacts, tasks, key facts, topics from emails
2. **Update the vault** - Patch READMEs with extracted information
3. **Provide context** - Gather related vault content for draft generation
4. **Generate drafts** - Create AI-powered response drafts with full context
5. **Archive sources** - Move processed emails to Sources/Email/ for reference

## 6-Step Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Inbox/Email/          →  6-Step Pipeline  →      Sources/Email/         │
│ (Raw imports)                                    (Processed archive)    │
└─────────────────────────────────────────────────────────────────────────┘

  Step 1: DEDUPE     - Remove duplicate exports from same email thread
  Step 2: EXTRACT    - AI extraction of structured data (contacts, tasks, facts)
  Step 3: PATCH      - Update/create vault READMEs with extracted knowledge
  Step 4: GATHER     - Collect related READMEs for context before drafting
  Step 5: DRAFT      - Generate AI response using email + vault context
  Step 6: ARCHIVE    - Move source email to Sources/Email/YYYY/ with links
```

## Usage

```bash
# Activate environment
cd ~/Documents/Notes/Workflow && source .venv/bin/activate

# Run full pipeline
python scripts/process_emails.py

# Run knowledge capture only (phases 1-3)
python scripts/process_emails.py --phase 1-3

# Run response generation only (phases 4-6)
python scripts/process_emails.py --phase 4-6

# Run single phase
python scripts/process_emails.py --phase extract

# Preview without changes
python scripts/process_emails.py --dry-run

# Process only first 5 emails
python scripts/process_emails.py --limit 5

# Skip archiving (keep in Inbox)
python scripts/process_emails.py --skip-archive

# Verbose output
python scripts/process_emails.py -v
```

## Phase Details

### Phase 1: DEDUPE

**Purpose**: Remove duplicate email exports from the same thread.

When you export emails from Apple Mail multiple times, or accidentally drag the same email to the import folder, duplicates are created. This phase identifies and archives them.

**Deduplication logic**:
- Group emails by subject slug (normalized subject line)
- Keep the newest export of each thread
- Archive older duplicates to `Inbox/_archive/dedupe/`

**Output**: Cleaned set of unique emails to process.

---

### Phase 2: EXTRACT

**Purpose**: Extract structured data from emails using AI.

Uses OpenAI to parse each email and extract:
- **Sender/Recipients**: Names, emails, organizations
- **Topics**: Main themes discussed
- **Tasks**: Action items with owners, due dates, priority (initially `- [?] ... #task #proposed #auto`; triage via status to `[ ]` / `/` / `x` / `R`)
- **Key Facts**: Important information to remember
- **Questions**: Items requiring clarification
- **Companies/Projects**: Mentioned entities

**Output**: JSON extraction files in `Inbox/_extraction/`

```
Inbox/_extraction/
├── {email-slug}.email_extraction.json   # Structured extraction
└── {email-slug}.email_changeplan.json   # Planned vault updates
```

**Extraction Schema**:
```python
class EmailExtraction:
    source_file: str
    processed_at: datetime
    email_type: str         # inquiry, follow-up, introduction, etc.
    urgency: str            # low, medium, high, urgent
    
    sender: ContactInfo     # name, email, organization, role
    recipients: List[ContactInfo]
    
    subject: str
    date: str
    summary: str
    
    tasks: List[TaskItem]
    key_facts: List[KeyFact]
    questions: List[str]
    topics: List[str]
    
    people_mentioned: List[str]
    companies_mentioned: List[str]
    projects_mentioned: List[str]
```

---

### Phase 3: PATCH

**Purpose**: Update vault READMEs with extracted knowledge.

For each entity (person, customer, project) mentioned in the email:
1. Find or create the entity's README
2. **Classify new entities** using entity discovery service
3. Apply structured patches:
   - Update frontmatter (last_contact, email address)
   - Append to Recent Context section
   - Add key facts
   - Insert tasks
   - Add wikilinks to related entities

**Entity Discovery & Classification**:

New entities are automatically classified using `entity_discovery.py`:

1. **Quick Classification** - Checks known entity lists (Microsoft, Google, Tesla, etc.)
2. **Heuristic Classification** - Name patterns, suffixes (Inc, LLC, Corp)
3. **AI Classification** - OpenAI for ambiguous cases (with caching)

| Classification | Destination                        | Example           |
| -------------- | ---------------------------------- | ----------------- |
| `person`       | `VAST/People/`                     | John Smith        |
| `company`      | `VAST/Customers and Partners/`     | Tesla, Slice      |
| `project`      | `VAST/Projects/`                   | Cloud Marketplace |

**Entity Creation Rules**:
- **Full names** (2+ words): Always create entity (classified first)
- **Single names with email**: Create with email as index
- **Single names without email**: Skip (can't disambiguate)
- **Known companies**: Quick-route to Customers (no API call)

**Patch Primitives**:
- `upsert_frontmatter`: Update/add YAML frontmatter fields
- `append_under_heading`: Add content under a specific heading
- `ensure_wikilinks`: Add wikilinks to Related section

---

### Phase 4: GATHER

**Purpose**: Collect related READMEs for context before drafting.

For each email, search the vault for:
- **People READMEs**: Sender + any mentioned people
- **Customer READMEs**: Mentioned companies
- **Project READMEs**: Mentioned projects

Reads the README content and formats it as context for the AI draft generator.

**Output**: Aggregated vault context per email.

---

### Phase 5: DRAFT

**Purpose**: Generate AI response drafts with full context.

Uses the gathered vault context + email content to generate intelligent response drafts:
1. Analyze email to determine if response is needed
2. If yes, combine email + vault context
3. Generate draft response in my voice/style
4. Save to `Outbox/Drafts/`

**Response determination**:
- Skip: No-reply senders, newsletters, auto-replies
- Skip: FYI-only emails, meeting invites
- Draft: Questions addressed to me, action requests, follow-ups needed

**Draft Output**:
```
Outbox/Drafts/{date}-draft-{subject-slug}.md

---
original_email: "Inbox/Email/{source}.md"
to: ["recipient@example.com"]
subject: "Re: Original Subject"
generated_at: "2026-01-04T10:00:00"
vault_context_used: ["VAST/People/John Doe/README.md", ...]
---

# Draft Response

{AI-generated response body}

---
## Source Context

### Vault Context
{Formatted README excerpts}

### Original Email
{Full email content}
```

---

### Phase 6: ARCHIVE

**Purpose**: Move processed emails to Sources/Email/ for reference.

After all processing is complete:
1. Move email from `Inbox/Email/` to `Sources/Email/YYYY/`
2. Update extraction JSON with new `source_file` path
3. Maintain links between vault READMEs and archived source

**Archive Structure**:
```
Sources/
└── Email/
    ├── 2024/
    ├── 2025/
    └── 2026/
        └── 2026-01-04_130424_1550_RE-Subject.md
```

## Entity Indexing

### Email Address as Primary Key

When available, email addresses are used as a stable identifier:

1. **On extraction**: Capture email addresses for all contacts
2. **On person lookup**: Search both folder names and frontmatter `email:` field
3. **On creation**: Store email in README frontmatter

```yaml
---
type: people
title: "John Doe"
email: "john.doe@company.com"
---
```

### Single-Name Handling

The pipeline allows single-name records when:
- The email address is available (can be used as index)
- The context is clear (e.g., sender of an email)

Single-name records without email are skipped to prevent ambiguity.

### Multi-Email Disambiguation

When a person has multiple email addresses:
- All addresses should be listed in frontmatter as array
- Search checks all listed addresses
- Manual review may be needed for matching

```yaml
---
email:
  - "john.doe@company.com"
  - "jdoe@personal.com"
---
```

## Artifacts

### Extraction JSON

```json
{
  "source_file": "Inbox/Email/2026-01-04_130424_1550_Subject.md",
  "processed_at": "2026-01-04T10:30:00Z",
  "email_type": "follow-up",
  "urgency": "medium",
  "sender": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "organization": "Acme Corp",
    "role": "VP Engineering"
  },
  "summary": "Follow-up on pricing discussion from last week...",
  "tasks": [
    {
      "text": "Send revised pricing proposal",
      "owner": "Myself",
      "priority": "high",
      "due_date": "2026-01-10"
    }
  ],
  "key_facts": [
    {
      "fact": "Budget approved for Q1",
      "category": "business"
    }
  ],
  "topics": ["pricing", "q1-planning", "partnership"]
}
```

### ChangePlan JSON

```json
{
  "source_file": "Inbox/Email/2026-01-04_130424_1550_Subject.md",
  "created_at": "2026-01-04T10:30:00Z",
  "patches": [
    {
      "target_path": "VAST/People/John Doe/README.md",
      "operation": "patch",
      "patches": [
        {
          "primitive": "upsert_frontmatter",
          "frontmatter": [
            {"key": "last_contact", "value": "2026-01-04"},
            {"key": "email", "value": "john.doe@example.com"}
          ]
        },
        {
          "primitive": "append_under_heading",
          "heading": "## Recent Context",
          "content": "- 2026-01-04: Follow-up on pricing..."
        }
      ]
    }
  ],
  "entities_to_create": [],
  "warnings": []
}
```

## Error Handling

### Extraction Failures

If extraction fails for an email:
- Error is logged with details
- Email remains in Inbox for retry
- Other emails continue processing

### Patch Failures

If patching fails for an entity:
- Warning is logged
- Email is still processed for other entities
- Failed patch can be manually applied

### Missing Entities

When an entity folder doesn't exist:
- New README is created from template
- Tagged with `#needs-review`
- Linked to source email

## Best Practices

1. **Run regularly**: Process emails daily to keep vault current
2. **Review new entities**: Check `#needs-review` tagged items
3. **Verify drafts**: Always review AI-generated drafts before sending
4. **Check extraction quality**: Spot-check extraction JSON for accuracy
5. **Merge duplicates**: If same person created under multiple names, merge manually

## Task Triage Workflow

AI-extracted tasks use **Proposed** status (`[?]`) and require triage before becoming actionable. This prevents auto-generated tasks from cluttering your real work.

### Task Format

```markdown
- [?] Follow up with Google on timeline @Myself 📅 2026-01-10 🔺 #task #proposed #auto
```

| Element | Meaning |
|---------|---------|
| `[?]` | Proposed status — needs triage |
| `@Owner` | Person responsible (Myself = you) |
| `📅 YYYY-MM-DD` | Due date |
| `🔺⏫🔼🔽⏬` | Priority (highest → lowest) |
| `#task` | Makes it visible in dashboards |
| `#proposed` | Marks as needing acceptance |
| `#auto` | AI-generated (not manual) |

### Triage in Obsidian

Open `TASKS.md` to see the **Proposed** section at the top. For each task:

| Action | How | Result |
|--------|-----|--------|
| **Accept** | Click checkbox → choose `Not Started` (`[ ]`) | Moves to "Not Started" section |
| **Start** | Click checkbox → choose `In Progress` (`/`) | Moves to "In Progress" section |
| **Complete** | Click checkbox → choose `Done` (`x`) | Task disappears from dashboard |
| **Reject** | Click checkbox → choose `Cancelled` (`R`) | Task hidden from all views |

### Status Lifecycle

```
[?] Proposed   →   [ ] Not Started   →   [/] In Progress   →   [x] Done
      ↓
     [R] Rejected (hidden)
```

### Quick Capture

For manual tasks, add directly to `TASKS_INBOX.md`:

```markdown
- [?] Quick task idea @Myself #task #proposed #inbox ⏫ 📅 2026-01-15
```

The `#inbox` tag keeps these separate until you move them to the right note.

### Dashboard Sections

| Section | Query | Contents |
|---------|-------|----------|
| Proposed | `status.name includes Proposed` | AI-generated + quick capture |
| Not Started | `status.name includes Not Started` | Accepted, not yet started |
| In Progress | `status.name includes In Progress` | Currently working on |
| Inbox | `path includes TASKS_INBOX.md` | Quick captures only |
| Backlog | `path includes TASKS_BACKLOG.md` | Legacy task list |

## Troubleshooting

### No emails processing

```bash
# Check for emails in inbox
ls -la ~/Documents/Notes/Inbox/Email/

# Check for existing extractions
ls -la ~/Documents/Notes/Inbox/_extraction/
```

### Extraction errors

```bash
# Run with verbose output
python scripts/process_emails.py -v --phase extract

# Check specific email
cat ~/Documents/Notes/Inbox/Email/{email}.md
```

### Draft not generated

Drafts are only created when the AI determines a response is needed. Check:
- Is sender a no-reply address?
- Is it a newsletter or auto-reply?
- Is it FYI-only content?

## Related Documentation

- [DESIGN.md](DESIGN.md) - System architecture
- [STANDARDS.md](STANDARDS.md) - File and folder conventions
- [REQUIREMENTS.md](REQUIREMENTS.md) - Full requirements
