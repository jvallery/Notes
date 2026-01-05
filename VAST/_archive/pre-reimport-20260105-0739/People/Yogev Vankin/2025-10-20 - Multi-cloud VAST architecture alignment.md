---
type: people
title: Multi-cloud VAST architecture alignment
date: '2025-10-20'
person: Yogev Vankin
participants:
- Jason Vallery
- Yogev Vankin
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-20 - Discussed cloud architectures for
  VAST on AWSGCPAzure, the need for object-sto.md
tags:
- type/customer
- account/yogev-vankin
- generated
---

# Multi-cloud VAST architecture alignment

**Date**: 2025-10-20
**Account**: [[Yogev Vankin]]
**Attendees**: Jason Vallery, Yogev Vankin

## Summary

Jason and Yogev reviewed VAST on-cloud architecture learnings across AWS/GCP/Azure (and an Oracle Cloud POC), focusing on making cloud object storage (Blob/S3/GCS) the durable system of record with VAST providing compute/caching and a global namespace. Key gaps and requirements discussed included dataset prefetch and cache-on-read semantics for GPU-adjacent storage, metadata persistence tradeoffs (block vs premium object tiers), consistency expectations, and the need for QoS/governance and high-TPS KV-store capabilities. They agreed to avoid overfitting to OpenAI by building a broadly applicable multi-cloud solution and to sync with Asaf on persistence and governance design.
## Action Items
- [?] Meet with Asaf (chief architect) to align on persistence design, object-store tiering, and QoS/governance. @Myself 📅 2025-10-21 🔺 #task #proposed
- [?] Prepare a proposal for object-tiering design (Blob/S3/GCS), including metadata persistence options and consistency trade-offs. @Myself 🔺 #task #proposed
- [?] Draft API requirements for dataset prefetch into GPU-adjacent cache and cache-on-read semantics. @Myself ⏫ #task #proposed
- [?] Plan travel to Tel Aviv and Iceland; coordinate timing and request/collect pre-reads from Yogev/team. @Myself 🔽 #task #proposed
- [?] Confirm with OpenAI teams whether S3 API suffices for GPU-adjacent storage or if Blob API parity is required. @Myself ⏫ #task #proposed
- [?] Capture requirements for a global KV store (maximize TPS per PB, <=64 KB I/O) and assess feasibility on VAST/DataSpaces. @Myself ⏫ #task #proposed
- [?] Define QoS/governance model: quotas and prioritization by identity across throughput, TPS, and capacity. @Asaf 🔺 #task #proposed
- [?] Benchmark viability of Premium Blob / S3 Express for metadata persistence versus block storage options (EBS/PD/Premium Disk). @Asaf ⏫ #task #proposed
- [?] Share current DataSpaces architecture docs and persistence roadmap with Jason. @Asaf ⏫ #task #proposed
- [?] Summarize Oracle Cloud POC learnings and current AWS/GCP/Azure cluster status for Jason. @Yogev Vankin 🔽 #task #proposed

## Decisions
- Pursue object-store tiering (Blob/S3/GCS) as a core design requirement for durability/system-of-record.
- Schedule a Jason–Asaf technical deep dive for persistence and QoS/governance on 2025-10-21.
- Build a generally applicable multi-cloud solution and avoid overfitting the design to OpenAI-specific needs.

## Key Information
- Initial AWS design used a single VM (~50 TB) as a global namespace cache; persistence later added with data to S3 and metadata to EBS, with reads from local SSD and ~30% cost overhead.
- GCP design evolved to a clustered approach with a mix of data-storing and compute-only VMs; multiple instance families were tried (N and z3).
- AWS and Azure clusters exist but are not production-grade; an Oracle Cloud POC was completed.
- There are no paying customers yet for this product track.
- OpenAI pattern: central durable storage in hero regions with GPUs spread across many regions/clouds; data is asynchronously pre-staged to GPU-adjacent stores.
- OpenAI uses a tool called Cyclone that inventories blob storage across accounts into Snowflake and supports researcher-driven pre-staging using Put Blob From URL.
- GPU-adjacent storage is needed for throughput/cost, network autarky (surviving WAN outages), and checkpointing workflows.
- Premium object tiers (e.g., Premium Blob / S3 Express) are NVMe-backed; Premium Blob time-to-first-byte was cited as ~3 ms, which may be high for metadata-heavy workloads.
- Consistency expectations differ: eventual consistency may work for some AI workloads, but strong consistency is often required for broader enterprise adoption.
- QoS/governance requirement: quotas and prioritization by identity across throughput, TPS, and capacity.
- OpenAI high-TPS KV-store approach mentioned: RocksDB + FoundationDB on L-series VMs; goal is maximizing TPS per PB for <=64 KB I/O.
- Spark/Databricks are used primarily for ETL of conversations/API logs into a training data lake (PII removal/normalization, parquet generation).

---

*Source: [[Inbox/_archive/2025-10-20/2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto.md|2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]]*

## Related

- [[Jeff Denworth]]
- [[Asaf Levy]]
- [[Alluxio]]
- [[Amazon]]
- [[Google]]
- [[Microsoft]]
- [[Oracle]]
- [[OpenAI]]
- [[CoreWeave]]
- [[Snowflake]]
- [[Databricks]]