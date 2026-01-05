---
type: transcript
title: 'Cloud strategy sync: Google TPU and Azure Apollo'
date: '2025-11-07'
entity: Jonsi Stephenson
folder: People/Jonsi Stephenson
participants: Myself, Jonsi Stephenson
tags:
- type/people
- entity/Jonsi Stephenson
source: 00 Inbox/Transcripts/20251107 0812 Parallels Transcription.txt
entities:
  people:
  - '[[Jonsi Stephenson]]'
source_type: unknown
---

# Cloud strategy sync: Google TPU and Azure Apollo
**Date:** 2025-11-07 · **Person:** Jonsi Stephenson · **Folder:** People/Jonsi Stephenson

> [!summary] Executive Summary
We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC is emerging as the vehicle to deliver on‑prem TPUs and currently only VAST and NetApp are viable file options; VAST’s real‑workload TPU benchmarks reportedly beat Google’s managed Lustre by ~20% and impressed with a cross‑region global namespace demo (Japan↔Ohio). We will leverage this in upcoming GDC leadership meetings. On Microsoft, Project Apollo is a Linux/Kubernetes control plane for supercomputers with MAI as first tenant; LSVx VMs are not viable for large‑scale throughput, pushing us toward running VAST on Azure Storage hardware (Gen9 flash SKU, ~40Gb NICs). Near‑term, MAI’s April Falcon build (120k GPUs in Dallas) is at risk if storage underperforms; we’ll explore swapping Azure Storage’s software stack for VAST on Azure Storage HW. Marketplace remains a critical checkbox for Microsoft. We also discussed a simpler cloud pricing unit (managed vCPU+capacity) to avoid pricing out of competition and improve transparency. Travel/logistics: Jonsi will join Google sessions remotely; we’ll try to meet Walmart and schedule a dinner next week.

## Relationship Context & Key Facts
- Google Distributed Cloud is the likely vehicle for on‑prem TPU deployments and tie‑back to GCP.
- Only VAST and NetApp are present on GDC; NetApp relies on revived OnTap Select.
- VAST’s TPU testing (from Google’s model set) showed ~20% improvement over Google’s current managed Lustre stack.
- Cross‑region global namespace demo (Japan↔Ohio) resonated with Google.
- Two Sigma: NVIDIA GPUs on‑prem, adopting Google TPUs for training; wants VAST across on‑prem and GCP via Marketplace; behind on cloud commits.
- Microsoft Project Apollo: new Linux/K8s control plane; first production DC targeted ~1 year out; MAI first tenant; DPUs under consideration (BlueField vs Fungible).
- Azure LSVx VMs are not viable for exabyte‑scale or large GPU clusters; Azure Storage hardware path preferred.
- MAI ‘Falcon’ build: ~120k GPUs in April (Dallas) at risk of storage bottlenecks; exploring VAST on Azure Storage HW.
- Marketplace listing is a required checkbox for Microsoft stakeholders.
- Leadership is concerned current cloud pricing may be uncompetitive; a managed unit (vCPU+capacity) is being pursued.

## Outcomes (What moved forward)
- Agreed to use VAST’s TPU benchmark results to support upcoming Google GDC discussions.
- Aligned to prioritize Azure Storage hardware path over LSVx VMs for large‑scale deployments.
- Confirmed marketplace offer as a near‑term priority to unblock Microsoft motions.
- Myself to continue driving hyperscaler strategy (Google/Microsoft) and propose a simplified cloud billing unit.
- Jonsi to join Google meetings remotely due to travel/house move; we will coordinate prep.

## Decisions (Agreements & rationale)
- Pursue deeper integration with Google Distributed Cloud and aim to be part of the GDC SKU.
- Treat Microsoft Azure as a distinct sell‑to motion (first‑party/Storage HW) separate from marketplace sell‑through.
- Use real‑workload benchmarks (not synthetic) as the standard for TPU/storage evaluations with Google.

## Risks (Interpersonal or dependency)
- Marketplace absence is a blocker for Microsoft credibility and internal alignment.
- Azure LSVx VM approach cannot meet throughput/power/rack constraints for large GPU clusters.
- April MAI Falcon (120k GPUs) may strand GPUs if storage underperforms; limited ability to change rack/DC plans.
- Internal resistance to a new cloud pricing unit; risk of pricing out of competition if unchanged.
- Potential relationship strain with Azure VM leadership when messaging VM unsuitability.
- Edge/minimal‑footprint deployments (e.g., McDonald’s) are not a fit for VAST’s current footprint.

## Open Questions
- Can Google formally share or allow us to share the TPU benchmark write‑up/numbers for external meetings?
- Will Azure approve running VAST on Storage HW for MAI’s April Falcon timeline, and who signs off?
- Which DPU (BlueField vs Fungible) will Apollo prefer, and what does that imply for VAST integration?
- Can Manish’s org (via Michael Myra) endorse using Azure Storage HW for VAST at scale?
- What exact next‑gen Azure Storage HW specs can be formally shared for planning?
- When is the Nidhi briefing, and what materials are expected in advance?
- What is the final definition and pricing for the managed cloud billing unit (vCPU+capacity)?
- Are we confirmed to meet Walmart next week, and who attends?

---

