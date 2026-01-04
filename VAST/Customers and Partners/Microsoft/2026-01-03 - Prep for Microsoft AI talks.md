---
type: customer
title: Prep for Microsoft AI talks
date: '2026-01-03'
account: Microsoft
participants:
- Jonsi Stephenson
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2026-01-03 - Prep for Microsoft AI talks.md
tags:
- type/customer
- account/microsoft
- generated
---

# Prep for Microsoft AI talks

**Date**: 2026-01-03
**Account**: [[Microsoft]]
**Attendees**: Jonsi Stephenson, Jason Vallery

## Summary

Jonsi and Jason aligned on a “better together” positioning with Microsoft: Azure Blob as the central exabyte-scale data lake and VAST as GPU-adjacent high-performance file storage deeply integrated with Blob. They reviewed Microsoft AI (MAI) political dynamics around Manish’s Bifrost effort, concerns triggered by an internal comparison slide, and MAI timeline slippage with a likely bake-off between VAST and Azure’s Bifrost/Blob approach.
## Action Items
- [ ] Send Jonsi the slide deck/comparison materials (including the power/footprint/throughput slide) before his meeting with Ong and Manish. @Myself ⏫ #task
- [ ] Text Jason after the meeting with Ong and Manish and schedule a follow-up call to debrief and formulate the go-forward strategy. @Jonsi #task

## Decisions
- Position the partnership narrative as Azure Blob for central data lakes and VAST for GPU-adjacent storage, enabled by deep integration with Blob (avoid expanding into higher-level database/event-broker topics in the Microsoft conversation).
- Proceed with drafting/starting the deep Azure Blob integration project rather than waiting for a Microsoft PO, to demonstrate commitment and be ready for MAI/OpenAI needs.

## Key Information
- Microsoft AI (MAI) has an existing production VAST cluster via CoreWeave and prior familiarity with VAST.
- Key MAI stakeholder identified: Kushal Datta, who owns the relationship between Microsoft AI and Azure.
- Microsoft AI escalation was triggered after the Inflection acquisition and Azure supercomputer issues; Mustafa Suleyman escalated problems, driving internal initiatives.
- Manish is running a project called Bifrost with ~30+ developers to address Azure stack issues and is pitching it to MAI.
- An internal comparison slide (Azure Gen10.3 vs VAST ODM) claims ~4.3x power reduction, ~7x footprint reduction, and ~1.5x more throughput for VAST; it upset Manish and leadership.
- MAI timeline has slipped: decision likely around March and go-live likely May; MAI wants a January POC that is viewed as political/bake-off oriented.
- Supply-chain risk noted: flash/QLC constraints worsening as manufacturers repurpose capacity to HBM/DRAM; Microsoft is constrained due to just-in-time purchasing; HDD supply may improve but lead times remain long.
- Deal sizing context discussed: VAST plan assumed ~1.8–1.9 data reduction ratio (~900PB effective) vs Blob deploying ~1.6EB raw without data reduction.
- Mustafa Suleyman’s decision is expected to be decisive for MAI outcomes; Satya Nadella may mediate between Scott Guthrie and Mustafa.
- OpenAI runs massive Databricks/Spark pipelines and has moved some workloads off Azure due to CPU capacity constraints, reinforcing a split between data-lake CPU regions and disaggregated GPU fleets.
- Temporary restraining order against Jonsi was lifted; remaining legal focus is on solicitation and Jonsi believes his contract has no consequence.

---

*Source: [[Inbox/_archive/2026-01-03/2026-01-03 - Prep for Microsoft AI talks.md|2026-01-03 - Prep for Microsoft AI talks]]*

## Related

- [[OpenAI]]
- [[CoreWeave]]
- [[Databricks]]
- [[Jonsi Stephenson]]
- [[Jason Vallery]]
- [[Maneesh Sah]]
- [[Kushal Datta]]
- [[Mustafa Suleyman]]
- [[Satya Nadella]]
- [[Scott Guthrie]]
- [[Jeff Denworth]]
- [[Shachar Feinblit]]
- [[Alon Horev]]
- Ong
- Manish
