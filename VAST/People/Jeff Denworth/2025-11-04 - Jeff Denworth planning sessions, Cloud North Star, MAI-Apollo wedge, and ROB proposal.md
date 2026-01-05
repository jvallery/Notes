---
type: people
title: Jeff Denworth planning sessions, Cloud North Star, MAI/Apollo wedge, and ROB proposal
date: '2025-11-04'
person: Jeff Denworth
participants:
- Jason Vallery
- Jeff Denworth
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-04 - Jeff Denworth - Planning sessions.md
tags:
- type/people
- generated
---

# Jeff Denworth planning sessions, Cloud North Star, MAI/Apollo wedge, and ROB proposal

**Date**: 2025-11-04
**With**: Jason Vallery, Jeff Denworth

## Summary

Planning notes for a set of sessions with Jeff Denworth to align VAST Cloud strategy for FY26: define a core-first North Star, avoid lift-and-shift, use MAI/Apollo as the wedge, and implement SLO-gated release readiness. The document proposes a staged crawl-walk-run plan, Working Backwards artifacts (PR/FAQ and 6-pager), a 30/60/90 plan for MAI/Apollo, and a Rhythm of Business cadence with RAPID decision rights and quality gates.

## Action Items

- [?] Draft and socialize a concise FY26 VAST Cloud vision statement and scope boundaries, including explicit "what we will not build" in the next 12 months, for approval with Jeff Denworth. @Myself 📅 2025-11-18 ⏫ #task #proposed #auto

- [?] Propose and document the staged crawl-walk-run plan for VAST Cloud with explicit SLO, error-budget, and runbook gates for each stage, and bring it to Jeff Denworth for approval. @Myself 📅 2025-11-25 ⏫ #task #proposed #auto

- [?] Create initial Working Backwards artifacts: PR/FAQ and a 6-pager outline for "VAST Cloud" and "VAST in Apollo", and identify initial owners for each document. @Myself 📅 2025-12-02 ⏫ #task #proposed #auto

- [?] Define MAI/Apollo 30/60/90 success criteria and a joint test plan, including performance targets and a thin control-plane topology proposal aligned to AKS/Apollo. @Myself 📅 2025-12-04 ⏫ #task #proposed #auto

- [?] Propose a VAST-operated tenancy and shared-responsibility model, including minimum SLO set, incident/severity model, on-call expectations, and GA gating criteria tied to SLO conformance. @Myself 📅 2025-12-09 #task #proposed #auto

- [?] Draft a proposed Rhythm of Business calendar and RAPID decision matrix, including a Decision Log template and quality gates (Design, Readiness, Release, Postmortem), for Jeff Denworth approval. @Myself 📅 2025-11-21 #task #proposed #auto

- [?] Prepare a minimum viable hiring plan and role charters (Principal PMs, TPM, Product Ops, Tech Writer, Sales/SE Enablement PM) and identify what work Jason Vallery should stop doing to create focus. @Myself 📅 2025-12-12 #task #proposed #auto

- [?] Draft and circulate a one-paragraph vision statement for "Neocloud-in-a-box" and explicit scope boundaries for what VAST Cloud will not build in the next 12 months, for review with Jeff Denworth. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Create initial PR/FAQ drafts for "VAST Cloud" and "VAST in Apollo" using the Amazon Working Backwards format, and propose initial 6-pager owners for each artifact. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Propose a concrete 30/60/90-day plan for the Microsoft MAI and Apollo wedge, including joint success criteria, a test plan, a thin control-plane topology proposal, and measurable performance targets tied to GPU idle time reduction. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Define a minimum SLO and error-budget set for VAST Cloud offers and a release readiness checklist that includes runbooks, documentation, and support plan requirements for ship/no-ship decisions. @Myself 📅 TBD ⏫ #task #proposed #auto

- [?] Draft a proposed RAPID decision matrix and a Decision Log template for the Cloud operating mechanism, and align with Jeff Denworth on which decisions must be logged. @Myself 📅 TBD #task #proposed #auto

- [?] Write a minimum viable hiring plan and role charters for 1-2 Principal PMs, 1 TPM, 1 Product Ops lead, 1 Tech Writer, and 1 Sales/SE Enablement PM, including what Jason Vallery should stop doing to create focus. @Myself 📅 TBD #task #proposed #auto

## Decisions

- Approve the VAST Cloud vision statement and scope boundaries for FY26, including the "Neocloud-in-a-box" concept and explicit "what we will not build" in the next 12 months.

- Endorse core-first prioritization for FY26, deferring opinionated higher-layer services until the base platform is proven at scale.

- Approve the staged crawl-walk-run plan for VAST Cloud and enforce SLO and error-budget gates plus runbooks as criteria to advance stages and to gate GA.

- Green-light creation of Working Backwards artifacts (PR/FAQ and initial 6-pagers) for "VAST Cloud" and "VAST in Apollo" and assign owners.

