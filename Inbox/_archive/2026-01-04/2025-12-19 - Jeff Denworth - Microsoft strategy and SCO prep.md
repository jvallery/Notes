---
entities:
  people:
  - '[[Jeff Denworth]]'
type: transcript
source_type: unknown
date: '2025-12-19'
---

Jason Vallery
Lots of things we should probably catch up on. Maybe we start with Microsoft and we can talk about the doc a little bit and then I think we should probably talk about the SCO and presentation you want me to do. Does that sound about right? Sure. I didn't read your document. That's fine. It's in a draft state but I want to do So. 

Jeff Denworth
I didn't read your document. 

Jason Vallery
I'm going to show you kind of the progress and where I'm at and what direction I'm headed. Okay, talk me through it. Just don't worry about the doc. Talk you through what we need to do. Yeah. So, I mean, the blob API itself versus this thing that Microsoft building is building called Tuscany versus the customer demand, I think is the set of trade-offs we need to weigh and make a decision around 

Jeff Denworth
Okay, talk me through it. Just don't worry about the doc. Yep. Okay. 

Jason Vallery
how important it is and what the breadth of the surface area looks like. And so I'll start with the Blob API as it relates to OpenAI and Microsoft AI. 

Jeff Denworth
Thank you. 

Jason Vallery
If those are the two customers that we really care about, then what do we need? 

Jeff Denworth
I think it's not. I think that's a myopic way to look at it. Those are the first two customers. But, you know, we can either be in for a penny or in for a pound. I'd rather be in for a pound. 

Jason Vallery
I think it's not...I think that's a myopic way to look at it. Sure. Those are the first two customers. But we can either be in for a penny or in for a pound. I'd rather be in for a pound. Right. So I'm thinking about it from like MVP of what we need like day one and then what the market opportunity would look like. Should we expand the breadth of it? And then like what is a complete solution? I guess it's crawl, walk, run in that sense. So one thing I recently heard, so I mentioned I was having coffee with Pete Eming yesterday. And for context, Pete 

Jeff Denworth
Sure. 

Jason Vallery
reports to Vamshi, great friend of mine. I knew him from his Amazon days. I hired him to the team, to my team, before I left about a year ago. And then when I left, he picked up from me the ownership of the relationship between Azure Storage and OpenAI and Microsoft AI. So he's very much in the loop of what's going on over there. And he over shares with me. He is just very friendly and loves to tell me everything. And what he shared with me is that OpenAI is replatforming away from the Blob API. the Blob API from their use in scenarios. And so like one of the key things that they had done was this big data movement engine that was responsible for replicating their bytes all over the Azure fleet. And they've actually started completely moving away of Blob's implementation of that and building their own solution using R clone and some other things. So it's fascinating just in the sense of like how the relationship with OpenAI would go in terms of what they would want. It seems like less and less the Blob API would be important to them. 

Jeff Denworth
Thank you. Why don't we give them sync engine? 

Jason Vallery
Why don't we give them SIG engine? Sure. I think that's all conversations we should have with OpenAI if we can actually crack the nut. You saw the thread from John Mao around what's going on there and that Rockset acquisition and this Venkat guy. And, you know, what I would say is that our competition at OpenAI is probably not like a Seth, Meneo, Weka. It is probably the internal we invented it here Rockset thing, right? because they do have their own effective capacity management thing with what they build with RocksDB. I would imagine our actual competition is them just doing this entirely in-house with their software. Wait, you mean like a blob store? They already have one. They just don't have the breadth of features and capabilities that we do. They already abstracted. That's what Rockset fundamentally is. This open source thing, Rockset, allows you to do log structure, merge trees, B trees. 

Jeff Denworth
Wait, you mean like a blob store? 

Jason Vallery
They have it. Capacity Management, it handles the SSDs and it all runs on L-Series VMs. Like if you squint a little bit, it is kind of like Vaston Cloud running in a VM that they already built for how they manage their VM infrastructure on L-Series. And now they're getting, and this is what he also shared with me, a bunch of bare metal L-Series, a bunch of bare metal UltraDisc, and a bunch of Blob Storage HDD clusters. And almost certainly some of that will be paid to be running this Rockset solution. So ultimately, like what I think we're competing with is OpenAI's in-house storage team that they're building their own object store. But they're never going to give that to Microsoft, but they might run it on bare metal to your point. Well, I mean, Microsoft owns the IP. To be crystal clear on your statement there, Microsoft gets the IP. They get the Rockset IP? 

Jeff Denworth
But they're never going to give that to... Okay, so... Oh, fuck. So I was just about to say they're never going to give that to Microsoft, but they might run it on bare metal, to your point. It doesn't really matter if they gave it to Microsoft or not. No, no, no, OpenAI owns the... They get the Rockset IP? Oh, okay. That's a card. 

Jason Vallery
Microsoft's deal with OpenAI is every line of code anyone at OpenAI writes is owned by Microsoft in exclusivity. They have unlimited use of it. Oh, okay. So does Microsoft decide to go and do something with it is a different question. But whatever that team is writing, I know. Go ahead. I'm also of the mind that you can't be born a dog and die a cat. 

Jeff Denworth
I'm also of the mind that you can't be born a dog and die a cat. And, you know, as much as you can say, oh, Rockset can build a, you know, geoscale, hyperscale object store, just to use that as an example. I'll believe it when I see it. 

Jason Vallery
You can say, oh, Rockstack can build a geoscale, hyperscale object store. Just to use that as an example. I'll believe it when I see it. I'm with you. The one comment I'll make here is of all of my experience working with various customers in my very tenured career, I never underestimated OpenAI. They get the best engineers want to work there and the smartest guys and they work really hard and they deliver things that seemed impossible. 

Jeff Denworth
Okay. 

Jason Vallery
So they're the one customer I wouldn't doubt would be able to pull this off. Because a decade to make ours still fucks up half the time. I get you. I get you. So I would just say like I think that is our opening eye competition and ultimately that could be our long-term competition at Microsoft more broadly. I'm certain that like what... You mean because Microsoft can use it for... 

Jeff Denworth
It took us a decade to make ours. It still fucks up half the time. Oh wait, you mean because Microsoft can use it for Azure services independent of open AI? Oh my God. Jesus Christ. 

Jason Vallery
Azure services independent of OpenAI? Because Microsoft gets the IP. They're already taking a bunch of OpenAI IP and putting their spin on it and reshipping it. So if Manish says, oh, I like that thing, I want it, Manish just gets handed the source code and the rights to use it however he wants. Jesus Christ. Is that true given they're trying to divorce each other? Is it as true? It is true until artificial general intelligence is declared by the board of 

Jeff Denworth
Is that true given they're trying to divorce each other? Is it as true? Which could be any day. Yeah, I think that's a big risk. Okay, well, we're rumor mongering here. Let's get to work. 

Jason Vallery
of directors of OpenAI. Which could be any day. It could be, but every bit of code written before that moment is owned by Microsoft. Yeah, I think that's a big risk. Okay, well, we're rumor mongering here. Let's... Yeah, no, I'm just telling you what I hear, right? So that's our biggest competitor is like John Mao's friends' new boss's product. 

Jeff Denworth
I'm not sure. 

Jason Vallery
That is the thing that they're heavily invested in over there. And they were invested when I was still working with them and they're clearly on that trend line. So, you know, I, you know, one thing that I'll observe is the compliance, portfolio, encryption, like all of those kinds of things that are going to matter to enterprise class customers are probably things that aren't in that stack. That's my experience with them. So, you know, if that stuff matters, we have the solution. But, you know, ultimately, I don't know how all of those decisions get made. So. I think you can boil it down to efficiency. 

Jeff Denworth
I think it could boil down to efficiency. 

Jason Vallery
I would bet that it's a pig. Because if I'm building a database, it's not exascale. I don't really care about optimizing to the nth bit like VAS does. And that leaves a lot of cruft. Yeah. I don't know, man. You're right. It's rumor mongering and conjecture at this point, but it would worry me. It does worry me. 

Jeff Denworth
I would bet that it's a pig because if you know if I'm building a database, although it's not exascale, I don't really care about optimizing to the nth bit like VAS does. And that leaves a lot of cruft. 

Jason Vallery
Noted. Microsoft AI, on the other hand, is not very sophisticated at all and doesn't know what the fuck they're doing. But they do leverage the blob API. And they have... Wait, wait, wait. So what's the API that Rockset would expose? Well, I mean, internally, the blob... So if you're talking about a training or inferencing workload, I mean, obviously there are dozens of workloads at OpenAI that use storage in some way or another. But if you narrow down to like training, 

Jeff Denworth
Noted. Wait, wait, wait, wait. So what's the API that Rockset would expose? 

Jason Vallery
They have an SDK that they built that all of their training platform sits on. It's actually open source. And that thing abstracts away the S3 API, the Google Cloud API, and the Blob Storage API. So it could be any of them. The Rockset team, going back to how they're currently using RocksDB for capacity management, they sit over top of that. What does that mean for capacity management? 

Jeff Denworth
What does that mean? What does that mean for capacity management? 

Jason Vallery
is the open source product. I mean, I don't know what they've done post open source product, but the open source solution that if you go and look at it, it does the like management of the node and the local SSDs and like log compaction, log structure, merge tree storage. And it manages how that like erasure codes and gets pushed off to volumes. It's like the bare storage layer. I, you know, would equate it in the object world as like the the stream or durability piece of the puzzle. It doesn't give you the abstractions over top of it and the niceties and the indexes that you would want to have like a full file system and all the metadata. And so the way that they have built that is they took there's a product from not product, an open source solution that was originally started in medical foundation DB. And so they have a layered solution foundation DB exposes a key value API and all the indices and like the niceties that make using a key value and then that uses rocks DB for the capacity underneath it and then rocks DB is managing the local NVMe that's sitting on all of the L series VMs that they get. So where's the database part? Foundation DB is the data like Foundation DB is actually the database. Are you fucking kidding me? Yeah. So this is what they're building they started building this purely for memory for ChadGPT but it's turned into they effectively have a distributed state store. 

Jeff Denworth
So where's the database part? Above that? Are you fucking kidding me? Go ahead. 

Jason Vallery
and they can store arbitrary objects of arbitrary size in it. So then that obviously could become what they use to manage all of their capacity. And it can run on bare metal because they're already running it as just like effectively bare metal on an L-Series VM. Why would OpenAI buy a foundation BB company for the storage layer? Because they bought the guys. It was an Acrehire. These are the guys that built it from the ground up and then they brought them on and they're the ones that are continuing to build it. 

Jeff Denworth
Why would OpenAI buy a FoundationDB company for the storage layer? 

Jason Vallery
it in closed source form opening eye they're not shipping a product they're not shipping it as a product they bought a team well they did but they're like they're not going to ship a storage platform they're building a storage platform for opening eye yeah so i'm still back to what's the what's the interface 

Jeff Denworth
Okay. But they also bought the product. So I'm still back to what's the interface. 

Jason Vallery
What's the interfaces? I mean, I don't know what they've built over top of FoundationDB at this point, but what they were using was the FoundationDB API against ChatGPT. Why don't we look at the code if it's open source? Well, I don't imagine they're pushing back the open source stuff anymore. It's all in-house now. No, you said the abstraction was open source. FoundationDB and RoxDB are open source, but I'm sure they've forked it since then. No, no, no, no, no, no, no, no, no, no, no, no, the abstraction, the thing that's... Oh, Boostable, okay. 

Jeff Denworth
Why don't we look at the code if it's open source? No, you said the abstraction was open source. No, no, no, no, no. No, the abstraction, the thing that sits above the... 

Jason Vallery
So, going back to Boosted Blob. So Boosted Blob is a client library for Python that does high degrees of parallelism, and it's what their training code uses. So that currently supports S3, Google Cloud Storage, and Blob. Okay. Then that would mean that RocksDB needs to use one of those, or it's been extended and your information is dated. So to clarify different workloads, RocksDB is for ChatGPT storage. So how ChatGPT talks to RocksDB and FoundationDB, 

Jeff Denworth
Okay. Then that would mean that RoxyD needs to use one of those, or it's been extended and your information is dated. 

Jason Vallery
I have no knowledge of. Boosted Blob is in their training platform for when they're running training on a model. Boosted Blob? Why did you say boosted? Okay, actually the origin of it, there was originally a library called Blobfile and then they took that and forked it and they called it Boosted Blob because it does, it's the same library but it does high degrees of parallelism. There's actually two open source projects. And actually what I heard from Pete yesterday is Microsoft is thinking about taking Boosted Blob and then taking it and reshipping Boosted blob. Why'd you say boosted? it as Microsoft's preferred Python library. 

Jeff Denworth
Okay. 

Jason Vallery
Oh, okay. I mean, it's unrelated anyway, because it's better than Microsoft. 

Jeff Denworth
Why would they ship a Python library? Who does that go to? 

Jason Vallery
Why would they ship a Python library? Like who does that go to? It goes to the model developers and it's integrated in OpenAI's internally built equivalent of PyTorch, right? Like OpenAI doesn't actually use PyTorch. I see. Go to it again. They built their own pane. Yeah. So when you're doing training data loads or you're doing checkpoints from their training framework, it's using this library to read and write from blob storage. Which is presumably also open source? No, their framework is very closed source. I've seen it. Microsoft has access to it, but it's very much OpenAI's IP. I see. Okay. All right. So we're no smarter on the answer. What do we need to support? So yeah, I was narrowly starting off with which is presumably also open source. 

Jeff Denworth
I see. Okay. All right. So we're no smarter on the answer of what do we need to support? Well, hold on, hold on. So they also needed a pen support. 

Jason Vallery
What do we need to support for OpenAI? And actually, I guess if I was to give you the TLDR of it, I don't actually think they're going to give a shit if we support blob APIs. In reality, they're trying to move away from them is what I hear. Hold on, hold on. So they also needed a pen support. So then this goes to a very narrow set of workloads. So then that is the data acquisition team that uses it. And that would be the best fit for them is actually VAST database, not a pen block. So what I would say, I wouldn't go and say, like, let's build a pen blob just speculatively. I would say until we sit down with the OpenAI team that would be using a pen blob and saying, have you seen VAST database? Because it's probably easier for you to just take that on than for us to go implement a pen blob for some arbitrary reason. Didn't you say you knew some of these people? I do. His name is Louie. I sent him a no and he didn't reply. So I mean, like, I haven't been hounding him because I don't want him to be like pissed off. He's a busy guy. I sent him an email. 

Jeff Denworth
Didn't you say you knew some of these people? 

Jason Vallery
He didn't get back to me. 

Jeff Denworth
Yeah. Not a good end to that story, by the way. You're one of them. Do you think he cares about event streams? 

Jason Vallery
Not a good end to that story, by the way. I know. I mean, I can keep hounding him, but like, you know, he's one that I met like a couple of times. I probably had like three different workshops with him, but like it wasn't a deep relationship. Do you think he cares about event streams? He cares very much about like, his team is the one that's doing the data acquisition from all the various sources. So why don't we... And the way they do that is they ingest it into a staging layer and HPC nodes. And then there's a bunch of like heads over it that are stateless. And they're streaming it into these big chunk files. So like they're effectively creating a tar file, if you will, that they then index into that tar file. So they do a bunch of random IO into these big chunks. And then those chunks go into their data processing platform. So that's why he's a pen blogging is because he doesn't actually care about the order within that file as long as he knows the byte offset. 

Jeff Denworth
But I what I'm getting at is if you were to send him a note with let's say our recent Kafka blog post and say hey we built this thing that you know scales transactions linearly and oh by the way you can also query natively from whatever you just ingested maybe you can get his attention 

Jason Vallery
But I'm getting at is if you were to send him a note with let's say our recent Afka blog post and say hey, thing that you know scales transactions linearly and oh by the way you can also query natively from whatever you just ingested. Maybe you can get his attention. Yeah, maybe I'll send him a blog. What I would say is that he isn't one making any of the infrastructure decisions and so he's been given and I know very much the capacity guys. He was given like 10 and he's already got it it's his and he's got like several million compute cores connected to it so he's like well you know i have to use what i've got so it would be a question of if he's going to go get something different you're you're being you're being short-sighted here i would say there's the stuff that he has but then there's the stuff that he could potentially get so the fact that we have we're moving in to have some conversations the fact that we're moving into a poc is like hey this thing's coming at you yeah 

Jeff Denworth
No, no, no, no, no, no, no. You're being short-sighted here. I would say there's the stuff that he has, but then there's the stuff that he could potentially get. So the fact that we have, we're moving in to have some conversations. The fact that we're moving into a POC is like, hey, this thing's coming at you. You should get smart about what it is because it could probably solve a bunch of your problems. That's okay. You have a history, so you just have to lean on that and see if you can move things forward in parallel a little bit faster. 

Jason Vallery
You should get smart about what it is because it could probably solve a bunch of your problems. Yeah, there. I mean, I'll send him a follow up and I'll send him a link. Misha mentioned him. So Misha is clearly talking. I mean, Misha owns that relationship. So I mean, clearly they're already having some conversations. So that's okay. You have a history. So you just have to lean on that and see if you can move things forward in parallel. Yeah. Yeah. But back to the blob API. My point would be, I don't think we support a pen blob because really nobody uses it. 

Jeff Denworth
All right, I'm with you. You just told me. Unless, unless, unless it's going to take them two years to move certain pipelines and we want that data. Okay, that's fine. 

Jason Vallery
I'm with you. You just told me. What we would support. Unless, unless, unless, it's going to take them two years to move certain pipelines and we want that data. Sure, but until they ask for it and we have that conversation with that team, I wouldn't put it on our priority list. Okay, that's fine. Yeah. Actually, the way I think about what the MVP should look like is around Microsoft ships a client library called AZ Copy. AZ Copy is the tool that's used to get data in and out of blob storage from a on-prem or between blob storage accounts, and it heavily leverages the data movement APIs. It leverages put, get, delete kind of semantics, verbs. It supports large files, can do basic metadata operations, doesn't support the breadth of the stack. I think our MVP is if we can work with azcopy and all of the azcopy supported scenarios and test cases pass, we've hit MVP. That's really what I frame in the document is to say... Is it open source? Yes. Well, why don't we check? It is open source. Exactly. Yeah, exactly. 

Jeff Denworth
Open Source? Why don't we check? We can get ahead of some of this stuff now. There's a sales engineer responsible for the success of OpenAI. I don't know who that... I think it's Daniel. But that's like great work to do over the holiday while you're trying to speed up time to PO. If it's Open Source, we can go test our S3 against it. 

