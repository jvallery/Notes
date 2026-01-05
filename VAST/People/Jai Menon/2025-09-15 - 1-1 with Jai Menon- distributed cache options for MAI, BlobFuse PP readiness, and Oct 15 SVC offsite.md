---
type: "people"
title: "1:1 with Jai Menon: distributed cache options for MAI, BlobFuse PP readiness, and Oct 15 SVC offsite"
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

# 1:1 with Jai Menon: distributed cache options for MAI, BlobFuse PP readiness, and Oct 15 SVC offsite

**Date**: 2025-09-15
**With**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon aligned on evaluating distributed cache approaches for Microsoft AI Infrastructure (MAI) using scenario-based requirements (fan-out writes, fan-out reads, fan-in reads, KV cache). Jai will centralize collateral in a shared Teams room and pursue a Manifold (Singularity) briefing, while Jason will obtain and benchmark BlobFuse PP, compare against Manifold and OpenAI TensorCache, and craft an MAI-oriented recommendation with benchmarks. They confirmed a team offsite in Silicon Valley on 2025-10-15 and intend to include DPU/FunOS and inferencing/KV cache sessions.


## Action Items


- [?] Create a Microsoft Teams room for distributed caching work and add all current documents and links, then share access with stakeholders (including Jason Vallery, Jean, and Jay Jagant). @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Coordinate with Vipul to schedule a Manifold (Singularity) team briefing and Q&A session. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Share Manifold slides and documents plus the Manifold vs OpenAI TensorCache comparison link in the Teams room. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Obtain BlobFuse PP bits and the deployment guide from Vishnu Charan TJ, stand up tests (including fan-out writes), and collect performance results at target scale. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate OpenAI TensorCache and compare it with Manifold and BlobFuse on functionality, performance, and stability for MAI-relevant scenarios. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Restructure the distributed cache evaluation document by scenarios (fan-out writes, fan-out reads, fan-in reads, KV cache) and map candidate solutions to each scenario. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Prepare an MAI-focused proposal showing how BlobFuse compares to MAI's current async copy approach (local NVMe to Azure Blob) across performance, complexity, risks, and scale, including benchmarks. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Set up a requirements call with Microsoft AI Infrastructure (MAI) stakeholders (including Pete and partners) to validate needs and adoption criteria for distributed caching. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Analyze metadata strategy trade-offs between consistent hashing and a high-TPS metadata store, including implications for scale-in/scale-out and rebalancing. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Assess BlobFuse implementation trade-offs (Go and FUSE) versus a potential C++ or kernel-mode client, including performance and time-to-market implications. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Reach out to Rajat Monga to invite an inferencing and KV cache session at the 2025-10-15 Silicon Valley offsite. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Book travel for the Silicon Valley offsite on 2025-10-15. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Share BlobFuse PP bits and the deployment guide with the Microsoft inferencing team once available and collect feedback on adoption and performance. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Draft the 2025-10-15 Silicon Valley offsite agenda including DPU/FunOS sessions and inferencing sessions, then circulate to attendees. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Confirm BlobFuse PP availability and the 100-node test results with Vishnu Charan TJ, capturing metrics and bottlenecks. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Verify Manifold's approach to scale-in/scale-out with consistent hashing and any rebalancing strategy. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Determine stability and roadmap status of OpenAI TensorCache relevant to near-term evaluations. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Clarify Alluxio IP and China optics concerns and Java runtime stack implications for enterprise adoption. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Confirm attendance and logistics for the Girish storage discussion and adjust travel if needed. @Jai Menon 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Align on the long-term vision for hardware offload or a kernel-mode driver versus an interim user-space approach for distributed caching. @Jai Menon 📅 2025-10-26 #task #proposed #auto




## Decisions


- Hold the team offsite in Silicon Valley on 2025-10-15 with a day-and-a-half agenda and optional social/dinner on day 1.

- Create a shared Microsoft Teams room to centralize distributed caching documents, links, and ongoing discussion.




## Key Information


- Jai Menon scheduled a team offsite in Silicon Valley for 2025-10-15 with a day-and-a-half format, light schedule, and a social event or dinner on day 1, with an early departure around noon on day 2.

- Microsoft AI Infrastructure (MAI) currently writes checkpoints to local NVMe and asynchronously copies them to Azure Blob Storage, prioritizing simplicity.

- BlobFuse PP is primarily focused on fan-out writes and has limited read caching; a recent 100-node test occurred but the deployment guide was still pending at the time of the discussion.

- The Microsoft inferencing team expressed interest in BlobFuse but had not received the pre-production bits, with an approximately two-month delay noted.

- Manifold (also referred to as Singularity) claims a consistent-hashing approach without a central metadata store, but questions remain about scale-in/scale-out behavior and data rebalancing.

- OpenAI TensorCache was described as unstable and fast-changing; a performance comparison presented by Whipple reportedly favored Manifold over TensorCache.

- Alluxio raised concerns related to IP and China optics and reliance on Java components, which may impact enterprise adoption.

- BlobFuse performance concerns were discussed around Go and FUSE implementation choices versus a potential C++ or kernel-mode client, with kernel-mode or hardware offload viewed as higher risk and longer time-to-market.



---

*Source: [[2025-09-15 - Discussed distributed cache strategy, MAI needs, and BlobFuse readiness. Aligned]]*