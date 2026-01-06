---
type: people
title: 'John Mao update: OpenAI org, Rockset stack, and engineering relationship via his friend'
date: '2025-12-12'
person: John Mao
participants:
- John Mao
- Myself
source: email
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-12_160426_5605_Re-OpenAI.md
tags:
- type/people
- person/john-mao
- generated
---

# John Mao update: OpenAI org, Rockset stack, and engineering relationship via his friend

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with his close friend who leads OpenAI's Online Data Infrastructure team, including OpenAI's org structure and key data platforms (Rockset, Snowflake, and Azure Blob persistence). Jason Vallery added context on CosmosDB usage, Rockset's likely RocksDB plus FoundationDB-style KV semantics, and OpenAI's internal DAQ (Data Acquisition) system and separate Data Platform team (Spark/Databricks). John plans an early New Year SF visit to deepen an engineering-centered relationship and offered to ask his friend for specific information needs.


## Action Items


- [?] Send John Mao a concise list of specific questions and information requests to ask his OpenAI friend (Online Data Infrastructure lead) during the planned early New Year San Francisco visit, focusing on Rockset architecture, CosmosDB usage patterns, DAQ requirements, and dataset integration plans. @Myself #task #proposed #auto

- [?] Identify whether anyone at VAST Data has previously evaluated Rockset in depth and summarize findings for John Mao (answering his question: "Has anyone internally looked at Rockset before?"). @Myself #task #proposed #auto




## Decisions


- John Mao intends to keep the relationship with his OpenAI friend engineering-centered and to open a dialogue that brings in VAST Data engineering during an early New Year visit to San Francisco.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, not clearly a platform team), and Research (data scientists reporting up to Jakob Pachoki, focused on offline training data for frontier clusters including in OCI).

- Within OpenAI Applications, two large data platforms mentioned were Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is one of Snowflake's largest customers).

- Rockset at OpenAI was described as a SQL-based "vector database" and the platform (persisted to Azure Blob) contains the entire history of ChatGPT conversations.

- There are discussions at OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao's OpenAI friend previously worked at Instagram/Facebook and Twilio, running infrastructure/platform engineering teams, and believes OpenAI is less "not invented here" than those companies.

- Jason Vallery stated that OpenAI's application side (ChatGPT) heavily leverages Azure Cosmos DB for conversation persistence and that this is publicly referenced as Cosmos DB's largest customer.

- Jason Vallery stated Rockset (acquired by OpenAI) was founded by the team behind RocksDB, including Venkat Venkataramani, and described the system as RocksDB managing persistence on local SSDs plus FoundationDB-like KV semantics on top, functioning as persistent "memory" for ChatGPT.

- Jason Vallery stated OpenAI Research uses an in-house system called DAQ (Data Acquisition) for training data, driving very high throughput and scale (TPS and PiB), and that Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated OpenAI has another big data team called "Data Platform" that runs Spark/Databricks workloads and is run by Emma Tang.

- John Mao clarified the reporting chain: Ben Ries reports to John Mao's friend, and John Mao's friend reports to Venkat (likely Venkat Venkataramani).




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