Jason Vallery
There's a sales engineer responsible for the success of OpenAI. I don't know who that... I think it's Daniel. Mm-hmm. But that's like great work to do over the holiday while you're trying to speed up time to PO. I'm sorry, what would you propose he do? If it's open source, we can go test our S3 against it. It doesn't support S3. It supports the blob API. Oh. I'm saying our MVP of a blob API is it works with AC copy. Sorry, I missed it. 

Jeff Denworth
Sorry. Oh, right, right, right, right. Sorry, I missed it. I missed it. I'm sorry. 

Jason Vallery
I mean it does support S3 as a data copy source. 

Jeff Denworth
But if they're moving away from blob, then, you know, are we racing towards a bad state? 

Jason Vallery
If they're moving away from blob then... But I'm saying... ...are we racing towards a bad state. No, what I'm saying is MAI does use it. So this is how MAI moves data around. So what I'm saying is that our MVP for Microsoft AI should be AZ Copy Support. 

Jeff Denworth
Nice. 

Jason Vallery
I'm catching up. Sorry, I'm slow. 

Jeff Denworth
I'm catching up. Sorry, I'm slow. 

Jason Vallery
It's okay. OpenAI I don't care about anymore for blob support. MAI does care about it and they use AZCopy as their data movement engine. If we support AZCopy, we win. I got it. Okay. The next part of this is then what is the opportunity above that? And this was what I was alluding to in the chat. Microsoft's API is actually huge. The blob API has a ton of shit in there that nobody uses. 

Jeff Denworth
I got it okay 

Jason Vallery
in there that is tied very much to specific workloads and client libraries that only those libraries use, although it is an API service. And so one example of that is what they did for Spark pipelines, Databricks pipelines. It's very comprehensive and it supports hierarchical namespace, file folder renames, a ton of stuff to make that work really well. You sold me like Spark workloads, go use the VAST driver. We don't really need it. 

Jeff Denworth
Well, that assumes that, well, it's not that easy, right? If we want Databricks as a customer, there might be a lot more work to do. You know what I mean? Yeah. Yeah. Why not? Like, that's kind of the idea. 

Jason Vallery
that assumes that well it's it's not that easy right if we want data bricks as a customer there might be a lot more work to do you know what i mean like data bricks running their managed service on top of vast or what do you mean by data bricks as a customer yeah why not like that's kind of the idea you take microsoft's biggest customers data bricks one of those 

Jeff Denworth
Microsoft's biggest customers. They'd break some one of those. 

Jason Vallery
Yeah. So, but they don't actually own the data storage. It doesn't sit in like their SAS tenant. They connect up to customer-owned tenants in customer-owned storage accounts. So if you look at it from like a pure consumption perspective, Databricks doesn't actually consume much storage. The storage sits in the customer's tenants. My point was simply like... 

Jeff Denworth
Sure. Okay. My point was simply like We either have to sell data breaks on our format, and that's going to have to be brought in. He walks back the last, you know, three years of their discussions around, or we're going to have to build a blob equivalent thing that does what Microsoft does. If the, you know, if the opportunity opens up for us to actually 

Jason Vallery
our format and that's going to have to be brought in. He walks back the last, you know, three years of their discussions around, or we're going to have to build a blob equivalent thing that does what Microsoft does. If the, if the, you know, if the opportunity opens up for us to actually go to war against the storage team. Yeah. 

Jeff Denworth
go to war against the storage team. 

Jason Vallery
The driver that Microsoft ships called ABFS, Azure Blob Storage File System driver for any HDFS compatible workloads. So it works with Spark, it works with Databricks, other things. That's the way that Databricks interfaces with Blob Storage. And it really is a tightly coupled client driver and API surface that really only that client uses. I'm not really aware of any customer that consumes that API directly, although it is exposed and theoretically customers could use it. I don't think anyone's actually went to it and said, I'm going to go use that API. But it is highly tuned for those workloads. Okay. I see. Yeah. And then there's the long tail like features and stuff that I don't think makes sense. Like, you know, versioning and soft delete. There's APIs for all of that shit. But like we have our own solutions and we don't necessarily need to expose those as an API. 

Jeff Denworth
Okay. Okay. Well, depends on if they get called by other services. The reason the APIs exist is because something else wants to, you know. 

Jason Vallery
Right. So where those get used is like there's client libraries and you know CLI, PowerShell, Commandlets, all of those things to like enable soft delete on this container. Like they're management APIs really. So unless you're trying to do management via the blob API, I don't think you really need them. And so our customers would not be doing management through a blob API. They'd be doing management through a-- 

Jeff Denworth
No, no, no, no. Hold on. Our customer in this case could be the Fabric team. When we start from the basis of stop thinking about cell two. Cell two, we can just use, or cell through, excuse me. Cell through, we can just use S3. Who gives a shit? Like nobody in the world wants the blob API other than Microsoft teams. 

Jason Vallery
Our customer in this case could be the fabric team. And we start from the basis of stop thinking about cell two. Cell two we can just use or sell through, excuse me. Cell three we can just use S3. Who gives a shit? Right. Like nobody in the world wants the blob of API other than Microsoft Teams. Sure. 

Jeff Denworth
They're like, oh, we have to use this. Everybody else will take S3 in a New York Minute. The fact that it runs on Azure is completely incidental. And so the only reason to support Blob is if there's kind of stuff that's hard coded into different services that you can't get away from easily. And the only place that I think people kind of assume they can't get away from easily, it just works for Steve Ballmer. 

Jason Vallery
There we go. We have to use this. Everybody else will take S3 in a New York minute. The only reason to support BLOP is if there's kind of stuff that's hard coded into different services that you can't get away from easily. And the only place that I think people kind of assume they can't get away from easily is just the work for Steve Ballmer. And they don't have a choice. They have to use that chain. 

Jeff Denworth
Then they don't have a choice. They have to use that tool. 

Jason Vallery
Yeah, I mean, we certainly could run into customers that have, or not customers, internal use cases at Microsoft where they're like, oh, this is broken. I think you react. But with our customers, like, you know, I want to go get the big team. Sure. You know, they don't even run on blob storage. What do they run on? So to rewind the clock, like, I don't know, 15 years, there was an internal platform Microsoft built for storage called Cosmos, completely unrelated to Cosmos DB. It just 

Jeff Denworth
Yep. Those are customers like, you know, I want to go get the Bing team. What do they run on? 

Jason Vallery
It has never been shipped externally. The Cosmos team and the original object storage team, Blob team, were like kind of competitors with each other. And the Cosmos platform evolved to be Bing's storage. And they took some of the Cosmos IP and it's the durability layer of what is Blob storage now, but it's a completely different API, a completely different metadata store. And so there's a little bit of overlap in the code base, but the Bing team manages their own object storage platform, runs on the same hardware. 

Jeff Denworth
Thank you. That's amazing. 

Jason Vallery
That's amazing. That's not a wildly shocking Microsoft story. I know. So they have their own API surface, their own library, their own clients, everything that's independent from what Azure ships. The rest of Microsoft runs on Blob API. Bing, actually Exchange Online has their own solution too. Okay. I know, it's Microsoft. There was a project to try and migrate Bing to Blob. 

Jeff Denworth
That's not a wildly shocking Microsoft story. Okay. 

Jason Vallery
and it all failed and then they said fuck you we're gonna keep doing our own thing so. Makes sense. Yeah. Anyway so that's point A of the integration. I think the more interesting problem to solve is the tiering and offload to blob. I think this is actually where we'll end up spending more of our thinking engineering resources and doing it correctly. And I want to highlight it in the sense that like I think it is probably a short-term win-win on the capacity supply chain challenge. 

Jeff Denworth
Makes sense. 

Jason Vallery
One thing that I'm very nervous about, kind of watching tea leaves and hearing rumors, is the flash supply is not going to get better. But hard drive supply will. And they're two different vendors. And so I actually imagine a world where Microsoft is going to be well positioned from a hard drive capacity perspective, but not a flash perspective. And so I think it's almost imperative for us to do this in a really intelligent way, or we're going to be in trouble in not too long. 

Jeff Denworth
Why? Because native blob can tier? Flash to hard drive? 

Jason Vallery
Because native blob can tier? Well, because they're going to be constrained on how much flash supply they can get, but they'll be able to store the data on blob just fine and give good enough performance on hard drives. And, you know, us being able to tier intelligently there and leverage blob as a capacity tier is critical for our success. I'm not sure. 

Jeff Denworth
I'm not sure. How much flashes in Azure today? 

Jason Vallery
How much flashes in Azure today? I don't know that number. I would, you know, it really is the disks business, right? Well, I can tell you a revenue number, but I don't know what it turns into in terms of petabytes and exabytes under management. I mean, it's a lot, lot, lot less than hard drives. But I don't know a percentage of it, like what percentage is flash. It is the majority of the revenue driver though. Yeah, I understand. So let's assume it's 10 exabytes. 

Jeff Denworth
Yeah, I understand. So let's assume that it's 10 exabytes for shits and giggles. If I can go to Microsoft today and say, 

