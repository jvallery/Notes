---
type: "customer"
title: "Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support"
date: "2025-12-15"
account: ""
participants: ["Jason Vallery", "Alon Horev", "Tomer Hagay", "Violet"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support

**Date**: 2025-12-15
**Account**: [[]]
**Attendees**: Jason Vallery, Alon Horev, Tomer Hagay, Violet

## Summary

After a Google Distributed Cloud RFP walkthrough, Jason Vallery asked Alon Horev and Tomer Hagay for clarification on FIPS/SED options and encryption key granularity across S3 and NFS. Alon redirected to Violet as the subject matter expert, and Tomer provided interim answers: VAST focuses on software-based encryption (potentially FIPS certified), encryption keys are managed at tenant or path level via encryption groups, and S3 SSE-C headers are supported starting in VAST 5.4.


## Action Items


- [?] Engage Violet to confirm and document answers for Google Distributed Cloud RFP encryption questions, including SED/FIPS positioning, key granularity across S3 and NFS, and multi-tenant behavior for buckets, encrypted paths, and views. @Myself ⏫ #task #proposed #auto

- [?] Clarify with Google where the self-encrypting drive (SED) requirement originates (for example, FIPS 140-3 drive removal threat model) to determine whether VAST software-based encryption satisfies the requirement. @Myself #task #proposed #auto

- [?] Provide Google RFP response references to VAST documentation for encryption groups and keys and to VAST 5.4 release notes for SSE-C support via x-amz-server-side-encryption-customer-* headers. @Myself #task #proposed #auto




## Decisions


- Route detailed encryption questions for the Google Distributed Cloud RFP to Violet as the VAST Data subject matter expert (per Alon Horev and Tomer Hagay).




## Key Information


- Alon Horev stated that Violet should be the primary VAST Data contact for questions about encryption key granularity and related encryption matters for the Google Distributed Cloud RFP.

- Tomer Hagay stated that VAST Data prefers software-based encryption rather than relying on self-encrypting drive (SED) hardware capabilities or availability, and that the software-based approach could also be FIPS certified.

- Tomer Hagay stated that VAST Data encryption keys are managed at the tenant level or path level, and that a "path" can be defined for any protocol including S3 buckets and NFS exports, using encryption groups.

- Tomer Hagay stated that an encryption group can be assigned to a path to support having a unique encryption key for that path.

- Tomer Hagay stated that VAST Data supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using the x-amz-server-side-encryption-customer-* headers starting from VAST cluster software version 5.4, and referenced the 5.4 release notes as documentation.

- Tomer Hagay suggested that if self-encrypting drives (SEDs) are requested to meet FIPS 140-3 data-at-rest requirements for protection against drive removal, VAST Data software encryption using FIPS-compatible algorithms should meet the same requirement.



---

*Source: [[2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-]]*