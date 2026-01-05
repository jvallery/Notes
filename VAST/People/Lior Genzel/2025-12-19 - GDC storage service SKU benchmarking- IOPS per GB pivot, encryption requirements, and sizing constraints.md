---
type: "customer"
title: "GDC storage service SKU benchmarking: IOPS per GB pivot, encryption requirements, and sizing constraints"
date: "2025-12-19"
account: ""
participants: ["Jason Vallery", "Lior Genzel", "Kamal (Unknown last name)", "David (Unknown last name)", "Malikar (Unknown last name)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-19 09:50 - New Recording.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# GDC storage service SKU benchmarking: IOPS per GB pivot, encryption requirements, and sizing constraints

**Date**: 2025-12-19
**Account**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Kamal (Unknown last name), David (Unknown last name), Malikar (Unknown last name)

## Summary

Discussion focused on how to benchmark and price storage configurations for Google Distributed Cloud (GDC) using IOPS per GB as the primary SKU dimension, with a 2 ms latency target and 4K I/O baseline. VAST clarified it does not support self-encrypting drives due to dual-controller architecture constraints, but meets FIPS requirements via dual software-layer encryption plus encryption-in-transit (IPsec for file and block, TLS for S3).


## Action Items


- [?] Update the benchmarking/pricing worksheet to explicitly note that self-encrypting drives (SED) are not supported in the VAST environment and that encryption at rest is provided via dual software-layer encryption. @TBD ⏫ #task #proposed #auto

- [?] Provide details of VAST Data encryption types used in the proposed configurations, including encryption in transit (IPsec for file and block, TLS for S3) and encryption at rest implementation, so the customer can validate security requirements and understand performance impact. @Myself ⏫ #task #proposed #auto

- [?] Share small, medium, large, and extra-large configuration options mapped to the requested capacity and IOPS per GB targets, and add extra lines where the nearest purchasable hardware unit is larger than the requested capacity (for example, if 112 TiB requires buying a 150 TiB or 223 TiB building block). @Myself ⏫ #task #proposed #auto

- [?] For each proposed configuration, provide estimated total IOPS, read throughput, write throughput, and price per GB at the target IOPS per GB levels (for example, 2 IOPS/GB, 5 IOPS/GB, 10 IOPS/GB) to enable vendor comparison. @Myself ⏫ #task #proposed #auto

- [?] Confirm whether deduplication and compression should be disabled for the benchmark runs (as suggested due to encrypted-at-source data reducing effectiveness) and document the rationale in the benchmark assumptions. @TBD #task #proposed #auto




## Decisions


- Use IOPS per GB as the primary pivot for comparing vendors and defining GDC storage service SKUs, with throughput and price per GB captured as secondary comparison dimensions.

- Document that self-encrypting drives are not supported in the VAST environment and that FIPS requirements are met via dual software-layer encryption plus encryption-in-transit.




## Key Information


- Benchmarking assumptions discussed: 80/20 read/write ratio, uniform random reads, 4K I/O size for IOPS benchmarking, and a latency target under 2 milliseconds.

- Protocols expected for benchmarking include NVMe/TCP for block, NFSv4 for file, and S3 for object.

- VAST Data does not currently support self-encrypting drives (SED) because supporting SEDs is challenging with VAST's dual-controller high availability design where two controllers manage the same drives.

- VAST Data stated it meets FIPS requirements using dual software-layer encryption (encryption at rest) rather than drive-level self-encrypting drives.

- Encryption in transit requirements for the benchmark: IPsec for file and block traffic, and TLS for S3 traffic, and these should be enabled during performance testing because they can reduce IOPS.

- GDC storage service SKUs and pricing are primarily based on IOPS per GB, with throughput optimized secondarily at a given IOPS per GB level.

- Multi-tenancy is a core part of Google Distributed Cloud architecture and will be relied on by the solution stack; it is complementary to the storage SKU benchmarking exercise.

- VAST Data indicated it may not have lab environments matching every requested hardware scenario and would provide scaling dimensions and approximations for expected performance at requested sizes.



---

*Source: [[2025-12-19 09:50 - New Recording]]*