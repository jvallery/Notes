---
type: "people"
title: "Prep for Microsoft AI talks"
date: "2026-01-03"
person: "Jonsi Stephenson"
participants: ["Jonsi Stefanson", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/_archive/2026-01-03/Jonsi:Jason 1-1 .md"
tags:
  - "type/people"
  - "person/jonsi-stephenson"
  - "generated"
---

# Prep for Microsoft AI talks

**Date**: 2026-01-03
**With**: Jonsi Stefanson, Jason Vallery

## Summary

Jonsi and Jason aligned on positioning a “better together” story with Microsoft: VAST as GPU-adjacent high-performance file storage deeply integrated with Azure Blob as the central exabyte-scale data lake. They reviewed the political context around Microsoft AI (MAI), Manish’s Bifrost effort, and why Microsoft leadership is upset about an internal performance/space/power comparison slide shared with MAI. They also discussed MAI timeline slippage (decision likely March, go-live May), supply-chain risk (flash constraints), and the likelihood of a bake-off between VAST and Azure’s Bifrost/Blob approach.

## Action Items

- [ ] Send Jonsi the slide deck/comparison materials (including the power/footprint/throughput slide) before his meeting with Ong and Manish. @Myself ⏫ #task
- [ ] Text Jason after the meeting with Ong and Manish and schedule a follow-up call to debrief and formulate the go-forward strategy. @Jonsi #task

## Decisions

- Position the partnership narrative as Azure Blob for central data lakes and VAST for GPU-adjacent storage, enabled by deep integration with Blob (avoid expanding into higher-level database/event-broker topics in the Microsoft conversation).
- Proceed with drafting/starting the deep Azure Blob integration project rather than waiting for a Microsoft PO, to demonstrate commitment and be ready for MAI/OpenAI needs.

## Key Information

- Temporary restraining order against Jonsi was lifted; remaining legal focus is on solicitation and Jonsi believes his contract has no consequence.
- MAI has an existing production VAST cluster (via CoreWeave) and prior familiarity with VAST; MAI’s interest is not new.
- Key MAI stakeholder: Kushal Datta, who owns the relationship between Microsoft AI and Azure.
- Microsoft AI escalation was triggered after Inflection acquisition and Azure supercomputer issues; Mustafa Suleyman escalated problems and this drove internal initiatives.
- Manish is running a project called Bifrost (described as “lipstick on a pig”) with ~30+ devs to address Azure stack issues and is pitching it to MAI.
- A comparison slide claims Azure Gen10.3 vs VAST ODM design shows ~4.3x power reduction, ~7x footprint reduction, and ~1.5x more throughput for VAST; this slide significantly upset Manish and leadership.
- MAI timeline has slipped: prior go-live January/scale February; now go-live likely May with decision around March; MAI wants a January POC (seen as largely political/bake-off).
- Supply chain risk: flash/QLC constraints worsening due to manufacturers repurposing capacity to HBM/DRAM; Microsoft is constrained due to just-in-time purchasing; HDD supply may improve but still long lead times.
- Deal sizing context: VAST plan assumed ~1.8–1.9 data reduction ratio, delivering ~900PB vs Blob deploying ~1.6EB raw (no data reduction).
- Mustafa’s decision is expected to be decisive for MAI outcomes, not Azure’s; Satya may mediate between Scott Guthrie and Mustafa.
- OpenAI runs massive Databricks/Spark pipelines (tens of millions of CPU cores) and has moved some workloads off Azure due to CPU capacity constraints; reinforces split between data-lake CPU regions and disaggregated GPU fleets.

---

*Source: [[Jonsi:Jason 1-1 ]]*

## Related

- [[Jonsi Stephenson]]
- [[Jeff Denworth]]
- [[Maneesh Sah]]
- [[Shachar Feinblit]]
- [[Kushal Datta]]
- [[Alon Horev]]
- [[VAST on Azure Integration]]
- [[Microsoft]]
- [[OpenAI]]
