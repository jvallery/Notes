---
type: customer
title: Google GDC RFP review
date: '2025-12-15'
account: Google
participants:
- Jason Vallery
- Lior Genzel
- David Pollack
- Jeff
- Kamal
- Malikarjan Sehzal
- Seiza Gersman
- Gopal
- Tim
- David
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-12-15 16 10 - Google GDC RFP.md
tags:
- type/customer
- account/google
- generated
---

# Google GDC RFP review

**Date**: 2025-12-15
**Account**: [[Google]]
**Attendees**: Jason Vallery, Lior Genzel, David Pollack, Jeff, Kamal, Malikarjan Sehzal, Seiza Gersman, Gopal, Tim, David

## Summary

Google’s procurement/product/storage engineering team reviewed VAST’s RFP responses and pricing at a high level, focusing on several “No” technical requirements (data-to-media isolation, synchronous replication/zero RPO, multi-region active-active consistency, granular S3 encryption, and fault-injection APIs). VAST explained architectural constraints (sharded/striped data across cluster, strong-consistency hub-and-spoke global namespace, roadmap items like global write leases and traffic failover) and walked through pricing assumptions (2x1 building block, bundled support, capacity-based discounts, and upcoming licensing change to per-terabyte increments on 2026-02-01). Key open questions remain around FIPS-certified QLC options, self-encrypting drive (SED) support and pricing, and encryption key granularity beyond tenant level.
## Action Items
- [ ] Provide details on FIPS-compliant drive options (including largest FIPS-certified QLC) for the proposed hardware shapes/sizes and how that impacts the proposed configurations. @TBD ⏫ #task
- [ ] Follow up with clarification on encryption key granularity (tenant vs view/subtree vs bucket/object) across block, file, and object, and how it maps to bucket policies/KMS integration. @TBD ⏫ #task
- [ ] Check internally and respond on whether VAST software supports self-encrypting drives (SEDs) and external key managers for SEDs, and whether ODM hardware options/pricing differ for SEDs. @TBD ⏫ #task
- [ ] Send a detailed email explaining pricing structure/knobs (capacity-based discounts, dark site uplift, 4-hour vs NBD support delta, SKU math) and the formula behind the quoted numbers. @TBD #task
- [ ] Digest the spreadsheet with the internal team and send follow-up questions in writing ahead of the next meeting; include a note summarizing discussed open items for tracking. @Myself #task

## Key Information
- RFP technical “No” items called out included B8, B16, C2, C3, C8, C18, and D7.
- B8: VAST cannot map a dataset/volume to specific physical disks/media because data is sharded/striped with data reduction, encryption, and erasure coding; logical isolation is via multi-tenancy and key management.
- Compliance scenario discussed: some customers may require confiscation of all media for a dataset, which implies physical mapping; workaround would be separate clusters per tenant but is suboptimal.
- B16: VAST does not currently support synchronous file/namespace replication with zero RTO/zero RPO across zones; can do low RPO/RTO (~10 seconds) and cluster-to-cluster sync block replication; file policy-driven synchronous replication is not configurable today.
- C8: VAST supports a hub-and-spoke global namespace model with one authoritative primary and satellites; active-active-active multi-region is not supported. Global write leases are on the roadmap for late summer 2026 timeframe; automatic traffic failover/load balancer is also on the roadmap but not delivered yet.
- C18: More granular S3 encryption semantics (e.g., client-provided keys per PUT/GET) are not implemented today; VAST sets encryption keys at tenant level (may be view-level/subtree—needs confirmation).
- D7: No dedicated fault-injection API; management API can perform some disruptive actions (e.g., take node out of service) but not designed for fault injection; Google wants automated fault simulation for SLO regression testing (drive/controller failures).
- Pricing: VAST used an entry-level 2x1 building block (2 C nodes + 1 D-box) for smaller requested clusters; pricing includes software, support, and quoted hardware (switches, cables, installation) but VAST does not take margin on hardware and is open to customer-supplied hardware with validation.
- C-boxes can be standard servers; D-boxes are dense flash shelves designed with ODM partners; E-box is a hyperconverged model (C and D containers on same server) used by OEM partners like Cisco, with tradeoffs (fixed perf/capacity ratio, more east-west traffic).
- Support is bundled into subscription; 4-hour vs next business day support is ~10% price difference; dark site uplift is ~<10%. Larger clusters get at least ~10% discount; deeper discounts at very large scale (e.g., exabyte deals).
- Current licensing uses 100TB usable capacity SKU increments; partial licensing was used for one line item; VAST plans to change to per-terabyte increments effective 2026-02-01 and asked not to place POs before 2026-02-01.
- Hardware assumptions did not explicitly account for self-encrypting drives; question remains whether SEDs are supported and what ODM options exist.
- Lab/POC: VAST indicated POCs would not be charged for software; lab configurations conceptually ~50% off pricing (details depend on equipment).
- An email referenced a $12.1M hardware investment; VAST wants clarity on usage, payment terms, and acquisition timing.

## Topics
- RFP technical requirements review (B8/B16/C2/C3/C8/C18/D7)
- Regulatory compliance and physical data/media isolation
- Synchronous replication and zero RPO/RTO expectations
- Multi-region consistency, global namespace, and roadmap (write leases, failover)
- Encryption at rest and customer-managed keys (tenant/bucket/object granularity)
- FIPS compliance and QLC drive availability
- Fault injection and SLO regression testing
- Pricing model, SKUs, discounts, and upcoming licensing change (per-TB)
- Hardware configurations (C-node/D-box/E-box), ODM vs OEM sourcing
- Self-encrypting drives (SED) support and external key management
- POC/lab pricing and bidder investment expectations

---

*Source: [[Inbox/_archive/2025-12-15/2025-12-15 16 10 - Google GDC RFP.md|2025-12-15 16 10 - Google GDC RFP]]*

## Related

- [[Cisco]]
- [[Dell]]
- [[HPE]]
- [[Lior Genzel]]
- [[Jason Vallery]]
- [[Google Distributed Cloud RFP]]
