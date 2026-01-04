---
type: "People"
title: "1:1 with Tomer: Product management structure at VAST"
date: "2025-11-07"
entity: "Tomer Hagay"
folder: "People/Tomer Hagay"
participants: "Jason Vallery, Tomer Hagay"
tags:
  - "type/people"
  - "entity/Tomer Hagay"
source: "00 Inbox/Transcripts/20251107 1004 Parallels Transcription 1.txt"
---

# 1:1 with Tomer: Product management structure at VAST
**Date:** 2025-11-07 · **Person:** Tomer Hagay · **Folder:** People/Tomer Hagay

> [!summary] Executive Summary
Jason and Tomer aligned on the need to introduce clearer product management discipline (objectives/KRs, traceability from epics to tasks, and a defined rhythm of business). Tomer described current constraints: leadership skepticism toward formal PM (Jeff prioritizes revenue and flexibility; Renan resists PM ownership; Shahar prefers ambiguity that enables shifting priorities), fragmented cloud vs. core workflows, and poor visibility into delivery status, which hampers customer responses and accountability. Jason noted he’s getting limited traction so far with Jeff, who prefers Jason to wait before proposing changes, but agreed that any solution must be org-wide and top-down endorsed by Jeff and Sahar. They agreed to defer action until the Tel Aviv onsite next week, then skunkworks a concise proposal outlining PM scope, accountability gates, and cadences to present jointly to Jeff (and likely Sahar). Goal: move from reactive “passenger” mode to a consistent planning and reporting system without fragmenting cloud from core product.

## Relationship Context & Key Facts
- Current PM practice at VAST lacks OKR/KR rigor and end-to-end traceability from tasks to strategy.
- Engineering effort for cloud success largely depends on core product changes; PM process must cover the whole stack.
- Jeff is cautious about structural change; prefers Jason to learn the org before proposing.
- Renan is resistant to traditional PM authority; Shahar avoids strict structure and gating.
- Cloud (Yancey’s area) and core teams have misaligned processes and limited workflow overlap.
- Lack of structured tickets/epics impedes status checks, commitments, and customer responses (e.g., MD migrate release movement).
- Jason proposes defining PM scope, accountability gates, and a monthly rhythm of business (e.g., MBRs, loss reviews within cadence).
- They will meet in Tel Aviv next week to observe and align before drafting a proposal.

## Outcomes (What moved forward)
- Shared diagnosis that the org needs PM rigor and traceability.
- Agreement to partner on a skunkworks proposal after the Tel Aviv onsite.
- Consensus that any PM framework must be top-down endorsed by Jeff and Sahar and apply across cloud and core.
- Plan to present a concise, practical PM scope and cadence to Jeff jointly.

## Decisions (Agreements & rationale)
- Defer proposal drafting until after the Tel Aviv onsite next week.
- Do not implement PM structure only for cloud; changes must span the entire product.
- Pursue a skunkworks proposal to socialize with Jeff (and likely Sahar) first.

## Risks (Interpersonal or dependency)
- Leadership resistance to added structure may block adoption.
- Continued ambiguity enables shifting priorities and missed commitments.
- Cloud and core process misalignment undermines delivery and accountability.
- Perception risk if changes are pushed before sufficient context-building with leadership.
- Inability to answer field/customer questions quickly due to poor status visibility.

## Open Questions
- Who will be the executive sponsor for PM discipline—Jeff, Sahar, or both?
- What minimal pilot scope can demonstrate value without disrupting delivery?
- Which tools and taxonomy (OKRs, epics, features, tickets) will be standardized?
- What cadence and artifacts will define the rhythm of business (MBRs, dashboards, loss reviews)?
- How will cloud and core teams align workflows and accountability gates?
- When will the joint proposal be reviewed with Jeff and Sahar post–Tel Aviv?

---

## Action Items (You & Counterpart)
> Tasks are standard Obsidian Tasks checklist lines. If you use a global filter (e.g., `#task`), ensure it appears in each line.  
> Common metadata: `📅` due · `⏳` scheduled · `🛫` start · `🔁` recurrence · priority `🔺⏫🔼🔽⏬`.  
- [x] Draft an outline for a PM framework (scope, accountability gates, RoB, OKR/KR mapping) to socialize with Jeff/Sahar. @Jason Vallery ⏫ ✅ 2025-11-08
- [x] Compile concrete pain points and examples (e.g., epic/ticket gaps, release slippage like MD migrate) to inform the proposal. @Tomer Hagay 🔼 ✅ 2025-11-08
- [x] Map current cloud–core workflow interfaces and handoffs to ensure any PM process spans the full stack. @Jason Vallery 🔼 ✅ 2025-11-08
- [x] Schedule a joint review with Jeff (and invite Sahar) to discuss the proposal after Tel Aviv. @Jason Vallery ⏫ ✅ 2025-11-08

