---
type: people
title: Align on MAI and UK Met
date: '2025-10-28'
person: Kanchan Mehrotra
participants:
- Jason Vallery
- Kanchan Mehrotra
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-28 - Jason and Koncha aligned on using
  MAI and UK Met Office as marquee wins to push.md
tags:
- type/people
- person/kanchan-mehrotra
- generated
---

# Align on MAI and UK Met

**Date**: 2025-10-28
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery and Kanchan Mehrotra aligned on using MAI and the UK Met Office as marquee wins to create executive pull for a VAST-suitable Azure hardware shape, given LSV4’s poor fit and LSV5’s long timeline. They agreed to run a dual track: progress an Azure Marketplace offer while simultaneously pushing leadership for better VM/storage shapes and networking to meet economics. Supercomputing/Ignite coordination and internal advocacy (notably Nidhi) were highlighted as key levers to advance the plan.
## Action Items
- [ ] Meet Kushal (MAI) Friday to discuss VAST opportunities and clarify the "not really Azure" capacity hint. @Myself 📅 2025-11-08 🔺 #task
- [ ] Reconnect with Vipin Sachdeva (MAI) to re-engage VAST. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Build internal comparative deck for a 1 EB deployment (VAST on LSV4/LSV5/on-prem vs Blob HDD/Flash) to support the hardware shape ask. @Myself 📅 2025-11-08 🔺 #task
- [ ] Coordinate a review with Nidhi to walk through the deck and align on the MAI + UK Met Office plan. @Koncha 📅 2025-11-08 ⏫ #task
- [ ] Meet UK Met Office stakeholders (Mike Kiernan, Nico, Allen) at Supercomputing to push the VAST path and surface LSV5 networking needs. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Speak with Egal to push on LSV5 shape and networking/bandwidth requirements and align timelines. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Align the joint VAST–Azure story for Supercomputing/Ignite (booths/panel) with Andrew, Joe Green, and Lior. @Koncha 📅 2025-11-08 ⏫ #task
- [ ] Check if Suresh will attend Supercomputing; if yes, set up a Neo cloud storage discussion with Jason; if not, schedule later. @Koncha 📅 2025-11-08 #task
- [ ] Provide input/content for Egal’s keynote slide referencing VAST. @Myself 📅 2025-11-08 #task
- [ ] Progress the Azure Marketplace offer (initial LSV4-based) and track ETA; be ready to brief sellers once credible. @VAST PM team 📅 2025-11-08 ⏫ #task
- [ ] Clarify MAI’s incremental opportunity and capacity location after the Friday meeting. @Myself 📅 2025-11-08 ⏫ #task
- [ ] Validate GPU-adjacent storage ratio guidance for Neo clouds with Suresh/Anand and explore Microsoft usage models (lease vs 1P vs Azure-sold). @Koncha 📅 2025-11-08 #task
- [ ] Keep Kurt informed so sellers remember VAST when qualifying 3P GPU deals. @Myself 📅 2025-11-08 🔽 #task
- [ ] Track Wave’s 40 PB request and assess a viable Azure configuration or alternatives; report back. @Myself 📅 2025-11-08 #task
- [ ] Confirm Nidhi’s Ignite/Supercomputing schedule and lock a time to review the deck. @Koncha 📅 2025-11-08 #task

## Decisions
- Focus first on MAI and UK Met Office to create executive pull for a VAST-suitable Azure hardware shape.
- Pursue a dual track: ship marketplace offers while driving a leadership-backed hardware path.
- Defer broad sales pushes until a credible Azure product/SKU path exists.

## Key Information
- Azure LSV4 is a poor fit for VAST (too many cores, weak networking, low NVMe density), driving poor cost/perf and sticker shock.
- LSV5 is committed by Egal’s team but is roughly a year+ out; networking plans may still be insufficient for UK Met Office economics.
- VAST density advantage cited: ~10x fewer racks (≈240 racks Blob vs ≈20 racks VAST for 1 EB) and ~1/5 power in MAI Falcon-like scenarios.
- MAI (ex-Inflection) has existing VAST affinity; champions include Kushal and Vipin Sachdeva.
- UK Met Office interest is constrained by SKU/networking economics and price/perf targets.
- Azure NetApp Files is cited as prior art for partner hardware running in Azure as a potential model for VAST via OEM/ODM.
- Neo cloud deployments need GPU-adjacent storage to mitigate network disconnect risk; a target ratio of local storage per ~8k GPUs is desired.
- Foundry/OpenAI long-term memory needs a high-TPS key-value store; VAST has an option (Undivided Attention) vs current RocksDB/FoundationDB usage.
- 3P GPU demand remains high but constrained by supply; co-sell motion is gated by capacity and tangible product offers.
- Marketplace control plane from Yancey’s team was acquired by VAST; Google first, Azure to follow (tracking suggests early next year).

---

*Source: [[Inbox/_archive/2025-10-28/2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push.md|2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]]*

## Related

- [[Kanchan Mehrotra]]
- [[Kishore Inampudi]]
- [[Erez Zilber]]
- [[Lior Genzel]]
- [[Jack Kabat]]
- [[John Mao]]
- [[Maneesh Sah]]
- [[Joe Green]]
- [[Jeff Denworth]]
- [[Vipin Sachdeva]]
- [[Mike Kiernan]]
- [[Neo]]
- [[Microsoft]]
- [[Google]]
- [[Amazon]]
- [[Oracle]]
- [[CoreWeave]]
- [[Tesla]]