Jason Vallery
I would like I think that's the right order of magnitude. Maybe a little bit. If I can go to Microsoft today and say I can turn that 10 into 20, we can buy some time. But you're talking about buying turning our the Azure Discs platform which is not something we're positioned to go and take over right like we're not going to go and take all the VMs that are running in Azure and migrate their operating system disks to VAST. Like that's just not even in the cards of something we could plausibly pull 

Jeff Denworth
I can turn that 10 into 20. We can buy some time. 

Jason Vallery
And if you're actually asking the question of how much of blob storage is on flash like it's a nascent business it's like that's not an exabyte. What's the word you use nascent? Nascent like infancy tiny infinitesimal however you want to describe it like the amount of premium blob that exists out there is a very very very little small number like it's probably still measured in petabytes not exabytes. Okay. 

Jeff Denworth
What's the word you use? Nascent? Or nascent? Yeah, I understand nascent. Okay. 

Jason Vallery
That's the winnable market there for us. It is not the discs business. We're not going to go win premium discs onto best. Listen, let's move forward. The world's going all flush. It is if you had a supply chain and a price point that could keep up with that. Yeah. 

Jeff Denworth
Yeah. Listen, let's move forward. World's going all flesh. 

Jason Vallery
Yeah. 

Jeff Denworth
If we just sell an exabyte this quarter, I'll be okay. 

Jason Vallery
this quarter, I'll be okay. I'm with you. But the industry will produce like 1.3 zettabytes of hard drives this year. So there you go. Yeah, it's about 400 exabytes of flash. Yeah. Data center flash. Yeah. And I sent that note. I didn't hear any feedback, but there's this guy. Which one? It was in response to Eric Wolfie. He was, 

Jeff Denworth
Yeah, it's about 400... 400... exabytes of flash. Datacenter flash. Which one? 

Jason Vallery
asking about supply chain and demand. So to give you that context, there's this guy who I worked with quite a bit at Microsoft. He was there for a decade and he owned the relationship between Microsoft and all of the storage supply chain. So he was a director level guy over there and had a big team that was responsible for all negotiations with Micron, SK, Samsung, Seagate, Western Digital, Toshiba, all of them. And he managed the contract and the supply signals and the relationship for Microsoft. And so I worked with him quite a bit on demand signals and forecasting and what AI was going to do to the curve and so forth. He left there like three, four months ago. And now he is a vice president at NVIDIA. And he owns the same thing with SK, Samsung and Micron for HBM and DRAM. And so I was chatting. He reached out to me actually and was like, hey, can we talk about what's going on? Yeah. and what's happening in the Flash market. And he said that NVIDIA is up against it because they have GPU clusters they can't deploy because they can't get Flash. And he said that what's happened is that the vendors have pivoted what was capacity for Flash and they're now using the same facilities to build HBM and DRAM because it's similar wafer kinds and similar requirements. And all of their CapEx is going to HBM and DRAM. So his point was that not only is the demand of flash going up, but the supply of flash is going down as they reallocate capacity towards higher margin products. Well, I think there's an equilibrium there, by the way, because the price of flash has doubled in the past few weeks. So it'll have inflow. Yeah. It's a scary world. It's a scary world, though. 

Jeff Denworth
Well, I think there's an equilibrium there, by the way, because the price of flash has doubled in the past few weeks. So it'll ebb and flow. It sucks, though. Yeah, we're like, you know, 

Jason Vallery
Yeah, we're like, you know, there's a whole bunch of work that this company is doing right now that you're not exposed to at all. Sure. Thankful, actually. But not my specialty. I'm glad it's happening, though. Yeah, not fun. But my macro point is that I want us to be really clean on our offload to blob story so that we know we can leverage this capacity regardless of how the future of flash and hard drives in the market evolves. Like, it de-risks us in the sense that being able to leverage 

Jeff Denworth
There's a whole bunch of work that this company's doing right now that you're not exposed to at all. It's... Yeah. Yeah. Not fun. 

Jason Vallery
for capacity is the win-win story we tell Manish and it gives us the opportunity to leverage that to expand a capacity pool and continue to use the flash for the performance tier. So that's where I actually think we need to be really buttoned up on the engineering and have the right story and solution in place and that is the higher priority for me over a blob API. Okay let's assume that that never happens. Yeah we can talk about it sure. 

Jeff Denworth
Okay. Let's assume that that never happens. Yeah, we can talk about it. Sure. But I think there is some sort of hearing 

Jason Vallery
I think there is some sort of hearing thinking happening but I don't expect to see much for the next I don't know 12 months I think it's important that you get your your fingerprints on the conversation by the way for reasons of this Walmart thing it's like well how do you think about hearing well you know is it 

Jeff Denworth
Thinking happening. Thinking happening. But I don't expect to see much. For the next. I don't know. 12 months. I think it's important that you get your. Your fingerprints on the conversation by the way. For reasons of this Walmart thing. It's like. Well how do you think about tearing. You know. It's. Citadel yesterday. Big discussion about Google, GCP. We want a proxy. We want a proxy. Same exact conversation as Walmart with, you know, some slight exception. We want it to be always fast. Well, either it's in one tier or another. Yeah, we don't want to worry about that. Like, you know, stupid stuff. But at the end of the day, we need to think long and hard about our relationship with these stores as well. 

Jason Vallery
We want a proxy. Same exact conversation as Walmart. With some slight exception. We want it to be always fast. Either it's in one tier or another. Yeah, we don't want to worry about that. Stupid stuff. But at the end of the day, we need to think long and hard about our relationship with these stores. as well. And I don't think we're having hardly any of those conversations. Unless you disagree. What do you mean exactly by relationship? Expand like what's our relationship with blobs that are preexisting in Azure block GTS S3. Sure. The namespace piece. How do we integrate our namespace? How do we immediately become more valuable to a customer that's been in the cloud for far too long? 

Jeff Denworth
And I don't think we're having hardly any of those conversations. Unless you disagree. Like what's our relationship with blobs that are preexisting in Azure Blob, GTS, S3? How do we immediately become more valuable to a customer that's been in the cloud for far too long? 

Jason Vallery
Yeah, so then this is the third layer of integration, which I have in the doc as well, which is how do we expose existing data and synchronize our metadata and namespace with that versus how do we offload for capacity? And those are two different kind of approaches. One is if we're offloading for capacity, we do it in a vast native format and a vast optimized way to get the best performance and DRR and TCO. If we want to expose customer data. Yes. 

Jeff Denworth
Maybe. No, no, I don't think you get the DRR. 

Jason Vallery
I don't think you get the DRR. You can. No. Why? If we own the namespace, it's really the question of like, where does the namespace ownership live? Is it in VAST or is it in... It's all about the rehydration of 32 kilobyte random blocks that are part of a compression loop. Right. So, you know, what you end up storing in the object system is a data structure that is multiple. 

Jeff Denworth
No. Why? Have you thought about the rehydration of 32 kilobyte random blocks that are part of a compression? 

Jason Vallery
Fuck that! It'll be super slow! that is super slow. It is super, it's optimized and performant because you can do range reads off of the object store and that namespace in the index lives in VAST. That is the way to get the best performance, the best bang for your buck. But what it prevents you is if you're the customer and you want to go use the blob native API or the S3 native API and you look at the 

Jeff Denworth
Range Reads. 

Jason Vallery
If you look at your data, it is a big file that you have no idea what to do with or how to make sense of. So, right? So, when a range read for random 32 kilobyte or? Absolutely. Yeah. The API totally supports that. That's exactly how you do it. Nah, I'm not worried about the API. I'm worried about the performance experience. I mean, it's still hard drives and there's caching that happens on blob, but there are a bunch of implementations of this that perform very well. Uh, well, like Avid, for example, they do this for their entire video 

Jeff Denworth
Do you think a range read for random 32 kilobyte or, you know? Nah, I'm not worried about the API. I'm worried about the performance experience. Name one. 

Jason Vallery
their media asset manager they built a solution that looks exactly like this they do it for like real-time video editing and it works pretty well I mean that was just top of mind there are other like cases where this has been done even internally so if you think about what a page blog is it is a special type of blog that exists No, but they don't, they don't, there's no deduplication. They have it. You're. Files? You're not selling me. Nope. no but they don't they don't there's no deduplication the dedupe happens in the client though so that's up to us We handle the dedupe. Think about it like this. Think about each one of these files as a stick of NVMe or a stick of QLC. And you're just reading into it the same way we would if it was on a denode. You're not selling me. Seriously, this is the way you would want to do it from a performance capacity optimized way. You're going to get the characteristics of the storage platform at its primitive, but it is the best way versus letting What you're effectively doing with this is removing all of the performance implications of the middle tier of blob storage, which is the index and metadata service, because you know exactly where the bytes you want to access live within the hierarchy that is blob storage, and you can go straight to them, and you read them at whatever rate the blob system is able to give you. So you've removed a whole layer of complexity from the blob system. 

Jeff Denworth
I just worry about latency. Okay. I'm not the engineer here, but I think we need to be very clear about what our anticipated latencies are before we decide the implementation. 

Jason Vallery
Okay, I'm not the engineer here, but I think we need to be very clear about what our anticipated latencies are before we decide the implementation. Sure. But your point though is that I'm an existing customer with petabytes or maybe exabytes of capacity that already sits in blob that is stored in a blob native way that I want to be able to consume inside of VAST. And that's a very different integration story because at that point, then what you're saying is now your index and metadata are owned by and you want to be able to synchronize that in some way back to VAST. And that is the Walmart story as an example. And that integration looks different because now you're dependent upon effectively change notification to say that the data in the cloud changed and now we have to replicate that in the view that you see on premises. And then you have a whole bunch of integrations on like the pub subsystem. Azure has a thing called change feed to be able to be notified of the deltas happening so that you can reflect them on prem. 

