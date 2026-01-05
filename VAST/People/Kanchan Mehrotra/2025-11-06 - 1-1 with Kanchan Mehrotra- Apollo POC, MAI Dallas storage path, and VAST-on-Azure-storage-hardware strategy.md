---
type: people
title: '1:1 with Kanchan Mehrotra: Apollo POC, MAI Dallas storage path, and VAST-on-Azure-storage-hardware strategy'
date: '2025-11-06'
person: Kanchan Mehrotra
participants:
- Jason Vallery
- Kanchan Mehrotra
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A.md
tags:
- type/people
- generated
---

# 1:1 with Kanchan Mehrotra: Apollo POC, MAI Dallas storage path, and VAST-on-Azure-storage-hardware strategy

**Date**: 2025-11-06
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery shared VAST Data momentum including a ~$1.2B software licensing deal with CoreWeave and discussed Microsoft Project Apollo requests: a VAST hardware rack POC shipped to an Azure datacenter and a request to run VAST bare metal on Azure Storage hardware (DPU options include Fungible and NVIDIA BlueField 3). Jason and Kanchan aligned on using MAI Dallas capacity timing and NVIDIA DGX Cloud storage requirements as leverage, while navigating Azure Storage political dynamics and sequencing engagement through Nidhi, Renan, and later Michael Myrah.

## Action Items

- [?] Share the CoreWeave ~$1.2B VAST Data software licensing deal press link internally within the Microsoft/Azure stakeholder set where helpful to build confidence in VAST. @Myself #task #proposed #auto

- [?] Confirm status and ETA of the VAST hardware rack shipment to the Microsoft target datacenter for the Project Apollo POC and track progress to first benchmarks. @Myself ⏫ #task #proposed #auto

- [?] Clarify with Microsoft Apollo stakeholders the exact Azure Storage hardware spec variants for the bare-metal POC, including whether the DPU choice is Fungible or NVIDIA BlueField 3, and what success criteria and benchmarking plan will be used. @Myself ⏫ #task #proposed #auto

- [?] Collect additional signal from Azure Storage members on Fungible DPU production readiness and prior partner experiences to inform VAST's recommendation for the Apollo bare-metal POC. @Kanchan Mehrotra ⏫ #task #proposed #auto

- [?] Reach out to Kushal Bhatta to assess MAI’s appetite for using VAST Data as storage for MAI Dallas, especially the April tranche, and clarify the current plan-of-record (POR) hardware. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Seed the VAST-on-Azure-storage-hardware bare-metal strategy with Nidhi and secure a meeting that includes Renan to align on engagement model and licensing approach. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate with Lior Genzel and Renan to request and prepare for an executive meeting with Nidhi (timed pre- or post-Microsoft Ignite) to align on the VAST-on-Azure-storage-hardware story and next steps. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Ask the Azure Storage team whether they have received NVIDIA DGX Cloud storage performance requirements and whether any related benchmarking requests have been made for Azure Storage. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Draft a plan for running VAST bare metal on classic Azure, including Overlake/SDN interoperability and networking requirements, contingent on MAI greenlight for MAI Dallas. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Finalize and circulate the exabyte-scale cost, power, and performance comparison slide to support executive discussions about why VAST must run on Azure storage hardware rather than LSv4/LSv5 compute SKUs. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Open a conversation with Michael Myrah about co-developing a VAST-optimized Azure storage SKU after securing Nidhi’s support for the approach. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Explore Azure Dedicated (Anand) as a parallel path for bare-metal deployment if the Azure Storage hardware path becomes blocked. @Kanchan Mehrotra 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Track Apollo POC progress, including rack arrival at the Azure data center, progress running VAST on Azure storage hardware, and the DPU selection decision between Fungible and NVIDIA BlueField 3. @Myself 📅 2025-11-08 #task #proposed #auto

## Decisions

- Sequence engagement so that Kanchan Mehrotra socializes the VAST-on-Azure-Storage bare-metal story internally (including with Nidhi and Renan) before Jason Vallery engages Michael Myrah on co-engineering a VAST-optimized Azure storage SKU.

- Jason Vallery will not contact Michael Myrah directly to avoid premature escalation; Kanchan Mehrotra will open the thread when internal Microsoft alignment is ready (after Nidhi buy-in).

- Primary engagement path is to pursue a unified VAST-on-Azure-storage-hardware story via Azure Storage hardware ownership (Michael Myrah), with Azure Dedicated (Anand) considered as a parallel option if needed.

## Key Information

- VAST Data signed a ~$1.2B software licensing deal with CoreWeave, which Jason Vallery described as transformational and a strong trust signal for VAST's platform.

- CoreWeave entered into a ~$1.2B software licensing deal with VAST Data, indicating CoreWeave is making a major platform bet on VAST.

- Microsoft Project Apollo leadership requested two items from VAST Data: (1) an urgent POC running VAST on VAST hardware in a Microsoft target datacenter, and (2) a POC running VAST bare metal on Azure Storage hardware by removing the Azure storage software stack and Windows and installing Linux plus VAST.

- The Azure Storage hardware POC request includes next-generation Azure Storage hardware specifications with DPU options, including Microsoft 1P Fungible DPUs and an alternative spec that includes NVIDIA BlueField 3.

- Kanchan Mehrotra reported receiving a lukewarm reception from Azure Storage members when asking about Fungible DPU maturity, and she was unsure she could recommend it based on that feedback.

- Jason Vallery stated that running VAST bare metal on Azure Storage hardware would likely create political friction with Azure Storage leadership (Manish Sah), because it implies replacing the Azure Storage software stack on their hardware.

- Jason Vallery described Azure Storage clusters as storage-optimized hardware used to run Azure Blob Storage and managed disk software, rather than general-purpose compute SKUs.

---

- VAST Data signed an approximately $1.2B software licensing deal with CoreWeave, publicly announced on 2025-11-06, which Jason Vallery intends to use as proof of VAST platform credibility with Microsoft stakeholders.

- Project Apollo leadership (Chi, CVP of Azure Kubernetes) asked VAST Data for two items: (1) an urgent POC running VAST on VAST hardware in a Microsoft Azure data center, and (2) a POC running VAST bare metal on Azure storage hardware by removing the Azure storage software stack and Windows, installing Linux, and deploying VAST.

- The Apollo POC plan includes drop-shipping a rack of VAST ODM hardware to a Microsoft target data center, and Jason Vallery stated the rack was already shipped and en route as of 2025-11-06.

- Microsoft requested VAST run on next-generation Azure storage hardware that uses Microsoft 1P DPUs, with hardware spec variants including Fungible DPU and NVIDIA BlueField 3 options.

- Kanchan Mehrotra reported a lukewarm reception from Azure Storage members regarding Fungible DPU maturity, based on prior partner testing requests, and she was not confident recommending it without more validation.

- Jason Vallery stated that deploying VAST on Azure storage hardware would likely create political resistance from Azure Storage leadership (Manish), because it implies replacing or bypassing the Azure storage software stack on their hardware.

- Jason Vallery described Azure storage clusters as storage-optimized systems used to run Azure Blob Storage and managed disk software (not general-purpose compute SKUs), designed by Manish's organization and built/delivered by Ronnie's organization.
