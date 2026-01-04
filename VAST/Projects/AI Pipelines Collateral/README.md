---
type: projects
title: AI Pipelines Collateral
last_contact: '2025-11-06'
created: '2026-01-03'
tags:
- type/projects
- generated
---

# AI Pipelines Collateral

## Recent Context

- 2025-11-06: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]] - Team review of updated AI Pipeline slides for an upcoming VAST SE Tech Summit, covering a continuous...

## Key Facts

- Audience is VAST SEs at next week’s Tech Summit/SE conference; messaging must be storage-centric and clear.
- Two pipelines covered: model training (continuous loop with feedback) and enterprise inference (RAG).
- Kafka should be shown as an event-stream ingestion head and RL feedback path, not a core storage tier.
- Embeddings are precomputed via NIMs on Kubernetes and stored in a vector DB; inference uses retriever + re-ranker against the vector DB.
- Database can support data prep (analytics tables to Parquet) and logging/archives; may optionally hold KV cache metadata.
- Current KV cache access is via NFS; GPU-direct-to-object is a future option.
- Including Data Engine and function triggers is a tradeoff: vision value vs risk of confusing storage-centric SEs.
- Primary buyers are NCPs/infrastructure providers; model builders are indirect.
- Jason Vallery lives outside Boulder, Colorado; previously lived in Seattle/Redmond; notes many VAST folks are in the Boston area.

## Topics

AI pipeline slide review for SE Tech Summit, Model training pipeline with continuous feedback loop, Fine-tuning vs reinforcement learning terminology; online RL concept, Enterprise inference pipeline (RAG) sequencing, Precomputed embeddings via NIMs on Kubernetes; vector database usage, Kafka placement for ingestion and RL feedback, VAST Database role in data prep, logging/archives, and possible KV cache metadata, KV cache access (NFS today; GPU-direct-to-object future), Whether to include Data Engine and function triggers for an SE audience, Ray workflow diagrams and how VAST components map to Ray workflows, Buyer/audience positioning (NCPs/infrastructure providers vs model builders), Participant location/background context (Boston area, Colorado/Boulder, Seattle/Redmond)

## Related

<!-- Wikilinks to related entities -->
