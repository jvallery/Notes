---
type: "people"
title: "Jason Vallery 1:1 with Tomer Hagay, align on PM-led cloud model and cloud design qualifiers (multi-tenancy)"
date: "2025-10-29"
person: ""
participants: ["Jason Vallery", "Tomer Hagay", "Shahar", "Noah", "Eyal", "David (former VAST PM leader, now VP at Dell)", "Renan", "Jeff Denworth"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# Jason Vallery 1:1 with Tomer Hagay, align on PM-led cloud model and cloud design qualifiers (multi-tenancy)

**Date**: 2025-10-29
**With**: Jason Vallery, Tomer Hagay, Shahar, Noah, Eyal, David (former VAST PM leader, now VP at Dell), Renan, Jeff Denworth

## Summary

Jason Vallery and Tomer Hagay aligned that VAST's cloud work should shift toward a PM-led operating model, including clearer ownership for definitions, architecture alignment, and release planning. They discussed the current decision funnel (PM prioritization, architect/engineering-owned FRDs, and final decisions routed via Noah/Eyal to Shahar), the constraints of a very small PM team, and multi-tenancy gaps that could block cloud timelines. They agreed to schedule a Friday follow-up to cover cloud pricing and a Salesforce walkthrough.


## Action Items


- [?] Schedule a 1-hour Friday meeting to discuss the cloud pricing model and run a Salesforce demo/walkthrough. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Prepare and deliver a Salesforce walkthrough covering dashboards and feature/request tracking for the PM and engineering workflow. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft an initial cloud design qualifiers checklist for FRDs, including multi-tenancy, call-home/instrumentation, and GUI analytics requirements. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Compile current multi-tenancy gaps across features (for example, tenant-scoped data spaces, authentication, and replication consistency) to inform the cloud backlog and GA readiness requirements. @Tomer Hagay 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the VAST Data 5.5 release plan with Shahar to align and prioritize cloud-critical items, especially multi-tenancy requirements needed for cloud timelines. @Shahar 📅 2025-11-08 #task #proposed #auto

- [?] Arrange face time with Shahar in Tel Aviv to align on adopting a PM-led model for cloud work and to confirm cloud-oriented design qualifiers for new features. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Set up a sit-down with Jeff Denworth (and potentially Noah and Eyal) to clarify ownership boundaries and decision rights for cloud work versus core platform work. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Consolidate multi-tenancy issues raised by Leora and Iki into a succinct findings document to support backlog prioritization and cloud GA readiness planning. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Provide a list of customers using multi-tenancy and describe their operating models (self-managed vs admin-only) to inform product requirements and qualifiers. @Tomer Hagay 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm whether multi-tenancy will be mandated as a design qualifier for all new features going forward, versus being optional or customer-specific. @Tomer Hagay 📅 2025-11-08 #task #proposed #auto




## Decisions


- Schedule a Friday follow-up meeting to cover the cloud pricing model discussion and a Salesforce demo/walkthrough for feature and request tracking.




## Key Information


- At VAST Data, product decisions for major releases ultimately come from Shahar, with more predictability in recent years because Noah and Eyal now funnel content and make the case to Shahar.

- VAST Data's current operating model is that PMs prioritize, while architects and engineering drive detailed specifications and FRDs, and PMs typically co-author, comment on, or add user stories rather than owning FRD writing end-to-end.

- VAST Data has approximately 4 PMs supporting roughly 400 engineers, which limits the PM team's ability to go deep on detailed specifications across all areas.

- A prior attempt to run a classic PM-led model at VAST Data (led by a predecessor named David, now a VP at Dell) was ineffective due to founder-driven decision changes and frequent last-minute reversals.

- Tomer Hagay believes cloud is a new area of serious investment at VAST Data and represents an opportunity to implement a more standard PM-led model that reduces friction between PM and architecture/engineering.

- Jason Vallery is doing an onboarding tour to meet teams and learn VAST Data's development lifecycle and decision processes, including discussions with the xAI team about customer success operations.



---

*Source: [[2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee]]*