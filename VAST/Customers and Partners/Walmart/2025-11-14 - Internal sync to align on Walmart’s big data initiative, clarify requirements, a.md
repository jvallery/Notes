---
type: "Customer"
title: "Walmart big data DR requirements and next steps sync"
date: "2025-11-14"
account: "Walmart"
folder: "Customers/Walmart"
participants: "Jason Vallery, Mikey, Brad, Paul"
tags:
  - "type/customer"
  - "account/Walmart"
source: "00 Inbox/Transcripts/20251114 1302 Parallels Transcription.txt"
---

# Walmart big data DR requirements and next steps sync
**Date:** 2025-11-14 · **Customer:** Walmart · **Folder:** Customers/Walmart

> [!summary] Executive Summary
Internal sync to align on Walmart’s big data initiative, clarify requirements, and plan near-term customer engagement. Jason emphasized that an architecture/whiteboarding session is gated on receiving definitive requirements from Walmart, especially around disaster recovery: do they need cloud access to a full VAST namespace or just a copy of data. Current VM-based approaches in public clouds won’t meet the anticipated scale, and the team is driving a hybrid roadmap, including deeper, more native integration with Google Cloud Storage. Jason will meet engineering in Tel Aviv the week after next to shape this roadmap, with Walmart as a marquee design partner. Walmart has a tight timeline (about 1–1.5 months) to select between a minimum configuration and a larger phase-one proposal (main difference: D-boxes/capacity). The opportunity could reach ~500 PB and is framed as a potential $300M deal if successful. The team will hold a 30-minute expectations/vision call with Mingming today after 2 pm PT; Jason will lead, with Brad and Paul joining, and Mikey scheduling and sharing Walmart’s answers beforehand.

## Stakeholders & Roles
Jason Vallery, Mikey, Brad, Paul

## Key Facts (Context, constraints, signals)
- Architecture session is gated on clarified requirements from Walmart.
- DR requirement ambiguity: full VAST namespace in cloud vs data copy.
- Current cloud VM approach is not viable at the anticipated scale.
- Hybrid roadmap in motion; goal is more native GCS integration.
- Jason meeting engineering in Tel Aviv the week after next to define roadmap.
- Two proposals shared: minimum config vs larger phase-one (primarily D-box/capacity difference).
- Walmart aims to decide within ~1–1.5 months.
- Potential scale discussed up to ~500 PB; deal framed as up to $300M.
- 30-minute call with Mingming scheduled for today after 2 pm PT.

## Outcomes (Stage movement, agreements)
- Agreed to hold off on technical answers until Mingming call sets expectations.
- Scheduled a 30-minute customer call today after 2 pm PT to align on vision and roadmap.
- Committed to use Walmart’s needs to inform hybrid big data roadmap priorities.
- Mikey to circulate Walmart’s answers in Slack prior to the call.

## Decisions (What we/they decided)
- Do not schedule an architecture/whiteboarding session until requirements are clarified.
- Lead with current capabilities plus forward roadmap narrative in today’s call.
- Consider escalating to deeper technical session with additional SMEs after requirement confirmation.

## Risks (Budget, timeline, legal/security, competitive)
- Incomplete requirements could delay architecture and stall momentum.
- Cloud scale limits for VM-based deployments may block near-term DR patterns.
- Customer timeline pressure (1–1.5 months) may compress evaluation and testing.
- Availability constraints next week (supercomputing conference) may hinder scheduling.
- Dependency on engineering roadmap delivery for native cloud integrations.

## Open Questions (clarifications, info requests)
- Is Walmart’s DR need full namespace access in cloud or only a data copy?
- What exact capacity, performance, and access patterns must be supported?
- Which configuration will Walmart select (minimum vs larger phase-one)?
- What testing milestones and acceptance criteria does Walmart require?
- Are there specific security/compliance constraints for hybrid data flows?
- When should the architecture whiteboarding session be scheduled post-clarification?

---

