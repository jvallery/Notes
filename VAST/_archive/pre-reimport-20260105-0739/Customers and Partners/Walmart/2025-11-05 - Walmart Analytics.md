Requirements -
- Data is ingested and processed via BigQuery in GCP
- A portion of that data, the hot working set, must be replicated into Walmart facilities for further processing/analytics 
- Desire is for active/active across Google Cloud, and two Walmart owned/managed facilities
- At minimum, the hot working set must be brought down via Sync Engine
- Desired state is "strong consistency" between on-prem storage and the cloud
- The Walmart facilities are 30+ ms apart of network latency
- Workload is tolerant of latency, but high write rates make strong consistency a challenge
- Workload is tolerant of small amounts of data loss during network unavailbility
- Processing is Trino, Spark, and similar analytics tools/frameworks
- Multiple business units consume the data and have their own jobs which get managed and ran on central infrastructure
- Posture is hybrid-cloud and desire is a single interaction model with SDKs/tools that are agnostic to if they are running on-prem or in GCP
- There is a proliferation of code, tools, and jobs which already deeply leverage the GCS JSON API. There is a strong desire to not have to refactor these and therefore the preference is a native GCS like API on prem.
- The entire data lake is ~500PiB, with ~10% churning daily that needs to be streamed out of the cloud and into the on-prem environment
- POC/pilot of VAST is ready to begin, with a clear path forward and decision goal by end of CY26. 
- Okay if we have a partial solution today, but need a clear roadmap commitment to closing the remaining gaps by ~October of 2026 before heading into the holiday period code freeze to ensure budget cycles for Jan 2027.

## 1) Requirements (From 11/5 meeting)

- **Primary ingestion & processing:** BigQuery on GCP.
- **Hybrid requirement:** Replicate a **hot working set** into two Walmart‑owned facilities for further processing/analytics.
- **Topology target:** Active/active across **GCP + two on‑prem** Walmart sites (~30+ ms WAN latency between the on‑prem sites).
- **Replication path (min bar):** Bring down hot working set via **VAST SyncEngine**.
- **Desired consistency:** “Strong consistency” between on‑prem storage and the cloud; workload is latency‑tolerant but has **high write rates** (strong consistency is challenging).
- **Resiliency:** Tolerant of **small data loss** during network unavailability.
- **Compute frameworks:** **Trino**, **Presto,** **Spark**, and similar engines.
- **Multi‑tenant execution:** Multiple business units run jobs on centrally managed infra.
- **Developer experience:** Single interaction model across on‑prem/GCP; heavy existing usage of the **GCS JSON API** with strong preference to avoid refactoring (ideally a **GCS‑like API** on‑prem).
- **Scale & churn:** Data lake ~500 PiB, ~**10% churn daily** that must be streamed from cloud to on‑prem (i.e., ~**50 PiB/day**).
- **Program status:** POC for VAST ready; decision **by end of CY26**; acceptable to start with a **partial solution** now with roadmap items closed **by ~Oct 2026** before holiday code freeze for **Jan 2027** budget cycles.

## 2) Open questions we need to answer


1. **Define “hot working set”:** Which tables/objects, selection logic (freshness, tier, BU ownership), expected **daily volume** and **peak write rate** at object/file/table level?
2. **Format & table type:** BigQuery native tables only, or also **external/BigLake/Hudi/Iceberg/Delta** tables? Expected object formats on‑prem (Parquet/ORC, Hudi table layout, etc.).
3. **Change detection:** What is the authoritative change feed? (BigQuery change data capture to GCS, Hudi commit logs, Pub/Sub streams, etc.)
4. **Consistency target, precisely defined:** Per file/object? Per partition? Per table? What **RPO/RTO** are **acceptable** for **on‑prem↔cloud** and **on‑prem↔on‑prem**?
5. **Write locality:** Where do most writes originate (GCP vs. each on‑prem site)? Can we **shard write ownership** to minimize cross‑site synchronous hops?
6. **Sustained replication budget:** With ~**50 PiB/day**, sustaining ~**5.21 Tbps** continuous throughput is implied; can we segment the workload, compress, or **ship only deltas/compacted data**? (5.21 Tbps = 50×1024^5×8 /(86,400×10^12)).
7. **Physical links:** What interconnects exist today between GCP↔Walmart and between the two Walmart facilities?
8. **GCS JSON API on‑prem:** Is there a **hard requirement** for zero‑refactor?, Can we adopt S3 API + a shim/translation layer? What subsets of the GCS JSON API must be supported (signed URLs, resumable uploads, object ACLs, multipart, etc.)?
9. **Catalog strategy:** Single logical catalog for Trino/Spark across clouds? Hiveserver/Glue/Unity/Dataplex? Who is **source‑of‑truth** for schema and table formats on‑prem?
10. **BigQuery↔on‑prem joins:** Need for **federation** (e.g., BigQuery Omni/BigLake to S3 endpoints) vs. materialization/replication?
11. **Multi‑tenant isolation:** Per‑BU tenancy model? (namespaces, buckets, VAST policies, IAM mapping, row‑/column‑level security).
12. **Compliance posture:** Data residency, encryption KMS strategy (GCP CMEK vs. on‑prem HSM), audit trails, lineage.
13. **POC success criteria:** Performance, correctness, failover behavior, developer compatibility (GCS API), and operability KPIs.
14. **Roadmap dependencies:** Which vendor features or custom gateways are needed by **Oct 2026**? Written commitments?

## 3) What public information exists about Walmart’s analytics workload?

- **Lakehouse & format choice:** Walmart publicly documented an internal bake‑off of **Hudi, Delta, Iceberg** and selected **Apache Hudi** for its next‑gen lakehouse. The article also mentions **600k+ cores of Hadoop/Spark** across Walmart internal cloud, **Google Cloud, and Azure**, underscoring a multi‑cloud posture. ([Medium](https://medium.com/walmartglobaltech/lakehouse-at-fortune-1-scale-480bcb10391b "Lakehouse at Fortune 1 Scale. Walmart systems produce very large and… | by Samuel Guleff | Walmart Global Tech Blog | Medium"))
    
- **Trino at Walmart on GCP:** Walmart Global Tech described a **Trino** platform **running on GCP**, with thousands of dashboards and >2k active users executing **>1M queries/month**; they built a **custom down‑scaler** to avoid query failures during GCP autoscaler downscale. ([Medium](https://medium.com/walmartglobaltech/custom-downscaler-for-trino-cluster-on-google-cloud-243f64112b86 "Custom Downscaler For Trino Cluster on Google Cloud | by Ayush Bilala | Walmart Global Tech Blog | Medium"))
    
- **Spark on Google Cloud:** Walmart Global Tech has recent posts about using **Dataproc Serverless Spark** (Google Serverless Spark) and when to choose serverless vs. ephemeral clusters—evidence of current Spark usage in GCP. ([Medium](https://medium.com/walmartglobaltech/google-serverless-spark-part-1-an-overview-and-guide-c3aaf900e9cf "Google Serverless Spark, Part 1: 
    An Overview and Guide | by Shobhit Sabharwal | Walmart Global Tech Blog | Medium"))
    