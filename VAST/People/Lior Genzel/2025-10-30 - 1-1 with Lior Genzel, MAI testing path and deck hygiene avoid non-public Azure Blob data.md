---
type: people
title: 1:1 with Lior Genzel, MAI testing path and deck hygiene (avoid non-public Azure Blob data)
date: '2025-10-30'
person: Lior Genzel
participants:
- Jason Vallery
- Lior Genzel
- Igal Figlin
- Maneesh Sah
- Renen (unknown last name)
- Manish (likely Maneesh Sah, but not confirmed)
- Ong (unknown last name)
- Kanchan Mehrotra
- Nidhi (unknown last name)
- Ronnie Booker
- Billy Kettler
- Yonce (unknown last name)
- Renata (unknown last name)
- Alon Horev
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De.md
tags:
- type/people
- generated
---

# 1:1 with Lior Genzel, MAI testing path and deck hygiene (avoid non-public Azure Blob data)

**Date**: 2025-10-30
**With**: Jason Vallery, Lior Genzel, Igal Figlin, Maneesh Sah, Renen (unknown last name), Manish (likely Maneesh Sah, but not confirmed), Ong (unknown last name), Kanchan Mehrotra, Nidhi (unknown last name), Ronnie Booker, Billy Kettler, Yonce (unknown last name), Renata (unknown last name), Alon Horev

## Summary

Jason Vallery and Lior Genzel aligned on MAI meeting preparation, emphasizing immediate functional testing via existing environments and hardware-based testing using pre-certified hardware, with limited VM support expected in December 2025. They agreed to avoid sharing non-public Azure Blob HDD/Flash performance details externally and to strengthen the MAI deck with observability and CSI driver messaging. They also discussed Azure internal politics around VM roadmap messaging and a potential executive-sponsored path to engage Azure hardware leadership (CVP Ronnie Borker).

## Action Items

- [?] Update the MAI deck to include a side-by-side comparison table of the two design options, ensuring any Azure Blob HDD/Flash performance figures are removed or replaced with public-only data for external sharing. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Clarify with the MAI contact what they expect from testing (functional validation vs performance KPIs), and propose immediate functional access via an existing VAST NeoCloud environment if hardware testing is not yet possible. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Ask Microsoft MAI whether they can host pre-certified hardware for immediate testing, and if yes, initiate a plan to ship a hardware kit to the appropriate Microsoft site. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Follow up with Igal Figlin to acknowledge the updated Azure VM roadmap, reduce political friction, and reinforce that VAST is not blocking on compute while still being honest about near-term constraints. @Lior Genzel 📅 2025-10-31 #task #proposed #auto

- [?] Review the MAI deck updates from Lior Genzel and confirm the side-by-side comparison approach excludes non-public Azure Blob HDD/Flash figures for any externally shared version. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Clarify with the MAI contact what they expect to validate in testing (functional access vs performance/KPIs) and confirm whether they can host pre-certified hardware for immediate testing; if yes, plan hardware shipment. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Follow up with Igal Figlin to acknowledge the updated Azure VM roadmap and reduce political friction created by internal messaging that VAST is dismissing Azure compute work. @Lior Genzel 📅 2025-10-31 #task #proposed #auto

## Decisions

- Do not include non-public Azure Blob on HDD or Azure Blob on Flash performance data in any externally shared deck materials, especially anything that could be forwarded to third parties such as N-scale.

- For MAI near-term testing, prioritize pre-certified hardware-based testing; treat VM-based testing as a later path starting in December 2025 with small VM sizes.

- Do not include non-public Microsoft Azure Blob on HDD/Flash performance or cost figures in externally shared decks or materials, especially when third parties (example: N-scale) could receive them.

- For the MAI engagement, prioritize immediate functional testing access via an existing VAST environment and pursue hardware-based testing using pre-certified hardware, since VM support is not available until December 2025 and will initially be limited.

## Key Information

- Lior Genzel prepared a MAI meeting deck with two design options and planned a side-by-side comparison table to compare the options and relevant cloud baselines.

- Jason Vallery considers Azure Blob on HDD and Azure Blob on Flash performance details to be non-public Microsoft information (known via NDA or internal context) and should not be shared externally with third parties such as N-scale.

- A MAI contact asked to start testing immediately and wanted functional access before the scheduled meeting, indicating urgency to validate VAST functionality quickly.

- VAST currently supports deployment on pre-certified hardware only, and does not support VMs yet; VM support is expected to start in December 2025 and will initially be limited to small VM sizes.

- LSv4 is viewed by the team as a poor VM option for VAST workloads, while Igal Figlin communicated a 2026 Azure VM roadmap with very strong specs, but the timeline is approximately a year out and therefore not useful for near-term MAI testing.

- Igal Figlin called Lior Genzel directly due to internal Microsoft politics, concerned that internal feedback (attributed to Renen) characterized Azure compute VMs as a blocker and undermined Igal's efforts to sponsor VAST at Microsoft Ignite.

- Lior Genzel told Igal Figlin that earlier feedback about LSv4 being the worst VM option was shared honestly during a Redmond visit 6 to 8 weeks prior, and that any escalation from Maneesh Sah was internal Microsoft politics rather than a change in VAST's intent to collaborate.

---

- Jason Vallery advised that Azure Blob on HDD and Azure Blob on Flash performance/cost figures are not publicly published by Microsoft and should not be shared externally with third parties (example given: N-scale), even if they are known under NDA contexts.

- A Microsoft AI Infrastructure (MAI) contact asked to start testing immediately and wanted functional access before the next-day meeting; Lior Genzel proposed offering functional testing access via an already-running VAST environment (NeoClouds) while clarifying expected testing outcomes.

- VAST currently supports deployment only on pre-certified hardware for MAI-style testing; VAST does not support VMs yet, and VM support tied to Igal Figlin's Azure compute work is expected in December 2025 but initially limited to small VM sizes.

- Lior Genzel stated that Azure LSv4 is currently the weakest VM option for VAST's needs, while the Azure compute roadmap communicated by Igal Figlin for 2026 appears very strong on paper, but the timeline is roughly a year out and therefore not useful for near-term decisions.

- Lior Genzel reported Azure internal politics: Igal Figlin called Lior directly after hearing that internal stakeholders (including Maneesh Sah and Renen, both referenced) believed VAST was dismissing the Azure VM work as inadequate, which Igal felt undermined his efforts to sponsor VAST at Microsoft Ignite.

- Jason Vallery and Lior Genzel discussed that Amazon has 300 Gbps-class VMs but on Amazon's ARM-based chips, implying a product decision for VAST if pursuing that path; Lior compared this to VAST's existing work with ARM-based components (example mentioned: BlueField).
