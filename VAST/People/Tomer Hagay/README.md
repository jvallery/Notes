---
type: people
title: Tomer Hagay
last_contact: '2025-12-01'
created: '2026-01-03'
tags:
- type/people
- generated
email: tomer.hagay@vastdata.com
company: VAST Data
---

# Tomer Hagay

## Profile

**Role**: Leads field request triage team at VAST Data (Tel Aviv team)
**Location**: Tel Aviv
**Relationship**: Internal collaborator (PM)

**Background**:
- PM perspective: very low PM-to-engineer ratio (~4 PMs / ~400 engineers); need Cloud Design Qualifiers; Slack support should not become backlog funnel; global namespace write leases preview in 5.5.
- Listed as a candidate for weekly/monthly 1:1 cadence.
- Tagged to help ask Shachar to confirm AI-first development mandate, training cadence, and measurable adoption targets.

## Open Tasks

```tasks
path includes Tomer Hagay
not done
```

## Recent Context

- 2025-10-01: Discussed FRD templates/examples and access to PM SFDC RFE/Feature dashboards and Jira links. [[2025-10-01 - FRD templates and access]]

- 2025-11-07: Discussed need for org-wide PM discipline (OKRs/KRs, epic-to-task traceability, RoB cadence) and plan to socialize a skunkworks proposal with leadership after Tel Aviv.

- 2025-10-29: PM-led cloud model alignment; agreed on PM-led cloud approach and FRD qualifiers checklist; follow-up planned for pricing + Salesforce walkthrough ([[2025-10-29 - PM-led cloud model alignment]])

- 2025-10-24: [[2025-10-24 - AI-first dev and cloud maturity]] (via VAST)

- 2025-10-28: [[2025-10-28 - GCP MVP launch alignment]] (via Google)

- 2025-10-01: [[Pricing vTeam action list]] (via Pricing)

- 2025-12-01: RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink

- 2025-12-15: Mentioned in: GDC RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support
## Key Facts

- Tomer Hagay stated that Violet is the expert for VAST encryption topics related to the Google Distributed Cloud (GDC) RFP follow-up.

- Tomer Hagay stated VAST prefers software-based encryption rather than relying on self-encrypting drive (SED) hardware capabilities or availability, and that software-based encryption can be FIPS certified.

- Tomer Hagay stated encryption keys in VAST are managed at the tenant level or at the path level, and that 'path' includes any protocol including S3 buckets and NFS exports.

- Tomer Hagay stated an encryption group can be assigned to a path to support having a unique encryption key for that path.

- Tomer Hagay stated VAST supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using x-amz-server-side-encryption-customer-* headers starting from VAST software version 5.4.

- Tomer Hagay asked where the self-encrypting drive (SED) requirement originates and noted that if SEDs are used to meet FIPS 140-3 data-at-rest encryption requirements for protection against drive removal, VAST software using FIPS-compatible encryption algorithms should meet the requirement.
## Topics

- RFE
- NVIDIA Corporation
- DGX Cloud
- VAST Data
- cluster visibility

- Google Distributed Cloud
- RFP
- encryption key granularity
- self-encrypting drives
- FIPS certification
## Key Decisions

## Related Customers

## Related Projects

## Related

<!-- Wikilinks to related entities -->

- [[NVIDIA Corporation]]
- [[DGX-C | Coreweave]]
- [[RFE 0482]]

- [[Google]]
- [[Google Distributed Cloud RFP]]