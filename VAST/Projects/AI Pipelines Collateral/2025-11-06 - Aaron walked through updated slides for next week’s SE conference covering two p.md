---
type: "Projects"
title: "Review of Tech Summit AI Pipeline Slides"
date: "2025-11-06"
project: "AI Pipelines Collateral"
folder: "Projects/AI Pipelines Collateral"
participants: "Aaron Chaisson, Allison Boerum, Jason Vallery, Glenn Lockwood"
tags:
  - "type/projects"
  - "project/AI Pipelines Collateral"
source: "00 Inbox/Transcripts/20251106 1500 Parallels Transcription.txt"
---

# Review of Tech Summit AI Pipeline Slides
**Date:** 2025-11-06 · **Project:** AI Pipelines Collateral · **Folder:** Projects/AI Pipelines Collateral

> [!summary] Status Summary (toward next milestone)
Aaron walked through updated slides for next week’s SE conference covering two pipelines: model training (with feedback loop) and enterprise inference (RAG). The team discussed where Kafka belongs (as an event-stream ingestion head and RL feedback path), clarifying that embeddings are precomputed and not done inline during inference. They agreed to reflect database usage in data prep and potentially for KV cache metadata, while noting current KV cache access is via NFS, with future GPU-direct-to-object possible. Terminology will emphasize fine-tuning/reinforcement learning, with “online RL” as a continuous loop concept. A key debate was whether to include Data Engine and function triggers in an SE-focused deck: value for vision vs risk of confusing storage-centric SEs. Jason shared analogous Ray-oriented diagrams illustrating how VAST Datastore/Data Engine/Database bookend popular workflows. Aaron will refine diagrams to show the continuous loop, the chatbot-to-inference linkage, and clearer sequencing in RAG. He’ll also consult SE leadership on Data Engine inclusion and will incorporate feedback on Kafka and database placement.

## Key Facts (scope, metrics, links)
- Audience: VAST SEs at next week’s Tech Summit/SE conference.
- Pipelines covered: model training (continuous loop) and enterprise inference (RAG).
- Kafka likely serves as an event-stream ingestion head and RL feedback path.
- Embeddings are precomputed via NIMs on Kubernetes; vector DB stores results.
- Inference flow: retriever + re-ranker against vector DB, then model response.
- Current KV cache access is via NFS; GPU-direct-to-object is a future option.
- Database can assist data prep (analytics tables → Parquet) and logging/archives.
- VAST components mapped: Datastore, Database, SyncEngine, InsightEngine, Data Engine.
- Primary buyers are NCPs/infrastructure providers; model builders are indirect.
- Jason to share Ray workflow diagrams showing where VAST augments Ray.

## Outcomes (progress this session)
- Slides are directionally correct for an SE audience.
- Agree to emphasize fine-tuning/reinforcement learning terminology, with online RL noted.
- Plan to show precomputed embeddings and clearer inference linkage in RAG.
- Database will be shown as an option in data preparation and possibly KV cache metadata.
- Kafka will be depicted as an ingestion/feedback head rather than a core storage tier.
- Aaron will consult SE leadership before deciding how prominently to include Data Engine.
- Jason will provide Ray-oriented diagrams to inform slide refinements.

## Decisions (architecture, resourcing, priority)
- Use fine-tuning/reinforcement learning phrasing in the training loop.
- Represent embeddings as precomputed in the vectorization phase.
- Add Database to data preparation and logging/archives in the diagrams.
- Show current KV cache usage via NFS in inference depictions.

## Risks (schedule, technical, external deps)
- Including Data Engine and function triggers may confuse storage-centric SEs; mitigate by framing as optional vision content and prioritizing storage-led wins.
- Ambiguity in Kafka placement could mislead field teams; mitigate with a simple pattern: event-stream head for ingestion and RL feedback.
- Overstating continuous training vs major releases could create credibility gaps; mitigate with notes on generational vs point releases.
- Tight prep timeline before next week’s conference may limit slide refinements; mitigate by prioritizing critical clarifications (RAG sequencing, Kafka, database roles).

## Open Questions
- Precisely where to depict Kafka heads and loops on the training diagram?
- To what extent should Data Engine and function triggers be included for this SE audience?
- Should database be explicitly shown for KV cache metadata or left as future option?
- What online RL cadence example (if any) should be shown without overcommitting?
- Any additional SE leadership guidance on balancing vision vs storage-first messaging?