## Action Items (Ownered & time‑bound)
> Use `📅 YYYY-MM-DD` for due dates; optionally add `⏳`/`🛫` and `🔁` where relevant.  
- [ ] Schedule and send invite for 30-minute call with Mingming after 2 pm PT today. @Mikey 📅 2025-11-14 ⏫
- [ ] Share Walmart’s requirement answers in Slack before the Mingming call. @Mikey 📅 2025-11-14 ⏫
- [ ] Lead the customer call and position current capabilities and hybrid roadmap. @Jason Vallery 📅 2025-11-14 🔼
- [ ] Attend the Mingming call and support with context and Q&A. @Brad 📅 2025-11-14 🔼
- [ ] Attend the Mingming call and support with context and Q&A. @Paul 📅 2025-11-14 🔼
- [ ] Notify Alon about the 2 pm PT discussion and share context in case he can join. @Jason Vallery 📅 2025-11-14 🔽
- [ ] Coordinate Tel Aviv engineering sessions to define native GCS integration requirements. @Jason Vallery 🔼

### Follow‑Ups (Customer / Us / Partner)
- [ ] Based on clarified requirements, schedule architecture/whiteboarding session with appropriate SMEs. @Jason Vallery ⏫
- [ ] Reconfirm Walmart timeline and decision process for config selection (minimum vs phase-one). @Mikey 🔼

### Next Meeting
- Next meeting (if scheduled): **2025-11-14**

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
[00:00:00.00]   RemoteIt's just the four of us, because then I could get on the call based on scheduling. So Jason, I just wanted to get a call set up. I know you and I have been going back and forth on this slide all week, trying to make something happen. Unfortunately, there was some miscommunication with the loan and trying to get them out there today to Walmart.

[00:00:35.50]  Jason ValleryYeah, well, even sending that aside, like, I don't think we have a comprehensive understanding of the requirements, and so it's kind of a premature thing to get the architecture session going until we. we actually know what we're architecting against, and so I do think getting those questions answered is a gate to a scheduling, like a whiteboarding session.

[00:00:55.55]   Remote- And that's completely fair, and so as far as from a timeline perspective go, it is what it is. I have been going back and forth with Ming Ming and she's going to get me. some of those questions as well as many of those questions answered over the next hour or so so once I get that all this you share it back via the slack I know we can review and discuss it but another another thing that came up as far as like a requirement and what they're asking that message that I sent them the slack channel i wasn't sure if you would be able to answer that or if it would be somebody like um leor or ndp to kind of help respond to the customer because they've they've pinged both all of myself twice now for the last 24 hours and i want to make sure that we get them something even if it's like we got to come back to you or they're like for a yes or no okay i see this is in the the win walmart thread this is the um the walmart big data oh let me go find the question yeah there it is big data

[00:02:15.03]  Jason ValleryWell, I mean, I think this is honestly part of the architecture design. This is a problem that you can solve in a variety of ways, and so how we approach it will kind of be dependent upon the solution we end up designing more comprehensively. But you know, a DR plan for this is like, is the DR plan they want to be able to store to a full vast need space in the cloud, or as the DR plan, you just need a copy of the data. So understanding that as a part of it, like, you know, if they've got several hundred megabytes, it's not going to be something we've currently got the ability to support in Google Cloud today. Like that, that scale running on VMs just doesn't make sense. You know, I mean, just to uplevel this a little bit and give you a little more context on why I'm so deeply engaged to follow this one through is right now we're pushing a lot of work to support hybrid scenarios in the cloud, and so the announcements we made last week around Google and the announcements we will soon make around Azure and AWS are a little bit of a checkbox exercise, if we're honest because what you've got is the ability to run. fast on virtual machines and they're storage optimized virtual machines, but you know you're not going to be able to run Ketamine. They're really great for bursts to cloud, expose the namespace to the cloud, but in Google's case it's a little more than that. They're really looking at data like that's in the cloud and bring it on-prem, and what that ultimately means is that we are able to directly integrate with Google Cloud Storage in more of a native way, and that's not something we can do today, and so we have to drive all of those requirements. We're really working right now, and I'm going to be in Tel Aviv the week, not next week, but the week after meeting with the engineering folks around what that roadmap looks like, kind of really starting to specify exactly the shape of what we want them to build. using Walmart here as a key customer that wants this and would leverage it immediately is why I'm deeply engaged in wanting to drive this forward and get some, some, some traction with it. So ultimately like we can answer Ming Ming's questions that you've got in the chat with sort of like the tap dance version answer, or we can say we want to build the right end end solution and that's our map that we'd like to kind of code, specify, code, develop, code, define with you, and I think that's

