---
type: "people"
title: "1:1 with Jai Menon: Distributed cache strategy for MAI, BlobFuse PP readiness, and Oct 15 SVC offsite"
date: "2025-09-15"
person: ""
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-15 - Discussed distributed cache strategy, MAI needs, and BlobFuse readiness. Aligned.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon: Distributed cache strategy for MAI, BlobFuse PP readiness, and Oct 15 SVC offsite

**Date**: 2025-09-15
**With**: Jason Vallery, Jai Menon

## Summary

Jai Menon and Jason Vallery aligned on evaluating distributed caching options for Microsoft AI Infrastructure (MAI) across clear scenarios (fan-out writes, fan-out reads, fan-in reads, KV cache) and producing a concise recommendation after benchmarking. Jai will stand up a shared Teams room and drive Manifold (Singularity) briefings, while Jason will obtain and test BlobFuse PP, compare against Manifold and OpenAI TensorCache, and craft an MAI-oriented narrative with benchmarks. The team offsite was confirmed for Wednesday 2025-10-15 in Silicon Valley with planned DPU/FunOS and inferencing/KV cache sessions.


## Action Items


- [?] Create a Microsoft Teams room for the distributed caching effort, add all current docs/links, and share access with stakeholders (Jason Vallery, Jean, Jay Jagant, and others). @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Coordinate with Vipul to schedule a Manifold (Singularity) team briefing and Q&A session. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Share Manifold slides/docs and the Manifold vs TensorCache comparison link in the Teams room. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Obtain BlobFuse PP bits and the deployment guide from Vishnu Charan TJ, stand up tests (including fan-out writes), and collect performance results at target scale. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate OpenAI TensorCache and compare it with Manifold and BlobFuse on functionality, performance, and stability for MAI-relevant scenarios. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Restructure the distributed cache evaluation document by scenarios (fan-out writes, fan-out reads, fan-in reads, KV cache) and map candidate solutions to each scenario. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Prepare an MAI-focused proposal showing how BlobFuse compares to the current async-copy-to-Blob approach on performance, complexity, risks, and scale, including benchmarks. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Set up a requirements call with MAI stakeholders (including Pete and partners) to validate needs and adoption criteria for a distributed cache solution. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Analyze metadata strategy trade-offs (consistent hashing vs high-TPS metadata store) and document implications for scale-in/scale-out and rebalancing. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Assess BlobFuse implementation choices (Go and FUSE) versus a potential C++ client or kernel-mode client, including performance and time-to-market trade-offs. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Reach out to Rajat Monga to invite an inferencing and KV cache session at the 2025-10-15 Silicon Valley offsite. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Book travel for the Silicon Valley offsite on 2025-10-15. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Share BlobFuse PP bits and the deployment guide with the inferencing team once available and collect feedback on usability and performance needs. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Draft the 2025-10-15 offsite agenda including DPU/FunOS and inferencing sessions, then circulate to attendees. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Confirm BlobFuse PP availability and capture the results and metrics from the recent 100-node test with Vishnu Charan TJ, including any bottlenecks. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Verify Manifold's scale-in/scale-out behavior with consistent hashing, including any rebalancing strategy and operational impact. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Determine the stability and near-term roadmap status of OpenAI TensorCache relevant to the evaluation and potential adoption. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Clarify Alluxio IP and China optics concerns and assess Java runtime stack implications for enterprise adoption. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Confirm attendance and logistics for the Girish storage discussion and adjust travel if needed. @Jai Menon 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Align on the long-term vision for hardware offload or a kernel-mode driver versus an interim user-space approach for distributed caching performance. @Jai Menon 📅 2025-10-26 #task #proposed #auto




## Decisions


- Hold the team offsite in Silicon Valley on 2025-10-15 as a day-and-a-half event with a light schedule and a social/dinner component, and include DPU/FunOS and potentially inferencing/KV cache sessions.

- Create a shared Microsoft Teams room to centralize distributed caching documents, links, and ongoing discussion for the evaluation.




## Key Information


- Jai Menon confirmed a team offsite in Silicon Valley on 2025-10-15, planned as a day-and-a-half with a light schedule and a social dinner, and intended to include DPU and FunOS sessions.

- Microsoft AI Infrastructure (MAI) currently writes checkpoints to local NVMe and asynchronously copies them to Azure Blob Storage, prioritizing simplicity.

- BlobFuse PP is primarily focused on fan-out writes and has limited read caching; a recent 100-node test was mentioned with a deployment guide still pending.

- The inferencing team expressed interest in BlobFuse but had not received the bits, and a roughly two-month delay was noted as a confidence risk.

- Manifold (also referred to as Singularity) claims a consistent-hashing approach without a central metadata store, but scale-in/scale-out rebalancing behavior remains an open question.

- OpenAI TensorCache was described as unstable and fast-changing; a performance comparison presented by Whipple reportedly favored Manifold over TensorCache.

- Alluxio raised concerns around IP and China optics as well as Java runtime components, which may be problematic for some enterprise customers.

- BlobFuse performance risk was discussed due to Go and FUSE implementation choices, with a potential longer-term path involving a C++ client or kernel-mode driver and possible hardware offload, which would increase risk and time-to-market.

- Jai Menon planned to reach out to Rajat Monga to invite an inferencing and KV cache session at the Silicon Valley offsite.



---

*Source: [[2025-09-15 - Discussed distributed cache strategy, MAI needs, and BlobFuse readiness. Aligned]]*