---
type: people
title: 'John Mao update: OpenAI org, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and intro path via his friend'
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

# John Mao update: OpenAI org, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and intro path via his friend

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with his close friend who recently joined OpenAI to lead the Online Data Infrastructure engineering team in the Applications org. The email outlines OpenAI's org structure and key data platforms (Rockset, Snowflake, Azure CosmosDB, and an internal Research system called DAQ), and John plans an early New Year SF visit to open an engineering-centered dialogue with OpenAI.


## Action Items


- [?] Send John Mao a list of specific information requests/questions to ask his OpenAI friend (Online Data Infrastructure lead) about OpenAI data platform requirements and integration plans between Applications and Research datasets. @Myself #task #proposed #auto

- [?] Confirm internally whether VAST has previously evaluated Rockset (post-OpenAI acquisition) and summarize findings for John Mao to use in his engineering-centered outreach. @Myself #task #proposed #auto




## Decisions


- John Mao intends to keep the relationship with his OpenAI friend engineering-centered and to open a dialogue that brings in VAST engineering rather than positioning it as a sales-led relationship.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, unclear scope), and Research (data scientists, reporting up to Jakob Pachoki).

- Within OpenAI Applications (online data), two largest platforms mentioned were Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is one of Snowflake's largest customers).

- Rockset (OpenAI Applications) was described as a SQL-based "vector database" whose persisted data platform contains the entire history of ChatGPT conversations, persisted to Azure Blob.

- Jason Vallery stated that OpenAI Applications also heavily leverages Azure CosmosDB for conversation persistence and that this is publicly referenced as CosmosDB's largest customer.

- Jason Vallery stated that Rockset is the company OpenAI acquired, founded by the creators of RocksDB, including Venkat Venkataramani.

- Jason Vallery described the Rockset-based system as RocksDB managing persistence on local SSDs plus FoundationDB providing KV semantics, functioning as the persistent "memory" of ChatGPT (more like a persistent KV-store than a KV-cache).

- OpenAI Research data is referred to internally as "offline" data and is used for training GPT models on large frontier supercomputing clusters in Oracle Cloud Infrastructure (OCI).

- Jason Vallery stated that OpenAI Research uses an in-house system called DAQ (Data Acquisition) for the research data platform, and that it was previously mentioned in a conversation with an individual named Misha; DAQ drives very high throughput and petabyte-scale data volumes.

- Louis Feuvrier was identified as the lead developer/architect for OpenAI's DAQ (Data Acquisition) system.

- Jason Vallery stated there is another OpenAI "big data" team called "Data Platform" where Spark and Databricks workloads run, led by Emma Tang.

- John Mao's OpenAI friend previously worked at Instagram/Facebook and Twilio, leading infrastructure/platform engineering teams, and characterized OpenAI as less "Not Invented Here" (N.I.H.) than those companies.

- John Mao stated that Ben Ries reports to John Mao's friend at OpenAI, and that John Mao's friend reports to Venkat (implied Venkat Venkataramani).

- There are discussions inside OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao gave his OpenAI friend a high-level pitch on what VAST is doing with the VAST Database, and the friend was intrigued.




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
