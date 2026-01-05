---
type: account
name: Walmart
last_contact: '2025-12-23'
created: '2026-01-05'
tags:
- type/account
- needs-review
---

# Walmart

## Key Facts

- Walmart’s hybrid posture is Microsoft Azure for dot-com and operational systems (order management, retail systems, Walmart.com) and Google Cloud Platform for enterprise analytics using BigQuery and Google Cloud Storage.

- Walmart’s target state is a consistent lakehouse view across Google Cloud Platform and two on-prem Walmart sites, with strong consistency as the long-term goal.

- Walmart’s immediate request is a Q4 pilot deploying two VAST clusters (Region 1 and Region 2) for testing and validation.

- Walmart’s scale assumptions discussed include roughly 450 PB initially growing to roughly 770 PB by 2029, and a daily replication target of about 10% of the lake from GCP to on-prem, estimated at about 5 Tbps sustained, with prior mentions up to 10 Tbps targets.

- Walmart’s two on-prem data centers are intended to run active-active with greater than 30 ms latency between sites.

- Walmart prefers a Google Cloud Storage compatible API surface; Amazon S3 compatibility alone is not sufficient for their long-term requirements.

- Walmart workloads mentioned for the lakehouse include Trino/Presto and Spark, with table formats including Delta and Hudi, and BigQuery access in GCP.

- Walmart’s pilot timeline discussed is starting now and running through roughly September or October 2026, with a decision window for a full project targeting calendar year 2027; budget cycles are expected to finalize at the end of calendar year 2026.

- Walmart’s hybrid cloud posture is Azure for dot-com systems (order management, retail systems, Walmart.com) and GCP for enterprise analytics using BigQuery and Google Cloud Storage (GCS).

- Walmart’s goal is a hybrid lakehouse with a consistent view across GCP and two on-prem Walmart data centers, with a long-term desire for strong consistency across all three locations.

- Walmart’s immediate request is to deploy two VAST clusters (Region 1 and Region 2) in Q4 2025 for pilot testing of the hybrid lakehouse approach.

- Walmart’s data scale for the lake is approximately 400 PiB (about 450 PB) initially, growing to about 700 PiB (about 770 PB) by 2029.

- Walmart’s replication target is roughly 10% of the lake per day from GCP to on-prem, estimated at about 5 Tbps sustained throughput, and Walmart previously floated up to 10 Tbps performance targets with high change rates.

- Walmart’s two on-prem data centers operate active-active with greater than 30 ms latency between sites.

- Walmart workloads discussed include Trino/Presto and Spark, with tables in Delta Lake and Apache Hudi, and BigQuery access in GCP.

- Walmart prefers a GCS-compatible API surface for object access; S3-only compatibility is not acceptable as the long-term endpoint for this program.

- Walmart’s pilot timeline is to start in late 2025 and run through approximately September or October 2026, with a decision window for a full program targeting calendar year 2027; budget cycles are expected to finalize at the end of calendar year 2026.

- A potential Walmart meeting was discussed for next week, but timing, attendees, and objectives were not yet confirmed in the notes.

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

- Walmart’s primary ingestion and processing for this analytics environment is done via BigQuery on Google Cloud Platform (GCP).

- Walmart’s target topology is active-active across Google Cloud Platform and two on-prem Walmart sites, with the two on-prem sites separated by 30+ ms network latency.

- Walmart’s minimum replication requirement is to bring the hot working set down from GCP to on-prem using VAST SyncEngine.

- Walmart’s desired end state is strong consistency between on-prem storage and cloud storage, but high write rates make strong consistency challenging even though the workload is tolerant of latency.

- Walmart’s workload can tolerate small amounts of data loss during network unavailability.

- Walmart’s analytics compute frameworks include Trino, Spark, and similar analytics tools, with multiple business units running jobs on centrally managed infrastructure.

- Walmart wants a single interaction model with SDKs and tools that are agnostic to whether workloads run on-prem or in GCP.

- Walmart has significant existing code and tooling that deeply leverages the Google Cloud Storage (GCS) JSON API and strongly prefers a native GCS-like API on-prem to avoid refactoring.

- Walmart is ready to begin a VAST Data POC/pilot, with a decision goal by the end of calendar year 2026 (CY2026).

- Walmart's big data initiative has an unresolved disaster recovery requirement: Walmart may need either full VAST namespace access in a public cloud for DR or only a copy of the data for DR.

- Walmart has been pinging the VAST team for answers in the last 24 hours and is expected to provide answers to VAST's requirements questions within about an hour of the meeting time.

- Walmart held an internal requirements meeting during the week of 2025-12-22 and restated that they need to build a long-term hybrid solution for their data team.

- Walmart was not successful in getting the business to accept two disjoint namespaces, so any acceptable solution must avoid separate namespaces.

- Walmart plans to start an internal big data proof of concept (POC) sometime in 2025, limited to workloads that can run exclusively on premises.

- Walmart requires integration with Google Cloud Storage (GCS) for any solution they move forward with, or they would need significant lobbying at the database layer including a hybrid cloud database.

- Walmart held an internal requirements meeting during the week of 2025-12-22 and restated that they need a long-term hybrid solution for their data team.

