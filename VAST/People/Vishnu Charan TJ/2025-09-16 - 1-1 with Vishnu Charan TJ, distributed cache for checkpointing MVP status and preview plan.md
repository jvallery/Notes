---
type: "people"
title: "1:1 with Vishnu Charan TJ, distributed cache for checkpointing MVP status and preview plan"
date: "2025-09-16"
person: ""
participants: ["Jason Vallery", "Vishnu Charan TJ", "Akanksha Mehrotra", "Tomer Hagay", "Sourav", "Amit", "Vikas"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Vishnu Charan TJ, distributed cache for checkpointing MVP status and preview plan

**Date**: 2025-09-16
**With**: Jason Vallery, Vishnu Charan TJ, Akanksha Mehrotra, Tomer Hagay, Sourav, Amit, Vikas

## Summary

Reviewed status of the distributed cache for checkpointing, implementation is complete and scale plus resilience testing is in progress. Agreed to target a private preview by end of September 2025 with Figure AI, use AKS Linux mounts initially due to CSI and containers team concerns, and defer MAI adoption until a data-driven scale and throughput narrative is established.


## Action Items


- [?] Run 100 to 200 node scale tests for the distributed cache checkpointing MVP and record performance and resilience results. @Akanksha Mehrotra 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Capture network throughput reduction to Azure Blob Storage with and without the distributed cache during scale tests. @Akanksha Mehrotra 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Measure TPS per node to metadata and blob endpoints and extrapolate scalability implications for 10,000 to 100,000 node clusters. @Tomer Hagay 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Finalize AKS Linux mount integration steps for the distributed cache checkpointing MVP and prepare a demo. @Amit 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Hand off AKS setup and build steps to Vishnu Charan TJ for validation ahead of the private preview. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Prepare the private preview plan for the distributed cache checkpointing MVP, including customer list, documentation, enablement, and stakeholder alignment. @Vishnu Charan TJ 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Document supported scenarios and explicit limitations for the distributed cache checkpointing MVP (no model loading, no dataset loading, no prefetch, no cross-node model refill on node loss). @Vishnu Charan TJ 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Investigate feasibility of SSD-only KV cache offload without a cloud tier to meet CoreAI requirements. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Continue resilience and performance tuning for the distributed cache checkpointing MVP to improve stability and performance. @Sourav 📅 2025-10-26 #task #proposed #auto

- [?] Review AWS PyTorch S3 storage writer patterns and evaluate applicable prefix and naming learnings for checkpoint sharding and layout. @Amit 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Evaluate long-term approach for caching integration: contribute caching into Python or open-source tools versus building a kernel-mode driver. @BlobFuse Engineering Team 📅 2025-10-26 🔽 #task #proposed #auto

- [?] Reassess the AKS CSI driver path with the AKS containers team and document concerns and an estimated timeline for CSI-based integration. @AKS Containers Team 📅 2025-10-26 #task #proposed #auto

- [?] Assemble a data-driven narrative for Microsoft MAI adoption, including scale targets, throughput reduction to Blob, and reliability outcomes from testing. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Schedule and run a deep-dive to address Vishnu Charan TJ requirements list, using the BlobFuse meeting if possible. @Vishnu Charan TJ 📅 2025-10-26 #task #proposed #auto

- [?] Confirm Figure AI private preview timing and environment details (VMSS vs AKS) and define next steps for onboarding. @Vishnu Charan TJ 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Share AKS Linux mount setup instructions with stakeholders for trial and validation. @Amit 📅 2025-10-26 #task #proposed #auto

- [?] Align on measurement methodology and tooling for throughput and TPS metrics for the distributed cache checkpointing MVP scale tests. @Akanksha Mehrotra 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Re-engage Microsoft MAI stakeholders after metrics and scalability narrative are ready for review. @Myself 📅 2025-10-26 #task #proposed #auto




## Decisions


- Proceed toward a private preview by 2025-09-30 with Figure AI for the distributed cache checkpointing MVP; defer Microsoft MAI engagement until scale and throughput metrics support a data-driven adoption narrative.

- Use Linux mount integration for AKS initially for the distributed cache checkpointing MVP; keep the CSI PV route under evaluation pending AKS containers team concerns and timeline.

- Limit the private preview MVP scope to checkpointing use cases only; exclude model loading, dataset loading, and prefetch capabilities from the MVP.

- Include measurement of network throughput reduction to Azure Blob Storage and TPS per node to metadata and blob endpoints as part of 100 to 200 node scale testing.




## Key Information


- Distributed cache for checkpointing (write and read) is implemented; node up and node down resilience scenarios are under test.

- MVP scope for distributed cache is checkpointing only; model loading, dataset loading, prefetch, and cross-node model refill on node loss are not supported in the MVP.

- Two checkpoint modes exist for the distributed cache: cache-only and cache with lazy writeback to storage.

- AKS integration for the distributed cache will proceed via Linux mounts initially because the AKS containers team raised concerns about CSI and Kubernetes integration, including use of internal IPs for inter-node communication.

- Scale testing is planned at 100 to 200 nodes with the goal of extrapolating implications for 10,000 to 100,000 node clusters, including metadata and blob TPS bottlenecks.

- Figure AI is the initial private preview candidate; the environment is expected to be VMSS rather than AKS (needs confirmation because AKS was also discussed).

- Microsoft MAI is currently deferred for adoption of the distributed cache and BlobFuse-related approach until a data-driven narrative is available (throughput reduction, scalability, reliability).

- CoreAI requested SSD-only KV cache offload without a cloud tier; feasibility is unclear and requires investigation.

- AWS reference patterns were discussed as inputs, including a PyTorch S3 storage writer, prefix layout conventions, and S3 Express.



---

*Source: [[2025-09-16 - Team reviewed status of distributed cache for checkpointing implementation comp]]*