---
entities:
  people:
  - '[[Deandre Jackson]]'
type: transcript
source_type: unknown
date: '2025-10-30'
---

# 1:1 — Dre — 2025-10-30

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Intro 1-1 between Jason and Dre. Dre outlined SE enablement cadence and an S3/Object course he built; asked where Jason fits in cloud efforts and if he’s attending TechSummit. Jason shared background (Azure object storage PM, AI workloads/OpenAI), current remit to build VAST’s cloud business and product, and clarified there is no transactable VAST on cloud yet (private offers with Google; aiming to unlock AWS/Azure). They aligned on a workload-centric enablement approach (object vs file, scenarios) and acknowledged GPU scarcity gating 3P cloud opportunities. Discussed MinIO price competition and focusing VAST on qualified, performance-driven workloads. Dre will send the course; Jason will review and wants SE/customer feedback on cloud blockers and desired workloads.

## Key facts learned

- Dre Jackson is Technical Enablement Director; team recently added 2 heads and is hiring 2 more
- Weekly SE call alternates technical sales upskilling and leadership updates with 10-minute competitive/pitch segments
- Jason: ex-Microsoft Azure object storage PM; supported OpenAI; now owns product management for VAST cloud and frontier model builders
- No VAST cloud marketplace today; private offers with Google; roadmap to enable AWS and Azure
- GPU scarcity prioritizes OpenAI and Microsoft first-party before third-party customers
- Dre created a multi-part S3/Object course (fundamentals, sales scenarios; deep-dive WIP) and wants feedback
- Jeff’s vision: VAST on Cloud as a SaaS overlaying CSP object capacity with VAST performance and RDMA to GPUs
- MinIO often wins on price for low-cost object workloads; VAST focuses on performance/workload-qualified scenarios
- Current selling guidance: avoid sub-500TB deals; Dre questions missing earlier enterprise growth
- SEs cautious to discuss unreleased features; perceived code lateness impacts confidence

## Outcomes

- Jason confirmed TechSummit attendance
- Dre will share the S3/Object course with Jason
- Jason will review the course and provide feedback
- Alignment to emphasize workload-centric enablement (object vs file, AI/data pipelines, multi-protocol)
- Jason requested SE/customer input on cloud blockers and target workloads

## Decisions

- Anchor enablement on workload scenarios rather than generic object features
- Avoid engaging in price-only competitions (e.g., MinIO) unless workload merits VAST’s performance/value

## Action items (for Dre)

- [x] Send S3/Object course link and materials to Jason @Dre Jackson ⏫ ✅ 2025-11-08
- [x] Review S3/Object course and provide structured feedback @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Collect and share SE/customer feedback on cloud blockers and desired workloads @Dre Jackson ⏫ ✅ 2025-11-08

## Follow-ups

- [x] Clarify internal messaging to SEs on current cloud status (no marketplace; Google private offers; AWS/Azure roadmap) @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Align with Yonce/Yancey and Tel Aviv platform team on requirements for VAST on Cloud (e.g., capacity offload to CSP object, RDMA to GPUs) @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Assess competitive stance vs MinIO and define qualification guidance for price-driven workloads @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Coordinate touchpoint at TechSummit to review early enablement feedback and cloud roadmap messaging @Jason Vallery 🔽 ✅ 2025-11-08

## Risks

- Ongoing confusion among SEs about actual cloud availability could hurt credibility
- GPU shortages at hyperscalers limit near-term 3P cloud opportunities
- Losing price-driven object deals to MinIO for low-performance workloads
- Enablement bandwidth constraints while Dre’s team ramps and content is still maturing
- Reluctance to discuss roadmap items due to historical delays in code delivery

## Open questions

