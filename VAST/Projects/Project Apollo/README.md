---
type: projects
title: Project Apollo
created: '2026-01-03'
last_updated: ''
status: active
auto_created: true
tags:
- type/projects
- needs-review
- status/active
last_contact: '2025-10-28'
---

# Project Apollo

## Overview

AKS-led initiative to build a slimmed-down Azure control plane/topology for single-tenant GPU sites (lease power/space) without full Azure region overhead; potential path to make VAST the standard storage for Apollo deployments via a thin VAST control plane integration.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | AKS team (Microsoft) |

## Current Blockers

- ❌ Azure Storage lacks a deployable solution for Apollo-like sites without full Azure region dependencies
- ❌ Control plane integration hurdles for first-party managed services and Azure Storage Resource Provider coupling
- ❌ Azure internal politics/P&L incentives (Compute vs Storage) may resist third-party storage adoption
- ❌ Early days; Microsoft teams have not coalesced on a clear strategy
- ❌ Azure region control plane and networking stack complexity limits deployment model

## Next Steps

- [ ] Use Kushal/MAI opportunity to create a wedge and open Apollo storage integration discussions
- [ ] Stay close with Lior and Tiffany to advance Apollo storage integration option
- [ ] Map Azure stakeholders across AKS/Apollo, Storage, Compute, and Hardware and their priorities
- [ ] Align MAI storyline with Kubernetes-led control plane framing
- [ ] Engage MAI PM owner (Kushal Datta) and Kubernetes leadership to position VAST + Polaris

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Tiffany]] |  |  |
| [[Vipin]] |  | Microsoft |
| [[Kushal Datta]] |  |  |
| [[Alon Horev]] |  |  |
| [[Keek]] |  | Microsoft |
| [[Lior Genzel]] |  |  |
| [[Anson]] |  | Microsoft |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Pursue dual-track go-to-market: marketplace offer for enterprise bursts plus sell-to hyperscaler-scale deals.
- ✅ Use routable IPs for GCP MVP; defer alias IPs/SaaS Runtime until post-launch.
- ✅ Adapt Enscale solution/deck for Microsoft/MAI with Kubernetes-led control plane and Polaris emphasis.
- ✅ Retain contractual control to avoid feature lock-out/abstraction in any Enscale/CoreWeave-like resale.

## Key Facts

- MAI Falcon plan includes Phoenix, Dallas, and Richmond sites (~40k GPUs per site) connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI struggles to use Falcon capacity due to control plane fragility and GPU issues.
- OpenAI GPT-4.5 training reportedly took ~9 months across multi-islands and up to ~100k H100s; outcome described as disappointing, shifting away from ever-bigger clusters.
- MAI is exploring online RL continuous learning loops with ~60s feedback cycles (trainers in Phoenix, generators elsewhere).
- Vipin values VAST features (global namespace, quotas, capacity estimation, QoS) and acknowledges Blob cannot match VAST performance.
- Marketplace VM offers (Lsv4/v5) are not price-performance competitive for VAST at scale; hardware qualification is viewed as the long-term path.
- Azure Hardware qualification for first-party SKUs is a multi-year effort; liquid-cooled storage SKUs could help with data center cooling fungibility and late-binding storage vs GPU rack decisions.
- Blob API is largely Microsoft-specific; S3 compatibility is broadly attractive; multi-protocol (Blob + S3) could broaden appeal but faces Azure control plane integration hurdles.
- GCP MVP will use routable IPs; customer must provide an IP range.
- GCP v1 performance observed: ~90% of theoretical read and ~50–60% of theoretical write; no standardized KPIs defined yet.

## Topics / Themes

Microsoft AI (MAI) org landscape and stakeholders, Falcon capacity rollout and AI WAN, MAI control plane fragility and GPU utilization constraints, Project Apollo (AKS-led slim control plane) and storage integration, Azure internal politics (Compute vs Storage incentives), Azure hardware qualification path and timelines, Liquid-cooled storage SKUs and data center cooling fungibility, Blob API vs S3 compatibility and multi-protocol strategy, Using MAI success as a wedge for broader Azure adoption, Dual-track cloud go-to-market (marketplace vs hyperscaler whales), GCP MVP launch readiness (networking, deployment flow, demos), Collateral gaps and product marketing deliverables, Standardized performance/TCO benchmarking and KPI framing, Marketplace private offers and pricing component tuning, Maintenance handling, HA, and failure domain behavior

## Related People

- [[Tiffany]]
- [[Vipin]]
- [[Kushal Datta]]
- [[Alon Horev]]
- [[Keek]]
- [[Lior Genzel]]
- [[Anson]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

## Recent Context

- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] - Cloud BU leadership aligned on a dual-track cloud strategy: ship a near-term GCP marketplace MVP wit... (via Cloud)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *