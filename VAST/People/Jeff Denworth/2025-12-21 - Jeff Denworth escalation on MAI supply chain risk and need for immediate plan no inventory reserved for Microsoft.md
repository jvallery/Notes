---
type: people
title: Jeff Denworth escalation on MAI supply chain risk and need for immediate plan (no inventory reserved for Microsoft)
date: '2025-12-21'
person: Jeff Denworth
participants:
- Jeff Denworth
- Jason Vallery
- Lior Genzel
- Renen Hallak
- Alon Horev
- Shachar Feinblit
- Avery Pham
- Jonsi Stefansson
- Rick Scurfield
- Manish Sah
- Kushal Datta
- Kanchan Mehrotra
- Qingying Zhang
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2025-12-21_075242_8515_Re-MAI--VAST-December-8th-EoD-update.md
tags:
- type/people
- person/jeff-denworth
- generated
---

# Jeff Denworth escalation on MAI supply chain risk and need for immediate plan (no inventory reserved for Microsoft)

**Date**: 2025-12-21
**With**: Jeff Denworth, Jason Vallery, Lior Genzel, Renen Hallak, Alon Horev, Shachar Feinblit, Avery Pham, Jonsi Stefansson, Rick Scurfield, Manish Sah, Kushal Datta, Kanchan Mehrotra, Qingying Zhang

## Summary

Jeff Denworth escalated that VAST is selling out of supply, lead times are increasing, and nothing is reserved for Microsoft, so any MAI deployment target in April to June 2026 requires an immediate plan. The thread also captures MAI decision dynamics (Mustafa is final decision maker, concerns about Kushal) and the need to build relationships with additional MAI stakeholders while aligning a VAST PoC into a large GPU environment for scale testing.


## Action Items


- [?] Create an immediate plan for how VAST Data will support any Microsoft MAI deployment targeted for April 2026, May 2026, or June 2026, explicitly addressing that no inventory is reserved for Microsoft and clarifying whether Microsoft expects to use VAST's supply chain. @Myself ⏫ #task #proposed #auto

- [?] Send Jeff Denworth the most recent analysis Jason Vallery has regarding the Microsoft MAI deal (requested by Jeff Denworth on 2025-12-12). @Myself ⏫ #task #proposed #auto

- [?] Work with VAST Operations to confirm whether VAST can deliver Microsoft MAI requirements within the tight timeframe and whether Microsoft Azure allocation is being preserved, including ordering timing and sourcing plan for a potential 2 EB requirement. @TBD ⏫ #task #proposed #auto

- [?] Obtain introductions and establish direct communication with Majid Mohammed (Mustafa's chief of staff), Yunchao Gong (Kushal Datta's boss), and Karén Simonyan (chief scientist, direct report of Mustafa) to build trust and alignment for the MAI storage decision. @Lior Genzel ⏫ #task #proposed #auto

- [?] Decide the most strategic environment to run Anson (Qi)'s VAST PoC for 1,000 to 2,000 GPU scale testing, evaluating MAI/Vipin environment versus Nscale or CoreWeave clusters, and align the PoC plan with MAI stakeholders. @TBD ⏫ #task #proposed #auto

- [?] Prepare analysis of working capital and opportunity cost for VAST Data versus Microsoft if Microsoft MAI is buying 100 EB, as requested by Jeff Denworth. @TBD #task #proposed #auto




## Decisions


- Lior Genzel will take the lead on obtaining introductions to key MAI stakeholders (Majid Mohammed, Yunchao Gong, and Karén Simonyan) to reduce reliance on Kushal Datta as the sole conduit to the final decision maker (Mustafa).




## Key Information


- Jeff Denworth stated that VAST Data is quickly selling out of supply, lead times are skyrocketing, and there is nothing reserved for Microsoft for the MAI effort, so any April to June 2026 deployment requires an immediate plan.

- Jeff Denworth asked whether Microsoft MAI expects to use VAST Data's supply chain for the MAI deployment and emphasized he does not care about internal politics if a deployment timeline is targeted.

- Jason Vallery reported hearing from multiple Azure contacts that the final MAI storage decision is Mustafa's and that Kushal Datta cannot be trusted.

- Jason Vallery stated that in a face-to-face meeting, Kushal Datta claimed he would influence Mustafa's decision and that VAST Data is the preferred solution, but Jason Vallery is concerned Kushal Datta may not be honest and may be 'playing' VAST.

- Jason Vallery identified MAI stakeholders VAST needs relationships with: Majid Mohammed (Mustafa's chief of staff), Yunchao Gong (Kushal Datta's boss), and Karén Simonyan (Yunchao Gong's boss, described as 'chief scientist' and a direct report of Mustafa).

- Jason Vallery stated he has no current relationship with Majid Mohammed, Yunchao Gong, or Karén Simonyan, and that Lior Genzel will take the lead on getting introductions.

- Lior Genzel reported that Anson (Qi) requested moving a VAST PoC into either the MAI/Vipin environment or other large GPU clusters (Nscale or CoreWeave) because their current lab cluster lacks 1,000 to 2,000 GPUs needed for performance scale testing.

- Lior Genzel said he messaged Alon Horev to strategize options for the most strategic environment for Anson (Qi)'s VAST PoC and described an opportunity to align Kushal Datta's MAI plans with Qi's PoC plans.

- In the December 8, 2025 end-of-day update, Lior Genzel reported that Kushal Datta said MAI's initial GPU drop will arrive in February 2026 and they need a storage solution ready for the May to June 2026 timeframe, and that January 2026 is no longer a hard date.

- Lior Genzel reported that Kushal Datta stated MAI will decide on the storage deployment and told Manish Sah that Azure Blob does not make sense versus VAST Data for MAI requirements.

- Lior Genzel reported that Vamshi (leader of the Azure Blob product, last name not provided) emphasized Microsoft's decision is internal and expressed frustration with VAST Data's aggressive approach in highlighting Azure Blob deficiencies.

- Jeff Denworth stated supply chain is a complete disaster for the upcoming year and asked how VAST would source a 2 EB requirement for Microsoft MAI, when it needs to be ordered, and who VAST would order it from.

- Jeff Denworth stated that Sagar took a job at Nscale and asked for an end-of-week status summary and analysis of working capital and opportunity cost if Microsoft is buying 100 EB.

- Lior Genzel reported that Sagar, who stepped into Nidhi's role after she left, resigned and will likely join Nscale, and that the team planned to speak with Sagar for advice on navigating Microsoft internal politics.

- Renen Hallak stated Microsoft should have their own flash allocation with NAND manufacturers and that VAST efficiencies could reduce Microsoft's NAND needs and potentially use Microsoft's excess allocation for other customers.




---

*Source: [[2025-12-21_075242_8515_Re-MAI--VAST-December-8th-EoD-update]]*
