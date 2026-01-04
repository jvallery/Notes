---
type: people
title: Mordechai Blaunstein
created: '2026-01-03'
last_contact: "2025-11-07"
auto_created: true
tags:
- type/people
- needs-review
---

# Mordechai Blaunstein

## Profile

**Role**: Product/program (between product and program; not highly technical) at VAST Data (Product / Program (current reporting line to Alon))
**Relationship**: Internal collaborator / potential direct report

**Background**:
- Referred to as 'Morty' and also as a potential new direct report; alignment needed on second-tier cloud coverage.
- Described as not technical; good at blocking/tackling and good with customers.
- Referred to as 'Morty'; owns Neo-cloud feature requirements; will support author's area but must maintain Neo-cloud coverage; should be pulled into follow-up with alliances on cloud-in-a-box/control-plane partners.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Mordechai Blaunstein")
SORT due ASC
```

## Recent Context

- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)
- 2025-10-28: [[2025-10-28 - Jason and Shachar aligned on setting a weekly 30-minute 11 and planning Jason’s]] - Weekly 30-minute 1:1 cadence was established between Jason Vallery and Shachar Feinblit, and they pl... (via Shachar Feinblit)
- 2025-10-27: [[2025-10-27 - Jason and Jeff aligned on near-term focus synthesize a cloud pipeline view and]] - Weekly 1:1 between Jason Vallery and Jeff Denworth aligning near-term cloud priorities: build a synt... (via Jeff Denworth)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Shachar Feinblit]] - Checklist and Slack snippets related to coordinating with Shachar Feinblit, including setting up rec... (via Shachar Feinblit)

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

## Background

Over 28 years of experience in the technology sector, holding leadership roles in product management, technical business development, and marketing at companies such as NeuroBlade, SolidRun, Marvell Technology, Lightbits Labs, and Sandisk.

## Key Decisions

- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.
- ✅ Begin sizing work starting with testing projections, then customer projections.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.
- ✅ Do not run an OpenAI alignment session until OpenAI engages.
- ✅ Primary focus is Microsoft while simultaneously investing in a Google TPU strategy.
- ✅ Lior Genzel focuses on hyperscalers and also has sell-to obligations; Mordechai Blaunstein covers second-tier clouds.

## Related Projects

- [[Cloud]]

## Related

---
*Last updated: *
