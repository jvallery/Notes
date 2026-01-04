---
type: transcript
title: Sam Hopewell - OpenAI storage strategy and VAST POC
date: "2025-10-22"
participants:
  - Sam Hopewell
  - Myself
entities:
  people:
    - "[[Sam Hopewell]]"
  customers:
    - "[[OpenAI]]"
tags:
  - type/transcript
  - entity/Sam Hopewell
  - entity/OpenAI
source_type: transcript
---

# Sam Hopewell - OpenAI storage strategy and VAST POC

**Date:** 2025-10-22 · **People:** [[Sam Hopewell]] · **Customer:** [[OpenAI]]

---

Updated stakeholder map:

- Sam Hopewell (primary storage owner for research),
- Rory Carmichael (Owns research infra/supercomputers, Sam's boss),
- Uday (above Sam & Rory, reports to Greg Brockman)
- DAQ/Louis (Applied data acquisition),
- Melissa Du (logistics for “neo clouds”/CoreWeave under Kevin Park (finance/capacity))

- POC purpose (in Sam’s words): Use VAST as “warm storage” adjacent to GPU fleets to isolate training from Azure/network vagaries and unlock more clusters for research that today lack reliable bandwidth.
-
- \*\*Desired outcome: Make more clusters research‑worthy despite poor/transient WAN in newly delivered GPU only inferencing clusters by staging checkpoints/training sets locally and serving some reads directly from VAST when GPU caching isn’t required.
-
- New Tiering vocabulary (from Sam):\*\*
  - **Azure Blob = “cold”**
  - **VAST = “warm” (near large numbers of GPUs, efficient, high‑throughput, suitable for staging/holding large working sets that don’t fit on local GPU storage).**
  - \*\*On‑GPU/local = “hot/ultra”
- Status: On hold due to firefighting/bandwidth. A CoreWeave cluster is “waiting for go‑aheads” to kick tires; timing tied to clearing near‑term fires and internal decision backlog. The team is heads down on bringing new research supercomputer capacity online and this hasn't been a focus for Sam's team. There is lots of internal pressure to get it done because it increases the fungibility of their GPU fleet and provides new capacity to research projects. Sam is short staffed, and actively hiring.
- \*\*Global namespace posture: OAI is building their own global state on top of a converged layer + multiple cloud object stores; they question both reliability and metadata performance of a third‑party global namespace. OpenAI is skeptical of global namespaces (single blast radius) and metadata scalability at multi‑EiB; Unless we can prove we can address these concerns, they likely manage global state themselves. They are open to our pitch. Short term, we can win by per‑cluster islands + object API,. Don’t touch software stack on GPU hosts unless you can prove net throughput gains. Any namespace/client component should run on VAST servers and present a local object (S3/Blob) endpoint; no heavy agents on GPU nodes.
- Where to win: Prove near‑GPU throughput, list/TPS at scale, resilience to WAN slowness/disconnect, and zero/near‑zero GPU‑host overhead. Show fast feature turnarounds aligned to their gaps (Blob‑compatible endpoint (PutBlobFromURL), KV cache/IOPS density, resource governance, quota, etc.).
