---
type: "1-1"
created: { { DATE } }
status: "done"
counterpart: "[[Yogev Vankin]]"
role: ""
team: ""
company: ""
series: "1-1/Yogev Vankin"
cadence: "Weekly"
meeting_mode: "Video"
location_or_link: ""
calendar_url: ""
start_time: ""
duration_min: "30"
privacy: "internal"
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251020 1052 Teams Meeting (Parallels) Transcription.txt"
tags: [meeting, "1-1"]
---

# 1:1 — Yogev Vankin — 2025-10-20

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Discussed cloud architectures for VAST on AWS/GCP/Azure, the need for object-store tiering as the durable layer, GPU-adjacent caching and prefetch APIs, metadata persistence options, QoS/governance, and high-TPS key-value use cases. Agreed to pursue object tiering, sync with Asaf on persistence design, and avoid overfitting to OpenAI by building a broadly applicable multi-cloud solution.

## Key facts learned

- Initial AWS design: single VM 50 TB as global namespace cache; later persisted data to S3 and metadata to EBS with SSD reads (~30% cost overhead).
- GCP moved to clustered design: mix of data-storing and compute-only VMs; tried N and z3 instance families.
- AWS and Azure clusters exist but are not production-grade; Oracle Cloud POC completed.
- No paying customers yet for this product track.
- OpenAI model: central durable storage in hero regions; GPUs spread across many regions/clouds; async pre-staging to GPU-adjacent stores.
- OpenAI tool Cyclone inventories blob across accounts (Snowflake) and uses Put Blob From URL for async copies.
- GPU-adjacent storage needed for throughput/cost, network autarky, and checkpointing.
- OpenAI checkpoints: RAM triple-write within IB domain, then NVMe, HDD adjacent, then subset to central storage.
- APIs desired: researcher-driven prefetch from global namespace; cache-on-read also valuable.
- Durability goal: object storage (Blob/S3/GCS) as system of record with VAST front-end compute/caching.
- Debate: metadata persistence on block (EBS/PD/Premium Disk) vs Premium Blob/S3 Express; Premium Blob ~3 ms TTFB may be high for metadata.
- Consistency debate: eventual consistency acceptable for some AI workloads but strong consistency required for broader customer base.
- QoS/governance needs: quotas and prioritization by identity across throughput, TPS, and capacity.
- KV store frontier: maximize TPS per PB for <=64 KB IO; OpenAI uses RocksDB + FoundationDB on L-series VMs.
- Spark/Databricks used primarily for global ETL of conversations/API logs into training data lake.
- Strategic focus: multi-cloud global namespace spanning hyperscalers and on-prem to reduce duplication and vendor lock-in.

## Outcomes

- Aligned that tiering to cloud object storage as the durable layer is required.
- Agreed Jason will sync with Asaf on persistence architecture and QoS/governance.
- Captured need for a prefetch API to stage data into GPU-adjacent cache; cache-on-read also valuable.
- Agreement to build a generally applicable multi-cloud product, not just for OpenAI.
- Jason to explore travel to Tel Aviv and Iceland and request pre-reads.

## Decisions

- Pursue object-store tiering (Blob/S3/GCS) as a core design requirement.
- Schedule Jason–Asaf technical deep dive for persistence/QoS (on 2025-10-21).

## Action items (for Yogev Vankin)

- [x] Meet Asaf (chief architect) to align on persistence design, object tiering, and QoS/governance @Jason Vallery ⏫ 📅 2025-10-21 ✅ 2025-10-27
- [x] Prepare proposal for object-tiering design (Blob/S3/GCS), including metadata persistence options and consistency trade-offs @Jason Vallery ⏫ ✅ 2025-10-27
- [x] Draft API requirements for dataset prefetch into GPU-adjacent cache and cache-on-read semantics @Jason Vallery 🔼 ✅ 2025-10-26
- [x] Define QoS/governance model: quotas and prioritization by identity across throughput, TPS, and capacity @Asaf ⏫ ✅ 2025-10-27
- [x] Plan travel to Tel Aviv and Iceland; coordinate timing and pre-reads with Yogev @Jason Vallery 🔽 ✅ 2025-10-27
- [x] Benchmark viability of Premium Blob/S3 Express for metadata persistence versus block storage options @Asaf 🔼 ✅ 2025-10-27

## Follow-ups

- [x] Share current DataSpaces architecture docs and persistence roadmap with Jason @Asaf 🔼 ✅ 2025-10-27
- [x] Confirm with OpenAI teams whether S3 API suffices for GPU-adjacent storage or if Blob API parity is required @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Capture requirements for global KV store (TPS per PB, <=64 KB IO) and assess feasibility on VAST @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Summarize Oracle Cloud POC learnings and current AWS/GCP/Azure cluster status for Jason @Yogev Vankin 🔽 ✅ 2025-10-27

## Risks

- Overfitting design to OpenAI could limit broader market fit.
- Eventual consistency may face strong customer pushback.
- Premium Blob latency may be unsuitable for metadata-heavy workloads.
- API parity and feature gaps between Blob and S3 could complicate adoption.
- Network choke points across regions can impair throughput if not prefetched.
- AWS/Azure clusters are not production-grade yet; time to harden.
- No paying customers yet increases delivery and runway risk.

## Open questions

- Where should metadata persist: block storage (EBS/PD/Premium Disk) or Premium Blob/S3 Express, and how to meet latency/IO needs?
- What consistency model will the platform guarantee (strong vs eventual) across sites and for which workloads?
- Exact API design for researcher-driven prefetch and cache management from the global namespace?
- Is Blob API support required for all OpenAI workflows, or will S3 API suffice for GPU-adjacent storage?
- How will the namespace/metadata be managed when tiered to object stores across clouds (layout, GC, recalls)?
- What is the QoS policy model and enforcement mechanism by identity for throughput/TPS/capacity?
- Feasibility and design options for a globally distributed high-TPS key-value store via DataSpaces?
- To what extent should cache-on-read be prioritized versus prefetch for target workloads?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.03] Jason Vallery :  Jason ValleryI'll get the cloud storage at the market, but you know.

[00:00:09.84] Remote : So we started in AWS, suggesting a single-instance solution of 50 terabytes that can be connected into vast on-prem. to other bus on clouds with global namespace. You know a bit about the global namespace?

[00:00:29.30] Jason Vallery :  Jason Vallery>> Yes, and I think that is a killer feature. I am super excited about that capability.

[00:00:34.42] Remote : >> Okay, great. So we started in AWS, single VM instance, 50 terabyte that was supposed to be. to be a cache for global namespace and allow users to access their data from everywhere. Later we worked on persisting this solution so the data was written to S3 and the metadata into EBS. The reads came from the local SSD, so the performance was decent. The cost was 30% more than just the VM, and it solved the persistency issue, because if the VM failed or something like that, you had all the data and so on. So it wasn't just... for a it wasn't just for a you know a femoral storage in order to access a global namespace it was also if you like to store data okay later we switch to a working on a GCP with a cluster in mind. So the idea was, and still is, to build a cluster with a few VMs, each VM on a different placement group, which mean that if one VM fail or we upgrade in it or whatever, it's still functional, and by the matter of fact, You can also do two VMs, it depends. So we started with GCP with N instances. This is type of, family of instances that GCP has. It was, claim it's not that cost efficient. the not not just cost-efficient but also for a large capacities you need a huge cluster then we change the we added option to add VMs that are not storing data they are only used for compute and later we change the gcp instance to be also z3, which is a different family of instances within gcp. So this is for the gcp part. Then we also started and brought up the gcp instance. in cluster in AWS. So not just a single VM, but a cluster, but without the persistency I mentioned in the single VM, because we said the persistency will come from the fact that we have few VMs, and we also... brought up Azure cluster, but not a, both Azure and AWS are not in production grade, and those are still ongoing projects.

[00:03:59.78] Jason Vallery :  Jason Vallery- Yeah, yeah.

[00:04:00.62] Remote : - In the middle, we also did a pretty intense, POC with the Oracle cloud So, I think I think in general it's a it's a story of The product without without a good you see how how much we did so far But we we still haven't got even one paying customer.

[00:04:33.68] Jason Vallery :  Jason ValleryMaybe I could walk you through how I think about the problem and what I kind of see as the biggest gap to a successful customer scenario.

[00:04:45.59] Remote : Go ahead.

[00:04:46.50] Jason Vallery :  Jason ValleryYou know, when I think about the three hyperscalers, but we could really extend this out to include Oracle and others, Google probably has the best vision and set of capabilities in market because what's really starting to emerge, and I think the Neo clouds and the kind of expansion is a good leading indicator for why this is important, is that the data global namespace is what enables customers to bring their data. data to the GPUs, and so let me give you the OpenAI example. OpenAI have many, many exabytes, tens of exabytes of data. That data spans different scenarios, but you broadly could sort of bucket it into training data, you know, this is data there are. wiring from data partnerships, they have their own web crawler, you know, this is the core training data assets, their user data, you know, the data that their users are sort of uploading and sharing, then there's checkpoints, you know, a checkpoint repository of all the checkpoints that are generated, and you know, each one of these classes of data, and I would say there's an overall like data analytics lake that does Spark style, Databricks style stream processing and aggregations and those sorts of things. So all of that data sums up to be tens of exabytes, and, you know, there's, uh requirements around durability and distribution of that data such that it really only can logically sit in one of the hyperscale, hyperscale hero regions within Azure, and so you know a um you know west U.S. east U.S. kind of location where you know that kind of capacity is possible, zones are possible, um, and, you know, that becomes what OpenAI describe as central storage. But when you think about the way GPUs are being provisioned, GPUs are being placed wherever there's power, and so, you know, and in fact, that's often not in what are typical hero Azure regions. So GPUs are put-- OpenAI specifically has GPUs in 50-something Azure regions today, and then obviously, you see they're getting GPUs in CoreWeave, and in Oracle Cloud, and in InScale, and in Next. So the way they manage their data, and OpenAI has been very successful, not because of any Azure capability, but because they have a bunch of really smart engineers on their side. They've been really successful in taking this concept where their data sits in these central storage repositories in big hero azure regions and then asynchronously moving data to and from all of these gpu adjacent storage right so so then when you think about like how do you deploy and manage the capacity, what happens is that OpenAI will get a ratio of storage racks to GPUs and so that, you know, there's a bunch of different math and we can get into some of the details around how that's all thought about, but then the storage that's adjacent to the GPUs in their mind is a family. We're still talking about hundreds of...

[00:08:15.24] Remote : pepabytes in most cases or at least 100 pepabytes. But ephemeral for specific tasks, yeah. Right,

