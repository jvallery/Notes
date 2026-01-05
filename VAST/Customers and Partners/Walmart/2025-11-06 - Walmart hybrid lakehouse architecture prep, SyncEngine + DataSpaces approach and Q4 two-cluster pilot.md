---
type: "customer"
title: "Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 two-cluster pilot"
date: "2025-11-06"
account: ""
participants: ["Jason Vallery", "Brett Tanzer", "Mikey", "Matt", "Avi", "Lior Genzel", "Jer", "Paul", "John Heidgerken", "Siyash"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 two-cluster pilot

**Date**: 2025-11-06
**Account**: [[]]
**Attendees**: Jason Vallery, Brett Tanzer, Mikey, Matt, Avi, Lior Genzel, Jer, Paul, John Heidgerken, Siyash

## Summary

Internal VAST prep to shape an in-person architecture whiteboarding session with Walmart’s Lakehouse team. Walmart runs dot-com systems on Microsoft Azure and enterprise analytics on Google Cloud (BigQuery and Google Cloud Storage), and wants a consistent hybrid lakehouse view across GCP and two on-prem data centers. Near-term plan is a Q4 pilot with two VAST clusters (Region 1 and Region 2) using SyncEngine replication from GCS plus DataSpaces across on-prem sites, while clarifying major open questions and product gaps (notably GCS API compatibility and stronger consistency semantics).


## Action Items


- [?] Compile and send consolidated architecture questions to Walmart contact Vandana for the Lakehouse team design session. @Myself 📅 2025-11-06 ⏫ #task #proposed #auto

- [?] Extract insights from Walmart technical blog links and incorporate into the proposed architecture and pilot test plan. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Secure the right Walmart stakeholders (Lakehouse owners and vector database team) and coordinate scheduling for the in-person architecture whiteboarding session targeted for next week. @Mikey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Follow up via email with answers to prior cloud questions raised in Slack related to Walmart hybrid cloud and GCP integration. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Align with Alon Horev and Andy Perlsteiner on the SyncEngine replication pattern and lessons learned from the Wave project to apply to Walmart’s GCS to on-prem replication design. @Avi 📅 2025-11-08 #task #proposed #auto

- [?] Produce Q4 configurations for two VAST clusters (Region 1 and Region 2) sized for Walmart pilot validation, including capacity and performance assumptions. @Paul 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft a pilot test plan framework and required data and artifacts list, including a sample query set for Trino/Presto and Spark against Delta or Hudi tables. @Matt 📅 2025-11-08 #task #proposed #auto

- [?] Validate whether Google Cloud Storage change-feed support can be consumed by VAST SyncEngine and outline required engineering work for near-real-time replication semantics. @Avi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide POC scope details including datasets, schemas, sample data, and representative Trino/Spark queries for the pilot. @Vandana 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm network bandwidth plan and connectivity paths between Google Cloud Platform and both on-prem Walmart data centers, including egress model assumptions. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver governance requirements for the hybrid lakehouse, including tenancy model, access controls (RBAC or ABAC), auditing, and data residency or compliance constraints. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify object table format standards (Delta vs Hudi), versions, and BigQuery interoperability expectations for data accessed from GCP versus on-prem VAST. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the required API surface and acceptance criteria for a Google Cloud Storage compatible endpoint, including timeline expectations and acceptable deltas versus strict compatibility. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Agree pilot success criteria and measurement plan, including RPO/RTO, query SLAs, and throughput targets for replication and analytics queries. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Confirm availability for an in-person architecture whiteboarding session with Walmart’s Lakehouse team targeted for the week of 2025-11-10. @Vandana 📅 2025-11-08 #task #proposed #auto




## Decisions


- Use VAST SyncEngine for the pilot to replicate data from Google Cloud Storage into on-prem VAST clusters, and use VAST DataSpaces to provide a unified view across the two on-prem sites.

- Focus the Walmart pilot on real Walmart workloads (representative tables and queries) rather than synthetic benchmarks.

- Consolidate a targeted question list and send it to Walmart before scheduling the in-person architecture whiteboarding session.




## Key Information


- Walmart’s hybrid posture is Microsoft Azure for dot-com and operational systems (order management, retail systems, Walmart.com) and Google Cloud Platform for enterprise analytics using BigQuery and Google Cloud Storage.

- Walmart’s target state is a consistent lakehouse view across Google Cloud Platform and two on-prem Walmart sites, with strong consistency as the long-term goal.

- Walmart’s immediate request is a Q4 pilot deploying two VAST clusters (Region 1 and Region 2) for testing and validation.

- Walmart’s scale assumptions discussed include roughly 450 PB initially growing to roughly 770 PB by 2029, and a daily replication target of about 10% of the lake from GCP to on-prem, estimated at about 5 Tbps sustained, with prior mentions up to 10 Tbps targets.

- Walmart’s two on-prem data centers are intended to run active-active with greater than 30 ms latency between sites.

- Walmart prefers a Google Cloud Storage compatible API surface; Amazon S3 compatibility alone is not sufficient for their long-term requirements.

- Walmart workloads mentioned for the lakehouse include Trino/Presto and Spark, with table formats including Delta and Hudi, and BigQuery access in GCP.

- Walmart’s pilot timeline discussed is starting now and running through roughly September or October 2026, with a decision window for a full project targeting calendar year 2027; budget cycles are expected to finalize at the end of calendar year 2026.

- Jason Vallery joined VAST Data about three weeks prior to 2025-11-06 as Vice President of Cloud Product Management, focused on hyperscaler success and hybrid cloud stories like Walmart.

- Jason Vallery previously spent 13 years at Microsoft on the Azure Storage engineering organization, in product management for Microsoft’s object storage platform, and has prior exposure to Walmart as an Azure customer.



---

*Source: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]]*