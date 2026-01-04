---
type: customer
title: Dell
created: '2026-01-03'
last_contact: '2025-11-14'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Dell

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | _Unknown_ |

## Key Contacts

_No key contacts identified._

## Active Projects

_What projects/initiatives are active with this customer?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Current Blockers

_No known blockers._

## Next Steps

_What are the immediate next actions for this account?_


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Opportunities

- Common GDC hardware platform; VAST to recommend Dell SKUs for air-gapped deployments
- Hardware recommendation shapes with Dell for GDC deployment
- Background context: Google partner stakeholder previously worked at Dell

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will connect Greg with Google stakeholders and drive RFP content assembly.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi on AI, VM shapes, RDMA, and storage/hardware tradeoffs.
- ✅ "Leo" will own the end-to-end RFP response and submissions.
- ✅ Use the Fort Meade on-prem "Gemini as a service" effort as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in proposals.
- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).

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

## Topics / Themes

Google Distributed Cloud storage replacement RFP (NetApp displacement), Air-gapped/dark-site operational readiness and support model, Compliance/attestations and ATO evidence (including DISA STIG), Multi-tenancy, quotas, encryption, tags integration, Hardware platform options (Dell/HPE/Cisco) and SKU recommendations, Commodity VM shapes and RDMA tradeoffs, Fort Meade on-prem Gemini validation/POC and rack-and-stack logistics, Alignment between Google corporate GDC and Google Federal/IC teams, Go-to-market linkage between VAST Federal and Google Federal sellers, Potential future partnership track around Google TPUs/model builders, HDD vs QLC TCO, Self-encrypting drives (SED), Hardware partners and Dell shapes, Availability zones (AZs), SyncEngine

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams coordinated a response to Google Distributed Cloud’s RFP to replace N... (via Google)
- 2025-11-13: [[2025-11-13 - GDC RFP meeting]] - Notes from a Google Distributed Cloud (GDC) RFP-focused discussion covering storage TCO (HDD vs QLC)... (via Google)
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders to align on the technical path for running VAST on GC... (via Google)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |

## Related People

- [[John Downey]]
