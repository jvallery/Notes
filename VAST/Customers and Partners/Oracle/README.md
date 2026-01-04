---
type: customer
title: Oracle
created: '2026-01-03'
last_contact: '2025-10-27'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Oracle

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | Enterprise software, cloud computing, computer hardware, consulting |

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

- Referenced as part of OpenAI’s multi-cloud access pattern (context for Azure Extended Zones/partner connectivity)

## Key Decisions

- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Key Facts

- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.
- VAST vs Azure Blob per 1 EB: ~1/10 racks, ~1/5 megawatts, >=5x performance, but ~2x capex.
- Azure Marketplace VAST offer on L-series VMs is not density/cost competitive for real workloads; positioned as a checkbox.
- Apollo ownership boundaries: Chi owns bare-metal control plane; Sky/Overlake owns security; Ronnie Booker’s org owns chassis/layout/storage placement decisions.
- Azure MAI/Falcon issues include lack of topology-aware scheduling; rack-level placement not expected until ~Feb; IB/telemetry improving.
- OpenAI infra leadership changed: Uday (ex-xAI) now runs infra at OpenAI and reports to Greg Brockman; may reduce Microsoft alignment; power is a major Azure constraint.
- Kurt expected A2N approval for Extended Zones/NodeJoin in ~3 weeks; target partners include sovereign/neo-clouds such as sakura.net in Japan.

## Topics / Themes

Azure GTM path for VAST storage (BizDev-led engagement), VAST density/power advantages vs Azure Blob and Marketplace L-series limitations, OEM/ODM hardware path into Azure data centers and Apollo decision-making, Azure Extended Zones (network-only) and AKS NodeJoin (ACAS FlexNode) GA proposal, MAI/Falcon operational issues: topology-aware scheduling, IB telemetry, reliability, Power constraints as primary bottleneck and translating storage savings into GPUs, OpenAI leadership changes and implications for Microsoft alignment, Supercomputing conference coordination and intros

## Recent Context

- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Related People

_Internal team members working on this account..._


---
*Last updated: *