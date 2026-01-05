---
type: people
title: '1:1 with Jai Menon: MAI AI caching strategy evaluation (OpenAI cache first) and Bifrost direct-read context'
date: '2025-09-03'
person: Jai Menon
participants:
- Jason Vallery
- Jai Menon
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-03 - Jai outlined a high-priority need to define an AI caching strategy for MAI at ma.md
tags:
- type/people
- generated
---

# 1:1 with Jai Menon: MAI AI caching strategy evaluation (OpenAI cache first) and Bifrost direct-read context

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jai Menon outlined a high-priority need to define an AI caching strategy for Microsoft AI Infrastructure (MAI) at massive scale, with a preference for a single pluggable cache for training and inference. Jason Vallery will start by evaluating the OpenAI cache (IP access, code quality, scalability to ~100,000 nodes, and fit with AKS/Spark) and compare it against Blobfuse/Blockfuse, AC Store/C-Store, and Alluxio/DAX, while Bifrost remains the near-term Blob performance focus with DeltaZero as a follow-on.

## Action Items

- [?] Evaluate the OpenAI cache for MAI requirements, including legality/access, architecture, code quality, performance, scalability to approximately 100,000 nodes, and fit with AKS/Kubernetes and Spark, and compare against Blobfuse/Blockfuse, AC Store/C-Store, and Alluxio/DAX. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Confirm OpenAI cache IP and usage rights for Microsoft production use and request repository/code access by coordinating with Pete and SILA legal. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Send OpenAI IP note or agreement details related to Microsoft usage of OpenAI cache IP to Jason Vallery. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send the MAI 10-page frustrations document (from Ong) to Jason Vallery for context on current pain points and requirements. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send the Apollo document to Jason Vallery for background and alignment on related storage initiatives. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Reconnect with Blobfuse/Blockfuse and AC Store/C-Store teams and review the latest materials including Blockfuse performance numbers, Krishnan proposals, and Nagendra's approximately 50-page progress document. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Verify MAI constraints and current status, including whether multi-region cache pooling is required, readiness of first GPU storage clusters, and training timelines, then report back to Jai Menon. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Discuss the retroactive performance snapshot outcome with Ong on Friday, and consider follow-up conversations with Wamshi and Manish if needed to clarify what happened and next steps. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Set up a regular 1:1 check-in cadence with Jai Menon after initial cache evaluation findings are available. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Connect Jason Vallery with Lukasz to review Bifrost direct read path implementation details and how it impacts MAI caching strategy. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Schedule a readout discussion with Jai Menon once initial OpenAI cache evaluation and MAI requirement confirmations are complete. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Evaluate OpenAI cache for MAI viability including legality/access, architecture, code quality, performance, scalability to approximately 100,000 nodes, and fit with AKS/Kubernetes and Spark; compare against Blobfuse/Blockfuse, AC Store/C-Store, and Alexio/DAX. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Confirm OpenAI cache IP and usage rights for Microsoft production use and request repo/code access by coordinating with Pete and SILA legal. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Send OpenAI IP note or agreement details related to cache usage to Jason Vallery. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send the MAI 10-page frustrations document (from Ong) to Jason Vallery. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send the Apollo document to Jason Vallery. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Connect Jason Vallery with Lukasz to discuss Bifrost direct read path implementation details. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Review latest materials and status with Blobfuse/Blockfuse (including performance numbers), AC Store/C-Store (Krishnan proposals), and Nagendra's progress document. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Verify MAI constraints and current status including whether multi-region cache pooling is required, readiness of first GPU storage clusters, and training timelines, then report back to Jai Menon. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Discuss the performance snapshot outcome with Ong on Friday and consider follow-up conversations with Wamshi and Manish to understand what happened and next steps. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Set up a regular 1:1 check-in cadence with Jai Menon after initial findings are available. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Review Jason Vallery's initial cache evaluation findings and choose a direction among OpenAI cache, Blobfuse/Blockfuse, AC Store/C-Store, and Alexio/DAX. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Introduce Jason Vallery to Qi Ke and Yumin for AKS/compute alignment if deeper engagement is needed for MAI cache integration. @Jai Menon 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Schedule a readout discussion once the initial OpenAI cache evaluation and MAI requirement confirmations are complete. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

