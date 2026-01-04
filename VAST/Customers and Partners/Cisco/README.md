---
type: customer
title: Cisco
created: '2026-01-03'
last_contact: '2025-11-14'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Cisco

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

- ❌ POC equipment/location approval and rack-and-stack delays
- ❌ Need to confirm Cisco SP team alignment and identify qualified opportunities
- ❌ Need to confirm whether Google intends to procure via Cisco and expected commercial model
- ❌ Potential misunderstanding/education gap with Cisco networking teams about VAST southbound switch constraints (buffering; clients must not connect).

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

- Cisco gear-based POC with Google DoD/IC and Fort Meade validation path
- Joint pursuit of VAST-qualified opportunities pending Cisco SP team alignment
- Channel/partner path for GDC RFP procurement (Google potentially procuring VAST via Cisco for GDC deployments)
- Referenced as a comparison point for customer events and as a networking ecosystem where partners may assume clients can connect to southbound switches.
- Referenced as example OEM/hardware partner type for Azure Dedicated-style specs
- Referenced as prior employer context for structured processes

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ P0 priority: enable capacity scaling independent of performance via object/S3 offload for cloud viability.
- ✅ Cloud team should spearhead GDC/neo-cloud single-tenant GPU-adjacent storage opportunities, coordinating required integrations.
- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Jason Vallery recently took on cloud product responsibility reporting to Jeff Denworth; vision is a planet-scale multi-tenant/SaaS platform across hyperscalers and neo-clouds.
- Karl Vietmeier is a hands-on Linux/distributed-systems specialist with strong automation skills (bash/PowerShell/Terraform/Ansible; some Python) and uses AI tools heavily for productivity.
- A GDC RFP surfaced via Cisco; success requires integration with Google control plane (APIs, monitoring, billing).

## Topics / Themes

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, VAST cloud strategy and multi-tenant SaaS vision, Google Distributed Cloud (GDC) RFP via Cisco, Control-plane integrations (API/monitoring/billing), Single-tenant GPU-adjacent storage patterns for neo-clouds, Global namespace portability and avoiding data gravity

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - The team aligned on a go-to-market strategy with global SIs focused on enterpris]] - GSI Team aligned on a go-to-market strategy with global SIs centered on enterprise workflow automati... (via GSI Team)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
- 2025-10-30: [[2025-10-30 - Weekly SE community call covering end-of-quarter push, Tech Summit logistics, an]] - Weekly SE community call focused on end-of-quarter execution, Tech Summit logistics/expense policy, ... (via SRE)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on improving VAST engineering maturity and ... (via Tomer Hagay)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Greg Castellucci]] |  | VAST Data |
| [[John Cedillo]] |  |  |

## Related People

- [[Greg Castellucci]]
- [[John Cedillo]]
