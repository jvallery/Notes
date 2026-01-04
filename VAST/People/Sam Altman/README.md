---
type: people
title: Sam Altman
created: '2026-01-03'
last_contact: '2025-10-28'
auto_created: true
tags:
- type/people
- needs-review
- company/openai
---

# Sam Altman

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** | OpenAI |
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
WHERE !completed AND contains(text, "Sam Altman")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@SamAltman") AND !completed
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
- Team offsite planned in Silicon Valley on 2025-10-15 for ~1.5 days; casual sessions plus social/dinner; release around noon on day 2.
- Goal is a distributed cache strategy covering fan-out writes, fan-out reads, fan-in reads, and separately KV cache.

## Topics Discussed

Microsoft AI (MAI) org landscape and stakeholders, Falcon capacity rollout and AI WAN, MAI control plane fragility and GPU utilization constraints, Project Apollo (AKS-led slim control plane) and storage integration, Azure internal politics (Compute vs Storage incentives), Azure hardware qualification path and timelines, Liquid-cooled storage SKUs and data center cooling fungibility, Blob API vs S3 compatibility and multi-protocol strategy, Using MAI success as a wedge for broader Azure adoption, Distributed cache strategy and decision framework, MAI checkpointing approach (local NVMe + async copy), BlobFuse private preview scope and readiness, Manifold/Singularity cache and consistent hashing, OpenAI TensorCache stability and roadmap (GPT-6 memory focus), Metadata/index store strategy (build vs open source like FoundationDB)

## Recent Context

- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)
- 2025-09-15: [[2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]] - Weekly 1:1 between Jason Vallery and Jai Menon focused on choosing a distributed cache strategy (Blo... (via Jai Menon)

## Profile

**Role**: OpenAI
**Relationship**: External industry figure

**Background**:
- Referenced in context of OpenAI leadership turmoil/board coup influencing Microsoft's first-party frontier model strategy.
- Publicly stated GPT-6 engineering focus is memory/long context, implying churn in caching layers.

## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Jason should book travel to attend the Oct 15 Silicon Valley team offsite.

## Related Customers

- [[OpenAI]]

## Related




---
*Last updated: *