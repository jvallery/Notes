---
type: customer
title: Two-track VAST evaluation plan
date: '2025-10-31'
account: Microsoft
participants:
- Qingying Zhang
- Yanzhao
- Jason Wilder
- Wendy
- Anson
- Paula
- Jovane
- Lior Genzel
- Jason Vallery
- Ray
- Paul Haddo
- Andy Prentice
- Alon
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-31 - Teams aligned on a two-track evaluation
  for Apollo’s AI cloud storage (A) valid.md
tags:
- type/customer
- account/microsoft
- generated
---

# Two-track VAST evaluation plan

**Date**: 2025-10-31
**Account**: [[Microsoft]]
**Attendees**: Qingying Zhang, Yanzhao, Jason Wilder, Wendy, Anson, Paula, Jovane, Lior Genzel, Jason Vallery, Ray, Paul Haddo, Andy Prentice, Alon

## Summary

Microsoft’s Apollo team and VAST aligned on a two-track evaluation: (A) validate VAST software on Azure-native lab hardware and (B) run a VAST loaner-hardware POC in Microsoft’s Stargate lab and/or via Azure Dedicated. Key blockers are unclear KPI targets and potential delays/constraints for hosting third-party hardware, while the timeline targets a Sep–Nov 2026 launch and an initial 30–40MW data center scaling toward ~400k GPUs.
## Action Items
- [ ] Share VAST rack/server specifications (C-nodes, D-box/D-node, network uplinks) and estimated costs sized for ~400k GPUs and a 30–40MW initial site @Lior 📅 2025-11-08 🔺 #task
- [ ] Send latest VAST hardware specs including AMD Turin-based updates and DPU details @Ray 📅 2025-11-08 🔺 #task
- [ ] Provide proposed Azure lab hardware SKUs/specs (e.g., Gen9 storage pod with BlueField-3 DPU) for software-only POC @Yanzhao 📅 2025-11-08 🔺 #task
- [ ] Confirm Stargate lab can host the POC (rack space, ~30kW power, air cooling, standard rack size, 400GbE uplinks, RoCE/RDMA) @Yanzhao 📅 2025-11-08 🔺 #task
- [ ] Provide POC power specs, rack size, connector types, and network uplink requirements @Ray 📅 2025-11-08 🔺 #task
- [ ] Ship minimal VAST POC kit (≈3 C-nodes, 1 D-box; optionally preconfigured) to Microsoft Stargate lab @Ray 📅 2025-11-08 🔺 #task
- [ ] Share evaluation license and installation/operations guide for deploying VAST on Azure lab hardware @Lior 📅 2025-11-08 🔺 #task
- [ ] Engage Anand Ramakrishna to scope an Azure Dedicated path for earlier access to VAST hardware POC @Qingying Zhang 📅 2025-11-08 ⏫ #task
- [ ] Coordinate with Anand’s team from VAST side to align on Azure Dedicated POC logistics and timing @Lior 📅 2025-11-08 ⏫ #task
- [ ] Research precise KPI targets from NVIDIA to build sizing slide; work with John Mao on per-GPU bandwidth, aggregate throughput, and capacity assumptions @Myself 📅 2025-11-08 🔺 #task
- [ ] Validate lab network configuration supports RoCE/RDMA (SP3/SP4) and VLAN/SDN requirements for single-tenant POC @Jason 📅 2025-11-08 ⏫ #task
- [ ] Share VAST reference design slides and materials discussed on the call @Lior 📅 2025-11-08 🔽 #task
- [ ] Arrange Ignite introductions (VAST CEO with Brendan Burns and Microsoft leadership) and confirm scheduling @Qingying Zhang 📅 2025-11-08 🔽 #task
- [ ] Clarify DPU programming interfaces (current DOCA/NVMe-oF usage) and compatibility considerations with DASH API @Alon 📅 2025-11-08 ⏫ #task
- [ ] Confirm minimal POC BOM and any switch requirements if not using VAST-provided switching @Ray 📅 2025-11-08 ⏫ #task
- [ ] Confirm whether VAST hardware POC will run in Microsoft lab and/or Azure Dedicated, and share expected timeline @Lior 📅 2025-11-08 ⏫ #task

## Decisions
- Proceed with a two-track evaluation: (A) VAST software on Azure lab hardware and (B) VAST loaner-hardware POC in Microsoft lab and/or Azure Dedicated.
- Initial deployment model will be single-tenant, with SDN designed in from day one for future multi-tenancy.
- POC will use RoCE/RDMA networking and require 400GbE uplinks if VAST switches are not used.
- Baseline POC footprint is ~3 C-nodes plus 1 D-box (dual BlueFields), expandable as needed.
- Defer Azure Lsv4 for performance benchmarking; consider VAST-optimized hardware and/or Azure Dedicated instead.

## Key Information
- Apollo is a new AI cloud separate from Azure, built on Linux and Kubernetes.
- Target maturity scale is ~100k nodes (~400k GPUs); first data center target is 30–40MW.
- Target launch timeframe is Sep–Nov 2026.
- Evaluation will compare VAST against alternatives (e.g., Lustre, Azure Storage) on the same hardware where possible.
- VAST architecture uses C-nodes (compute/protocol/erasure coding) and D-nodes/D-boxes (flash with DPUs, no x86 CPUs).
- D-nodes use BlueField-3 DPUs; NVMe-oF target via NVIDIA DOCA; SPDK on ARM is an alternative.
- Example rack power envelope is ~27kW including switching.
- Minimal resilient POC requires ~3 C-nodes, 1 D-box, and a pair of switches; requires RoCE/RDMA and 400GbE uplinks.
- Azure flash density and current VM shapes may limit perf/W and perf/PB versus VAST-optimized gear.
- VAST can ship loaner hardware within days and can preconfigure the POC kit.
- Throughput/KPI requirements are not finalized; Apollo will follow up with precise numbers.
- Anand Ramakrishna’s Azure Dedicated path may accelerate access to run VAST hardware POC (referenced as similar to UK Met Office engagement).

---

*Source: [[Inbox/Transcripts/2025-10-31 - Teams aligned on a two-track evaluation for Apollo’s AI cloud storage (A) valid.md|2025-10-31 - Teams aligned on a two-track evaluation for Apollo’s AI cloud storage (A) valid]]*

## Related

- [[Lior Genzel]]
- [[Jason Vallery]]
- [[Brendan Burns]]
- [[John Mao]]
