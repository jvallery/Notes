---
type: customer
title: 'Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support'
date: '2025-12-15'
account: Google
participants:
- Myself
- Alon Horev
- Tomer Hagay
- Violet (last name unknown)
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md
tags:
- type/customer
- account/google
- generated
---

# Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support

**Date**: 2025-12-15

**Account**: [[Google]]

**Attendees**: Myself, Alon Horev, Tomer Hagay, Violet (last name unknown)

## Summary

Following a Google Distributed Cloud RFP walkthrough, Jason Vallery asked Alon Horev and Tomer Hagay for clarification on FIPS/SED requirements and encryption key granularity across S3 and NFS. Tomer responded that VAST prefers software-based encryption (potentially FIPS certifiable) over relying on self-encrypting drives, confirmed encryption keys are managed at tenant or path level via encryption groups, and noted SSE-C header support starting in VAST 5.4.


## Action Items


- [?] Engage Violet (VAST contact, last name unknown) to validate and finalize answers for Google Distributed Cloud RFP follow-ups on encryption key granularity, customer-managed keys, encrypted paths, and multi-tenant policy behavior across S3 and NFS. @Myself ⏫ #task #proposed #auto

- [?] Confirm with Google where the self-encrypting drive (SED) requirement originates (for example, FIPS 140-3 drive removal threat model) and whether software-based FIPS-compatible encryption is acceptable for the RFP response. @Myself ⏫ #task #proposed #auto

- [?] Provide Google Distributed Cloud RFP response references for VAST encryption groups and keys documentation and VAST 5.4 SSE-C release notes, and summarize how tenant-level and path-level keys apply to S3 buckets and NFS exports. @Myself #task #proposed #auto




## Decisions


- Route Google Distributed Cloud RFP encryption and key management questions to Violet (VAST contact, last name unknown) as the subject matter expert.




## Key Information


- Alon Horev advised Jason Vallery to work with Violet (VAST contact, last name unknown) on Google Distributed Cloud RFP encryption and key management questions.

- Tomer Hagay stated VAST does not want to be restricted by hardware capabilities or availability for encryption and therefore focuses on software-based encryption that could also be FIPS certified, rather than depending on self-encrypting drives (SEDs).

- Tomer Hagay stated VAST encryption keys are managed at the tenant level or path level, where a "path" can be any protocol endpoint including S3 buckets and NFS exports, using encryption groups.

- Tomer Hagay stated an encryption group can be assigned to a path to support having a unique key for that path (unique key per encrypted path).

- Tomer Hagay stated VAST supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using x-amz-server-side-encryption-customer-* headers starting from VAST software version 5.4, and referenced the 5.4 release notes.

- Tomer Hagay asked for clarification on the origin of the self-encrypting drive (SED) requirement and noted that if SEDs are used to meet FIPS 140-3 data-at-rest encryption requirements (for example, protection against drive removal), VAST software using the same FIPS-compatible encryption algorithms should meet the requirement.

- Jason Vallery reported that during a Google Distributed Cloud RFP walkthrough call, Google asked follow-up questions about FIPS-certified QLC/self-encrypting drives, VAST support for SEDs and key management, and documentation for encryption key granularity across S3 and NFS in multi-tenant environments.




---

*Source: [[2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-]]*
