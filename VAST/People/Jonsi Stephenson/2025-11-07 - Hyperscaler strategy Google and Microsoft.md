---
type: people
title: 'Hyperscaler strategy: Google and Microsoft'
date: '2025-11-07'
person: Jonsi Stephenson
participants:
- Myself
- Jonsi Stephenson
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-07 - We aligned on hyperscaler strategy
  across Google and Microsoft. On Google, GDC i.md
tags:
- type/customer
- account/jonsi-stephenson
- generated
---

# Hyperscaler strategy: Google and Microsoft

**Date**: 2025-11-07
**Account**: [[Jonsi Stephenson]]
**Attendees**: Myself, Jonsi Stephenson

## Summary

Aligned on hyperscaler strategy across Google and Microsoft. For Google, Google Distributed Cloud (GDC) is emerging as the on-prem TPU vehicle, with VAST and NetApp as the only viable file options; VAST real-workload TPU benchmarks reportedly outperformed Google’s managed Lustre by ~20% and a cross-region global namespace demo resonated. For Microsoft, Project Apollo is a new Linux/Kubernetes control plane for supercomputers with MAI as first tenant; LSVx VMs are not viable at scale, pushing toward running VAST on Azure Storage hardware, with MAI’s April Falcon build (120k GPUs in Dallas) at risk if storage underperforms; marketplace listing remains a key checkbox and a simplified cloud pricing unit (managed vCPU+capacity) is being pursued.
## Action Items
- [ ?] Share TPU benchmark write-up and numbers for upcoming Google meetings @Jonsi Stephenson 📅 2025-11-14 ⏫ #task #proposed
- [ ?] Attend pricing model meeting @Myself 📅 2025-11-10 ⏫ #task #proposed
- [ ?] Attend Google Distributed Cloud team meeting @Myself 📅 2025-11-14 ⏫ #task #proposed
- [ ?] Join Google Distributed Cloud leadership sessions remotely @Jonsi Stephenson 📅 2025-11-13 #task #proposed

## Decisions
- Pursue deeper integration with Google Distributed Cloud and aim to be part of the GDC SKU.
- Treat Microsoft Azure as a distinct sell-to motion (first-party/Azure Storage HW) separate from marketplace sell-through.
- Use real-workload benchmarks (not synthetic) as the standard for TPU/storage evaluations with Google.

## Key Information
- Google Distributed Cloud is the likely vehicle for on-prem TPU deployments and tie-back to GCP.
- Only VAST and NetApp are present on GDC; NetApp relies on revived OnTap Select.
- VAST TPU testing using Google’s model set reportedly showed ~20% improvement over Google’s managed Lustre stack.
- A cross-region global namespace demo (Japan↔Ohio) resonated with Google stakeholders.
- Two Sigma is adopting Google TPUs on-prem for training and plans inferencing on GCP; they want VAST via Google Marketplace and are behind on cloud commits.
- Microsoft Project Apollo is a new Linux/Kubernetes control plane for supercomputers; first production DC targeted ~1 year out; MAI is first tenant.
- Azure LSVx VMs are not viable for exabyte-scale or large GPU clusters; Azure Storage hardware path is preferred.
- MAI Falcon build targets ~120k GPUs in April in Dallas and is at risk of storage bottlenecks; exploring VAST on Azure Storage hardware/software swap.
- Marketplace listing is a required checkbox for Microsoft stakeholders.
- Leadership concern that current cloud pricing may be uncompetitive; a managed unit (vCPU+capacity) is being pursued.

---

*Source: [[Inbox/Transcripts/2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i.md|2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]]*

## Related

- [[Kanchan Mehrotra]]
- [[Michael Myrah]]
- [[Qi Ke]]
- [[Brendan Burns]]
- [[Jai Menon]]
- [[Tiffany Stonehill]]
- [[Olivia Bouree]]
- [[Jeff Yonker]]
- [[Ronen Cohen]]
- [[Eric Wolfie]]
- [[Mike Requa]]
- [[Sam Hopewell]]
- [[Jack Kabat]]
- [[Google Distributed Cloud RFP]]
- [[Google]]
- [[Microsoft]]
- [[NetApp]]