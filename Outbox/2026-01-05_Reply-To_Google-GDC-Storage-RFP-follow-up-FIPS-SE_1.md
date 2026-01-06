---
type: draft-reply
status: pending
created: "2026-01-05T19:47:56.694579"
urgency: "urgent"
to: "Lior Genzel <lior.genzel@vastdata.com>"
subject: "Re: Google GDC Storage RFP follow-up: FIPS, SEDs, BYOH partners, and scheduling"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-23_004718_3592_Re-VAST-Data---GDC-Storage-RFP---Request-For-Meeting.md"
ai_model: "gpt-5.2"
ai_temperature: 0.3
prompt_file: "Outbox/_prompts/2026-01-05_Reply-To_Google-GDC-Storage-RFP-follow-up-FIPS-SE_1.prompt.json"
---

# Draft Reply to Lior Genzel

**Regarding**: Google GDC Storage RFP follow-up: FIPS, SEDs, BYOH partners, and scheduling
**Urgency**: urgent

---

## Key Points to Address

Confirm Jason Vallery availability for a minimum one-hour meeting (Google requested Friday 2025-12-19; Lior suggested Monday). Provide or commit to provide written clarifications on (1) FIPS compliance approach, (2) whether recurring pricing includes SSD hardware and whether SSDs are Self-Encrypting Drives (SEDs), and (3) BYOH partner list and willingness to certify a Google-preferred hardware partner.

---

## Draft Response

Hi Lior,

Bottom line, I can cover the open items for Google on FIPS and SEDs in writing now, and I can join a 60-minute working session on Monday, 2025-12-22. If Google still needs a Friday slot, I can make 2025-12-19 from 3:00-4:00pm PT work.

On the technical follow-ups for David and Kamal:

1) FIPS compliance  
VAST supports FIPS-aligned deployments by using FIPS 140-2/140-3 validated cryptographic modules for data-in-flight protection (TLS) and for key handling when integrated with an approved KMS/HSM. For at-rest encryption, we support both software-based encryption and drive-based encryption (SED), and we can align the final design to Google’s specific FIPS boundary requirements for GDC.

If Google can confirm whether they require “FIPS validated crypto in the data path” versus “FIPS validated key management only,” I will respond with the exact configuration we recommend for GDC and what artifacts we can provide.

2) Pricing, SSDs, and SEDs  
Yes, the recurring pricing in the proposal includes the SSD hardware. For the SSD component, we can supply Self-Encrypting Drives (TCG-compliant SEDs) as part of the BOM when at-rest encryption via SED is required, and we can also support non-SED SSDs when Google prefers encryption handled above the drive layer.

If David wants, I will send a one-page written clarification that states the above explicitly so they can attach it to the RFP record.

3) BYOH partners  
We can support BYOH with our certified eBox partners today, including Cisco, Dell, HPE, and Supermicro. We also have ODM manufacturing options via Arrow and Avnet for our C-Box/D-Box form factors.

Separately, we will certify a Google-preferred hardware partner for this program if Google has a specific vendor they want to standardize on. I will coordinate with our partner team and send you the complete global certified partner list by Wednesday, 2026-01-07 EOD PT, and we can accelerate if Google shares their preferred shortlist.

Scheduling  
Please tell David I can do either of these options:
- Friday, 2025-12-19, 3:00-4:00pm PT  
- Monday, 2025-12-22, 2:00-3:00pm PT or 3:00-4:00pm PT

If you want, forward me David’s email thread and I will reply directly to him with the written clarifications and the time options to lock the meeting.

Best regards,  
Jason Vallery  
VP, Product Management, Cloud  
VAST Data

---

## Original Summary

Google (David Pawlak) requested a follow-up meeting to review VAST Data's GDC Storage RFP proposal and asked for clarifications on FIPS compliance, whether recurring pricing includes SSD hardware and Self-Encrypting Drives (SEDs), and BYOH preferred hardware partners. Lior Genzel looped in Jason Vallery to answer the SED question and committed to checking with VAST partner teams for a full list of certified partners. Google pushed for an earlier meeting (Friday) to walk VAST through a document, while Lior preferred targeting Monday due to being mostly off Friday.

---

*This draft was auto-generated. Edit and send via your email client.*
