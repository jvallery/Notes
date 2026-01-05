---
type: people
title: Engineering maturity and cloud strategy
date: '2025-10-24'
person: Tomer Hagay
participants:
- Jason Vallery
- Tomer Hagay
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-24 - Jason and Tomer discussed accelerating
  VAST’s engineering maturity and cloud str.md
tags:
- type/people
- person/tomer-hagay
- generated
---

# Engineering maturity and cloud strategy

**Date**: 2025-10-24
**Account**: [[VAST]]
**Attendees**: Jason Vallery, Tomer Hagay

## Summary

Jason and Tomer aligned on using VAST’s cloud initiative to drive engineering process maturity, including AI-enabled development workflows, stronger release accountability, and SaaS operational readiness (telemetry/Live Site/24x7). They reviewed VAST’s RFE-to-release pipeline (Salesforce→Feature aggregation→Jira), support model (Co-Pilot + customer Slack channels), and Global Namespace architecture (strict consistency, lease-based caching; write-leases targeted for 5.5 preview). They agreed Jason should get hands-on via SE lab/OVA access and continue the discussion in a follow-up meeting the next week.
## Action Items
- [ ] Align with Shachar on AI development program goals and adoption metrics @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Draft proposal for AI-enabled dev workflow (PR/audits, agent usage) and training cadence @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Validate cloud P0 prioritization and resourcing with Brendan and Jeff @Myself 📅 2025-10-27 ⏫ #task #proposed
- [ ] Review and document current end-to-end dev lifecycle, gates, and tooling (RFE→Feature→Jira→Release) @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Contact Andy Perlsteiner to obtain SE lab access for hands-on evaluation @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Coordinate with Josh (Office of the CTO) to obtain OVA/bits for local testing @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Read Google Anywhere Cache documentation and compare to VAST Global Namespace; summarize gaps/opportunities @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Set up local VAST OVA on home cluster; move test data and validate GPU workflows @Myself 📅 2025-10-27 🔽 #task #proposed
- [ ] Schedule follow-up 1-1 for next week @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Plan Tel Aviv discussion on write-lease semantics and redirection model for Global Namespace @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed
- [ ] Connect with Rich to map full customer support structure and escalation paths @Myself 📅 2025-10-26 🔽 #task #proposed
- [ ] Share FRD templates/examples for Jason’s review @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed
- [ ] Introduce Jason to Eyal Tritel and Noah Cohen for planning cadence and scoping @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed
- [ ] Provide access to PM SFDC RFE/Feature dashboards and Jira links @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed
- [ ] Send Google Anywhere Cache reference links to Tomer @Myself 📅 2025-10-26 🔽 #task #proposed

## Decisions
- Proceed with lab/OVA onboarding for Jason to evaluate capabilities firsthand.
- Plan a follow-up meeting next week to continue driving cloud/process work.

## Key Information
- VAST engineering organization is approximately 400 developers.
- VAST releases have slipped without clear consequences (example cited: 5.4 moved by months) and there are many hotfix/service-pack variants per release (example cited: 5.2).
- VAST’s process is described as waterfall-ish and heavily RFE-driven via Salesforce; Jira is used at ticket level and epics are not consistently used.
- RFE triage is led by Jonathan Hayes; PMs aggregate RFEs into Salesforce “Features” that sync to Jira fixed versions.
- Support model includes Tier-3 “Co-Pilots” assigned per account and dedicated customer Slack channels; a vForce team can produce hotfixes.
- Global Namespace provides strict consistency with lease-based caching; read leases exist today and write-leases are planned for 5.5 as a preview.
- Cloud success is unlikely via lift-and-shift; a high-performance layer over object storage with global caching is viewed as necessary.
- A VAST-as-a-Service offering will require a SaaS operations model (telemetry, Live Site rotations, 24x7/365 support).
- Jason was pointed to Josh (Office of the CTO) for OVA/bits and to Andy Perlsteiner for SE lab onboarding/access.

---

*Source: [[Inbox/_archive/2025-10-24/2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str.md|2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]]*

## Related

- [[Google]]
- [[Amazon]]
- [[Cisco]]
- [[Microsoft]]
- [[OpenAI]]
- [[Tesla]]
- [[Andy Perlsteiner]]
- [[Brendan Burns]]
- [[David Holz]]
- [[Eyal Traitel]]
- [[Jonathan Hayes]]
- [[Noa Cohen]]
- [[Shachar Feinblit]]
- [[Tomer Hagay]]
- [[5.5 Features]]
- [[Cloud control plane]]
- [[OVA]]