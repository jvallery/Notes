---
type: "people"
title: "1:1 with Yogev Vankin, multi-cloud global namespace architecture and object-store tiering"
date: "2025-10-20"
person: ""
participants: ["Jason Vallery", "Yogev Vankin", "Asaf Levy"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Yogev Vankin, multi-cloud global namespace architecture and object-store tiering

**Date**: 2025-10-20
**With**: Jason Vallery, Yogev Vankin, Asaf Levy

## Summary

Jason Vallery and Yogev Vankin aligned on a multi-cloud architecture for VAST that uses hyperscaler object storage (S3/GCS/Blob) as the durable system of record, with GPU-adjacent caching and a prefetch API to stage data near compute. They discussed metadata persistence trade-offs (block vs premium object), consistency requirements, and QoS/governance, and agreed to avoid overfitting the design to OpenAI by building a broadly applicable solution.


## Action Items


- [?] Hold technical deep dive with Asaf Levy to align on persistence design, object-store tiering, and QoS/governance for VAST multi-cloud global namespace. @Myself 📅 2025-10-21 ⏫ #task #proposed #auto

- [?] Prepare a proposal for object-tiering design (Azure Blob Storage, Amazon S3, Google Cloud Storage) including metadata persistence options and consistency trade-offs for VAST multi-cloud deployments. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Draft API requirements for dataset prefetch into GPU-adjacent cache and define cache-on-read semantics for the VAST global namespace. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Define QoS and governance model for the VAST multi-cloud global namespace, including identity-based quotas and prioritization across throughput, TPS, and capacity. @Asaf Levy 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Plan travel to Tel Aviv and Iceland and coordinate timing and pre-reads with Yogev Vankin. @Myself 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Benchmark viability of Premium Blob and S3 Express for metadata persistence versus block storage options (EBS/PD/Premium Disk), focusing on latency and IO needs for metadata-heavy workloads. @Asaf Levy 📅 2025-10-27 #task #proposed #auto

- [?] Confirm with OpenAI teams whether S3 API support is sufficient for GPU-adjacent storage workflows or whether Azure Blob API parity is required. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Capture requirements for a global high-TPS key-value store (TPS per PB, <=64 KB IO) and assess feasibility on VAST (including potential DataSpaces approach). @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Summarize Oracle Cloud POC learnings and current AWS/GCP/Azure cluster status for Jason Vallery. @Yogev Vankin 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Share current DataSpaces architecture documentation and persistence roadmap with Jason Vallery. @Asaf Levy 📅 2025-10-27 #task #proposed #auto




## Decisions


- Make tiering to hyperscaler object storage (Azure Blob Storage, Amazon S3, Google Cloud Storage) a core design requirement for VAST multi-cloud deployments, with object storage as the durable system of record and VAST providing front-end compute and caching.

- Schedule a Jason Vallery and Asaf Levy technical deep dive on persistence architecture and QoS/governance for Tuesday 2025-10-21.




## Key Information


- Yogev Vankin described an initial AWS design for VAST cloud: a single VM with 50 TB acting as a global namespace cache, later extended to persist data to Amazon S3 and metadata to Amazon EBS, with reads served from local SSD and approximately 30% cost overhead versus the VM alone.

- Yogev Vankin said the GCP approach moved to a clustered design with multiple VMs across placement groups, including a mix of data-storing VMs and compute-only VMs, and experimented with GCP N-family instances and later z3-family instances.

- Yogev Vankin stated that AWS and Azure cluster efforts exist but are not production-grade yet, and that an Oracle Cloud proof-of-concept was completed.

- Yogev Vankin stated there were no paying customers yet for this cloud product track as of 2025-10-20.

- Jason Vallery framed the key gap for customer success as enabling data mobility to GPUs via a global namespace, using OpenAI as an example where durable data lives in large 'hero' regions while GPUs are provisioned across many regions and clouds, requiring asynchronous pre-staging to GPU-adjacent storage.

- The group aligned on a durability goal where hyperscaler object storage (Azure Blob Storage, Amazon S3, Google Cloud Storage) is the system of record, with VAST providing front-end compute and caching.

- A key design debate captured was whether metadata should persist on block storage (EBS/PD/Premium Disk) versus premium object options (Premium Blob or S3 Express), with concern that Premium Blob around 3 ms time-to-first-byte could be too high for metadata-heavy workloads.

- QoS and governance requirements were identified as quotas and prioritization by identity across throughput, transactions per second (TPS), and capacity for the multi-cloud global namespace platform.

- A high-TPS key-value use case was discussed: maximizing TPS per PB for IO sizes up to 64 KB, with OpenAI reportedly using RocksDB plus FoundationDB on Azure L-series VMs for parts of this workload.



---

*Source: [[2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]]*