---
type: "people"
title: "Encryption and Performance Discussion"
date: "2025-12-19"
person: "Jason Vallery"
participants: ["Jason", "Kamal", "David", "Lior", "Malikarjan"]
source: "transcript"
source_ref: "Inbox/_archive/2025-12-19/original.md"
tags:
  - "type/people"
  - "person/jason-vallery"
  - "generated"
---

# Encryption and Performance Discussion

**Date**: 2025-12-19
**With**: Jason, Kamal, David, Lior, Malikarjan

## Summary

The meeting focused on discussing encryption strategies and performance benchmarking for storage systems. Jason confirmed that VAST does not support self-encrypting drives but uses dual software layer encryption to meet FIPS requirements. The team also discussed performance metrics and configurations for different storage scenarios.
## Action Items
- [ ] Share the benchmarking process used by VAST. @Jason #task
- [ ] Provide a one-pager on VAST's encryption approach and FIPS certification. @Jason #task
- [ ] Send a copy of the meeting notes to the team. @David #task

## Decisions
- VAST will not implement self-encrypting drive support due to architectural challenges.
- Encryption will be handled at the software level to meet FIPS requirements.

## Key Information
- VAST uses dual software layer encryption instead of self-encrypting drives.
- Performance benchmarking will focus on IOPS per GB and pricing for different configurations.

---

*Source: [[Inbox/_archive/2025-12-19/original.md|original]]*

## Related

- [[Jason Vallery]]
- [[David Holz]]
- [[Lior Genzel]]
- [[VAST]]
