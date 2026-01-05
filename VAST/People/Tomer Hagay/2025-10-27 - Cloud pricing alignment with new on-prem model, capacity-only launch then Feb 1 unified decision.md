---
type: people
title: Cloud pricing alignment with new on-prem model, capacity-only launch then Feb 1 unified decision
date: '2025-10-27'
participants:
- Tomer Hagay
- Jason Vallery
- Yancey
- Eric Wolfie
- Lior Genzel
- Eiki
- Eric
- Timo Pervane
- Helen
- Eirikur Hrafnsson
- Unknown Remote Speaker
- Helen (Unknown)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-27 - The team debated how to align cloud pricing with the new on‑prem model. Two opti.md
tags:
- type/people
- generated
person: Tomer Hagay
---

# Cloud pricing alignment with new on-prem model, capacity-only launch then Feb 1 unified decision

**Date**: 2025-10-27
**Attendees**: Tomer Hagay, Jason Vallery, Yancey, Eric Wolfie, Lior Genzel, Eirikur Hrafnsson, Eric, Timo Pervane, Unknown Remote Speaker, Helen (Unknown)

## Summary

Internal pricing working session debated how to align VAST cloud pricing with the new on-prem core-plus-capacity model given hyperscaler instance core density differences. The team aligned on launching cloud private offers with capacity-only pricing and stricter discount guidance, while targeting a unified model decision by 2026-02-01. They also agreed not to disable or rate-limit excess vCPUs and prioritized an NBCU TCO deliverable plus marketplace entitlement definitions.

## Action Items

- [?] Propose a cloud private-offer pricing structure and discount guidance using capacity-only pricing for immediate field use. @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Forward the NBCU TCO working session invite to the core group (Jason Vallery, Lior Genzel, Eiki, Tomer Hagay, Eric Wolfie, Eric). @Yancey 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Join and support the NBCU TCO working session and align on inputs including reserved pricing assumptions, egress assumptions, and cloud infrastructure COGS. @Eric 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Join the NBCU TCO working session to validate the pricing approach and competitive posture for VAST cloud private offers. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Add core stakeholders to the NBCU TCO sync invite. @Tomer Hagay 📅 2025-10-27 #task #proposed #auto

- [?] Define and publish a cloud-specific discount policy for private offers to avoid extreme discounts and margin erosion. @Pricing vTeam 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Complete the NBCU TCO analysis and share it with NBCU by Wednesday 2025-10-29. @Eric 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Decide whether to introduce fixed cores-per-PB normalization for cloud pricing starting 2026-02-01 and document the model and rationale. @Pricing vTeam 📅 2026-02-01 ⏫ #task #proposed #auto

- [?] Define marketplace entitlements and pricing schema for a Google Cloud private offer and begin the approval process to avoid entitlement-change delays. @Yancey 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Plan and document a unified pricing rollout by 2026-02-01 that keeps on-prem and cloud pricing consistent, including how discounts and any normalization will be applied. @Tomer Hagay 📅 2026-02-01 ⏫ #task #proposed #auto

- [?] Forward the NBCU TCO working session invite to the core group (Jason Vallery, Lior Genzel, Eirikur Hrafnsson, Tomer Hagay, Eric Wolfie, Eric). @Yancey 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Join and support the NBCU TCO working session and align on inputs (reserved pricing, egress assumptions, and infrastructure COGS). @Eric 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Join the NBCU TCO working session and validate the pricing approach and competitive posture for VAST cloud private offers. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Define and publish a cloud-specific discount policy for private offers to avoid extreme discounts and margin erosion. @TBD 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Complete the NBCU TCO analysis and share it with NBCU by Wednesday, 2025-10-29. @Eric 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Decide whether to introduce fixed cores-per-PB normalization for cloud pricing starting 2026-02-01 and document the chosen model. @TBD 📅 2026-02-01 ⏫ #task #proposed #auto

- [?] Plan and document a unified pricing rollout for 2026-02-01 that keeps on-prem and cloud pricing consistent, including how list price and discount guidance will be applied. @Tomer Hagay 📅 2026-02-01 ⏫ #task #proposed #auto

- [?] Develop a public PAYGO marketplace offer within approximately 6 months, including consumption metering and billing requirements for customer-tenant deployments. @TBD 📅 2026-04-27 #task #proposed #auto

- [?] Plan a full multi-tenant SaaS offering (VAST-managed account model) and align pricing and COGS assumptions for a likely FY2028 timeframe. @TBD 📅 2028-06-30 🔽 #task #proposed #auto

