---
type: "people"
title: "1:1 with Sam Hopewell (OpenAI) on VAST GPU-adjacent warm storage, NDA boundaries, and pending CoreWeave POC"
date: "2025-10-22"
person: ""
participants: ["Jason Vallery", "Sam Hopewell"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Sam Hopewell (OpenAI) on VAST GPU-adjacent warm storage, NDA boundaries, and pending CoreWeave POC

**Date**: 2025-10-22
**With**: Jason Vallery, Sam Hopewell

## Summary

Jason Vallery reconnected with Sam Hopewell (OpenAI) to position VAST as GPU-adjacent warm storage and discuss NDA boundaries, global namespace and caching, and a pending CoreWeave-based POC. Sam described OpenAI bandwidth constraints due to firefighting and a goal to use local storage to isolate GPU fleets from network and Azure variability, with a possible in-person sync in San Francisco on 2025-11-04 to 2025-11-06.


## Action Items


- [?] Coordinate a possible in-person meeting in San Francisco on 2025-11-04 to 2025-11-06 with Sam Hopewell (OpenAI), including bringing a VAST founder and architect. @Myself 📅 2025-11-04 #task #proposed #auto

- [?] Send Sam Hopewell a concise VAST POC plan for OpenAI, including required features to evaluate (for example Blob-compatible API, caching, and global namespace capabilities). @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Confirm OpenAI internal bandwidth and provide a target window to start the VAST POC on the CoreWeave cluster. @Sam Hopewell 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Loop in OpenAI DAC and/or Applied teams to test the CoreWeave POC cluster once it is available. @Sam Hopewell 📅 2025-10-27 #task #proposed #auto

- [?] Clarify NDA boundaries for what prior OpenAI workload and architecture knowledge Jason Vallery can leverage when engaging from VAST Data. @Sam Hopewell 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Evaluate viability and reliability of VAST global namespace and metadata scaling for multi-exabyte namespaces under OpenAI-like metadata and IO patterns. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Assess whether a Blob-compatible API over VAST is required or preferred for OpenAI GPU-node integration and access patterns. @Sam Hopewell 📅 2025-10-27 #task #proposed #auto

- [?] Prepare POC environment details and staging requirements for OpenAI POC kickoff on the CoreWeave cluster. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto






## Key Information


- Jason Vallery leads VAST Data strategy and direction for hyperscalers and cloud platforms, including how VAST supports AI workloads like OpenAI.

- OpenAI's storage tiering mental model described by Sam Hopewell is Azure cold storage, VAST warm storage, and on-GPU hot local storage.

- OpenAI wants GPU-adjacent storage to isolate GPU fleets from network variability and Azure slowness, enabling fast staging of training data and checkpoints near large GPU counts.

- Sam Hopewell indicated OpenAI is exploring building its own global namespace and expects to manage its own global state due to a converged layer with multiple clusters and cloud object stores on top.

- Jason Vallery stated VAST CEO Renan gave a directive to do whatever it takes to close OpenAI gaps, including rapidly implementing requested platform features if needed.

- Sam Hopewell said OpenAI stores exabytes of data and expects to continue storing at least as much data going forward, with high expectations for list operations, throughput, and performance.



---

*Source: [[2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm]]*