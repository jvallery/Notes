---
type: "customer"
title: "OpenAI org and data platforms, intro path via John Mao's friend (Online Data Infrastructure)"
date: "2025-12-12"
account: ""
participants: ["John Mao", "Myself"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-12_160426_5605_Re-OpenAI.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# OpenAI org and data platforms, intro path via John Mao's friend (Online Data Infrastructure)

**Date**: 2025-12-12
**Account**: [[]]
**Attendees**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with a close friend who recently joined OpenAI to lead the Applications org's "Online Data Infrastructure" engineering team. The email outlines OpenAI's major org structure and key data platforms (Rockset, Snowflake, CosmosDB, DAQ, Databricks/Spark), and sets up an engineering-centered relationship with a planned SF visit in early 2026 to open a dialogue with VAST engineering.


## Action Items


- [?] Send John Mao a list of specific information requests/questions to ask his OpenAI friend (Online Data Infrastructure lead) about Rockset, Cosmos DB usage, Snowflake usage, and any planned merge of Applications and Research datasets. @Myself #task #proposed #auto

- [?] Coordinate with VAST engineering leadership to identify the right engineering participants for an engineering-centered dialogue with OpenAI during/after John Mao's San Francisco visit in early 2026. @Myself #task #proposed #auto




## Decisions


- John Mao will keep the OpenAI relationship with his friend engineering-centered and will open a dialogue that brings in VAST engineering during an in-person visit to San Francisco in early 2026.




## Key Information


- John Mao has a close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, not clearly a platform team), and Research (data scientists reporting up to Jakob Pachoki, focused on offline training data).

- Within OpenAI Applications (online data), two large platforms are Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is described as one of Snowflake's largest customers).

- Rockset is described by John Mao's OpenAI contact as OpenAI's "vector database" and the platform (persisted to Azure Blob) that contains the entire history of ChatGPT conversations.

- Jason Vallery stated that the ChatGPT application side heavily leverages Azure Cosmos DB for conversation persistence, and that this is publicly referenced with OpenAI as a major Cosmos DB customer.

- Jason Vallery stated that Rockset is the company OpenAI acquired, founded by the creators of RocksDB (including Venkat Venkataramani), and that the system can be viewed as RocksDB managing persistence on local SSDs plus FoundationDB providing KV semantics, serving as the persistent "memory" of ChatGPT (persistent KV-store, not just a KV-cache).

- Jason Vallery stated that OpenAI Research's in-house data platform is referred to as DAQ (Data Acquisition), previously mentioned in a conversation with Misha, and that Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated that OpenAI has another big data team called "Data Platform" that runs Spark and Databricks workloads, led by Emma Tang.

- John Mao's OpenAI contact is ex-Instagram/Facebook and ex-Twilio, and characterized OpenAI as less "Not Invented Here" than those companies, which John Mao viewed as positive for VAST partnership potential.

- John Mao stated he will fly to San Francisco in early 2026 to visit his OpenAI contact and open a dialogue to bring in VAST engineering, and requested keeping the relationship engineering-centered.

- John Mao clarified reporting lines: Ben Ries reports to John Mao's OpenAI friend, and that friend reports to Venkat (last name not provided in the email thread).



---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*