Jeff Denworth
Yep. 

Jason Vallery
that becomes an async model. It is eventual consistency. It's ugly, but it is the only way you can kind of do that today. Yeah, I understand. Yeah. That's the second type of offload to object that has to be done. I think both are important. Those are, I guess, the initial thoughts. There are other areas that we have to touch to make sure we're fully, you know, 

Jeff Denworth
Yeah, I understand. 

Jason Vallery
loving the Azure ecosystem that give me some concern. Like for example, we don't support Azure Key Vault today. So if customers want customer managed keys and we want to go hook those into the Azure ecosystem, we've not even done like the KMS integration. So there's a bunch of things like that I want to get the team, you know, doing an end to end deployment of validating and figuring out where the warts are and kind of making sure it works so that we actually have all that story buttoned up. But, you know, the hard reality 

Jeff Denworth
But, you know, The hard reality of Vast is that we're not going to do anything unless there's money almost immediately at the other side of the rainbow because there's too many competing priorities right now. And so this needs to be staged according to a business plan. I have a call with Yancey and Lior on Monday saying, if I'm to be honest, I don't see how we're going to close a big deal in January. 

Jason Vallery
is that we're not going to do anything unless there's like money right almost immediately at the under other side of the rainbow because there's too many competing priorities right now sure and so this needs to be staged according to a business plan yeah and i had a i have a call with yancey and leor on monday saying you know if i'm to be honest i don't see how we're going to close a big deal in january we need this deal in january microsoft needs to 

Jeff Denworth
We need this deal in January. Microsoft needs to decide what they're going to do by January. We can talk about March, April, May and whatever, but they're going to be on their back heels from a supply chain perspective. They're not going to ever have, you said it earlier, guys from NVIDIA. We don't have enough flash to power our GPUs. Yep. So this needs to be aligned to that. 

Jason Vallery
what they're gonna do by January. We can talk about March, April, May, and whatever, but they're gonna be on their back heels from a supply chain perspective. They're not gonna ever have, you said it already, guys from NVIDIA. We don't have enough flash to power our GPUs. Yep. Yep. So. I mean, I hear all positives. Like, I agree with you on the timeline. I agree that we're up against a clock. I hear all positives. Even Pete yesterday said to me, he's like, I hear internally things are really going well. between Microsoft and MAI. And yeah, I mean, that's in alignment with what we heard from Yancey yesterday in his call with Manish. Certainly the vibe I got from Kuchal when we had dinner with him last week. But does that turn into a PO? 

Jeff Denworth
These things go way too slow. 

Jason Vallery
These things go way too slow. Well, what I'll say is like, they've never seen commercials. And, you know, are we going to, like Microsoft is a very, very slow to act company. Are we going to close a deal in January? I'd certainly love to see that happen, but I'm not going to count my chickens before they hatch, so to speak. I know. But anyway, all this stuff needs to be aligned towards a revenue plan where either Microsoft's a customer or somebody else's, but we're not going to do this stuff for the goodness of our hearts. Yeah. Then your last ask. By the way, that might compel you to do 

Jeff Denworth
I know. But anyway, all this stuff needs to be aligned towards a revenue plan where either Microsoft's a customer or somebody else's. But we're not going to do this stuff for the goodness of our hearts. And by the way, that might compel you to do part three before you do part two because you got Walmart with the boot on your neck. Sure, but the scaffolding, the APIs vary, but the scaffolding needs to be roughly the same. Why would I develop something just for Microsoft or just for Google? 

Jason Vallery
Part 3 before you do Part 2 because you got Walmart with the neck on your, with the boot on your neck. Sure. Yeah. I mean, that's all Google Cloud work, right? That's not Azure work. Sure, but the scaffolding, the APIs vary, but the scaffolding needs to be roughly the same. Why would I develop something just for Microsoft, just for Google? Yeah, I think that's mostly right. Google has a very different change notification system. It doesn't work the same at all. Excuse me. 

Jeff Denworth
Excuse me. 

Jason Vallery
Yeah. So then your last point of what you want me to prepare, and this is in the document as well, probably flesh it some more, but it's kind of like, what are the first party integration opportunities? So like what, like of all of the Azure services, and there are many, like how might they play nicely with VAST? Like what is the scenario you light up? And then what is the integration story? And then what is needed from us to realize the vision? That's in there. I would say like, Give me. 

Jeff Denworth
Right. Okay. 

Jason Vallery
Across all of them, we also sort of layer the lens of what the actual market opportunity looks like. I think the one that's compelling is obviously Foundry. What the Foundry stories are and how it connects is a deeper conversation around like what are we really trying to solve for. The way I think about Foundry primarily is its use cases for customers that are building AI applications and pipelines. And so that really is two scenarios, which is like what is the application state store and storage platform? and RAG storage story. In all three of those- 

Jeff Denworth
Are we having any conversations with them? Because we should start. Lior doesn't know shit about key values, vectors, or anything. 

Jason Vallery
So we're having any conversations with them? Because we should start. Right. So we had, I mean, Lior had a conversation with them. I haven't had a conversation with them. Lior doesn't know shit about key values, vectors or anything. Gotcha. Yeah. I mean, we were supposed to meet with them last week when we were there and then that meeting fell through so we didn't actually get a face to face. I agree. What I would say is that the way the founder team has implemented this is that the compute actually can run in the customer's tenant. So when they deploy, They deploy it on a VM on your behalf that's managed by Foundry, but it sits within your virtual network. So it kind of breaks that virtual network boundary. And then once it's inside your virtual network as a customer and your tenant, it can talk to whatever is also in your virtual network. So if we expose an S3 endpoint into the customer's network or if we expose an NFS endpoint into the customer's network, Foundry can speak to both of those. And that scenario is already sort of lit up today. No engineering necessary. where this comes into play of like other scenarios would be if we wanted to do like a very purpose-built key value integration with their key value with their inference framework then you're actually talking about like integration with the foundry plumbing if there was something that was differentiated above our s3 api why do you need q value well why do they need it versus why do we want it and what's the long-term opportunity i think there's three different questions um short-term i mean you're familiar with the 

Jeff Denworth
Why do you need Q value? 

Jason Vallery
of what a key value cache provides. How that key value cache from a dynamo... Key value caches don't use key value stores at all. Well, they're starting to be able to page things in and out of network attached stores. So not necessarily key value stores. That's not a key value API. Right. That is just a NFSS3 kind of endpoint. It's not a key value endpoint. Right. I totally agree with that. So that's the case today. Now, if the case for that expands to the point where it's doing actual lookups against keys, 

Jeff Denworth
KeyValue Cache's don't use key value stores at all. Sure, but that's not a key value API that they're using. 

Jason Vallery
then that's where it changes to be a key value store. I think that's a where the puck's moving question versus where the puck's at. 

Jeff Denworth
I have no clue that's a question for NVIDIA and the videos like tripling down I'm not sure 

Jason Vallery
I have no clue. That's a question for NVIDIA. Not just NVIDIA, right? Not everybody's building on Dynamo. They're not building this on Dynamo. They're being agnostic of the underlying inference framework because they see that also they will support multiple types of accelerators. 

Jeff Denworth
Well, but if that's the case, then I understand. Sorry. 

Jason Vallery
Well, Microsoft has their own framework here. I understand. Yeah. Sorry. It's okay. So, I mean, how they end up implementing this is different than how NVIDIA implements it or may choose to implement it. And that's all a very evolving space. So that conversation could happen. And that was the one I was pushing for. But it hasn't happened. 

Jeff Denworth
Sounds like you're maybe making up some technology requirements that might not exist. 

Jason Vallery
Sounds like you're maybe making up some technology requirements that might not exist. I mean, I agree. And I'm only layering it from the lens of that's where I know opening eye to be headed. And so if opening eye is going there, that probably means everybody else will be there in a year. 

Jeff Denworth
Okay. What about fabric? I would think that's the other place where we could kill it. 

Jason Vallery
Okay. What about fabric? I would think that's the other place where we could kill it. Yeah, I mean, again, it's a similar story with the VNet integration, right? So what we need to actually focus then on from an engineering perspective is how we break through that private link kind of scenario, right? So for all of these, I mean, if you look across the entire spectrum of managed services that Azure has, there's always a story of how do you then connect it back to customers' infrastructure, and that is to break the VNet wall. And there's a few different methodologies for doing that. There's a private link service where customers can expose an endpoint into an Azure managed service. Supporting that is the key answer. How we do that with Polaris and how we do that with our deployments, something I need to spend time with. Maybe, but what if, you know, this is what I was trying to get to is like, what are the first party offerings that come from Microsoft, particularly the ones that are rooted deeply in open source software. So if I take, for example, an event streaming service, 

Jeff Denworth
Maybe. Maybe, but what if, you know, I don't, this is what I was trying to get to. It's like, what are the first party offerings that come from Microsoft, particularly the ones that are rooted deeply in open source software? So if I take, for example, an event streaming service, what's that built on? Kafka? Doubt? Is it fast? Is that Kafka compatible? 

