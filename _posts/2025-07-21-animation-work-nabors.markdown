---
layout: post
title:  "Animation at Work - Rachel Nabors"
tags: booksummaries
categories: booksummaries

---

**Note:** While reading a book whenever I come across something interesting, I highlight it on my Kindle. Later I turn those highlights into a blogpost. It is not a complete summary of the book. These are my notes which I intend to go back to later. Let's start!

Transitions take users from place to place in the information
space, or transition them out of one task into another. These
tend to have massive impacts on the content on the page,
replacing large portions of information.

Supplements bring information on or off the page, but don't
change the user's "location" or task. They generally add or
update bits of additional content on the page.

Feedback indicates causation between two or more events,
often used to connect a user's interaction with the interface's
reaction.

Demonstrations explain how something works or expose its
details by showing instead of telling.

Decorations do not convey new information and are
purely aesthetic.

All of these patterns (with the exception of maybe the
decorative ones) do something important: they supply context
in a context-poor environment.

The world around us is alive with information in the form
of noises, smells, and movements, and it responds when we
interact with it. The web is rich with information, but it's not
inherently rich with context and feedback. Animation can and
should help with that, from providing feedback about the status
of your tax return submission to attracting your attention to a
crucial update. That is animation's true purpose: to add context.

Then, to help quantify that context, ask the follow-
ing questions:
- Does it show the user where information came from or went to?
- Does it indicate progress?
- Does it move the user through an information space?
- Does it reinforce physics or branding?
- Does it explain something faster than words or a video could?

The more boxes an animation ticks and patterns it fulfills,
the more likely it is to provide a net gain for your users, and
the more justifiable it becomes. This is how you know it's not
just a nice-to-have.

Easing describes the rate at which something changes over a
period time. When applied to motion, easing can describe an
element's acceleration or deceleration. The term has its roots in
traditional studio animation, where it was called "cushioning"
or even "slowing."

In CSS, easings are called timing functions and are described in
a few ways. Every browser understands the default CSS timing
function keywords:
- **ease-in** (acceleration)
- **ease-out** (deceleration)
- **ease-in-out** (speed up then slow down)
- **linear** (constant rate of change)

Each of these easings works best in different situations:

**Acceleration** is good for system-initiated animations, like
a pop-up asking users to sign up for a newsletter. If this
unannounced animation starts slowly, it's less likely to startle
users, even if it takes the same amount of time as an anima-
tion with an ease-in.

**Deceleration** starts quickly and gives a UI a snappy, respon-
sive feeling. It's great for user-initiated interactions, like
button clicks and page transitions.

**Speeding up then slowing down** is useful for interaction
models when moving an element toward another.

**A constant rate of change** works best for fades and color
changes, which can look jarring with a steep curve.

**Bounces** can add extra animacy to draw attention to elements
or to add an air of "fun" to the brand.

The average time it takes people to react to visual change is
about 215 ms. Thus, it makes sense that 200-300 ms is a recurring sweet spot among game and interaction developers. Dura-
tions in this range tend to be the workhorses in an interface.

If something is moving across a screen, it will need more
time than something providing immediate feedback, like a color
change on hover. The eye is quite sensitive to color changes
when it's looking directly at the animation. For that reason, I've
found that color and opacity changes under the user's finger or
cursor can feel slow if they take more than 100 ms. But if you're
moving something across the page, 100 ms is too fast, and going
over 300 ms may be necessary.

Keyword duration:
- **Immediate** 100 ms - For fades and color-based animations
- **Fast** 300 ms - For interacting with elements that need to feel responsive and peppy
- **Slower** 400 ms - For moving elements on the page
- **Deliberate** 700 ms - For large movements across the screen or self-contained demonstrations

This timing scale is inspired by the Fibonacci sequence: 100 + 300 = 400, 300 + 400
= 700.

Referring to a chart like this will, once again, help standardize animations across a
site.

Properties describe what is changing over time. Color and
opacity changes convey fades. Changes in location convey
motion. Changes in scale or shape convey deformation and
transformation.

There is nothing so satisfying as hearing a beta tester remark,
"Oh, that's delightful!" upon seeing your first UI animations.
However, this could be a red flag. It means that they have
noticed an animation, and that means they are spending cogni-
tive power on it—the exact opposite of what animations should
do. There are some circumstances, such as demonstrative ani-
mations, where we want people to really notice the action. But
for the majority of microinteractions, we don't want animations
to distract users.

I like to think of animation as the waitstaff at a fancy restau-
rant. You come to eat and drink, and to have good conversation
with your companions. A good server facilitates this. No sooner
have you set your fork down than your dinner plate seemingly
disappears and is replaced with a dessert dish.

When testing with users, pay attention to when they notice
animation and when they don't. We know we're reducing their
cognitive load when they don't notice something.