[00:04:37.06]   RemoteKind of where we're at on this. Okay. Okay. I think that that's fair. I mean, I expect us to get the responses to the questions that you have asked, and a lot of this does coincide with it as So, it should give us a better picture as to what they're actually looking for. I'll hold off on answering these specific questions. Paul, I'll take your feedback too on how you think.

[00:05:06.80]  Jason ValleryMaybe we just do want to have effectively the conversation I just said with you directly with Walmart and talk a little bit about what we've got today. what the vision strategy looks like and how we'd like to have evolved that with Walmart as a marquee customer for us in doing these kind of hybrid cloud big data projects. I think, you know, bringing that narrative to Mingming will give her more assurances than just a tap-dance answer and I'd love to, you know, bring that conversation to her if you want to just, we can have a 30-minute conversation. minute chat with her and talk about it, however you want to approach that.

[00:05:42.32]   RemoteYeah, and that's pretty much what I was trying to get us to do this week, just to get on a call with her. If the questions that you asked were really good questions, they make a difference, and I can always get a meeting scheduled with Ming Ming and some of the folks that are part of that big data project.

[00:06:00.12]  Jason Vallery- Yeah, we want to, you know, if it was just, you know, me and you and Mingming this afternoon or something, I'd be fine with jumping on a Zoom with her. Next week, supercomputing, so it's a little more difficult, but I honestly prefer, but I can make time.

[00:06:12.72]   Remote- Yeah, Mike, Mikey, could you get her on a call today? - She has an appointment at 1 p.m. your time, so that's 3 p.m. my time. Uh, let me see, depending on when she gets out of her appointment. Is it an internal meeting or is it like a personal appointment? No, she has a personal appointment, she has a dental appointment. Okay. Alright, well it can't last that long. Depends on when she's getting done. Yeah. Let me, I'm sending a text right now, she's been in response all morning, so.

[00:07:30.15]  Jason ValleryAnd you can just ping me if you get a time block. Otherwise, find a slot next week. It is just, it's just super confusing. It's a little more difficult and I'd be like bouncing between meetings. So I'll have more focus time today.

[00:07:43.11]   Remote- Yeah. - Yeah, she's actually responding now. So whatever she says will kind of go based off. She's responding back to me right now. Oh good Yeah, so I'll see what she says Yes after 2 p.m She can make a call after 2 p.m. Today, which is 4 p.m. Your time Brad you might jump in into that one for me because I'll be with cross right therefore at 4 p.m. My time Yeah, no, no, no problem. Okay. Paul, can you make that as well? I'll be there. All right. So let me send something real quick to her, you guys.AUDIO

[00:08:46.48]  Jason ValleryOkay, so I'll just expect an invite for 2Pacific? Correct.

[00:08:53.42]   RemoteOkay, sounds good. Do we need any chats?

[00:08:54.46]  Jason ValleryI'm setting that right now. Okay. Any other topics you wanted to discuss?

[00:08:56.45]   RemoteBrad, is there anything I'm missing?

[00:08:57.10]  Jason ValleryPaul, anything I missed? No. Okay.

