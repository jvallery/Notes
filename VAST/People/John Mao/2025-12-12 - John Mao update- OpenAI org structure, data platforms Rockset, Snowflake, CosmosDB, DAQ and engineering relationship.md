---
type: people
title: 'John Mao update: OpenAI org structure, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and engineering relationship'
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

# John Mao update: OpenAI org structure, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and engineering relationship

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with a close personal friend who recently joined OpenAI to lead the Online Data Infrastructure engineering team (Applications org). The email outlines OpenAI's major org structure and key data platforms (Rockset, Snowflake, Azure Blob, Azure CosmosDB, and an internal system called DAQ), plus a plan for John to visit San Francisco early in the new year to open an engineering-centered dialogue with OpenAI.


## Action Items


- [?] Send John Mao a list of specific information requests/questions for his OpenAI friend (Online Data Infrastructure lead) to answer, focused on OpenAI online data architecture, Rockset usage, and any planned merge of Applications and Research datasets. @Myself #task #proposed #auto

- [?] John Mao to fly to San Francisco early in the new year to visit his OpenAI friend and open an engineering-centered dialogue, with the goal of bringing in VAST Data engineering. @John Mao #task #proposed #auto




## Decisions


- John Mao intends to keep the relationship with his OpenAI friend engineering-centered and to open a dialogue that brings in VAST Data engineering.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, unclear scope), and Research (data scientists reporting up to Jakob Pachoki, focused on offline data for training on frontier clusters including in Oracle Cloud Infrastructure).

- Within OpenAI Applications (online data), two large platforms are Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is described as one of Snowflake's largest customers).

- Rockset is described as OpenAI's "vector database" and the Rockset data platform persisted to Azure Blob contains the entire history of ChatGPT conversations.

- There are discussions inside OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao's OpenAI friend previously worked at Instagram/Facebook and Twilio, leading infrastructure/platform engineering teams, and stated OpenAI is less "not invented here" than those companies.

- Jason Vallery stated that OpenAI's application side (ChatGPT) heavily leverages Azure CosmosDB for conversation persistence and that this is publicly referenced, including that OpenAI is CosmosDB's largest customer.

- Jason Vallery stated Rockset was acquired by OpenAI and was founded by the team behind RocksDB, including Venkat Venkataramani, and described the system as RocksDB managing persistence on local SSDs plus FoundationDB providing KV semantics, functioning as persistent "memory" for ChatGPT.

- Jason Vallery stated OpenAI Research uses an in-house system called DAQ (Data Acquisition) for research data, referenced previously in a conversation with a person named Misha, and that Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated OpenAI has another big data team called "Data Platform" that runs Spark/Databricks workloads and is led by Emma Tang.

- John Mao clarified that Ben Ries reports to John Mao's friend at OpenAI, and that John Mao's friend reports to Venkat.




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
