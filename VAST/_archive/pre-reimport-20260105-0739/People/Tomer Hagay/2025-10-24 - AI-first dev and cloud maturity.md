---
type: people
title: AI-first dev and cloud maturity
date: '2025-10-24'
person: Tomer Hagay
participants:
- Jason Vallery
- Tomer Hagay
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-24 - Jason and Tomer discussed accelerating
  AI-driven software development practices.md
tags:
- type/people
- person/tomer-hagay
- generated
---

# AI-first dev and cloud maturity

**Date**: 2025-10-24
**Account**: [[VAST]]
**Attendees**: Jason Vallery, Tomer Hagay

## Summary

Jason and Tomer discussed accelerating AI-first software development practices at VAST, highlighting release slippage, limited accountability, and the need to codify AI-enabled workflows. They reviewed VAST’s RFE-to-Feature-to-Jira process, customer support via tier-3 “co-pilots” and per-customer Slack channels, and Global Namespace (strict consistency with read leases today; write leases planned for 5.5 preview). Next steps focus on getting Jason hands-on access to VAST (OVA or SC lab) and continuing the discussion the following week, using cloud as a wedge to drive SaaS operating model maturity.
## Action Items
- [?] Ping Josh Wentzell (Office of the CTO) to obtain VAST OVA access and onboarding for local lab testing @Myself 📅 2025-10-27 🔺 #task #proposed
- [?] Coordinate with Andy Perlsteiner for SC lab access as a backup/quick-start environment @Myself 📅 2025-10-27 ⏫ #task #proposed
- [?] Set up a local cluster with the VAST OVA to test Global Namespace, caching/prefetch, and GPU workflows @Myself 📅 2025-10-27 ⏫ #task #proposed
- [?] Draft VAST Cloud SaaS operating model requirements (DevOps/LifeSite rotations, telemetry, 24x7 support) @Myself 📅 2025-10-27 ⏫ #task #proposed
- [?] Schedule the next 1:1 for next week to continue on cloud plan and process changes @Myself 📅 2025-10-26 ⏫ #task #proposed
- [?] Meet with Customer Success (e.g., Rich) to understand account support workflows end-to-end @Myself 📅 2025-10-27 🔽 #task #proposed
- [?] Confirm with leadership (Brendan/Jeff) that Cloud is P0 and clarify resourcing expectations @Myself 📅 2025-10-26 ⏫ #task #proposed
- [?] Review Google Anywhere Cache documentation and compare policy/prefetch capabilities to VAST Global Namespace @Tomer Hagay 📅 2025-10-26 ⏫ #task #proposed
- [?] Ask Shachar to confirm AI-first development mandate, training cadence, and measurable adoption targets @Tomer Hagay 📅 2025-10-27 🔺 #task #proposed
- [?] Clarify VAST’s end-to-end dev lifecycle (gates, signoffs, source control, CI/CD, release) with engineering (Eyal Tritel/Noa Cohen) or documentation @Myself 📅 2025-10-27 ⏫ #task #proposed
- [?] Review and align on write-lease design and read redirection behaviors with Tel Aviv team for 5.5 @Tomer Hagay 📅 2025-10-27 🔽 #task #proposed
- [?] Proceed with Slack multi-channel polling capability with IT and report feasibility/timeline @Tomer Hagay 📅 2025-10-26 🔽 #task #proposed

## Key Information
- VAST has approximately 400 developers.
- Release cadence is described as waterfall-ish with frequent slips (e.g., 5.4 slipped from June to October) and limited accountability/consequences.
- Microsoft’s model was cited as an example: codified AI-first dev workflows and biweekly forced AI training days.
- RFEs are captured in Salesforce, require SE manager approval, and are initially triaged by Jonathan Hayes; PMs aggregate RFEs into “Features” linked to Jira tickets (epics are not consistently used).
- Support model includes a tier-3 “co-pilot” per account, a separate customer Slack workspace with per-customer channels, and a vForce team that builds hotfixes.
- Global Namespace provides strict consistency using read leases today; write leases are targeted for a 5.5 preview release.
- Global Namespace supports multi-protocol on satellites (NFS/SMB/S3) and includes caching/prefetch and explicit prefetching capabilities.
- Combining async replication with Global Namespace (5.4) enables active-active read/write access with point-in-time snapshots.
- Cloud success likely requires a layer over cloud object storage (lift-and-shift is unlikely to meet price/performance targets).
- Hotfix/service pack sprawl increases maintenance burden and reflects process maturity gaps.

---

*Source: [[Inbox/_archive/2025-10-24/2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices.md|2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices]]*

## Related

- [[Andy Perlsteiner]]
- [[Brendan Burns]]
- [[Jeff Denworth]]
- [[Jonathan Hayes]]
- [[Noa Cohen]]
- [[Tomer Hagay]]
- [[5.5 Features]]
- [[Cloud control plane]]
- [[Amazon]]
- [[Google]]
- [[Microsoft]]
- [[OpenAI]]
- [[Tesla]]