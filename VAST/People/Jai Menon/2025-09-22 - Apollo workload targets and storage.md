---
type: people
title: Apollo workload targets and storage
date: '2025-09-22'
person: Jai Menon
participants:
- Jason Vallery
- Jai Menon
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-22 - Jason and Jai discussed Apollo’s
  target workloads and deployment model (scale pe.md
tags:
- type/customer
- account/jai-menon
- generated
---

# Apollo workload targets and storage

**Date**: 2025-09-22
**Account**: [[Jai Menon]]
**Attendees**: Jason Vallery, Jai Menon

## Summary

Jason Vallery and Jai Menon discussed Apollo’s target workload assumptions and deployment model, including per-site GPU scale (4K vs 8K), geo-disaggregation driven by energy-centric placements, and implications for storage sizing and throughput. They also reviewed the need for a persistent, strongly consistent cross-site key-value store and shared namespace (blobs + KV), and flagged risk around a high-TPS Databricks storage workload potentially moving off Azure.
## Action Items
- [ ] Probe with Pete about the status of the high-TPS Databricks/Chat-related workload and capacity implications. @Myself 📅 2025-10-26 🔺 #task #proposed
- [ ] Review and incorporate/resolve Jason’s comments on the Apollo documents. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ] Define Apollo workload targets: GPU cluster size per site (e.g., 4K vs 8K), storage throughput per GPU, and degree of geo disaggregation. @TBD 📅 2025-10-26 🔺 #task #proposed
- [ ] Deepen research on Vast/CoreWeave’s persistent KV and data pipeline approach and assess applicability to Apollo’s shared namespace/consistency needs. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Provide Jason with specific next research topics and sources to investigate. @Jai Menon 📅 2025-10-26 ⏫ #task #proposed
- [ ] Confirm whether the new ‘Matt UK’ supercomputer deal aligns with Apollo or Fairwater. @Jai Menon 📅 2025-10-26 🔽 #task #proposed
- [ ] Clarify details on the DFW enrichment sites (approx. 160,000 GB200s under one roof) and implications for Apollo design. @Jai Menon 📅 2025-10-26 🔽 #task #proposed

## Key Information
- Apollo needs clarity on target GPU cluster sizes per site (4K vs 8K) and how disaggregated deployments should be across geographies due to energy-centric placements.
- Prior 8K-GPU design assumed ~100 PB storage (throughput-driven), ~120-rack cluster, and ~2.5 TB/s throughput; storage may be closer to ~120 PB in practice.
- OpenAI historically over-provisioned checkpoint storage and periodically cleaned up; petabytes were not the primary constraint.
- Shift toward online reinforcement learning implies training and inference sharing GPUs, changing storage and consistency requirements.
- Vast/CoreWeave are pursuing persistent, strongly consistent KV storage across disaggregated GPUs using Kafka-style change logs and a shared namespace concept.
- Apollo may require a shared namespace spanning blobs and a strongly consistent KV store across sites.
- A potential new ‘Matt UK’ supercomputer deal may relate to Satya’s UK investment announcement; unclear if it maps to Apollo or Fairwater.
- DFW enrichment sites were referenced as ~160,000 GB200s under one roof, similar in scale to Fairwater.
- Large InfiniBand-connected data centers are still needed for foundation model pre-training; fine-tuning/RL can run at smaller scale without InfiniBand.
- Risk flagged: losing a high-TPS Databricks storage workload could move the system of record off Azure and impact competitive positioning.

---

*Source: [[Inbox/_archive/2025-09-22/2025-09-22 - Jason and Jai discussed Apollo’s target workloads and deployment model (scale pe.md|2025-09-22 - Jason and Jai discussed Apollo’s target workloads and deployment model (scale pe]]*

## Related

- [[Jason Vallery]]
- [[Jack Kabat]]
- [[Fairwater]]
- [[CoreWeave]]
- [[Databricks]]
- [[Microsoft]]
- [[Oracle]]
- [[Google]]
- [[Amazon]]
- [[OpenAI]]
- [[NVIDIA]]
- [[xAI]]