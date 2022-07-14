---
layout: post
title:  "Gojek Shamelist & learnings"
---

I generally share this only once I leave a company. This time I am making an exception. With my company going public, I can't share details around specific features or metrics anyway. Also note that most of these are from my first year working as an IC.

### Shamelist

- I was hired to lead a new product charter: [charter X]. In the first month: I worked on the designs (as I had no dedicated designer), created the dev org (as developers reported to me in the absence of a TL), and even came up with architecture diagrams and API design. What I did not do? Validate if the product roadmap even made sense. When I joined Gojek the strategy for the BU was already frozen, and so was the roadmap. I should have done my independent research instead of just relying on existing stakeholders' opinions.

- Went to meetings with various stakeholders and tried to convince them to support the new BU without asking whether the new BU had exec buyin. Always think about the machinery.

- I was extremely blunt with my views on the quality of the team and the product direction. [After a reorg that happened 2 months post my joining, and after we shipped the initial MVP, I decided to move to Transport as the 3rd PM in the org].

- Missed involving <stakeholder X> in the [feature X] discussions from the very beginning. This meant we needed more meetings later on to get their buyin.

- I was given the ownership of the entire [X roadmap] and asked to ship half a dozen features within 2 months of joining the Transport team. I could have pushed back, but I said yes to everything.

- Missed few edge cases for [feature X]. To fix this, started involving designers even earlier in the process. Eventually created a checklist of edge cases, fallback, and error states that we went through for each feature release.

- Missed a few fallback scenarios in the [feature X] flow.  

- Did not make the feature toggle for [feature X] configurable based on version number.

- Could have shipped a better [feature X] web UI.

- Did not follow up with <team X> enough to close <bug X>.

- Found one bug in the [feature X] flow the day before the big launch of our [X roadmap].

- Sent a stinker email to <stakeholder X> with a lot of senior people cc'ed. I was upset at the person committing to a feature and then going back on their word. But I missed the first rule of corporate politics: I tried to argue with a person who was like 3 levels above me in the ladder and was at the company for a far longer period while I was a newbie. [I should have known that it would not end well. Over time I learned to control my emotions at work.]

- Missed an edge case on [feature X] that would have let drivers to game the system. Thankfully fixed it on time. Started involving fraud teams going forward and working closely with them on potential fraud scenarios.

- Iterated on [feature X] version 2 design after development started. Should have pushed back strongly and only done it in version 3.

- Lost my cool during discussion with an Android dev on whether the app should crash if the backend does not honor the API contract. I should have explained my POV better. If you are leading a team, you can't afford to be seen as someone who gets upset during meetings.

- For the first 6 months I was very focused on setting the bar high for the team. This got interpreted by a few team members as me not being happy with anything.

- Missed capturing a few launch decisions on paper. Learned never to rely on implicit verbal sign offs.

- Someone committing to something does not mean them committing to the delivery of that thing by a set date. Not realising this led to a major escalation.

- Did not escalate design bandwidth constraints for a major feature launch.

- Missed backward compatibility for a feature.

- Missed edge cases around moving to a new activity card instead of dialog card for the [feature X] flow. Even though this can be seen as a miss by the tech lead, it was also my responsibility to go through the flows carefully and highlight gaps even in the tech spec. Yes, another example of extreme ownership that I want not just myself, but my team to follow.

- Should have caught a case around retry failing in case of back button press for [feature X] flow.

- We did not use to highlight what copy we hardcoded vs what was coming from the backend vs what copy could be experimented upon because it was coming from the experimentation platform. We started capturing this in the tech spec much later.

- Missed putting a flat on a particupar API response that led to modded apps using <feature X>.

- Did not align all the stakeholders on the goal behind the [feature X] feature.

- Every feature should have one single DRI, even if multiple teams are working on it. Not making it clear led to a lot of last minute blame game when we released <feature X>. [I became more strict about ownership of services as well as features going forward. No one owning the overall delivery means no one being accountable.]

- Did not get all decisions taken on the call masking feature captured in the DACI section of the product spec.

- Tied to do a redesign, moved to a new design system, rearchitectured the front end codebase and also released multiple features - all at the same time. [Dumb dumb idea.]

- Roll out should have been planned much better for the redesign project.

