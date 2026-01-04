---
type: people
title: Timo Pervane
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Timo Pervane

## Recent Context

- unknown: [[2025-10 - Pricing Tasks]] - Checklist of completed pricing workstreams for cloud/private offers, discount policy, normalization ... (via Pricing)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-30: [[2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor]] - Group meeting to align the cloud support operating model (Customer Success, Support, SRE), hyperscal... (via Cloud)
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]] - Internal group meeting to finalize the MVP launch plan for VAST on Google Cloud Marketplace using pr... (via Google)
- 2025-10-28: [[2025-10-28 - Introductory 1-1 covering backgrounds, finance org context, and cloud solutions]] - Introductory 1:1 between Jason Vallery and Timo Pervane focused on finance org context, Cloud Soluti...
- 2025-10-27: [[2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]] - Group meeting transcript debating how to align VAST cloud pricing with the new on-prem core+capacity... (via Pricing)

## Profile

**Role**: Meeting participant at VAST Data (Corporate Finance)
**Location**: Boston area
**Relationship**: Internal finance partner

**Background**:
- Finance partner driving ARR/valuation framework, discount controls, pricing analysis datasets, and hiring a Finance Business Partner for Cloud Solutions.
- Partnering with Jason on cloud business models, pricing, and legal.
- Raises legal/compliance considerations and need for resourcing; asks about marketplace metering and billing mechanics; notes public-company internal controls/auditor scrutiny of metering engine.

## Key Decisions

- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Prioritize hyperscalers: GCP first, Azure second, AWS third.
- ✅ Proceed with phased rollout: private offer → public offer (6–8 months later) → SaaS in FY28.
- ✅ Adopt separated functions for Customer Success, Support, and SRE with 24/7 support coverage.

## Key Facts

- MVP launch on GCP uses private offers with fixed capacity pricing ($0.07/GB) via GCP Marketplace.
- Tackle.io is the middleware to generate private offers and sync them with Salesforce opportunities.
- Polaris is the source of truth for entitlements and metering; clusters call home to Polaris and enforce entitlements via tokens (no license keys).
- No BYOL for MVP; all transactions go through marketplaces to support hyperscaler partner status and MDF/marketing benefits.
- Considering ~10% overage allowance; goal is to charge overage at list PAYGO, but GCP Marketplace may not support this natively.
- Internal CS/sales alerting for entitlement usage/overage is not yet in place; customer alert exists.
- First GCP transactions targeted for Nov–Dec 2025; plan to replicate approach to AWS/Azure afterward.
- Finance will not have a separate cloud P&L; cloud metrics will be reported within overall P&L; SaaS/consumption metrics and forecasting model must be defined before full SaaS launch.
- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement/training plus PM augmentation, and marketing support.
- Documentation is currently feature/button-oriented and not scenario-driven; scenario guides are ad hoc and late.

## Topics

GCP Marketplace MVP launch scope (private offers, fixed capacity, no BYOL), Tackle.io integration with Salesforce for private offers, Polaris entitlements, metering, call-home, and Uplink registration automation, Overage policy and GCP marketplace limitations; PAYGO overage workaround, EULA language requirements for overage billing, Finance processes: billing, payout cadence, reconciliation, reporting controls, rev rec, Future pricing model: VAST units of measurement for compute/capacity, Hybrid on-prem/cloud conversion and revenue recognition complexity, Multi-cloud pooling feasibility and hyperscaler positioning concerns, Need for cloud customer success coverage and internal usage alerting, Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics

## Related Customers

- [[Microsoft]]
- [[Shopify]]
- [[Oliver Wyman]]

## Related Projects

- [[Pricing]]
- [[Cloud]]

## Related

<!-- Wikilinks to related entities -->
