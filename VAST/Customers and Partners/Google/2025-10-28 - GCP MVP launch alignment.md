---
type: customer
title: GCP MVP launch alignment
date: '2025-10-28'
account: Google
participants:
- Eirikur Hrafnsson
- Helen Protopapas
- Jason Ainsworth
- Jonsi Stephenson
- Lihi Rotchild
- Lior Genzel
- Timo Pervane
- Tomer Hagay
- Jason Vallery
- Yancey
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-28 - Team aligned on MVP launch on GCP
  via private offers with fixed capacity pricing.md
tags:
- type/customer
- account/google
- generated
---

# GCP MVP launch alignment

**Date**: 2025-10-28
**Account**: [[Google]]
**Attendees**: Eirikur Hrafnsson, Helen Protopapas, Jason Ainsworth, Jonsi Stephenson, Lihi Rotchild, Lior Genzel, Timo Pervane, Tomer Hagay, Jason Vallery, Yancey

## Summary

Team aligned on launching an MVP on Google Cloud Marketplace using private offers with fixed capacity pricing ($0.07/GB) and no BYOL. Tackle.io will generate private offers integrated with Salesforce, while Polaris will be the source of truth for entitlements, call-home registration, and usage/metering. Key open items include finalizing overage handling (including GCP marketplace limitations), EULA language, and finance processes for billing/reconciliation ahead of first transactions targeted for Nov–Dec.
## Action Items
- [ ?] Review and draft marketplace EULA language to enable overage billing at list PAYGO via Tackle workaround @Myself 📅 2025-11-08 🔺 #task #proposed
- [ ?] Invite finance (Jason Vallery) to Tackle kickoff and ongoing implementation meetings @Eirikur Hrafnsson 📅 2025-10-29 🔺 #task #proposed
- [ ?] Confirm with Tackle.io the feasibility and configuration for overage handling and pricing on GCP @Eirikur Hrafnsson 📅 2025-11-08 🔺 #task #proposed
- [ ?] Implement automation to create Uplink organization endpoints from Salesforce metadata for call-home registration @Polaris team 📅 2025-11-08 🔺 #task #proposed
- [ ?] Design and implement internal alerting for CS/sales when customers approach or exceed entitlement @Polaris team 📅 2025-11-08 🔺 #task #proposed
- [ ?] Define overage policy (thresholds, grace, pricing) and reflect in offer terms and EULA @Tomer Hagay Hagay 📅 2025-11-08 🔺 #task #proposed
- [ ?] Set up finance processes for marketplace billing, receivables reconciliation, and revenue recognition for fixed capacity and overages @Finance 📅 2025-11-08 🔺 #task #proposed
- [ ?] Provide finance with access to GCP marketplace reporting/portal and sample/mock payout reports @Eirikur Hrafnsson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Schedule and run a detailed walkthrough of the Tackle-to-Salesforce private offer flow and data sync @Eirikur Hrafnsson 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Define VAST units of measurement for compute and capacity for future pricing model @Tomer Hagay Hagay 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Plan for cloud customer success coverage to drive expansion and manage entitlement/usage @Lihi Rotchild 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Prepare pipeline visibility for expected first GCP transactions and timelines @Lior Genzel Genzel 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Validate GCP overage-at-PAYGO approach and confirm Tackle configuration path @Myself 📅 2025-11-08 🔺 #task #proposed
- [ ?] Set session to define billing, invoicing, payout cadence, and reconciliation across Polaris, Tackle, and GCP @Finance 📅 2025-11-08 🔺 #task #proposed
- [ ?] Decide whether to permit automatic expansion beyond entitlement or require account approval @Product 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Outline rev rec approach for future hybrid conversion model (on-prem ↔ cloud) @Finance 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Assess feasibility and policy for multi-cloud pooling and metadata roll-up to Salesforce @Polaris team 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Transact exclusively through cloud marketplaces for MVP (no BYOL).
- Use Tackle.io to generate and manage private offers integrated with Salesforce.
- MVP pricing based on fixed capacity at $0.07/GB.
- Polaris will manage entitlement, call-home registration, and usage reporting.

## Key Information
- MVP launch on GCP will use private offers only with fixed term/fixed price capacity pricing; no BYOL.
- Private offers will be generated via Tackle.io and synced to Salesforce opportunities/metadata.
- Polaris is the source of truth for entitlements, metering, and usage reporting; clusters call home to Polaris and entitlements are enforced via tokens (no license keys).
- Considering ~10% overage allowance; overage ideally charged at list PAYGO, but GCP Marketplace lacks native support and may require a Tackle workaround plus EULA language.
- Customer alerting exists for exceeding limits; internal CS/sales alerting and dashboards are not yet in place.
- Hybrid on-prem/cloud conversion introduces complex revenue recognition; a conversion model may be needed later.
- Multi-cloud is technically possible, but hyperscalers may resist cross-cloud messaging.
- First GCP transactions targeted for Nov–Dec; plan is to replicate approach to AWS/Azure afterward.
- Finance will not have a separate cloud P&L; cloud metrics will be reported within overall P&L.
- Consumption/usage-based SaaS metrics and forecasting model must be defined before full SaaS launch.

---

*Source: [[Inbox/_archive/2025-10-28/2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing.md|2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]]*

## Related

- [[Amazon]]
- [[Microsoft]]
- [[Oracle]]
- [[NetApp]]
- [[Snowflake]]
- [[Databricks]]
- [[Eirikur Hrafnsson]]
- [[Helen Protopapas]]
- [[Jason Ainsworth]]
- [[Jonsi Stephenson]]
- [[Lihi Rotchild]]
- [[Lior Genzel]]
- [[Timo Pervane]]
- [[Tomer Hagay]]
- [[Eric Wolfie]]
- [[Ronen Cohen]]