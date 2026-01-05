---
type: "people"
title: "1:1 with Jack Kabat: architect remit deep dive on VAST, CoreWeave, NVIDIA DGX, and Azure storage gaps (Apollo in scope)"
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

# 1:1 with Jack Kabat: architect remit deep dive on VAST, CoreWeave, NVIDIA DGX, and Azure storage gaps (Apollo in scope)

**Date**: 2025-09-18
**With**: Jason Vallery, Jack Kabat

## Summary

Jason Vallery and Jack Kabat aligned on Jason’s new architect remit to assess VAST Data and CoreWeave strategies, NVIDIA DGX-driven direction, and gaps in Microsoft Azure’s storage stack, with Project Apollo likely in scope. They compared VAST’s global namespace and strong consistency approach (DataSpaces) versus OpenAI’s pattern of local NVMe on GPU hosts plus Azure Blob for cheap and deep storage, with proprietary global and regional sync above Azure data movement. They agreed Azure needs a layered storage approach and capabilities independent of OpenAI, and Jason will return with recommendations after a deep dive.


## Action Items


- [?] Conduct a deep dive on VAST Data and CoreWeave strategies and capabilities, NVIDIA DGX alignment, and Microsoft Azure storage gaps, then propose a recommended direction for Microsoft AI Infrastructure. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate storage architecture options for Azure-scale AI workloads, including GPU-adjacent flash (VAST-style) versus OpenAI-style local NVMe on GPU hosts plus Azure Blob for cheap and deep storage, and recommend a layered approach including global namespace and strong consistency needs beyond OpenAI proprietary sync. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Identify and engage internal VAST Data SMEs, including the contact referred to as 'Khan Channel', to gather insights and any relevant offsite materials for the VAST and CoreWeave deep dive. @Myself 📅 2025-10-27 #task #proposed #auto

- [?] Assess Project Apollo implications, including whether it is an innovation path or duplicative effort, and identify integration points with the proposed Azure storage strategy. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Schedule a follow-up meeting with Jack Kabat to review findings and recommendations from the VAST and CoreWeave deep dive. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Share correct contact details for the internal Microsoft SME referred to as 'Khan Channel' and provide any relevant offsite notes related to VAST Data and storage strategy. @Jack Kabat 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Provide context on 'UK Met Office Gen 2' and how it relates to VAST Data engagements or evaluations. @Jack Kabat 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Check with NVIDIA contact 'Vlad' for current DGX Cloud storage deployment patterns that are relevant to Microsoft Azure strategy and share findings with Jason Vallery. @Jack Kabat 📅 2025-10-27 #task #proposed #auto




## Decisions


- Jason Vallery will proceed with a deep dive on VAST Data and CoreWeave strategies and capabilities, NVIDIA DGX alignment, and Microsoft Azure storage gaps as his first task in the new architect role.




## Key Information


- Jason Vallery returned from a 3-month sabbatical and moved into a new architect role carved out by Maneesh Sah to assess where Microsoft AI Infrastructure is headed, including likely involvement with Project Apollo.

- Jason Vallery’s initial architect focus is a deep dive on VAST Data and CoreWeave capabilities, NVIDIA alignment, and Microsoft Azure storage gaps, with Project Apollo likely relevant.

- Jack Kabat believes Microsoft has over-indexed on being an operational cloud (rack and ship GPUs) versus innovation, product design, and planning, and that internal execution has historically been slow for these AI infrastructure needs.

- Jack Kabat raised concern that Project Apollo may represent either meaningful innovation for an 'AI Cloud' or internal noise and duplication relative to Azure, creating uncertainty about where to focus.

- CoreWeave positions VAST Data as its preferred storage platform but also built its own object storage platform alongside VAST to avoid full vertical coupling to a single storage vendor.

- NVIDIA is pushing DGX architecture and hardware-level optimizations that integrate with the VAST Data stack; NVIDIA is not a storage company and fills the storage gap via partners.

- Jack Kabat stated that an internal Microsoft contact referred to as 'Khan Channel' is likely the closest SME on the team for VAST Data and related storage topics.

- A named NVIDIA contact 'Vlad' moved into NVIDIA professional services focused on deploying DGX Cloud globally; Jack Kabat described Vlad as a key deployment-side expert.



---

*Source: [[2025-09-18 - Jason outlined his new architect remit to assess VAST and CoreWeave strategies,]]*