# Folge 240 - Domain-Driven Design - Ein vollständiges Beispiel 1/2 where this is exactly the first episode on this topic.

The background is that I have a presentation for it, as you can see right now, and I have actually already held this presentation at various conferences, but when I prepared the presentation, I somehow produced so many slides that it just doesn't fit into a typical conference slot, and then I shortened it somehow to get it into a conference slot, and I thought, well, I could present that at some point, and that's exactly what I'm doing here.

I divided it up, so my expectation is that I won't be able to do everything today, but let's see, that means today it will mainly be about strategic stories, and then next time, I think it should be Friday, it will be about how to actually implement such tactical stories.

Feel free to ask questions at any time.

So, I think we actually have a lot of time to deal with questions.

Yes, and so I would say, let's just get started.

Why this talk, so Domain-Driven Design, has a lot of valuable tools, and the question is now, which of them are actually really useful and necessary, how can I combine them all, and right at the beginning, so to speak, a note, the whole thing may look a bit like a waterfall, that is, we are somehow talking about how we proceed, and we have to have a sequence of the different approaches, but in fact it is about different levels of abstraction, that is, we work from very abstract things onward, up to the more concrete levels, and that means we shouldn't proceed waterfall-wise right now, there are also various people who somehow say that this is not a good idea, but we should proceed in iterations, and we should somehow change this level of abstraction, that is, these techniques that we are discussing here somehow lead to feedback on different levels, and depending on which level I want to get feedback and things somehow, I turn to any of these techniques.

That doesn't mean that they are to be used in this order, but it's somehow about putting them in the right places, to get the right ideas, the right feedback.

Well, the question from zweierleiitdepends said, Hello, Eberhard has invited us to talk about Ports and Adapters and DDD.

I would like to ask my question about the context of this.

Yes, my plan is to discuss this topic, that is, Ports and Adapters or Hexagonal Architecture, in the next episode.

And in fact, the question about the context is a good one.

So, whether Domain Domain Design somehow has something to do with this topic.

Okay, so don't step in again next time, I would discuss the topic then.

Well, let's start with the topic of event-storming.

And now the question is, why do we actually want to do event-storming?

Well, we basically have the following problem.

On the one hand, we have people who are domain experts, and on the other hand, we have software developers.

And domain experts understand the domains by definition, and software developers understand the knowledge, so they know how to generate software out of knowledge, so that it is structured in such a way that in the end, somehow, software comes out of it.

And that means that we now have two roles that somehow have to work together.

So, Domain Domain Design means that the domain drives the design, that is, domain experts know what actually drives the design, but people like me, software developers, architects and such people, somehow have to understand how to structure this knowledge, or have to have this knowledge available in order to structure it in such a way that, in the end, software comes out of it.

And that now leads to the fact that we somehow have to collaborate here, because it's not the other way around.

So domain experts don't know formal methods, software developers don't understand the domains, that means we can't just say, okay, somehow one role will learn the skills of the other role, and then do it on its own, so to speak.

So there has to be a collaboration, in order to create this model together.

And that's what event storming is all about.

Event storming is a relatively low-tech approach, that means you use an event, it's something that happened in the past, that's why I use at least one main word, i.e. a noun and a verb.

And in the past, I wrote that on an orange sticky.

That means, for example, I accepted something like an order, that's now on an orange sticky, and now I have my event.

The colors, the color coding, is something that people value in event storming.

I think the standardization for that is not so bad, and that's kind of the idea.

Maybe at this point a note to the talk itself.

So my goal is not to present a complicated domain, but my intention is to say, okay, that's how these techniques work, that's how they interlock, which means that I have now chosen a very trivial modeling.

So nothing that is super, super complicated.

And that means, that we have a complete example with one technique, but it certainly can be done, which is, so to speak, in line with the typical domain complexity.

So strudelhund69 said on Twitch, thank you very much for all the videos, I always listen to them.

I am very happy and actually the feedback, what else comes from you, positive feedback is very important to me and an important motivator.

So that's just great.

Thank you very much for that.

Good, so that's event storming.

So I write such events down.

And the first phase in which I do that is chaotic exploration.

That means, I say, in principle, build as many events as possible and let the people, then give them free rein, so to speak, to make sure that they implement it somehow.

And then comes next, so logically the events run from left to right.

