---
type: "customer"
title: "Google Distributed Cloud RFP follow-up: encryption at rest, SEDs, and key granularity across S3 and NFS"
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

# Google Distributed Cloud RFP follow-up: encryption at rest, SEDs, and key granularity across S3 and NFS

**Date**: 2025-12-15
**Account**: [[]]
**Attendees**: Jason Vallery, Alon Horev, Tomer Hagay, Violet

## Summary

After a Google Distributed Cloud RFP walkthrough, Jason Vallery asked Alon Horev and Tomer Hagay for clarification on FIPS and self-encrypting drive (SED) requirements, and on encryption key granularity across S3 and NFS. Alon redirected to Violet as the subject matter expert, and Tomer provided interim answers including that VAST focuses on software-based encryption (potentially FIPS certified), encryption groups can be applied at tenant or path level across protocols, and S3 SSE-C headers are supported starting in VAST 5.4.


## Action Items


- [?] Engage Violet (VAST Data) to provide authoritative answers for the Google Distributed Cloud RFP on FIPS/SED requirements, encryption group and encrypted path behavior, and multi-tenant mapping across S3 buckets, NFS exports, views, and policies. @Myself ⏫ #task #proposed #auto

- [?] Confirm with Google Distributed Cloud RFP stakeholders why self-encrypting drives (SEDs) are being required (for example, FIPS 140-3 drive removal threat model) and whether software-based FIPS-compatible encryption is acceptable. @Myself ⏫ #task #proposed #auto

- [?] Share VAST Data documentation links with the Google Distributed Cloud RFP team: (1) "Managing encryption groups and keys" for tenant/path key granularity across protocols, and (2) VAST 5.4 release notes for S3 SSE-C header support. @Myself #task #proposed #auto




## Decisions


- Route detailed encryption and key management questions for the Google Distributed Cloud RFP to Violet as the subject matter expert.




## Key Information


- Alon Horev stated that Violet should be the primary person to work with on encryption and related RFP matters for Google Distributed Cloud.

- Tomer Hagay stated that VAST Data prefers not to be restricted by hardware capabilities or availability for encryption and therefore focuses on software-based encryption that could also be FIPS certified, rather than relying on self-encrypting drives (SEDs).

- Tomer Hagay stated that VAST Data encryption keys can be managed at the tenant level or at the path level, and that a "path" can be defined for any protocol including S3 buckets and NFS exports via encryption groups.

- Tomer Hagay stated that an encryption group can be assigned to a path to support having a unique encryption key for that path.

- Tomer Hagay stated that VAST Data supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using the x-amz-server-side-encryption-customer-* headers starting from VAST cluster version 5.4, and referenced the 5.4 release notes as documentation.

- Tomer Hagay suggested that if self-encrypting drives (SEDs) are being requested to meet FIPS 140-3 data-at-rest requirements for protection against drive removal, VAST Data software encryption using the same FIPS-compatible algorithms should meet the requirement.



---

*Source: [[2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-]]*