[00:08:22.25] Jason Vallery :  Jason Valleryso and then the GPUs themselves are used fungibly, right, so sometimes they're training on them in the middle of the night, sometimes they're running inference for production chat GPT workloads, sometimes they're doing data. I understand, I understand. Right, and so all of that data from All of these different sites moves in and out of the central storage repositories. So in my mind, our opportunity, and this is a real opportunity with OpenAI, is that we can manage the GPU-adjacent storage for them using global namespace, connected back to a central data repository that can scale out to literally exabytes of capacity. But then what that practically means is that we're able to offload that data into the most cost-effective tiers as possible. So that means that VaST is fronting an object storage, blob storage in Azure, such that we can scale out the compute nodes, but then the persistence is actually managed into blob, and you know what? Performance on this is okay. Even if it's running on HDD, we're not talking about high IOPS workloads. When you look at multi exabyte namespace, you're talking about a continuum of temp.

[00:09:33.21] Remote : - I know, I know, I know the workload of such users, okay. So I understand, I understand. But what you are saying, that VAT will also do the management layer instead of them? Well, I think that we have an opportunity, yeah, please note that they have much more information than us as the storage vendor has, so they know which job they are going to schedule where, right, so with global namespaces, it's not like I know beforehand. and something is going to access from somewhere. When the workload's starting, I'm doing few heuristics in order to prefetch the data, cache it, and so on. So I don't know what infrastructure they built, but at least they are superior in the knowledge they have. regarding which data should be where and when.

[00:10:34.45] Jason Vallery :  Jason Vallery- That's right. So I can walk you through that a little bit, and this is a question of view around prefetching and APIs that are existing today. But the way they think about this is they built an internal tool, they call it Cyclone, Science Clone, and what it is is a repository where, today they're working on top of Azure, and so they have a limited set of capabilities, but what they do is they level blob storage's inventory capability And then they take inventories from all of their storage accounts run it into a snowflake database And it gives the researchers kind of a view on what is the total data space that they have access to? And then the researcher that's got a they'll get allocated a cluster for a job, and they'll say, okay, well, this researcher is going to get a set of GPUs that are in, you know, the Portugal reason or whatever it is. Right. Um, and the researcher will then go in and say, I'm going to work on this project. I'm going to need this set of training data. Uh, and they might express it as a file folder path within the hierarchy. They might express it as a file, like all the JPEG files. they might express it as a tag where it's like all of the files tag with a certain tag or prefix. But the researchers then can go and put in an expression into that tool that says this is the set of data out of this exabyte scale corpus that I want pre-staged into the GPUs, and then that background async copy jobs if you haven't looked. at it, Microsoft Blob has a capability called "Put Blob from URL" and what that allows you to do is sort of service-to-service copies, and so they have a background set of tooling that then starts moving that data, or not moving, copying that data into the destination storage account where that is adjacent to the GPUs that researcher is going to be using. It's a pre-fetch kind of process and they manage that with a self-service portal. So ideally what you get in data space is some analogous kind of capability where you could say I'm going to be running this job and then give them an API that says this is the data

[00:12:39.41] Remote : Out of the global namespace I want to pre-fetch into the GPU adjacent cache. and it's not, so maybe the global instance is not the correct word for it because it's meant to do other stuff. But I understand you want to have some kind of API for them to say, here are the objects I want to have in this specific class, right?

[00:13:04.27] Jason Vallery :  Jason Vallery- I would also-- - Something like that. - I would also say there's a cache on read, obviously data spaces does well. So I think that cache on read is very interesting to them as well. Currently nothing like cache on read exists within blob storage, so they don't have this capability today, but I think if they

[00:13:19.98] Remote : Had cache on read, they would use it. But from my point of view, everything is cache, so from the moment, let's say we have a a vast on-cloud cluster and it gets an API call that will say, here are the objects I want you to store. Once it's stored, it's cached.

[00:13:42.78] Jason Vallery :  Jason Vallery- Okay, exactly. But, you know, I feel like, I think the key--

[00:13:49.33] Remote : - So it's not cached on read, it's cached on pref.

[00:13:52.80] Jason Vallery :  Jason ValleryRight? Cash on prefetch, cash on read are both valid scenarios. They're slightly. Okay. I mean, I think the key message here is that they consider central storage as the durable system of record for all data, and then I understand they want to have the data that is adjacent to the GPUs. there for two key reasons, actually three key reasons in some cases. The three reasons why they need GPU-adjacent storage. The first is purely the performance and bandwidth costs of data movement. When you think about the diversity of locations where they've got GPUs, the WAN connectivity between whatever... site that is and back to GPU or to the central storage repository has a high degree of variance. In some cases, I actually should point out though, in some cases, in many cases, actually particularly like Azure regions within the US, you still have like terabits of throughput between two different Azure regions. So if central storage is in say, you know, West US 3, which is in Phoenix, and they're trying to access that from a GPU, I don't know, say in Dallas in Texas, you know, they probably can push 10 terabits of throughput between there. There are other sites that even like there's, I mean, fights in the US with petabits, petabits of throughput.

[00:15:17.41] Remote : One minute, Jason, Jason, one minute. Jason, I'm back with you.