I think you can imagine that.

And if I do chaotic exploration, that means that this is not really implemented everywhere.

So on the left are the events, which are the prerequisites for the right events.

And that means, what I can do now, is to enforce the timeline.

So I make sure that the events, which are somehow arranged like this before, are somehow arranged like this afterwards, so that they are actually also linearly reasonably arranged.

And I do that by going through the timeline again through this time.

So I determine that the events are actually on the left of the events on the right.

I can also do it the other way around.

I can say, okay, here's some event.

Are the prerequisites actually all there for that?

Yes, then it's very good.

Otherwise, structured events, so that this is actually also there in this order.

Then I can identify swimlanes next.

These are parallel processes, which somehow happen in parallel.

And I can now say here in the example, for example, okay, here's a swimlane, and that's kind of the swimlane where I write in the direction.

So it's an e-commerce system.

Here's the swimlane where I'm delivering something.

And these are more or less parallel activities.

There are touch points.

I have to make sure that an invoice is written when the things have actually been delivered and vice versa.

But in essence, the concrete steps are actually things that essentially run in parallel.

And then there are pivotal events.

These are events according to which the world is somehow different.

There are a lot of heuristics.

For example, if an order is accepted, if a pre-order is accepted, it's relatively easy to say, okay, I'll pack something else.

Then I have the shopping cart.

After that, it's difficult.

So actually, it's already being sent.

And I can maybe only store it as a whole.

So that means the world is different.

And there are, because it's more difficult, not to order things anymore.

And it's also the case that there are new objects.

For example, there is the invoice, there is the delivery, and so on.

So that means that I actually have a different world there.

Here, for example, is something else.

So the package is now out of my warehouse.

That means that I can no longer say, okay, I'm not sending it out anymore.

But it's somehow in the responsibility of DHL, which means, for example, that if it's lost, it's their problem.

And that's maybe something where the world looks a little different.

And that's a Pivotal event now.

Order accepted would be more clear for a Pivotal event, because it's really very fundamental.

Pivotal is a fundamental change.

That the package has now left the warehouse is maybe a little less Pivotal, so to speak.

So that's maybe a little less clear.

Advantages of this.

This is relatively low-tech.

That means it's easy to understand for domain experts.

So I write an event on a map, do something that interests you.

That's what you should typically get.

People can work on this thing in parallel.

Because I have a wall, there are all these things somehow attached.

And it's very easy to work in parallel with many, many people.

Which might not be that easy otherwise.

And I think that's one of the non-obvious things, which are actually very important.

The social structures become obvious.

What I mean by that is, I see who works with whom, who understands things, who are experts for certain things.

And I think that's also an important point.

That means I have a kind of laboratory there, where all the people who are supposed to work on this whole thing, technicians, domain experts and so on, can show how they actually do it.

And that makes a lot of things obvious.

Challenges.

To get the right people into the room.

Domain expert is a bit of a difficult term.

There are people who use the system every day.

They know how the system actually works.

Then there are people who say, okay, why are we investing now?

Why are we building something?

These are people who have a vision and can discuss it on this level.

And I need both.

And ideally, I need people who are actually still working professionally with the system, but have a sustainable vision.

So I need people who just say, this is how the system works now.

This doesn't help me to develop the system further.

That's why I need a combination.

In other words, people who really use it, maybe don't have the vision and the context.

Managers may not have this understanding of how it works in everyday work.

And every person who is involved in it understands only part of this logic.

And I have to get them all together now.

The result of this is a common understanding of the domain.

And thus a model of the domain, which I have to change first and have to adapt before I can implement it.

So that means I actually only have the opportunity to get this common understanding up and running.

And here it says, as I said, the roles and the collaboration will be obvious.

Then let me take a quick look.

Oh, right.

I think I'll finish that briefly.

A few questions have come up.

I think I'll actually finish that briefly.

So alternatives to domain storytelling.

This is more process-oriented, but also something where I write and paint things collaboratively and work on it together.

And something like context mapping, where I just paint up contexts and say, okay, these are the contexts that I see here and these are the functionalities of the contexts.

Who cares?

There is an episode about domain storytelling with Stefan and Henning, who also wrote the book about it and invented it a bit.

So you can watch domain storytelling.

There is this episode, we build a software architecture.

