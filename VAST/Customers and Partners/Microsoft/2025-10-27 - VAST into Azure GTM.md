---
type: customer
title: VAST into Azure GTM
date: '2025-10-27'
account: Microsoft
participants:
- Jason Vallery
- Kurt Niebuhr
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-27 - Jason and Kurt aligned on a go-to-market
  path to bring VAST’s high-density, lowe.md
tags:
- type/customer
- account/microsoft
- generated
---

# VAST into Azure GTM

**Date**: 2025-10-27
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Kurt Niebuhr

## Summary

Jason and Kurt aligned on a go-to-market approach to bring VAST’s high-density, lower-power storage into Microsoft Azure deals, emphasizing power/megawatt constraints and the limitations of the current Azure Marketplace VM-based VAST offer. They agreed to pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and route into Ronnie Booker’s org for hardware/chassis decisions, while Kurt continues driving A2N approval for Azure Extended Zones (network-only) and AKS NodeJoin to connect neo-/sovereign cloud training sites to Azure for global inference.
## Action Items
- [ ] Educate Microsoft BizDev (Joe Vane/Harish) on VAST density/power and single-namespace story; secure intros to Ronnie Booker via John Tinter. @Myself 📅 2025-10-27 🔺 #task
- [ ] Create a one-pager converting VAST exabyte power savings into additional GPUs per site; share with Mustafa (MAI), Kushal, and Vipin. @Myself 📅 2025-10-27 🔺 #task
- [ ] Push MAI and UK Met to pilot VAST OEM/ODM racks (Falcon, UK Met) using the power-density angle. @Myself 📅 2025-10-27 🔺 #task
- [ ] Follow up with Kanchan Mehrotra on storage plays/density for Supercomputing (FAST) and schedule a discussion. @Myself 📅 2025-10-27 ⏫ #task
- [ ] Coordinate with Kishore Inampudi on Azure Extended Zones once A2N is approved; align on storage needs. @Myself 📅 2025-10-27 ⏫ #task
- [ ] Confirm with Yancey and Lior Genzel their awareness of VAST density/power benefits and enlist them to advocate with Mustafa. @Myself 📅 2025-10-27 ⏫ #task
- [ ] Quantify capex vs power tradeoffs to justify ~2x capex for decision-makers (e.g., Amy Hood, BizDev). @Myself 📅 2025-10-27 ⏫ #task
- [ ] Drive A2N approval for Extended Zones GA and AKS NodeJoin (ACAS FlexNode); confirm timeline and scope. @Kurt 📅 2025-10-27 🔺 #task
- [ ] Share Azure Extended Zone PM contact details when available. @Kurt 📅 2025-10-27 🔽 #task
- [ ] Keep Jason updated on neo-cloud partnership pipeline (e.g., sakura.net) and where VAST can plug in. @Kurt 📅 2025-10-27 ⏫ #task
- [ ] Validate whether InScale and similar deals follow the 'train on neo-cloud, infer on Azure' model. @Kurt 📅 2025-10-27 🔽 #task
- [ ] Assess complementing the Marketplace L-series offer with higher-density storage SKUs or an OEM hardware path. @Myself 📅 2025-10-27 ⏫ #task
- [ ] Plan Supercomputing touchpoint and intros (e.g., AMD event) and align joint targets. @Myself 📅 2025-10-27 🔽 #task

## Decisions
- Pursue a BizDev-led path (Joe Vane/Harish) to engage Ronnie Booker’s org rather than working through Nidhi/Manish.
- Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Key Information
- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations, supports mega-deals, and runs Azure Core feedback.
- All constrained GPU allocations require approval from Kurt’s team; deal triage includes stickiness, workload type, and platform pull-through.
- Proposal in flight: GA Azure Extended Zones (network-only) and AKS NodeJoin/ACAS FlexNode to connect neo-/sovereign cloud training sites to Azure for global inference.
- VAST vs Azure Blob (per 1 EB): ~1/10 racks, ~1/5 megawatts, and >=5x performance, but ~2x capex.
- Current Azure Marketplace VAST offer on L-series VMs is not density/performance competitive for real workloads; primarily a 'checkbox' cloud presence.
- Apollo ownership boundaries: Chi owns bare-metal control plane; Sky/Overlake owns security; Ronnie Booker’s org owns chassis/layout/storage placement decisions.
- BizDev contacts: Joe Vane (reports to Harish); path via BizDev and John Tinter to reach Ronnie Booker.
- Azure MAI/Falcon issues include lack of topology-aware scheduling; rack-level placement not expected until ~Feb (relative, not a firm date).
- OpenAI infra leadership change: Uday (ex-xAI) now runs infra at OpenAI and reports to Greg Brockman; may reduce Microsoft alignment; power is a major constraint for Azure.
- Kurt expects A2N approval for Extended Zones/NodeJoin in ~3 weeks (relative estimate).
- Target partner example for neo-cloud approach: sakura.net in Japan; model is 'train on neo-cloud, infer on Azure'.

---

*Source: [[Inbox/_archive/2025-10-27/2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe.md|2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]]*

## Related

- [[Amazon]]
- [[Oracle]]
- [[CoreWeave]]
- [[Google]]
- [[OpenAI]]
- [[Tesla]]
- [[Intel]]
- [[HPE]]
- [[Kurt Niebuhr]]
- [[Jason Vallery]]
- [[Joe Vane]]
- Harish
- [[John Tinter]]
- [[Ronnie Booker]]
- [[Kanchan Mehrotra]]
- [[Kishore Inampudi]]
- [[Lior Genzel]]
- [[Amy Hood]]
- [[Greg Brockman]]
- [[Brian Moore]]
- [[Brendan Burns]]
- [[John Lee]]
- [[Mike Requa]]
- [[Rory Kellerworthy]]
- [[Microsoft Azure Engagement Plan]]
