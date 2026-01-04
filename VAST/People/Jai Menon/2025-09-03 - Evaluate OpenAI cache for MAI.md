---
type: "people"
title: "Evaluate OpenAI cache for MAI"
date: "2025-09-03"
person: "Jai Menon"
participants: ["Jai Menon", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/_archive/2025-09-03/2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’.md"
tags:
  - "type/customer"
  - "account/jai-menon"
  - "generated"
---

# Evaluate OpenAI cache for MAI

**Date**: 2025-09-03
**Account**: [[Jai Menon]]
**Attendees**: Jai Menon, Jason Vallery

## Summary

Jai and Jason aligned on a forward-looking scope to evaluate OpenAI’s cache code as an input to Microsoft’s MAI caching strategy, targeting a single pluggable cache for training first and inference/KB caching later. Key constraints include AKS+Spark as the primary environment and scaling to ~100k nodes (~400k GPUs) for training, with IP/code access needing confirmation via Pete and SILA legal. They also discussed addressing a disappointing performance snapshot with Wamsi/Ong (and possibly Manish) and establishing a regular check-in cadence.
## Action Items
- [ ] Confirm Microsoft IP/licensing and repository access to OpenAI cache code with Pete and SILA legal; obtain code access. @Myself 📅 2025-10-26 🔺 #task
- [ ] Evaluate OpenAI cache code (architecture, performance, viability) for a unified training/inference cache; assess scalability to ~100k nodes and fit with AKS/Spark. @Myself 📅 2025-10-26 🔺 #task
- [ ] Review MAI 10-page feedback and Apollo materials once received; extract caching/storage requirements. @Myself 📅 2025-10-26 ⏫ #task
- [ ] Sync with Ong (MAI) to verify cluster status, timelines, and confirm whether multi-region cache pooling is required. @Myself 📅 2025-10-26 🔺 #task
- [ ] Re-engage with BlockFuse/BlobFuse team and review Nagendra’s document and current performance/scale claims. @Myself 📅 2025-10-26 ⏫ #task
- [ ] Connect with Lukasz to understand Bifrost direct read path design and interfaces. @Myself 📅 2025-10-26 ⏫ #task
- [ ] Meet Wamsi to discuss the performance snapshot and context. @Myself 📅 2025-10-26 ⏫ #task
- [ ] Discuss snapshot outcome with Ong and decide whether to speak with Manish. @Myself 📅 2025-10-26 ⏫ #task
- [ ] Establish a regular 1:1 cadence with Jai. @Myself 📅 2025-10-26 #task
- [ ] Send OpenAI IP agreement details and request code access if needed. @Jai 📅 2025-10-26 🔺 #task
- [ ] Send MAI 10-page frustrations document and Apollo materials to Jason. @Jai 📅 2025-10-26 🔺 #task

## Decisions
- Evaluate OpenAI cache as the first concrete step for MAI caching strategy.
- Prioritize training use cases first; add inference/KB caching support subsequently.
- Target deployment environment is AKS + Spark and the solution must scale to ~100k nodes.

## Key Information
- Goal is a single, pluggable caching solution supporting both training and inference (preferably one cache).
- MAI scale targets in ~2 years: ~400k GPUs for training (~100k nodes) and ~40k GPUs for inference.
- Primary environment is AKS/Kubernetes with Spark.
- Options under consideration include C-Store proposals (Krishnan’s team), Alluxio/DAX (now supports inference/KB caching), OpenAI cache code, and BlockFuse/BlobFuse approaches.
- OpenAI cache access appears permitted for Microsoft services but requires confirmation via Pete and SILA legal.
- Bifrost includes a direct read path from compute to capacity nodes (bypassing FE/table for reads); Lukasz is contributing to this direct path.
- Compute for MAI moved under Brendan Burns’ org (AKS); CVP Qi Ke involved; Yumin coordinating.
- Potential requirement to confirm: multi-region pooling for a distributed cache.
- Near-term platform focus is Bifrost plus a distributed cache; DeltaZero positioned as follow-on.

---

*Source: [[Inbox/_archive/2025-09-03/2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’.md|2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]]*

## Related

- [[Jason Vallery]]
- [[SILA legal]]
- [[Manish Sah]]
- [[Brendan Burns]]
- [[Qi Ke]]
- [[Alluxio]]
- [[Cloud control plane]]
- [[DeltaZero]]
- [[Microsoft]]
- [[OpenAI]]
- [[CoreWeave]]