- Who will be the technical leads supporting cloud PM, and when will roles be finalized?
- What is the concrete timeline to enable AWS and Azure transactions after Google private offers?
- Which initial workloads will VAST on Cloud prioritize (e.g., AI training, data streaming, hybrid pipelines)?
- Will VAST pursue a lower-cost HDD-based SKU to compete in on-prem object for enterprise growth segments?
- Should seller guidance on the 500TB threshold be adjusted to capture earlier-stage enterprise accounts?
- What integrations (e.g., with backup vendors) should be prioritized and how will benefits be quantified?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.00]   Remote(keyboard clicking) (mouse clicking) YouPause for group work (mouse clicking) (mouse clicking) (mouse clicking) (mouse clicking) (mouse clicking) (mouse clicking)Pause for group work (keyboard clacking) (mouse clicking) This is not a way you make a first impression.

[00:05:01.68]  Jason ValleryI was distracted a minute you made it no big deal at all. Yeah. Yeah, no worries at all I was reading emails and doing other things so not an issue at all man.

[00:05:15.09]   RemoteAnyway, I just got stuck on a theme interview that I could have actually left. It got to the point where I could have just left. Anyway, so very nice to meet you, sir. I'll let you know who I am. I kind of already know who you are. I stalked you a little bit. Not a lot, just a little bit. I'm Dre Jackson. I'm the Technical Enablement Director. I have about just two people under me at the moment. I'm in the process of hiring two more people and I just got the two people by the way within the last two months, so it's still like ramping them up and you know how fun that is. On our fully enablement team, I don't know who you have met yet, and I'm kind of jumping in this hot because I've already like five minutes late on the call and had a lot of caffeine today. So I kind of go Yeah, so I don't know if you met anyone from my team. Maybe Stacey possibly.

[00:06:22.66]  Jason Vallery- I don't, I've met a lot of people. I joined actually the last call you guys were on and just kind of, I was a fly on the wall listening. So I got a sense for the broader SE team and I think Stacey was on that call, but I don't think we've had the opportunity to meet formally.

[00:06:36.75]   Remote- Okay, so that's great that you're on that call. That is our... weekly call we kind of switch it up we have one week that's dedicated to like technical sales like up leveling your skills there then we have another week dedicated to um just updates that's come from the field from leadership um and we also do like these 10 minute spots where we are. still kind of up leveling and selling you but it's more of like a 10 minutes of who is the competitor that we need to be concerned about. 10 minutes of what is a cool way that we can start pitching a certain thing or what's the mindset we should be in as we pitch. Like last week we had two weeks ago we had Billy Grafton who is the SEVP, over SMR, basically going over, don't pitch the the product, pitch the solution, in a sense. So, just trying to get our SEs to, you know, have different conversations a different way. So, I actually, I wanted to meet with you. mainly because there is a lot of cloud conversations I'll say that I tend some I tend to sometimes want to go s3 blog type conversations but then I'm leaving out a bunch there so but there's a lot of that going around right now and I honestly don't know where you fit in all of the different buckets of cloudness and just trying to figure it all out and also to see if you're coming to TechSummit. Well the last question is

[00:08:26.12]  Jason ValleryThe easy one yeah I just registered so I'll be there it's great to meet you. Where do I fit in cloud? Well so you know you stalked me but I'll give you the 60 second spiel about my bio and what I bring. Deeply technical, I spent the first 10 years of my career as a software developer and then about 13 years ago I saw cloud native application paradigms emerging and Microsoft was at that time sort of an incubation phase of Azure. I jumped over to Microsoft at that point and joined Microsoft's object storage team. Initially, I owned things like the API and SDKs, and my scope in the organization grew over the years. When I left most recently, I ran product management for object storage and really a key focus on AI customers. My team supported. OpenAI, and so I have a lot of experience with AI model builders, the AI workflow, the AI pipelines, and so forth. I'm a big fan of BAST, so I've looked at it from a competitive lens, I've looked at it from a partner lens while at Microsoft, and obviously I knew some of the folks over here. Glenn Lockwood and I worked closely together, if you know him, and Jeff brought me over and convinced me to come help build a cloud business for best. So my role as it is now, I report to Jeff and I own product management for the cloud and are a frontier model builders, and I'm partnering with Yonce. I don't know if you've met Yonce yet, but he just obviously starts recently as well, and so, you know, I'm second week in the job, learning how best to execute here. But generally what I'd say is I'm gonna be responsible for how we evolve the platform, how we evolve our sales motions, how we evolve go-to-market, how do we evolve pricing models, all of the above to build a really successful Vastoc. cloud experience for our customers. So, yeah, looking in, looking again and figure out how I can help the SE team and, you know, certainly in the sales of the market lens, but also, you know, just learning from your existing customer engagements, what kinds of opportunities Vast has run into and what challenges they've seen. Obviously, there is no Vast on cloud. today. So, you know, we're in the process of getting there, but it'll be a road map and journey behind us.