Jason Vallery
What's that built on Kafka? Nope. Internal system is called Event Hubs. They build their own. I mean, customers will use Kafka, but Microsoft has their own internal event streaming service called Event Hubs. Is that Kafka compatible? I think they have a Kafka compatible SDK. Okay. So part of this relates to us being able to dig into other parts of Microsoft and kind of advocate our story around how we could give them 

Jeff Denworth
Okay. So part of this relates to us being able to like dig into other parts of Microsoft and you know, kind of advocate our story around how we can give them a common set of front end APIs 

Jason Vallery
a common set of front end APIs, but a much more scalable and cost effective service delivery model. Yeah. I mean, and that's one of the things that I was hoping to tease out with this document. Like I want a year of work for Lior, like Lior, here's your wins. Bing, bang, boom, boom, boom, boom, boom. Yeah. I think to go back to your statement of like, you need a book of business sitting on the other side of engineering commitments. It's similar here. 

Jeff Denworth
but a much more scalable and cost effective service delivery model. And that's one of the things that I was hoping to tease out with this document. I want a year of work for Lior. Like, Lior, here's your wins. Bing, bang, boom, boom, boom, boom, boom. 

Jason Vallery
All of these start with us getting the philosophical. I'm not saying we do a single amount of work, but I want to map Microsoft internally. Say, okay, here's the things that we need to do to enable, let's say, sell through, but here's the things that we can do from a sell to perspective, give them a much better service than what they take to market today. That's ultimately what we're doing with Microsoft AI. 

Jeff Denworth
Oh, all of these start with us getting the, you know, kind of the philosophical win. I'm not saying we do a single amount of work, but I want to map Microsoft internally. So, okay, here's the things that we need to do to enable, you know, let's say, sell through, but here's the things that we can do from a sell to perspective, give them a much better service than what they take to market today. That's ultimately what we're doing with Microsoft AI. 

Jason Vallery
Yeah. I mean, our challenge, if you think about it from a just pure raw infrastructure perspective, is how Azure is built. Like Azure is a core team that builds compute, network, and storage, right? Manish, Narayan, and whoever replaces Needy and Eric Lockhart's team. Those are like the three pillars, right? And then everything else that has an Azure label on it is built on top of those primitives. But those teams have have an opportunity to do a deeper layer of integration. And the real rubber meets the road is always on the network piece because there's opportunities for Microsoft to expose underlying infrastructure to first-party services that aren't exposed to customers and partners. And so to break through that Azure wall, you have to leverage, if you're a partner and don't have the ability to go convince them to do first-party kinds of engineering, the networking. And so how do you connect something running in a vast LSV4 VM up to one of those managed services becomes the challenge and it's all tied to private link. So that's the only solution we have available to us whereas those all of those customers Synapse, OneLake, Fabric, Foundry, whoever you want to name all have opportunities to access that infrastructure directly and then it's a security data exfiltration how does all of that stuff come together to tell a customer compliance story. Okay, I'm at the post office. Hey, can I just get postage in this regular mail? Sorry, Jason, one second. So the fundamental question is like how do we become a regular now? Sorry Jason, one second. That was amazing. 

Jeff Denworth
That was amazing. Thanks. I got it in and out of the post office in less than two minutes. To a lawyer. 

Jason Vallery
Thanks. I got it in the post office in less than two minutes. Excellent. Shipping a Christmas present, I hope? To a lawyer. No, that is fun. My point is it's all about an hour-to-day. There are rich people lawyer problems, not like an divorce lawyer or a criminal lawyer. There's always a good reason to talk to a lawyer. Actually, no, there's very few good reasons to talk to a lawyer. 

Jeff Denworth
Is there rich people lawyer problems, not like divorce lawyer or criminal lawyer? 

Jason Vallery
My point is, all of the Azure services really come down to the question around how network integration works and how we can expose based on the primitives that Azure gives us compared to what they have access to as a first-party service. And as a first-party service, they have access to things that we won't have short of Microsoft, you know, opening the kimono, so to speak. There's a thing called network security perimeter that enables first-party services to with storage at a deeper layer that removes the network complexity. And we don't have access to that because we're not a first party service. And so that's the problem. But some of this may change, right? The point is to kind of presume that. But anyway, I think we're getting too far down the rattle of like everything that you know that doesn't really matter at this point. They need to want it. Yeah. We have to tell a differentiating story. And that means that we're doing better price performance features that aren't 

Jeff Denworth
Yeah, but some of this may change, right? The point is to kind of presume that. So anyway, I think we're getting too far down the rat hole of like everything that you know that doesn't really matter at this point. They need to want it. Yes. Yeah, yeah, yeah, yeah. So that's the thing that needs to be. Okay, there's a few things. One is we need a real near term roadmap. Two is we need to know the attack vectors that we want to hit as we as we go and we 

Jason Vallery
So that's the thing that needs to be, okay, there's a few things. One is we need a real near-term roadmap. Two is we need to know the attack vectors that we want to hit as we go and we start to expand the business development push. Yeah. The business development push on cell to or cell with. Yeah. So through. Yeah. Yeah. And then we can also put some pressure on them through OpenAI, like, you know, 

Jeff Denworth
as we start to expand the business development push. Yep. Yep. And then, you know, we can also put some pressure on them through OpenAI. Like, you know, you're getting to Louie and saying, here's some kick-ass, you know, event streaming shit, whatever. 

Jason Vallery
You know you're getting to Louie and saying here's kick-ass you know event streaming shit whatever just pick that as an example and Microsoft takes notice or bro you need some bass like then maybe that's something else starts but you know if you tell the common set of stories to both open AI and Microsoft and they're they're compelling enough then good things should follow. Yeah I think we're already seeing good things but you're right it's the continuous drumbeat or jackhammer or whatever you call it in the chat. Oh but but I I want 

Jeff Denworth
Let's just pick that as an example. And Microsoft takes note and it's like, we need some bass. Like, then maybe something else starts. If you tell the common set of stories to both OpenAI and Microsoft, and they're compelling enough, then good things should follow. Oh, but I want different parties to now start to take notice. This is just starting to happen in NVIDIA. It took too fucking long. It took years and years and years for them to realize we have more than just an object store. 

Jason Vallery
I want different parties to now start to take notice. Like this is just starting to happen in NVIDIA. It's been too fucking long. It took years and years and years for them to realize we have more than just an object store. So and that's all our sales team really that's the only play they know how to run. So I'm asking for you to help like grow the dimensions of the sales scope so that we actually can root ourselves super deeply. The second that the Fabric team really understands what we have they're going to go gaga. 

Jeff Denworth
And that's all our sales team really, that's the only play they know how to run. So I'm asking for you to help like grow the dimensions of the sales scope so that we actually can root ourselves super deeply. The second that the Fabric team really understands what we have, they're going to go gaga. Which is particularly true for the Flash, you know, where they're probably running a lot of, 

Jason Vallery
One of the good conversations we had last week, and Alon joined us for this, was with Microsoft CPU. Which is particularly true for the Flash. They're probably running a lot of this shit on just standard, whatever EC2, or VM whatever's. And so your point is, it's all an object is very little Flash, blah, blah, blah, blah, blah, true. But where we're going is to compete with stuff that will draw 

Jeff Denworth
this shit on just standard whatever EC2 or VM whatever's, right? And so your point is, its own object is very little flash, blah, blah, blah, blah, blah, true. But where we're going is to compete with stuff that we'll draw from either, you know, remote block volumes or local volumes. And in both cases, we can save them a ton of info. 

Jason Vallery
from either remote block volumes or local volumes. And in both cases, we can save them on a MIFTRO. Yeah. One of the good conversations we had last week, and I'll join for this one, I thought it went very well, was with Microsoft CTO org. The CTO is responsible for like, how do all of these stories come together? And I think Alon did a great job of pitching the vision there. 

Jeff Denworth
That's cool. 

Jason Vallery
Hopefully that will bear fruit because that's the team that's talking to Foundry, that's the team that's talking to Fabric and they're trying to come up with like what is the future, how do these things come together, what is the infrastructure demand for these scenarios in sort of like a consolidated way. Yep, okay good. While I've still got a few minutes though, maybe we could pivot to SCO and what you want to see there. So I think I said user conference, you've said SCO now twice. Sorry, are they like the same, I mean maybe I'm just complaining things, but they're 

Jeff Denworth
Yep. Okay, good. So I think I said user conference. You've said SCO now twice. 

Jason Vallery
the same week and they have the same like different agenda obviously different audiences but you're saying in front of the customers and that's sorry my mistake okay um so there's probably a good case for 

Jeff Denworth
Okay. So there's probably a good case for you to have a session at SCO. And there's an extreme amount of overlap in the topics. Well, let me say a significant amount of overlap in the topics. But two things. One is we're earmarking a session for you. There's like 12 customer sessions and breakouts, and then there's like five vast breakouts. 

Jason Vallery
you to have a session at sco okay and there's um an extreme amount of overlap in the topics Let me say a significant amount of overlap with the topics. But two things. One is we're earmarking a session for you. There's like 12 customer sessions at the breakouts and then there's like five fast breakouts. 

