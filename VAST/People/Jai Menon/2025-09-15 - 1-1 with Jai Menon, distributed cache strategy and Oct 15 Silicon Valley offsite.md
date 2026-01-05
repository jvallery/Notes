---
type: "people"
title: "1:1 with Jai Menon, distributed cache strategy and Oct 15 Silicon Valley offsite"
date: "2025-09-15"
person: ""
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon, distributed cache strategy and Oct 15 Silicon Valley offsite

**Date**: 2025-09-15
**With**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon aligned on evaluating distributed caching options for Microsoft AI Infrastructure, including BlobFuse PP, open source caches (Alluxio, JuiceFS), and internal solutions (Manifold/Singularity, OpenAI TensorCache). They confirmed an in-person team offsite in Silicon Valley on 2025-10-15 and agreed to centralize cache materials in a shared Teams room while Jason benchmarks options and drafts a scenario-based recommendation.


## Action Items


- [?] Book travel for Jason Vallery to attend the Silicon Valley team offsite on 2025-10-15. @Myself 📅 2025-10-01 ⏫ #task #proposed #auto

- [?] Create a shared Microsoft Teams room to centralize distributed cache materials and share it with the distributed cache stakeholders (including Jean and Jagan). @Jai Menon 📅 2025-09-22 ⏫ #task #proposed #auto

- [?] Evaluate BlobFuse PP build for fan-out writes and benchmark against Microsoft AI Infrastructure needs, and compare results with OpenAI TensorCache and Manifold/Singularity approaches. @Myself 📅 2025-10-10 ⏫ #task #proposed #auto

- [?] Draft a scenario-based recommendation framing distributed cache requirements across fan-out writes, fan-out reads, fan-in reads, and KV cache, and update the shared document. @Myself 📅 2025-10-10 ⏫ #task #proposed #auto

- [?] Set up a deep-dive session with the Manifold/Singularity team via Vipul and collect collateral (slides and benchmarks) for comparison. @TBD 📅 2025-10-03 #task #proposed #auto

- [?] Explore adding inferencing leadership (Rajat Monga) and DPU stakeholders to the 2025-10-15 offsite agenda to align on KV caching and hardware offload opportunities. @Jai Menon 📅 2025-10-01 #task #proposed #auto




## Decisions


- Jason Vallery will book travel to attend the Microsoft team offsite in Silicon Valley on 2025-10-15.




## Key Information


- Jai Menon confirmed a Microsoft team offsite in Silicon Valley on 2025-10-15 for approximately 1.5 days, with casual sessions, a social event or dinner on day 1, and release around noon on day 2 to allow travel home.

- The distributed cache strategy goal discussed was to cover fan-out writes, fan-out reads, fan-in reads, and separately a KV cache use case for inferencing.

- Microsoft AI Infrastructure currently writes checkpoints to local NVMe and asynchronously copies to Azure Blob Storage, prioritizing simplicity and tolerating partial checkpoint loss.

- BlobFuse PP was described as primarily targeting fan-out writes today, with limited or no read caching, and having some scale testing including a 100-node CycleCloud simulation.

- Jai Menon planned to use the Silicon Valley offsite to connect his team with DPU stakeholders and discuss FunOS programming environment and future chip direction as potential enablers for hardware offload of caching.

- Jai Menon intended to invite Rajat Monga (inferencing lead) to the offsite to share inferencing and KV caching needs and how they fit into the OpenAI inferencing framework (not open source).

- Manifold was reported to outperform OpenAI TensorCache in shared benchmarks and to use consistent hashing rather than a central metadata store.

- OpenAI TensorCache was reported to have moved away from a metadata store toward hashing, with expected churn as GPT-6 focuses on memory and long context.

- Key technical concerns to validate included consistent hashing scalability and rebalancing, whether a high-TPS metadata or index store is required, Go plus FUSE performance versus a C++ or kernel client, and Alluxio IP and Java stack implications.

- The strategic tradeoff discussed was whether to productize best-of open source caching versus deeply integrating with platform and hardware offloads such as kernel-mode clients, GPUs, or DPU/FunOS acceleration.



---

*Source: [[2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]]*