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

- Google Distributed Cloud (GDC) has connected and air-gapped variants; NetApp is the current storage partner in GDC deployments.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and the pursuit is competitive/vendor due diligence.
- Google’s emphasis areas: air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags integration.
- Fort Meade on-prem "Gemini as a service" initiative is described as a Q4 commit and a strong candidate for rapid joint validation.
- GDC hardware commonly runs on Dell; deployments may also involve HPE and Cisco.
- VAST recently launched Google Marketplace offers; broader partnership is early-stage.
- There may be ambiguity whether "Leo" is the same person as Lior Genzel; needs clarification.

## Topics Discussed

Google Distributed Cloud storage replacement RFP (NetApp displacement), Air-gapped/dark-site operational readiness and support model, Compliance/attestations and ATO evidence (including DISA STIG), Multi-tenancy, quotas, encryption, tags integration, Hardware platform options (Dell/HPE/Cisco) and SKU recommendations, Commodity VM shapes and RDMA tradeoffs, Fort Meade on-prem Gemini validation/POC and rack-and-stack logistics, Alignment between Google corporate GDC and Google Federal/IC teams, Go-to-market linkage between VAST Federal and Google Federal sellers, Potential future partnership track around Google TPUs/model builders

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams coordinated a response to Google Distributed Cloud’s RFP to replace N... (via Google)

## Profile

**Relationship**: Internal collaborator / meeting participant

**Background**:
- Reached out to improve sync between corporate and federal teams; set up calls and offered help to federal efforts; referenced as part of corporate side and reporting chain involving Lior.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will connect Greg with Google stakeholders and drive RFP content assembly.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi on AI, VM shapes, RDMA, and storage/hardware tradeoffs.
- ✅ "Leo" will own the end-to-end RFP response and submissions.
- ✅ Use the Fort Meade on-prem "Gemini as a service" effort as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in proposals.

## Related




---
*Last updated: *