---
type: customer
title: Anthropic
created: '2026-01-03'
last_contact: '2025-11-14'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Anthropic

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | Artificial Intelligence |

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

- ❌ Prior outreach via investor path declined/stalled; Microsoft/Oracle-linked mutuals may be off-limits.
- ❌ No established door yet; capacity allocation dynamics may constrain

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

- Referenced as using Google TPU technology; context for TPU track
- Referenced as example of Google on-prem TPU hardware deal lacking surrounding software stack; motivates GDC direction
- Ongoing attempts to find the right entry point; multiple mutuals exist but quality varies.
- Mentioned competitively: Data Engine unlikely to be deciding factor vs Weka; storage-led win more likely
- Hyperscaler-scale engagement track (mentioned as target whale)
- Mentioned as fastest-growing model sales on Azure (context for Microsoft diversification beyond OpenAI)
- Referenced as AI tooling example (Claude agents) used for modern dev workflows

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

## Topics / Themes

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Org map and key leaders/roles, Cross-cloud platform strategy and homogenization across providers, Cloud GTM plays and integrations (Foundry/Bedrock/Vertex), Cataloging in-flight deals by product requirements, Control-plane partnerships and 'cloud-in-a-box' for Tier-2 clouds

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-11-06: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]] - Review of updated AI pipeline slides for an upcoming VAST SE Tech Summit, covering model training (c... (via AI Pipelines Collateral)
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] - Cloud BU leadership aligned on a dual-track cloud strategy: ship a near-term GCP marketplace MVP wit... (via Cloud)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on improving VAST engineering maturity and ... (via Tomer Hagay)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related People

- [[Jason Vallery]]
