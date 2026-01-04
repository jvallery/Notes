---
type: people
title: Jason Vallery
created: '2026-01-03'
last_contact: unknown
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Jason Vallery

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Product management (cloud); partnerships with hyperscale cloud providers |
| **Company** | VAST Data |
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

- [ ] Send intro email connecting Greg to Google GDC corporate and Federal stakeholders; share the RFP package. @Jason Vallery
- [ ] Assemble RFP supplements: compliance/attestations (e.g., DISA STIG), encryption/certs, multi-tenancy, quotas, tags integration, troubleshooting and ops model. @Jason Vallery
- [ ] Draft recommended Dell and HPE hardware SKUs and deployment patterns for GDC air-gapped. @Jason Vallery
- [ ] Schedule architecture review to decide on Dell/HPE/Cisco vs. commodity VM deployment approach. @Jason Vallery

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JasonVallery") AND !completed
SORT due ASC
```

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

## Topics Discussed

Google Distributed Cloud storage replacement RFP (NetApp displacement), Air-gapped/dark-site operational readiness and support model, Compliance/attestations and ATO evidence (including DISA STIG), Multi-tenancy, quotas, encryption, tags integration, Hardware platform options (Dell/HPE/Cisco) and SKU recommendations, Commodity VM shapes and RDMA tradeoffs, Fort Meade on-prem Gemini validation/POC and rack-and-stack logistics, Alignment between Google corporate GDC and Google Federal/IC teams, Go-to-market linkage between VAST Federal and Google Federal sellers, Potential future partnership track around Google TPUs/model builders, VAST on GCP architecture using Z4M storage-serving VMs, Local SSD vs HyperDisk vs object storage tiers, Metadata offload to object storage and need for a higher-performance object tier, Google Supercomputer (GSC) provisioning and co-placement/auto-deploy integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline

## Recent Context

- unknown: [[2025-10 - Microsoft Tasks]] - Task list for Microsoft/Azure engagement work, including networking/egress planning, validating Azur... (via Microsoft)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams coordinated a response to Google Distributed Cloud’s RFP to replace N... (via Google)
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]] - Group meeting with Google partner stakeholders to align on the technical path for running VAST on GC... (via Google)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Group meeting aligning on an MVP launch on Google Cloud Marketplace using private offers with fixed ... (via Google)

## Profile

**Role**: Product management (cloud); partnerships with hyperscale cloud providers at VAST Data (Cloud / Product Management)
**Relationship**: Internal collaborator

**Background**:
- Coordinating Microsoft/Azure-related validation and collateral creation (ROI data usage, BizDev education, one-pagers, offer/SKU assessment).
- Started at VAST ~3 weeks prior; reports to Jeff Denworth. Previously at Microsoft for ~13 years running product management for Azure Storage/Azure Blob Storage.
- Joined from Microsoft ~2 weeks prior after ~13 years focused on Azure; strong cloud and storage background; wants to make VAST on Cloud the best experience and deepen GCP integration (marketplace, VM types, networking).

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will connect Greg with Google stakeholders and drive RFP content assembly.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi on AI, VM shapes, RDMA, and storage/hardware tradeoffs.
- ✅ "Leo" will own the end-to-end RFP response and submissions.
- ✅ Use the Fort Meade on-prem "Gemini as a service" effort as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in proposals.
- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).
- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.

## Related Customers

- [[Microsoft]]
- [[Google]]

## Related Projects

- [[Marketplace L-series Offer Complement (SKUs/OEM path)]]
- [[Microsoft BizDev Education & Intros to Ronnie]]
- [[Pricing]]
- [[Cloud]]
- [[EB Power Savings to GPUs One-Pager]]
- [[Microsoft ROI Data Usage Validation]]

## Related




---
*Last updated: *