### Follow‑Ups & Check‑ins
- [x] Meet in person in Tel Aviv to observe processes and align on proposal approach. @Jason Vallery 🔼 📅 2025-11-10 ✅ 2025-11-08
- [x] Reconnect post–Tel Aviv to finalize proposal scope and presentation plan for leadership. @Tomer Hagay 🔼 ✅ 2025-11-08

### Next 1:1 / Touchpoint
- Next meeting (if scheduled): **2025-11-10**

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
[00:00:00.00]   RemoteAnd we'll see you next time. Okay, I'm with you.

[00:00:29.74]  Jason ValleryAwesome. How are you doing?

[00:00:32.87]   RemoteGood, good. How's your week been? Good.

[00:00:37.70]  Jason ValleryI unfortunately didn't get as much of Jeff one-on-one as I had hoped for. As you can imagine, he got pretty much fully booked up the time we were in San Francisco. So it was Uber from customer to customer to customer to event kind of thing. So we didn't really get a lot of strategic planning and figuring things out time. He actually booked out some time with me for this afternoon, here in a couple hours or an hour or two, to spend more time and actually kind of work through some of the key. topics and concerns so hopefully that'll be more productive. But it was good, you know, got to hear a lot more from customers directly which is obviously you know a key learning experience for me. You know, I still have a lot, as I've been meeting the rest of the team and kind of getting to know stakeholders across. Vast and you know like Andy's team, Rob's team, you know all kinds of different folks. It's really clear to me like product is ran very different here and in terms of what the PMs focus on and how they support the rest of Vast. Also still not entirely clear for me. how much of that I'm going to insert myself into, but I'd be curious about your take. What are some things that you're thinking about doing to assert a more traditional product management role for you and your team? Goal setting, one of the things we did at Microsoft It was a huge piece of the puzzle is OKR setting, tracking, and business reviews. So we would run a cyclical objective planning, objectives being durable over multiple years, typically, and a set of KRs that map to those objectives with things that are measurable that we would report out in a monthly rhythm of business, and then all of the work that the team did, like all of the epics, features, work items, like have hierarchical mapping, right? You should be able to say like, this dev task accrues to this feature, this feature accrues to this epic and user story, this epic and user story maps to this key result for the business, and this key result for the business. back to this overall product and strategy objective right and you should be able to have that lineage traceability through that entire hierarchy of things and you should sort that out on a monthly basis to your leadership team. Has anyone really started thinking about how to bring that kind of maturity and rigor to the way product is managed here?

[00:03:23.53]   RemoteYeah, so that's part of what I was sharing, you know, and when I started this role, that's the vision I had. Not exactly that, but really to have the structure and hierarchy of tasks and goals. you know, measurable outcomes and what have you. It's, you know, when you ask me of, like, how do I see the future of the PM, you know, my PM team or the PM team, it's kind of, on my side, kind of... evolving to this, I don't think, I don't think that, I mean, I'm not there. I'm not trying to push for this. I'm not, I don't think the organization is capable of working in that mode, and it doesn't matter how much and what I do, or how I do whatever, right? It has to, either if, you know, if things will, will start, you know, starting from Rennan, it should become a priority, then, then it will happen, but it won't, right? I mean, it, in Rennan, it's, it's pretty allergic to product management, and he often forbids, I'm telling you plainly, right? I mean, you can validate. Please don't share that I said that because it's coming, you know, people tell me, right? But he prohibits salespeople from saying, you know, I'll prioritize with our product management, right? He doesn't want people to, he said, we don't need product management. You know, customers are our product management, right? I mean, the whole approach in ADVAST is that what you described is not, it's not something we're doing, and, To me, I mean we can call this function whatever we want, if we don't want to call it product management, call it something else or whatever, but the methodology that you describe, I think must happen here, right, because it's already chaotic, it will become more chaotic, right. For me to even just, I mean, just a basic answer to a field. you know, SE of, you know, about a feature or, or, you know, something that's being developed or something to understand exactly where the status is, how many, how many components of a feature are developed, how many are left, right, like in an EPIC and in tickets, right? I can't do that, right? It's all, it's all manual. work, right, me reaching out to the right engineer, having the right conversation, and whatever, and then get the data and influence if I need to insert data, right? There's no structure, right? So that structure that you described must happen. I'm not the person that is capable of pushing the organization to this.

