---
type: people
title: Tiffany Stonehill
created: '2026-01-03'
last_contact: '2025-10-29'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Tiffany Stonehill

## Profile

**Role**: Cloud field lead for AWS and Azure (exact title not stated) at VAST Data (Cloud / Field)
**Relationship**: Internal collaborator

**Background**:
- At VAST ~1.5 years; previously covered OCI; now covers Azure and AWS; helps route field opportunities and adds people to Slack channel; involved with product marketing on talk tracks/battle cards.
- Owns AWS/Azure field engagement for VAST on Cloud; coordinating intake via Slack; working with product marketing on positioning/battle cards/talk tracks; covering Supercomputing and Ignite.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Tiffany Stonehill")
SORT due ASC
```

## Recent Context

- 2025-10-29: [[2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g]] - Group office hours aligned the team on positioning and operating mechanics for VAST on Cloud, emphas... (via VAST on Cloud Office Hours)
- 2025-10-29: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]] - Group meeting to align positioning and go-to-market for VAST on Cloud, including MVP architecture, m... (via VAST on Cloud Office Hours)
- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)

## Key Facts

- MAI Falcon plan includes Phoenix, Dallas, and Richmond sites (~40k GPUs per site) connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI struggles to use Falcon capacity due to control plane fragility and GPU issues.
- OpenAI GPT-4.5 training reportedly took ~9 months across multi-islands and up to ~100k H100s; outcome described as disappointing, shifting away from ever-bigger clusters.
- MAI is exploring online RL continuous learning loops with ~60s feedback cycles (trainers in Phoenix, generators elsewhere).
- Vipin values VAST features (global namespace, quotas, capacity estimation, QoS) and acknowledges Blob cannot match VAST performance.
- Marketplace VM offers (Lsv4/v5) are not price-performance competitive for VAST at scale; hardware qualification is viewed as the long-term path.
- Azure Hardware qualification for first-party SKUs is a multi-year effort; liquid-cooled storage SKUs could help with data center cooling fungibility and late-binding storage vs GPU rack decisions.
- Blob API is largely Microsoft-specific; S3 compatibility is broadly attractive; multi-protocol (Blob + S3) could broaden appeal but faces Azure control plane integration hurdles.
- Tiffany Stonehill covers AWS and Azure; Olivia Borey covers GCP and OCI.
- Jason Vallery joined as VP of Product Management for Cloud and reports to Jeff Denworth; previously spent 13 years leading Microsoft object storage PM.

## Background

_Career history, expertise, interests, personal details shared..._

## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Use the VAST on Cloud Slack channel as the primary intake for opportunities; Tiffany (AWS/Azure) and Olivia (GCP/OCI) lead engagement.
- ✅ Proceed with MVP 8-node HA VAST on Cloud clusters via marketplace automation (GCP first; Azure/AWS to follow).
- ✅ Actively pursue hyperscaler programs (e.g., AWS FSx) and larger VM shapes to improve cost/performance.
- ✅ Use Slack channel as the primary route for VAST on Cloud deals and support (Tiffany: AWS/Azure; Olivia: GCP/OCI).
- ✅ Lead with global namespace to enable data to move to compute across on-prem, cloud, and NeoClouds.
- ✅ Proceed with marketplace-based deployment and private offers to enable commit burn-down and smoother fulfillment.

## Related Projects

- [[AI Pipelines Collateral]]
- [[Cloud]]

## Related

---
*Last updated: *
