---
layout: post
title:  "A few disconnected thoughts on design reviews"

---

1. Don't like to look at UI components in isolation. Watching a new search box's UI and its functionalities demo'ed by the designer is not helpful for me unless I understand how the search experience will fit in the customer journey.
As a designer/PM designing a search experience for a dashboard, focus less on what features the search box will have such as autocomplete, suggestions etc, and more on why and how the search will be used and what job the user is trying to do while using search.

MVP design is not about features. It is about what job stories you will tackle as part of v1.

2. Have an opinion; this is true for both the presenter and the reviewer.

As a PM or a designer you want the user to perform a series of actions to complete a job they have hired your feature for. Don't hide your lack of opinion by suggesting 3 random alternatives to the reviewer or asking the PM to run an A/B test to figure out the best UI.

Let's take an actual example. Say you are the designer for Google Groups product and you are designing the experience of removing users from a group. Removing users essentially involves two tasks: 
  1. Finding the users.
  2. Removing them.
Finding the users can be done by
  1. Exposing all the users of the group upfront in a tabular format.
  2. A search box in case there are hundreds of users.
  3. Some sort of CSV upload feature if the admin has to remove hundreds/thousands and can't search and select each user manually.
Removal can be done by
  1. Searching and removing each individual users.
  2. Using a delete button next to each user's name.
  3. Multi-selecting users and then deleting.
  4. Mass delete using CSV.

Instead of stuffing all of these options in the UI and going for a features first approach, first ask:

  1. Why would an admin want to remove users in the first place?
  2. In a standard scenario will they remove a single user or multiple?
  3. Is there any realistic scenario where they would need to remove thousands of users from a group?
  4. Will they have the name of the list of users in a file? Will the list shared with them be or random or sorted alphabetically?
  5. How often will they have to do this delete task?

Only after you do this exercise you will know that you are not designing search or multi-select UI in isolation but designing the journey of how an admin will delete users from a group.

3. Design the whole experience based on actual jobs that the admin has to perform than hypothetical scenarios. 

4. If you are the reviewer, keep asking why you need a particular UI element. Has the UI components been fitted just because that is the norm? Because the designer or PM has seen it somewhere or are they there because they are actually needed to perform a real job by the user.

5. Avoid design through committee. Don't let stakeholders come and add UI components just because they did not have time to go through the real job stories and felt "Search should be there."

6. Design for the happy flow but keep thinking where things might break. Don't overdesign the v1 trying to cover all edge cases though. 

7. Test with real users. Unless you have feedback from actual users most debates are mental masturbation. 

Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
