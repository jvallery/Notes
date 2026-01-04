---
type: "customer"
title: "VAST warm storage POC sync"
date: "2025-10-22"
account: "OpenAI"
participants: ["Sam Hopewell", "Jason Vallery"]
source: "transcript"
source_ref: "Inbox/_archive/2025-10-22/2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm.md"
tags:
  - "type/customer"
  - "account/openai"
  - "generated"
---

# VAST warm storage POC sync

**Date**: 2025-10-22
**Account**: [[OpenAI]]
**Attendees**: Sam Hopewell, Jason Vallery

## Summary

Jason Vallery (VAST) and Sam Hopewell (OpenAI) reconnected to position VAST as GPU-adjacent warm storage and potentially a global namespace/caching layer, while clarifying NDA boundaries and operational constraints on GPU nodes. OpenAI interest in a CoreWeave-based POC remains, but timing is deferred due to ongoing firefighting and bandwidth constraints; they also discussed a possible in-person meeting in San Francisco Nov 4–6.
## Action Items
- [ ] Coordinate a possible in-person meeting in San Francisco Nov 4–6 with VAST founder and architect. @Myself 📅 2025-11-04 #task
- [ ] Share a concise POC plan and required features for review (e.g., Blob-compatible API, caching/global namespace). @Myself #task
- [ ] Confirm internal bandwidth and provide a target window to start the VAST POC on the CoreWeave cluster. @Sam Hopewell ⏫ #task
- [ ] Loop in DAC/Applied to test the cluster once it is available. @Sam Hopewell #task
- [ ] Clarify NDA boundaries on what prior workload/context knowledge Jason can leverage. @Sam Hopewell ⏫ #task
- [ ] Evaluate viability and reliability of VAST global namespace and metadata scale for multi-exabyte use. @TBD #task
- [ ] Assess whether a Blob-compatible API over VAST is required/preferred for GPU-node access. @Sam Hopewell #task
- [ ] Prepare POC environment details and staging requirements for kickoff (CoreWeave cluster). @Myself #task

## Key Information
- Jason Vallery now leads VAST strategy/direction for hyperscalers and cloud platforms.
- OpenAI conceptual tiering: Azure cold storage, VAST warm storage, and on-GPU hot/local storage.
- OpenAI wants local storage to insulate GPU fleets from network/Azure variability and enable moving some Applied clusters to Research despite weak connectivity.
- OpenAI is resistant to running non-OpenAI components on GPU nodes unless throughput improvements are clear and interference risk is minimal.
- OpenAI is exploring its own global namespace; concerns include metadata scale and global namespace as a single point of failure.
- VAST CEO (Ronen) committed to rapidly closing feature gaps (e.g., Blob-compatible API, global namespace, KV cache) to win OpenAI.
- A CoreWeave-based POC cluster is pending go-ahead; OpenAI timing is constrained by firefighting.
- Recent storage performance issues were traced to firmware/kernel configuration and are now resolved.
- Org context shared: Udi is above Rory and Sam; Rory owns Frontier clusters; Udi reports to Greg.
- Melissa coordinates Neo clouds/CoreWeave hardware within Kevin Park’s team; team added Misha (London).
- DAC may want to test the cluster once available.
- VAST targets multi-exabyte namespaces; OpenAI is skeptical due to metadata scaling limits.

---

*Source: [[Inbox/_archive/2025-10-22/2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm.md|2025-10-22 - Jason (VAST) reconnected with Sam (OpenAI) to discuss VAST as GPU-adjacent warm]]*

## Related

- [[Sam Hopewell]]
- [[Jason Vallery]]
- [[Sam Altman]]
- [[Greg Brockman]]
- [[Rory Kellerworthy]]
- [[Kevin Park]]
- [[Ronen Cohen]]
- [[Neo]]
- [[OpenAI VAST POC (CoreWeave cluster)]]
- [[VAST]]
- [[Microsoft]]
- [[CoreWeave]]
- [[Oracle]]