[00:15:38.20] Jason Vallery :  Jason ValleryYeah, no worries. So, so my, my key point there is that throughput isn't always a constraint and in many cases it's not. So, um, where it does become constrained potentially is like they've got a new site in Spain. and the data is sitting in the US and there's choke points. So I think you look at this from a... Actually, one thing I should point out here is when you look at this from a workload perspective, these are pretty large sequential IOs. So when they're loading training data into the GPU cluster, these are already pre-processed. In most cases, there's variance here, but in most cases, these are... pre-processed large parquet files that are, you know, gigabytes in size. So, you know, moving that isn't a bunch of I/O, it is purely throughput, and so latency is also not really a constraint that they care about. It is purely a throughput constraint that they really are looking at. So in some cases they actually will just train data across the WAN by accessing and moving the data into the GPU adjacent store. So one thing OpenAI has, I didn't mention earlier, is they actually have their own distributed file system-like. It's not actually a file system, but they have their own distributed data store that sits inside of the GPU hosts. So, you know, they might get a 4G 4,000, 8,000, 12,000 GPU node cluster, and each one of those nodes in the GPU hosts, there's a one-to-one relationship between the GPU and a locally attached NVMe, physically on the same host, and so they build their own distributed cache over top of that, that sits entirely within the InfiniBand envelope of the GPU cluster, and so what they'll do then, in some cases where there is no GPU-adjacent storage, is they'll read the data into that GPU-distributed cache, and when you think about, like, checkpointing, that's also where they checkpoint. So, like, when they generate a checkpoint, it goes into that distributed cache, and then they async copy that off to object storage. Which leads me to the next reason why they want GPU-adjacent storage, and it's... Network Autarky, and so Network Autarky is a fancy way of saying what happens when an idiot with a backhoe digs up the fiber and this GPU cluster has lost connectivity back to one of the central Azure regions, and so obviously these GPU clusters are massive expenses, and if it's in the middle of a training job and that site loses connectivity. activity back to central storage, they want to be able to survive and continue to use those GPUs to train even though there's no network connection. Otherwise, you're just stranding massive, massive capex. So they want that GPU-adjacent storage to be able to catch checkpoints while it's training, even if there's no network connection back to the central storage. and to have some amount of that training data pre-staged locally so that they can continue to operate. This is an interesting problem space because you have to start thinking about things like token expiry and authentication caches, where it's not just autarky from the network, it's also just you're disconnected services like you know Azure Active Directory and those sorts of things but this is a key scenario for them to make sure those GPUs are not ever idle and so

[00:18:54.54] Remote : That's really why they want... Which media do they use today in order to do the checkpoints? Which media? Media, yeah. What are they using in order to do the checkpoints?

[00:19:09.42] Jason Vallery :  Jason VallerySo the way that works is that if you're running in that distributed training GPU cluster, all of the checkpoints are written, actually the checkpoints go into, they have this internal distributed storage fabric that runs in the cluster that they built, and that stores it first into memory, and so it does the triple right into at least three nodes in the InfiniBand. envelope that all have different fault domains and so the GPU itself is checkpointing into host memory of an adjacent GPU node or three adjacent GPU nodes that are in different physical fault domains in the same cluster and then that gets persisted down onto the local NVMe of those same GPU hosts an async process copies the checkpoint into hard drives spinning in the blob storage cluster that is in the same data or dataset and then it gets copied from there back to central storage but not all of them so like they'll you could imagine their checkpointing very frequently like into host memory. like 1 out of every 5 gets persisted on local NVMe, and maybe like 1 out of 20 gets persisted on hard drives adjacent, and then maybe like 1 out of 50 get moved back into central storage. So, you know, their rollback times are very minimal as long as it's either in a peer node, so like if it's a single host failure, they can recover very quickly because a peer node probably has it either in RAM. or on local NVMe, and they never need to go back to hard drives to recover. But if it's a broader scale outage or another scenario is like they're doing A/B testing, well, they'll train forward to a certain epoch, and then they'll roll back, and they'll make some parameter change, and then they'll train again, and then they'll compare the two results. They do that quite frequently, and so in that case, they'll go out to hard drives for it. So the only case where they're ever actually restoring from the hard drives is when it's a cold job start, when that cluster is just switching jobs, and they do that all the time too, right? So as I mentioned, you know, they use their capacity very fungibly when they've got a big burst of chat GPT user inference traffic, they'll stop training on a cluster and then start the inferencing processes. traffic kind of dies down, they might switch back to training, they might partition clusters, and so they're always doing that kind of capacity balancing.

[00:21:30.25] Remote : Okay, okay, I don't believe we can do better than what they are doing for specific for the checkpoints because it seems like they build a robust infrastructure. just for the checkpoint but typically for the checkpoints I think I think they

[00:21:50.81] Jason Vallery :  Jason ValleryBuild the correct solution for them but the problem though you get where the opportunity sits yes your solution today is based entirely on Azure storage primitives yes based entirely on blob storage and their face real constraint where they're now into data centers where blob storage is not possible. So they have to have GPU adjacent storage that fits into this workflow that does not come from Azure, and so that means they're--

[00:22:21.02] Remote : - Yeah, I know, I know. I know I'm also, yeah, I'm also involved on this project. So I assume they will-- one or the other. One option, it seems like this is what at least they're asking for now, is to have the storage vendor compatible also with the Azure protocol, and the other option, I don't know if they are going to use it, but it's a valid option is to work with S3 protocol, which is pretty common in most of data centers, right?

[00:23:11.19] Jason Vallery :  Jason Vallery- Right. You know, what I want to hear is that, There aren't any real capabilities in the blob API that they depend on in a way that you can't with the S3 API, and they've extracted all of this code anyway into a storage driver. So, you know, I mean, well, first of all, we should up-level and say there are a whole bunch of different teams that use storage.

[00:23:34.13] Remote : Yeah, absolutely.

[00:23:35.06] Jason Vallery :  Jason ValleryCore training platform, their core training platform has a... Python driver that they built that already supports GCS, and it supports blob storage, and it abstracts all of the APIs that the actual researchers are using to load and to checkpoint, and so, you know, having S3 support there, I think, is non-trivial. I mean, sorry, is trivial. I think they probably already got that support. So it's more where the blob API will come into play. as for some of the other scenarios, like the data copies and their data analytics platform, they do use some interesting blob capabilities. So I don't worry so much about the blob API or S3 API here. I think a blob API for them would be a nice win. But I think more about like how, if we really are successful here, data spaces could come into play. and resolve a bunch of the friction and data duplication they have. So today this means a lot of data duplication. So when you think about the tens of exabytes they have on the Azure platform today, there are a lot of duplicate copies of things, and so really they can reduce their storage footprint pretty substantially and solve this scenario. at the same time, if we convince them that they can move away from some of the blob primitives and go straight to an S3 API on a GPU-adjacent VAS cluster or a blob API on a GPU-adjacent VAS cluster. I think that will be a very compelling narrative for them. So yeah, I don't think the checkpointing workload is out of question, and in some ways, it's.., and I think we could even win the checkpointing workload in Azure, assuming we could do the offload to the central storage repository and express that central storage repository as something that all the GPU adjacent clusters can go and connect to.

[00:25:23.17] Remote : - Yeah, okay, and what do you think we are missing? in order to be competitive in this use case.

[00:25:35.46] Jason Vallery :  Jason Vallery- So this is where I have a bunch of learning to go understand how and how we would leverage data spaces. I mean, clearly the first thing we need is the ability to offload capacity to blob storage such that that becomes the durability layer. and where all of the data sits, and similarly to S3 and Google Cloud, we need the ability to ensure that the data is persisted and the system of record is the object storage platform provided by the hyperscale. If we continue to depend on ephemeral local NVMe or even high-density NVMe SKUs, and those are-- pre-provision, we lose the ability to dynamically grow capacity, we lose the ability to scale the cluster in and out, and we lose the ability to hit the lowest cost point per gigabyte if we're not leveraging the native object storage provided by the hyperscalers.

[00:26:32.29] Remote : Okay, so one thing is tiering to objects. store. Okay. What else? I mean, I think when you look at

[00:26:42.16] Jason Vallery :  Jason ValleryTierendodge's store, there's a lot of open questions around how that would work from a metadata perspective and how the namespace would be managed and then how that would

[00:26:50.95] Remote : Integrate. Ah, it's simple. It's simple. I think that the metadata should be stored on EBS or the equivalent in Azure. So let me ask you is not is not is not the right media for for a metadata So let me tell you unless you are saying i'm only building a product for Open ai use cases where they don't have a lot of metadata and so on But I think we both want to build something that can serve more than a specific use case

[00:27:22.99] Jason Vallery :  Jason ValleryI might challenge you a little bit to think a bit more creative. Okay. The, I'll tell you the hardware perspective from an Azure lens. So in Azure today, if you're running a premium disk, which is, you know, Microsoft's equivalent to EBS, a block storage device. So, they're over-provisioned, they're pre-provisioned, and over-provisioned, such that you're paying for the full vault, the full IOPS, the full throughput, regardless of utilization. The second thing is that the hardware that that runs on, from a COGS perspective, is identical to Microsoft's premium blockchain. storage service. So if you go and leverage premium blob, you're actually running on the exact same storage racks, and when you think about like latency characteristics and the index and file system that Microsoft manages, it's all the same crap under the hook. You're not going to get that much better performance out of a premium disk than you are. are going to get out of Premium Blob, but you are going to pre-provision the capacity and it's going to be a lot more expensive and you're going to have to deal with the control plane to be able to attach that to a VM, and one of the things that we need to start thinking about is Microsoft has another real big problem, which--

[00:28:50.75] Remote : - Just let me reflect what you're saying. you are saying I can get with blob, even with the blob protocol, which is similar to S3, it's not meant for low latency. You think I can get with the premium blob storage on Azure same performance as the equivalent to EBS? If so, obviously we can use it.

[00:29:14.12] Jason Vallery :  Jason Vallery- Yeah.

[00:29:15.53] Remote : Look I'm trying to look at the infrastructure in the on the architecture in more wider form and and not just tied it to to specifically to to Azure and specifically a sweet spot they have. In general, let's say this we want the metadata to be stored in a service. or persistent service that allow a lot of small updates with high performance and relatively low latency, and we need only friction of capacity on this storage, and so it doesn't really matter if we can do it in lower cost, obviously it's better. I a bit doubt that the BLOB protocol can handle low latency, but. a year to be seen, but, but, but okay. But in the, in the most of the data should be on a, on a, a stream, globe, whatever, but whatever it's called in a tier that is a low cost, which means probably it's on a H, HTDs.

[00:30:21.54] Jason Vallery :  Jason Vallery- Yeah. So a couple of things. So Premium Blob, as well as S3 Express One Zone, so Amazon's Analogous Premium Object here, both of those are all on NVMe. The performance characteristics in Azure are you'll get about three milliseconds time to first byte on Premium Blob.

[00:30:41.87] Remote : - It's a lot for, it's a lot for metadata.

[00:30:45.77] Jason Vallery :  Jason ValleryIt is. You know, that you'll see is what's kind of crazy, and this is an implementation detail that's been around for Azure for a while. If you look at Azure, there's actually two different disks or block storage offerings. One is called, there's a premium V2, as well as a ultra disk offering, and then there's premium V1 and standard disks. Standard disks, premium v1, are all actually still an HTTP protocol under the hood. So the VM connects to a driver that's running on the hypervisor, and then that driver on the hypervisor is translating BlockIO to HTTP requests in the background to the storage cluster. So you there's an API that Microsoft publishes called the PageBlob API, so the disks VMs are still, when you're using either standard or premium v1, using an HTTP driver to translate block to rest. When you go to premium v2 and direct drive, that is actually a new internal implementation that Microsoft has that does bypass that HTTP layer. to improve performance and drive lower latency. But so for many years, and in still many cases, block storage at Microsoft is still actually carried over a REST API for many different customer workloads, and so there's been a lot of tuning that Microsoft has done to enable that case, and that is where we'll get the best cogs. If we can sacrifice what that means from a perspective. Agree, not all workloads are the same, but when I think about the core AI training scenarios and reporting, latency isn't that big of a deal, and particularly if what you can do is use that layer for the persistence of the metadata, but then load that metadata into the local NVMe in the cluster so you can spin it up and spin it down or it out so that you know you're really only using it for persistence not for reads so it's really only write latency that you're gonna incur and then

[00:32:49.05] Remote : Ultimately yeah I need to but I need to do a lot yeah I need to do a lot of

[00:32:53.89] Jason Vallery :  Jason VallerySmall upgrades so that's where I will I this is where I need to learn more about your architecture our architecture I'll change my words I don't understand the consistent models, but you know, the way I would be architecting something like this is providing an eventual consistency kind of tier where you can updates into the vast cluster that are then lazily written down to a durable metadata layer, and if you can enable that kind of case, then you fully. offloaded the problem, if you have to maintain strong consistency.

[00:33:27.39] Remote : Yeah, it's offloading the problem to the customer that need to come back from something that is not consistent.

[00:33:35.14] Jason Vallery :  Jason ValleryBut you could tune it, for many workloads it would be fine, like I would tell you OpenAI would be fine with that. Other customers...

[00:33:41.71] Remote : Yeah, I'm wondering if you're not... I'm just I'm just saying that I'm wondering if we are not typing it all too much to open because it's not It's a maybe it's fine for for them Which which is great But if I'm looking at the entire install base, but there's a to see I suggest a storage that is eventually consistent is something that we played with a bit, especially around the global namespace when eventual consistency is very tempting and we got a lot of pushbacks from customers. So maybe. I just don't want us to build something that will be beneficial only for one use case that when you know when I come to look at what OpenAI did and let's say I'm comparing them to XAI, I think the XAI architecture or infrastructure much more robust. They don't need all what you to say, because it's just-- Place the the GPUs and the storage in the same place. So I'm I'm a bit afraid I want to build a solution that can fit a lot of customers I don't want just to tie it only to a single customer

[00:35:06.62] Jason Vallery :  Jason VallerySo I hear you and I'm very aware there are many most scenarios require strong consistency, but what I think we see, as we see this proliferation of neoclouds and GPU capacity being tucked everywhere, somebody can find a spare megawatt, is even XAI will eventually be there, right? Today, XAI's scenario is they've got Colossus and Colossus 2, and everything's in one facility, and so that makes sense that they don't have this problem yet. But imagine the world that we're about to enter where we, as a large scale model builder, have GPUs spread around the planet.

[00:35:47.09] Remote : That's why to spread them, why to spread them around the planet.

[00:35:51.18] Jason Vallery :  Jason ValleryBut that's, it's a lot easier to do these things disaggregated, right? Because what's happening is the data center construction is chasing the power. problem is only going to get worse. You're not going to be able to get gigawatts of power in a single site and then assume that everything that you do is in a single site. The world that, like I said, OpenAI is already in is they have GPUs in 50-something Azure regions and an emerging number of these Neo clouds. When you get to this problem space, you'll end up having a disaggregated fleet of customers. capacity anyway. I would imagine that that will be a case.

[00:36:27.73] Remote : - Okay, it might be the case. I personally don't think this is the case, but it might be true. I think that the AWS and Azure showed us they can build huge data center in a single place, but okay, maybe I don't know enough and there is an option.

[00:36:45.66] Jason Vallery :  Jason ValleryLargest example that Microsoft has pulled off so far is 200 megawatts and that was the Fairwater project that Microsoft announced a few weeks ago. I was the storage lead for that project. 200 megawatts is nothing compared to where we're going, and you know the you're going to run into is how that data that needs to have a common representation across multiple sites. So even if you are able to go build multi-gigawatt single site locations, which I do think are in the future, like I know that Oracle's doing it obviously in Abilene, and then there's a project going on in Wyoming to build a couple of gigawatts in a single site, and Elon's got classes too, like even that--

[00:37:28.37] Remote : - Yeah, Elon is also bidding, yeah.

[00:37:30.67] Jason Vallery :  Jason ValleryScale though, like you're still going to run inference in disaggregated and because it's cheaper to, you know, tuck these things in wherever the power's at.

[00:37:42.21] Remote : Absolutely, I agree about the inference, but please note that some of the things you mentioned, like checkpoints, are not related. I totally agree regarding the inference.

[00:37:54.61] Jason Vallery :  Jason ValleryBut the problem with inferencing is that you still want to do training and off hours, right? So inferencing I mean maybe as we move to a more agentic model and it's depend. It's depend

[00:38:03.14] Remote : What what what the GPU is going to look like so I I cannot project at the moment But I'm not sure it's going to be the same GPUs and also in 3ds is At least one product line that is more toward the inference and also other companies. So I don't know, maybe, I don't know, it's yet to be seen.

[00:38:24.97] Jason Vallery :  Jason Vallery- I guess the point I would make there is that you, regardless of the type of GPU, I mean, if you're going to like TPUs that are ASICs that are just purpose optimized for inference and different levels of floating point precision, know, maybe this isn't the future, but in a case where you are using GPUs inferencing demand is, you know, diurnal in nature, meaning at peaks and valleys throughout the day based on user traffic going on, like you still make those things always running at a hundred percent. So if there's ways for customers to do capacity balancing such that they're doing training they're going to want to do that because that's getting the most ROI out of that very expensive catalyst.

[00:39:06.14] Remote : Okay. Okay. Okay. So let's go back to what you think we are missing. So one thing you said the tiering to S3 with a question regarding what we are going to do with metadata. Yeah. What else?

[00:39:25.21] Jason Vallery :  Jason ValleryYou know, where I know OpenAI has a lot of pain, and I don't have a full understanding of the vast capabilities around this yet, are quality of service and governance controls around resource utilization. So, being able to allocate certain amounts of... throughput, TPS, capacity to certain user principles, identities, being able to do request prioritization, saying, you know, if the request is coming from the GPU cluster, it should take priority over a request from a different application. So, at the service principle or authentication layer, being able to effectively delegate different resource quotas. across throughput capacity and TPS. That is a key use case for them, given the diversity of scenarios accessing their data systems, that they have real granular and tight controls that allow them to prioritize and apply quota on all three of those dimensions.

[00:40:25.40] Remote : - Okay. Okay. i would like to suggest that you also will speak with asaf we are now asaf is the chief architect we are now working on the persistent part of the of the architecture the persistent part of the the cluster things like you you just spoke about so I think it's going to be a good idea for you to talk with him.

[00:40:57.10] Jason Vallery :  Jason Vallery- Yep, I have time scheduled with Softomorrow to meet him, so that'll be great. - Great, okay. - The next thing I would comment on is that the emergence of the key value store, and obviously you guys, we have already been working on that with Dynamo support and so forth, but the question is, The question that OpeningEye has posed is how to get the maximum TPS per pepabyte stored. What are the architectural things, what are the hardware things that can be done to drive crazy high TPS or IOPs to a key value store where the values are...

[00:41:38.25] Remote : One thing is not to use is not to use blob storage for metadata

[00:41:42.41] Jason Vallery :  Jason ValleryWell, this is a different workload though. So just to be clear like it's a

[00:41:46.61] Remote : Right

[00:41:53.09] Jason Vallery :  Jason ValleryBut I would what I would say like the Holy Grail thing that we we should be thinking about delivering is how do we get to? a globally distributed, so, you know, a data space enabled global key value store that delivers the absolute maximum TPS on 64 KB or smaller I/O. So, that is a scenario that important to their current research trajectory because and then they talked about this publicly like GPT-6 the key innovation that they'll bring forward is long-term persistence memory if you look at what VLM is brought and what's happening in the open source world and what DeepSeq did it's paged attention but the idea that during the pre-fill phase of inference that it can load in historical context windows and effectively compute over those during decode, and so being able to grow that key value store and be able to run inference over that key value store on any you in the planet and get the maximum. TPS and throughput for our TPS from it is the key capability we're talking about. Um, they.

[00:43:15.26] Remote : Yeah. They're, they're using, they're using, uh, KB kits, right?

[00:43:18.68] Jason Vallery :  Jason ValleryWell, what they built, so they bought, they purchased a company. Uh, so last year, OpenAI purchased Rockset, which was a, the company that started, well, that started RocksDB which is an open-source distributed database, and so the way OpenAI is currently running this, and you may have some experience with Microsoft's L-series VMs, but the way they currently do this is they get a bunch of L-series capacity from Microsoft and then they run RocksDB on those nodes for the log structure merge tree, compaction, managing volumes and then they run foundation DB over top of rocks DB for the key value store so today that's okay I solution to this problem is a combination of rocks DB foundation DB and L series VMs and there you know why

[00:44:11.13] Remote : Did you do you know why you didn't go to to KV case dynamic

[00:44:17.89] Jason Vallery :  Jason VallerySo, OpenAI have their own inferencing stack, OpenAI built all their own internal inferencing frameworks and training frameworks and inferencing stack, they don't use Dynamo or any of that. They have their own KVCache, OpenAI built it.

[00:44:31.96] Remote : Do you know why or is this historical reasons?

[00:44:38.34] Jason Vallery :  Jason ValleryThis before NVIDIA had anything. Like they've been doing this for a while. So they saw the problem years ago and have been working on this and then everybody else is playing catch-up. So they were ahead of everyone else in the industry before there was a solution and they continue to evolve their own solutions. You could imagine a world where OpenAI recognized that the open source world has outpaced them and could

[00:45:00.85] Remote : Plat but right now they continue to invest. Yeah but at the moment they continue to work

[00:45:05.57] Jason Vallery :  Jason ValleryWith the stack which makes sense. Yeah. Understood. Exactly. Okay. There are other little like features in the platform like they do um a ton of Spark and Databricks um and so you know there are different constraints there in terms of how they do processing. and what it means for analytics workloads.

[00:45:25.50] Remote : - Do you know what they are doing with Spark?

[00:45:29.53] Jason Vallery :  Jason Vallery- Well, so the way the reinforcement learning pipeline works is, you know, you as a user are having your conversations with chat GPT, or you're using their API in either case, all of that inferencing happens, all the test time compute happens. Then the output of those... sessions or those API calls get stored into Microsoft's Cosmos DB, which is Microsoft's planet distributed database, and then it also gets pushed into a streaming data pipeline. So it's not Kafka, but they have their own sort of streaming data pipelines that go back into a centralized Spark Databricks cluster, and then that cluster, so this is every conversation, every API call points across the planet in all of those different regions. All of that comes into that single pipeline, and then that pipeline is cleaning that data, and so it's anonymizing it, PII removal, all of the kind of normalization, data normalization tasks you could imagine they would want to do across all of that data that's being generated across the fleet, and then that goes into a big data lake that they have. have, then that gets turned into parquet files and then that goes back into their training repository. So they have 30.

