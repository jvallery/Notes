---
type: draft-reply
status: pending
created: "2026-01-05T19:30:39.875785"
urgency: "normal"
to: "Brian Evans <brian.evans@vastdata.com>"
subject: "Re: RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md"
---

# Draft Reply to Brian Evans

**Regarding**: RFE 0482 (NVIDIA DGX Cloud): dual-uplink and tenant-scoped visibility via VAST Uplink
**Urgency**: normal

---

## Key Points to Address

Acknowledge RFE 0482 intake, confirm who will link the Salesforce RFE to the correct Related Feature, and respond to Mordechai Blaunstein on whether the proposed 'Service Aware VIP Pool' (ORION-261324) approach and tentative 5.6 targeting meets NVIDIA DGX Cloud needs or whether a workaround is required.

---

## Draft Response

Brian — thanks for flagging RFE 0482; we’ve got it in the queue and Mordechai is driving the technical analysis as Jeff requested. We’ll link the Salesforce RFE to the correct Related Feature under ORION-261324 (“Service Aware VIP Pool”) so tracking stays consolidated.

On the core question: the Service Aware VIP Pool approach is the right architectural fit for both asks in 0482—dual-uplink visibility for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster—because it enables multi-VIP access to VMS (GUI/CLI/REST/SSH/CSI) without forcing a single management path. The 5.6 target is still tentative, so I can’t commit that it meets DGX Cloud timelines yet; if NVIDIA needs this before 5.6, we should treat that as a separate delivery discussion rather than assuming a “shortcut” will be viable.

Next steps: I’ll have Mordechai confirm by Wednesday, January 8, 2026 whether 5.6 timing aligns with DGX Cloud’s deployment schedule and, if not, propose the best interim option (e.g., scoped access patterns and operational guidance) with clear limitations. If you can share NVIDIA’s required-by date (or the first NCP go-live date) for unified visibility, we’ll lock the plan and communicate it back to them.

Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

Brian Evans alerted the PM team about RFE 0482 from NVIDIA Corporation requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink visibility for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive analysis and pull in the right parties. Mordechai responded that VAST is already working similar CSP requests via a proposed 'Service Aware VIP Pool' (multi-VIP access to VMS for GUI/CLI/REST/SSH/CSI) tracked in ORION-261324, with a tentative target of VAST release 5.6 (not confirmed).

---

*This draft was auto-generated. Edit and send via your email client.*
