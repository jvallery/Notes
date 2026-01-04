---
last_contact: '2025-11-14'
---
---
type: projects
title: "Fort Meade "Gemini as a service" on-prem validation"
created: "2026-01-03"
last_updated: ""
status: "active"
auto_created: true
tags:
  - type/projects
  - needs-review
  - status/active
---

# Fort Meade "Gemini as a service" on-prem validation

## Overview

In-flight Fort Meade initiative to run Gemini on-prem ("Gemini as a service") as a rapid joint validation/reference for air-gapped GDC; described as a Q4 commit and double-digit PB opportunity.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Greg Castellucci |

## Current Blockers

- ❌ Rack-and-stack/location approval and equipment availability coordination between Google and Cisco

## Next Steps

- [ ] Coordinate with Google/Cisco on rack-and-stack progress and confirm validation scope for Q4
- [ ] Confirm whether Fort Meade status can be cited in the RFP as active validation

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jennifer Azzolina]] |  | VAST Data |
| [[Jan Niemus]] | Runs DoD/IC organization | Google |
| [[Alon Horev]] |  |  |
| [[Randy Hayes]] |  | VAST Data |
| [[Greg Castellucci]] |  | VAST Data |
| [[Muninder Singh Sambi]] | Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) | Google |

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.

## Topics / Themes

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track

## Related People

- [[Jennifer Azzolina]]
- [[Jan Niemus]]
- [[Alon Horev]]
- [[Randy Hayes]]
- [[Greg Castellucci]]
- [[Muninder Singh Sambi]]

## Related Customers

- [[Dell]]
- [[Cisco]]
- [[Google]]
- [[HPE]]

## Recent Context

- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)

## Artifacts

```dataview
TABLE file.mtime as "Modified"
FROM ""
WHERE type != "readme" AND type != "projects"
SORT file.mtime DESC
```

---
*Last updated: *