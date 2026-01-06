---
type: people
title: Jeff Denworth flags MAI supply chain risk and need for immediate deployment plan
date: '2025-12-21'
person: Jeff Denworth
participants:
- Jeff Denworth
- Jason Vallery
- Lior Genzel
- Renen Hallak
- Alon Horev
- Shachar Feinblit
- Jonsi Stefansson
- Rick Scurfield
- Manish Sah
- Kushal Datta
- Kanchan Mehrotra
- Qingying Zhang
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-21_075242_5666_Re-MAI--VAST-December-8th-EoD-update.md
tags:
- type/people
- person/jeff-denworth
- generated
---

# Jeff Denworth flags MAI supply chain risk and need for immediate deployment plan

**Date**: 2025-12-21
**With**: Jeff Denworth, Jason Vallery, Lior Genzel, Renen Hallak, Alon Horev, Shachar Feinblit, Jonsi Stefansson, Rick Scurfield, Manish Sah, Kushal Datta, Kanchan Mehrotra, Qingying Zhang

## Summary

Jeff Denworth asked whether Microsoft MAI expects to use VAST Data supply chain and warned that VAST is selling out inventory with skyrocketing lead times. Jeff emphasized that if Microsoft wants an April to June 2026 deployment window, VAST needs a concrete plan immediately because nothing is reserved for Microsoft.


## Action Items


- [?] Send Jeff Denworth the most recent analysis requested in the thread (context: MAI deal status and/or capacity and supply chain implications). @Myself ⏫ #task #proposed #auto

- [?] Work with VAST Operations to confirm whether any inventory or flash allocation is reserved or trackable for Microsoft MAI requirements, and determine feasibility to deliver within the April 2026 to June 2026 window given constrained supply chain. @Myself ⏫ #task #proposed #auto

- [?] Obtain introductions and establish communication with Majid Mohammed (Mustafa chief of staff), Yunchao Gong (Kushal Datta's boss), and Karén Simonyan (chief scientist reporting to Mustafa) to reduce reliance on Kushal Datta as the sole conduit. @Lior Genzel ⏫ #task #proposed #auto

- [?] Coordinate with Alon Horev to identify the most strategic environment to run Anson (Qi) VAST PoC at 1,000 to 2,000 GPU scale, evaluating Microsoft MAI/Vipin environment versus Nscale or CoreWeave clusters. @Lior Genzel #task #proposed #auto

- [?] Meet with Jeff Denworth on the next day (relative to 2025-12-21) to align on urgency, supply chain plan, and expectations for Microsoft MAI deployment timing. @Myself 📅 2025-12-22 ⏫ #task #proposed #auto




## Decisions


- Lior Genzel will take the lead on obtaining introductions to key Microsoft MAI stakeholders (Majid Mohammed, Yunchao Gong, and Karén Simonyan) to build trust beyond Kushal Datta.




## Key Information


- Jeff Denworth stated VAST Data is quickly selling out of inventory and lead times are skyrocketing, creating supply chain risk for any Microsoft MAI deployment that relies on VAST sourcing.

- Jeff Denworth stated that nothing is reserved for Microsoft MAI and that if Microsoft wants to deploy in April 2026, May 2026, or June 2026, VAST needs a plan immediately.

- Jason Vallery reported hearing from multiple Azure stakeholders that the final decision for Microsoft MAI storage is Mustafa's and that Kushal Datta cannot be trusted.

- Jason Vallery stated he has no current relationship with Majid Mohammed (Mustafa's chief of staff), Yunchao Gong (Kushal Datta's boss), or Karén Simonyan (Yunchao Gong's boss and chief scientist reporting to Mustafa), and that Lior Genzel will lead getting introductions.

- Lior Genzel reported that Anson (Qi) requested moving a VAST proof of concept into either the Microsoft MAI/Vipin environment or other large GPU clusters (Nscale or CoreWeave) because Microsoft labs lack 1,000 to 2,000 GPUs needed for performance scale testing.

- Jeff Denworth stated supply chain for the upcoming year is a complete disaster and asked how VAST would source Microsoft's stated requirement of 2 exabytes and when it must be ordered and from whom.

- Lior Genzel reported that Kushal Datta said Microsoft MAI's initial GPU drop will arrive in February 2026 and they need a storage solution ready for a May 2026 to June 2026 timeframe, and that January 2026 is no longer a hard date.

- Lior Genzel reported that Kushal Datta said Microsoft MAI will decide on the storage deployment and that Kushal told Manish Sah that Azure Blob does not make sense versus VAST for MAI requirements.

- Lior Genzel reported that Vamshi (Azure Blob product leader) said Microsoft's decision is internal and expressed frustration with VAST's aggressive approach in highlighting Azure Blob deficiencies.

- Lior Genzel reported that Kushal Datta requested a meeting with Alon Horev the following week to discuss solution design for Microsoft MAI.

- Jeff Denworth stated Sagar took a job at Nscale and asked for an end-of-week status summary and an analysis of working capital and opportunity cost if Microsoft is buying 100 exabytes.

- Renen Hallak stated Microsoft should have their own flash allocation with NAND manufacturers and that VAST efficiencies could reduce Microsoft's NAND needs and potentially allow using Microsoft's excess allocation for other customers.




---

*Source: [[2025-12-21_075242_5666_Re-MAI--VAST-December-8th-EoD-update]]*
