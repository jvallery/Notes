---
type: people
title: John Mao update on OpenAI org, data platforms (Rockset, Snowflake) and planned SF visit
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

# John Mao update on OpenAI org, data platforms (Rockset, Snowflake) and planned SF visit

**Date**: 2025-12-12
**With**: John Mao, Myself

## Summary

John Mao shared details from a catch-up with a close friend at OpenAI who leads the Online Data Infrastructure engineering team in the Applications org. The friend described OpenAI's org structure and key data platforms (Rockset on local SSD with Azure Blob persistence, Snowflake), and mentioned potential future merging of Applications and Research datasets. John plans to visit the friend in San Francisco early in the new year and keep the relationship engineering-centered, offering to ask OpenAI for specific information needs.


## Action Items


- [?] Send John Mao a concise list of specific technical and organizational questions to ask his OpenAI contact (Online Data Infrastructure lead) during the planned San Francisco visit, focusing on Rockset architecture, Cosmos DB usage, dataset merge plans, and interfaces where VAST Database could fit. @Myself #task #proposed #auto

- [?] Identify whether VAST has previously evaluated Rockset (as acquired by OpenAI) and summarize any prior internal findings for John Mao. @Myself 🔽 #task #proposed #auto




## Decisions


- John Mao will keep the OpenAI relationship engineering-centered and will open a dialogue that brings in VAST engineering during his planned San Francisco visit early in the new year.




## Key Information


- John Mao has a very close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research), and Research (data scientists, offline data for training).

- Within OpenAI Applications (online data), two largest platforms mentioned were Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is one of Snowflake's largest customers).

- OpenAI Research uses "offline" data for training GPT models on large frontier supercomputing clusters in Oracle Cloud Infrastructure (OCI).

- OpenAI's Rockset-based system was described as SQL-based and containing the entire history of ChatGPT conversations, persisted to Azure Blob.

- There are internal discussions at OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao gave his OpenAI contact a high-level pitch of VAST's Database work, and the contact was intrigued.

- John Mao's OpenAI contact is ex-Instagram/Facebook and ex-Twilio, with experience running infrastructure/platform engineering teams, and said OpenAI is less "not invented here" than those companies.

- John Mao plans to fly to San Francisco early in the new year to visit his OpenAI contact and open a dialogue that brings in VAST engineering, while keeping the relationship engineering-centered.

- John Mao stated his OpenAI contact will openly share information OpenAI is willing to provide, and John offered to ask for specific information needs.

- John Mao clarified that Ben Ries reports to John Mao's OpenAI contact, and the contact reports to Venkat (last name not provided in the email thread).

- Jason Vallery stated that OpenAI Applications (ChatGPT) heavily leverages Azure Cosmos DB for conversation persistence and that this is publicly referenced.

- Jason Vallery stated Rockset is the company OpenAI acquired, founded by the creators of RocksDB, including Venkat Venkataramani, and described the system as RocksDB managing persistence on local SSDs with FoundationDB providing key-value semantics, functioning as persistent "memory" for ChatGPT.

- Jason Vallery stated OpenAI Research has an in-house system called DAQ (Data Acquisition) that drives very high throughput and petabyte-scale data, and that Louis Feuvrier is the lead developer/architect for DAQ.

- Jason Vallery stated OpenAI has another big data team called "Data Platform" that runs Spark/Databricks workloads and is run by Emma Tang.




---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*
