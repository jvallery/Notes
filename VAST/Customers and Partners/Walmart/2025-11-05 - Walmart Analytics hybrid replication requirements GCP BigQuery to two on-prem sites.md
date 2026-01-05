---
type: customer
title: Walmart Analytics hybrid replication requirements (GCP BigQuery to two on-prem sites)
date: '2025-11-05'
account: Walmart
participants:
- Jason Vallery
- Unknown Walmart participants
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-05 - Walmart Analytics.md
tags:
- type/customer
- generated
---

# Walmart Analytics hybrid replication requirements (GCP BigQuery to two on-prem sites)

**Date**: 2025-11-05
**Account**: [[Walmart]]
**Attendees**: Jason Vallery, Unknown Walmart participants

## Summary

Walmart’s analytics pipeline ingests and processes data in BigQuery on GCP, then needs a hot working set replicated into two Walmart-owned facilities for additional analytics using Trino and Spark. The target topology is active/active across GCP and two on-prem sites with 30+ ms latency between sites, with a strong preference for a GCS JSON API compatible on-prem interface to avoid refactoring existing tooling. A VAST POC is ready to start, with a decision target by end of CY2026 and a need to close key gaps by ~October 2026 ahead of holiday code freeze and Jan 2027 budget cycles.


## Action Items


- [?] Define and document Walmart’s “hot working set” selection logic (tables/objects, freshness criteria, BU ownership), plus expected daily volume and peak write rates to size replication and consistency options. @Myself ⏫ #task #proposed #auto

- [?] Clarify Walmart’s required consistency semantics (object/file vs partition vs table) and acceptable RPO/RTO for GCP-to-on-prem and on-prem-to-on-prem replication, given tolerance for small data loss during network unavailability. @Myself ⏫ #task #proposed #auto

- [?] Confirm Walmart’s API compatibility requirements for on-prem access, specifically which subsets of the GCS JSON API must be supported to avoid refactoring existing tools and jobs. @Myself ⏫ #task #proposed #auto

- [?] Create an initial VAST POC plan for Walmart that includes success criteria (performance, correctness, failover behavior, operability, and developer compatibility) and aligns to a decision by 2026-12-31. @Myself 📅 2026-12-31 #task #proposed #auto

- [?] Identify the product gaps that prevent Walmart’s desired end state (active/active across GCP and two on-prem sites with strong consistency) and draft a closure plan that can be validated by ~2026-10-01 ahead of Walmart’s holiday code freeze. @Myself 📅 2026-10-01 ⏫ #task #proposed #auto






## Key Information


- Walmart’s primary ingestion and processing for this analytics workload is done in BigQuery on Google Cloud Platform (GCP).

- Walmart requires replication of a hot working set of analytics data from GCP into two Walmart-owned and Walmart-managed facilities for further processing and analytics.

- Walmart’s desired topology is active/active across Google Cloud Platform and two on-prem Walmart facilities, with 30+ ms network latency between the two on-prem sites.

- Walmart’s minimum requirement is to bring the hot working set down from GCP to on-prem using VAST SyncEngine.

- Walmart’s desired state is strong consistency between on-prem storage and cloud storage, but high write rates make strong consistency challenging even though the workload is tolerant of latency.

- Walmart’s workload is tolerant of small amounts of data loss during network unavailability.

- Walmart’s analytics compute frameworks include Trino, Spark, and similar analytics tools/frameworks.

- Multiple Walmart business units consume the data and run their own analytics jobs, which are centrally managed and executed on shared infrastructure.

- Walmart’s developer experience requirement is a single interaction model with SDKs and tools that are agnostic to whether workloads run on-prem or in GCP.

- Walmart has extensive existing code and tooling that deeply leverages the Google Cloud Storage (GCS) JSON API and strongly prefers not to refactor, implying a preference for a native GCS-like API on-prem.

- Walmart’s total data lake size is approximately 500 PiB, with about 10% churning daily that needs to be streamed from cloud to on-prem (approximately 50 PiB/day).

- A VAST Data proof of concept (POC) for Walmart is ready to begin, with a decision goal by the end of calendar year 2026 (CY2026).

- Walmart is willing to start with a partial solution now but needs a clear roadmap commitment to close remaining gaps by approximately October 2026, ahead of a holiday period code freeze to support January 2027 budget cycles.

- Public Walmart Global Tech information indicates Walmart selected Apache Hudi after evaluating Hudi, Delta, and Iceberg for its next-generation lakehouse.

- Public Walmart Global Tech information indicates Walmart runs a Trino platform on GCP with thousands of dashboards, more than 2,000 active users, and more than 1 million queries per month, and built a custom downscaler to avoid failures during GCP autoscaler downscale.



---

*Source: [[2025-11-05 - Walmart Analytics]]*