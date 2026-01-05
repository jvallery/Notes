---
type: "customer"
title: "Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with strong consistency goals"
date: "2025-11-05"
account: ""
participants: ["Unknown"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-05 - Walmart Analytics 2.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with strong consistency goals

**Date**: 2025-11-05
**Account**: [[]]
**Attendees**: Unknown

## Summary

Walmart’s analytics data is ingested and processed in BigQuery on GCP, with a requirement to replicate a hot working set into two Walmart-owned facilities for additional analytics using Trino and Spark. They want an active-active topology across GCP and both on-prem sites, prefer a native GCS JSON API on-prem to avoid refactoring, and are willing to tolerate small data loss during network outages. A VAST POC is ready to start, targeting a decision by end of CY2026 and closure of key gaps by ~October 2026 ahead of holiday code freeze and Jan 2027 budget cycles.


## Action Items


- [?] Define and document Walmart’s 'hot working set' selection criteria (datasets/tables/objects, freshness rules, BU ownership), plus expected daily volume and peak write rates to size SyncEngine replication and on-prem capacity. @TBD ⏫ #task #proposed #auto

- [?] Clarify Walmart’s required consistency semantics (object/file vs partition vs table), and acceptable RPO/RTO for GCP-to-on-prem and on-prem-to-on-prem paths given 30+ ms site latency and high write rates. @TBD ⏫ #task #proposed #auto

- [?] Inventory the exact subset of the GCS JSON API Walmart depends on (auth, signed URLs, resumable uploads, ACLs, metadata semantics) to assess feasibility of a native GCS-like API on-prem or a compatibility layer. @TBD ⏫ #task #proposed #auto

- [?] Quantify network and throughput feasibility for streaming ~50 PiB/day from GCP to on-prem, including existing interconnect capacity, compression/delta strategies, and whether replication can be segmented by BU or dataset. @TBD ⏫ #task #proposed #auto

- [?] Define POC success criteria for the VAST pilot (performance, correctness, failover behavior, operability, and developer compatibility for Trino/Spark and GCS-like access). @TBD #task #proposed #auto






## Key Information


- Walmart’s primary ingestion and processing for this analytics environment is done via BigQuery on Google Cloud Platform (GCP).

- Walmart requires replication of a hot working set of analytics data from GCP into two Walmart-owned and Walmart-managed facilities for further processing and analytics.

- Walmart’s target topology is active-active across Google Cloud Platform and two on-prem Walmart sites, with the two on-prem sites separated by 30+ ms network latency.

- Walmart’s minimum replication requirement is to bring the hot working set down from GCP to on-prem using VAST SyncEngine.

- Walmart’s desired end state is strong consistency between on-prem storage and cloud storage, but high write rates make strong consistency challenging even though the workload is tolerant of latency.

- Walmart’s workload can tolerate small amounts of data loss during network unavailability.

- Walmart’s analytics compute frameworks include Trino, Spark, and similar analytics tools, with multiple business units running jobs on centrally managed infrastructure.

- Walmart wants a single interaction model with SDKs and tools that are agnostic to whether workloads run on-prem or in GCP.

- Walmart has significant existing code and tooling that deeply leverages the Google Cloud Storage (GCS) JSON API and strongly prefers a native GCS-like API on-prem to avoid refactoring.

- Walmart’s total data lake size is approximately 500 PiB, with about 10% churning daily that needs to be streamed from cloud to on-prem (approximately 50 PiB/day).

- Walmart is ready to begin a VAST Data POC/pilot, with a decision goal by the end of calendar year 2026 (CY2026).

- Walmart is willing to start with a partial solution now but needs a clear roadmap commitment to close remaining gaps by approximately October 2026, ahead of a holiday period code freeze to support January 2027 budget cycles.



---

*Source: [[2025-11-05 - Walmart Analytics 2]]*