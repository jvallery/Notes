---
type: "people"
title: "1:1 with Kanchan Mehrotra: Apollo POC, MAI Dallas storage path, and VAST-on-Azure-storage-hardware strategy"
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

# 1:1 with Kanchan Mehrotra: Apollo POC, MAI Dallas storage path, and VAST-on-Azure-storage-hardware strategy

**Date**: 2025-11-06
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery and Kanchan Mehrotra aligned on how to position VAST Data with Microsoft for Project Apollo and MAI, including an urgent Apollo POC using a shipped VAST rack and a request to run VAST bare metal on Azure storage hardware (DPU options: Fungible or NVIDIA BlueField 3). They discussed political dynamics in Azure Storage, using NVIDIA DGX Cloud storage requirements as leverage, and sequencing outreach through Nidhi and Renan before engaging Michael Myrah on a co-engineered VAST-optimized Azure storage SKU.


## Action Items


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


- Jason Vallery will not contact Michael Myrah directly to avoid premature escalation; Kanchan Mehrotra will open the thread when internal Microsoft alignment is ready (after Nidhi buy-in).

- Primary engagement path is to pursue a unified VAST-on-Azure-storage-hardware story via Azure Storage hardware ownership (Michael Myrah), with Azure Dedicated (Anand) considered as a parallel option if needed.




## Key Information


- VAST Data signed an approximately $1.2B software licensing deal with CoreWeave, publicly announced on 2025-11-06, which Jason Vallery intends to use as proof of VAST platform credibility with Microsoft stakeholders.

- Project Apollo leadership (Chi, CVP of Azure Kubernetes) asked VAST Data for two items: (1) an urgent POC running VAST on VAST hardware in a Microsoft Azure data center, and (2) a POC running VAST bare metal on Azure storage hardware by removing the Azure storage software stack and Windows, installing Linux, and deploying VAST.

- The Apollo POC plan includes drop-shipping a rack of VAST ODM hardware to a Microsoft target data center, and Jason Vallery stated the rack was already shipped and en route as of 2025-11-06.

- Microsoft requested VAST run on next-generation Azure storage hardware that uses Microsoft 1P DPUs, with hardware spec variants including Fungible DPU and NVIDIA BlueField 3 options.

- Kanchan Mehrotra reported a lukewarm reception from Azure Storage members regarding Fungible DPU maturity, based on prior partner testing requests, and she was not confident recommending it without more validation.

- Jason Vallery stated that deploying VAST on Azure storage hardware would likely create political resistance from Azure Storage leadership (Manish), because it implies replacing or bypassing the Azure storage software stack on their hardware.

- Jason Vallery described Azure storage clusters as storage-optimized systems used to run Azure Blob Storage and managed disk software (not general-purpose compute SKUs), designed by Manish's organization and built/delivered by Ronnie's organization.



---

*Source: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]]*