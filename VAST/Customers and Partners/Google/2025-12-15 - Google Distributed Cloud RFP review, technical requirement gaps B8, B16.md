---
type: customer
title: Google Distributed Cloud RFP review, technical requirement gaps (B8, B16)
date: '2025-12-15'
account: Google
participants:
- Jason Vallery
- Lior Genzel
- Speaker 1
- Speaker 3
- Speaker 4
- Speaker 5
- Speaker 7
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-15 16 10 - Google GDC RFP.md
tags:
- type/customer
- generated
---

# Google Distributed Cloud RFP review, technical requirement gaps (B8, B16)

**Date**: 2025-12-15
**Account**: [[Google]]
**Attendees**: Jason Vallery, Lior Genzel, Speaker 1, Speaker 3, Speaker 4, Speaker 5, Speaker 7

## Summary

Google participants walked VAST through the submitted Google Distributed Cloud RFP response, focusing on the technical requirements tab and the items VAST marked as 'No'. The discussion centered on (1) whether VAST can map a dataset or volume to specific physical disks for regulatory confiscation scenarios (B8) and (2) whether VAST supports synchronous replication with zero RTO and zero RPO across zones (B16), which VAST stated is not currently prioritized due to performance tradeoffs.

## Action Items

- [?] Confirm which Google Distributed Cloud RFP technical requirements were marked 'No' in VAST's submission (B8, B16, C2, C3, C8, C18, D7) and prepare precise written clarifications for each item, including whether any are 'No today but possible with architecture changes' versus 'No by design'. @Myself ⏫ #task #proposed #auto

- [?] Follow up with the Google storage engineering contact 'Jeff' to capture Google’s acceptability criteria and any workaround options for requirement B8 (regulatory confiscation scenario), including whether disjoint clusters per tenant/dataset is acceptable for Google Distributed Cloud deployments. @Myself ⏫ #task #proposed #auto

- [?] Clarify with Google product management (Kamal and Malikarjan) the specific workload use cases driving requirement B16 (synchronous replication, zero RPO for files) and whether low RPO (approximately 10 seconds) is acceptable for any subset of those workloads. @Myself ⏫ #task #proposed #auto

- [?] Confirm which RFP technical requirement rows were marked "No" in the submitted Google GDC RFP spreadsheet (B8, B16, C2, C3, C8, C18, D7 were read out on the call) and prepare a written explanation per row with VAST Data capability, workaround, and risk. @Myself ⏫ #task #proposed #auto

- [?] Follow up with Google (David Pollack, Kamal, Malikarjan, and Jeff) to capture the exact regulatory compliance requirement behind B8, including whether separate clusters per tenant/dataset is acceptable and what evidence or controls Google needs for audit/regulator requests. @Myself ⏫ #task #proposed #auto

- [?] Clarify with Google the precise B16 requirement scope (file-level vs block-level replication, cross-zone topology, and acceptable RTO/RPO targets) and document VAST Data's current snapshot-based and cluster-to-cluster replication options plus performance tradeoffs. @Myself ⏫ #task #proposed #auto

## Decisions

- Proceed through the Google Distributed Cloud RFP technical requirements tab top-to-bottom, starting with the items VAST marked as 'No' (including B8 and B16), to clarify gaps and scenarios.

- The group agreed to proceed through the RFP technical requirements spreadsheet top-to-bottom, starting with the items marked "No" (including B8 and B16) to understand gaps and scenarios.

## Key Information

- Lior Genzel stated he was born during Hanukkah and that his name 'Lior' relates to 'my light' in the Hanukkah context.

- Google RFP review call attendees from Google included David Pollack (Partnerships Lead), Seiza Gersman and Gopal (procurement team overseeing the bid through completion), Kamal and Malikarjan (product management), and Jeff (storage engineering).

- VAST Data architecture described by Jason Vallery: data reduction, encryption, and erasure coding distribute blocks across the cluster, so data cannot be isolated to a specific share or volume at the physical media level; logical multi-tenancy and key management provide separation above the physical pool.

- Jason Vallery stated that even at coarse-grained volume-level granularity, VAST Data still shards data across the cluster-wide physical capacity pool, with logical isolation above it rather than physical disk mapping per volume.

- Google described a regulatory compliance scenario requiring the ability to map a dataset or volume to a specific set of disks so that media associated with that dataset could be confiscated by regulators; Google noted the fallback is using disjoint clusters per dataset/tenant but that is suboptimal.

- Jason Vallery stated VAST Data does not currently prioritize synchronous replication with zero RTO and zero RPO across zones because it imposes latency and performance penalties; VAST can deliver low RTO/RPO (on the order of ~10 seconds) across multiple zones today and has considered zero RTO/RPO on the roadmap.

- A Google participant stated there are workload use cases requiring synchronous replication and zero RPO for files, and they believed VAST's element-level replication architecture might already support it or would soon.

- Jason Vallery stated VAST currently supports snapshot-based approaches and synchronous replication for cluster-to-cluster block-level replication, and referenced a potential three-zone, policy-driven replication approach for files (details not fully captured due to transcript truncation).

---

- Lior Genzel stated he was born during Hanukkah and that his name "Lior" means "my light".

- Jason Vallery introduced himself as VP of Cloud Product Management at VAST Data.

- Google RFP participants included David Pollack (Partnerships Lead), Seiza Gersman and Gopal (procurement team overseeing the bid through completion), Kamal and Malikarjan (product management), and Jeff (storage engineering).

- For RFP requirement B8, VAST Data explained that due to data reduction, encryption, and erasure coding, data blocks are distributed across the cluster and cannot be isolated to a specific share, volume, or set of physical disks; logical multi-tenancy and key management provide separation above the physical pool.

- Google explained the driver for RFP requirement B8 was a regulatory compliance scenario where a regulator may require confiscation of all physical media associated with a particular dataset/volume, which requires mapping the dataset to specific disks; a fallback is using separate clusters per dataset/tenant, but that is operationally suboptimal.

- For RFP requirement B16, VAST Data stated it does not currently provide synchronous replication with zero RTO and zero RPO across zones because of latency and performance penalties; VAST can deliver low (non-zero) RTO/RPO on the order of ~10 seconds across multiple zones today and has considered zero RTO/RPO but it is not currently prioritized.

- A Google storage engineering participant (Jeff, last name not provided) expected the B8 isolation limitation based on VAST's architecture and indicated it would need to be addressed as a 'call isolation' concern for the solution.

- Google stated there are workload use cases requiring synchronous replication and zero RPO for files, and they believed prior discussions with VAST suggested element-level replication might already provide this or would be delivered soon.

- VAST Data clarified that current replication is snapshot-based today, and referenced cluster-to-cluster synchronous block-level replication, while file-level multi-zone policy-driven replication was discussed as a separate capability area (details truncated in transcript).
