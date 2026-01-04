---
type: people
title: Glenn Lockman
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
---

# Glenn Lockman

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
WHERE !completed AND contains(text, "Glenn Lockman")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@GlennLockman") AND !completed
SORT due ASC
```

## Key Facts

- Jason Vallery reports to Jeff Denworth; charter is making VAST successful on hyperscalers and marketplaces.
- Jason Vallery is ex-Microsoft Azure Storage GPM (object storage/AI storage) and was OpenAI’s primary storage relationship owner starting in 2018.
- Rob Benoit leads the global pre-sales SE org; 18 years at NetApp; strong networking/sysadmin background.
- VAST cloud deployment is complex; marketplace should expose tenant outcomes rather than cluster administration.
- Cloud VM economics are poor for VAST at scale; preferred approach is object storage for capacity tier plus bare metal for performance.
- GCP Z3 helps but becomes expensive at larger sizes; bare metal instances are preferred.
- VAST DataSpaces/global namespace is a major differentiator for hybrid/multi-cloud AI data mobility.
- OpenAI pattern: central CPU-adjacent data lake plus GPU-adjacent working set caches across many regions/clouds.
- Field enablement/content ownership is fragmented with duplicative Confluence docs and unclear owners.
- SE bandwidth is constrained by installs (rack/stack ~2 weeks); a new partner program was created to offload rack-and-stack but cabling errors can cause multi-day delays.

## Topics Discussed

VAST-in-cloud strategy and cloud economics, Marketplace packaging (tenant outcomes vs cluster admin), Bare metal instances vs cloud VMs, Object storage capacity tiering, DataSpaces/global namespace for hybrid/multi-cloud AI, OpenAI reference architecture patterns, Field enablement and solution content ownership, SE org maturity and enterprise selling gaps, Install/rack-and-stack burden and partner program, Networking complexity requirements for deployments, Tech Summit follow-up

## Recent Context

- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)

## Profile

**Relationship**: Internal colleague (mentioned)

**Background**:
- Former Microsoft colleague of Jason; joined VAST in July and was a catalyst for Jason joining.

## Key Decisions

- ✅ Meet at Tech Summit for follow-up conversation

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *