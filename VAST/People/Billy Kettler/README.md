---
type: people
title: Billy Kettler
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
- company/google
---

# Billy Kettler

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** | Google |
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
WHERE !completed AND contains(text, "Billy Kettler")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@BillyKettler") AND !completed
SORT due ASC
```

## Key Facts

- Z4M is the next Google storage-serving VM with higher storage and network density; Z3 exists today.
- Z4M targets storage-serving use cases; CPU/RAM may be overprovisioned initially with planned pricing optimization.
- Google is developing a Google Supercomputer (GSC) provisioning interface to optimize co-placement of storage and accelerators and potentially automate partner deployments like VAST.
- Local SSD is the initial choice due to latency; HyperDisk decouples capacity/performance but has higher latency than local SSD.
- Anywhere Cache reduces intra-zone egress/operational cost but does not improve object-store latency.
- RDMA planned for Z4M and A5X GPUs with GPUDirect Storage; TPU RDMA will come later.
- Internal networking features (e.g., ILB) can create egress-like costs that become prohibitive at multi-TB/s throughput.
- VAST marketplace launch on GCP is near; integration with Vertex/TPU is being considered.
- Cross-region/CSP/neo-hyperscaler data movement economics (egress) are a major constraint for customers with exabyte-scale data lakes.
- GCP IP reassignment requires remove then reassign, creating a short race window during failover.

## Topics Discussed

VAST on GCP architecture using Z4M storage-serving VMs, Local SSD vs HyperDisk vs object storage tiers, Metadata offload to object storage and need for a higher-performance object tier, Google Supercomputer (GSC) provisioning and co-placement/auto-deploy integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline, Cloud WAN and networking architecture for multi-region data movement, Egress and internal networking (ILB) cost mitigation and commercial constructs, Marketplace launch and deeper integration with Google ecosystem (Vertex/TPU), Hybrid/neo-hyperscaler scenarios and global namespace/data mobility, GCP IP allocation/reservation semantics and failover race window, Static IP reservation via Terraform and MIG static IP pools, VIP/failover approaches: alias IP vs route-based vs ILB, RDMA networking constraints on Z4M shapes, Dual-interface (RDMA + TCP) topology and bandwidth allocation, Cross-project RDMA connectivity via Private Service Connect interfaces (PSCI) vs VPC peering

## Recent Context

- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders to align on the technical path for running VAST on GC... (via Google)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP networking/IP failover options for upcoming... (via Google)

## Profile

**Role**: Google
**Relationship**: Customer/partner contact (Google)

**Background**:
- Google partner/technical stakeholder for VAST on GCP; involved in marketplace launch, Z4M program, RDMA/GPUDirect planning, and GSC integration scoping.
- Google counterpart involved in networking/RDMA discussions; tasked with scheduling networking follow-up and confirming RDMA support details.

## Key Decisions

- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).
- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.

## Related Customers

- [[Google]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *