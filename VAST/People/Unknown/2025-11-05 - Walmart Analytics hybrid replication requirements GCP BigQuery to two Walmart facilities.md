---
type: "customer"
title: "Walmart Analytics hybrid replication requirements (GCP BigQuery to two Walmart facilities)"
date: "2025-11-05"
account: ""
participants: ["Unknown"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-05 - Walmart Analytics.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Walmart Analytics hybrid replication requirements (GCP BigQuery to two Walmart facilities)

**Date**: 2025-11-05
**Account**: [[]]
**Attendees**: Unknown

## Summary

Walmart runs primary ingestion and processing in Google Cloud (BigQuery) and needs a hot working set replicated into two Walmart-owned facilities for analytics using Trino/Spark. They want an active/active topology across GCP and two on-prem sites with a single developer interaction model, ideally a native GCS JSON API on-prem, while acknowledging strong consistency is hard with 30+ ms site latency and high write rates. A VAST POC is ready to start, with a decision target by end of CY2026 and a need to close key gaps by ~October 2026 ahead of holiday code freeze and Jan 2027 budget cycles.


## Action Items


- [?] Define and document Walmart's 'hot working set' scope for replication, including selection logic, daily volume, and peak write rates, to size SyncEngine and any active/active design. @TBD ⏫ #task #proposed #auto

- [?] Collect Walmart requirements for GCS JSON API compatibility on-prem, including which endpoints and behaviors are mandatory to avoid refactoring (for example resumable uploads, signed URLs, ACL semantics). @TBD ⏫ #task #proposed #auto

- [?] Quantify network and replication feasibility for streaming approximately 50 PiB/day from GCP to Walmart facilities, including available interconnect capacity and whether deltas/compaction can reduce bandwidth. @TBD ⏫ #task #proposed #auto

- [?] Define POC success criteria with Walmart for correctness, performance, failover behavior, and operability for Trino/Spark analytics on replicated data. @TBD #task #proposed #auto

- [?] Clarify Walmart's consistency and resiliency targets (RPO/RTO) for cloud-to-on-prem and on-prem-to-on-prem replication given 30+ ms latency and tolerance for small data loss during outages. @TBD ⏫ #task #proposed #auto






## Key Information


- Walmart's primary data ingestion and processing for this analytics workload is done in Google Cloud using BigQuery.

- Walmart requires replication of a hot working set of data from Google Cloud into two Walmart-owned and Walmart-managed facilities for further processing and analytics.

- Walmart's target topology is active/active across Google Cloud and two on-prem Walmart sites, with the two on-prem sites separated by 30+ ms network latency.

- Walmart's minimum acceptable replication approach is to bring the hot working set down from cloud to on-prem using VAST SyncEngine.

- Walmart desires strong consistency between on-prem storage and cloud, but the workload has high write rates and is latency-tolerant, making strong consistency challenging across 30+ ms WAN links.

- Walmart's workload is tolerant of small amounts of data loss during network unavailability.

- Walmart analytics processing frameworks include Trino, Spark, and similar analytics tools, with multiple business units running jobs on centrally managed infrastructure.

- Walmart wants a single interaction model with SDKs and tools that are agnostic to whether they run on-prem or in Google Cloud.

- Walmart has significant existing code and jobs that deeply leverage the Google Cloud Storage (GCS) JSON API and strongly prefers not to refactor, implying a preference for a native GCS-like API on-prem.

- Walmart's total data lake size is approximately 500 PiB, with about 10% of the data churning daily that needs to be streamed from cloud to on-prem (approximately 50 PiB/day).

- A VAST proof of concept (POC) for Walmart is ready to begin, with a decision goal by the end of calendar year 2026.

- Walmart is willing to start with a partial solution now but needs remaining gaps closed by approximately October 2026 ahead of a holiday period code freeze to align with January 2027 budget cycles.



---

*Source: [[2025-11-05 - Walmart Analytics]]*