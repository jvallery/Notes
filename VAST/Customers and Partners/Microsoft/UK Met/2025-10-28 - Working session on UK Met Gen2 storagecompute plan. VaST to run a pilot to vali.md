---
type: "group-meeting"
created: { { DATE } }
title: "20251028 0930 Parallels Transcription"
participants: [{ { PARTICIPANTS } }]
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251028 0930 Parallels Transcription.txt"
tags: [meeting, group]
---

# 20251028 0930 Parallels Transcription

**Date:** 2025-10-28  
**Participants:** Jason Vallery, Niko Dukic, Lior Genzel

## Summary

Working session on UK Met Gen2 storage/compute plan. VaST to run a pilot to validate mandatory requirements. Two paths under consideration: Azure-provided compute VMs (preferred) vs ODM/bare metal with SDN intermediary (complex). Awaiting Microsoft compute SKU update by Nov 15 for ~300 TB/node and 800 Gb NICs. Interim testing may start on 100 Gb VMs. Lior coordinating with Mike and Anand for minimal test config and potential hardware shipment. IO expected mostly sequential, ~50/50 read/write; detailed profile pending.

## Key facts learned

- Gen2 replaces current ClusterStore; not an archive project.
- Contract originally envisioned up to 3x scale, but specifics under discussion.
- Compute path TBD: Azure VM SKU with high‑speed NICs vs ODM/bare metal with SDN bridge.
- Requested node spec: ~300 TB/node and 800 Gb NICs.
- Azure team to propose a new SKU by 2025-11-15; LSP5 as proposed does not fit.
- Interim option: start with 100 Gb VM SKU, then switch when full VM SKU is available.
- Alternative topology: HBv5 with InfiniBand for backend storage connectivity.
- Network concern: SDN intermediary adds complexity and an extra hop.
- Pilot must validate mandatory requirements; others are nice-to-have.
- Workload: large files, mostly sequential; roughly 50/50 read/write; detailed IO profile pending.

## Outcomes

- Agreed to define a minimal viable test configuration to begin pilot work.
- Plan to confirm availability and SKU details for full VMs with high-speed NICs.
- Coordination to begin with Mike and Anand on staging hardware and test plan.
- Interim testing may proceed on 100 Gb VMs if full VM SKU is not yet available.

## Decisions

- (none)

## Action items

- [x] Confirm availability and exact SKU name for full VMs with high-speed NICs; provide date if/when ready. @Niko Dukic ⏫ 📅 2025-10-28 ✅ 2025-11-08
- [x] Share the email thread with Mike and Anand; schedule and run the configuration meeting. @Lior Genzel ⏫ 📅 2025-10-29 ✅ 2025-11-08
- [x] Align with Mike to confirm Anand is waiting on minimal test configuration and greenlight staging. @Niko Dukic ⏫ 📅 2025-10-29 ✅ 2025-11-08
- [x] Propose minimal viable test config (node count, per-node capacity/compute) sufficient for functional and initial scale testing. @Lior Genzel ⏫ 📅 2025-10-29 ✅ 2025-11-08
- [x] Obtain written confirmation and timeline for VMs supporting ~300 TB/node and 800 Gb NICs. @Niko Dukic ⏫ 📅 2025-11-15 ✅ 2025-11-08
- [x] Prepare to ship and deploy a small ODM/VASt cluster for testing if required; prioritize rapid turn-up. @Lior Genzel 🔼 ✅ 2025-11-08
- [x] Provide initial IO workload details (sequential vs random, read/write mix, typical file sizes) once available. @Niko Dukic 🔼 ✅ 2025-11-08
- [x] Decide between Azure VM path vs bare metal + SDN based on SKU outcome and timelines. @Niko Dukic 🔼 📅 2025-11-15 ✅ 2025-11-08

## Follow-ups

- [x] Validate whether HBv5 with InfiniBand backend is viable for direct storage connectivity in this deployment. @Niko Dukic 🔼 ✅ 2025-11-08
- [x] If full VM SKU is delayed, confirm starting tests on the 100 Gb VM and plan migration path. @Niko Dukic 🔼 📅 2025-10-29 ✅ 2025-11-08
- [x] Confirm pilot validation criteria map to contract mandatory requirements. @Jason Vallery 🔼 ✅ 2025-11-08

