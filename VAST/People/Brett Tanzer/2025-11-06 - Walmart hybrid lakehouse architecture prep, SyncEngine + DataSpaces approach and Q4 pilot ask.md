---
type: "customer"
title: "Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 pilot ask"
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

# Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 pilot ask

**Date**: 2025-11-06
**Account**: [[]]
**Attendees**: Jason Vallery, Brett Tanzer, Mikey, Matt, Avi, Lior Genzel, Jer, Paul, John Heidgerken, Siyash

## Summary

Internal VAST prep to shape an in-person architecture whiteboarding session with Walmart's Lakehouse team. Walmart runs dot-com systems on Azure and enterprise analytics on GCP (BigQuery/GCS), and wants to repatriate analytics to two on-prem sites while maintaining a consistent lakehouse view across GCP and both sites. The near-term plan is to pilot two VAST clusters (Region 1/2) in Q4 using SyncEngine replication from GCS plus DataSpaces across the on-prem sites, while clarifying workload, governance, and network feasibility for multi-Tbps replication.


## Action Items


- [?] Compile and send consolidated architecture questions to Walmart contact Vandana for the Lakehouse architecture whiteboarding session. @Myself 📅 2025-11-06 ⏫ #task #proposed #auto

- [?] Extract insights from Walmart technical blog links to inform the hybrid lakehouse architecture proposal and pilot test plan. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Secure the right Walmart stakeholders (Lakehouse owners and vector database team) and coordinate scheduling for the in-person architecture whiteboarding session. @Mikey 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Follow up via email with answers to prior cloud questions raised in Slack related to Walmart hybrid cloud and GCP integration. @Lior Genzel 📅 2025-11-08 #task #proposed #auto

- [?] Align with Alon Horev and Andy Perlsteiner on the SyncEngine replication pattern and lessons learned from the Wave project to apply to Walmart's pilot architecture. @Avi 📅 2025-11-08 #task #proposed #auto

- [?] Produce Q4 configuration proposals for two VAST clusters (Region 1 and Region 2) sized for Walmart's pilot validation. @Paul 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft a pilot test plan framework and a required data and artifacts list, including a sample query set for Trino/Spark validation on VAST. @Matt 📅 2025-11-08 #task #proposed #auto

- [?] Validate whether and how a GCS change-feed can be consumed by VAST SyncEngine for near-real-time replication, and outline required engineering work if gaps exist. @Avi 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide pilot scope details to VAST, including datasets, schemas, sample data, and representative Trino/Spark queries for the Walmart hybrid lakehouse pilot. @Vandana 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the network bandwidth plan and connectivity paths between GCP and both on-prem Walmart data centers, including egress model assumptions. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Deliver governance requirements for the Walmart lakehouse, including tenancy model, access controls (RBAC/ABAC), auditing, and data residency/compliance constraints. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify object table format standards (Delta vs Hudi) and BigQuery interoperability expectations for the Walmart hybrid lakehouse architecture. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Confirm Walmart's API requirement for a GCS-compatible endpoint, including acceptable deltas from strict GCS behavior and timeline for acceptance. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Agree on pilot success criteria for the Walmart hybrid lakehouse pilot, including RPO/RTO, query SLAs, and throughput targets. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Confirm availability for an in-person architecture whiteboarding session next week with Walmart's Lakehouse team. @Vandana 📅 2025-11-08 #task #proposed #auto




## Decisions


- Use VAST SyncEngine as the pilot mechanism to replicate data from Google Cloud Storage (GCS) into on-prem VAST clusters for Walmart's hybrid lakehouse pilot.

- Use VAST DataSpaces to provide a unified view across the two on-prem Walmart sites during the pilot, while acknowledging strong consistency across GCP plus both sites is not currently achievable end-to-end.

- Focus the Walmart pilot on real Walmart workloads (representative tables and queries) rather than synthetic benchmarks.

- Consolidate and send a targeted question list to Walmart before scheduling the in-person architecture whiteboarding session.




## Key Information


- Walmart's hybrid posture is Azure for dot-com systems (order management, retail systems, Walmart.com) and GCP for enterprise analytics using BigQuery and Google Cloud Storage (GCS).

- Walmart's goal is a hybrid lakehouse with a consistent view across GCP and two on-prem Walmart data centers, with an aspirational requirement for strong consistency across all three locations.

- Walmart's analytics ingestion pipelines currently run through GCP and leverage BigQuery, making GCP the current source of truth for the lakehouse data.

- Walmart requested a Q4 pilot with two VAST clusters (Region 1 and Region 2) for testing a hybrid lakehouse architecture.

- Walmart scale assumptions discussed include approximately 450 PB initially (about 400 PiB) growing to approximately 770 PB by 2029 (about 700 PiB).

- Walmart replication targets discussed include replicating about 10% of the lake per day from GCP to on-prem, estimated at about 5 Tbps sustained, with prior discussions mentioning up to 10 Tbps performance targets and high change rates.

- Walmart operates two on-prem data centers in an active-active model with greater than 30 ms latency between sites.

- Walmart workloads discussed include Trino/Presto and Spark, with table formats including Delta and Hudi, and BigQuery access in GCP.

- Walmart prefers a GCS-compatible API surface; S3-only access is not acceptable as a long-term solution for their lakehouse strategy.

- Jason Vallery joined VAST Data about three weeks before 2025-11-06 as VP of Cloud Product Management, after 13 years at Microsoft on Azure Storage (object storage platform) product management and engineering.

- Jason Vallery has prior exposure to Walmart as an Azure customer from his time at Microsoft, though not specifically for the Walmart analytics workload discussed here.



---

*Source: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]]*