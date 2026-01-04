---
type: people
title: Karl Vietmeier
last_contact: "2025-11-07"
created: '2026-01-03'
tags:
- type/people
- generated
---

# Karl Vietmeier

## Profile

**Role**: Technical specialist / SE/TME (cloud/distributed systems) at VAST Data (Cloud (implied))
**Location**: Inland Empire (near Pomona/Diamond Bar), Los Angeles area
**Relationship**: Internal collaborator

**Background**:
- Maintains a capacity/overhead calculator sheet with explicit FS and SCM overhead terms (~8% FS + ~3% SCM) referenced as inputs to parameterize.
- Not directly discussed in transcript; included in known entities but not referenced in this note's narrative.
- Helped run Google demo/test case showing global namespace across Japan↔Ohio regions; part of TPU benchmark/demo effort.

## Open Tasks

- [ ] Parameterize Karl’s calculator with cloud/region, zones, FD count, per-zone/per-FD SKU counts, EC width, non-EC overheads, rebuild headroom, and rolling-update headroom; output “available capacity” and derived overhead % for pricing.
- [ ] Work with Karl and dev leads to wire calculator inputs into deployment tooling so customer-facing “available capacity” matches deployed striping for the chosen region/SKU.

## Recent Context

- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-10-31: [[Sources/Transcripts/2025/2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for.md|Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] — Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for a planet-scale, mult...
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi...
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)
- 2025-10-28: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra ("Koncha") aligning on using MAI and UK Met Of... (via Kanchan Mehrotra)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- unknown: [[Available Capacity Calculations]] - Email-style note proposing replacing a fixed overhead percentage with a first-principles “available ... (via Cloud)

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

GCP IP allocation and reservation semantics, VIP failover approaches (alias IP vs route-based vs ILB), RDMA constraints on Z4M shapes, Dual-interface model (RDMA + TCP) and subnet/VPC design, Cross-project connectivity via Private Service Connect interfaces (PSCI), MIG static IP pools and mitigating IP reassignment race windows, Network convergence/latency and client reconnect behavior, Capacity planning via testing and customer volume projections, NIC topology and bandwidth allocation, Org map and key leaders/roles, Cross-cloud platform strategy and homogenization across providers, Cloud GTM plays and integrations (Foundry/Bedrock/Vertex), Cataloging in-flight deals by product requirements, Control-plane partnerships and 'cloud-in-a-box' for Tier-2 clouds, Customer requirements/FRDs documentation in Confluence

## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.
- ✅ Pursue deeper integration with Google Distributed Cloud and aim to be part of the GDC SKU.
- ✅ Treat Microsoft Azure as a distinct sell-to motion (first-party/Storage HW) separate from marketplace sell-through.
- ✅ Use real-workload benchmarks (not synthetic) as the standard for TPU/storage evaluations with Google.

## Related Projects

- [[VAST on Azure Integration]]
- [[Z4M RDMA Networking (GCP)]]
- [[Cloud]]

## Related

<!-- Wikilinks to related entities -->
