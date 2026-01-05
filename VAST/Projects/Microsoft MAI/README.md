---
type: projects
title: Microsoft MAI
created: '2026-01-04'
status: active
tags:
- type/projects
- project/microsoft-mai
- customer/microsoft
last_contact: '2025-12-27'
---

# Microsoft MAI

## Overview

Microsoft AI (MAI) project - VAST storage deployment at Nebius NeoCloud Dallas for 120K GPU infrastructure.

**Related**: [[Microsoft]]

## Key Details

- **Customer**: Microsoft AI / MAI
- **Location**: Nebius NeoCloud, Dallas
- **Scale**: 120K GPUs (GB300), ~1.6 exabytes storage
- **Timeline**: First racks Jan 2026, 9K GPUs Feb 2026

## Open Tasks

```dataview
TASK
FROM "VAST/Customers and Partners/Microsoft" OR "VAST/Projects/Microsoft MAI"
WHERE !completed AND (contains(text, "MAI") OR contains(text, "Microsoft AI"))
SORT due ASC
```

## Notes

```dataview
LIST
FROM "VAST/Projects/Microsoft MAI"
WHERE file.name != "README"
SORT date DESC
```

## Key Facts

- Lior Genzel reported that MAI's initial GPU delivery is expected in February 2026 and MAI needs a storage solution ready for the May to June 2026 timeframe, with January no longer a hard deadline.

- Lior Genzel reported that Kushal (MAI) said MAI will decide on the storage deployment and told Manish (last name unknown) that Azure Blob does not meet MAI requirements compared to VAST.

- Jeff Denworth stated global supply chain conditions are in turmoil and VAST likely cannot support the MAI deal natively via Arrow or Avnet supply chain channels.

- Jeff Denworth stated Microsoft is considering HDDs for the first April delivery for MAI scale-up, and that HDD supply is also constrained.

- Jeff Denworth stated VAST has not started commercial discussions with Microsoft about the MAI deal at the time of the email thread.
## Recent Context

- 2025-12-21: Mentioned in: Jeff Denworth escalation: MAI supply chain risk and need for immediate deployment plan (no Microsoft inventory reserved)

- 2025-12-27: Jeff Denworth escalated that he has low confidence in closing a Q1 Microsoft MAI deal unless VAST ac...
## Topics

- Microsoft MAI 2EB storage requirement and Q1 deal risk

- Global supply chain constraints, including Arrow/Avnet limitations and HDD scarcity

- Need for on-site Redmond presence to accelerate commercial discussions

- Azure Blob integration proposal requested by Microsoft stakeholders

- CoreWeave testing status and its role in Microsoft MAI decisioning

## Key Decisions

- Jeff Denworth proposed shifting VAST execution mode to assume CoreWeave testing is largely cosmetic and to prioritize immediate commercial and supply chain actions to drive a January first order for Microsoft MAI.
