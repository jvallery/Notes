---
type: "people"
title: "1:1 with Tomer Hagay: shift cloud work to PM-led model, add cloud design qualifiers, and assess multi-tenancy gaps"
date: "2025-10-29"
person: ""
participants: ["Jason Vallery", "Tomer Hagay", "Shahar", "Noah", "Eyal", "Renan", "Jeff Denworth", "LaRoz", "David"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Tomer Hagay: shift cloud work to PM-led model, add cloud design qualifiers, and assess multi-tenancy gaps

**Date**: 2025-10-29
**With**: Jason Vallery, Tomer Hagay, Shahar, Noah, Eyal, Renan, Jeff Denworth, LaRoz, David

## Summary

Jason Vallery and Tomer Hagay aligned that VAST's cloud work should move toward a PM-led operating model, including PM ownership of definitions, architecture alignment, and release planning. They discussed current decision flow (Noah and Eyal funneling decisions to Shahar), the constraints of a small PM team, and multi-tenancy gaps that could block cloud timelines. They agreed to schedule a Friday follow-up to cover cloud pricing and a Salesforce walkthrough.


## Action Items


- [?] Schedule a 1-hour Friday meeting to discuss VAST cloud pricing model and a Salesforce demo. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare and deliver a Salesforce walkthrough covering dashboards and feature or request tracking for cloud work. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft an initial cloud design qualifiers checklist for FRDs, including multi-tenancy, call-home instrumentation, and GUI analytics requirements. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Compile current multi-tenancy gaps across VAST features, including tenant-aware data spaces, authentication, and replication, to inform the cloud backlog. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the VAST 5.5 release plan with Shahar to align and prioritize cloud-critical items, especially multi-tenancy requirements. @Shahar 📅 2025-11-08 #task #proposed #auto

- [?] Arrange face time with Shahar in Tel Aviv to align on a PM-led model for cloud work and cloud-oriented requirements. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up a sit-down with Jeff Denworth (and potentially Noah and Eyal) to clarify ownership boundaries for cloud work versus core platform work. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Consolidate multi-tenancy issues raised by Leora and Iki into a succinct findings document for cloud planning. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Provide a list of customers using VAST multi-tenancy and document their operating models (self-managed vs admin-only). @Tomer Hagay 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm whether multi-tenancy will be mandated as a design qualifier for all new VAST features going forward, and document the policy decision. @Tomer Hagay 📅 2025-11-08 #task #proposed #auto




## Decisions


- Schedule a 1-hour Friday follow-up session to discuss VAST cloud pricing model and a Salesforce walkthrough for dashboards and feature or request tracking.

- Create an initial cloud design qualifiers checklist (including multi-tenancy, call-home instrumentation, and GUI analytics) to attach to FRDs for cloud-related work.




## Key Information


- VAST's current product decision flow is that PMs prioritize, architects and engineering drive detailed specs and FRDs, and final decisions are funneled via Noah and Eyal to Shahar for approval.

- VAST's PM organization is approximately 4 PMs supporting roughly 400 engineers, limiting PM ability to go deep on all feature specifications and FRDs.

- Tomer Hagay joined VAST expecting a classic industry PM model (PM owning definitions and interface with engineering), but adapted because founder-driven last-minute decision changes made that model ineffective.

- A prior VAST product leader named David (now a VP at Dell) attempted to build a classic PM organization at VAST, but decision meetings devolved into arguments with Shahar and the model did not stick.

- Tomer Hagay described VAST FRDs as often solution-oriented rather than problem-oriented, with PMs typically co-authoring, commenting, or adding user stories rather than owning full FRD authorship.

- Cloud is becoming a new serious investment area at VAST, creating an opportunity to establish a more standard PM-led operating model for cloud work.

- Multi-tenancy limitations were called out as a cloud risk, including data spaces configured at the cluster level rather than per-tenant, plus inconsistencies in authentication and replication behavior.

- VAST's 5.5 release plan was described as missing cloud-critical multi-tenancy items needed for cloud readiness.

- Multi-tenancy at VAST is currently delivered as feature or customer-driven MVPs rather than a strategic end-to-end initiative, creating gaps for cloud timelines and GA readiness.

- Customers using VAST multi-tenancy include CoreWeave and Lambda, with different operating models such as admin-only management versus self-managed tenant models.



---

*Source: [[2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee]]*