## Action Items (You & Counterpart)
> Tasks are standard Obsidian Tasks checklist lines. If you use a global filter (e.g., `#task`), ensure it appears in each line.  
> Common metadata: `📅` due · `⏳` scheduled · `🛫` start · `🔁` recurrence · priority `🔺⏫🔼🔽⏬`.  
- [x] Share TPU benchmark write-up and numbers for Google meetings @Jonsi Stephenson ⏫ 📅 2025-11-14 ✅ 2025-11-08
- [x] Attend pricing model meeting on Monday @Myself ⏫ 📅 2025-11-10 ✅ 2025-11-08
- [x] Prepare power/space and GPU-throughput tables for Microsoft (capacity- and GPU-indexed) to support Nidhi briefing @Myself ⏫ ✅ 2025-11-08
- [x] Coordinate with Kanchan and brief Nidhi on Apollo, MAI, and UK Met strategy and Azure Storage HW plan @Myself ⏫ ✅ 2025-11-08
- [x] Socialize VAST-on-Azure-Storage approach with Manish’s org via Kanchan (connect with Michael Myra) @Myself 🔼 ✅ 2025-11-08
- [x] Define proposal for a managed cloud billing unit (vCPU+capacity) and circulate for leadership buy-in @Myself ⏫ ✅ 2025-11-08
- [x] Join Google Distributed Cloud leadership sessions remotely @Jonsi Stephenson 🔼 📅 2025-11-13 ✅ 2025-11-08
- [x] Attend Google Distributed Cloud team meeting @Myself ⏫ 📅 2025-11-14 ✅ 2025-11-08

### Follow‑Ups & Check‑ins
- [x] Schedule dinner/1:1 in-person (Mon–Wed next week) @Myself 🔽 ✅ 2025-11-08
- [x] Confirm Walmart meeting timing, attendees, and objectives @Myself 🔼 ✅ 2025-11-08
- [x] Request and obtain formal next-gen Azure Storage hardware specs from Qi for planning @Myself 🔼 ✅ 2025-11-08
- [x] Assess feasibility of BlueField vs Fungible DPUs for Apollo integration @Myself 🔼 ✅ 2025-11-08

### Next 1:1 / Touchpoint
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
[00:00:00.02]  Jason ValleryI'm doing great, how about yourself?

[00:00:11.03]   RemoteYeah, doing, uh, it's been, it's been a crazy week, to be honest, with all the cleaning And I have this like I Had a couple of follow-up calls one from the guy that I know very well that leads Google Corta He was basically like hey Can you jump on a call with me real quick after the TPU meeting like like two days after that? one and basically like just a friend to friend do you think vast would potentially look into google acquiring them and i was and i was like uh everything

[00:01:07.51]  Jason ValleryFor sale for the right price yeah I think it would be more interesting to replicate the core we do right because that keeps options open in terms of replicating the deal with others and certainly that's how much do you know

[00:01:22.56]   RemoteAbout the core we do because I mean we are fluffing the numbers quite a bit I mean the actual deal is 270 million and then there are certain requirements that need to be fulfilled that's an additional 400 and then when the 700 comes we have to be able to deliver ease of management, ease of use, exposing more of the features and capabilities, there are specific roadmap items that need to be fulfilled. It's sort of like, yeah, I understand why we're doing it, uh, fluffing the numbers, but, uh, you know, it's not there yet. Yeah. The only thing that is true revenue

[00:02:04.75]  Jason Valleryis 278. Uh, I knew there was stage gates. I mean, I haven't seen the specific terms yet. Um, were there, I mean, it sounds like you've seen the details. things in there that we're committing to that you think we won't be able to deliver on?

[00:02:19.17]   RemoteNo, no, I think we will be able to deliver on all of it. I mean, it is a five-year deal, you know? It's actually a six-year deal. Yeah, there might be. There might be something. I don't think there's any glaring things that it's going to be tough in delivering. But I mean, it caught a lot of attention. I can tell you that.

[00:03:02.85]  Jason ValleryI mean, it's a huge number for a software-only deal. just for a software license, I mean, it's crazy. So Google, Jeff is certainly challenging me to help figure out the CPU problem. We've got a meeting next Thursday around this big cloud thing. Maybe I'm wrong, maybe you have more insight, but it feels like they've got us, need a solution to be managing these supercomputers that aren't deployed inside of Google cloud. This distributed cloud product may be the right answer there. I'm curious if your contacts have any take on that, or if you know anything.

[00:03:36.49]   RemoteSo Google distributed cloud, there has, like, this is going to become the vehicle to to deliver TPUs on-prem because they need to have some level of tie-ins back to GCP. Because right now, like the Anthropic deal, it's basically just, here are the TPUs, use your software, good luck, basically, and they are not surrounding it with anything. hardware deal, and they have to be able to really monetize on this properly. They have to be able to surround it with the right software stack.

[00:04:15.83]  Jason ValleryYour control point. Logging.

[00:04:18.05]   RemoteYeah, everything, and I think Google Distributed Cloud is going to become that. But this is also, like for example, this McDonald's deal that Google won was huge, like it was a massive deal. It's basically every single McDonald's restaurant in the world that's running on the ads and then everything gets consolidated. back to headquarters and then synced into GCP. So there are more and more deals like this coming up and they need a software solution like that would be able to manage or basically do all of the data management that is needed Running everything under a global namespace. I don't think that's very appealing when you when you think about when it's, you know, hundreds and thousands of McDonald's, you know, all over the world.

