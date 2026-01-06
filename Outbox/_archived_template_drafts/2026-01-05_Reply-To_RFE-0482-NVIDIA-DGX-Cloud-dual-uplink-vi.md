---
type: draft-reply
status: pending
created: "2026-01-05T19:09:34.132186"
urgency: "normal"
to: "Brian Evans <brian.evans@vastdata.com>"
subject: "Re: RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via VAST Uplink"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-04_100559_9782_Re-RFE-Alert-RFE-0482---Existing-Feature-Enhancement-RFE-Sub.md"
---

# Draft Reply to Brian Evans

**Regarding**: RFE 0482 (NVIDIA DGX Cloud): dual-uplink visibility and tenant-scoped visibility via VAST Uplink
**Urgency**: normal

---

## Key Points to Address

Acknowledge RFE 0482 intake, confirm who will link the Salesforce RFE to the correct Related Feature, and respond to Mordechai Blaunstein on whether the tentative (not confirmed) 5.6 target meets NVIDIA DGX Cloud timing or whether a workaround is required. Align on whether ORION-261324 (Service Aware VIP Pool) fully covers dual-uplink visibility for LAX-02 and tenant-scoped visibility for LAX-03.

---

## Draft Response

Hi Brian,

Thank you for your email. Here's my response:

- Acknowledge RFE 0482 intake, confirm who will link the Salesforce RFE to the correct Related Feature, and respond to Mordechai Blaunstein on whether the tentative (not confirmed) 5.6 target meets NVIDIA DGX Cloud timing or whether a workaround is required
- Align on whether ORION-261324 (Service Aware VIP Pool) fully covers dual-uplink visibility for LAX-02 and tenant-scoped visibility for LAX-03.

To answer your questions:
- Does the tentative (not confirmed) target to support 'Service Aware VIP Pool' in VAST release 5.6 meet NVIDIA DGX Cloud's timeline for RFE 0482, or is a shortcut/workaround required?: [TODO: Add answer]
- Do Chuck Cancilla and Brian Evans agree that the ORION-261324 'Service Aware VIP Pool' design addresses the dual-uplink and tenant-scoped visibility requirements described in RFE 0482?: [TODO: Add answer]

I'll follow up on:
- Mordechai Blaunstein committed to take ownership of RFE 0482 investigation and to coordinate with relevant parties, referencing ORION-261324 and the internal wiki as the current approach.

Let me know if you have any questions.

Best,
Jason

---

## Original Summary

Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud requesting unified visibility across VAST clusters deployed at multiple NCPs, including dual-uplink access for a dedicated cluster and tenant-scoped visibility for a multi-tenant cluster. Jeff Denworth flagged the request as complex and asked Mordechai Blaunstein to drive it; Mordechai responded that VAST is already working on a related approach (Service Aware VIP Pool) tracked in ORION-261324 and asked whether a tentative 5.6 target meets NVIDIA's timeline.

---

*This draft was auto-generated. Edit and send via your email client.*
