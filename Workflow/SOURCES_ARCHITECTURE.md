# Sources Architecture: Single Source of Truth Design

> **Status**: Design Document  
> **Created**: 2026-01-03  
> **Purpose**: Eliminate content duplication, enable bidirectional linking

## Problem Statement

Currently, source materials (transcripts, emails, documents) are either:

1. Duplicated across multiple entity folders
2. Archived to `Inbox/_archive/` where they're not discoverable
3. Lost when the original transcript path no longer exists

READMEs contain inline text summaries rather than links to sources, making it impossible to navigate back to the original context.

## Core Principle

**Every piece of source material is stored exactly once and cross-linked to all relevant entities.**

```
Source Document (stored once)
    ↓ contains frontmatter links to
Entity READMEs (context ledgers)
    ↓ contain wikilinks back to
Source Document
```

## Folder Structure

```
Notes/
├── Sources/                              # PRIMARY SOURCE ARCHIVE
│   ├── Transcripts/
│   │   ├── 2024/
│   │   ├── 2025/
│   │   │   ├── 2025-09-16 - Lior Genzel Intro Call.md
│   │   │   ├── 2025-10-28 - Google GCP Kickoff.md
│   │   │   └── ...
│   │   └── 2026/
│   │
│   ├── Email/
│   │   ├── 2025/
│   │   │   └── 2025-12-11 - Microsoft Ignite Follow-up.md
│   │   └── 2026/
│   │
│   └── Documents/                        # Collateral, PDFs, attachments
│       ├── 2025/
│       └── 2026/
│
├── VAST/
│   ├── People/{Name}/
│   │   └── README.md                     # Context ledger only
│   ├── Customers and Partners/{Account}/
│   │   └── README.md
│   └── Projects/{Project}/
│       └── README.md
│
└── Inbox/                                # LANDING ZONE (unchanged)
    ├── Transcripts/                      # Raw input
    ├── Email/
    ├── Attachments/
    └── _extraction/                      # Processing artifacts
```

## Source Document Format

Each source document has rich frontmatter with entity wikilinks:

```yaml
---
type: transcript                          # transcript | email | document
title: "Lior Genzel Intro Call"
date: 2025-09-16

# Source metadata
source_type: macwhisper                   # macwhisper | teams | email | manual
duration: 45m
original_filename: "20250916 1100 Teams Meeting.txt"

# Bidirectional entity links (Obsidian wikilinks)
participants:
  - "[[Lior Genzel]]"
  - "[[Jason Vallery]]"

entities:
  people:
    - "[[Lior Genzel]]"
    - "[[Jay Parikh]]"
  customers:
    - "[[Microsoft]]"
  projects:
    - "[[VAST on Azure Integration]]"

# Processing metadata
processed: 2025-09-16
tags:
  - source/transcript
  - year/2025
---

## Summary

Intro call exploring roles for Jason at VAST. Lior outlined three potential
homes (Jay's model builders GTM, Lior's hyperscalers/Azure GTM, or CTO Office)...

## Key Points

- Jason has ~13 years at Microsoft Azure Storage
- VAST signed Microsoft Lifter
- Cloud GA plan: GCP (October), AWS (December), Azure (February)

## Tasks

- [x] Initiate candidate process for Jason @HR ✅ 2025-10-26
- [x] Set up interviews with founders @Lior Genzel ✅ 2025-10-26

## Decisions

- Proceed with interviews for Jason at VAST
- Focus on Azure GTM/business side initially

---

## Original Transcript

[Full transcript content preserved below]

Speaker 1: Hi Jason, thanks for making time...
```

## README Format (Context Ledger)

READMEs become indexes with one-line entries linking to sources:

```markdown
## Recent Context

| Date       | Source                                                                       | Summary                                          |
| ---------- | ---------------------------------------------------------------------------- | ------------------------------------------------ |
| 2025-11-14 | [[Sources/Transcripts/2025/2025-11-14 - Google GDC RFP Discussion\|GDC RFP]] | Aligned on RFP response, compliance requirements |
| 2025-11-07 | [[Sources/Transcripts/2025/2025-11-07 - Jeff Denworth 1-1\|Weekly 1:1]]      | Reviewed org landscape, cloud priorities         |
| 2025-10-31 | [[Sources/Email/2025/2025-10-31 - Azure Pricing Update\|Email]]              | Pricing tier approved                            |
```

