---
type: "customer"
title: "OpenAI org and data infrastructure notes via John Mao friend (Online Data Infrastructure)"
date: "2025-12-12"
account: ""
participants: ["John Mao", "Jason Vallery", "Unknown OpenAI friend (leads Online Data Infrastructure engineering team)", "Ben Ries", "Venkat Venkataramani", "Jakob Pachoki", "Louis Feuvrier", "Emma Tang", "Misha (last name unknown)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-12_160426_5605_Re-OpenAI.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# OpenAI org and data infrastructure notes via John Mao friend (Online Data Infrastructure)

**Date**: 2025-12-12
**Account**: [[]]
**Attendees**: John Mao, Jason Vallery, Unknown OpenAI friend (leads Online Data Infrastructure engineering team), Ben Ries, Venkat Venkataramani, Jakob Pachoki, Louis Feuvrier, Emma Tang, Misha (last name unknown)

## Summary

John Mao shared notes from a catch-up with a close friend who joined OpenAI to lead the Online Data Infrastructure engineering team (Applications org). The discussion covered OpenAI's org structure, key data platforms (Rockset, Snowflake, CosmosDB, DAQ, Databricks/Spark), and a potential future integration of Applications and Research datasets; John plans an engineering-centered visit to San Francisco in early 2026 to deepen the relationship.


## Action Items


- [?] Send John Mao a concise list of specific technical and organizational questions to ask his OpenAI friend (Online Data Infrastructure lead) during the planned San Francisco visit, focusing on Rockset architecture, Cosmos DB usage, Blob persistence patterns, and any planned merge of Applications and Research datasets. @Myself #task #proposed #auto

- [?] Confirm internally whether VAST has previously evaluated Rockset (OpenAI-acquired) and capture any findings relevant to positioning VAST for OpenAI online data infrastructure. @Myself #task #proposed #auto




## Decisions


- John Mao will keep the engagement with his OpenAI friend engineering-centered and intends to bring VAST engineering into the dialogue after an in-person visit.




## Key Information


- An unknown OpenAI leader (John Mao's close personal friend) recently joined OpenAI to lead the "Online Data Infrastructure" engineering team within the Applications organization (ChatGPT, online data).

- OpenAI is described as organized into three major teams: Applications (ChatGPT and online data), Scaling (between Applications and Research, function unclear), and Research (data scientists reporting up to Jakob Pachoki, focused on offline training data for frontier clusters including OCI).

- OpenAI Applications team's two largest data platforms were described as Rockset (uses local SSDs and persists to Azure Blob) and Snowflake (OpenAI is described as one of Snowflake's largest customers).

- Jason Vallery stated that the application side (ChatGPT) heavily leverages Azure Cosmos DB for conversation persistence and that this is publicly referenced, including that OpenAI is Cosmos DB's largest customer.

- Rockset was described as OpenAI's "vector database" and the platform (persisted to Azure Blob) contains the entire history of ChatGPT conversations.

- Jason Vallery described Rockset (acquired by OpenAI) as founded by the RocksDB founders, including Venkat Venkataramani, and characterized the system as RocksDB managing persistence on local SSDs plus FoundationDB providing KV semantics, functioning as persistent "memory" for ChatGPT (persistent KV-store vs KV-cache).

- OpenAI Research data platform was described by Jason Vallery as an in-house system called DAQ (Data Acquisition), previously mentioned in a conversation with Misha (last name unknown), and said to drive very high throughput and scale (TPS/PiB).

- Jason Vallery stated that Louis Feuvrier is the lead developer/architect for OpenAI's DAQ (Data Acquisition) system.

- Jason Vallery stated that OpenAI has another big data team called "Data Platform" where Spark/Databricks workloads run, led by Emma Tang.

- John Mao stated his OpenAI friend is ex-Instagram/Facebook and ex-Twilio where he ran infrastructure/platform engineering teams, and that OpenAI is less "not invented here" than those companies, which John views as positive for VAST.

- John Mao stated Ben Ries reports to John's OpenAI friend, and John's OpenAI friend reports to Venkat (implying Venkat Venkataramani).

- John Mao requested that the relationship with his OpenAI friend remain engineering-centered.



---

*Source: [[2025-12-12_160426_5605_Re-OpenAI]]*