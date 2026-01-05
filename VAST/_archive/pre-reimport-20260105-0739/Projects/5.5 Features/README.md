---
type: projects
title: 5.5 Features
created: '2026-01-03'
last_updated: '2025-10-01'
status: active
tags:
- type/projects
last_contact: '2025-12-01'
---

# 5.5 Features

## Overview

_Project description and goals..._

## Status

**Current Status**: Active

## Recent Context

- 2025-11-03: [[2025-11-03 - 5.5 plan timeline review]] (via Roy)

- 2025-10-24: [[2025-10-24 - AI-first dev and cloud maturity]] (via VAST)

- 2025-10-24: [[2025-10-24 - Engineering maturity and cloud strategy]] (via VAST)

- 2025-10-27: [[2025-10-27 - UK Met dual-track Azure plan]] (via Microsoft)

- 2025-10-28: 2025-10-28 - Weekly 1:1 and Tel Aviv plan (via Shachar Feinblit)

- 2025-10-29: 2025-10-29 - Intro 1:1 on release process (via Liraz Ben Or)

- 2025-10-29: [[2025-10-29 - PM-led cloud model alignment]] (via Tomer Hagay)

- 2025-10-29: [[2025-10-29 - Release process walkthrough with Liraz]] (via Liraz Ben Or)

- 2025-11-01: [[2025-11-01 - Planning sessions operating model]] (via Jeff Denworth)

- 2025-10-01: [[2025-10-01 - Shachar org roles and actions]] (via Shachar Feinblit)

- 2025-12-17: Brian Evans notified the PM team that Cisco submitted RFE 0526 (Existing Feature Enhancement) reques...

- 2025-12-01: An RFE (0482) was submitted for NVIDIA DGX Cloud requesting unified visibility across VAST clusters ...
## Tasks

```dataview
TASK FROM "VAST/Projects/5.5 Features"
WHERE !completed
```

## Related


## Key Facts

- RFE 0526 indicates 'Deal Blocker: No' and estimates 'Additional PB from RFE: 100' with opportunity amount listed as 0 in the RFE record.

- Mordechai Blaunstein indicated a tentative target to support the Service Aware VIP Pool capability in VAST release 5.6, but explicitly noted it is not confirmed.
## Topics

- Cisco RFE 0526 for replication policy filtering using regex allow/deny patterns

- Salesforce RFE workflow, linking RFE to the correct Related Feature

- Enterprise multi-geo compliance and liability protection via replication exclusions

- RFE 0482 for NVIDIA DGX Cloud: unified visibility across VAST clusters deployed at multiple NCPs

- Dual-uplink visibility requirement for dedicated cluster LAX-02 (lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com)

- Tenant-scoped visibility requirement for multi-tenant cluster LAX-03 (DGX Cloud tenant only)

- Proposed implementation approach: Service Aware VIP Pool enabling multi-VIP access to VMS for GUI/CLI/REST/SSH/CSI

- Release targeting discussion for the capability (tentative 5.6, not confirmed)

## Key Decisions

- Jeff Denworth assigned Mordechai Blaunstein to lead investigation and coordination for RFE 0482 and to bring in additional parties as needed.
