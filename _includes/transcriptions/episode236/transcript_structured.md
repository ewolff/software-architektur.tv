# Folge 236 - Code Retreat live - mit Marco Emrich So, for a while, the pleasure with the Tidy First story and it's supposed to be about the topic Code Retreat.

That's a bit of a challenge, because on the 8th and 9th of November, especially on the 9th of November, on Saturday, there is the Global Day of Code Retreat.

There are Code Retreats all over the country and even beyond, so in the entire German-speaking area and even worldwide.

We just want to present the concept.

Before we get to that, Marco, would you like to say a few words about yourself?

With pleasure.

So, I'm an IT consultant at CodeCentric, which is perhaps still interesting in the context of co-organizers of the Software Chamber in Nuremberg, where we also have such cutters and Code Retreats at events.

Exactly, and you are actually part of the Code Retreat of those that DATEV is doing in Nuremberg.

You can experience yourself live if you are interested.

We'll see how many participants come.

So if there aren't that many, I might just join myself.

Otherwise, I think we currently have three moderators.

And if there are a lot of participants, then we can also support them well.

So, and I think we want to talk about the topic of Game of Life first.

I'll take a look at the slides.

There they are.

Conway's Game of Life.

That's what you implement at Code Retreat.

And at this point I would hand it over to you, so to speak.

What is Game of Life and why are we interested in it?

Let's take a quick look at that.

First of all, it's basically our vehicle, our exercise, of course.

We want to have a code example that poses as many interesting design challenges as possible.

And Conway's Game of Life fulfills this sweet spot a bit.

What is it about?

It's basically a cell simulation.

Or you could also say it's a zero-player game that plays itself according to certain rules.

A simulation that runs according to certain rules.

And there's a grid of cells.

You could also say a field on which these cells are arranged.

And a cell has exactly two possible states.

It's either dead or it's alive.

And this is now represented graphically by saying that filled means alive, empty means dead.

But the graphical representation is what it is.

We're not going to look at that.

It's not about the UI and the representation, but purely about the simulation logic.

Exactly.

And a quick note.

The Conway of Conway's Game of Life is not the Conway of Conway's Law.

These are two different Conways.

Exactly.

The other Conway.

Sorry, I interrupted you.

There are several Conways.

There's also an Australian Professor Conway who worked on Pearl 6.

So there are even three Conways that are of interest in our field.

Exactly.

These are the rules of the Game of Life.

And it's basically just about what happens to a cell in the next generation.

These are discrete generations.

A new generation is always formed from the old one.

But that can't be self-explanatory.

It's always a new generation based on the state of the old one.

And you have to look at each cell individually and see how many living neighbors it has.

A cell has a two-dimensional grid, always exactly eight neighbors.

But how many of them are alive?

And depending on how many are alive, this has an impact on the next generation.

There are these four rules.

If fewer than two neighboring cells, for example one, are alive, then this cell dies in the next generation.

And it's always just about the middle cell that we're looking at right now.

So it's just about the rule of what happens to each of these cells.

And as I said, it's only relevant how many neighbors are alive.

If there are exactly two or three living neighbors, then the cell survives in the next generation.

So a living cell is still a living cell in the next generation.

If there are more than three neighbors, that's the overcrowding rule.

These rules still have names.

Then the cell also dies in the next generation.

Overpopulation, whatever.

And then there's this special case.

If a cell is dead and it has exactly three living neighbors, then it comes to reproduction and the cell lives in the next generation.

These are four really simple rules.

But if you apply them consistently, a lot of interesting constellations can arise from them.

And there are a few very exciting examples.

Here, for example, there is a pulsar.

Simply because there is a certain basic configuration and you apply the rules consistently, it falls back to its original state after several steps.

And iterates between three or four states and then starts again and again from the beginning.

Or another pattern is a chimera, for example.

It moves over the field, so to speak, by moving a little bit to the right and to the top and reproducing again.

So it reproduces itself, but always in a different position.

These are all things that can simply arise by applying these rules.

That's why it was also of mathematical interest for Conway to do a little research on what could arise from such rules.

And there's another example.

It's a YouTube video.

Shall I start it up?

Yes, exactly.

I'd love to.

Then I'll switch here for a moment.

Okay.

And there you can also see a configuration of cells.

There is a basic configuration.

Then you let the simulation run.

And the exciting thing about this example is that the basic configuration is designed in such a way that the Game of Life, which takes place in the small one, which manipulates these cells in the small one, now you can see it right away, produces a Game of Life again in the larger one, because these cells themselves again form cells on a meter level.

Exactly.

And the edge length, I think, of such a single cell that we see here, so we see a slider when zooming out, the edge length seems to me to be hundreds of cells or something like that.

Something like that, right?

So a lot, at least.

It's always such a classic sign of this, because the Game of Life is actually also Turing-complete.

So you can practically prove that you could theoretically develop any program in Game of Life, if you interpret the data accordingly.

Exactly.

So Turing-complete is this theoretical concept that says, everything you can calculate, you can calculate with the Turing machine, and various other things, also Game of Life, can be reduced to it, are ultimately identical.

That is, everything you can calculate with the Turing machine, you can, funnily enough, also calculate with Game of Life.

I'm still missing a C++ template expansion, so only that the template code is already generated by Turing-complete.

You could probably also write Game of Life completely in C++ template meta language or something like that.

Also an interesting challenge.

Exactly, so that's the random example we want to take and implement.

In fact, we want to do it right away.

Now the other question is, how do we actually not do that?

I think that's the thing we have to discuss.

Now I have a little insight into why we are doing this at all, what the idea behind Code Retreat is.

Let's take a quick look at that.

Exactly, that's kind of the idea.

It's called Code Retreat because you're withdrawing from everyday life, because it's about not being disturbed all the time by customer calls, requests, whatever, but that you can concentrate on it all day long, to advance your own learning in some way.

There is also a website for this, where the whole thing is centrally organized.

That's CodeRetreat.org.

And there you can also find a lot more information, like how you host and organize a Code Retreat yourself, for example.

And that's where all these events are included, and you can find out which city the next Code Retreat is in.

And of course we now have a whole lot of cities with Global Day, which suddenly appear there.

Did you want to say anything else about the organizer there, or do we do it later?

No, don't go any further.

Okay.

The idea is, we all know, we're not perfect.

We're not all super coders, super designers, super architects, but we can still learn new things.

And we try to practice that in one way or another.

And basically you could argue now, well, we've been practicing on the job all the time.

So when we're in projects, of course we're learning all the time.

But just practicing in the shop can of course, as is shown here, be dangerous.

And if you compare that to musicians, it's a bit absurd to imagine that they would go on stage and start practicing there.

Whereas with us, in our industry, it's actually common.

So we're actually practicing all the time on stage.

We're in the shop, we have a gig, so to speak, we're live, we're developing something for someone and at the same time we're still practicing the whole thing.

And what is unthinkable for musicians would be normal for us.

But of course we would like to try to practice beforehand.

And that's why the idea is to deliberate practice and just get the chance outside of the shop to strengthen our skills.

And one idea is, of course, to simply say, we're expanding our toolbox.

Toolbox doesn't necessarily mean tool in the technical sense, but toolbox also in the sense of more methods, more concepts that we know, things that we've tried before, experiences that we have, that we can reuse.

And we're expanding our toolbox in the sense of, if we then later in a real project come across similar problems, then we may already have the solution ready.

Because then we've practiced it before, we've already done it before.

And that's actually the whole idea of the story.

It's important, such a cult retreat, it goes on all day.

This is the no shipping day.

So the idea is, we don't have to deliver anything.

We don't have to deliver anything.

It's not about getting done quickly with any feature.

Because that's often the problem.

When I'm on the job, then I have to deliver, then I have to get done.

And then I might just do things the way I know, even if I already know it's not the optimal way.

But I don't have the time to try something else, which might be better or not.

Here we take the time.

Here we don't have to deliver anything, but the focus is on the learning experience.

The focus is that we try as much as possible to understand what we're doing there.

And not that in the end, somehow a deliverable product is created.

We do that in pair programming.

This is also a basic philosophy, also supports learning.

You can also sit next to each other.

That's totally okay.

You don't have to do it like the two of them here.

And then of course you can also do it remotely.

And one thing that is also a basic requirement, so to speak, we do the whole thing test-driven.

We also want to try to practice good practices, so to speak.

And that's the way it is traditionally at Code Retreat.

You could do it differently.

But it has simply been established that test-driven development is such a basic pattern that you use all day long.

So far, so good.

Exactly.

Maybe briefly about test-driven.

So actually test-first.

We will actually write a test before we write an implementation.

And we will try to keep this cycle.

That would be to say, okay, we make the test green by implementing a functionality and then refactoring it to make it look nice.

And then we make the test green again so that the refactoring works and so on and so on.

I just wanted to say that briefly.

So we're actually going to write a test first and then the implementation.

Exactly.

To keep this TDD cycle consistent.

Good.

And you had already switched to IDE.

And I don't even know what IDE that is.

That's Visual Studio Code.

Exactly.

The stack is TypeScript and VTest.

So a testing tool for TypeScript is a bit of the unofficial test successor.

It is sometimes handled a bit like that.

I think it was originally a fork, too.

I'm not quite sure.

But it's very, very similar to test, which is also very, very similar to Mocha, which was previously in this TypeScript, JavaScript and Unity.

Exactly.

They all have this philosophy with described int.

So it comes from the behavior-driven development that you can organize your tests a bit in a natural language.

But it's still a classic unit testing framework from a technical point of view.

Exactly.

And what we're seeing now is a piece of code that is currently being tested, whether it's 1.1.

So to make sure that the tuning works, Marco had prepared that nicely.

And now we would sit down together to implement this thing.

And logically, I'm not sitting at the keyboard.

So we want to do hyper-programming, but Marco is sitting at the keyboard.

And we want to...

Briefly from the stack.

Maybe I'll demonstrate that very briefly before we continue at this point.

I just want to show one more thing.

There is now also an integrated tool where we get direct feedback in the IDE.

It's called Wallaby.

And there we can now, for example, if I now install an error here, then we get a feedback right away.

And we're told the test is now red because 1 is not equal to 2.

Exactly.

So that means you've changed the code now and actually now appears on the left next to the code page already a red or a green dot.

You just said it's 1, 2, and that's not the page.

And on the left next to it now the hint that this page is erroneous.

Exactly.

And we can of course also get errors simply because it's not compiled.

For us, it's just as red.

Whether it's not compiled now or whether the test, so to speak, returns red, we consider both as an error in the TDD cycle.

Exactly.

So we would actually start now.

You wanted to say something about programming.

Sorry, I interrupted you.

Oh yes, exactly.

So you're sitting at the keyboard and we're going to discuss together how we want to get started with it.

I would like to clarify a few questions from the chat.

So in the meantime, we would actually, I think, program down somehow so that we have a little focus.

It says, is the concept of socio-technical systems also something that fits into your toolbox?

Yes, but that's not an issue for a code retreat.

Test first on extensions.

Which is the most common test you use and which are the most important extensions you should have in Visual Studio Code?

I think you just described that.

Right?

I think you have.

Yes.

So I mean, the most important thing is always very, also personal preference plays a role.

So that's a bit hard to say now, but I'll say it.

So there are these typical test frameworks.

Mocha, Jasmine, Jest, VTest.

VTest is definitely one of the more modern ones.

Exactly.

And do you also use AI for code generation?

No, we don't.

So that's really old school, isn't it?

I have a GitHub co-pilot installed, but I have now deliberately deactivated it for the session so that it doesn't crawl into us now.

Exactly, because it distracts too much from what we actually want to show.

So.

And with that, so to speak, everything is said first.

That means we can get started now.

And we have to implement these rules somehow.

That means we should just take one of the rules that I would suggest now.

We can, for example, say this rule with which, exactly, you go there again somehow.

This rule with, if I have less than two neighbors, then the thing is dead.

We could do that now.

We could do that now.

Then we would have to build a field.

So with field you mean now, the field in large, the grid with all the cells and the connection?

That would be an idea, wouldn't it?

That would be a possibility.

If we do that, however, then we will immediately charge up a lot of complexity, because we then have to solve this topology problem at the same time.

So where are the cells?

How are they connected to the other cells?

What are the directions, so to speak?

And of course also the rules, with how many living neighbors something actually happens.

So that you should actually separate the two things.

One thing that may also be exciting, as the game is supposed to be, is that it is conceptually infinitely large.

That means if we were to take an array now, which would somehow be my first idea, then we would already torpedo that.

And it's probably not that great.

That is probably possible, but then you will get problems when you get to the corners of the array and then you have to think about what you do then.

So there are certainly smarter solutions for that.

So let's try to make a cell.

Let's start with a cell.

I think that's a good idea.

That we first concentrate on the rules themselves.

And then you can later try to assign the cells again in the topology.

Exactly, and then you would have some possibilities that we refer cells to other cells or whatever.

Okay, so let's take a cell.

And the cell, we should probably first say that it is alive, right?

Because the rule says, if the thing is alive, it will then be dead with too few neighbors.

The question is, how you would like to present it now.

The cell could of course be represented as different data structures.

What would be a data structure that makes sense to you?

So I would have built a class now and made it object-oriented.

So a cell has a state and it is alive or dead.

We can do that.

We notice, of course, that we are now in the middle of the design.

So the moment we start modeling this rule, we have to think about the data structure.

That means we are now in the middle of a design process and we have to make this decision at this point.

Okay, you would have liked to have it object-oriented.

I'll create a new cell.

Yes, so far?

Yes, exactly.

Now we are at a point where we already have a red test.

So that's enough at the moment to say, now I have to write a piece of production code to get it green again.

Exactly, so you wrote const cell equals new cell and now it says it doesn't know the cell.

So it doesn't know the cell class.

And now you can tell it ...

I think I have to do that manually now.

I don't think I can do it.

Exactly, now you actually assign the cell class and then it's free so far.

Good.

Now you said you would like it to start with a living cell.

Would you like to do that with a constructor?

Should we do it with a setter?

What would be your preference?

I would do it with a constructor because a cell without a state somehow doesn't make sense.

So I would now ...

I think I'll take a boolean.

So alive or dead I can just ...

We can do something that we say we just put a true in there.

We can also do it differently that we say we put in a property object or we put in an inname alive.

There are different possibilities.

But we can also start with a very simple solution first.

We can also refactor later.

That's right.

Actually, we could take an inname.

I don't know.

What is your favorite?

Then let's see if we can actually say new cell alive.

So not that we give an alive as a value for the inname that can be dead or alive.

Okay.

Then let's build it for a moment.

So the same point, I should say again briefly.

So we're back to a compile error because the constructor doesn't expect any arguments.

That means we're now forced to write production code again.

And I would now pick up a bit more and say let's define this type.

You can do it differently in TypeScript, but that's not what it's about today.

It's just that we say, what would you call the type?

Dead or alive, cell state.

What would be a good term for it?

I think cell state is good.

Again?

I think cell state is good.

Okay.

Then type convention capitalized and then you could say here that's either dead or it's alive.

That's one way to define in TypeScript.

Okay, good.

So, now we also need a constructor.

Nothing to do with it, but it's combined.

Yes, and it's a green test, so it's fine.

So, then I think we would say that the cell has two neighbors.

Okay.

That's not true.

Sorry, less than two neighbors.

So we would say one neighbor.

Okay, right.

So a test is always an example.

That means we're looking for a neighbor as an example.

So one living neighbor.

How do we do that?

I would say the thing should have an attribute or something like that.

The number of neighbors and then...

So we can just access a public attribute.

I can write a setter for it.

So again, different design options.

I would do it as an attribute.

So I think that with the set method, it's a Java or Bleibse.

So if I can have logic behind the attribute, So the code executor is...

You can catch this attribute later with a setter, if you want.

But we can just start with a public property.

Number of living neighbors.

So, and it should be one, you said.

Yes, exactly.

Okay.

Well, now he's complaining, of course, because the property doesn't exist yet.

Then I would create it now.

Public number of living neighbors.

Type can be number first.

If you don't mind, you can maybe do it differently later.

Exactly, I would actually like integers or something.

Not quite optimal would be, if I could say, that's a whole integer.

Smaller equals eight, but yes.

So what we could do here would be to build a guy who was...

But it might go too far now.

We'll call him number of neighbors and say, he can have exactly these values, one, two, three.

So kind of an enum.

But it might be a bit of an overkill now.

Yes, I think that's fine.

So you just said cell number of living neighbors is one.

And then I would think, I'll calculate the next generation.

So Excel.calculateNextGeneration or something.

