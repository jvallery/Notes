---
type: "customer"
title: "Azure Managed Lustre architecture, scaling, and pricing comparison vs VAST Azure offering"
date: "2025-10-31"
account: ""
participants: ["Jason Vallery", "Lior Genzel", "Wolfgang"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Discussion comparing Azure Managed Lustre architecture, scaling, and pricing wit.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Azure Managed Lustre architecture, scaling, and pricing comparison vs VAST Azure offering

**Date**: 2025-10-31
**Account**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Wolfgang

## Summary

Jason Vallery, Lior Genzel, and a Microsoft participant (likely Wolfgang) compared Azure Managed Lustre architecture, scaling model, and pricing against VAST Data’s planned Azure offering. The discussion covered Managed Lustre tiers and increments, Premium Disk backing, Availability Zone pinning, asynchronous Blob offload via Lustre HSM, resiliency characteristics, and open items around RDMA, VMSS Flex fault domains, and Azure VM SKU pricing for L192/LSv5.


## Action Items


- [?] Deliver Terraform scripts for the VAST Data Azure POC deployment. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define a backup and recovery strategy for VAST Data on Azure, including target RPO/RTO, snapshot/offload approach, and rehydration process. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm whether Azure Managed Lustre supports Premium Disk v2 (Direct Drive) and share any timeline guidance. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Coordinate the timeline for guest RDMA between Azure VMs and assess implications for Azure Managed Lustre clients and VAST Data performance roadmap (Boost and Overlake teams). @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Hold a roadmap discussion with the VMSS Flex team (including Jerry Steele’s team) on fault domains and LSv5 readiness for VAST Data’s Azure offering. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Obtain and share Azure VM SKU pricing and availability guidance for L192 and LSv5 to inform cost comparisons between Azure Managed Lustre and VAST Data on Azure. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Schedule a Supercomputing conference meetup and add Jason Vallery to the existing session with Lior Genzel. @Lior Genzel 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Document current Availability Zone pinning and locality guarantees for Azure Managed Disks and Azure Managed Lustre VMs. @TBD 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Assess feasibility to expose Lustre HSM state and automation hooks so users can programmatically determine when Blob offload/archive completion has finished. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Advance Azure Marketplace listing work for VAST Data toward the February 2026 GA target. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Share detailed Azure Managed Lustre tier and increment documentation plus performance tuning notes with Jason Vallery. @Wolfgang 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm Supercomputing conference booth and meeting logistics and share details with Jason Vallery and Lior Genzel. @Wolfgang 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Track Lifter and Azure-native VAST milestones and SaaS architecture decisions for the Azure offering. @Myself 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- VAST Data will use currently available Azure VM SKUs for the initial VAST on Azure release, accepting initial performance limits (for example, 40 Gbps NIC constraints) until higher-performance options are available.

- VAST Data will target an early December 2025 delivery of Terraform-based POC deployment artifacts for the initial VAST on Azure approach.

- VAST Data will target February 2026 for Azure Marketplace GA for the initial VAST Azure offering, with a later follow-on path toward a more Azure-native or Lifter SaaS approach.

- VAST Data’s SaaS control plane approach for Azure will run in a VAST-owned tenant and expose endpoints into customer tenants.




## Key Information


- Azure Managed Lustre has four service tiers named 500, 250, 125, and 40, where the number represents throughput in MB/s per TB provisioned.

- Azure Managed Lustre tiering is designed so MLS 500 is the cheapest way to hit a bandwidth target, while MLS 40 is the cheapest way to hit a capacity target, similar to AWS FSx for Lustre tiering rationale.

- Azure Managed Lustre provisioning uses incremental units; an example given was 4 TB steps that provide about 2 GB/s per increment.

- A Microsoft participant (Wolfgang, Azure Managed Lustre) stated he would only share information that is published or clearly allowed, and would cross-validate anything potentially confidential with an engineering manager.

- Lior Genzel stated VAST Data is exploring use of persistent storage on Azure as part of its solution design and wants to learn Managed Lustre best practices for VAST’s next-generation Azure offering.



---

*Source: [[2025-10-31 - Discussion comparing Azure Managed Lustre architecture, scaling, and pricing wit]]*