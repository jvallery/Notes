---
type: projects
title: PSC Interfaces for Cross-Project RDMA
created: '2026-01-03'
last_updated: ''
status: active
auto_created: true
tags:
- type/projects
- needs-review
- status/active
last_contact: '2025-10-28'
---

# PSC Interfaces for Cross-Project RDMA

## Overview

Assess requirement to use Private Service Connect interfaces (PSCI) for cross-project RDMA connectivity (VPC peering not supported) and implications for complexity, performance, and architecture.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Google networking team |

## Current Blockers

- ❌ Unclear whether PSCI will meet performance/feature needs for the use case
- ❌ Added complexity due to PSCI being load-balancer-based implementation

## Next Steps

- [ ] Evaluate PSCI requirements and implications for cross-project RDMA data plane
- [ ] Confirm cross-project RDMA constraints and performance impact

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Billy Kettler]] |  | Google |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.

## Key Facts

- GCP IP reassignment requires remove then reassign, creating a short race window during failover.
- MIGs can use a pool of reserved static IPs for primary addresses; alias IP behavior differs.
- Alias IPs are expected to be unsupported with RDMA; RDMA uses a separate subnet/interface.
- Z4M will launch with inter-node RDMA; GPU-direct storage RDMA is a separate effort.
- Two interfaces (RDMA and TCP) are expected per Z4M instance; may be same VPC on different subnets.
- Cross-project RDMA will require Private Service Connect interfaces; VPC peering will not be supported.
- Route-based failover has latency/convergence considerations; ILB introduces pricing/feature tradeoffs.
- Per-VM bandwidth is capped; adding NICs does not increase aggregate bandwidth.
- Initial test scale target is roughly 10–30 instances; CI and scale testing will require more.
- Ben is the new Google PM counterpart for this effort.

## Topics / Themes

GCP IP allocation and reservation semantics, VIP failover approaches (alias IP vs route-based vs ILB), RDMA constraints on Z4M shapes, Dual-interface model (RDMA + TCP) and subnet/VPC design, Cross-project connectivity via Private Service Connect interfaces (PSCI), MIG static IP pools and mitigating IP reassignment race windows, Network convergence/latency and client reconnect behavior, Capacity planning via testing and customer volume projections, NIC topology and bandwidth allocation

## Related People

- [[Billy Kettler]]

## Related Customers

- [[Google]]

## Recent Context

- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *