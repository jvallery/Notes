---
type: draft-reply
status: pending
created: "2026-01-05T19:44:06.332546"
urgency: "urgent"
to: "Jeff Denworth <jeff@vastdata.com>"
subject: "Re: Jeff Denworth flags MAI supply chain risk and need for immediate deployment plan"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-21_075242_5666_Re-MAI--VAST-December-8th-EoD-update.md"
ai_model: "gpt-5.2"
ai_temperature: 0.3
prompt_file: "Outbox/_prompts/2026-01-05_Reply-To_Jeff-Denworth-flags-MAI-supply-chain-ris.prompt.json"
---

# Draft Reply to Jeff Denworth

**Regarding**: Jeff Denworth flags MAI supply chain risk and need for immediate deployment plan
**Urgency**: urgent

---

## Key Points to Address

Acknowledge Jeff Denworth's supply chain concern, answer whether Microsoft MAI expects to use VAST supply chain, and propose an immediate plan to secure sourcing and delivery for an April 2026 to June 2026 deployment window. Include current status on any inventory reservation, what VAST Operations can commit to, and next steps to de-risk ordering for the stated capacity requirements (2EB and/or 100EB).

---

## Draft Response

Jeff — you’re right to flag this as a serious supply-chain risk: if MAI wants an April–June 2026 deployment window, we need to lock a sourcing plan now because we are not holding inventory for Microsoft today. MAI can either (a) use VAST’s supply chain (preferred for schedule certainty and end-to-end accountability) or (b) Microsoft can source the servers/flash independently and we qualify/integrate; both work, but option (a) is the only path where VAST Ops can commit to delivery dates.

Current status: there is no inventory reserved for Microsoft MAI at this moment. What VAST Operations can commit to is a dated allocation and delivery plan once we have (1) a firm capacity target (2EB initial vs. 100EB program), (2) a target configuration/BOM, and (3) an ordering vehicle (PO or binding forecast with agreed deposit/terms) so we can place upstream commitments with our OEM/flash partners.

Concrete plan to de-risk April–June 2026: by Tuesday, 2025-12-23 5:00pm PT, my team will send you two BOMs and schedules—one for 2EB and one for a phased ramp to 100EB—with required order-by dates, long-lead items, and the minimum commitment needed to reserve supply. By Thursday, 2025-12-25 12:00pm PT, we’ll align with MAI procurement on which path you want (VAST-supplied vs. Microsoft-supplied hardware) and, if VAST-supplied, we’ll initiate an allocation request with Ops and our suppliers the same day; by Monday, 2025-12-29 12:00pm PT, we’ll return a written allocation confirmation and a delivery window tied to that commitment.

On the Anson (Qi) PoC environment: for 1,000–2,000 GPU scale testing, MAI/Vipin is the right host if the goal is to validate MAI’s network/storage integration and operational model; Nscale/CoreWeave are good fallbacks for speed, but they won’t de-risk MAI’s production integration the same way. If you confirm by Tuesday, 2025-12-23 12:00pm PT that MAI/Vipin is the target, we’ll staff the PoC plan and integration checklist and have a ready-to-execute runbook to you by Wednesday, 2025-12-24 5:00pm PT.

Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

Jeff Denworth asked whether Microsoft MAI expects to use VAST Data supply chain and warned that VAST is selling out inventory with skyrocketing lead times. Jeff emphasized that if Microsoft wants an April to June 2026 deployment window, VAST needs a concrete plan immediately because nothing is reserved for Microsoft.

---

*This draft was auto-generated. Edit and send via your email client.*
