---
type: customer
title: UK Met dual-track Azure plan
date: '2025-10-27'
account: Microsoft
participants:
- Jason Vallery
- Lior Genzel
- Jonsi Stephenson
- Rony
- Ronen Cohen
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-27 - Team aligned on making UK Met Office
  successful with dual paths Plan A on Azure.md
tags:
- type/customer
- account/microsoft
- generated
---

# UK Met dual-track Azure plan

**Date**: 2025-10-27
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Lior Genzel, Jonsi Stephenson, Rony, Ronen Cohen

## Summary

Team aligned on a dual-track approach to win UK Met Office: Plan A is VAST on new Azure Compute (targeting an 800 Gb network / 300 TB local SSD VM) and Plan B is VAST on Specialized/ODM hardware to de-risk Microsoft timeline risk. UK Met has verbally selected VAST pending software/performance validation and expects Microsoft spec confirmation mid-November, with Azure testing access targeted for the first week of December. Product/GTM needs clear GA/MVP acceptance criteria (spin up/down, DR/offload) plus competitive performance/TCO comparisons versus Managed Lustre, Weka, and Hammerspace.
## Action Items
- [ ] Communicate first-week-of-December Azure testing availability to UK Met Office. @Lior Genzel 📅 2025-12-01 🔺 #task #proposed

## Decisions
- Pursue UK Met Office Plan A (Azure Compute) and Plan B (Specialized/ODM) concurrently.
- Defer aggressive field marketing until MVP/GA criteria are defined, while advancing a few lighthouse projects per cloud.

## Key Information
- UK Met expects an Azure VM with 800 Gb networking and ~300 TB local SSD; they currently test on 200 Gb VMs and plan to extrapolate performance linearly.
- Microsoft Compute timeline discussed: testing hardware expected in Q1 (next calendar year) and production in Q2 (next calendar year); final spec confirmation expected mid-November from Igal’s group.
- UK Met has verbally selected VAST pending software/performance validation; they need something to test by early December.
- UK Met has tested Weka and Hammerspace on Azure LSV4 due to lack of VAST software access.
- Managed Lustre is reportedly ~20% cheaper list, but UK Met is believed to prefer not to return to Lustre.
- GA gating capabilities discussed include: spin up/down clusters, DR/offload to object storage, and a credible SaaS roadmap.
- GCP cloud offering performance bottleneck was removed; GA expected soon with lighthouse customers.
- Two Sigma meeting is set for 2025-11-12 to discuss a Google POC; ICE/NYSE AWS POC was technically successful but cloud adoption was deferred due to maturity concerns.
- Zoom is exploring an OCI-based training stack; decision depends on apples-to-apples VM comparison and TCO viability.

---

*Source: [[Inbox/Transcripts/2025-10-27 - Team aligned on making UK Met Office successful with dual paths Plan A on Azure.md|2025-10-27 - Team aligned on making UK Met Office successful with dual paths Plan A on Azure]]*

## Related

- [[Lior Genzel]]
- [[Jonsi Stephenson]]
- [[Ronen Cohen]]
- [[Jason Vallery]]
- [[Jeff Denworth]]
- [[5.5 Features]]
- [[Google]]
- [[Amazon]]
- [[Oracle]]