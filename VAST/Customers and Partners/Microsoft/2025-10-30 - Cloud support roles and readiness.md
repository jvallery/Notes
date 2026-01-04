---
type: customer
title: Cloud support roles and readiness
date: '2025-10-30'
account: Microsoft
participants:
- Jason Vallery
- Lior Genzel
- Daniel
- Rob Banga
- Yancey
- Timo Pervane
- Joe
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-30 - The group aligned on establishing
  distinct Customer Success, Support, and SRE ro.md
tags:
- type/customer
- account/microsoft
- generated
---

# Cloud support roles and readiness

**Date**: 2025-10-30
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Lior Genzel, Daniel, Rob Banga, Yancey, Timo Pervane, Joe

## Summary

Team aligned on a distinct Customer Success (proactive), Support (reactive), and SRE (24/7 operations) model for hyperscaler cloud deployments, with near-term prioritization on Azure/Microsoft opportunities. Key dependencies include Tackle–Salesforce–Polaris integration, improved Salesforce data hygiene and access controls, and defined telemetry/analytics surfaced in Tableau. Compliance/legal implications of becoming a data custodian (including SOC2/FedRAMP path) and enablement/documentation for SKO were highlighted, with an operational readiness target of 2026-02-01.
## Action Items
- [ ] Draft and circulate a simple cloud support plan covering CS/Support/SRE responsibilities, 24/7 coverage, and phasing; circulate for feedback. @Rob Banga 📅 2025-11-08 🔺 #task
- [ ] Start recruiting initial SRE and cloud support hires to meet cloud support readiness needs. @Rob Banga 📅 2025-11-08 🔺 #task
- [ ] Sync offline on CS/Support/SRE model and on-call rotations. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Define Tableau telemetry/analytics for cloud customers (e.g., churn, feature usage) and required data feeds. @Yancey 📅 2025-11-08 ⏫ #task
- [ ] Plan Tackle–Salesforce–Polaris integration for marketplace offers, customer registration, and entitlements/role management. @Yancey 📅 2025-11-08 🔺 #task
- [ ] Confirm leadership for cloud implementations (align with Carl and scope the team). @Rob Banga 📅 2025-11-08 ⏫ #task
- [ ] Prepare enablement and documentation for SEs, Support, and CS, including SKO content. @Product Marketing 📅 2025-11-08 ⏫ #task
- [ ] Define metering evidence and internal control requirements with Finance and auditors for Polaris data. @Finance 📅 2025-11-08 🔺 #task
- [ ] Outline overage policy and SaaS pricing unit model options with Jason. @Yancey 📅 2025-11-08 ⏫ #task
- [ ] Schedule and run a Salesforce/Tackle deep-dive to understand current flows and gaps. @Christina 📅 2025-10-31 🔺 #task
- [ ] Meet offline to refine org design and rotations. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Conduct legal review covering data custodian obligations, EULA updates, and compliance roadmap (SOC2, FedRAMP). @Legal 📅 2025-11-08 🔺 #task
- [ ] Attend GCP meeting to review TPU test setup and defend results. @Lior Genzel Genzel 📅 2025-11-04 ⏫ #task
- [ ] Validate Salesforce access/role model for customers and internal users; define data hygiene rules and validation. @Sales Operations 📅 2025-11-08 🔺 #task
- [ ] Confirm hyperscaler prioritization and target account list for near-term execution. @Yancey 📅 2025-11-08 ⏫ #task

## Decisions
- Adopt distinct Customer Success, Support, and SRE model for cloud deployments (including 24/7 SRE rotation).
- Prioritize Azure opportunities in the near term due to demand and large opportunities.
- Use Polaris as the metering source of truth with hourly usage reporting.
- Reaffirm phased go-to-market: private offers first, public offers 6–8 months later, full SaaS targeted for FY28.
- Cover cloud enablement and messaging at SKO.

## Key Information
- Target operational readiness for cloud support is 2026-02-01.
- Private and public marketplace offers are deployed in the customer tenant; SaaS introduces a materially different operational/legal model.
- Polaris is the metering source of truth; marketplace requirements include hourly utilization reporting.
- Tackle–Salesforce–Polaris integration is required for marketplace flows, customer registration, and entitlement/role management.
- Expected support shift: fewer hardware issues but more networking-related complexity/tickets in cloud deployments.
- Compliance considerations include data custodianship, access controls, and likely SOC2/FedRAMP path; SaaS may require a different EULA.
- Initial target accounts discussed include Microsoft (MAI, UKMET, NBCU, Microsoft internal), Google (Sigma, Jump Trading, Citadel), and AWS (Zoom exploratory).
- Private offers expected to be fixed capacity with an overage model under definition; longer-term SaaS pricing may use a unit-based model with multipliers.

---

*Source: [[Inbox/_archive/2025-10-30/2025-10-30 - The group aligned on establishing distinct Customer Success, Support, and SRE ro.md|2025-10-30 - The group aligned on establishing distinct Customer Success, Support, and SRE ro]]*

## Related

- [[Rob Banga]]
- [[Jason Vallery]]
- [[Lior Genzel]]
- [[Timo Pervane]]
- [[Google]]
- [[Amazon]]
- [[NBCU]]
- [[Zoom]]
- [[OpenAI]]
