---
type: customer
title: Google
last_contact: unknown
created: '2026-01-03'
tags:
- type/customer
- generated
---

# Google

## Recent Context

- unknown: [[Untitled]] - Forwardable write-up/email draft instructing an internal Performance team to populate Google’s “VAST...
- unknown: [[2025-10 - Google Tasks]] - Task to confirm Google Cloud Platform (GCP) general availability timing after a bottleneck fix and a...
- unknown: [[2025-10 - Lior Genzel]] - Note covers coordination on Google TPU strategy outside GCP, pricing/private offer topics, and sales... (via Lior Genzel)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]]
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal team sync to align on Walmart’s big data initiative, focusing on clarifying disaster recove... (via Walmart)
- 2025-11-13: [[2025-11-13 - GDC RFP meeting]] - Notes from a Google GDC RFP meeting covering storage TCO (HDD vs QLC), security/compliance (SED, air...
- 2025-11-05: [[2025-11-05 - Walmart Analytics]] - Note captures Walmart’s hybrid analytics storage/replication requirements for moving a hot working s... (via Walmart)
- 2025-11-03: [[2025-11-03]] - Brief note capturing topics to clarify around a Microsoft hardware SKU, a proof of concept with MAI,... (via Lior Genzel)
- 2025-10-31: [[2025-10-31 - GCP outlined the path to run VAST on storage-serving VMs (Z4M) with higher stora]]
- 2025-10-30: [[2025-10-30 - Intro 1-1 between Jason and Dre. Dre outlined SE enablement cadence and an S3Ob]] - Intro 1:1 between Jason Vallery and Deandre (Dre) Jackson focused on aligning cloud enablement messa... (via Deandre Jackson)
- 2025-10-29: [[2025-10-29 - Intro 1-1 to understand Customer Success operations for CoreWeave and XAI and im]] - Intro 1:1 with Rick Haselton to understand how Customer Success operates for the CoreWeave and XAI a... (via Rick Haselton)
- 2025-10-28: [[2025-10-28 - The teams discussed IP management and failover approaches on GCP (alias IPs, rou]]
- 2025-10-28: [[2025-10-28 - Team aligned on MVP launch on GCP via private offers with fixed capacity pricing]]
- 2025-10-20: [[2025-10-20 - Discussed cloud architectures for VAST on AWSGCPAzure, the need for object-sto]] - Weekly 1:1 with Yogev Vankin focused on VAST multi-cloud architecture across AWS/GCP/Azure, centerin... (via Yogev Vankin)
- 2025-09-15: [[2025-09-15 - Silk briefed Jason on its cloud storage architecture optimized for databases and]] - Weekly 1:1 where Silk briefed Jason on its software-defined cloud storage architecture optimized for... (via Silk)

## Key Facts

- Federal connection needed for a mutual customer, involving SE and operations considerations.
- Separation of duties and potential two-sign/two-person rule is a key security/compliance concern.
- Multi-tenancy requirements include QoS/quotas, tags, and policy-based management.
- Security topics include network security, air-gapped security details, certifications, and remote patching.
- Operational concerns include how to manage, troubleshoot, and patch systems.
- Hardware recommendation shapes discussed with Dell as a partner.
- Google will compare vendors primarily on IOPS per GiB and price per GiB; throughput is secondary.
- IOPS results must be reported only where mean latency is under 2 ms (apples-to-apples constraint).
- Benchmarks must have encryption enabled: IPsec for file+block, TLS for S3; encryption at rest must also be enabled with an additional tenant-granularity (or finer) layer.
- Dedupe and compression must be disabled for performance tests and random data used to avoid inflated results.

## Topics

HDD vs QLC TCO, SED (self-encrypting drives), Hardware partners, Availability zones (AZs), SyncEngine, GCS API compatibility/questions, Federal connection for mutual customer, Separation of duties / two-sign rule, Multi-tenancy, QoS and quotas, Tags and policy-based management, Network security, Tenant/tag model for workloads, Air-gapped security, certifications, Remote patching

## Related

<!-- Wikilinks to related entities -->
