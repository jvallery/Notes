---
type: projects
title: MAI and VAST supply chain risk and stakeholder alignment for May/June deployment
date: '2025-12-21'
project: Cloud
participants:
- Jeff Denworth
- Jason Vallery
- Lior Genzel
- Renen Hallak
- Alon Horev
- Shachar Feinblit
- Jonsi Stefansson
- Rick Scurfield
- Avery Pham
- Manish Sah
- Kushal Datta
- Kanchan Mehrotra
- Qingying Zhang
- Unknown Microsoft contact (Mustafa)
- Majid Mohammed
- Yunchao Gong
- Karén Simonyan
- Vamshi (Azure Blob product lead, last name unknown)
- Sagar (last name unknown)
- Nidhi (last name unknown)
- Anson (Qi) (last name unknown)
- Vipin (last name unknown)
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-21_075242_5666_Re-MAI--VAST-December-8th-EoD-update.md
tags:
- type/projects
- project/cloud
- generated
---

# MAI and VAST supply chain risk and stakeholder alignment for May/June deployment

**Date**: 2025-12-21

**Project**: [[Cloud]]

**Attendees**: Jeff Denworth, Jason Vallery, Lior Genzel, Renen Hallak, Alon Horev, Shachar Feinblit, Jonsi Stefansson, Rick Scurfield, Avery Pham, Manish Sah, Kushal Datta, Kanchan Mehrotra, Qingying Zhang, Unknown Microsoft contact (Mustafa), Majid Mohammed, Yunchao Gong, Karén Simonyan, Vamshi (Azure Blob product lead, last name unknown), Sagar (last name unknown), Nidhi (last name unknown), Anson (Qi) (last name unknown), Vipin (last name unknown)

## Summary

Jeff Denworth escalated that VAST supply chain capacity is selling out quickly, lead times are rising, and nothing is reserved for Microsoft, so a concrete plan is needed immediately if Microsoft MAI expects deployment in April through June 2026. The thread also highlights MAI decision dynamics (final decision attributed to Mustafa), concerns about Kushal’s trustworthiness, and the need to build relationships with additional MAI stakeholders while selecting the best environment for a large-scale VAST PoC requiring 1,000-2,000 GPUs.


## Action Items


- [?] Send Jeff Denworth the most recent analysis requested in the thread (analysis content not specified in email). @Myself 📅 2025-12-12 ⏫ #task #proposed #auto

- [?] Lead introductions and establish communication with Microsoft MAI stakeholders Majid Mohammed, Yunchao Gong, and Karén Simonyan to reduce reliance on Kushal Datta as the sole conduit. @Lior Genzel 📅 2025-12-19 ⏫ #task #proposed #auto

- [?] Determine the most strategic environment to run Anson (Qi)'s VAST PoC at 1,000-2,000 GPU scale, evaluating MAI/Vipin environment versus Nscale or CoreWeave clusters. @Lior Genzel 📅 2025-12-19 ⏫ #task #proposed #auto

- [?] Coordinate with Alon Horev on options to merge Kushal Datta's MAI plans with Anson (Qi)'s PoC plans into a single validation path. @Lior Genzel 📅 2025-12-19 #task #proposed #auto

- [?] Schedule and hold a solution design meeting with Kushal Datta to review MAI storage deployment design requirements. @Alon Horev 📅 2025-12-16 ⏫ #task #proposed #auto

- [?] Create an internal plan for how VAST will source and deliver Microsoft's potential 2 EB requirement given 2026 supply chain constraints, including whether Microsoft uses VAST supply chain or their own allocations. @TBD 📅 2025-12-23 ⏫ #task #proposed #auto




## Decisions


- Lior Genzel will take the lead on obtaining introductions to key Microsoft MAI stakeholders Majid Mohammed, Yunchao Gong, and Karén Simonyan to build trust beyond Kushal Datta.




## Key Information


- Jeff Denworth stated VAST Data is selling out of supply chain capacity quickly and lead times are skyrocketing, so there is nothing reserved for Microsoft MAI unless a plan is made immediately.

- Jeff Denworth asked whether Microsoft MAI expects to use VAST Data's supply chain for any part of the MAI deployment.

- Jason Vallery reported hearing from multiple Azure contacts that the final MAI storage decision is made by an individual named Mustafa (last name not provided).

- Jason Vallery reported hearing from multiple Azure contacts that Kushal Datta cannot be trusted, and Jason is concerned Kushal may be misrepresenting VAST's preferred status to influence Mustafa.

- Jason Vallery stated he has no current relationship with Majid Mohammed, Yunchao Gong, or Karén Simonyan and that Lior Genzel will lead getting introductions to them.

- Lior Genzel stated there is no waiting time in the current plan and VAST is positioned to accelerate the MAI process.

- Lior Genzel reported that Anson (Qi) requested moving a VAST PoC into either the MAI/Vipin environment or other Nscale or CoreWeave clusters because their lab cluster lacks 1,000-2,000 GPUs needed for performance scale testing.

- Lior Genzel messaged Alon Horev to strategize options for the most strategic environment to run Anson (Qi)'s VAST PoC and to potentially merge Kushal Datta's MAI plans with Qi's PoC plans.

- In the December 8 EoD update, Kushal Datta said MAI's initial GPU drop will arrive in February (year implied 2026) and they need a storage solution ready for the May/June timeframe, with January no longer a hard date.

- In the December 8 EoD update, Kushal Datta stated MAI will decide on the storage deployment and told Manish Sah that Azure Blob does not make sense versus VAST for MAI requirements.

- A Microsoft contact named Vamshi (Azure Blob product lead, last name not provided) communicated that Microsoft's decision is internal and expressed frustration with VAST's aggressive approach in highlighting Azure Blob deficiencies.

- Kushal Datta requested a meeting with Alon Horev the following week (relative to 2025-12-08/2025-12-09) to discuss MAI solution design.

- Jeff Denworth stated supply chain constraints are expected through 2026 and recommended taking the whole Microsoft deal down in one shot with partial delivery milestones.

- Renen Hallak stated Microsoft should have their own flash allocation with NAND manufacturers and that VAST efficiencies could reduce Microsoft's NAND needs and potentially use Microsoft's excess allocation for other customers.

- Jeff Denworth asked whether VAST Operations is tracking Microsoft's requirement and whether VAST can deliver within a tight timeframe, emphasizing flawless execution.

- Jeff Denworth noted that Sagar (last name not provided) took a job at Nscale and that there were concerns about Nscale having a disastrous configuration that VAST should capitalize on.




---

*Source: [[2025-12-21_075242_5666_Re-MAI--VAST-December-8th-EoD-update]]*