Again, what should the function be called?

CalculateNextGeneration.

CalculateNextGeneration, yes.

And that's a method that's just called and does it as a side effect.

Exactly, so it has an effect.

And then I would have to have as a result, that the cell is no longer alive, that is, dead.

Okay, that means we ask the state of the cell again.

Of course, we now need a way to access it somehow.

So how would you like to call it?

The cell state or the state?

State is better, I think.

That we already have in the context of the cell.

Yes, exactly.

So cell.state would be then.

And it should, what should it be now?

It should now be dead.

Dead, exactly.

ToEqualDead.

That would be our expectation.

Exactly.

Somehow the property state doesn't exist yet.

You have to embed it.

Right.

This is now our red again, because we have formulated our expectation.

And KillCurrentNextGeneration doesn't exist either.

Exactly, that doesn't exist either.

Exactly, that means we can define that here again.

And we can say there is a cell state.

This is of course a type cell state.

Yes, but there is only state.

Sorry.

There is no cell state, there is only state.

That's the type state.

And...

KillCurrentNextGeneration.

The method doesn't exist either.

Exactly.

Oh, we can use cde here.

We can actually say declare method.

Exactly, that's what it does.

The position doesn't fall, but it's good.

Okay, so.

And then I would take the straw out here.

It says the method is not yet implemented.

And now it compiles, but the test says it expects that the cell state is dead here.

But we get an undefined.

Because we haven't read anything yet.

Then you can just say the cell state is dead.

Sure, that would be the easiest solution, of course.

We can just say that the point...

State, that's what it's called.

Now it offers me here.

There are only two possibilities.

He's dead.

Is the test green first?

Yes.

I mean, we haven't implemented logic yet.

That's fake, of course.

But the test is green.

Exactly.

And with that we have now reached the goal, so to speak.

I don't think the test is that cool yet.

It says here, it should run a test.

There should be something else.

The rule means something from...

We can take a quick look at the other screen.

It's called underpopulation.

Exactly.

Then you write that down here with the underpopulation, right?

Okay.

So we could say it executes...

It dies if underpopulated or something?

Again?

It dies if underpopulated.

Ah, okay.

Cell dies if underpopulated.

That's what we have.

And if you want to do it that way...

Ah, okay.

We don't describe the whole Game of Life, but we describe the cell.

That's why there's this id.

It's always the idea that you use the context in the language.

It's the idea to proceed a little bit behavior-driven.

It dies.

You don't have to do that, but just offer the framework.

Cell dies if underpopulated.

That would be the rule for it.

And that's a specification.

So the test is a specification that says...

That happens in the case of the underpopulated rule.

Exactly.

Actually, you have to write if neighbor is underpopulated.

But I don't know if that makes sense.

Yes, yes.

Good.

No.

We could improve it.

No.

Neighbor.

I don't even know if I wrote that right.

I think it depends.

You are consistent.

You write it with just O.

And I think that's British English.

Oh, British.

I think...

We're just pretending to be people who don't know English.

Good.

Then let's see if we can implement the next rule.

That would be the rule with...

Which one do we want to take?

I would say we'll take the one that survives if it's two, right?

So it survives if it has two living neighbors.

In brackets.

Survival rule.

Right?

Exactly.

And then we could actually do the same...

I think you can copy the code below, right?

Or do we want to write a test method... ...that takes over parameters?

Okay.

So, exactly.

So I copied it now.

That's not right, of course.

What do we have to change?

The number of living neighbors is two.

Okay.

And then it should be alive.

Then it should be alive.

Good.

Understood.

Exactly.

And now we also get the feedback.

That doesn't work yet.

So this specification is not yet fulfilled.

Because he expects...

Exactly.

So he expects alive, but he gets dead.

Expected dead.

That's what he gets, that it should be identical with...

Because our implementation...

Exactly.

Because our implementation in Calculate Next Generation says at the moment... ...this.state is dead.

So that means this survival is just not in there.

Right.

Then I would write in there now... ...if the state...

No, no, no.

So if the number of neighbors is two, I'll do alive.

Okay.

We can do a little experiment again.

If I would just write in alive for fun... ...then the new test would be successful, but the old one would break.

Okay, good point.

That means we have to write an if statement.

It's not enough that we change that to dead now.

So we actually have to write the if statement.

That's compulsorily.

So what kind of condition should be in there now?

Number of living neighbors is two.

Number of living neighbors is two.

Then it should be... ...this.state... ...equals...

Sorry.

Oh.

Very short.

I'm sorry.

Deactivate the bell.

This.state is alive.

Exactly.

And the other...

I'll do it quickly here.

A few syntactic things.

And that would be the alternative case, right?

Exactly.

That's how you wanted it.

And now we have the reason.

Exactly.

I think we can stop at this point.

From my perspective, just to give a few hints.

The one thing that is now a problem, of course, is...

Actually, you should have the case of three.

Does the cell survive too?

We don't have that now.

So I have to change something there.

We'd probably have to write a test case for that.

That would be a next step I wouldn't see.

And the other...

Sorry.

I think there are both possibilities.

I mean, it's always the question of how far you want to go.

If it's important to us to say we want to check the three-way case in detail, then of course you should write your own test case for it.

But of course you could also say these two test cases would be in the same equivalence class.

And it would be okay to say we change the behavior without having a special test case for it at this point.

Exactly.

And just go here to...

No, wait a minute.

At two or three.

Well, then you have to say it has to...

So in that case, it would be a greater equal to two.

Exactly.

So you can already see...

Even with these trivial things, you get lost quickly.

The tests are totally helpful.

It probably always makes sense to write more tests.

