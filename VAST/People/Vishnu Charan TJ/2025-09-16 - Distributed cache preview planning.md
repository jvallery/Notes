---
type: "people"
title: "Distributed cache preview planning"
date: "2025-09-16"
person: "Vishnu Charan TJ"
participants: ["Vishnu Charan TJ", "Amit", "Jason Vallery", "Sourav", "Shankar", "Pete", "Tomer", "Akanksha"]
source: "transcript"
source_ref: "Inbox/_archive/2025-09-16/2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp.md"
tags:
  - "type/people"
  - "person/vishnu-charan-tj"
  - "generated"
---

# Distributed cache preview planning

**Date**: 2025-09-16
**With**: Vishnu Charan TJ, Amit, Jason Vallery, Sourav, Shankar, Pete, Tomer, Akanksha

## Summary

Reviewed status of the distributed cache for checkpointing: implementation is complete, with resilience and scale testing (100–200 nodes) in progress. Agreed to proceed toward a private preview by end of September starting with Figure AI, using an AKS Linux mount approach initially due to CSI/containers team concerns, and to defer MAI re-engagement until a data-driven scale/throughput narrative is available.
## Action Items
- [ ] Run 100–200 node scale tests for distributed cache and record performance/resilience results @Akanksha 📅 2025-10-26 🔺 #task
- [ ] Capture network throughput reduction to Blob with and without cache during scale tests @Akanksha 📅 2025-10-26 🔺 #task
- [ ] Measure TPS per node to metadata/blob and extrapolate scalability to 10k–100k nodes @Tomer 📅 2025-10-26 🔺 #task
- [ ] Finalize AKS Linux mount integration steps and prepare demo @Amit 📅 2025-10-26 ⏫ #task
- [ ] Hand off AKS setup and build to Vishnu for validation @Amit 📅 2025-10-26 ⏫ #task
- [ ] Prepare private preview plan (customers, docs, enablement) and align stakeholders @Vishnu 📅 2025-10-26 🔺 #task
- [ ] Document supported scenarios and explicit limitations for MVP @Vishnu 📅 2025-10-26 🔺 #task
- [ ] Investigate feasibility of SSD-only KV cache offload without cloud tier for CoreAI @Amit 📅 2025-10-26 ⏫ #task
- [ ] Continue resilience and performance tuning for distributed cache @Sourav 📅 2025-10-26 ⏫ #task
- [ ] Review AWS PyTorch S3 storage writer and evaluate applicable prefix/naming learnings @Amit 📅 2025-10-26 🔽 #task
- [ ] Evaluate long-term approach: contribute caching into Python/open-source tools vs kernel-mode driver @BlobFuse Engineering Team 📅 2025-10-26 🔽 #task
- [ ] Reassess AKS CSI driver path with containers team and document concerns/timeline @AKS Containers Team 📅 2025-10-26 ⏫ #task
- [ ] Assemble data-driven narrative for MAI (scale targets, throughput reduction, reliability) @Amit 📅 2025-10-26 ⏫ #task
- [ ] Schedule and run deep-dive to address Vishnu’s requirements list (use BlobFuse meeting if possible) @Vishnu 📅 2025-10-26 ⏫ #task
- [ ] Confirm Figure AI preview timing and environment details (VMSS vs AKS) and next steps @Vishnu 📅 2025-10-26 🔺 #task
- [ ] Share AKS Linux mount setup instructions with stakeholders for trial @Amit 📅 2025-10-26 ⏫ #task
- [ ] Align on measurement methodology and tooling for throughput and TPS metrics @Akanksha 📅 2025-10-26 🔺 #task
- [ ] Re-engage MAI after metrics and scalability narrative are ready @Jason Vallery 📅 2025-10-26 ⏫ #task

## Decisions
- Proceed toward a private preview by end of September with Figure AI; defer MAI until metrics and a scale narrative are ready.
- Use Linux mount for AKS integration initially; CSI route remains under evaluation.
- Limit MVP/preview scope to checkpointing (exclude model/dataset loading and prefetch).
- Include measurement of network throughput reduction and TPS to metadata/blob as part of scale testing.

## Key Information
- Distributed cache for checkpointing (write/read) implementation is complete; node up/down scenarios are under test.
- MVP does not support model or dataset loading, has no prefetch, and does not support cross-node model refill on node loss.
- Two checkpoint modes exist: cache-only and cache with lazy writeback to storage.
- AKS integration is proceeding via Linux mount due to CSI/containers team concerns about internal IP/inter-node communication and Kubernetes operator integration.
- Scale testing planned at 100–200 nodes with intent to extrapolate to 10k–100k nodes; key risk is metadata/blob TPS bottlenecks at large scale.
- Figure AI is the initial preview candidate and is believed to use VMSS rather than AKS for training.
- MAI currently prefers Python/open-source tooling (e.g., blobfile) and is not adopting BlobFuse until shown data-driven benefits.
- CoreAI requested SSD-only KV cache offload without cloud tier; feasibility is unclear.
- AWS reference patterns discussed: PyTorch S3 storage writer, prefix layout/high-entropy naming to reduce partition hot spots, and S3 Express as a cache-like layer.

---

*Source: [[Inbox/_archive/2025-09-16/2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp.md|2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp]]*

## Related

- [[Vishnu Charan TJ]]
- [[Jason Vallery]]
- [[Akanksha Mehrotra]]
- [[Noa Cohen]]
- [[David Holz]]
- [[John Mao]]
- [[Cloud control plane]]
- [[Microsoft]]
- [[Amazon]]