[00:05:27.09]  Jason ValleryWe can't scale that. We're not like that was what I heard from my friend Dario is that like the McDonald's deployment is a minimum footprint of just a few like pizza boxes, right? It's like a couple of pizza boxes. We can't scale down to that size and deploy vast in every McDonald's. Like that's not a platform. So I don't know if we could actually respond to that scenario.

[00:05:48.96]   Remote- No, I agree. But it's still going to be, you know, going forward, it's going to be really crucial for us to have that level of integration with the... Google Distributed Cloud and be a part of that, be a part of that skew and in all honesty, the only other player in that is going to be or is currently NetApp and the way they are doing that is actually deploying a 15-year-old software stack called OnTapSelect, and by the way, it was like discontinued and end-of-life notification sent out 2019, and now they're just walking it back up because this is the only way they can actually deliver on top, on GDC. On the large, sort of, Google TPU cloud, I don't think they're going to be doing Google Distributed Cloud there, for their internal use.

[00:07:00.12]  Jason ValleryI mean, it probably is the full GCP stack, you'd assume.

[00:07:04.28]   RemoteYeah, it's the full GCP stack. Google Distributed Cloud has way different APIs, it has very little correlation with Google. Yeah. With Google Cloud. So that's a real issue for them. Like for example, Google Elastifile, the Elastifile acquisition or Google Filestore. that doesn't have any data management capabilities and they decided not to port it to Google distributed cloud. So the only file systems that are there is us and NetApp. So I think it's crucial for us to win it, especially when it comes to these large TPU opportunities that they are going to be going after in the future.

[00:07:52.63]  Jason ValleryThe two sigma deal is that that's not going to be a GCP region that will be something else it'll rather look like the anthropic deal is that your

[00:08:01.27]   RemoteUnderstanding of it so the the two sigma currently has all Nvidia GPUs they are Google TPUs for on-prem for their training environments and then they're going to be doing all of the inferencing on GCP. But they are trying to, trying to take the entire amount for granted. vast, both for the entire software license, both for on-prem and Google, through the Google Marketplace. Got it. Because they are, like everybody else, way behind on their cloud commits.

[00:08:54.01]  Jason ValleryYeah. It's a common thread. That was happening all over Microsoft for years. theme. Every year there was always a customer that overcommitted and underspend and would have some sort of, like, either what Microsoft would do is allow them to roll the commit into their renewal and so you know they you know just their next commit at the renewal time when they were coming due would be even bigger and it'd be a bigger problem or they would have a small amount. they were trying to find partner or marketplace things they could go buy to spend it down or whatever.

[00:09:27.86]   RemoteYeah.

[00:09:28.92]  Jason ValleryThat's been the cloud since the beginning.

[00:09:31.47]   RemoteYeah. Absolutely, and they were like, I was in a Gartner briefing the other day, no, I was in a 451 group briefing and I'm going into a Gartner briefing and they told me that there are $52 billion of commits between all three of the hyperscalers?

[00:09:49.47]  Jason ValleryYeah, well, there's this interesting thing now of how that accounting is playing out, because there's the traditional enterprises that have what we just described, where they overcommit and underspend, and then there's all this AI training money from OpenAI and Anthropic and others, where it's not necessarily the same lens. It is pre-commits on these. super computer capacity build outs so that that looks a little different in my mind you know I think that money gets spent if the capacity gets delivered the risk is execution on the hyperscaler not on the customer to a certain extent but those numbers are going to get bigger and bigger and bigger as all of these deals get signed for you know GPU yeah but we had a

[00:10:32.27]   RemoteReally good meeting with Nirav, Rich Sansi and his team. Rich Sansi leads the compute team in GCP and therefore the TPU as well. So they really challenged us on the numbers. that we were getting, but I followed, I got the testing framework, all the models that they wanted us to showcase, I got it from the TPU team. So we weren't like paying any flavors, we got it directly from the TPU team, and we were 20% better than what Google currently has, as their sort of TPU offering and the entire software stack, the file system and everything that they have. It's managed luster that they do. It's not DDN, even though DDN of course is managed luster as well. So, we had already put it into the press release and Nirav was like, "Hey, we need to have a meeting because we can't figure out how you got basically Nearline local NVMe SSD performance out of it." And we actually got it better because of the parallelism. that Navast is able to achieve and how we are actually feeding it into it, and then they were blown away when we actually asked Kartik and Karl to actually do the demo and do the test case with the global namespace between two Google regions, and we had one in Japan and one in Ohio, and that popped up. Was where they were like, wait a minute. This is this is crazy. Hmm. That's and

[00:12:28.20]  Jason ValleryWe were run the VMs and when we're using the same VMs like apples to apples for the managed luster

[00:12:34.96]   RemoteSame disks not same VMs. We are using the c3m and And they were using a more sort of storage oriented capacity, but still on local NVMe, but just with fewer cores, you know, but yeah, from a TCO perspective, it's very easily compared to together. We're very price competitive, even with larger VMs for Google, of course. So they want to have a bunch of follow-ups meetings with us, and this was the only way I ... You can ask Jeff and Alon and everybody. They were very skeptical of me going into this head-to-head. of benchmark, but it isn't. It's like real work. It's not some, you know, made-up benchmark or using, you know, tools that you can bend to show you in a more favorable light than anybody else. This was basically, you know, model training that we did. Yeah, that's where we really shine. That was the only way I could possibly figure out how to get us into the TPU discussion with Google, and it definitely paid off.

