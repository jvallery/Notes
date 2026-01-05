---
entities:
  people:
  - '[[Maneesh Sah]]'
type: transcript
source_type: unknown
date: '2025-09-29'
---

# 1:1 — Maneesh Sah — 2025-09-29

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason shared disappointment with his rewards and anxiety about scope and support, noting multiple external offers and layoff concerns. Maneesh affirmed Jason’s value, especially on AI/OpenAI work, outlined a significant role for him in Apollo (GPU-adjacent storage, agentic systems), and committed to investigate rewards with Aung and consider future compensation adjustments. They discussed strategic directions: central storage vs GPU-adjacent caching, standards/ABIs for agentic memory, partnering with NeoClouds, and building a stronger NVIDIA relationship. Jason will consider options and update Maneesh by week’s end.

## Key facts learned

- Jason received 100% rewards despite a high-impact year and is disappointed.
- Jason has 13 years at Microsoft and strong OpenAI relationships.
- Jason currently has 2 external job offers and expects ~4 by end of the week.
- Concern: insufficient ownership/scope for Jason’s IC level and layoff anxiety.
- Juergen left; Jason feels Maneesh is his remaining champion.
- Apollo funded; plan to hire ~20 principal+ developers.
- Maneesh values Jason’s AI expertise for strategy and architecture (agents, post-training, KVCache).
- Discussion: central storage as system of record; GPU-adjacent storage as cache.
- Debate over POSIX/file APIs vs object/standard ABIs for agentic storage.
- Need to build Microsoft storage advocacy with NVIDIA; Vast has close NVIDIA alignment.
- Karthik to focus on agentic application stack; Jay to provide space for Jason.
- Jason has a significant stock cliff in July (year unspecified).

## Outcomes

- Maneesh will investigate Jason’s rewards with Aung.
- Alignment that Jason could play a key architecture role in Apollo.
- Recognition to build a direct storage advocacy channel with NVIDIA.
- Jason will update Maneesh on his decision/thinking by the end of the week.

## Decisions

- (none)

## Action items (for Maneesh Sah)

- [x] Discuss and debug reward outcome with Aung and report back to Jason. @Maneesh Sah ✅ 2025-10-26
- [x] Define proposed Apollo role and ownership scope for Jason, including collaboration model with leadership. @Maneesh Sah ✅ 2025-10-26
- [x] Plan approach to build Microsoft storage advocacy and roadmap alignment with NVIDIA. @Maneesh Sah ✅ 2025-10-26
- [x] Consider mid-term compensation adjustments for Jason over the next 6–9 months. @Maneesh Sah ✅ 2025-10-26
- [x] Inform Maneesh of decision/status on external offers and interest in Apollo by end of the week. @Jason Vallery ✅ 2025-10-26

## Follow-ups

- [x] Share a short proposal on Apollo strategy for agentic memory/KVCache and GPU-adjacent caching, including NeoCloud partnership model. @Jason Vallery ✅ 2025-10-26
- [x] Schedule deeper working session on Apollo architecture and Jason’s ownership areas. @Maneesh Sah ✅ 2025-10-26

## Risks

- High retention risk: Jason has multiple external offers and compensation dissatisfaction.
- Scope/ownership ambiguity may reduce engagement and impact.
- Potential competitive pressure from NeoClouds and vendors (e.g., Vast) if NVIDIA alignment lags.
- Resource constraints could force tradeoffs between app-stack integration and infrastructure.

## Open questions

- What concrete ownership and scope will Jason have within Apollo?
- When and how will compensation adjustments be applied for Jason?
- Which APIs/ABIs should Microsoft prioritize for agentic storage and inferencing (POSIX vs object vs new standards)?
- What is Microsoft’s partnership strategy with NeoClouds versus building overlapping managed services?
- Who will represent Microsoft Storage in NVIDIA roadmap and architecture discussions?
- Will NeoClouds build or acquire key-value/agentic stores, and how should Microsoft respond?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.00] Jabra Speak 710 :  Jason Vallery(computer chiming)

