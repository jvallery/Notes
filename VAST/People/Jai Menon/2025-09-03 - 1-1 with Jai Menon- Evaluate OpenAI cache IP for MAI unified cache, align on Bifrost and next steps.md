---
type: "people"
title: "1:1 with Jai Menon: Evaluate OpenAI cache IP for MAI unified cache, align on Bifrost and next steps"
date: "2025-09-03"
person: ""
participants: ["Jason Vallery", "Jai Menon"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon: Evaluate OpenAI cache IP for MAI unified cache, align on Bifrost and next steps

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jai Menon outlined a near-term technical focus to evaluate OpenAI’s caching code as a candidate for Microsoft AI Infrastructure (MAI) unified cache, prioritizing training first while designing for inference and KB caching. Jason Vallery will confirm IP and repository access, review the code for architecture and production readiness, assess scalability to ~100k nodes on AKS plus Spark, and compare against BlobFuse, Alluxio/DAX, and AC Store, while also syncing with Ong and Bifrost owners and setting a regular cadence with Jai.


## Action Items


- [?] Confirm Microsoft legal and IP clearance and repository access for OpenAI’s caching code, coordinating with Pete and Sila, and request access for Jason Vallery. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Review OpenAI cache code and document architecture, training vs inference and KB caching capabilities, and production readiness for MAI unified cache evaluation. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Assess whether OpenAI cache can scale to approximately 100,000 nodes and fit with AKS plus Spark, and identify gaps versus MAI requirements. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Meet with Ong on Friday to discuss performance review snapshot feedback and MAI constraints, then decide whether to escalate to Manish and Wamshi. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Re-engage with Nagendra and Krishnan teams to get the latest on BlobFuse and AC Store proposals and performance data, and compare them to OpenAI cache. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Confirm with MAI stakeholders whether multi-region logical cache pooling is a requirement and capture latency and consistency expectations. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Connect with Lukasz to understand the Bifrost direct read path design and implications for distributed cache integration. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Send OpenAI IP agreement details and MAI pain points document to Jason Vallery, and share the Apollo document when it is ready. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Set a regular 1:1 cadence with Jai Menon for ongoing alignment on MAI unified cache evaluation and related stakeholder coordination. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] If OpenAI IP is cleared, obtain OpenAI cache code artifacts and set up a review environment for evaluation. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Collect performance numbers and scaling plans from Alluxio/DAX and BlobFuse teams for a side-by-side comparison against OpenAI cache for MAI workloads. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Review MAI pain points and Apollo documents to refine MAI unified cache requirements and evaluation criteria. @Myself 📅 2025-10-26 #task #proposed #auto




## Decisions


- Jason Vallery will lead an evaluation of OpenAI’s caching approach as a candidate for Microsoft MAI unified cache and compare it against BlobFuse, Alluxio/DAX, and AC Store.

- The preferred architecture direction for MAI is a single, pluggable cache that supports training first and is designed to extend to inference and KB caching.

- Near-term performance direction for Azure Blob is Bifrost (direct read path bypassing FE and table layers), with DeltaZero positioned as a follow-on.




## Key Information


- Jai Menon stated that Microsoft AI Infrastructure (MAI) is targeting approximately 400,000 GPUs for training and 40,000 GPUs for inference within two years, implying a cache layer that can scale to roughly 100,000 nodes.

- Jai Menon stated that the MAI cache must run on AKS plus Spark and should be pluggable across frameworks, with a preference for a single unified cache that supports both training and inference, including KB caching.

- Jai Menon identified OpenAI caching code as a candidate for MAI unified cache, but Microsoft legal and IP clearance and repository access must be confirmed (contacts mentioned: Pete and Sila).

- Jai Menon stated that options under evaluation for MAI caching include OpenAI cache IP, Alluxio/DAX, BlobFuse, and AC Store (associated with Krishnan’s team).

- Jai Menon stated that Bifrost is the near-term performance path for Azure Blob, adding a direct read path that bypasses FE and table layers, and that DeltaZero is positioned as a potential follow-on.

- Jai Menon stated that Lukasz is building parts of Bifrost related to the direct read path.

- Jai Menon stated that compute for AI moved to Brendan’s organization, that Kiki (CVP) is leading AKS compute for MAI, and that Yumin is interfacing.

- Jason Vallery stated he has a 1:1 scheduled with Ong on Friday to discuss the snapshot feedback and MAI needs, and may escalate to Manish and Wamshi depending on the outcome.

- Jai Menon indicated a possible MAI requirement to confirm: multi-region logical cache pooling, including latency and consistency expectations.



---

*Source: [[2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca]]*