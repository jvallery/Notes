---
type: "projects"
title: "Azure integration recording, outline and MVP focus on Blob API compatibility for GPU-adjacent VAST"
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

# Azure integration recording, outline and MVP focus on Blob API compatibility for GPU-adjacent VAST

**Date**: 2025-12-18
**Project**: [[]]
**Attendees**: Unknown

## Summary

The discussion frames a single document to describe how VAST Data integrates with Microsoft Azure, covering business strategy, workloads, differentiation, and required engineering on both sides. The core near-term integration opportunity described is GPU-adjacent VAST clusters that synchronize with a central Azure data lake using Azure Blob data movement primitives, with an MVP emphasis on implementing enough Blob REST API compatibility to work with azCopy.


## Action Items


- [?] Draft the initial outline for the 'VAST Data integration with Microsoft Azure' document, including sections for business strategy, partnership areas, target workloads, differentiation, and engineering responsibilities/constraints for both VAST and Microsoft. @TBD ⏫ #task #proposed #auto

- [?] Use AI-assisted research to compile a coverage map of Azure platform surface area and VAST Data platform surface area to identify potential integration points and overlaps. @TBD #task #proposed #auto

- [?] Review the azCopy open source codebase to enumerate the exact Azure Blob REST API calls and request/response signatures azCopy depends on, and use that list to define the MVP Blob API surface area for VAST. @TBD ⏫ #task #proposed #auto

- [?] Document which Azure Blob features are explicitly out of scope for the MVP VAST Blob API (for example Append Blob, Page Blob, ADLS Gen2 hierarchical namespace/DFS endpoint) and provide scenario-based justification for each exclusion. @TBD #task #proposed #auto




## Decisions


- Define the Azure integration document as a single master document that can be split into independent sections, explicitly answering the 'what, why, and how' of VAST Data integration with Microsoft Azure.

- Treat azCopy compatibility as the minimum viable product requirement for any VAST implementation of an Azure Blob Storage-compatible API, focusing on data movement between central Azure Blob storage and GPU-adjacent VAST.




## Key Information


- The planned Azure integration document is intended to answer the 'what, why, and how' of VAST Data integration with Microsoft Azure, and be structured as one document with sections that can be split into standalone documents.

- VAST on Cloud (as described) runs on virtual machines in any cloud provider, which constrains price-performance and makes it better for exposing endpoints than for storing large volumes of data due to VM and local ephemeral storage capacity limits.

- A current VAST on Cloud scenario is burst-to-cloud where an on-premises VAST cluster remains the system of record and VAST on Cloud provides cloud-based caching and endpoints (NFS or S3) via VAST global namespace and global data spaces so cloud compute can access on-prem data.

- A key target scenario described is frontier model builders (examples given: OpenAI and Microsoft AI Infrastructure) with a centralized Azure data lake in a large 'hero' Azure region and disaggregated GPUs deployed across many smaller Azure regions and non-Azure locations, requiring GPU-adjacent storage for staging training data and checkpoints synchronized back to the central data estate.

- The integration opportunity described is to connect a GPU-adjacent VAST cluster with a central Azure data lake using data movement primitives such as Azure 'Put Blob from URL' APIs, effectively enabling synchronization between VAST and Azure Blob storage.

- OpenAI's internal data movement tool 'SciClone' (spelled S-C-I-C-L-O-N-E) previously used Microsoft's azCopy library and was said to have refactored away from azCopy to use rclone.

- azCopy is described as the de facto tool for moving data in and out of Azure Blob storage and between storage accounts and regions, implemented in Go and using 'Put Blob from URL' APIs; Microsoft internal tools like Azure Storage Mover are described as being built on top of azCopy.

- Microsoft AI Infrastructure (MAI) is described as using azCopy to move data in and out of Azure Blob storage and between blob accounts or to non-blob targets.

- One proposed VAST approach is to implement an Azure Blob Storage-compatible API on top of VAST so customers can use existing Azure tooling (especially azCopy) to move data between central Azure Blob storage and GPU-adjacent VAST deployments.

- The MVP definition for a VAST Blob API is described as implementing the minimum Azure Blob REST API surface required for azCopy compatibility, including operations such as Put Blob, Put Block, List Blobs, Get Blob, Get Blob metadata, and container listing operations.

- Non-MVP Blob features called out as longer-tail include Append Blob, Page Blob, and ADLS Gen2 hierarchical namespace (DFS endpoint), and the intent is to document why these are out of scope for MVP.

- For analytics workloads (Databricks, Spark, analytics pipelines), the guidance described is to prefer VAST native integrations (VAST drivers and VAST database capability) rather than relying on a Blob API, positioning the Blob API primarily for compatibility and data movement scenarios.

- VAST is described as having a Kafka endpoint to enable data streaming directly into VAST, reducing the need to run Kafka separately for some ingestion scenarios.



---

*Source: [[2025-12-18 - Azure integration recording]]*