---
type: projects
title: 'Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support'
date: '2025-12-15'
project: GCP MVP
participants:
- Alon Horev
- Tomer Hagay
- Myself
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md
tags:
- type/projects
- project/gcp-mvp
- generated
---

# Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS, and SSE-C support

**Date**: 2025-12-15

**Project**: [[GCP MVP]]

**Attendees**: Alon Horev, Tomer Hagay, Myself

## Summary

Internal email thread between Jason Vallery, Alon Horev, and Tomer Hagay to answer Google Distributed Cloud RFP follow-up questions on FIPS/SED requirements, encryption key granularity across S3 and NFS, and S3 SSE-C support. Tomer clarified VAST’s position favoring software-based encryption (potentially FIPS certifiable), confirmed encryption groups can be applied at tenant or path level (including S3 buckets and NFS exports), and confirmed SSE-C header support starting in VAST 5.4.


## Action Items


- [?] Engage Violet (internal SME) to validate and finalize answers for Google Distributed Cloud RFP follow-up questions on encryption key granularity, customer-managed keys, encrypted paths, and SSE-C behavior/gotchas. @Myself ⏫ #task #proposed #auto

- [?] Confirm the origin and rationale of Google's self-encrypting drive (SED) requirement for the Google Distributed Cloud RFP (for example, whether it is specifically tied to FIPS 140-3 drive-removal threat model) and feed that context back into the RFP response. @Myself #task #proposed #auto

- [?] Use VAST documentation on 'Managing encryption groups and keys' to support the Google Distributed Cloud RFP response regarding tenant-level and path-level encryption key granularity across S3 and NFS. @Myself #task #proposed #auto

- [?] Reference VAST 5.4 release notes to document S3 SSE-C support via x-amz-server-side-encryption-customer-* headers in the Google Distributed Cloud RFP response. @Myself #task #proposed #auto




## Decisions


- For Google Distributed Cloud RFP responses, position VAST as focusing on software-based encryption (potentially FIPS certifiable) rather than relying on self-encrypting drive (SED) hardware capabilities or availability.




## Key Information


- Alon Horev advised Jason Vallery to work with a person named Violet on Google Distributed Cloud RFP encryption and key management questions, indicating Violet is the internal subject matter expert for these topics.

- Tomer Hagay stated that Violet is the expert on encryption/key management topics for the Google Distributed Cloud RFP follow-ups.

- Tomer Hagay stated VAST prefers software-based encryption (which could be FIPS certified) rather than being restricted by self-encrypting drive (SED) hardware capabilities or availability.

- Tomer Hagay stated VAST encryption keys can be configured at the tenant level or the path level, and that 'path' includes any protocol, including S3 buckets and NFS exports.

- Tomer Hagay stated an encryption group can be assigned to a path to support having a unique key for that path.

- Tomer Hagay stated VAST supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using the x-amz-server-side-encryption-customer-* headers starting from VAST software version 5.4, and referenced the 5.4 release notes as documentation.

- Tomer Hagay suggested that if self-encrypting drives (SEDs) are requested to meet FIPS 140-3 data-at-rest encryption requirements for protection against drive removal, VAST software encryption using FIPS-compatible algorithms should meet the same requirement.

- Jason Vallery reported that a Google Distributed Cloud RFP walkthrough call with Google generated follow-up questions about FIPS-certified QLC/SED options, software support for SEDs and key management, and documentation for encryption key granularity across S3 and NFS in a multi-tenant context.




---

*Source: [[2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-]]*