- Dropped the ball on a decision on how the new address pill would look. [Should have pushed the team to think through the edge cases more.]

-  <Feature X> project looked fine on the surface but lacked the rigor I wanted in my projects.

-  <Feature X> project needed more data before kick off with <stakeholder X>. [Always always over prepare before big meetings.]

- Should have created a dedicated spec on the Address pill design. The component was not well thought out. The issue was that we hid the complexity of this feature under the mega project that was Aristos (the big redesign of the entire transport flow).

- Should have pushed for UT much earlier and not waited till the Alpha.

- Should have avoided debating with multiple people on design decisions in the public slack channel for the project. It made it seem like we were not clear on the design direction. [Started debating and closing key decisions on private channels instead].

- Missed adding a couple of analytics events for [feature X].

- Should have pushed <stakehoder X> more on decisions taken on [project X].

- If a project goes on for a long period, people lose focus and productivity drops. [Always go for smaller milestones].

- Did not have weekly BI and Research syncups in the first 6 months.

- Was not proactive with post launch monitoring and updates. This took a long time to fix and something I teach PMs in my team from day 1.

- Did not send enough updates for <feature X> project. This was a big miss considering the number of stakeholders involved.

- Should have reacted early to the covid situation and planned nonserveseable flows much earlier.

- Paused <feature X> project after just 2 milestones. Should have highlighted the impact more and pushed for more iterations.

- Should have identified dependencies on [team X] for [feature X] earlier.  

- Missed adding the DACI table for [project X].

- Took too long to close the milestones for [project X].

- Took delivery of a few projects too seriously and ended up burning out the team.

- Alignment on timeline for [project X] was not closed on time.

- Did not get commitment from other teams on [project X] on time.

- Missed planning the delivery of design assets for [project X]. Knowing the illustrations are provided by the central team and they don't work dedicatedly with my team, I should have kept a buffer and also pushed much more to get the assets on time.

- Did not work with [team X] on the testing plan and acceptance criteria for their side of the work. Even if it was work picked up by a different team, as the DRI of the project I should have made sure that these things were picked up by their QA team.

- Should have got [team X] added as an external stakeholder and collaborated with them far more. [A team is either internal or external.] If external then follow up and set SLAs like an external team].

- Should have pushed [team X] more on [project X].

- Missed adding notifications to the scope for [project X].

- Did not create all Asana cards for [feature X]. Assumed the other team would do the work because it was handed over to them.

- There were two separate source of truth for scope of [project X]. [Always have the product spec as the source of truth].

- Should have involved Tax, Fraud and  Government relations teams on [project X].

- Should have created the migration plan for [project X].

- Missed deloyment a few config updates during roll out of [project X].

- Should have asked for stricter timeline for [issue X] from [team X].

- Security team should have been involved much earlier for [project X].

- Missed fallback for default icons for [project X] launch

- Did not create a dedicated war room for launch of [feature X]. It was a big launch and we needed all the stakeholders together in a room in case something went wrong.

- Missed kick off with with QA and regional teams for [feature X].

- Did not have principles to decide the structure and milestones as well as work allocation for [project X].

- Did not push [PM X] in my team to work on the [project X] plan earlier.

- Internal then external was not followed for [project X].

- Should have posted more insights on [channel X] on Slack.

### Learnings

1. Create influence.
2. Create your own identity. What do you want your team/yourself to be known as? Data driven / super technical/ user experience experts?
3. Send regular updates to stakeholders.
4. More face time with leadership.
5. Always work in the mothership and not satellite office.
6. Tailor content based on who is reading.
7. Highlight wins as well as issues in real time.
8. Regular 1-1s with manager. The 1-1 is for you. Don't skip them.
9. Sometime speaking less is the way.
10. Be crisp.
11. Don't volunteer too much info about your career moves.
12. Do the fix then do the RCA.
13. Know the agenda of stakeholders.
14. You don't update leadership, every call with them is actually a sales call.
15. You can't fight all battles. So pick your battles wisely.

Related:
  - [Organizational learnings](https://manassaloi.com/2021/12/08/master-organizational-learnings.html)
  - [Build Measure Learn (for you)](https://manassaloi.com/2019/11/24/build-measure-learn.html)
