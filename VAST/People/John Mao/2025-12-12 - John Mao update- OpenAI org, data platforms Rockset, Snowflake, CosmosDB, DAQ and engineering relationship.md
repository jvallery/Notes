---
type: people
title: 'John Mao update: OpenAI org, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and engineering relationship'
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

# John Mao update: OpenAI org, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and engineering relationship

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with a close personal friend who recently joined OpenAI to lead the Online Data Infrastructure engineering team in the Applications org. The email outlines OpenAI's org structure and key data platforms (Rockset, Snowflake, Azure CosmosDB, DAQ, and a separate Data Platform team), and John plans an early New Year SF visit to open an engineering-centered dialogue with OpenAI.


## Action Items


- [?] Send John Mao a prioritized list of information requests to ask his OpenAI contact (for example: current Rockset architecture details, CosmosDB usage patterns, DAQ storage requirements, and plans/timeline for merging Applications and Research datasets). @Myself #task #proposed #auto

- [?] Coordinate with John Mao to identify the right VAST engineering participants to engage with John Mao's OpenAI contact after John Mao's San Francisco visit (engineering-centered engagement). @Myself #task #proposed #auto




## Decisions


- John Mao will keep the OpenAI relationship engineering-centered and will open a dialogue to bring in VAST engineering after visiting his OpenAI contact in San Francisco early in the New Year.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and other products, "online data"), Scaling (between Applications and Research, not clearly a platform team), and Research (data scientists using "offline" data for training).

- OpenAI Applications team's two largest data platforms (per John Mao's OpenAI contact) are Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is one of Snowflake's largest customers).

- Rockset is described by John Mao's OpenAI contact as OpenAI's "vector database" and the SQL-based platform (persisted to Azure Blob) that contains the entire history of ChatGPT conversations.

- Jason Vallery stated that the application side (ChatGPT) heavily leverages Azure CosmosDB for conversation persistence and that this is publicly referenced as CosmosDB's largest customer use case.

- Jason Vallery stated that Rockset is the company OpenAI acquired, founded by the team behind RocksDB, and that the system can be viewed as RocksDB managing persistence on local SSDs plus FoundationDB providing KV semantics on top, functioning as persistent "memory" for ChatGPT (persistent KV-store, not just a KV-cache).

- John Mao's OpenAI contact mentioned there are talks about integrating or merging more of the Applications datasets with the Research datasets.

- OpenAI Research data platform is described by Jason Vallery as an in-house system called DAQ (Data Acquisition) that drives very high throughput and PiB-scale data movement; Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated OpenAI has another big data team called "Data Platform" where Spark and Databricks workloads run, led by Emma Tang.

- OpenAI Research organization reports up to Jakob Pachoki (per John Mao's OpenAI contact).

- John Mao's OpenAI contact is ex-Instagram/Facebook and ex-Twilio, and said OpenAI is less "not invented here" than those companies, which John Mao viewed as positive for VAST.

- John Mao stated he will fly to San Francisco early in the New Year to visit his OpenAI contact and open a dialogue to bring in VAST engineering, and he requested keeping the relationship engineering-centered.

- John Mao stated that Ben Ries reports to John Mao's OpenAI friend, and that the friend reports to Venkat (likely Venkat Venkataramani, per context in the thread).




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
