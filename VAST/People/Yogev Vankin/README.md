---
type: people
email: ''
company: VAST Data
title: Yogev Vankin
last_contact: '2026-01-05'
created: '2026-01-05'
tags:
- type/people
- needs-review
---

# Yogev Vankin

## Key Facts

- Yogev Vankin described an initial AWS design for VAST cloud architecture using a single VM with 50 TB as a global namespace cache, later adding persistence by writing data to Amazon S3 and metadata to Amazon EBS, with reads served from local SSD and an estimated ~30% cost overhead versus the VM alone.

- Yogev Vankin stated the GCP approach moved to a clustered design with multiple VMs across placement groups, including a mix of data-storing VMs and compute-only VMs, and experimentation with GCP N and z3 instance families.

- Yogev Vankin stated AWS and Azure cluster implementations exist but are not production-grade yet, and an Oracle Cloud proof-of-concept was completed.

- Yogev Vankin stated there were no paying customers yet for this cloud product track at the time of the meeting (2025-10-20).

- Yogev Vankin was responsible for summarizing Oracle Cloud POC learnings and the current status of VAST clusters on AWS, GCP, and Azure for Jason Vallery.

- Jason Vallery planned to establish a weekly or monthly 1:1 cadence with Yogev Vankin for coordination on cloud-related work.
## Recent Context

- 2025-10-20: Jason Vallery and Yogev Vankin reviewed VAST multi-cloud architecture experiments across AWS, GCP, a...

- 2026-01-05: A task was captured for Yogev Vankin to summarize Oracle Cloud POC learnings and provide the current...

- 2026-01-05: Mentioned in: 1:1 with Jeff Denworth - travel planning, scope ownership, and cloud team alignment
## Open Tasks
```tasks
path includes Yogev Vankin
not done
```

## Topics

- VAST multi-cloud architecture patterns across AWS, GCP, Azure, and Oracle Cloud

- Global namespace as a differentiator for bringing data to GPUs

- Object-store tiering as the durable layer (Blob, S3, GCS)

- GPU-adjacent caching, prefetch API, and cache-on-read semantics

- Metadata persistence options and latency trade-offs (block vs premium object)

- Oracle Cloud POC learnings for VAST Data

- Status of VAST clusters on AWS, GCP, and Azure
## Key Decisions

- Make tiering to hyperscaler object storage (Azure Blob, Amazon S3, Google Cloud Storage) a core design requirement for VAST multi-cloud architecture, with object storage as the durable system of record and VAST providing compute and caching.

- Schedule a Jason Vallery and Asaf Levy technical deep dive on persistence architecture and QoS/governance for Tuesday 2025-10-21.