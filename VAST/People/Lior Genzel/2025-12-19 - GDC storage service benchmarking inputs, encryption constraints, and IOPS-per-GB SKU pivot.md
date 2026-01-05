---
type: "projects"
title: "GDC storage service benchmarking inputs, encryption constraints, and IOPS-per-GB SKU pivot"
date: "2025-12-19"
project: ""
participants: ["Jason Vallery", "Lior Genzel", "Kamal (last name unknown)", "Malikar (last name unknown)", "David (last name unknown)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-19 09:50 - New Recording.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# GDC storage service benchmarking inputs, encryption constraints, and IOPS-per-GB SKU pivot

**Date**: 2025-12-19
**Project**: [[]]
**Attendees**: Jason Vallery, Lior Genzel, Kamal (last name unknown), Malikar (last name unknown), David (last name unknown)

## Summary

The group aligned on a benchmarking framework for a cloud storage service where the primary sizing and pricing pivot is IOPS per GB, with a target latency under 2 ms using 4K I/O and an 80/20 read/write mix with uniform random reads. VAST clarified it does not support self-encrypting drives due to HA controller architecture constraints, but meets FIPS requirements via dual software-layer encryption plus encryption-in-transit (IPsec for file and block, TLS for S3). The team discussed mapping requested small/medium/large configurations to VAST's available hardware building blocks, including adding extra lines when the requested capacity does not match VAST's minimum shippable configuration.


## Action Items


- [?] Update the benchmarking/configuration worksheet to explicitly note that VAST Data does not support self-encrypting drives (SED) and that encryption-at-rest is provided via dual software-layer encryption outside the drive. @Myself ⏫ #task #proposed #auto

- [?] Add explicit details of VAST Data encryption types to the configuration documentation, including encryption-in-transit (IPsec for file and block, TLS for S3) and the two software encryption layers used for encryption-at-rest to meet FIPS requirements. @Myself ⏫ #task #proposed #auto

- [?] Provide Google Distributed Cloud team with VAST Data small/medium/large/extra-large configuration mappings, including additional lines where requested capacities (for example 112 TiB) require purchasing a larger minimum hardware configuration (for example 150 TiB or 223 TiB), and include expected total IOPS and throughput for each mapping. @Myself ⏫ #task #proposed #auto

- [?] Share VAST Data 'building block' scaling dimensions (per-controller and per-drive performance characteristics) to help Google Distributed Cloud approximate performance for configurations that cannot be replicated exactly in lab environments. @Myself #task #proposed #auto




## Decisions


- Use a benchmark baseline of 4K I/O with an 80/20 read/write mix, uniform random reads, and require reported latency under 2 milliseconds for performance comparisons.

- Run benchmarking with encryption-in-transit enabled (IPsec for file and block, TLS for S3) to reflect real-world overhead in IOPS and throughput results.

- Treat self-encrypting drives as not supported in the VAST environment and document that encryption-at-rest is achieved via dual software-layer encryption instead.




## Key Information


- The benchmarking workload assumptions are 80/20 read/write ratio with uniform random reads, using 4K I/O for IOPS benchmarking, and a target latency under 2 milliseconds.

- VAST Data does not implement or support self-encrypting drive (SED) support because it is problematic with VAST's high-availability dual-controller architecture where both controllers manage the same drives.

- VAST Data meets FIPS requirements using dual software-layer encryption outside the drive rather than drive-level self-encrypting drives.

- Encryption in transit requirements for the benchmark are enabled: IPsec for file and block protocols, and TLS for S3 object protocol.

- The benchmark compares vendors primarily on IOPS per GB (IOPS/GB) and then evaluates read throughput per GB, write throughput per GB, and price per GB for each configuration.

- Google Distributed Cloud storage service SKUs and pricing are based on IOPS per GB as the primary pivot, and throughput is optimized secondarily at a given IOPS/GB tier.

- Multi-tenancy is a core part of Google Distributed Cloud architecture and will be relied on by the solution stack, and it is complementary to the storage benchmarking exercise.

- VAST Data can size throughput and performance independently from capacity in customer workload conversations, but for this exercise the request is to map fixed capacity plus IOPS/GB targets to concrete configurations and pricing.



---

*Source: [[2025-12-19 09:50 - New Recording]]*