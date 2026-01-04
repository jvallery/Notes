---
type: customer
title: GDC RFP federal coordination
date: '2025-11-14'
account: Google
participants:
- Jason Vallery
- Alon Horev
- Jennifer Azzolina
- Jeremiah Hinrichs
- Greg Castellucci
- Randy Hayes
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-11-14 - VAST’s cloud and federal teams
  aligned on responding to Google Distributed Cloud.md
tags:
- type/customer
- account/google
- generated
---

# GDC RFP federal coordination

**Date**: 2025-11-14
**Account**: [[Google]]
**Attendees**: Jason Vallery, Alon Horev, Jennifer Azzolina, Jeremiah Hinrichs, Greg Castellucci, Randy Hayes

## Summary

VAST cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace NetApp storage, with heavy emphasis on air-gapped/dark-site readiness, compliance evidence, and operational posture. The team agreed to use the in-flight Fort Meade “Gemini as a service” on-prem effort as a near-term joint validation path and to tighten coordination between Google corporate GDC and Google Federal stakeholders. Ownership was clarified across RFP response, stakeholder engagement, and technical follow-ups (including a 1:1 with Muninder Singh Sambi and an upcoming architecture review).
## Action Items
- [ ] Send intro email connecting Greg Castellucci to Google GDC corporate and Federal stakeholders and share the RFP package @Jason ⏫ #task
- [ ] Assemble RFP supplements covering compliance/attestations (e.g., DISA STIG), encryption/certifications, multi-tenancy, quotas, tags integration, troubleshooting practices, and operations model @Jason ⏫ #task
- [ ] Own and submit the formal Google Distributed Cloud RFP response coordinating inputs across teams @Leo ⏫ #task
- [ ] Run point with Google Federal and corporate GDC teams; coordinate near-term meetings and the joint validation path @Greg ⏫ #task
- [ ] Schedule and conduct a 1:1 with Muninder Singh Sambi to review AI approach, VM shapes, RDMA, and hardware tradeoffs @Alon ⏫ #task
- [ ] Provide lists of federal air-gapped customers and obfuscated past performance references for inclusion in the RFP @Jennifer ⏫ #task
- [ ] Provide federal compliance/ATO summaries and links to public artifacts for inclusion in the RFP @Jeremiah ⏫ #task
- [ ] Coordinate with Google and Cisco on Fort Meade rack-and-stack progress and confirm validation scope for Q4 @Greg ⏫ #task
- [ ] Prepare an EBC-style briefing on AI workloads, storage patterns, and air-gapped operations for Google @Randy #task
- [ ] Draft recommended Dell and HPE hardware SKUs and deployment patterns for GDC air-gapped @Jason ⏫ #task
- [ ] Set a near-term meeting with Google GDC team to review RFP Q&A and air-gapped operations posture @Greg ⏫ #task
- [ ] Schedule an architecture review to decide on Dell/HPE/Cisco vs commodity VM deployment approach @Jason ⏫ #task
- [ ] Link VAST Federal sellers with Google Federal for FBI, State, and Army opportunities @Greg #task
- [ ] Confirm whether Fort Meade status can be cited in the RFP as active validation/past performance reference @Jennifer #task

## Decisions
- Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- Alon Horev will pursue a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- Leo will own the end-to-end formal RFP response and submission.
- The team will use the Fort Meade on-prem “Gemini as a service” effort as the primary near-term validation path/reference.
- RFP proposal will include recommended Dell and HPE SKUs and consider Cisco/commodity VM options for deployment.

## Key Information
- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner today.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence (not guaranteed).
- Google’s emphasis areas include air-gapped support, compliance/attestations, ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tagging.
- Muninder Singh Sambi is new in role leading GDC (connected side) and is prioritizing dark-site/air-gapped readiness and quick joint validation with a customer.
- Fort Meade “Gemini as a service” on-prem initiative is described as a Q4 commit and a strong candidate for rapid joint validation.
- GDC deployments commonly run on Dell; HPE and Cisco are also in play for some deployments.
- VAST has active relationships with Google’s DoD/IC org (Jan Niemus) and has been working with Google/Cisco on a Fort Meade POC concept.
- A key risk is misalignment between Google corporate GDC and Google Federal teams, plus lack of a marquee air-gapped anchor tenant and sensitivity of compliance/ATO evidence.

---

*Source: [[Inbox/_archive/2025-11-14/2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud.md|2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]]*

## Related

- [[NetApp]]
- [[Cisco]]
- [[Dell]]
- [[HPE]]
- [[Microsoft]]
- [[AWS]]
- [[Leidos]]
- [[Google Distributed Cloud RFP]]
- [[Fort Meade "Gemini as a service" on-prem validation]]
- [[Jennifer Azzolina]]
- [[Jeremiah Hinrichs]]
- [[Greg Castellucci]]
- [[Jason Vallery]]
- [[Alon Horev]]
- [[Randy Hayes]]
- [[Muninder Singh Sambi]]
- [[Jan Niemus]]
- [[Lior Genzel]]
- [[Olivia Bouree]]
- [[Seth Haynes]]
- [[Jeff Denworth]]
- [[Jeremy Winter]]