Definitely.

Exactly.

And the other thing that I just noticed, what would be a to-do, we have a code that says I take a living cell, I just say it has so many neighbors and then I look to see if it has survived or died.

And you could factor that out.

So the two tests look very similar.

You could write a method that says, okay, I say alive, so not alive, a neighbor should be dead.

So then I have a method that generally says I take a cell state, I take a number of neighbors and I take a desired target state and test whether that is correct.

There were still questions...

So Random had written on YouTube, better would be a name, I don't know what she referred to, that was at 1323, and furthermore wrote, a cell should not have neighbors, but eyes that check whether a neighbor exists on the grid.

And Jan agreed with that on YouTube.

Exactly.

That means we have now made a different decision to do it differently.

And that leads a little bit to these retrospectives.

So we are now on the retrospective level of code.

And what we tried again today in the morning, and what I found totally exciting was...

So I have to admit, I haven't participated in a code retreat for a long time.

I think the format is somehow exciting and I wanted to do this episode because we are so close to the Global Dev Code Retreat.

What I found so exciting was... the first thing, the first test, which does nothing.

It does nothing, but it is totally helpful to figure out how to build the thing fundamentally.

And in the pre-interview it was actually the case that I went in and said, hey, let's just do the field.

And then you said, like here now, no, that's not a good idea.

Let's start with the cell.

And random would have just started now and would have somehow already built up this relationship between the cells.

And then we would have...

And that's something we had in the very, very first test, which in principle had no logic at all.

It just said, as an implementation, in the next generation it is dead.

It didn't implement a rule, but I, so to speak, tapped the API.

And I found that exciting.

And that just showed how insanely fine-grained we are.

So I don't know how many test runs we actually had now.

So now the test run is not explicit, but it runs in the background.

And we actually went extremely fine-grained, but also test-first.

So that was exemplary.

I said, okay, I'll just write it down.

Then I have a compilation error, I have a red thing.

And then I'll just fix it until it's green, so to speak.

And I noticed that.

The idea is always that you should actually, I'll say, change under 30 seconds between production and test code.

So that you really get into such a micro-cycle to get instant feedback.

Because the more code you write before you get feedback from the other side, the higher the risk, of course, that the mental model no longer fits what is actually happening.

Exactly.

And that's just one of the things where you might otherwise say, that doesn't work at all.

But here you can try it out and it actually works.

Maybe a quick comment from Random.

I mean, of course, there's not just one solution.

There are a lot of real solutions.

Of course, you can also make completely different design decisions.

But it would be quite possible that we would come to a point at some point, if we now say, okay, how does the topology work?

Now we no longer specify the number of living neighbors, but it has to be determined somewhere.

And that we then end up with exactly such a concept.

So that can also happen at a later time.

I think one of the nice possibilities with test-driven development is that you can also start in different places.

So you could first implement the topology and not worry about the rules at first.

That would also work.

Exactly.

That's what I was just telling you.

So in the next iteration, that would be something that I might want to try out.

You saw these two roles, right?

So I took on this navigator role and somehow said, no, I want to go there.

And you were the driver, so the person who actually sat on the keyboard.

You can also change the roles.

I didn't do that now, because, to be honest, I can't do TypeScript.

But that would have been a possibility now.

Although that might have been exciting for me too.

So that would have been a possibility for me now, to learn TypeScript at the point where you told me what I had to type in, so to speak.

That might have been good for a change in the roles.

It's technically a bit difficult for us, of course, because we have to share the code somehow.

And that just makes it a bit more complex.

But I say, in a real code retreat, where you're still physically sitting, or you just have some other technique with which you can share the code remotely, it works well, of course.

Although this is a Zoom call, and I can now remotely control your computer when you leave it on, so you could actually do that.

Actually, that was a missed opportunity.

But I don't want to annoy people with the fact that I don't remember TypeScript.

That's not the focus right now.

Just so you know, in a real code retreat, it is of course more common to change these roles more often.

Maybe another note on that, which you also saw quite well with us, which I also find so elegant about this role concept, is that you can push it even further.

So if you do real strict style pairing, as is described, for example, by Lou and Forko, then the idea is that the navigator just gives high-level commands.

And you basically did that.

And the driver doesn't worry about the design, but can take away this low-level part from the navigator.

That means you say, write a class, and I know how a class is written, and write it on Sundays.

But you don't have to worry about where every single character is, but you can think in a higher level of abstraction.

Exactly.

We also discussed this before, that we have relaxed the roles a bit.

And we'll get to the constraints in a moment.

You can do that differently.

You could do that now.

I don't think there is such a nasty variant of it.

You could also design the role that you somehow say, I'll do what I'm told.

And I intentionally don't think about it.

And then you notice what comes out of it.

And then I would be in absolute control.

But I wouldn't have this...

You gave feedback and said, no, we can do it this way.

And this discussion about the cell, we could have worked differently.

And you can control that explicitly.

There are a lot of different pairing games that you can do to try things like that.

There is actually one constraint, it's called Evil Coder.

But there is actually the idea that both can also be alternating drivers.

The only difference is that one person writes the test and the other person does the implementation.

And the person who does the implementation actually only has the goal of getting the tests green.

Whether that makes sense or not.

And then you are the person who writes the test, somewhere in the responsibility to write really good tests or who forces the other person that at the end of the day a meaningful implementation comes out.

Exactly, there we are again in this discussion, not number of living neighbors.

So we say ex act 2, then it's just alive, then we get a test green.

But of course that's not what we actually want.

And with Evil Coder, it would be like this that you would have to force him to write another test method.

So that he says, okay, please do the test with 3.

And then I have to catch this case, so to speak.

