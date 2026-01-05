---
type: people
title: 1:1 with Eyal Traitel, release intake and SaaS multi-tenancy blockers
date: '2025-10-29'
person: Eyal Traitel
participants:
- Jason Vallery
- Eyal Traitel
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i.md
tags:
- type/people
- generated
---

# 1:1 with Eyal Traitel, release intake and SaaS multi-tenancy blockers

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

- [?] Send the Confluence page containing the current VAST Data cluster multi-tenancy gaps list for SaaS readiness review. @Eyal Traitel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up call with Eyal Traitel to continue discussion on SaaS transition and the release process model. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate an in-person meeting with Eyal Traitel during Jason Vallery's Tel Aviv visit (2025-11-23 to 2025-11-26). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Review the multi-tenancy gaps list and identify priorities required for VAST Data cloud and SaaS readiness (durability, security, availability, and agility). @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Sync with the Polaris/Icelandic control plane team to determine which SaaS and multi-tenancy gaps can be addressed in the control plane versus requiring cluster-side changes. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the backport and forward-port plan for delivering customer features and fixes when customers are running hotfix builds, to reduce divergence risk across release streams. @Eyal Traitel 📅 2025-11-08 🔽 #task #proposed #auto

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

- Noa (last name not stated) is a long-tenured VAST Data employee (approximately employee 19) and manages major releases, while Eyal Traitel plans minor releases.

- VAST Data release intake sources include leadership-driven priorities (example: S3 RDMA), architect inputs (Asaf and his team, and Sagi), and field/SE requests submitted in Salesforce and tied to opportunities.

- Field request triage is handled by Tomer Hagay's team; Jonathan Hayes was assigned to review incoming Salesforce requests, with bi-weekly meetings to review top requests.

- Release phase-gate and release operations are driven by Shelly Martin and Liraz (R&D), and release scope changes frequently due to urgent customer requests (example: Tesla).

- VAST Data uses separate release manager roles for major releases and minor releases; Eyal Traitel collaborates closely with the minor release manager to track minor releases and large hotfixes.

- Service packs and hotfixes are driven primarily by vForce (including Roy Sterman) and Dafna's team, with an emphasis on backporting and forward-porting fixes.

- Minor releases at VAST Data are treated as full releases with extensive regression and performance testing, including weekly content and testing reviews.

- VAST Data is not yet operating as full SaaS; the Polaris/Icelandic team owns the control plane, and significant cluster-side multi-tenancy gaps remain.

- A key cluster-side multi-tenancy blocker is that authentication providers are limited to 8 and configured at the cluster level rather than per tenant, requiring significant work to scale and tenantize.

- VAST Data release cadence discussed: version 5.4 released, 5.5 upcoming, and 5.6 targeted for GA in July 2026, with roughly 2 to 2.5 major releases per year recently.

- Jason Vallery planned travel to Tel Aviv from 2025-11-23 to 2025-11-26 to meet in person.
