---
type: people
title: Asaf Levy
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Asaf Levy

## Recent Context

- unknown: [[2025-10 - Asaf Levy]] - Note tracks completed action items from working with Asaf Levy (chief architect) to align on persist...
- 2025-10-20: [[2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]] - Weekly 1:1 with Yogev Vankin focused on VAST multi-cloud architecture across AWS/GCP/Azure, centerin... (via Yogev Vankin)

## Profile

**Role**: Chief Architect at VAST
**Relationship**: Architecture stakeholder/partner I met with to align on design decisions

**Background**:
- Partnered on persistence design, object tiering, and QoS/governance; contributed by defining governance model, benchmarking metadata persistence storage options, and sharing DataSpaces architecture/persistence roadmap.

## Key Facts

- Asaf Levy is the chief architect involved in aligning persistence design, object tiering, and QoS/governance for DataSpaces.
- QoS/governance model includes quotas and identity-based prioritization across throughput, TPS, and capacity.
- Metadata persistence options under consideration include Premium Blob and S3 Express versus block storage.
- Object-tiering design proposal spans Blob/S3/GCS and includes metadata persistence and consistency trade-offs.
- DataSpaces architecture docs and persistence roadmap were shared with Jason.
- Initial AWS design used a single VM (50 TB) as a global namespace cache; later persisted data to S3 and metadata to EBS with local SSD reads, at ~30% cost overhead.
- GCP design moved to a clustered approach with a mix of data-storing and compute-only VMs; experimented with N and z3 instance families.
- AWS and Azure clusters exist but are not production-grade; Oracle Cloud POC is completed.
- There are no paying customers yet for this product track.
- OpenAI pattern: central durable storage in hero regions with GPUs distributed across many regions/clouds; async pre-staging to GPU-adjacent stores.

## Topics

Persistence design, Object tiering, QoS and governance, Quotas and identity-based prioritization, Metadata persistence storage options, Consistency trade-offs, DataSpaces architecture and persistence roadmap, Benchmarking Premium Blob and S3 Express vs block storage, Multi-cloud architecture for VAST across AWS/GCP/Azure (and Oracle Cloud POC), Global namespace caching and durability via object-store tiering, GPU-adjacent caching, prefetch APIs, and cache-on-read semantics, Metadata persistence options (block storage vs Premium Blob/S3 Express) and latency concerns, Consistency models (strong vs eventual) for different workloads, QoS/governance (identity-based quotas and prioritization across throughput/TPS/capacity), API parity considerations between S3 and Blob

## Related

<!-- Wikilinks to related entities -->
