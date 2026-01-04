---
type: "customer"
title: "Walmart lakehouse pilot prep"
date: "2025-11-06"
account: "Walmart"
participants: ["Mikey", "Brett", "Jason Vallery", "Matt", "Avi", "Lior", "Jer", "Paul", "John Heidgerken", "Siyash"]
source: "transcript"
source_ref: "Inbox/_archive/2025-11-06/2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake.md"
tags:
  - "type/customer"
  - "account/walmart"
  - "generated"
---

# Walmart lakehouse pilot prep

**Date**: 2025-11-06
**Account**: [[Walmart]]
**Attendees**: Mikey, Brett, Jason Vallery, Matt, Avi, Lior, Jer, Paul, John Heidgerken, Siyash

## Summary

Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team. Walmart runs dot-com on Azure and enterprise analytics on GCP (BigQuery/GCS) and wants a consistent hybrid lakehouse view across GCP and two on-prem sites, starting with a Q4 pilot of two VAST clusters. Key risks are extreme scale and replication rates (targeting ~10%/day, estimated ~5 Tbps sustained), >30ms latency between on-prem sites, and product gaps around GCS API compatibility, change-feed integration, and stronger consistency/write-lease semantics.
## Decisions
- Use SyncEngine for the pilot to replicate from GCS to on-prem VAST clusters.
- Pursue GCS API compatibility on the roadmap; S3 alone is insufficient for Walmart.
- Focus the pilot on real Walmart workloads (tables/queries), not synthetic benchmarks.
- Consolidate questions and send to Walmart before scheduling the design session.

## Key Information
- Walmart uses Azure for dot-com systems and GCP (BigQuery/GCS) for enterprise analytics.
- Walmart goal is to repatriate analytics to two on-prem sites while maintaining a consistent lakehouse view across GCP and both sites.
- Immediate ask is two VAST clusters (Region 1 and Region 2) in Q4 for pilot testing.
- Scale discussed: ~400 PiB (~450 PB) initially, growing to ~700 PiB (~770 PB) by 2029.
- Daily replication target discussed: ~10% of the lake from GCP to on-prem; estimated sustained replication throughput ~5 Tbps; prior discussions included up to ~10 Tbps targets and ~100 PB/month change rates.
- Two on-prem data centers run active-active with >30 ms latency; deep fiber interconnect capacity is unclear.
- Workloads mentioned include Trino/Presto and Spark; table formats include Delta and Hudi; BigQuery remains the access layer in GCP.
- Walmart has significant code written against GCS APIs and is pushing for GCS-compatible access on-prem; S3-only is not acceptable long-term.
- Pilot timeframe discussed as now through roughly Sep/Oct next year; 2027 is the target year for full project if approved; budgets finalize end of next calendar year.
- Walmart is expected to lean on VAST to help draft the pilot test plan, but meaningful validation requires Walmart to provide real datasets/schemas and representative queries.

---

*Source: [[Inbox/_archive/2025-11-06/2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake.md|2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]]*

## Related

- [[Google]]
- [[Microsoft]]
- [[Amazon]]
- [[GCP]]
- [[John Heidgerken]]
- [[Lior Genzel]]
- [[Andy Perlsteiner]]
