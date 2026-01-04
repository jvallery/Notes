---
type: projects
title: Enscale deck
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

# Enscale deck

## Overview

Adapt Enscale solution/deck to support Microsoft/MAI storyline; emphasize Kubernetes-led control plane and Polaris-managed operations; avoid CoreWeave-style lock-in in any resale.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | _Unknown_ |

## Current Blockers

- ❌ Need rapid internal working session and updated storyline/diagram/deck by Friday

## Next Steps

- [ ] Run internal working session with Enscale technical team
- [ ] Deliver MAI presentation aligned to Kubernetes/Polaris

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Alon Horev]] |  |  |
| [[Asaf Levy]] |  |  |
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

- [[Alon Horev]]
- [[Asaf Levy]]
- [[Jason Vallery]]

## Related Customers

- [[Microsoft]]

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