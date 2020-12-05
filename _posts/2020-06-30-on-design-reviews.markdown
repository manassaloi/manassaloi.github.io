---
layout: post
title:  "On design reviews"

---

- Don't look at UI components in isolation.
- As a PM, I care less about a new search box's UI and its functionalities than how the search experience will fit in the customer journey.
- Say you are a designer/PM designing the search experience for a dashboard. Focus less on what features the search box will have, be it autocomplete, suggestions, full text search vs partial etc, and more on why and how the search will be used by the user. Understand what job the user is trying to accomplish while using search.
- MVP design is not about features. It is about what job stories you want to tackle as part of the v1.
- Have an opinion; this is true for both the presenter and the reviewer. Reviews should not be able superficial compliments and backslapping. It should be about constructive feedback and how we can make the product even better.
- You want the user to perform a series of actions to complete a job they have hired your feature for. Don't hide your lack of opinion by suggesting 3 random alternatives to the reviewer or asking the PM to run an A/B test to figure out the best UI.

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
  4. Will they have list of usernames in a file? Will the list shared with them be or random or sorted alphabetically?
  5. How often will they have to do this delete task?

Only once you do this exercise you will realise that you are not designing a search or multi-select UI in isolation but designing the experience of how an actual admin will delete users from a group.

- Design the whole experience based on actual jobs that the admin has to perform in their job than hypothetical scenarios you have cooked up. 
- If you are the reviewer ask why you need a particular UI element. Are the UI components there because the designer or PM has seen it somewhere and felt a search experience should have them or are they there because they are needed to complete a real job by the user.
- Avoid design through committee. Don't let stakeholders come and add/remove UI components just because they wanted to add some value.
- Design for the happy flow but keep thinking where things might break. Don't over design the v1 trying to cover all edge cases. Some of them can be fixed post the MVP.
- Test with real users. Unless you have feedback from actual users most debates are mental masturbation. 

Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
