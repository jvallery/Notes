---
type: people
title: Cloud pricing alignment debate
date: '2025-10-27'
person: Tomer
participants:
- Tomer
- Jason Vallery
- Yancey
- Wolfie
- Lior Genzel
- Eiki
- Eric
- Timo
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-27 - The team debated how to align cloud
  pricing with the new on‑prem model. Two opti.md
tags:
- type/people
- person/tomer
- generated
---

# Cloud pricing alignment debate

**Date**: 2025-10-27
**With**: Tomer, Jason Vallery, Yancey, Wolfie, Lior Genzel, Eiki, Eric, Timo

## Summary

The group debated how to align cloud pricing with the upcoming on-prem core+capacity model given large cross-cloud differences in vCPU density and infrastructure costs. They converged on launching cloud private offers with capacity-only pricing and stricter discount guidance, while targeting a broader unified pricing model decision by 2026-02-01 and reaffirming a three-phase GTM (private offers now, public PAYGO in ~6 months, full SaaS likely FY28). They rejected disabling/rate-limiting excess vCPUs and focused near-term on delivering an NBCU TCO and defining marketplace entitlements/discounts (notably for Google private offers).
## Action Items
- [?] Propose cloud private-offer pricing structure and discount guidance (capacity-only) for immediate use by field. @Tomer Hagay 📅 2025-10-27 🔺 #task #proposed
- [?] Forward NBCU TCO call invite to the core group (Jason, Lior, Eiki, Tomer, Wolfie, Eric). @Yancey 📅 2025-10-27 🔺 #task #proposed
- [?] Join and support NBCU TCO working session; align on inputs (reserved pricing, egress, infra COGS). @Eric 📅 2025-10-27 🔺 #task #proposed
- [?] Join NBCU TCO working session; validate pricing approach and competitive posture. @Myself 📅 2025-10-27 ⏫ #task #proposed
- [?] Add core stakeholders to NBCU TCO sync invite. @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed
- [?] Define and publish a cloud-specific discount policy for private offers to avoid extreme discounts. @Pricing vTeam 📅 2025-10-27 🔺 #task #proposed
- [?] Complete NBCU TCO analysis and share with customer by Wednesday. @Eric 📅 2025-10-29 ⏫ #task #proposed
- [?] Decide whether to introduce fixed cores-per-PB normalization for cloud starting Feb 1 and document the model. @Pricing vTeam 📅 2025-10-27 🔺 #task #proposed
- [?] Define marketplace entitlements and pricing schema for Google private offer and begin approval process. @Yancey 📅 2025-10-27 🔺 #task #proposed
- [?] Plan and document a unified Feb 1 pricing rollout that keeps on-prem and cloud consistent. @Tomer Hagay 📅 2026-02-01 🔺 #task #proposed

## Decisions
- Launch cloud private offers with capacity-only pricing in the near term.
- Do not disable or rate-limit vCPUs in cloud instances; any normalization should be commercial rather than technical.
- Reaffirm three-phase GTM: private offers in customer tenants now, public PAYGO offers in ~6 months, and full SaaS later (likely FY28).
- Proceed with marketplace private offers (AWS, Azure, GCP, OCI) before public offers.
- Target 2026-02-01 for a broader pricing model decision/rollout to better align on-prem and cloud.

## Key Information
- Instance core density varies widely across hyperscalers, making raw core-based cloud pricing inconsistent unless normalized.
- Network limits (e.g., ~100 Gbps east-west) can cap performance; additional cores may not translate to throughput gains.
- Cloud infra COGS for NVMe VMs is high (~$0.15–$0.30/GB/month), so early cloud use cases are expected to be primarily burst.
- Initial market reference discussed: cloud capacity list around ~$0.07/GB/month; on-prem list rework targets ~$13/TB with a core component.
- Customers and use cases referenced include NBCU, Two Sigma, UK Met Office, and Zoom on OCI; hybrid ELAs and marketplace burn-down are important.
- Marketplace entitlement/schema changes can take ~3 weeks for approvals, creating launch timing risk.

---

*Source: [[Inbox/_archive/2025-10-27/2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti.md|2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti]]*

## Related

- [[Tomer]]
- [[Jason Vallery]]
- [[Lior Genzel]]
- [[Eric Wolfie]]
- [[Timo Pervane]]
- [[Pricing]]
- [[Cloud control plane]]
- [[5.5 Features]]
- [[Microsoft ROI Data Usage Validation]]
- [[Google]]
- [[Microsoft]]
- [[Amazon]]
- [[Oracle]]
- [[Databricks]]
- [[NetApp]]
- [[NBCU]]
- [[Two Sigma]]
- [[Zoom]]
- [[Intel]]
- [[Western Digital]]
- [[CoreWeave]]