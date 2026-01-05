---
date: '2025-12-19'
entity: GCP MVP
participants:
- Myself
- Kamal
- David
- Malikarjan
- Lior Genzel
source: transcript
tags:
- type/projects
title: Performance Benchmarking and Encryption Discussion
type: projects
---

## Summary

The meeting focused on discussing performance benchmarking parameters, encryption strategies, and hardware configurations for the GCP MVP project. Key topics included the use of dual software layer encryption, the challenges of supporting self-encrypting drives, and the need for benchmarking with specific IOPS and capacity configurations.

## Topics

- Performance benchmarking
- Encryption strategies

## Key Facts

- VAST Data uses dual software layer encryption to meet FIPS requirements. *(about VAST Data)*
- VAST Data's hardware is primarily sourced from Supermicro. *(about VAST Data)*

## Decisions

- VAST Data will use dual software layer encryption instead of self-encrypting drives.

## Action Items

- [ ] Share the benchmarking process and tools used by VAST Data. @Myself 🔼 #task
- [ ] Follow up on the possibility of supporting multiple encryption keys per bucket. @Myself 🔼 #task
- [ ] Provide a one-pager on VAST's encryption strategy and FIPS compliance. @Myself 🔼 #task

## Follow-ups

- [ ] Review the latest notes sent by David. @Myself 🔼 #task #followup
- [ ] Plan a security deep dive session. @Myself 🔼 #task #followup

## Related

- [[Kamal]]
- [[David]]
- [[Malikarjan]]
- [[Lior Genzel]]
- [[Supermicro]]
- [[GCP MVP]]
