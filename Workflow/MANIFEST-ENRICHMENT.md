# Manifest & Enrichment System

> **Version**: 1.0  
> **Last Updated**: 2026-01-04  
> **Entry Points**: `manifest_sync.py`, `enrich_person.py`

## Overview

This system maintains glossary manifests for People, Projects, and Customers, and provides AI-powered enrichment to fill in missing information from public sources.

### Key Goals

1. **Prompt Caching** — Stable glossary prefix for OpenAI cost reduction (up to 90%)
2. **Entity Resolution** — Help AI correctly identify people, companies, projects
3. **Knowledge Enrichment** — Automatically gather public information about contacts
4. **Bidirectional Sync** — READMEs and manifests stay in sync

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            MANIFEST SYSTEM                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐    scan     ┌──────────────┐    format    ┌───────────┐ │
│   │ Entity       │ ─────────►  │ Manifest     │ ──────────►  │ Glossary  │ │
│   │ READMEs      │             │ _MANIFEST.md │              │ Cache     │ │
│   │              │  ◄───────── │              │              │ .json     │ │
│   └──────────────┘    patch    └──────────────┘              └───────────┘ │
│         │                              │                            │       │
│         └──────────────────────────────┴────────────────────────────┘       │
│                                        │                                     │
│                                   enrich                                     │
│                                        ▼                                     │
│                              ┌──────────────────┐                           │
│                              │ OpenAI API       │                           │
│                              │ (Search + LLM)   │                           │
│                              └──────────────────┘                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Prompt Caching

### How It Works

OpenAI automatically caches prompt prefixes that are:
- **1024+ tokens** (minimum threshold)
- **Static content first** (glossary + persona)
- **Dynamic content last** (task-specific instructions)

Our implementation:
1. Glossary (~1600 tokens) + Persona (~500 tokens) = ~2100 tokens ✅
2. These are placed at the START of every system prompt
3. Cache persists 5-10 min (in-memory) or up to 24 hours (extended)
4. **90% cost reduction** on cached input tokens

### Scripts Using Cached Prompts

| Script | Purpose | Uses Glossary |
|--------|---------|---------------|
| `extract.py` | Transcript extraction | ✅ Compact |
| `plan.py` | ChangePlan generation | ✅ Compact |
| `ingest_emails.py` | Email extraction | ✅ Compact |
| `draft_responses.py` | Email drafting | ✅ Full |
| `entity_discovery.py` | Entity classification | ✅ Compact |

### Verifying Cache Hits

Check `usage.prompt_tokens_details.cached_tokens` in API responses:
```python
response = client.chat.completions.create(...)
cached = response.usage.prompt_tokens_details.cached_tokens
print(f"Cached: {cached} / {response.usage.prompt_tokens} tokens")
```

---

## Manifests

### Location & Format

| Manifest | Path | Columns |
|----------|------|---------|
| People | `VAST/People/_MANIFEST.md` | Name, Role, Company, Email, Context |
| Projects | `VAST/Projects/_MANIFEST.md` | Name, Owner, Status, Description |
| Customers | `VAST/Customers and Partners/_MANIFEST.md` | Name, Type, Industry, Context |

### Sync Flow

```
README.md (source of truth)
    │
    ▼ scan_*_folder()
    │
Manifest _MANIFEST.md (derived)
    │
    ▼ build_glossary_cache()
    │
Glossary cache (Workflow/_cache/glossary.json)
```

### CLI Commands

```bash
cd ~/Documents/Notes/Workflow && source .venv/bin/activate

# Scan and report status
python scripts/manifest_sync.py scan

# Update manifests from READMEs
python scripts/manifest_sync.py sync

# AI-enrich sparse entries (from README content)
python scripts/manifest_sync.py enrich --limit 20

# Rebuild glossary cache
python scripts/manifest_sync.py build-cache
```

---

## Enrichment System

### Enrichment Levels

Enrichment happens in stages, each adding more information:

| Level | Source | Data Added | Trigger |
|-------|--------|------------|---------|
| **L0: Stub** | Folder name only | Name | Auto on folder creation |
| **L1: Contact** | Email extraction | Email, phone, company | Email ingestion |
| **L2: README** | AI from README | Role, company, context | `enrich --from-readme` |
| **L3: Web** | OpenAI web search | Bio, LinkedIn, background | `enrich --web` |
| **L4: Deep** | Multi-source research | Full profile | `enrich --deep` |

### What We Can Extract (by level)

#### L1: Contact Info (from emails)
- Email address
- Phone number
- Job title (from signature)
- Company (from signature/domain)

#### L2: README Context (AI inference)
- Role/title
- Company affiliation
- Relationship context (how we know them)
- Areas of expertise

#### L3: Web Enrichment (OpenAI Search)
- LinkedIn URL and profile summary
- Current role and company (verified)
- Professional background
- Public bio/about
- Company website
- Notable achievements/publications

#### L4: Deep Research
- Full career history
- Mutual connections
- Recent news/mentions
- Company details (size, industry, funding)
- Social media presence

### Data Model

