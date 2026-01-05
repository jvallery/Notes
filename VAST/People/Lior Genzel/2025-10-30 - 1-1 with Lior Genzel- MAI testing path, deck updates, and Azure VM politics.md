---
type: "people"
title: "1:1 with Lior Genzel: MAI testing path, deck updates, and Azure VM politics"
date: "2025-10-30"
person: ""
participants: ["Jason Vallery", "Lior Genzel"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Lior Genzel: MAI testing path, deck updates, and Azure VM politics

**Date**: 2025-10-30
**With**: Jason Vallery, Lior Genzel

## Summary

Jason Vallery and Lior Genzel aligned on MAI meeting preparation, emphasizing immediate functional testing via existing environments and hardware-based testing using pre-certified hardware, with limited VM support expected in December 2025. They agreed to avoid sharing non-public Azure Blob HDD/Flash performance details externally and to strengthen the MAI deck with observability and CSI driver messaging. They also discussed Azure internal politics around VM roadmap messaging and a potential executive-sponsored path to engage Azure hardware leadership (CVP Ronnie Borker).


## Action Items


- [?] Review the MAI deck updates from Lior Genzel and confirm the side-by-side comparison approach excludes non-public Azure Blob HDD/Flash figures for any externally shared version. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Clarify with the MAI contact what they expect to validate in testing (functional access vs performance/KPIs) and confirm whether they can host pre-certified hardware for immediate testing; if yes, plan hardware shipment. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Follow up with Igal Figlin to acknowledge the updated Azure VM roadmap and reduce political friction created by internal messaging that VAST is dismissing Azure compute work. @Lior Genzel 📅 2025-10-31 #task #proposed #auto




## Decisions


- Do not include non-public Microsoft Azure Blob on HDD/Flash performance or cost figures in externally shared decks or materials, especially when third parties (example: N-scale) could receive them.

- For the MAI engagement, prioritize immediate functional testing access via an existing VAST environment and pursue hardware-based testing using pre-certified hardware, since VM support is not available until December 2025 and will initially be limited.




## Key Information


- Jason Vallery advised that Azure Blob on HDD and Azure Blob on Flash performance/cost figures are not publicly published by Microsoft and should not be shared externally with third parties (example given: N-scale), even if they are known under NDA contexts.

- A Microsoft AI Infrastructure (MAI) contact asked to start testing immediately and wanted functional access before the next-day meeting; Lior Genzel proposed offering functional testing access via an already-running VAST environment (NeoClouds) while clarifying expected testing outcomes.

- VAST currently supports deployment only on pre-certified hardware for MAI-style testing; VAST does not support VMs yet, and VM support tied to Igal Figlin's Azure compute work is expected in December 2025 but initially limited to small VM sizes.

- Lior Genzel stated that Azure LSv4 is currently the weakest VM option for VAST's needs, while the Azure compute roadmap communicated by Igal Figlin for 2026 appears very strong on paper, but the timeline is roughly a year out and therefore not useful for near-term decisions.

- Lior Genzel reported Azure internal politics: Igal Figlin called Lior directly after hearing that internal stakeholders (including Maneesh Sah and Renen, both referenced) believed VAST was dismissing the Azure VM work as inadequate, which Igal felt undermined his efforts to sponsor VAST at Microsoft Ignite.

- Jason Vallery and Lior Genzel discussed that Amazon has 300 Gbps-class VMs but on Amazon's ARM-based chips, implying a product decision for VAST if pursuing that path; Lior compared this to VAST's existing work with ARM-based components (example mentioned: BlueField).



---

*Source: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]]*