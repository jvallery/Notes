---
type: people
title: Intro 1:1 on VAST on Cloud
date: '2025-10-31'
person: Josh Wentzell
participants:
- Jason Vallery
- Josh Wentzell
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-31 - Introductory 1-1 focused on VAST
  on Cloud strategy and current platform gaps. Jo.md
tags:
- type/people
- person/josh-wentzell
- generated
---

# Intro 1:1 on VAST on Cloud

**Date**: 2025-10-31
**With**: Jason Vallery, Josh Wentzell

## Summary

Introductory 1:1 to align on VAST on Cloud strategy and surface platform gaps. Josh highlighted multi-tenancy API/GUI limitations, VOC deployment friction (lack of preflight/wizard), and automation gaps (Terraform coverage; no official Ansible), while noting strong CSI adoption and rising CoSy interest. Jason shared 12-month priorities around cloud marketplace offers, improving price/performance via cloud primitives/possible ODM hardware, and enabling multi-cloud data spaces for durable global access and efficient data-to-GPU mobility.
## Action Items
- [?] Spin up OVA in home lab and/or loopback instance to get hands-on with VAST @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Review flight school materials and attend Tech Summit @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Engage with Rob Gerard to align on CSI/CoSy status and roadmap @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Connect with Carl on VAST on Cloud deployment nuances @Myself 📅 2025-11-08 🔽 #task #proposed
- [?] Share additional learning links/docs as needed (loopback link sent) @Josh Wentzell 📅 2025-11-08 🔽 #task #proposed
- [?] Confirm Jason received and used the loopback link; share any additional setup tips @Josh Wentzell 📅 2025-11-08 🔽 #task #proposed
- [?] Report initial findings from OVA hands-on and list of VOC pain points @Myself 📅 2025-11-08 ⏫ #task #proposed
- [?] Share marketplace offer plan and timelines across AWS/Azure/GCP with stakeholders @Myself 📅 2025-11-08 ⏫ #task #proposed

## Key Information
- Josh Wentzell focuses on automation/DevOps and lab tooling; he is often customer-facing for API automation and previously handled AWS VOC discussions before Carl joined.
- Multi-tenancy gaps include unclear tenant-scoped APIs, tenant admins lacking needed privileges, and limited tenant visibility (e.g., VIP pool selection/filters).
- VOC deployment is not streamlined; it lacks preflight checks and a guided wizard, leading to failures late in the process.
- Large customers prefer Terraform/Ansible; Terraform provider lacks endpoint coverage, forcing REST fallbacks and causing state-management pain.
- There is no official Ansible module; a beta exists but is not maintained; the Do team prioritizes Terraform provider maturity.
- CSI adoption is common; CoSy requests have increased in the last 2–3 months; Rob Gerard manages CSI/CoSy.
- Customers often build internal front-ends for buckets, policies, and S3 key rotation to enforce approvals and guardrails.
- Loopback OVA can be spun up via AWX/Cosmodrome in OCI; Josh sent the link.

---

*Source: [[Inbox/_archive/2025-10-31/2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo.md|2025-10-31 - Introductory 1-1 focused on VAST on Cloud strategy and current platform gaps. Jo]]*

## Related

- [[Josh Wentzell]]
- [[Jason Vallery]]
- [[Rob Gerard]]
- [[Seth Haynes]]
- [[Andy Perlsteiner]]
- [[Jeff Denworth]]
- [[VIP]]
- [[OVA]]
- [[Microsoft Azure Engagement Plan]]
- [[Microsoft]]
- [[Amazon]]
- [[Google]]
- [[Oracle]]
- [[Toshiba]]
- [[Databricks]]
- [[Micron]]
- [[Shopify]]
- [[Tesla]]
- [[CoreWeave]]
- [[Samsung]]
- [[HPE]]
- [[Cisco]]
- [[Snowflake]]
- [[Seagate]]