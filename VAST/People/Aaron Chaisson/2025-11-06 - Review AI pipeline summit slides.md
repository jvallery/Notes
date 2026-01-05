---
type: people
title: Review AI pipeline summit slides
date: '2025-11-06'
person: Aaron Chaisson
participants:
- Aaron Chaisson
- Allison Boerum
- Jason Vallery
- Glenn Lockwood
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-06 - Aaron walked through updated slides
  for next week’s SE conference covering two p.md
tags:
- type/people
- person/aaron-chaisson
- generated
---

# Review AI pipeline summit slides

**Date**: 2025-11-06
**With**: Aaron Chaisson, Allison Boerum, Jason Vallery, Glenn Lockwood

## Summary

Aaron reviewed updated AI pipeline slides for next week’s VAST SE Tech Summit, covering a continuous model-training loop and an enterprise inference (RAG) pipeline. The group aligned on key diagram clarifications: Kafka as an event-stream ingestion/feedback head, embeddings as precomputed, and Database shown in data prep and logging (with KV cache currently via NFS and GPU-direct-to-object as a future option). A key open point was whether to include Data Engine and function triggers in an SE-focused deck; Aaron will consult SE leadership before finalizing.
## Action Items
- [ ?] Refine training slides to show continuous loop, clarify pretraining vs tuning, and depict fine-tuning/reinforcement learning terminology @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Adjust RAG slides to show precomputed embeddings (NIMs on Kubernetes), retriever and re-ranker flow, and explicit chatbot-to-inference linkage @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Depict Kafka as an event-stream ingestion head and RL feedback path; remove Kafka from the core storage lane in the diagrams @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Add Database to data preparation and logging/archives in the diagrams; note optional role around KV cache metadata @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Consult SE leadership on whether/how to include Data Engine and function triggers in the SE conference deck @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Share Ray workflow diagrams/links in the Product Marketing drive and notify Aaron @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Present the updated deck at next week’s SE conference @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Confirm final decision on Data Engine inclusion after SE leadership review @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Validate with Glenn that KV cache representation (current NFS, future GPU-direct-to-object) matches engineering reality @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Distribute Ray diagram links and incorporate any applicable patterns into the slides @Aaron Chaisson 📅 2025-11-08 🔽 #task #proposed

## Decisions
- Use fine-tuning/reinforcement learning phrasing in the training loop (with online RL as a continuous-loop concept).
- Represent embeddings as precomputed in the vectorization phase (not inline during inference).
- Add Database to data preparation and logging/archives in the diagrams.
- Show current KV cache usage via NFS in inference depictions.

## Key Information
- Audience is VAST SEs at next week’s Tech Summit/SE conference.
- Two pipelines are covered: model training (continuous loop) and enterprise inference (RAG).
- Kafka is positioned as an event-stream ingestion head and reinforcement-learning feedback path rather than a core storage tier.
- Embeddings are precomputed via NVIDIA NIMs on Kubernetes and stored in a vector database.
- Inference flow includes retriever + re-ranker against the vector DB before model response.
- Database may assist in data prep (analytics tables to Parquet) and in logging/archives; KV cache metadata use is optional/future.
- Current KV cache access is via NFS; GPU-direct-to-object is a future option.
- Primary buyers discussed are NCPs/infrastructure providers; model builders are typically indirect customers.

---

*Source: [[Inbox/_archive/2025-11-06/2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p.md|2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]]*

## Related

- [[Allison Boerum]]
- [[Jason Vallery]]
- [[Glenn Lockwood]]
- [[AI Pipelines Collateral]]
- [[Amazon]]
- [[Microsoft]]
- [[NetApp]]
- [[Seagate]]
- [[OpenAI]]
- [[CoreWeave]]
- [[NVIDIA]]
- [[Google]]
- [[Anthropic]]