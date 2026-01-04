---
type: people
title: Ronnie Borker
created: '2026-01-03'
last_contact: '2025-10-30'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Ronnie Borker

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Runs Azure hardware |
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
WHERE !completed AND contains(text, "Ronnie Borker")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@RonnieBorker") AND !completed
SORT due ASC
```

## Key Facts

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

Microsoft AI (MAI) org landscape and stakeholders, Falcon capacity rollout and AI WAN, MAI control plane fragility and GPU utilization constraints, Project Apollo (AKS-led slim control plane) and storage integration, Azure internal politics (Compute vs Storage incentives), Azure hardware qualification path and timelines, Liquid-cooled storage SKUs and data center cooling fungibility, Blob API vs S3 compatibility and multi-protocol strategy, Using MAI success as a wedge for broader Azure adoption, MAI meeting preparation and testing plan, Hardware vs VM support timeline, External sharing constraints for Azure Blob data, Deck improvements: observability and CSI driver, Microsoft internal politics and stakeholder management, Engaging Azure hardware leadership via sponsorship

## Recent Context

- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)
- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)

## Profile

**Role**: CVP (Azure hardware platform / datacenter hardware) at Microsoft (Azure hardware)
**Relationship**: Target stakeholder at Microsoft for hardware engagement

**Background**:
- Owns end-to-end Azure datacenter hardware platform; potential path for hardware-optimized Azure deployments; intro ideally sponsored by another CVP (e.g., Nidhi).
- Key stakeholder for qualifying hardware SKUs in Azure; seen as the path to get a VAST-friendly storage-optimized SKU qualified (multi-year effort).

## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Do not include non-public Azure BLOB performance data in externally shared decks.
- ✅ Emphasize observability (single pane of glass) and CSI driver in the MAI deck.
- ✅ Pursue parallel strategy: marketplace SaaS maturity and first-party hardware-optimized wins.
- ✅ Near-term focus: Azure first-party opportunities (MAI, UK Met); OCI as secondary; AWS deprioritized for SC.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *