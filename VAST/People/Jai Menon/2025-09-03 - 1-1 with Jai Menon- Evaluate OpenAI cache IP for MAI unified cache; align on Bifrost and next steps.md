---
type: people
title: '1:1 with Jai Menon: Evaluate OpenAI cache IP for MAI unified cache; align on Bifrost and next steps'
date: '2025-09-03'
person: Jai Menon
participants:
- Jason Vallery
- Jai Menon
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-03 - Jai outlined a near-term technical focus evaluate OpenAI’s caching code as a ca.md
tags:
- type/people
- generated
---

# 1:1 with Jai Menon: Evaluate OpenAI cache IP for MAI unified cache; align on Bifrost and next steps

**Date**: 2025-09-03
**With**: Jason Vallery, Jai Menon

## Summary

Jai Menon aligned with Jason Vallery on a near-term technical focus to evaluate OpenAI’s caching code as a candidate for Microsoft AI Infrastructure (MAI) unified cache, prioritizing training first while designing for eventual inference and KB caching. Jason will confirm IP and repo access, review the code for architecture and production readiness, assess scalability to ~100k nodes on AKS plus Spark, and compare against BlobFuse, Alluxio/DAX, and AC Store; Bifrost remains the near-term performance path for Azure Blob with DeltaZero as a follow-on.

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

- [?] Confirm Microsoft legal and IP clearance and repository access for OpenAI’s caching code (coordinate with Pete and Sila) and request access for Jason Vallery. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Review OpenAI caching code and document architecture, training vs inference and KB caching capabilities, and production readiness for MAI unified cache evaluation. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Assess whether OpenAI caching code can scale to approximately 100k nodes and fit with AKS plus Spark, and identify gaps versus MAI requirements. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Meet with Ong on Friday, 2025-09-05, to discuss snapshot feedback and MAI constraints, then decide whether to escalate to Manish and Wamshi. @Myself 📅 2025-09-05 ⏫ #task #proposed #auto

- [?] Re-engage with Nagendra and Krishnan teams to obtain the latest BlobFuse and AC Store proposals and performance data, then compare against OpenAI cache evaluation results. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Connect with Lukasz to understand Bifrost direct read path design and implications for integrating a distributed cache for MAI workloads. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Send OpenAI IP agreement details and MAI pain points document to Jason Vallery, and share Apollo documentation when available. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Set a regular 1:1 cadence with Jai Menon. @Myself 📅 2025-10-26 🔽 #task #proposed #auto

- [?] After the Ong discussion, schedule conversations with Manish and Wamshi if escalation is needed based on snapshot feedback and MAI constraints. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Collect performance numbers and scaling plans from Alluxio/DAX and BlobFuse teams for side-by-side comparison against OpenAI cache. @Myself 📅 2025-10-26 #task #proposed #auto

## Decisions

- Jason Vallery will lead an evaluation of OpenAI’s caching approach as a candidate for Microsoft MAI unified cache and compare it against BlobFuse, Alluxio/DAX, and AC Store.

- The preferred architecture direction for MAI is a single, pluggable cache that supports training first and is designed to extend to inference and KB caching.

- Near-term performance direction for Azure Blob is Bifrost (direct read path bypassing FE and table layers), with DeltaZero positioned as a follow-on.

- Jason Vallery will lead the evaluation of OpenAI’s caching code for potential use in MAI’s unified cache and compare it against BlobFuse, Alluxio/DAX, and AC Store.

- The preferred architecture direction is a single unified, framework-agnostic cache that can serve training first and later inference and KB caching.

- Near-term performance direction for Azure Blob is Bifrost (direct read path), with DeltaZero positioned as a follow-on.

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

- Jai Menon stated MAI’s target scale is approximately 400k GPUs for training and 40k GPUs for inference within two years, implying a cache that can scale to roughly 100k nodes.

- Jai Menon stated the MAI cache is expected to run on AKS plus Spark.

- Jai Menon expressed a design preference for a single unified cache that supports both training and inference, including KB caching, and is pluggable across frameworks.

- OpenAI caching code is being evaluated as a candidate implementation for MAI’s unified cache, but Microsoft legal and IP clearance and repository access must be confirmed (Pete and Sila are relevant contacts).

- Bifrost is positioned as the near-term performance path for Azure Blob by adding a direct read path that bypasses FE and table layers; DeltaZero is positioned as a follow-on.

- Lukasz is building parts of Bifrost related to the direct read path.

- Compute for AI moved to Brendan’s organization; Kiki (CVP) is leading AKS compute for MAI, with Yumin interfacing.

- A possible MAI requirement discussed was multi-region logical cache pooling, pending confirmation of latency and consistency expectations.

- Jason Vallery planned to meet with Ong on Friday to discuss snapshot feedback and MAI constraints, and then decide whether to escalate to Manish and Wamshi.
