# Backfill Design: Processing Historical Content

> **Version**: 1.0.0  
> **Created**: 2026-01-03  
> **Last Updated**: 2026-01-04  
> **Status**: Implemented  
> **Related**: [REFACTOR.md](REFACTOR.md) | [DESIGN.md](DESIGN.md)

## 1. Problem Statement

The current migration (Phase 8) only creates **structural compliance**:

- Creates missing README.md files
- Fixes frontmatter issues
- Uses empty templates

But it does NOT:

- Read existing notes content
- Extract summaries, tasks, facts
- Populate "Recent Context" sections
- Handle multi-entity content

**Goal**: Process ALL historical content to populate entity README.md files with rich context.

---

## 2. Scope

| Source            | Count | Action                                   |
| ----------------- | ----- | ---------------------------------------- |
| VAST notes        | ~164  | Extract → update entity READMEs          |
| Personal notes    | ~26   | Extract → update entity READMEs          |
| Inbox/Transcripts | 6     | Normal pipeline (extract → create notes) |
| Inbox/Email       | 7     | Normal pipeline (extract → create notes) |

**Key distinction**:

- **Inbox items** → Create NEW dated notes via normal pipeline
- **Existing notes** → Extract context → UPDATE README.md only (no new files)

---

## 3. Multi-Entity Challenge

### The Problem

A single transcript may involve multiple entities:

```markdown
# 2025-11-14 - VAST + Google GDC Alignment

**Attendees**: Jeff Denworth, Sarah from Google, Karl Vietmeier

Discussed:

- GDC integration roadmap
- Jeff's concerns about timeline
- Karl's technical requirements
```

This should update:

1. `VAST/Customers and Partners/Google/README.md` → Recent Context
2. `VAST/People/Jeff Denworth/README.md` → Recent Context
3. `VAST/People/Karl Vietmeier/README.md` → Recent Context

### Current Behavior (Implemented)

Multi-entity attribution is supported end-to-end:

- Normal pipeline: planner prompt (`prompts/system-planner.md.j2`) generates PATCH ops for relevant mentioned entities.
- Backfill: aggregation (`scripts/backfill/aggregator.py`) uses extracted `mentions` to update multiple READMEs per note.

### Proposed Solution

Extraction already captures `mentions`:

```json
{
  "mentions": {
    "people": ["Jeff Denworth", "Karl Vietmeier", "Sarah"],
    "projects": ["GDC Integration"],
    "accounts": ["Google"]
  }
}
```

**New behavior**: Planner generates PATCH operations for ALL mentioned entities:

```json
{
  "operations": [
    // Primary: Create note in main entity folder
    { "op": "create", "path": "VAST/Customers and Partners/Google/2025-11-14 - GDC Alignment.md" },

    // Primary: Update main entity README
    { "op": "patch", "path": "VAST/Customers and Partners/Google/README.md", ... },

    // Secondary: Update mentioned people READMEs
    { "op": "patch", "path": "VAST/People/Jeff Denworth/README.md",
      "patches": [
        { "primitive": "upsert_frontmatter", "frontmatter": [{"key": "last_contact", "value": "2025-11-14"}] },
        { "primitive": "append_under_heading", "heading": "## Recent Context",
          "content": "- 2025-11-14: [[2025-11-14 - GDC Alignment]] (via Google)\n" }
      ]
    },
    { "op": "patch", "path": "VAST/People/Karl Vietmeier/README.md", ... }
  ]
}
```

---

## 4. Architecture

### 4.1 Backfill vs. Normal Pipeline

```
                    ┌─────────────────────────────────────────────────┐
                    │                  BACKFILL MODE                   │
                    │         (for existing notes in folders)          │
                    └────────────────────┬────────────────────────────┘
                                         │
    ┌────────────────────────────────────┼────────────────────────────────────┐
    │                                    │                                    │
    ▼                                    ▼                                    ▼
┌───────────┐                     ┌────────────┐                       ┌────────────┐
│   SCAN    │                     │  EXTRACT   │                       │   APPLY    │
│           │                     │            │                       │            │
│ Find all  │                     │ For each   │                       │ Patch all  │
│ notes in  │──────────────────▶  │ note, get  │─────────────────────▶ │ READMEs    │
│ entity    │                     │ summary +  │                       │ atomically │
│ folders   │                     │ mentions   │                       │            │
└───────────┘                     └────────────┘                       └────────────┘
                                         │
                                         │ Uses AI: gpt-4o-mini
                                         │ (lightweight extraction)
                                         │
                                         ▼
                              ┌────────────────────┐
                              │  For each mention  │
                              │  generate PATCH op │
                              │  for that README   │
                              └────────────────────┘
```

