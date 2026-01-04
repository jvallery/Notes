---
type: people
title: Greg Castellucci
created: '2026-01-03'
last_contact: '2025-11-14'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Greg Castellucci

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Director of Federal Sales |
| **Company** | VAST Data |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | Herndon, Virginia, United States |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

Greg Castellucci has over 30 years of experience in the technology sector, specializing in federal sales and systems engineering. Prior to his current role at VAST Data, he held positions such as Federal Chief Technology Officer and Director of Systems Engineering at Extreme Networks, and Systems Engineering Manager at Brocade Communications. He has also worked at General Dynamics Information Technology and Booz Allen Hamilton.


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

- [ ] Send intro email connecting Greg to Google GDC corporate and Federal stakeholders; share the RFP package. @Jason Vallery
- [ ] Run point with Google Federal and GDC corporate; coordinate near-term meetings and joint validation path. @Greg Castellucci
- [ ] Coordinate with Google/Cisco on Fort Meade rack-and-stack progress and confirm validation scope for Q4. @Greg Castellucci
- [ ] Set near-term meeting with Google GDC team to review RFP Q&A and air-gapped ops posture. @Greg Castellucci
- [ ] Link VAST Federal sellers with Google Federal for FBI, State, and Army opportunities. @Greg Castellucci

## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@GregCastellucci") AND !completed
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
- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement/training plus PM augmentation, and marketing support.
- Documentation is currently feature/button-oriented and not scenario-driven; scenario guides are ad hoc and late.
- PM process gaps include training ownership, PRDs vs FRDs (engineering writes FRDs), release visibility, and access to builds/docs.

## Topics Discussed

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on accelerating AI-first software developme... (via Tomer Hagay)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on improving VAST engineering maturity and ... (via Tomer Hagay)
- 2025-10-22: [[2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm]] - 1:1 between Jason Vallery (VAST) and Sam Hopewell (OpenAI) to re-establish alignment on VAST as GPU-... (via Sam Hopewell)
- 2025-09-16: [[2025-09-16 - Intro call exploring roles for Jason at VAST. Lior outlined three potential home]] - 1:1 intro call between Lior Genzel and Jason Vallery exploring Jason joining VAST, with discussion o... (via Lior Genzel)
- 2025-09-16: [[2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp]] - Weekly 1:1 focused on the distributed cache for checkpointing: implementation is complete, with scal... (via Vishnu Charan TJ)

## Profile

**Role**: VAST Data (Federal)
**Relationship**: Internal collaborator; federal point person for Google

**Background**:
- Federal point person for Google; coordinating Google Federal and corporate GDC engagement; also coordinating with Google/Cisco on Fort Meade rack-and-stack progress. Noted upcoming heavy focus on Leidos next year.
- Not directly discussed in transcript; included in known entities but not referenced in this note's narrative.
- Listed in known entities; not discussed in note content beyond manifest context.

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

## Related Customers

- [[Leidos]]
- [[Microsoft]]
- [[Cisco]]
- [[Google]]

## Related Projects

- [[Google Distributed Cloud RFP]]
- [[Cloud]]
- [[Fort Meade "Gemini as a service" on-prem validation]]
- [[Cisco POC (DoD/IC)]]

## Related




---
*Last updated: *