---
type: "people"
title: "Distributed cache evaluation alignment"
date: "2025-09-15"
person: "Jai Menon"
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "Inbox/_archive/2025-09-15/2025-09-15 - Jason and Jai aligned on next steps for a distributed cache strategy and short-t.md"
tags:
  - "type/customer"
  - "account/jai-menon"
  - "generated"
---

# Distributed cache evaluation alignment

**Date**: 2025-09-15
**Account**: [[Jai Menon]]
**Attendees**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon aligned on evaluating a distributed cache strategy, with MAI currently favoring a simple async NVMe-to-Blob checkpoint copy approach and only considering BlobFuse if it clearly improves performance and reduces complexity at MAI scale. They agreed to frame requirements by fan-out writes, fan-out reads, and fan-in reads (treating KV cache separately), compare BlobFuse+ACStore against Manifold/Singularity, OpenAI TensorCache, Alluxio, JuiceFS, and NVIDIA AIStore, and centralize collateral in a shared Teams space ahead of an Oct 15 Silicon Valley offsite.
## Action Items
- [ ] Create a Teams room for the distributed cache workstream and upload/share key collateral (e.g., Manifold/Singularity slides, comparison docs) with stakeholders (Jason, Jean, Jagan, etc.). @Jai ⏫ #task
- [ ] Coordinate and schedule a Manifold (Singularity) deep-dive with Vipul/Whipple’s team and circulate invite and pre-reads. @Jai ⏫ #task
- [ ] Set up a focused call with MAI to capture concrete requirements, scale targets, and evaluation criteria for adopting a cache. @Jai ⏫ #task
- [ ] Obtain and test BlobFuse private preview when available; validate fan-out write performance and any read caching behavior. @Myself ⏫ #task
- [ ] Obtain and test OpenAI TensorCache for comparative evaluation. @Myself ⏫ #task
- [ ] Review Manifold materials (including Whipple’s performance comparison vs TensorCache) and prepare questions on consistent hashing and scaling. @Myself ⏫ #task
- [ ] Draft a scenario-based recommendation covering fan-out write/read and fan-in read (treat KV cache separately), including positioning for MAI. @Myself ⏫ #task
- [ ] Plan Oct 15 Silicon Valley offsite sessions (including DPU topics and inferencing/KV cache) and confirm agenda/invites. @Jai 📅 2025-10-15 ⏫ #task

## Decisions
- Jason will travel to the Silicon Valley offsite on 2025-10-15.
- Collateral for the distributed cache workstream will be centralized in a new Teams room.

## Key Information
- Team offsite planned in Silicon Valley on 2025-10-15 for ~1.5 days (social/dinner day 1; half-day day 2).
- MAI checkpointing approach: write to local NVMe and async copy to Azure Blob; BlobFuse is not needed unless it clearly improves performance and reduces complexity at MAI scale.
- BlobFuse private preview is currently focused on fan-out writes; read caching maturity is limited; a 100-node CycleCloud test was run and a deployment guide is pending.
- Alternatives under review include Manifold (formerly Singularity), OpenAI TensorCache, Alluxio, JuiceFS, and NVIDIA AIStore.
- Manifold vs TensorCache performance document exists; Manifold reportedly outperforms TensorCache in shared results.
- Key design questions include consistent hashing vs metadata store scalability and whether a high-TPS metadata/index store (e.g., FoundationDB) is needed.
- Alluxio concerns include IP/China perception risk and Java stack implications.
- Inference team has been waiting ~2 months for BlobFuse private preview bits after an initial intro, creating credibility risk.
- North Star goal discussed: one solution that covers fan-out write/read and fan-in read; KV cache treated separately.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Jason and Jai aligned on next steps for a distributed cache strategy and short-t.md|2025-09-15 - Jason and Jai aligned on next steps for a distributed cache strategy and short-t]]*

## Related

- [[Jason Vallery]]
- [[Rajat Monga]]
- [[Alluxio]]
- [[DeltaZero]]
- [[Microsoft]]
- [[OpenAI]]
- [[NVIDIA]]
- [[CoreWeave]]
