---
type: people
title: John Mao update on OpenAI org, data platforms (Rockset, Snowflake, DAQ) and intro path via his friend
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

# John Mao update on OpenAI org, data platforms (Rockset, Snowflake, DAQ) and intro path via his friend

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with a close friend who leads OpenAI's Online Data Infrastructure team (Applications org) and described OpenAI's major org structure and key data platforms. Jason Vallery added context on OpenAI's use of Azure Cosmos DB, Rockset lineage (RocksDB + FoundationDB semantics), and an internal Research data system called DAQ, plus a separate OpenAI Data Platform team for Spark/Databricks. John plans to visit the friend in San Francisco early in the new year to open an engineering-centered dialogue and offered to ask for specific information needs.


## Action Items


- [?] Send John Mao a concise list of specific questions to ask his OpenAI friend about OpenAI data platform requirements (Rockset, Cosmos DB, Snowflake, DAQ) and any planned Applications-to-Research dataset integration. @Myself #task #proposed #auto

- [?] John Mao to visit his OpenAI friend in San Francisco early in the new year to open an engineering-centered dialogue and explore bringing VAST Data engineering into the conversation. @John Mao #task #proposed #auto




## Decisions


- John Mao intends to keep the relationship with his OpenAI friend engineering-centered and will open a dialogue that brings in VAST Data engineering when he visits in San Francisco early in the new year.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the Online Data Infrastructure engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research), and Research (data scientists reporting up to Jakob Pachoki, focused on offline data for training on frontier supercomputing clusters including OCI).

- Within OpenAI Applications, two large data platforms mentioned were Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is one of Snowflake's largest customers).

- John Mao's OpenAI contact described Rockset as OpenAI's vector database, SQL-based, and the platform persisted to Azure Blob contains the entire history of ChatGPT conversations.

- There are discussions at OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao's OpenAI contact is ex-Instagram/Facebook and ex-Twilio, where he ran infrastructure/platform engineering teams, and he believes OpenAI is less 'not invented here' than those companies.

- Jason Vallery stated that OpenAI Applications (ChatGPT) heavily leverages Azure Cosmos DB for conversation persistence and that this is publicly referenced as Cosmos DB's largest customer.

- Jason Vallery stated that Rockset is the company OpenAI acquired, founded by the team behind RocksDB, and that the system is effectively RocksDB managing persistence on local SSDs with FoundationDB providing key-value semantics, serving as persistent 'memory' for ChatGPT (more like a persistent KV-store than a KV-cache).

- Jason Vallery stated that OpenAI Research has an in-house system called DAQ (Data Acquisition) for training data, referenced previously in a conversation with a person named Misha, and that Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated that OpenAI has another big data team called Data Platform that runs Spark/Databricks workloads and is led by Emma Tang.

- John Mao clarified that Ben Ries reports to John Mao's OpenAI friend, and that the friend reports to Venkat (implied Venkat Venkataramani).




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
