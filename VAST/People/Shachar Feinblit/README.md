---
type: people
title: Shachar Feinblit
last_contact: unknown
created: '2026-01-03'
tags:
- type/people
- generated
---

# Shachar Feinblit

## Recent Context

- 2025-10-28: [[Sources/Transcripts/2025/2025-10-28 - Jason and Shachar aligned on setting a weekly 30-minute 11 and planning Jason’s.md|Jason and Shachar aligned on setting a weekly 30-minute 11 and planning Jason’s]] — Jason and Shachar aligned on setting a weekly 30-minute 1:1 and planning Jason’s Tel Aviv visit (Nov...

- unknown: [[Sources/Transcripts/2025/2025-10 - Shachar Feinblit.md|Shachar Feinblit]] — - [x] Ask Shachar to confirm AI-first development mandate, training cadence, and measurable adoption...

- unknown: [[2025-11-4 - Planning sessions]] - Planning notes for a set of sessions with Jeff Denworth to align on VAST’s cloud-first product strat... (via Jeff Denworth)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Shachar Feinblit]] - Checklist and Slack snippets related to coordinating with Shachar Feinblit, including setting up rec...
- unknown: [[_Open Topics]] - Open topics note for Shachar Feinblit, listing key internal Slack contacts by functional area (suppo...
- 2026-01-03: [[2026-01-03 - Prep for Microsoft AI talks]] - Jonsi Stephenson and Jason Vallery aligned messaging and strategy for upcoming Microsoft AI discussi... (via Jonsi Stephenson)
- 2025-11-07: [[2025-11-07 - We reviewed the org landscape and aligned on my near-term focus. Jeff outlined k]] - 1:1 with Jeff Denworth to review the org landscape, clarify key stakeholders, and align on the autho... (via Jeff Denworth)
- 2025-11-06: [[2025-11-06 - Internal prep to shape an architecture whiteboarding session with Walmart’s Lake]] - Internal prep for an in-person architecture whiteboarding session with Walmart’s Lakehouse team to d... (via Walmart)
- 2025-11-03: [[2025-11-03 - Team reviewed the updated 5.5 plan feature freeze next week, beta in January, r]] - Group meeting reviewing the VAST 5.5 release plan and scope changes, including timeline (feature fre... (via Phase Gate 1)
- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-30: [[2025-10-30 - Reviewed MAI meeting prep and testing path (prefer hardware; VMs supported in De]] - Weekly 1:1 with Lior Genzel focused on preparing for an upcoming MAI call, defining the near-term te... (via Lior Genzel)
- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h... (via Eyal Traitel)
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m... (via Eyal Traitel)
- 2025-10-29: [[2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga]] - Weekly 1:1 where Liraz Ben Or explained VAST’s non-traditional major release management process (4 p... (via Liraz Ben Or)
- 2025-10-29: [[2025-10-29 - Intro 1-1 where Liraz walked Jason through VAST’s non-traditional release manage]] - Weekly 1:1 intro where Liraz Ben Or walked Jason Vallery through VAST’s non-traditional release mana... (via Liraz Ben Or)

## Profile

**Role**: R&D leader (implied; receives reports from Roy, Dafna, Eyal, Noa) at VAST Data (R&D)
**Location**: Tel Aviv (implied by visit and team location)
**Relationship**: Internal collaborator (engineering leadership)

**Background**:
- Engineering leader perspective: architects write FRDs; wants stronger technical depth and end-to-end product involvement; optimizes for throughput; notes widespread use of Cursor and preference for organic AI enablement.
- Listed as a candidate for weekly/monthly 1:1 cadence (marked '++').
- Point person for confirming AI-first development mandate, training cadence, and adoption targets; involved in organizing Tel-Aviv trip meetings and coordinating team/all-hands participation.

## Key Facts

- Walmart uses Azure for dot-com systems and GCP (BigQuery/GCS) for enterprise analytics.
- Walmart wants a consistent lakehouse view across GCP and two on-prem sites; two on-prem DCs run active-active with >30 ms latency.
- Immediate ask: two VAST clusters (Region 1/Region 2) in Q4 for pilot testing.
- Scale: ~450 PB initially, growing to ~770 PB by 2029.
- Replication target: ~10% of the lake per day from GCP to on-prem; estimated sustained ~5 Tbps; prior discussions included up to ~10 Tbps targets and ~100 PB/month change rate claims.
- Walmart prefers GCS-compatible APIs; S3-only access is not acceptable long-term.
- Near-term architecture direction: SyncEngine for near-real-time replication from GCS plus DataSpaces across on-prem sites; gaps include GCS API endpoint, stronger consistency/write-lease semantics, and GCS change-feed integration.
- Pilot timeline: now through roughly Sep/Oct next year; decision frame for full project in calendar year 2027; budgets finalize end of next calendar year.
- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement/training plus PM augmentation, and marketing support.
- Documentation is currently feature/button-oriented and not scenario-driven; scenario guides are ad hoc and late.

## Topics

Walmart hybrid lakehouse architecture (GCP + two on-prem sites), SyncEngine replication from GCS to on-prem, DataSpaces/global namespace across on-prem sites, GCS API compatibility requirement, Strong consistency challenges and write-lease semantics, Network throughput/egress feasibility for multi-Tbps replication, Pilot/POC scoping using real workloads (Trino/Presto, Spark; Delta/Hudi tables), Governance, multi-tenancy, auditing, and compliance requirements, BigQuery interoperability considerations, Q4 pilot cluster configurations (Region 1/Region 2), Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics

## Key Decisions

- ✅ Use SyncEngine for the pilot to replicate from GCS to on-prem VAST clusters.
- ✅ Pursue GCS API compatibility on the roadmap; S3 alone is insufficient for Walmart.
- ✅ Focus the pilot on real Walmart workloads (tables/queries), not synthetic benchmarks.
- ✅ Consolidate questions and send to Walmart before scheduling the design session.
- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Carl will move to ProServe under Rob rather than supporting customer-facing PM work.
- ✅ Set a monthly touchpoint with Brandon to align on cloud platform priorities.
- ✅ Customer requirement docs and FRDs will be authored and maintained in Confluence.

## Related Projects

- [[AI Pipelines Collateral]]
- [[GCP MVP]]
- [[Cloud]]
- [[5.5 Features]]

## Related

<!-- Wikilinks to related entities -->
