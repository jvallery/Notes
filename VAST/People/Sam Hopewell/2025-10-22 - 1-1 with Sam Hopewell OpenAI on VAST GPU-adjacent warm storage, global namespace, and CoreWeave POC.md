---
type: "people"
title: "1:1 with Sam Hopewell (OpenAI) on VAST GPU-adjacent warm storage, global namespace, and CoreWeave POC"
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

# 1:1 with Sam Hopewell (OpenAI) on VAST GPU-adjacent warm storage, global namespace, and CoreWeave POC

**Date**: 2025-10-22
**With**: Jason Vallery, Sam Hopewell

## Summary

Jason Vallery reconnected with Sam Hopewell (OpenAI) to position VAST as GPU-adjacent warm storage between Azure cold storage and on-GPU hot storage, and to discuss NDA boundaries, global namespace and caching, and a pending CoreWeave POC. Sam described OpenAI bandwidth constraints due to ongoing firefighting and emphasized isolating GPU fleets from network and Azure variability, with strong resistance to extra GPU-node components unless throughput improves. They aligned on a possible in-person sync in San Francisco on 2025-11-04 to 2025-11-06 and Jason follow-up items.


## Action Items


- [?] Coordinate a possible in-person meeting in San Francisco between VAST and OpenAI during 2025-11-04 to 2025-11-06, potentially including a VAST founder and architect. @Myself 📅 2025-11-04 #task #proposed #auto

- [?] Send Sam Hopewell a concise VAST POC plan for OpenAI, including required features such as a Blob-compatible API, caching, and global namespace capabilities. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Prepare POC environment details and staging requirements for the OpenAI VAST POC on the CoreWeave cluster. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Confirm OpenAI internal bandwidth and provide a target window to start the VAST POC on the CoreWeave cluster. @Sam Hopewell 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Clarify NDA boundaries for what prior OpenAI workload and architecture knowledge Jason Vallery can leverage while at VAST Data. @Sam Hopewell 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Assess whether a Blob-compatible API over VAST is required or preferred for OpenAI GPU-node integration. @Sam Hopewell 📅 2025-10-27 #task #proposed #auto

- [?] Loop in OpenAI DAC and Applied teams to test the CoreWeave cluster once it is available for the VAST POC. @Sam Hopewell 📅 2025-10-27 #task #proposed #auto

- [?] Evaluate viability and reliability of VAST global namespace and metadata scaling for multi-exabyte namespaces under OpenAI metadata and IO patterns. @TBD 📅 2025-10-26 ⏫ #task #proposed #auto






## Key Information


- Jason Vallery leads VAST Data strategy and direction for hyperscalers and cloud platforms, including how VAST supports large AI workloads like OpenAI.

- Sam Hopewell described OpenAI's storage tiering model as Azure cold storage, VAST warm storage, and on-GPU hot local storage.

- OpenAI wants GPU-adjacent storage that isolates GPU fleets from network variability and Azure slowness, enabling fast staging of data onto GPUs when needed.

- Sam Hopewell stated OpenAI is exploring building its own global namespace and expects to manage its own global state due to a converged layer with multiple clusters and cloud object stores on top.

- Sam Hopewell indicated OpenAI has high expectations for list operations, throughput, and performance at exabyte scale, and expects data growth to continue.

- Jason Vallery stated VAST CEO Renan gave a directive to do whatever it takes to close OpenAI feature gaps quickly, including implementing requested platform features if needed.



---

*Source: [[2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm]]*