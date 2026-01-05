---
type: "projects"
title: "Comments on 'VAST and Azure Integration.docx' about cold data tiering format and supply-chain messaging"
date: "2026-01-02"
project: ""
participants: ["Jonsi Stephenson", "Myself"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2026/2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Comments on 'VAST and Azure Integration.docx' about cold data tiering format and supply-chain messaging

**Date**: 2026-01-02
**Project**: [[]]
**Attendees**: Jonsi Stephenson, Myself

## Summary

Google Docs notification email shows two open comments from Jonsi Stefansson on the document 'VAST and Azure Integration.docx'. The comments question whether cold data tiering should use VAST object format versus native Azure Blob format, and whether the document should more strongly state how VAST data reduction efficiencies mitigate flash supply-chain constraints.


## Action Items


- [?] Review the 'VAST and Azure Integration.docx' section on cold data tiering and decide whether to position Azure Blob tiering as VAST object format (opaque) or native Azure Blob format (open/readable directly from Azure Blob), then update the document accordingly. @Myself #task #proposed #auto

- [?] Update the 'VAST and Azure Integration.docx' supply-chain narrative to explicitly quantify or clearly state how VAST data reduction efficiencies (DRR) mitigate flash supply constraints and reduce the economic risk of an all-flash strategy at exabyte scale. @Myself #task #proposed #auto






## Key Information


- Jonsi Stephenson raised a concern that describing cold data as tiered to Azure Blob using VAST object format may be undesirable because data stored in VAST object format would not be readable directly from Azure Blob.

- Jonsi Stephenson suggested reconsidering the cold data tiering description to use native Azure Blob format for ecosystem accessibility and direct readability from Azure Blob.

- The document text claims that integrating VAST with Azure Blob allows customers to place the long-tail dataset on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set, as a hedge against flash component price volatility.

- Jonsi Stephenson asked whether the document should make a firmer statement that VAST unique data reduction and efficiency features reduce exposure to flash supply-chain constraints.



---

*Source: [[2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx]]*