[00:00:22.50] Parallels Desktop : You (paper rustling) (keyboard clacking) (keyboard clicking) You you you >> Good morning. >> I'm doing okay. >> It's Monday. >> It's going to be a big week.

[00:03:45.56] Jabra Speak 710 :  Jason ValleryYeah. Is that, are there more announcements or is that just the, the Douglas?

[00:03:50.10] Parallels Desktop : No, I don't know. I think these guys will just keep cascading this stuff out. We did not have, generally they announce in July, this time it seems like it's almost October, so.

[00:04:00.47] Jabra Speak 710 :  Jason ValleryAnything happen in storage or is it just the stuff we see?

[00:04:04.06] Parallels Desktop : No, no, no, no, no changes in storage. plan and we were not part of this round of changes so we're not getting anything

[00:04:11.93] Jabra Speak 710 :  Jason Valleryno addition, no subtraction. I mean status quo is okay I guess better than subtraction.

[00:04:17.01] Parallels Desktop : Yeah, yeah in the current time status quo is not a bad idea at all. Yeah, exactly.

[00:04:22.85] Jabra Speak 710 :  Jason ValleryWell, how was your break? You know, it wasn't the break I expected. My wife had accident like the first week. It wasn't a big deal but she ended up needing a knee replacement so she had full knee replacement surgery kind of like right at the beginning of my time off so we weren't able to travel or do anything too exciting we were home the whole time and yeah I did stuff around here took care of her and my kids and my son and I He's a sophomore computer science major at the University of Colorado, and he and I spent kind of most of July playing around with vibe coding. Like we learned Codex and played around with Copilot and just really got our hands dirty and built kind of like a project together. So it was pretty fun in that way, and lots of good learning opportunity, and yeah, I went running, as you said.

[00:05:15.09] Parallels Desktop : I know you did work on yourself. It definitely shows up a lot more lean.

[00:05:20.85] Jabra Speak 710 :  Jason ValleryYeah that was pretty much my summer. Okay well you know I appreciate that you took some time to kind of have a chat with me because I do want to just level set on what my career looks like frankly just to put it out there I'm kind of a put it all on the table guy and I think you know that about me. I just have a lot of anxiety. Um, you know, I went into the break feeling cautiously optimistic, uh, feeling like I'd come back and be able to make a new home for myself and figure out what I was going to do next. Um, you know, I was going to be up front with you, like coming back and getting my rewards. I was very disappointed. Um, you I felt like, you know, 13 years at Microsoft, I've never had a year like I did last year. I really feel like I put everything out there. I was working 60 hours a week all year and I feel like I just really stepped up and come back and get 100%. Like it's not about the money as much as it is that felt like. If I'm going to be honest, it felt retaliatory. It felt like because I was about a manager that didn't support me that I came back to, well, we don't support you either, and that's left me in a kind of very unsure position about what my future in this team

[00:06:41.05] Parallels Desktop : Looks like.

[00:06:41.95] Jabra Speak 710 :  Jason ValleryI don't know if anyone gives a shit about me. and if they don't, what I should be doing with my career?

[00:06:51.23] Parallels Desktop : I will have to talk to Aung about the reward part of it. I have not looked into it. I went along with the recommendations I got. I can talk more about future looking stuff and then follow up on the rewards, Jason, if that works. - Of course, thank you for sharing it out. I will definitely go chat with Aung as to what was factored into the reward process.

