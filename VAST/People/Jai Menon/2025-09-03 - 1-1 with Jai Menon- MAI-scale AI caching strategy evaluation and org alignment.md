---
type: "people"
title: "1:1 with Jai Menon: MAI-scale AI caching strategy evaluation and org alignment"
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

# 1:1 with Jai Menon: MAI-scale AI caching strategy evaluation and org alignment

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jai Menon and Jason Vallery aligned on a high-priority evaluation of AI caching options to support Microsoft AI Infrastructure (MAI) scale, with a near-term focus on training and a preference for a unified cache spanning training and inference. Jason will validate feasibility of using OpenAI cache IP at MAI scale and fit with AKS and Spark, and will reconnect with MAI stakeholders and the Bifrost team to clarify requirements and current Blob performance direction.


## Action Items


- [?] Evaluate feasibility of using OpenAI cache IP for Microsoft MAI at approximately 100,000 nodes, including confirming IP access, obtaining code, assessing code quality, architecture, scalability, and operational fit with AKS and Spark, with training as first priority and inference later. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Confirm legal and IP rights for using OpenAI cache code across Microsoft services by checking with Pete and SILA, and arrange access to the OpenAI cache codebase for evaluation. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Review latest Blockfuse and BlobFuse progress materials, including Nagendra's document if available, and capture current maturity and performance status for MAI caching needs. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Meet with Ong on Friday, 2025-09-05 to clarify Microsoft MAI requirements (scale, regions, timelines) and discuss concerns about the performance snapshot outcome. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Sync with Lukasz to understand the Bifrost direct-read path design (bypassing FE/table for reads) and current implementation status. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Draft an initial recommendation comparing OpenAI cache IP versus Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse for Microsoft MAI requirements, including a view on unified cache for training and inference. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] After the 2025-09-05 meeting with Ong, decide whether to escalate the performance snapshot discussion to Maneesh Sah. @Myself 📅 2025-09-05 #task #proposed #auto

- [?] Propose and establish a regular 1:1 cadence between Jason Vallery and Jai Menon. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Send Jason Vallery the OpenAI IP and usage note (and contact details), the MAI pain-points document (approximately 10 pages), and the Apollo document to support the caching evaluation. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Coordinate with Wamshi and SILA as needed after the initial OpenAI cache IP check to unblock access and evaluation. @Myself 📅 2025-10-26 #task #proposed #auto




## Decisions


- Prioritize a unified caching approach for Microsoft MAI, with training requirements addressed first and inference (including KB cache) following.

- Proceed with an initial feasibility evaluation of OpenAI cache IP for MAI-scale caching, in parallel with continued evaluation of Alluxio/DAX, C-Store proposals, and Blockfuse/BlobFuse approaches.

- Continue the Blob performance direction via Bifrost (including a direct read path), with DeltaZero considered as a subsequent step.




## Key Information


- Jai Menon stated MAI scale targets of approximately 400,000 GPUs for training and approximately 40,000 GPUs for inference within about two years.

- The MAI caching data-plane target scale discussed was approximately 100,000 nodes, with an operational environment of AKS plus Spark.

- Jai Menon indicated MAI may require multi-region, cross-WAN cache pooling, pending confirmation with MAI stakeholders.

- Jai Menon described a strategic preference for a single caching solution usable for both training and inference, and for the cache to be pluggable rather than tightly coupled to a single framework.

- Caching options under consideration for MAI included OpenAI cache IP, Alluxio/DAX (including inference and KB caching support), C-Store proposals, and Blockfuse/BlobFuse approaches.

- Jai Menon stated Bifrost is the current Blob performance direction and includes a direct read path that bypasses FE/table for reads, with Lukasz building parts of this.

- Jai Menon positioned DeltaZero as a potential follow-on to Bifrost (work in progress).

- Jai Menon stated compute ownership for MAI moved to Brendan Burns's AKS organization, with a CVP named Qi (also referred to as "Kiki" Ke) leading the compute side and Yumin interfacing from the storage side.

- Jason Vallery stated he was surprised and disappointed by a performance snapshot outcome that appeared to be "Meets Expectations" and planned to discuss it with Ong and potentially escalate to Maneesh Sah.



---

*Source: [[2025-09-03 - Jai outlined a high-priority evaluation for an AI caching strategy to support MA]]*