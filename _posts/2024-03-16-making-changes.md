---
layout: post
title: Making changes
tags:
  - tech lead
  - reviewing
---
Knowing how to make changes that are easy to review will help not only getting your changes past review faster, others will be more willing to review your changes.
These are my thoughts on how to achieve this.

This post is the other side of the coin related to reviewing. You can read about that other side in [my post on reviewing]({% post_url 2024-03-16-approaching-reviewing %}).

## What makes a change easy to review?

To summarize it, I'd say about a chrystal clear context. I've found that a few things simplify the reviewing process. They are, in no particular order, listed below.

Let your reviewer into your head. What you feel unsure about and would like the reviewer to focus more on. Clarify your plan on future changes to motivate your choices in the current change.

Something many struggle with, both when creating changes and when reviewing them, is the size of the change. It's not difficult to see why a small change would be faster and easier to review compared to a change possibly even spanning numerous files.

## Split your delivery
Consider that there is nothing forcing you to deliver the entire solution in one pull request or what you might call it in your context. Split the delivery of your work into several steps to simplify the review process. Don't forget that each delivery should be contained in such a way that it does not break anything while upcoming changes are yet to be delivered.

Broadly speaking, you could under most circumstances split your delivery into the following parts. These are examples, you can introduce other steps or skip some steps. It all depends on the change you have in mind. It takes time and experience to see how far to take this.

At any stage in the process your reviewers might find space for improvement or that your intended path is inappropriate for reasons you might not see or know about. This is why you should show your work as early as possible. This happens to us all! When it does, don't automatically think you need to revert all your previous steps. There is the possibility that you need to revert it all. Often I find that I just have to adjust one or two things in a previous step to get on track. Make those changes as separate steps and then keep showing your work, one step at a time.

### The preparatory step
At this step you fix formatting and refactoring to allow your changes to come to be easier to do. When you are done and is ready to get your work reviewed, tell your reviewers that this change is not intended to introduce any functional change and that you are laying out the foundation for your change. You can describe your plan for your future changes if you think it helps or if asked for.

This will help the reviewer in many ways. It sets the reviewer's frame of mind to where you want it, helping them know what to focus on. This could, of course, also be used to mislead the reviewer. We should work diligently to avoid this as responsible professionals! Another benefit is that it can be pointed out immediately if the reviewer finds a functional change as that would, in this context, be undesired.

### Introducing new stuff
The next step could be to introduce your new types and constructs, without having them used everywhere they need to be.

As this is a change purely devoted to introducing new things, but not use them, there is minimal risk of breaking anything and the reviewers can focus entirely on other things like scalability, readability, and correctness.

### Start to tie things up
The next step would start to tie together everything you have prepared and introduced in previous changes. Everything that needs to use your solution will not use it at this stage. You rather focus on one or a couple of prime examples to show the reviewers concrete examples of how you intend to tie things together.

At this point your reviewers know the foundation you have prepared and what you have introduced. It's time to start to use it. Here, the reviewers can focus on the change in behavior and see examples of how you intend to use what you have introduced.

### Finalizing your changes
What you have prepared and introduced are in use now, but not everywhere. At this step you complete the change, having everything that needs your change use it.

Your reviewers should now know enough about your changes for you to essentially copy and the change throughout the code base repeating the process they have already in the previous step. Here the reviewers should focus on variations on the theme making the copy paste operation inappropriate or in need of adjustments.

### Clean up
Once you have applied all your changes, you might find the need to clean up or do some more refactoring. This is the place to do that!

At this point we are essentially coming full circle. You can see this step as either putting down some finishing touches or the spring board to  develop your solution further.
