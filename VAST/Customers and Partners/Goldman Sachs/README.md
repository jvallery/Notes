---
type: customer
title: Goldman Sachs
created: '2026-01-03'
last_contact: '2025-10-31'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Goldman Sachs

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | _Unknown_ |

## Key Contacts

_No key contacts identified._

## Active Projects

_What projects/initiatives are active with this customer?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Current Blockers

_No known blockers._

## Next Steps

_What are the immediate next actions for this account?_


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Opportunities

_No active opportunities._

## Key Decisions

- ✅ Meet at Tech Summit for follow-up conversation

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

## Topics / Themes

VAST-in-cloud strategy and cloud economics, Marketplace packaging (tenant outcomes vs cluster admin), Bare metal instances vs cloud VMs, Object storage capacity tiering, DataSpaces/global namespace for hybrid/multi-cloud AI, OpenAI reference architecture patterns, Field enablement and solution content ownership, SE org maturity and enterprise selling gaps, Install/rack-and-stack burden and partner program, Networking complexity requirements for deployments, Tech Summit follow-up

## Recent Context

- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)

## Related People

_Internal team members working on this account..._


---
*Last updated: *