Jeff Denworth
One of them is like vast database updates stuff like that. We have a session that's called like building an AI cloud with vast. Now you could argue that Morty is the better of the two spokespeople for this given if I just if I just did it measured by subject matter familiarity. Not really a good presenter and ultimately I want you to kind of be the lord of all things cloud so I'm putting you in the hot seat for this one. 

Jason Vallery
One of them is like here, you know, fast database updates, stuff like that. We have a session that's called like building an AI cloud with VAST. Now, you could argue that Morty is the better of the two spokespeople for this given, if I just did it measured by subject matter familiarity. Not really a good presenter, and ultimately I want you to kind of be the lord of all things cloud, so I'm putting you in the hot seat for this one. Okay. Now, it's basically everything other than how do you build storage for Microsoft. Is that true? No, that's not. 

Jeff Denworth
Now, it's basically everything other than how do you build storage for Microsoft. Is that true? No, that's not true. It's actually the same thing that you used to do. It's just, you know, less how to build the storage yourself and more how to take VAST and integrate it into a set of cloud services that you want to build. And so part of it is, you know, in the use cases, they come from AI labs and enterprises. 

Jason Vallery
True. It might be the same thing that you used to do. It's just, you know, less how to build the storage yourself and more how to take VAST and integrate it into a set of cloud services that you want to build. And so part of it is, you know, in the use cases that come from AI labs and enterprises that will draw from these AI clouds. 

Jeff Denworth
that will draw from these AI clouds. Part of it is best practices for establishing multi-tenancy. Part of it is unveiling the work that we want to do with control planes and stuff like that. And so, you know, I'm wandering a little bit mentally just because I don't have the full agenda built out just for your session. But you basically should walk out of there as some neocloud just got $100 million of funding saying, okay, you know, VAS is what CoreWeave uses, so I'll use that. 

Jason Vallery
Part of it is best practices for establishing multi-tenancy. Part of it is unveiling the work that we want to do with control planes and stuff like that. And so, you know, I'm wandering a little bit mentally just because I don't have the full agenda built out just for your session, but you basically should walk out of there as some neoclou just got a hundred million dollars of funding saying, okay, you know, that's before we use this values that and here's all the shit that I need to do. 

Jeff Denworth
And here's all the shit that I need to do. Yep. But it also starts with like the basics. Don't assume that everybody uses us for storage in the audience. 

Jason Vallery
Yeah, it is the NeoCloud in a box that we've talked about and how would I go to market with it? So this is thinking about it from a PM lens of what are your revenue opportunities? How do you position this kind of mentality? Like what are the services you can expose and how might your target customers leverage them? But it also starts with like the basics. Don't assume that everybody uses us for storage in the audience. Your audience is actually the camera. 

Jeff Denworth
Your audience is actually the camera. So all this shit is going on. And it's a 45-minute session intended to help people get up to speed on, hey, why is VASP being used? Where are they going? And how do I build this into my business? Just on that topic, though, 

Jason Vallery
So all this shit is going on YouTube. Sure. And it's a 45 minute session intended to help people get up to speed on, hey, where, why is that being used? Where are they going? And, and, you know, how do I build this into my business? Yeah. Um, so one of the things that I'm, I just, just on that topic though, uh, sales kickoff, you probably have another session about like, Hey, fuck. 

Jeff Denworth
You probably have another session about like, hey, fuckheads, cloud's real now, so can we please get going and start selling some stuff? And all the considerations that go along with that. There's still a lot of people that believe cloud's not real, including Lior. Sure. And, you know, the definition of every startup is to not go to the customer. 

Jason Vallery
"Cloud's real now, so can we please get going and start selling some stuff?" Sure. And all of the considerations that go along with that. Sure. There's still a lot of people that believe Cloud's not real, including Lior. Well, I mean, it's a limited set of scenarios that we can support today, but agree. Like, there's something there. There are opportunities. And, you know, the definition of every startup is to not go to the customer that needs every fucking feature and be like, "Would you buy from us?" 

Jeff Denworth
that needs every fucking feature and be like, "Would you buy from us?" 'cause that's not how you start things up, right? I'm not looking for 100,000 cloud customers, I'm looking for the first 10. Why? 

Jason Vallery
That's not how you start things up. I'm not looking for 100,000 cloud customers. I'm looking for the first 10. Yeah. Yeah. I mean, it is the, like, to be the dead horse, it's the burst on cloud scenario that we can realistically do today. It's not cloud as primary storage. Why? Scale up, scale down, offload to object, capacity, price performance, they all really kind of suck compared to what you can get directly from the cloud vendors. Like, there's no obvious, value we're bringing over top what you totally don't agree with you everything I just talked about with event streaming I could crush it in the battery sure vast database I could crush it you're thinking like an s3 guy welcome to vast read the fucking white paper understand that we have a database I love it has a plug-in for spark I love you Jeff let me let me let me pivot back to what what we want to say at the user conference and call it like one of the things that I'm 

Jeff Denworth
Totally don't agree with you. Everything I just talked about with event streaming, I could crush it in the cloud. VAS database, I could crush it. You're thinking like an S3 guy. Welcome to VAS. Read the fucking white paper. Understand that we have a database. Know that it has a plugin for Spark. 

Jason Vallery
What I'm a little nervous about when you start describing event streaming and database and all of those amazing features, I actually think they have a real place in the cloud. Where I actually don't know that they have a place is on the quote, "Neoclouds," the NCPs. Because all of those workloads, it's Spark or Kafka or whatever, they need CPUs. And I haven't met a Neocloud yet that has CPU capacity. - Then you haven't talked before, we... 

Jeff Denworth
Hold on. And then you haven't talked to Corweave. 

Jason Vallery
out CPU at scale? HPC kind of clusters? Listen, we're building a market. We're building it together. You're acting like a historian. And what I'm trying to say is that at the end of the day, a NeoCloud that needs to be successful will have to acknowledge the fact that they can't just sell flops by the pound. And if that's true, then they have to evolve their service offering. Lambda will be there. And you know this because you manage all the NeoCloud 

Jeff Denworth
Relative, listen, we're building a market. We're building it together. You're acting like a historian. And what I'm trying to say is that at the end of the day, a NeoCloud that needs to be successful will have to acknowledge the fact that they can't just sell flops by the pound. And if that's true, then they have to evolve their service offering. Lambda will be there. And you know this because you manage all the NeoCloud relationships by virtue of you managing Morty. 

Jason Vallery
Relationships by virtue of you managing Morty Landia will be there. I know you don't know this. Announcing that they're going to launch the entirety of the VAS portfolio. But then we need to map those back to the different use cases that AI labs will bring to the table, right? Stay on event streaming. Great for reinforcement learning. VAS vector database. We've got a 12 petabyte POC starting up at XAI next couple weeks. 

Jeff Denworth
Lambda will be there. I know you don't know this. Announcing that they're going to launch the entirety of the VAS portfolio. And then we need to map those back to the different use cases that AI labs will bring to the table. Right? If I stay on event streaming, great for reinforcement learning. VAS vector database. I've got a 12 petabyte POC starting up at XAI next couple weeks. But your logic is because they do not have a service, they will not have a service. These things evolve in parallel. 

Jason Vallery
I'm sure it makes sense for them but I'm sure they also have like a big CPU cluster. I'm with you what I would love to understand and I'll have this guy. Your logic is because they do not have a service they will not have a service. No I'm not saying that. These things evolve in parallel. Yeah exactly I would love to understand like their thinking and roadmap around this and if that that is like a market they're planning to go try to crack which is more than just GPU clouds they want to go and be an HPC cloud or an analytics cloud or an application cloud. And if those are true statements. It's an AI cloud. You're saying HPC and analytics, but those are practices that live within AI. You know, Snowflake's biggest customer is open AI. Databricks' biggest customer is open AI. Are they analytics companies? Maybe, maybe not. Are they AI companies? Well, if their biggest customer is open AI, they're doing something pretty right in AI. A hundred percent. My macro point is. 

Jeff Denworth
I think it's an AI cloud. You're saying HPC and analytics, but those are practices that live within AI. You know, Snowflake's biggest customer is open AI. Databricks' biggest customer is open AI. Are they analytics companies? Maybe, maybe not. Are they AI companies? Well, if their biggest customer is open AI, they're doing something pretty right in AI. Okay, so the point is, don't be so pedantic. 

Jason Vallery
- You're so pedantic. - I'm not being pedantic. What I'm pointing out is that the way that's playing out today is that the hyperscalers are the ones that are owning the CPU bound workloads and the NeoClouds are the ones that are owning the GPU workloads. Do I state that that is the long-term way this plays out? No, but I haven't seen any signals of investment that the NeoClouds are wanting to go win the breadth of those workloads. 

Jeff Denworth
Did I not just tell you about Lambda? You actually just got a signal three seconds ago. And that's the whole point of Morty's job right now, by the way, Mr. Valerie. Like, his job is to go make that fucking market. So if you don't have any signals, that means we are failing at our job. 

Jason Vallery
- Did I not just tell you about landing? - You did tell me about landing. - You just got a signal three seconds ago. - I got my first signal. I got my first signal. And that's the whole point of Morty's job right now, by the way, Mr. Valerie, like his job is to go make that fucking market. So if you don't have any signals, that means we are failing at our job. Sure. I have a one-on-one with Morty today. I'll ask him more about it. I mean, I brought this conversation in and just said, like, I think going into this NeoCloud in a Box thing unlocks this, but then you also have to know that they're planning a vision around how they build out their cloud. We have to work with them. We have to work with them. Yeah. 

