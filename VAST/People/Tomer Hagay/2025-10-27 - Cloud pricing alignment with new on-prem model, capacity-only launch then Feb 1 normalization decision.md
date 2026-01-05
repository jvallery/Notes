---
type: "projects"
title: "Cloud pricing alignment with new on-prem model, capacity-only launch then Feb 1 normalization decision"
date: "2025-10-27"
project: ""
participants: ["Tomer Hagay", "Jason Vallery", "Yancey", "Eric Wolfie", "Lior Genzel", "Eiki", "Eric", "Timo Pervane", "Helen"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Cloud pricing alignment with new on-prem model, capacity-only launch then Feb 1 normalization decision

**Date**: 2025-10-27
**Project**: [[]]
**Attendees**: Tomer Hagay, Jason Vallery, Yancey, Eric Wolfie, Lior Genzel, Eiki, Eric, Timo Pervane, Helen

## Summary

Internal pricing working session debated how to align VAST cloud pricing with the new on-prem core-plus-capacity model given hyperscaler instance core density differences. The team aligned on launching cloud private offers with capacity-only pricing and stricter discount guidance, while targeting a unified model decision by 2026-02-01. They also agreed not to disable or rate-limit excess vCPUs and prioritized an NBCU TCO deliverable plus marketplace entitlement definitions.


## Action Items


- [?] Propose a cloud private-offer pricing structure and discount guidance using capacity-only pricing for immediate field use. @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Forward the NBCU TCO working session invite to the core group (Jason Vallery, Lior Genzel, Eiki, Tomer Hagay, Eric Wolfie, Eric). @Yancey 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Join and support the NBCU TCO working session and align on inputs including reserved pricing assumptions, egress assumptions, and cloud infrastructure COGS. @Eric 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Join the NBCU TCO working session to validate the pricing approach and competitive posture for VAST cloud private offers. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Add core stakeholders to the NBCU TCO sync invite. @Tomer Hagay 📅 2025-10-27 #task #proposed #auto

- [?] Define and publish a cloud-specific discount policy for private offers to avoid extreme discounts and margin erosion. @Pricing vTeam 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Complete the NBCU TCO analysis and share it with NBCU by Wednesday 2025-10-29. @Eric 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Decide whether to introduce fixed cores-per-PB normalization for cloud pricing starting 2026-02-01 and document the model and rationale. @Pricing vTeam 📅 2026-02-01 ⏫ #task #proposed #auto

- [?] Define marketplace entitlements and pricing schema for a Google Cloud private offer and begin the approval process to avoid entitlement-change delays. @Yancey 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Plan and document a unified pricing rollout by 2026-02-01 that keeps on-prem and cloud pricing consistent, including how discounts and any normalization will be applied. @Tomer Hagay 📅 2026-02-01 ⏫ #task #proposed #auto




## Decisions


- Launch VAST cloud private offers using capacity-only pricing (no core-based charge) as the near-term model while broader pricing alignment work continues.

- Do not implement disabling or rate-limiting of excess vCPUs in cloud instances; any future core normalization will be handled commercially rather than via technical enforcement.

- Target a unified pricing model decision by 2026-02-01 to better align cloud pricing with the new on-prem core-plus-capacity model.




## Key Information


- Jason Vallery started at VAST Data on Monday 2025-10-20 and was one week into the role as of 2025-10-27.

- VAST Data is changing the on-prem price list by lowering capacity list price, lowering core list price, and tightening discount levels, and the team validated the new numbers against historical opportunity data for the broader VAST business.

- Hyperscaler instance core density (vCPU per TB or cores per PB) varies significantly across instance types such as Azure LSv4 versus AWS i3en, which causes large price-per-TB swings if cloud pricing uses a core-based component without normalization.

- A proposed commercial normalization approach for cloud pricing is to charge a fixed normalized number of cores per petabyte (example discussed: 200 cores per PB) regardless of the actual vCPU count in the chosen cloud instances, to preserve cross-cloud parity and align with the on-prem core-plus-capacity model.



---

*Source: [[2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]]*