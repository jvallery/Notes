# Entity Discovery Service

> **Version**: 1.0  
> **Last Updated**: 2026-01-05  
> **Entry Point**: `Workflow/scripts/entity_discovery.py`

## Overview

The Entity Discovery Service classifies and enriches entities (people, companies, projects) across all ingestion flows. It ensures entities are routed to the correct vault location regardless of source.

## Classification Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Entity Name                                                              │
│ + Context (email subject, transcript snippet, etc.)                      │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 1: Check Existing Entity                                            │
│ Search VAST/People/, VAST/Customers and Partners/, VAST/Projects/        │
│ → If found: Use existing, return immediately                             │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ Not found
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 2: Quick Classification (No API)                                    │
│ • Known companies list (Microsoft, Google, Tesla, Slice, etc.)           │
│ • Company suffixes (Inc, LLC, Corp, Ltd, etc.)                           │
│ • Project indicators (MVP, POC, Initiative, etc.)                        │
│ → If matched: Return with 95% confidence                                 │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ Not matched
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 3: Heuristic Classification                                         │
│ • Person pattern: 2-4 words, capitalized first letters                   │
│ • Single word without context → Unknown                                  │
│ → Returns with 50-70% confidence                                         │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ Low confidence / need more info
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 4: AI Classification (OpenAI, cached)                               │
│ • Uses gpt-4o with JSON response format                                  │
│ • Returns enriched data: description, title, company, industry           │
│ • Cached for 30 days in Workflow/_cache/entity_discovery/                │
│ → Returns with 80-100% confidence + enrichment                           │
└─────────────────────────────────────────────────────────────────────────┘
```

## Entity Types

| Type      | Vault Location                     | Examples                        |
| --------- | ---------------------------------- | ------------------------------- |
| `person`  | `VAST/People/`                     | Satya Nadella, John Smith       |
| `company` | `VAST/Customers and Partners/`     | Tesla, Microsoft, Slice, kodeON |
| `project` | `VAST/Projects/`                   | Cloud Marketplace MVP           |
| `unknown` | `VAST/People/` (with needs-review) | Ambiguous single names          |

## EntityIndex Lookup & Aliases

- People lookup order: **email → alias normalization (`Workflow/entities/aliases.yaml`) → exact name → initial + last name → fuzzy match** (cached per query). Alias files include canonical names as keys to stabilize normalization.
- Companies/projects use alias normalization plus fuzzy difflib matching to catch minor spelling variants.
- ContextBundle uses EntityIndex to pull README summaries (VAST + Personal) for manifest hits, participants, and proper names found in source content before extraction.

## Usage

### CLI Testing

```bash
cd ~/Documents/Notes/Workflow && source .venv/bin/activate

# Test classification
python scripts/entity_discovery.py "Tesla" --context "email about credits"
python scripts/entity_discovery.py "Satya Nadella" --context "Microsoft CEO"
python scripts/entity_discovery.py "Slice" --context "pizza ordering"

# Skip cache for fresh classification
python scripts/entity_discovery.py "John Smith" --no-cache
```

### Programmatic Usage

```python
from entity_discovery import discover_entity, find_or_create_entity, EntityType

# Just discover and classify
result = discover_entity(
    name="Tesla",
    context="email about credits expiring",
    source_type="email",
    client=openai_client  # Optional, will create if not provided
)

print(result.entity_type)      # EntityType.COMPANY
print(result.canonical_name)   # "Tesla"
print(result.suggested_path)   # "VAST/Customers and Partners/Tesla"
print(result.confidence)       # 0.95

