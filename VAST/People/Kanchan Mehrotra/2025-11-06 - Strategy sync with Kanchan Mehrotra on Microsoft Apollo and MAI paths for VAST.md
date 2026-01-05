---
type: "people"
title: "Strategy sync with Kanchan Mehrotra on Microsoft Apollo and MAI paths for VAST"
date: "2025-11-06"
person: ""
participants: ["Jason Vallery", "Kanchan Mehrotra"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# Strategy sync with Kanchan Mehrotra on Microsoft Apollo and MAI paths for VAST

**Date**: 2025-11-06
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery and Kanchan Mehrotra aligned on accelerating VAST adoption inside Microsoft via Project Apollo and Microsoft AI Infrastructure (MAI), with emphasis on a hardware-led, bare-metal VAST path on Azure storage hardware rather than VM-based deployments. They discussed Apollo-requested POCs, risks around Fungible DPU readiness and internal politics, and using NVIDIA DGX Cloud reference storage requirements as executive leverage to secure leadership support and engage Azure Storage Hardware leadership.


## Action Items


- [?] Circle with Lior Genzel on framing the executive session with Microsoft leadership (Nidhi and Renan), emphasizing NVIDIA DGX Cloud reference storage requirements and the VAST bare-metal on Azure storage hardware path. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Track status of the Apollo urgent POC hardware shipment and the start of VAST testing in the target Microsoft Azure data center for the VAST-on-VAST hardware POC. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Reach out to Kushal (Microsoft contact, last name not provided) to gauge willingness for MAI to sponsor pushing VAST bare metal on classic Azure for Dallas capacity tranches and align next steps. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Quietly brief Nidhi (Microsoft leader, last name not provided) on the VAST-optimized Azure storage hardware path and secure support before engaging Azure Storage Hardware leadership. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] If Nidhi supports, coordinate an introduction with Michael Myrah (Azure Storage Hardware) to discuss co-designing a VAST-optimized Azure storage SKU for running VAST bare metal on Azure storage hardware. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Ask the Azure Storage team whether NVIDIA has requested DGX storage benchmarking or compliance validation and relay findings back to the working group. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Confirm Nidhi availability and schedule a focused deep-dive session with Renan, Lior Genzel, and VAST leadership (potentially around Microsoft Ignite or in a dedicated Redmond session). @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide an update after the Kushal conversation on whether MAI will sponsor the Dallas classic-Azure VAST exploration for the December and April capacity tranches. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto




## Decisions


- Prioritize exploring a hardware-led path for VAST on Azure storage hardware (bare metal) as the primary approach for Apollo and MAI needs, rather than relying on VM-based deployments for performance and scale.




## Key Information


- VAST Data signed an approximately $1.2B software-only licensing deal with CoreWeave, announced publicly on 2025-11-06, which Jason Vallery positioned as a confidence signal for Microsoft partnership discussions.

- Project Apollo leadership (introduced to VAST by a Microsoft CVP, name unclear in transcript) requested two proofs of concept from VAST Data: (1) an urgent VAST-on-VAST hardware POC using a rack of VAST ODM hardware shipped to a Microsoft target data center, and (2) a POC to run VAST bare metal on Azure storage hardware by removing the Azure storage software stack and Windows and installing Linux plus VAST.

- The Azure storage hardware stack discussed for the Apollo bare-metal POC includes Microsoft first-party DPUs and Fungible NICs, and the intent is to benchmark VAST running directly on Azure storage hardware.

- Jason Vallery stated that Azure storage-optimized clusters used for Blob Storage and Managed Disks are designed by Manish Sah's organization and built and delivered by Ronnie Booker's organization, and that asking to replace the Azure storage software stack with VAST could create internal political resistance.



---

*Source: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]]*