[00:14:02.19]  Jason ValleryIs there any kind of write-up on the numbers? If you could share that, that way I have it when we meet with them next Friday just to be able to pull out some data to defend the solution, that would be helpful.

[00:14:15.27]   RemoteWhen, uh, uh, when, uh, who are you meeting on Friday?

[00:14:18.25]  Jason ValleryThe distributed cloud team. So they're not, okay. Yeah. Uh,

[00:14:22.34]   RemoteThe VP of distributed clouds. Oh, you're on the same meeting as I am. I was alone myself.

[00:14:28.70]  Jason ValleryAre you going to go out there in person alone? And they're planning to be there on Thursday, Thursday, I think afternoon.

[00:14:32.82]   RemoteYes. Thursday afternoon. No, I, I, I'm selling my house here. I'm really. I'm struggling just to get over to Ignite, you know, I'm handing over my house on the 17th and 18th and if that all goes well, I'm off to San Francisco for Ignite.

[00:14:48.19]  Jason ValleryOkay.

[00:14:48.84]   RemoteSo I have to be, yeah, packing up the house. So I'll join remotely, but like... If possible, I mean, Michelle Rochler, she added in a Google meet link for me to join. I would have loved to join in person, but I spoke to Alon and I will have to be remote. Are you flying down there?

[00:15:18.79]  Jason ValleryYeah, we're also going to try to meet with Walmart. There's a big Google project with Walmart. Walmart as well. They want to repatriate a bunch of, well, it's not initially a repatriation, but they want to do a big push to sync Google cloud storage data into an on-prem vast system to be able to run their analytics workload in a Walmart managed facility. I think long-term their plan is to actually get out of Google cloud, but yeah, that'd be interesting. of an update on where we're at with Microsoft, particularly as you go into your Ignite meeting.

[00:15:49.28]   Remote- Yep.

[00:15:50.54]  Jason Vallery- So I think you and Renan are gonna meet with Nidhi. She delegated a lot of the day-to-day and engagement with her team to a woman named Kanchan. I know Kanchan very, very well. We've worked together for many years, and she and I had a meeting yesterday and kind of went through a bunch of points. So she's going to be briefing Nidhi, and so I think the key updates are where we're at with Project Apollo, Microsoft AI, UKMath, and how a lot of this all comes together and what the strategy looking forward should be. So on Apollo, we met with Chi, who is the CBP... Her previous role was she owned the Kubernetes Service for Microsoft, AKS. She is now running Project Apollo, and they used the term Project Apollo, but they didn't use it heavily. But I know it very well from my days there. But the idea of Apollo, and I think you know this, is it is a brand new Azure control plane with new features. no legacy tech debt, bringing nothing forward from current Azure, none of the hypervisor, none of the storage stack, none of the net, well, maybe some of the bare metal network stack, but it is a Linux only new cloud solution for deploying supercomputers. So in some ways, I think of this as like what I'm imagining we're hearing from Google in their GDC team. Microsoft isn't going to be able to deploy Azure's Extended Edge Zone thing or their Azure Stack thing for this. It's just not going to work. So they have to build something new, and it's all going to be Kubernetes-based, and that's why the AKS team kind of ended up driving it and taking the lead position.

[00:17:31.67]   RemoteDoes he report to Brendan Burns?

[00:17:34.38]  Jason ValleryI think Brendan reports to her. owner and he's the PM owner, but yes, Brendan's involved with Apollo. Brendan is on the Project Apollo V team. The Project Apollo V team includes delegates from MAI, so Microsoft AI is the tenant, the first tenant customer, so they'll use it with Microsoft AI initially, but the plan is be Microsoft's go-to solution for this problem for all customers, not just in the eye. So it will evolve to be a mainstream solution. I don't know if it'll be called Azure or what they'll do with it, but for 3B customers, all the supercomputers that are being built, OpenAI will I'm sure end up in Project Apollo data centers, and I can even imagine that they're likely to to pave existing deployments of GPUs with Apollo once it's ready. The timeline for the first production data center is about a year from now. So they've got a little bit of work in front of them before they actually go and do the first full build. They're planning a 40 megawatt deployment for like September, October next year. MAI has a lot of requirements going into it additional stakeholders include you know the Azure Storage team and Asia's team has a representation in there with I don't know if you've ever met Jay Menon but he was running the storage unit and then there's this guy that founded Bungible Pradeep is the second lead he is pushing to bring their DPUs into it. I think there's a lot of skepticism about the maturity of the fungible DPU. At this point, I think three years behind schedule. It should have already been in mainstream Azure, but it still hasn't had a single production deployment. So, Qi gave us some guidance around the hardware footprint we'd likely run on and wants us to do. to talk about what it would look like to run on the Bluefield DBU, but also potentially to run on the Fungible DBU. I don't think they've made a decision as to if Fungible becomes part of this. What's interesting here, Qi wants us to run on Azure Storage Partner. So this isn't running on VMs, this isn't running on some ODM hardware that we provide. They want us to run on the hardware that Azure Storage has been planning to run on and the next generation Azure Storage clusters. Surprising to me, like Manish, I'm sure will be very upset when he finds out that's the plan of record. But, you know, I don't see them having a better solution. I think that the, their hands are somewhat tied about taking in third-party hardware and we obviously can't go on a compute-based solution. I put together a table and I've been kind of circulating with Jeff and some other folks that really shows what does it look like from a power and space perspective to run on Azure Compute, so LSV4, LSV5, to get to like an exabyte volume. what does it take for Azure storage blob hardware on hard drives, what does it take for Azure storage hardware on flash, and then our ODM hardware, and just sort of the to get to one exabyte running Azure Compute, the LSV4 is like 40 megawatts. Yeah, you know, it's just just a joke that you can't do that. So, one of the key messages we have to land with NITI is how just fundamentally flawed the idea that we're going to be able to ever use eagles VMs for any sort of scale deployment in nature to solve customer challenges, where we're talking about large scale GPUs, like if you're talking about a couple thousand GPUs, you're not going to back those with LSP for you.

