---
type: "projects"
title: "GDC RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support"
date: "2025-12-15"
project: ""
participants: ["Jason Vallery", "Alon Horev", "Tomer Hagay", "Violet"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# GDC RFP follow-up: encryption key granularity, SED/FIPS posture, and SSE-C support

**Date**: 2025-12-15
**Project**: [[]]
**Attendees**: Jason Vallery, Alon Horev, Tomer Hagay, Violet

## Summary

Internal email thread between Jason Vallery, Alon Horev, and Tomer Hagay to answer Google Distributed Cloud (GDC) RFP follow-up questions on data-at-rest encryption. Alon and Tomer direct Jason to work with Violet as the subject matter expert, and Tomer provides interim guidance on software-based encryption, encryption group granularity, and S3 SSE-C support starting in VAST 5.4.


## Action Items


- [?] Engage Violet to confirm authoritative answers for the Google Distributed Cloud (GDC) RFP follow-up, including FIPS-certified QLC/SED positioning, software stack compatibility with SEDs and key management, and documentation for encryption key granularity across S3 and NFS. @Myself ⏫ #task #proposed #auto

- [?] Determine the source and rationale of Google's self-encrypting drive (SED) requirement in the GDC RFP (for example, whether it is specifically to satisfy FIPS 140-3 drive-removal threat model) and report back to Tomer Hagay and Violet. @Myself #task #proposed #auto

- [?] Share with the Google RFP response team the VAST documentation links for encryption groups and VAST 5.4 SSE-C support, and validate any 'gotchas' for SSE-C usage in the GDC context. @Myself #task #proposed #auto




## Decisions


- Route Google Distributed Cloud (GDC) RFP encryption follow-up questions to Violet as the primary subject matter expert.




## Key Information


- Alon Horev advised Jason Vallery to work with Violet as the subject matter expert for encryption-related questions for the Google Distributed Cloud (GDC) RFP follow-up.

- Tomer Hagay stated that Violet is the expert for VAST encryption topics related to the Google Distributed Cloud (GDC) RFP follow-up.

- Tomer Hagay stated VAST prefers software-based encryption rather than relying on self-encrypting drive (SED) hardware capabilities or availability, and that software-based encryption can be FIPS certified.

- Tomer Hagay stated encryption keys in VAST are managed at the tenant level or at the path level, and that 'path' includes any protocol including S3 buckets and NFS exports.

- Tomer Hagay stated an encryption group can be assigned to a path to support having a unique encryption key for that path.

- Tomer Hagay stated VAST supports S3 Server-Side Encryption with Customer-Provided Keys (SSE-C) using x-amz-server-side-encryption-customer-* headers starting from VAST software version 5.4, and referenced the 5.4 release notes as documentation.

- Tomer Hagay asked where the self-encrypting drive (SED) requirement originates and noted that if SEDs are used to meet FIPS 140-3 data-at-rest encryption requirements for protection against drive removal, VAST software using FIPS-compatible encryption algorithms should meet the requirement.



---

*Source: [[2025-12-15_183201_0409_Re-Google-Distributed-Cloud---RFP-Follow-up3-Encryption-key-]]*