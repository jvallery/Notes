---
type: people
title: OpenAI cache evaluation for MAI
date: '2025-09-03'
person: Jai Menon
participants:
- Jai Menon
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-03 - Jai outlined a near-term technical
  focus evaluate OpenAI’s caching code as a ca.md
tags:
- type/customer
- account/jai-menon
- generated
---

# OpenAI cache evaluation for MAI

**Date**: 2025-09-03
**Account**: [[Jai Menon]]
**Attendees**: Jai Menon, Jason Vallery

## Summary

Jai and Jason aligned on a near-term focus to evaluate OpenAI’s caching code as a candidate for MAI’s unified cache, prioritizing training use cases first while designing for eventual inference/KB caching. They discussed MAI scale targets (400k training GPUs / 40k inference GPUs in two years), the need to scale to ~100k nodes on AKS+Spark, and the near-term storage performance path via Bifrost (direct read path) with DeltaZero as a follow-on.
## Action Items
- [ ] Confirm Microsoft legal/IP clearance and repository access for OpenAI cache code (coordinate with Pete and SILA legal) and request access @Myself 📅 2025-10-26 ⏫ #task
- [ ] Review OpenAI cache code and document architecture, training vs inference/KB capabilities, and production readiness @Myself 📅 2025-10-26 ⏫ #task
- [ ] Assess OpenAI cache scalability to ~100k nodes and fit with AKS + Spark; identify gaps vs MAI requirements @Myself 📅 2025-10-26 ⏫ #task
- [ ] Meet with Ong to discuss snapshot feedback and MAI constraints; decide on escalation to Manish and Wamshi as needed @Myself 📅 2025-10-26 ⏫ #task
- [ ] Re-engage with Nagendra and Krishnan teams to get latest on BlobFuse and AC Store proposals/performance data; compare to OpenAI cache @Myself 📅 2025-10-26 ⏫ #task
- [ ] Confirm with MAI whether multi-region logical cache pooling is a requirement and capture additional constraints @Myself 📅 2025-10-26 ⏫ #task
- [ ] Connect with Lukasz to understand Bifrost direct read path design and implications for cache integration @Myself 📅 2025-10-26 ⏫ #task
- [ ] Send OpenAI IP agreement details and MAI pain points document; share Apollo document when available @Jai 📅 2025-10-26 ⏫ #task
- [ ] Set a regular 1:1 cadence with Jai @Myself 📅 2025-10-26 🔽 #task
- [ ] If IP is cleared, obtain OpenAI code artifacts and set up a review environment @Myself 📅 2025-10-26 ⏫ #task
- [ ] Collect performance numbers and scaling plans from Alluxio/DAX and BlobFuse teams for side-by-side comparison @Myself 📅 2025-10-26 ⏫ #task
- [ ] Review MAI pain points and Apollo documents to refine cache requirements @Myself 📅 2025-10-26 ⏫ #task

## Decisions
- Jason will lead the OpenAI cache evaluation and compare it against internal/external options.
- Design preference is a single, pluggable cache for training and inference (framework-agnostic).
- Near-term product direction centers on Bifrost plus a distributed cache; DeltaZero positioned as follow-on.

## Key Information
- MAI target in two years: ~400k GPUs for training and ~40k GPUs for inference.
- Cache must scale to ~100k nodes and run on AKS + Spark.
- Preference is one cache for training and inference (including KB caching), pluggable across frameworks.
- Options under evaluation include OpenAI cache IP, Alluxio/DAX, BlobFuse, and AC Store (Krishnan’s team).
- OpenAI cache IP usability by Microsoft requires legal confirmation (Pete and SILA legal).
- Bifrost adds a direct read path bypassing FE/table layers; DeltaZero is a potential follow-on.
- Lukasz is building parts of Bifrost, including the direct read path.
- Compute for AI moved to Brendan Burns’ org; Qi Ke ("Kiki") is leading AKS compute for MAI; Yumin is interfacing.
- Possible MAI requirement: multi-region logical cache pooling (to confirm).

---

*Source: [[Inbox/_archive/2025-09-03/2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca.md|2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]]*

## Related

- [[Jason Vallery]]
- [[SILA legal]]
- [[Manish Sah]]
- [[Brendan Burns]]
- [[Qi Ke]]
- [[Alluxio]]
- [[DeltaZero]]
- [[Microsoft]]
- [[OpenAI]]
- [[CoreWeave]]
- [[NVIDIA]]
