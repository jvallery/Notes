---
type: draft-reply
status: pending
created: "2026-01-05T19:45:01.629810"
urgency: "urgent"
to: "Jeff Denworth <jeff@vastdata.com>"
subject: "Re: Jeff Denworth escalates MAI supply chain risk and asks if Microsoft expects VAST supply chain"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-21_075242_5666_Re-MAI--VAST-December-8th-EoD-update.md"
ai_model: "gpt-5.2"
ai_temperature: 0.3
prompt_file: "Outbox/_prompts/2026-01-05_Reply-To_Jeff-Denworth-escalates-MAI-supply-chain.prompt.json"
---

# Draft Reply to Jeff Denworth

**Regarding**: Jeff Denworth escalates MAI supply chain risk and asks if Microsoft expects VAST supply chain
**Urgency**: urgent

---

## Key Points to Address

Reply to Jeff Denworth confirming whether Microsoft MAI expects VAST to supply hardware and flash, and outline immediate next steps to create a supply and ordering plan for an April 2026 to June 2026 deployment given no inventory is reserved. Also confirm you will send your latest MAI analysis and align on who owns sourcing and reservation with VAST Operations.

---

## Draft Response

Jeff — Microsoft MAI should plan on VAST supplying the full validated VAST configuration (servers + networking + flash) through our supply chain; we can support Microsoft-direct sourcing only if MAI explicitly chooses that path and we re-qualify the exact BOM and support boundaries. Given the April–June 2026 target and zero inventory reserved today, we need to lock an ordering and reservation plan this week to avoid schedule risk.

Next steps: let’s use our 12/22 call to confirm the deployment window, target usable capacity/perf, and the reference architecture (rack count, node type, flash TB, NICs/switches). By Wednesday, 12/24 5:00pm PT I will send you (1) my latest MAI sizing/architecture analysis, and (2) a proposed long-lead BOM with the specific supplier lanes we can execute (flash, server SKUs, NICs, optics, switches) and the order-by dates required to hit April and June 2026 delivery.

In parallel, I’m pulling VAST Operations into this immediately to align ownership for sourcing and reservation; by Thursday, 12/25 12:00pm PT we’ll confirm whether we reserve via VAST PO placement, supplier allocation holds, or a Microsoft-backed commit, and who signs each step. On the POC location: to get to 1,000–2,000 GPUs for scale testing, CoreWeave is the fastest path; if MAI/Vipin requires the MAI environment specifically, we’ll run the functional POC there and use CoreWeave for the large-scale performance/soak runs, with identical software and telemetry.

Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

Jeff Denworth raised a critical concern that VAST is selling out of inventory, lead times are increasing, and nothing is reserved for Microsoft. He asked whether Microsoft MAI expects to use VAST's supply chain and emphasized that if Microsoft wants an April to June 2026 deployment, VAST needs a plan immediately.

---

*This draft was auto-generated. Edit and send via your email client.*
