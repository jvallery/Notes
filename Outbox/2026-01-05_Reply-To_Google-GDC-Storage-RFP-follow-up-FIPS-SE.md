---
type: draft-reply
status: pending
created: "2026-01-05T19:47:16.586558"
urgency: "urgent"
to: "Lior Genzel <lior.genzel@vastdata.com>"
subject: "Re: Google GDC Storage RFP follow-up: FIPS, SEDs, BYOH partner list, and meeting scheduling"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-23_004718_3592_Re-VAST-Data---GDC-Storage-RFP---Request-For-Meeting.md"
ai_model: "gpt-5.2"
ai_temperature: 0.3
prompt_file: "Outbox/_prompts/2026-01-05_Reply-To_Google-GDC-Storage-RFP-follow-up-FIPS-SE.prompt.json"
---

# Draft Reply to Lior Genzel

**Regarding**: Google GDC Storage RFP follow-up: FIPS, SEDs, BYOH partner list, and meeting scheduling
**Urgency**: urgent

---

## Key Points to Address

Confirm Jason Vallery contact details are included; propose specific meeting times for Monday 2025-12-22 (or offer limited Friday 2025-12-19 availability if feasible); answer or commit to follow up on (1) FIPS compliance approach, (2) whether recurring pricing includes hardware and SSDs, (3) whether SSDs are Self-Encrypting Drives (SEDs), and (4) BYOH partner list and ability to certify a Google-preferred partner.

---

## Draft Response

Hi Lior,

Bottom line, we can confidently answer Google’s FIPS and SED questions now, and I can get David a clean BYOH partner list plus propose concrete meeting times for Monday, December 22, 2025.

For scheduling, I can make any of the following work on Monday, December 22 (PT):
- 10:00-11:00 AM PT
- 1:00-2:00 PM PT
- 3:00-4:00 PM PT

If you want a backup option, I can also do Friday, December 19 from 2:30-3:30 PM PT, but Monday is better on my side.

Here are the written follow-ups you can forward to David (or I can send directly if you prefer):

FIPS compliance
- VAST supports FIPS 140-2 compliant cryptography for data-in-flight via TLS using FIPS-validated crypto modules when deployed on FIPS-enabled operating systems.
- For data-at-rest, we support encryption at rest with keys managed by an external KMS, and we can align the deployment to a FIPS posture by using FIPS-validated components in the host OS and key management path.
- If Google’s requirement is specifically “FIPS 140-2 validated at-rest encryption implemented in drive hardware” versus software-based encryption, that ties directly to the SED selection below.

Pricing, hardware, and SEDs
- Yes, the recurring pricing in the proposal includes the hardware for the VAST storage nodes and the SSD media, as Lior noted, we do not sell HDD-based configurations for this offering.
- On SEDs, we can deliver the SSD component as Self-Encrypting Drives (TCG-compliant SEDs) when required by the customer security profile, and we will specify the exact drive SKUs as part of final BOM lock for the award.
- If Google needs a specific SED standard (for example, TCG Enterprise vs Opal, or a specific FIPS-validated drive model), we will align the BOM to that requirement during final configuration.

BYOH partner list
- We support BYOH via certified eBox partners today, including Cisco, Dell, HPE, and Supermicro, plus ODM manufacturing via Arrow and Avnet for our C/D box solutions.
- We can also certify a Google-preferred hardware partner for this program, assuming we agree on the target platform requirements and run the standard qualification process.

Next steps
1) Please reply with your preferred Monday time slot (or confirm if you want me to take the Friday 2:30 PM PT backup).
2) Tell me whether you want me to email David directly with the above, or if you’d like to forward it from your thread.
3) I will send you the expanded global certified partner list by Tuesday, January 6, 2026 at 12:00 PM PT after I confirm with our partner team.

Thanks for looping me in.

Best regards,  
Jason Vallery  
VP, Product Management, Cloud  
VAST Data

---

## Original Summary

Google (David Pawlak) requested a follow-up meeting to review and clarify VAST Data's GDC Storage RFP proposal and asked for written clarifications on FIPS compliance, whether recurring pricing includes hardware and Self-Encrypting Drives (SEDs), and BYOH preferred hardware partners. Lior Genzel looped in Jason Vallery to address the SEDs question and committed to checking with VAST partner teams for a full list of certified global hardware partners.

---

*This draft was auto-generated. Edit and send via your email client.*
