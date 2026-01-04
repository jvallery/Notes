---
type: people
title: PM-led cloud model alignment
date: '2025-10-29'
person: Tomer Hagay
participants:
- Jason Vallery
- Tomer Hagay
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-29 - Jason and Tomer aligned on shifting
  cloud work toward a PM-led model and the nee.md
tags:
- type/people
- person/tomer-hagay
- generated
---

# PM-led cloud model alignment

**Date**: 2025-10-29
**With**: Jason Vallery, Tomer Hagay

## Summary

Jason and Tomer aligned that cloud work should move to a PM-led model, with a checklist of cloud design qualifiers (including multi-tenancy) attached to FRDs to reduce solution-first bias and improve release planning. They discussed current decision flow via Noah/Eyal to Shahar, the constraints of a small PM team, and how multi-tenancy gaps (tenant-level configuration, auth, replication) could block cloud timelines. They agreed to schedule a Friday follow-up to cover pricing and a Salesforce walkthrough.
## Action Items
- [ ] Schedule a 1-hour Friday meeting to discuss pricing model and Salesforce demo @Tomer 📅 2025-11-08 ⏫ #task
- [ ] Prepare and deliver Salesforce walkthrough (dashboards, feature/request tracking) @Tomer 📅 2025-11-08 ⏫ #task
- [ ] Draft initial cloud design qualifiers checklist (multi-tenancy, call home/instrumentation, GUI analytics) for inclusion in FRDs @Myself 📅 2025-11-08 🔺 #task
- [ ] Compile current multi-tenancy gaps across features (e.g., data spaces per-tenant, auth, replication) to inform backlog @Tomer 📅 2025-11-08 🔺 #task
- [ ] Review 5.5 plan with Shahar to align and prioritize cloud-critical items @Shachar 📅 2025-11-08 ⏫ #task
- [ ] Arrange face time with Sahar in Tel Aviv to align on PM model and cloud requirements @Myself 📅 2025-11-08 🔺 #task
- [ ] Set up a sit-down with Jeff (and potentially Noah/Eyal) to clarify ownership boundaries for cloud vs core @Myself 📅 2025-11-08 🔺 #task
- [ ] Consolidate multi-tenancy issues raised by Leora and Iki into a succinct findings doc @Myself 📅 2025-11-08 ⏫ #task
- [ ] Provide a list of customers using multi-tenancy and their models (self-managed vs admin-only) @Tomer 📅 2025-11-08 🔽 #task
- [ ] Confirm whether multi-tenancy will be mandated as a qualifier for all new features going forward @Tomer 📅 2025-11-08 ⏫ #task

## Decisions
- Schedule a follow-up on Friday to cover pricing and a Salesforce demo.

## Key Information
- Current decision flow: PM prioritizes; architects/engineering drive specs/FRDs; decisions funneled via Noah/Eyal to Shahar.
- PM team scale is small (~4 PMs supporting ~400 engineers), limiting depth across all features.
- Past attempts at a classic PM model were disrupted by founder-driven last-minute decision changes.
- Cloud is becoming a serious investment area and an opportunity to establish a more standard PM-led model.
- Multi-tenancy gaps include tenant-level configuration limitations (e.g., data spaces set at cluster level), plus authentication and replication inconsistencies.
- The 5.5 plan does not currently include cloud-critical multi-tenancy items.
- Multi-tenancy work has been driven by customer MVP needs rather than a strategic end-to-end initiative.
- Customers using multi-tenancy include CoreWeave, Lambda, and Caruso, with differing models (admin-only vs self-managed).

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee.md|2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee]]*

## Related

- [[Jason Vallery]]
- [[Tomer Hagay]]
- [[Jeff Denworth]]
- [[5.5 Features]]
- [[Cloud control plane]]
- [[CoreWeave]]
- [[Lambda]]
- [[Microsoft]]
