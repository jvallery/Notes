---
type: "people"
title: "Jeff Denworth 1:1 - Microsoft strategy, Blob API vs Tuscany, and SCO presentation prep"
date: "2025-12-19"
person: ""
participants: ["Jason Vallery", "Jeff Denworth", "Pete Eming", "John Mao", "Vamshi (last name unknown)", "Manish Sah", "Venkat (last name unknown)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-19 - Jeff Denworth - Microsoft strategy and SCO prep.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# Jeff Denworth 1:1 - Microsoft strategy, Blob API vs Tuscany, and SCO presentation prep

**Date**: 2025-12-19
**With**: Jason Vallery, Jeff Denworth, Pete Eming, John Mao, Vamshi (last name unknown), Manish Sah, Venkat (last name unknown)

## Summary

Jason Vallery and Jeff Denworth aligned on how to frame VAST's Microsoft strategy discussion, focusing on trade-offs between supporting the Azure Blob API versus Microsoft's internal project "Tuscany" and the broader market opportunity beyond OpenAI and Microsoft AI. They discussed competitive dynamics at OpenAI, including OpenAI's move away from Blob-based replication toward an internal sync approach and the implications of Microsoft's IP rights to OpenAI-developed code. They also noted the need to prepare for an upcoming SCO presentation, but specific deliverables and dates were not finalized in the captured transcript.


## Action Items


- [?] Define the decision framework for VAST's Microsoft strategy: compare required Azure Blob API surface area for day-one MVP versus broader market requirements, and explicitly weigh against Microsoft's internal project Tuscany. @Myself ⏫ #task #proposed #auto

- [?] Follow up with Jeff Denworth to clarify expectations for the SCO presentation Jason Vallery will deliver, including target audience, key messages, and required artifacts. @Myself ⏫ #task #proposed #auto

- [?] Validate with a Microsoft or OpenAI contact whether OpenAI is actively replacing Blob-based replication with an rclone-based internal sync engine, and assess what that means for VAST's Blob API investment. @Myself #task #proposed #auto

- [?] Confirm the current contractual and practical reality of Microsoft's rights to OpenAI-developed code (including Rockset-related IP) and document the risk implications for VAST's competitive positioning in Azure. @Myself #task #proposed #auto




## Decisions


- Jeff Denworth directed Jason Vallery to talk through the Microsoft strategy and trade-offs verbally rather than reviewing Jason's draft document during this meeting.




## Key Information


- Jeff Denworth stated that focusing only on OpenAI and Microsoft AI as the target customers for Blob API support is too myopic, and he prefers committing to a broader market approach ("in for a pound").

- Jason Vallery said he had coffee with Pete Eming, who reports to Vamshi (last name unknown) and currently owns the relationship between Azure Storage and OpenAI and Microsoft AI after Jason transitioned out about a year prior.

- Jason Vallery reported (secondhand from Pete Eming) that OpenAI is replatforming away from Azure Blob API usage for certain scenarios, including replacing a Blob-based data movement/replication engine with an internal solution using rclone and other tools.

- Jason Vallery asserted that VAST's competition at OpenAI is likely OpenAI's internal storage platform work (influenced by Rockset acquisition and RocksDB-based capacity management), rather than external vendors like Weka.

- Jason Vallery stated that OpenAI has an SDK used by its training platform that abstracts multiple cloud object APIs, including S3, Google Cloud Storage, and Azure Blob Storage.

- Jason Vallery stated that Microsoft's deal with OpenAI grants Microsoft ownership and unlimited use rights to code written by OpenAI until an "AGI" declaration event by OpenAI's board, and Jeff Denworth reacted that this could create risk if Microsoft can reuse OpenAI storage IP for Azure services.

- Jeff Denworth expressed skepticism that a Rockset-derived team could quickly build a geoscale, hyperscale object store, noting it took Microsoft a decade to build theirs and it still has reliability issues.

- Jason Vallery stated that Microsoft AI (MAI) is less sophisticated than OpenAI but currently leverages the Azure Blob API.



---

*Source: [[2025-12-19 - Jeff Denworth - Microsoft strategy and SCO prep]]*