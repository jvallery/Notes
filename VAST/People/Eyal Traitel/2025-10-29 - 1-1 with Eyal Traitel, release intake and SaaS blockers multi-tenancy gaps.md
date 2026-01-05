---
type: "people"
title: "1:1 with Eyal Traitel, release intake and SaaS blockers (multi-tenancy gaps)"
date: "2025-10-29"
person: ""
participants: ["Jason Vallery", "Eyal Traitel"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Eyal Traitel, release intake and SaaS blockers (multi-tenancy gaps)

**Date**: 2025-10-29
**With**: Jason Vallery, Eyal Traitel

## Summary

Jason Vallery and Eyal Traitel aligned on how VAST Data intake flows into major and minor releases, how phase gates and release operations work, and how urgent customer requests disrupt planned scope. They also aligned that cluster-side multi-tenancy gaps, especially authentication provider scaling and tenant-level configuration, are key blockers to SaaS agility; Eyal will share the current multi-tenancy gap list and they will sync again and meet during Jason’s Tel Aviv visit (2025-11-23 to 2025-11-26).


## Action Items


- [?] Send the Confluence page containing the current list of VAST Data cluster multi-tenancy gaps (SaaS readiness blockers) to Jason Vallery. @Eyal Traitel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up call with Eyal Traitel to continue discussion on VAST Data SaaS agility and the release process model. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate an in-person meeting with Eyal Traitel during Jason Vallery’s Tel Aviv visit (2025-11-23 to 2025-11-26). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Review the multi-tenancy gaps list and identify which items are highest priority for VAST Data cloud and SaaS readiness. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Sync with the Polaris (Icelandic) control plane team to determine which SaaS and multi-tenancy gaps can be addressed in the control plane versus requiring cluster-side changes. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the backport and forward-port process for fixes and features delivered to customers on hotfix builds to reduce quality and divergence risk. @Eyal Traitel 📅 2025-11-08 🔽 #task #proposed #auto






## Key Information


- Eyal Traitel joined VAST Data in December 2024 and works in release planning.

- At VAST Data, Noa (veteran employee, approximately employee 19) manages major releases while Eyal Traitel plans minor releases.

- VAST Data release intake comes from leadership-driven priorities (example: S3 RDMA), from architects (example: Asaf and Sagi), and from Sales Engineering requests filed in Salesforce and tied to opportunities.

- Field feature requests are triaged by Tomer Hagay’s team; Jonathan Hayes was assigned to review requests, and they run bi-weekly reviews of the top requests.

- VAST Data phase-gate and release operations are driven by Shelly Martin and Liraz (R&D), with documented commitments at phase gates that often change by final release due to deferrals and new urgent requests.

- Urgent customer requests, including from Tesla, can require multiple weeks of development plus QA and frequently reallocate teams away from planned work, changing release scope.

- VAST Data uses dedicated release manager roles (separate from Eyal Traitel and Noa) to run day-to-day execution for major releases and for minor releases.

- For minor releases, VAST Data sometimes ships large customer-driven builds labeled as hotfixes that include features (not only bug fixes) when minor release timing is not fast enough.



---

*Source: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]]*