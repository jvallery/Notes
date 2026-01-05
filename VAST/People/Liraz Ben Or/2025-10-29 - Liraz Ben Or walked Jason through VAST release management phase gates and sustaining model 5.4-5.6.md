---
type: people
title: Liraz Ben Or walked Jason through VAST release management phase gates and sustaining model (5.4-5.6)
date: '2025-10-29'
person: Liraz Ben Or
participants:
- Jason Vallery
- Liraz Ben Or
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga.md
tags:
- type/people
- generated
---

# Liraz Ben Or walked Jason through VAST release management phase gates and sustaining model (5.4-5.6)

**Date**: 2025-10-29
**With**: Jason Vallery, Liraz Ben Or

## Summary

Liraz Ben Or explained VAST Data's non-traditional major release management using four phase gates (scope, plan/change management, code freeze/beta readiness, release) with overlapping planning and execution across major versions. The discussion covered sustaining support via a separate vForce team for older majors, QA cycle targets, decision-making roles across product, architects, and development leadership, and the need to bring cloud-driven work into the same governed phase-gate and QA process.

## Action Items

- [?] Review VAST Data 5.4 phase-gate decks and materials shared by Liraz Ben Or. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Send VAST Data 5.5 status wiki and Excel Gantt link(s) to Jason Vallery. @Liraz Ben Or 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review VAST Data 5.5 status wiki and Excel Gantt to understand current execution status and upcoming feature freeze. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up 1:1 with Liraz Ben Or next week to go deeper on VAST Data release process details (phase gates, roles, tooling, and governance). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate with Asaf Levy on thematic and architectural planning approach for VAST Data releases, including how priorities are shaped beyond single-customer asks. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Plan and schedule an in-person sync with Liraz Ben Or in Tel Aviv during Jason Vallery's trip (2025-11-23 to 2025-11-26). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Share the current VAST Data 5.5 anchor features and the beta customers enlisted for those anchor features. @Liraz Ben Or 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Ensure cloud-driven features follow VAST Data phase gates and are included in release QA plans (avoid ad hoc cloud releases outside governance). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the exact calendar date planned for VAST Data 5.6 Phase Gate 1. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Obtain access to VAST Data per-release wiki pages, QTest views/dashboards, and the weekly release status deck materials. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Connect with the release managers for VAST Data 5.5 and 5.6 (referenced as Orly and Roy) to establish working rhythms and clarify planning vs execution ownership. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Clarify VAST Data official support policy for older major versions (target 'major minus two') and document any exceptions (for example, 5.1 hotfix-only). @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Review the VAST Data 5.4 phase-gate decks and materials shared by Liraz Ben Or. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Send the VAST Data 5.5 status wiki link(s) and Excel Gantt link(s) to Jason Vallery. @Liraz Ben Or 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the VAST Data 5.5 status wiki and Excel Gantt to understand current execution status and upcoming feature freeze readiness. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up 1:1 with Liraz Ben Or for a deeper dive on the VAST Data release process. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate with Asaf Levy on how VAST Data does thematic and architectural planning and how priorities are shaped beyond single-customer feature asks. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Plan and schedule an in-person sync with Liraz Ben Or in Tel Aviv during 2025-11-23 to 2025-11-26. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Ensure cloud-driven features and cloud components follow the VAST Data phase-gate process and are included in the release QA plans rather than being released ad hoc. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Obtain access to VAST Data per-release wiki pages, QTest dashboards/views, and the weekly release status deck used for internal status reviews. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Connect with the release managers for VAST Data 5.5 and 5.6 (examples mentioned: Orly and Roy) to establish working rhythms and clarify planning vs execution ownership. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Clarify the official VAST Data support policy for older major versions (target major minus two) and document any exceptions (for example, continued 5.1 hotfix support). @Myself 📅 2025-11-08 🔽 #task #proposed #auto

## Key Information

- Liraz Ben Or has worked at VAST Data for almost six years (six years in March 2026) and leads program management for major releases with a team of three.

