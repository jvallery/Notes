---
type: person
name: Vishnu Charan TJ
email: ''
company: ''
title: ''
last_contact: '2025-09-15'
created: '2026-01-05'
tags:
- type/person
- needs-review
---

# Vishnu Charan TJ

## Key Facts

- There is industry and internal confusion about the term “distributed caching”; Vishnu Charan TJ stated that Ray’s “distribution” is not a distributed cache with replicas, redundancy, and cache semantics.

- Vishnu Charan TJ is engaging NVIDIA Dynamo regarding KVCache offload, with interest in a potential Azure Blob backend integration; Dynamo is described as a KV block manager across GPU, CPU, local SSD, and cloud tiers, using GDS and RDMA, and having S3 support today.

- Vishnu Charan TJ was promoted in September 2025.

- Jai Menon planned to coordinate with Vishnu Charan TJ to share BlobFuse private preview bits and a deployment guide with inference and evaluation teams.

- Lukasz is building parts of Bifrost including the direct read path, working with Vishwajith on Jay Jagant's team.
## Recent Context

- 2025-09-16: Reviewed status of the distributed cache for checkpointing: core implementation is complete, with sc...

- 2025-09-15: Jason Vallery and Vishnu Charan TJ aligned on Jason’s new focus areas, especially distributed cachin...

- 2025-09-15: Mentioned in: 1:1 with Jai Menon, distributed cache evaluation plan and Oct 15 Silicon Valley offsite

- 2025-09-03: Mentioned in: 1:1 with Jai Menon: MAI AI caching strategy evaluation (OpenAI cache first) and Bifrost direct-read context
## Tasks

```tasks
path includes Vishnu Charan TJ
not done
```

## Topics

- Distributed cache for checkpointing MVP implementation status and node up-down testing

- Scale testing plan (100 to 200 nodes) and extrapolation to 10,000 to 100,000 nodes

- AKS integration approach: Linux mounts vs Blob CSI PV and Kubernetes operator concerns

- Private preview planning with Figure AI and customer environment confirmation (VMSS vs AKS)

- MAI adoption gating on data-driven throughput, scalability, and reliability narrative

- Jason Vallery role transition and initial priorities (distributed caching, KB/over-index)

- Definition of “distributed caching” and misconceptions about Ray

- AC store and EI store ambiguity, distributed cache vs shared storage

- Blobfuse distributed caching preview architecture and feature gaps

- Scale testing plans (100 to 1000 nodes) and MLPerf-style benchmarking needs
## Key Decisions

- Target a private preview by 2025-09-30 with Figure AI for the distributed cache checkpointing MVP, and defer MAI adoption until scale and throughput metrics support a data-driven narrative.

- Use AKS Linux mounts for initial AKS integration and validation; keep the CSI-based approach under evaluation pending AKS containers team concerns and timeline.

- Keep MVP scope limited to checkpointing; exclude model loading, dataset loading, and prefetch from the private preview.

- Include measurement of network throughput reduction to Azure Blob and TPS per node to metadata and blob services as part of 100 to 200 node scale testing.

- Blobfuse distributed caching preview scope will remain focused on the write path for distributed checkpointing, including write replicas, asynchronous flush to Azure Blobs, and resync on node recovery, and will not include cache-on-read, read replicas, or fan-in in the initial preview.

- Use early customer testing (Figure AI and a potential MIT proof-of-concept) to validate the Blobfuse distributed caching preview and to guide prioritization of missing features such as cache-on-read, read replicas, and fan-in.