[00:21:28.25]   RemoteIt's just not even doesn't really make it we can't even do the you know NBC Universal 4 petabyte diplomas 175 LSB force, right so you can see like it just goes out the window But the thing is like we have to I have to figure out a way to break it to them very, very gently because EGAL has already sent a hate mail after Renen called out that the VMs were not suitable for it. So we had to backtrack, and we sent a really nice note to EGAL saying, "Hey, we really appreciate the support, we're super looking forward to moving from LSV4 to LSV5, which to have 138 terabytes per VM versus 23 as is today. So I had to give him something because he was like, "Hey, I'm your executive sponsor and you're like burying me. People, EVPs across the organization are sending me, 'Why am I not supporting Vast?'"

[00:22:30.42]  Jason ValleryLike it's crazy yeah this is the the data around it I'm gonna do a similar so so another key message that I landed with conch on that she's gonna start socializes Nvidia's obviously got their reference designs around throughput per GPU and so this this version of this is indexed on usable capacity and trying to what a exabyte looks like, but I think another version of this table, which is indexed on the GPU reference design throughput per GPU, and so what would it take for a 4K cluster? What would it take for an 8K cluster, whatever kind of size cluster, to have a similar comparison point of megawatts and rack counts to achieve throughput for a 4K GPU? But I think both of those messages lend us to start pushing into there's no viable answer for vast on Azure until we get to hardware that is purpose built for this scenario, and I think, you know, ultimately, what this means is that we have to go to the Azure storage flash hardware that we can co-engineer with them. How do we make this something that Manish can digest without having just a heart attack? Because he will. He owns the specification for Azure Storage Hardware, so the PMT responsible for this and the requirements all sit in his org. There's a guy named Michael Myra that I've asked Kanchan to start talking to. I know Michael very well, I think ultimately we want to get his buy-in that what we could do is take what his team's already working on and make it the preferred way that we deploy VAST in Azure. Okay, what does that mean for MAI? What does that mean for other projects in flight? Independently, as I mentioned, there's this guy Khrushal Dada. He is the primary, I would call him the buyer for Microsoft AI. So he is the one responsible for interfacing between the MAI organization and the Azure organization and he's the Project Paulo V Team member. I know him very well. He and I had a one-on-one on Friday and we talked quite a bit. Independently they have a very large tranche of GPUs coming up. in April in Dallas for Falcon. It's 120,000 GPUs in one facility. They've ordered a bunch of Azure Storage to go with it, and given their experience with Azure Storage in their first deployments, they're very nervous that they're going to end up stranding a bunch of GPUs and they're not going to be as productive as they want with this 120,000 deployment. Obviously, 120,000 GPUs is a huge investment for Microsoft, and he wants to de-risk that deployment, and so he's asked, like, is it even feasible that in the April timeline, VaST could be running in, again, this isn't Apollo, this is current-gen Azure, and replace Azure Storage as a software stack on top of it. of Azure Storage Hardware. So, I'd ask Kanchan to start socializing. Last point, there's a UK Met opportunity. It's actually a similar conversation playing out again, where, you know, is it Azure Storage Hardware? Is it our ODM hardware? I think in that example, there's more flexibility because, you know, UK Met. already off the rails on a hardware footprint, they've got pretty supercomputers and cluster store and it's obviously not Azure already. So in that world, maybe it's even our ODM hardware. But what I'm trying to do with Nitti is get her to kind of sponsor this idea that VAST on Azure storage hardware to meet the needs of Apollo, to meet the needs of MAI in the short term, to meet the needs of UK MET. is really our shared path forward and for her to start using soft power to go influence Manish to let us do that and get that project meaningfully going. I think that's our best path to

[00:26:26.86]   RemoteSuccess with Microsoft. I agree. Do you have the specs of the storage hardware that they have today?

[00:26:38.00]  Jason ValleryWe asked Chi for it, and she came back and gave us the specs for the next gen version, which I can share with you, but that isn't something that we can deploy on today. That is the, you know, what they plan to deploy next September, October. Personally, I know the specs, but we haven't been formally sure. The cluster that we would be going on to is today known as Gen 9. storage fast XIO. I don't know the CPU, but it's qualified with 16 terabyte E1S rulers, so it's very low capacity. The reason why they designed it that way is what they were prioritizing was TPS and IOPS because that's the pain point for it. This is the hardware solution that Microsoft uses for the It is, as a result, because the NVMe is so small or the flash is so small, you're actually only getting like, after their EC scheme, maybe like 12, 13 petabytes per 10 rack unit. So it's not like it's very capacity friendly, and then separately, again, because the priority was not throughput, it was IOPS and TPS, they only have CX-5 NICs in them, and so you're only getting, I think it's a 40 gigabit NIC per box. So, and it's Intel CPUs, I don't know which CPUs specifically. But again, since TPS and IOPS were the priority, I imagine it's kind of beefy in the relationship. So what you're talking about is a hardware SKU that isn't going to you know be super impressive in terms of throughput, but it'll beat what we're going to get out of the LSV4. So you're going to get a 10 rack unit of deployment that's going to give you call it 13, 14 petabytes. I think they have enough buffer there that we're going to run it more efficiently. Maybe we'll get 15. to 20 out of it and 40 gigabit NICs and a beefy CPU yeah the like the 40 gigabyte

