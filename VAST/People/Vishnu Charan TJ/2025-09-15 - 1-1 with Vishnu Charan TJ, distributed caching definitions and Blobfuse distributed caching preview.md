---
type: "people"
title: "1:1 with Vishnu Charan TJ, distributed caching definitions and Blobfuse distributed caching preview"
date: "2025-09-15"
person: ""
participants: ["Jason Vallery", "Vishnu Charan TJ"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Catch-up on Jason’s new role and priorities (distributed caching, KBover-index).md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Vishnu Charan TJ, distributed caching definitions and Blobfuse distributed caching preview

**Date**: 2025-09-15
**With**: Jason Vallery, Vishnu Charan TJ

## Summary

Jason Vallery and Vishnu Charan TJ aligned on Jason’s new role focus areas, especially distributed caching and the KB/over-index problem, and discussed industry confusion around what “distributed caching” means (for example, Ray distribution is not replica-based caching). Vishnu shared the current Blobfuse distributed caching preview scope (distributed checkpointing with write replicas, resync on node recovery, async flush to Azure Blobs) and gaps (no cache-on-read, no read replicas, no fan-in), plus NVIDIA Dynamo KVCache offload plans and Azure Blob backend integration ideas.


## Action Items


- [?] Attend the Blockfuse execution/status meeting. @Myself 📅 2025-09-16 ⏫ #task #proposed #auto

- [?] Share Blobfuse distributed caching preview demo steps and bits with Jason Vallery after the internal demo setup is ready. @Vishnu Charan TJ 📅 2025-09-16 ⏫ #task #proposed #auto

- [?] Sync with Tomer Hagay and Vikas (last name not provided) to learn outcomes of the prior week’s distributed caching meeting and relay key takeaways. @Vishnu Charan TJ 📅 2025-09-16 ⏫ #task #proposed #auto

- [?] Request and compile detailed Blobfuse distributed caching preview performance numbers, and plan MLPerf-style benchmarks and larger-scale tests up to approximately 1000 nodes. @Vishnu Charan TJ 📅 2025-10-26 #task #proposed #auto

- [?] Test the Blobfuse distributed caching preview once Vishnu Charan TJ shares the bits and instructions, and provide product feedback on gaps such as cache-on-read, read replicas, and fan-in. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Review NVIDIA Dynamo materials and assess fit alongside alternative KV/cache frameworks (LM Cache, vLLM AI Bricks, CoreWeave approaches, and VAST as a KV store) for multi-node KV offload. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Clarify and document a shared definition and requirements for “distributed caching” across teams, including replicas, redundancy, tiering, and fan-in. @Jay Parikh 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate feasibility and sequencing for adding cache-on-read, read replicas, and fan-in support to the Blobfuse distributed caching roadmap. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Determine the approach for GPUDirect and RDMA (and potential successor transports) integration in the distributed caching data path. @Jay Parikh 📅 2025-10-26 #task #proposed #auto

- [?] Advance the NVIDIA Dynamo Azure Blob backend integration plan and define a community contribution path for the integration. @Vishnu Charan TJ 📅 2025-10-26 #task #proposed #auto

- [?] Confirm whether AC store and EI store qualify as distributed caches versus shared storage backends for the target distributed caching scenarios. @TBD 📅 2025-10-26 #task #proposed #auto




## Decisions


- Blobfuse distributed caching preview scope will remain focused on the write path, including write replicas, asynchronous flush to Azure Blobs, and resync on node recovery, and will not include cache-on-read, read replicas, or fan-in in the initial preview.

- Use early customer testing (Figure AI and a potential MIT POC) to validate the Blobfuse distributed caching preview and to guide prioritization of missing features such as cache-on-read, read replicas, and fan-in.




## Key Information


- Jason Vallery’s initial focus areas in his new role are distributed caching and the KB/over-index problem, aligned to Jay’s priorities.

- Vishnu Charan TJ observed industry and internal confusion around the term “distributed caching”, specifically that Ray’s “distribution” is not a replica-based cache with redundancy and copies.

- The container storage team referenced “AC store” and “EI store”, and there is ambiguity whether these are true distributed caches or shared storage backends that multiple nodes can access.

- Vishnu Charan TJ is engaging NVIDIA Dynamo for KVCache offload and is considering an Azure Blob backend integration path.

- NVIDIA Dynamo positions a KV block manager that tiers data across GPU, CPU, local SSD, and cloud storage, and uses GPUDirect Storage (GDS) and RDMA; it has an S3 backend today.

- Blobfuse distributed caching preview scope is focused on distributed checkpointing with write replicas, resync on node recovery, and asynchronous flush to Azure Blobs; it does not include cache-on-read, read replicas, or fan-in initially.

- Blobfuse distributed caching preview testing showed strong node-to-node communications and scaled to approximately 100 nodes in CycleCloud; larger scale testing (for example, 1000 nodes) is planned.

- Blobfuse distributed caching preview performance can saturate NICs on writes (north-south and east-west), but MLPerf-style benchmarks and larger datasets are still needed to validate realistic performance.

- Prospective early testers for Blobfuse distributed caching preview include Figure AI (lined up) and a potential short POC with MIT; a demo environment is being prepared.

- Manish asked Jay to drive the architectural direction for distributed caching, and meetings are ongoing.

- Vishnu Charan TJ was promoted in September 2025.



---

*Source: [[2025-09-15 - Catch-up on Jason’s new role and priorities (distributed caching, KBover-index)]]*