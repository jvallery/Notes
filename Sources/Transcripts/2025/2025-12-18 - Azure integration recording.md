---
entities:
  projects:
  - '[[VAST on Azure Integration]]'
type: transcript
source_type: unknown
date: '2025-12-18'
---


VAST DataEngine
VAST SyncEngine
VAST InsightEngine
VAST DataStore
VAST DataSpace
VAST DataBase
VAST Data Platform Services
VAST AI Operating System
VAST DASE Architecture

Okay, we're going to have a conversation together and we're going to ultimately write a document together. This document will describe how vast data will integrate with Microsoft Azure. We're going to cover a variety of dimensions. And so let's start off just kind of brainstorming on the document structure and then diving into each sub area. At the macro level, the document needs
*00:00*

to cover the business strategy, why we partner, the areas of partnership, the workloads, how those workloads will present in a joint Azure and vast world, and where the opportunities of differentiation are for each platform.
*00:30*

to talk about the engineering that needs to happen on each side to realize the end-to-end vision. And then we'll talk at each one of those engineering points about specific design and constraint areas that are exposed by the systems. This will be built as one document, but it'll be broken into sections that can be carved out to be independent documents.
*01:00*

in the context of the what we're building, the why we're building it, and the how it will work. The what, why, and the how are the questions we have to answer with this document. And we, as a first step, need to really rationalize what all the sections are. Now, the capabilities of the Azure Platform All Up and the Vast Data Platform All Up are well-documented and understood.
*01:30*

So from a what is out there perspective, we will use AI to go kind of do the research report for us and pull out all of the areas of the surface area of the two platforms to identify areas where there's potential integration points. And that's useful from a broader, like just coverage map perspective.
*02:00*

that we want to create of what are all the things that customers use on Azure and how can those be empowered, enlightened, or augmented by the current capabilities of VAST data? There are areas of overlap and there are areas of collaboration that are possible here. And it's important that we think about this in the lens of how we evolve the VAST data roadmap so that we have a clear unified vision around it.
*02:30*

There are clear short-term opportunities that we will focus on. And then there's the, like, what are the scenarios we want to light up in each direction? So we'll start off with the Vast on cloud offering as it exists today. The Vast on cloud offering as it exists today runs on virtual machines.
*03:03*

in any cloud provider, not just Azure. And this has certain constraints as a result. It's not very price-performing. The cost of running a vast instance when you're using VMs and the associated local ephemeral storage mean that it's really good for exposing an endpoint, but not so great for storing large volumes of data because the capacity is limited in terms of what those instances are.
*03:31*

So what scenarios that kind of unlocks today is where you're talking about an existing on-premises vast cluster from an existing on-premises vast customer who has a burst to cloud scenario where they're getting compute in the cloud. And they can connect vast on cloud back to their on-premises instance and expose it via the global data spaces, global namespace capability so that they
*04:01*

can access their on-prem data set from the cloud with cloud-based caching, cloud-based endpoints for either NFS or S3.
*04:30*

So this unlocks cases where the data sits on-prem and the compute is in the cloud.
*04:42*

The inverse opportunity is what I'm thinking about at the moment, though,
*04:50*

which is the canonical example I will reference here is a hypothetical frontier model builder like an OpenAI or a Microsoft AI who are potential target customers for this case who have an end-to-end data pipeline. An end-to-end data pipeline is a Kafka stream coming in or some other sort of event streaming system into a Spark data pipeline or a data
*04:56*

pipeline that does transformations, feature extractions, data normalization, data preprocessing into a large central Azure data lake where there is large amounts of HPC style compute, millions of cores in these examples of compute transacting against these incredibly high volume data pipelines. And the data is coming from external sources, data
*05:26*

partnerships, reinforcement feedback loops coming out of the conversations their customers are having with the models themselves, their data acquisition pipelines that would include web crawls, you know, we're really wherever they're getting data, they're ingesting it into these systems and processing it, and normalizing it and turning it into training data to be distributed to GPUs. So that's sort of the ingestion flow. And because of the, you know, quantity of data, the need to have a centralized
*05:56*

data lake and the adjacent compute, these workloads typically run in hero cloud regions or hero Azure regions in this example, where they can get millions of compute cores and exabytes of storage. But the data needs to be accessed by GPUs and the GPUs in this world are being disaggregated. They're being deployed wherever power is available. They're being deployed in Neo clouds like Nebius,
*06:26*

CoreWeave, NScale, Core42, I don't know, lots of lots of others. And they're being deployed in what are typically known as satellite Azure regions. These are kind of the smaller regions, you know, like Portugal or Spain or Sweden or Brazil or wherever, like these smaller sites around the globe. So in this canonical example, and, you know, I'd imagine, you know, a customer like OpenAI having a central data lake in a region like US East
*06:56*

or US West 2 where they're getting large amounts of capacity. But then, you know, there's 50 something Azure regions around the globe where they might get GPUs plus all of these non-Azure locations plus on-premises. And so those sites are used for both inferencing and training. And when they're being used for training, they need to be able to stage important training data adjacent to the GPUs. And then they need to be able to stage checkpoints coming out of the GPUs. And both of those things need to be synchronized back into their central data estate.
*07:26*

So this is notion of GPU adjacent storage and central storage comes into play. Central storage are the lake house, the multi-exabyte data lakes, and GPU adjacent is kind of like an ephemeral cache of data that sits adjacent to the GPU for being able to train off of the data sets and be able to stage checkpoints before they're centralized. And when you think about this from a infrastructure perspective, Microsoft is now well positioned to deliver the GPU adjacent storage. The blob storage platform
*07:56*

You mean hard drive based or even flash based, the rack counts and the power efficiencies and so forth have made it problematic for customers like Microsoft and OpenAI, Microsoft AI and OpenAI to deliver capacity in this way. And so they've looked at solutions like VAST data for this use case. But what you're really talking about then is how do you integrate a GPU adjacent VAST cluster with a central Azure data lake. And that's an opportunity point for integration.
*08:26*

to effectively replicate that sort of hybrid burst-to-cloud stretch story, but doing it between Microsoft's own storage platform and Blob, and that's adjacent to the GPUs. This is a data spaces conversation, and this is a data movement conversation leveraging things like put Blob from URL, which is an API that Microsoft delivers for this case. What does that mean from a workload perspective?
*08:56*

OpenAI is done via an in-house built tool they call SciClone. S-C-I-C-L-O-N-E. ScienceClone. Up until recently, that was built on top of Microsoft's first-party data movement library and tool called azCopy, which is the de facto way that customers use to move data in and out of Blob and between Blob storage accounts and between Azure regions.
*09:26*

built in Go that uses the put blob from URL APIs to move data. I did learn recently that OpenAI has refactored away from azcopy and now use R clone, which I find interesting for a variety of reasons, but I'll leave it out of the scope of this for now. Similarly, all of Microsoft's internal data movement platforms and frameworks like Azure Storage Mover are built on top of azcopy. And so it becomes, you know,
*09:56*

the engine of data movement for Microsoft. Even things like Microsoft's first party object replication service are built on top of these same primitives and APIs. So from an MVP surface, supporting easy copy in VAST becomes a priority to enable data movement scenarios where you're moving data in and out of central data
*10:26*

and GPU-adjacent storage. This is also how MAI does it. Microsoft AI similarly uses azcopy to move data in and out of blob storage to and from non-blob or between blob accounts. So one of the ideas that we have at VAST is to deliver a blob storage API as an additional API on top of VAST. A blob storage API on top of VAST
*10:56*

would empower customers like open AI and Microsoft AI to deploy vast GPU adjacent and leverage existing tooling frameworks and libraries with the service. So if we do that, we have to think about what is the minimum surface area of the blob storage API that we would want to support. And I think about this in the lens of the workloads we would enable. And so from a minimum viable product perspective,
*11:26*

The critical set of capabilities we would have to deliver is compatibility with azcopy. You would need to be able to, without forcing Microsoft to refactor azcopy, support Avast API that emulates or mimics the blob API such that it would work with azcopy for moving data in and out Avast.
*11:56*

you're able to do that as you support the put blob, put blob list, put block, get blob, list blobs, get blob containers, get blob, get blob metadata, all of the core rest APIs because azcopy uses those. So an order of exercise here is to look at azcopy, which is an open source tool, and identify all of the blob storage APIs
*12:26*

and what specific signatures of those APIs azcopy has a dependency on so that you could use that as the definition of what the minimum viable blob API should look like. You could continue the journey and extend what additional blob APIs you might support, including the longer tail of different scenarios like append blob, page blob, and
*12:56*

ADLS gem 2, hierarchical namespace, the DFS endpoint, the entire blob surface area is actually quite substantial. I think these are not MVP, but it's something that we should document and have justification for why we're not covering them. And, you know, this ties back to what the core scenarios are we're trying to unlock and why a blob API in the first place should exist. And when I think about it from that lens,
*13:26*

when you look at Databricks type workloads, Spark type workloads, analytics pipelines, and so forth. VAST already has a best in class solution that directly integrates with the ecosystem. And VAST has its own driver for Databricks and for Spark that uses the Azure or that uses the VAST database capability. And so if customers were interested in using VAST for these types of workloads, we would push them towards using
*13:56*

the VAST native methodology for integration with analytics pipelines. VAST also has its own Kafka endpoint, which enables data streaming directly into VAST versus running your own Kafka. So in this world, it's better to use the VAST native primitives. The unlock of why we support a blob API is really focused on compatibility sake and data movement scenarios. In a completeness solution, what we would ideally
*14:26*

What we motivate Azure to do is build an actual integration with our data spaces capability such that we could connect our index and metadata to the blob storage index and metadata. But this would require a deeper level of integration that you then you can currently achieve based on the primitives that Microsoft exposed today. A ideal solution would enable something that looks a little bit like strong consistency and we were able to do things like
*14:56*

read and write leases. We could explore the capabilities around blob lease to see if there's something we could do. But broadly speaking, it's likely that what we would end up having is data movement and async kinds of synchronization engine between blob and VAST. So this gets the data to a GPU adjacent scenario and you're pulling it out of the central data lake into VAST or you're pulling it from VAST back into the
*15:26*

the central data lake. But what ideally we would also have is the ability to tier and offload data directly from VAST into blob. Now there's a few different justifications for why this is important. Either if you're running VAST on cloud in a central Azure region, you've exposed the endpoints, or you're running VAST on premises or in one of these Neo clouds or hybrid scenarios. You know, the VAST capacity is all flash based, which is
*15:56*

for high performance but it's not great for TCO. The industry is also facing an inflection point related to supply chain and the challenges associated with procuring flash don't seem to be in a time horizon of the next 18 months to years going to get a whole heck of a lot better. We're going to be in a world where we're really constrained on flash supply and in that world hard drives are not going to be quite as constrained. I think there is certainly a
*16:26*

at the moment, but the hard drive manufacturers have their own ability to spin up manufacturing and scale up manufacturing and can respond to the demand in a way that the flash manufacturers will struggle to keep up with as they prioritize investments against DRAM and HBN memory because it's a higher margin service, a higher margin skew for them. So if you think about Samsung, Soledine, SK, Micron, they're at the moment prioritizing their manufacturing scale
*16:56*

against HBM and DRAM. And there are rumors of even cannibalization of their existing flash manufacturing capabilities in the form of SLC-QLC and repurposing it for HBM and DRAM. And so what that practically means is that the supply chain of flash storage is going to remain constrained for some time. And so when you think about what this means, for VAST, it will be problematic in that we won't be able to get the capacity
*17:26*

you need to satisfy customer demand. Further, when you think about the aggregation of datasets, they will be centralized in multi-exabyte central data lakes. And when you think about performance per petabyte, throughput per petabyte, TPS per petabyte scalability, these become, because of their sheer capacity requirements and volume, cooler in nature and can still be serviced by hard drives.
*17:56*

So blob storage has an advantage here because it already runs on hard drives and that is sort of the de facto way it gets deployed and so we can continue to assume that you'll get economies of scale by running blob storage on hard drives and driving down the cost per gigabyte for central data lakes. Currently, VAST has no notion of tiering and so a capability that needs to be introduced to VAST here is to be able to tier from the GPU adjacent high performance flash capacity or just high
*18:26*

or high-performance, flash capacity running in VAST on cloud, whatever the scenario be, be able to tear that off to hard drives. And the obvious way to do that when you're doing this in a cloud-centric world or an Azure-centric world is to, instead of tearing it directly to hard drives that are managed by VAST, you tear it to the Blob Storage Platform via Blob APIs. So we have to think through how we would do this. There are really two permutations of how you could go down this path. Path A, you store the data in Blob in what I would describe as an
*18:56*

and this means that the data is written in VAST optimized data structures. So the customer is accessing the data from VAST exposed endpoints only and then the way the data gets structured is post things like data reduction, encryption, deduplication, all of those capabilities that's within VAST. Even in fact it would be post erasure coded and we would store effectively
*19:26*

and extents of erasure-coded data striped across blob storage accounts. And that data would then be by necessity be fully managed by VAST and in order to access the data the customer would have to go through a VAST endpoint so that it could reconstruct the data. And so in that world what you're actually describing is that VAST treats blob storage as a different capacity medium that is accessed through the VAST front end. This gives likely the best performance
*19:56*

experience as well as the most cost-effective experience because of VAST's data reduction capabilities and deduplication. The downside to this approach is that if you want to access your data directly from blob storage APIs that are hosted on top of blob storage itself, the data is useless. It would just be encrypted and chunked fragments of data that would be unreadable by the customer without
*20:26*

the VAST head over top of it. So this impacts our ability to integrate with other first-party services or for customers that are using Blob directly against their own workloads and have sort of a scenario where they don't want VAST centralized. And it can be problematic for existing datasets that are already on Blob that you're trying to expose with VAST. So the alternative is where the data sits in its native format, the full file
*20:56*

the full object sitting in blob storage that vast then can index and you know kind of replicate the namespace of what's happening in the central blob data lake into the vast cluster locally and then expose it as what looks more like a reverse proxy this has the downside that now vast has to be kept aware of what the data structures and objects stored in that central data lake are and be able to be
*21:26*

updated on changes. So you can introduce things like eventing, Microsoft's change feed capability, to have sort of a pub/sub model or a ordered update log, transaction log that then VAST is monitoring to find out when the central data lake changes and then indexing that data into the VAST's local metadata store so that it knows that object exists and how to get it if it needs to. This becomes putting a lot of
*21:56*

and a burden on VAST to try and keep track of and synchronizing the namespace between blob storage and VAST itself. Of course, in this world, you don't get the benefits of data reduction and VAST has an independent now security model from what blob storage has and authentication and authorization complexities and drift can occur. And you've got all kinds of just challenges around all of those
*22:26*

those problems. So that integration looks a little bit differently. But the benefit is that you get access to all of Microsoft's first party ecosystem of tools and services, and the customer will be able to expose datasets that already exist without the necessity to kind of have it ran through the VAST front end to be ingested. So there's an argument to be made that VAST should support both of these scenarios.
*22:56*

their preferences for the data to be stored transparently in blob storage because then they can retain the ownership of the customer and you know they'll be able to upsell services on top of it and you know the customer could terminate the relationship with VAST and still continue to access all of their data without doing a heavy data migration out of VAST. From the VAST perspective the former is stickier and keeps the customer on VAST because the data is stored in a VAST native format. From the integration with the rest of the ecosystem
*23:26*

perspective. One of the things we want to cover in this document is all of the various Microsoft services that could potentially have a touch point with the data set, with VAST, and how that would work and what we would need from Microsoft for that scenario to be ended and successful. And so you can bring into scope things like the Azure Foundry service, which does manage inference and managed AI application building. You could bring into scope things like Azure Fabric and the
*23:56*

One Lake Team and then there's basically every service inside of Azure that sits above the core layer likely has an integration of some kind with Blob Storage for data persistence. So all of those things become potential scope opportunities for VAST to have integrations with as well if it enables a differentiated solution. And if you go with the first option where we're storing data in a VAST native format into Blob, it necessitates a direct integration with all of those services.
*24:26*

services for the customer to be able to get the full value out of the Azure ecosystem. Of course, the challenge associated with that then is that the Azure ecosystem must support connecting to a VAST managed API, which brings us full circle back to what is the blob storage API that VAST exposes? Does it work with all of these different scenarios and all of these different features inside of the Azure ecosystem? And how can they wire themselves up to connect to VAST? This brings into scope
*24:56*

a whole slew of conversations around networking, network isolation, endpoint management, how endpoints are exposed within Azure, what things can be done as a first party versus a third party, and then this becomes a very, very complicated conversation on a per-service-by-service basis. At the high level, blob storage is exposed to those services through deeper integration in the Azure platform that are
*25:26*

called Private Endpoints. And there's a managed service endpoints, I think they're called. Maybe there's another name for them. But what they enable is that you can expose blob storage to a first party service in such a way that there's networking routes for that service without actually exposing public IPs to the internet that then you increase the sort of blast radius of potential vulnerability. There's some
*25:56*

that Azure Blob Storage supports as well called NSP or Network Security Perimeter, which also further enables the story. It's focused around policy driven preventing data exfiltration and ensuring that first party Microsoft services have access to customer data, but that the customer data doesn't need to be exposed onto any sort of public endpoint. If you do this with Avast on VM,
*26:26*

you can kind of experience exposing the endpoint, the blob API endpoint. Ultimately, you're now exposing that to a publicly routable IP address for those services to be able to connect to it because there's no opportunity for VAST, given the current exposure of how these services work from a 3P perspective, to expose its own managed service endpoint or a network security perimeter kind of Azure service in the same way that blob storage has.
*26:56*

So this potentially is a security issue that would likely prevent adoption of VAST being exposed this way. Further, when you look at these services, and there is a service-by-service conversation that needs to be researched, in many cases when you're wiring it up to connect to blob storage, you're doing it using the storage resource provider and connecting it using the control plane, not putting in the FQDN of your
*27:25*

your Blob endpoint. So obviously Blob would have a, you know, my storage account. blob.cord.windows.net endpoint. But when you are building that out in, you know, we'll say configuring Azure Foundry, you're not typing that in. What you're actually doing is selecting the Blob storage account from a pick list of storage accounts that are in the same resource group as the Foundry instance, for example. And so in that world, the control plane wouldn't be aware of any vast endpoint and wouldn't be able to wire up natively
*27:55*

to a VAST endpoint. It would only be able to wire up natively to a Blob storage endpoint. So without Microsoft doing engineering here, that scenario ends up being blocked. And this ultimately translates into why we would want to do a transparent version of integration so that all of those existing services will continue to work with Blob, but then they can still get the best of VAST through VAST's exposure back to Blob via the deeper layers of transparent integration.
*28:25*

Microsoft itself has something they've called Project Tuscany, which hasn't been discussed publicly, but I'm very aware of and was encouraged to consider how we can leverage this with VAST, which is effectively a reverse proxy through blob. And so the scenario here is that a customer would be able to see data exposed in a S3 bucket. Their initial implementation is focused on S3. That is not part of blob storage.
*28:55*

service tries to access the data, it hits a Blob Storage endpoint, and that Blob Storage endpoint goes and fetches the data from the remote S3 endpoint and then returns it back to the first-party system. So this makes Blob become a reverse proxy back to VAST. So if you think about this from an end-to-end flow perspective, ideally what you've got is a Blob endpoint and an S3 endpoint hosted by VAST that you can access, and that would either be data sitting local to VAST or tiered up into Blob, and similarly you've got a Blob
*29:25*

storage endpoint that could be accessed from within Azure by first party services that exposes data stored in VAST. And if all of these scenarios become played together, you've got sort of that end-to-end solution working. Ideally, you could do a deeper level of integration with the VAST data spaces capability, but that would require cooperation with Microsoft to really build that out in a first party kind of way. But if we have the project
*29:55*

we have blob API on top of vast and we have blob able or if we have vast able to consume the change feed and index of the blob storage account we kind of can build the indent narrative with those primitives in a what i'll describe as duct tape and shoestring way so all of this context it goes back to our first principle of what we want to design as an indent
*30:26*

that describes why we want to integrate, what scenarios we unlock, which workloads we want to target, and what kind of integration for each one of those workloads is necessary, and what the end-to-end customer value would be. And for each one of the scenarios, what the MVP would look like. So I'm going to pause here and we're going to go and do a little bit more iterating on this recording.
*30:56*