Jeff Denworth
We have to work with them. The CPUs will come as they have demand. It's so much easier to stick CPUs in a 100 megawatt data center than it is GPUs. Yes, yes, yes. And so anyway, don't get focused on the CPUs. Let's go make a market. That's one of the things that I need you to help with. Help Morty with. 

Jason Vallery
The CPUs will come as they have demand. It's so much easier to take CPUs in a 100 megawatt data center than it is GPUs. Oh, great. There's a lot less complexity. Air-cooled AMD can just go in there and drop some racks, a lot less density. Makes sense. Yes, yes, yes. And so anyway, don't get focused on the CPUs. Let's go make a market. That's one of the things that I need you to help with. Help more to you with. Like, I've been waiting for when are the QBRs. Two months ago, we started making the, here's a template for the QBRs. I don't know if we've actually had 

Jeff Denworth
QBRs. Two months ago, we started making the, here's the template for the QBRs. I don't know if we've actually had one. It sounds like you don't either. And if we all agreed, this is what we're going to do. I would not call that a QBR. And CoreWeave is such an exceptional case that I don't think it makes sense to build a worldview around. 

Jason Vallery
One. Fair. It sounds like you don't either. Have one with a specific customer? I mean, there was the thing at CoreWeave last week. I don't know if you call it a QBR, but I mean, I know the team got together with CoreWeave last week. I would not call that a QBR. Yeah. And CoreWeave is such an exceptional case that I don't think it makes sense to build a worldview around. Yeah. But, you know, CoreWeave might be one of those clouds that 

Jeff Denworth
But, you know, CoreWeave might be one of those clouds that could move faster with us than anybody else. So I'm not ruling them out. I'm just saying, you know, they march to the tune of their own drum. But we have now Sharon AI that's saying they want to do stuff. We have Lambda. We have N-Scale saying they want to do this stuff. The market's kind of primed. We need to push them over the hump. 

Jason Vallery
to move faster with us than anybody else. So I'm not ruling them out. I'm just saying, you know, they march to the tune of their own drum. But we have now Sharon AI saying they want to do stuff. We have Lambda. We have N-Scale saying they want to do this stuff. The market's kind of primed. We need to push them over the hump. Okay. That is in your charter of like the things in your day job. And OpenAI isn't consuming that much of your time right now. 

Jeff Denworth
That is in your charter of the things in your day job. And no offense, but OpenAI isn't consuming that much of your time right now. And so until that gets hot and heavy, maybe go manage Morty and kind of get this cloud in the boxing a little bit more buttoned up. You're going to have to speak on stage about it in two months' time. I know, I know, I know. 

Jason Vallery
and get this thought of the boxing a little bit more buttoned up. Sure. You're going to have to speak on stage about it in two months' time. Well, yeah. So to recap, yes, you're right. OpenAI does not consume much of my time. Microsoft has been a fair bit also just being on the road and trying to meet the teams and travel, and I've still got some of that to go do with Iceland and otherwise. Ultimately, having the right team structure will be part of this. I am still very interested in making sure I have the right people to support all of these different conversations. You know, Morty seems great. He's also kind of already on his set of tasks. And so I haven't like leaned on him to go do anything for me other than to just kind of touch base and see how things are going. I'm not asking him to do anything for you. I'm asking him to do the things he already said he was going to do. Agreed. I will push on him. I guess he told me he was actually in the hospital all week. So I don't know. I'm not sure what happened there, but I'm meeting with him this afternoon. Yeah. That needs to start to crystallize over the next two months. A, because it will inform how you think about 

Jeff Denworth
I'm not asking him to do anything for you. I'm asking him to do the things he already said he was going to do. And if he needs help, help him. That needs to start to crystallize over the next two months. A, because it will inform how you think about content. But we need to be going to these guys with very, very clear user stories. Here's something that you can sell. And this is why I wanted to get you into it, because you had full purview of this at Microsoft. You can't stick your head in the sand there and say, you need to help them. 

Jason Vallery
content, but we need to be going into these guys with like very, very clear user stories. Here's something that you can sell. Yeah. And this is why I wanted you to get, to get you into it because you had full purview of this at Microsoft. They can't stick your head in the sand there and say, you know, you need to help. Well, you know, like the big picture question about the Neo clouds that I have all up and I'm sure, you know, you know them way better than I do. Cause you've had all the meetings with them that I haven't had, but like, how does this actually play out? It's great when you have a narrow case like I'm going to go do AI training and I can go drop a data center and I can do this GPU as a service kind of business model. And that makes sense to me. But if you want to crack the cloud knot and they want to actually go try to compete with the hyperscalers on the breadth of workloads, that's a whole complex beast. And is that their ambition or not? And then what kind of consolidation comes into play? I think there's a diversity of answers to that question, depending 

Jeff Denworth
I don't know. 

Jason Vallery
I don't know their long term business strategies in this regard. I mean, what is your take? 

Jeff Denworth
They're not formed. This market emerged three years ago. Some of these companies don't have product managers. They're not Jason Valerie. They haven't been in the market for 20 years. You use the term tenured. Stop thinking in those terms. 

Jason Vallery
They're not formed. This market emerged three years ago. Some of these companies don't have product managers. They're not Jason Valerie. They haven't been in the market for 20 years. You use the term tenured. Stop thinking in those terms. 

Jeff Denworth
We have to go shape it with them. Pure and simple. And not all of them will take the same trajectory. 

Jason Vallery
We have to go shape it with them. Yeah. I'm just wondering. Not all of them will take the same trajectory. Right. Yeah. And like maybe there's a, the way we should frame ourselves is thinking about where the opportunity sits. And like, if we want to be a little bit more narrow and opinionated about what we want to light up, because like trying to go and say, we're going to enable them to compete across the breadth of what a hyperscaler already has in market is I think a fool's errand. But if there's like a small set of scenarios that we think are valuable and we can give them the right tools to do that, then that's That's more interesting. Yes, sure, sure. Bar cluster, an analytics system, an enterprise data warehouse to capture model feedback and event streaming systems so that you can actually, you know, stream telemetry natively from a platform for everything from observability reinforcement learning. You're already in a really good position. You add serverless, something on top like, oh, by the way, you can also get program functions into this thing for certain parts of your pipeline. Okay. 

Jeff Denworth
Yes, sure, sure. Bar cluster, an analytics system, an enterprise data warehouse to capture model feedback and event streaming systems so that you can actually, you know, stream telemetry natively from a platform for everything from observability reinforcement learning. You're already in a really good position. You add serverless, something on top, like, oh, by the way, you can also just program functions into this thing for certain parts of your pipeline. Okay. So we're not going to solve it on this call, but I want to bring it to your attention, remind you, something on your plate, as you have bandwidth, and I knew you do, need help kind of moving Morty along, because we're not making progress on this topic. Now, if he's sick, then that's a whole different thing, but 

Jason Vallery
So we're not going to solve it on this call. No. But I want to bring it to your attention, remind you, someone on your plate, as you have been with, and I knew you do, need help kind of moving Morty along because we're not making progress on this topic. Yeah. Now, if he's sick, then that's a whole different thing that I didn't know about. 

Jeff Denworth
I didn't know about, but we can do this. Yep, yep. There's going to be a lot of follow-up where, you know, you're going to have a bunch of people chasing you for both of these things. Start working on those, too. Okay. 

Jason Vallery
But we can do this. Yeah. Okay. I'll work with him on what we say in February on this topic and then think about what we want to say in terms of fast on cloud readiness for scope those are what I'm hearing is my two deliverables for February yeah yep you're gonna there's gonna be a lot of file follow-up where you know you're gonna have a bunch of people chasing you for both of these things yeah start working on those two okay okay before Christmas Christmas to you too got any plans taking time off 

Jeff Denworth
I don't know if I'll talk to you before Christmas but if I don't Merry Christmas I'm going to try to go to Canada for a few days 

Jason Vallery
I'm gonna try to go to Canada for a few days. It's like 10:30. What is this? What's Canada got? Family? Canada's got some ski slopes. Probably better than family, I suppose. Oh, you killed me. I totally missed the meeting. You are a chatty Cathy. You're chatty. All right, you're, no, you're chatty. All right, listen, I'm gonna go. All right. All right. You got a lot of shit on your plate. Thanks. Bye. 

Jeff Denworth
tomorrow at 10 30 what is this Canada's got some ski slopes oh he killed me I totally missed a meeting you are a chatty Kathy All right, no, you're chatty. All right, listen, I'm going to go. You got a lot of shit on your plate. Bye. 

Jason Vallery
Bye. 

Jeff Denworth
Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. 

Jason Vallery
Okay. 

Jeff Denworth
Thank you. 

Jason Vallery
- 

Jeff Denworth
Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. 

Jason Vallery
I'm sorry. 

Jeff Denworth
Thank you. Thank you. 

Jason Vallery
. 

Jeff Denworth
Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. 

Jason Vallery
Thank you. 

Jeff Denworth
Thank you. Thank you. Thank you. 

Jason Vallery
Thank you. 

Jeff Denworth
Thank you. Thank you. Thank you. Thank you. Thank you. 

Jason Vallery
Thank you. 

Jeff Denworth
Thank you. Thank you. 