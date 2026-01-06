---
type: draft-reply
status: pending
created: "2026-01-05T19:14:46.372348"
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

Acknowledge Alon Horev and Tomer Hagay guidance to work with Violet (encryption SME). Summarize interim answers: VAST prefers software-based encryption over SED dependency; encryption keys are tenant or path level via encryption groups (paths include S3 buckets and NFS exports); unique key per path is supported by assigning an encryption group to that path; SSE-C via x-amz-server-side-encryption-customer-* headers is supported starting in VAST 5.4. Ask Google to clarify the origin of the SED requirement (for example, FIPS 140-3 drive removal threat model) to confirm software encryption suffices.

---

## Draft Response

Hi Alon,

Thank you for your email. Here's my response:

- Acknowledge Alon Horev and Tomer Hagay guidance to work with Violet (encryption SME)
- Summarize interim answers: VAST prefers software-based encryption over SED dependency; encryption keys are tenant or path level via encryption groups (paths include S3 buckets and NFS exports); unique key per path is supported by assigning an encryption group to that path; SSE-C via x-amz-server-side-encryption-customer-* headers is supported starting in VAST 5.4
- Ask Google to clarify the origin of the SED requirement (for example, FIPS 140-3 drive removal threat model) to confirm software encryption suffices.

To answer your questions:
- Does VAST have a FIPS-certified QLC option and have any specific self-encrypting drives (SEDs) been validated for use with VAST?: [TODO: Add answer]
- Does the VAST software stack support working with self-encrypting drives (SEDs), including key management integration?: [TODO: Add answer]
- Can VAST configure a unique encryption key per encrypted path (sub-directory) via encryption groups, and how is this represented in documentation?: [TODO: Add answer]

I'll follow up on:
- Tomer Hagay provided interim answers and documentation links for encryption groups/key granularity and SSE-C support while recommending Violet as the expert.

Let me know if you have any questions.

Best,
Jason

---

## Original Summary

Following a Google Distributed Cloud RFP walkthrough, Jason Vallery asked Alon Horev and Tomer Hagay for clarification on FIPS/SED options and encryption key granularity across S3 and NFS. Tomer responded with VAST's position favoring software-based encryption over self-encrypting drives, confirmed encryption keys are managed at tenant or path level via encryption groups, and confirmed SSE-C support via x-amz-server-side-encryption-customer-* headers starting in VAST 5.4.

---

*This draft was auto-generated. Edit and send via your email client.*
