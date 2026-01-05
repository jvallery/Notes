---
type: "people"
title: "Jeff Denworth planning sessions: Cloud north star, MAI/Apollo wedge, SLO-gated operating cadence"
date: "2025-11-04"
person: ""
participants: ["Jason Vallery", "Jeff Denworth"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-04 - Jeff Denworth - Planning sessions.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# Jeff Denworth planning sessions: Cloud north star, MAI/Apollo wedge, SLO-gated operating cadence

**Date**: 2025-11-04
**With**: Jason Vallery, Jeff Denworth

## Summary

Planning outline for a set of sessions with Jeff Denworth to align VAST Cloud strategy around a core-first, staged crawl-walk-run approach with SLO and error-budget gates. The notes propose using Microsoft MAI and Apollo as the lighthouse wedge, adopting Working Backwards artifacts (PR/FAQ and 6-pager), and standing up a Rhythm of Business with RAPID decision rights and release readiness governance.


## Action Items


- [?] Draft and circulate a one-paragraph vision statement for "Neocloud-in-a-box" and explicit scope boundaries for what VAST Cloud will not build in the next 12 months, for review with Jeff Denworth. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Create initial PR/FAQ drafts for "VAST Cloud" and "VAST in Apollo" using the Amazon Working Backwards format, and propose initial 6-pager owners for each artifact. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Propose a concrete 30/60/90-day plan for the Microsoft MAI and Apollo wedge, including joint success criteria, a test plan, a thin control-plane topology proposal, and measurable performance targets tied to GPU idle time reduction. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Define a minimum SLO and error-budget set for VAST Cloud offers and a release readiness checklist that includes runbooks, documentation, and support plan requirements for ship/no-ship decisions. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Draft a proposed RAPID decision matrix and a Decision Log template for the Cloud operating mechanism, and align with Jeff Denworth on which decisions must be logged. @Myself 📅 TBD #task #proposed #auto

- [?] Write a minimum viable hiring plan and role charters for 1-2 Principal PMs, 1 TPM, 1 Product Ops lead, 1 Tech Writer, and 1 Sales/SE Enablement PM, including what Jason Vallery should stop doing to create focus. @Myself 📅 TBD #task #proposed #auto




## Decisions


- Approve the "Neocloud-in-a-box" vision statement and scope boundaries for VAST Cloud, including explicit "what we will not build" in the next 12 months.

- Endorse a core-first prioritization for FY26, deferring opinionated higher-layer services until the base platform is proven at scale.

- Approve a staged crawl-walk-run plan for VAST Cloud offers and enforce SLO and error-budget gates before advancing stages or declaring GA.

- Green-light drafting Amazon Working Backwards artifacts (PR/FAQ and 6-pager) for "VAST Cloud" and "VAST in Apollo" and assign initial owners.

- Name the VAST single-threaded owner for Microsoft MAI and Apollo motions and define success criteria and a 90-day attack plan.

- Agree on minimum SLO set, error budgets, and a ship/no-ship governance model that gates releases on readiness (runbooks, docs, support plan).

- Approve the proposed Rhythm of Business cadence, RAPID decision rights, and maintaining a Decision Log for major decisions.

- Approve headcount and budget for the minimum viable product organization (Principal PMs, TPM, Product Ops, Tech Writer, Sales/SE Enablement PM).




## Key Information


- The proposed product vision is a "Neocloud-in-a-box": a repeatable foundation for GPU-dense, single-tenant sites and select non-Azure data centers that is software-first, hardware-flexible, and liquid-cooling-friendly.

- The proposed FY26 prioritization is core layers first, explicitly avoiding building opinionated higher-layer services (for example Insight/Agent engines) until the base platform is proven at scale.

- The cloud strategy proposal is explicitly not lift-and-shift of the on-prem "box" product, and instead requires cloud primitives plus a new control-plane stance aligned to AKS and Apollo with clear tenancy, operability, and SLOs.

- The plan proposes adopting Amazon Working Backwards artifacts (PR/FAQ and a 6-pager) for both "VAST Cloud" and "VAST in Apollo" to force clarity before build.

- The staged go-to-market plan is Crawl (private offer, single-tenant, thin control plane), Walk (public offer, customer-tenant, hardened ops and telemetry), Run (public SaaS, VAST-tenant with billing, quotas, audit/forensics, DR, compliance).

- Progression between stages is gated by error-budget-backed SLOs and runbooks, following Google SRE practices for SLIs, SLOs, and error budgets.

- The MAI and Apollo strategy is to treat MAI success as the lighthouse wedge and use Apollo to standardize VAST as storage for single-tenant GPU sites, with multi-protocol (S3 plus Blob) positioned as exploratory while near-term focus remains performance and GPU utilization.

- The notes propose that Jason Vallery can be the VAST single-threaded owner for MAI and Apollo motions on the product and alliances side.

- Moving to VAST-operated deployments would make VAST a data custodian for some tenants, requiring shared-responsibility definitions, SLO vs SLA definitions, runbooks, incident/severity model, on-call, audit, and cost telemetry, with pricing aligned to operational burden.

- The proposed operating model uses RAPID decision roles and a documented Decision Log to speed decisions and avoid churn.

- The proposed Rhythm of Business includes: Monday WBR, Tuesday RFE triage, Wednesday design review, Thursday release readiness, Friday decision council, monthly MBR, and quarterly PI/OKR planning, with explicit quality gates for design, readiness, release, and postmortems.

- The resourcing proposal states the current PM to Dev ratio is unsustainably low and requests minimum viable hires: 1-2 Principal PMs (Cloud Platform and Azure/Microsoft), 1 TPM (release/readiness), 1 Product Ops lead, 1 Tech Writer, and 1 Sales/SE Enablement PM.

- A quoted Microsoft stakeholder named Vipin values global namespace, quotas, capacity estimation, and QoS, and stated that Azure Blob cannot match VAST performance.

- The notes claim Azure Marketplace VM options (LSv4 and LSv5) are not price/performance competitive at scale, and that software-first plus ODM liquid-cooled options are attractive for large deployments.

- The notes state that MAI Falcon's first tranche came online with approximately 3 EB of Azure Blob storage but is struggling due to control-plane fragility and GPU issues.

- The notes state a MAI Falcon plan includes Phoenix, Dallas, and Richmond sites with approximately 40,000 GPUs per site.



---

*Source: [[2025-11-04 - Jeff Denworth - Planning sessions]]*