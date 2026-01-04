---
type: people
title: Leeraz Ben Or
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Leeraz Ben Or

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Release/program support |
| **Company** | VAST Data |
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
WHERE !completed AND contains(text, "Leeraz Ben Or")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@LeerazBenOr") AND !completed
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
- Ben is the new Google PM counterpart for this effort.

## Topics Discussed

GCP IP allocation and reservation semantics, VIP failover approaches (alias IP vs route-based vs ILB), RDMA constraints on Z4M shapes, Dual-interface model (RDMA + TCP) and subnet/VPC design, Cross-project connectivity via Private Service Connect interfaces (PSCI), MIG static IP pools and mitigating IP reassignment race windows, Network convergence/latency and client reconnect behavior, Capacity planning via testing and customer volume projections, NIC topology and bandwidth allocation, Org chart and key leaders across marketing, alliances, SE, sales, finance, Multi-cloud strategy mandate (Azure/AWS/GCP/Oracle) and complement vs compete framing, Cloud packaging and serverless/pipelines gaps, Neo cloud requirements ownership and team transition, Customer Success vs support operating model, SE engagement strategy and Tech Summit embedding

## Recent Context

- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)

## Profile

**Role**: Release/program support at VAST Data
**Relationship**: Internal collaborator

**Background**:
- Helps with release/program management alongside Daphna.

## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.
- ✅ Carl to move to ProServe under Rob.
- ✅ FRDs and detailed customer requirements will be authored/maintained in Confluence.
- ✅ Jason will own multi-cloud strategy end-to-end and catalog in-flight opportunities from a product requirements lens.
- ✅ Establish a monthly touchpoint between Jason and Brandon.

## Related




---
*Last updated: *