There I show how I can do context mapping, how I just put things together that have a common functionality.

And there is the episode on the subject, designing an architecture, for example, the ISRQB example task.

And I actually discuss how to do context mapping based on the architecture example task.

So now let me briefly go into the things from the chit and I'll briefly show the slides for that.

Question, now Feierlei Etipenz has written, the model between the heads, is that your domain model?

And maybe you can briefly say what is between domain and domain model?

In my opinion, important.

So a model is for me a more or less formalized a more or less formalized recording of what is actually happening out there.

And we have such a model here now.

So we have these events and they show what is happening out there.

CRUD is another model on a more concrete abstraction level.

It's just that I actually implemented these business processes so that I can run them in an IT system.

Here I only have a common understanding through some events.

These are somehow models, so things that tell me something about reality, so that I can reflect on it.

And this joint development of the models is actually the core task of software development.

The model that this is all about is of course the code, but the other models, such as event storming or domain storytelling or context mapping, are also exciting because they are prerequisites for us to get such models at the F3.

Jan wrote, I don't need a lot of tool support to work with CRUD, with a twinkle smiley.

Exactly, that's one of the features.

And maybe at this point Miro is also your friend.

That means if you have that, or concept board, or whatever is flying around, Miro, that means you can actually do these things with tool support remote.

And that's also a thing that I think makes sense.

So I like the digital tools better now than the post-its, because with the digital tools I automatically have the stuff archivable somewhere and I can copy it relatively easily and pick it up again, and so on, and so on.

And I can change it remotely together.

So by now I think it's maybe better.

Wasn't the result even something to throw away?

It should be shared know-how and an artifact can be created.

Yes, that's a good point.

That's how I can pick it up.

I wouldn't be so orthodox and would say I'll throw the artifact away.

But the idea to say maybe it's not about the artifact at all, but it's about that we have this process and exchange knowledge and especially to observe how this artifact is created.

That's true.

That's a good point at this point.

Nafetz Nesniv wrote LOL managers have no idea.

Zfenka Smiley I find it difficult.

They should at least be able to say why we're spending so much money to implement a new piece of software.

And at least on that level they should be able to say something.

I think it's important for event-storming that all involved groups can actually participate.

And I wouldn't exclude anyone.

So, as I said, a vision that says why we want to make it better from a management perspective can be very valuable.

Philipp Sporrer says should you always deal with the entire business process in event-storming or can you also make use of sub-areas?

How should I put it?

That's a good point because we're discussing a lot of techniques.

And I would say a technique should solve a problem.

And whatever your problem is, if you think the technique can help, then use it.

Event-storming for a sub-process is fine in my opinion.

If the system is big enough, I will probably bring in different people in several sessions to investigate different sub-areas.

And that's a result of complexity.

Mark M. writes there's Ruth Malan who deals a lot with system design and contextual design.

Domain driven design is a good example.

It's probably also linked to systems thinking.

That's what I'm saying here.

With systems thinking I'm also trying to look at the social component.

And I can do that with event-storming because I see how people work together.

Question 2.

Did you make asynchronous formats from your workshop experience?

Uhm...

I'm not sure what asynchronous formats mean.

I would try to make these things we're talking about now, like event-storming, synchronous.

Because otherwise I would have more difficulties.

I think if you have everyone virtually in a common room and let them work on it, it's probably a lot more productive.

I've never done anything asynchronous before, and I think I would advise against it.

What is the connection between system thinking and system design and this video, including Lisa's?

Lisa made two videos, one with Diana.

I think an essential point that we have to think about even more is that we have to see systems integrated between social and human relationships.

The system is inevitably what this social setting has created, and that is part of the explanation for what it looks like.

I also like the question, this discussion with, is this really the artifact that is so relevant?

We have a learning process here, we see how people interact, that is perhaps even more important than the artifact itself.

We had an episode with Xing Chao some time ago, she said exactly that, and I still think that's a very exciting and important point at this point.

Thank you for the answers.

I think we can continue.

I'll tell you something about building a context.

Why build a context?

It's a granular division of the domain.

Something that I can assign to a team.

A team can also work on several building contexts, but a building context should ideally belong to a team.

You can also discuss this.

Building a context is a very nice name.

These are boundaries in which a model exists.

