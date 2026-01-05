---
type: people
title: MAI testing path and deck
date: '2025-10-30'
person: Lior Genzel
participants:
- Lior Genzel
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-30 - Reviewed MAI meeting prep and testing
  path (prefer hardware; VMs supported in De.md
tags:
- type/people
- person/lior-genzel
- generated
---

# MAI testing path and deck

**Date**: 2025-10-30
**With**: Lior Genzel, Jason Vallery

## Summary

Jason and Lior aligned on the MAI meeting approach: a short design review followed by clarifying testing scope/KPIs/timeline and hardware logistics, given MAI’s desire to start testing immediately and limited VM support until December. They agreed to avoid sharing non-public Azure BLOB performance data externally and to strengthen the deck with observability (portal/logging) and CSI driver callouts. They also discussed Microsoft internal politics and a potential engagement path to Azure hardware leadership (Ronnie Booker) via an executive sponsor, plus broader cloud prioritization (Azure primary, OCI secondary; AWS deprioritized near term).
## Action Items
- [ ?] Add observability (portal/logging) slide(s) and a CSI driver callout to the MAI deck. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed
- [ ?] Adjust the side-by-side comparison in the MAI deck to exclude non-public Azure BLOB performance data for external sharing. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed
- [ ?] Confirm with MAI whether they can host pre-certified hardware for testing and arrange shipment if yes. @Lior Genzel 📅 2025-10-31 ⏫ #task #proposed
- [ ?] Send Ronnie Booker’s LinkedIn/contact information to Lior. @Myself #task #proposed
- [ ?] Follow up with Igal (Azure compute) thanking him for the updated VM roadmap; CC Yonsi and Renata; clarify that VAST is not trying to block him (manage internal politics). @Lior Genzel 📅 2025-10-31 #task #proposed
- [ ?] Schedule MAI meetings at KubeCon/Ignite/SC with relevant Microsoft contacts (e.g., Alon/Yonsi/Renen) as applicable. @Lior Genzel #task #proposed
- [ ?] Set a call with Billy (GCP) to review Google programs and GKE-integrated deployment patterns (if calendar allows). @Lior Genzel 📅 2025-10-31 #task #proposed
- [ ?] Align with Jeff on cloud priorities/ownership (Azure/GCP/OCI), team structure, goals, and BD expectations. @Myself ⏫ #task #proposed
- [ ?] Decide whether to bring Karl onto Jason’s team and define his scope (lab/POC support). @Myself #task #proposed
- [ ?] Confirm plan/need to attend AWS re:Invent. @Myself 🔽 #task #proposed
- [ ?] Determine sponsorship path to engage Azure hardware CVP Ronnie Booker (e.g., via Nidhi or Anand) vs using an Israeli backchannel. @Myself #task #proposed
- [ ?] Capture MAI testing requirements, KPIs, and timeline after the next MAI call; define the hardware shipment plan. @Lior Genzel 📅 2025-11-01 ⏫ #task #proposed
- [ ?] Plan Azure/GCP marketplace timelines and minimal viable offerings to satisfy key stakeholders (e.g., Foundry, Kanchan). @Myself #task #proposed

## Decisions
- Do not include non-public Azure BLOB performance data in externally shared decks/materials.
- Emphasize observability (single pane of glass) and CSI driver in the MAI deck.
- Pursue a parallel strategy: marketplace SaaS maturity plus first-party hardware-optimized wins.
- Near-term focus on Azure first-party opportunities (e.g., MAI, UK Met); OCI as secondary; AWS deprioritized near term.

## Key Information
- MAI contact asked to start testing immediately; functional access may be possible via an existing NeoCloud system, but installation requires pre-certified hardware.
- Current support is pre-certified hardware only; VM support is expected in December and initially limited to small VMs.
- Azure LSV4 is viewed as poor; future VM specs may be strong but are ~1 year out and uncertain versus competitors.
- Avoid exposing non-public Azure BLOB HDD/Flash performance data to third parties (e.g., N-scale).
- Microsoft internal incentives/politics across compute, storage, and networking are sensitive and can create friction.
- Potential Azure hardware engagement path: Ronnie Booker (Azure hardware CVP) ideally via sponsorship from another CVP (e.g., Nidhi; possibly Anand).
- OpenAI is described as the top strategic win; Microsoft right of first refusal reportedly lifted, enabling a multi-cloud data plane approach.
- Jason’s travel is heavy until mid-December; he plans to meet Jeff in San Francisco next week for guidance on priorities.

---

*Source: [[Inbox/Transcripts/2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De.md|2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]]*

## Related

- [[Lior Genzel]]
- [[Jason Vallery]]
- [[Kanchan Mehrotra]]
- [[Ronnie Booker]]
- [[Michael Myrah]]
- [[Cliff Henson]]
- [[Paul Clark]]
- [[Jan Niemus]]
- [[Jonsi Stephenson]]
- [[Jeff Denworth]]
- [[Brendan Burns]]
- [[John Mao]]
- [[Yogev Vankin]]
- [[Neo]]
- [[Cloud control plane]]
- [[Microsoft Azure Engagement Plan]]
- [[Microsoft]]
- [[Google]]
- [[Amazon]]
- [[Oracle]]
- [[CoreWeave]]