[00:06:45.19]  Jason ValleryDirection. It needs top-down alignment. That's no ding on you. To make this happen, it has to be something that comes from, if not Ren and Jeff and Sahar, they have to be the ones that are pushing this out to their teams and managing it. It's a two-in-a-box problem. You need the engineering team aligned, and you need the product strategy folks aligned. have that from a hierarchy in the org chart. You can't implement a hierarchy of product strategy with that. So, I completely agree. This isn't on you to solve without...

[00:07:19.75]   RemoteOh, I know. Yeah. Sorry to cut you off. I wasn't thinking that way. I'm saying this is not really, it's not something that I... I kind of, you know, spend my day thinking how to structure or whatever, right? So when you ask me or like, how do I plan or whatever, I don't, I actually don't plan those kind of things, right? It's not, it's not, you know, it's not something, it's like, you know, I think we do some aspects of product management here, but it's not, it's not typical product management and that's to. For me, for the foreseeable future, that's how I'm still going to operate. That's why I mentioned that, I mean, for you starting, especially coming in senior, covering an area that is growing, there's a serious investment in, I mean, this is a place where you can definitely push for this type of structure.

[00:08:19.93]  Jason ValleryIt doesn't make sense for us to do it in the cloud side of things and not in the entire product stack, right? Because if you think about what we're doing on the cloud, really Yancey's piece of this is fairly small, at least from an engineering lens. Like the work that's going into the control plane and the marketplace, super- - Don't discount it, it's super critical work. But like from an engineering cycles perspective, most of the work that we need to go do are actually in the core product itself. It doesn't make sense for me to try to run a product management structure and traditional approach just for what Yancey's doing. Like we would have to come to some way, and this is actually one of the key pieces of feedback from other senior folks in the company I won't name names just in the interest of anonymity. But, you know, obviously I'm talking to Yancey and Elone and Sahar and others, right, and getting to know them, and, you know, one of the things that I've heard, and actually literally both from Yancey's side of the fence and from Sahar's side of the fence, not them necessarily specifically, like those two teams aren't working together at all. Like they're working together. but from a process, relief management, you know, leaving the workflows, like there's no overlap today, and so, you know, I would say, like, in a real world, we would be getting buy-in from Jeff together and from Sahar together to say, "We want to revamp this." product management at best and get buy-in on like here's the way we want to structure uh how we would what what our role is being very specific in scope to say this is what product management is and this is what it's not at best and then from that turning that into what I describe as the rhythm of business like what are the accountability gates. and what do we deliver at each one of those accountability gates that's ultimately planning that is you know what Jeff tags me on random shit he's like hey go do a loss review for BCDR customers like what the fuck Jeff that first of all has nothing to do with the cloud but even if it did like that's not I mean that could be a product management function and I would certainly say when you're looking at it from the lens of you know features and backlog and prioritization you do those loss reviews but you would tie that into what is an established rhythm of business. You would be hosting monthly you know product MBRs and you would use those forums to do it. So I guess I'm off on a bit of a tangent but what I would like to say. No no no. We have to go build. I'm glad I'm happy that you're saying.

[00:10:52.75]   RemoteAll this because yeah, go ahead, go ahead.

[00:10:54.86]  Jason ValleryI mean, so obviously we have to work together. We have to go convince Jeff and Sahar that we want to do this and it's the right thing to vast, or we just continue sitting in a role where we're the passengers on a journey and we're just reactive in our nature, and that's not product management to me, certainly that isn't the role I signed up for. Maybe it's the role I'm going to end up being in. because we can't get the institutional momentum, but I think it's on us to go and sell a vision of how product management can influence Vast's roadmap.

