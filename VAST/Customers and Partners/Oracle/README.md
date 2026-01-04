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

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | Enterprise software, cloud computing, computer hardware, consulting |

## Key Contacts

_No key contacts identified._

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Key Facts

- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.
- VAST vs Azure Blob per 1 EB: ~1/10 racks, ~1/5 megawatts, >=5x performance, but ~2x capex.
- Azure Marketplace VAST offer on L-series VMs is not density/cost competitive for real workloads; positioned as a checkbox.
- Apollo ownership boundaries: Chi owns bare-metal control plane; Sky/Overlake owns security; Ronnie Booker’s org owns chassis/layout/storage placement decisions.
- Azure MAI/Falcon issues include lack of topology-aware scheduling; rack-level placement not expected until ~Feb; IB/telemetry improving.
- OpenAI infra leadership changed: Uday (ex-xAI) now runs infra at OpenAI and reports to Greg Brockman; may reduce Microsoft alignment; power is a major Azure constraint.
- Kurt expected A2N approval for Extended Zones/NodeJoin in ~3 weeks; target partners include sovereign/neo-clouds such as sakura.net in Japan.

## Opportunities

- Referenced as part of OpenAI’s multi-cloud access pattern (context for Azure Extended Zones/partner connectivity)
