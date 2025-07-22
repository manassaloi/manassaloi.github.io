---
layout: post
title:  "Your driver has arrived. What's next?"

---
I wrote a thread recently on the Driver has Arrived Notification of Uber and how Uber could have designed it better. Turning it into a blogpost (with some minor edits) because I am trying to hack my writing goals for this year.

/threadstarts

{% include webp-image.html img="uber_arrived.png" alt="Uber driver arrived" %}


**When you design you have to think about jobs for each component of your UI.**

Example. You send a driver has arrived notification. What is the most important info you can put there?

Is it the status of the trip?
Is it the driver name?
Is it the location?
Is it the vehicle info?
If you think about it, the most important info is the status of the trip. Because you just keep looking at the heading of the persistent notification for any change in the trip status

**So Information Architecture wise it makes total sense.**

**What is the 2nd most important info?**

Is it the name of the driver? TBH It is not helpful for identification of the vehicle. Nor verification of the driver.

Model of the vehicle? It helps for 4W. But for Auto it is just Bajaj Everytime. So it is redundant info.

So what is it?

**It is the license plate info.** The notification 's job is to let you know that the vehicle has arrived at your location and also for you to identify the vehicle.

For both Car and Auto it is the most important info after trip status. **IT SHOULD NOT GET TRIMMED UNDER ANY CIRCUMSTANCE.**

Otherwise the user would have to open the app to get the remaining info!

For car, model type and color can add extra info.

For Autos license plate is the only relevant and trust worthy info.

Okay. UX gyaan khatam.

**/threadends**
