---
type: "projects"
title: "Azure integration recording, document structure and MVP Blob API for GPU-adjacent VAST"
date: "2025-12-18"
project: ""
participants: ["Unknown"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-18 - Azure integration recording.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Azure integration recording, document structure and MVP Blob API for GPU-adjacent VAST

**Date**: 2025-12-18
**Project**: [[]]
**Attendees**: Unknown

## Summary

The transcript outlines a planned joint document describing how VAST Data integrates with Microsoft Azure, covering business strategy, workload scenarios, and engineering design constraints. The core near-term integration opportunity described is GPU-adjacent VAST clusters synchronized with a central Azure data lake using Azure Blob data movement primitives, with an MVP focus on implementing enough Blob API compatibility to work with azCopy.


## Action Items


- [?] Draft an outline for the 'VAST Data integrates with Microsoft Azure' document that explicitly covers business strategy, partnership areas, target workloads, differentiation, and engineering responsibilities and constraints, organized so sections can be published independently. @Myself ⏫ #task #proposed #auto

- [?] Use azCopy open source code to enumerate the exact Azure Blob REST API calls and required request/response signatures that azCopy depends on, and convert that into a concrete MVP requirements list for a VAST Blob Storage-compatible API. @Myself ⏫ #task #proposed #auto

- [?] Document which Azure Blob features are explicitly out of MVP scope (for example Append Blob, Page Blob, ADLS Gen2 hierarchical namespace and DFS endpoint) and provide scenario-based justification tied to the GPU-adjacent storage and central data lake synchronization use case. @Myself #task #proposed #auto

- [?] Capture the canonical workload narrative for frontier model builders (central Azure data lake plus distributed GPU sites) including data staging and checkpoint flows, and map where VAST DataSpaces and data movement tooling (azCopy, Put Blob from URL) fit in the end-to-end architecture. @Myself #task #proposed #auto




## Decisions


- Define the Azure integration document around 'what, why, and how', and structure it so sections can be separated into standalone documents.

- Treat azCopy compatibility as the minimum viable product requirement for any VAST implementation of an Azure Blob Storage-compatible API intended to support GPU-adjacent VAST to central Azure data lake data movement.




## Key Information


- The planned 'VAST Data integrates with Microsoft Azure' document is intended to answer 'what we are building, why we are building it, and how it will work', and be structured so sections can be carved out into independent documents.

- The current 'VAST on cloud' offering runs on virtual machines in any cloud provider, which constrains price-performance and makes it better for exposing endpoints than for storing large volumes of data due to VM and local ephemeral storage capacity limits.

- A current supported scenario is burst-to-cloud where an on-premises VAST cluster is accessed from cloud compute via VAST global namespace (Global DataSpaces), using cloud-based caching and cloud endpoints for NFS or S3.

- A target integration scenario described is a frontier model builder (examples given: OpenAI, Microsoft AI) with a centralized Azure data lake in a large 'hero' Azure region and disaggregated GPUs across many Azure regions and non-Azure locations, requiring staging training data and checkpoints near GPUs and synchronizing back to the central data estate.

- The integration opportunity is to connect GPU-adjacent storage (VAST cluster near GPUs) with central Azure storage (Azure Blob-based data lake) using data movement primitives such as Azure 'Put Blob from URL'.

- azCopy is described as the de facto Microsoft and customer tool for moving data in and out of Azure Blob Storage, built in Go and using 'Put Blob from URL' APIs; Microsoft internal tools like Azure Storage Mover are described as being built on top of azCopy.

- OpenAI's in-house data movement tool 'SciClone' (spelled S-C-I-C-L-O-N-E) was described as previously built on azCopy, and later refactored to use rclone instead of azCopy.

- Microsoft AI Infrastructure (MAI) is described as using azCopy to move data in and out of Azure Blob Storage and between Blob accounts.

- A proposed VAST approach is to implement an Azure Blob Storage-compatible API on top of VAST to enable customers (examples given: OpenAI, Microsoft AI) to use existing tooling and frameworks for data movement with GPU-adjacent VAST deployments.

- The MVP definition for a VAST Blob API is described as 'compatibility with azCopy' without requiring Microsoft to refactor azCopy, implying VAST should emulate the Blob REST API surface that azCopy depends on.

- The transcript lists core Blob REST operations as likely required for azCopy compatibility, including Put Blob, Put Block, Get Blob, List Blobs, Get Blob Containers, and Get Blob Metadata (exact API names/signatures to be validated against azCopy source).

- Non-MVP Blob features called out as longer-tail include Append Blob, Page Blob, and ADLS Gen2 hierarchical namespace (DFS endpoint), and the document should justify why these are not covered in the MVP.

- For analytics workloads (Databricks, Spark), the transcript asserts VAST already has native integrations and drivers, and also has a Kafka endpoint for streaming directly into VAST, so the Blob API motivation is primarily compatibility for data movement rather than analytics integration.



---

*Source: [[2025-12-18 - Azure integration recording]]*