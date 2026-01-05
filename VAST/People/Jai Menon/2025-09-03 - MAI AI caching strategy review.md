---
type: people
title: MAI AI caching strategy review
date: '2025-09-03'
person: Jai Menon
participants:
- Jai Menon
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-03 - Jai outlined a high-priority need
  to define an AI caching strategy for MAI at ma.md
tags:
- type/customer
- account/jai-menon
- generated
---

# MAI AI caching strategy review

**Date**: 2025-09-03
**Account**: [[Jai Menon]]
**Attendees**: Jai Menon, Jason Vallery

## Summary

Jai and Jason aligned on a high-priority need to define an AI caching strategy for MAI at massive scale, starting with an evaluation of the OpenAI cache and comparison to Blobfuse/Blockfuse, AC Store/C-Store, and Alexio/DAX. Key requirements include scaling to ~100,000 nodes (400k GPUs training) and fitting AKS/Kubernetes and Spark, while near-term storage performance work remains focused on Bifrost (including a new direct read path) with DeltaZero as a follow-on.
## Action Items
- [ ?] Evaluate OpenAI cache for MAI viability (legality/access, architecture, code quality, performance, scalability to ~100k nodes, and fit with AKS/Spark) and compare against Blobfuse/Blockfuse, AC Store/C-Store, and Alexio/DAX. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ?] Confirm OpenAI cache IP/usage rights with Pete and SILA legal and request repo/code access. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ?] Send OpenAI IP note/agreement details to Jason. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Send MAI frustrations document (from Ong) to Jason. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Send Apollo document to Jason. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Connect Jason with Lukasz to review Bifrost direct read path implementation details. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Review latest materials/status with Blobfuse/Blockfuse (including performance numbers), AC Store/C-Store (Krishnan), and Nagendra’s progress document. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Verify MAI constraints and current status (multi-region pooling need, GPU storage cluster readiness, training timelines) and report back. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Discuss performance snapshot outcome with Ong on Friday; consider follow-up conversations with Wamshi and Manish. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ?] Set up a regular 1:1 check-in cadence with Jai. @Myself 📅 2025-10-26 🔽 #task #proposed
- [ ?] Introduce Jason to Qi Ke and Yumin for AKS/compute alignment if deeper engagement is needed. @Jai Menon 📅 2025-10-26 🔽 #task #proposed
- [ ?] Schedule a readout/discussion once initial evaluation and MAI requirement confirmations are complete. @Myself 📅 2025-10-26 🔽 #task #proposed

## Decisions
- Jason will start by evaluating the OpenAI cache as the first concrete task.
- Retroactive performance snapshot discussion will be handled with Ong first, with possible follow-up to Wamshi and Manish.
- Primary cache focus is MAI training/checkpoint/find-data workloads first; inference KB cache supported later.
- Aim for a single, framework-pluggable cache rather than separate caches per use case.
- Near-term storage performance focus remains Bifrost; DeltaZero positioned as follow-on.

## Key Information
- MAI target scale in ~2 years: ~400,000 GPUs for training (~100,000 nodes) and ~40,000 GPUs for inferencing.
- Primary environment is AKS/Kubernetes and Spark.
- Caching options under consideration include OpenAI cache, Blobfuse/Blockfuse, AC Store/C-Store, and Alexio/DAX.
- OpenAI reportedly permits Microsoft to use their IP (including cache), but confirmation via Pete and SILA legal is needed.
- Bifrost aims to improve Blob latency/throughput and adds a direct read path from compute to capacity nodes (bypassing FE/table) for many reads.
- Lukasz is building parts of Bifrost (including the direct path) with Vishwajith on Jagan’s team.
- Compute for AI moved to Brendan’s org (AKS); CVP Qi Ke leads compute/AKS support for MAI; Yumin is engaged on the Microsoft side.
- MAI may require multi-region logical pooling for cache; not yet confirmed.
- Nagendra shared a ~50-page progress document; Krishnan has proposals; Blockfuse is sharing performance numbers.

---

*Source: [[Inbox/_archive/2025-09-03/2025-09-03 - Jai outlined a high-priority need to define an AI caching strategy for MAI at ma.md|2025-09-03 - Jai outlined a high-priority need to define an AI caching strategy for MAI at ma]]*

## Related

- [[Jason Vallery]]
- [[SILA legal]]
- [[Brendan Burns]]
- [[Qi Ke]]
- [[DeltaZero]]
- [[Microsoft]]
- [[OpenAI]]
- [[CoreWeave]]