In this case it is code.

So conceptually the idea.

And on the other hand, the ubiquitous language.

So a common language.

And here, at least in Stream, we have a standard example, the famous Nali, the replication.

And that is something that is known in a building context, with a certain customer.

And the idea is now that this is part of this ubiquitous language.

And that is ubiquitous in the sense that I have it in the code.

So there I would have a class replication or Nali.

If we were in the database, I might have a table for it.

And that would now also be something that software developers and domain experts need in everyday conversation.

And that's how I get into this communication.

I have a simplified communication.

So I can now set myself up and say, okay, the replication.

And then I can ...

So not that we're just here.

That is, domain experts say, we deliver things when the following conditions are met.

And I can now, if I can set myself up as a technician, say, okay, all right.

That means there is a class replication, I'll just write it in.

And that makes the translation easier.

It would be more difficult if there was a delivery or a post-delivery or whatever you could think of.

But I want to have exactly this post-delivery in there somehow.

That leads to, for example, if I look at the invoice process and the delivery process, that I want to have certain information there.

So, for example, in the invoice process, the customer who paid the bill.

And in the delivery process, the customer to whom the products are sent.

And there are potentially two different ones.

So if I order a laptop at the expense of Swag Lab, then Swag Lab is the company that pays the bill.

And I'm the one who has to deliver it.

Swag Lab in Hamburg, I'm in Kaiserslautern.

And I'm kind of left out if that gets mixed up somehow.

A classic example is also the hotel check-in.

At the hotel check-in, it is now the case that I somehow say, I'm the Ebert Wolf and I live in Swag Lab GmbH, Simon von Utrechtstrasse in Hamburg.

Because I would like to have the invoice at the end.

And that's kind of difficult.

That's why I only enter the invoice address now.

And because the domain modeling is not clean, they actually ask for my home address, because they need it for registration.

And they have to report to some people so that they know who it is.

And that's the problem, that this modeling is not clean in this typical hotel system.

And I try to counteract that, so to speak.

Should architects take influence that the language may become a little more generic?

Yes.

So, in general, it's just that we forcibly concretize this language a little bit now.

Because we have to build some kind of class.

So I can go back a slide, so to speak.

And then we find out, I have this NALI or after delivery in the code.

And you can't see it.

There is the NALI and the after delivery.

One is an acronym for the other.

Or a abbreviation.

And now I decide that I write after delivery here.

Or NALI.

I have now given a term, because that's the one in the code.

Apart from that, I wouldn't try to make it too generic.

Our goal is, on the contrary, exactly for the business problem that exists there, to build a solution.

And for that I would try to be very specific.

Generalizing is difficult, because it's difficult because I can't predict what I'm generalizing about.

So I always have one example, a NALI, a after delivery.

What is the general one?

No idea.

And then the question is, whether I want to generalize that.

In many cases, generalization, especially early generalization, is difficult, because it leads to concepts that are not general.

And then the system becomes unclear and difficult to maintain, because you have chosen the wrong generalization.

So I told you that.

Now the question is, how do I get to my contexts?

And that's one of the things where I've already done a few things with event storming.

That means I can now identify candidates here.

And candidates are exactly these areas here between the pivotal events and the swim lanes.

That means I can now say, okay, I have an order process, which ends with me accepting the order.

Then there's a swim lane that does something about invoicing.

Then there's a swim lane for delivery.

And now I decide that we have exactly these three buildings and contexts.

And what I've done now is that I said, there was a pivotal event in the middle of the delivery process.

Namely, where the package, so to speak, went out of the warehouse.

And now I've decided that this part is not enough to start a new building and context.

So the language is essentially identical.

So the thesis, I basically strike that with the same code model.

So it's a model.

And that's kind of a discussion that you could lead.

You could say, yes, I want to have something new.

Yes, exactly.

That's just an architectural challenge.

What are the advantages?

So another note first.

These are just candidates.

I still have to think about design.

For example, here we said, I have decided that a pivotal event, at least not now, that divides these systems.

And then there are questions like, how is it that if I get money back now, is it that I do it with the same model as the calculation?

So that's maybe this story that Nafels asked earlier.

From whom should that be a generalization?

No idea.

You could now say that I do it with the same model.

So if I give someone money, I give the document in the hand and money.