---

## Action Items (critical path first)
> Use `📅` for due; optionally include `⏳` scheduled, `🛫` start, and `🔁` recurrence; set priorities to shape urgency views.  
- [x] Refine training slides to show continuous loop, clarify pretraining vs tuning, and depict fine-tuning/reinforcement learning. @Aaron Chaisson ⏫ ✅ 2025-11-08
- [x] Adjust RAG slides to show precomputed embeddings (NIMs on K8s), retriever and re-ranker flow, and explicit chatbot-to-inference linkage. @Aaron Chaisson ⏫ ✅ 2025-11-08
- [x] Depict Kafka as event-stream ingestion head and RL feedback path; remove from core storage lane. @Aaron Chaisson 🔼 ✅ 2025-11-08
- [x] Add Database to data preparation and logging/archives; note optional role around KV cache metadata. @Aaron Chaisson 🔼 ✅ 2025-11-08
- [x] Consult SE leadership on including Data Engine and function triggers in the deck and how to position them. @Aaron Chaisson ⏫ ✅ 2025-11-08
- [x] Share Ray workflow diagrams and links in Product Marketing drive and notify Aaron. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Present updated deck at next week’s SE conference. @Aaron Chaisson 🔼 ✅ 2025-11-08

### Follow‑Ups / Reviews
- [x] Confirm final decision on Data Engine inclusion after SE leadership review. @Aaron Chaisson ⏫ ✅ 2025-11-08
- [x] Validate with Glenn that KV cache representation (current NFS, future GPU-direct-to-object) matches engineering reality. @Aaron Chaisson 🔼 ✅ 2025-11-08
- [x] Distribute Ray diagram links and incorporate any applicable patterns into slides. @Aaron Chaisson 🔽 ✅ 2025-11-08

### Next Standup/Review
- Next meeting (if scheduled): **(none)**

---

## Task Views (this note only)
```tasks
not done
filter by function task.file.path === query.file.path
group by priority
sort by priority
sort by due
```

## Original Transcript
[00:00:00.00]  Jason ValleryYeah, I grew up duty, and I don't know, 2016 era, I went and lived in Seattle for a little while in the Redmond area, part of the Mothership thing, but Northwest isn't for me, and I grew up here in Colorado, so we moved back.

[00:00:15.72]   RemoteVery good. Very good. What about you?

[00:00:18.73]  Jason ValleryWhere are you based at?

[00:00:21.39]   RemoteI'm in Massachusetts. I'm just outside of Boston.

[00:00:25.74]  Jason VallerySurprising number of vast folks I keep bumping into that are apparently in Boston. It seems like there's a lot of folks in the area.

[00:00:33.17]   RemoteWell, so EMC was based out of Boston, out of Hopkinton, so when, you know, the world's number one storage vendor, and then we are a storage player, so there's a lot of storage people in the Boston area.

[00:00:45.15]  Jason ValleryMakes sense. You know, that's true here. I live just outside Boulder and there's a ton of storage companies. What's funny about me though is I've never worked for any of them. I found my way into storage through a different route. But you know, NetApp is here, Spectralogic, IBM's storage division, a whole bunch of random startups that have come and gone or been merged. and Seagate's headquarters are here. Never worked for any of them.

[00:01:13.10]   Remote- Yeah, I think there's, yeah. I think most of the storage players have stuff, Boulder's the hotspot for that, isn't it?

[00:01:21.73]  Jason Vallery- Yeah, the Seagate's headquarters is like a mile from my house, which is funny.

[00:01:27.71]   Remote- Yeah, that's right.

[00:01:30.02]  Jason ValleryJason I used to work with Peter Imming. Peter Imming? Oh he was he reported to me

[00:01:35.36]   RemoteUntil I switched roles. I was his boss. Yeah yeah he texted me the other day and said that oh I should say hi to you and reach out because he saw that you joined VAST.

[00:01:44.94]  Jason ValleryI had coffee with him not long ago. I think two weeks ago I had coffee with him just to catch up yeah he's uh he's in for a long time, too. I recruited him out of Amazon to Microsoft, and he's done well.

[00:01:57.25]   RemoteYeah, that's what he said.

[00:01:58.92]  Jason ValleryYeah, that's fun.

[00:01:59.75]   RemoteAwesome. Well, welcome.

