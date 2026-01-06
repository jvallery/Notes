---
type: draft-reply
status: pending
created: "2026-01-05T19:30:20.620250"
urgency: "normal"
to: "Brian Evans <brian.evans@vastdata.com>"
subject: "Re: RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via Uplink"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md"
---

# Draft Reply to Brian Evans

**Regarding**: RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via Uplink
**Urgency**: normal

---

## Key Points to Address

Confirm ownership and next steps for RFE 0482: (1) ensure the Salesforce RFE is linked to the correct related feature, (2) align on whether ORION-261324 (Service Aware VIP Pool) covers dual-uplink and tenant-scoped visibility requirements, and (3) clarify timing expectations versus the tentative 5.6 target and whether an interim workaround is required.

---

## Draft Response

Brian, Mordechai owns the technical analysis for RFE 0482, and I’ll own the product-side closure to make sure we land the right solution and timeline for NVIDIA DGX Cloud. The working hypothesis is that ORION-261324 (“Service Aware VIP Pool”) is the correct umbrella feature for both dual-uplink visibility on a dedicated cluster and tenant-scoped visibility via Uplink on a multi-tenant cluster, but we need your confirmation.

Next steps: by Wednesday, January 8, 2026 EOD PT, I’ll ensure the Salesforce RFE 0482 is explicitly linked to ORION-261324 (and any dependent epics) and that the RFE text reflects the two concrete requirements (dual-uplink + tenant-scoped visibility). In parallel, Mordechai will validate the mapping end-to-end (GUI/CLI/REST/SSH/CSI access paths) and call out any gaps where RFE 0482 needs additional scope beyond Service Aware VIP Pool.

Two questions to close: (1) Does a 5.6 delivery for Service Aware VIP Pool meet DGX Cloud timing for RFE 0482, or do you need an interim workaround before 5.6? (2) Do you and Chuck agree that ORION-261324 fully addresses the dual-uplink and tenant-scoped visibility requirements as stated, or is there a specific DGX Cloud constraint we should bake in now? If you reply with your target date/quarter and any hard launch milestones, we’ll either lock 5.6 as the plan or propose a concrete workaround path by Friday, January 10, 2026.

Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud, requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink access for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive analysis and pull in the right parties. Mordechai responded that VAST is already working on similar CSP requests via a proposed "Service Aware VIP Pool" (ORION-261324) enabling multi-VIP access to VMS services (GUI/CLI/REST/SSH/CSI), and asked whether a tentative 5.6 target meets the needed timeline or if a workaround is required.

---

*This draft was auto-generated. Edit and send via your email client.*