When I write an invoice, I have an invoice and I get money.

That could be that I build the same model for it.

That means I have a big code block, it can write invoices and it can also perform re-equipment.

You would have to discuss that.

And then there is exactly the other question.

If I give something back, is that also done by the delivery process?

That's a similar discussion.

And then there is again the question whether it really is the same.

So that's just the way it is that in the delivery process, a goods is sent out.

With a return, a goods comes back to me.

Is that the same model or not?

No idea.

That would be a story that you have to do professionally.

Advantages of this.

We have thus structured the domain logic on a granular level.

And if we do that, if we now say that things that belong together are actually together in a building context, that is, specialties are implemented in a building context, then that implies that we only need a building context for each specialty.

So we have things like create the invoice, calculate the invoice amounts or in delivery, I send out this clicker or whatever.

And these things are implemented in one model.

What does that mean?

If I want something, I will probably end up essentially in a building context.

And if I want to change something, I typically end up also in a building context.

It is clear that some changes may include several building contexts, but that is more of an exception.

So I would say this is a good architecture because it actually divides well.

Challenges.

Well, legacy systems, because they often have different models.

If I tell people something about building contexts, they usually come to some ways and how these systems are structured.

And that's just difficult to consistently shift the responsibility for some specialist features somewhere.

And that's just hard to get used to, so to speak.

That's why this generics may be a problem for me.

So it's especially about functionalities.

So what I'm saying here is we have the ordering process, deliver, write invoices.

And we don't have real customers or something like that.

So we're on functionalities.

We're not on data.

And the results are now building contexts as models for these business functionalities.

Small, loosely coupled models.

A change will typically only kill a model, which means that I have a loose coupling there.

I made an episode on the subject of building contexts, where I show that it's much more difficult.

The concept is a bit ambivalent.

We've already seen two things here.

A building context is something that defines a language, so it's language-bound.

But it's also something that's model-bound.

And then there's the third thing, that we're actually talking about something that typically deals with teams.

And then the concept is very overloaded.

And that sometimes leads to difficulties in practice.

Jan wrote, I once heard the quote that you should have implemented something three times.

In my opinion, it was more in the direction of reuse.

Exactly, there's this episode with the...

I'll take a quick look.

It was exactly about this topic.

No, you don't write like that.

Ah yes, with Bert-Jan Schriever about generic or specific.

That's exactly what he said to me.

So that's a measure that you can have.

Here you can see that the question is, what is technically correct?

So it's technically correct to say something like a calculation and something like a return, that's actually the same, or that's technically incorrect.

And that's actually the discussion I would lead.

So Max asks, how important is it to ask the right questions?

That's super important, of course.

And in general, in the consulting business, it's an important topic.

Also when creating a portal.

Question 2, a browser makes a request to a port.

The port is in an application where it's the non-technical.

Is the sticky the request?

Yes, good point.

So actually I mean a request in the sense of a HTTP request or a method call.

What I mean by that is, a specialty is typically implemented in a built-in context.

That's what I mean.

And that means if this specialty is used, then I end up with a built-in context for a module.

And Mark writes a request in a built-in context, a team, a module.

So is that still valid?

Yes, maybe.

So I talked about that.

A team can manage at least several built-in contexts.

And in reality, it's more complicated.

But actually, I think we still wanted to go in this direction, because then we have a good specialist division of the system.

Good.

Then I think we'll go on.

And what comes next is the story with the core domain.

And why is that relevant?

Because we have to understand the focus.

So we have to understand what is it that is particularly important to us.

And this core domain, that is typically the motivation for the project.

And we are now reducing the complexity of this model.

Especially for this part, we want to reduce it so that it is particularly maintainable and changeable.

And there should be particularly good maintainability.

And we can now ask the question in this system, where might the core domain be?

So we have order, process, invoicing and delivery to choose from.

And as I said, this is a lecture that I have given more often.

You can now briefly think about what you think what the core domain is.

And most people say that the ordering process is what the core domain is.

And probably because that's where the money comes in, so to speak.

Well, our differentiation is that we deliver fast and reliably.

In fact, I have been seeing advertising spots from a company that promises exactly that.

So it tries to differentiate.

And that's why the core domain would be this delivery process.

We say here I would like to be particularly good in the delivery process.

That should be particularly changeable.

