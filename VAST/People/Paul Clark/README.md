---
type: people
title: Paul Clark
created: '2026-01-03'
last_contact: '2025-11-06'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Paul Clark

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Runs CO&I/CNLI (Azure datacenter org; per transcript) |
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
WHERE !completed AND contains(text, "Paul Clark")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@PaulClark") AND !completed
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
- MAI contact requested to start testing immediately and prefers functional access now.
- Current support requires pre-certified hardware; VM support expected in December and only for small VMs.

## Topics Discussed

Walmart hybrid lakehouse architecture (GCP + two on-prem sites), SyncEngine replication from GCS to on-prem, DataSpaces/global namespace across on-prem sites, GCS API compatibility requirement, Strong consistency challenges and write-lease semantics, Network throughput/egress feasibility for multi-Tbps replication, Pilot/POC scoping using real workloads (Trino/Presto, Spark; Delta/Hudi tables), Governance, multi-tenancy, auditing, and compliance requirements, BigQuery interoperability considerations, Q4 pilot cluster configurations (Region 1/Region 2), MAI meeting preparation and testing plan, Hardware vs VM support timeline, External sharing constraints for Azure Blob data, Deck improvements: observability and CSI driver, Microsoft internal politics and stakeholder management

## Recent Context

- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d... (via Walmart)
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)

## Profile

**Role**: Runs CO&I/CNLI (Azure datacenter org; per transcript) at Microsoft (CO&I)
**Relationship**: Microsoft infrastructure leader (context)

**Background**:
- One of three CVPs responsible for building/delivering Azure infrastructure capacity.

## Key Decisions

- ✅ Use SyncEngine for the pilot to replicate from GCS to on-prem VAST clusters.
- ✅ Pursue GCS API compatibility on the roadmap; S3 alone is insufficient for Walmart.
- ✅ Focus the pilot on real Walmart workloads (tables/queries), not synthetic benchmarks.
- ✅ Consolidate questions and send to Walmart before scheduling the design session.
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