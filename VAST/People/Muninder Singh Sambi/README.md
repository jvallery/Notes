---
type: people
title: Muninder Singh Sambi
created: '2026-01-03'
last_contact: '2025-11-14'
auto_created: true
tags:
- type/people
- needs-review
- company/google
---

# Muninder Singh Sambi

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) |
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

- [ ] Schedule and conduct 1:1 with Muninder Singh Sambi to review AI approach, VM shapes, RDMA, and hardware tradeoffs. @Alon Horev
- [ ] Meet with Muninder Singh Sambi ('Manu') at lunch time (noon PST) to discuss federal connection and related requirements (SE/operations, separation of duties).
- [ ] Follow up with Mallikarjun and Muninder Singh Sambi ('Manu').

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@MuninderSinghSambi") AND !completed
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
- GDC RFP discussion areas included HDD vs QLC TCO, SED, hardware partners, AZs, SyncEngine, and potential GCS API requirements.
- Operational/security requirements discussed: separation of duties/two-sign rule, multi-tenancy (QoS/quotas, tags/policy-based management), network security, air-gapped certifications, remote patching, and troubleshooting/patch management.

## Topics Discussed

Google Distributed Cloud storage replacement RFP (NetApp displacement), Air-gapped/dark-site operational readiness and support model, Compliance/attestations and ATO evidence (including DISA STIG), Multi-tenancy, quotas, encryption, tags integration, Hardware platform options (Dell/HPE/Cisco) and SKU recommendations, Commodity VM shapes and RDMA tradeoffs, Fort Meade on-prem Gemini validation/POC and rack-and-stack logistics, Alignment between Google corporate GDC and Google Federal/IC teams, Go-to-market linkage between VAST Federal and Google Federal sellers, Potential future partnership track around Google TPUs/model builders, HDD vs QLC TCO, Self-encrypting drives (SED), Hardware partners and Dell shapes, Availability zones (AZs), SyncEngine

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams coordinated a response to Google Distributed Cloud’s RFP to replace N... (via Google)
- 2025-11-13: [[2025-11-13 - GDC RFP meeting]] - Notes from a Google Distributed Cloud (GDC) RFP-focused discussion covering storage TCO (HDD vs QLC)... (via Google)

## Profile

**Role**: Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) at Google (Google Distributed Cloud)
**Relationship**: Partner stakeholder (Google)

**Background**:
- New in role; focused on air-gapped/dark-site readiness, compliance, ops posture; requested quick joint validation and asked for education on AI and VM shape tradeoffs.
- Partner stakeholder for GDC; referenced as 'Manu' with a planned lunch-time discussion.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will connect Greg with Google stakeholders and drive RFP content assembly.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi on AI, VM shapes, RDMA, and storage/hardware tradeoffs.
- ✅ "Leo" will own the end-to-end RFP response and submissions.
- ✅ Use the Fort Meade on-prem "Gemini as a service" effort as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in proposals.

## Related Customers

- [[Google]]

## Related




---
*Last updated: *