[00:02:01.25]  Jason ValleryThank you.

[00:02:02.84]   RemoteWell, thank you guys for joining. This probably will not take a half an hour. I've updated my model training pipeline and my inferences. pipeline slides that I want to use next week at the SE conference, and so I kind of wanted to run them by you, get your thoughts and feedback, especially on data engine inclusion in the model training side. I feel like it's a leap too far right now, but I'd love to get your thoughts. So I will skip the opening of the slot of the deck. I'm just going to go to the slides in question. I want to kind of walk them through both of the pipelines to understand what the vast opportunity is and where our different components play. So obviously this slide looks very familiar. this very first one, we added Kafka to the data ingest piece of the pipeline, but my sense is it doesn't belong there. It is file object, but does anybody use message buses to populate the

[00:03:16.23]  Jason VallerySource content for model training? It's actually how OpenAI does it, is they have events streams coming out of the chat GPT conversation. So if you think about this in a disaggregated way, all the inferencing is happening all over the world and all these GPU clusters, 50 plus apps and regions core weave everywhere else, right? And those conversations are happening. The source of truth goes back to a document database. In this case, it's Microsoft's Cosmos DB, are, you know, getting updated, they're pushing it back to a centralized event bus, and I think they actually do use Kafka, to then push that into the ingestion pipeline. So it's a head over top of their ingestion pipeline for the conversations. You know, I don't know how reference that is in terms of customers that aren't at opening eyes scale. thoughts on that, but I certainly think it's a valid argument to say that is a way to get data

[00:04:12.31]   RemoteInto the system. Would it enter at this phase or would it enter at this phase? Because remember, if I built that, we had the loop back. So is that where it happens or does it happen in this phase?

[00:04:28.33]  Jason ValleryYeah, I mean, honestly, like in the argument... and I'm making, like, I guess, technically the loop really goes back into the Kafka. You know, what I would say in their architecture, there's kind of multi heads that are sitting there. There's crawlers going out and pulling data. There's data pipelines coming in from partnerships, and then there's this kind of reinforcement learning feedback loop that comes via Kafka. So. So, yeah.

[00:04:54.36]   Remote- Okay, 'cause I could move Kafka over to here, but let's go through it all and we can debate that then. So this is the flow that I basically got for it, which is a little bit of the, so it's NFSS3, Kafka can be a feeder into that core collection. Then you move into the Klemski. cleansing and prep a portion of this would, would a model trainer refer to it as curated data or is that a, is that the wrong term for that? Would that be just prepared data

[00:05:26.47]  Jason Valleryor cleansed prepared? I don't know the semantic difference between them. Okay. I don't have an opinion. I don't know. Okay. So it's

[00:05:37.62]   Remotea word that would trip anybody up then? It doesn't trip me up. Okay. That's typically going to be... Spark is going to be used to do that work and it's going to drop it on an object store? Should I add NFS in here as well because it could be file or object? Yeah, you could even

[00:05:55.54]  Jason ValleryPotentially add in data store here or database here in the same... that it's really a, at that point, they're analytics tables that then get turned into parquet files. So, you know, this is where the data engine and the database story could

[00:06:11.96]   RemotePotentially be relevant. So Kardik said that he's tried this using the vast database. Oh no, I think he said he was using parquet. he said it was kind of wonky and we haven't done a lot of work around it yet. All right, come back to the data engine. We'll get into that in a second. This obviously is the world of parallel processing. So it's gonna be your PNFS, NFSS3. We're not getting into vast specific terminology yet. This is more just generically what's underneath these pieces. Inferencing. uh portion of this as part of the training inferencing model there's the distribution catalog of the models that you're inferencing against maybe cache comes in here um and can be used as part of this inferencing piece um and then in the inference logging you've got content archives for the output logging of the whole process and then feedbacks into the system. system to create that training loop. So what you end up having is, that's the pre-training phase, and that's the tuning phase. Before I get to the, where does data store, database data, whatever's go into, you might even pull this back to this phase, or is kind of how I have it represented well.

[00:07:30.15]  Jason ValleryConcept I think is incomplete because it's deployment, it's reinforcement learning, it's tuning, it's a lot of things that kind of happen in this loop. In some ways like I mean I don't necessarily have a better idea but the whole idea of pre-training and tuning and these boxes kind of start to fade into the background where we're talking about just a continual. process that is one thing, and I think that's the paradigm shift.

