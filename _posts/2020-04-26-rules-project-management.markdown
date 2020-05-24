---
layout: post
title:  "Project management rules"
image: 'https://manassaloi.com/assets/img/project_management_rules.png'
---

Following these rules will help you to manage a big project more effectively.

1. Every task should be assigned to a single directly responsible individual 
2. If a task is assigned to a team, then it is not assigned to anyone
3. All discussions regarding a project should happen in the relevant public channel on Slack. No private DMs allowed
4. A task should remain in 2 states:
 - Waiting for a timeline
 - Has a timeline
5. A task's status should be one of these:
 - Yet to be picked
 - In progress
 - Done
 - Delayed
 - At-Risk
6. Keeping multiple trackers does not lead to better project management. You just need a single source of truth, which can be even a google sheet. Keep it simple
7. Different stakeholders have different needs when it comes to status. Your CEO or VP won't have time to go into the details of each individual project. For them a simple card on asana with the status updated regularly would work. For active collaborators who need more context, make sure they can get more details in your spec. I always keep the status for a project at the top of [my spec](https://docs.google.com/document/d/1sUX-sm5qZ474PCQQUpvdi3lvvmWPluqHOyfXz3xKL2M/edit). If they need more granular info they can always scroll below and see details on completion of each milestone. Follow the pyramid principle for communication. For PM, EM, and devs working on the project, the micro details regarding individual stories are kept on Jira. Tools and their stakeholders:
 - Asana board with card regarding the project - CEO, VP
 - Status at the top of the spec - Different collaborators who might or might not be active collaborators
 - Detailed milestones and their completion %
 - Active collaborators for the project
 - Status on stories for each milestone on Jira - For devs and PM
 - Google sheet with every dev is working on - For your team 
8. Keep the trackers updated. I update my trackers on Monday (time-based) or when there is a big update, say something moved to Production (event-driven project management)
9. Escalate blockers early
10. Send regular status updates. I send out a weekly mail for each big project I am working on, where I highlight the following: status, % completion, details on milestones, blockers, if we are on track to meet the timeline. Everyone who is part of the project, or needs info about the project, gets cc'ed on this mail. This is the same MOM mail, which is resent as a status update mail
11. [Push > Pull](https://manassaloi.com/2020/04/21/push-pull.html)
12. Always highlight external dependencies on email. Slack is ephemeral. Messages get missed. The more important the info, the more critical the dependency, the more you need to make sure that the info is captured and communicated well
13. Avoid last-minute surprises. I have always hated last-minute bad news as a manager. And I make sure I avoid giving the same to my own boss. Keep giving frequent updates so that blockers are highlighted much before they delay your project
14. Delays are okay. Waking up one day before release and telling there are 10 things broken which will delay the release is not
15. If dependent items are not resolved, keep escalating till they are. If the dependent person is X, then escalate to their boss Y. If you don't get a response then escalate to Y's boss Z
16. Take extreme ownership of your work
17. Communicate early, and often. I don't worry about overcommunication. It is under communication which has always caused issues for people. Not the other
18. [Use documentation as cache](https://manassaloi.com/2020/04/19/documentation-cache.html)
19. [Steer into objections early](https://manassaloi.com/2020/02/22/steer-into-objection.html)
20. Follow the communication rules followed here: [Lessons from working at Gojek](https://manassaloi.com/2019/08/11/20-lessons-gojek.html)
21. Share information in the Slack Channel where the most number of people can gain context on an issue. If you have to tag people later on it is also easier
22. Don't create temporary private DMs with multiple people
23. [Measure your communication](https://manassaloi.com/2020/02/05/measuring-communication.html)
24. You don't need to wait for something to go live on Production to share an update. If the project is running ahead of schedule, even better. Share an update on the Slack channel praising your developer
25. Be quick to praise others. Take blame if things don't go as per the plan. Most managers do the opposite
26. When things don't go per plan, people turn every discussion into a blame gaming session. Keep reiterating that you are in this together, and you will do your best till the end
27. In case a project fails, make sure you highlight both the good and the bad. Most people focus only on the bad. Write a post-mortem report with learnings, and share the next steps
28. Pin all relevant documents on the Slack channel.
  - Pin spec as the master doc on the Slack channel
  - Asana card for the project
  - Jira epic
  - Roll out plan (when you are in the endgame)
29. If it is a FYI, then mark it as such. Don't let people assume that there is an action item for them
30. [Remember that owner's word weighs a ton](https://m.signalvnoise.com/the-owners-word-weighs-a-ton/)
31. For every project, no matter how you want to manage it, the following info should be easily accessible
  - what is the plan
  - what has been executed till now
  - what are the next steps
  - are we on track to meet the deadline
  - open items not closed till now
  - potential blockers
  - DRI to whom people should reach out if they have any query
32. Identify external stakeholders with whom you would need to coordinate for launch. Add them on Slack so that they have full context
33. If there are multiple items marked as P0, then you don't have a P0
34. [Welcome message for people joining a project channel](https://manassaloi.com/2020/03/06/welcome-on-slack.html)
35. All features shipped successfully are celebrated with ice-cream parties; mostly the PM's treat 

I am working on a master post of all principles and frameworks I use as a PM here: [PM frameworks](https://manassaloi.com/2020/03/05/pm-frameworks.html)

Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