- VAST Data major releases use four phase gates: PG1 scope review, PG2 plan/timeline and change management, PG3 code freeze and beta readiness, PG4 release.

- VAST Data QA runs three cycles for a release: Phase 1 runs all tests, Phase 2 reruns failed tests only, and a Golden Run reruns all tests, targeting 96-97% success.

- VAST Data release cadence is roughly every five months, and planning for the next major overlaps with code freeze of the current major.

- VAST Data released version 5.4 in the week prior to 2025-10-29; 5.5 is in execution toward feature freeze; 5.6 Phase Gate 1 was expected in approximately two weeks from 2025-10-29.

- VAST Data uses a sustaining organization called vForce to handle minors and hotfixes for older major versions; the intent is to maintain 'major minus two' but customers still run 5.1 in the field, which receives hotfixes only.

- Unplanned VAST Data 5.2 minor releases were shipped to fix upgrade issues; the current migration focus is moving customers to 5.3 because 5.4 was described as not yet stable enough for broad push.

- VAST Data splits release management responsibilities so release managers focus on planning while Liraz Ben Or's team focuses on execution; release managers for 5.5 and 5.6 were referenced as Orly and Roy.

- Decision roles for VAST Data releases were described as: product management (example: Tomer Hagay) sources customer needs, architects (example: Asaf Levy's team) design, and development leadership (example: Shachar, last name not provided) makes trade-off calls with product.

- VAST Data release tracking tools include per-release wiki status pages, Excel Gantt plans, and QTest for QA, plus weekly internal status reviews using slides.

- Anchor features for a VAST Data major release are used to recruit beta customers, and change management at phase gates can push features to later releases.

- Liraz Ben Or stated cloud components should be integrated into the same phase-gate and QA process as core releases, rather than being released ad hoc outside governance.

---

- Liraz Ben Or has worked at VAST Data for almost six years and is Head of Program Management, responsible for major releases and the phase-gate release meetings.

- VAST Data major releases use four phase gates: PG1 scope review, PG2 plan and timeline plus change management, PG3 code freeze and beta readiness, and PG4 release.

- VAST Data QA for a major release runs three cycles: Phase 1 runs all tests, Phase 2 reruns failed tests only, and a Golden Run reruns all tests, targeting 96-97% success.

- VAST Data release cadence is roughly every five months, and planning for the next major overlaps with code freeze of the current major release.

- VAST Data released version 5.4 in the week prior to 2025-10-29; version 5.5 is in execution toward feature freeze; version 5.6 Phase Gate 1 was expected approximately two weeks after 2025-10-29.

- VAST Data maintains older versions via a sustaining development organization called vForce, which handles minors and hotfixes for versions still in the field after a major release ships.

- VAST Data aims to support major minus two, but customers still run 5.1 in the field; 5.1 receives hotfixes only, not planned minors.

- VAST Data shipped unplanned 5.2 minor releases to address upgrade failures; the current migration focus is moving customers to 5.3 because 5.4 was not yet stable enough at the time of the meeting.

- VAST Data split development into two groups: a major-release development organization focused on future major releases and a separate sustaining vForce group for older versions; developers may rotate between the groups, and sustaining work is high-stress due to escalations and off-hours calls.

- VAST Data uses per-release wiki status pages, Excel Gantt plans, and QTest for QA tracking, plus weekly internal status reviews using slides.

- Release management at VAST Data is split so that release managers typically handle planning while Liraz Ben Or's program management team focuses on execution for the major release.

- Product management (example: Tomer Hagay) sources customer needs and desired features for upcoming releases; architects (example: Asaf Levy's team) design; development leadership (example: Shachar, last name not provided) makes trade-off calls jointly with product.

- VAST Data seeks beta customers for anchor features, and change management during phase gates can push features to later releases if commitments cannot be met.

- Cloud components at VAST Data should be integrated into the same phase-gate and QA process as core releases rather than being released ad hoc outside the gated process.
