---
type: people
title: Eyal Traitel
last_contact: "2025-10-29"
created: '2026-01-03'
tags:
- type/people
- generated
---

# Eyal Traitel

## Profile

**Role**: Program manager at VAST Data (Release planning)
**Location**: Tel Aviv
**Relationship**: Internal collaborator (release planning)

**Background**:
- Release planning perspective: minor releases caused churn; 5.6 GA around July; 5.5 missed cloud-critical items; auth providers limited (~8) and config not tenant-scoped.
- Referenced as a program manager to sync with.
- Joined VAST in Dec 2024; focuses on planning minor releases; works closely with release managers and with vForce/service pack teams; involved in planning discussions with control plane (Polaris/Iceland) and cluster teams for VAST on Cloud.

## Open Tasks

- [ ] Create unified backlog with RICE scoring and define Cloud Design Qualifiers required for 5.6; decide P0 vs P1 scope without slipping GA.
- [ ] Publish release discipline and support/EOL policy (freeze windows, gates, deal-override policy and RAPID table).

## Recent Context

- 2025-10-29: [[Sources/Transcripts/2025/2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i.md|Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] — Jason and Eyal discussed VAST’s release intake, planning, and execution model, including how majors,...
- 2025-10-29: [[Sources/Transcripts/2025/2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf.md|Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] — Jason and Eyal aligned on how VAST plans and executes major/minor releases, hotfixes, and service pa...
- 2025-10-29: [[2025-10-29 - Jason and Eyal aligned on how VAST plans and executes majorminor releases, hotf]] - Jason Vallery and Eyal Traitel aligned on VAST’s release planning/execution (major/minor releases, h...
- 2025-10-29: [[2025-10-29 - Jason and Eyal discussed VAST’s release intake, planning, and execution model, i]] - 1:1 between Jason Vallery and Eyal Traitel covering VAST’s release intake, planning, and execution m...
- 2025-10-29: [[2025-10-29 - Liraz walked Jason through VAST’s non-traditional release management 4 phase ga]] - Weekly 1:1 where Liraz Ben Or explained VAST’s non-traditional major release management process (4 p... (via Liraz Ben Or)
- 2025-10-29: [[2025-10-29 - Intro 1-1 where Liraz walked Jason through VAST’s non-traditional release manage]] - Weekly 1:1 intro where Liraz Ben Or walked Jason Vallery through VAST’s non-traditional release mana... (via Liraz Ben Or)
- 2025-10-29: [[2025-10-29 - Jason and Tomer aligned on shifting cloud work toward a PM-led model and the nee]] - 1:1 between Jason Vallery and Tomer Hagay aligning on shifting cloud work to a PM-led model, introdu... (via Tomer Hagay)
- 2025-10-28: [[2025-10-28 - Jason and Shachar aligned on setting a weekly 30-minute 11 and planning Jason’s]] - Weekly 30-minute 1:1 cadence was established between Jason Vallery and Shachar Feinblit, and they pl... (via Shachar Feinblit)
- 2025-10-27: [[2025-10-27 - Jason and Jeff aligned on near-term focus synthesize a cloud pipeline view and]] - Weekly 1:1 between Jason Vallery and Jeff Denworth aligning near-term cloud priorities: build a synt... (via Jeff Denworth)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on accelerating AI-first software developme... (via Tomer Hagay)
- 2025-10-24: [[2025-10-24 - Jason and Tomer discussed accelerating VAST’s engineering maturity and cloud str]] - Weekly 1:1 between Jason Vallery and Tomer Hagay focused on improving VAST engineering maturity and ... (via Tomer Hagay)
- unknown: [[Sources/Transcripts/2025/2025-10 - Eyal Traitel.md|Eyal Traitel]]
- unknown: [[2025-11-4 - Planning sessions]] - Planning notes for a set of sessions with Jeff Denworth to align on VAST’s cloud-first product strat... (via Jeff Denworth)
- unknown: [[2025-10 - Noa Cohen]] - A completed action item to introduce Jason Vallery and sync with several program managers, including... (via Noa Cohen)

## Key Facts

- Eyal Traitel joined VAST in Dec 2024; Noa Cohen is a long-tenured VAST employee focusing on major releases while Eyal focuses on minor releases.
- Feature intake channels include leadership/architects, and SE requests filed in Salesforce tied to opportunities and triaged by Tomer Hagay’s team with bi-weekly reviews.
- Release managers run day-to-day execution for major and minor releases; Shelly Martin (Ops) and Liraz Ben Or (R&D) drive phase-gate documentation/process.
- vForce (Roy Sterman) and Dafna’s team manage service packs and hotfixes, including back/forward-porting and ensuring fixes go upstream to minors/majors.
- Minor releases are treated like full releases with regression and performance testing; weekly content/testing reviews.
- Planning is highly dynamic due to frequent urgent customer/field requests (example: Tesla), causing scope churn and parallel streams.
- 5.6 phase gates are underway with target GA in July next year.
- Historical cadence is roughly 2–3 major releases per year.
- Major multi-tenancy blocker: authentication providers limited to 8 and configured at host cluster rather than tenant-scoped; scaling and tenantizing is a large effort.
- Control plane (Polaris/Iceland) is more cloud-native; cluster layer is not yet operating in an agile/SaaS mode.

## Topics

Release planning and execution (major/minor releases), Hotfixes and service packs (backport/forward-port, upgrade alignment), Feature intake and triage process (Salesforce tied to opportunities), Phase-gate process and documentation, QA/regression/performance testing for minor releases, SaaS and multi-tenant readiness, Multi-tenancy gaps (auth providers limit, tenant-scoped auth), Control plane vs cluster responsibilities (Polaris/Iceland vs cluster), Impact of urgent customer requests on scope and resourcing, 5.6 timeline and GA target, Release intake and prioritization (leadership, architects, SE/Salesforce), Major vs minor releases and phase-gate process, Service packs and hotfix process (vForce, upstreaming fixes), Regression/performance testing practices for minors, SaaS agility vs storage reliability constraints

## Key Decisions

- ✅ Do not run an OpenAI alignment session until OpenAI engages.
- ✅ Primary focus is Microsoft while simultaneously investing in a Google TPU strategy.
- ✅ Lior Genzel focuses on hyperscalers and also has sell-to obligations; Mordechai Blaunstein covers second-tier clouds.
- ✅ Pricing/consumption discussion must include Brett.
- ✅ Endorse core-first prioritization (defer opinionated higher-layer services) for FY26.
- ✅ Approve staged crawl-walk-run cloud plan with SLO/error-budget gates.
- ✅ Name single-threaded owner(s) for MAI/Apollo and define success criteria and 90-day attack plan.
- ✅ Approve scope, decision rights (RAPID/DACI), and the ROB cadence; create/maintain a decision log.
- ✅ Approve headcount/budget and recruiting lanes for PM/TPM/Product Ops/Tech Writer/Enablement.
- ✅ Approve initial SLO set, error budgets, and on-call RACI; gate GA on SLO conformance.

## Related Projects

- [[Cloud]]
- [[5.5 Features]]
- [[OVA]]

## Related

<!-- Wikilinks to related entities -->
