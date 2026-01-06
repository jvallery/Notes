---
type: customer
title: Walmart
account_type: customer
status: Active
industry: Retail
my_role: ''
last_contact: '2025-12-23'
created: '2026-01-05'
tags:
- type/customer
- status/active
- needs-review
---

# Walmart

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Industry** | Retail |

## Key Contacts

- [[Jeff Denworth]]
- [[Mikey]]

## Open Tasks

```tasks
path includes VAST/Customers and Partners/Walmart/
not done
```

## Recent Context

- 2025-12-23: [[2025-12-23 - Walmart requirements reset- hybrid namespace, GCS integration, Alluxio risk]]
- 2025-11-14: [[2025-11-14 - Walmart big data DR requirements gating architecture session; plan Mingming expectations call]]
- 2025-11-06: [[2025-11-06 - Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 two-cluster pilot]]
- 2025-11-05: [[2025-11-05 - Walmart Analytics hybrid replication requirements GCP BigQuery to two on-prem sites]]
- 2025-11-05: [[2025-11-05 - Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with active-active and GCS API compatibility]]

- 2025-12-23: Mentioned in: Walmart restates hybrid requirements, rejects disjoint namespaces, GCS integration required
## Key Facts

- Walmart’s enterprise analytics system-of-record is GCP (BigQuery + GCS); their operational systems are Azure.
- Target architecture is hybrid: replicate a hot working set from GCP to two Walmart-managed on-prem sites and present a single interaction model across environments.
- Two on-prem sites are active-active with ~30ms+ latency; long-term goal is strong consistency, with pragmatic tradeoffs for high write rates.
- Walmart strongly prefers a GCS-compatible API surface; S3-only compatibility is insufficient.
- Scale assumptions discussed are exabyte-class over time, with multi-terabit/day replication targets driving feasibility questions.

- Walmart held an internal requirements meeting during the week of 2025-12-22 and restated that they need a long-term hybrid solution for their data team.

- Walmart was not successful in getting the business to accept operating with two disjoint namespaces, indicating a requirement for a unified namespace across environments.

- Walmart plans to start an internal big data proof of concept (POC) sometime in 2026, but only for workloads that can exclusively run on premises.

- Walmart requires integration with Google Cloud Storage (GCS) for any solution they move forward with, or would need significant lobbying at the database layer including potentially adopting a hybrid cloud database.

- Jeff Denworth warned that Walmart's GCS integration requirement could put Alluxio back in a leading position for the account and that VAST should be careful.
## Topics

- Hybrid lakehouse architecture (GCP → two on-prem sites)
- GCS API compatibility and developer experience
- Replication throughput, consistency model, and pilot scope/criteria
