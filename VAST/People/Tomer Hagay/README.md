---
type: people
title: Tomer Hagay
last_contact: '2025-10-28'
created: '2026-01-03'
tags:
- type/people
- generated
---

# Tomer Hagay

## Recent Context

- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Group meeting aligning on an MVP launch on Google Cloud Marketplace using private offers with fixed ... (via Google)

## Profile

**Role**: Product/pricing stakeholder
**Relationship**: Internal collaborator

**Background**:
- Owner for defining overage policy and units of measurement for future pricing model (compute/capacity).

## Key Facts

- MVP pricing is $0.07/GB capacity with fixed term/fixed price via Google Cloud Marketplace private offers.
- All MVP transactions go through marketplaces; BYOL is explicitly excluded for MVP.
- Tackle.io is used as middleware to generate private offers and sync them with Salesforce opportunities.
- Polaris is the source of truth for entitlements, usage, and metering; entitlements enforced via tokens (no license keys).
- Considering ~10% overage allowance; goal is to charge overage at PAYGO list price, but GCP Marketplace may not support this natively.
- EULA language must explicitly cover overage billing terms in marketplace offers.
- Customer alerting exists for exceeding limits; internal CS/sales alerting was identified as missing and needed.
- First GCP transactions targeted for Nov–Dec, with intent to replicate approach to other hyperscalers afterward.
- Finance will not have a separate cloud P&L; cloud metrics will be reported within overall P&L, and SaaS/consumption metrics need definition before SaaS launch.

## Topics

GCP Marketplace MVP launch scope (private offers, no BYOL), Fixed capacity pricing and $0.07/GB list price, Tackle.io integration with Salesforce for private offers, Polaris entitlements, call-home, metering, and token enforcement, Overage policy (10% allowance) and PAYGO list pricing workaround, Marketplace EULA language for overage billing, Internal alerting/dashboards for CS/sales on entitlement usage, Finance processes: billing, payout cadence, reconciliation, rev rec, Hybrid on-prem/cloud conversion and revenue recognition complexity, Multi-cloud pooling feasibility and hyperscaler messaging concerns, Unit-based pricing model for compute/capacity

## Key Decisions

- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.

## Related Customers

- [[Google]]

## Related Projects

- [[Pricing]]
- [[Cloud]]

## Related

<!-- Wikilinks to related entities -->
