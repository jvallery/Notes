---
type: people
title: 'UK Met Office dual-track plan: Azure 800 Gb/300 TB VM (Plan A) plus Specialized/ODM fallback (Plan B)'
date: '2025-10-27'
participants:
- Jason Vallery
- Lior Genzel
- Jonsi Stephenson
- TBD
- TBD
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-27 - Team aligned on making UK Met Office successful with dual paths Plan A on Azure.md
tags:
- type/people
- generated
person: Lior Genzel
---

# UK Met Office dual-track plan: Azure 800 Gb/300 TB VM (Plan A) plus Specialized/ODM fallback (Plan B)

**Date**: 2025-10-27
**Attendees**: Jason Vallery, Lior Genzel, Jonsi Stephenson, TBD, TBD

## Summary

Internal team aligned to win UK Met Office by running two paths in parallel: Plan A is VAST on a new Azure compute VM spec (target 800 Gb networking and 300 TB local SSD), and Plan B is VAST on Specialized/ODM hardware to de-risk Microsoft compute timelines. UK Met Office has verbally selected VAST pending software access and performance validation, expects a Microsoft compute answer by mid-November 2025, and wants Azure testing access in the first week of December 2025.

## Action Items

- [?] Follow up with Anand and the VAST Data Specialized team to accept and provision VAST ODM hardware access for UK Met Office as Plan B. @Lior Genzel 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Start and maintain an email thread with Igal Figlin's Microsoft group to confirm the 800 Gb networking and 300 TB local SSD VM specification (including whether it is QLC-based) and the testing/production availability timeline. @Lior Genzel 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Validate whether Hibernate-to-object is required before full object offload for early cloud customers, and decide prioritization with the relevant engineering/product stakeholders (including Yogev if needed). @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

## Decisions

- Run UK Met Office pursuit as a dual-track execution: Plan A is VAST Data on Azure compute (targeting the 800 Gb networking and 300 TB local SSD VM), and Plan B is VAST Data on Specialized/ODM hardware to de-risk Microsoft compute schedule and spec uncertainty.

- Avoid setting performance expectations based on current Azure LSv4 testing that could mislead UK Met Office, because UK Met Office will extrapolate results to the 800 Gb networking target VM.

## Key Information

- UK Met Office requested an Azure compute VM with 800 Gb networking and 300 TB local SSD, and is currently testing on 200 Gb VMs while extrapolating performance linearly to the 800 Gb target.

- UK Met Office expects a final confirmation from Igal Figlin's Microsoft group by mid-November 2025 on the 800 Gb networking and 300 TB local SSD VM specification and availability.

- Microsoft compute indicated the committed server for the new VM is expected for testing in Q1 2026 and production readiness in Q2 2026.

- A possible new Azure VM variant under discussion may use QLC drives, and the team suspects the 300 TB local SSD configuration could be QLC-based, requiring validation with Microsoft product contacts.

- UK Met Office stakeholders (Mike and Niko, Microsoft-side) stated multiple times that UK Met Office has verbally selected VAST Data, contingent on software availability and performance validation.

- There is a recurring gap between what the UK Met Office Microsoft account team communicates and what Igal Figlin communicates, even though Igal Figlin stated he is in full sync with the UK Met Office team.

- Jason Vallery noted that an unnamed Microsoft contact's role is changing from a storage PM team stream to reporting directly to Mike, with a mandate to focus 100% on UK Met Office.

- The internal VAST Data plan is to ensure UK Met Office Plan A is VAST on Azure compute and Plan B is VAST on Specialized/ODM hardware, rather than allowing a competitor to become the fallback option.

---

*Source: [[2025-10-27 - Team aligned on making UK Met Office successful with dual paths Plan A on Azure]]*