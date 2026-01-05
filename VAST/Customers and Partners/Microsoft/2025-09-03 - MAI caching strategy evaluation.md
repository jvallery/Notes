---
type: customer
title: MAI caching strategy evaluation
date: '2025-09-03'
account: Microsoft
participants:
- Jai Menon
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-03 - Jai outlined a high-priority evaluation
  for an AI caching strategy to support MA.md
tags:
- type/customer
- account/microsoft
- generated
---

# MAI caching strategy evaluation

**Date**: 2025-09-03
**Account**: [[Microsoft]]
**Attendees**: Jai Menon, Jason Vallery

## Summary

Jai and Jason aligned on a high-priority evaluation of caching options to support Microsoft AI (MAI) scale, with emphasis on a unified cache for training first and inference (KB cache) later. Jason will lead feasibility evaluation of OpenAI cache IP (including IP access, code quality, scalability to ~100k nodes, and fit with AKS/Spark) while also tracking Blockfuse/BlobFuse (Bifrost) progress and comparing against Alluxio/DAX and C-Store proposals.
## Action Items
- [ ] Evaluate feasibility of using OpenAI cache IP for MAI scale (confirm IP access, obtain code, assess architecture/code quality, scalability to ~100k nodes, and operational fit with AKS/Spark; training first, inference later). @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Confirm legal/IP rights with Pete and SILA legal and arrange access to OpenAI cache code. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Review latest Blockfuse/BlobFuse progress materials (e.g., Nagendra’s document) and current status. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Meet Ong to clarify MAI requirements (scale, regions, timelines) and discuss performance snapshot concerns. @Myself 📅 2025-09-05 🔺 #task #proposed
- [ ] Sync with Lukasz to understand Bifrost direct-read path design and status. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Draft an initial recommendation comparing OpenAI cache vs Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse for MAI needs. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Send OpenAI IP/usage note and contact details; share MAI pain-points doc (10 pages); share Apollo doc. @Jai Menon Menon 📅 2025-10-26 🔺 #task #proposed
- [ ] Coordinate with Wamshi and SILA legal as needed after initial IP check. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] After meeting Ong, decide whether to escalate performance snapshot discussion to Manish. @Myself 📅 2025-09-05 ⏫ #task #proposed
- [ ] Propose a regular 1:1 cadence with Jai. @Myself 📅 2025-10-26 🔽 #task #proposed

## Decisions
- Near-term priority is a unified caching approach, with training requirements prioritized first and inference (KB cache) following.
- Proceed to evaluate OpenAI cache alongside ongoing reviews of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse.
- Continue Blob performance direction via Bifrost and consider DeltaZero as a subsequent step.

## Key Information
- Performance snapshot outcome appears to be Meets Expectations; Jason is disappointed and plans to discuss with Ong and potentially Manish.
- MAI scale targets: ~400k GPUs for training and ~40k GPUs for inference in ~2 years.
- Target data-plane scale is ~100k nodes; environment is AKS + Spark.
- Multi-region, cross-WAN cache pooling may be required (to confirm with MAI).
- Caching options under consideration include OpenAI cache IP, Alluxio/DAX (now supports inference/KB caching), C-Store proposals, and Blockfuse/BlobFuse.
- Strategic preference is one caching solution usable for both training and inference; pluggable and not tightly coupled to a single framework.
- Bifrost includes a direct read path bypassing FE/table for reads; Lukasz is building parts of this.
- DeltaZero is positioned as a follow-on to Bifrost (work in progress).
- Compute for MAI moved to Brendan Burns’s AKS org; Qi Ke ("Kiki") is leading compute side; Yumin is interfacing from storage side.

---

*Source: [[Inbox/_archive/2025-09-03/2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA.md|2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]]*

## Related

- [[OpenAI]]
- [[CoreWeave]]
- [[NVIDIA]]
- [[Jai Menon]]
- [[Jason Vallery]]
- [[SILA legal]]
- [[Brendan Burns]]
- [[Qi Ke]]
- [[Alluxio]]
- [[DeltaZero]]