[00:28:39.40]   RemoteNICs basically take out takes out that this would be an e-box this would have to be disaggregated C and D's because otherwise we will be hammered on each

[00:28:53.03]  Jason ValleryBus traffic. We'll have to play with that because that would change the capacity plan so like if we really are serious about winning the April business from MAI which I mean I think that is the big like if we get to go power 120,000 GPUs inside of Azure I think that is a huge feather in our cap but what I will share with you is that Microsoft doesn't make leak binding decisions around tile placement and rack counts, and so I can almost guarantee for an April deployment that there's already signed off DC specifications around which rack is going where, and what that practically means is they've filled that facility to the brim and there's a finite number of Azure storage, air-cooled racks that are already in the plan, and so if we have to go disaggregate and ask them to do that. deploy additional C-box, C-node capacity, that would mean a change in architecture for them, and them deploying like adjacent CPU racks, I doubt they're gonna be able to accommodate that. The other thing I would point out is that the way they sign off this hardware and design it and everything, we wouldn't be able to change a rack topology. You know, we'll go deploy 10 racks of general purpose compute over there We'll go deploy 10 racks of Azure storage hardware over there. They wouldn't be interleaved under the same network spines

[00:30:11.09]   RemoteYeah So, I mean like this is this is part of the this is one of the reasons that We have to have, like, when we're doing the AOP planning and the goal settings, to me we should have it completely separate. You know, it's all, it's all clout, but we have to have like a cell to Microsoft Azure and we have to set a goal. there, and we have to treat, for example, in many cases, UKMAT isn't an end-customer deal with us because the end-customer for us is actually Microsoft. Microsoft has already won that deal and the name on the paper is going to be Microsoft. that deal. It's not going to be UK-MAT. Ultimately, we have to have one for enterprise, how we're doing that. Because in these deals, it's all going to be completely different based on the size of the opportunity, how much we're charging for the licenses, how we're building up the software license, and then it is the end customer where it's on our paper, where we are closing, for example, Two Sigma, Jump Trade, Waze, it's not a Microsoft, we would have a deal with Waze, NBC Universal, all of that. marketplace where we own the customer relationship with that customer and then have like, that's a sell through motion in my opinion and completely different and needs to be gold differently as well, and then you have the sell to the hyperscalers, like these deals that we're all working on. On the side, but we have to have, and I was talking to Leo about this as well, I was like, "Leo, you're all over the MIA deal and the UK MET. I need Tiffany and Olivia to be really focusing on the marketplace offering as well because we need to grow that." at the same time.

[00:32:40.29]  Jason Vallery- What's your take on how Renan will want to structure this? Because there's a couple of ways I can see this going and how this even gets framed with Nitti will be an important direction, you know, fork in the road. Like I could see the CoreWeave deal, and again, I haven't seen it in. like detail, but my understanding is it's, it's an all you can eat license. Right. So how much ever, or, um, how many of our customers they want to go deploy doesn't impact the total bottom line for us. It is, they can go and sell as much of it as they want. So you could imagine that like the deal that Brennan would want to replace ourself, Microsoft is that, and in that world, we don't even give a shit about the marketplace anymore, right? Like you go. write us a check for N billion dollars Microsoft and then you can go and sell this as a first-party solution. You know you don't even need a marketplace solution anymore because we're not getting any revenue for what customers in Azure consume. Microsoft gets all of that but we get one big upfront license or we continue down this path where we're selling individual deals, individual licenses for individual deployment. I mean, what do you think is in Renan's mind right now?

[00:33:50.79]   RemoteI know what's in there. He would always go for the big deal, but I mean, then we are a first party. It doesn't alleviate us from, you know, building the management layer on top of it because Microsoft is never going to be willing to do where they are. you know, where they have to be calling Vaast engineers all the time, like Corvive, and that's one of the biggest beefs from Corvive to Vaast, and it's a requirement in the contract that we supply the ease of use, ease of deployment and all of that to them, which isn't there today so ultimately if we become a first party offering where Microsoft can sell us whatever they want and they pay us $5 billion a year or $3 billion or whatever it is and all you

[00:34:45.61]  Jason ValleryCan eat we would always go down that route. in any way suggesting that it's not perfect?

[00:34:54.48]   Remote- No, no, no, no, no, I totally agree with you, but to your point, then we are a first party offering and Microsoft is selling us. We just have to, we then become the tier two and tier three support for that offering. But I mean, if they go down that path, I really believe that they would then try to acquire last.

