---
type: people
title: Director Hampson
created: '2026-01-03'
last_contact: '2025-10-29'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Director Hampson

## Profile

**Role**: Director (exact function not stated) at VAST Data
**Relationship**: Internal collaborator

**Background**:
- Committed to share prior customer learnings (e.g., ICE/NYSE evaluation) in Slack; referenced SyncEngine as a gap-closer for moving data in/out of cloud object storage.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Director Hampson")
SORT due ASC
```

## Recent Context

- 2025-10-29: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]] - Group meeting to align positioning and go-to-market for VAST on Cloud, including MVP architecture, m... (via VAST on Cloud Office Hours)

## Key Facts

- VAST on Cloud MVP: 8-node cluster on cloud VMs with local NVMe, deployed per customer tenant; positioned as lift-and-shift for performance.
- Differentiator: global namespace enabling data mobility across on-prem, public cloud, and NeoClouds.
- Marketplace automation starts with GCP; Azure and AWS targeted within ~3 months.
- AWS current supported VM shapes ~120TB; estimated VM cost ~$0.20/GB-month; roughly ~20x on-prem hardware cost.
- Azure current VM shape ~23TB; Microsoft discussing ~300TB VM shapes targeting late next year.
- Better cloud TCO path: integrate cloud object storage (e.g., S3) in future releases; SyncEngine mentioned for object moves.
- Pushing AWS for FSx first-party program to unlock better economics and shapes.
- Cloud engineering headcount grew from ~5 to ~25, increasing roadmap velocity.
- Marketplace private offers (once GA/transactable) will burn down customer cloud commits.
- NeoCloud contractual constraints (example: CoreWeave) may restrict enabling global namespace/data movement; dedicated environments may be required for some large projects.

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Use Slack channel as the primary route for VAST on Cloud deals and support (Tiffany: AWS/Azure; Olivia: GCP/OCI).
- ✅ Lead with global namespace to enable data to move to compute across on-prem, cloud, and NeoClouds.
- ✅ Proceed with marketplace-based deployment and private offers to enable commit burn-down and smoother fulfillment.
- ✅ Showcase VAST on Cloud demos at Supercomputing to drive awareness and pipeline.

## Related Projects

- [[Cloud]]

## Related

---
*Last updated: *
