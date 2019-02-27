---
layout: post
title:  "Product Manager Talk: “Help! Our numbers went down yesterday"

---


As a Product Manager the first thing you should do every morning is look at yesterday’s data. Most of the times there won’t be any dramatic change in your metrics. But if you wake up one fine morning to find a 20% drop in any of your KPIs, you should know why. You won’t appreciate your CEO sending you a Stinker mail cc’ing half of the company, do you?

In this post I will teach you how to do a **RCA** (Root cause analysis). We used to track a lot of KPIs at Craftsvilla, but our north start metric was **Conversion** (Transactions/DAU).

Say conversation hovered around X and due to some reason it dropped by 20% the day before. I would notice the drop in my daily morning metrics email and use the following process to figure out what went wrong:

1. First thing to check — **If there was any seasonal effect**. For most B2C businesses usage peaks during weekend as majority users are at home. While for B2B SaaS companies there is a drop as employees are not at work. It is stupid to compare Sunday’s data with Monday and feel bad if there was a drop in conversion. Or comparing numbers during Diwali week with the week after.

1. In absence of any seasonal effect the next step is to check **if anything went wrong at our end.**

Was there any server downtime?
Were the API response times same as usual? For this I would look at New Relic* data and cross check with my Dev Lead.
Did any new build go out yesterday?
I would open Crashlytics* to see crash rate and if there was any spike in it

3. **What does yesterday’s hourly data say**? Checking this report is always the easiest way to confirm if something broke.

Example: Between 2PM to 5PM there were no transactions recorded. It means something happened during that period which let to overall conversion drop.

4. If I am convinced there was no seasonal effect as well as tech I would** check the conversion funnel next.**

For a typical e-com company the funnel looks something like this:
Home -> Category Page -> Product Detail Page -> Cart -> Success Page

Was there any significant drop in any part of the funnel?

5. Next step is to **check performance of all traffic sources and user segments**.

Mobile vs Desktop
New Users vs Old Users
Organic vs Paid
Did our SEO rank drop?
What about yesterday’s push notification? Did they go out on time. How did it perform compared to our historical push data
Perform same exercise for email campaigns

6. **How many new users transacted on the app yesterday?** There is a chance of some acquisition campaign performing poorly too. I would check the performance of each marketing campaign and if any particular one out of them led to the drop. Any mobile attribution platform like Tune/ Apsalar/Appsflyer gives you this data.

7. Lastly I would **look at all customer engagement channels**. Check Support tickets, Play Store reviews, Customer chat logs to see if the volume of complaints increased.

After doing all these steps there is a high chance I would find the root cause of the drop and fixed it.

In case you are not doing this exercise at your company here are some action items:

A) Get [New Relic up](https://newrelic.com/) and running. Also set up Server logs to catch errors
B) Have something like Pingdom to alert you of downtime instantly
C) Track funnels on [Google Analytics](https://analytics.google.com/analytics/web/)*
D) Track performance of Push notifications and Emails
E) Schedule daily metrics report along with hourly data
F) If you find any bug, ping your Developers on [Flock](https://flock.com) and report it!

Having data is not enough though. Make it a practice to look at data daily. Set half an hour in your daily schedule just to look at data.

* Or some similar service


Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
