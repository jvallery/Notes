---
name: Jonsi Stephenson
role: CEO
company: VAST Data
last_contact: unknown
---

# Jonsi Stephenson

CEO of VAST Data.

## Recent Context

- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Jonsi Stephenson]] - A completed action item to align with Jonsi Stephenson on travel plans in order to enable an in-pers...
- unknown: [[_Open Topics]] - Open topics note for Jonsi Stephenson that currently only contains a task query filtering for incomp...
- 2026-01-03: [[2026-01-03 - Prep for Microsoft AI talks]] - Jonsi Stephenson and Jason Vallery aligned messaging and strategy for upcoming Microsoft AI discussi...
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro...
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
- 2025-10-30: [[2025-10-30 - Intro 1-1 between Jason and Dre. Dre outlined SE enablement cadence and an S3Ob]] - Intro 1:1 between Jason Vallery and Deandre (Dre) Jackson aligning on cloud enablement messaging and... (via Deandre Jackson)
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m... (via Eyal Traitel)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Internal group meeting to finalize the MVP launch plan for VAST on Google Cloud Marketplace using pr... (via Google)


- 2025-10-06: [[2025-10-06 - Jason has a complex VAST offer with risky, sales-linked compensation and a more]] - Weekly 1:1 between Jason Vallery and Jai Menon focused on Jason’s decision to leave Microsoft due to... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 between Jason Vallery and Jai Menon discussing Jason’s competing offers from VAST and Cru... (via Jai Menon)
## Profile

**Role**: CEO at VAST Data
**Location**: Iceland (traveling; in Orlando during call)
**Relationship**: Internal executive stakeholder

**Background**:
- Listed as a candidate for weekly/monthly 1:1 cadence.
- CEO of VAST Data.
- Discussed positioning VAST with Microsoft AI; noted a temporary restraining order was lifted and remaining legal focus is on solicitation.

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


- Crusoe deadline is 2025-10-08.
- Prospective VAST role: PM title reporting to Jeff Denworth and VAST CEO (referred to as Renan); owns PM for a cloud control plane via Red Stapler (founded by Jan C. Stefansson); dotted-line support to Microsoft sell-to/sell-with and OpenAI Project Stargate.
- VAST compensation includes commission as a percentage of sales to OpenAI/Azure; equity component described as modest; outcome could range from zero to many millions.
- Leaving Microsoft would forfeit roughly $800K already vested, reducing the net gap versus a $2M offer to about $1.1–$1.2M.
- Apollo scope/boundaries at Microsoft are unclear with many stakeholders and tight timelines as data centers go live.
- Path to partner at Microsoft remains undefined.
- Jason has a VAST offer with complex, highly variable compensation tied to OpenAI/Azure sales plus equity.
- Crusoe offer deadline is Wednesday; VAST has not set a decision deadline.
- Microsoft cannot approach Crusoe-level compensation; any change would be modest and potentially insulting.
- Apollo scope and responsibilities are unclear, making it hard to define a successful role or path to partner.
## Topics

GCP IP allocation and reservation semantics, VIP failover approaches (alias IP vs route-based vs ILB), RDMA constraints on Z4M shapes, Dual-interface model (RDMA + TCP) and subnet/VPC design, Cross-project connectivity via Private Service Connect interfaces (PSCI), MIG static IP pools and mitigating IP reassignment race windows, Network convergence/latency and client reconnect behavior, Capacity planning via testing and customer volume projections, NIC topology and bandwidth allocation, GCP Marketplace MVP launch scope (private offers, fixed capacity, no BYOL), Tackle.io integration with Salesforce for private offers, Polaris entitlements, metering, call-home, and Uplink registration automation, Overage policy and GCP marketplace limitations; PAYGO overage workaround, EULA language requirements for overage billing, Finance processes: billing, payout cadence, reconciliation, reporting controls, rev rec


Offer comparison (VAST vs Crusoe vs staying at Microsoft), Compensation structure and risk (commission vs equity), Apollo scope ambiguity and execution risk, Career trajectory and path to partner at Microsoft, Resignation timing and decision deadline pressure, Job offers comparison (VAST vs Crusoe vs Microsoft), Compensation structure risk (commission/equity variability), Apollo program scope ambiguity and execution risk, Resignation timeline
## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.
- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Anchor enablement on workload scenarios rather than generic object features.
- ✅ Avoid engaging in price-only competitions (e.g., MinIO) unless the workload merits VAST’s performance/value.
- ✅ Do not pursue Microsoft compensation changes for Jason.

## Open Tasks

- [ ] Send Jonsi the slide deck/comparison materials (including the power/footprint/throughput slide) before his meeting with Ong and Manish.
- [ ] Text Jason after the meeting with Ong and Manish and schedule a follow-up call to debrief and formulate the go-forward strategy. @Jonsi Stephenson

## Related Customers

- [[Microsoft]]
- [[OpenAI]]
- [[Google]]

## Related Projects

- [[Pricing]]
- [[OpenAI VAST POC (CoreWeave cluster)]]
- [[Cloud]]
- [[VAST on Azure Integration]]
- [[Polaris]]
- [[Project Stargate]]
- [[VIP/Failover Design (GCP RDMA)]]
- [[GCP MVP]]

## Related

- [[VAST Data]]
