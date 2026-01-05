---
type: "customer"
title: "OpenAI storage strategy: VAST as near-GPU warm storage and POC posture (Sam Hopewell)"
date: "2025-10-22"
account: ""
participants: ["Sam Hopewell", "Jason Vallery"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-22 - Sam Hopewell meeting notes.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# OpenAI storage strategy: VAST as near-GPU warm storage and POC posture (Sam Hopewell)

**Date**: 2025-10-22
**Account**: [[]]
**Attendees**: Sam Hopewell, Jason Vallery

## Summary

Sam Hopewell described OpenAI's desired storage tiering model where Azure Blob is cold, VAST is warm near GPU fleets, and on-GPU/local storage is hot. The near-term win is per-cluster storage islands with a local object endpoint running on VAST servers, proving throughput, metadata/list performance at scale, WAN-disconnect resilience, and near-zero GPU-host overhead, while OpenAI remains skeptical of third-party global namespaces at multi-EiB scale.


## Action Items


- [?] Define a VAST-for-OpenAI POC proposal centered on per-cluster islands with a VAST-hosted local object endpoint (S3 and/or Azure Blob compatible) and explicitly no heavy GPU-node agents unless measurable throughput gains are demonstrated. @Myself ⏫ #task #proposed #auto

- [?] Prepare an evidence plan for OpenAI covering near-GPU throughput, list/TPS at scale, resilience to WAN slowness or disconnect, and measurement of GPU-host overhead (targeting zero or near-zero). @Myself ⏫ #task #proposed #auto

- [?] Assess feasibility and ownership for fast-turn feature asks relevant to OpenAI: Azure Blob-compatible PutBlobFromURL, KV cache or IOPS density improvements, resource governance, and quota controls, then align internal teams on what can be delivered and how it will be validated. @Myself #task #proposed #auto

- [?] Confirm OpenAI stakeholder map details and roles (Rory Carmichael, Uday, Louis/DAQ, Melissa Du, Kevin Park) and identify the decision-maker and approver for the CoreWeave cluster go-ahead. @Myself #task #proposed #auto




## Decisions


- Position the near-term OpenAI approach as per-cluster storage islands with a local object endpoint running on VAST servers, avoiding heavy GPU-host agents unless throughput gains are proven.




## Key Information


- Sam Hopewell is the primary storage owner for OpenAI research.

- Rory Carmichael owns OpenAI research infrastructure and supercomputers and is Sam Hopewell's manager.

- An OpenAI leader named Uday sits above Sam Hopewell and Rory Carmichael and reports to Greg Brockman.

- An OpenAI stakeholder referred to as DAQ/Louis is associated with applied data acquisition at OpenAI.

- Melissa Du handles logistics for OpenAI "neo clouds" including CoreWeave, under Kevin Park (finance/capacity).

- OpenAI's stated POC purpose is to use VAST as warm storage adjacent to GPU fleets to isolate training from Azure and network variability and unlock more GPU clusters for research that currently lack reliable bandwidth.

- OpenAI's desired outcome is to make newly delivered GPU-only inferencing clusters research-worthy despite poor or transient WAN by staging checkpoints and training datasets locally and serving some reads directly from VAST when GPU caching is not required.

- OpenAI's tiering vocabulary (per Sam Hopewell) is Azure Blob as cold, VAST as warm near large numbers of GPUs for high-throughput staging of large working sets, and on-GPU/local storage as hot or ultra-hot.

- The OpenAI VAST POC is on hold due to bandwidth firefighting and internal decision backlog; a CoreWeave cluster is waiting for internal go-aheads to begin evaluation.

- OpenAI is under internal pressure to complete the warm-storage work because it increases fungibility of their GPU fleet and provides additional capacity to research projects; Sam Hopewell is short staffed and actively hiring.

- OpenAI is building its own global state on top of a converged layer plus multiple cloud object stores and is skeptical of third-party global namespaces due to concerns about reliability, single blast radius, and metadata scalability at multi-exbibyte scale.

- OpenAI's near-term preference is per-cluster storage islands with an object API; any namespace or client component should run on VAST servers and present a local object endpoint (S3 or Azure Blob compatible), avoiding heavy agents on GPU nodes unless net throughput gains are proven.

- OpenAI's evaluation criteria for VAST include near-GPU throughput, list and transactions-per-second performance at scale, resilience to WAN slowness or disconnect, and zero or near-zero GPU-host overhead; they also value fast feature turnarounds aligned to gaps like Blob-compatible PutBlobFromURL, KV cache or IOPS density, resource governance, and quota.



---

*Source: [[2025-10-22 - Sam Hopewell meeting notes]]*