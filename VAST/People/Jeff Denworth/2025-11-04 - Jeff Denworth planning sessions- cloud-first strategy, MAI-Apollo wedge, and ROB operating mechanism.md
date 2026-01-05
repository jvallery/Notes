---
type: "people"
title: "Jeff Denworth planning sessions: cloud-first strategy, MAI/Apollo wedge, and ROB operating mechanism"
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

# Jeff Denworth planning sessions: cloud-first strategy, MAI/Apollo wedge, and ROB operating mechanism

**Date**: 2025-11-04
**With**: Jason Vallery, Jeff Denworth

## Summary

Planning notes for a set of sessions with Jeff Denworth to align on VAST Cloud north star, cloud-first sequencing (not lift-and-shift), and a MAI/Apollo wedge strategy with 30/60/90-day outcomes. The document proposes an operating mechanism (ROB) with SLO and error-budget quality gates, clarifies product decision rights (RAPID), and outlines a resourcing plan for Product Ops, TPM, and PM coverage.


## Action Items


- [?] Draft and socialize a one-sentence vision statement and explicit scope boundaries for 'Neocloud-in-a-box' (what VAST Cloud will build and what it will not build in the next 12 months) for approval with Jeff Denworth. @Myself 📅 2025-11-18 ⏫ #task #proposed #auto

- [?] Create initial Working Backwards artifacts (PR/FAQ and 6-pager) for 'VAST Cloud' and 'VAST in Apollo' and propose document owners and review cadence. @Myself 📅 2025-11-25 ⏫ #task #proposed #auto

- [?] Propose the crawl-walk-run stage gates with explicit SLOs, SLIs, error budgets, and required runbooks for each stage, and align with Jeff Denworth on using these gates for ship/no-ship decisions. @Myself 📅 2025-12-02 ⏫ #task #proposed #auto

- [?] Define MAI/Apollo 30/60/90-day plan details (success criteria, test plan, thin control-plane topology proposal, performance targets, and executive alignment plan) and bring to Jeff Denworth for decision on single-threaded ownership and Microsoft exec sponsor. @Myself 📅 2025-12-09 ⏫ #task #proposed #auto

- [?] Draft a proposed ROB calendar (WBR, RFE triage, design review, release readiness, decision council, MBR, PI/OKR planning) including attendees, content owners, and required inputs, and review with Jeff Denworth for approval. @Myself 📅 2025-11-18 #task #proposed #auto

- [?] Write a hiring and resourcing request that maps the minimum viable team (Principal PMs, TPM, Product Ops, Tech Writer, Enablement PM) to first-100-day outcomes and present to Jeff Denworth for headcount and budget approval. @Myself 📅 2025-12-02 #task #proposed #auto




## Decisions


- Pending decision: Approve the 'Neocloud-in-a-box' vision statement and scope boundaries for VAST Cloud, including what not to build in the next 12 months.

- Pending decision: Endorse core-first prioritization for FY26, deferring opinionated higher-layer services until the base platform is proven at scale.

- Pending decision: Approve the staged crawl-walk-run cloud plan and enforce SLO and error-budget gates before advancing stages.

- Pending decision: Green-light creation of Working Backwards artifacts (PR/FAQ and 6-pager) for 'VAST Cloud' and 'VAST in Apollo' and assign owners.

- Pending decision: Name the VAST single-threaded owner for MAI and Apollo motions and define the Microsoft executive sponsor.

- Pending decision: Establish minimum SLO set and error budgets and gate GA on SLO conformance.

- Pending decision: Approve the proposed ROB cadence, RAPID decision rights, and the hiring plan (PMs, TPM, Product Ops, Tech Writer, Enablement).




## Key Information


- The proposed product vision is a 'Neocloud-in-a-box' that is a repeatable foundation for GPU-dense, single-tenant sites and select non-Azure data centers, with a software-first and hardware-flexible approach that is liquid-cooling-friendly.

- The proposed FY26 prioritization is core layers first, explicitly avoiding building opinionated higher-layer services (for example Insight/Agent engines) until the base platform is proven at scale.

- The cloud strategy proposal uses a staged crawl-walk-run model: Crawl is private offer and single-tenant deployments with a thin control plane and basic tenancy; Walk is a public offer with hardened operations, cost telemetry, and upgrade path; Run is public SaaS with VAST-tenant operations including billing, quotas, audit/forensics, disaster recovery plans, and compliance baselines.

- The proposal gates progression between crawl-walk-run stages on error-budget-backed SLOs and runbooks, following Google SRE practices for SLIs, SLOs, and error budgets.

- The proposal recommends using Amazon 'Working Backwards' artifacts (PR/FAQ and a 6-pager) for 'VAST Cloud' and 'VAST in Apollo' to force clarity before building.

- The MAI/Apollo strategy proposal treats MAI success as the lighthouse and uses Apollo to standardize VAST as storage for single-tenant GPU sites; multi-protocol (S3 plus Blob) is positioned as exploratory while near-term focus remains performance and GPU utilization.

- The proposal states that moving to VAST-operated deployments makes VAST a data custodian for some tenants and requires shared-responsibility definitions, SLO versus SLA definitions, runbooks, incident severity model, audit, and cost telemetry, with GA gated on SLO conformance.

- The proposed operating mechanism is a weekly ROB with WBR, RFE triage, design review, release readiness, and a decision council, plus monthly MBR and quarterly PI/OKR planning; quality gates include Design (FRD/PRFAQ), Readiness (SLO/runbooks, docs, support), Release (error budget healthy), and Postmortem (blameless retro).

- The proposal defines decision rights using RAPID and logs major decisions in a Decision Log; architects own FRDs while Product owns the why/priority, backlog, PR/FAQ, RICE scoring, and release gates.

- The resourcing proposal states the PM-to-Dev ratio is unsustainably low and requests minimum viable staffing of 1-2 Principal PMs (Cloud Platform and Azure/Microsoft), 1 TPM (release/readiness), 1 Product Ops lead, 1 Tech Writer, and 1 Sales/SE Enablement PM.

- A quoted Microsoft contact named Vipin values global namespace, quotas, capacity estimation, and QoS, and stated that Azure Blob cannot match VAST performance.

- The notes claim Azure Marketplace VM offers (LSv4/LSv5) are not price/performance competitive at scale, and that software-first plus ODM liquid-cooled options are attractive for large deployments.

- The notes claim MAI Falcon first tranche came online with approximately 3 EB of Azure Blob storage but is struggling due to control-plane fragility and GPU issues.

- The notes claim MAI Falcon plan includes Phoenix, Dallas, and Richmond sites with approximately 40,000 GPUs per site.



---

*Source: [[2025-11-04 - Jeff Denworth - Planning sessions]]*