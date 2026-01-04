---
type: people
title: Distributed caching preview alignment
date: '2025-09-15'
person: Vishnu Charan TJ
participants:
- Jason Vallery
- Vishnu Charan TJ
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-15 - Catch-up on Jason’s new role and
  priorities (distributed caching, KBover-index).md
tags:
- type/people
- person/vishnu-charan-tj
- generated
---

# Distributed caching preview alignment

**Date**: 2025-09-15
**With**: Jason Vallery, Vishnu Charan TJ

## Summary

Jason and Vishnu aligned on Jason’s new focus areas (distributed caching and KB/over-index) and discussed industry confusion around what “distributed caching” means (e.g., Ray vs true replica/redundancy semantics). Vishnu shared status of the Blobfuse distributed caching preview (write replicas, resync on node recovery, async flush to Azure Blobs) and gaps (no cache-on-read, no read replicas, no fan-in), plus early customer testing plans and performance/benchmark needs. They also discussed NVIDIA Dynamo KVCache offload and the opportunity to integrate an Azure Blob backend while learning from NVIDIA’s broader inference ecosystem insights.
## Action Items
- [ ] Attend the Blockfuse execution/status meeting. @Jason 📅 2025-09-16 ⏫ #task
- [ ] Share Blobfuse distributed caching preview demo steps and bits with Jason once the internal demo setup is ready. @Vishnu 📅 2025-09-16 ⏫ #task
- [ ] Sync with Tomer and Vikas to learn outcomes of last week’s distributed caching meeting. @Vishnu 📅 2025-09-16 ⏫ #task
- [ ] Request and compile detailed performance numbers and plan MLPerf-style benchmarks and larger-scale tests (up to ~1000 nodes) for the Blobfuse distributed caching preview. @Vishnu ⏫ #task
- [ ] Play with the Blobfuse distributed caching preview once bits/instructions are received and provide feedback. @Jason #task
- [ ] Review NVIDIA Dynamo materials and assess fit alongside alternative frameworks (e.g., LM Cache, VLLM AI Bricks). @Jason #task

## Decisions
- Blobfuse distributed caching preview scope will focus on distributed checkpointing with write replicas, async flush to Azure Blobs, and resync on node recovery; cache-on-read and fan-in are not included initially.
- Use early customer testing (Figure AI and a potential MIT POC) to validate the preview and guide prioritization of missing read/fan-in features.

## Key Information
- Jason’s initial priorities in the new role are distributed caching and the KB/over-index problem, aligned with Jay’s priorities.
- There is significant cross-team/industry ambiguity about what qualifies as “distributed caching” versus distribution/shared storage (e.g., Ray misconceptions; AC store/EI store questions).
- Blobfuse distributed caching preview capabilities: strongly consistent write replicas for checkpointing, resync on node recovery, and optional async flush from cache to Azure Blobs; supports restore from cache for written checkpoints.
- Blobfuse preview gaps: no cache-on-read, no read replicas, and no fan-in scenario support; recovery assumes most recent checkpoints.
- Testing status: node-to-node comms look good; scaled to ~100 nodes in CycleCloud; higher-scale testing (e.g., ~1000 nodes) and MLPerf-like benchmarks are still pending.
- Performance signal: writes can saturate NICs (north-south and east-west), but behavior at larger scales and with larger datasets is not yet validated.
- NVIDIA Dynamo is being explored for KVCache offload; Dynamo has S3 today and uses a KV block manager to orchestrate tiering across GPU/CPU/local SSD/cloud, with GDS and RDMA mentioned; goal is an Azure Blob backend integration.
- Prospective early testers mentioned: Figure AI (lined up) and MIT (open to a short POC).
- Vishnu was promoted in September 2025.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Catch-up on Jason’s new role and priorities (distributed caching, KBover-index).md|2025-09-15 - Catch-up on Jason’s new role and priorities (distributed caching, KBover-index)]]*

## Related

- [[Vishnu Charan TJ]]
- [[Jason Vallery]]
- [[Microsoft]]
- [[Amazon]]
- [[Google]]
- [[NVIDIA]]
- [[Cloud-in-a-box (Tier-2 clouds)]]
