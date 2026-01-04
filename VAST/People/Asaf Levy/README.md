---
type: people
title: Asaf Levy
last_contact: "2025-11-07"
created: '2026-01-03'
tags:
- type/people
- generated
---

# Asaf Levy

## Profile

**Role**: Chief architect at VAST Data (Architecture team (within engineering))
**Location**: Tel Aviv
**Relationship**: Internal collaborator / technical stakeholder

**Background**:
- Aligned on persistence design, object tiering, and QoS/governance; contributed by defining governance model, benchmarking metadata persistence options, and sharing DataSpaces architecture/persistence roadmap.
- Listed as a candidate for weekly/monthly 1:1 cadence (marked '++').
- Author has met Asaf and has more time scheduled; technical collaborator.

## Open Tasks

```tasks
path includes Asaf Levy
not done
```

## Recent Context

- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-03: [[2025-11-03 - Team reviewed the updated 5.5 plan feature freeze next week, beta in January, r]] - Group meeting reviewing the VAST 5.5 release plan and scope changes, including timeline (feature fre... (via Phase Gate 1)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m... (via Eyal Traitel)
- 2025-10-29: [[2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga]] - Weekly 1:1 where Liraz Ben Or explained VAST’s non-traditional major release management process (4 p... (via Liraz Ben Or)
- 2025-10-29: [[2025-10-29 - Intro 1-1 where Liraz walked Jason through VAST’s non-traditional release manage]] - Weekly 1:1 intro where Liraz Ben Or walked Jason Vallery through VAST’s non-traditional release mana... (via Liraz Ben Or)
- 2025-10-29: [[2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee]] - 1:1 between Jason Vallery and Tomer Hagay aligning on shifting cloud work to a PM-led model, introdu... (via Tomer Hagay)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)
- 2025-10-28: [[2025-10-28 - Jason and Shachar aligned on setting a weekly 30-minute 11 and planning Jason’s]] - Weekly 30-minute 1:1 cadence was established between Jason Vallery and Shachar Feinblit, and they pl... (via Shachar Feinblit)
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] - Cloud BU leadership aligned on a dual-track cloud strategy: ship a near-term GCP marketplace MVP wit... (via Cloud)
- unknown: [[Sources/Transcripts/2025/2025-10 - Asaf Levy.md|Asaf Levy]] — - [x] Meet Asaf (chief architect) to align on persistence design, object tiering, and QoS/governance...
- unknown: [[2025-10 - Asaf Levy]] - Completed action items from a working session with Asaf Levy to align on DataSpaces persistence desi...
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)

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

## Topics

GCP IP allocation and reservation semantics, VIP failover approaches (alias IP vs route-based vs ILB), RDMA constraints on Z4M shapes, Dual-interface model (RDMA + TCP) and subnet/VPC design, Cross-project connectivity via Private Service Connect interfaces (PSCI), MIG static IP pools and mitigating IP reassignment race windows, Network convergence/latency and client reconnect behavior, Capacity planning via testing and customer volume projections, NIC topology and bandwidth allocation, Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics, Multi-tenancy backlog toward SaaS

## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.
- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.

## Related Customers

- [[OpenAI]]

## Related Projects

- [[Cloud]]
- [[5.5 Features]]
- [[Enscale deck]]
- [[Project Apollo]]
- [[VIP/Failover Design (GCP RDMA)]]

## Related

<!-- Wikilinks to related entities -->
