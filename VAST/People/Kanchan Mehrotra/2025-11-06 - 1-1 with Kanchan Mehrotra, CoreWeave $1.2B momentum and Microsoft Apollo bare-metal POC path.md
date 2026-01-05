---
type: "people"
title: "1:1 with Kanchan Mehrotra, CoreWeave $1.2B momentum and Microsoft Apollo bare-metal POC path"
date: "2025-11-06"
person: ""
participants: ["Jason Vallery", "Kanchan Mehrotra"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Kanchan Mehrotra, CoreWeave $1.2B momentum and Microsoft Apollo bare-metal POC path

**Date**: 2025-11-06
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery shared VAST Data momentum including a ~$1.2B software licensing deal with CoreWeave and discussed Microsoft Project Apollo requests: a VAST hardware rack POC shipped to an Azure datacenter and a request to run VAST bare metal on Azure Storage hardware (DPU options include Fungible and NVIDIA BlueField 3). Jason and Kanchan aligned on using MAI Dallas capacity timing and NVIDIA DGX Cloud storage requirements as leverage, while navigating Azure Storage political dynamics and sequencing engagement through Nidhi, Renan, and later Michael Myrah.


## Action Items


- [?] Share the CoreWeave ~$1.2B VAST Data software licensing deal press link internally within the Microsoft/Azure stakeholder set where helpful to build confidence in VAST. @Myself #task #proposed #auto

- [?] Confirm status and ETA of the VAST hardware rack shipment to the Microsoft target datacenter for the Project Apollo POC and track progress to first benchmarks. @Myself ⏫ #task #proposed #auto

- [?] Clarify with Microsoft Apollo stakeholders the exact Azure Storage hardware spec variants for the bare-metal POC, including whether the DPU choice is Fungible or NVIDIA BlueField 3, and what success criteria and benchmarking plan will be used. @Myself ⏫ #task #proposed #auto

- [?] Collect additional signal from Azure Storage members on Fungible DPU production readiness and prior partner experiences to inform VAST's recommendation for the Apollo bare-metal POC. @Kanchan Mehrotra ⏫ #task #proposed #auto




## Decisions


- Sequence engagement so that Kanchan Mehrotra socializes the VAST-on-Azure-Storage bare-metal story internally (including with Nidhi and Renan) before Jason Vallery engages Michael Myrah on co-engineering a VAST-optimized Azure storage SKU.




## Key Information


- VAST Data signed a ~$1.2B software licensing deal with CoreWeave, which Jason Vallery described as transformational and a strong trust signal for VAST's platform.

- CoreWeave entered into a ~$1.2B software licensing deal with VAST Data, indicating CoreWeave is making a major platform bet on VAST.

- Microsoft Project Apollo leadership requested two items from VAST Data: (1) an urgent POC running VAST on VAST hardware in a Microsoft target datacenter, and (2) a POC running VAST bare metal on Azure Storage hardware by removing the Azure storage software stack and Windows and installing Linux plus VAST.

- The Azure Storage hardware POC request includes next-generation Azure Storage hardware specifications with DPU options, including Microsoft 1P Fungible DPUs and an alternative spec that includes NVIDIA BlueField 3.

- Kanchan Mehrotra reported receiving a lukewarm reception from Azure Storage members when asking about Fungible DPU maturity, and she was unsure she could recommend it based on that feedback.

- Jason Vallery stated that running VAST bare metal on Azure Storage hardware would likely create political friction with Azure Storage leadership (Manish Sah), because it implies replacing the Azure Storage software stack on their hardware.

- Jason Vallery described Azure Storage clusters as storage-optimized hardware used to run Azure Blob Storage and managed disk software, rather than general-purpose compute SKUs.



---

*Source: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]]*