- [?] Deepen competitive cloud pricing analysis versus Pure, NetApp, Isilon, WEKA, and Hammerspace, including pricing models and reference price points. @TBD 📅 2025-11-10 #task #proposed #auto

- [?] Evaluate feasibility and policy for an optional 'unlock all cores' add-on price in cloud while keeping the product behavior unchanged (no core disabling). @TBD 📅 2025-11-24 🔽 #task #proposed #auto

- [?] Assess using performance tiers (instance class or throughput per PB) to simplify cloud pricing communication without synthetic core units. @TBD 📅 2025-11-24 #task #proposed #auto

- [?] Investigate Azure Compute Unit or other cross-generation normalization metrics as potential future inputs to cloud pricing normalization. @Tomer Hagay 📅 2025-11-24 🔽 #task #proposed #auto

- [?] Define hybrid ELA conversion and deployment tracking across on-prem and cloud in Polaris/Uplink to support marketplace burn-down and entitlement management. @TBD 📅 2025-12-15 #task #proposed #auto

## Decisions

- Launch VAST cloud private offers using capacity-only pricing (no core-based charge) as the near-term model while broader pricing alignment work continues.

- Do not implement disabling or rate-limiting of excess vCPUs in cloud instances; any future core normalization will be handled commercially rather than via technical enforcement.

- Target a unified pricing model decision by 2026-02-01 to better align cloud pricing with the new on-prem core-plus-capacity model.

- Launch VAST cloud private offers using capacity-only pricing (no core-based charge) as the near-term model.

- Do not implement engineering changes to disable or rate-limit excess vCPUs in cloud instances; any core normalization must be commercial, not technical.

- Target 2026-02-01 as the decision point for a broader unified pricing rollout aligning on-prem and cloud (including deciding whether to adopt fixed cores-per-PB normalization or another approach).

- Proceed with marketplace private offers across AWS, Azure, GCP, and OCI before launching public offers.

## Key Information

- Jason Vallery started at VAST Data on Monday 2025-10-20 and was one week into the role as of 2025-10-27.

- VAST Data is changing the on-prem price list by lowering capacity list price, lowering core list price, and tightening discount levels, and the team validated the new numbers against historical opportunity data for the broader VAST business.

- Hyperscaler instance core density (vCPU per TB or cores per PB) varies significantly across instance types such as Azure LSv4 versus AWS i3en, which causes large price-per-TB swings if cloud pricing uses a core-based component without normalization.

- A proposed commercial normalization approach for cloud pricing is to charge a fixed normalized number of cores per petabyte (example discussed: 200 cores per PB) regardless of the actual vCPU count in the chosen cloud instances, to preserve cross-cloud parity and align with the on-prem core-plus-capacity model.

---

- Jason Vallery stated his first day at VAST Data was Monday, 2025-10-20, and he is based in the Boston area.

- Tomer Hagay explained that VAST Data is changing the on-prem price list by lowering capacity list price, lowering core list price, and reducing discount levels, and that the model was validated against historical opportunity/deal data for the broader VAST business.

- Tomer Hagay highlighted that hyperscaler instance core density (vCPU-to-core normalized) varies widely, which makes a core-based cloud pricing model produce materially different $/TB across clouds (example range cited roughly $41/TB to $80/TB depending on instance family such as Azure LSv4 vs AWS i3en).

- Tomer Hagay and Eric Wolfie discussed a commercial normalization approach for cloud pricing: charge a fixed, normalized number of cores per petabyte (example used 200 cores/PB) regardless of the actual instance vCPU count, to preserve cross-cloud parity and align with the on-prem core-plus-capacity model.

- The meeting summary states the team agreed to launch cloud with capacity-only pricing for private offers, provide stricter cloud discount guidance to the field, and target a unified pricing model decision by 2026-02-01.

- The meeting summary states the team rejected implementing technical controls to disable or rate-limit excess vCPUs, preferring any normalization to be commercial rather than engineering-enforced.

- The meeting summary states a three-phase cloud GTM was reaffirmed: marketplace private offers in customer tenants first, public PAYGO offers targeted in approximately 6 months, and a full multi-tenant SaaS offering likely in FY2028.

- The meeting summary states cloud infrastructure COGS for NVMe-based VMs is high (approximately $0.15 to $0.30 per GB per month), implying early cloud use cases are primarily burst-oriented.

- The meeting summary states an initial market reference list price for cloud capacity is approximately $0.07 per GB per month, and the on-prem list rework target is approximately $13 per TB with a core component.
