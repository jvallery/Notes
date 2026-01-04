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

- unknown: [[Untitled]] - Forwardable email draft instructing the Performance team how to populate Google’s GDC Storage RFP Ex...
- unknown: [[2025-10 - Google Tasks]] - A completed task to confirm Google Cloud Platform GA timing after a bottleneck fix and align the fir...
- unknown: [[2025-10 - Lior Genzel]] - Note captures discussion points and completed follow-ups with Lior Genzel around Google TPU strategy... (via Lior Genzel)
- unknown: [[Available Capacity Calculations]] - Email-style note proposing replacing a fixed overhead percentage with a first-principles “available ... (via Cloud)
- unknown: [[2025-10 - Pricing Tasks]] - Checklist of completed pricing workstreams for cloud/private offers, discount policy, normalization ... (via Pricing)
- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne...
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal sync to align on Walmart’s big data initiative, focusing on clarifying disaster recovery re... (via Walmart)
- 2025-11-13: [[2025-11-13 - GDC RFP meeting]] - Notes from a Google Distributed Cloud (GDC) RFP-related discussion covering storage TCO (HDD vs QLC)...
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-07: [[2025-11-07 - Jason and Tomer aligned on the need to introduce clearer product management disc]] - Jason Vallery and Tomer Hagay discussed gaps in VAST’s product management discipline (OKRs/KRs, trac... (via Tomer Hagay)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- GDC RFP discussion topics included HDD vs QLC TCO, SED, hardware partners, availability zones, SyncEngine, and potential GCS API considerations.
- Operational/security focus areas: multi-tenancy, QoS/quotas, tags and policy-based management, network security, air-gapped security certifications, remote patching, and troubleshooting/patching processes.
- Dell was referenced for hardware recommendation shapes.

## Topics

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, HDD vs QLC TCO, SED (self-encrypting drives), Hardware partners and sizing (Dell shapes), Availability zones (AZs), SyncEngine

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | _Unknown_ |

## Key Contacts

- [[Jai Menon]]
- [[Olivia Kim]]
- [[Henry Perez]]
- [[Jan Niemus]]
- [[John Downey]]
- [[Billy Kettler]]
- [[Muninder Singh Sambi]]
- [[Ben]]

## Opportunities

- GDC Storage RFP: provide normalized performance + pricing data in Google Excel template for VAST (NVMe/TCP, NFSv4, S3)
- Align first 2–3 lighthouse customers for GCP GA rollout
- TPU strategy outside GCP (pending disclosure; prep meetings such as GTC-DC).
- Cloud deployment capacity/overhead modeling aligned to GCP fault-domain structure and rolling update budgets (MIG maxUnavailable/maxSurge).
- Google private offer marketplace entitlements and pricing schema; approval process initiated
- Similar proxy/tiering conversation as Walmart; relationship with existing cloud stores and namespace integration
- Google Distributed Cloud RFP to replace NetApp storage
- Fort Meade on-prem "Gemini as a service" validation (Q4 commit)
- Joint federal account alignment (FBI, State, Army referenced as opportunities)
- Potential TPU/model-builder partnership track

## Blockers

- ❌ Template requests Self-Encrypting Drives (FIPS 140-2/3), but VAST does not support SEDs; must position software-based dual encryption instead
- ❌ Potential mismatch between requested '112TiB usable' sizing and nearest sellable SKU; must document nearest-SKU approach with extra explanatory rows
- ❌ GA timing dependent on post-bottleneck fix
- ❌ Two-week timeline for disclosure of TPU strategy outside GCP.
- ❌ Sub-zonal availability domain support varies by region/zone; wide EC (e.g., 7+1) depends on actual availability domain guarantees.

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Jeff Denworth]] |  |  |
| [[Jason Valeri]] | Finance |  |
| [[Olivia Kim]] |  | Google |
| [[Henry Perez]] |  | Google |
| [[Jan Niemus]] | Runs DoD/IC organization | Google |
| [[Randy Hayes]] |  | VAST Data |
| [[Ben]] | Product Manager (block storage) | Google |
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |
| [[Tomer Hagay]] | Product/pricing stakeholder |  |
| [[Billy Kettler]] |  | Google |
| [[Lior Genzel]] |  |  |
| [[Greg Castellucci]] |  | VAST Data |
| [[Muninder Singh Sambi]] | Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) | Google |
| [[Eirikur Hrafnsson]] |  |  |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

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

## Related People

- [[Jai Menon]]
- [[Jeff Denworth]]
- [[Jason Valeri]]
- [[Olivia Kim]]
- [[Henry Perez]]
- [[Jan Niemus]]
- [[Randy Hayes]]
- [[Ben]]
- [[John Downey]]
- [[Tomer Hagay]]
- [[Billy Kettler]]
- [[Lior Genzel]]
- [[Greg Castellucci]]
- [[Muninder Singh Sambi]]
- [[Eirikur Hrafnsson]]
- [[Jonsi Stephenson]]
- [[Jason Vallery]]

## Related

<!-- Wikilinks to related entities -->