[00:08:00.66]   RemoteYeah, so I was thinking like the data comes in and then you end up having this recursive loop that happens through here, until eventually you get to a point where the models ready and out it spits trained models that are ready for others to use.

[00:08:15.16]  Jason ValleryI mean, the higher point here is like the historical notion of you have to go do a big pre-training run and that is some big monolithic event isn't necessarily the case anymore as it's just a continual evolution of the model.

[00:08:30.76]   RemoteIs that for dot releases of the model or does each major release no longer have that initial training?

[00:08:49.72]  Jason ValleryI think it'll be interesting to see how the model providers do this, you know, to the earlier points of, if the base weights are always getting updated, like the notion of dot releases is gone. Clearly, that's still certainly something OpenAI is doing. Less clear what's happening with XAI behind the scenes.

[00:09:04.71]   RemoteSo would like GPT-6? be just an iteration of five or do they start with another foundation model and train it from there? Every GPT is a ground-up new architecture, but that's how OpenAI does it. It's like their philosophy. So because I know that that is a OpenAI, is it? that suggests that not everyone else is like that.

[00:09:27.56]  Jason Vallery- Yeah, and you know, they're big, like it's going major, major versions means there's architectural differences. We know their vision around six is with long-term memory and capabilities like that. So it certainly makes sense to say, this is a generational leap, but the point releases between it. I mean, they shipped 5.1 yesterday or something like that. that. So clearly they're not in a mode where it's continuously improving if they're still

[00:09:49.99]   RemoteIssuing point releases. But yeah, I'm clear what that will look like. Okay, because I, the way I'm and the way I'm imagining is, is the major release comes through this way and then this is just like agile sprints, and it just keeps looping and looping and looping ad infinitum until eventually there's another major version update and then they start from scratch. I think that I don't think that would cause any confusion. My intuition is that at least for the next six months, there might be people from OpenAI who would look at this and snicker knowingly to themselves, but the general public, I think, would accept that because that's how recommender models work as well, right? Anyone who's slinging ads using AI models is doing exactly what you described, where every week they roll up. a whole bunch of A/B testing which is really reinforcement learning and then they retrain and then re-release up like a point release and then they A/B test that and they just keep doing that on a weekly basis or bi-weekly or whatever their cadence is. Yeah I put in here I have fine-tuning retraining that was Cardix terms from a year ago or a year and a half. ago. Would reinforcement learning be added to this? Is that a new fine-tuning in reinforcement

[00:11:21.84]  Jason ValleryLearning? It's more than just reinforcements. Online reinforcement learning is where we get to where you're doing RL, but it is in a continuous loop, and that's of real-time, like you and I, interacting with it, not just their engineers interacting with it. Yeah, I mean frequency... of how this works is probably where some of the special sauce is coming into play, but in example, I can tell you that Microsoft AI's ambitions is to have that happen every 60 seconds, and so that is obviously a continuous loop process if you're kind of doing it on that frequency.

[00:11:53.47]   RemoteWow, okay. So I think, so fine-tuning reinforcement learning has is a subset of fine-tuning, and so I don't think you'll raise any eyebrows if you say fine-tuning/reinforcement learning, and then whether that is online or offline RL, a subset of RL, which itself is a subset of fine-tuning. - Okay, okay. All right, so the next build on this is. So where does VaST fall into play here? So now we're going away from the generic stuff and we're saying this is really where the data store and sync engine are. So this is gonna be your file object. Sync engine is the ability to go out and find data from a bunch of different data sources and pull it into the data store. If Kafka comes here instead of here, then I could add database here too, because the Kafka stream rolls into the database. I had the data store here for, okay, now that we're prepping, we're prepping the data, getting it ready for training. That's more of a file object use case. The training itself is. file object, the inferencing phase is file object, whether it's the models being inferenced against or whether it's the KB cache offloading cache, and then you've got data store for content archives and database for logging.

[00:13:25.26]  Jason ValleryA couple of-- I certainly think you could potentially use database for data preparation. I think the KV cache scenario is potentially more than just data store, could be database. I don't know, Glenn, maybe you've looked at this closer and have a sense on what we're likely to do here in the Dynamo integration and how all that plays.

