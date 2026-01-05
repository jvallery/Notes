---
type: "people"
title: "1:1 with Jai Menon: MAI-scale AI caching evaluation and OpenAI cache IP feasibility"
date: "2025-09-03"
person: ""
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon: MAI-scale AI caching evaluation and OpenAI cache IP feasibility

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jai Menon outlined a high-priority evaluation of an AI caching strategy to support Microsoft AI Infrastructure (MAI) at scale, with a strong preference for a unified cache spanning training and inference. Jason Vallery will validate feasibility of using OpenAI's cache IP (access, code quality, scalability to ~100k nodes, and fit with AKS and Spark) while also comparing Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse, and will reconnect with MAI stakeholders and Lukasz on Bifrost.


## Action Items


- [?] Evaluate feasibility of using OpenAI cache IP for Microsoft MAI, including confirming IP access, obtaining code, assessing architecture and code quality, validating scalability to approximately 100,000 nodes, and confirming operational fit with AKS and Spark (training first, inference later). @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Confirm legal and IP rights for using OpenAI cache code across Microsoft services by coordinating with Pete and SILA, and arrange access to the OpenAI cache codebase. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Review the latest Blockfuse and BlobFuse progress materials, including the document authored by Nagendra (if available), and capture current status and gaps for MAI needs. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Meet with Ong on Friday at the scheduled 1:1 to clarify Microsoft MAI requirements (scale, regions, timelines, and whether cross-WAN cache pooling is required) and discuss the performance snapshot outcome. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Sync with Lukasz to understand the Bifrost direct-read path design (bypassing front end and table layer for reads) and current implementation status. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Draft an initial recommendation comparing OpenAI cache vs Alluxio/DAX vs C-Store proposals vs Blockfuse/BlobFuse for Microsoft MAI requirements, including training-first and inference follow-on considerations. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] After the meeting with Ong, decide whether to escalate the performance snapshot discussion to Maneesh Sah and, if needed, request time with Maneesh Sah. @Myself 📅 2025-09-05 #task #proposed #auto

- [?] Propose and establish a regular 1:1 cadence between Jason Vallery and Jai Menon. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Send Jason Vallery the OpenAI IP and usage note (and contact details), the MAI pain-points document (approximately 10 pages), and the Apollo document referenced in the discussion. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Coordinate with Wamshi and SILA as needed after the initial OpenAI cache IP check to unblock access and evaluation. @Myself 📅 2025-10-26 #task #proposed #auto




## Decisions


- Prioritize a unified caching approach for Microsoft MAI, with training requirements addressed first and inference (knowledge base caching) following.

- Proceed with an initial feasibility evaluation of OpenAI cache IP in parallel with continued review of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse approaches for MAI.

- Continue Blob performance direction via the Bifrost initiative and consider DeltaZero as a subsequent step.




## Key Information


- Jason Vallery stated he was "wildly disappointed" by a performance snapshot outcome that appeared to be "Meets Expectations" and planned to discuss it with Ong and potentially escalate to Maneesh Sah.

- MAI scale targets discussed were approximately 400,000 GPUs for training and 40,000 GPUs for inference within about two years.

- Target MAI data-plane scale discussed was approximately 100,000 nodes, with an operational environment including AKS and Spark.

- Jai Menon expressed a strategic preference for a single caching solution usable for both training and inference, and for the cache to be pluggable rather than tightly coupled to a single framework.

- Caching options under consideration included OpenAI cache IP, Alluxio/DAX (noted as supporting inference and knowledge base caching), C-Store proposals, and Blockfuse/BlobFuse approaches.

- Bifrost was described as the current Blob performance direction, including a direct read path that bypasses the front end and table layer for reads, with Lukasz building parts of this.

- DeltaZero was positioned as a potential follow-on to Bifrost for Blob performance improvements.

- Compute ownership for MAI was said to have moved to Brendan Burns's AKS organization, with a CVP named Qi (also referred to as "Kiki" Ke) leading the compute side and Yumin interfacing from the storage side.

- Potential multi-region, cross-WAN cache pooling was raised as a possible MAI requirement, pending confirmation with MAI stakeholders.



---

*Source: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]]*