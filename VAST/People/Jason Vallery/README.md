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
- [ ] Lead the customer call and position current capabilities and hybrid roadmap @Jason Vallery 📅 2025-11-14
- [ ] Notify Alon about the 2 pm PT discussion and share context in case he can join @Jason Vallery 📅 2025-11-14
- [ ] Coordinate Tel Aviv engineering sessions to define native GCS integration requirements @Jason Vallery
- [ ] Based on clarified requirements, schedule architecture/whiteboarding session with appropriate SMEs @Jason Vallery
- [ ] Text Jason after the meeting with Ong and Manish and schedule a follow-up call to debrief and formulate the go-forward strategy. @Jonsi Stephenson
- [ ] Meet with Customer Success (e.g., Rich) to understand account support workflows end-to-end. @Jason Vallery

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JasonVallery") AND !completed
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

- unknown: [[2025-10 - Microsoft Tasks]] - Checklist of completed action items for Microsoft/Azure engagement, including networking/egress plan... (via Microsoft)
- unknown: [[2025-10 - OpenAI Tasks]] - Task list for coordinating with OpenAI on storage API requirements, global KV store needs, and sched... (via OpenAI)
- unknown: [[2025-10 - Andy Pernsteiner]] - A completed action item to set up a 1:1 with Andy Bernstein to learn meeting rhythms and communicati... (via Andy Perlsteiner)
- unknown: [[2025-10 - Asaf Levy]] - Completed action items from a working session with Asaf Levy to align on DataSpaces persistence desi... (via Asaf Levy)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Jonsi Stephenson]] - A completed action item to align with Jonsi Stephenson on travel plans in order to enable an in-pers... (via Jonsi Stephenson)
- unknown: [[2025-10 - Josh Wentzell]] - Follow-up task to contact Josh Wentzell (Office of the CTO) to obtain VAST OVA and onboarding materi... (via Josh Wentzell)
- unknown: [[2025-10 - Kanchan Mehrotra]] - A completed follow-up task to connect with Kanchan Mehrotra about storage plays and density for Supe... (via Kanchan Mehrotra)
- unknown: [[2025-10 - Kishore Inampudi]] - Follow-up task to coordinate with Kishore Inampudi on Azure Extended Zones after A2N approval, align... (via Kishore Inampudi)
- unknown: [[2025-10 - Kurt Niebuhr]] - Action items related to keeping Jason informed on neo-cloud partnership pipeline opportunities and p... (via Kurt Niebuhr)
- unknown: [[2025-10 - Lior Genzel]] - Note captures discussion points and completed follow-ups with Lior Genzel around Google TPU strategy... (via Lior Genzel)
- unknown: [[2025-10 - Noa Cohen]] - A completed action item to introduce Jason Vallery and sync with several program managers, including... (via Noa Cohen)
- unknown: [[2025-10 - Rick Hasleton]] - A single action item to meet with Customer Success to learn the end-to-end account support workflow,... (via Rick Haselton)
- unknown: [[2025-10 - Rob Benoit]] - A completed task to coordinate with Rob Benoit regarding expectations for Tech Summit content, assig... (via Rob Benoit)
- unknown: [[2025-10 - Shachar Feinblit]] - Checklist and Slack snippets related to coordinating with Shachar Feinblit, including setting up rec... (via Shachar Feinblit)

## Profile

**Role**: Product management (cloud); partnerships with hyperscale cloud providers at VAST Data (Cloud / Partnerships)
**Location**: Colorado (near Boulder)
**Relationship**: Internal collaborator

**Background**:
- Coordinated Microsoft-related collateral and validations (ROI data usage, BizDev education/intros, power-savings one-pager, marketplace offer assessment).
- Internal collaborator coordinating partner/customer requirements and meetings.
- Internal collaborator coordinating cloud/partner-related work.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).
- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.

## Related Customers

- [[Microsoft]]
- [[VAST Data]]
- [[Avanade]]
- [[Anthropic]]
- [[Silk]]
- [[Crusoe]]
- [[Amazon]]
- [[Google]]
- [[NBCU]]
- [[OpenAI]]
- [[Walmart]]

## Related Projects

- [[Win/Loss + Product MBR cadence]]
- [[BlockFuse/C-Store]]
- [[DeltaZero]]
- [[BlobFuse]]
- [[Project Stargate]]
- [[Project Apollo]]
- [[AC Store]]
- [[VAST-as-a-Service]]
- [[Enscale deck]]
- [[NeoCloud in a box]]
- [[MAI unified cache]]
- [[Platform Learning]]
- [[Bifrost]]
- [[Model Builder Turbine]]
- [[Confluence FRDs taxonomy]]
- [[Google RFP]]
- [[Cloud]]
- [[Google Marketplace offers]]
- [[Microsoft Azure Engagement Plan]]
- [[OVA]]
- [[Microsoft Comparison Slide (LSv4/LSv5/OEM-ODM/Azure Storage)]]
- [[Pricing]]
- [[Cloud control plane]]
- [[OpenAI cache evaluation]]
- [[Apollo]]
- [[Neo]]
- [[Cloud-in-a-box (Tier-2 clouds)]]
- [[VAST on Azure Integration]]
- [[AI Pipelines Collateral]]
- [[Marketplace L-series Offer Complement (SKUs/OEM path)]]
- [[Alluxio/DAX]]
- [[AI caching strategy for MAI]]
- [[GSI Team]]
- [[GCP MVP]]
- [[Google Distributed Cloud RFP]]
- [[Building an AI cloud with VAST]]
- [[Microsoft BizDev Education & Intros to Ronnie]]
- [[OpenAI cache IP feasibility evaluation]]
- [[OpenAI VAST POC (CoreWeave cluster)]]
- [[AI caching strategy for MAI scale]]
- [[5.5 Features]]
- [[Microsoft ROI Data Usage Validation]]
- [[Blockfuse/BlobFuse]]
- [[EB Power Savings to GPUs One-Pager]]

## Related




---
*Last updated: *