[00:08:58.74]   RemoteGreat. Thank you. All right. Thank you. I think I'm good on my side. Yeah, so no other deliverables Mikey that you're concerned with us delaying on right now. You think we'll get this word away today to I guess Jason. I don't know how much we talked about it last time when we first got the the other day, but obviously there's a big push from a Walmart perspective to get those things tested, right? They have a pretty timeline, and last Friday I actually shared a proposal with them on what they actually were, what they asked for, which was a minimum configuration, but based on some performance metrics, and then what VAST was proposing, which I phrased it as more so of as a phase one into this big data project. So with the minimum configuration, fundamentally, the only difference between the two is the D-boxes, right? Capacity-wise, one is smaller, the other one's a lot bigger, but the one that's a lot bigger is what we actually created, the larger proposal, which would allow them to expand and fully roll out this thing based on that specific timeline. So just from a timing perspective, on a rollout, meeting expectations, et cetera, the bigger one makes more sense, and our engineers can explain that better from a technical perspective than I can, but I gave them both those options. They're reviewing those. So Mingming may or may not bring that up. She did say that she was gonna spend some time this week to review it, but... That's kind of what it is at a high level. They're trying to do something within the next, I would say probably in the next month or so, a month and a half to pull the trigger on either one of those configurations.

[00:10:40.99]  Jason ValleryYeah, and I mean, it is really, this is a tire kicking size and scoping of that thing that, that, you know, that ultimately translates into a much, much larger deployment. I would imagine if we're successful with. proposing from an engineering roadmap and we can align on how to go do this, you know, even your questions, what I'm hearing is they really want to repatriate that entire data. Like this could turn into a 500 petabyte opportunity, maybe even more if we're successful. So, I mean, the sizing makes sense for them to get access to the APIs, get access to be able to do some like validation of the platform, and yeah, hopefully they can move forward with that. So yeah, I think it's goodness.

[00:11:20.11]   Remote- Good, I just want to make sure you had all the details.

[00:11:24.43]  Jason Vallery- Cool.

[00:11:25.27]   Remote- And you kind of been in on this with us, so we appreciate it.

[00:11:27.59]  Jason Vallery- And I'm the new guy. I got to know what I don't know around here. So make sure you bring me in and educate me because I'm learning from the fire hose right now. So it's great.

[00:11:36.11]   Remote- Yeah. - Jason, anybody you want us to try to get on that call for assistance?

[00:11:43.33]  Jason Vallery- I don't, for just chatting with Mamie and setting expectations, I'm perfectly happy to take that. I think when we get to the architecture section where we wanna have like the deep technical conversation around how we start putting all the puzzle pieces together, certainly I'll bring a loan to that, and he's on board, right? 'Cause you know, he's helping me with building out the. right strategy and direction that we're trying to go build. Obviously, his time is precious though, and there's a lot going on. So I don't think we need that alignment level setting with me.

[00:12:08.71]   RemoteOkay. All right. Well, just remember that the end goal here is a $300 million deal. So I know that a loan does like $300 million deals. So if we, if you feel that's and then we bring him in, then, yeah.

[00:12:25.07]  Jason Vallery- I'll let him know we're chatting.

[00:12:25.92]   Remote- It doesn't hurt to, yeah, let him know we're chatting at two and see if he wants to join and give him a little bit of context around it, and he may, might, he's probably on a plane back to the East Coast, but it's at least worth alerting him of what's going on if he is available to join.

[00:12:42.95]  Jason Vallery- Yeah, he's home now, actually, was just chatting. Oh, okay. Okay. Yeah. Okay. Okay. Okay.

[00:12:55.78]   RemoteAll right. Okay. We'll talk to you in an hour and a half. Sounds good. Okay. See you guys. but answers in 10 minutes. So you'll have that to read before the call. It'll be helpful.

[00:13:12.36]  Jason Vallery- Awesome.

[00:13:13.32]   RemoteThanks guys. Appreciate it. Bye. - Take care guys. (keyboard clacking) (keyboard clacking) (upbeat music)