## Decisions

- Jason Vallery will start by evaluating the OpenAI cache as the first concrete task for defining an AI caching strategy for Microsoft AI Infrastructure (MAI).

- The caching strategy should prioritize MAI training workloads first (checkpoint and find-data), with inference knowledge-base caching supported later.

- The preferred direction is a single, framework-pluggable cache rather than separate caches for training and inference.

- Near-term Azure Blob performance focus remains the Bifrost project (including a direct read path), with DeltaZero positioned as a follow-on.

- Jason Vallery will start by evaluating the OpenAI cache as the first concrete task for the MAI AI caching strategy, before selecting among alternatives (Blobfuse/Blockfuse, AC Store/C-Store, Alexio/DAX).

- The caching strategy should prioritize MAI training workloads first (checkpoint and find-data), with inference KB cache supported later.

- The preferred direction is a single, framework-pluggable cache rather than separate caches per use case.

- Near-term storage performance focus remains Bifrost (including a direct read path), with DeltaZero positioned as a follow-on.

## Key Information

- Jai Menon stated that Microsoft AI Infrastructure (MAI) is targeting approximately 400,000 GPUs for training (about 100,000 nodes) and approximately 40,000 GPUs for inference within about 2 years.

- Jai Menon stated that MAI's primary environment for the caching solution is AKS/Kubernetes and Spark.

- Jai Menon and Jason Vallery discussed caching options for MAI including OpenAI's cache, Blobfuse/Blockfuse, AC Store/C-Store, and Alluxio/DAX.

- Jai Menon expressed a preference for a single, framework-pluggable cache that can serve both MAI training workloads (including checkpoint and find-data) and inference workloads (knowledge base cache), rather than multiple bespoke caches.

- Jai Menon reported that OpenAI may permit Microsoft to use OpenAI IP including the cache implementation, but this requires confirmation with Pete and SILA legal before code access and production use.

- Jai Menon stated that Bifrost is the near-term focus for improving Azure Blob performance, including a new direct read path from compute to capacity nodes that bypasses the front-end/table path for many reads; DeltaZero is positioned as a follow-on effort.

- Jai Menon stated that Lukasz is building parts of Bifrost including the direct read path, working with Vishwajith on Jay Jagant's team.

- Jai Menon stated that MAI compute for AI moved into Brendan Burns' organization (AKS), and that Qi (Anson) Ke leads compute/AKS support for MAI; Yumin is engaged on the VAST side for alignment.

- Jai Menon stated that MAI may require multi-region logical pooling for the cache, but this requirement is not yet confirmed.

- Jai Menon stated that Nagendra shared an approximately 50-page progress document, Krishnan has proposals for AC Store/C-Store, and the Blockfuse team is sharing performance numbers relevant to MAI caching decisions.

---

- Microsoft AI Infrastructure (MAI) target scale discussed was approximately 400,000 GPUs for training (about 100,000 nodes) and approximately 40,000 GPUs for inference within about 2 years.

- The primary MAI environment for the caching strategy is AKS/Kubernetes and Spark.

- Caching options considered for MAI included OpenAI's cache, Blobfuse/Blockfuse, AC Store/C-Store, and Alexio/DAX.

- Jai Menon expressed a preference for a single, pluggable cache that can serve both training workloads (including checkpoint and find-data) and inference workloads (KB cache), rather than multiple bespoke caches.

- OpenAI reportedly permits Microsoft to use OpenAI IP including the cache, but this requires confirmation with Pete and SILA legal and may require repo/code access approval.

- Bifrost was described as the near-term performance focus for Azure Blob, including improved latency/throughput and a new direct read path from compute to capacity nodes that bypasses the front end and table layer for many reads.

- Lukasz is building parts of Bifrost including the direct read path, working with Vishwajith on Jay Jagant's team.

- Compute for AI moved to Brendan Burns' organization (AKS), and Qi Ke leads compute/AKS support for MAI; Yumin is engaged on the VAST side for alignment.

- MAI may require multi-region logical pooling for cache, but this requirement was not yet confirmed.

- Nagendra shared an approximately 50-page document on progress, Krishnan has proposals for AC Store/C-Store, and the Blockfuse team is sharing performance numbers.
