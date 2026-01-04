---
type: "people"
title: "Release process walkthrough with Liraz"
date: "2025-10-29"
person: "Liraz Ben Or"
participants: ["Liraz Ben Or", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-29/2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga.md"
tags:
  - "type/people"
  - "person/liraz-ben-or"
  - "generated"
---

# Release process walkthrough with Liraz

**Date**: 2025-10-29
**With**: Liraz Ben Or, Jason Vallery

## Summary

Liraz walked Jason through VAST’s non-traditional major release management using four phase gates (scope, plan/change management, code freeze/beta readiness, release) in a Waterfall model with overlapping planning/execution across releases. They covered decision roles (product, architects, dev leadership), QA’s three-cycle approach and success targets, and the tooling/rhythms used (per-release wiki pages, Excel Gantt, QTest, weekly status decks). They also aligned on sharing 5.4/5.5 materials, scheduling a deeper follow-up, and meeting in person during Jason’s late-November Tel Aviv visit.
## Action Items
- [ ] Review 5.4 phase-gate decks/materials shared by Liraz @Myself 📅 2025-11-08 ⏫ #task
- [ ] Send 5.5 status wiki and Gantt link(s) to Jason @Liraz 📅 2025-11-08 ⏫ #task
- [ ] Review 5.5 status wiki and Gantt @Myself 📅 2025-11-08 ⏫ #task
- [ ] Schedule a follow-up 1:1 next week to go deeper on the release process @Myself 📅 2025-11-08 ⏫ #task
- [ ] Coordinate with Asaf on thematic/architectural planning approach and how priorities are shaped beyond single-customer asks @Myself 📅 2025-11-08 ⏫ #task
- [ ] Plan and schedule an in-person sync in Tel Aviv during 2025-11-23 to 2025-11-26 @Myself 📅 2025-11-08 ⏫ #task
- [ ] Share current 5.5 anchor features and beta customers enlisted @Liraz 📅 2025-11-08 🔽 #task
- [ ] Ensure cloud-driven features follow phase gates and are included in QA plans @Myself 📅 2025-11-08 ⏫ #task
- [ ] Confirm the exact calendar date for 5.6 Phase Gate 1 @Myself 📅 2025-11-08 ⏫ #task
- [ ] Obtain access to the per-release wiki pages, QTest views, and the weekly status deck @Myself 📅 2025-11-08 ⏫ #task
- [ ] Connect with the current release managers for 5.5 and 5.6 (e.g., Orly and Roy) for working rhythms @Myself 📅 2025-11-08 🔽 #task
- [ ] Clarify official support policy for older majors (major minus two) and exceptions @Myself 📅 2025-11-08 🔽 #task

## Key Information
- VAST major releases use four phase gates: PG1 scope review; PG2 plan/timeline and change management; PG3 code freeze and beta readiness; PG4 release.
- QA runs three cycles (Phase 1 all tests, Phase 2 failed tests only, Golden Run all tests) targeting ~96–97% success.
- Release cadence is roughly every ~5 months; planning for the next major overlaps with code freeze/late stages of the current major.
- As of the meeting: 5.4 released the prior week; 5.5 in execution toward feature freeze; 5.6 PG1 expected in ~2 weeks (exact date TBD).
- A sustaining “vForce” team handles minors/hotfixes for older majors; goal is major-minus-two support, with 5.1 receiving hotfixes only.
- Unplanned 5.2 minors are shipping to address upgrade issues; current push is to move customers to 5.3 due to 5.4 stability concerns.
- Decision-making: product (e.g., Tomer) sources customer needs; architects (Asaf’s team) design; dev leadership (Shachar) makes trade-off calls with product.
- Release managers work in parallel to split planning vs execution across majors (e.g., Orly and Roy).
- Tooling includes per-release wiki status pages, Excel Gantt plans, QTest for QA tracking, and weekly internal status reviews with slides.
- Anchor features seek beta customers and early drops; change management can push features to later releases.
- Cloud components should be governed by the same phase-gate and QA process rather than released ad hoc.
- Tesla was cited as a large deal driving prioritization and milestone delivery within 5.4/related work.

---

*Source: [[Inbox/_archive/2025-10-29/2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga.md|2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga]]*

## Related

- [[Liraz Ben Or]]
- [[Jason Vallery]]
- [[Noa Cohen]]
- [[5.5 Features]]
- [[Tesla]]
- [[Microsoft]]
- [[Google]]
