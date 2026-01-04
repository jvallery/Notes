---
type: customer
title: OpenAI intel from John Mao
date: "2025-12-12"
account: OpenAI
participants:
  - John Mao
source: email
tags:
  - type/customer
  - account/openai
---

# OpenAI Intel from John Mao

**Date**: 2025-12-12

## Summary

John Mao shared valuable intel about OpenAI's internal structure from a close personal friend who recently joined to lead their "Online Data Infrastructure" engineering team.

## Key Intelligence

### Organization Structure

OpenAI is organized into three major teams:

1. **Applications** - ChatGPT, etc. Deals with "online data". John's friend sits here.
   - Two largest platforms: Rockset (vector database, persists to Azure Blob) and Snowflake (one of largest SNOW customers)
2. **Scaling** - Sits between Applications and Research teams. Not a Platform team per se.

3. **Research** - Data scientists reporting to Jakob Pachoki. "Offline" data used for training GPT on large frontier supercomputing clusters in OCI etc.

### Technical Details

- **Rockset** is their vector database - SQL-based, stores entire history of conversations, persists to Azure Blob
- Uses local SSDs with persistence to Azure Blob
- OpenAI is "not as N.I.H." as Instagram/Facebook/Twilio - good for vendor engagement

### Organizational Intel

- Ben Ries reports to John's friend, who reports to Venkat
- Talks of integrating Applications datasets with Research datasets

## Action Items

- [ ] John flying to SF in New Year to visit and open engineering dialogue 🔽
- [ ] Keep relationship engineering-centered per John's request
- [ ] Ask John for any specific info we need - he'll openly share

## Follow-up Contacts

- [[John Mao]] - internal VAST contact
