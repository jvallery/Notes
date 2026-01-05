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

## Key Facts

- Walmart’s enterprise analytics system-of-record is GCP (BigQuery + GCS); their operational systems are Azure.
- Target architecture is hybrid: replicate a hot working set from GCP to two Walmart-managed on-prem sites and present a single interaction model across environments.
- Two on-prem sites are active-active with ~30ms+ latency; long-term goal is strong consistency, with pragmatic tradeoffs for high write rates.
- Walmart strongly prefers a GCS-compatible API surface; S3-only compatibility is insufficient.
- Scale assumptions discussed are exabyte-class over time, with multi-terabit/day replication targets driving feasibility questions.

## Topics

- Hybrid lakehouse architecture (GCP → two on-prem sites)
- GCS API compatibility and developer experience
- Replication throughput, consistency model, and pilot scope/criteria
