---
type: people
title: VAST–Microsoft alignment on Nebius MAI storage options (file vs Blob, network integration, sizing inputs)
date: '2025-11-20'
participants:
- Jason Vallery
- Lior Genzel
- Bilal (Unknown last name)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-20 - Microsoft (Bilal) and VAST (Jason, Lior) aligned on storage options for MAI’s la.md
tags:
- type/people
- generated
person: Lior Genzel
---

# VAST–Microsoft alignment on Nebius MAI storage options (file vs Blob, network integration, sizing inputs)

**Date**: 2025-11-20
**Attendees**: Jason Vallery, Lior Genzel, Bilal (Unknown last name)

## Summary

Microsoft (Bilal) and VAST (Jason Vallery, Lior Genzel) aligned on storage options for MAI's large-scale Nebius deployment (roughly 100K-120K GPUs). MAI strongly prefers file-based storage with NFS over RDMA and GPU Direct Storage, and Azure Blob has created tooling friction and protocol/performance gaps. Next steps focus on confirming MAI per-GPU throughput and capacity requirements, validating network attachment options (potentially avoiding Sirius overlay), and scheduling a three-way engineering workshop plus early-December site survey participation.

## Action Items

- [?] Debrief MAI on the VAST Data option and validate MAI requirements (file-based posture, per-GPU throughput targets, read/write mix, and capacity requirements) and confirm whether MAI intends to pivot from Azure Blob or supplement it. @Bilal (Unknown last name) 📅 2025-11-20 ⏫ #task #proposed #auto

- [?] Share VAST Data sizing examples, performance and capacity design options, and management/API documentation with Microsoft stakeholders (Bilal and Suresh). @Myself #task #proposed #auto

- [?] Schedule a three-way technical workshop with Microsoft, MAI, and VAST engineering to capture requirements and draft the site design for the Nebius deployment. @Suresh (Unknown last name) #task #proposed #auto

- [?] Confirm Nebius front-end and back-end network topology and determine whether storage can attach to the physical GPU network without Sirius overlay, and document required security and compliance controls. @Suresh (Unknown last name) #task #proposed #auto

- [?] Provide detailed Gen10.3 plan-of-record specifications (rack counts, CX7 NICs, power per rack, usable PB per rack, total Tbps) and clarify Sirius overlay limits relevant to storage attachment. @Bilal (Unknown last name) #task #proposed #auto

- [?] Validate VAST Data supply chain and lead times for a 2026 ramp (flash volumes, compute and data node quantities) and propose tranche sizing aligned to MAI deployment phases. @Myself #task #proposed #auto

- [?] Coordinate VAST Data participation in the early-December 2025 Nebius site survey and align agenda time for storage and network integration review. @Bilal (Unknown last name) #task #proposed #auto

- [?] Decide the deployment model for VAST Data (deploy on Azure storage hardware vs bring qualified VAST ODM hardware) including pros/cons, cost, and performance implications. @Suresh (Unknown last name) #task #proposed #auto

- [?] Draft a rack adjacency and row allocation plan for a VAST Data deployment given constraints across 14 data halls and potential row isolation preferences. @Suresh (Unknown last name) #task #proposed #auto

- [?] Align on deduplication planning assumptions to set effective capacity targets for MAI datasets on VAST Data. @Lior Genzel 🔽 #task #proposed #auto

- [?] Send meeting notes and VAST Data design tables to MAI stakeholders to accelerate requirements confirmation and workshop preparation. @Myself #task #proposed #auto

- [?] Confirm the exact early-December 2025 site survey date, location, and attendee list, and circulate logistics to Microsoft, MAI, and VAST participants. @Bilal (Unknown last name) #task #proposed #auto

- [?] Book an in-person workshop (Redmond or the Nebius site) with Microsoft, MAI, and VAST engineering for requirements and site design deep dive. @Suresh (Unknown last name) #task #proposed #auto

- [?] Introduce Kajan (unknown last name) and other MAI stakeholders into the working email or chat thread and invite them to the three-way workshop. @Bilal (Unknown last name) 🔽 #task #proposed #auto

- [?] Debrief MAI stakeholders on 2025-11-20 about the VAST Data option for Nebius MAI storage and validate file-based posture, per-GPU throughput targets, read/write mix, and capacity requirements, including whether Microsoft should pivot from or supplement the current Azure Blob plan-of-record. @Bilal (Unknown last name) 📅 2025-11-20 ⏫ #task #proposed #auto

- [?] Share VAST Data sizing examples, performance and capacity design options, and management/API documentation with Microsoft contacts (Bilal and Suresh) to enable MAI requirements mapping and solution evaluation. @Myself #task #proposed #auto

- [?] Schedule a three-way technical workshop with Microsoft, MAI engineering, and VAST Data engineering to capture requirements and draft the Nebius site design. @Suresh (Unknown last name) #task #proposed #auto

- [?] Confirm Nebius front-end and back-end network topology and determine whether storage can attach to the physical GPU front-end network without Sirius overlay, and document required security and compliance controls for approval. @Suresh (Unknown last name) #task #proposed #auto

- [?] Provide detailed Gen10.3 plan-of-record specifications for the current Blob-based design, including rack counts, CX7 NIC configuration, power per rack, usable PB per rack, total Tbps targets, and Sirius overlay limits. @Bilal (Unknown last name) #task #proposed #auto