## Risks

- Delay/uncertainty on Azure compute SKU (timeline and capabilities).
- Bare metal + SDN topology adds operational complexity and potential throughput bottlenecks.
- Final required scale (up to 3x) is ambiguous, affecting sizing.
- Incomplete IO characterization could mis-size the solution.
- Resource constraints across teams may slow pilot and integration.
- No written confirmation yet for full VM support/timeline.

## Open questions

- What is the exact Azure VM SKU name and availability date that meets ~300 TB/node and 800 Gb NIC requirements?
- What is the definitive scale target (is the 3x scale fully applicable)?
- What are the detailed IO characteristics (sequential size, concurrency, read/write mix) for the ClusterStore workloads?
- Is HBv5 with InfiniBand acceptable for backend storage connectivity in this environment?
- What minimal test configuration is sufficient to validate functionality and extrapolate performance scaling?
- Can ODM/bare metal be integrated without an SDN intermediary or with a simplified topology?

---

## Transcript (auto)

```text
[00:00:00.00]   RemoteAre you enjoying yourself with vast training like i must say that you have landed successfully good compared to to others like it seems that you're you're at the right place at the right time that's what i'm trying to say it's a fun time to be here yeah it's a fight you came with the right experience for sure. Hey Nico. All right I can't see either of you maybe that's okay. No you can't see because I can't open a video. This is zoom so it's not actually um yeah somehow put my camera because every time when I use zoom and when I turn on my camera my pc just froze. after all the teams meetings we've had together video was off because it's dark sorry what did you say leo no no i kind of said it just i had to stand out and just breathe some air i was in my office all day it's already like 6 p.m or whatever it is it looks lovely are you in uh tel aviv right now are you in the states no i'm in tel i'm not in tel aviv I'm actually in the south of Israel. I'm in Eilat. I have a place in Eilat and a place in Tel Aviv. So for the next two days in Eilat and then back to Tel Aviv and I'm back to the States only in 10 days. I took a vacation from the States.

[00:01:21.39]  Jason ValleryYeah, that's a problem. What about you, Niko? Are you down on the coast or

[00:01:25.12]   RemoteYour vacation home? Or are you in Zagreb? No, I came back like a month. ago. It's now, I mean, I'm not there during winter typically. I was there from like July till mid of September or something like that. Yeah. That was enough.

[00:01:41.94]  Jason ValleryWell, hi from the other side. It's great to connect. I've been working with, well, on a lot of things. but one of the topics that's top of mind for everybody I've asked is UK Met and you're the guy. How's the new role treating you? Are you formally landed on

[00:02:01.57]   RemoteMike's team now? Yeah I just landed today. It was supposed to happen on like October 15th so we are just 14 days late which is not that bad. Now it officially happened today. I'm still kind of of working for call till end of the month but basically that just means tomorrow because on Thursday and Friday I'm off so from Monday I'm like fully fully with a new team yeah that's the plan. When do you get your car? I'm not getting my car, I got car allowance. Why? I don't need a car when I'm not traveling. It's actually car loans fit me better because I already have a car. You know why I bought my car. Different story. No, but I'm getting car loans, which is actually much more than I expected. It was smaller amount before, but now it grew to like, yeah, a lot. I basically bought more than I thought. So it's nice. look I got like I think I got like 20% more so yeah I mean congratulations I'm

[00:03:11.59]  Jason ValleryReally glad that all worked out for me well I'm over here now and I guess what I want to understand from you and whatever you can kind of share is what the heck's going on with Met UK in this new you know, phase two project. I know, you know, there's been a number of conversations. Where does VaST fit in? What's the IO pattern? What's the workload? How does that compare to the active archive that we know from the past? Like maybe you can just kind of brain dump on what we need to be thinking about on our side.

[00:03:40.03]   Remote- Yeah, okay. So Gentoo has nothing to do with archives. I mean, in general, kind of, but it's not really related. It's basically a replacement of the current cluster store, together with the additional compute power that they will get as part of generation two. The AI pattern pretty much remains similar. The only thing that it's currently not clear is how much will that that need to improve. That contract, that the original contract, that was supposed to scale for 3x. However, there are some parts of the contract that doesn't mean that it's actually going to be 3x. That's currently under discussion with the Met Office and internally as well. So we don't really know at this point in time where that-- increase will come and how much it will be right. There are ongoing discussion on that currently. So once that is clear then we will know much more information around what is what would be the potential vast configuration from that side. Now will it land on the custom hardware from vast or will it land on our internet? That's still to be, because it depends on, it will depend on which configuration the, the, the computing will, will, will, will, will, will finalize. The, the LSP5 that they proposed will not fit for sure, but they asked us to give them enough time till November 15th to come up with a new skew. Potentially only format office or broader that's still to be determined, but they they will come back to To us so that we did ask for like 300 terabytes per node and 800 gigabit nix Which is the most important part for you guys Uh, so we are waiting will they will be able to do that and in case they will be able to do it What is the timeline when they expect that to be delivered? So that's kind of where we are at this point in time until that is done and that is decided We don't really know in which direction we'll go So but it will be one of those two So a few comments and just popping in right I had dinner with eagle last night And I asked the eagle is visiting Israel. He was visiting Israel. I think it's flying to India today and I asked him, "Igal, UKMAT is waiting for mid-November." He said, "Between us, they don't need to wait." The answer is yes. We're going to build them VMs with 800 gig. (audio cutting out) It's 400, right? So that's what we need, and the capacity you require. So again, he's going to use the Microsoft. to communicate, but from what he told me, he's committed to make it work. That's great, until I get that written form from him. No, I know, I know, now, you know, you know, you know how it goes, right? But yeah, there are like two parts of that, so one, great, I would be really happy to do it because I I don't want to do it with bare metal one because they're just too complicated. Uh, and the other thing is, uh, he needs to share the timeline, right? We need to understand. Is that something that he, that they will be able to do within a year or it will take them three to four years to build that because at the end, that will depend on, on, on, on, on the timeline of the whole project. I didn't ask about timeline but I agree with you and it will follow up but the second second point two more points on that on that level second point is that I did reach out to Anand and Mike is on the fridge and I and I told Anand we want to put hardware in your in your data center to enable it for UK Met Even if it comes with the right type of news, there is no reason for you guys not to have access to our, you know, ODM hardware and be able to start testing so you can see what RAS can provide, and Anand is waiting to understand what is the configuration that is required, and Anand is waiting to see that Mike is saying, "Please make it ready." So that's an email. - If that's the case, I'll ask Mike to confirm that. However, we can, for now, no, it's kind of tricky. We don't know the final configuration of it. So we can only-- - No, no, it's final. - Yeah, we can only-- - No, once again, not final, I'm talking about the minimal configuration that will be big enough to support the testing you wish to start with. I need X level of compute and Y level of capacity and if I get that I can start testing I can start picking tires We're not looking to build the final configuration. We're just Understand that the thing that I don't know is basically what that testing includes right because it includes any Functional testing that it doesn't matter whatever whatever whatever whatever is there it is there, if it will require any kind of benchmarking, that's a different story, right? Because then we need to understand how that scales and what is the minimum amount of hardware that we'll need to get to a point and then estimate the scalability going forward. So that is the part that is not clear to me yet, and that will actually depend on, but I'll talk to Mike, and I'll tell him that Anand is waiting for that so we can we can we can start there How much time do you need to deploy a relatively small cluster? And then as approved it we can ship hardware in days and we can deploy and make it the priority So we can move fast and we want to move fast My logic was to saying whatever you plan to test with lsv4 you want to test an 8-node, 16-node cluster, then let's build something that would replicate that with the proprietary hardware. So that would be the minimum. But again, you guys give us the answer, and the last thing that is tactically important for me to understand, our engineering are full steam ahead in making the LSD4 available for testing, and the basic question they have is, to the new LS LS before VM which is a full VM do you know if that SKU is available and if it is what is the SKU so I'll be helping Sarah as soon as we finish this and I'll ask her I asked her to tell me but she didn't come back to me so I assume it's not available yet I'll ping her up immediately after the call I'll let you know if it's not available I'm told him to start with a The 6 VM, the 100 gig VM, and later on change, because right now I'm holding them back on moving forward. - Yeah, give me a date to do all that. As long as she responds, I'll let you know. - Okay, that's the tactical stuff I had, yeah.

[00:10:23.15]  Jason Vallery- Let me ask you a couple of questions. It's clear to me if we go with a Azure provided compute SKU, our storage dense-- compute skew that that how this would work from a network topology perspective because that would then have a hypervisor in the overlay chip but if we're shipping you know vast oem odm hardware to a facility how on earth can we connect back to the virtual network um yeah that would be

[00:10:48.50]   RemoteThat would be the same and that would be the same the same the same topology that we currently have format office, right? So basically you will have a separate compute. You will have somebody, probably something like Rotterdam in between that will be used to connect to the bare metal implementation to SDN. The same thing that we do for everything else, which is currently bare metal in Asia. That's the part that I want to avoid because that's overly complicated in terms of what needs to be done.

[00:11:13.49]  Jason Vallery- Well, and it's another network hop. how does that scale when we're talking about 800 gig NICs and the kinds of throughput we'd want to push through the vast like will that intermediary layer

[00:11:22.36]   RemoteThat does the translation be able to scale. Yes and no it doesn't allow us to basically option to use SKUs that for example have an infinite band and then basically just use that as a back-end to the storage platform. That part is not clear but we do have options, right? You can use HBB5 which have InfiniBand backend and then just use InfiniBand to connect directly to the storage cluster and then you have frontend to service the frontend traffic. This is what this is what currently is connected with Dolphin, it's just not InfiniBand, it's Slingshot but it's the

[00:11:53.73]  Jason VallerySame, it's the same principal. I forgot, Project Slingshot, I remember that. What is So, in the ClusterStore implementation, is it running on non-Azure hardware?

[00:12:04.99]   RemoteYeah. Yeah.

[00:12:06.29]  Jason VallerySo, you mentioned that the I/O characteristics will be the same as ClusterStore, but I never really plugged in on it. So, I was more, when we were chatting back then, more thinking about the archive problem space. What is the I/O pattern for ClusterStore?

[00:12:18.79]   RemoteWhat can you share? I have no clue at this point. started to run so we can gather information, but I don't know. I'm not familiar with that, but that will be shared as part of the implementation once we have more information on what we actually

[00:12:36.24]  Jason ValleryWant to build. I guess what I'm looking for is this sequential throughput read-heavy, write-heavy kind of IOPS characteristic.

[00:12:45.22]   RemoteIt's both. If I understand correctly, it's close to 50/50 in terms of recent writes. But let's leave that, but mostly it is sequential, right? It's not random, right? Because we are talking about large files in general, so most of the work is really sequentially it's not uh it's not random but well yeah let's leave that for when we actually have more information.

[00:13:10.84]  Jason ValleryI'm sure Lior, you've probably already had these conversations, but what's the decision frame of reference, what options is UKMAT considering, who are the other competitors,

[00:13:22.31]   RemoteMicrosoft? UKMAT office is not considering anything, we are considering, we do have a contract, so we basically need to fulfill the service. So it's really our choice more than more than more than we need to provide a service and it's basically our choice. What do we, what do we select. That's the reason why we had the whole early marketing engagement or whatever the legal team allows me to use this as a name for that. it came on top, but that doesn't mean that you don't have... contract in your hand. You will have a contract in your hand once we actually have run the pilot and then we understand that everything that you wrote in that response is actually true. In that case, then we'll start the commercial agreement and then we'll agree on terms and everything that goes with it. But Metofit doesn't make a decision, right? We do. Well so the gating factor right now is seeing that the Performance numbers we've shared are Because we need to we need to be we need to support that because that's part of the Everything that was mandatory there. I do know that there were some points that you didn't satisfy on that front But neither nobody did satisfy everything so it's fine, but we need to close on that and see how we work around that because everything that was mandatory was actually coming from an office everything that was not mandatory is potentially for other customers as well but it's not critical because we don't have a contract for that right for this we do have a contract and we do need what we need to support so that needs to be closed but as I said it's mostly our decision not to say that Met Office doesn't have any decision yeah clearly they have. If they don't want somebody, well, they can clearly tell us that. But legally,

[00:15:06.88]  Jason Valleryit's actually our decision, and what solutions are still in play? Is it, what's been ruled out

[00:15:14.02]   RemoteAnd what's still a possible path forward? What you can share? I'm not going to share anyone else. You know me, Jason, well enough that you know I'm not going. to share. Currently, we are not working with anyone. They are still there. All the others are on hold because it will depend on, as I said, the pilot and the commercial agreement between us. We don't have enough resources to deal with multiple at the same time. But as I said, if something doesn't go as planned, we do have backup options in that case. Okay, guys, I need to go up to a call with Google. It's funny as it sounds right. I apologize So I need the answer on the full VMs because right now Let's be realistic it's a Wednesday night in Israel. So tomorrow is a business day. Nobody will touch anything before Sunday morning So if we get an answer this week and I and which VM It's good enough if it's tomorrow is the day after if we didn't they're just going to follow up with the one on the gig and I will I will share with you the thread that Mike is on and Jason is now on with An end and we have a meeting tomorrow Let's get to a configuration tomorrow on the call with Mike and then we'll show you back with an end and then I will Escalate it internally for it to be shipped Again, I am all for eagles computes. I just want you to have plenty and plenty ready Make sense and it also helps us because at least we'll be able to start doing some work on With vast and so you know, you guys never touch fast. So Nico we talk soon, but one last question Are you coming to supercomputing Jason is coming. I'm going are you coming? No Okay, so we want to talk to Mikey that change but yeah If you come I'll buy you a beer. All right, then you can buy me a steak. Okay, we'll talk soon - That's fine, bye.

[00:17:17.23]  Jason Vallery- How are you doing, man? I mean, it's good to see you.

[00:17:21.14]   Remote- Oh, it's fine. Let's see how the new role will be. I mean, you've been here long enough that you know everything, right? So, yeah, let's see.

[00:17:34.42]  Jason Vallery- I'll tell you, I don't know how to translate to a. in the life of Nico, but one of the things, and really one of the tipping points for me, was just the culture in storage, and I think we got into this culture, and I was part of it, of just so much negativity and so much complaining, and the more time I spent, the more I realized that isn't a universal truth across. Microsoft. As I was working with OpenAI and working with Needy's team, I really saw the energy that that team has. It was just a different experience. I will say, I have a ton of respect for Needy, and I hope that translates into your role and the culture in your team being a different experience than what you have in store. I think it's possible. I don't know Mike well, but I do know needy pretty well, and I think she's a great

[00:18:28.18]   RemoteNo, I mean yeah, I'm not thinking about that this, but I needed the change. I mean, I really like Carl I mean a great guy, but you've been in that shoes He cannot basically make any serious decision without talking to one she and one she is always a blocking stone for everything, right? Not just that he's the blocking stone, he basically changes his opinion like weekly. So anything very crucial that you need to build, it just takes forever, right? So, yeah, I kind of got (laughs) got sick of it, to be honest. So let's see, I think I made the right call. At the end, worst case, if I don't like it, I can always change a company, right? That's always an option. I didn't want to do it now, but as I said, worst case, that's always an option. But let's see, this role seems interesting. Let's see how it will go. I know Mike long enough. I know Mike for like eight, nine years, even more, ten. Kyle just told me that he got the notification that my 10th year anniversary is in 15 days. I have no clue, to be honest, so I said, I think that I know Mike probably from the early days when I joined, so I know him a long time.

[00:19:48.98]  Jason ValleryYeah, I mean, that was obviously what happened with me. You know, Vanshi's team was incredibly difficult because he managed through you, right? So it was very much like I'm his mouthpiece, but then I'm disconnected from him and I didn't know what he wanted, and it was really, really difficult, and I don't envy Carl or Scott or any of the other guys that are managing because in reality, it's like. Bob, she kind of comes in, strongly opinionates, tell you what to do, tells you what your team to do. Sometimes manages around you. It was just a toxic environment.

[00:20:24.11]   RemoteYeah, but thanks. - And even that, I could live it, right? The thing that I couldn't live is basically that everything takes forever and that he changes his opinion weekly, right? - Totally. - That's a problem, right? I mean, you... Okay, I don't agree with micromanaging because at the end we are all professionals if you don't if you're not capable of doing your job You shouldn't really even even even even be here about okay that he stopped but the problem that everything is blocked on him I I know that I've been waiting for some of the some of the decisions for him for like Four six five six months, right? That's just ridiculous. I think it makes it makes no sense I literally, it literally took him four and a half months to review a paper that has a page and a half. I'm sorry, you can read it in the toilet while doing whatever you're doing in the toilet. I mean, we're not talking about 30-page documents, right? So you really need to concentrate and take time. So I said, it's kind of. >> I mean, you've been here more than I do, so you understand how he operates.

[00:21:28.72]  Jason Vallery>> The thing that really excites me about Vast, and what you described, like Vamshi is totally guilty of not making decisions, changing his mind, and inaction, but that is not just a Vamshi problem, that is actually an aggro storage problem. like that actually the root of that cultural issue sits firmly with Manish in my mind, and uh you know one of the things that's really refreshing about VAST is how quickly they make decisions and even more and refreshing is how like quickly the dev team can turn things around. Like I'm super excited about their velocity like the ability to go and say we should go build this thing and have it turn into reality you know we're I mean just transparent we're having conversations right now which is about implementing the blob API and they're like oh yeah we can knock that out in like two months you know like those kinds of things are that would have sat for years in after storage you know vast is exciting you

[00:22:28.54]   RemoteMean not you mean something like s3 right

[00:22:32.30]  Jason ValleryWell, that's exactly the reference point of like, you know, we've been talking about S3 for how many years on Blob, but then like VaST is like, well, yeah, we'll just go add a Blob API over top of VaST, and we'll knock that out, and it'll be a really quick project. I had a meeting about it this morning. It's why it's top of mind. So I'm just excited about like the culture here, the decision empowerment, and yeah, I think it's a fun place. So I'm excited.

[00:22:52.91]   RemoteI mean, like, every, every, I mean, a small company, I mean, small, Wast is not that small, but in comparison to Microsoft, everything is small. You cannot afford to lose time on stupid things, like, I do agree with you, right? I think that Vamsi is to blame, I mean, Vamsi has a lot to blame, but somebody actually lives with it, lives with that, right? and somebody allows him to behave like that. The thing that I really don't understand is-- in VR, for example, you basically have the same comments from Manish every single time, and every single time, Vamshi says, I thought I didn't have time to do it. We'll do it next month. Fine, I can understand that it goes a month, two months, after three months, and Manish just lives in it, right, which is kind of strange, because if it's important for you, well, you should actually hold him accountable. That doesn't happen, right? So, yeah, he just uses the same principle for everything else. But I do agree with you. I mean, it's the whole culture is really bad, and the one thing that you could never understand is how the hell is not responding to an email acceptable behavior I'm sorry. We just not tell me no, which is absolutely fine. No, it's a completely Acceptable responsible response, but just give me a response But by the way, they're not just Microsoft. That's not just storage that happens all the time while I was working with partners You know, how many times did I need to ping like somebody from networking or compute? Same thing He's the CDP is basically on the line. They still don't respond, right?

[00:24:34.10]  Jason ValleryI guess sometimes

[00:24:38.38]   RemoteBy the way, the best comment that ever heard somebody Christopher was talking to somebody I don't remember who it was the guy literally told him that he doesn't do email I'm sorry how is that possible I saw that in and out

[00:24:56.19]  Jason Valleryof office recently somebody just sat there out of office and said I don't respond to my email if you need me send me a team's message somebody yeah I mean just like whatever I guess that's your culture

[00:25:09.67]   RemoteHow can you as a manager tolerate that, right? I'm sorry, that makes literally no sense, right? So as I said, yeah, let's see. I hope it will be different in the new work. As the worst case, if it's not, I'll just change a company, right? That's always an option. After 10 years, I think it's time anyhow. I was supposed to stay here for six years.

[00:25:30.46]  Jason ValleryI don't know. That's a whole other set of constraints around who's hiring, what's happening. Amazon just laid off 30,000 people today, so stability is important in this economy.

[00:25:44.85]   RemoteWell, I mean, it's not like the difference before. Microsoft always paid less in comparison to AWS. and GCP, but your position was stable. That's not the case anymore. That's not even close to the truth, right? What I do know is that the next company will definitely not be a corporation. It will definitely be a smaller company, whatever that is. I have no clue, but it doesn't matter. But it will not be AWS. or GCP that I can guarantee because I have enough share of corporations. I don't want to do it anymore. So I'll give this a try. I think it's a good rule. Let's see.

[00:26:28.64]  Jason ValleryWill you have the opportunity to work with any customers other than UKMAT? Like as the supercomputer plans expand and they start doing other...

[00:26:35.47]   RemoteThat's possible. The team currently does only Met Office, but yes, eventually it will scale to other supercomputing customers.

[00:26:45.61]  Jason ValleryAre you going to be traveling a lot to London, or what's the kind of travel situation?

[00:26:51.67]   RemoteI assume, yes, not a lot, but I assume that I will have to travel periodically there. Most of the work will be remote. That's why, by the way, that's one of the reasons why it took so long. Because yeah, Mike had a hard time explaining why he wants me, not somebody from UK. So yeah, it took actually a long time.

[00:27:16.63]  Jason Vallery- Well, it's good to see your face. You know, my role here is successful. on the cloud, so I've got a whole bunch of things going on, but you know, UKMet's a key opportunity for Vast, and so I'll stay plugged in. Lior obviously will run all the BD side of things, but I'm very interested in understanding from a product lens where the gaps are, and what we need to drive into the platform, into the cloud control plane, and so forth, so that's kind of what I own. I'm just looking forward. working together and figure out how we make mast on azure the default yeah how

[00:27:50.54]   RemoteAre you by the way I mean privately not business related I'll tell you the the

[00:27:57.66]  Jason VallerySummer month you know the way it kind of worked out was I just had enough in May I mean I've gone on multiple times over the last 18 months about Vamshi and just said I can't work with this guy. No actions. What ended up happening is obviously my scope started to shrink and you know having really this is all rooted in Jürgen retiring. When Jürgen retired he was my like champion. I talked to Jürgen all the time. He was my ally. He believed in me. As soon as Juergen left and Ong took over, you know, Vamsi saw that as an opportunity to reduce my scope and to push me to the edge, and that just kept happening. There was a whole bunch of FOMO that happened because, you know, Vamsi saw that I was getting invited to meetings with Scott Guthrie and Satya and Amy Hood, and I was, like, getting all kinds of visibility because of the OpenAI work, and Vamshi was frustrated by that because he clearly wanted to be in those meetings. Nidhi became a champion of mine and Nidhi was pushing me to take on more scope, pushing Manish to give me more scope, and then Vamshi just made it very, very difficult for me, and I kept going to Aung and saying, "This doesn't work. I need a different manager." And Aung kept saying no, and then ultimately I went to Manish in April. May and said, "I'm out. I'm not gonna work as a PM anymore. You need to find a different job for me. I can't deal with Banshee shipping. I don't need to get in the weeds." But he was backstabbing me, going behind my back, really making it difficult for me to do my job. Manish said, "Okay, I'll make you an architect on Project Apollo. I don't know if you know anything about Apollo." like, okay, whatever. It was supposed to still have an opening eye component to it. I was supposed to keep my relationships with opening eye. I was supposed to have a team, and I said, okay, good transition point. I haven't used my sabbatical. I've been keeping it on the back burner because I didn't have time. I thought it would impact my career. I'm gonna take my three months off. When I come back, I'm gonna hit the ground running. New role, new structure in Manisha's team. are in Jay Menon's team, came back from sabbatical, like feeling kind of refreshed and excited about the opportunity. I didn't do any career searching while I was off over the summer. Summer was awesome. I spent a bunch of time with my son. My wife had a surgery, so she had like knee replacement and we didn't get to do as much as we wanted, like from a travel perspective, but it was a good summer, and it was clear, I didn't have a role, right. I was being pushed out, my rewards were bad. I'm like, I had the most impactful year of my entire career at Microsoft last year, and I came back to 100% rewards. I just basically told Manish and Jay, this isn't gonna work, and started talking to a handful of companies here. So that's kind of how it all played out. But I had a good summer, and then this transition, and I'm actually really excited now. So I'm in a much better place with this role, I think. Clearly, I have good influence, respect, ton of opportunity. Compensation is good. So I can't.

[00:31:04.59]   RemoteNo, I mean, I'm glad for you. I'm surprise that you left. I mean, I did expect that you will leave storage team anyhow, because it was clear that that Vamshi is pushing you around. But yeah, I thought that you will probably go to like compute or I know that you have a good relationship with Niri, so I kind of expected you that you will end up there. But look, at the end, you you you made my so I said, like, I think like six months ago, I was talking to somebody, I said that you will become VP before, before WAMSHI, so I didn't have that in mind. But, and that's not it, it was not for VP, it was for a partner, but it doesn't matter, it's still, it's still, it's still the same thing.

[00:31:46.57]  Jason ValleryEven verbally promised me partner, and then it didn't happen, and I got shit rewards, I'm like, okay, Maneesh, you've bitflipped on me. So I don't know what happened needy was pushing for it. He was pushing to make me a partner

[00:31:57.07]   RemoteBut

[00:31:59.07]  Jason ValleryI don't know it all went to hell. Oh

[00:32:00.99]   RemoteI said i'm not I I can't say that i'm surprised. Uh, knowing vamshi for like eight nine years now Yeah, he he's a really intelligent person but yeah, he can really be As a person he can

[00:32:16.51]  Jason ValleryThe verbatim, I sat and had dinner with him in person, in Redmond, I don't know, 18 months

[00:32:22.83]   RemoteAgo.

[00:32:23.52]  Jason ValleryAnd the verbatim statement he made to me is, "There's not enough room for the two of us

[00:32:26.70]   Remoteon this team."

[00:32:27.74]  Jason ValleryHe looked me straight in the eye and basically said, "One of us is gonna have to go."

[00:32:31.14]   RemoteAnd then he made it his goal from that moment forward to push me out. Again, I can't say that I'm surprised, that's a different story, but that person has some issues, right? I mean, even for me, right? I mean, you know how long I've been chasing a principal promo? So basically, when I decided to leave... He called me which he didn't call me for like months and he promised that he'll that he'll give me level 65 immediately I I said look. Thanks. I I gave my my word. I mean, I'm not kind of a person that will go against my word So he just basically told me look think about it. Like once you think about it, just send me a send me a note I'm fine. I said I'll think about it and I immediately knew my answer, but I said, fine. So I sent him and I am like two days later, he never responded, right? The guy literally never responded back. I just write, look, I appreciate your offer, blah, blah, like three sentences, right? I appreciate your offer, thanks for the kind words, but you know me as a person, I cannot go back on my word. I promised Mike that I'll move. if he makes me a principal, that's it, right? He never responded. After eight, nine years, the guy just couldn't write even like, thanks, look, sorry, whatever. Just write two stupid sentences, it's not that big of a problem. He literally never, never responded, right? So as I said, he's, ah, I'm not surprised. Anyhow, I am surprised that you left, but I'm not surprised that you left storage team, to be perfectly honest with you.

[00:34:14.17]  Jason ValleryYeah, I didn't see, I'm a storage guy at heart. I mean, I wanted to be in this space and work on these kinds of problems and have a lot of respect for VAST. You know, I mean, I did another thing that happened was I did a deep dive competitive analysis of the various storage providers. and how Blob stacked up to Vast, because that's really the root of what Project Apollo was to do, is to have a first party offering that competes with CoreWeave plus Vast.

[00:34:38.13]   Remote- With CoreWeave plus Vast.

[00:34:39.80]  Jason Vallery- So through that, I really got to know Vast, and Glenn came over, and I was chatting a lot with Glenn, and then I met Renan and Jeff, I don't know if you know the founders of Vast, and I really liked those guys, and I'm going to say this and it's going to sound terrible, but Indians are taking over Microsoft, and I was refreshed that this culture isn't that.

[00:35:01.06]   Remote- No, I mean, I completely agree on the culture side. It changed a lot and it's getting worse and worse. That's why I said, look, I'll give this role a try. Because at the end it's a completely new organ. It sounds interesting But yeah, I mean if it doesn't work if I see that the culture is the same I'm not going to stay for all for a long to be honest if it's a different story then definitely it makes sense for me to stay but otherwise Yeah, I'm not going I'm not going to stay a long time if it turns out to be the same Let's see. I don't think it will be the same, but you never know.

[00:35:42.97]  Jason Vallery- I got to bounce out of the meeting, I'm late for it, but great seeing your face. Always appreciated you, Nico.

[00:35:47.63]   Remote- Likewise. - Working together. See ya. - Enjoy, bye. (clicking)
```