[00:07:17.65] Jabra Speak 710 :  Jason Vallery- Yeah, I mean, I've got a big stock clip coming up in July and I'll tell you, coming back to that, I'll be all on the table. Coming back to that, I fully anticipated it. from the break I was actually feeling optimistic I was fully committed to making this role successful getting a number I reached out to some folks and so I've got you know there's no shortage of people in the industry that would like to hire somebody like me yeah my resume experience and I'll tell you I already have two job offers and by the end of the week I should have a total of four different offers to pick from and I don't know what that looks like. You know, I will tell you, I've got my Microsoft Crystal sitting over there on the shelf, and I will tell you, if you and I talked a year ago, I would have said I would have retired from this team. A lot of storage is in my DNA, you know, it's my core identity. You know, I love what we've accomplished over my time in this team, and I never thought there was a chance I'd really leave, but I have

[00:08:15.25] Parallels Desktop : Consider this week and I don't know what the next step is. Okay, okay, and I'm assuming both internal and external? All external. All external. Okay, okay. Well, thank you

[00:08:30.05] Jabra Speak 710 :  Jason ValleryFor putting it out on the table. Yeah. We'll see. You know, the time here meeting is interesting. because I wasn't sure where we would be at that point, you know, you and I met, but I have enough confidence to say now that I have other options on the team.

[00:08:45.93] Parallels Desktop : Okay. Um, is money the reason or are you worried about the work or?

[00:08:54.49] Jabra Speak 710 :  Jason ValleryI mean, there's a few things. Money's always a consideration. Like I said, I've got a big stock. year, and money is always a nice motivator, but I do worry about having scope for level, right? Like where I sit is I'm an IC with basically no real ownership of anything, who makes an awful lot of money on this team and whose skills are probably not being put to good use, and so, you know, in that world and layer that with the culture we've got of… layoffs happening all the time. I feel like there's a gigantic target on my back. You know, after Juergen left, I felt like I didn't have a champion in this organization anymore, and honestly, at this point, I think you're the only one that actually cares about me. So that's kind of where I'm sitting. Like, you know, I don't want to be the first guy out when

[00:09:38.81] Parallels Desktop : The layoffs occur. Yeah, I honestly will not worry about layoff for you. I don't know. what parameters they will define, but you're not in my list of people who I think I should offer, right? I'll just say it upfront and clearly. I tremendously value the work you did on the AI front and how far you got us along, especially in all the relationships you've built with OpenAI. I think in terms of your area of ownership, we were waiting for you to come back, honestly. Right? And I'll be honest, we were a little bit worried that would you come back or not. Right? Because two months break gives people a chance time to pause, and when you left, clearly, you were not the happiest person in the world. Right? With how the move had happened. So we were in a slight of a let's see when Jason comes back where his head is and what he wants to work on right I think you've seen some of the Apollo discussion there's a lot of work there right and I do see that with the background you have there's a lot of options for us to actually use your expertise in building the right AI system, and it's not just about training or inferencing, right? Like all the things which are happening with agents and post-training stuff. That's a place where I don't think we even have deep expertise to understand what the workload looks like, and I would love to be able to use your expertise in that space to actually. define our strategy and also talk about how do we build a system which actually goes against the scheme. Because I'll say this again, I think after 15 years of course I feel that storage is at the center of a workload rather than always being tagging along and forgotten. it is ours to lose, right, and I do need people who will actually make it land. I just got some funding allocated for Apollo so we can invest in actually making things happen as well. We'll probably have 20 devs hired, pretty much everybody, principal and beyond, just to kind of go quickly build a system. required. So, your expertise as an architect should be very valuable. Right? So, I do see a future. Regarding the cliff, I can go look at that in the next six months or nine months in terms of how to make sure that you are monetarily compensated well enough so that money is not a concern for you. I need time. I can't do anything right now but I will keep you in mind to make sure that I take care of it. I don't know your offer so you are in the best place to really judge whether your opportunities and upside financially are better outside. Probably you will get a good boost of stocks when you join somebody, but you will leave some behind. I'll let you decide on that front of it, right? You should make the best decision for your career and your personal life because money does matter, like you say, right? And all of us are in a phase of life where we need to make money in the next few years to plan for our retirement. I don't want to say that. that let go of those things. If you feel you are going to be better served in those places. But I do see significant upside for the work we are doing in AI. I do need strong people like you who can represent the team really good in front of others and can hold their own because the arguments and discussions fairly heated here in terms of viewpoints and positions and such, and you've done a really good job in open AI, in learning, in going and telling them what our system is and isn't. I do see the value of that as we work with OpenMAI and others to build AI. and they're seeing quite a bit of movement. So I personally am quite excited about where we will get to, and I do see a role for you.