- [?] Decide the deployment model for VAST Data in Nebius MAI, comparing Azure storage hardware versus qualified VAST ODM hardware, including pros/cons, cost, and performance implications. @Suresh (Unknown last name) #task #proposed #auto

- [?] Draft a rack adjacency and row allocation plan for a VAST Data deployment given constraints across 14 data halls and potential early-2026 space limitations. @Suresh (Unknown last name) #task #proposed #auto

- [?] Align on deduplication planning assumptions (expected reduction ratios and dataset characteristics) to set effective capacity targets for MAI datasets on VAST Data. @Lior Genzel 🔽 #task #proposed #auto

- [?] Confirm the exact early-December 2025 site survey date, location, and attendee list, and circulate logistics to Microsoft, MAI, and VAST Data participants. @Bilal (Unknown last name) #task #proposed #auto

- [?] Book an in-person workshop (Redmond or Nebius site) with Microsoft, MAI, and VAST Data engineering teams to finalize requirements and site design decisions. @Suresh (Unknown last name) #task #proposed #auto

- [?] Introduce Kajan (last name unknown) and other MAI stakeholders into the working email or chat thread and invite them to the three-way technical workshop. @Bilal (Unknown last name) 🔽 #task #proposed #auto

## Decisions

- Suresh (unknown last name) will serve as DRI while Bilal (Microsoft) is out of office in early December 2025.

- Proceed with a requirements-first approach for MAI Nebius storage (confirm per-GPU throughput, read/write mix, and capacity), then move into site design and an early-December site survey.

- Suresh (Microsoft, last name unknown) will serve as DRI for the Nebius MAI storage planning workstream while Bilal (Microsoft) is out of office in early December 2025.

- Proceed with a requirements-first approach for Nebius MAI storage (confirm per-GPU throughput, read/write mix, and capacity), then move into site design and an early-December 2025 site survey.

## Key Information

- Bilal (Microsoft) is the current Microsoft point of contact for evaluating VAST Data as a storage option for MAI's Nebius large-scale GPU deployment.

- MAI's Nebius deployment is discussed at a scale of roughly 100,000 to 120,000 GPUs.

- MAI strongly prefers file-based storage access and specifically wants NFS over RDMA and GPU Direct Storage for large-scale training and data access.

- Azure Blob storage has created friction for MAI by forcing tooling refactors and is perceived as lacking required protocol and performance features for this deployment.

- VAST Data supports NFS over RDMA, S3 over RDMA, and GPU Direct Storage, and can tune compute node to data node ratios to meet per-GPU throughput targets.

- Microsoft's plan-of-record for the current Blob-based approach was shared as approximately 1.6 exabytes all-flash across about 400 Gen10.3 racks delivering about 192 Tbps total throughput, with a stated rack power profile around 15 kW per rack and CX7 NICs.

- VAST Data deduplication can increase effective capacity, with an observed example of about 1.7x effective capacity at an MAI cluster (as referenced in the meeting notes).

- VAST Data can integrate with Azure Active Directory and provide a dedicated management plane for the deployment.

- Microsoft is running an internal bake-off comparing VAST Data and Lustre on future Azure hardware.

- A potential cost and complexity reduction was identified if VAST Data can attach to the physical GPU front-end network and avoid the Sirius overlay network gear, pending security and compliance approval.

- Bilal (Microsoft) is expected to be out of office roughly from Wednesday 2025-12-03 through Tuesday 2025-12-16, and Suresh (unknown last name) will act as DRI during that period.

---

- MAI (Microsoft AI Infrastructure) strongly prefers file-based storage access for large-scale GPU deployments, specifically NFS over RDMA and GPU Direct Storage, because Azure Blob has forced tooling refactors and lacks required protocol/performance features for their workflows.

- VAST Data supports NFS over RDMA, S3 over RDMA, and NVIDIA GPU Direct Storage, and can tune compute-node versus data-node ratios to meet per-GPU throughput and capacity targets.

- Microsoft's plan-of-record for the Nebius MAI deployment is approximately 1.6 exabytes of all-flash storage across about 400 Gen10.3 racks, targeting roughly 192 Tbps total throughput, with a rack/power profile around 15 kW per rack and CX7 NICs.

- VAST Data deduplication has shown approximately 1.7x effective capacity improvement in an MAI cluster observation, which can materially change usable capacity planning assumptions for MAI datasets.

- VAST Data can integrate with Azure Active Directory and provide a dedicated management plane for deployments that need enterprise identity and operational separation.

- Bilal (Microsoft) will be out of office roughly from 2025-12-03 to 2025-12-16, and Suresh (Microsoft, last name unknown) will act as DRI during that period.

- An internal Microsoft bake-off comparing VAST Data and Lustre on future Azure hardware is underway to evaluate performance and fit for MAI-like workloads.

- VAST Data is not currently an Azure hardware provider, and an Azure Marketplace approach using LSv4 is not viable for the Nebius MAI scale discussed.

- A potential cost and complexity reduction exists if VAST Data storage can attach directly to the physical GPU front-end network, which could avoid the Sirius overlay network gear, pending Microsoft security and compliance approval.
