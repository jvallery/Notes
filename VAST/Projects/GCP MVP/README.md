---
type: projects
title: GCP MVP
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

# GCP MVP

## Overview

Near-term Google Cloud marketplace MVP launch; requires routable IP deployment flow, demos, collateral, QA/support readiness, maintenance handling, and marketplace offer activation/pricing tuning.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | _Unknown_ |

## Current Blockers

- ❌ Collateral gaps (customer/internal/CSP seller decks, battlecards, datasheets)
- ❌ Insufficient time for QA/testing and support readiness
- ❌ Deployment preflight gaps; customer environment variability
- ❌ Marketplace pricing components need tuning; risk of activation delays
- ❌ Maintenance concurrency across failure domains could impact redundancy/perf if not serialized

## Next Steps

- [ ] Implement deployment flow requiring customer-provided IP range (routable IPs)
- [ ] Produce end-to-end demo video (Polaris CLI/UI deployment and end state) for booths
- [ ] Tune marketplace private offer components and confirm no new approvals needed
- [ ] Validate maintenance handling via VM migration/serialization across failure domains
- [ ] Ramp QA/support playbooks including break-glass procedures
- [ ] Ask Google about maintenance overlap guarantees across failure domains and document guidance

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |
| [[Lior Genzel]] |  |  |
| [[Ronnie Lazar]] |  | VAST Data |
| [[Eirikur Hrafnsson]] |  |  |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Shachar Feinblit]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Pursue dual-track go-to-market: marketplace offer for enterprise bursts plus sell-to hyperscaler-scale deals.
- ✅ Use routable IPs for GCP MVP; defer alias IPs/SaaS Runtime until post-launch.
- ✅ Adapt Enscale solution/deck for Microsoft/MAI with Kubernetes-led control plane and Polaris emphasis.
- ✅ Retain contractual control to avoid feature lock-out/abstraction in any Enscale/CoreWeave-like resale.

## Key Facts

- GCP MVP will use routable IPs; customer must provide an IP range.
- GCP v1 performance observed: ~90% of theoretical read and ~50–60% of theoretical write; no standardized KPIs defined yet.
- Google has 8 failure domains; Azure typically has 3, impacting usable capacity/performance for HA designs.
- Marketplace activation expected to leverage an existing blanket private offer to avoid new approvals; pricing components still need tuning.
- MAI opportunity discussed at ~160,000 GPUs; follow-up planned Friday; storyline/deck due by Friday.
- Supercomputing presence includes VAST booth plus Google and Microsoft booths; ~10 end-user cloud meetings planned.
- Key dates: Ignite 2025-11-18 to 2025-11-21; re:Invent 2025-12-01 to 2025-12-05; planned Iceland trip 2025-12-08.

## Topics / Themes

Dual-track cloud go-to-market (marketplace vs hyperscaler whales), GCP MVP launch readiness (networking, deployment flow, demos), Collateral gaps and product marketing deliverables, Standardized performance/TCO benchmarking and KPI framing, Marketplace private offers and pricing component tuning, Maintenance handling, HA, and failure domain behavior, QA/support readiness and break-glass procedures, Microsoft MAI supercomputing opportunity and Enscale storyline adaptation, Kubernetes-led control plane concept (Project Apollo) and Polaris lifecycle management, Risk of resale lock-in/feature abstraction (CoreWeave-style)

## Related People

- [[John Downey]]
- [[Lior Genzel]]
- [[Ronnie Lazar]]
- [[Eirikur Hrafnsson]]
- [[Jonsi Stephenson]]
- [[Shachar Feinblit]]
- [[Jason Vallery]]

## Related Customers

- [[Google]]

## Recent Context

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