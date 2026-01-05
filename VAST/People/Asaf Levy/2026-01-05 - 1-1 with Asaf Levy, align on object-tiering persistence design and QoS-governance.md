---
type: "people"
title: "1:1 with Asaf Levy, align on object-tiering persistence design and QoS/governance"
date: "2026-01-05"
person: ""
participants: ["Jason Vallery", "Asaf Levy"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10 - Asaf Levy.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Asaf Levy, align on object-tiering persistence design and QoS/governance

**Date**: 2026-01-05
**With**: Jason Vallery, Asaf Levy

## Summary

Jason Vallery and Asaf Levy aligned on VAST object-tiering persistence design across Blob/S3/GCS, including metadata persistence options and consistency trade-offs. They also defined a QoS and governance model based on identity-driven quotas and prioritization across throughput, TPS, and capacity, and evaluated cloud storage options for metadata persistence.


## Action Items


- [?] Meet with Asaf Levy (VAST chief architect) to align on persistence design, object tiering, and QoS/governance for VAST multi-cloud object-tiering. @Myself 📅 2025-10-21 ⏫ #task #proposed #auto

- [?] Prepare a proposal for VAST object-tiering design across Azure Blob Storage, Amazon S3, and Google Cloud Storage (GCS), including metadata persistence options and consistency trade-offs. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Define the QoS and governance model for VAST object-tiering, including identity-based quotas and prioritization across throughput, TPS, and capacity. @Asaf Levy 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Benchmark the viability of using Azure Premium Blob Storage and Amazon S3 Express for metadata persistence for VAST object-tiering, and compare against block storage options. @Asaf Levy 📅 2025-11-08 #task #proposed #auto

- [?] Share current VAST DataSpaces architecture documentation and the persistence roadmap with Jason Vallery. @Asaf Levy 📅 2025-11-08 #task #proposed #auto




## Decisions


- Proceed with an object-tiering design proposal for Azure Blob Storage, Amazon S3, and Google Cloud Storage (GCS) that explicitly documents metadata persistence options and consistency trade-offs.

- Use an identity-driven QoS/governance model with quotas and prioritization across throughput, TPS, and capacity.




## Key Information


- Asaf Levy is the chief architect at VAST Data and is a key decision-maker for persistence architecture and QoS/governance design for VAST multi-cloud object-tiering.

- The object-tiering design under discussion targets cloud object stores including Azure Blob Storage, Amazon S3, and Google Cloud Storage (GCS), with explicit consideration of metadata persistence and consistency trade-offs.

- The QoS and governance model being defined uses identity-based quotas and prioritization across throughput, transactions per second (TPS), and capacity.



---

*Source: [[2025-10 - Asaf Levy]]*