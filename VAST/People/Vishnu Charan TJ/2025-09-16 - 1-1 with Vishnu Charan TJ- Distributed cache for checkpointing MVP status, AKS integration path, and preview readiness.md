---
type: "people"
title: "1:1 with Vishnu Charan TJ: Distributed cache for checkpointing MVP status, AKS integration path, and preview readiness"
date: "2025-09-16"
person: ""
participants: ["Jason Vallery", "Vishnu Charan TJ", "Amit", "Sourav", "Akanksha Mehrotra", "Tomer Hagay", "Vikas (last name unknown)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Vishnu Charan TJ: Distributed cache for checkpointing MVP status, AKS integration path, and preview readiness

**Date**: 2025-09-16
**With**: Jason Vallery, Vishnu Charan TJ, Amit, Sourav, Akanksha Mehrotra, Tomer Hagay, Vikas (last name unknown)

## Summary

Reviewed status of the distributed cache for checkpointing: core implementation is complete, with scale, resilience, and node up-down testing in progress. Agreed to target a private preview by end of September 2025 with Figure AI, use AKS Linux mounts initially due to CSI and containers team concerns, and defer MAI adoption until a data-driven scale and throughput narrative is established.


## Action Items


- [?] Run 100 to 200 node scale tests for the distributed cache checkpointing MVP and record performance and resilience results. @Akanksha Mehrotra 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Capture network throughput reduction to Azure Blob with and without the distributed cache during scale tests. @Akanksha Mehrotra 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Measure TPS per node to metadata and blob services and extrapolate scalability implications for 10,000 to 100,000 node clusters. @Tomer Hagay 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Finalize AKS Linux mount integration steps for the distributed cache checkpointing MVP and prepare a demo. @Amit 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Hand off AKS setup and build steps to Vishnu Charan TJ for validation ahead of private preview. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Prepare the private preview plan for the distributed cache checkpointing MVP, including customer list, documentation, enablement, and stakeholder alignment. @Vishnu Charan TJ 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Document supported scenarios and explicit limitations for the distributed cache checkpointing MVP (no model/dataset loading, no prefetch, no cross-node refill on node loss). @Vishnu Charan TJ 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Investigate feasibility of SSD-only KV cache offload without a cloud tier to meet CoreAI requirements. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Continue resilience and performance tuning for the distributed cache checkpointing MVP to improve stability and performance ahead of preview. @Sourav 📅 2025-10-26 #task #proposed #auto

- [?] Review AWS PyTorch S3 storage writer patterns and evaluate applicable learnings for prefix layout and naming conventions. @Amit 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Evaluate long-term approach for caching delivery: contribute caching into Python or open-source tools versus building a kernel-mode driver. @BlobFuse Engineering Team 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Reassess the AKS CSI driver path with the AKS containers team and document concerns and an estimated timeline for resolution. @AKS Containers Team 📅 2025-10-26 #task #proposed #auto

- [?] Assemble a data-driven narrative for MAI adoption, including scale targets, throughput reduction to Azure Blob, and reliability outcomes from testing. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Schedule and run a deep-dive to address Vishnu Charan TJ requirements list, using the BlobFuse meeting if possible. @Vishnu Charan TJ 📅 2025-10-26 #task #proposed #auto

- [?] Confirm Figure AI private preview timing and environment details (VMSS vs AKS) and define next steps. @Vishnu Charan TJ 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Share AKS Linux mount setup instructions with stakeholders for trial and validation. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Align on measurement methodology and tooling for throughput and TPS metrics collection during scale tests. @Akanksha Mehrotra 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Re-engage Microsoft MAI stakeholders after metrics and scalability narrative are ready for review. @Myself 📅 2025-10-26 #task #proposed #auto




## Decisions


- Target a private preview by 2025-09-30 with Figure AI for the distributed cache checkpointing MVP, and defer MAI adoption until scale and throughput metrics support a data-driven narrative.

- Use AKS Linux mounts for initial AKS integration and validation; keep the CSI-based approach under evaluation pending AKS containers team concerns and timeline.

- Keep MVP scope limited to checkpointing; exclude model loading, dataset loading, and prefetch from the private preview.

- Include measurement of network throughput reduction to Azure Blob and TPS per node to metadata and blob services as part of 100 to 200 node scale testing.




## Key Information


- Distributed cache for checkpointing (write and read) implementation is complete; testing continues for node up and node down scenarios.

- The MVP scope for distributed cache is checkpointing only; model loading and dataset loading are out of scope, and there is no prefetch or cross-node model refill on node loss.

- Two checkpoint modes exist: cache-only and cache with lazy writeback to storage.

- AKS integration will proceed via Linux mounts initially because the AKS containers team raised concerns about CSI and Kubernetes integration, including use of internal IPs for inter-node communication and lack of Kubernetes operator integration.

- Scale testing is planned at 100 to 200 nodes, with intent to extrapolate implications for 10,000 to 100,000 node clusters; key metrics include network throughput reduction to Azure Blob and TPS per node to metadata and blob services.

- Figure AI is the initial private preview candidate; the notes indicate Figure AI uses VMSS rather than AKS, but the transcript also contains a statement that Figure AI uses AKS, so the deployment environment needs confirmation.

- MAI is currently not adopting BlobFuse and will be re-engaged only after a data-driven narrative is assembled (scale targets, throughput reduction, reliability).

- CoreAI requested SSD-only KV cache offload without a cloud tier; feasibility is currently unclear.

- Resilience and performance tuning for the distributed cache is ongoing to improve stability and performance ahead of preview.

- AWS reference patterns were discussed as examples, including a PyTorch S3 storage writer, prefix layout conventions, and S3 Express.



---

*Source: [[2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp]]*