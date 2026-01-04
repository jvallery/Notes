---
type: people
title: Olivia Borey
created: '2026-01-03'
last_contact: '2025-11-14'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Olivia Borey

## Contact Information

| Field | Value |
|-------|-------|
| **Role** |  |
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

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Olivia Borey")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@OliviaBorey") AND !completed
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
- John runs alliances/partnerships and is the go-to for AMD/NVIDIA and conventional channel partnerships (non-cloud).
- Sagi leads pipelines/serverless; packaging and cloud GTM for pipelines is under-thought.
- Morty owns Neo-cloud feature requirements; he can support Jason but must maintain Neo-cloud coverage.

## Topics Discussed

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Org map and key leaders/roles, Cross-cloud platform strategy and homogenization across providers, Cloud GTM plays and integrations (Foundry/Bedrock/Vertex), Cataloging in-flight deals by product requirements, Control-plane partnerships and 'cloud-in-a-box' for Tier-2 clouds

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-29: [[2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g]] - Group office hours aligned the team on positioning and operating mechanics for VAST on Cloud, emphas... (via VAST on Cloud Office Hours)
- 2025-10-29: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]] - Group meeting to align positioning and go-to-market for VAST on Cloud, including MVP architecture, m... (via VAST on Cloud Office Hours)

## Profile

**Role**: Cloud field lead for GCP and OCI (exact title not stated) at VAST Data (Cloud / Field)
**Relationship**: Internal collaborator / meeting participant

**Background**:
- Reached out to improve sync between corporate and federal teams; set up calls with corporate team; on call with Lior.
- Mentioned as someone the author met (with Tiffany) in context of alliances/BD org.
- Was on the GDC RFP call.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.
- ✅ Prioritize building a first-class cross-cloud platform and GTM versus ad hoc deal chasing.

## Related Projects

- [[Google Distributed Cloud RFP]]
- [[Cloud]]

## Related




---
*Last updated: *