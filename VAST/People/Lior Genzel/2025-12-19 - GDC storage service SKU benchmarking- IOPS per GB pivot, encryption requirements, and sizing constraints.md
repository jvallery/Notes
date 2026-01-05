---
type: people
title: 'GDC storage service SKU benchmarking: IOPS per GB pivot, encryption requirements, and sizing constraints'
date: '2025-12-19'
participants:
- Jason Vallery
- Lior Genzel
- Kamal (Unknown last name)
- David (Unknown last name)
- Malikar (Unknown last name)
- Kamal (last name unknown)
- Malikar (last name unknown)
- David (last name unknown)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-19 09:50 - New Recording.md
tags:
- type/people
- generated
person: Lior Genzel
---

# GDC storage service SKU benchmarking: IOPS per GB pivot, encryption requirements, and sizing constraints

**Date**: 2025-12-19
**Attendees**: Jason Vallery, Lior Genzel, Kamal (Unknown last name), David (Unknown last name), Malikar (Unknown last name)

## Summary

The group aligned on a benchmarking framework for a cloud storage service where the primary sizing and pricing pivot is IOPS per GB, with a target latency under 2 ms using 4K I/O and an 80/20 read/write mix with uniform random reads. VAST clarified it does not support self-encrypting drives due to HA controller architecture constraints, but meets FIPS requirements via dual software-layer encryption plus encryption-in-transit (IPsec for file and block, TLS for S3). The team discussed mapping requested small/medium/large configurations to VAST's available hardware building blocks, including adding extra lines when the requested capacity does not match VAST's minimum shippable configuration.

## Action Items

- [?] Update the benchmarking/pricing worksheet to explicitly note that self-encrypting drives (SED) are not supported in the VAST environment and that encryption at rest is provided via dual software-layer encryption. @TBD ⏫ #task #proposed #auto

- [?] Provide details of VAST Data encryption types used in the proposed configurations, including encryption in transit (IPsec for file and block, TLS for S3) and encryption at rest implementation, so the customer can validate security requirements and understand performance impact. @Myself ⏫ #task #proposed #auto

- [?] Share small, medium, large, and extra-large configuration options mapped to the requested capacity and IOPS per GB targets, and add extra lines where the nearest purchasable hardware unit is larger than the requested capacity (for example, if 112 TiB requires buying a 150 TiB or 223 TiB building block). @Myself ⏫ #task #proposed #auto

- [?] For each proposed configuration, provide estimated total IOPS, read throughput, write throughput, and price per GB at the target IOPS per GB levels (for example, 2 IOPS/GB, 5 IOPS/GB, 10 IOPS/GB) to enable vendor comparison. @Myself ⏫ #task #proposed #auto

- [?] Confirm whether deduplication and compression should be disabled for the benchmark runs (as suggested due to encrypted-at-source data reducing effectiveness) and document the rationale in the benchmark assumptions. @TBD #task #proposed #auto

- [?] Update the benchmarking/configuration worksheet to explicitly note that VAST Data does not support self-encrypting drives (SED) and that encryption-at-rest is provided via dual software-layer encryption outside the drive. @Myself ⏫ #task #proposed #auto

- [?] Add explicit details of VAST Data encryption types to the configuration documentation, including encryption-in-transit (IPsec for file and block, TLS for S3) and the two software encryption layers used for encryption-at-rest to meet FIPS requirements. @Myself ⏫ #task #proposed #auto

- [?] Provide Google Distributed Cloud team with VAST Data small/medium/large/extra-large configuration mappings, including additional lines where requested capacities (for example 112 TiB) require purchasing a larger minimum hardware configuration (for example 150 TiB or 223 TiB), and include expected total IOPS and throughput for each mapping. @Myself ⏫ #task #proposed #auto

- [?] Share VAST Data 'building block' scaling dimensions (per-controller and per-drive performance characteristics) to help Google Distributed Cloud approximate performance for configurations that cannot be replicated exactly in lab environments. @Myself #task #proposed #auto

## Decisions

- Use IOPS per GB as the primary pivot for comparing vendors and defining GDC storage service SKUs, with throughput and price per GB captured as secondary comparison dimensions.

- Document that self-encrypting drives are not supported in the VAST environment and that FIPS requirements are met via dual software-layer encryption plus encryption-in-transit.

- Use a benchmark baseline of 4K I/O with an 80/20 read/write mix, uniform random reads, and require reported latency under 2 milliseconds for performance comparisons.

- Run benchmarking with encryption-in-transit enabled (IPsec for file and block, TLS for S3) to reflect real-world overhead in IOPS and throughput results.

- Treat self-encrypting drives as not supported in the VAST environment and document that encryption-at-rest is achieved via dual software-layer encryption instead.

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

- The benchmarking workload assumptions are 80/20 read/write ratio with uniform random reads, using 4K I/O for IOPS benchmarking, and a target latency under 2 milliseconds.

- VAST Data does not implement or support self-encrypting drive (SED) support because it is problematic with VAST's high-availability dual-controller architecture where both controllers manage the same drives.

- VAST Data meets FIPS requirements using dual software-layer encryption outside the drive rather than drive-level self-encrypting drives.

- Encryption in transit requirements for the benchmark are enabled: IPsec for file and block protocols, and TLS for S3 object protocol.

- The benchmark compares vendors primarily on IOPS per GB (IOPS/GB) and then evaluates read throughput per GB, write throughput per GB, and price per GB for each configuration.

- Google Distributed Cloud storage service SKUs and pricing are based on IOPS per GB as the primary pivot, and throughput is optimized secondarily at a given IOPS/GB tier.

- Multi-tenancy is a core part of Google Distributed Cloud architecture and will be relied on by the solution stack, and it is complementary to the storage benchmarking exercise.

- VAST Data can size throughput and performance independently from capacity in customer workload conversations, but for this exercise the request is to map fixed capacity plus IOPS/GB targets to concrete configurations and pricing.