[00:13:52.99]   RemoteJust using our NFS, right? - Yeah, that's just NFS today. Once we can do GPU direct to object, we might do that too. But right now I think we're just doing NFS. So I can add database over here, okay. So the other thing that I said was, do we add data engine? So here's the gotcha that I'm wondering on this. I was talking to Kardik this morning and his guidance was for the model training use case, I go back, this is what we're known as. We're known as a storage vendor to model builders and to the neoclouds that support them. There are hundreds of billions of dollars that's being spent right now. It's accelerating and we want our 3%, and we are proven, we've, you know, we got two more announcements in the last 48 hours about neoclouds getting us for these use cases. Do we go through? pain of trying to teach our field how to bring in the data engine triggers and functions because now you've got to start talking to data engineers, data architects who already have their well-proven processes in place. Do we want to get into the thick of trying to to do function calls to run Spark or PyTorch, executing them from our system. Yes, there's a play there. Yes, we could automate that. But given it's a land grab for dollar buckets right now, do we just go after storage? we can win there, or is it worth expanding our story to an SE audience that is a Storage SE audience right now? I know you don't have the exact answers, but I'm curious on your thoughts.

[00:15:56.61]  Jason ValleryI actually have two minds around this, and I think your point around this being narrowly scoped to a Storage SE audience probably answers the question based on this frame. You know, if I was doing a generalized market slide that might show up at supercomputing or might show up in, you know, whatever event we're hosting and wanting to talk the vision, I want to pull those in because it's about selling the vision, selling the stack, bringing awareness to the capabilities. It may not be grounded in the truth of what's actually going to be deployed and managed by our customers, and last night it was at a Fast Forward event and Jeff was speaking and he had brought in Chan Zuckerberg as a customer reference and one of the points was made there and he was kind of joking. It's like, how many people are actually doing an entire training pipeline themselves and training a base model and fine-tuning it? Like there's very, very, very few customers that are going to be doing that. that end-to-end pipeline. It's really the foundation model builders and you know in the Chan Zuckerberg example, it's like they're building a biology first model but the vast majority of the customer base we're going after are not model builders. That's a finite number of them. We already have those relationships going. They don't need a sales team, and you're right, they'll probably end up just using data source. They won't end up using those higher level services. But again, if you're going out to sell the vision, pulling those into the talk track, it just helps evangelize in your education how the platform could come together in a more optimized way. So I have two minds around it. If this is an education, just going into the SEs, telling them the ground truth, Yeah, it's probably never actually going to happen. But bringing awareness to those capabilities is valuable.

[00:17:44.42]   RemoteYeah, I think I'm debating whether to include, because I'm 100% in agreement with you. I as a marketer, if I'm marketing, going to the market, if I am putting messaging together, if I'm putting stuff, white papers together, blog posts, if I'm going to a conference, I absolutely include those. this. With an Etsy training audience, I'm debating, do I show it? And I'm not, yeah, I'm still on the fence of whether I show it to say, this is the story we're going to tell so that you're hearing the story. However, my advice to you is don't let a good story get in the way of getting your money, which is the low hanging fruit is go after storage. at these accounts, it's a more difficult sell to try to sell up stack into the other pieces. So, or you could do a sell the storage and then cross-sell this capability. But I don't think that we win an Anthropic deal against Weka because we have data engine? We don't. But if we only win storage deals, we're not worth as much as pure storage, right? Or, you know, we get that multiplier. becomes a storage multiplier and not an AI multiplier, and like putting my jet pad on, my feeling is we shouldn't have storage SEs in this company. They should be vast SEs selling AI infrastructure, and so I would definitely be in the camp of include data engine. because what's the opportunity cost like what's the downside of doing that is an sc really going to get confused and lose the storage deal because they were worrying too much about data engine i don't know i am afraid of them getting confused on it the i'm also remember jeff is schizophrenic with some of his guidance right so But on the one hand, he absolutely wants a pipelines team that is skilled with a bunch of data analytics people so that they can talk to data analysts, but on the flip side, he gets on their sales calls and says, "Stop trying to talk to analysts. We talk to infrastructure people. We've got to go talk to them about why it's for the best architecture." And so it's like... You know, Cardix comment this morning was like, if we're gonna go have that data engine conversation, we need new SEs having new conversations with new stakeholders at those accounts, none of which we have the, while we may have the strategic desire to do that, is that something that I, spend precious minutes out of a 30-minute keynote in front of SEs to try to explain and parse. Yeah. So I think I may go to show it and then a little bit of guidance, but I'm going to run this by the SE leadership before I make that final decision. But you are saying there's... It's absolutely a role there. It's a legitimate role that if we positioned it correctly to the right people, there's value in serverless functions running, running, running, running our run executing functions from the vast system to go and drive some of that cleansing and training.

[00:21:23.54]  Jason ValleryOperations? I think so. I think that's truth. I can see different scenarios in each one of those steps even in the training phase where it's maybe like checkpoint purging or you know maintaining specific versions. There's a whole bunch of serverless scenarios you could put in each one of these boxes that could come into play and having that orchestrated. make sense.

[00:21:46.55]   Remote>> Do our SEs sell to-- I feel like this message would sell well with infrastructure providers like NCPs who are looking for the anthropics of the world to be their customers, and so I wouldn't try to sell anthropic on this, but that doesn't mean-- I mean, like, we don't sell direct to them anyway. - Correct. - And so in a sense, we only have to be smarter than our customer, not their customer. - Yeah, so we sell this stuff primarily to the NCPs who then host the model builders on top. probably the exception, but they're kind of built for our data centers too, and then the other one is this is, you know, Jeff's dream would be we replace the storage underpinnings of Azure, Google, and AWS. Yeah, sure, and so that would be another use for this story. All right, let me keep going. So that's the training phase piece that I want to go through with them, and I only want to spend probably five minutes on this slide, that sequence. So again, it comes down to prioritizing the time. The Enterprise Inference Pipeline then builds out similarly. got the enterprise data corpus, so this is the beginnings of feeding data into a RAG pipeline. So that's running on-- it's enterprise apps and SAS apps. You've got the data prep phase, which is we're going to start to take all of that enterprise data and identify what data I want to feed into a particular RAG pipeline. You've got the vector. phase so context data which chunking embedding saving it on a vector database so the down here we've got the k8s district cluster that the microservices are running on that are doing the chunking and embedding and then the vector database that's storing the vectors you're in the inference phase that's primarily about tokens and so there's retrieving and reasoning from the vector database, which is retrievers that are running on top of k8s, and then you've got the tokens, the KB cache that are in S3 and NFS, and what do we do? We pull a model out of the model catalog, we query against it, we run the rag pipeline against the vector store, data comes back, output of that. that gets logged and archived, and some of that feeds back through the system, and this is where I bring in this sort of flywheel process that is, that NVIDIA is always talking about, and then where do we sit here? but now the whole portfolio comes to bear. Datastore and Database is your production enterprise backend for storage and database services. SyncEngine, Datastore, InsightEngine, Database, these are all used in this prep phase. The vector phase is InsightEngine for managing the NIMS, DataEngine for the container runtime for the microservices. database for the vector store. Inferencing is data engine, data store, and inside engine that manage the inference process and the storage for KV cache, and then you've got data store and database for these pieces over here. So this is the whole shebang. Everything we've got can be used across this entire pipeline, and then I phase it in to say from a sales perspective, this is the enterprise workloads conversation. Go run your enterprise apps on best. This is the AI conversation, which is once it's in the pipeline, how do we now operationalize the pipeline for... for chunking, vectorizing, retrieval, KB cache, the whole nine yards of how do we do the whole inference process of this, and by the way, the way this goes is this then turns into the marketing campaigns and sales plays that we're creating to help them go capture these opportunities. So that's what this all is leading into is, all right. to go capture this, what are we building for you and enabling you on going forward? Any thoughts on this phase that jumps out that could be fixed or improved?

[00:26:28.26]  Jason ValleryI hate to make you go like 20 builds backwards, but can you go back to the first slide of when you started this? I want to see that. lines again of the training or the go for it after it builds out the first no no on the on the rag pipeline oh the rag pipeline yep right after this is built yeah so what I'm trying to get my head around is how the the dotted lines above play out sequencing perspective in the way you're pitching it is what I didn't hear in your your walkthrough is an understanding around how the inferencing is managed and that data flow is coming through because on the vector embeddings like to start with those things could be pre-computed you know you're not doing that in the flow of a conversation or an agent executing necessarily you may be querying pre-computed embeddings so like that didn't come

[00:27:29.30]   Remoteoh okay i'll go fast i'll go through it differently then so once once you get to this phase we've now got the data that we want to train for a particular rag pipeline like hey we're creating a chat bot for customer support so we want to make sure all of our user guides and admin guides, and all the historical customer support conversations, and the knowledge base, all of that stuff wants to be in that pipeline. So then the next phase is the embedding phase. So the trigger, when the data hits this, it triggers a function that calls an NVIDIA NIMM that runs on this K8s cluster. NIM takes the data, chunks it, embeds it, and then saves the data in the vector database. So it's all pre-vectorized, pre-calculated, and done, right? So then the inference phase is you've got your chatbot or your agent. You've selected the model that you want to be using. If the model knows the answer to the request, then it will answer. request if it doesn't and it wants to go get more data it goes to the rag process that does a similarity search against the vector store so it right it it it vectorizes the the request it does a similarity search against the vector store that gets passed to a re-ranking microservice that hands it back to the model to create the response to give to the chatbot.

[00:28:57.43]  Jason Vallery- Makes sense. I think then you're not connecting into the inference step there. Like, I guess maybe I'm just being pedantic about this, but wouldn't then the chatbot agent be connecting into the inferencing step and then the glue be up top?

[00:29:12.47]   Remote- Yeah, I think of just for space. why is everything up here is part of the inference step? Yeah. It's very fun to be pedantic. Okay, anything else here? You know, it's funny, I made almost the exact same slide for this. ray thing i did the other day i'll show you what i did and uh it's eerie how similar they are do you want to show it well sure i can save yourself some time erin mine are not these this this fancy looking erin knows how to make good diagrams um i'm not going our road but um how did that rape summit go by the way uh i don't know i was the closing acts and so everyone had pretty much evacuated the conference center except for four very enthusiastic vast sales people in the back so it was nice you know i had a cheering crowd but the The idea here was this is a world without VAST, and this is a rag ingestion pipeline, but the hook here is insert the Ray pieces to make it clear where Ray fits and all the stuff that isn't Ray that no one wants to deal with, and then when you add VAST, suddenly Datastore, Data Engine, and Database bookend the Ray that everyone loves. we get the benefits of unified stuff, and then I did a similar one which is this continuous model evaluation which is much more a recommender thing but it's conceptually reinforcement learning where you know you're inferencing over here and then logging all of that and then you're doing this continuous uh retraining here, fine-tuning and hyper-framer optimization, and then you've got to evaluate the results of all of that and pick the best model that popped out of this sweep and then roll it out. Again, all this extra crap between your array that you want to keep, and then with VAST, VAST plays a much bigger role. just, you know, databases everywhere save you from having to crawl all the results yourself and try to extract answers or rankings or evaluations from every single model that came out of hyperparameter optimization, things like that. So it's a very similar story, but this was for the Ray, like it plays to the workflows that Ray specifically implements. Yeah. Okay. Hey, can I get these? I'm not sure how much I will take, but I'd love to. Absolutely. I'll stick them in our SharePoint or Google Drive. Okay. Product marketing. I'll find a place to dump them. Okay. Throw there and let me know where it goes. All right. So we're a couple minutes over, and you guys are West Coast, so you might actually have other meetings today. But I'm going to let you guys go. Thank you. Thank you. Bye. Bye. Bye. Bye. Bye. All in all, directionally, this looks good for an audience of RSEs. Any last minute feedback or thoughts that I should tweak on there?

[00:32:24.92]  Jason ValleryWho's delivering it? Are you doing it or is it going to be on the site?

[00:32:28.38]   RemoteYeah.

[00:32:29.28]  Jason ValleryI'm going to deliver this, yeah. I don't know.

[00:32:31.28]   RemoteThis is next week, right?

[00:32:32.28]  Jason ValleryYep.

[00:32:33.28]   RemoteBe there. It'll be fun. Cool. So you can come up afterwards and tell me everything. I'm like, "Yeah, it's all right."

[00:32:38.44]  Jason ValleryOh no, I think it's going to be great.

[00:32:43.55]   RemoteAll right. Cool. Well, thank you for the time. I appreciate it. Got a lot out of these conversations last week and this week, so yeah, good, and I'll meet you next week then, Jason.

[00:32:55.38]  Jason ValleryLooking forward to it.

[00:32:56.15]   RemoteSee you. Glenn, you're not going to it, are you, Glenn? No, I didn't know it was a thing until I saw it on Howard's calendar. But that's just as well Okay Well, I'm underwater next year. We'll get you on stage sure Okay


