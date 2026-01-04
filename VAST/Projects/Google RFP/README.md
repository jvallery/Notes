---
type: projects
title: Google RFP
created: '2026-01-03'
last_updated: ''
status: active
auto_created: true
tags:
- type/projects
- needs-review
- status/active
last_contact: '2025-11-07'
---

# Google RFP

## Overview

Prepare for Google RFP discussions; quickly triage whether requirements are block/latency-heavy (NetApp advantaged) vs object/throughput-heavy (better VAST fit).

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |

## Current Blockers

- ❌ Unclear workload orientation; risk of misfit if block/low-latency is primary

## Next Steps

- [ ] Create and use a fast filter checklist (p99/p999 latency, IO size distribution, block vs object mix, bandwidth ceilings, checkpoint cadence)
- [ ] Confirm whether it is a TPU opportunity in disguise
- [ ] Decide go/no-bid posture based on filters

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jeff Denworth]] |  | VAST Data |
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

- [[Jeff Denworth]]
- [[Jason Vallery]]

## Related Customers

- [[Google]]

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