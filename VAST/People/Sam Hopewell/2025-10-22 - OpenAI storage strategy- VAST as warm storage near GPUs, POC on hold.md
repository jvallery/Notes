---
type: "customer"
title: "OpenAI storage strategy: VAST as warm storage near GPUs, POC on hold"
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

# OpenAI storage strategy: VAST as warm storage near GPUs, POC on hold

**Date**: 2025-10-22
**Account**: [[]]
**Attendees**: Sam Hopewell, Jason Vallery

## Summary

Sam Hopewell described an OpenAI proof-of-concept to use VAST as "warm storage" adjacent to GPU fleets to reduce dependence on Azure and unreliable WAN bandwidth, making more GPU clusters usable for research. OpenAI is skeptical of third-party global namespaces at multi-exbibyte scale and prefers per-cluster storage islands with local object endpoints and minimal or zero software on GPU hosts. The POC is currently on hold due to bandwidth firefighting and internal decision backlog while OpenAI brings new research supercomputer capacity online.


## Action Items


- [?] Confirm OpenAI stakeholder details and full names for Rory Carmichael, Uday, Louis (DAQ), Melissa Du, and Kevin Park, and map them to roles in the OpenAI storage decision process for the VAST warm storage POC. @Myself #task #proposed #auto

- [?] Prepare a VAST POC proposal tailored to OpenAI's constraints: per-cluster island deployment, local object endpoint (S3/Blob) served from VAST servers, and no heavy agents on GPU nodes unless throughput gains are demonstrated. @Myself ⏫ #task #proposed #auto

- [?] Define and share a benchmark plan for OpenAI that measures near-GPU throughput, list performance and TPS at scale, behavior under WAN slowness or disconnect, and GPU-host overhead for the VAST warm storage design. @Myself ⏫ #task #proposed #auto

- [?] Assess feasibility and ownership for feature gaps OpenAI called out, including Blob-compatible PutBlobFromURL, KV cache or IOPS density improvements, and resource governance and quota controls, and identify what can be delivered via configuration vs product work. @Myself #task #proposed #auto




## Decisions


- OpenAI's short-term architectural posture is to pursue per-cluster storage islands with a local object API endpoint rather than adopting a third-party global namespace, unless VAST can prove reliability and metadata scalability at multi-exbibyte scale.




## Key Information


- Sam Hopewell is the primary storage owner for OpenAI research.

- Rory Carmichael owns OpenAI research infrastructure and supercomputers and is Sam Hopewell's manager.

- An OpenAI leader named Uday is above Sam Hopewell and Rory Carmichael and reports to Greg Brockman.

- OpenAI has a stakeholder named Louis (DAQ, Applied Data Acquisition) involved in applied data acquisition.

- Melissa Du handles logistics for OpenAI "neo clouds" including CoreWeave, under Kevin Park (finance and capacity).

- OpenAI's stated POC purpose is to use VAST as warm storage adjacent to GPU fleets to isolate training from Azure and network variability and unlock more clusters for research that currently lack reliable bandwidth.

- OpenAI's desired outcome is to make newly delivered GPU-only inferencing clusters research-worthy despite poor or transient WAN by staging checkpoints and training datasets locally and serving some reads directly from VAST when GPU caching is not required.

- OpenAI's tiering vocabulary: Azure Blob is "cold", VAST is "warm" near large numbers of GPUs for high-throughput staging of large working sets, and on-GPU or local storage is "hot/ultra".

- The OpenAI VAST POC is on hold due to bandwidth firefighting and internal decision backlog while the team focuses on bringing new research supercomputer capacity online; there is internal pressure to complete it because it increases GPU fleet fungibility and research capacity, and Sam Hopewell is short staffed and actively hiring.

- OpenAI is building its own global state on top of a converged layer plus multiple cloud object stores and is skeptical of third-party global namespaces due to concerns about reliability, single blast radius, and metadata scalability at multi-exbibyte scale.

- OpenAI's near-term preference is per-cluster storage islands with an object API; any namespace or client component should run on VAST servers and present a local object endpoint (S3 or Blob), with no heavy agents on GPU nodes unless net throughput gains are proven.

- OpenAI evaluation criteria for VAST include near-GPU throughput, list and transactions-per-second at scale, resilience to WAN slowness or disconnect, and zero or near-zero GPU-host overhead; they also value fast feature turnarounds for gaps like Blob-compatible PutBlobFromURL, KV cache or IOPS density, resource governance, and quota.



---

*Source: [[2025-10-22 - Sam Hopewell meeting notes]]*