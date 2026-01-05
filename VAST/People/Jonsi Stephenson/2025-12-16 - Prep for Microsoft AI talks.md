---
type: people
title: Prep for Microsoft AI talks
date: '2025-12-16'
person: Jonsi Stephenson
participants:
- Jonsi Stefanson
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-12-16 09 08 - Jonsi Jason 1-1.md
tags:
- type/people
- person/jonsi-stephenson
- generated
---

# Prep for Microsoft AI talks

**Date**: 2025-12-16
**With**: Jonsi Stefanson, Jason Vallery

## Summary

Jonsi and Jason aligned on positioning a “better together” story with Microsoft: VAST as GPU-adjacent high-performance storage with deep Azure Blob integration, while Blob remains the exabyte-scale data lake. They discussed Microsoft AI (MAI) politics around Bifrost/Apollo, a likely performance bake-off vs Azure, and timeline slippage (POC in January; decision around March; go-live around May) plus supply-chain risk (flash constraints).
## Action Items
- [?] Send Jonsi the slide deck/comparison (power/footprint/throughput) to use before the Ong/Manish meetings. @Myself ⏫ #task #proposed
- [?] Review the Azure Blob deep-integration document with Jeff on Friday. @Myself #task #proposed
- [?] Text Jason after the meeting with Ong and Manish and debrief to formulate forward strategy. @Myself #task #proposed
- [?] Add Jonsi to the thread and send notes previously shared with the team regarding supply-chain/flash constraints. @Myself #task #proposed

## Decisions
- Position the partnership as Blob for central exabyte-scale data lakes and VAST for GPU-adjacent storage, enabled by deep integration between VAST and Azure Blob.
- Proceed with drafting/planning the Azure Blob deep-integration approach rather than waiting for a Microsoft PO as a prerequisite.

## Key Information
- Jonsi’s temporary restraining order was lifted; the remaining case focus is solicitation, which he believes has no contractual consequence.
- Microsoft AI (MAI) historically used VAST prior to Microsoft acquisition; they already run VAST in production (Condor cluster) and are familiar with it.
- Internal Microsoft project context: Apollo (net-new Azure effort) and Bifrost (Manish-led effort to improve Azure stack; described as “lipstick on a pig”).
- MAI timeline has slipped: they want a POC in January; decision expected around March; go-live now more like May (previously January/February).
- Supply chain risk: flash/QLC constraints are significant; Microsoft may be constrained due to just-in-time purchasing; rumors include considering HDDs due to flash shortages.
- A comparison slide claims roughly 4.3x power reduction, ~7x footprint reduction, and ~1.5x more throughput for VAST vs Azure Gen10.3 all-flash (planned to ship in March).
- Decision authority for MAI capacity is described as Mustafa Suleyman’s decision rather than Azure’s; Satya may mediate between Scott Guthrie and Mustafa.
- OpenAI’s large Databricks CPU pipelines hit Azure capacity limits; Scott Guthrie allowed migration of that workload to AWS; OpenAI’s Azure exclusivity was removed from the contract.

## Topics
- Microsoft AI (MAI) deal dynamics and stakeholder politics
- VAST vs Azure Blob positioning and “better together” integration strategy
- Bifrost/Apollo internal Microsoft initiatives
- Performance bake-off/POC planning and timeline slippage
- Flash vs HDD supply-chain constraints and procurement strategy
- Neo-clouds/NCPs (Nebius, Nscale, CoreWeave) and control-plane opportunity
- Risk profile of neo-cloud business models and GPU lifecycle economics

---

*Source: [[Inbox/_archive/2025-12-16/2025-12-16 09 08 - Jonsi Jason 1-1.md|2025-12-16 09 08 - Jonsi Jason 1-1]]*

## Related

- [[Jonsi Stephenson]]
- [[Jason Vallery]]
- [[Jeff Denworth]]
- [[Maneesh Sah]]
- [[Jai Menon]]
- [[Ronen Cohen]]
- [[Bo Wang]]
- [[Amy Hood]]
- [[Sam Altman]]
- [[Satya Nadella]]
- [[Microsoft]]
- [[Amazon]]
- [[Google]]
- [[CoreWeave]]
- [[NetApp]]
- [[Micron]]
- [[Samsung]]
- [[Western Digital]]
- [[Toshiba]]
- [[Intel]]
- [[Cloud control plane]]
- [[OpenAI VAST POC - CoreWeave Cluster]]