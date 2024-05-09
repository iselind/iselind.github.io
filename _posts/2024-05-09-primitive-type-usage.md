---
layout: post
title: Primitive Type Usage
tags:
  - type safety
---

A recurring problem I see in many code bases is that the primitive types are used in the wrong way. My intention with this post is to challenge you to look beyond your own assumptions. Let's look at a couple of examples.

```java
int age = 13
float length = 18.6
double speed = 13.4
int timeout = 15
```

Can you see what is wrong with these examples?

In short, all the examples lack a unit and require validation. Let's take age as an example. Being an integer allows for negative numbers. Does a negative age make sense? That hints at the need for validation. Is this age for a bacteria, human, or a galaxy? This highlights the need for a unit. The unit here might, for example, be milliseconds, years, eons, or sols (days on mars).

For age, it might feel natural that an age is an integer. Depending on the context that might not be so. A float might make more sense.

Some instances might not require a unit, like
```java
long postbox = 312631994
```
Negative values still does not make sense. Hence, validation is still required.

What about instances where the entire value range is valid and no unit is required? In other words, a primitive type would suffice.

You still run the risk of polluting your value if you have several variables of primitive types. Consider for a moment that you have a timeout and length as primitive types. There is nothing stopping you from, for example, multiplying them. What you would get is a value that does not make sense, but your types cannot help protect you from these kinds of issues.

Hence, it all comes down to type safety. We are not using the types to their full extent, neither for expressiveness nor safety. Let's take a look at what the above examples would look like if we were to employ type safety.

## What to do instead
Let's assume for the moment that negative values are invalid in the present context. We use age as the example.

```java
public enum AgeUnit {
  MilliSeconds,
  Years,
  Eons,
  Sols
}

public class NegativeAgeException extends RuntimeException {}

public class Age {
  private int value; // Might be a float if that make sense
  private AgeUnit unit;

  public Age(int value, AgeUnit unit) throws NegativeAgeException{
    if (age < 1>) throw new NegativeAgeException();
    this.value = value;
    this.unit = unit;
  }
}
```
We can add methods for, for example,
 - getting the values,
 - comparing Ages,
 - adding Ages, and
 - subtracting Ages

Have you noticed that nothing have been mentioned concerning setting values? Immutability tend to lead to safer programming in my experience. You can still base new Ages from already present ones. Adding and subtracting ages, for example, should then return a new instance of Age with the result and leave the instances of Age used in the operation unaltered.

## Enumerations vs Strings vs Integers for units
A string has a far larger value space than we need for our units. That leads to almost endless possibilities we need to validate, especially for comparisons to work.

We are not using enums enough. We should automatically grab for enums when there are very few distinct values that make sense and where each such value hold a significant meaning.

Pure integers hold the value but you'd have to translate that value somewhere to make it mean something. There is nothing stopping me from assigning an integer a value that makes absolutely no sense in that context. It's better to keep all of that together, which is exactly what an enum does.

## Why is this better?
In short, there are tools at your disposal that you are not using. The reason is either that you do not know about the tool or have not been taught how to use it. The tool I am talking about is the type system you find in programming languages.

Your programming language of choice will not allow you to mix types it does not know how to mix. The types you allow to be mixed have to be explicitly allowed by adding methods that allow the mix. This will lead you to keep types that should not be mixed separate.

You can also be assured that the values in any instance has already been validated. You cannot create invalid instances. If you try, you will get an exception or what other means you use to communicate the issue. It's impossible for you to miss validating anywhere.

We should aim for enforcing validation on everything. Things we do not want to, or cannot, validate should still have an empty validation section expressing the deliberate act of not validating along with ample motivation.
