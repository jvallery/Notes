---
type: customer
title: Google
last_contact: unknown
created: '2026-01-03'
tags:
- type/customer
- generated
---

# Google

## Recent Context

- unknown: [[Untitled]] - Forwardable email draft instructing the Performance team how to populate Google’s GDC Storage RFP sp...
- unknown: [[2025-10 - Google Tasks]] - Task to confirm Google Cloud Platform GA timing after a bottleneck fix and align on the first 2–3 li...
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams coordinated a response to Google Distributed Cloud’s RFP to replace N...
- 2025-11-13: [[2025-11-13 - GDC RFP meeting]] - Notes from a Google Distributed Cloud (GDC) RFP-focused discussion covering storage TCO (HDD vs QLC)...
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders to align on the technical path for running VAST on GC...
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]] - Group meeting with Google and VAST teams to evaluate GCP networking/IP failover options for upcoming...
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Group meeting aligning on an MVP launch on Google Cloud Marketplace using private offers with fixed ...

## Key Facts

- Google Distributed Cloud (GDC) has connected and air-gapped variants; NetApp is the current storage partner in GDC deployments.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and the pursuit is competitive/vendor due diligence.
- Google’s emphasis areas: air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags integration.
- Fort Meade on-prem "Gemini as a service" initiative is described as a Q4 commit and a strong candidate for rapid joint validation.
- GDC hardware commonly runs on Dell; deployments may also involve HPE and Cisco.
- VAST recently launched Google Marketplace offers; broader partnership is early-stage.
- There may be ambiguity whether "Leo" is the same person as Lior Genzel; needs clarification.
- GDC RFP discussion areas included HDD vs QLC TCO, SED, hardware partners, AZs, SyncEngine, and potential GCS API requirements.
- Operational/security requirements discussed: separation of duties/two-sign rule, multi-tenancy (QoS/quotas, tags/policy-based management), network security, air-gapped certifications, remote patching, and troubleshooting/patch management.
- Z4M is the next Google storage-serving VM with higher storage and network density; Z3 exists today.

## Topics

Google Distributed Cloud storage replacement RFP (NetApp displacement), Air-gapped/dark-site operational readiness and support model, Compliance/attestations and ATO evidence (including DISA STIG), Multi-tenancy, quotas, encryption, tags integration, Hardware platform options (Dell/HPE/Cisco) and SKU recommendations, Commodity VM shapes and RDMA tradeoffs, Fort Meade on-prem Gemini validation/POC and rack-and-stack logistics, Alignment between Google corporate GDC and Google Federal/IC teams, Go-to-market linkage between VAST Federal and Google Federal sellers, Potential future partnership track around Google TPUs/model builders, HDD vs QLC TCO, Self-encrypting drives (SED), Hardware partners and Dell shapes, Availability zones (AZs), SyncEngine

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | _Unknown_ |

## Key Contacts

- [[Billy Kettler]]
- [[Muninder Singh Sambi]]
- [[John Downey]]
- [[Jan Niemus]]

## Opportunities

- GDC Storage RFP: provide normalized performance + price/perf data for VAST (NVMe/TCP, NFSv4, S3) via provided Excel template
- GCP GA launch readiness and initial lighthouse customer alignment
- Google Distributed Cloud (GDC) US-based RFP to replace NetApp storage partner (air-gapped emphasis)
- Fort Meade on-prem "Gemini as a service" initiative (Q4 commit) as joint validation path
- Potential future track: Google TPU/chip sales to model builders where VAST keeps accelerators productive (mentioned as separate partnership track)
- GDC RFP response/work (requirements around security, multi-tenancy, operations, and hardware shapes)
- Near-term VAST marketplace launch on GCP
- Z4M storage-serving VM adoption for VAST deployments
- GSC (Google Supercomputer) provisioning integration (auto-deploy/co-placement)
- RDMA + GPUDirect Storage enablement with A5X GPUs; TPU RDMA later

## Blockers

- ❌ Template requests Self-Encrypting Drives (SEDs) with FIPS 140-2/140-3; VAST does not support SEDs and must position software-layer encryption instead
- ❌ Potential mismatch between requested '112TiB usable' sizing and nearest sellable SKU; requires clarification rows/notes
- ❌ GA timing dependent on bottleneck fix
- ❌ Need to prove air-gapped/dark-site operational readiness and provide evidence
- ❌ Lack of marquee/anchor air-gapped GDC customer (per Jason’s understanding)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Muninder Singh Sambi]] | Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) | Google |
| [[Lior Genzel]] |  |  |
| [[Jan Niemus]] | Runs DoD/IC organization | Google |
| [[Randy Hayes]] |  | VAST Data |
| [[Billy Kettler]] |  | Google |
| [[Eirikur Hrafnsson]] |  |  |
| [[Greg Castellucci]] |  | VAST Data |
| [[Jason Valeri]] | Finance |  |
| [[Jennifer Azzolina]] |  | VAST Data |
| [[Timo Pervane]] | Meeting participant |  |
| [[Alon Horev]] |  |  |
| [[Jason Ainsworth]] | Meeting organizer |  |
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |
| [[Tomer Hagay]] | Product/pricing stakeholder |  |
| [[Jeremiah Hinrichs]] |  | VAST Data |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

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

## Related People

- [[Jonsi Stephenson]]
- [[Muninder Singh Sambi]]
- [[Lior Genzel]]
- [[Jan Niemus]]
- [[Randy Hayes]]
- [[Billy Kettler]]
- [[Eirikur Hrafnsson]]
- [[Greg Castellucci]]
- [[Jason Valeri]]
- [[Jennifer Azzolina]]
- [[Timo Pervane]]
- [[Alon Horev]]
- [[Jason Ainsworth]]
- [[John Downey]]
- [[Tomer Hagay]]
- [[Jeremiah Hinrichs]]
- [[Jason Vallery]]

## Related

<!-- Wikilinks to related entities -->
