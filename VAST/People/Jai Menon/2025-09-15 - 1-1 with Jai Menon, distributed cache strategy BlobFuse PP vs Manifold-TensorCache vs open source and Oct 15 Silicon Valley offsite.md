---
type: "people"
title: "1:1 with Jai Menon, distributed cache strategy (BlobFuse PP vs Manifold/TensorCache vs open source) and Oct 15 Silicon Valley offsite"
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

# 1:1 with Jai Menon, distributed cache strategy (BlobFuse PP vs Manifold/TensorCache vs open source) and Oct 15 Silicon Valley offsite

**Date**: 2025-09-15
**With**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon aligned on evaluating distributed caching options for Microsoft AI Infrastructure (MAI), including BlobFuse PP, internal Manifold/Singularity, and OpenAI TensorCache, with scenario-based requirements (fan-out writes, fan-out reads, fan-in reads, and KV cache). Jai confirmed a 1.5-day Silicon Valley team offsite on 2025-10-15 and agreed to centralize cache materials; Jason will test builds and produce a scenario-based recommendation.


## Action Items


- [?] Book travel to attend the Microsoft Apollo team offsite in Silicon Valley on 2025-10-15. @Myself 📅 2025-10-01 ⏫ #task #proposed #auto

- [?] Evaluate the BlobFuse PP build for fan-out writes and benchmark it against MAI requirements; compare results with OpenAI TensorCache and internal Manifold/Singularity approaches. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Draft and publish scenario-based framing for distributed caching (fan-out writes, fan-out reads, fan-in reads, and KV cache) and update the shared documentation. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Prepare an MAI-focused proposal comparing the current lazy copy approach (local NVMe plus async copy to Blob) versus BlobFuse on performance, complexity, and risk. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Create a Microsoft Teams room to centralize distributed cache materials and share it with the team, including Jean (unknown last name) and Jay Jagant. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Upload and share Whipple/Manifold slides and related comparison links in the shared Teams room. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Schedule a Manifold/Singularity deep-dive session and invite the broader team. @TBD 📅 2025-10-26 #task #proposed #auto

- [?] Provide the BlobFuse PP build, deployment guide, and 100-node CycleCloud performance results to enable evaluation. @Vishnu Charan TJ 📅 2025-09-19 ⏫ #task #proposed #auto

- [?] Ensure the inferencing team receives a usable BlobFuse build and completes an evaluation. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Explore adding inferencing leadership (Rajat Monga) and DPU stakeholders to the 2025-10-15 Silicon Valley offsite agenda. @Jai Menon 📅 2025-10-10 #task #proposed #auto

- [?] Get a clear answer on why MAI cannot use BlobFuse today and what specific changes would unblock adoption. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Validate Manifold's consistent hashing approach for scale-in/scale-out behavior and quantify data rebalancing costs. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Assess Alluxio viability to fork and own, including IP and China-related concerns and Java stack implications for customers and internal teams. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Confirm whether BlobFuse's Go plus FUSE implementation can meet performance targets; define a fallback plan if a C++ or kernel-mode client is required. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Decide metadata strategy for distributed caching: build a high-TPS metadata/index store versus adopting an open-source option such as FoundationDB. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Clarify the North Star decision for distributed caching: build/own versus open source versus internal solutions, and whether to pursue hardware offload or kernel-mode integration now versus later. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Obtain current stability and roadmap signals for OpenAI TensorCache and assess whether expected churn (driven by GPT-6 memory/long-context focus) is acceptable for dependency or reference use. @Myself 📅 2025-10-26 🔽 #task #proposed #auto




## Decisions


- Jason Vallery will book travel to attend the Microsoft Apollo team offsite in Silicon Valley on 2025-10-15.




## Key Information


- Jai Menon confirmed a Microsoft Apollo team offsite in Silicon Valley on 2025-10-15 for approximately 1.5 days, with casual sessions, a social/dinner on day 1, and release around noon on day 2.

- Microsoft AI Infrastructure (MAI) currently writes checkpoints to local NVMe and asynchronously copies them to Azure Blob Storage; simplicity is valued and checkpoints tolerate partial loss.

- BlobFuse PP currently targets fan-out writes and has limited or no read caching; some scale testing was done via a 100-node CycleCloud simulation.

- The inferencing team expressed interest in BlobFuse but reportedly has not received a usable build for approximately two months.

- Manifold reportedly outperforms OpenAI TensorCache in shared benchmarks and uses consistent hashing without a central metadata store.

- OpenAI TensorCache reportedly moved away from a metadata store toward hashing, and churn is expected as GPT-6 focuses on memory and long context.

- Jai Menon chose Silicon Valley (instead of Redmond) for the 2025-10-15 offsite to enable the team to meet DPU/FunOS stakeholders and learn about upcoming chip directions and the FunOS programming environment.



---

*Source: [[2025-09-15 - Jason and Jai discussed options and strategy for distributed caching (BlobFuse v]]*