---
type: "customer"
title: "Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with active/active and GCS API compatibility"
date: "2025-11-05"
account: ""
participants: []
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-05 - Walmart Analytics 2.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with active/active and GCS API compatibility

**Date**: 2025-11-05
**Account**: [[]]
**Attendees**: 

## Summary

Walmart runs primary ingestion and processing in BigQuery on GCP and needs to replicate a hot working set into two Walmart-owned facilities for analytics using Trino/Spark. They want an active/active topology across GCP and both on-prem sites, prefer strong consistency but can tolerate small data loss during network outages, and strongly prefer a native GCS JSON API compatible interface on-prem to avoid refactoring existing code.


## Action Items


- [?] Define and document Walmart's 'hot working set' scope for replication, including selection logic, daily volume, and peak write rates at object/file/table granularity. @TBD ⏫ #task #proposed #auto

- [?] Clarify Walmart's data formats and table types in scope (BigQuery native tables vs. external/BigLake and lakehouse formats such as Hudi/Iceberg/Delta) and the expected on-prem object layout (Parquet/ORC and table directory structure). @TBD ⏫ #task #proposed #auto

- [?] Quantify and validate the replication throughput requirement implied by ~50 PiB/day churn, and identify whether Walmart can segment, compress, or ship deltas/compacted data to reduce sustained bandwidth needs. @TBD ⏫ #task #proposed #auto

- [?] Elicit Walmart's precise consistency and resiliency requirements, including acceptable RPO/RTO for cloud-to-on-prem and on-prem-to-on-prem, and whether strong consistency is required per object, partition, or table. @TBD ⏫ #task #proposed #auto

- [?] Confirm the hard requirements for GCS JSON API compatibility on-prem, including which specific API features must be supported and whether a shim/translation layer is acceptable. @TBD ⏫ #task #proposed #auto

- [?] Capture Walmart's network topology and interconnect details between GCP and each Walmart facility and between the two Walmart facilities, including bandwidth, latency, and failure modes. @TBD #task #proposed #auto

- [?] Define POC success criteria for the Walmart VAST pilot, including performance, correctness, failover behavior, developer compatibility (GCS API), and operability KPIs. @TBD #task #proposed #auto






## Key Information


- Walmart's primary data ingestion and processing for this analytics workload is done in BigQuery on Google Cloud Platform (GCP).

- Walmart requires replication of a hot working set of data from GCP into two Walmart-owned and Walmart-managed facilities for further processing and analytics.

- Walmart's target topology is active/active across Google Cloud Platform (GCP) and two on-prem Walmart facilities, with the two on-prem facilities separated by 30+ ms of network latency.

- The minimum acceptable replication mechanism for Walmart is to bring the hot working set down from cloud to on-prem using VAST SyncEngine.

- Walmart's desired end state is strong consistency between on-prem storage and cloud storage, but high write rates make strong consistency challenging even though the workload is tolerant of latency.

- Walmart's workload can tolerate small amounts of data loss during network unavailability, implying a non-zero RPO is acceptable in failure scenarios.

- Walmart's analytics compute frameworks for this environment include Trino and Spark (and similar analytics tools/frameworks).

- Multiple Walmart business units consume the data and run their own analytics jobs, which are centrally managed and executed on shared infrastructure.

- Walmart's developer posture is hybrid-cloud with a requirement for a single interaction model and SDK/tooling that is agnostic to whether workloads run on-prem or in GCP.

- Walmart has significant existing code and tooling that deeply leverages the Google Cloud Storage (GCS) JSON API, and they strongly prefer not to refactor it, creating a preference for a native GCS-like API on-prem.

- Walmart's total data lake size is approximately 500 PiB, with about 10% of the data churning daily that needs to be streamed from cloud to on-prem, implying roughly 50 PiB/day of movement.

- A VAST Data proof of concept (POC) or pilot for Walmart is ready to begin, with a decision goal by the end of calendar year 2026 (CY26).

- Walmart is willing to start with a partial solution now but wants a clear roadmap commitment to close remaining gaps by approximately October 2026, ahead of a holiday-period code freeze to align with January 2027 budget cycles.



---

*Source: [[2025-11-05 - Walmart Analytics 2]]*