---
type: "customer"
title: "Google Distributed Cloud RFP technical requirements review (B8 data-to-media mapping, B16 sync replication)"
date: "2025-12-15"
account: ""
participants: ["Jason Vallery", "Lior Genzel", "Speaker 1", "Speaker 3", "Speaker 4", "Speaker 5", "Speaker 7"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-15 16 10 - Google GDC RFP.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# Google Distributed Cloud RFP technical requirements review (B8 data-to-media mapping, B16 sync replication)

**Date**: 2025-12-15
**Account**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Speaker 1, Speaker 3, Speaker 4, Speaker 5, Speaker 7

## Summary

Google team walked VAST through the GDC RFP proposal technical requirements spreadsheet, focusing on items VAST marked as "No". Key gaps discussed were (1) inability to map a dataset/volume to specific physical disks due to VAST's distributed data layout, and (2) lack of synchronous replication with zero RTO and zero RPO across zones, with VAST offering snapshot-based replication and low (but non-zero) RTO/RPO today.


## Action Items


- [?] Confirm which RFP technical requirement rows were marked "No" in the submitted Google GDC RFP spreadsheet (B8, B16, C2, C3, C8, C18, D7 were read out on the call) and prepare a written explanation per row with VAST Data capability, workaround, and risk. @Myself ⏫ #task #proposed #auto

- [?] Follow up with Google (David Pollack, Kamal, Malikarjan, and Jeff) to capture the exact regulatory compliance requirement behind B8, including whether separate clusters per tenant/dataset is acceptable and what evidence or controls Google needs for audit/regulator requests. @Myself ⏫ #task #proposed #auto

- [?] Clarify with Google the precise B16 requirement scope (file-level vs block-level replication, cross-zone topology, and acceptable RTO/RPO targets) and document VAST Data's current snapshot-based and cluster-to-cluster replication options plus performance tradeoffs. @Myself ⏫ #task #proposed #auto




## Decisions


- The group agreed to proceed through the RFP technical requirements spreadsheet top-to-bottom, starting with the items marked "No" (including B8 and B16) to understand gaps and scenarios.




## Key Information


- Lior Genzel stated he was born during Hanukkah and that his name "Lior" means "my light".

- Jason Vallery introduced himself as VP of Cloud Product Management at VAST Data.

- Google RFP participants included David Pollack (Partnerships Lead), Seiza Gersman and Gopal (procurement team overseeing the bid through completion), Kamal and Malikarjan (product management), and Jeff (storage engineering).

- For RFP requirement B8, VAST Data explained that due to data reduction, encryption, and erasure coding, data blocks are distributed across the cluster and cannot be isolated to a specific share, volume, or set of physical disks; logical multi-tenancy and key management provide separation above the physical pool.

- Google explained the driver for RFP requirement B8 was a regulatory compliance scenario where a regulator may require confiscation of all physical media associated with a particular dataset/volume, which requires mapping the dataset to specific disks; a fallback is using separate clusters per dataset/tenant, but that is operationally suboptimal.

- For RFP requirement B16, VAST Data stated it does not currently provide synchronous replication with zero RTO and zero RPO across zones because of latency and performance penalties; VAST can deliver low (non-zero) RTO/RPO on the order of ~10 seconds across multiple zones today and has considered zero RTO/RPO but it is not currently prioritized.

- A Google storage engineering participant (Jeff, last name not provided) expected the B8 isolation limitation based on VAST's architecture and indicated it would need to be addressed as a 'call isolation' concern for the solution.

- Google stated there are workload use cases requiring synchronous replication and zero RPO for files, and they believed prior discussions with VAST suggested element-level replication might already provide this or would be delivered soon.

- VAST Data clarified that current replication is snapshot-based today, and referenced cluster-to-cluster synchronous block-level replication, while file-level multi-zone policy-driven replication was discussed as a separate capability area (details truncated in transcript).



---

*Source: [[2025-12-15 16 10 - Google GDC RFP]]*