[00:11:23.44]   Remote- Yeah. So I'll tell you what I'll play, what I've been experiencing and like I'm on board, I'm on board with everything we're saying it's just I'm I hate to say it but I'm I'm I admitted that I lost that battle and I'm you know and if you want to if if you think we can get or if with your work with Jeff and and the fact that I mean again you join your senior you've seen things you know how things should work whatever it's like you You speak with conviction on those kind of things, and you get the buy-in because of the credibility you bring, and we can drive this together. I'm on board. We'll be happy to partner, divide, conquer, or whatever. Divide the tasks that we need. I mean, it's a lot of work, right? as you now know how we operate to get to how we need to operate, right, it's just a lot needs to happen, and putting the system in place, I'm happy to work with you. That's what I signed up to do, and I'm exactly, you know, I was exactly in your spot of like, you know, coming in and saying, that's not what I signed up to do. So, either I'm, I'm to keep fighting this, have a miserable life at best, and I mean that was my experience, I'm not saying it's yours, right? Maybe I didn't come with the same conviction as you're joining, right? Or the same experience, or seniority level, or whatever. But anyway, for me, the options were I either conform with the situation, see what I can do, or work in a I add value, try to align with what Jeff's priorities are and move along or try to fight the fight that I thought I'm going to lose anyway and that's why I ended up here and that's what product management ended up being here, which I agree, it's not really product management and we are passengers in many areas. We're sometimes drivers, not very often, and I definitely understand, and this is-- like I said multiple times, Jason, I speak very openly with you on this and between us and all that, right? the another issue is that jeff is is for him product management is more of of uh it's kind of another channel to to to to drive revenue and sell stuff and he doesn't really what's that yeah no i agree it's just technology yeah so I mean, he really doesn't care about the mechanics, right? And I care a lot about the mechanics. I think that I can't, even if I want to sell, you know, be the selling PM, which I am, right? I'm trying, you know, to like always talk about value and, you know, finding solutions that are, just checking boxes and things like that, right? Still, without having the right way of organizing things, similar, the same as you described or similar, my job is very, very difficult. I can't answer the customer's question with certainty. I can't, definitely cannot do it. quickly. I can't drive changes or kind of small modifications to features that are ongoing or anything in an easy way. I mean, there's no way of doing that, and you and I know that it could work differently. In the past, I have, you know, I had the other experience, right? I had a team of engineers in India that waited for me to wake up in the morning because they got stuck and they what to do and I need to because something wasn't really defined in the way that and I was the one defining those those details right so here is you know and everything was structured and whatever but at least when I looked at the ticket if someone if a customer asked me you know I don't know will will this feature end up having this detail in it I could go to the epic and look at the tickets and see exactly what happens and and follow up if needed and how needed right and today it's just impossible right I spent so many cycles not just me everyone else spent so many cycles trying to chase things so anyway a long story short right I'm saying even But even if we want to, I mean, I think I don't think Jeff sees it, but even if we want to align with Jeff's priorities, we need the structure to do that. It's just Jeff doesn't value those, and, anyway.

[00:16:25.85]  Jason ValleryYeah, I mean I've learned. I've been talking a lot here but I'm learning Jeff. obviously he's an interesting guy. I appreciate his frankness. I detect, and you know, we'll keep this between us because he's our shared boss and we gotta manage up, you know, I detect his bipolarism, maybe a little bit of that, like sometimes he's all in on one thing and then

[00:16:49.15]   Remotehe's not. - He's in bipolarism, yeah.

[00:16:50.97]  Jason Vallery- Kind of all over the place a bit. it. Um, and you know, that's the kind of person who probably is going to struggle to prioritize structure and discipline. Um, because as soon as the structure gets in the way of what his top of mind priority is, it's hard for you to let go of that in acknowledgement of this isn't the way we do it around here, and so I think the challenge for both of us is to manage up here and sell this vision to Jeff. Um, I'm trying to sell this vision to Jeff and I'll be honest with you between us, it, it isn't going well, um, I'm going to, you know, you know, his, his immediate response to me is like, don't have opinions until you've been here three months and know how things work around here.

[00:17:35.60]   RemoteI'm like, yeah. Yeah.

[00:17:37.93]  Jason ValleryThree weeks and I've talked to everybody and I can detect a little bit of like we're very undisciplined as an organization and so he's he's very he's very hesitant to give me any latitude until he thinks I fully understood how things work around here. I don't know that I need to be here three months to have the conversation you and I just had and I appreciate you kind of helping me

