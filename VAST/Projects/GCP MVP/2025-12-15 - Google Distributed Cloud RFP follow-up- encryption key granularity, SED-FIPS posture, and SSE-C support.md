---
type: projects
title: 'Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support'
date: '2025-12-15'
project: GCP MVP
participants:
- Jason Vallery
- Alon Horev
- Tomer Hagay
- Violet (last name unknown)
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md
tags:
- type/projects
- project/gcp-mvp
- generated
---

# Google Distributed Cloud RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support

**Date**: 2025-12-15

**Project**: [[GCP MVP]]

**Attendees**: Jason Vallery, Alon Horev, Tomer Hagay, Violet (last name unknown)

## Summary

Jason Vallery asked Alon Horev and Tomer Hagay for help answering Google Distributed Cloud RFP follow-up questions about FIPS/SED options, software-based encryption, and encryption key granularity across S3 and NFS. Alon and Tomer directed Jason to work with Violet as the subject matter expert, and Tomer provided interim answers plus support documentation links.


## Action Items


- [?] Engage Violet (last name unknown) to confirm and finalize answers for the Google Distributed Cloud RFP follow-up on encryption key granularity across S3, NFS, and block, including multi-tenant behavior for buckets, encrypted paths, and views. @Myself 📅 2025-12-17 ⏫ #task #proposed #auto

- [?] Confirm with the Google Distributed Cloud RFP stakeholders why self-encrypting drives (SEDs) are required (for example, FIPS 140-3 drive removal threat model) and whether VAST software-based FIPS-compatible encryption is acceptable. @Myself 📅 2025-12-17 ⏫ #task #proposed #auto

- [?] Use the VAST support documentation on 'Managing encryption groups and keys' to draft the RFP response section describing tenant-level and path-level key granularity across S3 buckets and NFS exports. @Myself 📅 2025-12-18 #task #proposed #auto

- [?] Validate the exact VAST software version requirement and any limitations for S3 SSE-C support using x-amz-server-side-encryption-customer-* headers (noted as supported starting in VAST 5.4) for inclusion in the Google Distributed Cloud RFP response. @Myself 📅 2025-12-18 #task #proposed #auto




## Decisions


- Route Google Distributed Cloud RFP encryption and key management questions to Violet (last name unknown) as the subject matter expert.




## Key Information


- Alon Horev stated that Violet (last name unknown) should be the primary person to work with on Google Distributed Cloud RFP encryption and key management questions.

- Tomer Hagay stated that VAST prefers software-based encryption (potentially FIPS certified) rather than relying on self-encrypting drive (SED) hardware capabilities or availability.

- Tomer Hagay stated that VAST encryption keys are managed at the tenant level or path level, and that 'path' applies across protocols including S3 buckets and NFS exports, documented under 'encryption groups' in the VAST support documentation.

- Tomer Hagay stated that an encryption group can be assigned to a path to support having a unique encryption key for that path.

- Tomer Hagay stated that VAST supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using the x-amz-server-side-encryption-customer-* headers starting in VAST software version 5.4, and referenced the 5.4 release notes.

- Tomer Hagay stated that if the Google requirement for SEDs is driven by FIPS 140-3 data-at-rest encryption to protect against drive removal, VAST software encryption using FIPS-compatible algorithms should meet the requirement.




---

*Source: [[2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-]]*
