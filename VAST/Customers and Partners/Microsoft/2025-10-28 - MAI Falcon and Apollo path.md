---
type: customer
title: MAI Falcon and Apollo path
date: '2025-10-28'
account: Microsoft
participants:
- Jason Vallery
- Alon Horev
- Kushal
- Vipin
- Lior Genzel
- Tiffany Stonehill
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-28 - Discussed Microsoft AI (MAI) landscape,
  Falcon capacity rollout, and Azure dynam.md
tags:
- type/customer
- account/microsoft
- generated
---

# MAI Falcon and Apollo path

**Date**: 2025-10-28
**Account**: [[Microsoft]]
**Attendees**: Jason Vallery, Alon Horev, Kushal, Vipin, Lior Genzel, Tiffany Stonehill

## Summary

Jason and Alon aligned ahead of Jason’s Friday meeting with Kushal (MAI) on deploying VAST outside Azure data centers, using MAI’s Falcon capacity challenges as a wedge. They discussed Project Apollo (AKS-led slim control plane for single-tenant GPU sites) as the most promising entry path, plus longer-term Azure hardware qualification and optional Blob compatibility exploration while keeping near-term focus on performance to keep GPUs utilized.
## Action Items
- [ ?] Meet Kushal (MAI) to discuss VAST deployment options outside Azure data centers and clarify target site and hardware profile @Myself 📅 2025-10-31 🔺 #task #proposed
- [ ?] Send notes to Alon after the Kushal meeting to inform next steps with Vipin @Myself 📅 2025-10-31 ⏫ #task #proposed
- [ ?] Follow up with Vipin after receiving Jason’s notes to align on path and probe AKS/Project Apollo conversations (including whether Vipin spoke with Anson and Keek) @Alon ⏫ #task #proposed
- [ ?] Stay close with Lior and Tiffany to advance the Project Apollo storage integration option and positioning of VAST as standard storage for Apollo deployments @Myself ⏫ #task #proposed
- [ ?] Map Azure stakeholders (AKS/Apollo, Storage, Compute, Hardware) and their priorities to navigate internal incentives and resistance @Myself ⏫ #task #proposed
- [ ?] Engage Azure Hardware (Ronnie Booker’s team) on qualifying a VAST-friendly storage-optimized SKU (including liquid-cooled options) @Myself 🔽 #task #proposed
- [ ?] Explore liquid-cooled storage SKU options with ODMs to leverage data center cooling fungibility and late-binding storage vs GPU rack decisions @Myself 🔽 #task #proposed
- [ ?] Evaluate Blob compatibility and a multi-protocol (Blob + S3) head; test interest with Azure contacts while keeping near-term focus on performance wins @Myself 🔽 #task #proposed
- [ ?] Confirm whether the Microsoft–Nscale contract maps to MAI and assess implications for a potential VAST deployment @Myself 🔽 #task #proposed

## Decisions
- Wait until the Friday Kushal meeting before Alon follows up with Vipin.
- Prioritize Project Apollo as the first entry path over Azure Marketplace VM offers.
- Use MAI success as a wedge to influence broader Azure storage strategy and hardware qualification.
- Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.

## Key Information
- Kushal (ex-Inflection, now in MAI under Mustafa) scheduled a Friday meeting with Jason about using VAST outside Azure data centers.
- MAI Falcon plan spans Phoenix, Dallas, and Richmond with ~40k GPUs per site connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI is struggling to utilize Falcon capacity due to control plane fragility and GPU issues.
- OpenAI GPT-4.5 training reportedly took ~9 months across multi-islands (up to ~100k H100s) and was disappointing, shifting philosophy away from ever-bigger clusters.
- MAI is exploring online RL continuous learning with a tight (~60s) trainer/generator loop.
- Vipin values VAST features (global namespace, quotas, capacity estimation, QoS) and acknowledges Blob cannot match VAST performance.
- Microsoft reportedly closed a large contract with Nscale; end customer not disclosed.
- Project Apollo is an AKS-led effort to create a slim control plane for single-tenant GPU sites without full Azure region overhead; Azure Storage lacks a deployable solution for Apollo-like sites today.
- Azure Marketplace VM offers (e.g., Lsv4/v5) are not price-performance competitive for VAST at scale.
- Azure Compute leadership incentives may resist third-party storage adoption; hardware qualification via Azure Hardware is likely multi-year.
- Blob API is Microsoft-specific; S3 compatibility is broadly attractive; multi-protocol (Blob + S3) could broaden appeal but faces control plane integration hurdles.

---

*Source: [[Inbox/_archive/2025-10-28/2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam.md|2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]]*

## Related

- [[CoreWeave]]
- [[Seth Haynes]]
- [[David Holz]]
- [[John Mao]]
- [[Sam Altman]]
- [[Lior Genzel]]
- [[Tiffany Stonehill]]
- [[Kushal Datta]]
- [[Vipin Sachdeva]]
- [[Maneesh Sah]]
- [[Ronnie Booker]]
- [[Alon Horev]]
- [[Jason Vallery]]
- [[Cloud control plane]]