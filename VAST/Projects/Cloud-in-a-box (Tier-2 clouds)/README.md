---
type: projects
title: Cloud-in-a-box (Tier-2 clouds)
created: '2026-01-03'
last_updated: ''
status: proposed
auto_created: true
tags:
- type/projects
- needs-review
- status/proposed
last_contact: '2025-11-07'
---

# Cloud-in-a-box (Tier-2 clouds)

## Overview

Alliance-driven blueprint for Tier-2 clouds using control-plane partners to deliver a packaged AI pipeline solution (GPU-as-a-service orchestration + required services).

## Status

| Field | Value |
|-------|-------|
| **Status** | proposed |
| **Owner** | Jason Vallery |

## Current Blockers

- ❌ Partner ecosystem alignment and role clarity
- ❌ Need Morty involvement without pulling focus from Neo

## Next Steps

- [ ] 1:1 with John to align on control-plane partners and blueprint scope
- [ ] Pull Morty into the conversation after initial alignment
- [ ] Draft blueprint outline and partner responsibilities

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Morty]] |  | VAST Data |
| [[John]] | Alliances/partnerships lead (conventional channels; AMD/NVIDIA; control-plane partners) | VAST Data |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Carl to move to ProServe under Rob.
- ✅ FRDs and detailed customer requirements will be authored/maintained in Confluence.
- ✅ Jason will own multi-cloud strategy end-to-end and catalog in-flight opportunities from a product requirements lens.
- ✅ Establish a monthly touchpoint between Jason and Brandon.

## Key Facts

- John owns alliances/partnerships for conventional channels (incl. AMD/NVIDIA) and control-plane partner ecosystem for Tier-2 cloud-in-a-box.
- Morty owns Neo cloud feature requirements; moving to Jason’s team but must keep Neo focus.
- Customer Success under Rob is effectively reactive support, not proactive CS.
- SE org is critical to Jason’s success; Hari called out as a top SE.
- China posture agreed: software-only sales outpost; avoid CAPEX/headcount build-out.
- Need a crisp, quantified Azure Storage gaps narrative ('dagger' slide) and a repeatable measurement rubric across clouds.
- Win/loss analysis should be routine and tied to Sales Ops; cloud is a platform, product gaps apply across deployment environments.
- Confluence is the engineering-respected source of truth for FRDs/requirements; coordinate taxonomy with Alon (A.L.) and Tomer.

## Topics / Themes

Org chart and key leaders across marketing, alliances, SE, sales, finance, Multi-cloud strategy mandate (Azure/AWS/GCP/Oracle) and complement vs compete framing, Cloud packaging and serverless/pipelines gaps, Neo cloud requirements ownership and team transition, Customer Success vs support operating model, SE engagement strategy and Tech Summit embedding, China go-to-market posture (software-only), Azure Storage limitations and messaging for Microsoft, Google RFP triage and no-bid criteria for block/latency-heavy asks, Confluence as FRD system of record and documentation taxonomy, Win/loss cadence and product MBR rhythm

## Related People

- [[Morty]]
- [[John]]
- [[Jason Vallery]]

## Related Customers

_Which customers/accounts is this project related to?_


## Recent Context

- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *