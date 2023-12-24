# Design a Multi-Class Program

_**This is a Makers Vine.** Vines are designed to gradually build up sophisticated skills. They contain a mixture of text and video, and may contain some challenge exercises without proposed solutions. [Read more about how to use Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to design a multi-class program.

## Introduction

Once more we need to update our design recipe. However, this time we have a
whole new level of challenge. How do we figure out how to break our program up
into classes? There are two common approaches to this:

1. **Emergent Design**  
   Start with a single class, and then extract out new classes when it seems
   like it is doing too much.

2. **Planned Design**  
   Design a multi-class system and then build it, updating your design as you
   learn where you were wrong at first.

You can also use a mix of both.

We are going to start off with Planned Design. Exercises on Emergent Design are
available in the adventure section — and you're not too far!

Here's our Multi-Class Planned Design Recipe

> # Multi-Class Planned Design Recipe
> 
> ## 1. Describe the Problem
> 
> Typically you will be given a short statement that does this called a user
> story. In industry, you may also need to ask further questions to clarify
> aspects of the problem.
> 
> ## 2. Design the Class System
> 
> Design the interfaces of each of your classes and how they will work together
> to achieve the job of the program. You can use diagrams to visualise the
> relationships between classes.
> 
> Consider pulling out the key verbs and nouns in the problem description to
> help you figure out which classes and methods to have.
> 
> Steps 3, 4, and 5 then operate as a cycle.
> 
> ## 3. Create Examples as Integration Tests
> 
> Create examples of the classes being used together in different situations
> and combinations that reflect the ways in which the system will be used.
> 
> Encode one of these as a test and move to step 4.
> 
> ## 4. Create Examples as Unit Tests
> 
> Create examples, where appropriate, of the behaviour of each relevant class at
> a more granular level of detail.
> 
> Encode one of these as a test and move to step 5.
> 
> ## 5. Implement the Behaviour
> 
> For each example you create as a test, implement the behaviour that allows the
> class to behave according to your example.
> 
> Then return to step 3 until you have addressed the problem you were given. You
> may also need to revise your design, for example if you realise you made a
> mistake earlier.

Copy and fill out the recipe template for the exercise below.

## Exercise

This is the big one! You might want to start a new pytest project for this.

Use object-oriented design and test-driven development, backed up by your
debugging and pairing skills, to develop the following program.

> As a user  
> So that I can record my experiences  
> I want to keep a regular diary

> As a user  
> So that I can reflect on my experiences  
> I want to read my past diary entries 

> As a user  
> So that I can reflect on my experiences in my busy day  
> I want to select diary entries to read based on how much time I have and my
> reading speed

> As a user  
> So that I can keep track of my tasks  
> I want to keep a todo list along with my diary

> As a user  
> So that I can keep track of my contacts  
> I want to see a list of all of the mobile phone numbers in all my diary
> entries

Some pointers:

* Remember that user stories don't map to classes 1:1. You'll need to digest the
  full problem and then develop a multi-class system that meets the user's
  needs.
* Don't worry about user interface or input-output. That means you shouldn't be
  using `input()` and only use `print()` for debugging purposes.