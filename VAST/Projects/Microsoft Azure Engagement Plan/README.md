---
type: projects
title: Microsoft Azure Engagement Plan
created: '2026-01-03'
last_updated: ''
status: complete
auto_created: true
tags:
- type/projects
- needs-review
- status/complete
last_contact: unknown
---

# Microsoft Azure Engagement Plan

## Overview

Draft a Microsoft networking engagement plan focused on minimizing egress (e.g., ExpressRoute Direct Local) for VAST’s Azure offerings.

## Status

| Field | Value |
|-------|-------|
| **Status** | complete |
| **Owner** | Jeff Denworth |

## Current Blockers

- ❌ Azure networking constraints and unclear path to improved topology

## Next Steps

- [ ] Engage Igal’s team on networking needs; validate UKMO constraints

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jeff Denworth]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Start HR process and interviews for Jason at VAST.
- ✅ Position Jason initially as an Azure-focused business development/strategic lead paired with a highly technical counterpart.
- ✅ Near-term focus on MAI and UK Met Office over broad sales motion.
- ✅ Pursue a dual-track: marketplace listing plus flagship customer escalations.
- ✅ Use Nidhi to re-energize internal advocacy once the story and offer are ready.

## Key Facts

- All listed Microsoft/Azure tasks were completed on 2025-11-08.
- Focus areas included minimizing Azure egress (ExpressRoute Direct Local), aligning Azure GA milestones with Lifter phases, and producing BizDev/ROI/marketplace collateral.
- Jason Vallery has ~13 years on Azure and previously led Microsoft’s OpenAI engagement and large-scale storage programs; recently returned from sabbatical into an architect role under Manish.
- Azure Storage org is ~1,600+ people; Jason cited slow execution as a cultural challenge.
- VAST cloud GA plan discussed: GCP GA in October, AWS GA (MVP) in December, Azure GA in February, with broader Azure/Lifter milestone targeted next September.
- VAST signed Microsoft Lifter and is pursuing Azure marketplace, customer-tenant managed offering, and future 1P alignment.
- ExpressRoute Direct Local was identified as a key mechanism to mitigate egress costs via fixed-price high-bandwidth connectivity.
- GPU supply constraints limit 3P deals; demand remains high.
- Azure LSV4 is the only current option and has poor economics (too many cores, weak networking, low drive density).
- VAST density claim: ~1 EB needs ~20 VAST racks vs ~240 Blob racks; power can be ~1/5 in MAI Falcon-type clusters.

## Topics / Themes

Microsoft Azure networking and egress minimization, Azure GA milestones and Lifter program alignment, ROI data usage validation for comparisons, LSv4/LSv5 vs OEM/ODM vs Azure Storage positioning, Microsoft BizDev enablement and introductions, Power savings translated to GPU capacity, Marketplace L-series offer expansion (SKUs/OEM path), VAST accelerated cloud GTM hiring plan, Potential role scope for Jason (Azure BD/strategic lead vs broader cross-cloud), Azure marketplace vs customer-tenant managed offering vs SaaS/1P trajectory, Multi-cloud/neo-cloud strategy and global namespace, Egress fees mitigation via Microsoft networking (ExpressRoute Direct Local), Microsoft execution speed/culture and partnership dynamics, MAI as lighthouse customer to force Azure hardware shape, UK Met Office constraints (price, networking) and Supercomputing meetings

## Related People

- [[Jeff Denworth]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

- unknown: [[2025-10 - Microsoft Tasks]] - Checklist of completed action items for Microsoft/Azure engagement, including networking/egress plan... (via Microsoft)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- 2025-09-16: [[2025-09-16 - Jeff outlined VAST’s accelerated cloud push and multiple potential roles for Jas]] - Weekly 1:1 between Jeff Denworth and Jason Vallery covering VAST’s accelerated cloud GTM push, poten... (via Jeff Denworth)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *