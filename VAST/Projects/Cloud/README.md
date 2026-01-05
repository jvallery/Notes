---
type: projects
title: Cloud
status: active
my_role: owner
description: Cloud platform strategy, multi-tenancy, operability, and marketplace readiness across hyperscalers.
last_contact: '2025-12-15'
created: '2026-01-05'
tags:
- type/projects
- status/active
- needs-review
---

# Cloud

**Owner**: Jason Vallery

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |
| **My Role** | owner |

## Overview

Workstream for VAST on Cloud: platform primitives, control plane stance, tenancy, operability/SLOs, and marketplace transactability.

## Open Tasks

```tasks
path includes VAST/Projects/Cloud/
not done
```

## Recent Context

- 2026-01-05: [[2026-01-05 - VAST Cloud SaaS operating model requirements draft DevOps, telemetry, 24x7 support]]
- 2025-12-15: [[2025-12-15 - Review requested- VAST on Cloud Course and Project Brief feedback due January 7, 2026]]
- 2025-11-14: [[2025-11-14 - Google Distributed Cloud RFP debrief and federal coordination air-gapped focus]]
- 2025-10-30: [[2025-10-30 - Cloud operations org design- distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target]]
- 2025-10-30: [[2025-10-30 - Cloud marketplace support operating model, hyperscaler priority, and readiness plan target 2026-02-01]]
- 2025-10-29: [[2025-10-29 - VAST on Cloud positioning, intake process, and near-term roadmap constraints VM shapes, marketplace automation, object storage integration]]
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligns on dual-track GTM- GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline]]

## Key Facts

- No generally available, transactable “VAST on Cloud” offering exists today; current work is roadmap plus early marketplace/private-offer motions.
- FY26 prioritization is core layers first (cloud primitives, control plane stance, tenancy, operability/SLOs) before building higher-layer services.
- Marketplace offers are necessary for transactability, but VM economics can be non-competitive at scale; longer-term paths include cloud primitives and potentially CSP data-center hardware.
- Multi-tenancy gaps exist; a key blocker is limited identity provider scale and tenant-scoping constraints.
- Preferred architecture is hyperscaler object storage as the durable system of record, with VAST providing compute-adjacent caching and global namespace access.
- Control plane requirements include entitlements/fulfillment notifications and metering integration (e.g., marketplace/private offers).
- Google Distributed Cloud (GDC) is a strategic opportunity: Google issued a US-based RFP to replace NetApp for Distributed Cloud deployments.
- Hybrid-scale customer requirements (e.g., Walmart) drive deeper native cloud object integration expectations (especially GCS API compatibility).

## Topics

- Multi-tenancy and tenant-scoped auth/quotas
- Control plane, fulfillment, metering, and marketplace operations
- Operability, SLOs, support model, and release readiness
- Cloud primitives (storage tiers, metadata persistence, QoS/governance)
- GTM positioning: global namespace + data mobility vs raw storage economics

## Key Decisions

- Prioritize core cloud layers before higher-layer services.
- Use an explicit operating cadence and decision log to reduce churn and speed decisions.
