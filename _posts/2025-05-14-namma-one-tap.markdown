---
layout: post
title:  "Namma's one click feature"
---

When I posted my thoughts on Zepto's Swap and Save feature, a few people felt I was overanalyzing a simple feature to drive up ad spend. Some even DM'd to tell me that.

But I believe that if you want to get better at building products, you need to think holistically about how a simple feature can evolve into a platform feature and support multiple use cases. That's exactly what I tried to do with Zepto.

There's another example: the one click booking on Namma's Home. This one click feature is a staple across many products. We had it at Gojek, there's something similar in Grab, and I think Lyft has it too, though I'm not entirely sure.

The point is, features like this are incredibly useful. When you design a single component that can adapt and serve different needs, you're able to support multiple use cases without taking up more screen space.

Let's talk about the one click Booking feature on Namma:

How much space do you want to give the feature on homepage?

What info on this card will drive conversion?
- Destination
- Date
- Pickup date
- Service type
- Payment method and price
- Coupon if applicable

Trade-off between:
- Conversion on this card
- Intermediate screen to verify all info (info that couldn't be incorporated in this card)
- Cancellation of booking because some assumed input was wrong. This could happen later

Now this same card can have different info and serve different business needs.
1. Namma can predict with high confidence how you are going and what service type you will take. This is the shortcut one click booking. For the power user.
2. Continue where you left *(very common feature in ecom)*. Surprisingly most ride hailing companies don't do it. Extremely high ROI. So many times you cancel because of long ETA. Try competitors. Come back and have to go through the same flows again. This one click experience is far better.
3. Return booking for office commuters. One tap to return home in the evening. Works for cases where you can predict non commute return trips too.
4. One tap booking for trips you can predict because you have personal info. Let's say you have access to the user's calendar.
5. Take users to popular places (impossible to do, probably doesn't work, but when we can predict popular events — let's say some cricket match in a stadium).

Basically, one platform feature that can support multiple uses and can dynamically transform to show the relevant info to drive up conversion.

I believe we were the only player to build a truly delightful one click feature that scaled (though I might be biased). Our competitors had versions like “Continue where you left off,” and another had “Return Trip.” From what I’ve heard, Uber is now finally building its own One Tap.

We were obsessed with handling multiple use cases, and our implementation of one click was delightful. I’ve heard from many users who said they chose our product specifically because the booking experience was so seamless, all thanks to one click.
