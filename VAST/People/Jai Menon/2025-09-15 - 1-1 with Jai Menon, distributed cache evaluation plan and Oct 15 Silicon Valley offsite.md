---
type: "people"
title: "1:1 with Jai Menon, distributed cache evaluation plan and Oct 15 Silicon Valley offsite"
date: "2025-09-15"
person: ""
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Jason and Jai aligned on next steps for a distributed cache strategy and short-t.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon, distributed cache evaluation plan and Oct 15 Silicon Valley offsite

**Date**: 2025-09-15
**With**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon aligned on evaluating distributed cache options for Microsoft AI Infrastructure (MAI) and agreed to frame requirements by fan-out writes, fan-out reads, and fan-in reads, with KV cache treated separately. They also confirmed a Silicon Valley team offsite on 2025-10-15 for about 1.5 days, including DPU and inferencing sessions.


## Action Items


- [?] Book travel for the Silicon Valley team offsite starting 2025-10-15 (approximately 1.5 days). @Myself 📅 2025-10-15 ⏫ #task #proposed #auto

- [?] Create a shared Microsoft Teams space for the distributed cache workstream and upload or link relevant collateral (for example Manifold or Singularity slides and comparison documents) and grant access to stakeholders. @Jai Menon 📅 2025-09-22 ⏫ #task #proposed #auto

- [?] Invite Microsoft DPU engineers to the 2025-10-15 Silicon Valley offsite and confirm sessions covering next DPU chip direction and the FunOS programming environment. @Jai Menon 📅 2025-10-01 #task #proposed #auto

- [?] Attempt to secure Rajat Monga (Microsoft inferencing leader) participation in the 2025-10-15 Silicon Valley offsite to cover KV caching and inferencing integration with the OpenAI inferencing framework. @Jai Menon 📅 2025-10-01 #task #proposed #auto

- [?] Evaluate BlobFuse plus AC Store against alternatives (Manifold or Singularity, OpenAI TensorCache, Alluxio, JuiceFS, NVIDIA AIStore) using scenario-based use cases (fan-out writes, fan-out reads, fan-in reads) and treat KV cache separately, then draft a recommendation for MAI adoption criteria. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto




## Decisions


- Jason Vallery will travel to the Silicon Valley team offsite on 2025-10-15 (approximately 1.5 days).

- Centralize distributed cache workstream collateral in a new shared Microsoft Teams space.




## Key Information


- Jai Menon is organizing a team offsite in Silicon Valley on 2025-10-15 for approximately 1.5 days, with dinner or a social event on day 1 and a half-day session on day 2 so attendees can fly home around noon.

- The Silicon Valley offsite is being held in California (instead of Redmond) to enable Jai Menon’s team to meet Microsoft DPU engineers and learn about the next DPU chip, the FunOS programming environment, and potential DPU-related work.

- Jai Menon plans to invite Microsoft inferencing stakeholders, including Rajat Monga, to discuss KV caching, inferencing, and how their work fits into the OpenAI inferencing framework (not open source).

- Jason Vallery confirmed he should book travel to attend the Silicon Valley offsite on 2025-10-15; Jai Menon noted Jason’s travel was not originally included in the submitted budget but should be included.

- Jason Vallery recently met with Ankit to understand what Ankit is working on and met with Lukash to learn about the Bifrost project status.

- For MAI checkpointing, the current preferred approach is writing to local NVMe and asynchronously copying checkpoints to Azure Blob Storage; MAI will only consider BlobFuse if it clearly improves performance and reduces complexity at MAI scale.

- BlobFuse private preview is currently focused on fan-out writes, with limited read caching maturity; a recent 100-node CycleCloud test occurred and a deployment guide is pending.

- Alluxio has perceived risks including IP or China perception concerns and implications of its Java-based stack.

- The inference team has been waiting approximately two months for BlobFuse private preview bits after an initial introduction, creating a credibility risk with internal stakeholders.



---

*Source: [[2025-09-15 - Jason and Jai aligned on next steps for a distributed cache strategy and short-t]]*