And that's what the core domain is.

The rest would now be generic subdomains.

So things that you can simply sell in the extreme, which are actually completely generic.

Or maybe supporting subdomains, if they are complicated, I build them myself and have to add the core functionality.

In fact, I was in a project where we bought this ordering process.

That's what you get with Shopify.

And what we focused on was the product configurator, which was incredibly complicated.

And that's just an example where we're talking about the core domain, which in this case was the product configurator.

And the other things are, for example, the ordering process is a generic subdomain.

So in contrast to what the majority says, your process doesn't necessarily have to be the core domain.

It could be theoretical, but I don't know.

And if we can get that out of the way, then we have a clear focus there and we have a better understanding of the domain.

So what we get from this is, strategically, if I take technical responsibility, the delivery process is important, I have to take care of that seriously.

That's really bad if it doesn't work properly.

And I understood, we are, we differentiate through the delivery process.

That means I understood what my domain approach looks like.

That's additional information.

And that's a bit of an advantage there.

There seems to be no questions.

Then I would, I think at this point, just go on and move on to strategic design.

So that's kind of the question.

So somehow teams don't have to collaborate with each other.

And especially now that we have the core domain and the core domain has to be supported somehow by the other parts of the system.

So that means we still have to make sure that this core domain is successful.

And my claim is, we can't do that just with architectural aids.

So we have the delivery process.

The delivery process, for example, depends on that the information comes from the order process.

I can't deliver anything if I don't know what the order looks like.

And with that, the order process has to provide an interface for the delivery process.

And if anything changes, the delivery process has to follow suit.

Nonsense.

The order process has to provide the right information to the delivery process.

I need more information, and then the delivery process has to say, all right, we'll implement that because you're more important than we are.

Delivery process is what we're differentiating ourselves from.

And that's exactly what strategic domain-driven design is actually doing now.

That means we have to prioritize the core domains on this organizational level.

We can't do anything architecturally.

We have to say, you're more important.

And that's exactly what strategic design says.

Strategic design has patterns that overlap with collaboration.

So, for example, customer-supplier.

The supplier team, the delivery process, the customer team, the order process, would support the customer team, the delivery process.

So it would mean the following.

I have the team for the order process, and I have the team for the delivery process.

And I say now, you, dear team, that you are responsible for the delivery process.

You are the customer for the other team.

That means you can say, I want to have the following things.

And then these things are built.

Of course, there are negotiations about how exactly this should happen.

So no, there is a discussion about the budget, how long it will take.

We have to talk about testing, how far the interface tests and so on.

But in essence, this team for the order process is a supporting function for the delivery process.

And the opposite of that would be the conformist pattern.

In this case, the team, the order process, would ensure that the delivery process is in a conformist role.

The delivery process has to live with what is there.

And this can result, for example, in saying, well, I would like to change.

I would like to provide you with other information.

I would like to support you.

I just can't, because our software is unchangeable.

And then I'm in a conformist role.

Then that doesn't mean that I have to live with whatever is delivered to me.

This is a result of Core Domain.

This is what the impact of Core Domain is now.

And my problem here is, so far I think it's all logical.

So I say the delivery process is like the Core Domain.

I'm trying to make a customer out of it for the supplier order process, and so on, and so on.

And the challenges I see there are that it's hard to get it in order.

And it's relatively complicated.

So I've shown you two patterns here, because I didn't feel like painting all ten patterns or whatever.

And it's not particularly intuitive either.

These two patterns are still intuitive.

But there are patterns that define other things.

For example, say something like Published Language.

There is a data structure.

This has little to do with prioritization.

I'm talking about data structures all of a sudden.

And that's why it's like that for me, that I'm pessimistic overall.

Because it's not intuitive.

It seems too complicated.

And that's, how should I put it, not an abstract criticism.

But it actually leads to the fact that, in my opinion, it is not adapted enough.

So it's actually true that it leads to real difficulties.

Because it's just difficult for people to implement it.

And the other point is, we're actually only talking about teams here.

We're talking about building a context.

And if I'm building a development platform, for example, then I'm not building a context.

And that is, strictly speaking, no longer part of these patterns, because I'm not building a context.

And that's at least conceptually problematic.

Because I have teams that take care of other things, not just building a context.

And that's why I find strategic design difficult now.