Learning constraint.

Of course you don't want to do that in practice, but you can learn a lot from it, how to write tests very explicitly.

I'm afraid I have to come back to this crew resource management topic.

So that's also something that is not the case in air traffic.

There is one person at the wheel and the other is this person who then works on this other level.

That has also established itself a bit here.

And I think you can see very well that somehow this feedback cycle, the way we did it now, is much more productive than if you now say, no, we even work a little bit against each other.

Exactly, you have also prepared slides, because we have now only seen how it would otherwise go beyond that.

Exactly, those were the rules.

Forward in the slides.

Exactly.

Yes, what we have now basically already done, but maybe not so explicitly said, these are the four rules of simple design.

So also a concept from Kent Beck.

Whereby the idea is that you have four rules that you basically follow and which are deliberately arranged in a certain order.

And there is the first rule, the tests should all be successful, they should all be green.

That is always the prerequisite that you first make sure that it works.

And if it works, then you can go into the refactoring mode and say, what can we improve now?

We can take out duplication, as you have already explained.

For example, you can also take out duplication in the test, but also in the production code.

As soon as we are able to say, we have green tests, we can try to reduce the duplication.

We can do refactoring to make the code more readable, maximize clarity.

You can argue a little bit, which of the two rules is more important.

Sometimes they also play a little bit against each other.

Then you have to make smart decisions.

And the last rule is has fewer elements.

If the other rules are fulfilled and you manage to do the whole thing with fewer methods, with fewer classes, with fewer variables, whatever, to get fewer code lines, then you try to minimize that.

But that's why the rules have a sequence.

If I lose clarity because of that, or suddenly get duplication again, then I prefer to have more elements, if the other rules are better fulfilled.

If more code is fulfilled.

The design is driven in principle.

We have not just sat down and said, let's get the pen out and see how we divide and build this thing at all.

In principle, we jumped in and said, we are doing this story with the neighborhood and we are trying to clean it up with these four rules.

And then we come to the next topics.

And you said it, I could have started with the neighborhood and, nonsense, with the overall topology.

Or not random, he just had another idea.

And I come from different places, I just go there, but I didn't make the big plan beforehand.

I also want to get rid of a question.

Doesn't that overwhelm people?

So does it always work that you say, please write a little code and don't think about the big picture?

That will come to light.

So that's at least unusual.

But does that somehow also lead to strange designs and you have the feeling that it doesn't work at all?

What is your experience?

Is that a big hurdle?

CDD doesn't say that you always have to do it that way.

We have now practiced the extreme form, so to speak.

In fact, it is even more extreme than what Canback in the original Chicago School itself suggests.

Because what Canback would normally do is first make a list of, so to speak, what we have described in the id blocks.

So to find a list of potential tests first.

So he would go there first and write several ids here and say, what are all test cases?

For example, you could mark here in the framework as to do.

What are all test cases that we could think about?

What do we need?

And with that you also have a little bit of forethought.

That would actually be the very classic procedure.

We have chosen an even more extreme form, so to speak.

But there are also other TDD schools.

For example, the Hamburg School of Ralf Westphal.

It does exactly the opposite.

So what Ralf does is, he will do very classic object-oriented analysis and design in advance.

And only when he knows, so to speak, this is what my design looks like, only then does he start to drive the individual elements by TDD.

So he would develop a single method, for example, test-driven.

But he wouldn't let TDD design the class in principle, but he would have thought about it in advance, on the drawing board, so to speak.

So there are different schools, different ways of thinking, how you can also use this in the environment.

And my personal opinion is, there is not one truth, but it just depends a lot on the situation and on the people, what works best at the moment.

So I think this old Goldilocks principle applies.

So too much design upfront is usually not good.

So we know that from the past, who have been building UML diagrams buried for half a year.

Elfenbein architect, you have mentioned the term several times, it's certainly not good not to worry at all and always start with the code right away.

But in many cases, it is certainly not the perfect practice, but the truth is somewhere in between.

And where it is exactly in this spectrum can be very different.

And that would mean for you now, I could introduce these different schools that you have mentioned in such a code retreat as constraints, that you are brought in this direction.

Exactly, we have done that before.

In this session, we specifically do this one TDD school to learn this approach.

Exactly.

To see how well it works for us too.

So then you had, exactly, we can actually move on to the next slide, I think.

Exactly, it's a bit about the question, what we have shown in principle was a cutter, which we both carried out together.

Coding dojo is still such a popular term, what a setup would be, in which you can make such a cutter.

What is the special thing about the code retreat now?

Exactly, maybe briefly about that.

So cutters are motivated by what you have in martial arts, I think, where you have certain movements, just keep doing it more and more often.

And that somehow also exists for coding.

And we have a code retreat, and there is a difference.

And that's what we're discussing right now.

Exactly, so basically a cutter is an exercise that you can repeat more often, where you can learn new aspects at each repetition.

And that's exactly what you want to do in the code retreat.

And that's why you do five sessions every 45 minutes.

So if you have a lot of time, you can do more sessions.

So I can remember, in the early days we did seven sessions.

But it turned out that for most of the participants, including the moderators, it was clearly much too exhausting after such a long day.

That's why you typically do five sessions every 45 minutes.

And in each session, you start building the Game of Life from scratch every time.

Exactly, which means it's a very daily thing.

And this global day of code retreat is on a Saturday.

Which also means that people, in the first place, are so motivated in the back and just want to go there.

Of course, no one stops you from doing something like that internally.

Exactly, sorry.

The original idea was this retreat idea, that you don't get disturbed by typical business issues that you just have in everyday life, but that you can just concentrate and pull back.

Yes, exactly, and after these 45 minutes, you throw the solution away completely.

That's always a bit shocking at the beginning.

I just wrote a great solution, and why should I throw it away now?

But it's actually an important element that you do that, because it also frees you, because it means that every time you start Greenfield again, that you don't even try to copy code from the last solution and you just have the chance to try out new design decisions, to go new ways to get to other experiences.

Yes, exactly, and I think you said in the previous interview that this is one of the things that is somehow difficult to convey, so to speak, for beginners.

I found it ...

It was the same for me at the beginning.

So, in my first code retreat, where I participated, and then it was suddenly said, now please delete all the code.

That's just such a shock at first, because you're just not used to throwing code away in your daily business.

Actually, it would also make total sense every now and then, but it's always such an overwhelming feeling that you have to create.

Exactly, and what I now ...

So, we're getting to the constraints, so that means one thing, why that might be useful, is because you might do something different in the next iteration, for example, proceed differently driven by tests.

And I have to admit, I would really like to do the opposite right now, so not with cells, but somehow to say, I'll take the field first and try to figure out how I build a field, which data structure I use, so probably no array and how I get something like that.

Mivo wrote, in London School you do a lot of design in theory compared to Kent Beck style.

I think we said that, didn't we?

So, I don't know if you want to add something to that.

London School is a TDDS school where you also proceed outside-in, that is, you start very, very high-level and then break it down in small steps.

That's absolutely right, yes.

Then, of course, you have a lot more design up front, no question about it.

How would I proceed for Game of Life after London School?

Can you illustrate that?

You would write an acceptance test at the beginning, so actually a bit in the direction you suggested at the very beginning, that you already design a field in some form.

So, that doesn't necessarily mean that you already have the complete data structure, but that you think about the external API.

And write an acceptance test where you say, I have a basic configuration, or I'll say the classic would be something like an oscillator, where I have four cells in a certain configuration and I know what the next generation looks like.

And then I take that, I configure the entire field, look at the next generation and actually check the entire field, so whether all cells in the next generation have behaved properly.

That means you can then also, in one test, test several rules at once, if you want to, and then you have a very extensive acceptance test, which will remain red for a very, very long time.

And then you comment on it first, make sure that it is not executed, and then take the first small step out of this acceptance test, which you can then formulate as a unit test again, to test yourself step by step.

And you use mocks or stubs all the time, so essentially mocks at London School, to simulate the code that you don't have yet on the higher level.

Okay, all right.

Good.

Sounds exciting, doesn't it?

So that's just what you could try.

And then you can figure out how it feels, right?

So I think it sounds weird to me right now, because you're right, the test stays red for a long time.

We only have 45 minutes.

And in the end I have a red test.

I don't know.

So it would be my feeling that it might actually look a bit strange in such a quota sheet, but you could try that out.

And after the iteration, I don't think, I don't know if you said that, you would do exactly that again, right?

So say, okay, what did you learn?

What are the topics?

And take that a bit retrospectively.

We haven't even talked about it, but you mentioned it earlier.

So that's a very important aspect, definitely.

If you do a retrospective after each of these sessions and talk about it again, what did I actually learn now?

What did I take with me?

Sometimes you push things to the extreme to see that they just don't work well, to take this learning with you, to say, okay, we tried it out.

I now know when this method is useful and when it is more problematic than it helps me.

Exactly.

The other thing, to go back to this Greenfield again, is of course, you can also write a complete chunk code and that's okay.

So I mean, the idea is also, we want to experiment.

In practice, we are always driven to say, we have to write the code that will somehow pass it on to us, which somehow fulfills the feature and is definitely also deliverable.

But here we also have the chance to experiment and say, we'll write something just because we want to understand what happens.

And it doesn't have to be embarrassing for us, because we know exactly, at the latest, or let's say, in an average of 22 and a half minutes, the code is gone again.

That means, this lightening also frees you a little bit in the sense of psychological safety, but it brings a certain security with it.

So what happens on the code retreat stays on the code retreat.

I can exhaust myself.

I can learn things without having to be afraid of having to give me the crap somewhere.

Yes, and I'm not even sure if you absorb these factors.

I think it's actually important.

So exactly this factor that you're talking about, that somehow you don't have the stuff anymore afterwards.

And I don't know if I would call it psychological safety, but not that you just say, okay, I have the learning and the stuff is gone and I don't have to burden myself with it anymore.

And that's it.

So the experimental thought becomes much stronger.

And that's why I thought that I would actually do it myself, because I said it, I have no idea about TypeScript, but you can still do it.

Especially from a driver position, I don't need this know-how.

And I just said it, so if I had the intention to learn TypeScript now, that might be an option.

So I remember when I was at a code retreat, that someone was there, worked with some Python or something and said, hey, I would like to work with someone who does Java, because they have these great ideas, they have a lot of cool features and I would like to see that.

And these are things that you can do quite well.

Also a super important aspect.

So on the one hand, you can just do that, that you say, I work consciously in a programming language that I don't know, to see it, to learn it.

And the other thing is, because you're in a code retreat, I don't think we said that either.

So we do pair programming, but we don't do these five sessions with the same pairing partner, but in the code retreat, the pairs change.

That means you always have a different pairing partner.

And that's where the idea is, that you can also learn from other people.

If I pair with someone now, I'm not a Java developer, but I'm just fit in my Java IDE.

And then I get an impression of it.

How do you even work with Java?

How can the IDE features support you?

That's an experience I wouldn't get otherwise.

But if I pair with someone who knows it, I have a very quick opportunity to learn it.

Exactly, and the participants also bring their laptops with them.

