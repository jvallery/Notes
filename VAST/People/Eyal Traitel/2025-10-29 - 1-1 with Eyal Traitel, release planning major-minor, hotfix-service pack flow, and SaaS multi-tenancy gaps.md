---
type: "people"
title: "1:1 with Eyal Traitel, release planning (major/minor), hotfix/service pack flow, and SaaS multi-tenancy gaps"
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

# 1:1 with Eyal Traitel, release planning (major/minor), hotfix/service pack flow, and SaaS multi-tenancy gaps

**Date**: 2025-10-29
**With**: Jason Vallery, Eyal Traitel

## Summary

Jason Vallery and Eyal Traitel aligned on how VAST plans and executes major and minor releases, including how urgent field requests, hotfixes, and service packs are handled. Eyal described intake channels (leadership, architects, and SE Salesforce requests), the phase-gate process run by Ops and R&D, and the roles of release managers and vForce in hotfix/service pack execution. They also discussed SaaS and multi-tenant readiness, with Eyal committing to share a Confluence multi-tenancy gap list and planning follow-ups including an in-person meeting during Jason's Tel Aviv visit (2025-11-23 to 2025-11-26).


## Action Items


- [?] Send Jason Vallery the Confluence page detailing the VAST Data multi-tenancy gap list for SaaS and on-prem multi-tenant readiness. @Eyal Traitel 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Schedule a follow-up call to dive deeper into VAST Data release planning mechanics and VAST on Cloud needs (SaaS and multi-tenant readiness). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Schedule an in-person meeting with Eyal Traitel during Jason Vallery's Tel Aviv visit (2025-11-23 to 2025-11-26). @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Review the multi-tenancy gap list and identify the highest-priority items required for SaaS and on-prem multi-tenancy, then feed priorities back into release planning discussions with Eyal Traitel and relevant engineering owners. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Align with Polaris and Iceland control plane teams on which SaaS and multi-tenancy gaps should be addressed in the control plane versus the cluster layer. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the VAST Data 5.6 phase-gate timeline and assess implications for delivering key SaaS and multi-tenancy items within the 5.6 release scope. @Myself 📅 2025-11-08 #task #proposed #auto






## Key Information


- Eyal Traitel joined VAST Data in December 2024 and works in release planning, focusing primarily on minor releases while Noa (veteran employee) focuses on major releases.

- VAST Data feature intake comes through leadership and architects (for example, NVIDIA-driven requests like S3 RDMA) and through Sales Engineering requests filed in Salesforce tied to opportunities, which are triaged by Tomer Hagay's team with Jonathan Hayes and reviewed bi-weekly.

- VAST Data uses release managers (separate from Eyal Traitel and Noa) to run day-to-day execution for major and minor releases across development and QA teams.

- VAST Data phase-gate release documentation and process are driven by Ops (Shelly Martin) and R&D (Liraz), and release scope often changes between phase gate 1 commitments and final GA content due to urgent requests and churn.

- Minor releases at VAST Data are treated like full releases, including regression and performance testing, with weekly content and testing reviews.

- Urgent customer-driven requests (example given: Tesla) frequently introduce new scope during a release cycle, forcing teams to reallocate effort from planned work and creating parallel workstreams.

- Large "hotfixes" sometimes include feature work to close deal or install gaps when the minor release cadence is not fast enough, creating an out-of-band delivery stream separate from the regular minor release cycle.

- Service packs and hotfixes are driven primarily by vForce (Roy Sterman and team), acting as an R&D-facing arm in front of Customer Success and customers, including initiating backports from future releases for specific customer needs.



---

*Source: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]]*