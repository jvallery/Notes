---
type: "people"
title: "1:1 with Jai Menon: MAI caching evaluation focus and OpenAI IP/code access"
date: "2025-09-03"
person: ""
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon: MAI caching evaluation focus and OpenAI IP/code access

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon reconnected after Jason’s sabbatical and aligned Jason’s initial focus on evaluating OpenAI’s AI caching approach for Microsoft AI Infrastructure (MAI) at extreme scale. They discussed MAI scale and integration requirements (100k-node cache, AKS/Kubernetes, Spark), compared alternative cache options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX), and reviewed Microsoft’s Blob/Bifrost direction including a direct read path. Next steps include confirming OpenAI IP/code access, meeting MAI and Ong on Friday 2025-09-05, and starting a technical evaluation with supporting docs from Jai.


## Action Items


- [?] Evaluate OpenAI caching code for feasibility, architecture (unified vs separate caches), performance/scale to approximately 100,000 nodes, and fit with AKS/Kubernetes and Spark; produce a recommendation for MAI. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Confirm OpenAI IP rights and request code access with Pete and SILA legal so Jason Vallery can review the OpenAI cache implementation. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Send Jason Vallery the OpenAI IP agreement details referenced in prior discussions. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Discuss the performance snapshot outcome with Ong and decide whether to escalate to Maneesh Sah. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Meet MAI team (lunch) to confirm requirements including GPU counts, whether multi-region pooling is required, cluster status, and training framework plans. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Review latest Blockfuse/BlobFuse progress and Nagendra’s 50-page document and sync with the team on implications for MAI caching. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Compare caching options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX) against MAI scale and AKS/Kubernetes and Spark integration requirements; capture pros and cons. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Send the MAI 'frictions with Microsoft infra' 10-page document to Jason Vallery. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send the Apollo document to Jason Vallery. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Connect Jason Vallery with Lukasz to review Bifrost direct read path implementation details and relevance to MAI workloads. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Sync with Lukasz to understand Bifrost direct read path and assess applicability to MAI workloads. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Draft an AI caching requirements and options document for MAI, emphasizing unified cache design and training-first sequencing with inference KB caching later. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Walk Jai Menon through the agentic coding workflow demo when time permits. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Establish a regular 1:1 cadence between Jason Vallery and Jai Menon. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] After IP confirmation, obtain and review the OpenAI cache codebase. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto




## Decisions


- Primary focus for the MAI caching workstream is training cache requirements first, with inference KB caching to follow after.

- Target architecture direction is a unified, pluggable cache design that can support multiple frameworks (not tied to a single training framework).

- Jason Vallery will prioritize evaluation of the OpenAI caching solution while tracking alternative options (BlobFuse/Blockfuse, AC Store, Alluxio/DAX).




## Key Information


- Jason Vallery returned from a sabbatical and is shifting focus toward engineering deep dives and technical evaluations.

- Microsoft AI Infrastructure (MAI) target scale discussed was approximately 400,000 GPUs for training and approximately 40,000 GPUs for inference within about two years.

- MAI caching requirements discussed include scaling a cache to approximately 100,000 nodes and integrating with AKS/Kubernetes and Spark.

- Cache options under consideration for MAI include BlobFuse/Blockfuse, AC Store, Alluxio/DAX (including a KB cache), and an OpenAI cache if IP/code access is approved.

- A preference was stated for a single, pluggable caching solution usable for both training and inference, not tied to a single framework.

- OpenAI may provide IP/code that could be usable across Microsoft services, pending legal confirmation involving Pete and SILA legal.

- Bifrost was described as adding a direct read path that bypasses FE/table layers, and Lukasz is implementing parts of this.

- A potential MAI constraint to confirm is whether multi-region pooling is required for a distributed cache.

- Jai Menon indicated he sent Jason Vallery a performance snapshot and offered to join conversations with Wang Xi and/or Ong, and supported escalation to Manish if needed.



---

*Source: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]]*