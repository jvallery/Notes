---
type: people
title: Alon Horev
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Alon Horev

## Recent Context

- 2025-10-28: [[Sources/Transcripts/2025/2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam.md|Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] — Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynamics to align before ...

- unknown: [[_Open Topics]] - Open topics note for Alon Horev that currently only contains a task query filtering for incomplete t...
- unknown: [[2025-11-4 - Planning sessions]] - Planning notes for a set of sessions with Jeff Denworth to align on VAST’s cloud-first product strat... (via Jeff Denworth)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- 2026-01-03: [[2026-01-03 - Prep for Microsoft AI talks]] - Jonsi Stephenson and Jason Vallery aligned messaging and strategy for upcoming Microsoft AI discussi... (via Jonsi Stephenson)
- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal sync to align on Walmart’s big data initiative, focusing on clarifying disaster recovery re... (via Walmart)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d... (via Walmart)
- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)

## Profile

**Role**: Founder/CTO office leader (founder; CTO) at VAST Data (CTO Office)
**Relationship**: Internal collaborator (architecture/technical leadership)

**Background**:
- This note is an 'Open Topics' page for Alon Horev and contains a task query for incomplete tasks that mention @alon.
- Architect/technical leader input on MAI/Apollo wedge, marketplace price/perf limitations, and value of liquid-cooled storage SKUs for DC fungibility and late-binding storage vs GPU rack decisions.
- Listed as a possible candidate for weekly/monthly 1:1 cadence (marked '?').

## Open Tasks

- [ ] Schedule and conduct 1:1 with Muninder Sambi to review AI approach, VM shapes, RDMA, and hardware tradeoffs. @Alon Horev
- [ ] Notify Alon about the 2 pm PT discussion and share context in case he can join @Jason Vallery 📅 2025-11-14

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Walmart DR requirement is ambiguous: full VAST namespace access in cloud vs only a data copy.
- VM-based cloud deployments are not viable at the anticipated Walmart scale.
- Team is driving a hybrid roadmap with a goal of more native Google Cloud Storage integration.

## Topics

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Walmart big data initiative requirements, Disaster recovery approach (full namespace vs data copy), Hybrid cloud roadmap and native Google Cloud Storage integration, Customer engagement sequencing (expectations call before architecture session), Proposal sizing (minimum config vs phase-one; D-box/capacity)

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Do not schedule an architecture/whiteboarding session until Walmart requirements are clarified.
- ✅ Lead with current capabilities plus forward hybrid roadmap narrative in the Mingming call.
- ✅ Escalate to a deeper technical session with additional SMEs only after requirement confirmation.
- ✅ Use SyncEngine for the pilot to replicate from GCS to on-prem VAST clusters.

## Related Customers

- [[Microsoft]]
- [[Walmart]]

## Related Projects

- [[Google Distributed Cloud RFP]]
- [[Model Builder Turbine]]
- [[Confluence FRDs taxonomy]]
- [[Neo]]
- [[Cloud]]
- [[VAST on Azure Integration]]
- [[Project Apollo]]
- [[Enscale deck]]
- [[Fort Meade "Gemini as a service" on-prem validation]]
- [[OVA]]

## Related

<!-- Wikilinks to related entities -->