[00:10:59.65]   RemoteYou said there's no VAS on cloud today. A lot of SEs would differ, mainly because of what we've been told, right? There's a lot of that that happens where we're told that But also, the SEs are very smart, and they try to be very true SEs to the point where they don't like talking about anything. They have not touched. They're not put their hands on. Sometimes that could be a little bit of a problem because of-- some of these sales cycles will be long. So you can talk about something on day one with the mindset knowing that it won't be there until day 50 of that sell cycle, and trying to get them to understand that balance. Which is weird, because I know they come from other companies where they did the same thing. But for here, and it's not like we are-- I do kind of know what the problem is, is that our code is always late, but it's always-- time as you know it's gonna be here so but we are working through some of that right now with the SDs I just created an S3 course for object now there is there's these levels here of like, you have some folks that really do well with S3, and then you have like these pockets of certain regions that that is like part of their main focus, and then you have some regions where the competitive is a problem. So it's really hard to like really pinpoint a lot of things. So I tried. not to underestimate anything, and don't just make it so general to where that we're not touching anything. So I'm going to send over a course to you. You don't have to take it at all, but it's getting your eyes on certain things to make sure that we don't miss the mark would be so ideal, especially where you're coming from. and you're focused around certain things that you'll be doing here. I don't know who you will have under you as like your tech leads or anything like that.

[00:13:18.85]  Jason Vallery- We're working.

[00:13:19.69]   Remote- But I do see...

[00:13:20.53]  Jason Vallery- Yeah, we don't have that all finalized yet. I'm still working on it with Jeff, but yeah, we'll certainly have some folks to support the cloud side from a product lens. and what we need there. Yeah, and I'd like to take your course. Let me qualify my statement on there's no master cloud. You know, what we don't have is a marketplace. We don't have a way to transact it. You know, obviously if you kind of--

[00:13:41.77]   Remote- No, no, you're right. Just so you know, your watch will say correct. Just telling you from conversations you may have with SEs,

[00:13:50.14]  Jason ValleryLike they may be condescending, and you're coming to take something I'm trying to like prep you they make this best they will corner you I mean, we'll shortly You know private offers with Google and we've got a roadmap between now and February to unlock Amazon and Azure one of the things that I think it's relevant for You know you and the SP community understand is the opportunity pipeline and what it particularly means and when that that's not just gated on on vast so you know I bring a very Microsoft centric lens to this problem but today GPUs are scarce you know in terms of when when Microsoft gets a tranche of GPUs to go live in Azure you know they have three choices who gets them. OpenAI, Microsoft's internal AI initiatives, the first party, so Microsoft themselves, and third-party customers for Azure, and I'll tell you, when you rank order that set of priorities, I listed them in the way Microsoft thinks about it, right? So the vast majority of the GPUs that go live in Azure go to OpenAI. If there's any left over, they go to Microsoft themselves, and the only third party customers getting GPUs and Azure right now are like strategic bets that Microsoft sees as key joint opportunities for some other higher level business value, and they're very, very, very small tranches of GPUs. So one of the things, and I assume Google and I assume Amazon are going through this So we'll see a moment in industry as build out kind of equalizes and supply and demand equalizes, where the third party opportunity really explodes, and then we have a real play with a vast customer base, and so the way I think about the problem right now is we have to get the platform ready, we have to get all the sales motions, the SEs educated, suddenly the 3P business for these hyperscalers kicks off because now supply and demand have equalized. That's kind of where we sit in the industry today.

[00:15:54.91]   Remote- Okay. This course will be different by the way. It will reference like the AWS, but I think when we talk S3 object, we talk more about more of it. a hybrid type of situation where we're still sitting on-prem moving the data back and forth but in a more efficient type of way also contributing to a data pipeline in some sense but on-prem because like you said it's really not nothing there so maybe I should not see this course right now uh because I mean I'm interested

[00:16:30.30]  Jason Vallery- Objects my bread and butter. You know, one of the things that's really, you know, there's a workload-centric view you have to take, right? So object storage is, you know, in a similar sense to file storage, you know, support a lot, swath of scenarios, and so, you know, you can have object storage one-on-one But really, to fully evangelize the capabilities of AST and what customers are going to be doing in the cloud, I think you ultimately want to want to pivot to a workload kind of focus, and so, what are the scenarios that you're trying to educate the SEs on and why is object importance the lens I would take? And maybe you could talk about how you've structured the curriculum.

[00:17:12.00]   RemoteI mean, yes. Okay, so. So I strongly believe in solution selling, and I also believe that in order to solution sell, you have to understand the customer's workload, you have to understand their pain points, you also have to understand their workflow, especially with what we have in our triggers and functions. So to answer your question on the object, so the approach that I kind of took was, Why even have this type of conversation with the customer and it's more around trying to get them to understand what's the best way that folks are using, well, get the SEs and sales reps to understand what is the best approach to talk to a customer that has an object opportunity. How do you navigate that conversation? what is that baseline of fundamental understanding that they need to know in order to have that basic conversation okay so you are an application builder and you have some object in the cloud or multiple clouds like how do you start having that conversation of what are they trying to build can we help with them but then also understanding if that is a is that play worthy of mass when you start thinking about the data but then also not resting there and just thinking that it's all about applications well application builders it's also about the applications that they may use within an object like backup, storage, stuff like that, which is how well do we work with the convo's of the world in order to get some return back on your reduction rates and things of that nature. So now it's more of a, it's less of a object cloud conversation. to more of a workload, how can I save you money conversation, which is where you kind of want to have them. If they don't buy today, they do remember that you can save them money tomorrow type of conversation. So it was, it started off as we have someone here named Scott Howard, which I'm pretty sure you and me already know him. him, you know him already. He would definitely be at Tech Summit. I go to him or I send anyone to him as it relates to S3 and Object around our software. He created a two and a half hour, let me say that right, 2.5, so that's two hours and 50 minutes of content. around s3 like fundamentals deep dive and that's not consumable um two hours like who's watching a two hour and 50 minute video but some etsies will speed it up a little bit but you'll pause it come back to it later type of deal i took it and turned it into a three hour well a three a three day like not three day a three course mechanism so started off like a fundamental but then I built the sales side based upon a conversation that I had with a it's me and APAC well an S.E. and APAC that has like a sales mentality and I kind of trust them. So I reached out to him. He had a conversation with one of our sales and neighborhood persons, personnels, turned that information into an actual course of how he sees it, and then I created a document that had marketing, make it look pretty for sales understanding, like a takeaway. But I think the powerful thing for the sales side of that is there's some built-in. scenarios that's really like intricate and deep to where you don't I don't always there's like one wrong answer in a three level deep type of scenario so it starts you off at three levels and then each level after that just drops you down three more levels of like really getting into the conversation a scenario with the customer that is looking to make a move or understand more about why they would need VADs for their object. So I think that is powerful to get them to like take what you teach them in the beginning of this course and start being able to understand and use that out in the field. Then on the back end of that, there's two more courses that I'm still finishing up that more deep into, it's like that double-click-in for the SEs. So you got the fundamental, the cells, everybody can go through the fundamentals and cells, and then the deep is really for SEs. So that part is still in the making. I am not an instructional designer. I am not an LMS admin. We don't have a lot of things so I'm saying be kind as you go through the course, but I want your feedback.

[00:22:15.90]  Jason ValleryYeah, I mean, again, I would, I would want to think about, and I'll give you this feedback after I take a look at it, but, you know, just looking at all of the scenarios for object you probably have. to organize your content that way. If you're saying why is the customer picking object over file, what is the value of object? And to me it is ecosystem, there's a whole bunch of open source tools. It is scalability. NFS is not a great protocol for crossing data center boundaries and getting to trillions of objects and exabytes of capacity. It's API-driven, so you're running from an SDK and using cloud-native application paradigms. It's data pipelines, where you're ingesting via one head and consuming via another. That's where multi-protocol comes into play. There's a whole bunch in the AI training space as to why object versus file. Ultimately, what you're trying to evangelize is to a set of folks that probably more familiar with file, um, why you ever even care about object, and so it's selling them on that vision, and then you can go into the nuances of like, what are the constraints and opportunities that object bring to those various workloads? That's how I would traditionally have approached this problem of bringing folks up to speed.

[00:23:32.69]   RemoteYeah.

[00:23:33.78]  Jason VallerySo I'll take it.

[00:23:35.08]   RemoteI can't wait. I can't wait now. may be super happy today that's the that's the initial approach of the fundamentals exactly what you just said it starts off bow bow versus object right up the top of the course yeah what's the difference yeah oh man so Jason I get you'll see this over this time like I get excited very quickly okay um if you are if you're selling me something you're find out very early if you got me hooked because I will get excited, and sir, I am super excited that you're here.

[00:24:08.09]  Jason ValleryWe have a lot of product gaps at best in terms of what we need to get to to make ObjectRelay bring the capabilities it needs in the cloud. You know, we're looking right now at the product roadmap to support Bastion Cloud and it'll be things like offloading capacity to the cloud csps object stacks and you know what how do we position that and so forth so there's a bunch

[00:24:34.05]   Remoteto do here but uh yeah that's why i was trying to figure out like where you fit in all of that because there's so much to do even uh oh man you said the offloading okay getting me too high

[00:24:45.53]  Jason ValleryRight now. Calm down, Dre. Okay. Yeah, I mean, that's, I mean, Jeff's vision is that we would have a vast on cloud software as a service kind of model that allows us to go and, you know, in some ways even compete with the hyperscalers on object storage because we can use them as the underlying capacity, but then we can get the performance benefits of fast and we can get the head and we can then connect it up to customers' GPUs with RDMA. That's just a huge win. There's a lot of engineering that has to happen between here and there, and there's a bunch of partnership work that has to happen with hyperscalers, but that's what I'm here for and Yancey's here for.

[00:25:24.74]   RemoteAwesome. It's safe to say that you guys are basically

[00:25:30.50]  Jason ValleryWalking this thing hand-in-hand as you build you know there's a lot of core platform work that'll happen and want to drive that back through the Tel Aviv

[00:25:41.61]   RemoteFolks but yeah all right amazing so I will be I'm gonna be bothering you so

[00:25:49.89]  Jason VallerySorry sorry but not sorry How you can help me, you know, I need to know what you're hearing from our customers and the sales engineers around why cloud isn't working for them and what kinds of workload scenarios they want to bring to the cloud, like that's that's what's useful information and feedback.

[00:26:10.12]   RemoteOkay. What about competitive, competitive, just competitive? Competitors in general.

[00:26:16.48]  Jason ValleryOn-prem competitors or what do you mean competitors? What kind of competitors?

[00:26:19.84]   RemoteGood question. Good question.

[00:26:21.84]  Jason VallerySo MinIO.

[00:26:22.84]   RemoteYeah. They beat us on price.

[00:26:24.91]  Jason ValleryYeah.

[00:26:25.84]   RemoteWell, I mean, just the architecture of it is different.

[00:26:26.84]  Jason ValleryYeah. But that's an object.

[00:26:28.84]   RemoteRight. So.

[00:26:30.84]  Jason ValleryBecause you're talking about.

[00:26:31.84]   RemoteYeah.

[00:26:32.88]  Jason ValleryI think there's an interest. The approach that I've had.

[00:26:34.84]   RemoteI think there's an interest.

[00:26:35.87]  Jason ValleryI think there's an interest.

[00:26:36.84]   RemoteI think there's an interest.

[00:26:38.07]  Jason ValleryThere's an interesting thing, like, fundamentally, that's a hardware problem, not a vast one, right? Like, it's, you know, I pushed on, you know, when I was chatting with Jeff and stuff in the past, like, I pushed on, why the hell don't we go do, like, a really low-cost hardware SKU qualification and use hard drives and so forth to try and be able to be competitive on-prem with Object? Um, you know, it's not, in fact... DNA today, and so sometimes you've got that confliction around, is that a distraction or is that a good opportunity for business? And, you know, I don't know, I actually think there is an opportunity there, but I haven't convinced Jeff of that. So we'll see how that

[00:27:17.20]   RemoteGoes. So good luck on that because that is, that's the enterprise play, right? That we're looking for and we just don't, in my opinion, we don't have. We tell our sellers don't talk to anyone that has less than 500 terabytes and I'm like okay that is we're how we need to go a little bit lower to like snatch those enterprise before they get there because once they're there they're already working with Databricks. You can't get that back, you know, it's hard to pull them off of that so attacking them when they're On the rise and being able to get them to I'm glad you're here, sir. Oh Just a conversation around around me now. Yo, I try to tell them to not even worry about having a more of a price conversation call is all about about the benefits, if you can get them to realize the benefits that we bring also along with the object, then that's a better conversation to have. But if it starts talking price, like gracefully buy out, thank you for the time, try to become more of a trusted advisor, like, hey, guys, you're making the right decision for you, but just know that we're here.

[00:28:28.73]  Jason ValleryIt's a workload scenario problem. wins if it's, I don't know, a video surveillance workload right? Like, yeah, it just makes sense, right? You're gonna, all you care about is cost per gigabyte and how you make sure you've got durable data and you're not doing analytics pipelines over top of that so you don't need high performance. Flash doesn't make sense, but if you're talking about a Spark data streaming pipeline that connects to GPUs for training, then VaST is an obvious. So, you know, you got to be, you got to be qualifying these things again on does the scenario that the customer is trying to solve even make sense on vast and are there better price performance solutions that they're going to trend towards? And so, yeah, it's, it's, you know, you have to.

[00:29:07.59]   RemoteThank you for being so, but three months ago there was a whole shit moment. We lost two men IO and it was like, we ain't. need to go like everybody need to focus and let's move around and let's figure out how we train our people on competing against Minayo and I'm like but it's a price thing they did not go with us they didn't say hey we're not going with bass because of the architecture it's a price thing that's a price thing like it's we can't beat that no matter how you slice it up we can't beat the number if we can beat the number then let's have a conversation about how we have the rest of the conversation so yes you at you being able to you know really articulate that at the top will probably help me not have to stop doing one thing and pivot to one thing and then that one thing is not important anymore because the next week we had another issue at whatever and now we have to focus in on selling that now and that's so you see but sorry to ramble I do that and the course that I sent over I really would enjoy your feedback on that I love the way that you said that we should start off so I think that you're going to enjoy it I hope so okay man look I will go ahead and end this call yeah and I look forward to seeing you in about two weeks man I'll see you

[00:30:35.09]  Jason ValleryThere oh nice meeting you yes sir

[00:30:45.75]   Remote(keyboard clacking)
```

<!-- ai:transcript:end -->
