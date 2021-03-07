---
layout: post
title:  "PM'ing at a big company"
---

PM'ing at bigcos/late stage startups is mostly about risk mitigation. Let's talk about risks you will face and how to mitigate them.

1. **Team risk:** Not having a vision for your team and not prioritizing projects based on that vision.
  - [Without a charter and OKRs](https://manassaloi.com/2020/12/09/how-to-be-strategic.html), your team will have an existential crisis every quarter and your execs will wonder if you are capable of thinking long term.

2. **Prioritisation risk:** Not prioritizing the right projects based on the company/team goals and then having projects scrapped midway.
  - Ideally, OKRs should improve your North star. Initiatives/projects should map to specific KRs for the quarterly OKRs you have chosen and got approved by management. If you think planning OKRs is a bit too much for your company stage, then identify a few key themes and focus on those.
  - Have a backlog of projects is important. Long term prioritization exercise can happen once per quarter or the semester.
  - I generally have enough projects in my backlog, irrespective of whether they get picked this quarter or next year. Not having enough projects in your backlog means you are too focussed on implementation details and don't have an eye for the future. Your developers should not have to sit idle after a big project because you did not plan properly for the next few months.
  - Without a proper backlog, you will be seen as someone who is always in a reactive mode instead of thinking ahead.
  - Charter -> Vision -> OKRs/ Themes -> Inititives tied to KRs.
  - Initiatives/projects can be picked from your backlog.
  - Know what is top in the mind of management and understand [their decision-making process](https://danco.substack.com/p/six-lessons-from-six-months-at-shopify). Links to all of the documents mentioned above are [here](https://manassaloi.com/2020/03/23/running-product-team.html).

3. **Scoping risk:** Do you continuously get into arguments with your designers because you change scope midway through your projects? Do you find it difficult to say No to stakeholders when they come and tell you to add X more features to a product you are building? If your answer is an emphatic yes, then let's go through these 2 frameworks that might help.
  - [Concentric circles of alignment:](https://manassaloi.com/2021/02/02/internal-external.html) Think of alignment when it comes to scope as well as stakeholders as concentric circles. Alignment happens at multiple levels. This means that all projects go through the following stages. WHY -> WHAT -> HOW. Don't move to the next without closing the inside circle. Most projects die of scope creep because WHY is not defined well. Scope of a project = What needs to be done to meet the success metric.
  - [Internal then external:](https://manassaloi.com/2021/02/02/internal-external.html) First, reach internal alignment then align externally. Here is how the alignment process works in my team: PM works on the first draft. Creates a narrative. Focuses on WHY -> Aligns me -> Once we align then we align our Head of Product (HOP) -> Then we align more stakeholders. We follow an unique checklist for each project because all products are different when it comes to scope and complexity. But we never forget internal then external. Even here you can see that the alignment follows concentric circles. WHY is closed first -> Scoping happens post that -> Implementation details get figured out last. We align relevant stakeholders at each stage. We will arrive on a tech spec very rarely without the devs giving detailed feedback on the spec and designs first. Very rarely will we start high fidelity wireframes without closing the WHY of the project first. This way random scope creep does not happen and the scope is closely aligned with the success metric.
  - This whole elaborate practice is to adhere to a simple principle I have followed all my life: DO NOT WASTE PEOPLES' TIME. So unless I am sure about the WHY and the narrative of a project, I will work with the PM to perfect it. Unless I know my HOP has agreed to the project, and I can defend the WHY behind it, I will almost never engage our designers' time.
  - For complex big bet projects that might take more than a couple of months effort, I will write a separate pitch doc before working on the spec.

4. **Stakeholder risk** If you are working on a project that involves external stakeholders make sure you OVERCOMMUNICATE. Assume good intention always, but always know that your goals might not be aligned with their priorities. Read [How to write and communicate better](https://manassaloi.com/2020/05/19/master-communication-writing.html).


5. **Execution risk:** The last risk is the execution risk for a project. You should be able to figure out where something might go wrong for a project to either not meet the delivery deadline or the goal. Keep asking yourself this question and escalate risks early and course correct if needed.
  - Say, you have a feature coming up that can be gamed by users to learn more referral bonus. In this case align your Fraud and Risk early.
  - You are taking a new service to Production which will expose new API endpoints? Have you discussed it with the Security team?
  - Your feature delivery is dependent on another team. They need to make changes to their API contract so that you can consume more fields. Have you got a written commitment from them? Do you know who is the PIC working on the change? Do you have a delivery deadline?
  - To avoid missing things, I make sure that there is an open item list to track all the dependencies. To avoid edge cases, I make sure we have covered all the states in a design spec and have an acceptance critaria list ready. To cover all tech changes, we write a tech spec. We also get stakeholders from Design and Security to give sign offs on big projects. Links to all of these are [here](https://manassaloi.com/2020/03/23/running-product-team.html).

  **Note:** I talked about the risks you face as PM at a big company, not about product risks. If you want to read about the later, then go to this post: [The Four Big Risks by Marty Cagan](https://svpg.com/four-big-risks/).

  Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