Exactly, question two has asked, can you still build the results of DDD in layers or layer architecture?

We'll discuss that next time.

So actually, is layers a DDD pattern?

Mark M. wrote, many architects use the term business capabilities.

That seems to be a task definition.

Does that come up with you in your approach as a concept?

No, it doesn't.

And somehow that's domain-driven design by the book.

So business capabilities is something that I know from enterprise architecture management.

So, when I say that strategic domain-driven design is a bit problematic, then I feel obliged to say how I can do it better.

And I would like to briefly go back to team topologies.

So somehow teams have to collaborate with each other now.

And team topologies, in my opinion, are not that super complicated.

Relatively intuitive.

At least I find it somehow clearer.

And it contains more fracture planes than just building a context.

So, for example, something like location.

That is, there is somehow not said, okay, we divide the teams only by expertise.

But somehow it is said that there are also other things, such as when teams sit together somewhere or people sit together, then they can perhaps form a team.

In times of remote work, this is something that may become less and less important.

But otherwise, if you can meet in a room, that is often an advantage.

And we're talking about more than just development teams.

What are there?

There are Stream Aligned Teams.

Stream Aligned Teams are teams that completely cover a change stream, i.e. from demand to production.

Then there are Enabling Teams, teams that support these Stream Aligned Teams to build up certain skills.

Then there are Platform Teams, which offer a platform, Kubernetes, CI, maybe also something business-like, so maybe a payment system or something.

Complicated Subsystem Teams, which include some complicated algorithms.

In my example, there are different collaboration options.

Access to Service means that I implement an interface.

This could be done by a Complicated Subsystem, or a Platform Team.

This interface could either be programmatic or an interface that I can use over a user interface.

And then there's something like Facilitating, so that I look at what the teams are doing in a certain area and support them.

Or Collaboration means that I hire someone who then actively works with this team on a certain challenge.

So, we can now interrupt that in our case.

So, I have Invoicing, Order Process and Delivery Process.

Then I have a thing that says how I want to deliver things.

For example, there's this logic for this after delivery.

And they now offer an interface, an Access to Service for the delivery.

So, this team here, delivery is responsible for any change that has happened there, from analysis to production.

And they now offer a thing that I can say, hey, Eberhard ordered these things, what do you want it to be?

A laptop and a washing machine.

How do I get this delivered to him?

And then the system will say, okay, unfortunately we have to send a shipment for the washing machine and we have to make the laptop extra, if it would have been something else.

If I had ordered two laptops, he might have summarized it, whatever happened there.

So, and that's actually a very specific algorithm.

You can imagine that it's very complicated to implement it.

And that is now offered to this team as a purely technicality.

And in building contexts, this is perhaps the same building context, this optimization and the delivery process.

Here we separate it, because we say this algorithm is so complicated and that is something that this other team has done.

Then we have the Kubernetes CI team.

That offers Kubernetes clusters and somehow ensures that you can book them via a website or via an interface.

Then there is the architecture team, which either ensures that the other teams build up architectural skills or maybe even hire someone to make sure that some architectural problem is really solved there.

So we sit down together and we build the thing really finished so that the team builds up this skill and at the same time it's also a feedback channel.

That means I somehow notice where there are difficulties and I somehow notice as an architecture team where I have to get better, so to speak.

Results, the team setup is defined and also the collaborations are defined.

Challenges, these are magnets.

So that's kind of a target image.

And I made an episode about it.

Here is the poster that Lisa created for it.

You can also download it.

You can look at it for an hour.

And I discussed a few practical things with Kim about it.

I would like to go back to this problem with the org charts.

For example, I now have streamlined teams and I want to take over some common functionalities in a platform team.

Some common business functionalities.

And that's a story where I would say, hey, abstract, that might make sense.

That means that I can now say from a purely architectural perspective, listen to me, we're going to investigate this.

Yes, these are actually common functionalities.

We implement it once, so to speak, centrally.

So that was the question here.

Should we involve a platform team?

There are some common functionalities and that might make sense.

But it was a toxic environment.

Problems were not communicated.

And if you said, by the way, I have problems, then there was a punishment accordingly.

And that leads to the following problem.

I can stop.

So if I sit down now and say I'm a streamlined team and I want to use this platform, then I can't trust the platform team because they won't communicate their problems openly.

