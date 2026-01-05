---
type: customer
title: Azure Managed Lustre vs VAST
date: '2025-10-31'
account: Microsoft
participants:
- Jason Vallery
- Lior Genzel
- Wolfgang
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-31 - Discussion comparing Azure Managed
  Lustre architecture, scaling, and pricing wit.md
tags:
- type/customer
- account/microsoft
- generated
---

# Azure Managed Lustre vs VAST

**Date**: 2025-10-31
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Lior Genzel, Wolfgang

## Summary

The group compared Azure Managed Lustre’s architecture, scaling limits, resiliency characteristics, and pricing against VAST’s planned Azure offering. Key discussion points included Lustre performance/capacity tiers, Premium Disk v1 persistence requirements, AZ pinning, asynchronous Blob offload via HSM (no strong consistency), and the RDMA/VM roadmap constraints impacting AI workload performance and availability. They aligned on next steps around RDMA timelines, VMSS Flex/fault-domain changes, and meeting at Supercomputing, while VAST confirmed near-term delivery targets for a Terraform-based POC and Marketplace GA.
## Action Items
- [?] Deliver Terraform scripts for VAST Azure POC @TBD 📅 2025-11-08 🔺 #task #proposed
- [?] Define backup/recovery strategy for VAST on Azure (RPO/RTO, snapshot/offload, rehydration) @TBD 📅 2025-11-08 ⏫ #task #proposed
- [?] Confirm whether Azure Managed Lustre supports Premium Disk v2 (Direct Drive) and share timelines @TBD 📅 2025-11-08 ⏫ #task #proposed
- [?] Coordinate guest RDMA enablement timeline between VMs and implications for Lustre/VAST @TBD 📅 2025-11-08 🔺 #task #proposed
- [?] Hold roadmap discussion with VMSS Flex/Jerry Steele’s team on fault domains and Lsv5 readiness @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Share SKU pricing/availability guidance for L192/Lsv5 to inform cost comparisons @TBD 📅 2025-11-08 ⏫ #task #proposed
- [?] Schedule Supercomputing meetup and add Jason to existing session @Lior Genzel 📅 2025-11-08 🔽 #task #proposed
- [?] Document current AZ pinning/locality guarantees for Managed Disks and Lustre VMs @TBD 📅 2025-11-08 🔽 #task #proposed
- [?] Assess feasibility to expose HSM state/automation hooks for users waiting on Blob archive completion @TBD 📅 2025-11-08 ⏫ #task #proposed
- [?] Advance Marketplace listing work toward February GA @TBD 📅 2025-11-08 ⏫ #task #proposed
- [?] Share detailed tier/increment documentation and performance tuning notes with Jason @Wolfgang 📅 2025-11-08 🔽 #task #proposed
- [?] Provide update on Blob HSM enhancements preserving directory hierarchy and any roadmap changes @TBD 📅 2025-11-08 🔽 #task #proposed
- [?] Confirm dates/logistics for Supercomputing booth and meetings @Wolfgang 📅 2025-11-08 🔽 #task #proposed
- [?] Track Lifter/Azure-native VAST milestones and SaaS architecture decisions @TBD 📅 2025-11-08 🔽 #task #proposed

## Decisions
- VAST will proceed using currently available VM SKUs for the initial Azure release even if limited to 40 Gbps.
- Target POC/Terraform deliverable in early December.
- Marketplace GA target is February; Azure-native/Lifter path targeted later (tentatively Q3).
- VAST SaaS control plane will run in a VAST-owned tenant exposing endpoints into customer tenants.
- Azure Managed Lustre remains persistence-only (no ephemeral), Premium Disk v1, AZ-pinned; Blob offload stays asynchronous.

## Key Information
- Azure Managed Lustre tiers provide 500/250/125/40 MB/s per TB; 500 is bandwidth-optimized and 40 is capacity-optimized.
- Provisioning increments yield ~2 GB/s per increment; tier differences are driven by attached disk counts per OSS.
- Azure Managed Lustre is backed by Premium LRS Managed Disks (v1 today) and does not support an ephemeral deployment mode.
- Availability Zone selection is mandatory; VMs and disks are pinned to a single AZ with no lower-level placement control discussed.
- Azure Managed Lustre scales to ~12.5 PB on MLS 40 today, with higher targets planned.
- Blob integration uses Lustre HSM and is asynchronous; it can preserve directory hierarchy in Blob.
- Strong consistency (write-through to Blob before close/ack) is not supported; HSM state can be checked per file to confirm archive completion.
- Loss of MDS/MGS makes the filesystem unavailable; OSS loss degrades performance but I/O can continue.
- Managed Lustre was modeled as ~30–40% cheaper than VAST on L96 v4 (license excluded); L192/Lsv5 pricing was unknown at the time.
- Guest RDMA between VMs is not broadly available yet; enablement is under discussion with Boost/Overlake teams.
- AWS offers an ephemeral Lustre tier; Azure Managed Lustre does not.
- VAST initial Azure approach uses available VMs; performance is bounded by NIC (e.g., 40 Gbps).

---

*Source: [[Inbox/_archive/2025-10-31/2025-10-31 - Discussion comparing Azure Managed Lustre architecture, scaling, and pricing wit.md|2025-10-31 - Discussion comparing Azure Managed Lustre architecture, scaling, and pricing wit]]*

## Related

- [[Jason Vallery]]
- [[Lior Genzel]]
- [[Cloud control plane]]
- [[Amazon]]
- [[Google]]
- [[HPE]]