# Find or create with folder creation
folder_path, discovery = find_or_create_entity(
    name="Slice",
    context="pizza app",
    email="info@slice.com",
    client=openai_client,
    dry_run=False
)
```

## Known Entity Lists

The service maintains lists of known entities for quick classification:

### Known Companies (No API Required)
```
microsoft, google, amazon, aws, meta, facebook, apple, nvidia, openai, 
anthropic, tesla, ibm, dell, hp, hpe, intel, amd, cisco, oracle, 
salesforce, vmware, netapp, pure storage, vast, vast data, coreweave, 
lambda, crusoe, databricks, snowflake, walmart, target, costco, kroger,
goldman sachs, jpmorgan, morgan stanley, citadel, blackrock, nebius, 
yandex, alibaba, tencent, baidu, samsung, lg, slice, kodeon, ey, 
deloitte, pwc, kpmg, accenture, mckinsey, bain, bcg, infosys, tcs, 
wipro, cognizant
```

### Company Suffixes
```
inc, inc., corp, corp., corporation, llc, ltd, ltd., limited, co, co.,
company, group, holdings, partners, technologies, systems, solutions, 
services, labs, ai
```

### Project Indicators
```
project, initiative, program, mvp, poc, pilot, implementation, 
migration, deployment, rollout
```

## EntityDiscovery Model

```python
class EntityDiscovery(BaseModel):
    # Classification
    original_name: str          # As provided
    entity_type: EntityType     # person, company, project, unknown
    confidence: float           # 0.0 - 1.0
    
    # Enrichment
    canonical_name: str         # Proper full name
    description: str | None     # Brief description
    
    # Person-specific
    title: str | None           # Job title
    company: str | None         # Employer
    linkedin_url: str | None    # LinkedIn URL
    
    # Company-specific
    industry: str | None        # Industry sector
    website: str | None         # Company website
    company_type: str | None    # customer, partner, competitor
    
    # Vault routing
    suggested_path: str | None  # Suggested vault path
    
    # Metadata
    sources: list[str]          # Where classification came from
    discovered_at: str          # ISO timestamp
```

## Integration Points

### Email Ingestion
```python
# In ingest_emails.py → _generate_person_patches()
from entity_discovery import discover_entity, EntityType

discovery = discover_entity(
    name=contact.name,
    context=f"Email about: {extraction.subject}",
    source_type="email",
    client=openai_client
)

if discovery.entity_type == EntityType.COMPANY:
    folder = vault / "VAST" / "Customers and Partners" / discovery.canonical_name
elif discovery.entity_type == EntityType.PROJECT:
    folder = vault / "VAST" / "Projects" / discovery.canonical_name
else:
    folder = vault / "VAST" / "People" / contact.name
```

### Transcript Ingestion
```python
# In extract.py or plan.py
from entity_discovery import discover_entity

for mention in extraction.mentions.people:
    discovery = discover_entity(
        name=mention,
        context=extraction.summary,
        source_type="transcript"
    )
    # Route based on discovery.entity_type
```

### Document Ingestion
```python
# Future: document ingestion
from entity_discovery import discover_entity

for entity in extracted_entities:
    discovery = discover_entity(
        name=entity.name,
        context=document.summary,
        source_type="document"
    )
```

## Caching

Entity discoveries are cached to avoid redundant API calls:

- **Location**: `Workflow/_cache/entity_discovery/`
- **Format**: JSON files named by normalized entity name
- **TTL**: 30 days
- **Skip cache**: Use `--no-cache` flag or `use_cache=False`

```
Workflow/_cache/entity_discovery/
├── tesla.json
├── microsoft.json
├── satya_nadella.json
└── john_smith.json
```

## Error Handling

| Error                  | Behavior                                  |
| ---------------------- | ----------------------------------------- |
| No API key             | Falls back to heuristic classification    |
| API call fails         | Falls back to heuristic classification    |
| Ambiguous entity       | Returns `unknown` type with low confidence |
| Cache read error       | Ignores cache, re-classifies              |

## Configuration

The service reads from `Workflow/config.yaml`:

```yaml
# Not yet implemented - currently uses defaults
entity_discovery:
  cache_ttl_days: 30
  min_confidence_for_creation: 0.6
  model: gpt-4o
```

## Adding Known Entities

To add entities to the quick-classify list (no API call):

```python
# In entity_discovery.py

KNOWN_COMPANIES = {
    "microsoft", "google", "amazon",
    # Add new known companies here
    "new_company_name",
}
```

## Testing

```bash
# Run discovery tests
cd ~/Documents/Notes/Workflow
source .venv/bin/activate
pytest tests/test_entity_discovery.py -v

# Test known companies route correctly
python -c "from scripts.entity_discovery import _quick_classify, EntityType; assert _quick_classify('Tesla') == EntityType.COMPANY"

# Test person names route correctly
python -c "from scripts.entity_discovery import _quick_classify, EntityType; assert _quick_classify('John Smith') == EntityType.PERSON"
```
