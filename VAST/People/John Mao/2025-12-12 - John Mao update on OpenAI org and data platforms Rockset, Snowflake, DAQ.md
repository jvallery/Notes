---
type: people
title: John Mao update on OpenAI org and data platforms (Rockset, Snowflake, DAQ)
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

# John Mao update on OpenAI org and data platforms (Rockset, Snowflake, DAQ)

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with a close friend at OpenAI who leads the Online Data Infrastructure engineering team in Applications. The email outlines OpenAI's org structure and key data platforms (Rockset, Snowflake, CosmosDB, DAQ, and a separate Data Platform team), and John plans an early-2026 SF visit to deepen an engineering-centered relationship and gather more information as needed.


## Action Items


- [?] Send John Mao a concise list of specific questions to ask his OpenAI friend about Rockset architecture (RocksDB and FoundationDB usage), Azure Blob persistence patterns, Cosmos DB role, and any planned Applications-to-Research dataset integration. @Myself #task #proposed #auto

- [?] Coordinate with John Mao to identify which VAST Data engineering leaders should join the planned engineering-centered dialogue with his OpenAI friend during John's early New Year SF visit. @Myself #task #proposed #auto

- [?] John Mao to visit San Francisco early in the New Year to meet his OpenAI friend and open an engineering-centered dialogue with VAST Data engineering. @John Mao #task #proposed #auto




## Decisions


- John Mao intends to keep the relationship with his OpenAI friend engineering-centered and to open a dialogue that brings in VAST Data engineering.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the Online Data Infrastructure engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, not clearly a platform team), and Research (data scientists reporting up to Jakob Pachoki, focused on offline data for training on frontier clusters including OCI).

- Within OpenAI Applications, two of the largest data platforms are Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is one of Snowflake's largest customers).

- OpenAI uses Rockset as a SQL-based vector database and the Rockset platform persisted to Azure Blob contains the entire history of ChatGPT conversations.

- There are internal discussions at OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao's OpenAI friend previously worked at Instagram/Facebook and Twilio, leading infrastructure/platform engineering teams, and believes OpenAI is less 'not invented here' than those companies.

- Jason Vallery stated that OpenAI Applications also heavily leverages Azure Cosmos DB for conversation persistence and that this is publicly referenced as Cosmos DB's largest customer.

- Jason Vallery stated that Rockset is the company OpenAI acquired, founded by the team behind RocksDB, and that the system is conceptually RocksDB for local SSD persistence plus FoundationDB providing key-value semantics, functioning as persistent 'memory' for ChatGPT (more like a persistent KV-store than a KV-cache).

- John Mao clarified that Ben Ries reports to John Mao's friend at OpenAI, and that John Mao's friend reports to Venkat (Venkat Venkataramani).

- Jason Vallery stated that OpenAI Research's in-house data platform is referred to as DAQ (Data Acquisition), previously mentioned in a conversation with Misha, and that Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated that OpenAI has another big data team called Data Platform that runs Spark and Databricks workloads, led by Emma Tang.




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
