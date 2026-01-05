---
type: "people"
title: "1:1 with Jai Menon: OpenAI cache evaluation for MAI and next-step deep dives"
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

# 1:1 with Jai Menon: OpenAI cache evaluation for MAI and next-step deep dives

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon reconnected after Jason’s sabbatical and aligned Jason’s initial focus on evaluating OpenAI’s AI caching approach for Microsoft AI Infrastructure (MAI) at extreme scale. They reviewed MAI scale and integration requirements (up to ~100k nodes, AKS/Kubernetes, Spark), compared alternative cache options (BlobFuse/BlockFuse, AC Store, Alluxio/DAX), and discussed Microsoft’s Blob and Bifrost direction including a direct read path. Next steps include confirming OpenAI IP and code access, meeting with MAI and Ong on Friday 2025-09-05, and starting a technical evaluation with supporting docs from Jai.


## Action Items


- [?] Confirm legal/IP rights for OpenAI caching code and request/secure code access for Jason Vallery (coordinate with Pete and SILA legal). @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate OpenAI caching code for MAI feasibility, including architecture (unified vs separate caches), performance and scale to ~100,000 nodes, and fit with AKS/Kubernetes and Apache Spark; produce a written recommendation. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Meet with Ong on Friday 2025-09-05 to discuss the performance snapshot outcome and decide whether to escalate concerns to Manish. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Meet MAI stakeholders on Friday 2025-09-05 (lunch) to confirm requirements and current status, including GPU counts, multi-region distributed cache needs, cluster status, and training framework plans. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Review latest BlockFuse/BlobFuse progress and Nagendra’s long-form document (described as ~50 pages) and sync with the relevant team on implications for MAI caching. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Compare caching options (BlobFuse/BlockFuse, AC Store, Alluxio/DAX) against MAI scale and AKS/Spark integration requirements; capture pros and cons in a short options matrix. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Sync with Lukasz to understand the Bifrost direct read path (bypassing FE/table layers) and assess applicability to MAI workloads. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Send Jason Vallery the OpenAI IP agreement details referenced in prior discussions (OpenAI IP note). @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send Jason Vallery the MAI 'frictions with Microsoft infrastructure' document (described as ~10 pages). @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Send Jason Vallery the Apollo document referenced in the discussion. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Connect Jason Vallery with Lukasz regarding Bifrost direct read path implementation details. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Establish a regular 1:1 cadence between Jason Vallery and Jai Menon (recurring meeting). @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] After OpenAI IP/legal confirmation, obtain and review the OpenAI cache codebase. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Walk Jai Menon through the agentic coding workflow demo when time permits. @Myself 📅 2025-10-26 🔽 #task #proposed #auto




## Decisions


- Jason Vallery’s primary near-term focus is to evaluate OpenAI’s caching solution for feasibility and suitability for Microsoft AI Infrastructure (MAI), while tracking alternative options (BlobFuse/BlockFuse, AC Store, Alluxio/DAX).

- The caching work will prioritize training cache requirements first, with inference knowledge-base caching to follow after training requirements are understood.

- The target design direction is a unified, pluggable cache that can support multiple frameworks (not tied to a single training framework).




## Key Information


- Microsoft AI Infrastructure (MAI) target scale discussed was approximately 400,000 GPUs for training and approximately 40,000 GPUs for inference within about 2 years.

- MAI caching requirements discussed included scaling to approximately 100,000 nodes and integrating with AKS/Kubernetes and Apache Spark.

- The group preferred a unified, pluggable caching solution that can be used for both training and inference rather than framework-specific caches.

- OpenAI may provide IP and/or code that could be usable across Microsoft services, but legal confirmation and access approval were identified as prerequisites (involving Pete and SILA legal).

- Bifrost was described as adding a direct read path that bypasses front-end and table layers, and Lukasz was identified as implementing parts of this work.

- Jason Vallery’s sabbatical was impacted by his wife’s knee replacement, and he spent significant time at home; he also spent time learning agentic coding workflows and experimenting with tools like Codex, Claude, and GitHub Copilot.



---

*Source: [[2025-09-03 - Reconnected post-sabbatical and aligned on Jason’s initial focus evaluate OpenA]]*