[00:35:20.70]  Jason Vallery- Yeah, but it'd be a wild ride. You know, I'm sure you went through this to a certain extent at NetApp, maybe a bit different though, because what we were actually doing at NetApp was running on NetApp hardware, and so there was less of the hooks in place. But what I'll say is, if we go down this path where we're running on hazardous- storage hardware. None of the marketplace work is useful. I shouldn't say the marketplace work, none of the control plane work is useful. As you can imagine, like the way bare metal nodes are bootstrapped for Azure native stuff has nothing to do with ARM APIs, right? Because if you think of it as a layer cake, like the bottom layer cake is... arm is built on top of upper layers, and so the bottom layer cake is this internal thing called pilot fish that you've never even heard of. You know, you're talking about a whole bunch of firmware work, golden master images that then get paved up with nodes, like there's a whole bunch of management and ugly glue and PowerShell scripts and like all kinds of shit that is actually goes and bootstraps all those bare metal instances. There's a whole bunch of networking crap that has to be done, and then you think about upper layers get built on top of that stuff, and so ARM and Lifter has nothing to do with that world. It'll be an interesting journey to go on because that's not how we would be provisioning Vast in Azure if we get to this new Vast on Azure hardware world.

[00:36:46.24]   RemoteWell, I mean, everything in Azure is controlled. Every single product is controlled by the resource provider construct. Once it gets into business, that's how customers can actually consume it. So you have to do that work anyways. How you're bootstrapping it and how it's actually delivered to the customer, you have to have a resource provider, that's the glue that actually ties it into the customer accounts.

[00:37:12.64]  Jason ValleryYeah. That's fair for classic Azure. Apollo won't have them. Apollo is going to have an

[00:37:17.47]   RemoteEntirely new control plane. Okay. Yeah, I mean, yeah. I don't have any knowledge about the Apollo and the actual... software layer there or the integration layer there, or what they are planning, I would assume that they would have to be able to service it from a multi-tenant environment.

[00:37:43.53]  Jason ValleryInitially it's single tenant per deployment. So it's like, hey, there's one data center, one customer, we're going to give you the whole thing. Certainly their roadmap includes tenancy. But the initial Apollo project, Apollo is single tenancy.

[00:37:57.13]   RemoteOkay. That's, that's, that's crazy to me, to me, uh, like you're not reaping the benefits of a scale and it's, uh, once in a blue moon that you get a customer that is willing to take a full 20 megawatt data center or a hundred megawatt data center.

[00:38:15.72]  Jason ValleryBut that's the plan that's what they're headed towards I mean you clearly they recognize the same point you just made and they'll have to get to multi tenancy but initially this for MAI, Anthropic, OpenAI, like somebody who's like yeah I want all 28,000 GBE-200s that are in this building and we're gonna run them as a single non-blocking cluster I need a control plane for it let's go Yeah, then they'll get to multi-tenancy over time. Yeah. No, but I mean like

[00:38:44.56]   RemoteThis what we have right now is a is a Luxury problem in my opinion like there are almost too many opportunities to And I'm trying to like focus the engineering team on one parts of it, because Renan is dead set on getting the ease of use of Polaris and the deployments into the Neo clouds as well, and I'm really trying to focus the engineering team on just delivering on the marketplace, right? now, and like the overall strategy, I just don't want them to defocus on and missing any deadlines.

[00:39:30.71]  Jason ValleryCompletely agree with that. I think the marketplace, you know, one of the key things I heard from Microsoft as well is that internally us not having a marketplace offer in place, regardless of if it's actually a checkbox exercise or not, is a big... you know, red flag for Microsoft. So, you know, regardless of as if we think it is the way we're going to scale the business with the cloud providers, getting that checkbox checked is super important, and so I'm all in on that. Okay, we've got just a few minutes left. I'm obviously still coming up to speed with folks. I'm still getting clarity from Jeff on role and how I'm going to manage everything. But short-term, what can I do for you?

[00:40:12.85]   RemoteDo exactly what you're doing. You have been very quick into proving that you're a massive asset to Vest, and I really need you to run with these larger opportunities, and especially your inside knowledge of it. of Azure is tremendously valuable for us. Right now, if I could get you to work on one thing that is more related to the overall cloud strategy, it is figuring out this vast unit of measurement that we want to build by. You know, the chunks of vCPUs plus capacity, what is one billable unit? Because I feel like that's a much healthier approach than Eric Wolff and Tomer are doing, which is like these vCPUs, individual capacity, like, if you can do that as a managed unit, I think it's going to simplify the billing and it's going to increase the transparency to our customers instead of having to count like what is a virtual CPU versus a physical core. How do you reach like doing like, oh, a vCPU is. to have a physical core. I think that's very strange math that they do because in a multi-tenant environment you literally aren't getting a dedicated, so how are you actually making that calculation? Just continue down that path. path alongside with working on these massive deals or the strategy with the hyperscalers.

[00:42:12.43]  Jason ValleryWhat conversations have you had around this NVIDIU, VCU idea? I'll tell you, I tiptoed around it with Jeff, kind of soft brought it up, and I got a pretty violent negative reaction. So I don't know how much I can work up that tree without a lot of buy-in from other people. others. How many folks have talked to it about it and what's your take?

