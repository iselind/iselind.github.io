---
layout: post
title: Scaling Out - Transitioning Your Storage from One Data Center to Multiple
---
Your project have been deployed in one data center since the start. Due to operational concerns you are now investigating deploying your project in multiple data centers. How does this affect your storage solution?

You must rethink your storage strategy when moving from deploying in one data center to many. Having storage in a subset of the data centers is a big operational risk that can be circumvented by choosing storage solutions that support spanning multiple data centers.

Let’s consider why. What would happen to your application if the data centers keeping the storage went dark? Many applications would not survive that event. That’s why spreading load and storage over several data centers makes operational sense, which is where cloud-native storage solutions come in.

Transitioning from deploying in one data center to many means that constructs like new File(...) will no longer work. You have to change them to something else, which can be tricky. We do not want to change everything at once; the changes have to be applied over time in a controlled manner.

Let’s review the plan.

## The Plan

Firstly, you need something that can abstract away the interaction with the storage solution. Hide the implementation behind an interface. That way, you can easily swap it out for something else during testing and debugging.

Secondly, we must alter all instances of `new File(...)` into something that uses either the storage abstraction we just covered or the legacy storage solution, depending on the provided path. Let’s call this new version of File “SuperFile”. The `SuperFile` implementation has to implement the File API.

That means a search and replace of
`File f = new File(...)`
into
`File f = new SuperFile(...)`
which also suggest that `SuperFile` should be a drop-in replacement for File.

Once the search and replace has been done you need to maintain and enforce the use of `SuperFile` instead of File. You accomplish this by adding a test in your CI pipeline where you search for instances of “new File” and fail the pipeline if you find any.  Provide the hint that a `SuperFile` should be used instead.

The next step is to look inside `SuperFile`.

## The internals of SuperFile
`SuperFile` takes the same parameters as your ordinary `File`. The distinction comes with how the parameters are handled. It will be up to `SuperFile` to choose if the specified path is supposed to be handled by the legacy or the cloud-native “path”. Think something like a Strategy pattern. I can see three strategies.

If the legacy path is selected, then it could, internally, be represented by an ordinary File.

If the cloud-native path is chosen, then we can no longer use the File directly. Instead, we have to use the previously mentioned abstraction for the cloud-native storage solution.

In some cases you might want `SuperFile` to maintain the same file in both the legacy and cloud-native solutions.

## Considerations for the SuperFile implementation
Now that you have your SuperFile in place, how do you migrate your storage piece by piece. One possibility is to go folder by folder, updating the configuration within `SuperFile` to say which folders should be kept in the legacy storage solution.

The configuration itself should, or course, not be kept in the `SuperFile` code. Instead you could keep that in, for example, S3 which can be downloaded and parsed once to some static field within `SuperFile`.

There's no point in listing all folders in that configuration. Consider the situation having thousands of folders but only two of them should at this point be handled by the cloud-native solution. Then `SuperFile` would only have to test for these two. If there is a match, use the cloud-native solution. Otherwise, use the legacy storage solution. The focus could change once the situation is the reversed; fewer folders should be handled by the legacy storage solution than the cloud-native solution.

Once the transition is complete your path test could be removed along with the legacy storage solution. Another option could be to keep the strategy pattern for future needs. Just make sure the strategy choosing logic is written in a way that avoids unnecessary performance penalties.

A big difference between using legacy File versus cloud-native alternatives is that you cannot use the files/objects in quite the same way.

Using legacy file access allows you to use files as you are most likely already used to. The operating system takes care of making the content available, possibly by keeping only pieces of the file's contents in memory rather than the entire file. Saving the file means writing the changed contents back to disk.

Using cloud-native solutions require you to first download the object's contents in its entirety, either to memory or a hard drive. Here you need to consider cases where the object might be larger than the amount of RAM your machine have available. Once the contents have been downloaded; possibly along with metadata like byte length, content type, and content encoding; you can do what you need with the contents. Once you are done you have to upload the contents again to save the changed contents. Reading and writing these object is done using network requests, which leads us to the next consideration: the size of your objects. Working with a lot of very small objects is not as efficient as working with larger objects, which might lead to the need for restructuring your files to more suitable sizes.
