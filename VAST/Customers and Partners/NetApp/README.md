---
type: customer
title: NetApp
created: '2026-01-03'
last_contact: unknown
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# NetApp

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

- ❌ Competitive risk: NetApp excels at block I/O latency; could disqualify VAST for certain Google RFP scopes
- ❌ Competitive risk: NetApp excels at block I/O latency/features; avoid pursuing block I/O-heavy RFP scope

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

- Competitive pricing analysis vs NetApp as part of broader competitive benchmarking
- Incumbent storage partner in GDC being displaced by RFP
- Competitive context: only other file option on GDC besides VAST; relies on revived OnTap Select
- Comparative context for marketplace/first-party cloud storage offerings (e.g., Azure NetApp Files) and field enablement practices
- Referenced as an example of companies hosting large annual customer events that drive awareness and opportunities.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Do not pursue a Microsoft counteroffer given compensation constraints and unclear scope.
- ✅ Proceed toward a decision between VAST and Crusoe with intent to resign by Wednesday.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Jason has a VAST offer with complex, highly variable compensation tied to OpenAI/Azure sales plus equity.
- Crusoe offer deadline is Wednesday; VAST has not set a decision deadline.
- Microsoft cannot approach Crusoe-level compensation; any change would be modest and potentially insulting.

## Topics / Themes

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Job offers comparison (VAST vs Crusoe vs Microsoft), Compensation structure risk (commission/equity variability), Apollo program scope ambiguity and execution risk, Career trajectory and path to partner at Microsoft, Resignation timeline

## Recent Context

- unknown: [[2025-10 - Pricing Tasks]] - Checklist of completed pricing workstreams for cloud/private offers, discount policy, normalization ... (via Pricing)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-06: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]] - Review of updated AI pipeline slides for an upcoming VAST SE Tech Summit, covering model training (c... (via AI Pipelines Collateral)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
- 2025-10-30: [[2025-10-30 - Weekly SE community call covering end-of-quarter push, Tech Summit logistics, an]] - Weekly SE community call focused on end-of-quarter execution, Tech Summit logistics/expense policy, ... (via SRE)
- 2025-10-27: [[2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]] - Group meeting transcript debating how to align VAST cloud pricing with the new on-prem core+capacity... (via Pricing)
- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 between Jason Vallery and Jai Menon discussing Jason’s competing offers from VAST and Cru... (via Jai Menon)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Rob Benoit]] | Leads global pre-sales SE organization | VAST Data |

## Related People

- [[Rob Benoit]]
