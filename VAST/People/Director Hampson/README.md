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

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Director (exact function not stated) |
| **Company** | VAST Data |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

_Career history, expertise, interests, personal details shared..._


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Director Hampson")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@DirectorHampson") AND !completed
SORT due ASC
```

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

## Topics Discussed

VAST on Cloud positioning and talk track (global namespace, data-to-compute), MVP architecture (8-node VM/NVMe cluster per tenant) and deployment mechanics, Marketplace rollout and private offers; commit burn-down, Hyperscaler dependencies: VM shapes, AWS FSx first-party path, Object storage integration roadmap (S3) and SyncEngine, Handling multi-PB opportunities and expectation setting (Visa ~20PB), Customer learnings from ICE/NYSE evaluation (burst to AWS vs on-prem), Genomics pipeline use case (~100TB ephemeral) and POC/fulfillment mechanics, Tenant-level peering / multi-tenancy constraints and NeoCloud contracts, Supercomputing demos and field enablement

## Recent Context

- 2025-10-29: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]] - Group meeting to align positioning and go-to-market for VAST on Cloud, including MVP architecture, m... (via VAST on Cloud Office Hours)

## Profile

**Role**: Director (exact function not stated) at VAST Data
**Relationship**: Internal collaborator

**Background**:
- Committed to share prior customer learnings (e.g., ICE/NYSE evaluation) in Slack; referenced SyncEngine as a gap-closer for moving data in/out of cloud object storage.

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