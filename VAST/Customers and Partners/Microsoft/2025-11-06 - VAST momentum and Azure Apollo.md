---
type: customer
title: VAST momentum and Azure Apollo
date: '2025-11-06'
account: Microsoft
participants:
- Kanchan Mehrotra
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-06 - Jason shared VAST’s momentum (CoreWeave
  $1.2B deal) and updates on Microsoft’s A.md
tags:
- type/customer
- account/microsoft
- generated
---

# VAST momentum and Azure Apollo

**Date**: 2025-11-06
**Account**: [[Microsoft]]
**Attendees**: Kanchan Mehrotra, Jason Vallery

## Summary

Jason and Kanchan discussed VAST’s momentum (including a ~$1.2B CoreWeave software license) and Microsoft Azure Apollo requests: an urgent VAST-on-VAST-hardware POC rack shipment and a POC to run VAST bare metal on Azure Storage hardware (Fungible DPU vs NVIDIA BlueField 3). They aligned on navigating Azure Storage political dynamics, using NVIDIA DGX Cloud storage requirements as leverage, and sequencing outreach: validate MAI Dallas appetite with Kushal, seed the story with Nidhi, then engage Michael Myrah and pursue an exec meeting including Renan.
## Action Items
- [ ] Reach out to Kushal Bhatta to assess MAI’s appetite for VAST as storage for Dallas (especially April) and clarify current plan-of-record hardware. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task
- [ ] Seed the VAST-on-Azure-storage bare-metal strategy with Nidhi and secure a meeting including Renan. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task
- [ ] Coordinate with Lior and Renan to request/prepare for an exec meeting with Nidhi (pre/post Ignite). @Myself 📅 2025-11-08 ⏫ #task
- [ ] Ask Azure Storage team whether they have received NVIDIA DGX storage performance requirements and whether any storage benchmarking has been requested. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task
- [ ] Draft a plan for running VAST bare metal on classic Azure, including Overlake/SDN interoperability and networking approach, pending MAI greenlight. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Finalize and circulate the exabyte cost/power/performance comparison slide for exec discussions. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Open a conversation with Michael Myrah about co-engineering a VAST-optimized Azure Storage hardware SKU after securing Nidhi’s support. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task
- [ ] Explore Azure Dedicated (Anand) as a parallel bare-metal path if needed. @Kanchan Mehrotra 📅 2025-11-08 🔽 #task
- [ ] Track Apollo POC progress (rack arrival, VAST on Azure storage hardware, and DPU choice between Fungible and BlueField 3). @Myself 📅 2025-11-08 ⏫ #task
- [ ] Schedule and confirm the meeting with Nidhi and Renan; align on engagement model and licensing approach. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task

## Decisions
- Jason will not contact Michael Myrah directly to avoid premature escalation; Kanchan will open that thread when appropriate.
- Primary path is through Azure Storage hardware (Myrah) for a single unified story; Azure Dedicated (Anand) is a parallel option if needed.

## Key Information
- VAST signed a ~$1.2B software licensing deal with CoreWeave.
- Azure Apollo leadership requested (1) an urgent POC running VAST on VAST hardware (rack shipped to an Azure DC) and (2) a POC running VAST bare metal on Azure Storage hardware.
- Azure Storage hardware spec options for the POC include Fungible DPU and NVIDIA BlueField 3; Fungible maturity is viewed as a risk with no production storage tenants using it yet.
- MAI is Apollo’s first customer; near-term MAI Dallas capacity includes an initial tranche in December and a larger tranche in April, with April storage plan still fluid.
- To support MAI Dallas on classic Azure (not Apollo), VAST would need to run bare metal on Azure Storage hardware and interoperate with Overlake/SDN.
- UK Met Office is exploring a POC with VAST hardware in an Azure Canary region.
- NVIDIA DGX Cloud storage requirements are aggressive; VAST and Weka are qualified while Azure Storage is perceived to lag current specs.
- VAST prefers an all-you-can-eat enterprise license model with Microsoft rather than per-capacity deals.
- Political resistance from Azure Storage leadership (Manish) is a key risk; exec alignment (Ignite timing) may affect scheduling.

---

*Source: [[Inbox/_archive/2025-11-06/2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A.md|2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]]*

## Related

- [[CoreWeave]]
- [[Google]]
- [[Kanchan Mehrotra]]
- [[Jason Vallery]]
- [[Michael Myrah]]
- [[Lior Genzel]]
- [[Jay Parikh]]
- [[Jason Taylor]]
- [[Jeff Denworth]]
- [[John Lee]]
- [[Mike Requa]]
- [[OpenAI VAST POC - CoreWeave Cluster]]
- [[Microsoft Azure Engagement Plan]]
- [[Neo]]
- [[Enscale deck]]
