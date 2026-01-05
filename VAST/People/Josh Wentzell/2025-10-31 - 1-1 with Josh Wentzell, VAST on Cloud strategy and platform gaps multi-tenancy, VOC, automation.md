---
type: people
title: 1:1 with Josh Wentzell, VAST on Cloud strategy and platform gaps (multi-tenancy, VOC, automation)
date: '2025-10-31'
person: Josh Wentzell
participants:
- Jason Vallery
- Josh Wentzell
- Andy Perlsteiner
- Jeff Denworth
- Carl (last name unknown)
- Rob Gerard
- Yancey (last name unknown)
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo.md
tags:
- type/people
- generated
---

# 1:1 with Josh Wentzell, VAST on Cloud strategy and platform gaps (multi-tenancy, VOC, automation)

**Date**: 2025-10-31
**With**: Jason Vallery, Josh Wentzell

## Summary

Jason Vallery and Josh Wentzell held an introductory 1:1 focused on VAST on Cloud strategy and current platform gaps. Josh described multi-tenancy API/GUI limitations, VOC deployment friction (lack of preflight checks and guided workflow), and automation tooling gaps (Terraform coverage gaps and no maintained official Ansible). Jason shared 12-month priorities including cloud marketplace offers, improving price/performance using cloud primitives and potential ODM hardware in CSP data centers, and enabling multi-cloud data spaces for durable, globally distributed access to large data lakes and GPUs.

## Action Items

- [?] Spin up the VAST loopback OVA (home lab and/or loopback instance) to get hands-on with VAST on Cloud deployment and workflows. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review VAST flight school materials and attend Tech Summit to accelerate hands-on understanding of VAST on Cloud and platform gaps. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share additional learning links and documentation for VAST on Cloud and loopback OVA setup as needed (loopback link already sent). @Josh Wentzell 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Engage with Rob Gerard to align on CSI and CoSy adoption patterns, current gaps, and roadmap ownership for CSI/CoSy. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect with Carl to understand VAST on Cloud (VOC) deployment nuances and current customer friction points. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define and implement tenant admin capabilities and tenant-scoped visibility, including VIP pool visibility and selection, and clarify tenant-scoped APIs for multi-tenancy. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Add VOC deployment preflight checks and a guided deployment wizard to reduce late-stage failures during VAST on Cloud deployments. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Expand the Terraform provider to cover missing endpoints so customers do not need to fall back to direct REST API calls that create state-management issues. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Evaluate plan and resourcing for an official Ansible collection once Terraform provider maturity reaches acceptable parity for customer automation needs. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Confirm receipt and usability of the loopback OVA link and share any additional setup tips if Jason hits issues. @Josh Wentzell 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Report initial findings from hands-on OVA usage, including a concrete list of VOC deployment pain points and multi-tenancy gaps observed. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide a timeline for Terraform provider parity and a decision on whether VAST will fund and own an official Ansible module/collection. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Share the marketplace offer plan across AWS, Azure, and GCP with stakeholders, including how price/performance will be addressed using cloud primitives and potential ODM hardware in CSP data centers. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Spin up the VAST loopback OVA in a home lab and/or loopback instance to get hands-on with VAST on Cloud. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review VAST flight school materials and attend Tech Summit to accelerate hands-on learning and alignment. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Engage with Rob Gerard to align on CSI and CoSy status, adoption patterns, and roadmap implications for VAST on Cloud. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect with Carl (last name unknown) to understand VAST on Cloud (VOC) deployment nuances and current customer friction points. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define and implement tenant admin capabilities and tenant-scoped visibility, including tenant-scoped APIs and visibility into VIP pools, to support a true SaaS multi-tenant VAST on Cloud model. @TBD 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Evaluate plan and resourcing for an official Ansible collection after Terraform provider maturity stabilizes. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] Report initial findings from hands-on loopback OVA usage, including a concrete list of VOC deployment pain points and multi-tenancy gaps observed. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share the cloud marketplace offer plan across AWS, Azure, and GCP with stakeholders, including how VAST will address price/performance concerns in marketplace VM shapes. @Myself 📅 2025-11-08 #task #proposed #auto

