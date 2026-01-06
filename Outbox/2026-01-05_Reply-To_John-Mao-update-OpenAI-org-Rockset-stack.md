---
type: draft-reply
status: pending
created: "2026-01-05T19:35:19.776311"
urgency: "normal"
to: "John Mao <john@vastdata.com>"
subject: "Re: John Mao update: OpenAI org, Rockset stack, and engineering relationship via his friend"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-12_160426_5605_Re-OpenAI.md"
---

# Draft Reply to John Mao

**Regarding**: John Mao update: OpenAI org, Rockset stack, and engineering relationship via his friend
**Urgency**: normal

---

## Key Points to Address

Thank John Mao for the detailed OpenAI context, confirm you will keep the engagement engineering-centered, and provide a short prioritized list of questions for his friend (Rockset architecture details, CosmosDB vs Rockset split for conversation persistence, DAQ storage and throughput requirements, and timeline/driver for merging Applications and Research datasets). Also answer or commit to finding the internal status on whether VAST has evaluated Rockset before.

---

## Draft Response

John — thanks for the detailed OpenAI context and the org/platform breakdown; it’s exactly what we need to stay grounded. Let’s keep this engagement engineering-centered and focused on concrete workload fit, not a generic “platform pitch.”

For your friend, here’s the prioritized ask list: (1) Rockset internals: what’s the actual storage/indexing architecture today (RocksDB vs something else), how they handle ingestion + indexing pipelines, and whether they rely on any FoundationDB-style transactional KV layer; (2) persistence split: what data lives in CosmosDB vs Rockset for conversation/state (what’s authoritative, what’s cached/derived), and the read/write patterns + latency SLOs for each; (3) DAQ: where DAQ lands raw/processed data (Blob vs other), peak ingest throughput (GB/s and events/s), retention, and the top 2–3 query/scan patterns that hurt today; (4) Applications + Research dataset convergence: the current timeline, the forcing function (cost, governance, reuse, latency), and what “merged” means in practice (shared lake, shared metadata, shared serving layer, or all three).

On Rockset specifically: I don’t have a confirmed internal record yet of a deep VAST evaluation (architecture/fit/implications). I’ll check with Product/Field/SE leadership and get you a definitive answer by Wednesday, January 8, including who looked at it (if anyone) and what conclusions we captured.

Appreciate you making the SF trip early in the New Year—once you have a target date/time, send it over and I’ll make sure we’re aligned on the engineering narrative and the 2–3 “must learn” outcomes going into that conversation.

Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

John Mao shared details from a catch-up with his close friend who leads OpenAI's Online Data Infrastructure team, including OpenAI's org structure and key data platforms (Rockset, Snowflake, and Azure Blob persistence). Jason Vallery added context on CosmosDB usage, Rockset's likely RocksDB plus FoundationDB-style KV semantics, and OpenAI's internal DAQ (Data Acquisition) system and separate Data Platform team (Spark/Databricks). John plans an early New Year SF visit to deepen an engineering-centered relationship and offered to ask his friend for specific information needs.

---

*This draft was auto-generated. Edit and send via your email client.*
