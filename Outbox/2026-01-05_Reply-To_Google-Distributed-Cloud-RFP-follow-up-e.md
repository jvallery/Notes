---
type: draft-reply
status: pending
created: "2026-01-05T19:37:02.077124"
urgency: "normal"
to: "Alon Horev <alon@vastdata.com>"
subject: "Re: Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
---

# Draft Reply to Alon Horev

**Regarding**: Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support
**Urgency**: normal

---

## Key Points to Address

Reply internally to Alon Horev and Tomer Hagay acknowledging Violet as the SME, confirm you will engage Violet, and summarize the interim answers: VAST focuses on software-based encryption (potentially FIPS certifiable), encryption groups can be applied at tenant or path level (including S3 buckets and NFS exports) with unique keys per path, and SSE-C support via x-amz-server-side-encryption-customer-* headers is available starting in VAST 5.4 with release notes as reference. Ask Tomer for any additional guidance on the multi-tenant mapping of buckets, encrypted paths, and views to customer-managed keys and policy, and ask where the SED requirement originates in Google's RFP.

---

## Draft Response

Hi Alon,

Bottom line: Violet is the right SME for the FIPS/SED portion, and I’ll engage her today and send you a consolidated answer by 2026-01-08 EOD PT. In the meantime, Tomer’s interim guidance is solid: VAST’s primary posture is software-based encryption (with a path toward FIPS-certifiable implementations), encryption groups can be applied at the tenant or path level (covering both S3 buckets and NFS exports) with unique keys per path, and S3 SSE-C using the x-amz-server-side-encryption-customer-* headers is supported starting in VAST 5.4 (per the 5.4 release notes Tomer referenced).

On SEDs specifically, our current direction is not to rely on drive-level SED as the primary control; we’ll confirm with Violet what we can state about SED interoperability/validated models and any key-management integration expectations or limitations for Google’s RFP language. If the RFP is explicitly requiring “FIPS-certified QLC using SED,” I want to understand whether that’s a hard requirement or a generic checkbox that can be satisfied via software encryption + FIPS posture.

Tomer—can you add any additional guidance on the multi-tenant mapping story (S3 buckets, encrypted paths, and views) to customer-managed keys and policy, and whether we have a single end-to-end doc we should point Google to? Also, do we know where the SED requirement originates in the Google Distributed Cloud RFP (exact section/wording), so we can respond precisely rather than over-scoping?

Thanks,  
Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

Internal email thread between Jason Vallery, Alon Horev, and Tomer Hagay to answer Google Distributed Cloud RFP follow-up questions on FIPS/SED requirements, encryption key granularity across S3 and NFS, and S3 SSE-C support. Tomer clarified VAST’s position favoring software-based encryption (potentially FIPS certifiable), confirmed encryption groups can be applied at tenant or path level (including S3 buckets and NFS exports), and confirmed SSE-C header support starting in VAST 5.4.

---

*This draft was auto-generated. Edit and send via your email client.*
