---
layout: post
title: Approaching Reviews
tags:
  - tech lead
  - reviewing
---

In this post I want to share how I approach reviewing changes, what I focus on and what not to focus on.

What you will find when igniting an interest in reviews is how your own changes start to change, because you know how it is to review messes and noisy changes. You can read more on this in [my post on creating changes]({% post_url 2024-03-16-making-changes %})

## What to focus on
The purpose of a review is **not** to enable endless nitpicking. Focus on the things that are functionally important and readability. If applicable, you should comment on scalability issues that might come up from the way the problem at hand was solved.

If at all possible, do try to suggest alternative and solutions along with your comments. Others might see issues with your suggestion as well, enabling a discussion.

## What to avoid
Some things are hard to avoid, but we need to try our best anyway. One such issue I see often is when the developer has solved a problem in a different way than the one reviewing it would have. There is no obvious reason why the reviewer's way is better, it's just not the way the reviewer would have solved the problem.

This issue should be avoided, sometimes someone can come in from the side and highlight that this is what is going on trying to put an end to it. Doing this avoids wasting everyone's time and lets us focus on more productive things.
