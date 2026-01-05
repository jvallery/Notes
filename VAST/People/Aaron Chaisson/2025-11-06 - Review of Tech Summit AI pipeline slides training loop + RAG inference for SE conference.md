---
type: "projects"
title: "Review of Tech Summit AI pipeline slides (training loop + RAG inference) for SE conference"
date: "2025-11-06"
project: ""
participants: ["Aaron Chaisson", "Allison Boerum", "Jason Vallery", "Glenn Lockwood"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Review of Tech Summit AI pipeline slides (training loop + RAG inference) for SE conference

**Date**: 2025-11-06
**Project**: [[]]
**Attendees**: Aaron Chaisson, Allison Boerum, Jason Vallery, Glenn Lockwood

## Summary

Aaron Chaisson reviewed updated slides for next week’s VAST SE conference covering two AI pipelines: model training with a reinforcement learning feedback loop and enterprise inference using RAG. The group aligned on depicting Kafka as an event-stream ingestion and RL feedback head, showing embeddings as precomputed (not inline during inference), and adding Database as an optional component for data prep and logging, with KV cache currently accessed via NFS and a future GPU-direct-to-object option.


## Action Items


- [?] Refine the model training slides to show a continuous feedback loop and clarify pretraining versus fine-tuning and reinforcement learning terminology. @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Adjust the RAG inference slides to show precomputed embeddings (via NVIDIA NIMs on Kubernetes), include retriever and re-ranker flow, and make the chatbot-to-inference linkage explicit. @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Update the diagrams to depict Kafka as an event-stream ingestion head and reinforcement learning feedback path, and remove Kafka from the core storage lane. @Aaron Chaisson 📅 2025-11-08 #task #proposed #auto

- [?] Add Database to the diagrams for data preparation and logging or archives, and note an optional role for KV cache metadata without overcommitting. @Aaron Chaisson 📅 2025-11-08 #task #proposed #auto

- [?] Consult VAST SE leadership on whether to include Data Engine and function triggers in the SE conference deck and how to position them for a storage-centric audience. @Aaron Chaisson 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share Ray-oriented workflow diagrams and links in the Product Marketing drive and notify Aaron Chaisson so he can incorporate applicable patterns into the deck. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Validate with Glenn Lockwood that the KV cache depiction (current NFS access and future GPU-direct-to-object option) matches engineering reality. @Aaron Chaisson 📅 2025-11-08 #task #proposed #auto

- [?] Present the updated AI pipeline deck at the next week VAST SE conference (Tech Summit). @Aaron Chaisson 📅 2025-11-08 #task #proposed #auto




## Decisions


- Use fine-tuning and reinforcement learning terminology in the model training loop, and treat online reinforcement learning as a continuous loop concept rather than a one-time step.

- Depict embeddings as precomputed during vectorization and stored in a vector database, not computed inline during inference.

- Show Kafka as an event-stream ingestion head and reinforcement learning feedback path rather than a core storage tier in the pipeline diagrams.

- Add Database to the diagrams as an option for data preparation and logging or archives, and note an optional future role for KV cache metadata.

- Show current KV cache access via NFS in the inference depiction, with GPU-direct-to-object as a future option.




## Key Information


- Jason Vallery is based in Colorado and previously lived in the Seattle and Redmond area around 2016 before moving back to Colorado.

- An unknown meeting participant is based in Massachusetts, just outside Boston, and noted the Boston area has many storage professionals due to EMC’s historical presence in Hopkinton, Massachusetts.

- Jason Vallery had coffee with Peter Imming about two weeks before 2025-11-06; Jason previously recruited Peter Imming from Amazon to Microsoft.

- Aaron Chaisson updated slides for a VAST SE conference to explain VAST’s opportunity and where VAST components fit across two pipelines: model training (with a continuous feedback loop) and enterprise inference (RAG).

- The team discussed Kafka placement in the model training pipeline and aligned that Kafka should be depicted as an event-stream ingestion head and reinforcement learning feedback path, not as a core storage tier.

- Jason Vallery described an example architecture where ChatGPT conversation events flow into a document database (example given: Microsoft Cosmos DB) and then into a centralized event bus (example given: Kafka) to feed ingestion for reinforcement learning feedback.

- For the inference (RAG) pipeline, embeddings should be shown as precomputed (example: via NVIDIA NIMs on Kubernetes) and stored in a vector database, rather than computed inline during inference.

- The inference flow discussed includes retriever and re-ranker queries against a vector database followed by model response generation.

- Current KV cache access in the inference depiction is via NFS, with a future option discussed as GPU-direct-to-object access.

- Database should be shown as supporting data preparation (for example, analytics tables to Parquet) and logging or archives, and may optionally be shown for KV cache metadata.

- A key open debate for the SE-focused deck is whether to include VAST Data Engine and function triggers, balancing vision value against the risk of confusing storage-centric SEs.



---

*Source: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]]*