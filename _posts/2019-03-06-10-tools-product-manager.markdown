---
layout: post
title:  "10 Tools for every Mobile Product Manager"

---


A lot of people in the past have asked me for a list of tools we use here at CouponDunia for our product development and growth efforts. Here is a list of the same (I have divided the tools into categories) :

**Attribution and Analytics**

We use **[Tune](http://www.tune.com/)****(Earlier MAT)** **+ **Localytics** here for[ CouponDunia Apps](https://play.google.com/store/apps/details?id=in.coupondunia.androidapp&hl=en).

The other options are **Apsalar**, **AppsFlyer**, **Adjust** etc.

We use Localytics because Tune is not an authorized partner of Facebook. So to track facebook marketing campaigns and measure their ROI we selected Localytics. Also **Google Analytics** was pretty bad earlier and Localytics doubled up as an **Analytics** tool.

[**Localytics** ](http://www.localytics.com/welcome/)can also track Push Notification funnels if tied with Parse (A Push Notification tool).

You can export all the Localytics data to [**Redshift** ](https://aws.amazon.com/redshift/getting-started/)(Data warehouse) and you don’t need to set up another data pipeline for mobile at least. This is useful for long term reporting and we are building a solution like that here at CouponDunia.

For [**CashBoss** ](https://play.google.com/store/apps/details?id=in.coupondunia.cashboss&hl=en)we use **[Apsalar](https://apsalar.com/)**. It is a partner with Facebook and Twitter and also supports all major ad networks.

For Analytics we (CashBoss) prefer to use **Google Analytics** (GA). The mobile analytics version has become comparable to their Desktop version. GA is also getting its own complete attribution solution which will let people run install campaigns and measure them through GA directly without having to use another attribution solution.

For crashes and real time analysis we use **[Crashlytics](https://try.crashlytics.com/)**. Their Analytics Dashboard is cool and Developers get notifications in case of crashes.

For Facebook Attribution you need to ship their SDK with the App. And the numbers would be reflected in the Facebook dashboard as well as the panel of any partner Facebook has tied up with. Example Apsalar, Localytics. Facebook is also getting into attribution soon (like Google) and app developers will be able to run campaigns on other ad Networks using Facebook SDK and panel.

**Engagement and Retention (Ratings/Customer Support + Push Notifications + Email Marketing)**

These are the outbound marketing options which are available for an app today to get engagement on their apps.

I have already mentioned [**Apptentive** ](http://www.apptentive.com/)in my [blog post on how to improve app ratings](https://www.linkedin.com/pulse/your-definitive-guide-5-star-app-ratings-manas-j-saloi). It is a great tool for faster customer requests response and will help immensely in boosting your ratings.

We (Coupondunia Apps) use [Parse ](https://www.parse.com/)for sending push notifications. It helps you send targeted push notifications by segmenting users. Another advantage being the ability to send pushes to both Android as well as iOS from a single dashboard.

There are other tools too like [Urban Airship](https://www.urbanairship.com/). We are trying to slowly move towards building our own in house push notification solution for CouponDunia having tried it out for CashBoss already. Instead of sending requests to Parse like in case of CouponDunia we directly send requests to GCM.

For email marketing we use [SendGrid](https://sendgrid.com/).

We use [Hotjar ](https://www.hotjar.com/)for setting up heatmaps, visitor recordings etc for our CouponDunia website. We are planning to go live with a similar solution soon for our apps. Best on my research [Appsee ](https://www.appsee.com/)and [Appanalytics.io](https://appanalytics.io/) seem like the best options.

**PlayStore Optimization + Competitor Analysis**

I have been using [SimilarWeb](http://www.similarweb.com/) as well as [AppAnnie ](https://www.appannie.com/)for keeping an eye on Competitor apps as well checking our own trends (Play Store rankings, keyword rankings etc).

[SensorTower](https://sensortower.com/) is another great tool for Play Store keyword analysis.

You can try [Addons Detector](https://play.google.com/store/apps/details?id=com.denper.addonsdetector&hl=en) which detects addons used by various applications installed on your Android phone.

[Stackshare](http://stackshare.io/) is helpful for discovering other company’s entire software stack.

**If you liked reading this blog post you might also want to check out:**

[How We Scaled CashBoss To 500K downloads in 5 months](https://www.linkedin.com/pulse/how-we-scaled-cashboss-500k-downloads-5-months-manas-j-saloi)

[7 Hacks to get 5-Star reviews on Play Store](https://www.linkedin.com/pulse/your-definitive-guide-5-star-app-ratings-manas-j-saloi)

**P.S I tweet a lot of interesting articles/studies. Follow me here:[@manas_saloi](https://twitter.com/manas_saloi)**

Cross posted from: [https://www.linkedin.com/pulse/10-tools-every-mobile-product-manager-manas-j-saloi](https://www.linkedin.com/pulse/10-tools-every-mobile-product-manager-manas-j-saloi)
