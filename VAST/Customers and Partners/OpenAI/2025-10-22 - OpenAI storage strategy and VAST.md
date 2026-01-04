---
type: "customer"
title: "OpenAI storage strategy and VAST"
date: "2025-10-22"
account: "OpenAI"
participants: ["Sam Hopewell", "Myself"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-22/2025-10-22 - Sam Hopewell meeting notes.md"
tags:
  - "type/customer"
  - "account/openai"
  - "generated"
---

# OpenAI storage strategy and VAST

**Date**: 2025-10-22
**Account**: [[OpenAI]]
**Attendees**: Sam Hopewell, Myself

## Summary

Sam Hopewell outlined OpenAI’s storage tiering model (Azure Blob as cold, VAST as warm near GPUs, and on-GPU/local as hot) and the purpose of the VAST POC: improve research cluster usability by staging checkpoints/training sets locally to reduce dependence on WAN/Azure variability. The POC is currently on hold due to bandwidth firefighting and internal backlog, while OpenAI remains skeptical of third-party global namespaces and prefers per-cluster islands with local object endpoints and minimal/no GPU-host agents.
## Key Information
- Stakeholder map: Sam Hopewell (primary storage owner for research); Rory Carmichael (research infra/supercomputers, Sam’s boss); Uday (above Sam & Rory, reports to Greg Brockman); DAQ/Louis (Applied data acquisition); Melissa Du (logistics for “neo clouds”/CoreWeave under Kevin Park).
- POC goal: use VAST as “warm storage” adjacent to GPU fleets to isolate training from Azure/network vagaries and make more clusters research-worthy despite poor/transient WAN.
- Tiering vocabulary: Azure Blob = cold; VAST = warm; on-GPU/local = hot/ultra.
- Status: POC on hold; a CoreWeave cluster is waiting for go-aheads; timing depends on clearing near-term fires and internal decision backlog; Sam is short staffed and hiring.
- OpenAI posture: building their own global state on top of a converged layer + multiple cloud object stores; skeptical of third-party global namespaces due to reliability, metadata performance, blast radius, and multi-EiB metadata scalability concerns.
- Near-term win path: per-cluster islands + object API; avoid touching GPU host software stack unless net throughput gains are proven; any namespace/client component should run on VAST servers and present a local object (S3/Blob) endpoint; no heavy agents on GPU nodes.
- Evaluation criteria: near-GPU throughput, list/TPS at scale, resilience to WAN slowness/disconnect, and zero/near-zero GPU-host overhead; desired fast feature turnarounds aligned to gaps (e.g., Blob-compatible endpoint/PutBlobFromURL, KV cache/IOPS density, resource governance/quota).

---

*Source: [[Inbox/_archive/2025-10-22/2025-10-22 - Sam Hopewell meeting notes.md|2025-10-22 - Sam Hopewell meeting notes]]*

## Related

- [[Microsoft]]
- [[CoreWeave]]
- [[Sam Hopewell]]
- [[Rory Carmichael]]
- [[Greg Brockman]]
- [[Melissa Du]]
- [[Kevin Park]]
- [[OpenAI VAST POC (CoreWeave cluster)]]
- [[Neo]]