### 4.2 Backfill Extraction (Lightweight)

Since we're processing existing notes (not raw transcripts), we use a **simpler extraction**:

```python
class BackfillExtraction(BaseModel):
    """Lightweight extraction for existing notes."""
    date: str                           # From frontmatter or filename
    title: str                          # From frontmatter or H1
    summary: str                         # 1-2 sentence summary
    mentions: dict[str, list[str]]      # people, projects, accounts
    key_facts: list[str]                # Top 3 facts
    has_tasks: bool                     # Are there tasks in this note?
```

**API call**: `gpt-4o-mini` with `store=False`, ~500 tokens per note

- 164 notes × 500 tokens = 82K input tokens
- Estimated cost: ~$0.04

### 4.3 Aggregation Logic

For each entity README, aggregate ALL related notes:

```python
def aggregate_for_entity(entity_path: str, extractions: list[BackfillExtraction]) -> ReadmeUpdate:
    """
    Aggregate extractions mentioning this entity.

    Returns structured update for README.md
    """
    # Filter extractions that mention this entity
    relevant = [e for e in extractions if entity_mentioned_in(e, entity_path)]

    # Sort by date descending
    relevant.sort(key=lambda e: e.date, reverse=True)

    # Build Recent Context section
    recent_context = []
    for ext in relevant[:10]:  # Last 10 interactions
        line = f"- {ext.date}: [[{ext.title}]]"
        if ext.summary:
            line += f" - {ext.summary[:100]}"
        recent_context.append(line)

    # Determine last_contact
    last_contact = relevant[0].date if relevant else None

    return ReadmeUpdate(
        path=f"{entity_path}/README.md",
        last_contact=last_contact,
        recent_context="\n".join(recent_context),
        interaction_count=len(relevant)
    )
```

---

## 5. Implementation Plan

### Phase 8A: Structural Migration (DONE)

- ✅ Create missing README.md with empty template
- ✅ Fix frontmatter compliance

### Phase 8B: Backfill (NEW)

**Step 8B.1: Backfill Scanner**

```bash
python scripts/backfill.py scan --scope "VAST" --output backfill-manifest.json
```

Output:

```json
{
  "entities": [
    {
      "path": "VAST/People/Jeff Denworth",
      "readme_exists": true,
      "notes": [
        { "path": "2025-11-14 - GDC Alignment.md", "date": "2025-11-14" },
        { "path": "2025-10-30 - Weekly 1-1.md", "date": "2025-10-30" }
      ]
    }
  ],
  "total_notes": 164,
  "total_entities": 53
}
```

**Step 8B.2: Backfill Extractor**

```bash
python scripts/backfill.py extract --manifest backfill-manifest.json --output extractions/
```

For each note, calls gpt-4o-mini to get:

- Summary (1-2 sentences)
- Mentions (people, projects, accounts)
- Key facts

Output: `extractions/{note-hash}.json`

**Step 8B.3: Backfill Aggregator**

```bash
python scripts/backfill.py aggregate --extractions extractions/ --output backfill-plan.json
```

For each entity README:

- Collect all notes mentioning this entity
- Build "Recent Context" section
- Calculate `last_contact` date
- Generate PATCH operations

**Step 8B.4: Backfill Apply**

```bash
python scripts/backfill.py apply --plan backfill-plan.json --dry-run
python scripts/backfill.py apply --plan backfill-plan.json
```

Uses TransactionalApply pattern:

- Backup all READMEs
- Apply all patches atomically
- Git commit on success
- Rollback on failure

---

## 6. Handling Edge Cases

### 6.1 Note Without Clear Entity

Some notes might not have clear entity ownership:

```
VAST/Projects/Cloud/Available Capacity Calculations.md
```

**Solution**:

- Still extract summary
- Update project README only
- Skip if no mentions

### 6.2 Duplicate Content

Same content might appear in multiple note versions:

```
VAST/Projects/Cloud/2025-10-29 - Team aligned on positioning...
VAST/ROB/VAST on Cloud Office Hours/2025-10-29 - Team aligned...
```

**Solution**:

- Hash content to detect duplicates
- Flag for review if >90% similar
- Process primary only

### 6.3 Notes Without Dates

Some notes don't have dates:

```
VAST/Projects/Pricing/Pricing.md
```

**Solution**:

- Use file modification time as fallback
- Flag with `#needs-date` tag
- Place at end of Recent Context

