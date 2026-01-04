---
type: customer
title: Crusoe
created: '2026-01-03'
last_contact: '2025-10-06'
status: active
auto_created: true
tags:
- type/customer
- needs-review
- status/active
---

# Crusoe

## Account Overview

_Brief description of this customer, their business, and relationship..._

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | _Unknown_ |

## Key Contacts

_No key contacts identified._

## Active Projects

_What projects/initiatives are active with this customer?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Current Blockers

- ❌ Short decision timeline (Wednesday deadline)

## Next Steps

_What are the immediate next actions for this account?_


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```


## Opportunities

- Employment offer to Jason with deadline Wednesday

## Key Decisions

- ✅ Do not pursue a Microsoft counteroffer given compensation constraints and unclear scope.
- ✅ Proceed toward a decision between VAST and Crusoe with intent to resign by Wednesday.

## Key Facts

- Jason has a VAST offer with complex, highly variable compensation tied to OpenAI/Azure sales plus equity.
- Crusoe offer deadline is Wednesday; VAST has not set a decision deadline.
- Microsoft cannot approach Crusoe-level compensation; any change would be modest and potentially insulting.
- Apollo scope and responsibilities are unclear, making it hard to define a successful role or path to partner.
- Jason values clear scope, hands-on technical work, and influencing customer deals.
- Jason estimates ~$800k in vested compensation would be forfeited if leaving Microsoft.
- Jason planned to meet Renan (described as VAST CEO) to quantify risk and negotiate equity/commission.
- Jason stated staying at Microsoft is effectively a closed option.

## Topics / Themes

Job offers comparison (VAST vs Crusoe vs Microsoft), Compensation structure risk (commission/equity variability), Apollo program scope ambiguity and execution risk, Career trajectory and path to partner at Microsoft, Resignation timeline

## Recent Context

- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 between Jason Vallery and Jai Menon discussing Jason’s competing offers from VAST and Cru... (via Jai Menon)

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related People

- [[Jason Vallery]]
