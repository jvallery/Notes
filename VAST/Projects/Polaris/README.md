---
type: projects
title: Polaris
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

# Polaris

## Overview

System of record for cloud entitlements, metering/usage reporting, call-home registration, and integration hub with marketplaces and Salesforce/Tackle for the GCP MVP launch.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | _Unknown_ |

## Current Blockers

- ❌ Automation gap: creating Uplink organization endpoints from Salesforce metadata for call-home registration
- ❌ Internal CS/sales alerting for approaching/exceeding entitlements not yet implemented
- ❌ Need to finalize overage handling approach and ensure marketplace/Tackle support (GCP limitations)
- ❌ Need EULA language to enforce overage billing terms in marketplace offers
- ❌ Unclear licensing/packaging for Polaris as VAST-as-a-Service for neoclouds

## Next Steps

- [ ] Implement Salesforce-to-Uplink org endpoint automation for call-home registration
- [ ] Implement internal alerting/dashboards for CS/sales on entitlement usage
- [ ] Confirm overage handling feasibility/configuration with Tackle for GCP
- [ ] Align finance reporting/reconciliation processes with Polaris usage data
- [ ] Clarify licensing/packaging for Polaris as VAST-as-a-Service for neoclouds
- [ ] Ensure demos and decks emphasize Kubernetes-led control plane + Polaris operations

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Eirikur Hrafnsson]] | Meeting participant; coordinating Tackle implementation and GCP MVP launch readiness |  |
| [[Jonsi Stephenson]] | CEO | VAST Data |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Pursue dual-track go-to-market: marketplace offer for enterprise bursts plus sell-to hyperscaler-scale deals.
- ✅ Use routable IPs for GCP MVP; defer alias IPs/SaaS Runtime until post-launch.
- ✅ Adapt Enscale solution/deck for Microsoft/MAI with Kubernetes-led control plane and Polaris emphasis.
- ✅ Retain contractual control to avoid feature lock-out/abstraction in any Enscale/CoreWeave-like resale.

## Key Facts

- MVP launch on GCP uses private offers with fixed capacity pricing ($0.07/GB) via GCP Marketplace.
- Tackle.io is the middleware to generate private offers and sync them with Salesforce opportunities.
- Polaris is the source of truth for entitlements and metering; clusters call home to Polaris and enforce entitlements via tokens (no license keys).
- No BYOL for MVP; all transactions go through marketplaces to support hyperscaler partner status and MDF/marketing benefits.
- Considering ~10% overage allowance; goal is to charge overage at list PAYGO, but GCP Marketplace may not support this natively.
- Internal CS/sales alerting for entitlement usage/overage is not yet in place; customer alert exists.
- First GCP transactions targeted for Nov–Dec 2025; plan to replicate approach to AWS/Azure afterward.
- Finance will not have a separate cloud P&L; cloud metrics will be reported within overall P&L; SaaS/consumption metrics and forecasting model must be defined before full SaaS launch.
- GCP MVP will use routable IPs; customer must provide an IP range.
- GCP v1 performance observed: ~90% of theoretical read and ~50–60% of theoretical write; no standardized KPIs defined yet.

## Topics / Themes

GCP Marketplace MVP launch scope (private offers, fixed capacity, no BYOL), Tackle.io integration with Salesforce for private offers, Polaris entitlements, metering, call-home, and Uplink registration automation, Overage policy and GCP marketplace limitations; PAYGO overage workaround, EULA language requirements for overage billing, Finance processes: billing, payout cadence, reconciliation, reporting controls, rev rec, Future pricing model: VAST units of measurement for compute/capacity, Hybrid on-prem/cloud conversion and revenue recognition complexity, Multi-cloud pooling feasibility and hyperscaler positioning concerns, Need for cloud customer success coverage and internal usage alerting, Dual-track cloud go-to-market (marketplace vs hyperscaler whales), GCP MVP launch readiness (networking, deployment flow, demos), Collateral gaps and product marketing deliverables, Standardized performance/TCO benchmarking and KPI framing, Marketplace private offers and pricing component tuning

## Related People

- [[Eirikur Hrafnsson]]
- [[Jonsi Stephenson]]

## Related Customers

- [[Microsoft]]
- [[Google]]

## Recent Context

- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Internal group meeting to finalize the MVP launch plan for VAST on Google Cloud Marketplace using pr... (via Google)
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