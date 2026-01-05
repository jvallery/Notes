---
type: people
title: VAST cloud strategy and enablement
date: '2025-10-31'
person: Rob Benoit
participants:
- Jason Vallery
- Rob Benoit
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-31 - Intro discussion covering VAST-in-cloud
  strategy, field enablement gaps, and SE.md
tags:
- type/people
- person/rob-benoit
- generated
---

# VAST cloud strategy and enablement

**Date**: 2025-10-31
**With**: Jason Vallery, Rob Benoit

## Summary

Jason Vallery and Rob Benoit aligned on a VAST-in-cloud strategy emphasizing object storage for capacity and bare metal for performance to improve cloud economics, with DataSpaces/global namespace as a key differentiator for hybrid/multi-cloud AI patterns. They discussed field enablement gaps (fragmented content ownership, duplicative Confluence docs), SE org constraints (install/rack-and-stack time, high networking skill bar), and the need for a feedback loop between field pain points and the cloud roadmap. They agreed to connect at Tech Summit for a deeper follow-up and to exchange roadmap context and consolidated field feedback.
## Action Items
- [ ?] Schedule coffee with Rob during Tech Summit @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Share initial VAST cloud roadmap context with SE leadership @Myself 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Provide consolidated field pain points on current product for cloud/hyperscaler use @Rob Benoit 📅 2025-11-08 ⏫ #task #proposed
- [ ?] Confirm time and location for Tech Summit meeting @Myself 📅 2025-11-08 🔽 #task #proposed
- [ ?] Loop in Yancey and relevant owners on marketplace and bare-metal plans as needed @Myself 📅 2025-11-08 🔽 #task #proposed

## Decisions
- Meet at Tech Summit for a follow-up conversation.

## Key Information
- Jason reports to Jeff and is focused on making VAST successful on hyperscalers and marketplaces; he is ex-Microsoft Azure Storage GPM with deep object storage and OpenAI workload experience.
- Rob Benoit leads the global pre-sales SE organization; previously 18 years at NetApp with enablement and Americas SE leadership experience.
- VAST cloud deployment is complex; marketplace success likely requires exposing tenant outcomes rather than cluster administration.
- Cloud VM economics are unfavorable for VAST at scale; preferred approach is object storage for capacity tier plus bare metal for performance.
- GCP Z3 instances help but become expensive at larger sizes; bare metal instances are preferred.
- VAST DataSpaces/global namespace is a major differentiator for hybrid/multi-cloud AI data mobility patterns.
- OpenAI pattern described: central CPU-adjacent data lake with GPU-adjacent working-set caches across many regions/clouds.
- Field enablement/content ownership is fragmented with duplicative Confluence documentation and unclear owners.
- SE org is bandwidth constrained by installs (rack/stack and deployment can take ~2 weeks), reducing selling time.
- A new partner program was created to offload rack-and-stack; cabling errors can cause multi-day delays.
- High networking skills are required across the SE org (400G fabrics, leaf-spine, VXLAN, BGP).
- Tech Summit approved for ~200 attendees at a little over $500k cost; Renan supports SE investment.

---

*Source: [[Inbox/_archive/2025-10-31/2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE.md|2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]]*

## Related

- [[Jason Vallery]]
- [[Rob Benoit]]
- [[Rob Banga]]
- [[Jeff Denworth]]
- [[Andy Perlsteiner]]
- [[Ronen Cohen]]
- [[NetApp]]
- [[Microsoft]]
- [[Google]]
- [[Amazon]]
- [[Oracle]]
- [[Databricks]]
- [[OpenAI]]
- [[CoreWeave]]
- [[Goldman Sachs]]
- [[Cisco]]