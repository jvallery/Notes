---
type: projects
title: OVA
last_contact: "2025-11-06"
created: '2026-01-03'
tags:
- type/projects
- generated
---

# OVA

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Josh Wentzell |

## Overview

VAST OVA needed along with onboarding materials for local lab testing.

## Open Tasks

```tasks
path includes OVA
not done
```

## Recent Context

- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d... (via Walmart)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo]] - Introductory 1:1 with Josh Wentzell to align on VAST on Cloud strategy and identify platform gaps, e... (via Josh Wentzell)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m... (via Eyal Traitel)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-10-27: [[2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]] - Group meeting transcript debating how to align VAST cloud pricing with the new on-prem core+capacity... (via Pricing)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on accelerating AI-first software developme... (via Tomer Hagay)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on improving VAST engineering maturity and ... (via Tomer Hagay)
- 2025-09-30: [[2025-09-30 - Jason shared he has multiple external management opportunities and plans to deci]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s potential departure from Microsoft... (via Jai Menon)
- unknown: [[2025-10 - Josh Wentzell]] - Follow-up task to contact Josh Wentzell (Office of the CTO) to obtain VAST OVA and onboarding materi... (via Josh Wentzell)
- unknown: [[2025-10 - Learning]] - Checklist items for Platform Learning focused on setting up a local VAST OVA environment and deepeni... (via Platform Learning)

## Key Facts

- Walmart uses Azure for dot-com systems and GCP (BigQuery/GCS) for enterprise analytics.
- Walmart wants a consistent lakehouse view across GCP and two on-prem sites; two on-prem DCs run active-active with >30 ms latency.
- Immediate ask: two VAST clusters (Region 1/Region 2) in Q4 for pilot testing.
- Scale: ~450 PB initially, growing to ~770 PB by 2029.
- Replication target: ~10% of the lake per day from GCP to on-prem; estimated sustained ~5 Tbps; prior discussions included up to ~10 Tbps targets and ~100 PB/month change rate claims.
- Walmart prefers GCS-compatible APIs; S3-only access is not acceptable long-term.
- Near-term architecture direction: SyncEngine for near-real-time replication from GCS plus DataSpaces across on-prem sites; gaps include GCS API endpoint, stronger consistency/write-lease semantics, and GCS change-feed integration.
- Pilot timeline: now through roughly Sep/Oct next year; decision frame for full project in calendar year 2027; budgets finalize end of next calendar year.
- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement/training plus PM augmentation, and marketing support.
- Documentation is currently feature/button-oriented and not scenario-driven; scenario guides are ad hoc and late.

## Topics

Walmart hybrid lakehouse architecture (GCP + two on-prem sites), SyncEngine replication from GCS to on-prem, DataSpaces/global namespace across on-prem sites, GCS API compatibility requirement, Strong consistency challenges and write-lease semantics, Network throughput/egress feasibility for multi-Tbps replication, Pilot/POC scoping using real workloads (Trino/Presto, Spark; Delta/Hudi tables), Governance, multi-tenancy, auditing, and compliance requirements, BigQuery interoperability considerations, Q4 pilot cluster configurations (Region 1/Region 2), Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics

## Blockers

- ❌ Need alignment on SyncEngine pattern/lessons from Wave project
- ❌ Unclear GCS change-feed support path for SyncEngine
- ❌ Need for setup guidance/links and practical hands-on validation to surface pain points
- ❌ Networking setup for client access is cumbersome
- ❌ Not officially supported; limited scale and capacity

## Related

<!-- Wikilinks to related entities -->
