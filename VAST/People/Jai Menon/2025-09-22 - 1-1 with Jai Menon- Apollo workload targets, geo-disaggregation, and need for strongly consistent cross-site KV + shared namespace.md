---
type: "people"
title: "1:1 with Jai Menon: Apollo workload targets, geo-disaggregation, and need for strongly consistent cross-site KV + shared namespace"
date: "2025-09-22"
person: ""
participants: ["Jason Vallery", "Jai Menon", "Jack Kabat", "Mark (unknown)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-22 - Jason and Jai discussed Apollo’s target workloads and deployment model (scale pe.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jai Menon: Apollo workload targets, geo-disaggregation, and need for strongly consistent cross-site KV + shared namespace

**Date**: 2025-09-22
**With**: Jason Vallery, Jai Menon, Jack Kabat, Mark (unknown)

## Summary

Jason Vallery and Jai Menon discussed Apollo’s target workloads and deployment model, focusing on per-site GPU scale (4K vs 8K GPUs), geo-disaggregation driven by energy-centric placements, and storage sizing driven by throughput rather than raw PB. Jason argued Apollo likely needs a persistent, strongly consistent key-value store and a shared namespace spanning blobs and KV across sites, similar to what VAST Data and CoreWeave appear to be building with Kafka-style change logs.


## Action Items


- [?] Probe with Pete about the status of the high-TPS Databricks/Chat-related storage workload and any capacity or competitive implications for Microsoft Azure and Apollo. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Review and incorporate or resolve Jason Vallery’s comments on the Apollo documents. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Define Apollo workload targets, including per-site GPU cluster size (for example 4,000 vs 8,000 GPUs), required throughput per GPU, and the intended degree of geo-disaggregation across sites. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Deepen research on VAST Data and CoreWeave’s persistent key-value store and data pipeline approach (including Kafka-style change logs and shared namespace concepts) and assess applicability to Apollo’s cross-site shared namespace and strong consistency needs. @Myself 📅 2025-10-26 #task #proposed #auto

- [?] Provide Jason Vallery with specific next research topics and sources to investigate for Apollo architecture and workload requirements. @Jai Menon 📅 2025-10-26 #task #proposed #auto

- [?] Confirm whether the rumored 'Matt UK' supercomputer deal aligns with the Apollo program or the Fairwater program. @Jai Menon 📅 2025-10-26 🔽 #task #proposed #auto






## Key Information


- Apollo architecture discussions need clarity on target per-site GPU cluster size, specifically whether Apollo sites are designed for approximately 4,000 GPUs or 8,000 GPUs per site, and how that maps to data center footprints.

- A prior Apollo sizing model for an approximately 8,000-GPU site assumed about 100 PB of storage, but the sizing driver was throughput per GPU rather than checkpoint capacity, and the implied storage was closer to approximately 120 PB in practice.

- The prior throughput proxy used in Apollo sizing was a roughly 120-rack storage cluster delivering approximately 2.5 TB/s aggregate throughput.

- OpenAI historically over-provisioned checkpoint storage and periodically performed large cleanup efforts because petabytes of checkpoint capacity were not the primary constraint.

- Energy-centric deployments, influenced by public partnerships with CoreWeave and Nebbius, imply Apollo may need to support disaggregated, multi-geo footprints where a single customer spans diverse locations with varying scale.

- A shift toward online reinforcement learning, where inference and training can share the same GPUs, changes storage and consistency requirements compared to traditional large-scale pre-training.

- Jason Vallery believes VAST Data and CoreWeave are pursuing a persistent, strongly consistent key-value store across disaggregated GPUs, using Kafka-style streaming change logs and a shared namespace to propagate updates across sites.

- Jason Vallery believes Apollo may require a shared namespace spanning both blob/object data and a persistent key-value store, with strong consistency across multiple sites to support multi-geo deployments.

- Jason Vallery spoke with Jack Kabat, who mentioned another 'Matt UK' supercomputer deal that might relate to either Apollo or Fairwater and could be connected to Satya Nadella’s UK investment announcement.



---

*Source: [[2025-09-22 - Jason and Jai discussed Apollo’s target workloads and deployment model (scale pe]]*