---
type: "people"
title: "Distributed cache strategy alignment"
date: "2025-09-15"
person: "Jai Menon"
participants: ["Jai Menon", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/_archive/2025-09-15/2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v.md"
tags:
  - "type/people"
  - "person/jai-menon"
  - "generated"
---

# Distributed cache strategy alignment

**Date**: 2025-09-15
**With**: Jai Menon, Jason Vallery

## Summary

Jason and Jai aligned on evaluating distributed caching options (BlobFuse PP vs open source vs internal Manifold/TensorCache) and clarifying why MAI is not adopting BlobFuse today. They confirmed an Oct 15 Silicon Valley offsite and agreed to centralize cache materials, run a Manifold deep-dive, and have Jason produce scenario-based recommendations and MAI-focused comparisons.
## Action Items
- [ ] Book travel to attend the Silicon Valley team offsite on 2025-10-15 @Myself ⏫ #task
- [ ] Create a Teams room to centralize distributed cache materials and share with the team (including Jean and Jagan) @Jai ⏫ #task
- [ ] Upload and share Whipple/Manifold slides and related comparison links in the Teams room @Jai ⏫ #task
- [ ] Schedule a Manifold/Singularity deep-dive session (via Vipul) and invite the team @Vipul ⏫ #task
- [ ] Provide BlobFuse PP build, deployment guide, and 100-node performance results @Vishnu 📅 2025-09-19 ⏫ #task
- [ ] Evaluate BlobFuse PP (fan-out writes) and benchmark against MAI needs; also assess TensorCache and Manifold @Myself ⏫ #task
- [ ] Draft scenario-based framing (fan-out writes, fan-out reads, fan-in reads, KV cache) and update the doc @Myself ⏫ #task
- [ ] Prepare an MAI-focused proposal comparing lazy copy vs BlobFuse on performance, complexity, and risk @Myself ⏫ #task
- [ ] Ensure the inferencing team receives the BlobFuse build and evaluates it @Jai ⏫ #task

## Decisions
- Jason will attend the 2025-10-15 Silicon Valley team offsite (travel to be booked).

## Key Information
- Team offsite planned in Silicon Valley on 2025-10-15 for ~1.5 days; casual sessions plus social/dinner; release around noon on day 2.
- Goal is a distributed cache strategy covering fan-out writes, fan-out reads, fan-in reads, and separately KV cache.
- MAI currently writes checkpoints to local NVMe and asynchronously copies to Blob; simplicity is valued and checkpoints tolerate partial loss.
- BlobFuse PP currently targets fan-out writes and has limited/no read caching; some scale testing done via a 100-node CycleCloud simulation.
- Inferencing team expressed interest in BlobFuse but has not received a usable build for ~2 months.
- Options considered include building/owning, forking open source (e.g., Alluxio, JuiceFS), or adopting internal solutions (Manifold/Singularity, OpenAI TensorCache).
- Manifold reportedly outperforms OpenAI TensorCache in shared benchmarks and uses consistent hashing (no central metadata store).
- OpenAI TensorCache reportedly moved away from a metadata store toward hashing; churn expected as GPT-6 focuses on memory/long context.
- Key validation concerns include consistent hashing scalability/rebalancing, whether to build a high-TPS metadata/index store, Go+FUSE performance vs C++/kernel client, and Alluxio IP/Java considerations.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v.md|2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]]*

## Related

- [[Jai Menon]]
- [[Jason Vallery]]
- [[Rajat Monga]]
- [[Sam Altman]]
- [[Maneesh Sah]]
- [[Alluxio]]
- [[Microsoft]]
- [[OpenAI]]