### 6.4 Orphan Notes

Notes in folders that don't match entity patterns:

```
VAST/Projects/OVA/docs/archive/VAST_Lessons_Learned.md
```

**Solution**:

- Extract but don't update READMEs
- Log for manual review
- Consider as "documentation" not "interactions"

---

## 7. Prompt + Structured Output

- **Prompt**: `prompts/backfill-extractor.md.j2`
- **Structured output model**: `scripts/backfill/__init__.py` → `BackfillExtractionLite`

Example output shape:

```json
{
  "summary": "1-2 sentence summary",
  "suggested_title": "Optional improved title",
  "note_type": "meeting|1-1|project|call|email|...",
  "mentions": {
    "people": ["Name1"],
    "projects": ["Project1"],
    "accounts": ["Company1"]
  },
  "key_facts": ["Fact 1", "Fact 2"],
  "topics_discussed": ["Topic 1", "Topic 2"],
  "tasks": [{"text": "Action item", "owner": "Myself", "due": "YYYY-MM-DD"}],
  "decisions": ["Decision 1"]
}
```

---

## 8. Testing Strategy

### Unit Tests

| Test | Purpose |
|------|---------|
| `test_backfill_scanner` | Finds all notes in entity folders |
| `test_backfill_extractor` | Extracts summary + mentions |
| `test_multi_entity_aggregation` | One note updates multiple READMEs |
| `test_duplicate_detection` | Detects similar content |
| `test_date_inference` | Handles missing dates |

### Integration Tests

| Test | Purpose |
|------|---------|
| `test_backfill_dry_run` | Full pipeline without writes |
| `test_backfill_apply` | Actual README updates |
| `test_backfill_idempotent` | Running twice = same result |

### Manual Verification

```bash
# 1. Run on small scope first
python scripts/backfill.py run --scope "VAST/People/Jeff Denworth" --dry-run

# 2. Check generated Recent Context looks right
cat VAST/People/Jeff\ Denworth/README.md

# 3. Run on full scope
python scripts/backfill.py run --scope "VAST" --dry-run
```

---

## 9. CLI Interface

```bash
# Full backfill pipeline
python scripts/backfill.py run --scope "VAST" --dry-run

# Individual phases (defaults write to Inbox/_extraction/backfill-*.json)
python scripts/backfill.py scan --scope "VAST"
python scripts/backfill.py extract --manifest ../Inbox/_extraction/backfill-manifest.json --limit 100 --verbose
python scripts/backfill.py aggregate --extractions ../Inbox/_extraction/backfill-extractions.json
python scripts/backfill.py apply --plan ../Inbox/_extraction/backfill-plan.json --dry-run

# Utilities
python scripts/backfill.py sync-manifests
python scripts/backfill.py rename --extractions ../Inbox/_extraction/backfill-extractions.json --dry-run
python scripts/backfill.py merge --propose

# Options (see --help per command)
--dry-run         # Preview changes without writing
--verbose         # Detailed output (varies by command)
--limit N         # Limit number of notes/entities processed
--workers N       # Parallel extraction workers (run/enrich)
--no-auto-create  # Disable auto-creation of new entity folders (run)
```

---

## 10. Estimated Effort

| Component               | Effort        | Notes                    |
| ----------------------- | ------------- | ------------------------ |
| Backfill scanner        | 2 hours       | Reuse migration scanner  |
| Backfill extractor      | 3 hours       | New prompt, API calls    |
| Multi-entity aggregator | 3 hours       | Core logic               |
| Apply with patches      | 2 hours       | Reuse TransactionalApply |
| Testing                 | 3 hours       | Unit + integration       |
| **Total**               | **~13 hours** |                          |

---

## 11. Execution Order

1. **Complete structural migration first** (Phase 8A)
   - All READMEs exist with valid frontmatter
2. **Run backfill on small scope**
   - Test with 1-2 entity folders
   - Verify README content looks right
3. **Run backfill on full vault**

   - Process all 164+ notes
   - Generate comprehensive Recent Context

4. **Process Inbox items** (normal pipeline)
   - 6 transcripts + 7 emails
   - These create NEW dated notes

---

## 12. Success Criteria

- [ ] Every entity README has populated "Recent Context"
- [ ] `last_contact` dates are accurate
- [ ] Multi-entity notes update ALL relevant READMEs
- [ ] No duplicate entries in Recent Context
- [ ] Backfill is idempotent (safe to re-run)
- [ ] Full process completes in <10 minutes