```yaml
# Person README frontmatter (enriched)
---
type: people
title: "John Smith"
created: "2026-01-04"
last_contact: "2026-01-04"
last_enriched: "2026-01-04"  # NEW: Track enrichment date
enrichment_level: 3           # NEW: L0-L4 level achieved

# Contact (L1)
email: "john@company.com"
phone: "+1-555-123-4567"

# Profile (L2+)
role: "VP of Engineering"
company: "TechCorp"
linkedin: "https://linkedin.com/in/johnsmith"

# Web enrichment (L3)
bio: "20-year veteran of cloud infrastructure..."
location: "San Francisco, CA"
previous_roles:
  - title: "Director of Engineering"
    company: "PrevCorp"
    years: "2018-2022"

tags:
  - type/people
  - company/techcorp
  - needs-review
---
```

### Triggering Enrichment

#### Manual CLI

```bash
# Enrich from README content (L2) - uses existing README text
python scripts/enrich_person.py "John Smith" --from-readme

# Enrich from web (L3) - uses OpenAI search
python scripts/enrich_person.py "John Smith" --web

# Deep enrichment (L4) - full research
python scripts/enrich_person.py "John Smith" --deep

# Enrich all sparse entries (batch)
python scripts/enrich_person.py --all --level 2 --limit 20

# Enrich specific company's contacts
python scripts/enrich_person.py --company "Microsoft" --level 3
```

#### Agent Prompt

When asking an AI agent to run enrichment:

```
Run person enrichment for [Person Name] at level [2/3/4].

Commands:
- Level 2 (from README): python scripts/enrich_person.py "John Smith" --from-readme
- Level 3 (web search): python scripts/enrich_person.py "John Smith" --web  
- Level 4 (deep): python scripts/enrich_person.py "John Smith" --deep

For batch enrichment of all sparse entries:
python scripts/enrich_person.py --all --level 3 --limit 20
```

#### Automatic Triggers

| Event | Enrichment Triggered |
|-------|---------------------|
| New person folder created | L0 (stub) |
| Email processed with contact | L1 (contact info patched) |
| `manifest_sync.py enrich` | L2 (from README) |
| Manual `--web` request | L3 (web search) |

---

## Bidirectional Sync

### README → Manifest

When a README is updated:
1. Run `manifest_sync.py sync` to regenerate manifest from READMEs
2. Run `manifest_sync.py build-cache` to update glossary

### Manifest Updates

When enrichment adds new data:
1. **Patch README** — Update frontmatter with new fields
2. **Update manifest row** — Regenerate manifest entry
3. **Rebuild cache** — Update glossary for future prompts

### Patch-to-Manifest Hook

During email ingestion (`ingest_emails.py`), when patching a person's README:

```python
# After applying patches to README...
if "frontmatter" in patch and any(k in frontmatter_updates 
    for k in ["role", "company", "email", "title"]):
    # Trigger manifest sync for this person
    sync_person_to_manifest(person_name, frontmatter_updates)
```

---

## Web Enrichment Details

### OpenAI Search API

For L3 enrichment, we use OpenAI's web search capability:

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": ENRICHMENT_PROMPT},
        {"role": "user", "content": f"Research: {name} at {company}"}
    ],
    tools=[{"type": "web_search_preview"}],  # Enable web search
    tool_choice="auto"
)
```

### Search Strategy

For best results, we search with context:
1. **With company**: `"John Smith" "TechCorp" linkedin OR about`
2. **With email domain**: `"John Smith" site:techcorp.com`
3. **Role verification**: `"VP Engineering" "TechCorp" "John Smith"`

### Rate Limiting

- Max 10 web searches per minute (API limit)
- Cache results for 30 days in `Workflow/_cache/web_enrichment/`
- Skip enrichment if cached data is fresh

---

## Files Reference

| File | Purpose |
|------|---------|
| `manifest_sync.py` | Manifest scan/sync/enrich/cache CLI |
| `enrich_person.py` | Person enrichment CLI (to be created) |
| `cached_prompts.py` | Glossary loading for prompt caching |
| `_MANIFEST.md` | Per-folder manifest tables |
| `_cache/glossary.json` | Combined glossary cache |
| `_cache/web_enrichment/` | Web search result cache |

---

## Maintenance

### Daily
- Manifests auto-update after email processing (PATCH phase)
- Glossary cache rebuilt when patches applied

### Weekly
- Run `manifest_sync.py scan` to check sparse entry count
- Run `manifest_sync.py enrich --limit 50` for batch L2 enrichment

### Monthly
- Review `#needs-review` tagged entities
- Run L3 web enrichment on key contacts
- Audit and merge duplicate entities

---

## Troubleshooting

### Manifest out of sync
```bash
python scripts/manifest_sync.py sync
python scripts/manifest_sync.py build-cache
```

### Enrichment not working
1. Check `OPENAI_API_KEY` is set
2. Check rate limits haven't been hit
3. Review logs in `Workflow/logs/`

### Cache stale
```bash
rm Workflow/_cache/glossary.json
python scripts/manifest_sync.py build-cache
```
