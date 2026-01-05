---
type: "customer"
title: "OpenAI data infrastructure org and platforms, via John Mao friend in Online Data Infrastructure"
date: "2025-12-12"
account: ""
participants: ["John Mao", "Jason Vallery"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-12_160426_5605_Re-OpenAI.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# OpenAI data infrastructure org and platforms, via John Mao friend in Online Data Infrastructure

**Date**: 2025-12-12
**Account**: [[]]
**Attendees**: John Mao, Jason Vallery

## Summary

John Mao shared details from a catch-up with a close friend who joined OpenAI to lead the Online Data Infrastructure engineering team (Applications org). The email outlines OpenAI's major org structure and key data platforms (Rockset, Snowflake, CosmosDB, DAQ, Databricks/Spark), plus a potential future integration of Applications and Research datasets and a planned SF visit to deepen an engineering-led relationship.


## Action Items


- [?] Provide John Mao a list of specific information requests/questions to ask his OpenAI friend about OpenAI Online Data Infrastructure, Rockset architecture, and potential Applications-to-Research dataset integration. @Myself #task #proposed #auto

- [?] John Mao to visit San Francisco early in the New Year to meet his OpenAI friend and open an engineering-centered dialogue that can include VAST engineering. @John Mao #task #proposed #auto




## Decisions


- John Mao intends to keep the relationship with his OpenAI friend engineering-centered and to open a dialogue that brings in VAST engineering.




## Key Information


- John Mao has a close personal friend who recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (online data).

- OpenAI is described as organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, not clearly a platform team), and Research (data scientists).

- OpenAI Applications team's two largest online data platforms were described as Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is described as one of Snowflake's largest customers).

- OpenAI Research team reports up to Jakob Pachoki and uses "offline" data for training GPT models on large frontier supercomputing clusters in OCI (Oracle Cloud Infrastructure).

- Rockset is described as OpenAI's "vector database" and the platform (persisted to Azure Blob) contains the entire history of ChatGPT conversations.

- There are discussions at OpenAI about integrating or merging more of the Applications datasets with the Research datasets.

- John Mao gave a high-level pitch of VAST's Database work to his OpenAI friend, and the friend was intrigued.

- John Mao's OpenAI friend previously worked at Instagram/Facebook and Twilio running infrastructure/platform engineering teams, and said OpenAI is less "Not Invented Here" than those companies.

- Jason Vallery stated that OpenAI's application side (ChatGPT) heavily leverages Azure Cosmos DB for conversation persistence and that this is publicly referenced with OpenAI as Cosmos DB's largest customer.

- Jason Vallery stated that Rockset is the company OpenAI acquired, founded by the creators of RocksDB (including Venkat Venkataramani), and that the system is effectively RocksDB for local SSD persistence plus FoundationDB for key-value semantics, serving as the persistent "memory" of ChatGPT.

- Jason Vallery stated that OpenAI's research data platform is an in-house system called DAQ (Data Acquisition), previously mentioned in a conversation with Misha, and that it drives very high throughput and scale (TPS/PiB).

- Jason Vallery stated that Louis Feuvrier is the lead developer/architect for OpenAI's DAQ (Data Acquisition) system.

- Jason Vallery stated that OpenAI has another big data team called "Data Platform" where Spark/Databricks workloads run, led by Emma Tang.

- John Mao clarified the reporting chain: Ben Ries reports to John Mao's friend, and the friend reports to Venkat (likely Venkat Venkataramani).



---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*