That means they will hide their problems.

And then I have a risk because I'm a streamlined team.

I have to achieve certain goals.

And I'm now dependent on this platform team.

Maybe I won't reach them because of the platform team.

And then I have the problem that this streamlined team punishes me for it.

And I have officially failed.

And then I'll probably say, okay, I'll build the platform myself, because then I have it under control.

Then I know that I have a problem.

I can manage it.

And that's a decision that's completely independent of whether it makes professional sense, so to speak, but is only driven by me trying to manage my risks.

And that means that we may also have a more general problem here.

People don't necessarily work the way it says in the org charts.

That means you have to solve these problems first.

And we have informal communication channels.

So I can talk to some people informally.

I can somehow make sure that they solve it.

And that's a topic where I...

We've done a lot of episodes.

For example, we also have too much of the change that I can let work for me.

But that's something on a different level.

And I added this earlier, because painting an org chart, as it is said in team topologies, that's not enough.

And that's what the team topologies book itself says.

So the problem with org charts is a chapter headline from the team topologies book.

Nesnif writes, Unfortunately, there is always stress with the responsibilities in the different teams in the approach.

Maybe that's a cause for it.

So these informal channels and what is a responsibility at all.

How should I put it?

That's something that's actually in the consulting on my topic.

Explaining team responsibilities, so to speak.

I'm not sure if I'll get that through org charts.

And Jan just wrote it.

Org chart is not a communication chart.

And that's something where...

I have to collect my thoughts for a moment.

That's why I chose this example.

So I said to myself, Okay, it might make sense to have this platform team.

But by mistrust, it may be that I can't actually implement it.

And then I have a problem with that in the end.

So question two, It depends writes, Own rationalities.

So every team has its own rationalities.

This creates risks for other teams and advantages.

I think, to be honest...

So we did this episode.

I did it together with my colleague Michael about this topic with corporate politics.

And yes, own rationality and weighing your own goals against each other is, I think, an essential point for corporate politics to get this balance there.

I think that in reality, it might go a little further.

So it may be that some teams, that's why I chose this toxic example, are actually not helpful.

Maybe forced by the environment.

So they may not be helpful.

And in the extreme case, it may even be that there is, how should I say, a competition and an unpleasant overall situation that leads to that there is such a destructive competition.

I wouldn't rule that out.

But then I have a completely different set of problems and that is certainly not solvable with OrgCharts.

And then there may not be a serious solution on this level.

Philipp Sporrer writes, How do you identify the streams?

So are there heuristic methods for this?

I have to say again, These streams are change streams.

That is, it goes from the requirement to the fact that something is being implemented.

And so as far as production is concerned.

That means, essentially, these are streams that ensure that we can implement something and it goes to production.

And the special thing about team topologies is that there is a variety of fracture planes that can assign very different things to such stream-aligned teams.

So here we have seen, there are, for example, built-in contexts.

I think that's a pretty good model.

I could, for example, have something like personas.

So new customers versus existing customers would be a possibility.

And I can, for example, have something like a UI.

So not just a UI, I can also say I want this change and then I pass it on to production.

And a stream-aligned team could do that.

That means these stream-aligned teams are actually very flexible.

Because that means that almost any change channels or change streams are conceivable there.

So that's why it's a bit of a question of how to identify them.

It's a bit, how should I put it, that's not the question.

I assign something to these teams and team topologies are actually relatively flexible.

Question two, three writes, it's nice that you have a surrounding interview with a boss on the subject of your own rationality.

Exactly, thank you very much.

Oh, thank you for the, there was even more positive feedback and people who left likes, so to speak.

Thank you for that too.

Then I think we're actually through so far.

And we can, so to speak, take another look ahead.

On the 29th, that's the week after next, the episode with Lars.

Ralf talks to Lars on the subject of Generative AI Beans Software Architecture.

And yes, then there will probably be an episode on Friday where I continue this here and then talk about tactical domain design.

I don't want to rule out that there will be a third episode.

We'll see.

It just depends on how things go.

Good.

Let's see if I've forgotten anything.

That doesn't seem to be the case.

Then I would say, yes, thank you for watching.

Thank you for the positive feedback.

Thank you for the questions.

And then we'll see you next time.

Exactly.

See you then.