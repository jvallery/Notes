---
type: people
title: Release planning and SaaS gaps
date: '2025-10-29'
person: Eyal Traitel
participants:
- Jason Vallery
- Eyal Traitel
source: transcript
tags:
- type/people
- person/eyal-traitel
- generated
---

# Release planning and SaaS gaps

**Date**: 2025-10-29
**With**: Jason Vallery, Eyal Traitel

## Summary

Jason and Eyal reviewed VAST’s release intake and planning model (majors, minors, service packs, and hotfixes) and how field requests and urgent customer asks can disrupt planned scope. They aligned that minor releases are treated as full releases with rigorous regression/performance testing, and discussed key cluster-side multi-tenancy gaps (notably authentication provider limits) that block SaaS agility. Eyal committed to share the current multi-tenancy gaps Confluence page, and they planned a follow-up call plus an in-person meeting during Jason’s Tel Aviv visit.
## Action Items
- [?] Send the Confluence page with the current multi-tenancy gaps list @Eyal 📅 2025-11-08 ⏫ #task #proposed
- [?] Schedule a follow-up call to continue SaaS and release process discussion @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Coordinate an in-person meeting during the Tel Aviv visit (2025-11-23 to 2025-11-26) @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Review the multi-tenancy gaps list and identify priorities for cloud/SaaS readiness @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Sync with the Polaris/Icelandic team on which gaps can be addressed in control plane vs cluster @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Confirm the backport/forward-port plan when delivering features to customers on hotfix builds @Eyal 📅 2025-11-08 🔽 #task #proposed

## Key Information
- Eyal joined VAST in 2024-12; Noa is an early employee and manages major releases while Eyal plans minor releases.
- Release intake sources include leadership-driven initiatives (e.g., S3 RDMA), architects (Asaf, Sagi), and SE requests filed in Salesforce tied to opportunities.
- Field requests are triaged by Tomer Haggai’s team; Jonathan Hayes was assigned to review requests; bi-weekly reviews cover top items.
- Phase-gate and release operations are driven by Shelly Martin and Liraz (R&D).
- Urgent customer asks (example: Tesla) frequently reallocate teams and shift release scope.
- Service packs/hotfixes are driven by vForce (Roy Sterman) and Dafna’s team, with emphasis on ensuring fixes are backported/forward-ported into regular builds.
- Minor releases are treated as full releases with extensive regression and performance testing and weekly content/testing reviews; hotfixes/service packs typically undergo less regression.
- VAST is not yet full SaaS; Polaris/Icelandic team owns the control plane; significant cluster-side multi-tenancy gaps remain.
- Key multi-tenancy blocker: authentication providers are limited to 8 and configured at the cluster level rather than per-tenant; scaling and tenantizing is a large effort.
- Release cadence discussed: 5.4 released, 5.5 upcoming; 5.6 targeted for GA in July next year; roughly ~2–2.5 major releases per year recently.
- Jason will be in Tel Aviv from 2025-11-23 to 2025-11-26.

---

*Source: [[Inbox/_archive/2025-10-29/original.md|original]]*

## Related

- [[Eyal Traitel]]
- [[Jason Vallery]]
- [[5.5 Features]]
- [[Tesla]]
- [[Microsoft]]