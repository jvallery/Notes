---
type: draft-reply
status: pending
created: "2026-01-05T19:35:45.760404"
urgency: "normal"
to: "John Mao <john@vastdata.com>"
subject: "Re: John Mao update: OpenAI org structure, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and engineering relationship"
source_file: "/Users/jason.vallery/Documents/Notes/Sources/Email/2025/2025-12-12_160426_5605_Re-OpenAI.md"
---

# Draft Reply to John Mao

**Regarding**: John Mao update: OpenAI org structure, data platforms (Rockset, Snowflake, CosmosDB, DAQ) and engineering relationship
**Urgency**: normal

---

## Key Points to Address

Thank John Mao for the org and platform details, confirm the reporting chain clarification (Ben Ries and Venkat), and provide a short list of specific questions for his OpenAI friend (Rockset architecture details, CosmosDB role, DAQ interfaces, and any Applications-to-Research dataset merge plans). Reiterate respect for keeping the relationship engineering-centered.

---

## Draft Response

John — thanks for the detailed update on OpenAI’s org structure and the data platform stack; it’s exactly the level of signal we need. Also confirming I’m aligned with your read on the reporting chain: Ben Ries under Venkat, with the Online Data Infrastructure team sitting in Applications.

On Rockset: we have not done a formal internal evaluation specifically mapped to OpenAI’s implementation (local SSD persistence to Azure Blob and conversation history storage). We’ve looked at Rockset in the market context, but not a deep architectural teardown against their exact patterns—if you can pull a few concrete details below, we’ll do a targeted assessment immediately.

Here are the specific questions I’d like you to ask your friend, focused on architecture and interfaces (and keeping it engineering-centered): (1) Rockset: what’s the deployment model (SaaS vs self-managed), what data is stored on local SSD vs persisted to Azure Blob, what are their ingestion sources (event streams, OLTP logs, blob files), and what are the dominant query patterns/SLAs (latency, QPS, concurrency) for “conversation history” and other online features? (2) CosmosDB: what is it the system of record for (user/session metadata, conversation state, auth/entitlements, rate limiting, etc.), what API model are they using (Core/SQL, Mongo, Cassandra), and what are the partitioning/hot-partition pain points? (3) DAQ: what does it stand for internally, what are its northbound/southbound interfaces (APIs, connectors, file formats), and where does it sit relative to Blob/Snowflake/Rockset (source of truth vs transport vs cache)? (4) Applications-to-Research: are there active plans to merge datasets or unify pipelines between Applications and Research, and if so what’s the driver (governance, cost, latency, reproducibility) and the expected timeline/ownership?

Your plan to go to San Francisco early in the new year is the right move—let’s keep it engineering-to-engineering and use that visit to open a technical dialogue rather than a sales motion. If you can send me answers to the questions above by Friday, January 17, I’ll turn it into a crisp set of follow-ups and identify the right VAST engineering participants for the next conversation.

Jason Vallery  
VP, Product Management – Cloud  
VAST Data

---

## Original Summary

John Mao shared details from a catch-up with a close personal friend who recently joined OpenAI to lead the Online Data Infrastructure engineering team (Applications org). The email outlines OpenAI's major org structure and key data platforms (Rockset, Snowflake, Azure Blob, Azure CosmosDB, and an internal system called DAQ), plus a plan for John to visit San Francisco early in the new year to open an engineering-centered dialogue with OpenAI.

---

*This draft was auto-generated. Edit and send via your email client.*
