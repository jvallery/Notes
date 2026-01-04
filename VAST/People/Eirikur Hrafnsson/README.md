---
type: people
title: Eirikur Hrafnsson
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
---

# Eirikur Hrafnsson

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Vice President of Cloud Engineering |
| **Company** | VAST Data |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | [https://www.linkedin.com/in/eirikurhrafnsson](https://www.linkedin.com/in/eirikurhrafnsson) |
| **Location** | Seattle, Washington, United States |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

Eirikur Hrafnsson co-founded Greenqloud in 2010, serving as CEO and later COO until 2017. He then joined NetApp as Technical Director, advancing to Chief Architect of Data Fabric, and eventually Vice President of Cloud Engineering. In 2025, he co-founded Red Stapler, which was acquired by VAST Data, where he now serves as Vice President of Cloud Engineering.


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
WHERE !completed AND contains(text, "Eirikur Hrafnsson")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@EirikurHrafnsson") AND !completed
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

GCP IP allocation and reservation semantics, VIP failover approaches (alias IP vs route-based vs ILB), RDMA constraints on Z4M shapes, Dual-interface model (RDMA + TCP) and subnet/VPC design, Cross-project connectivity via Private Service Connect interfaces (PSCI), MIG static IP pools and mitigating IP reassignment race windows, Network convergence/latency and client reconnect behavior, Capacity planning via testing and customer volume projections, NIC topology and bandwidth allocation, GCP Marketplace MVP launch scope (private offers, fixed capacity, no BYOL), Tackle.io integration with Salesforce for private offers, Polaris entitlements, metering, call-home, and Uplink registration automation, Overage policy and GCP marketplace limitations; PAYGO overage workaround, EULA language requirements for overage billing, Finance processes: billing, payout cadence, reconciliation, reporting controls, rev rec

## Recent Context

- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Internal group meeting to finalize the MVP launch plan for VAST on Google Cloud Marketplace using pr... (via Google)
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] - Cloud BU leadership aligned on a dual-track cloud strategy: ship a near-term GCP marketplace MVP wit... (via Cloud)
- 2025-10-27: [[2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]] - Group meeting transcript debating how to align VAST cloud pricing with the new on-prem core+capacity... (via Pricing)

## Profile

**Role**: Meeting participant; coordinating Tackle implementation and GCP MVP launch readiness at VAST Data
**Relationship**: Meeting participant

**Background**:
- Meeting participant.
- Involved in Tackle meetings and operational readiness for GCP Marketplace launch; coordinating finance access to GCP reporting and scheduling walkthroughs.
- Owns GCP MVP deployment flow decisions; implements routable IP approach and follows up with Google on maintenance overlap guarantees.

## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.
- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Pursue dual-track go-to-market: marketplace offer for enterprise bursts plus sell-to hyperscaler-scale deals.
- ✅ Use routable IPs for GCP MVP; defer alias IPs/SaaS Runtime until post-launch.
- ✅ Adapt Enscale solution/deck for Microsoft/MAI with Kubernetes-led control plane and Polaris emphasis.

## Related Customers

- [[Google]]

## Related Projects

- [[Pricing]]
- [[Polaris]]
- [[Cloud]]
- [[GCP MVP]]

## Related




---
*Last updated: *