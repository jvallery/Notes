---
type: people
title: Brett Tanzer
created: '2026-01-03'
last_contact: '2025-11-06'
auto_created: true
tags:
- type/people
- needs-review
---

# Brett Tanzer

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | _Unknown_ |
| **Company** | _Unknown_ |
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
WHERE !completed AND contains(text, "Brett Tanzer")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@BrettTanzer") AND !completed
SORT due ASC
```

## Key Facts

- Walmart uses Azure for dot-com systems and GCP (BigQuery/GCS) for enterprise analytics.
- Walmart wants a consistent lakehouse view across GCP and two on-prem sites; two on-prem DCs run active-active with >30 ms latency.
- Immediate ask: two VAST clusters (Region 1/Region 2) in Q4 for pilot testing.
- Scale: ~450 PB initially, growing to ~770 PB by 2029.
- Replication target: ~10% of the lake per day from GCP to on-prem; estimated sustained ~5 Tbps; prior discussions included up to ~10 Tbps targets and ~100 PB/month change rate claims.
- Walmart prefers GCS-compatible APIs; S3-only access is not acceptable long-term.
- Near-term architecture direction: SyncEngine for near-real-time replication from GCS plus DataSpaces across on-prem sites; gaps include GCS API endpoint, stronger consistency/write-lease semantics, and GCS change-feed integration.
- Pilot timeline: now through roughly Sep/Oct next year; decision frame for full project in calendar year 2027; budgets finalize end of next calendar year.
- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.

## Topics Discussed

Walmart hybrid lakehouse architecture (GCP + two on-prem sites), SyncEngine replication from GCS to on-prem, DataSpaces/global namespace across on-prem sites, GCS API compatibility requirement, Strong consistency challenges and write-lease semantics, Network throughput/egress feasibility for multi-Tbps replication, Pilot/POC scoping using real workloads (Trino/Presto, Spark; Delta/Hudi tables), Governance, multi-tenancy, auditing, and compliance requirements, BigQuery interoperability considerations, Q4 pilot cluster configurations (Region 1/Region 2), Azure GTM path for VAST storage (BizDev-led engagement), VAST density/power advantages vs Azure Blob and Marketplace L-series limitations, OEM/ODM hardware path into Azure data centers and Apollo decision-making, Azure Extended Zones (network-only) and AKS NodeJoin (ACAS FlexNode) GA proposal, MAI/Falcon operational issues: topology-aware scheduling, IB telemetry, reliability

## Recent Context

- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d... (via Walmart)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Key Decisions

- ✅ Use SyncEngine for the pilot to replicate from GCS to on-prem VAST clusters.
- ✅ Pursue GCS API compatibility on the roadmap; S3 alone is insufficient for Walmart.
- ✅ Focus the pilot on real Walmart workloads (tables/queries), not synthetic benchmarks.
- ✅ Consolidate questions and send to Walmart before scheduling the design session.
- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Related




---
*Last updated: *