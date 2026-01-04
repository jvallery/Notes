---
type: customer
title: Walmart hybrid analytics requirements
date: '2025-11-05'
account: Walmart
participants:
- Walmart
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-05 - Walmart Analytics.md
tags:
- type/customer
- account/walmart
- generated
---

# Walmart hybrid analytics requirements

**Date**: 2025-11-05
**Account**: [[Walmart]]
**Attendees**: Walmart

## Summary

Walmart described a hybrid analytics requirement where data is ingested/processed in BigQuery on GCP and a hot working set must be replicated into two Walmart-managed facilities, targeting active/active behavior. Key challenges include achieving strong consistency under high write rates across ~30+ ms latency sites, minimizing refactoring by supporting a GCS-like API on-prem, and handling very large scale (~500 PiB lake, ~10% daily churn). A VAST POC is ready to begin with a decision targeted by end of CY26 and a roadmap to close gaps by ~Oct 2026 ahead of holiday code freeze and Jan 2027 budget cycles.
## Key Information
- Primary ingestion and processing is in BigQuery on GCP.
- A hot working set must be replicated into two Walmart-owned/managed facilities for further processing/analytics.
- Target topology is active/active across GCP and two on-prem sites; the two on-prem sites are ~30+ ms apart.
- Minimum replication approach is to bring down the hot working set via VAST SyncEngine.
- Desired state is strong consistency between on-prem storage and cloud, but high write rates make this challenging.
- Workload can tolerate latency and small amounts of data loss during network unavailability.
- Analytics compute frameworks include Trino/Presto and Spark.
- Multiple business units run jobs on centrally managed infrastructure (multi-tenant).
- There is heavy existing usage of the GCS JSON API; strong preference for a native GCS-like API on-prem to avoid refactoring.
- Total data lake is ~500 PiB with ~10% daily churn (~50 PiB/day) needing to be streamed from cloud to on-prem.
- POC/pilot of VAST is ready to begin; decision goal is by end of CY26.
- Partial solution is acceptable now, but roadmap gaps should be closed by ~Oct 2026 before holiday code freeze to support Jan 2027 budget cycles.
- Open questions include defining the hot working set, table formats (e.g., Hudi/Delta/Iceberg), change detection mechanism, precise consistency/RPO/RTO targets, write locality, replication bandwidth feasibility, physical interconnects, GCS API subset requirements, catalog strategy, federation vs materialization, multi-tenant isolation, compliance posture, POC success criteria, and roadmap dependencies by Oct 2026.
- Public info suggests Walmart selected Apache Hudi for its lakehouse and runs large-scale Trino and Spark workloads on GCP.

---

*Source: [[Inbox/Transcripts/2025-11-05 - Walmart Analytics.md|2025-11-05 - Walmart Analytics]]*

## Related

- [[Google]]
