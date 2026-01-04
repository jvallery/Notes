---
type: people
title: Ronnie Booker
created: '2026-01-03'
last_contact: '2025-10-27'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Ronnie Booker

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Owns chassis/layout/storage placement decisions for Apollo deployments |
| **Company** | Microsoft |
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
WHERE !completed AND contains(text, "Ronnie Booker")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RonnieBooker") AND !completed
SORT due ASC
```

## Key Facts

- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.
- VAST vs Azure Blob per 1 EB: ~1/10 racks, ~1/5 megawatts, >=5x performance, but ~2x capex.
- Azure Marketplace VAST offer on L-series VMs is not density/cost competitive for real workloads; positioned as a checkbox.
- Apollo ownership boundaries: Chi owns bare-metal control plane; Sky/Overlake owns security; Ronnie Booker’s org owns chassis/layout/storage placement decisions.
- Azure MAI/Falcon issues include lack of topology-aware scheduling; rack-level placement not expected until ~Feb; IB/telemetry improving.
- OpenAI infra leadership changed: Uday (ex-xAI) now runs infra at OpenAI and reports to Greg Brockman; may reduce Microsoft alignment; power is a major Azure constraint.
- Kurt expected A2N approval for Extended Zones/NodeJoin in ~3 weeks; target partners include sovereign/neo-clouds such as sakura.net in Japan.


- MAI Falcon plan includes Phoenix, Dallas, and Richmond sites (~40k GPUs per site) connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI struggles to use Falcon capacity due to control plane fragility and GPU issues.
- OpenAI GPT-4.5 training reportedly took ~9 months across multi-islands and up to ~100k H100s; outcome described as disappointing, shifting away from ever-bigger clusters.
- MAI is exploring online RL continuous learning loops with ~60s feedback cycles (trainers in Phoenix, generators elsewhere).
- Vipin values VAST features (global namespace, quotas, capacity estimation, QoS) and acknowledges Blob cannot match VAST performance.
- Marketplace VM offers (Lsv4/v5) are not price-performance competitive for VAST at scale; hardware qualification is viewed as the long-term path.
- Azure Hardware qualification for first-party SKUs is a multi-year effort; liquid-cooled storage SKUs could help with data center cooling fungibility and late-binding storage vs GPU rack decisions.
- Blob API is largely Microsoft-specific; S3 compatibility is broadly attractive; multi-protocol (Blob + S3) could broaden appeal but faces Azure control plane integration hurdles.
- MAI contact requested to start testing immediately and prefers functional access now.
- Current support requires pre-certified hardware; VM support expected in December and only for small VMs.
## Topics Discussed

Azure GTM path for VAST storage (BizDev-led engagement), VAST density/power advantages vs Azure Blob and Marketplace L-series limitations, OEM/ODM hardware path into Azure data centers and Apollo decision-making, Azure Extended Zones (network-only) and AKS NodeJoin (ACAS FlexNode) GA proposal, MAI/Falcon operational issues: topology-aware scheduling, IB telemetry, reliability, Power constraints as primary bottleneck and translating storage savings into GPUs, OpenAI leadership changes and implications for Microsoft alignment, Supercomputing conference coordination and intros


Microsoft AI (MAI) org landscape and stakeholders, Falcon capacity rollout and AI WAN, MAI control plane fragility and GPU utilization constraints, Project Apollo (AKS-led slim control plane) and storage integration, Azure internal politics (Compute vs Storage incentives), Azure hardware qualification path and timelines, Liquid-cooled storage SKUs and data center cooling fungibility, Blob API vs S3 compatibility and multi-protocol strategy, Using MAI success as a wedge for broader Azure adoption, MAI meeting preparation and testing plan, Hardware vs VM support timeline, External sharing constraints for Azure Blob data, Deck improvements: observability and CSI driver, Microsoft internal politics and stakeholder management, Engaging Azure hardware leadership via sponsorship
## Recent Context

- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)


- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)
- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)
## Profile

**Role**: Owns chassis/layout/storage placement decisions for Apollo deployments at Microsoft
**Relationship**: Key Microsoft decision-maker to engage

**Background**:
- Key decision-maker for what goes in the data center (chassis design, layout, storage placement). Identified as the right target vs Nidhi/Manish for hardware/OEM storage-dense path.

## Key Decisions

- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Microsoft BizDev Education & Intros to Ronnie]]

## Related




---
*Last updated: *