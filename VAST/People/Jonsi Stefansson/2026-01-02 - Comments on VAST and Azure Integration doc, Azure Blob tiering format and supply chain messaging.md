---
type: people
title: Comments on 'VAST and Azure Integration' doc, Azure Blob tiering format and supply chain messaging
date: '2026-01-02'
participants:
- Jonsi Stephenson
- Jonsi Stefansson
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2026/2026-01-02_095616_9612_VAST-and-Azure-Integrationdocx.md
tags:
- type/people
- generated
person: Jonsi Stefansson
---

# Comments on 'VAST and Azure Integration' doc, Azure Blob tiering format and supply chain messaging

**Date**: 2026-01-02
**Attendees**: Jonsi Stephenson

## Summary

Google Docs notification email shows two open comments from Jonsi Stephenson on the document 'VAST and Azure Integration.docx'. The comments ask whether VAST should avoid using VAST object format for cold data tiered to Azure Blob (to keep data readable directly in Azure Blob), and whether the doc should more strongly state that VAST DRR/efficiencies mitigate flash supply chain constraints.

## Action Items

- [?] Respond in 'VAST and Azure Integration.docx' to Jonsi Stephenson's comment and decide whether cold data tiered to Azure Blob should be stored in VAST object format (max data reduction but not directly readable in Azure Blob) or in native Azure Blob format (direct readability and ecosystem accessibility). @Myself ⏫ #task #proposed #auto

- [?] Update 'VAST and Azure Integration.docx' to address Jonsi Stephenson's request for stronger messaging on how VAST DRR/efficiencies mitigate flash supply chain constraints and rising flash prices, ensuring claims are accurate and supportable. @Myself #task #proposed #auto

- [?] Review 'VAST and Azure Integration.docx' and decide whether the Azure Blob cold tier should be described as using VAST object format (opaque, maximum data reduction) or native Azure Blob format (direct readability and ecosystem accessibility), then update the document accordingly. @Myself ⏫ #task #proposed #auto

- [?] Update 'VAST and Azure Integration.docx' to clarify and potentially strengthen the statement about how VAST DRR/efficiencies reduce flash capacity requirements and mitigate flash supply chain constraints and price volatility. @Myself #task #proposed #auto

## Key Information

- Jonsi Stephenson left an open comment in 'VAST and Azure Integration.docx' questioning whether cold data tiered to Azure Blob should use VAST object format (not directly readable from Azure Blob) versus native Azure Blob format for direct readability and ecosystem accessibility.

- Jonsi Stephenson left an open comment in 'VAST and Azure Integration.docx' asking whether the document should make a firmer statement that VAST DRR/efficiencies reduce the impact of flash supply constraints and rising prices.

- The document text states that cold data can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), positioning this as enabling infinite scale without flash price premium.

- The document text argues that constrained flash supply and rising prices make an 'all-flash everything' strategy economically risky for exabyte-scale data, and that deep integration with Azure Blob lets customers keep the long-tail on HDD-based object storage while reserving VAST flash for GPU-adjacent working sets as a hedge against component volatility.

---

- Jonsi Stefansson raised a concern that tiering cold data to Azure Blob using VAST object format would not be readable directly from Azure Blob, and suggested reconsidering native Azure Blob format for ecosystem accessibility.

- The document 'VAST and Azure Integration.docx' includes a statement that cold data can be transparently tiered to Azure Blob using either VAST native opaque formats for maximum data reduction or transparent open standard formats for ecosystem accessibility.

- Jonsi Stefansson suggested strengthening the document's messaging to more firmly state that VAST data reduction ratio (DRR) and efficiencies reduce the impact of flash supply constraints and rising prices.
