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

- [ ] Schedule and conduct 1:1 with Muninder Sambi to review AI approach, VM shapes, RDMA, and hardware tradeoffs. @Alon Horev

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@MuninderSinghSambi") AND !completed
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
- Silk is software-defined cloud storage optimized for database and single source-of-truth workloads.
- Typical scale cited: up to ~1 PB per data pod with tens of GB/s throughput and sub-ms latency.
- Silk cited ~2–3M TPS with 64k transactions and noted single-VM DB performance is often the limiting factor.

## Topics Discussed

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Silk cloud storage architecture for databases, Performance characteristics (throughput, latency, TPS), AI-driven access to systems of record (real-time vs near-real-time), Positioning vs Azure native storage (Azure NetApp Files), RDMA requirement on Azure L-series and CPU overhead

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture for high-perf... (via Silk)

## Profile

**Role**: Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) at Google (Google Distributed Cloud)
**Relationship**: Partner stakeholder (Google)

**Background**:
- New in role; focused on air-gapped/dark-site readiness, compliance, ops posture; requested proof of air-gapped support and joint customer validation; offered to share VM shapes and discuss RDMA tradeoffs; wants AI education from VAST perspective.
- Not directly discussed in transcript; included in known entities but not referenced in this note's narrative.
- Known partner stakeholder; not substantively discussed in this note.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.

## Related Projects

- [[Google Distributed Cloud RFP]]
- [[Fort Meade "Gemini as a service" on-prem validation]]

## Related Customers

- [[Google]]

## Related




---
*Last updated: *