[00:42:29.81]   RemoteSo my take in the beginning was this was not suitable for cloud, lowering the capacity because I said initially, all the customers in the cloud are thinking of us as a file system, a multi-protocol storage offering. and global namespace. I'm not seeing a lot of interest from the cloud customers in doing the database, for example. Even though it's a huge part of our value proposition, I just don't think the early on customers are going to be going for it. a lot of customers saying, "Well, here's how we're calculating the price." When you grow, you have to take into account your vCPUs and your capacity, even though you're not using the vCPUs. Because the instances that we are running on today is massively over-provisioned vCPUs and memory. We're probably, in best case scenario, using 30% of the cores or 40% of the cores, and then saying, "Well, deactivate the cores?" No. It might not be suitable, but if we go down... the path of building something that makes sense for the cloud and it's easily understandable for vast on-prem customers, how we're doing it, how we're doing it slightly different in the cloud, I don't think we're ever going to get to 100% correlation between on-premise software and on-premise TCO and cloud.

[00:44:15.84]  Jason ValleryTCO with the model that they are building. Yeah, until we have purposeful hardware and we're a

[00:44:21.90]   RemoteFirst party server. Yeah, yes. If you have that, then yeah, then it becomes easy. Yeah, yeah. But

[00:44:29.39]  Jason ValleryThen I think you go to a entirely different SAS model anyway, so you still need a different unit of measure. Um, well, I guess my ask... I mean, I'm all in on the idea, obviously. I think my ask back has helped me get our leadership bought in. You know, use Kaufbauer to go influence Renan and Jeff when you're in those conversations and make sure that you are advocating the same point I am so that I don't look like a squeaky wheel about it. But I'll keep pushing.

[00:44:54.67]   Remote- No, no, like I have already spoken to Renan about that we are working and I asked you specifically to figure out a model that works for the cloud because he is, Ranan is actually worried about that we are pricing ourselves out of the competition in the cloud, which is a real concern, and I don't think the new pricing model, it's actually going to skew it. it in the wrong direction, the way Jeff Tomer and Eric Wolf are thinking about it. But we have this meeting on Monday, right? It's Monday. When was it? We had the pricing meeting on Monday, right?

[00:45:39.24]  Jason ValleryOh, the one we had last Monday, I think it was.

[00:45:43.73]   RemoteNo, this Monday.

[00:45:45.86]  Jason ValleryWe're both on it 9 9 30. I don't know if I'm gonna be I'm flying to Florida Right Yeah, I think I Oh, I will be probably just about to board a plane. I'll board it. I'll join it, but I'll be just about boarded

[00:46:08.36]   RemoteI mean, yeah, I'll throw all the support and if you need any other support I'm here for you buddy because I think you're doing an amazing job and in all honesty if we do this correctly with both Google and Azure. we might be able to create a competitive bidding war on vast as an acquisition

[00:46:39.10]  Jason ValleryTarget yes yeah but I wonder like I mean playing business you know scheme theory and strategy and how this all unfolds what's the better outcome for shareholders vast is it Is it a bidding war or is it big lockup contracts with all of them?

[00:46:58.61]   RemoteBig lockup contracts with all of them is the best for the shareholders, and for us, I would say, and being able to go IPO on that, on those grounds is absolutely insane. be way more beneficial. I'm just saying like, uh, it, I wouldn't be surprised if that scenario would rise. Hey, like, Hey, like let's say we get, you came at MIA and scale, go, uh, over the nebulous part of Microsoft, Apollo, everything, you're looking at like somewhere between $7 and $10 billion of revenue. That would always be way better than them actually acquiring us. I just feel like they would go like, "Wait a minute." this doesn't make any financial sense for us, we're buying you for a hundred billion dollars and get a seven-year ROI on that acquisition, instead of paying you for life, you know, on it.

[00:48:20.17]  Jason ValleryI agree, and you and I both know that. I mean, I've... at least with Microsoft, they don't have a storage solution that they can engineer in any meaningful time frame. So, you know, if they're gonna go through a bunch of headcount at this problem and say, go replicate the success fast as a first party thing, that's a, you know, even if they put their best people on it in a three to five year project and they can't wait.

[00:48:41.72]   Remote- No, absolutely, then they've missed the boat.

[00:48:44.58]  Jason Vallery- Yeah.

[00:48:45.90]   RemoteSo absolutely continue down the path that you are on and really help us on the sort of larger projects, but ultimately you're the only PM that I got.

[00:49:08.46]  Jason ValleryTrying to figure this out. I've got more time with him today Obviously, I didn't sign up to be an IC. So hopefully we can make more more traction there I got a bounce. Let's make sure we get dinner next week. I come in on Monday and I'm there through Wednesday So either Monday Tuesday or Wednesday night, let's find a slot to get together or during the day

[00:49:26.75]   RemoteAbsolutely My talk is on Tuesday around noon, I think, and then I fly out to New York for the Two Sigma meeting.

[00:49:41.04]  Jason ValleryOn Wednesday or on Tuesday? On Wednesday, yeah.

[00:49:43.00]   RemoteI fly out like really early.

[00:49:44.38]  Jason ValleryTuesday? Is that possible? Yeah. Tuesday and Monday.

[00:49:48.05]   RemoteI mean, I'm going to try to be... there and take some of the meetings where the team's at.

[00:49:57.20]  Jason Vallery- Okay.

[00:49:58.04]   Remote- So we'll definitely go for dinner and some one-on-one time. How long is Jack gonna be here? Is he gonna be at the Tech Summit or?

[00:50:07.98]  Jason Vallery- Definitely there. I don't know which days and how long. He's giving us, he has a talk as well. So I'm not sure. - Okay, I got to pass down the meeting. Talk soon, bye.

[00:50:18.55]   Remote- Okay.


