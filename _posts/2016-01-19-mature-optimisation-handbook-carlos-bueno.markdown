---
layout: post
title:  "The Mature Optimization Handbook - Carlos Bueno"
tags: booksummaries
categories: booksummaries

---
**Note:** While reading a book whenever I come across something interesting, I highlight it on my Kindle. Later I turn those highlights into a blogpost. It is not a complete summary of the book. These are my notes which I intend to go back to later. Let's start!

A problem definition must be falsifiable. You have to risk being wrong to have a chance at gaining the truth. Let’s start with a bad definition and make it better.“WidgetFactoryServer is too slow.”What does “slow” mean here?

“Too slow” is a judgement about walltime, ie time passing according to the clock on the wall.Two things generally contribute to walltime: computation on the local CPU and time spent waiting for data from storage or the network. You wrote WFS so you know that it doesn’t read from disk or network. Another contributor in threaded code is waiting for locks, but WFS isn’t threaded. So it’s probably all in computation. This fits a familiar pattern. We can use a ready-made problem definition.“WidgetFactoryServer is transactional. It receives requests and emits responses. It is probably CPU-bound. So if we profile to discover which functions take up the most time, and optimize those, the total CPU time per transaction should decrease.”

Find out what resource is bottlenecked, suggests a method of finding the right places to optimize, and is clear about what result you expect to see

The kinds of computers in use today have four major levels of “where data goes”, each one hundreds to thousands of times slower than the last as you move farther from the CPU:
* Registers & CPU cache: 1 nanosecond
* RAM: 102 nanoseconds
* Local drives: 105 to 107 nanoseconds
* Network: 106 to 109 nanoseconds

Memory controllers try mightily to keep the first level populated with the data the CPU needs because every cache miss means your program spends 100+ cycles in the penalty box. Even with a 99% hit rate, most of your CPU time will be spent waiting on RAM

**Story about optimising HHVM**

HHVM is a virtual machine for the PHP programming language. Some of the time it runs bytecode that is dynamically generated (“just-in-time” aka JIT), but most of the time is spent running precompiled C++ code. The implementation wasn’t completely settled, but there were legitimate reasons for making performance a feature.

The team had to come up with a different problem definition, which went something like this:CPU time in HHVM is dominated by CPU cache misses. If we somehow log both the function which suffered a cache miss and the function which replaced the data that was missed, we may find that a small number of functions cause most of the evictions. If we optimize those to use less cache space, we expect to see a reduction in both cache misses and CPU time spent across the board.

The surface problem was CPU time. But most of the time wasn’t actually going to computation (ie, moving data around inside the CPU) it was spent fetching data from RAM into the CPU.

 That’s a mouthful, but it worked. To prove this theory they ended up gathering very expensive and detailed logs, for example, every datum accessed or CPU instruction executed. They then fed that through a cache simulation program, and modified the simulator to record the causal path from evictor to evictee, so they knew what functions to blame. Sort the list to find the worst offenders and optimize them. Not easy, but a lot more straightforward.

Optimizing comes down to whether the system is doing unnecessary queries, or whether their results can be cached, or perhaps the query itself (or the indexes, or the database) needs tuning. Only the data can tell you where to look next


Here are some metrics that are probably relevant to any large networked application:Error ratesLatency (average, median, low and high percentiles)CPU Time / InstructionsNetwork bytes in & outRequests per secondActive usersActive serversServer utilization (CPU, RAM, I/O)Database queriesCache hit / miss rates

These metrics should be further broken down by country, datacenter, WWW versus API versus mobile, and a half-dozen other dimensions.

In particular, making schema changes or adding indexes to a database with more than 10-20 million rows completely locks the database for hours at a time. Removing old indexes takes just as much time, and not removing them hurts performance... There are complex operational procedures you can do to circumvent these problems... so error prone and heavyweight, they implicitly discouraged adding features that would require schema/index changes...

Stay up to date with my latest posts/tweets here: [@manas_saloi](http://twitter.com/manas_saloi)
