---
type: people
title: Cloud support operating model alignment
date: '2025-10-30'
person: Rob Banga
participants:
- Jason Vallery
- Lior Genzel
- Yancey
- Rob Banga
- Daniel
- Timo Pervane
- Christina
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-30 - The group aligned on the cloud
  support operating model (Customer Success, Suppor.md
tags:
- type/people
- person/rob-banga
- generated
---

# Cloud support operating model alignment

**Date**: 2025-10-30
**With**: Jason Vallery, Lior Genzel, Yancey, Rob Banga, Daniel, Timo Pervane, Christina

## Summary

The group aligned on a cloud support operating model separating Customer Success, reactive Support, and 24/7 SRE on-call, with operational readiness targeted for 2026-02-01. They confirmed hyperscaler prioritization (GCP first, Azure second, AWS third), a phased marketplace rollout (private offers then public offers), and identified key gating workstreams including hiring, Salesforce/Tackle/Polaris integrations, analytics/telemetry, and legal/compliance (SOC2/FedRAMP, data custodian obligations). A follow-up is needed to address GCP’s challenge to TPU test results and to finalize enablement/documentation for SKO.
## Action Items
- [?] Draft a clear cloud support/Customer Success/SRE operating plan including 24/7 support desk and on-call rotations for marketplace phases, and bring back to this group for review. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed
- [?] Begin recruiting initial SREs and support engineers with hyperscaler experience (GCP/Azure/AWS). @Rob Banga 📅 2025-11-08 ⏫ #task #proposed
- [?] Schedule an offline working session with Rob to detail the SRE/support model and lessons learned from Microsoft/OCI. @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Schedule a Salesforce/Tackle integration deep-dive covering customer registration, entitlements, and data flows. @Christina 📅 2025-10-31 ⏫ #task #proposed
- [?] Define telemetry and metrics to push from Polaris to Tableau for churn, feature utilization, and cloud customer health views. @Yancey 📅 2025-11-08 ⏫ #task #proposed
- [?] Scope reporting and analytics needed for consumption forecasting and ensure resourcing. @Joe 📅 2025-11-08 ⏫ #task #proposed
- [?] Assess and confirm additional Salesforce and Tableau licenses/seats needed for cloud operations. @Timo Pervane Pervane 📅 2025-11-08 ⏫ #task #proposed
- [?] Evaluate Carl as the initial leader for cloud implementation/support and define the team structure. @Rob Banga 📅 2025-11-08 ⏫ #task #proposed
- [?] Propose a role-based access and data segmentation model across Salesforce, Polaris, and support tooling. @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Prepare an enablement and documentation plan for end-customer and sell-to-hyperscaler motions (including SKO content). @Product Marketing 📅 2025-11-08 ⏫ #task #proposed
- [?] Consolidate notes and circulate action items from this session. @Daniel 📅 2025-10-31 🔽 #task #proposed
- [?] Initiate a legal/compliance workstream to define data custodian obligations for SaaS and the path to SOC2/FedRAMP. @Legal 📅 2025-11-08 ⏫ #task #proposed
- [?] Attend the GCP meeting to defend TPU test methodology and results (with Nirav and Rich Shanshee). @Yancey 📅 2025-11-08 ⏫ #task #proposed
- [?] Confirm target customer list and POC sequencing by hyperscaler (Microsoft, UKMET, NBCU, Sigma, Jump Trading, Citadel, Zoom). @Yancey 📅 2025-11-08 ⏫ #task #proposed
- [?] Define overage policy mechanics for private offers (thresholds, pricing, billing). @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Detail metering, entitlement, and billing integration flows between Polaris, hyperscaler marketplaces, and ERP. @Yancey 📅 2025-11-08 ⏫ #task #proposed
- [?] Plan SKO sessions for cloud go-to-market, support model, and SE enablement. @Benoit 📅 2025-11-08 ⏫ #task #proposed

## Decisions
- Prioritize hyperscalers in this order: GCP first, Azure second, AWS third.
- Proceed with a phased rollout: private offers first, then public offers 6–8 months later, with full SaaS targeted in FY28.
- Adopt separated functions for Customer Success (proactive), Support (reactive), and SRE (24/7 on-call break/fix).
- Target operational readiness for the cloud support model by 2026-02-01.

## Key Information
- Marketplace rollout plan: private offers begin ~2 months after the meeting; public offers follow 6–8 months later; full SaaS is targeted for FY28.
- Initial cloud delivery is deployed in the customer tenant (not VAST-hosted SaaS), with no hardware involved; networking complexity is expected to drive ticket volume.
- Tackle integration with Salesforce is a gating dependency; Polaris is the source of truth for metering and billing.
- Metering is planned as hourly utilization with aggregation for hyperscalers and ERP; auditors will scrutinize the metering engine as evidence of delivery.
- Analytics in Tableau are needed for churn, feature usage, customer health, and consumption forecasting.
- Legal/compliance needs include defining data custodian obligations for SaaS and establishing a SOC2/FedRAMP roadmap.
- Candidate/target customers discussed include Microsoft (including MAI), UKMET (via Microsoft), NBCU, Sigma, Jump Trading, Citadel, and Zoom (AWS exploration).
- GCP challenged TPU test results (claimed ~23% better than their Managed Lustre); a review meeting is being set up with Nirav and Rich Shanshee.

---

*Source: [[Inbox/_archive/2025-10-30/2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor.md|2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor]]*

## Related

- [[Rob Banga]]
- [[Jason Vallery]]
- [[Lior Genzel]]
- [[Timo Pervane]]
- [[Amy Hood]]
- [[Kanchan Mehrotra]]
- [[Rick Scurfield]]
- [[Ms. Ross]]
- [[Cloud control plane]]
- [[Google]]
- [[Microsoft]]
- [[Amazon]]
- [[Oracle]]
- [[SK]]
- [[NBCU]]
- [[Zoom]]