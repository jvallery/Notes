---
type: customer
title: GDC RFP encryption key questions
date: "2025-12-15"
account: Google
participants:
  - Jason Vallery
  - Alon Horev
  - Tomer Hagay
  - Violet
source: email
tags:
  - type/customer
  - account/google
  - project/gdc-rfp
---

# GDC RFP Encryption Key Questions

**Date**: 2025-12-15

## Summary

Following the GDC RFP walkthrough with Google, technical questions came up about FIPS certification, self-encrypting drives, and encryption key granularity. Tomer and Alon provided initial guidance, with Violet as the expert for detailed follow-up.

## Questions from Google

1. **FIPS-certified QLC option** - Looking for self-encrypting drives (SEDs). Have we validated specific drives?
2. **SED compatibility** - Can our software stack work with self-encrypting drives for key management?
3. **Encryption key granularity** - Documentation walking through encryption across S3 and NFS

## Technical Details to Verify

- Customer Managed Keys as "Encryption Groups" at tenant level
- Encrypted Paths - new encryption group per sub-directory
- Unique key per encrypted path capability
- S3 SSE-C support via x-amz-server-side-encryption-customer-\* headers
- How buckets, encrypted paths, and views work with customer managed keys in multi-tenant setup

## Answers from Tomer

1. **SEDs**: VAST focuses on software-based encryption (FIPS certifiable) rather than HW-dependent SED
2. **Encryption keys**: At path or tenant level - "Path" includes S3 buckets and NFS exports
3. **Documentation**: [Encryption Groups Guide](https://support.vastdata.com/s/document-item?bundleId=vast-cluster-administrator-s-guide5.3&topicId=managing-data/encryption-of-data-at-rest/managing-encryption-groups-and-keys.html)

## Open Question

- If SEDs are required for FIPS 140-3, VAST SW with FIPS-compatible encryption algorithms should meet requirement - need to clarify Google's specific requirement source

## Action Items

- [ ] Follow up with Violet for detailed encryption architecture answers 📅 2025-12-18 🔼 #task
- [ ] Clarify Google's SED requirement source @Tomer Hagay 🔽 #task

## Contacts

- [[Alon Horev]] - VAST (routed to Violet)
- [[Tomer Hagay]] - VAST PM
- [[Violet]] - Encryption expert
