---
type: "people"
title: "Planning sessions operating model"
date: "2025-11-01"
person: "Jeff Denworth"
participants: ["Jeff Denworth"]
source: "transcript"
source_ref: "Inbox/_archive/2025-11-04 - Jeff Denworth - Planning sessions.md"
tags:
  - "type/people"
  - "person/jeff-denworth"
  - "generated"
---

# Planning sessions operating model

**Date**: 2025-11-01
**With**: Jeff Denworth

## Summary

Planning-session notes outline a cloud-first product/program charter, decision rights, and a staged crawl-walk-run approach for “VAST Cloud” and “VAST in Apollo,” with SLO/error-budget gates. The document proposes a 30/60/90-day MAI/Apollo execution plan, a Rhythm of Business cadence (WBR, triage, design review, release readiness, decision council), and resourcing needs (PM/TPM/Product Ops/enablement) to improve predictability and throughput.
## Key Information
- Proposed North Star: “Neocloud-in-a-box” as a repeatable foundation for GPU-dense, single-tenant sites and select non-Azure DCs; software-first, hardware-flexible, liquid-cooling-friendly.
- Strategy emphasizes core layers first (defer opinionated higher-layer services) with horizons: 0–12 months (wedge wins + reliability), 12–36 (Azure hardware & control-plane integrations, multi-site repeatability), 36–60 (operational automation; AI-operated fleet).
- Cloud plan should avoid lift-and-shift; adopt cloud primitives and a new control-plane stance aligned with AKS/Apollo, with explicit tenancy/operability/SLOs.
- Staged offer model: Crawl (private offer/single-tenant), Walk (public offer/customer-tenant), Run (public SaaS/VAST-tenant) with SLO/error-budget gates and runbooks before advancing.
- Working Backwards artifacts (PR/FAQ + 6-pager) proposed for “VAST Cloud” and “VAST in Apollo.”
- MAI success positioned as the lighthouse/wedge; near-term focus on performance and GPU utilization; Blob compatibility treated as exploratory/leverage, not the main near-term goal.
- 30/60/90 proposal: 30 days success criteria + test plan + thin control-plane topology proposal + perf targets + exec alignment; 60 days POC live with measurable perf and decision on liquid-cooled SKU exploration; 90 days written scale plan and Go/No-Go to expand to 2–3 additional sites.
- SaaS/tenancy shift implies VAST may become a data custodian; requires shared-responsibility model, SLO vs SLA definitions, runbooks, compliance baselines, and pricing aligned to ops burden.
- Proposed ROB cadence includes: Mon WBR, Tue RFE triage, Wed design review, Thu release readiness, Fri decision council, plus monthly MBR and quarterly PI/OKR planning.
- Org/operating model: architects own FRDs; product owns why/priority/backlog/PR-FAQ/RICE/release gates; use RAPID (and DACI for specs) and maintain a decision log.
- Resourcing ask (minimum viable): 1–2 Principal PMs (Cloud Platform; Azure/MSFT), 1 TPM (release/readiness), 1 Product Ops lead, 1 Tech Writer, 1 Sales/SE Enablement PM.
- Risks called out: Azure internal P&L politics, long hardware qualification timelines, MAI control-plane fragility, timeline optimism, and fragmentation from investing too early in higher-layer services.
- Release discipline topics include support/EOL policy, stage gates with exit criteria, code freeze vs golden run alignment, and a deal-override policy with RAPID.
- Tel Aviv visit window mentioned: 2025-11-23 to 2025-11-26, with desired outcomes to lock 5.6 Cloud Design Qualifiers/P0s and leave an Apollo/MAI execution plan with owners and dates.
- 5.6 GA timing mentioned as “around July” (year not specified in the note).

---

*Source: [[Inbox/_archive/2025-11-04 - Jeff Denworth - Planning sessions.md|2025-11-04 - Jeff Denworth - Planning sessions]]*

## Related

- [[Jeff Denworth]]
- [[Cloud-in-a-box (Tier-2 clouds)]]
- [[Cloud control plane]]
- [[5.5 Features]]
- [[Amazon]]
- [[Google]]
- [[Microsoft]]