[00:18:00.43]   RemoteYeah, no, I mean, like I said many times, I want you to be successful, I think your success is my success even, even in like in multiple ways, right? If you're successful in changing things, then I can take a long help you, we both benefit. If you change something that that shows that I'm not part of, but it will show that that this is, you know, the right path. I will benefit from it longer term as well, right? Either way, your success is my success, and regardless, we need a good cloud program, right? I mean, it's, you know, that's on top of things. But, so you mentioned this thing about Jeff, about his interest. or kind of what's in it for him for doing that right it will just restrict him in the future right i mean if you look at it simply i mean kind of rephrasing but i think shahar is also the same right and that's why those things so so again my experience was chef doesn't care or doesn't want because he wants to wake up one day and think of something and try to to drive it or whatever uh renan is allergic to you know he's an engineer and he will debate that you know why would product management need to tell engineering what to do because the engineers are smart enough to decide right we have architect we have this and whatever like why do we need to have more people to have philosophical conversations and argue about stuff where you have opinionated engineers that can do their own research, they can speak with customers, they can figure whatever, that's where Ryan is coming from. He's not just me, you know, hating product management. He doesn't think it's a super important function where you have smart people in other places. So that's the other angle, and Shahar, and the reason why I called you after the... phase gate is because this is this is a typical experience why Shachar likes keeping things vague and not structured with epics and and features and tickets and all that is because he can he can juggle you know more balls in the air and the example I gave you with this MD migrate feature moving from you know the whole release release slip right, and then the feature moved from, you know, 5.4 to minor releases after, and then it's covered most of 5.5, because then he's saying, well, it's too big for a minor release. That's why, I mean, that was his explanation of why we're moving it to 5.5, because it's too big for a minor release. But it wasn't a major release. wasn't 5-4. So now, you know, you moved it to 5-4-1, 5-4-2 without asking anyone, and now you're saying, oh, no, no, I can't have it there. Because anyway, that's how he rolls, right? So he has zero interest in changing this because it will restrict, he will need to give more explanations on why he thinks. and why you know we can't do what he promised to do or whatever we'll hold him accountable we'll have customers that hold us accountable right now that accountability I'm trying to to have it shared right so if if I make a commitment I make sure that it's a joint commitment with Shachar right and and Because if not, then I'll be in trouble. You know, I can't make the commitment and agree with Shafar about something without like the account teams in the loop or something, right? Because his commitment to me is more tangible than, it's more flexible. than his commitment to account teams and customers. So, anyway.

[00:21:52.78]  Jason Vallery- It's a tricky problem.

[00:21:53.62]   Remote- Giving you the complete picture because I think it's important to know reality before attempting something. So anyway, I'm just in with this triangle of like, you know, people. that will be against what we're proposing, and I was proposing something similar and failed, right?

[00:22:17.77]  Jason Vallery- Maybe what we should do is, Skunk works this a little bit with Jeff, and maybe you and I could work on a little bit of a proposal on how we would want things together, and then kind of present it together to Jeff and see if we can. and get him bought in together. Let me think about that a little bit. My time is super booked up over the next couple of weeks. I don't know how much time I can focus on this, but yeah, I'll be, I'm going to the next week. I don't know if, are you participating?

[00:22:45.67]   Remote- Yeah, me too, I'll be there. Oh, great, we'll see you in person.

[00:22:48.55]  Jason Vallery- Yeah, I arrive Monday, midday, and then I have to leave on Wednesday.

[00:22:53.79]   Remote- Yeah, right, Monday night.

[00:22:54.55]  Jason Vallery- Okay, I'm gonna be there Monday, Tuesday, Wednesday. I won't be there Thursday. I have to change my flights around, but yeah, I'll be good. Okay.

[00:23:01.60]   Remote- Yeah, yeah, so I think that maybe whatever next step is, let's do it after Tel Aviv, right? You'll experience, you'll have the live experience there. get to know people, get to know shopper or whatever I think I think it would be

[00:23:19.13]  Jason ValleryBetter for even even for skunkworks or like initial yeah I agree okay well I'm

[00:23:28.53]   RemoteExcited I'm glad that you're excited I'm trying to share everything I can but without discouraging you without being like, "Hey, I tried that, it failed, don't do it." I'm sharing what I tried and failed in order for us to maybe try something else and be successful or do things differently and be successful, not because I'm trying to say, "Hey, lost cause." right? That's not the thing. I'm still here. I don't think it's a lost cause. I think I'm a believer.

[00:24:06.86]  Jason ValleryIt's exciting times for the company regardless of the culture or institutional challenge, but it's hard to deny that Vast is on a rocket ship. Like that whole meme inside the company, while it's kind of a little bit cheesy, it's also very true. The CoreWeave deal, the opportunity with Microsoft, the opportunity... up doing with Google, like, oh my gosh, this company is going to make a shit ton of money in the near future, and that's a fun ride to be on, even if you've got challenges on execution. So, I think it's a great time. Okay, I got to bounce to another meeting. I will see you on Monday.

[00:24:38.93]   Remote- Sounds good, yeah, see you Monday, looking forward.

[00:24:42.61]  Jason Vallery- Thanks, Tomer, bye.

[00:24:43.69]   Remote- Have a great weekend, bye.AUDIO


