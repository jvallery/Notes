# Manifest & Enrichment System

> **Version**: 1.1  
> **Last Updated**: 2026-01-05  
> **Entry Points**: `scripts/manifest_sync.py`, `scripts/enrich_person.py`, `scripts/enrich_customer.py`

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
| `scripts/ingest.py` (pipeline/extract) | Unified ingest (email/transcript/document/voice) | ✅ Compact |
| `pipeline/extract.py` | Core extractor (used by ingest CLI) | ✅ Compact |
| `scripts/draft_responses.py` | Email drafting | ✅ Full |
| `scripts/entity_discovery.py` | Entity classification | ✅ Compact |

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
| People | `VAST/People/_MANIFEST.md` | Name, Role, Company, Email, My Relationship, Context |
| Projects | `VAST/Projects/_MANIFEST.md` | Name, Owner, My Role, Status, Description |
| Customers | `VAST/Customers and Partners/_MANIFEST.md` | Name, Type, Stage, Industry, My Role, Last Contact, Context |

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

# Scan and report status (shows sparse counts)
python scripts/manifest_sync.py scan --verbose

# Update manifests from READMEs
python scripts/manifest_sync.py sync

# AI-enrich sparse entries from README content
python scripts/manifest_sync.py enrich --entity people --limit 20
python scripts/manifest_sync.py enrich --entity customers --limit 20

# Customer enrichment helper (per-account or batch)
python scripts/enrich_customer.py "Microsoft" --from-readme
python scripts/enrich_customer.py --all --limit 20

# Rebuild glossary cache (persona + manifests)
python scripts/manifest_sync.py build-cache
```

---

## Enrichment System

### Enrichment Levels

**People**

| Level | Source | Data Added | Trigger |
|-------|--------|------------|---------|
| **L0: Stub** | Folder name only | Name | Auto on folder creation |
| **L1: Contact** | Email extraction | Email, phone, company | Ingest pipeline |
| **L2: README** | AI from README | Role, company, context | `enrich_person.py --from-readme` or `manifest_sync.py enrich --entity people` |
| **L3: Web** | OpenAI web search | Bio, LinkedIn, background | `enrich_person.py --web` |
| **L4: Deep** | Multi-source research | Full profile | `enrich_person.py --deep` |

**Customers / Partners**

| Level | Source | Data Added | Trigger |
|-------|--------|------------|---------|
| **L0: Stub** | Folder name only | Name | Auto on folder creation |
| **L1: Contact** | Frontmatter/tags | Account type, status, industry (if present) | Ingest/patch |
| **L2: README** | AI from README | Type, Stage, Industry, My Role, Last Contact, context | `manifest_sync.py enrich --entity customers` or `enrich_customer.py` |
| **L3–L4** | Web/Deep (TBD) | — | Not implemented |

### What We Can Extract (by level)

#### People
- **L1 (Contact)**: email, phone, job title, company (signature/domain)
- **L2 (README)**: role/title, company affiliation, relationship context, areas of expertise
- **L3 (Web)**: LinkedIn URL + summary, current role/company (verified), professional background, public bio/about, company website, notable achievements/publications
- **L4 (Deep)**: full career history, mutual connections, recent news/mentions, company details (size/industry/funding), social links

#### Customers / Partners
- Account type (customer/partner/prospect)
- Stage/status (Active, Prospect, Churn Risk, Blocked)
- Industry/vertical
- My role/ownership (account-owner, technical-lead, support, stakeholder)
- Last contact date
- 1–2 sentence context from README

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

# Customer README frontmatter (enriched)
---
type: customer
title: "Contoso"
account_type: customer
status: Active
industry: "Cloud / AI"
my_role: account-owner
last_contact: "2026-01-05"
last_enriched: "2026-01-05"
enrichment_level: 2
tags:
  - type/customer
  - status/active
  - industry/cloud
---
```

### Triggering Enrichment

#### Manual CLI

```bash
# People
python scripts/enrich_person.py "John Smith" --from-readme
python scripts/enrich_person.py "John Smith" --web
python scripts/enrich_person.py "John Smith" --deep
python scripts/enrich_person.py --all --level 2 --limit 20
python scripts/enrich_person.py --company "Microsoft" --level 3
python scripts/manifest_sync.py enrich --entity people --limit 20

# Customers / Partners
python scripts/enrich_customer.py "Microsoft" --from-readme
python scripts/enrich_customer.py --all --limit 20
python scripts/manifest_sync.py enrich --entity customers --limit 20
```

#### Agent Prompt

When asking an AI agent to run enrichment:

```
Run enrichment for [Entity] at level [2/3/4].

Commands:
- People (L2): python scripts/enrich_person.py "John Smith" --from-readme
- People (L3): python scripts/enrich_person.py "John Smith" --web  
- People (L4): python scripts/enrich_person.py "John Smith" --deep
- Customers (L2): python scripts/enrich_customer.py "Microsoft" --from-readme

For batch enrichment of sparse entries:
python scripts/enrich_person.py --all --level 2 --limit 20
python scripts/enrich_customer.py --all --limit 20
```

#### Automatic Triggers

| Event | Enrichment Triggered |
|-------|---------------------|
| New person/customer folder created | L0 (stub) |
| Email processed with contact | L1 (contact info patched for people) |
| `scripts/ingest.py` patches README | Manifest sync for people |
| `manifest_sync.py enrich --entity people` | L2 (from README) |
| `manifest_sync.py enrich --entity customers` | L2 (from README) |
| Manual `--web` request | L3 (people only) |

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

Unified ingest (`scripts/ingest.py`) calls `sync_person_to_manifest` / `sync_customer_to_manifest` after patches land so manifests + glossary stay fresh. If you apply frontmatter updates in another path, call the same helpers:

```python
sync_person_to_manifest("John Smith", updates, rebuild_cache=True)
sync_customer_to_manifest("Microsoft", updates, rebuild_cache=True)
```

---

## Web Enrichment Details

> People only; customer/partner web enrichment is not wired yet.

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
| `scripts/manifest_sync.py` | Manifest scan/sync/enrich/cache CLI |
| `scripts/enrich_person.py` | People enrichment CLI (L2–L4) |
| `scripts/enrich_customer.py` | Customer/partner enrichment CLI (L2) |
| `scripts/utils/cached_prompts.py` | Glossary loading for prompt caching |
| `_MANIFEST.md` | Per-folder manifest tables |
| `_cache/glossary.json` | Combined glossary cache |
| `_cache/web_enrichment/` | Web search result cache |

---

## Maintenance

### Daily
- Manifests auto-update after email processing (PATCH phase)
- Glossary cache rebuilt when patches applied

### Weekly
- Run `scripts/manifest_sync.py scan` to check sparse entry count
- Run `scripts/manifest_sync.py enrich --entity people --limit 50`
- Run `scripts/manifest_sync.py enrich --entity customers --limit 50`

### Monthly
- Review `#needs-review` tagged entities
- Run L3 web enrichment on key contacts
- Audit and merge duplicate entities

## Common Workflows

- **Resync everything after pipeline changes:** `python scripts/manifest_sync.py sync && python scripts/manifest_sync.py build-cache`
- **Batch fill sparse people:** `python scripts/manifest_sync.py enrich --entity people --limit 20`
- **Batch fill sparse customers:** `python scripts/manifest_sync.py enrich --entity customers --limit 20`
- **Enrich a single account deeply:** `python scripts/enrich_person.py "Name" --deep` (people) or `python scripts/enrich_customer.py "Account" --from-readme` (customers)
- **Check sparse counts:** `python scripts/manifest_sync.py scan --verbose`

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
