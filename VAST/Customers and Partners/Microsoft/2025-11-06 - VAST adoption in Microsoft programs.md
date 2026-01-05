---
type: customer
title: VAST adoption in Microsoft programs
date: '2025-11-06'
account: Microsoft
participants:
- Myself
- Kanchan Mehrotra
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-06 - Discussion centered on accelerating
  VAST adoption within Microsoft programs (MAI.md
tags:
- type/customer
- account/microsoft
- generated
---

# VAST adoption in Microsoft programs

**Date**: 2025-11-06
**Account**: [[Microsoft]]
**Attendees**: Myself, Kanchan Mehrotra

## Summary

Discussion focused on accelerating VAST adoption inside Microsoft via Apollo and MAI, including two Apollo-requested POCs (VAST-on-VAST hardware and VAST bare metal on Azure storage hardware). Key risks included Fungible DPU readiness and internal political resistance, while NVIDIA DGX Cloud storage requirements were identified as leverage to justify a hardware-led, bare-metal VAST path. Next steps centered on discreetly aligning leadership (Nidhi/Renan) before engaging Azure Storage Hardware (Michael Myrah) and gauging MAI sponsorship (Kushal) for a Dallas timeline.
## Action Items
- [ ?] Reach out to Kushal to gauge willingness to push VAST bare metal on classic Azure for Dallas and align next steps. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Quietly brief Nidhi on the VAST-optimized Azure storage hardware path and secure her support. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed
- [ ?] If Nidhi aligns, coordinate an intro with Michael Myrah to discuss a co-designed VAST-optimized Azure storage SKU. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Ask Azure Storage team if NVIDIA has requested DGX storage benchmarking/compliance and relay findings. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed
- [ ?] Circle with Lior on framing the Nidhi/Renan session, emphasizing DGX storage requirements and bare-metal path. @Myself 📅 2025-11-08 #task #proposed
- [ ?] Confirm Nidhi’s availability and schedule a focused deep-dive with Renan/Lior and VAST leadership. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Update on Kushal conversation and whether MAI will sponsor the Dallas classic-Azure VAST exploration. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Track status of Apollo POC hardware arrival and start of VAST testing in the target Azure data center. @Myself 📅 2025-11-08 #task #proposed

## Decisions
- Prioritize a storage-hardware path (Azure Storage Hardware / Myrah’s team) over VM-based approaches for VAST performance and scale.
- Use MAI-driven demand (via Kushal) to advance the Dallas April window for a VAST bare-metal option.
- Position NVIDIA DGX reference storage compliance as strategic justification in executive conversations.
- Avoid engaging Michael Myrah directly until Nidhi’s support is secured.

## Key Information
- VAST signed an approximately $1.2B software-only licensing deal with CoreWeave (press released the same day as the meeting).
- Apollo requested two POCs: (1) urgent VAST-on-VAST hardware (rack drop-shipped to a Microsoft data center) and (2) VAST bare metal on Azure storage hardware (removing Azure storage stack/Windows, running Linux + VAST).
- Azure storage hardware spec variants discussed include Fungible DPU and NVIDIA BlueField-3; Fungible production readiness in Azure storage is uncertain and considered a risk.
- MAI is the initial single-tenant customer for Apollo; longer-term vision is multi-tenant/third-party offering.
- MAI Dallas capacity tranches are expected in December and April; April storage plan is not finalized and could be a window for VAST on classic Azure (Overlake/SDN integration).
- NVIDIA DGX Cloud reference storage requirements reportedly only met today by VAST and Weka; Azure Storage is far from those performance targets.
- VAST is open to an all-you-can-eat software license model for Microsoft.
- Proposed approach: co-engineer a VAST-optimized Azure storage SKU with Azure Storage Hardware (Michael Myrah) with leadership air cover (Nidhi/Renan).

---

*Source: [[Inbox/_archive/2025-11-06/2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI.md|2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]]*

## Related

- [[CoreWeave]]
- [[NVIDIA]]
- [[Kanchan Mehrotra]]
- [[Michael Myrah]]
- [[Lior Genzel]]
- [[Maneesh Sah]]
- [[Jay Parikh]]
- [[Jason Taylor]]
- [[Jeff Denworth]]
- [[John Lee]]
- [[Apollo]]
- [[Cloud control plane]]
- [[Microsoft Azure Engagement Plan]]
- [[Enscale deck]]
- [[OpenAI VAST POC - CoreWeave Cluster]]