Or simpler bullet format:

```markdown
## Recent Context

- 2025-11-14: [[Sources/Transcripts/2025/2025-11-14 - Google GDC RFP Discussion|GDC RFP Discussion]] — Aligned on RFP response strategy
- 2025-11-07: [[Sources/Transcripts/2025/2025-11-07 - Jeff Denworth 1-1|Weekly 1:1]] — Org landscape review
```

## Ingest Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│  1. CAPTURE                                                             │
│     File lands in Inbox/{Transcripts,Email,Attachments}/                │
│     Naming: YYYY-MM-DD HH MM - {Title}.md (transcripts)                 │
│             YYYY-MM-DD_HHMMSS_{Subject}.md (email)                      │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  2. EXTRACT (AI)                                                        │
│     Input: Raw source content                                           │
│     Output: extraction.json with:                                       │
│       - date, title, summary                                            │
│       - entities (people, customers, projects)                          │
│       - tasks, decisions, key_facts                                     │
│       - suggested_title for filename                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  3. ENRICH SOURCE                                                       │
│     - Inject frontmatter with entity wikilinks                          │
│     - Prepend AI-generated summary section                              │
│     - Preserve original content in "## Original" section                │
│     - Rename file to: YYYY-MM-DD - {Suggested Title}.md                 │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  4. MOVE TO SOURCES                                                     │
│     Move: Inbox/Transcripts/file.md → Sources/Transcripts/YYYY/         │
│     (File is now in permanent home with rich metadata)                  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  5. UPDATE ENTITY READMEs                                               │
│     For each entity in extraction.entities:                             │
│       - Append one-line context entry with [[wikilink]] to source       │
│       - Update last_contact date in frontmatter                         │
│       - Auto-create entity folder/README if new                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## Migration Plan

### Phase 1: Create Structure

```bash
mkdir -p Sources/Transcripts/{2024,2025,2026}
mkdir -p Sources/Email/{2024,2025,2026}
mkdir -p Sources/Documents/{2024,2025,2026}
```

### Phase 2: Migrate Existing Dated Notes

Move 123 dated notes from entity folders to Sources:

```python
# For each dated note in VAST/People/*/2025-*.md:
#   1. Parse frontmatter and content
#   2. Add entity wikilinks to frontmatter
#   3. Move to Sources/Transcripts/YYYY/
#   4. Update README Recent Context with wikilink
```

### Phase 3: Process New Inbox Items

Apply new flow to 6 pending transcripts in `Inbox/Transcripts/`.

### Phase 4: Update README Template

Change Recent Context from inline summaries to wikilinks.

## Benefits

| Before                                      | After                                     |
| ------------------------------------------- | ----------------------------------------- |
| Summary text duplicated in N entity READMEs | Source stored once, linked N times        |
| No way to find original transcript          | Wikilink goes directly to source          |
| Entity folders cluttered with dated notes   | Entity folders contain only README.md     |
| Obsidian graph shows no connections         | Graph shows entity ↔ source relationships |
| Hard to see "all meetings with Person X"    | Backlinks on source show all entities     |

## Implementation Files

```
Workflow/
├── scripts/
│   ├── ingest.py                 # NEW: Main ingest pipeline
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── extractor.py          # AI extraction (existing)
│   │   ├── enricher.py           # NEW: Inject frontmatter + summary
│   │   ├── archiver.py           # NEW: Move to Sources/
│   │   └── linker.py             # NEW: Update entity READMEs
│   └── migrate/
│       └── consolidate_sources.py # NEW: One-time migration
│
└── templates/
    ├── source-transcript.md.j2    # NEW: Source document template
    ├── source-email.md.j2         # NEW
    └── readme-context-entry.md.j2 # NEW: One-liner for README
```

## Commands

```bash
# Process new inbox items
python scripts/ingest.py run

# Migrate existing dated notes to Sources
python scripts/migrate/consolidate_sources.py --dry-run
python scripts/migrate/consolidate_sources.py --execute

# Check source coverage
python scripts/ingest.py status
```
