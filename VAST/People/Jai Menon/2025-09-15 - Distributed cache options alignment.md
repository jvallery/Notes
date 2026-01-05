---
type: people
title: Distributed cache options alignment
date: '2025-09-15'
person: Jai Menon
participants:
- Jai Menon
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-15 - Discussed distributed cache strategy,
  MAI needs, and BlobFuse readiness. Aligned.md
tags:
- type/customer
- account/jai-menon
- generated
---

# Distributed cache options alignment

**Date**: 2025-09-15
**Account**: [[Jai Menon]]
**Attendees**: Jai Menon, Jason Vallery

## Summary

Jason Vallery and Jai Menon aligned on how to evaluate distributed caching options (BlobFuse PP/AC Store model, OSS like Alluxio/JuiceFS, and internal options like Manifold/Singularity and OpenAI TensorCache) using scenario-based comparisons (fan-out writes/reads, fan-in reads, and KV cache). They discussed MAI’s current checkpointing approach (local NVMe with async copy to Blob) and the need to build an MAI-oriented narrative backed by benchmarks, while also addressing concerns about BlobFuse readiness, performance (Go/FUSE vs C++/kernel), and metadata strategy (consistent hashing vs high-TPS metadata store). An offsite was confirmed for 2025-10-15 in Silicon Valley with intent to include inferencing/KV cache and DPU/FunOS sessions, and a shared Teams room will centralize collateral and discussions.
## Action Items
- [ ] Create a shared Teams room and add all current distributed caching docs/links; share access with stakeholders (Jason, Jean, Jagan, etc.). @Jai Menon Menon 📅 2025-10-26 🔺 #task #proposed
- [ ] Coordinate with Vipul to schedule a Manifold (Singularity) team briefing and Q&A session. @Jai Menon Menon 📅 2025-10-26 🔺 #task #proposed
- [ ] Share Manifold slides/docs and the Manifold vs TensorCache comparison link in the Teams room. @Jai Menon Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ] Obtain BlobFuse PP bits and deployment guide from Vishnu; stand up tests (including fan-out writes) and collect performance at target scale. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Evaluate OpenAI TensorCache and compare with Manifold and BlobFuse on functionality, performance, and stability. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Restructure the evaluation document by scenarios (fan-out writes, fan-out reads, fan-in reads, KV cache) and map candidate solutions to each. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Prepare an MAI-focused proposal showing how BlobFuse compares to async copy on performance, complexity, risks, and scale; include benchmarks. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Set up a requirements call with MAI (with Pete/partners) to validate needs and adoption criteria. @Myself 📅 2025-10-27 🔺 #task #proposed
- [ ] Analyze metadata strategy trade-offs (consistent hashing vs high-TPS metadata store) and implications for scale-in/out. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Assess BlobFuse implementation choices (Go/FUSE) vs potential C++/kernel client for performance and time-to-market trade-offs. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Reach out to Rajat Monga to invite an inferencing/KV cache session at the offsite. @Jai Menon Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ] Book travel for the Silicon Valley offsite on 2025-10-15. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Share BlobFuse PP bits and guide with the inferencing team once available and collect feedback. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Draft the offsite agenda (including DPU/FunOS and inferencing sessions) and circulate. @Jai Menon Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ] Confirm BlobFuse PP availability and 100-node test results with Vishnu; capture metrics and any bottlenecks. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Verify Manifold’s approach to scale-in/out with consistent hashing and any rebalancing strategy. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Determine stability and roadmap status of OpenAI TensorCache relevant to near-term evaluations. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Clarify Alluxio IP/China concerns and runtime stack implications for enterprise adoption. @Myself 📅 2025-10-26 🔽 #task #proposed
- [ ] Confirm attendance/logistics for the Girish storage discussion and adjust travel if needed. @Jai Menon Menon 📅 2025-10-26 🔽 #task #proposed
- [ ] Align on long-term hardware offload/kernel-mode driver vision vs interim user-space path. @Jai Menon Menon 📅 2025-10-26 ⏫ #task #proposed

## Decisions
- Hold team offsite in Silicon Valley on 2025-10-15 (day and a half).
- Create a shared Teams room to centralize distributed caching documents and discussions.

## Key Information
- Team offsite set for 2025-10-15 in Silicon Valley; day and a half format with light schedule and social/dinner.
- MAI checkpointing approach: write to local NVMe and asynchronously copy to Blob; prioritizes simplicity and can tolerate occasional checkpoint loss by falling back to previous checkpoint.
- BlobFuse PP is currently focused on fan-out writes with limited read caching; a 100-node test was run and a deployment guide was pending.
- Inferencing team expressed interest in BlobFuse but had not received bits; a roughly two-month delay was noted.
- Candidate solution categories discussed: build/fork (BlobFuse/AC Store model), open source (Alluxio, JuiceFS), and internal (Manifold/Singularity, OpenAI TensorCache).
- Manifold claims consistent hashing without a central metadata store; questions remain about scale-in/out and rebalancing.
- OpenAI TensorCache was described as unstable/fast-changing; a comparison presented by Whipple reportedly favored Manifold.
- Concerns raised about Alluxio IP/China optics and Java components, and about BlobFuse performance implications of Go/FUSE vs a potential C++/kernel client.
- Long-term performance idea discussed: hardware offload/kernel-mode driver, acknowledged as higher risk and longer timeline.

---

*Source: [[Inbox/_archive/2025-09-15/2025-09-15 - Discussed distributed cache strategy, MAI needs, and BlobFuse readiness. Aligned.md|2025-09-15 - Discussed distributed cache strategy, MAI needs, and BlobFuse readiness. Aligned]]*

## Related

- [[Jason Vallery]]
- [[Rajat Monga]]
- [[Sam Altman]]
- [[Alluxio]]
- [[DeltaZero]]
- [[Microsoft]]
- [[OpenAI]]
- [[CoreWeave]]