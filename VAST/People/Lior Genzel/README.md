---
type: people
title: Lior Genzel
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Lior Genzel

## Recent Context

- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Lior Genzel]] - Note captures discussion points and completed follow-ups with Lior Genzel around Google TPU strategy...
- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - The team aligned on a go-to-market strategy with global SIs focused on enterpris]] - GSI Team aligned on a go-to-market strategy with global SIs centered on enterprise workflow automati... (via GSI Team)
- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d... (via Walmart)
- 2025-11-06: [[2025-11-06 - Jason shared VAST’s momentum (CoreWeave $1.2B deal) and updates on Microsoft’s A]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra covering Microsoft Project Apollo and MAI Dall... (via Kanchan Mehrotra)
- 2025-11-06: [[2025-11-06 - Discussion centered on accelerating VAST adoption within Microsoft programs (MAI]] - 1:1 strategy sync focused on accelerating VAST adoption inside Microsoft via MAI and Project Apollo,... (via Kanchan Mehrotra)
- 2025-11-03: [[2025-11-03]] - Brief note capturing open questions and next items around Microsoft hardware SKUs, a POC with MAI, b...
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders on the technical and commercial path to run VAST on G... (via Google)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te...
- 2025-10-30: [[2025-10-30 - Jason and Rob aligned on maturing VaST’s support and customer success for a SaaS]] - 1:1 between Jason Vallery and Rob Banga aligning on how to mature VAST’s support and customer succes... (via Rob Banga)

## Profile

**Role**: Cloud ("cloud guy") at VAST Data (BizDev / Alliances)
**Relationship**: Internal collaborator

**Background**:
- Owns 'Sell To' for Microsoft per note; included in proposed 1:1 cadence; question raised on what Jeff owns vs what to push to Lior.
- Point person for coordinating cloud/hyperscaler pipeline requirements and introductions; driving follow-ups on performance/TCO comparisons and product marketing alignment.
- Involved in Microsoft planning call; had a conversation with Foundry team; Jeff says Lior 'doesn't know key values/vectors'; Jeff wants a year of work/wins mapped for Lior.

## Open Tasks

- [ ] Identify Azure ecosystem gaps (e.g., Azure Key Vault / customer-managed keys) and validate end-to-end Azure deployment to find integration warts

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Google Z3 exists; Z4M is the next storage-serving VM with higher storage and network density.
- Z4M targets storage-serving use cases; CPU/RAM may be overprovisioned but pricing optimization is planned.
- Google is developing a Google Supercomputer (GSC) interface to provision AI/HPC infrastructure with co-placement optimization; VAST could be integrated as a selectable storage option with potential auto-deploy.

## Topics

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Z4M storage-serving VM roadmap (density, pricing optimization), Local SSD vs HyperDisk vs object storage tiers (latency/economics), Google Supercomputer (GSC) provisioning, co-placement, and partner integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline, Anywhere Cache (cost vs performance)

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).
- ✅ Create a shared pros/cons document to re-evaluate VIP/failover options (ILB, alias IP, route-based).
- ✅ Engage Google networking for a follow-up deep dive on RDMA and cross-project connectivity.

## Related Customers

- [[Microsoft]]
- [[Zoom]]
- [[Google]]
- [[OpenAI]]
- [[Walmart]]

## Related Projects

- [[Google Distributed Cloud RFP]]
- [[Pricing]]
- [[Building an AI cloud with VAST]]
- [[Google RFP]]
- [[Cloud]]
- [[VAST on Azure Integration]]
- [[AI Pipelines Collateral]]
- [[Project Apollo]]
- [[GSI Team]]
- [[NeoCloud in a box]]
- [[GCP MVP]]

## Related

<!-- Wikilinks to related entities -->