[00:46:37.78] Remote : Okay. So it's mainly, mainly, mainly the Spark is used mainly for ATM.

[00:46:43.51] Jason Vallery :  Jason ValleryYeah, I would say that's primary. Okay. It's for sure. Obviously they have a bunch of other use cases around the data partnerships and their web crawlers and, you know. data feature extraction and those sorts of things, but I would say they have many different connectors going into different SaaS applications where they do data normalization. They have a very large data analytics team that does all of this preprocessing, but the biggest use case they have is ETL of the conversations and API calls. so that they can push that straight back into their training loop in their

[00:47:19.65] Remote : Training data repository. Yeah, I understand. The reason I'm asking is because we had a lot of work integrating with Spark SQL in the vast database group but it seems like it's not the main use case. So I don't think it's really relevant, but OK.

[00:47:43.22] Jason Vallery :  Jason ValleryYeah.

[00:47:43.44] Remote : OK.

[00:47:44.99] Jason Vallery :  Jason ValleryBut I think a lot of these learnings are applicable to other customer scenarios that we're going to face. I always think about it as, if you can go and understand who's doing things at the frontier, that becomes the common customer of the future. are applicable to the platform broadly, not just to an OpenAI win, but obviously the key priority for me is to help us win OpenAI.

[00:48:09.22] Remote : - Okay, I understand. I think I learned a lot from the conversation. One thing I want you to think about is not focus only on the OpenAI win. use case because you know when you go to hunt a whale, like OpenAI, you can win it and you may not, but if you build a strong product in the way, you can hunt other whales also. So we need to think how we build a product that is good for... all kinds of use cases and users and then if you can win OpenAI, that's great, but even if not, at least we build a strong product that can win other deals.

[00:48:59.92] Jason Vallery :  Jason ValleryThat's right, and so I think what, where I'm applying my lens around that problem is how do we win on the hybrid? scalers with the primitives that we can get from the cloud. So, you know, what it would take to build the kind of scenario I talked about on Azure primitives, on AWS primitives, on GCP primitives, and the other lens that I'm applying to that is this multi-cloud, neo-cloud hybrid. world, because I think that is a key thing that I've observed happening, not just with OpenAI. Obviously, OpenAI is notoriously going multi-cloud right now. That's all over the news, but enterprise customers are becoming much more skeptical of all of their eggs in one basket, and I can definitively say that over the years. Having watched Azure evolve from nothing to where it is now, we went through a cycle, and we went in the early days where CIOs and CTOs of all the big enterprises were betting their careers on a cloud migration and recognized the complexity of multi-cloud being just too much of an uphill battle. basket, and so there was a moment in time where every enterprise that already made their bet, they were either an Azure customer, an AWS customer, or a GCP customer. That has proven out to be a bad mistake for most enterprise customers because they have given and ceded too much control to a single infrastructure provider, and so the world that I see is customers who are repatriating back on-premises, customers who are diversifying their infrastructure investments and becoming actually multi-cloud, and so when I think about data, that is a really gnarly problem to solve for those customers as well, and then this new layer of the neoclouds, and so having the global data namespace being multi-cloud, including on-prem, is the enabler to all of those enterprises. So if we can leverage hyperscaler primitives to truly deliver a global native namespace, we can win those customers. that are trying to go multi-cloud or are already multi-cloud. I think that is the other key area of focus for us to ensure we have a breadth solution.

[00:51:32.42] Remote : - Okay, I agree with that and this part of the reason really the global namespace.

[00:51:44.51] Jason Vallery :  Jason Vallery- Yeah. You know, I'm looking forward to working with you closely, obviously, we've got a lot of work to do and to figure out together. I still have a lot of learning. You know, I want to get some time with you and the team, you know, Jeff challenged me with getting over to Tel Aviv as soon as I can getting over to Iceland as soon as I can. You know, I'm working on some of the logistics around that now. want to partner with you on figuring out when and how that makes sense. Love your guidance on things I should learn in advance before I go, like any specific areas of the stack I should investigate. All of that, like how do I partner with

[00:52:21.92] Remote : You best. Okay, so I think the next good step is to contact the staff as you said. that you're already going to do.

[00:52:34.46] Jason Vallery :  Jason Vallery- Yeah, okay. Yeah, I'm meeting with him tomorrow.

[00:52:35.75] Remote : - Great, cool.

[00:52:38.22] Jason Vallery :  Jason Vallery- Anything else we should chat about now or anything else I can answer for you?

[00:52:42.78] Remote : - No, I think we are fine.

[00:52:47.81] Jason Vallery :  Jason Vallery- Good, good. Pleasure to meet you. Looking forward to working together.

[00:52:52.47] Remote : - Thank you.

[00:52:53.49] Jason Vallery :  Jason Vallery- Bye-bye. - All right, thanks, bye.

[00:52:56.61] Remote : - Bye.silence (audience member speaking faintly) to share with you all. You We'll see you in a little while, okay? Thank you. Do you want to get a photo? Sure. Can you give us a photo of that? There's a picture of you. Wow. All right. All right, buddy.
```

<!-- ai:transcript:end -->
