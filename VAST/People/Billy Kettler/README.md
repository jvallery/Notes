---
type: people
title: Billy Kettler
created: '2026-01-03'
last_contact: '2025-11-14'
auto_created: true
tags:
- type/people
- needs-review
- company/google
---

# Billy Kettler

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
| **Company** | Google |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

_Career history, expertise, interests, personal details shared..._


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Billy Kettler")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@BillyKettler") AND !completed
SORT due ASC
```

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

## Topics Discussed

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Z4M storage-serving VM roadmap (density, pricing optimization), Local SSD vs HyperDisk vs object storage tiers (latency/economics), Google Supercomputer (GSC) provisioning, co-placement, and partner integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline, Anywhere Cache (cost vs performance)

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders on the technical and commercial path to run VAST on G... (via Google)
- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP IP/VIP management and failover options unde... (via Google)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)

## Profile

**Role**: VP of Product Management (as described in transcript); partner contact at Google
**Relationship**: Customer/partner contact (Google)

**Background**:
- Listed in known people manifest; not substantively discussed in note content.
- Not directly discussed in transcript; included in known entities but not referenced in this note's narrative.
- Google partner/technical stakeholder for VAST; previously at Scality, Nexenta, and Dell; storage/backup/DR background; involved in defining Z4M storage-serving VM and partner integration into GSC; discussed RDMA/GPUDirect roadmap and object-tier options (Anywhere Cache, future premium object tier).

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

- [[Dell]]
- [[Google]]

## Related Projects

- [[Google Distributed Cloud RFP]]
- [[Z4M RDMA Networking (GCP)]]
- [[Cloud]]
- [[PSC Interfaces for Cross-Project RDMA]]
- [[VIP/Failover Design (GCP RDMA)]]

## Related




---
*Last updated: *