[00:14:02.90] Jabra Speak 710 :  Jason Vallery- You know, I think Apollo is interesting. I mean, I see the problem space and I think about, you know, the need for us to pivot. You know, we have, we in this team have said for data has gravity, and the compute follows the data, and that's just not true anymore, and the data has to follow the compute. So I think fundamentally, Apollo being distributed caching, GPU adjacent storage, is a paradigm shift that requires us to rethink the platform, and so being at the beginning of what needs to be, in my mind, a new stack, is exciting. love to be part of that. I think I could add a lot there. I just worry about true ownership scope, who I'm going to have to collaborate with, what my opportunities to really influence others will be, and if that's work that I'm going to be well-positioned to go do, and

[00:14:55.50] Parallels Desktop : so that's a huge apprehension for me, what I actually get to do. No, I appreciate the things that you are saying and I can see why you might be worried as well, and I think working for Jay, he is non-territorial and very good and smart. He will create enough space for you. I don't worry about you getting overshadowed or... not getting enough of a scope for you to go do it. In fact, I would love to actually have somebody with high bandwidth who can think through and come up with the right strategy and architecture because I have a small number of high bandwidth people and we are realizing that we need more bandwidth just to handle all the things which are coming through. at us, right? My go-to people right now are Jay Jagant on that side for the most of it. I brought in Karthik, but I really want him to focus not on the infrastructure side of things, right? At least not on the infrastructure training at all. I really want him to focus on the agent side of the world because I think that's the place. where we have a chance to work on defining the application stack rather than just implement what gets thrown at us at some point of time. So how do you think about agentic memory, KVCache, and all that stuff? I want him to just focus on that piece of it, and then maybe a subsection of how do we integrate AI into our products such that our customer-facing products are more AI-friendly, so having somebody like you would definitely

[00:16:38.32] Jabra Speak 710 :  Jason ValleryCreate bandwidth in the team, like I said. I saw your note over the weekend about the NeoClouds, and I think a lot about this agentic problem and how inferencing is going to work and how customers are going to select their inferencing. providers, and I think one of the biggest mistakes I still maintain, Manish, after all this time is we said we're going to go build our own API for storage and we're going to stick to it no matter what. We're not going to adopt the industry standard that is S3. I see that space needing an industry standard, a clear API that all of the providers go implement. I expect all the neoclouds are going to rally towards that vision and then become the commoditization of how you go and run these things because their advantage is they move fast, they build fast, they'll end up having lowest cogs and they'll end up being able to eat a lunch on price. I mean, how do you think about that? I think that's going to end up just being a commoditization play. then it's going to be a differentiator in value.

[00:17:42.09] Parallels Desktop : My take is that industry is still consolidating behind the POSIX file system as the application exposes API, right? And everything is going to just sit behind it. You can plug in anything you want, so long as it has the performance and the scale, and at some point, cost will also come into equation because thus far, it has always been, "Hey, who cares about storage costs? GPUs are so much costlier, just throw the money at it." But now I see OpenAI actually squeezing us really hard on the storage pricing as well. So I think I don't see a. object storage API being the way apps integrate. Everything will probably just sit behind some file system API. I mean, that's what I see right now, because even 4V, which has built its own object storage system, they put it behind a cache so that you don't ever see that object storage system directly.

[00:18:42.67] Jabra Speak 710 :  Jason Vallery- Yeah.

[00:18:43.51] Parallels Desktop : - Right? everybody's going that path. I think S3 versus Blob will probably be in material discussion.

[00:18:51.42] Jabra Speak 710 :  Jason Vallery- Well, I was, just to clarify, I was making the point that we were, in my mind, still on the wrong side of the decision of not adopting industry standards. I'm not saying it's an S3 versus Blob question. I think it's more of a, the industry will likely coalesce around standard ABIs. for how you do agentic storage and memory and KB stores and probably have some sort of coalescence around even how you deploy and manage the managed inferencing stack, and so as those things start to coalesce, like where do we fit in that equation? And let me just be a little more transparent. Obviously in all of these conversations I've had very recently, I've maybe talked to folks like CoreWeave And so yeah, and they're all of this mindset and I think it's the right mindset that they'll never be the storage system Right, right. They're not they're not going after CPU workloads. They don't want to go in Databricks They don't want to go win backup workloads. They don't want any of that, right? They just want the GPU inferencing business because that's where the money up and so they're building these caching layers thinking that what? are going to end up doing is having, you know, customer's data will sit in Azure and in AWS and in Google and maybe on-prem, and then they'll need to have some sort of local representation of that that they push and pull back. So, geo-namespace, hierarchical storage, cache are all the things that they're looking at building. I think about that in the lens of Apollo, what has to be replicated within our stack, but I worry about, like what you said, is building sort of value above the platform versus building into an industry ecosystem and leveraging our infrastructure as the strategic advantage. I think like those are two different pivots you can kind of take with us.

[00:20:33.79] Parallels Desktop : They are, and I don't know, I haven't. understood or heard enough about Corvi wanting to attach to one of the hybrid scalers because that's where the customer data might be. I think that's something as we work on Nibius and some of the other places we'll probably learn a lot this year in terms of how we actually build and integrate with those systems because we're going to have mostly GPU capacity. in those places and nothing else and how do we serve as the persistent store and they are the cash do we need to put our cash there that's the discussion which we need to go solve we are investing and looking into multi-region training and such so in my mind I don't know if it will be either all one of the things I What I am trying to do by being in the app stack is that one of my mistakes, if I look back, is that we kind of stayed at the just impure in front level all the time. There was a lot of programming and other things were actually fairly marginalized in terms of how's the app evolving, what do they need from storage for them to run. be successful and if you are not in that space then you actually just never get the direct feedback you need. So I'm trying to this time lay it out such that I don't play this either/or game to the extent possible and if resourcing does not become a huge issue for us, thread the needle in a way that we build storage for If resourcing becomes an issue, then we have to choose our bet and say where does our future lie, where do we have to spend more resources, and where the money will come from, right? And thus far, interest is where the money has been, right? Just because of the volume of storage, which gets consumed. So I would love to hear if you have more thoughts on what is... our role in this new cloud world where we are complementing them rather than fighting it out all together. I think there will be competition for sure.

[00:22:41.95] Jabra Speak 710 :  Jason ValleryWell, I mean, I think of what OpenAI has today. They have central storage and then they have the the GPU adjacent storage, and I think the central storage is ours. like the Neo clouds are not going to go build exabyte scale ZRS where you're running all of your line of business applications on top of it and doing data ingestion and processing. They have no aspirations, nor do they have the ability to execute against something like that, and so fundamentally, all of these GPU fast build regions are a cache, a cache of the central storage. A read/write catch perhaps, but that data is not in those GPU regions as a system of record. So I think it's two things. You have to partner with the Neo clouds, enable them to build a business model that allows them to push and pull data from central storage efficiently, and replicate that same stack internally for where we build Apollo-like data centers and that's the capsule layer and that in the you know GPU adjacent flash-based high-performance storage. I think those are the two you have to do.

[00:23:47.23] Parallels Desktop : No, fair point, fair point. I think NeoCloud what you're saying probably will be there. I do see them moving into a little bit more of the managed So I don't know where they will draw the line and say no more, right? Like WASP going into object storage to me is a little bit of that, right? They're trying to probably get rid of WASP at some point of time and have more control of their stack. But if I were to believe what you're saying, you're saying that they will not build anymore. they'll stop there, they will not add more managed services, so to speak.

[00:24:28.93] Jabra Speak 710 :  Jason ValleryI think the key value store scenario is one that still needs to be fleshed out. I think Vast has a good vision.

[00:24:33.56] Parallels Desktop : I think they will build something like that, because that's very integrated as part of the app stack, and they probably don't want somebody else to be playing. That's one challenge Vast is facing, to be honest. I said, "God, many of these new clouds started," but they are realizing that as time goes by, these people will invest and then marginalize who lasts in some ways.

[00:24:55.63] Jabra Speak 710 :  Jason ValleryThe flip side is that it's going to be hard for CoreWeave and others to go and replicate a platform like VaST or even Azure Storage. We've had a decade at start. VaST has got whatever, start. They've got hundreds of engineers. We've got whatever 1,600. I don't know how many you've got at this point. I don't see like CoreWeave or Crusoe or any of them like being able to go

[00:25:19.01] Parallels Desktop : And replicate a mature storage platform anytime soon. Yeah, with the amount of money they have, storage companies are fairly cheap if you leave vast out of the picture. might see some acquisitions happening. I guess $3 billion is not a big deal for these guys. You might see some acquisition like Weka, DDN, and some of these others might just go up for sale.

[00:25:44.97] Jabra Speak 710 :  Jason ValleryYeah, that's a fair point.

[00:25:46.00] Parallels Desktop : Yeah. I don't think Vaast can be bought just because of the size of what the market cap is. just too big. So Vast is aligning very deeply with NVIDIA. Met with a team and seems like there's at least a quarterly one-on-one which Renan gets with Jensen, and they tell them that, "Hey, this is what I'm building in the next GPU. I have to system with this. Right, so that's the reason why mass comes out almost immediately after the NVIDIA announcement. Yeah, they had opportunity to work. Yeah, yeah, we have no such connection. We need to actually start really seeing with all the Microsoft connection into NVIDIA, how do we get that kind of start and start to build storage. line to what NVIDIA is planning to release?

[00:26:40.64] Jabra Speak 710 :  Jason ValleryI don't know if you know, I'm sure you know, Jack and Nidhi's team, you know, I think he's probably one of the best connected folks at NVIDIA. I actually had a one-on with him last week and I was asking him some of these same questions around where they're headed and what their roadmap looks like and what should we do. He really didn't have a sense, you know, in his conversations that really isn't coming up. representation that's meeting with NVIDIA advocating the storage interests?

[00:27:04.67] Parallels Desktop : I think we need to build that. I think we need to build that. You are right that we don't have one. But we got to build one because if we don't, then we're going to have a real problem. Right? Because we will constantly be chasing the tail and then you look at last and they'll continue to have the mindshare. That's the kind of stuff I want to go change. because the world is evolving fast and there is value in being for a small world in a bunch of these places.

[00:27:31.64] Jabra Speak 710 :  Jason ValleryYeah.

[00:27:32.60] Parallels Desktop : Right. So, think about it. Like I said, I value the work you put in and I will go debug your rewards thing a little bit. I do see. a lot of possibilities in what we are looking at and I will go work on the financial parts at some point over the next six months or so.

[00:27:59.53] Jabra Speak 710 :  Jason ValleryYeah. Well, let me see how this week goes and, you know, I'll ping you by the end and let you know where my thoughts are.

[00:28:06.26] Parallels Desktop : Okay. Sounds good. - Thank you.

[00:28:09.01] Jabra Speak 710 :  Jason Vallery- I appreciate you. Thank you.

[00:28:10.75] Parallels Desktop : - Bye. (computer chiming)
```

<!-- ai:transcript:end -->