So that means that what we had now, that you have a specially prepared development environment, we would also expect that to be typical for the participants.

I think we have one more slide.

You have one more slide.

Maybe just one more aspect to that.

So what I also find exciting, so we often ask at the code retreat, also with which languages people are on the road.

And sometimes you meet languages, which may not be represented so often.

For example, I have already met APL in a code retreat, which is a relatively exotic language.

You can actually solve the Game of Life in one line of APL code.

I learned the complete Game of Life.

And I think it's an exciting opportunity to pair with someone, who may be on the road with an exotic language, to get an experience, that you wouldn't have the opportunity to do otherwise.

Mivo asked, outside-in would then be the ingoing port in hexarch or really UI or something like that?

I don't quite understand the question at the moment.

It's actually...

I mean, hexagonal architecture.

Yes, that's clear.

So where I just say, I have the business logic core, and I have this adapter around it, which has some ports to implement.

It came from the business logic core, and he wrote, outside-in would then be the ingoing port in hexarch or really UI or something like that?

Yes, the problem is that we have to distinguish between methodology and code here.

So with outside-in, there is no specific configuration or no specific design, but it's about the way in which I start from the outside.

So one thing has little to do with the other.

Of course, when you work outside-in, you can also use hexagonal architecture.

But one thing is the methodology and the other thing is the concrete design.

These are two different aspects.

Okay, outside-in is where I say, I'll start with the acceptance test and then I'll build the granularity.

I can imagine that there is a connection, because with hexagonal architecture, the advantage is that I can have tests from outside.

And acceptance tests, so to speak, then just...

You could dock your acceptance tests to the ports of your application and you wouldn't have to go through the adapters, so to speak.

You can work on logical knowledge levels and you don't have the whole technicality first.

It's just an adapter first.

So it helps in any case.

So hexagonal architecture would definitely help to make the whole thing more tangible.

No question, that's one of the goals.

Exactly, good.

So now we have the last morning, I think.

Exactly.

And that was just another piece of information that you also have constraints in short-term retreats.

We've talked a lot about it, actually.

And with a constraint, it's actually the idea that you kind of put a handcuff on your arm and just take things away that you normally have, that you're usually used to using.

So a constraint could be, for example, in this session, I'm not allowed to use an if statement.

That's a constraint, because normally you're used to it.

We've just used it.

If I don't have this option, I have to find another option to come up with a solution.

And the idea of constraints is that you're basically forced to explore other ways.

So maybe another classic example would be, I'm not allowed to use loops.

Then I might have to work with higher-order structures like MapFilterRetuse and can learn something from it.

If I'm not used to working with MapFilterRetuse, I force myself to do so by saying beforehand, I'm not allowed to use loops or I come up with another solution.

But that's the way it is.

Constraints are also available on very different levels.

You can also say, for example, I make a constraint where it's about Maybe the keyboard shortcut is a better idea to internalize.

And then the constraint is, I'm not allowed to touch the mouse.

Then we take the mouse and put it somewhere else.

Or we switch the touchpad off the laptop and then force ourselves to look, how can you control the whole thing with the keyboard and learn other things through this constraint.

Exactly.

We're actually a little over time.

I don't want to give any hints.

There are probably some in the vicinity of you who are just looking at the website.

There are just a lot of them.

That means in the German-speaking room I would expect that you will probably get something in there.

I'll put the folders in there again as a link.

And I think that's just a good first step.

That you say, okay, I'll take part in such a CodeReachWeek.

How would you proceed if you wanted to do something like that yourself?

So in your company, for example.

Or whatever.

For me, the obvious way, that's how I did it, is to participate and then do it yourself and trust it somehow.

And chances are, it works somehow.

And there are also documents on CodeReachWeek.org.

Would you dare to do it?

Do you have another idea?

Would you dare to do it if you haven't been to a CodeRetreat before?

Well, as you say, that's the best way to get involved somewhere.

It's also relatively easy.

Because there are many CodeRetreats in different cities.

Or you can also participate remotely.

I would definitely recommend that.

On CodeRetreat.org, there is also a lot of learning material.

In fact, it is also described relatively precisely.

Typically, there are two roles.

There is the moderator and there is the host.

What do I have to do as a host?

What do I have to prepare?

What kind of environment do I need?

What do I have to do as a moderator?

You can't really do anything wrong.

Even if you do things differently, you can only learn from it.

What should the outcome be?

In the worst case, you noticed that you did it a little differently than the official way to do CodeRetreat.

And if everyone takes something with them and learns from it, that's okay too.

You can just do it.

You don't have to do it both ways.

Everyone can find their own way.

I think that's a very important point.

It can't go wrong.

In many of these moderation stories, we also had the episode with Martin Günther, the trust that something meaningful will come out of it.

You said in the prelude that this is something that has actually been developed through several iterations.

As is so often the case, there were many iterations before that, so it probably can't go wrong.

What I took with me is that you should get someone to help you.

I think that's a good point.

This role sharing is good.

Someone wrote to me about the acceptance test.

I sometimes wonder where the starting point is when you develop outside-in.

I think that's a very exciting point, because you can start at different heights.

There are people who do TDD, so acceptance-driven test-driven development, and that's where it's actually common.

For example, there is a book by Martin Gertner where he describes it very precisely.

It actually starts with the UI, where the whole application is not only developed and is of course a completely different approach.

I don't have anything left to say.

If you are interested, feel free to go to the Global TF Code Research.

There are a lot of things there.

You are in charge of the data for Nuremberg.

Next week there will definitely be an episode.

I have to see how I organize it exactly.

Probably not on Friday.

Thank you for the invitation.

It was fun, as always.

Have a nice weekend.