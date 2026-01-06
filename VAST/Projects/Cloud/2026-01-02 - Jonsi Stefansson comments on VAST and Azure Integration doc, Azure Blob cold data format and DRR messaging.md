---
type: projects
title: Jonsi Stefansson comments on 'VAST and Azure Integration' doc, Azure Blob cold data format and DRR messaging
date: '2026-01-02'
project: Cloud
participants:
- Jonsi Stefansson
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2026-01-02_095616_6115_VAST-and-Azure-Integrationdocx.md
tags:
- type/projects
- project/cloud
- generated
---

# Jonsi Stefansson comments on 'VAST and Azure Integration' doc, Azure Blob cold data format and DRR messaging

**Date**: 2026-01-02

**Project**: [[Cloud]]

**Attendees**: Jonsi Stefansson

## Summary

A Google Docs notification email captured two open comments from Jonsi Stefansson on the 'VAST and Azure Integration.docx' document. Jonsi questioned whether VAST cold data tiering to Azure Blob should use VAST object format (not directly readable in Azure Blob) versus native Azure Blob format, and asked whether the doc should more strongly state how VAST DRR and efficiencies mitigate flash supply chain risk.


## Action Items


- [?] Review the 'VAST and Azure Integration.docx' section on cold data tiering to Azure Blob and propose whether the recommended format should be VAST object format (opaque, maximum data reduction) or native Azure Blob format (direct readability and ecosystem accessibility). @Myself ⏫ #task #proposed #auto

- [?] Update or propose edits to the 'VAST and Azure Integration.docx' narrative to more explicitly quantify or explain how VAST DRR and storage efficiencies reduce risk from flash supply constraints and rising flash prices. @Myself #task #proposed #auto






## Key Information


- Jonsi Stefansson raised a concern that tiering cold data to Azure Blob using VAST object format would make the data not directly readable from Azure Blob, and suggested reconsidering native Azure Blob format for better Azure ecosystem compatibility.

- Jonsi Stefansson requested stronger messaging in the 'VAST and Azure Integration' document about how VAST DRR and storage efficiencies reduce exposure to flash supply constraints and rising flash prices.

- The 'VAST and Azure Integration' document includes a positioning statement that integrating with Azure Blob allows customers to place the long-tail dataset on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set to hedge against flash component price volatility.




---

*Source: [[2026-01-02_095616_6115_VAST-and-Azure-Integrationdocx]]*
