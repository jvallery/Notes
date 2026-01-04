---
type: projects
title: Cloud
last_contact: unknown
created: '2026-01-03'
tags:
- type/projects
- generated
---

# Cloud

## Recent Context

- unknown: [[2025-10 - Google Tasks]] - Task to confirm Google Cloud Platform GA timing after a bottleneck fix and align on the first 2–3 li... (via Google)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams coordinated a response to Google Distributed Cloud’s RFP to replace N... (via Google)
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders to align on the technical path for running VAST on GC... (via Google)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP networking/IP failover options for upcoming... (via Google)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Group meeting aligning on an MVP launch on Google Cloud Marketplace using private offers with fixed ... (via Google)

## Key Facts

- Google Distributed Cloud (GDC) has connected and air-gapped variants; NetApp is the current storage partner in GDC deployments.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and the pursuit is competitive/vendor due diligence.
- Google’s emphasis areas: air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags integration.
- Fort Meade on-prem "Gemini as a service" initiative is described as a Q4 commit and a strong candidate for rapid joint validation.
- GDC hardware commonly runs on Dell; deployments may also involve HPE and Cisco.
- VAST recently launched Google Marketplace offers; broader partnership is early-stage.
- There may be ambiguity whether "Leo" is the same person as Lior Genzel; needs clarification.
- Z4M is the next Google storage-serving VM with higher storage and network density; Z3 exists today.
- Z4M targets storage-serving use cases; CPU/RAM may be overprovisioned initially with planned pricing optimization.
- Google is developing a Google Supercomputer (GSC) provisioning interface to optimize co-placement of storage and accelerators and potentially automate partner deployments like VAST.

## Topics

Google Distributed Cloud storage replacement RFP (NetApp displacement), Air-gapped/dark-site operational readiness and support model, Compliance/attestations and ATO evidence (including DISA STIG), Multi-tenancy, quotas, encryption, tags integration, Hardware platform options (Dell/HPE/Cisco) and SKU recommendations, Commodity VM shapes and RDMA tradeoffs, Fort Meade on-prem Gemini validation/POC and rack-and-stack logistics, Alignment between Google corporate GDC and Google Federal/IC teams, Go-to-market linkage between VAST Federal and Google Federal sellers, Potential future partnership track around Google TPUs/model builders, VAST on GCP architecture using Z4M storage-serving VMs, Local SSD vs HyperDisk vs object storage tiers, Metadata offload to object storage and need for a higher-performance object tier, Google Supercomputer (GSC) provisioning and co-placement/auto-deploy integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline

## Overview

Cloud-related workstream to confirm GCP GA timing after a bottleneck fix and align initial lighthouse customers.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |

## Blockers

- ❌ Bottleneck fix pending/just completed (timing dependent on resolution)
- ❌ Potential disconnect between Google corporate GDC team and Google Federal/IC teams
- ❌ Need for credible air-gapped/dark-site proof points and shareable compliance/ATO evidence
- ❌ Hardware/platform alignment decisions (Dell/HPE/Cisco vs commodity VM shapes; RDMA support)
- ❌ Competitive RFP with NetApp incumbency and other vendors under due diligence

## Next Steps

- [ ] Confirm GCP GA timing post bottleneck fix
- [ ] Align on first 2–3 lighthouse customers with Cloud Team
- [ ] Send intro email connecting Greg to Google GDC corporate and Federal stakeholders and share RFP package
- [ ] Assemble RFP supplements covering compliance/attestations, encryption/certs, multi-tenancy, quotas, tags integration, troubleshooting and ops model
- [ ] Schedule and conduct 1:1 between Alon and Muninder on AI approach, VM shapes, RDMA, and hardware tradeoffs
- [ ] Run architecture review to decide deployment approach (Dell/HPE/Cisco vs commodity VMs)
- [ ] Use Fort Meade on-prem Gemini initiative as near-term joint validation reference
- [ ] Meet in person at Supercomputing and include key GCP stakeholders (Ilyas, Dean)
- [ ] Draft and share networking questions/formal requests with GCP
- [ ] Review Cloud WAN materials and assess applicability to data movement

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will connect Greg with Google stakeholders and drive RFP content assembly.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi on AI, VM shapes, RDMA, and storage/hardware tradeoffs.
- ✅ "Leo" will own the end-to-end RFP response and submissions.
- ✅ Use the Fort Meade on-prem "Gemini as a service" effort as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in proposals.
- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).
- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Asaf Levy]] |  |  |
| [[Greg Castellucci]] |  | VAST Data |
| [[Jason Valeri]] | Finance |  |
| [[Jennifer Azzolina]] |  | VAST Data |
| [[Tomer Hagay]] | Product/pricing stakeholder |  |
| [[Randy Hayes]] |  | VAST Data |
| [[Jeff Denworth]] |  |  |
| [[Jason Ainsworth]] | Meeting organizer |  |
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |
| [[Lior Genzel]] |  |  |
| [[Billy Kettler]] |  | Google |
| [[Mordechai Blaunstein]] |  |  |
| [[Timo Pervane]] | Meeting participant |  |
| [[Karl Vietmeier]] |  |  |
| [[Ronnie Lazar]] |  |  |
| [[Eirikur Hrafnsson]] |  |  |
| [[Jeremiah Hinrichs]] |  | VAST Data |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Olivia Bouree]] |  |  |
| [[Alon Horev]] |  |  |

## Related People

- [[Asaf Levy]]
- [[Greg Castellucci]]
- [[Jason Valeri]]
- [[Jennifer Azzolina]]
- [[Tomer Hagay]]
- [[Randy Hayes]]
- [[Jeff Denworth]]
- [[Jason Ainsworth]]
- [[John Downey]]
- [[Jason Vallery]]
- [[Lior Genzel]]
- [[Billy Kettler]]
- [[Mordechai Blaunstein]]
- [[Timo Pervane]]
- [[Karl Vietmeier]]
- [[Ronnie Lazar]]
- [[Eirikur Hrafnsson]]
- [[Jeremiah Hinrichs]]
- [[Jonsi Stephenson]]
- [[Olivia Bouree]]
- [[Alon Horev]]

## Related Customers

- [[Google]]

## Related

<!-- Wikilinks to related entities -->
