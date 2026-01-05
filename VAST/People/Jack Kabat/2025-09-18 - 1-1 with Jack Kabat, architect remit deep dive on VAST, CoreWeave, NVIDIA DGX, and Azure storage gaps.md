---
type: "people"
title: "1:1 with Jack Kabat, architect remit deep dive on VAST, CoreWeave, NVIDIA DGX, and Azure storage gaps"
date: "2025-09-18"
person: ""
participants: ["Jason Vallery", "Jack Kabat"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-18 - Jason outlined his new architect remit to assess VAST and CoreWeave strategies,.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jack Kabat, architect remit deep dive on VAST, CoreWeave, NVIDIA DGX, and Azure storage gaps

**Date**: 2025-09-18
**With**: Jason Vallery, Jack Kabat

## Summary

I shared with Jack Kabat that I returned from a 3-month sabbatical into a new architect role (carved out by Manish Sah) and my first task is a deep dive on VAST Data and CoreWeave strategies, NVIDIA DGX alignment, and Azure storage gaps, with Project Apollo likely in scope. We compared VAST DataSpaces (global namespace, strong consistency, cross-region locking) versus OpenAI patterns (local NVMe on GPU hosts plus blob for cheap and deep, with proprietary global/regional sync above Azure data movement) and aligned that Azure needs layered storage capabilities independent of OpenAI IP.


## Action Items


- [?] Conduct a deep dive on VAST Data and CoreWeave strategies and capabilities, NVIDIA DGX alignment, and Microsoft Azure storage gaps, then propose a recommended direction for Azure AI storage. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate storage architecture options for Azure AI workloads, comparing GPU-adjacent flash and global namespace approaches (VAST DataSpaces) versus OpenAI-style local NVMe on GPU hosts plus blob for cheap and deep, and recommend a layered approach including global namespace and consistency needs independent of OpenAI IP. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Identify and engage internal SMEs on VAST Data (including the person referred to as "Khan Channel") to gather insights and any relevant offsite materials for the VAST and CoreWeave deep dive. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Assess Project Apollo implications for Azure AI storage strategy, including whether Apollo is an innovation path, a duplicative effort, or an integration point for the recommended layered storage approach. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Schedule a follow-up meeting with Jack Kabat to review findings and recommendations from the VAST and CoreWeave deep dive and Azure storage gap assessment. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Share correct contact details for the internal SME referred to as "Khan Channel" and provide any relevant offsite notes that inform the VAST Data and CoreWeave assessment. @Jack Kabat 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Provide context on "UK Met Office Gen 2" and how it relates to VAST Data engagements or learnings relevant to Azure AI storage strategy. @Jack Kabat 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Check with NVIDIA contact "Vlad" for current DGX Cloud storage deployment patterns that could inform Microsoft Azure AI storage strategy and the VAST Data and CoreWeave deep dive. @Jack Kabat 📅 2025-10-27 🔽 #task #proposed #auto




## Decisions


- Jason Vallery will proceed with a deep dive on VAST Data and CoreWeave strategies, NVIDIA DGX alignment, and Microsoft Azure storage gaps as the first task in his new architect role, including assessing Project Apollo implications.




## Key Information


- Jason Vallery returned from a 3-month sabbatical and moved into a new architect role carved out by Maneesh Sah to assess where Microsoft is headed on AI cloud and storage strategy.

- Jason Vallery's initial architect focus is a deep dive on VAST Data and CoreWeave capabilities, NVIDIA DGX alignment, and Microsoft Azure storage gaps, with Project Apollo likely relevant.

- Jack Kabat described Microsoft as over-indexing on operational execution (rack and ship GPUs) versus innovation and product planning, with frequent organizational changes and new initiatives creating uncertainty (including Project Apollo).

- Jack Kabat stated Microsoft Azure has walls between control plane and job plane, while CoreWeave offers a more curated, integrated control plane and job plane experience that enables maintenance awareness of job placement and synchronization.

- Jason Vallery stated CoreWeave positions VAST Data as its preferred storage platform but also built its own object storage platform alongside VAST to avoid full vertical coupling to VAST.

- Jack Kabat said NVIDIA is deploying DGX Cloud globally via its professional services organization and NVIDIA is not a storage company, so it fills the storage gap via partners.

- Jack Kabat referenced an NVIDIA contact named Vlad who moved to NVIDIA and works in NVIDIA professional services deploying DGX Cloud globally; Vlad previously supported deployments at Microsoft.

- Jack Kabat recommended an internal Microsoft team member whose name sounded like "Khan Channel" as the closest SME on VAST Data and related storage topics.



---

*Source: [[2025-09-18 - Jason outlined his new architect remit to assess VAST and CoreWeave strategies,]]*