---
type: people
title: Olivia Bouree
created: '2026-01-03'
last_contact: '2025-10-28'
auto_created: true
tags:
- type/people
- needs-review
---

# Olivia Bouree

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
WHERE !completed AND contains(text, "Olivia Bouree")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@OliviaBouree") AND !completed
SORT due ASC
```

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
- Ben (Google PM) is the new PM counterpart for this effort, replacing a prior counterpart (name not captured as a full name).

## Topics Discussed

GCP IP allocation/reservation semantics and failover race window, Static IP reservation via Terraform and MIG static IP pools, VIP/failover approaches: alias IP vs route-based vs ILB, RDMA networking constraints on Z4M shapes, Dual-interface (RDMA + TCP) topology and bandwidth allocation, Cross-project RDMA connectivity via Private Service Connect interfaces (PSCI) vs VPC peering, Testing scale planning and longer-term volume projections for capacity planning, GPU direct storage RDMA vs inter-node RDMA

## Recent Context

- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP networking/IP failover options for upcoming... (via Google)

## Profile

**Relationship**: Meeting participant

**Background**:
- Meeting participant (name appears as Olivia Bouree/Bouree).

## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *