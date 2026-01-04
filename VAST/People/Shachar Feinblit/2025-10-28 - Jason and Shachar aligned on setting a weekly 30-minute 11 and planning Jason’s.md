---
type: "1-1"
created: { { DATE } }
status: "done"
counterpart: "[[Shachar Feinblit]]"
role: ""
team: ""
company: ""
series: "1-1/Shachar Feinblit"
cadence: "Weekly"
meeting_mode: "Video"
location_or_link: ""
calendar_url: ""
start_time: ""
duration_min: "30"
privacy: "internal"
ai_extracted: true
transcript_path: "00 Inbox/Transcripts/20251028 1044 Parallels Transcription.txt"
tags: [meeting, "1-1"]
---

# 1:1 — Shachar Feinblit — 2025-10-28

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Shachar aligned on setting a weekly 30-minute 1:1 and planning Jason’s Tel Aviv visit (Nov 23–26) to meet key teams, share cloud platform knowledge, and conduct cloud architecture/design planning. Shachar suggested contacts across UX, release management, support, cloud teams, and solutions; he may move the monthly all-hands to that week. They discussed AI/automation usage (Cursor, prior Copilot; experimentation, focus on analysis/CI/bug triage) and debated a formal AI center of excellence vs organic innovation. Shachar asked for stronger technical depth and end-to-end involvement from product; architects currently write FRDs, and Jason will explore upskilling and recruiting more technical PMs.

## Key facts learned

- Weekly 30-minute 1:1 to be set between Jason and Shachar
- Jason visiting Tel Aviv 2025-11-23 to 2025-11-26
- Cloud work split: Ronnie and Max lead two teams (VMs vs platform aspects)
- Release management: Noah and Yael Treitel coordinate; Roit Suhr manages 5.5; Orly manages 5.4 and will move to 5.6
- UX: Liron; Support: Omri; Solutions: Ronen (lead) and Dotan (cloud with Intel)
- Potential team all-hands may be moved to align with Jason’s visit
- Shachar’s org uses AI tools (e.g., Cursor; previously Copilot; evaluating Windsurf) mainly for analysis, CI, and bug triage
- Feature planning buckets: tactical deal-driven, strategic innovation, and technical debt
- Architects author detailed FRDs; product depth needs strengthening
- Mordecai: between product/program, less technical; currently reports to Alon; Jeff considering moving him to a different team

## Outcomes

- Agreed to establish a weekly 30-minute sync
- Plan set to build a Tel Aviv visit agenda including knowledge sharing and cloud architecture/design sessions
- Shachar will share a list of people for Jason to meet; Jason will set intros
- Shachar will consider moving the monthly team all-hands to the Tel Aviv week
- Alignment that product should increase technical depth and end-to-end product involvement

## Decisions

- Establish a weekly 30-minute 1:1 sync between Jason and Shachar
- Proceed with Tel Aviv visit on 2025-11-23 to 2025-11-26 focusing on knowledge sharing and cloud planning

## Action items (for Shachar Feinblit)

- [x] Find and propose a time for a weekly 30-minute 1:1 with Shachar @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Draft Tel Aviv (Nov 23–26) visit agenda: knowledge-sharing session, cloud architecture/design planning, and key team meetings @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Provide a list of recommended contacts for Jason to meet (names in chat) @Shachar Feinblit 🔼 ✅ 2025-11-08
- [x] Set up intros/1:1s with key contacts (Ronnie, Max, Liron, Roit Suhr, Orly, Omri, Ronen, Dotan) ahead of or during the visit @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Check feasibility of moving the monthly team all-hands to the week of Nov 23 so Jason can join in person @Shachar Feinblit 🔼 ✅ 2025-11-08
- [x] Connect with Mordecai after syncing with Jeff on potential team move @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Prepare and deliver a cloud platform knowledge-sharing session for the Tel Aviv visit @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Align cloud architecture/design planning sessions with Yogev and Asaf during the Tel Aviv visit @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Evaluate plan to strengthen product’s technical depth (upskilling and recruiting pipeline for technical PMs) @Jason Vallery 🔼 ✅ 2025-10-28

## Follow-ups

- [x] Confirm preferred time windows for the regular weekly sync @Shachar Feinblit 🔽 ✅ 2025-11-08
- [x] Verify date/time of the monthly all-hands and whether it can be moved to the Tel Aviv week @Shachar Feinblit 🔼 ✅ 2025-11-08
- [x] Decide on Mordecai’s team placement @Jeff 🔼 ✅ 2025-11-08
- [x] Provide the final contact list for Tel Aviv meetings @Shachar Feinblit 🔼 ✅ 2025-11-08
- [x] Reassess AI-based performance analysis with newer models in a few months @Architecture team 🔽 ✅ 2025-11-08
- [x] Consider a lightweight forum (e.g., all-hands highlights) to share AI tool success stories @Shachar Feinblit 🔽 ✅ 2025-11-08

## Risks

- Resource constraints and competing priorities between cloud and insight engine work
- Deal-driven tactical features may increase product complexity and technical debt
- Lack of a formal AI center of excellence may limit systematic productivity gains
- AI tool licensing lock-in can hinder rapid tool switching
- Scheduling constraints on Shachar’s calendar could delay coordination
- Product team’s current technical depth and limited end-to-end involvement may slow execution quality

## Open questions

- What exact time will the weekly 1:1 sync be scheduled?
- Will the monthly team all-hands be moved to the week of 2025-11-23?
- Who is the QA lead for cloud that Jason should meet (name unclear in transcript)?
- Will there be any formal structure (e.g., center of excellence) for AI practices and training?
- What is the final decision and timeline for Mordecai’s team transfer?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.04]   RemoteGood. Good.

[00:00:02.00]  Jason ValleryThanks for taking a few minutes. I kind of wanted to just reconnect now that I'm officially in role and, you know, week one is behind me and make sure we establish a good working relationship together and I can kind of learn from you how best to collaborate. A couple of tactical things. First, I want to do, I do want some sort of regular cadence with you. We can kind of talk about top priorities and how best to work with your team. I just wanted to double check, are you okay if I find a time for us to have like a weekly 30-minute sync?

[00:00:38.62]   RemoteYeah, yeah. Of course. Especially when you start, you probably need more coordination.

[00:00:45.02]  Jason ValleryYeah, yeah, I mean we can evolve it over time obviously, but I just want to make sure that I'm working with your team and setting, you know, things up with you correctly. Okay, so any guidance on what time of day works for you or should I just find an open slot in your calendar and try to make it work?

[00:01:01.02]   RemoteNormally I prefer if it's very late to do it only if it's customer, but whatever. - It's not that easy to find time, so find something and it will be okay.

[00:01:12.03]  Jason Vallery- Okay, we'll evolve it and I'll try to find an empty slot that looks friendly.

[00:01:15.51]   Remote- It's so difficult, I will let you know, because I have some slots that are, I have some slots that for meeting, I'm not really joining. So we can put something, okay?

[00:01:34.27]  Jason Vallery- Okay, we can kind of collaborate offline and find a good slot, but I'll take a first pass at it. So, you know, one of the things that I'm quickly learning in my first week is that a lot of the work that we're going to have to do to make the cloud successful really sits more with your team than Yancey's team. he's going to be owning all the control plane work obviously in the marketplace work, but when I actually think about what happened to the platform itself you know there's a bunch of stuff we're going to need to do together, and so I'm coming to Tel Aviv on the 23rd through 26th of November and I kind of want your help navigating the team. and setting up the right agenda around it and you know I see a few different topics for discussion you know first I think there's a knowledge sharing opportunity where I can sort of answer the team's questions around cloud platform opening I workloads Azure you know really just be able to share my experience and knowledge around those things with the team and then I'd like to have some like cloud planning conversations around architecture and design. It's just been great with connecting me with, you know, Yogev and Asaf. I don't know who else you'd want me to start having conversations with and how I You know setting up an agenda for that week

[00:03:02.94]   RemoteI think it's important that you are also meet the UX team Okay So the one from the UX team (typing) Maybe the release manager for five, five and five.

[00:03:30.65]  Jason Vallery- Noah and, oh, I forgot the other name. Who are the release?

[00:03:35.73]   Remote- So basically what I'm doing, like Noah and Yael Treitel are arranging the release manager. like the tactical selection, but then I have someone that is running the release until the end. So I have Roit Suhr that is managing 5-5 and Orly that manage 5-4 and she will jump to 5-6, okay? So it's good that you will meet them. I think the actual team that is doing the cloud work, so we have Ronnie and Max that are leading two teams that are, one is more working on the VMS side, the other one is more working on the platform aspects. I think this will be good and you will be up if it's not sounding I need to check when is my monthly meeting so but I think it will be good I'm doing like once a month all end with the team is if you can introduce yourself I think it's Opportunity and I'm not sure if it's that week. But if not, let's On I Can also move it. I think we had maybe it's that week Because we had last week Maybe I can move it to the way to that. You are you are So you'll do it in person. What else? Maybe, I don't know, maybe you want to meet the support team as well.

[00:05:37.61]  Jason VallerySo maybe if, I don't know if you want to put them in the chat or something, you could type out some names of folks I could reach out to and start getting to know. I've got syncs already established with Noah and Yael, I'm meeting the two of them soon. But if there are other folks that you're thinking of that I should kind of maybe introduce myself before I show up in Tel Aviv, that would be good.

[00:06:03.19]   RemoteI'm writing here, so I will stay on Omri for support, okay?

[00:06:10.40]  Jason ValleryYeah.

[00:06:11.27]   RemoteI think, and Ronny, Lazard. Yeah. I've been... I don't know. I don't know. Um... I don't know. I don't know.

[00:06:20.27]  Jason ValleryI don't know.

[00:06:21.27]   RemoteI don't know.

[00:06:22.65]  Jason Valleryon a couple calls with Ronnie already. We haven't had a one-on-one to connect yet, but I'll set

[00:06:26.97]   RemoteSomething up. I'm not sure that you, but if you are in Israel, I'm not sure that you need to dedicate before, but in Israel, just say hi. Liron. for the UX okay okay you already told me that you spoke with your given stuff

[00:07:02.49]  Jason ValleryYeah you're giving us off I've met with already and I've got more time with them

[00:07:05.23]   RemoteScheduled yes maybe a new is like the QA for, leaving the QA for the cloud.

[00:07:12.78]  Jason Vallery- Okay.

[00:07:31.84]   RemoteOkay, and who else? Maybe the solution team, okay?

[00:08:00.35]  Jason ValleryOkay.

[00:08:00.68]   RemoteWe have a solution team, so Ronen, that's leading the team, and Dotan, which is more focused on cloud with Intel.

[00:08:15.20]  Jason ValleryTeam? Okay, I think you have a good list. That's a good list, that will keep me busy.

[00:08:26.94]   RemoteLike a team, join team meeting, team all hands. I will try to, let's see if I can move it. to the way you are there, if not, we'll do it from remote.

[00:08:41.11]  Jason Vallery- Okay.

[00:08:41.95]   Remote- In US, did you meet Alon?

[00:08:48.95]  Jason Vallery- Yes, he and I are chatting about a couple of things already, so yeah, good relationship going now already, and then, yeah, my inflection situation is, and opening eye as well, I've been chatting with him those because there's some good facts and existing knowledge that he has so good.

[00:09:04.68]   RemoteMaybe also Mordecai.

[00:09:07.64]  Jason ValleryMordecai?

[00:09:09.16]   RemoteMordecai, yeah.

[00:09:11.24]  Jason ValleryYeah, Jeff mentioned, I have an open question to Jeff around that, so I'll reach out to Mordecai after I talk to Jeff, but yeah, he's on my list.

[00:09:18.84]   RemoteOh, I think Jeff. - Jeff has an idea to maybe move him into a different team.

[00:09:26.23]  Jason Vallery- Yeah, yeah. - Okay. - I think that's a good idea. So I'm waiting to hear from Jeff.

[00:09:29.82]   Remote- Anyway, I can tell you the story about him if you have anything.

[00:09:33.51]  Jason Vallery- I'd love to. Yeah, sure. I always appreciate insight.

[00:09:36.74]   Remote- So the story, so it started as like, the CE for Lior Grimm, and in saleskeep last year he came to me and told me that he doesn't have enough work. That's okay because we are still building the product and he feels that he doesn't have enough work yet. So I... So I told him to join a loan to help with the work with the new clouds, okay? And I can tell you that is somewhere between product and program, okay? - Thank you. is not like super duper technical. He knows how to arrange things, he can write best practice, and he can collect status and requests from new cloud customers. But when you need a little bit more technical, it's better to have more people. in the color of the customer, okay? This is like the eye level right now. So it was some sort of workaround to, like, we have so many things to do. If someone is telling me that he doesn't have enough work, I just give him some work, okay? But if we put, I think whatever we do, that he will have the even the unofficial work with Talon that he's doing a lot of work with the new clouds okay but I think we can manage him better like like Talon gives him tasks I'm not sure he's really managing okay to right so so maybe it's a better infrastructure in product uh to have him there and yeah i mean but but don't expect him to be the most technical uh product managers is okay technically not more than this okay just I don't want to sell you more than it is, okay?

[00:12:05.96]  Jason ValleryYeah, one of the things that I had asked you for, I think, is somebody who can do a lot of the blocking and tackling, and as you say, it's connecting on status, chasing vendors, chasing partners, you know, I think that makes sense. So it sounds like I can leverage it in that way versus on the technical front. Okay, well, I'll connect.

[00:12:22.82]   RemoteBut also on this meeting with the customers there, sometimes we need to organize all the inputs and requests so it's not like, like, like when I speak with customers, sometimes I'm not doing all the photo ops, right, I'm asking someone to do a thumbnail. I'm trying to do the follow-up, but you know, it's a, so if you have someone that owns it, I think this is something that is helping us. So he knows what core is one, and he helps us like with inputs, like for instance, for Yael when he plans the minor version make sure that we don't forget like this small request for code, okay, for instance. But you will not be the one to challenge them. Why do you really need this? And maybe you can do it differently and what are you trying to accomplish? So this, you will need a little bit of help there. Okay, but then it's clear he will follow up well on the things that needs to be done. Okay.

[00:13:38.49]  Jason ValleryOkay.

[00:13:39.48]   RemoteI'm looking forward to meeting. Okay. Okay. Okay.

[00:13:43.48]  Jason ValleryIs he, so he's not in line to a loan right now, or is he reporting to a loan?

[00:13:50.16]   RemoteHe's reporting to a loan. Okay. he was reporting to Lior and I took him because yeah I don't like I like tattoo type of people right people they don't have enough work and feel good about it you don't want them in the company and people they don't feel good about it so they will leave if you don't give them enough work. So it's also good, right? So I felt he is a guy that he needs the real work. So I felt that I don't think occupying well with the new class and I think it. it was done. I think now that we'll have more of hyperscaler clouds, maybe it can do more of the things and that's more of the thing that he was originally hired for, right?

[00:14:56.28]  Jason ValleryMakes sense.

[00:14:58.52]   RemoteAnd then it makes sense.

[00:15:00.48]  Jason VallerySay. Okay. Okay. Another question. So I want to understand how you're thinking about resourcing and just how you plan and you're at your level, like how you're thinking about decisions on what projects you're funding. You know, I talked to Lior and Lior's perspective is very much, resources, we don't have enough cycles on these things, and I want to just intersect that with the culture I'm leaving and what's been kind of happening at Microsoft most recently, and so very specifically, what I'll call out is that Microsoft's engineering organizations, and Azure Storage being a key example, are fully embracing AI development. and really trying to culture shift the top engineers away from writing code to becoming architects and managing AI-driven development pipelines. There's plenty of industry reporting about the layoffs and what it means to be a software developer in the future, and I'll tell you personally, my son is a computer science major right now in university, and I don't know what the future looks like for him. But what are you thinking about as the dev leader in terms of how you transform the dev culture, how you resource things going forward?

[00:16:30.33]   RemoteSo, it really depends on the layer of the stack, okay, you're focused on. For instance, if you look at what we do with the UX/UI, it's the amount of kernel code there is much bigger than the, I don't know, kernel patches that we're building, okay? Because it's the nature of things and the amount of examples that you have and stuff like this. Almost all of our developers are using cursor. We are using AI tools to optimize the cycle like finding duplicate, like a lot of it is also like if you look at the development cycle, developers are most of the time not developing. They are analyzing, testing, and yeah, they are also writing code, right? So we put more focus and effort on the one hand to just use standard tools to write code faster, but more... or dedicated focus on the scabbing of the bugs, analysis, assigning the bugs to the right teams. It sounds like trivial, but it's not always that trivial, and it can cause a lot of inefficiencies, optimizing the CI cycle. and like if you have a problem with CI it's always a question if it's my problem or someone else's problem right and maybe someone like there is a bug like not the in the in upstream that is not like consistent and if people do not understand it they might touch in their code something that is unrelated so a lot of effort is around not just writing code, but also making it production ready, and so this is the area we put more, by the way, AI, but also automation, not everything is AI, okay, so there are things that you can do also with automation. automation. I think in a company like Microsoft, you have more overhead compared to us. I assume so it's It's easier to say, okay, let's cut 20% because AI can do it. But I'm trying to grow slower than without AI.

[00:19:46.91]  Jason Vallery- What kinds of career--

[00:19:54.04]   RemoteI think that I feel that they are a little bit hyped and they are not as successful. Like, if you look at code maintainability, sometimes it's very difficult with the code cursor deliverance, okay? So, we have some practices how to use it. it's not always, but we did a lot of like things, for instance, we started with copilot, we switched to cursor, now we're talking about windsurf and others, so we will keep, we are keep looking at what is the best tool, and sometimes it's difficult, by the way, because you're buying a license for a year and you don't want to switch every month and pay twice, right?

[00:20:50.36]  Jason ValleryPersonal experiences with Kodak. Well, I mean, I've used a variety of them in the past. I don't know how much I share, but I took a couple of months off over the summer for and I spent most of that time with my son working on projects, and Codex, like OpenAI's Codex model that came out in August, and its ability to really spend a day or longer on a long-running process. It deploys, it'll do deployments, tail log files. I was just really stunned about about how capable it has evolved even compared to where you were with like Claude six months ago. So I guess my key point is, like, do you have a center of excellence around this within Tel Aviv that's really looking at what the frontier of these models can do and how are you like training, bringing folks up to speed, encouraging them to do the right thing? encouraging the use, identifying new use cases, like what's the plan on how you continue to evolve the dev process and the use of these tools as they become more mature to make sure we're sort of amplifying the productivity of the team?

[00:21:59.32]   Remote- Actually, what we are trying to do is to use our tools to do it your own dog food. So for instance, we have tools. that help perform initial analysis of a ticket, using a pipeline that we built with the data engine, and many of them were just initiatives of people within the company. that, so, we also have a team that are building applications like part of the, like, the developer in the architecture team and developer in the solution team that are building application on top of the platform, and it's always varied between like internal use and building demos to customers and solutions or to partners. I can tell you that From what I saw, this is why I put more focus on bringing something to production. So far what we saw is that bringing data which is non-production. is much, much, much, much faster with bytecoding. But to transform into production quality, it's a little bit more difficult, and there are other tools, and we are doing more proprietary stuff, and we are also learning, like, best practices of how to do stuff. I can tell you that many of my developers, they put more focus on, like, analyzing tickets because they don't like to analyze tickets. So there are a few parallel initiatives, and I'm okay with parallel initiatives around AI, like the best one wins, right? So it's okay to do it. Maybe we can do more, by the way. But there are also some initiatives that were less successful. For instance, we tried to do performance analysis like getting all the HTOP and PERV and other statistics and prices and to better analyze performance and where we can improve performance and To be honest, even if it fails, you need to do it after a few months again with a new model. But for instance, we tried it a few months back and it was not beneficial enough. It was consuming many tokens and our output was not high quality. But I think it's a matter of time. So we just need to try, I think.

[00:25:32.62]  Jason Vallery- Yeah, I mean, that's my meta point is really, you know, I would love to see a center of excellence within your team. That's really just tracking these capabilities, planning how to use them, evangelizing them, identifying use cases. You know, one thing Microsoft rolled out is like forced training on all the dev teams. So like every two weeks, a full day, where the devs are just off of their project work, and they spend the entire day in a virtual workshop, and then that center of excellence team is leading a topic for that cycle. Like, here's a scenario, use case, how you should use it, and it's deeply thought about in the context of the end-to-end pipeline, like, you know, stores there's well-established tools and processes and frameworks and a whole bunch of internal stuff and so it's like here's a scenario of how we can make this work with our existing process. I don't know just just food for a lot. I mean I'm a big proponent of these things.

[00:26:33.08]   RemoteI personally don't like this organized... is innovation, meetings, or stuff. I think it should just happen by nature. I think, at least I'd say with my team, they really want to do it. So they are just doing it, even sometimes in their spare time, and I want everybody to have the opportunity to do it, not just okay, this group of smart people, right? So this is more our DNA. I agree that sometimes you see that... it is important and it's not done enough, then you need to assign it to someone. But with this type of thing, normally it happens by nature, okay.

[00:27:42.67]  Jason Vallery- And I think it's a forum to share the success. So if you're doing it organically and you've got somebody who accomplishes something cool and it's impactful, you know. bringing them to your all hands and saying, look, this is what they got, they got done and how it works and so forth. Sharing that kind of thing is an important component too.

[00:27:57.13]   RemoteYeah. So it's sharing, but also people are sharing on Slack. Yeah. So they are not really always waiting for the monthly all hands meeting. Okay.

[00:28:08.44]  Jason ValleryWell I mean I'm asking this just in the lens of obviously we've got a lot of cloud work to go do and we've got opportunities to improve productivity of the team and I hear a lot of anxiety around you know what kind of resourcing is available so I'm just kind of encouraging out-of-the-box thinking around what we can do.

[00:28:32.76]   RemoteFocus so we have of course we can also improve productivity and we can grow the team but also we are doing so many things that sometimes some of the projects are less important and it is what it is. Last year we put less focus on cloud, now we decided to put more focus. We brought also the Yonsei team. and double the core team doing clouds and of course we can do it also five times faster but we also have areas with revenue we want to do for instance we put more focus on the invite engine than cloud over this year for instance okay. and we made huge progress with insight engine and it's but it's okay for you to to want more but i'm not it's not always the right decision and great but i agree i think and I don't think that AI will do 3X, OK? So we need to go with it. So we are going the cloud thing quite fast, and we are recruiting the right people. So we are not compromising on the quality of the-- throughout LinkedIn.

[00:30:25.32]  Jason Vallery- Oh, that's good to hear. I mean, I think, so to turn it back to you, like, what can I do to support you and your team, you know, across a bunch of things, you know, process and product management rigor being what's top of mind, and I've got some initial thoughts, even just based on what I've discussed with Tomer, but I would love to hear it from you.

[00:30:45.84]   RemoteI can tell you that a good part of what, I think I told it during the interview, that in many areas, products are more outbound in a way that they are telling what is being built and not enough parts of really defining what to build okay beyond the title that you know we need a support a means and really gets insights from customers and be able to create like to have a good technical discussion with the customer so I think I think we need to level up the depth of the product team and so this is something I think you can you can help and like like if you look at Tomer or Jonathan they they are part of many customer meetings but like the focus is to present the roadmap or and to get like the high level request. But in the past, we tried that they will create the detail requirement document and it was a little bit, and it was like a marketing MRD, more than like a real technical requirement document of what needs to be built, and after we tried it for a while, we would say, "Okay, let's have the architects do it." I think it's working fine, but I want the product to do more. this okay the other thing that i believe products should do more is to be involved in the full life cycle of the product and by that i mean not just saying what need to be built and as I said to do it with more like a little technical but also to play with the product to see that oh what what will be is what I meant okay and just okay this is what I asked okay you understand what I mean so and then of course then you're also more relevant with customers because you understand not just what someone told you, how it is working and not of the limitations, you felt it with your hands, and so I feel that the product right now in the very early, OK, we need this feature, without defining the details of it. In the very end, to talk with customers after they used it, OK? And not in the middle, to really invoke the product, OK? So--

[00:34:26.66]  Jason Vallery- Let me give you a couple of thoughts. So-- I think the existing team, we can do things to up-skill and try to bring that technical expertise, but it's a real challenge to take somebody who doesn't have that background and bring them into a highly technical, highly hands-on kind of role if they just, that's not who they are or where they came from. So there's a recruitment pipeline problem there. is you have to source candidates into those roles that come from the right background and so certainly like when I've been hiring in the past I would have been looking at folks that wanted to make that transition from software developer to product because they see that sort of best of both worlds and like that's myself so I think you know we can address that as resource and

[00:35:15.66]   RemoteAnd we grow the team and then until we do it, because I just need to say what

[00:35:25.06]  Jason ValleryYou want, not to do it, right, you know, the controversial take here, like, you know, if you've got a really strong technical person who also has the product skills and the customer facing skills, that person writing a detailed architecture technical requirements design empowered with AI coding can get pretty far on their own. I think there's a world where that trend of the best architects, the best developers on your team shift a little bit to look a little bit more like a product manager over time as these tools become more capable. I'm not saying that's the state of the art today, but I think there's a road.

[00:36:09.24]   RemoteI can tell you that my most capable architects are writing the FRDs because we need the detail and the planning, and then I want them to talk with customers to make sure that coming with the right requirements to what customer really care about, right? I agree that it's super super super important, and I agree that AI can help, yeah, that's for sure. Yes, I agree. I think that sometimes like I can tell you that I can give you a good product manager. I think Jeff is a good product manager. He gives good insight from the customer. He brings us good insight from the customer.

[00:37:03.86]  Jason ValleryYeah.

[00:37:04.59]   RemoteAlthough he was never a developer, okay? But you really understand what customer needs, what all the customer needs, and I think this is the added value. I don't need the product. like to do, it's fine to do brainstorming, but that value is not to have, like R&D sometimes is more disconnected than sales, and of course, product in between, right? Because they are doing more outbound. So it's fine to... to hear like brainstorming opinions from a product but if if you have like a real example of why customers need it and not just what they ask but what they care about and why they care about it then it gives a lot of perspective right and sometimes And not all of my engineers have it. We are trying to make R&D very outbound. So they will not be disconnected. But in general, products are talking much more with customers than typical-- And I think the challenge is how to bring the real insights from all the discussions.

[00:38:50.50]  Jason VallerySo a couple of thoughts on that, which initial reactions from conversations with Tomer and kind of looking at, you know, the work that's been in flight, what was shipped in 5.4 and so forth. what I see and it's very natural is that the organization historically has done planning based on deal pipeline which is customer A needs feature X and it's blocking Y revenue therefore it gets it into the release I think nothing it's

[00:39:19.33]   RemoteNot I think with three types of features, okay? We have, yeah, the tactical features for deals. It can be like huge deal or many small deals. We have innovation. Like I can tell you that a good part of my team did this. the data engine it's not what we are coming with a vision to customer it's not that customer ask us oh I need this feature okay but for instance if they need some special another extra authentication feature for SMB so this is the tactical features that we need to do And the third is to do technical depth, because sometimes you are delivering a feature, and it's like you took some compromise, so you want to improve it. Or you deliver something, and you learn something in the field, and you want to improve it. Or you feel that this area of the code, it's good to do a refactor. So I think there is a portion that's in technical depth, a portion which is tactical features, and the third is more strategic innovation. I think that Tomer was much more focused on collecting the content for the team, not just tactical features than the strategic, and the technical depth by nature is just R&D should know it's coming from R&D from support, right? The technical depth. So I think Turner brings less value with the technical depth and he was less involved in the most strategic initiatives, okay?

[00:41:25.27]  Jason Vallery- Well, I guess that's the final statement I wanted to make, which is, I think a couple of things are necessary. So even on the tactical stuff, you know, as the number of customers scales. the number of requests scale and the business matures, like you need to kind of bucket those into thematic versus looking at a very granular level. So there's like an up leveling to whatever you wanna call it an epic, you know, a bigger picture plan than it is today. I think that's a piece of how you do product planning. But then on the visionary stuff, like how do we get product engagement there like was there a product owner for insights engine that was driving it end-to-end for you or was that purely

[00:42:10.54]   RemoteDriven out of R&D it was it was a product owner which was architects and that It was both from the solution team as well as the architecture team that really consumed the technology very, very early and gave us inputs and improvements and stuff, as well partners. We did a lot of work inside engine work with NVIDIA for instance and with some selective customers like design partners. So it's not like developing in a bubble, and we did like also alpha and beta and, you know, to, to and so and we try to go out early. So we get, we get input when we still able to impact the delivery of the version. To be honest, I didn't try to optimize, like in what I call the tactical feature. I didn't want, I didn't try to optimize to perfection the order of doing things, because sometimes. invest too much time deciding what to do and then you don't have enough time to do it. So I'm okay, I'm okay to even, I'm okay to pick something sub-optimal and just do it, and then, like, so I was more optimizing for It's then predictability, but of course sometimes there are deals that you are committed to something so it's also predictability is important, but in general I don't need to optimize for predictability. I prefer to optimize for a throughput of my organization, okay? That's in general what I'm I'm trying to do, and it means that sometimes, in every version, you have features that you are trying to do, and it will arrive at the version after, just because I don't want to stop the version just because of one feature that is out. So not everything is like this encore, and you must deliver it in the version, but. some more commitment. So you put a little bit extra to not miss the commitment. But I don't want to do it for every feature because then I will do much less, right? If I just want to be predictable in what I'm doing, then I will take less risk and then I will do less.

[00:45:20.36]  Jason ValleryI mean, I think this is where a deep technical product manager can help. You know, they can look at this and take a number of different feature requests in an area coming from a customer and maybe abstract them up to a level where they can design a better solution that meets multiple customers' requirements and push that through versus you've got a bunch of just like grab bag items to go do. I mean, in the area and you know what you're trying to accomplish oh of course that's by the way we are

[00:45:50.65]   RemoteReal value we're trying to do it and i can tell you that our hp is very high so sometimes you just need to do it right like if you have a 200 million dollar deal you just do it right even if it's a We always try to do a thing without throwaway, that even if you are doing a little bit of shortcuts to bring it on time, then you can extend it, but sometimes it's too big to say no, right? So it's...

[00:46:25.85]  Jason ValleryI completely agree.

[00:46:26.80]   RemoteI mean, you don't want to block the business.

[00:46:27.85]  Jason ValleryI'm not advocating that. What you end up with, though, is two challenges. You've got, well, three challenges. One, you potentially have inefficient resource use, but even setting that aside, you've got a complicated product surface area as a result, and a bunch of technical debt that you might have to go back and look at later. So, you know, avoiding that where possible is the goal.

[00:46:53.37]   RemoteYeah, yeah, you normally want an architecture that is unlimited, then a design which is a little bit narrow and the implementation also even more narrow. But if you are doing it like this, you deliver something, but you can expand it well without rewriting. and refactoring everything, and you are aligned with your vision. Yeah, I need to go to my next meeting. I'm already one minute late.

[00:47:31.64]  Jason Vallery- I appreciate the time. I'm, you know, all in on helping you and making this successful. So I'm looking forward to working with you. working closely with you. I'll follow up on getting us a regular sync.

[00:47:42.49]   Remote- Thank you, bye bye and good that you are coming.

[00:47:47.22]  Jason Vallery- Thank you.

[00:47:48.06]   Remote- Bye. (silence) (clicking)
```

<!-- ai:transcript:end -->
