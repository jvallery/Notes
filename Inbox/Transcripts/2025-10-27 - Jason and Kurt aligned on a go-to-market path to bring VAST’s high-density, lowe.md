---
entities:
  people:
  - '[[Kurt Niebuhr]]'
type: transcript
source_type: unknown
date: '2025-10-27'
---

# 1:1 — Kurt Niebuhr — 2025-10-27

> [!info] Purpose
> Build trust, surface and remove blockers, align on priorities, coach & grow.

## Summary

Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lower-power storage into Azure deals. Kurt outlined his team’s remit (deal scoring for constrained GPUs, large-deal pre-sales, and Azure Core feedback) and a proposal to GA Azure Extended Zones (network-only) and AKS NodeJoin to connect sovereign/neo-cloud training sites to Azure for global inference. Jason shared VAST’s density/power advantages and the limits of the current Marketplace VM-based offer. They agreed the initial path is via Microsoft BizDev (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and route to Ronnie Booker for hardware design decisions, with MAI/Mustafa as key advocates given power constraints.

## Key facts learned

- Kurt is global pre-sales lead for AI Infra under Zia; team scores constrained GPU allocations, supports mega-deals, and runs Azure Core feedback.
- Deal triage now scores stickiness, workload type, and platform pull-through; all constrained GPU allocations require Kurt’s team approval.
- Proposal: GA Azure Extended Zones (network-only) and AKS Stretch/NodeJoin (ACAS FlexNode) to link neo-cloud training to Azure inference.
- VAST vs Blob (per 1 EB): ~1/10 racks, ~1/5 megawatts, >=5x performance, but ~2x capex.
- Azure Marketplace VAST offer (on L-series VMs) is a checkbox, not density/perf competitive for real workloads.
- Apollo: Chi owns bare-metal control plane; Sky/Overlake owns security; Ronnie Booker’s team owns chassis/layout/storage placement.
- BizDev contacts: Joe Vane (reports to Harish); path via BizDev and John Tinter to reach Ronnie.
- MAI/Falcon issues: Azure lacks topology-aware scheduling; IB/telemetry improving but rack-level placement not until ~Feb.
- OpenAI shift: Uday (ex-XAI) now runs infra at OpenAI; possible reduced Microsoft alignment; power is a major constraint for Azure.
- Kurt expects A2N approval for Extended Zones/NodeJoin in ~3 weeks; target partners include sovereign/neo-clouds (e.g., sakura.net in Japan).

## Outcomes

- Agreed Azure is the priority hyperscaler for VAST near-term.
- Aligned on pursuing BizDev (Joe Vane/Harish) to secure exec sponsorship (John Tinter) and route to Ronnie’s org.
- Plan to pitch MAI/Mustafa on VAST’s density/power to free megawatts and GPUs (Falcon, UK Met).
- Kurt to continue driving A2N approval for Extended Zones/NodeJoin; Jason to prepare power-to-GPU savings materials.
- Plan to reconnect at Supercomputing for deeper coordination and intros.

## Decisions

- Pursue BizDev-led path (Joe Vane/Harish) to engage Ronnie’s org rather than Nidhi/Manish.
- Treat the Marketplace VM offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.

## Action items (for Kurt Niebuhr)

- [x] Educate Microsoft BizDev (density/power, single-namespace story) and secure intros to Ronnie via John Tinter. @Jason Vallery ⏫ ✅ 2025-10-27
- [x] Create a one-pager converting VAST EB power savings into additional GPUs per site; share with MAI (Mustafa), Kushal, and Vipin. @Jason Vallery ⏫ ✅ 2025-10-27
- [x] Push MAI and UK Met to pilot VAST OEM/ODM racks (Falcon, UK Met) using the power-density angle. @Jason Vallery ⏫ ✅ 2025-10-27
- [x] Follow up with Kanchan on storage plays/density for Supercomputing (FAST) and schedule discussion. @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Coordinate with Kishore Enamapuri on Azure Extended Zones once A2N is approved; align on storage needs. @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Drive A2N approval for Extended Zones GA and AKS NodeJoin (ACAS FlexNode); confirm timeline and scope. @Kurt Niebuhr ⏫ ✅ 2025-10-27
- [x] Share Extended Zone PM contact details with Jason when available. @Kurt Niebuhr 🔽 ✅ 2025-10-27
- [x] Keep Jason updated on neo-cloud partnership pipeline (e.g., sakura.net) and where VAST can plug in. @Kurt Niebuhr 🔼 ✅ 2025-10-27

## Follow-ups

- [x] Confirm with Yancey and Lior their awareness of VAST density/power benefits and enlist them to advocate with Mustafa. @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Assess complementing the Marketplace L-series offer with higher-density storage SKUs or an OEM hardware path. @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Quantify capex vs power tradeoffs to justify 2x capex for decision-makers (e.g., Amy Hood, BizDev). @Jason Vallery 🔼 ✅ 2025-10-27
- [x] Validate whether InScale and similar deals follow the ‘train on neo-cloud, infer on Azure’ model. @Kurt Niebuhr 🔽 ✅ 2025-10-27
- [x] Plan Supercomputing touchpoint and intros (e.g., AMD event) and align joint targets. @Jason Vallery 🔽 ✅ 2025-10-27

## Risks

- Azure power constraints limit GPU expansion; storage inefficiency worsens the bottleneck.
- Marketplace VM-based offer may see low adoption due to poor density/cost-per-PB.
- OpenAI leadership changes (Uday) may reduce Microsoft’s influence and shift infra choices.
- Azure’s current lack of topology-aware scheduling hinders reliable large-scale training/inference.
- Internal org churn and layoffs create execution risk and slow cross-team alignment.
- A2N approval delays could stall Extended Zone/NodeJoin GA and partnership execution.

## Open questions

- Who is the current Azure Extended Zone PM to engage?
- Will A2N approval land within the proposed ~3-week timeline?
- Can Azure accept VAST OEM/ODM storage-dense racks for Falcon and UK Met deployments?
- Will MAI/Mustafa sponsor VAST deployment to unlock power-density gains?
- How many GPUs per exabyte can be freed by switching to VAST in common Azure configurations?
- How will Apollo ownership boundaries (Chi control plane, Overlake/Sky security) impact third-party storage integration?
- What scope is Kanchan covering for storage plays relevant to Supercomputing?

> Next meeting (if any): (none)

---

<!-- ai:transcript:start -->

## Transcript (auto)

```text
[00:00:00.05]   RemoteOh no, so now your video's not working so well. I know what you look like.

[00:00:04.58]  Jason ValleryWell, I can fix that too.

[00:00:06.71]   RemoteThis is the problem.

[00:00:09.96]  Jason ValleryI'm running everything in a VM because I'm still waiting for my work laptop.

[00:00:15.25]   RemoteAh, that'll make it-- I'll make it happen.

[00:00:17.91]  Jason ValleryIt does make a difference.

[00:00:20.03]   RemoteI don't know why that's not connecting. Stupid video now, well maybe we do this without video, I don't know. I was just on a video call a few minutes ago and it was working fine. What is going on with no video? What if I do this? And then this? There we go, there we go, make it, there you are, that's life. Life is good, it'll be interesting here. I've got to worry now with a bunch of panic people because now today, I don't know if you saw, but Amazon announced they're going to fire 30,000 people from

[00:01:03.77]  Jason ValleryCorp, from AWS, or just broadly.

[00:01:07.51]   Remoteuh... aws not know broadly amazon straight-up so and replace them with a how's everything tomorrow uh... well because the mcaf center doesn't just went through a gut-wrenching where they fired a bunch of people couple months ago so now in generally speaking Every time Amazon fires a bunch of people, Microsoft works with the courage to lay off more people themselves, right? - Yeah. - So they're, yeah, I'm gonna have to, I mean, we're probably not affected, I would think, our team, but I'm still, you know, there's a lot of people who are still gun-shy from the last round, right?

[00:01:48.84]  Jason Vallery- It didn't, it did, I should say, factor into my thinking around my switch. I don't know what all you know, but you know, I was coming back from sabbatical and didn't really have a role. All the kind of political issues with bombsheet and PM and stuff. I came back to, I was expecting an actual job, and Manish was like, well, you're just gonna sit on the bench and do nothing, and so I came back and I had literally no work, and I'm sitting there thinking, okay, well, it's great and all you're paying me to sit here, but you know, the next time a layoff round comes along, who's gonna get the ax first?

[00:02:30.87]   Remote- Right. - So that was in my thinking of this isn't a normal situation so, yeah. I was in a kind of a similar situation as well, I don't know if you know it, but over in compute.

[00:02:43.64]  Jason ValleryYou've alluded to some, maybe you didn't get along with Niddy, but what else happened?

[00:02:48.62]   RemoteWell, Niddy just decided, Niddy, it's, Niddy basically wants to do Noelle's job and Ronnie's job and not basically be an... Azure PM lead right she just does build out and I kept telling her look if the VMs don't work if the product doesn't work we can't like yes open a it's buying a bunch of stuff from us but it's that might snap back and then if if opening a currently opening is the only customer that can are what we're pushing out. So if all of a sudden they decide to take it, who's gonna deploy it, right? We're fucked, and she didn't want to hear that. She would rather just pull stuff out. I mean like everyone does, everyone, like I don't know if you know, but it's all build-out now, right? It's just build-out. They're getting teams, like they just pulled all of Mitra's team, and they put them on buildout, because Mitra inherited a lot of my team, right? She inherited about half of my team, Mike Requa inherited the other half.

[00:04:00.67]  Jason ValleryWhat does that mean, by moving them to buildout? They're just capacity spreadsheet monkeys, and no...

[00:04:07.57]   RemoteSpreadsheet monkeys. Yeah. Capacity spreadsheet monkeys. They call up, they call up Nimbus and say, "Hey, when's the cluster coming up?" I mean, I had one guy on who reported, who I helped bring in, who reports it in. He's like, he's like, he's like, he's smart beyond his ears because he's like, he's real young still. He's like 25, 26. He's like, it's a really easy job, and A, is it okay for me to get paid this much to call up Nimbus and ask them for a schedule? And he's like, so what I was doing, or Stevie P wasn't too interested in, but I was building skills and working with customers, which were marketable. He says, like, I don't know if from what I'm doing now, it... could use it to get a job somewhere else.

[00:04:55.88]  Jason Vallery- I mean, this was what was happening in storage too, and I feel bad for Pete because, you know, he was hired in with decades of storage experience, full understanding of object, you know, great customer engagement skills.

[00:05:09.94]   Remote- Yep.

[00:05:10.74]  Jason Vallery- He got tasked with spreadsheets, right?

[00:05:12.98]   Remote- Yep. So, yeah, I mean, and then that's what I had become with MAI, right? Yeah. I was a spreadsheet monkey. Just what's MAI schedule, where's it going? And then, you know, Sagar was like, "Yeah, but you're doing a good job, you don't have to leave the team. I mean, Nidhi's no longer calling for your head." And I'm like, and then I told Sagar, I was like, "Okay, what I'm doing now is valuable." but it's not value added, and I'm sorry, but a lot of this stuff vendors could do. I don't know why you're putting-- there's this woman called Priya on the team. She's got a PhD in data science. Her side gig, her side hustle is she's a professor at Seattle U for data science, right? I said, she literally calls up these companies and asks them-- what they state, if there's an update on the cluster of the status, and then because you guys are jockeying for position and trying to stay independent from CO&I and Sky, you guys don't share, so you build your own separate spreadsheets. So that requires everyone to manually update their own independent spreadsheet, right? right, so it's they're trying to each trying to break their turf and widen their own turf so they have compound or or like overlapping like data and they don't share it so it requires all these manual people to call each other that they don't trust to get updates so then each of them can then copy paste what their POV into a PowerPoint. than each of their COVs, this shares with Amy. It's so stupid. It's beyond stupid.

[00:06:51.56]  Jason ValleryI'm assuming you've seen the movie "Office Space."

[00:06:53.69]   RemoteYeah.

[00:06:55.36]  Jason ValleryI saw a hot take the other day that I think is really interesting. You know, the scene with the Bobs where they come in and say, "What is it exactly you do here?" You know, Accenture. I think is about to have a renaissance, because what you're describing is exactly the problem of there's a whole bunch of human-driven workflow and process that can completely be automated. I see what Accenture is going to do, and they can build a really big business on this, coming in like the bobs and saying, "Okay, what is it you do currently?" what is it you do, Marco? What is it you do?" And just being able to connect all of these things together, use AI, automate the shit out of it, and put you all out of jobs, and make a fortune doing

[00:07:41.25]   Remoteit. Yeah, yeah. So that's why I wanted out. I was like, "There's no way. Once someone figures out how much waste is in the system, we're all toast. We're all toast." That's why I got out.

[00:07:52.87]  Jason ValleryYeah, so what are you doing now?

[00:07:55.63]   RemoteSo now I'm over in Zia's org. I'm basically the global pre-sales lead for AI Infra. So I sell the shit I had to build the last 10 years. So that's why I met with people from Vast. Because when the new thing like market-- place they can comes online in like January I think it is they wanted like you know like how are we gonna go sell this kind of thing so all of the high-performance storage that'll most mostly my team will do a lot of the pre-sales for that

[00:08:37.65]  Jason ValleryReasonably engaged with Pia's team, but it was Mike Gahl and some other folks who are like driving a bunch of the deal qualification and pipeline for the 3P GPU

[00:08:46.80]   RemoteBusiness? Is it still really supporting those? So Pia still runs the process. Like, okay, who has requested what? Getting it all on the spreadsheet, right? But then my team basically does three things. First of all is we now score all the deals because we now don't have the capacity anyways. So we do one thing that's very tactical. We do two things that are more strategic. The tactical one is simply make sure Zia makes the right decision for Microsoft. because he can't give everyone what they want. So of the asks, which is the most strategic and better for Microsoft? So now we score those deals. It used to be they just looked at just like pull through, like how much additional pull through was there, but now we do stuff like, okay, how sticky is it? What type of workload is it? Is it a platform play then where they sell on Azure or just like, so, you know, we have a kind of a spider graph thing where we score the deals and basically come up with metrics. So any GPU allocation of a constrained SKU, someone on my team has to approve it. So Mike Gall, he can't go to DWR until we like literally sign it, right? So that's our tactical thing. The two strategic ones are then, like right now, there's a really big customer in Asia. You can probably guess who it is. It's asking for an obnoxious amount of GPUs within a year. So we have to go in and say, "Oh, okay, so we're doing everything from like, you know, sizing up the workload. Do they really need what they're asking?" for. Do they really need that type of GPU or actually can part of those workloads be on a different type of GPU? When they say they need like X number in a single data center, do they really need that many? Can they spread it out a bit? Then basically working with on the pre-sales and we have to then back working with you know my old team in engineering like you know how much power do you have where? Yeah then just stuff like that. that, and then basically help close the really large deals, and then last but not least, the third one is the feedback loop. So I don't know what conscience can be doing these days, because now a lot of the feedback loop, I'm tasked with doing that her team will do the same thing like the white gloving, because that's we don't we only pre sales, and that's post sales, right? So that for her won't change. But as far as the so then Zia has been now starting next month as a monthly meeting then with Jeremy Winter to kind of review all the Azure core feedback loop, like, you know, what's working, what's not working. So right now, as you can imagine, most of my stuff is on the very basic stuff, just like the VMs, make them reliable, please. support for the RdbInfini band?

[00:11:39.59]  Jason ValleryNidhi just sent me to Kanchan because I was trying to get some time with her to talk about FAST and the density problem that we can solve at supercomputing, and she said I should go talk to Kanchan. So I literally just sent a note to Kanchan asking for time to chat because apparently she said Kanchan's covering all the storage plays.

[00:11:59.03]   RemoteInteresting.

[00:12:00.22]  Jason VallerySo, I mean, here's the situation that I was shocked about. I'll tell you, Kirk, coming over here, obviously I had a comprehensive understanding of Blob and what he meant from a racks and megawatts and performance perspective and good opening eye, what you saw in Falcon. I just had no like internal frame of reference. how far VAST was ahead on the density play. But there's a problem in that what's going to come to market on the marketplace is very different than what VAST can do in private cloud on-prem, and so the marketplace offer that's gonna go out is built on top of L-series VFs, and so just like the math of it doesn't stack. on. No real developer is going to use it because cost per petabyte is astronomical. It's just like you're talking just insane numbers of CPU cores wasted, right? Because the ratio of CPU cores to NVMe on the L-series v4, and even EGOL's team is talking about an L-series v5. and then I'll make this better. But when you look at those numbers compared to what an on-premises high density SKU look like, it's just a fundamentally different world. So just internalize these numbers for a second. For one exabyte of blob versus one exabyte of vast, like apples to apples, one exabyte of capacity. Vast is one-tenth the number of racks, one-fifth the number of megawatts, and 5x the performance or more depending on the scenario. One-fifth the megawatts is the key selling point, like if you think about how many extra cram into that same power envelope and you look at what we were doing with Falcon, which is three exabytes of capacity, you would have freed up, and I need to do the exact math, but probably a couple thousand GB200 worth of capacity, at least a thousand. I need to get the math. So that's the that VAST has in the cloud. Doing that same thing on L-series VMs and doing this in the marketplace offer,

[00:14:21.20]   RemoteLike it's just not even gonna be the density in core ratio.

[00:14:26.39]  Jason VallerySo the marketplace offer is a fundamentally just lift and shift, check a box exercise at this point.

[00:14:34.11]   RemoteAnd so the task- - Why did they do it?

[00:14:37.75]  Jason ValleryFrankly, for Gartner's sake, just to say that you're in the cloud, you know, there's a difference. The product that's being built right now at Vast is a couple of things. So it is a control plane that'll work across GCP, AWS, Azure, OCI, and, you know, extensible into Core, Weave, and IBM. others that makes the management and deployment a vast super simple and something that where the customers don't even have to even log into the VMs to manage them. So that's super, but the way it'll be deployed will vary based on provider and you know that'll be the highest density storage optimized SKU you can get your hands on. You know, Google has better instance types, better shapes of the instances. Amazon's not as good as Google, and Azure's the worst, and it is fundamentally just this gap of number of terabytes of storage to core on the instance. So, you know, when we go do this, what we'll get out of it is checking a bunch of boxes saying there's a burst of cloud option. I don't really expect much customer penetration unless we can get to the point where either a) we're deploying OEM hardware into Azure that is storage optimized. For example, if they go on-prem, they partner with a hardware manufacturers and Solidigm to go and grab 160 and there's coming up 240 terabytes in the QLC drives and they just put as many of these in there as they can and they don't actually need much CPU. That's what enables the kind of density numbers I was talking about where you're getting one of the power 1/10th racks. Unless we can go off or something like that in the hyperscalers. it's going to be an uphill battle to win the cloud. But I think that opportunity is there. You know, the inflection AI guys, you heard this when we were working on Falcon together, how much they preferred Vast, you know, the platform, the performance.

[00:16:45.53]   Remote- And CoreWeave.

[00:16:46.51]  Jason Vallery- And CoreWeave, you know, my goal is-

[00:16:49.09]   Remote- CoreWeave just announced their own new storage, by the way, you see that?

[00:16:52.83]  Jason VallerySo what's interesting about it is it's like a proxy layer over VAST, so they can potentially like replace VAST in the long run. They're going to try and do something like that.

[00:17:05.23]   RemoteI was actually wondering that. So they... Wondering how much is theirs.

[00:17:10.74]  Jason ValleryI am. I do the core leaf too, so I got to talk to some of their peers when I was trying to decide

[00:17:12.74]   RemoteWhere I was going to go. I had an offer from Caruso, I said no. Yeah. Yeah, they wanted me to turn around and work back with Microsoft. I was like, no. No. I also had an offer from Caruso, if you know those guys, they were like a core week wannabe. I applied to Caruso, but then the thing from came in, so I pulled my application.

[00:17:41.19]  Jason Vallery- I mean, I kind of feel this way about all the neoclods is that they're going to end up being cannibalized. Like they're really right now, their business is a diversification of risk from the hyperscalers, but it isn't sustainable in a world where, you know, demand becomes much more predictable and data center build out schedules are much more controllable. So I feel like they're capitalizing on a niche moment where they can take the risk of selling the GPUs back to the hyperscalers and eat a little margin on it, but I don't see that as a sustainable business model.

[00:18:09.91]   RemoteI agree with you that is their primary risk, but these days I'm thinking less and less that's much of a risk. Simply because we, Amazon, just can't get out of our own way.

[00:18:31.14]  Jason ValleryWell, the debt of Azure, right, when you deploy first footprint services, they're 40, 60 racks, and each one of these new supercomputers that are going out, each new 4A, 12K cluster, you're building out 40 racks of computers. or whatever, bring it online. I mean, that's where I'm thinking a lot about how BAST comes into play, is how we can go and win those deals using BAST, bare metal, and I don't know, you know, this is where I'm in this weird situation because I know shit that you know, but BAST can't know, but I still know it. Like the whole Apollo thing, where they really need to just rip out. Azure and build a new bare-metal cloud that looks a little bit more like

[00:19:11.57]   RemoteOrweave? She's Apollo should go through. That's why I would talk to Ronnie. Nidhi's not your target. Manisha isn't your target. It's Ronnie. Ronnie Booker? Yeah.

[00:19:26.43]  Jason ValleryWhat does she own right now in terms of Apollo? Is she driving that?

[00:19:31.67]   RemoteNo, no, so basically the Apollo, the new bare-metal control plane would be a Chi, but the person that actually says, "Here's what goes in the data center," right, the people who do the chassis design, and then a lot of the blade design, then everything that, like, how do you do the layout, where do you put storage, all that, that's all, that design is owned

[00:19:52.85]  Jason ValleryTeam right yeah but where's the control plane sitting thank you because I knew

[00:19:59.73]   Remoteso they own Overlake right that's what I'm saying has to go through that yeah because they own they own the security that FPGA that when that when it starts it says I am sure here's my security stack So, so I would think because sky owns that anything that then goes around and be at storage, be at the chassis for this, they designed the chassis then right and and a lot of the, the data center designs, and then they also own, then on the back end they own break fix right. Yeah. So you have to have, if you're going to put your own product in there, and then maybe do like what Core was doing, just put a proxy wrapper around it, you would have to go through them first. Right.

[00:20:53.64]  Jason ValleryAnd I mean, there's no reason, the thing about Vast is interesting is that the hardware is it is just sort of like certified and plenty of deployments of assets and commodity hardware, variety of different white label providers. There's no reason that Agra couldn't go build

[00:21:13.49]   Remotea storage-dense SKU, which they have done. I'm sorry, they haven't built a storage-dense SKU, but they've taken that approach. For compute, they've actually had like the IBMs or the HPs or like this is what Brett Tanzer's team does a lot, right? They go in and they, for Azure Dedicate, they go in and say, okay, here's the spec, here's the standards that then they define. Yeah, do you know BizDev? I mean, 'cause Jovain, like, was the guy who was bringing together your team. teams, like when Lior was there?

[00:21:48.81]  Jason ValleryNo, yeah, so I know obviously Lior, but I don't know the Microsoft side on BizDev yet.

[00:21:55.74]   RemoteSo there's a guy named Joe Vane, and then his boss, Harish, they're over in BizDev, and what they know is Marketplace, right? Right. They probably don't know to propose what you're proposing, and you could educate them, and because they're biz dev, you get John Tinter to sign up and he goes and talks to Ronnie. Yeah. That's your path. Yeah. That makes sense. I would think you would be wasting your time with Manish and Nitti. Well, for sure, Manish.

[00:22:27.51]  Jason ValleryI mean, I think Nitti understands this a little bit. Hopefully she can become an ally in pushing the agenda, but I know she isn't going to own this.

[00:22:36.12]   Remote- We'll only push it if it helps her with OpenAI.

[00:22:39.07]  Jason Vallery- Well, and it will because it will free up megawatts and for more GPUs that she can go sell.

[00:22:44.62]   Remote- So just, so when it comes time to like sell her, tell her, explain exactly how it will help her with OpenAI.

[00:22:53.60]  Jason ValleryWell you know it's interesting at OpenAI, man I live in a weird world where I don't know what I can share with you and what I can't so I'm just going to tell you things. You know the VAST guys worked really closely with XAI and Tesla. So today XAI and Tesla use VAST storage in Elon owned and managed. manage data, right? And so it's all running the vast stack, and this guy, Uday, who was Elon's head of infrastructure, and so he's built out the Colossus supercomputer for XAI. OpenAI just hired him, and he's now Rory's boss. Did you know Rory at OpenAI? I don't know how much you guys meet the OpenAI folks.

[00:23:41.92]   Remote- I didn't meet, I didn't work with OpenAI very much. I work mostly with just MAI because-

[00:23:46.40]  Jason Vallery- OpenAI would be like Nitty's counterpoint. Like he's the key buyer of OpenAI, right? So this Uday-

[00:23:51.80]   Remote- I know the name, yeah.

[00:23:53.09]  Jason Vallery- This guy Uday at XAI is now Rory's boss, and then nearly last Thursday, he cleaned up. So a bunch of the people that I used to work with with open AI found out their last day was this Friday, and we're bringing in a whole bunch of people from XAI who are pro-vast in their open AI.

[00:24:11.42]   RemoteOh, wow.

[00:24:14.48]  Jason ValleryYeah, as of Friday.

[00:24:16.42]   RemoteWhat's his last name?

[00:24:18.55]  Jason ValleryOh, let me see. I'm going to go look it up. I haven't met this guy yet. find it elon suing openai over this oh really that's a mouthful yeah how can i share this to

[00:24:37.49]   RemoteYou i will send this in wait a second i can probably one second one second i can probably

[00:24:45.44]  Jason ValleryGoogle search, there's a data center dynamics article about it, but do a search for Uday, OpenAI, XAI and you'll see a very recent article about lawsuits and all kinds of shit. But so now Uday is making all of the infrastructure decisions at OpenAI. He's now the buyer and clearly there's obviously a bunch of work to go and diversify away from Microsoft. So it's a shit.

[00:25:08.84]   RemoteEND PLAYBACK Budai is U-D-A-Y?

[00:25:20.34]  Jason ValleryYeah, U-D-A-Y.

[00:25:21.54]   RemoteAnd last-- Yeah, yeah, yeah, yeah, I see him, yeah, yeah, yeah. Yeah. Yeah, yeah, yeah.

[00:25:26.15]  Jason VallerySo this guy, everybody at Bath knows really well, and he's-- now taken over the entire infrastructure team at OpenAI, and he reports to Greg Brockman. Oh. Yeah. So, I mean, I think that's good things for BATS. I think probably not great things for Microsoft, if I'm honest. Clearly, this is the guy that built the supercomputer for Elon, so probably they have ambitions of doing similar, of building their I think that you've been talking about it to a certain extent, so I don't know how it

[00:25:57.25]   RemotePlays out. Between you and me, I'm perfectly okay with us not doing any more deals with OpenAI because it's killing the rest of our business. So I'd be happy if that happened because increasingly, you know, I'm on the other side now. So what I see is very different, which is we actually do better when we don't have just OpenAI, when we have Grok, when we have like right now the fastest growing on a model right now. You know what it is? That's where our sales go?

[00:26:38.16]  Jason ValleryClawed?

[00:26:39.70]   RemoteNope. Anthropic.

[00:26:41.27]  Jason ValleryWell, that is.

[00:26:41.93]   RemoteThat's Anthropic.

[00:26:43.94]  Jason ValleryClawed is not wild.

[00:26:46.21]   RemoteOh, sorry. So Anthropic, as far as sales on Azure, it's growing the fastest in sales. Grok does well. But we do better when all of our tools and services can take-- use any model, and then we have capacity then for Mistral or Black Forest Labs, who then want to build their own models and then sell it on us, create more endpoints. That's actually a better business for us because right now we have OpenAI consuming all of our capacity. trying to warn NITIUM, like, they want to get off of our platform. You have no backup plan. The minute that they stop taking our shit, no one else can- it can't- it doesn't work anywhere else. Like, Black Forest Labs is still barely deployed, after three months.

[00:27:38.90]  Jason ValleryYeah, there was a big-

[00:27:43.14]   RemoteMAI, you know MAI did all- went to shit fast right what happened huh what happened nothing worked so falcons live the first tranche then and they're not able to use it uh well then they had to basically manually you know there's a bunch of people doing it man everything manually what does manually mean like run everything, basically fire up the VMs, make sure they stay up, have someone constantly ping pong the network, basically have our own like engineers who have access to the inner workings of the stack to constantly probe the IV network looking for IV health, and basically, and then troubleshoot, figure out why a job failed, try and bring it back as quickly online as possible. So it's, it's, it's basically you have a, they just released, actually, I forget the name they have for it, but they just released a tool though, that now actually gives them IV telemetry, like, like, we'll pull it in a standard way, rather than, than we're like, have doing a bunch of manual queries to just try to figure out what's going wrong and stuff goes wrong because remember um the when we deploy it okay there's no support in the azure resource manager for arm i mean there's no support for the ib network or nb link domain so it doesn't know where in the network what gpu's it's loading because knows how many GPUs or how many racks it has, right? It can't say okay put a job on this rack, this rack, and this rack, like say CoreWeave can. CoreWeave can actually do it like inside the rack, say you know this node, this node, this node, this node to contain individual nodes, okay? Whereas Azure can't. It's blind. It just knows I can launch GPUs on this cluster but it's not topology aware. They should be, so they just did one thing now, at least where they can do now telemetry. So they actually see what nodes didn't launch. So now they can like reverse engineer and figure out what went wrong. But they actually won't be able at the rack boundary level to then place like jobs until like February at the earliest.

[00:29:56.96]  Jason ValleryHow did the storage side of it go? that Vishal or Vipin and Vishal had a bunch of anxiety over it. Like, is it working? Are they

[00:30:05.89]   RemoteAble to use Blob? Yeah, the storage seems to be working okay as speeds and feeds go. I mean, it's just keeping, I mean, it might start hitting throughput overhead if they were able to get all their VMs up and running at once. When you can't get all your VMs up. running. It's hard to know if you have a storage throughput problem, right? Yeah. If you have an aggregate throughput problem, but yeah. So it's, um, yeah, I don't know too much of the details because, you know, I'm out of that since July 1st, right? ARCO is still driving in. So they, what they did was is they then made John the manager. John Lee who ran OpenAI and then they everyone under him then now supports OpenAI and MAI right but he's losing people fast for two reasons One, OpenAI is not fun to work with. Increasingly, MAI is less fun to work with, and then John's just a horrible manager. He's a nice guy, but he doesn't fight for his people, and he throws his own devs under the bus, so then the devs don't want to work with him, which then makes life worse for the PMs. Right? And it's just it's it's he's never he's never been an operations guy. Right?

[00:31:37.59]  Jason ValleryYeah, well, I mean, that's the role. It's so interesting because it's not a PM role at all. It's a TPM, and really, it's just a capacity manager.

[00:31:45.59]   RemoteRight, right. So he's a he's a he's a he's an operations manager, like, okay, when are they going to exit, then, you know, they're no-fly zone and how could they repave it like in the SLA of 12 hours or whatever, right? It's just like, and it's not, I mean, nothing against the guy, it's just he's, yeah, he's never, yeah.

[00:32:06.18]  Jason ValleryWell, I think it sounds like you and I might have a chance to work a little bit more seriously together as we go down. I can tell you. I think that's priority at the moment is, right? - Yeah. - In terms of all of the different hyperscalers and where we sit against the play, it is an Azure opportunity before it is an AWS or GCP opportunity, and getting in there with better hardware skews is a priority, but we've still got to get the marketplace out the door. I guess I'd be interested to hear from you doing this triage of the 3BGVU business, what they're asking for in terms of storage and how like we can kind of come in and respond and support that over and above what first-party

[00:32:50.40]   RemoteOptions exist. Yeah, so I think I was able to establish pretty decent credibility with Lior and the guy from Iceland that I met.

[00:33:00.58]  Jason ValleryYancey. Yancey or something like that? Yeah, Yancey. He and I are, he's my peer, so Yancey is the prep owner and I'm the PM owner for Cloud.

[00:33:08.58]   RemoteOkay, so I think we established pretty good rapport, but yeah, you might want to double check because sometimes I don't know. I think your meeting went well and maybe it didn't, but anyway, I thought that. I thought they thought I was Daley Winozdak and I told them and I hinted at it but I couldn't say it at the time but I'll go ahead and tell you because now we're getting closer but one recommendation I'm making right now is um it's we just got essay approval which is like it's okay to tell you we're not at A2N yet I got to get A2N but thing I have pitched is we have a problem in the sense that in Japan or even in the states with neoclouds, I'm not going to do with every neocloud, like I'm not interested in doing it with like the coreweaves of the world, I'm more so doing with some of the smaller like lambdas, the ones that the fringe but it's it and it's actually more of a big deal in japan or in europe or other places where we have the japanese government of the korean government they go in and they indirectly subsidize startups in their country by basically backing a their own national neocloud like in or even established players like KDDI or SoftBank, right? And they subsidized them buying GPUs from NVIDIA, like GB200s, GB300s. So they have these GB200s, GB300s sitting in all these data centers, right? And then the field team, the account teams, they come to me and they want a discount on something I don't even have to match the pricing. of the subsidized GB300 price in this data center, right? That's never gonna get approved, never. Even if we had the capacity, there's no way Judson would dump shit on the market at a 60% discount just to grab training, right? So we do have NZ series GPUs. So basically my proposal, like I said, SAZ approved, what's his name, Brendan Burns approved, and then Naren in networking approved. I basically proposed that we take the Azure Extended Zones that we use to connect to the third party data centers now and make that an actual product. GA it, and then we also, I also recommend we GA the ACAS Stretch. They're going to call it ACAS NodeJoin. So we're getting a FlexNode, ACAS FlexNode is the name. Okay, and then what we'll do is, is we say, hey, go ahead. We'll just create a partnership with these different clouds, like in Japan or in Europe or in Southeast Asia, and we'll say, okay, guys, train away on that shit. Then when you want to, none of those companies are going to go international, outside their national borders, right? But they'll want to do inferencing on our stuff globally, right? Services, because they want to sell to actually Microsoft corporate customers. So I'm going to say, okay, so then why don't we then have this connection into your data center, where then they'll train, train, train, train, train, and then when they go to deploy the models and run them globally, you know, then they can do that on Azure, and so that's the pitch. So what's missing of what I just described? Storch, and the ability to have a same namespace, okay? And we don't have something that we're even saying namespace across us and our partner, you guys do. So you are the missing link.

[00:36:38.34]  Jason Vallery- Yeah, I mean, certainly one of the product priorities that I have for the platform is to be able to have the model where it is central storage where the core data assets live in Blob likely and then we continue to live in Blob but then you can spin up a vast cluster in a CoreWeave data center, an InScale data center, Nebius, wherever and be able to connect back to that central data repository sitting in Blob and have it performant and locally cached against the GPUs. in the third-party data center like that is a key part of the strategy we have to get you but vast can't do that today because that just isn't how it's architected and it needs a bunch of work to get there. You could do that today if you had a high density hardware deployment as central storage but we don't have the offload blob yet. Yeah, interesting. So, but the extended zone piece, what's preventing you from putting Blob in one of those data centers? I mean, that seems to be what was happening with...

[00:37:38.51]   RemoteIn the bare metal? In one of their bare metal data centers?

[00:37:42.43]  Jason ValleryYeah, but once you put in extended zone, you're not... I mean, the GPUs could be bare metal, but you could still deploy Blob...

[00:37:49.02]   RemoteThey're going to want to have a local storage, because, remember, we don't... Right, it's contracted independently. Okay, these these these companies like a DD air where they're gonna have their own local storage

[00:38:00.45]  Jason ValleryBut my point is if you make it an Azure extended Went in and deployed, you know, whatever that team's minimum footprint is the 2040 racks that make it in no, no, there's no hardware

[00:38:13.05]   RemoteIt's just the connection. It's just basically expressed through

[00:38:15.67]  Jason ValleryConnection but then it's not an extended because you don't have the the because the extended zone when i i mean i did a bunch of extended zones for open ai they they got a whole bunch of first footprint services and you know you've got like 40 racks of maybe 20 racks of compute minimum like

[00:38:30.85]   RemoteThat's what we did with coral weave in portland i'm sorry it's going to be it's it's going to be the Azure Extended Zone is pretty much just a network. - Interesting. - That they've downscoped it to that. Because these third party, 'cause remember, they're not contracting with us.

[00:38:53.66]  Jason Vallery- Yeah. Who's the extended, like the guys that worked with on the Extended Zone team all at Microsoft too, like who's your Extended Zone PM at this point? Oh.

[00:40:08.21]   RemoteYou you youBLANK You you You Hi! And we're back. We're back! Although I am on the web version of Teams, which literally, this is the first time I've

[00:45:16.80]  Jason ValleryEver used it, so I don't know how this goes.

[00:45:23.44]   RemoteLet me look at it real quick and answer your question about who's the PM? One on my team is the primary conduit on that, not me. >> Well, I mean, I like- >> Exactly, yes.

[00:45:34.80]  Jason Vallery>> It's kind of in line with where I was thinking things were headed. Even when you like later in the Apollo conversation of you've got all of this new cloud capacity coming online, sovereign capacity. data centers that are just hosting GPUs, somehow Microsoft has their, you know, finger in the pie, and those sites will need some amount of local storage, and Azure Storage can't deploy unless you've got the first footprint services there, which puts you in a little bit of a bind, and it feels like the opportunity for a third-party to step in.

[00:46:08.32]   RemoteThere is, you nailed it. That's exactly the opportunity, and I don't think anyone's really woken up to that yet.

[00:46:15.13]  Jason Vallery- Yeah.

[00:46:16.08]   Remote- I pitched it, so he was like, yeah, we need that. Yeah.

[00:46:20.30]  Jason Vallery- Well, and you know, Manish has, if I had stayed, Manish said, oh, you're going to be architect on Apollo. But, you know, he got, he got. 30-something headcount for the project, but he's just doling him out to the same old players and the whole idea is Well, we're gonna go build a brand new storage platform that doesn't have all of these external dependencies but like Even if even if I had a vision on what to build there like executions of three-year projects at minimum and all of this capacity is coming online now, which means that, you know, they're really just, they don't have a solution. Just, there is no storage solution in Microsoft for Apollo in my mind.

[00:47:04.33]   Remote- Brian Moore is the... so be sure, Kishore Enamapuri, Enamapuri is the-

[00:47:21.84]  Jason ValleryI know Kishore, I should set up some time with him. Yeah, I know, I know Kishore, I've worked with him.

[00:47:27.84]   RemoteOkay, yeah, I'll reach out to him. Oh, not on this just yet, it's still an essay. about this but we don't know yet yeah we gotta get we gotta get um sign off on a2n before we can actually like say okay let's go do this because remember until a2n you hit a2n no head count right yeah yeah i'll play we're probably three we're probably three weeks away from getting past a2n and this would be

[00:48:00.88]  Jason ValleryFor all of these sovereign - does that include in scope the in-scale deal that's going on?

[00:48:05.52]   RemoteSo right now the scope is, very deliberately, we instead of competing for training with these Neo clouds We say we just tell because we don't have the capacity which rather than say no we say hey deploy this Neo cloud and Then we'll build a connection to the Neo cloud into Azure So then you can run your inferencing and all your foundry stuff on Azure Build your model on the Neo cloud deploy your model on Azure. So it's basically providing that connection and the ability to then, you know, have a control plane in Azure that can look at then what's going on in the Neo cloud. It's really that simple. I'm not trying to complicate it right

[00:48:59.57]  Jason ValleryNow. No, no, I think that's right. Of the deals that Microsoft has been publicly signing, like the InScale deal, is that how they consider the... that infrastructure that it will be something like that. You go train here, deploy into Azure kind of model. Is that what they're doing there?

[00:49:17.11]   Remote- So I'm building on what they use today for those things. Yes. It's all, that's why I'm pretty confident I can get there because I'm basically saying, I know how they, I'm like, you know, to your point, we do with core, we did it with core. although it's more pronounced, and then MAI. It's also how OpenAI accesses Oracle and OCA and all the other stuff they use. So I'm basically saying, "Hey, let's take this Azure Extended AI Zone connection, and let's take AKS Stretch, and let's just GA them because we know they work." like we enable our first-party services, or OpenAI, to effectively pull data back and forth between a third-party data center, let's enable our customers to pull data back and forth between a third-party data center. That's all I'm doing. Yeah, makes sense.

[00:50:09.26]  Jason ValleryDo you have a pipeline of customers interested in this?

[00:50:14.27]   RemoteMore so than a pipeline. of customers, I'm going after the Neo cloud or the Neo quad equivalent, and then their customers in that order. So for example, I know sakura.net bought 20,000 GPUs for GB300s in Japan, and I know that almost all of the startups who are funded under the Japanese government's GENIAC program are going to be deploying-- they're going to train their models on these clusters. So I want to get all those. So if I get Sakuran.net as my partner, then I get access to all those customers for then their global inferencing. Make sense? Yeah. That's the, I'm going via, so yes, there's customers that I want to get and I know who they're partnered with, but I'm first locking down the partnership so then I can go after the customers rather than vice versa.

[00:51:16.63]  Jason ValleryWhat's, like, Microsoft in this game is kind of just a middleman GPU broker.

[00:51:23.44]   RemoteNot even a middleman. We're just letting them say go buy it from them. Okay, and then when you wanted to put, because the first thing I did after I became, took my job now, I had access to all the subscriptions as I basically had my team, I went ahead and go through a new analysis. Okay. Of how we make money. Okay. We make more than two X. on inferencing that we do on training. Training, for every training VM we sell, we get basically $0.80 on the dollar.

[00:51:55.75]  Jason ValleryIs that--

[00:51:56.25]   RemoteAnd other additional services.

[00:51:57.61]  Jason ValleryIncluding OpenAI or excluding OpenAI?

[00:52:00.61]   RemoteThis is public customers. I don't deal with OpenAI, and I don't deal with MAM. I only deal with third-party customers. So with our third-party customers, the only pull-through in services is pretty much storage. - Yeah. - Right? For training. For inferencing, it pulls through a bunch of other storages. So we make more than $2 for every dollar. - Yeah. - Right? I did this across, I did analysis of 1,400 corporate subscriptions, and so, I went to my, I went to Zia, I said, "Look, we make more money, okay, we don't have ND series anyways, so why don't we go to these neoclouds where all these ND equivalents are going and saying, 'Hey, Mr. Customer, Sir, after you train your model over on this neocloud, you got to deploy it on inferencing globally. We have Foundry, we have these other goodness, why don't you deploy it on us and run, you know." do all your NC type workloads on on azure that's that's the pitch you know you make more money than it needs open the eyes the way they think about

[00:53:02.91]  Jason Valleryit is that these clusters are fungible and that they can use them for training one day and inferencing the next and they do that like that's how they

[00:53:09.95]   RemoteCorrect correct but our clusters aren't fungible apology aware. No, OpenAI can use our clusters fungibly. We cannot. Remember, you have to be able to go in and say, okay, here, well, I'm sorry, you could probably do it the entire cluster level, but within a cluster, like the way CoreWeave can say, okay, within this cluster, rack, you know, like rack one to 14, you are now going to be inferencing rack 15 to 28, you were training and then, oh, wait a second, we're now going to launch a new model. So we're going to keep training, but without interrupting the training job, we're going to squeeze it down to just now four racks we'd be running the training load and we'll have this overflow then of all these extra racks available now to handle the influx of all the inferencing jobs coming in. Okay. OpenAI can do that on our shit because they built their own control plane. - Right. - Right. We have no ability to do that. Yeah.

[00:54:05.18]  Jason ValleryBut that's got to come. I mean, that's got to be part of what this Apollo clan looks at.

[00:54:08.98]   RemoteI assume. Years away. Yeah. So I've got to do something. I've got to sell shit now. Yeah. Right? Yeah. I'm going to sell shit this fiscal year. Yeah. I can't wait for Apollo.

[00:54:24.89]  Jason ValleryHow do we work together? What do I do next? I'll go talk to people in Ronnie's work maybe, but how do we, how do we get going with this?

[00:54:35.10]   RemoteUm, I think, um, probably the first path, a good path to go through is, um, Harisha's org over in biz dev start to you got to educate them because they are the ones who get set of the meetings With pretty if they're believers, they can set up a meeting with pretty much anyone inside answer Yeah, or anyone inside Ronnie's org or if they have John Tinter's blessing, right? and so Use them as your sounding board to say, you know, go in and say, "Look, great first step with the marketplace thing, but, you know, let's not have a Winston-Wolf moment here, if you know what I mean, and let's do more. Have you guys thought about this? Look, we, you know, we have a, we can do a single namespace across all these different clouds. So what can we do to help you pull those workloads to Azure and then get their wheels turning?

[00:55:42.88]  Jason ValleryYeah, I think the biggest win we'll get, and we're trying to push MAI on this right now, is the higher density, higher performance, or megawatts, that seems to be the biggest win we'll win.

[00:55:53.66]   Remote- That's a good idea, if you get Mustafa. Yeah, that's a good idea. Well, you weren't involved, so you don't know. So you should ask your deaf counterpart, the Icelandic dude, if they're aware of the density. and the power wattage because if they know that, then they're your best advocate, and then if you get Mustafa to start pushing for it, 'cause if Mustafa says, aha, using VAS gets us more nets, it's more wattage, what's nets mean or GPUs? 'Cause right now we are capacity constrained on power. Right now they run out of power, effectively the end of June, next year. There's no more power. They're running around trying to negotiate more power now. Yeah.

[00:56:43.17]  Jason ValleryYeah, that's the angle I've been pushing, and I will continue to push. I sent a note to Kushal and to Vipin to try and kind of walk them through. I put a slide deck together that shows the comparative density and power characteristics of a vast rack, and if those guys were like, well, let's go, can they can push through Mustafa to say fuck it we just want to put VAS racks in the Falcon cluster that's that's the foot in the door I think there's a similar deal going down with UK Met where we're attacking it now where UK Met made a better performance lower power and so if that can be that I think that's I think that's VAST's Put in the door to deploy oem odm hardware into an azure data. Yeah

[00:57:28.35]   RemoteYeah, yeah, and then well, I think if you were to go look look Mai wants it Uh, uh uk matt wants it And then, you know, basically get corp corporate dev and biz dev to be your hounds ones that have to build all of the justifications. Yeah. They're the ones that have built a business plan and they're the ones that pitched to Amy. Yeah. So, and ultimately it's going to be an Amy thing, and right now Amy is on the hunt for power. Not personal, like power, but like lots. megawatts yeah so that's that's that's I think that's your ticket is to basically say hey look you guys are gonna run out of power you still haven't found power you need it we'll get it to you well at least save yourself um yeah I have to quantify it against

[00:58:28.72]  Jason Vallerya few different scenarios but I mean the

[00:58:31.15]   Remoteis pretty clear. It's about a fifth the power per exabyte as blob. Right, but if you then have, if it's denser to begin with, and it's one fifth of the denser thing, then it should reduce by quite a considerable amount. Yeah, exactly. Right? Yeah, exactly. I need to translate that back into GPU counts, but yeah, exactly. Oh, yeah, if you create a cheat sheet, But basically, every exabyte of VAST data nets you Y number of GPUs, you're golden.

[00:59:04.36]  Jason ValleryYeah. I mean, here's the math, though. The number I left out in selling the story and the vision is that it's 2X the Catholics. So while VAST is one-fifth the power, one-tenth the racks, at least 5X or greater the performance. performance, it's also 2x the capex.

[00:59:18.41]   RemoteYeah, but right now you can't buy power. Right. That's the vision.

[00:59:24.37]  Jason ValleryAnd that's the reason why I'm like, well, you know, maybe you're paying twice as much for storage, but you're getting way better performance and way better power utilization. You probably can justify that 2x in capex.

[00:59:37.61]   RemoteRight. Because if it's cheaper in power, yeah, if you save your money in power Yeah, exactly. I would think power. I would think I would think powers that is at a higher unit cost than storage. Anyways, isn't it?

[00:59:50.30]  Jason ValleryFor cheap use yeah, I don't think it's the kilowatt hours that are the thing that are the constraint It's the opportunity cost of using that

[01:00:01.21]   RemoteI always appreciate her, but I thought of her mostly as an industry person and not the

[01:00:18.94]  Jason ValleryMost technical person. These guys are really technical, and I think that's the best way to do it.

[01:00:23.69]   RemoteSkillset needed. What's your take? I think she's quite technical, but where I think she's quite technical is she has, she knows the tech across networking storage and compute, right? So I'm sure you can find someone in storage who has deeper technical like depth than her in storage, but where she's good is kind of like I said, seeing where those. three things come together. Uh, I don't, um, you know, so yes, she knows the various industries. Um, but I, I kind of look at her as a secondary, um, industry person, not a primary industry

[01:01:01.47]  Jason ValleryPerson. Yeah. What's she up to, uh, right now? What happened at, you mentioned she's being repurposed where she had.

[01:01:08.70]   RemoteRight now assuming she doesn't leave. They put her on observability which is now that they can actually get the telemetry out of the the IV telemetry. You know how do you kind of productize

[01:01:24.14]  Jason Valleryit? Yeah. How do you turn it into a service? One of the things that you know Jeff one of the co-founders said to me the other day is because there's actually actually, you know, I won't name names, but let's just say there's several people in the storage organization that have been trying to get roles at VaST even before I applied, so I was thankful to kind of come through. Yeah. You know, right now, the relationship with Microsoft is delicate, and so the last thing that VaST wants to do is rock that boat too much. So I think there's a little bit of, like, waiting. see before they make more moves but there's a couple of people in Manisha's org that have been working closely with Vas for a long time who they were considering um who are disappointed at the moment because hiring them kind of got put on hold after they hired me so I don't know what

[01:02:08.75]   RemoteThat for Mitra but you know I see that makes sense because yeah you but you both you and Glenn right

[01:02:16.22]  Jason ValleryAnd I can tell you, there were a couple of other folks in Ong's org that were about to be hired and then they hired me instead. So, yeah.

[01:02:29.22]   RemoteInteresting much with Microsoft at the moment, small too much.

[01:02:33.45]  Jason VallerySo, I don't know. Jeff mentioned to me that he mentioned. So, I knew that Nidhi had reached out on Mitra's behalf as well.

[01:02:42.13]   RemoteNidhi pinged Jeff the other day and said, "I've got this person on my team, Mitra, looking for a role." Yeah, my boss. I don't think Mitra knows that Nitti's doing that, by the way.

[01:03:10.99]  Jason ValleryThat's how I found out about Mitra's situation before you mentioned it to me, because Jeff pinged me the other day. He's like, "What do you know about Mitra?" He's like, "Oh, Nitti, that she's looking for a job."

[01:03:21.03]   RemoteI was like, "Oh, okay." No, Niddy, Niddy basically wants to get rid of everyone who's 66. Yeah. She's basically swapping it out and anyone who did software or like basically, anyone who basically doesn't want to be a worksheet hound, she's getting rid of them. Yeah. Everyone she's hiring is a worksheet hound. I don't know if you've known the type. Remember, like, Ahmet? Yeah. That's the profile. Yeah. There's more worker drones for Suresh.

[01:03:57.25]  Jason ValleryIf I would have stayed in the role I was in previously, that's the kind of profile of person I would have wanted for the storage engagements, because that's what the job looked like. It was going and changing capacity, demand, turning it into a forecast. building it out with CO&I, CSCP, and, you know, just turning that crank, you know.

[01:04:15.27]   RemoteLike, it's Jane's job in her minions. That's what Jane does for VMs, and that's what Suresh does for bare metal, right? Basically, so those are the two main teams, so there's really now only four teams under Niddy. Forget about Kanchan's team, but she's kind of worried about how her team will survive because they're already getting picked off as well. But there's basically Jane's team and her minions that do the VM-based, which you just described. There's Suresh's team, which is the equivalent for bare metal. There's then Jon's team, which is the operations team. for OpenAI and MAI, and then of course, then there's the team everyone always forgets about, which is UKMet back in England, because it's contracted to be under her, and then there's Conscience team, which is desperately trying to like attach themselves to every opportunity

[01:05:08.49]  Jason ValleryThat comes down the pipeline. How are Jack and Cyra kind of dividing and conquering? How do they think of themselves?

[01:05:16.45]   RemoteSo, oh, I'm sorry. I forgot about Jack. So then they still have to do nominally, you know, the CPU and the GPU, like host designs, right? But increasingly, it's just it's, it's just a lot of paper pushing, right? It's reconciling the design, because like, you know, five years years ago we would just we would say okay what type of CPU do we want to put the host we would negotiate for different types of CPU types Intel or this or that what generation what generation the PCIe should we do or but now it's all fixed because Nvidia basically says increasingly and I don't even know what Evan will do with the interconnect because with Nvidia pushing their standardized blue field out and if already done the gb200 gb300 now they're going to be bundling then the networking then with the with the host design as well right right now it's so the host comes like we have no choice okay it's oh it's going to be a 72 gpu rack it's going to be the grace and then the uh blackwell super chip take it and you will like it there's no design going

[01:06:23.85]  Jason Valleryon, right? Right. Who's owning third-party accelerator? Well, they're all third-party. Who's owning the other accelerators? AMD, and then I know OpenAI, and Broadcom, and everybody

[01:06:33.85]   RemoteElse has their own. Maya, of course. Who's driving all of the hardware? So under Jack, the PMs that basically say, "Okay, Maya, AMD, and then the special..." CPUs, and then the GPUs, they're all under Jack. But like I said, increasingly, they don't, their job is to say, okay, so like, for the GB 200s, most of the that team right now, it's like, okay, what's the reliability? Like, so how many like, like, what do they call it? Buffer racks do they need? So it's more like that kind of stuff. It's okay, which drivers do we need to include in the image? It's the very basic stuff. It's important work, but it's... there's no... I mean, Jack's team is probably the only team that even has a little bit of creative... creativity left everyone else because it's like, OK. You know, OK, like, for example, oh, do we really want to go for the B three hundred or just want to skip it and go for the GB three hundred, right, at least they get to make some decisions. Right. Or how do we assess, say, the M.I. 450 versus the. VR200, right? At least they have some creative work, but yeah. So Jane's team, Suresh's team, Jack's team, John's team, all report to Sucker. So Sucker's end-to-end AI, right?

[01:08:11.49]  Jason ValleryYeah, and then Jack's just running the platform side. Makes sense.

[01:08:14.93]   RemoteRight. Yeah, so that's, that's the end and they basically collapsed software then they took my team and gave it to Jack, and then they're blowing up in the whole team, and they're just making them, they split some of them, half of them wound up being spread over to either couple went to Jane, a couple went, three of them went to And then two went to John's team, and then the rest are still kind of spread across among Jack's team like under Evan or under Vijay. So yeah, I had about 20 people, so they're all split four wins. Yeah, and two of them have already quit. they didn't want to be worksheet jockeys. Yeah, I get that. Well, good enough, Kurt.

[01:09:08.77]  Jason ValleryYeah, we should keep in touch and let me know as your deal pipeline matures and your ideas around Sovereign Cloud mature and how I can help you with those, and yeah, I'll let you know how things evolve on this.

[01:09:24.12]   RemoteYeah, and yeah, let's let's let's touch base and you're gonna be at super good. Yeah, you're gonna be there Yep Yep, and yeah, I can bring you into the AMD party if you want to go there. It's free food free dinner

[01:09:38.22]  Jason ValleryI'm waiting to be assigned on what I'm doing, but I was told there like 400 vast meetings happen that week and I'm going to get sprinkled through them, so it should be a wild week.

[01:09:50.59]   RemoteYeah. We're good. Cool. Cool.

[01:09:54.59]  Jason VallerySee you at Supercutty.

[01:09:55.59]   RemoteAll right, sir.

[01:09:56.59]  Jason ValleryTalk to you soon.

[01:09:57.62]   RemoteSee you at Supercutty. Bye. Three weeks. Bye.
```

<!-- ai:transcript:end -->
