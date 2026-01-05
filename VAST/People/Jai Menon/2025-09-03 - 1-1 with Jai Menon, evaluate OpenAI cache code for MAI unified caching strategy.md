---
type: people
title: 1:1 with Jai Menon, evaluate OpenAI cache code for MAI unified caching strategy
date: '2025-09-03'
person: Jai Menon
participants:
- Jason Vallery
- Jai Menon
- Ong (unknown full name)
- Manish (unknown full name)
- Wamsi (unknown full name)
- Pete (unknown full name)
- Lukasz (unknown full name)
- Brendan Burns
- Qiu Ke (Kiki) (unknown full name)
- Yumin (unknown full name)
- Nagendra (unknown full name)
- Krishnan (unknown full name)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’.md
tags:
- type/people
- generated
---

# 1:1 with Jai Menon, evaluate OpenAI cache code for MAI unified caching strategy

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon, Ong (unknown full name), Manish (unknown full name), Wamsi (unknown full name), Pete (unknown full name), Lukasz (unknown full name), Brendan Burns, Qiu Ke (Kiki) (unknown full name), Yumin (unknown full name), Nagendra (unknown full name), Krishnan (unknown full name)

## Summary

Jai Menon and Jason Vallery aligned on a forward-looking scope to evaluate OpenAI's cache code as an input to Microsoft's AI caching strategy for MAI, targeting a single pluggable cache for both training and inference. Jason will confirm IP and repository access via Pete and SILA, assess technical fit for AKS and Spark at ~100k-node scale, and sync with MAI and adjacent efforts (BlockFuse/C-Store, Alluxio/DAX, Bifrost). They also discussed Jason addressing a disappointing performance snapshot with Ong and potentially Manish.

## Action Items

- [?] Confirm IP and repository access to OpenAI cache code with Pete and SILA legal, and obtain code access if permitted for Microsoft MAI services. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate OpenAI cache code architecture and performance, and assess viability for a unified training and inference cache that scales to approximately 100k nodes and fits AKS plus Spark. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Review the MAI 10-page feedback document and Apollo materials from Jai Menon, and extract caching and storage requirements relevant to MAI. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Sync with Ong (MAI stakeholder, full name unknown) to verify MAI cluster status, timelines, and whether multi-region cache pooling is required for early clusters. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Re-engage with the BlockFuse and BlobFuse team and review Nagendra's document plus current performance and scale claims for MAI caching. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Connect with Lukasz (full name unknown) to understand the Bifrost direct read path design, interfaces, and expected impact on read performance. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Send OpenAI IP agreement details to Jason Vallery and request code access if needed. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Send the MAI 10-page frustrations and feedback document and Apollo materials to Jason Vallery. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Meet with Wamsi (full name unknown) to discuss the performance snapshot, context, and what drove the outcome. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Discuss the performance snapshot outcome with Ong (full name unknown) and decide whether to also speak with Manish (full name unknown). @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Establish a regular 1:1 cadence with Jai Menon for ongoing alignment on MAI caching strategy and cross-team dependencies. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

## Decisions

- Jason Vallery will evaluate OpenAI cache code as the first concrete step toward defining a unified MAI caching strategy.

- The unified cache design will prioritize training use cases first, then add inference and knowledge-base caching support.

- The cache solution must target AKS plus Spark and be evaluated for scaling to approximately 100k nodes.

## Key Information

- Jai Menon and Jason Vallery aligned that the MAI caching strategy goal is a single, pluggable caching solution that can support both training and inference, ideally one cache implementation.

- Microsoft MAI scale targets discussed were approximately 400k GPUs for training (about 100k nodes) and 40k GPUs for inference over roughly a two-year horizon.

- The primary target environment for the MAI cache solution is AKS (Kubernetes) with Spark.

- Options under consideration for MAI caching included C-Store proposals (Krishnan's team), Alluxio/DAX (noted as supporting inference and knowledge-base caching), OpenAI cache code (potentially usable under Microsoft IP terms pending confirmation), and BlockFuse/BlobFuse approaches.

- OpenAI cache code access was described as likely permitted for Microsoft services but requiring confirmation with Pete and SILA legal before proceeding.

- Bifrost was described as adding a direct read path from compute to capacity nodes, bypassing the front-end and table layer for reads.

- Lukasz was identified as contributing the Bifrost direct read path and able to brief Jason Vallery on the design and interfaces.

- Compute for Microsoft MAI was said to have moved under Brendan Burns' organization (AKS), with CVP Qiu Ke (Kiki) involved and Yumin coordinating.

- A potential MAI requirement mentioned was multi-region pooling for a distributed cache, pending confirmation with MAI stakeholders.

- Near-term platform focus discussed was Bifrost plus a distributed cache, with DeltaZero positioned as a follow-on effort.

- Jason Vallery stated he was 'wildly disappointed' by a performance snapshot and planned to unpack what happened with Wamsi and discuss it with Ong, and potentially Manish, with Jai Menon's support.

---

*Source: [[2025-09-03 - Jai welcomed Jason back and aligned on a forward-looking scope evaluate OpenAI’]]*