## Key Information

- Josh Wentzell focuses on automation/DevOps and lab tooling at VAST Data, including customer-facing API automation workflows and internal tools for SE demos and lab environment management.

- Josh Wentzell previously handled most AWS VAST on Cloud (VOC) discussions until Carl joined, after which Josh reduced involvement in VOC customer discussions.

- VAST Data lab hardware is not owned by VAST; it is provided on a burn-in period from manufacturers, requiring coordination with ops teams for system rotation.

- VAST Data multi-tenancy is currently not intuitive for tenant-scoped API usage, and documentation and APIs for multi-tenancy need improvement to support a true SaaS multi-tenant model.

- Tenant admin capabilities in VAST Data have gaps versus cluster admin privileges, creating operational friction because tenant admins still need cluster admin intervention for tasks that should be tenant-scoped.

- Tenant-scoped visibility is limited in the VAST Data GUI and APIs, including difficulty seeing which VIP pools are available to a tenant and lack of filtering/selection controls.

- VOC deployment is not streamlined and lacks preflight checks and a guided wizard, which can cause failures late in the deployment process.

- Large customers prefer Terraform and Ansible for automation; when Terraform provider coverage is incomplete, customers fall back to direct REST API calls, which creates state-management pain.

- VAST Data does not have an official maintained Ansible module/collection; a beta exists but is not maintained, and the Do team prioritizes Terraform provider maturity first.

- CSI adoption is common among VAST Data customers, and interest in CoSy has increased recently; Rob Gerard manages CSI and CoSy.

- Customers often build internal front-ends for buckets, policies, and S3 key rotation to enforce approvals and guardrails when using VAST Data.

- Jason Vallery stated his 12-month focus is to deliver cloud marketplace offers across hyperscalers, improve price/performance using cloud primitives and potential ODM hardware in CSP data centers, and enable multi-region and multi-cloud data spaces for durable global access and efficient data mobility to GPUs.

- Josh Wentzell shared a loopback OVA link and noted it can be spun up via AWX/Cosmodrome in OCI for hands-on testing.

---

- Josh Wentzell focuses on automation/DevOps and lab tooling at VAST Data, including customer-facing API automation workflows and internal dev tools for SE enablement.

- Josh Wentzell previously handled most AWS VAST on Cloud (VOC) discussions until Carl (last name unknown) joined, after which Josh reduced involvement in VOC discussions.

- VAST Data lab hardware is not owned by VAST; it is provided during a burn-in period from manufacturers, requiring coordination with ops teams for system rotation.

- Multi-tenancy in VAST has API and documentation gaps, including unclear tenant-scoped API usage and non-intuitive behavior when making API calls against a tenant context.

- Tenant admin capabilities in VAST are incomplete relative to cluster admin, forcing tenant admins to rely on cluster admins for tasks that should be tenant-scoped in a SaaS multi-tenant model.

- Tenant visibility gaps include limited ability for a tenant admin to see or filter available VIP pools for their tenant.

- VAST does not have a maintained official Ansible module; a beta exists but is not maintained, and the team prioritizes Terraform provider maturity first.

- CSI adoption is common among VAST customers, and interest in CoSy has increased recently; Rob Gerard manages CSI and CoSy.

- Customers often build internal front-ends for buckets, policies, and S3 key rotation to enforce approvals and guardrails on top of VAST.

- Jason Vallery joined VAST Data in late October 2025, reports to Jeff Denworth, and is responsible for making VAST on Cloud successful with a vision toward fully managed SaaS multi-tenancy across hyperscalers.

- Jason Vallery previously worked at Microsoft for 13 years running Microsoft object storage.

- Josh Wentzell shared a loopback OVA link for hands-on work; the loopback OVA can be spun up via AWX or Cosmodrome in Oracle Cloud Infrastructure (OCI).
