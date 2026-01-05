---
type: "people"
title: "1:1 with Eyal Traitel, VAST release planning (major/minor, hotfix/service packs) and multi-tenancy gaps"
date: "2025-10-29"
person: ""
participants: ["Jason Vallery", "Eyal Traitel"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Eyal Traitel, VAST release planning (major/minor, hotfix/service packs) and multi-tenancy gaps

**Date**: 2025-10-29
**With**: Jason Vallery, Eyal Traitel

## Summary

Jason Vallery and Eyal Traitel aligned on how VAST plans and executes major and minor releases, and how hotfixes and service packs are handled. Eyal described feature intake channels, planning ownership, and the operational reality of frequent urgent customer requests causing scope churn. They also discussed SaaS and multi-tenant readiness, including a known multi-tenancy gap list and a key blocker around authentication provider scaling and tenant scoping.


## Action Items


- [?] Send Jason Vallery the Confluence page detailing the VAST Data multi-tenancy gap list for SaaS and multi-tenant readiness. @Eyal Traitel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up call to dive deeper into VAST Data release planning and VAST on Cloud needs. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Schedule an in-person meeting with Eyal Traitel during Jason Vallery’s Tel Aviv visit (2025-11-23 to 2025-11-26). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Review the multi-tenancy gap list and identify the highest-priority items for SaaS and on-prem multi-tenancy enablement. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Align with Polaris and Iceland control plane teams on which multi-tenancy gaps can be addressed in the control plane versus the cluster layer. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the VAST Data 5.6 phase-gate timeline and assess implications for delivering key multi-tenancy items. @Myself 📅 2025-11-08 #task #proposed #auto






## Key Information


- Eyal Traitel joined VAST Data in December 2024 and works in release planning; he expects to continue planning minor releases while Noa (a long-tenured VAST employee) manages major releases.

- VAST Data feature intake comes through leadership and architects (including requests influenced by NVIDIA discussions such as S3 RDMA), and through Sales Engineering requests filed in Salesforce tied to an opportunity and triaged by Tomer Hagay’s team with Jonathan Hayes, reviewed bi-weekly.

- VAST Data release planning is highly dynamic due to frequent urgent customer-driven requests (example given: Tesla), which causes scope churn between initial phase-gate commitments and final release content.

- For each VAST Data major release and minor release, a dedicated release manager (separate from Eyal Traitel and Noa) runs day-to-day execution with development and QA teams.

- VAST Data phase-gate release process is driven by operations and R&D process owners, specifically Shelly Martin (Ops) and Liraz (R&D), who drive documentation of release commitments.

- VAST Data uses a minor release process to address faster-turn requests, but urgent requests can still require out-of-band large hotfixes that may include feature work rather than defect fixes.

- Service packs and hotfixes at VAST Data are driven largely by vForce (Roy Sterman and team), acting as an R&D-facing arm in front of Customer Success and customers, including initiating backports from future releases for specific customers.



---

*Source: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]]*