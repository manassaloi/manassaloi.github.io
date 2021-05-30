---
layout: post
title:  "Lean from the Trenches - Henrik Kniberg"
tags: booksummaries
categories: booksummaries


---

**This blogpost is not an exhaustive summary of the book. Just contains the notes I took**  

Set goals. At the beginning of every Sprint ask "Do you believe we will reach this goal?"

What does done means?
1. Automated acceptance test passed
2. Regression test(backward compatibility test done)
3. Demonstration to QA
4. Add comments to commit
5. Test on dev environment
6. Merge code

Always have dev stories and user stories

Have a bugs list.
If there is a blocker address immediately. Don't wait for the next planning meeting

If there is a new bug, check if they are in top 30 bugs you want to tackle. If not then don't put in the Bugs list

Try to tackle: Next 10 user stories, 5 tech stories and 5 top bugs

Set up a RCA meeting for recurring bugs in the system

Processes should be discovered and not designed forcefully

Have story points and cycle time (time to release features)

Draw the branches: individual, team, trunk
If code unit tested move to team. Need not be complete. Complete feature move to trunk
System test branch is another branch where system test (if all features are working together) is done.
Automated regression testing is done  on team branch before merging to trunk
On system branch mostly do manual testing + specific scenario testing
If there is a bug on system branch send a hotfix to system branch and merge the fix down to trunk

List out test cases
Sort test cases by risk, how expensive to do manually and by auto
Sort in terms of priority
Automate a few. Then iterate

Solve problems not symptoms. In case of fire don't open window, get smoke out. Find out what caused the fire and install alarms

Figure out consequences of a problem. Check your goal. See if problem conflicts with goal. What is actually the real problem. For this go upward

To figure out root go down ward. Use 5 why's.
