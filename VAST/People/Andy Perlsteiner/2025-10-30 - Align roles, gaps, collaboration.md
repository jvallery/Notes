---
type: "people"
title: "Align roles, gaps, collaboration"
date: "2025-10-30"
person: "Andy Perlsteiner"
participants: ["Andy Perlsteiner", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-30/2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four.md"
tags:
  - "type/people"
  - "person/andy-perlsteiner"
  - "generated"
---

# Align roles, gaps, collaboration

**Date**: 2025-10-30
**With**: Andy Perlsteiner, Jason Vallery

## Summary

Jason and Andy aligned on how to collaborate between PM and Andy’s Field CTO/Octo team, including major gaps in documentation, training, and release visibility (PRDs vs FRDs, late implementation reviews, limited access to builds/docs). Jason’s near-term focus is making VAST on Cloud sellable (Azure marketplace objects, CSP shapes, multi-tenancy toward SaaS, pricing/legal), while discussing skepticism on cloud economics and the OpenAI multi-region data lake + GPU-adjacent model where VAST could serve as a global data plane. They agreed Jason should get hands-on via OVA and SE Lab, obtain GitLab access, join phase gates/implementation reviews, and schedule a follow-up deep-dive on OpenAI architecture; Sync Engine lacks a PM and urgently needs Azure Blob read support for wave.ai migrations with an early-December customer timeline.
## Action Items
- [ ] Provide sales team update on Sync Engine Blob-source support status @Andy 📅 2025-10-30 🔺 #task
- [ ] Meet with Josh to obtain OVA and setup guidance @Myself 📅 2025-10-31 ⏫ #task

## Decisions
- Use Phil Wagstrom as primary multi-tenancy SME contact.
- Proceed with OVA and SE Lab access for Jason’s learning.
- Schedule a follow-up focused on OpenAI architecture and needs.

## Key Information
- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement (training)/PM augmentation, and marketing support.
- Current product docs are feature-by-feature and not scenario-driven; scenario guides are ad hoc and late.
- PM process gaps include unclear training ownership, engineering-authored FRDs instead of PM-authored PRDs, limited release visibility, and inconsistent access to builds/docs.
- Jason’s charter is to make VAST on Cloud sellable: partner with Yonce on marketplace objects, push CSPs (starting with Azure) for better instance shapes, drive multi-tenancy backlog toward SaaS, and align pricing/legal with Timo.
- Cloud economics are currently viewed as uncompetitive versus first-party capacity storage; value may be in higher-level compute + a global data plane.
- OpenAI pattern described: multi-exabyte data lakes in three Azure regions (CPU/Spark/Databricks) with GPUs in 50+ regions plus CoreWeave and Oracle; GPU-adjacent cache with checkpoints back to central.
- OVA is available but unsupported; requires ~128GB RAM host; client networking requires tunneling/proxies; single-VM multi-container demo only.
- SE Lab access is via VPN and octo.selab.fastdata.com with an AD account; multiple clusters exist with varying admin rights.
- GitLab access (get.vastdata.com) is restricted and requires an IT ticket for a licensed account.
- Release hygiene: phase gates and implementation reviews (run by Galit/Orly) plus Confluence release pages (e.g., 5.4 dev) and FRDs/recordings.
- Sync Engine has no formal PM; Andy and Blake are acting PMs.
- wave.ai has ~100PB in Azure Blob (Sweden) and plans to migrate ~50PB to CoreWeave while syncing checkpoints back to Azure; needs Sync Engine to read from Azure Blob.
- Aaron Zilber is investigating Blob APIs but is OOO for ~2.5 weeks; customer needs early December start for migration.

---

*Source: [[Inbox/_archive/2025-10-30/2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four.md|2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]]*

## Related

- [[Andy Perlsteiner]]
- [[Jason Vallery]]
- [[Jeff Denworth]]
- [[Ms. Ross]]
- [[Phil Wagstrom]]
- [[Ray Coetzee]]
- [[Timo Pervane]]
- [[Aaron Zilber]]
- [[John Mao]]
- [[Ronen Cohen]]
- [[Ryan McGinty]]
- [[Leo Stone]]
- [[Olivia Bouree]]
- [[OVA]]
- [[Cloud control plane]]
- [[5.5 Features]]
- [[OpenAI VAST POC (CoreWeave cluster)]]
- [[Microsoft]]
- [[Amazon]]
- [[Google]]
- [[Oracle]]
- [[Databricks]]
- [[CoreWeave]]
