---
type: people
title: Tomer Hagay
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Tomer Hagay

## Recent Context

- unknown: [[2025-11-4 - Planning sessions]] - Planning notes for a set of sessions with Jeff Denworth to align on VAST’s cloud-first product strat... (via Jeff Denworth)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Shachar Feinblit]] - Checklist and Slack snippets related to coordinating with Shachar Feinblit, including setting up rec... (via Shachar Feinblit)
- unknown: [[2025-10 - Tomer Hagay]] - Completed follow-ups for Tomer Hagay to support Jason by sharing FRD templates/examples and providin...
- unknown: [[Global Namespace]] - A completed action item to review and align the 5.5 Global Namespace write-lease design and read red... (via 5.5 Features)
- unknown: [[2025-10 - Pricing Tasks]] - Checklist of completed pricing workstreams for cloud/private offers, discount policy, normalization ... (via Pricing)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and immediate priorities. Jeff highlighted key pla]] - 1:1 discussion with Jeff Denworth reviewing VAST org landscape, immediate priorities, and a pragmati... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i]] - 1:1 strategy sync with Jonsi Stephenson aligning VAST’s hyperscaler approach across Google and Micro... (via Jonsi Stephenson)
- 2025-11-07: [[2025-11-07 - Jason and Tomer aligned on the need to introduce clearer product management disc]] - Jason Vallery and Tomer Hagay discussed gaps in VAST’s product management discipline (OKRs/KRs, trac...
- 2025-11-03: [[2025-11-03 - Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN]] - Group meeting transcript reviewing how VAST cloud clusters must map to Salesforce assets (Account/Si... (via Cloud)
- 2025-10-31: [[2025-10-31 - Introductory 1-1 aligning on VAST’s cloud strategy. Jason outlined a vision for]] - Introductory 1:1 between Jason Vallery and Karl Vietmeier aligning on VAST’s cloud strategy, includi... (via Karl Vietmeier)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)

## Profile

**Role**: Leads field request triage team at VAST Data (Tel Aviv team)
**Location**: Tel Aviv
**Relationship**: Internal collaborator (PM)

**Background**:
- PM perspective: very low PM-to-engineer ratio (~4 PMs / ~400 engineers); need Cloud Design Qualifiers; Slack support should not become backlog funnel; global namespace write leases preview in 5.5.
- Listed as a candidate for weekly/monthly 1:1 cadence.
- Tagged to help ask Shachar to confirm AI-first development mandate, training cadence, and measurable adoption targets.

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

## Key Decisions

- ✅ Transact exclusively through cloud marketplaces for MVP (no BYOL).
- ✅ Use Tackle.io to generate and manage private offers integrated with Salesforce.
- ✅ MVP pricing based on fixed capacity at $0.07/GB.
- ✅ Polaris will manage entitlement, call-home registration, and usage reporting.
- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.

## Related Customers

- [[Microsoft]]
- [[Dell]]
- [[Google]]
- [[NBCU]]

## Related Projects

- [[Pricing]]
- [[Confluence FRDs taxonomy]]
- [[Cloud]]
- [[5.5 Features]]
- [[OVA]]

## Related

<!-- Wikilinks to related entities -->
