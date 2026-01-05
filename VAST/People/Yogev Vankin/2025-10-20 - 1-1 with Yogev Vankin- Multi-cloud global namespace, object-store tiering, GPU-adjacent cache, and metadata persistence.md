---
type: "people"
title: "1:1 with Yogev Vankin: Multi-cloud global namespace, object-store tiering, GPU-adjacent cache, and metadata persistence"
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

# 1:1 with Yogev Vankin: Multi-cloud global namespace, object-store tiering, GPU-adjacent cache, and metadata persistence

**Date**: 2025-10-20
**With**: Jason Vallery, Yogev Vankin, Asaf Levy

## Summary

Jason Vallery and Yogev Vankin reviewed VAST multi-cloud architecture experiments across AWS, GCP, and Azure, and aligned that durable storage must tier to hyperscaler object stores (S3, GCS, Azure Blob) with VAST providing compute, caching, and a global namespace. They discussed GPU-adjacent caching and a prefetch API, metadata persistence trade-offs (block vs premium object), and the need to avoid overfitting the design to OpenAI by building a broadly applicable multi-cloud solution.


## Action Items


- [?] Meet with Asaf Levy (VAST chief architect) to align on persistence design, object-store tiering, and QoS/governance for VAST multi-cloud architecture. @Myself 📅 2025-10-21 ⏫ #task #proposed #auto

- [?] Prepare a proposal for object-tiering design using Azure Blob, Amazon S3, and Google Cloud Storage, including metadata persistence options and consistency trade-offs. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Draft API requirements for dataset prefetch from the global namespace into GPU-adjacent cache, including cache-on-read semantics. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Define a QoS and governance model for the multi-cloud global namespace, including identity-based quotas and prioritization across throughput, TPS, and capacity. @Asaf Levy 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Plan travel to Tel Aviv and Iceland and coordinate timing and pre-reads with Yogev Vankin. @Myself 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Benchmark viability of Premium Blob and S3 Express for metadata persistence versus block storage options (EBS, Persistent Disk, Premium Disk), focusing on latency and IO requirements for metadata-heavy workloads. @Asaf Levy 📅 2025-10-27 #task #proposed #auto

- [?] Confirm with OpenAI teams whether S3 API support is sufficient for GPU-adjacent storage workflows or whether Azure Blob API parity is required. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Capture requirements for a global key-value store (maximize TPS per PB with <=64 KB IO) and assess feasibility for VAST DataSpaces. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Summarize Oracle Cloud proof-of-concept learnings and the current status of AWS, GCP, and Azure cluster implementations for Jason Vallery. @Yogev Vankin 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Share current DataSpaces architecture documentation and persistence roadmap with Jason Vallery. @Asaf Levy 📅 2025-10-27 #task #proposed #auto




## Decisions


- Make tiering to hyperscaler object storage (Azure Blob, Amazon S3, Google Cloud Storage) a core design requirement for VAST multi-cloud architecture, with object storage as the durable system of record and VAST providing compute and caching.

- Schedule a Jason Vallery and Asaf Levy technical deep dive on persistence architecture and QoS/governance for Tuesday 2025-10-21.




## Key Information


- Yogev Vankin described an initial AWS design for VAST cloud architecture using a single VM with 50 TB as a global namespace cache, later adding persistence by writing data to Amazon S3 and metadata to Amazon EBS, with reads served from local SSD and an estimated ~30% cost overhead versus the VM alone.

- Yogev Vankin stated the GCP approach moved to a clustered design with multiple VMs across placement groups, including a mix of data-storing VMs and compute-only VMs, and experimentation with GCP N and z3 instance families.

- Yogev Vankin stated AWS and Azure cluster implementations exist but are not production-grade yet, and an Oracle Cloud proof-of-concept was completed.

- Yogev Vankin stated there were no paying customers yet for this cloud product track at the time of the meeting (2025-10-20).

- Jason Vallery framed the target problem as enabling customers to bring data to GPUs via a global namespace, using OpenAI as an example of central durable storage in large Azure 'hero regions' with asynchronous movement of data to GPU-adjacent storage across many regions and clouds.

- The group aligned on a durability goal where hyperscaler object storage (Azure Blob, Amazon S3, Google Cloud Storage) is the system of record, with VAST providing front-end compute, caching, and global namespace access.

- A key design debate captured was metadata persistence on block storage (EBS, Persistent Disk, Premium Disk) versus premium object options (Premium Blob or S3 Express), with concern that Premium Blob ~3 ms time-to-first-byte could be too high for metadata-heavy workloads.

- The meeting captured a requirement for QoS and governance, including quotas and prioritization by identity across throughput, transactions per second (TPS), and capacity for a multi-tenant multi-cloud global namespace.

- The meeting captured a requirement for a researcher-driven prefetch API to stage datasets from the global namespace into GPU-adjacent cache, and also noted cache-on-read as valuable.

- The meeting noted a consistency trade-off: eventual consistency may be acceptable for some AI workloads, but strong consistency is required for a broader customer base beyond OpenAI-like scenarios.

- The meeting captured a high-TPS key-value store use case targeting <=64 KB IO and maximizing TPS per PB, with an example that OpenAI uses RocksDB plus FoundationDB on Azure L-series VMs.

- The meeting captured a strategic focus to build a broadly applicable multi-cloud global namespace spanning hyperscalers and on-premises to reduce data duplication and vendor lock-in, explicitly avoiding overfitting to OpenAI requirements.



---

*Source: [[2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]]*