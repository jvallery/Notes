---
type: draft-reply
status: pending
created: "2026-01-05T19:37:19.863486"
urgency: "normal"
to: "Alon Horev <alon@vastdata.com>"
subject: "Re: Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
---

# Draft Reply to Alon Horev

**Regarding**: Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support
**Urgency**: normal

---

## Key Points to Address

Acknowledge Alon Horev and Tomer Hagay guidance to work with Violet; confirm interim answers for Google Distributed Cloud RFP: VAST positions software-based encryption (potentially FIPS certifiable) vs committing to SED hardware; encryption groups provide tenant and path-level keys across protocols including S3 buckets and NFS exports; unique key per path is supported by assigning an encryption group to that path; SSE-C via x-amz-server-side-encryption-customer-* headers is supported starting in VAST 5.4. Ask Google to clarify the origin of the SED requirement and whether it is specifically tied to FIPS 140-3 drive-removal threat model.

---

## Draft Response

Hi Alon,  

Thanks for the guidance—I'll work directly with Violet on the Google Distributed Cloud RFP encryption/FIPS/SED items. In the meantime, I want to confirm Tomer’s interim answers are what we should anchor on for the response: VAST’s position is software-based encryption (with a path to FIPS certifiability) rather than committing to specific self-encrypting drive (SED) models, and encryption keys are managed via encryption groups that can be applied at the tenant and path level across protocols (including S3 buckets and NFS exports).  

On key granularity, we can support a unique key per encrypted path by assigning a distinct encryption group to that path (and similarly for S3 by applying the encryption group to the bucket / relevant namespace construct). On S3 SSE-C, we support the x-amz-server-side-encryption-customer-* headers starting in VAST 5.4; I’ll have Violet confirm any operational constraints/gotchas and the best authoritative documentation to cite for both encryption groups and SSE-C.  

One clarification I’d like to drive with Google: what is the source of the SED requirement, and is it specifically tied to a FIPS 140-3 data-at-rest posture for drive-removal scenarios? If you have any context from the RFP language or prior GDC guidance, please forward it—otherwise I’ll ask the Google team directly and circle back with what we learn by Wednesday, January 8.  

Best,  
Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

Following a Google Distributed Cloud RFP walkthrough, Jason Vallery asked Alon Horev and Tomer Hagay for clarification on FIPS/SED requirements, encryption key granularity across S3 and NFS, and S3 SSE-C support. Alon directed Jason to work with Violet as the subject matter expert. Tomer provided interim answers: VAST prefers software-based encryption (potentially FIPS certifiable) over relying on self-encrypting drives, encryption keys are managed via encryption groups at tenant or path level (including S3 buckets and NFS exports), and SSE-C headers are supported starting in VAST 5.4.

---

*This draft was auto-generated. Edit and send via your email client.*
