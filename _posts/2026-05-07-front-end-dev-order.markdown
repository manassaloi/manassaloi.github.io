---
layout: post
title:  "Front end development process"
---

My front-end development process for a new product:
1. Proven execution
2. Product feel
3. User-led iteration and invention

Proven Execution is the baseline.
Everything here should be treated as non-negotiable.

1.1 Coverage: All required screens, flows, and components should exist. First the designer creates them, then the front-end dev executes according to design. Considering most developers are one-shotting the first cut, I am less focused on pixel perfect design at this stage, but making sure all the components and flows exist. You can think of this stage as getting the static components in code.

1.2 Functionality: All components should work as expected. This means integrating with the backend API. Making sure the happy flow works. Buttons, inputs, filters, tabs, trading actions, navigation, and state changes should behave correctly. The product should not just look clickable. It should work.

1.3 Correctness: Now you make sure that if the UI matches the designs. Make it pixel perfect. This means layout, spacing, typography, colors, component sizing, visual hierarchy, responsiveness, and designer feedback.

1.4 All States, Edge Cases, and Errors: Every screen should handle real-world conditions. This includes loading, empty, error, success, disabled, pending, partial data, offline, and permission states. The product should behave well when things go wrong.

You can decide to pick 1.4 before 1.3 too.

1.5 Scalability: The front end should be built in a way that supports future versions. Components should be reusable. Layouts should handle more content.

We should not build the first version in a way that makes the second version harder.

With this we complete the first stage.

Product Feel: Once the known product works, we improve how it feels.

2.1 Performance: The product should feel fast. Screens should load quickly. Interactions should respond immediately. Scroll should be smooth.

2.2 Delight: Delight should support the product, not decorate it. Motion, transitions, hover states, confirmations, price movement cues, and micro-interactions should make the product feel clearer, faster, and more satisfying. If motion slows the user down or distracts from the action, cut it.

2.3 Information architecture and copy: The hierarchy should be clear. The copy should be simple. The actions should be obvious. The mobile experience should feel native. A normal consumer should understand what to do without being trained.

2.4 Brand and Product Refinement: Branding is not just the landing page. Once the design system, part of the branding exercise, is ready, it should make everything cohesive. This includes typography, font sizes, colors, spacing, icons, illustrations, motion, charts, copy, empty states, and product personality.  I am keeping Brand and Product refinement for later because a lot of companies would not wait for branding before starting on the product development.

2.5 Gamification: Best products feel like games.

Second stage is complete.

User led invention and iteration: As you are closer to launch, you will learn a lot from alpha users. You will do UTs.  You should watch where users get confused, where they drop off, what they click, what they ignore, what they misunderstand, and what they try to do that we did not design for.

User feedback should improve the product. User behavior matters more than internal opinions.

This stage is also where we solve what others have not solved. But we should not start here.

Most teams have all of these things in their heads. What they get wrong is the order. They start with new (invention) because it's exciting. They debate brand before the product works. They skip edge cases because users haven't complained yet. They add motion while basic flows are broken.

First, we build the known product. Then we make it better. Then we invent.

Related read: [Proven, better, new](https://manassaloi.com/2026/05/05/proven-better-new.html).