- Walmart was not successful in getting the business to accept operating two disjoint namespaces, indicating a requirement for a unified namespace across environments.

- Walmart plans to start an internal big data proof of concept (POC) sometime in 2025, but only for workloads that can run exclusively on premises.

- Walmart requires integration with Google Cloud Storage (GCS) for any solution they move forward with, or they would need significant lobbying at the database layer including potentially a hybrid cloud database.
## Recent Context

- 2025-11-06: Internal VAST prep to shape an in-person architecture whiteboarding session with Walmart’s Lakehouse...

- 2025-11-07: Mentioned in: Cloud strategy 1:1 with Jonsi Stephenson, Google GDC TPU positioning and Microsoft Apollo storage path

- 2025-11-05: Walmart’s analytics pipeline ingests and processes data in BigQuery on GCP, then needs a hot working...

- 2025-11-05: Walmart’s analytics data is ingested and processed in BigQuery on GCP, with a requirement to replica...

- 2025-11-14: Internal VAST sync aligned on how to respond to Walmart's big data initiative, with the key gating i...

- 2025-12-23: Jeff Denworth relayed that Walmart restated requirements after an internal meeting: they need a long...
## Tasks

```tasks
path includes Walmart
not done
```

## Topics

- Walmart hybrid lakehouse target architecture across GCP and two on-prem data centers

- Replication strategy from Google Cloud Storage to on-prem VAST using SyncEngine

- Multi-site on-prem consistency model using VAST DataSpaces with >30 ms inter-site latency

- API requirements, specifically need for Google Cloud Storage compatible endpoint beyond S3

- Pilot scope definition: datasets, schemas, Delta or Hudi formats, and representative Trino/Presto and Spark queries

- Walmart hybrid lakehouse architecture spanning GCP and two on-prem data centers

- Replication architecture and feasibility for multi-terabit per second sustained throughput from GCP to on-prem

- Consistency model expectations and limitations for strong consistency across GCP and two on-prem sites

- API compatibility requirements, specifically GCS-compatible object API vs S3-only

- Pilot scope definition, success criteria, and workload-driven validation plan

- Hybrid analytics architecture: BigQuery on GCP with hot working set replicated to two Walmart on-prem sites

- Active/active design constraints with 30+ ms latency between on-prem sites

- Consistency model tradeoffs for high write-rate analytics data replication

- Developer compatibility requirement: GCS JSON API and GCS-like on-prem access

- Scale planning for 500 PiB lake and ~50 PiB/day churn replication

- Active-active topology feasibility across GCP and two on-prem sites with 30+ ms latency

- Consistency model tradeoffs: strong consistency goals vs high write rates and WAN latency

- Replication approach using VAST SyncEngine for cloud-to-on-prem hot set movement

- Developer experience requirement: GCS JSON API compatibility on-prem to avoid refactoring

- Walmart big data initiative disaster recovery requirement clarification (full namespace in cloud vs data copy)

- Limits of VM-based VAST deployments in public cloud at very large scale

- Hybrid cloud roadmap priorities and need for more native Google Cloud Storage integration

- Customer engagement plan: expectations and vision call with Mingming, then deeper technical session with SMEs after requirements are confirmed

- Scheduling constraints due to Supercomputing conference next week

- Walmart hybrid data platform requirements (single namespace expectation)

- Integration requirements with Google Cloud Storage (GCS)

- Walmart on-prem-only big data POC planned for 2025

- Competitive risk and positioning versus Alluxio

- Product planning implications for VAST cloud and hybrid capabilities

- Walmart hybrid data platform requirements (on-prem plus cloud integration)

- Unified namespace requirement (rejection of two disjoint namespaces)

- Google Cloud Storage (GCS) integration requirement for Walmart

- Walmart internal big data POC scope limited to on-prem-only workloads in 2025

- Competitive risk from Alluxio due to GCS-centric architectures
## Key Decisions

- Use VAST SyncEngine for the pilot to replicate data from Google Cloud Storage into on-prem VAST clusters, and use VAST DataSpaces to provide a unified view across the two on-prem sites.

- Focus the Walmart pilot on real Walmart workloads (representative tables and queries) rather than synthetic benchmarks.

- Consolidate a targeted question list and send it to Walmart before scheduling the in-person architecture whiteboarding session.

- Use VAST SyncEngine as the near-term pilot mechanism to replicate data from Google Cloud Storage (GCS) into on-prem VAST clusters for Walmart’s hybrid lakehouse pilot.

- Use VAST DataSpaces to provide a unified view across the two on-prem Walmart sites as part of the pilot architecture approach.

- Focus the pilot on representative Walmart workloads (real tables and queries using Trino/Presto, Spark, Delta Lake, and/or Hudi) rather than synthetic benchmarks.

- Consolidate and send a targeted question list to Walmart’s Lakehouse team before scheduling the in-person architecture whiteboarding session.

- Do not schedule a Walmart architecture or whiteboarding session until Walmart provides definitive requirements, especially the disaster recovery requirement (full VAST namespace access in cloud vs data copy).

- Hold off on providing detailed technical answers in Slack until after an expectations and vision call with Walmart's Mingming sets context, current capabilities, and forward roadmap narrative.