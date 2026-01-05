---
type: "people"
title: "1:1 with Vishnu Charan TJ, distributed caching definitions and Blobfuse distributed caching preview status"
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

# 1:1 with Vishnu Charan TJ, distributed caching definitions and Blobfuse distributed caching preview status

**Date**: 2025-09-15
**With**: Jason Vallery, Vishnu Charan TJ

## Summary

Jason Vallery and Vishnu Charan TJ aligned on Jason’s new focus areas, especially distributed caching and the KB/over-index problem, and discussed industry confusion around what “distributed caching” means (for example, Ray distribution is not replica-based caching). Vishnu shared the current Blobfuse distributed caching preview scope (distributed checkpointing with write replicas, resync on node recovery, async flush to Azure Blobs) and gaps (no cache-on-read, no read replicas, no fan-in), plus early scale and performance observations and planned customer testing.


## Action Items


- [?] Attend the Blockfuse execution/status meeting. @Myself 📅 2025-09-16 ⏫ #task #proposed #auto

- [?] Share Blobfuse distributed caching preview demo steps and the required bits/instructions once the internal demo environment is ready. @Vishnu Charan TJ 📅 2025-09-16 ⏫ #task #proposed #auto

- [?] Sync with Tomer Hagay and Vikas (last name not provided) to learn outcomes of the prior week’s distributed caching meeting and report back. @Vishnu Charan TJ 📅 2025-09-16 ⏫ #task #proposed #auto

- [?] Request and compile detailed Blobfuse distributed caching performance numbers, and plan MLPerf-style benchmarks and larger-scale tests up to approximately 1000 nodes. @Vishnu Charan TJ 📅 2025-10-26 #task #proposed #auto

- [?] Test the Blobfuse distributed caching preview once instructions/bits are received and provide product feedback on gaps (cache-on-read, read replicas, fan-in) and requirements. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Review NVIDIA Dynamo materials and assess fit alongside alternative frameworks (LM Cache, vLLM AI Bricks, CoreWeave approaches, and VAST as a KV store) for multi-node KV management and KVCache offload. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Clarify and document a shared definition and requirements for “distributed caching” across teams, including replicas, redundancy, tiering, and fan-in. @Jay Parikh 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate feasibility and sequencing for adding cache-on-read, read replicas, and fan-in support to the Blobfuse distributed caching effort. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Determine the approach for GPUDirect and RDMA (and potential successor transports) integration in the distributed caching data path. @Jay Parikh 📅 2025-10-26 #task #proposed #auto

- [?] Advance the NVIDIA Dynamo Azure Blob backend integration plan and define the community contribution path for open source engagement. @Vishnu Charan TJ 📅 2025-10-26 #task #proposed #auto

- [?] Confirm whether AC store and EI store qualify as distributed caches (replicas, redundancy, cache semantics) versus shared storage backends for target scenarios. @TBD 📅 2025-10-26 #task #proposed #auto




## Decisions


- Blobfuse distributed caching preview scope will remain focused on the write path for distributed checkpointing, including write replicas, asynchronous flush to Azure Blobs, and resync on node recovery, and will not include cache-on-read, read replicas, or fan-in in the initial preview.

- Use early customer testing (Figure AI and a potential MIT proof-of-concept) to validate the Blobfuse distributed caching preview and to guide prioritization of missing features such as cache-on-read, read replicas, and fan-in.




## Key Information


- Jason Vallery’s initial focus areas in his new role are distributed caching and the KB/over-index problem, aligned to Jay’s priorities.

- There is industry and internal confusion about the term “distributed caching”; Vishnu Charan TJ stated that Ray’s “distribution” is not a distributed cache with replicas, redundancy, and cache semantics.

- The container storage team referenced “AC store” and “EI store”, and it was unclear whether these are true distributed caches or shared storage systems that multiple nodes can access.

- Vishnu Charan TJ is engaging NVIDIA Dynamo regarding KVCache offload, with interest in a potential Azure Blob backend integration; Dynamo is described as a KV block manager across GPU, CPU, local SSD, and cloud tiers, using GDS and RDMA, and having S3 support today.

- Blobfuse distributed caching preview scope is focused on distributed checkpointing with write replicas, resync on node recovery, and asynchronous flush to Azure Blobs; it does not include cache-on-read, read replicas, or fan-in initially.

- Blobfuse distributed caching preview testing showed good node-to-node communications and was scaled to approximately 100 nodes in CycleCloud; higher-scale testing (for example, 1000 nodes) and MLPerf-style benchmarks were identified as needed.

- Vishnu Charan TJ stated that performance on the write path can saturate NICs (north-south and east-west), but larger datasets and realistic mixed read/write benchmarks are still pending.

- Prospective early testers for the Blobfuse distributed caching preview include Figure AI, and MIT was described as open to a short proof-of-concept.

- Manish Sah asked Jay to drive the architectural direction for distributed caching, and meetings were ongoing to align teams.

- Vishnu Charan TJ was promoted in September 2025.



---

*Source: [[2025-09-15 - Catch-up on Jason’s new role and priorities (distributed caching, KBover-index)]]*