---
type: "people"
title: "1:1 with Lior Genzel, MAI testing path and deck hygiene (avoid non-public Azure Blob data)"
date: "2025-10-30"
person: ""
participants: ["Jason Vallery", "Lior Genzel", "Igal Figlin", "Maneesh Sah", "Renen (unknown last name)", "Manish (likely Maneesh Sah, but not confirmed)", "Ong (unknown last name)", "Kanchan Mehrotra", "Nidhi (unknown last name)", "Ronnie Booker", "Billy Kettler", "Yonce (unknown last name)", "Renata (unknown last name)", "Alon Horev"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Lior Genzel, MAI testing path and deck hygiene (avoid non-public Azure Blob data)

**Date**: 2025-10-30
**With**: Jason Vallery, Lior Genzel, Igal Figlin, Maneesh Sah, Renen (unknown last name), Manish (likely Maneesh Sah, but not confirmed), Ong (unknown last name), Kanchan Mehrotra, Nidhi (unknown last name), Ronnie Booker, Billy Kettler, Yonce (unknown last name), Renata (unknown last name), Alon Horev

## Summary

Jason Vallery and Lior Genzel aligned MAI meeting prep around immediate testing, with a strong preference for pre-certified hardware and VM support only starting in December 2025 for small VM sizes. They agreed to avoid sharing non-public Azure Blob HDD/Flash performance details externally and to strengthen the MAI deck with side-by-side design comparison plus observability and CSI driver callouts.


## Action Items


- [?] Update the MAI deck to include a side-by-side comparison table of the two design options, ensuring any Azure Blob HDD/Flash performance figures are removed or replaced with public-only data for external sharing. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Clarify with the MAI contact what they expect from testing (functional validation vs performance KPIs), and propose immediate functional access via an existing VAST NeoCloud environment if hardware testing is not yet possible. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Ask Microsoft MAI whether they can host pre-certified hardware for immediate testing, and if yes, initiate a plan to ship a hardware kit to the appropriate Microsoft site. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Follow up with Igal Figlin to acknowledge the updated Azure VM roadmap, reduce political friction, and reinforce that VAST is not blocking on compute while still being honest about near-term constraints. @Lior Genzel 📅 2025-10-31 #task #proposed #auto




## Decisions


- Do not include non-public Azure Blob on HDD or Azure Blob on Flash performance data in any externally shared deck materials, especially anything that could be forwarded to third parties such as N-scale.

- For MAI near-term testing, prioritize pre-certified hardware-based testing; treat VM-based testing as a later path starting in December 2025 with small VM sizes.




## Key Information


- Lior Genzel prepared a MAI meeting deck with two design options and planned a side-by-side comparison table to compare the options and relevant cloud baselines.

- Jason Vallery considers Azure Blob on HDD and Azure Blob on Flash performance details to be non-public Microsoft information (known via NDA or internal context) and should not be shared externally with third parties such as N-scale.

- A MAI contact asked to start testing immediately and wanted functional access before the scheduled meeting, indicating urgency to validate VAST functionality quickly.

- VAST currently supports deployment on pre-certified hardware only, and does not support VMs yet; VM support is expected to start in December 2025 and will initially be limited to small VM sizes.

- LSv4 is viewed by the team as a poor VM option for VAST workloads, while Igal Figlin communicated a 2026 Azure VM roadmap with very strong specs, but the timeline is approximately a year out and therefore not useful for near-term MAI testing.

- Igal Figlin called Lior Genzel directly due to internal Microsoft politics, concerned that internal feedback (attributed to Renen) characterized Azure compute VMs as a blocker and undermined Igal's efforts to sponsor VAST at Microsoft Ignite.

- Lior Genzel told Igal Figlin that earlier feedback about LSv4 being the worst VM option was shared honestly during a Redmond visit 6 to 8 weeks prior, and that any escalation from Maneesh Sah was internal Microsoft politics rather than a change in VAST's intent to collaborate.



---

*Source: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]]*