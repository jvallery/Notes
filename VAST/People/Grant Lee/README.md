---
type: people
title: Grant Lee
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
---

# Grant Lee

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** |  |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

_Career history, expertise, interests, personal details shared..._


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Grant Lee")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@GrantLee") AND !completed
SORT due ASC
```

## Key Facts

- Targets reviewed included Thinking Machines, Reflection, Physical Intelligence, Midjourney, SSI (Safe Superintelligence Inc.), Perplexity, Cohere, Magic, Anthropic, and Apple.
- Reflection is reportedly discussing ~10,000 GB300s for an upcoming run.
- SSI outreach via OpenAI connections is considered non-viable due to conflict.
- Chris’s target list is primarily labs with $500M–$2B+ funding or strong bootstrapped revenue (e.g., Midjourney).
- Warm-intro quality varies; weak LinkedIn mutuals can waste cycles.
- Hyperscaler conflicts (Google/Microsoft) can block introductions.

## Topics Discussed

Warm intro mapping via LinkedIn mutuals, Investor vectors for introductions, NVIDIA relationship strategy (events vs 1:1 intros), Outreach messaging strategy (pipeline components vs platform narrative), Persona targeting (data/pipeline teams vs exec-only), Salesforce history audit before re-engagement, Target account prioritization and expansion (e.g., Black Forest Labs)

## Recent Context

- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)

## Profile

**Relationship**: External connector

**Background**:
- Suggested connector for Perplexity intros (to Noah Yonick / Kevin Wu / Tony Wu).

## Key Decisions

- ✅ Reframe outreach to focus on concrete pipeline components (Kafka for RL, real-time vector DB) rather than platform narratives.
- ✅ Use an NVIDIA-customer event (via AI Circle) as the primary NVIDIA intro mechanism; direct 1:1 intros from NVIDIA reps are unlikely.
- ✅ Broaden persona targeting to include data/pipeline owners, not just CTO-level contacts.
- ✅ Defer direct Google/Microsoft-introduced paths where conflicts exist to reduce hyperscaler conflict risk.

## Related Projects

- [[Model Builder Turbine]]

## Related




---
*Last updated: *