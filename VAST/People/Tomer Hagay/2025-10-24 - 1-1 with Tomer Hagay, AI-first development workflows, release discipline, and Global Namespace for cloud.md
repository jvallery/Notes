---
type: "people"
title: "1:1 with Tomer Hagay, AI-first development workflows, release discipline, and Global Namespace for cloud"
date: "2025-10-24"
person: ""
participants: ["Jason Vallery", "Tomer Hagay"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Tomer Hagay, AI-first development workflows, release discipline, and Global Namespace for cloud

**Date**: 2025-10-24
**With**: Jason Vallery, Tomer Hagay

## Summary

Jason Vallery and Tomer Hagay aligned on the need to codify AI-first software development workflows at VAST Data and raise accountability to reduce chronic release slippage. They reviewed VAST’s RFE-to-feature-to-Jira intake process, customer support model (Tier-3 co-pilots and per-customer Slack channels), and Global Namespace design (strict consistency with read leases today and write leases planned for 5.5 preview). Jason will get hands-on with VAST via OVA or SC lab to test Global Namespace, caching/prefetch, and GPU workflows, and they plan to continue the discussion the following week.


## Action Items


- [?] Ping Josh Wentzell (Office of the CTO) to obtain VAST OVA access and onboarding for local lab testing. @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Coordinate with Andy Perlsteiner to obtain SC lab access as a backup or quick-start environment for testing. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Set up a local cluster using the VAST OVA to test Global Namespace behavior, caching/prefetch, and GPU-related workflows. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Review Google Anywhere Cache documentation and compare its policy and prefetch capabilities to VAST Data Global Namespace caching and prefetch design. @Tomer Hagay 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Ask Shachar to confirm whether VAST Data will mandate AI-first development, including training cadence and measurable adoption targets (KPIs). @Tomer Hagay 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Draft VAST Cloud SaaS operating model requirements, including DevOps or LifeSite rotations, telemetry requirements, and 24x7 support expectations. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Schedule the next 1:1 with Tomer Hagay for the following week to continue the cloud plan and process changes discussion. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Meet with Customer Success (example contact: Rich) to understand VAST Data account support workflows end-to-end. @Myself 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Confirm with Brendan and Jeff Denworth that VAST Cloud is P0 and clarify resourcing expectations for cloud workstreams. @Myself 📅 2025-10-26 ⏫ #task #proposed #auto

- [?] Clarify VAST Data end-to-end development lifecycle (requirements, planning, gates, signoffs, source control, CI/CD, release) with engineering leaders such as Eyal Traitel and Noah Cohen, or via existing documentation. @Myself 📅 2025-10-27 ⏫ #task #proposed #auto

- [?] Review and align on VAST Data write-lease design and read redirection behaviors with the Tel Aviv engineering team for VAST 5.5 preview. @Tomer Hagay 📅 2025-10-27 🔽 #task #proposed #auto

- [?] Proceed with evaluating Slack multi-channel polling capability with IT and report feasibility and timeline. @Tomer Hagay 📅 2025-10-26 🔽 #task #proposed #auto






## Key Information


- VAST Data has approximately 400 software developers.

- VAST Data engineering and release cadence was described as waterfall-like with chronic slips and limited accountability, including VAST release 5.4 slipping from June 2025 to October 2025.

- Microsoft’s internal model for AI-first development was cited as having structured workflows and biweekly forced AI training days for developers.

- VAST Data RFEs are captured in Salesforce, require SE manager approval, are triaged by Jonathan Hayes, then PMs aggregate into Features linked to Jira, and Epics are not consistently used.

- VAST Data support model includes a Tier-3 'co-pilot' per account, a separate customer Slack workspace with per-customer channels, and a vForce team that builds hotfixes.

- VAST Data Global Namespace design targets strict consistency, uses read leases today with cache/prefetch, supports multi-protocol access on satellites (NFS, SMB, S3), and targets write leases for a VAST 5.5 preview.

- VAST Data async replication plus Global Namespace in VAST 5.4 enables active-active read/write access with point-in-time snapshots.

- For VAST Cloud, a lift-and-shift approach was considered unlikely to meet price/performance targets, and the approach discussed was a performant layer over cloud object storage with a region-spanning namespace and caching, using Google multi-region and caching patterns as a reference.

- Jason Vallery planned to obtain VAST OVA access via Josh Wentzell (Office of the CTO) to tinker locally, with SC lab access as an alternative via Andy Perlsteiner.

- Jason Vallery stated that OpenAI publicly claims approximately 95% of their code is written by AI tools, and he used this as a benchmark for AI-driven development transformation.

- Jason Vallery stated that Azure Storage has approximately 1,600 software developers and that Microsoft is actively transforming development workflows with AI tooling and structured processes.



---

*Source: [[2025-10-24 - Jason and Tomer discussed accelerating AI-driven software development practices]]*