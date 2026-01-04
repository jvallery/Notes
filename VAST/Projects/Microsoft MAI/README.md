---
type: projects
title: Microsoft MAI
created: "2026-01-04"
status: active
tags:
  - type/projects
  - project/microsoft-mai
  - customer/microsoft
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