- Name the single-threaded VAST owner for MAI and Apollo motions and define success criteria and a 90-day attack plan.

- Approve the proposed Rhythm of Business cadence, RAPID decision rights, and a Decision Log process.

- Approve headcount and budget for the minimum viable product organization (Principal PMs, TPM, Product Ops, Tech Writer, Sales/SE Enablement PM).

- Approve the "Neocloud-in-a-box" vision statement and scope boundaries for VAST Cloud, including explicit "what we will not build" in the next 12 months.

- Endorse a core-first prioritization for FY26, deferring opinionated higher-layer services until the base platform is proven at scale.

- Approve a staged crawl-walk-run plan for VAST Cloud offers and enforce SLO and error-budget gates before advancing stages or declaring GA.

- Green-light drafting Amazon Working Backwards artifacts (PR/FAQ and 6-pager) for "VAST Cloud" and "VAST in Apollo" and assign initial owners.

- Name the VAST single-threaded owner for Microsoft MAI and Apollo motions and define success criteria and a 90-day attack plan.

- Agree on minimum SLO set, error budgets, and a ship/no-ship governance model that gates releases on readiness (runbooks, docs, support plan).

- Approve the proposed Rhythm of Business cadence, RAPID decision rights, and maintaining a Decision Log for major decisions.

## Key Information

- The proposed product vision is a "Neocloud-in-a-box": a repeatable foundation for GPU-dense, single-tenant sites and select non-Azure data centers that is software-first, hardware-flexible, and liquid-cooling-friendly.

- The FY26 prioritization proposal is core layers first (cloud primitives, control plane stance, tenancy, operability, SLOs) and to avoid building opinionated higher-layer services (for example Insight/Agent engines) until the base is proven at scale.

- The cloud strategy proposal explicitly rejects a lift-and-shift of the on-prem "box" product and instead calls for cloud primitives and an AKS/Apollo-aligned thin control plane with clear tenancy, operability, and SLOs.

- The proposed delivery model is staged crawl-walk-run with gating that prevents advancing stages without error-budget-backed SLOs and runbooks, following Google SRE practices for SLIs/SLOs/error budgets.

- The proposal recommends using Amazon Working Backwards artifacts (PR/FAQ and a 6-pager) for "VAST Cloud" and "VAST in Apollo" to force clarity before building.

- The MAI/Apollo strategy proposal is to treat MAI success as the lighthouse and use Apollo to standardize VAST as storage for single-tenant GPU sites; multi-protocol (S3 + Blob) is exploratory while near-term focus remains performance and GPU utilization.

- The proposed MAI/Apollo success metrics include time-to-first-IO, sustained read/write throughput, GPU idle time reduction, cutover time, and site recovery time.

- The proposed 30/60/90 plan for MAI/Apollo is: 30 days to align on joint success criteria and test plan plus a thin control-plane topology proposal and perf targets; 60 days to run a live site POC with measurable performance and decide on liquid-cooled storage SKU exploration with an ODM; 90 days to produce a written scale plan for the first production site and a Go/No-Go on expanding to 2-3 additional sites.

- The proposal states that moving to VAST-operated deployments makes VAST a data custodian for some tenants and requires shared-responsibility definitions, SLO vs SLA definitions, runbooks, incident/severity model, on-call, audit, and cost telemetry, with pricing aligned to operational burden.

- The proposed operating model uses RAPID decision roles and a documented Decision Log to reduce churn and speed major decisions.

- The proposed Rhythm of Business cadence includes: Monday WBR (Product and Eng weekly business review), Tuesday RFE triage, Wednesday design review (FRDs and PR/FAQs), Thursday release readiness (ship/no-ship gates), Friday decision council (Jeff Denworth as Decider), plus monthly MBR and quarterly PI/OKR planning.

- The proposal asserts the current PM-to-development ratio is unsustainably low and requests minimum viable staffing: 1-2 Principal PMs (Cloud Platform and Azure/Microsoft), 1 TPM (release/readiness), 1 Product Ops lead, 1 Tech Writer, and 1 Sales/SE Enablement PM.

- The notes claim that Azure Marketplace VM-based offers (LSv4/LSv5) are not price/performance competitive at scale and that marketplace offers are not the win path at scale for the targeted deployments.

- A quoted internal perspective attributes to Vipin that key values include global namespace, quotas, capacity estimation, and QoS, and that Blob cannot match VAST performance.

- The notes state that MAI Falcon's first tranche came online with approximately 3 EB of Blob storage but is struggling due to control-plane fragility and GPU issues.

- The notes list MAI Falcon site plan locations as Phoenix, Dallas, and Richmond, with approximately 40,000 GPUs per site.

- The long-game Azure strategy described is to pursue Azure hardware qualification via Ronnie Booker and align with liquid-cooled storage SKUs to improve data center fungibility.

---

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
