---
type: people
title: 'Prep with Jonsi Stephenson for Microsoft AI (MAI) talks: positioning, Bifrost politics, and MAI timeline risk'
date: '2026-01-03'
person: Jonsi Stefansson
participants:
- Jonsi Stephenson
- Jason Vallery
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2026-01-03 - Prep for Microsoft AI talks.md
tags:
- type/people
- generated
---

# Prep with Jonsi Stephenson for Microsoft AI (MAI) talks: positioning, Bifrost politics, and MAI timeline risk

**Date**: 2026-01-03
**With**: Jonsi Stephenson, Jason Vallery

## Summary

Jason Vallery and Jonsi Stephenson aligned on a Microsoft “better together” narrative: Azure Blob as the central exabyte-scale data lake and VAST as GPU-adjacent high-performance file storage with deep Blob integration. They reviewed MAI political dynamics around Maneesh Sah’s Bifrost effort, fallout from an internal Azure vs VAST comparison slide, MAI timeline slippage (decision likely March 2026, go-live likely May 2026), and supply-chain risk (flash/QLC constraints).

## Action Items

- [?] Send Jonsi Stephenson the slide deck and comparison materials (including the power, footprint, and throughput comparison slide) before Jonsi Stephenson’s meeting with Ong and Maneesh Sah. @Myself 📅 2026-01-03 ⏫ #task #proposed #auto

- [?] After the meeting with Ong and Maneesh Sah, text Jason Vallery and schedule a follow-up call to debrief and formulate the go-forward strategy for Microsoft MAI engagement. @Jonsi Stephenson 📅 2026-01-03 #task #proposed #auto

- [?] Send Jonsi Stephenson the slide deck and comparison materials, including the power, footprint, and throughput comparison slide, before Jonsi Stephenson's meeting with Ong (unknown identity) and Maneesh Sah. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] After the meeting with Ong (unknown identity) and Maneesh Sah, text Jason Vallery and schedule a follow-up call to debrief and formulate the go-forward strategy for Microsoft MAI engagement. @Jonsi Stephenson 📅 TBD #task #proposed #auto

## Decisions

- Position the Microsoft partnership narrative as Azure Blob for central data lakes and VAST Data for GPU-adjacent storage, enabled by deep integration with Azure Blob, and avoid expanding into higher-level database or event-broker topics in Microsoft conversations.

- Proceed with drafting and starting the deep Azure Blob integration project rather than waiting for a Microsoft purchase order, to demonstrate commitment and be ready for MAI and OpenAI needs.

## Key Information

- Jonsi Stephenson said a temporary restraining order against him was lifted; remaining legal focus is on solicitation, and he believes his contract has no consequence.

- Microsoft AI Infrastructure (MAI) already has an existing production VAST Data cluster via CoreWeave and has prior familiarity with VAST Data; MAI interest in VAST is not new.

- Kushal Datta was identified as a key MAI stakeholder who owns the relationship between Microsoft AI and Azure.

- Microsoft AI escalation was triggered after the Inflection acquisition and Azure supercomputer issues; Mustafa Suleyman escalated problems and this drove internal initiatives.

- Maneesh Sah is running a Microsoft project called Bifrost with approximately 30+ developers to address Azure stack issues and is pitching it to MAI.

- An internal comparison slide (Azure Gen10.3 vs VAST ODM design) claimed approximately 4.3x power reduction, approximately 7x footprint reduction, and approximately 1.5x more throughput for VAST Data; this slide significantly upset Maneesh Sah and Microsoft leadership.

- MAI timeline slipped from prior go-live in January 2026 and scale in February 2026 to a likely decision around March 2026 and go-live around May 2026; MAI still wants a January 2026 POC that was characterized as political and likely a bake-off.

- Supply-chain risk discussed: flash and QLC constraints are worsening as manufacturers repurpose capacity to HBM and DRAM; Microsoft is constrained due to just-in-time purchasing; HDD supply may improve but still has long lead times.

- Deal sizing context discussed: VAST Data plan assumed approximately 1.8 to 1.9 data reduction ratio, delivering approximately 900PB effective, versus Azure Blob deploying approximately 1.6EB raw with no data reduction.

- Mustafa Suleyman’s decision was expected to be decisive for MAI outcomes (more than Azure’s internal preference), and Satya Nadella may mediate between Scott Guthrie and Mustafa Suleyman.

- OpenAI runs massive Databricks and Spark pipelines (tens of millions of CPU cores) and has moved some workloads off Azure due to CPU capacity constraints; this reinforces a split between data-lake CPU regions and disaggregated GPU fleets.

---

- Jonsi Stephenson said a temporary restraining order against him was lifted, and the remaining legal focus is on solicitation; he believes his contract has no consequence.

- Kushal Datta is a key MAI stakeholder and owns the relationship between Microsoft AI and Azure.

- Maneesh Sah is running a project called Bifrost with approximately 30+ developers to address Azure stack issues and is pitching it to MAI.

- An internal comparison slide (Azure Gen10.3 vs VAST Data ODM design) claimed approximately 4.3x power reduction, approximately 7x footprint reduction, and approximately 1.5x more throughput for VAST Data; this slide significantly upset Maneesh Sah and Microsoft leadership.

- MAI timeline slipped from prior go-live January 2026 and scale February 2026 to a likely decision around March 2026 and go-live around May 2026; MAI still wants a January 2026 POC that was characterized as largely political and a bake-off.

- Supply chain risk is increasing for flash, including QLC, due to manufacturers repurposing capacity to HBM/DRAM; Microsoft is constrained due to just-in-time purchasing, while HDD supply may improve but still has long lead times.

- Deal sizing context discussed: VAST Data planning assumed approximately 1.8 to 1.9 data reduction ratio, delivering approximately 900PB effective, versus Azure Blob deploying approximately 1.6EB raw with no data reduction.

- Mustafa Suleyman's decision is expected to be decisive for MAI outcomes (more than Azure's), and Satya Nadella may mediate between Scott Guthrie and Mustafa Suleyman.

- OpenAI runs massive Databricks/Spark pipelines (tens of millions of CPU cores) and has moved some workloads off Azure due to CPU capacity constraints, reinforcing a split between data-lake CPU regions and disaggregated GPU fleets.
