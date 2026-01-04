---
type: customer
title: McDonald's
created: '2026-01-03'
last_contact: '2025-11-14'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# McDonald's

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Active |
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

- ❌ Edge/minimal-footprint deployments not feasible for VAST to serve directly

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

- Referenced as marquee GDC customer (connected variant) demonstrating GDC footprint
- Referenced as large Google deal with minimal-footprint edge deployments; noted as not a fit for VAST current footprint

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Pursue deeper integration with Google Distributed Cloud and aim to be part of the GDC SKU.
- ✅ Treat Microsoft Azure as a distinct sell-to motion (first-party/Storage HW) separate from marketplace sell-through.
- ✅ Use real-workload benchmarks (not synthetic) as the standard for TPU/storage evaluations with Google.

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Google Distributed Cloud (GDC) is emerging as the vehicle for on-prem TPU deployments and tie-back to GCP.
- Only VAST and NetApp are present as file options on GDC; NetApp relies on revived OnTap Select.
- VAST TPU testing using Google-provided model set reportedly showed ~20% improvement over Google’s managed Lustre stack.

## Topics / Themes

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Google Distributed Cloud (GDC) strategy for on-prem TPUs, TPU benchmark results vs managed Lustre and demo outcomes, Walmart Google project and potential repatriation trajectory, Microsoft Project Apollo control plane and timeline, MAI Falcon April deployment risk and Azure Storage HW approach

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-09-29: [[2025-09-29 - Jason shared disappointment with his rewards and anxiety about scope and support]] - Weekly 1:1 between Maneesh Sah and Jason Vallery focused on Jason’s dissatisfaction with rewards, re... (via Maneesh Sah)

## Related People

_Internal team members working on this account..._


---
*Last updated: *