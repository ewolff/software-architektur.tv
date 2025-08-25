# Folge 241 - Domain-Driven Design - Ein vollständiges Beispiel 2/2 I have one more note.

There is this training, Domain-Driven Design, Saniert Legacy, that is one afternoon on the 16th and 12th, about Socratory.

It is not particularly expensive, if you are interested in this topic of Domain-Driven Design, especially the handling of legacy.

This is an opportunity to actually experience something very practical with me again.

So we do practical exercises and not only talk about it, but also do it.

And that is, I think, a good addition to what we see here.

Because, as I said, here we don't see how to deal with legacy.

Well, the first thing I actually want to talk about is the topic of tactical design.

That's also a bit of a breaking point for the last time.

So we talked very roughly about the whole thing last time.

So how do I divide a system into building contexts?

How do I somehow build?

What responsibilities do teams have?

And so on and so forth.

And this is a completely different level here now.

This is actually the level of classes.

And why tactical design now?

So tactical design are object-oriented concepts.

And it makes a lot of sense to me to build good object-oriented systems.

Tactical design is exactly what helps.

We can go through the patterns now.

The first pattern is an entity.

That's something that has an identity.

So a person has an identity.

That means, if I give the Eberhard Wolf again, there is now a completely identical copy, which looks like me, who lives there, where I live and is not so much identical.

That's still another person.

I can somehow distinguish them.

And that means that things actually have an identity here.

A person has an identity.

A product has an identity.

Such stories.

And something like value objects, i.e. a value such as 2 euros or 2 meters.

2 meters are just 2 meters.

And it doesn't really matter if these 2 euros are 2 euros.

So these are actually things that only differ in value.

Then there are domain events.

These are things that are relevant to domain experts.

So something has happened in the past.

We talked about this last time.

This is also something that plays a role in event storming, for example.

These are things that I can implement as classes.

Maybe two more general things.

The one general note is that what we see here is that we have a fundamental dependency from top to bottom.

That is, these are actually basic things that depend on nothing else.

And the other thing is, we're talking about a real object-oriented concept.

That means the things we see here have logic.

So if I say, for example, I have 2 euros.

I can somehow sum amounts of money.

And I can try to round them.

And whatever else I can do.

These are things that I will model in this value object, for example.

So these are things that actually contain logic.

So, based on that, there are these aggregates on the next layer.

They are made up of several different things.

That's why they're a little higher.

So that means there are entities and value objects that are summarized in aggregates.

And there is an aggregate root that is now responsible for ensuring consistency there.

That means, for example, if I have an order and I add something to this order that I would like to order.

Then this is added to one and the other ensures that the total amount of the order is adjusted accordingly.

Then the thing is consistent in itself.

And the aggregate root ensures that this change takes place automatically.

Which means that consistency conditions are implemented synchronously within aggregates.

Not necessarily synchronously across aggregates.

And I can also use aggregates to replicate them in the network.

Then I also have eventual consistency.

That means that all aggregates will eventually become consistent.

This is interesting because a transfer, for example, changes two accounts.

Now you might think, I want to have that consistent.

And what Domain Driven Design says is, no, the account itself is consistent.

So on the one hand, the amount would be correct.

I have € 240 after the transfer.

And on the other hand, the transfer is actually booked or nothing from both.

But the accounts can be inconsistent.

Which, by the way, is exactly what reality looks like.

If I now transfer money, it is somewhere between these two accounts for some time.

So the money has been lost for some time.

At least that's what I assume.

So that's what plays a role here.

What this also means is that in contexts that are roughly granular, not total consistency in itself, but aggregate consistency.

This consists of entities.

So my individual bookings would be, for example, some entities.

And value objects, the account balance, for example, would be such a value object.

Then I have repositories.

They give me the illusion of a collection of aggregates, which is apparently stored in the memory, but is actually in the database.

This is also a conceptual thing.

And what I find particularly exciting is that repositories also implement the right questions.

That means a repository will not say, I'll give you access to any objects, but the repository will say, okay, I now have the option of finding an account number, maybe also according to the name of the account holder and the date of birth, but not based on the account balance, because that somehow doesn't make any sense in terms of subject matter.

And that would mean that the repository only exposes the subject matter of queries.

Which I think is a very interesting design concept, because something like GraphQL, for example, says I can ask any questions.

Repository says that doesn't really make any sense.

We just want the subject matter-correct requirements to be able to ask questions.

Then there are factories.

Factories generate complex value objects or aggregates.

Very similar to for patterns.

I don't think you need to say much about it.

If a constructor is not enough, I use a factory.

And then there are services.

Services are the things where I can't use business logic in a sense in an aggregate or entities.

So there is business logic that is interdependent over different aggregates.

So the transfer, for example, is something where I have two aggregates.

So now I can't assign the two accounts to an account.

So I'm probably going to build that into a service.

And that makes it clear how it works.

I say I have some logic.

I'm going to put it in one of these classes.

And it's not like entities, for example, should be logic-free.

So now the question is, it's something that goes through this talk.

I think it's always important to name alternatives.

So we now have tactical domain-driven design.

And now the question is, can I not implement tactical domain-driven design?

And one way to do that is to make it functional.

Then I have a side-effect-free functional core.

That means I don't have entities, I don't have aggregates.

When I change an entity, it has a side effect.

The thing has a state.

The account has an account state, for example.

And that means this state changes.

This is obviously a side effect or an effect.

And with functional programming, I can't have that.

That means, with functional programming, I would have a core that says, okay, I'm calculating the new account state from a set of interest.

But then it's the job of the system all around to ensure that this side effect is generated, that this information is actually stored.

So I would have a core that says, okay, this is the new account state.

And then I would have something around this core that ensures that it is actually stored in the database.

I talked about this topic with Mike Sperber some time ago.

In fact, that was more than a year ago.

So we discussed what a functional architecture should look like.

Mike is someone who has dealt with it a lot.

We looked at the ISRQB example task.

So you can talk about this topic in detail.

What other alternatives are there when I have less complex systems?

So the premise for this set of patterns is, I have complex business logic.

And if I have a system that copies data from A to B and I'm building a repository and aggregates and entities and value objects and so on, then the question is whether that's really smart.

Because I invest a lot of effort in building these things.

But the advantage that I have object-oriented possibilities to structure my logic, I don't have that much of that, because I don't have any logic.

And for that there is an alternative, something like a transaction script.

So a transaction script says, I process a request from the presentation layer directly and have a database code in there.

So that means I have an HTTP request that comes into my system and then I say, insert into my great database table some value.

And something similar is a table model, where I say, there is an object that represents a database table.

And that has the advantage that I don't have all these layers.

And I can relatively easily say, okay, if that comes from the HTTP layer, then I change exactly that in the database.

And I see that at a glance.

Of course, that goes massively wrong if I have complex logic there, because I would have to rub it in somehow.

And that doesn't make much sense.

Here, for example, I also have the advantage that I can now optimize the database requests, for example.

I can now build in hand-optimized queries and construct some great things there without having to go to a lot of effort.

Let's go through the example.

The example we had was an e-commerce system.

That means we would now take one of these building contexts out.

I have now taken out the building context with the delivery.

So that's the thing that says, okay, I want to send the clicker.

How do I actually send this clicker?

Or if I have something cheap, the iPhone, that's even more expensive.

I might want to send that to the insurance company again, and so on and so on.

And that's what I want to decide here now.

That means I have some logic and start now and say, okay, I have an entity here, so I have a package.

I have an address, that's a value object.

So you can see it from Utrechtstrasse, where the Swaglab GmbH is located.

That's a value, that's not an identity in this case.

And I have that together in such a delivery.

So that means in this delivery it says, this package goes to this address.

Maybe there's some information in there like, what goods are actually in the respective package?

That's how I assume it now, to build complicated, that I need a factory for that.

And I also have such a delivery repository, where I can now say, give me a package for this customer.

So that would be something that I might be able to motivate in question, that I would like to have in this car.

That would be something that I might be able to motivate in question, and so on and so on.

Alexander is writing, I'm a big fan of DDD, and I think it's way too little that people talk about, where you shouldn't use DDD.

Good that it was mentioned here.

Exactly, thank you very much.

Another actual gap that I can have now is, for example, a customer.

And I would have some information there now.

Maybe he sent me a set of addresses, multiple things, or whatever.

But then I would have a service here that says, okay, I'm just scheduling a delivery.

So I say, for this customer, I would like to have this delivery somehow.

And that means, this thing then ensures that these deliveries may arise, needs access to the customer.

So now I can hardly give it to the customer or the delivery.

The delivery would have things like, tell me what your value is, tell me if you're insured, things like that.

And this general logic would now be in such a service.

And I still have such an event here.

The delivery has somehow been scheduled.

That means, I have now said, this and that should be delivered then and then.

And now anyone can react to that, if this person feels like it.

I had a whole episode about it, where I discussed it again.

It's actually from this year.

And I'm actually talking about all these concepts for an hour.

And I'll go into more detail about it.

The question is how I implement that.

And in a way, what we're discussing here is plain old Java objects.

So that's actually just an object-oriented construct to somehow divide up logic.

And that's why that could be enough.

What that means is, I don't have any special technical requirements here.

So I might still want to save entities.

That means, I might have something like that, that I want to have a persistence solution.

Maybe there's a persistence solution in the repositories, that actually implements that.

But essentially, I just have an object-oriented system here.

And there's something like xMolecules, which supports the concepts directly for different programming languages.

And that's what the good Oliver Rothbohm described in a blog post.

And that's what we talked about.

That means, I can now build such a system with something like jMolecules.

And it's also about dependencies, for example.

So I would like to be able to use aggregates in a service, but aggregates shouldn't use services.

That means, there are relationships that result quite directly from these patterns.

And that means that I actually have these dependencies, like, for example, that services are allowed to use aggregates.

And I can use such architecture management tools.

So the architecture management tools, I've actually had several episodes about that.

Incidentally, I also link all of this in the show notes.

These are tools with which I can somehow say, okay, services are allowed to access aggregates, aggregates are allowed to access entities and value objects, and so on.

And then these dependencies are implemented, so to speak.

That means, I have a checker that runs over it and says, no, you can't do that.

And there are very different tools.

So there is something like Structure 101 or such a graph that somehow shows it more graphically, which I can also get into the image process.

There is, for example, something like ArcUnit, where I have it as part of the unit test.

And as I said, there is a big selection and you can look at all these tools, so to speak.

So, in that context, I would like to talk again about the topic of design-level event storming.

We talked about big-picture event storming in the last session.

And big-picture event storming is ultimately something that I have domain events.

I have domain events and I write down these domain events somehow and get information about how my domain works.

And I can use that, for example, to identify building contexts.

That means, I have such stories there, typically, like, I made an order, the thing is now delivered to me, things like that.

Then I can somehow say certain functionalities, so the delivery and the accounting writing is perhaps in different building contexts.

We talked about this last time.

So, Jude Rude writes, which objects should not be immutable and thus have no logic?

Exactly, they represent value and values are immutable.

Two euros are just two euros.

I can't say two euros are suddenly two euros and 10 cents, but that's just a value.

Which means, for example, if I have the value of my order, and the old value object is still there.

In other words, they are unchangeable.

They have value semantics.

And also...

How should I put it?

Things like comparisons are also a topic.

If I compare meters or compare money amounts, maybe that's something I have in there as logic.

So they also have logic.

That's exactly the idea.

Christian Trutz writes, for example, do you use Spring Modulus to structure packages?

Exactly, that's what you can use, for example, to structure a system on this package level.

Exactly.

Good.

I think we're done with that topic.

I'll take a quick look to see if anything else comes in here.

Otherwise I would actually continue with this design-level event storming.

When it comes to design-level event storming, it's important to face what it's really about.

I would like to understand how the business logic is.

And I want to understand that in this big-picture event storming, which we discussed last time, roughly granular.

And here I would like to understand it finely granular.

So that means I have, for example, a read model.

And a read model is something where I can now, for example, paste in a UI and say, okay, it just shows something.

Then I have some actors, so people who do something and, for example, can issue a command.

And either through an external system or through my own system, then some events arise.

So I could say, for example, yes, I'm a customer, so I'm an actor here.

I give the command, I would like to have it now.

So I would like to submit this order.

That goes to my system.

Event, which somehow comes out, is order accepted.

And then it could be that I have generated an order from it, which I can then display to myself.

And here might be a policy that says, the next command is being created.

So that's an automatism.

That means, if the order has been accepted, I can have a policy that now says, okay, all right.

Then I will now somehow, please write an invoice and make sure that the thing is delivered.

So that's the idea.

And that's how I get into a granular model.

So I would have in the Big Picture Event Storming, which we discussed last time, I would only have this here, so the domain events.

Here I have a lot of additional information that gives me a deeper, better understanding of what is actually happening.

And I'll remind you again that this is something that we now want to create together with domain experts.

And the goal is, so the domain is now at this detail level, that I need for a tactical domain-driven design, that I understand that on this level.

And there is now no, so I would say, obviously there is no trivial mapping to tactical domain-driven design.

In other words, what we see here now is a completely different field of view.

So we're talking about systems, we're talking about read models, we're talking about UI.

These are all things that don't occur in this tactical domain-driven design.

That's why it might be very exciting to see how I'm actually mapping this now.

And I would expect a command in tactical domain-driven design is a method call on an aggregate or on a service.

So if I say now, I would like to order this, then I would expect there is a method somewhere or maybe several methods.

Yes, I would even say one method.

It would say, okay, I'll order this whole thing for you now.

And in that case, it's probably in a service, because I have to make an order in the context of it and have to create various other things.

But it could also be in an aggregate for simple cases.

So then I have the system, that would be my aggregate or my service, when I see the fine granular.

Now a domain event comes out of it.

I could implement that directly as a domain event also in tactical domain-driven design.

So that's something where this terminology is actually identical.

Then I have a read model, and that's ultimately an aggregate again.

That means the thing where I call the command here and the thing that I'm showing here can be the same object from my point of view.

In one case, I use the reading stories and in the other case, the writing stories.

I think it's a good practice to separate the methods that change state from the methods that give me information about the state.

So I either have methods that say, I'll tell you something about the delivery, what's in there, about products or something.

Or I have methods that make sure that something happens with this delivery.

And this read model would then be part of the aggregate that actually gives this information about this state.

We'll talk about things like CQS in a moment.

We would actually separate the read model now and say, these are different classes, maybe even a different microservice.

That's an option.

I personally don't think it's necessary.

And here you can see exactly one of the possibilities I have now.

So I can sit down as an architect and say, okay, we have a relatively simple case.

We just pack the commands and the read model together.

Or I can say, for whatever reason, it's complicated and I want to separate that.

Maybe I want to scale the class.

Whatever.

Then I'll do CQS.

But that's not mandatory.

I just want to understand what people want here.

And for that, it might be quite interesting to see what I actually want to read here.

And I get exactly this information from the design level events topic.

The policy would now also be something where a domain event is reacted to.

So some business logic that ensures that, for example, this invoice is written.

That's something that might happen again in an aggregate or in a service.

Where business logic is typically.

And that's actually where I'm through with the topic so far.

And can continue with the next topic.

This is this story with the event sourcing.

Let's see that I have the next table.

Exactly, here it is.

Here is a little bit.

We still have about half time.

Here is a little bit now.

How should I say?

This is another topic.

Event sourcing and CQS are somehow possibilities how I just implement certain things.

And they are independent of tactical domain design.

I think I'll say again in a moment how I rate this topic as a whole.

So whether it's mandatory or whatever.

And event sourcing means that the events that have led to a certain state I also save.

I can also save the state itself.

Obviously I don't necessarily have to.

Because I can emit this state from the events.

And I can now as a system of record.

So the system that should actually be the reliable one.

I can either say that's the state or the events.

That's up to me.

So that means what I can do now.

For example with an order.

I have an event store here.

And I have the state here.

And now I have an interface here.

And some calls, some messages are pressed on me.

So I'm talking about a system which is dealing with to do something with orders.

And here comes in a call which says this order 42 which should be delivered now.

That means I notice in the event store that this order 42 should actually be delivered and is accepted.

And then I have the state here which now somehow says the order 42 exists.

Then comes the next call which somehow says okay, order 23 is somehow there.

And then I have here as a state also the order 23.

Then I say next the order 42 is cancelled.

That's an event again.

I notice that again in the state.

And then I say the other is somehow delivered.

And I notice that again in the state.

So that means I have a system here which saves the state and also the events which led to this state.

When ordering I'm not sure whether this is really necessary.

With an account I'm relatively sure that this is really necessary.

Because I'm not only interested how much money I have on my account right now but also whether the last transfers have entered me.

And that leads to that we can distinguish systems here.

So we have systems which only save the state.

So I could now have a system which says hey, the order 42 is delivered to me, period.

And I could calculate the state on the fly.

I could, for example, determine the account state from the transfers and transactions that have occurred so far.

Or I can save the account state and also the events that led to it.

And when I save these events then it is event sourcing.

There is one more note which is important to me.

This is actually a persistence strategy.

That means the question is how do I save my account or my order.

And I can now say I save the state and also the events that led to it.

A persistence strategy should be internal.

That means whoever is responsible for something like accounts or whatever I have there should choose whether to do event sourcing or not.

This means in particular that it should not be the case that the externally observable events lead to me having my local state.

And there is actually in the show notes there is a video where I said when I save all events in Kafka and then somehow say okay, I can somehow use the local state of the microservices from these central events in Kafka for communication.

I can reconstruct this state of the microservices.

Then I actually have a database monolith.

The microservices do not have independent data models, but they only have a cache for what is in Kafka.

I can somehow remove their database.

Then they say, no problem, I read all the events again.

I have reconstructed the site.

And that can not, that must lead to that I somehow have a high dependency there.

And that's something I actually like to avoid.

That's why I find it difficult.

I'll link the video again.

And there is another story.

I have to get the article out again.

Christian Stettler wrote an article about it that these internal events are possibly fine granular.

Than what I want to announce externally.

If I say now, I am responsible for that I register a customer.

Then I have stories like, hey, your email address was not valid.

Hey, your ID check did not work.

And these are all things that do not interest me externally.

I just want to say this person is now validated.

And that's why it does.

And there's the story again.

The internal events are different than the external events.

That's why I want to separate that.

So what does that mean now?

Can I do something like a ...

So I have such a delivery.

The delivery is scheduled.

The delivery is accepted.

Has been taken out of the warehouse.

Has been packed into a truck.

Has been delivered.

And the customer said, I got it too.

Now the question is, can I model this delivery or such an event store at all?

Probably not.

Because that's exactly what interests me.

So I'm interested in who did what with it.

Because then I can say later, okay, you said it arrived.

Or that it was in your truck.

Where did that come from?

On the contrary, it's just that I'm not sure about this delivery.

Whether I actually want to calculate the state of the delivery.

So what do I get out of it if I don't save the state?

So I would write in here next to the event store, yes, this delivery has arrived and the customer said, everything is fine.

So I have a state that says, is successfully completed.

And then I can, on the other hand, if someone is interested in how it came about, somehow pull out these events and can display them.

That means this ...

So that's a technical discussion.

Actually, I say, that's the way I want to model something in a professional way.

And that's something where I don't want to reconstruct the state, which is often sold as an advantage from the events.

CQRS, that's the other approach.

This is this command query responsibility separation, where I somehow separate reading and writing.

And that would work now so that I have a command queue.

So there are some commands, I don't generate an invoice, for example, but I have a command handler, which, for example, may ensure that when an invoice is generated, it is immediately paid.

Then there is a database, where the invoices are stored, for example.

And then there is a query handler and it is somehow separated.

And there I can now, for example, read invoices.

And the commands I may now still have in the command store.

And that would be my model now.

And now I would actually have this read model here.

That would be what the query handler would use.

And here I would have the model where I actually change things or this part, which is not the system, which takes commands from the design level event storming.

So, if I build it that way, it means that the model for writing here through the commands and that of the queries is actually the same, because this is a common database.

Do I have anything of it at all?

Yes, I have something of it, because this query handler, for example, can use a read replica.

So I can now somehow say, okay, I'll build the system as it says here.

I now have the query handler.

The query handler uses a read replica of the database.

And I can read about it more scalably.

I think that's a bit of an advantage that is essentially created here.

These two parts are, for example, independently scalable.

I can now execute the command handler and the query handler in two different microservices.

And that also leads to that, how should I say, I'm not so sure about this pattern, how often I would actually want to use it.

Because it only makes sense if I have something, or for scaling at least, it only makes sense if I somehow say, okay, I want to scale this query handler area independently of writing.

And I think I have to come to significant scaling heights so that I have a profit there.

I can do something else.

I can say, the query handler has a snapshot and I build this snapshot through event sourcing stories together.

So that would mean that I have these commands here.

Something is built on logic here.

So I say, for example, that the payment takes place.

And then I have an event sourcing to the database for the snapshot.

And there I would now somehow every time a calculation is created, a new entry is made into this database.

That is decoupled even more.

And that could be useful, for example, for something like statistics.

So for statistics, I might really want to have a separate reading model.

I also want to have other information, somehow rather sums.

And that's something where I might really want to build such a CQS thing.

So I have the data, so to speak, which is motion data.

And then I have the data for the statistics.

And that would probably mean that statistics are perhaps even a different context with a completely different data model.

So maybe I have to model statistics and I have a reading model, because I can only write and create an invoice once and then I can only read it.

That's actually technically correct.

So I can't say, oops, I got lost in this invoice, let me change it for a moment, but I have to say, I got lost in the invoice, let me storm the invoice, I'll write a new one.

That's a model that somehow says, okay, not allow queries, are just separated, work on the read replica.

And I have the other thing that somehow generates this invoice.

Maybe it's not bad at all to implement this policy strictly.

Maybe it's not so bad from a technical point of view.

Typhonix writes, the wording snapshot is actually something else in the event sourcing context, so that the data is saved in between when storing.

Actually, projections are meant, right?

Yes, it may well be that I got lost in the naming.

Good point, thank you for the hint.

So exactly, snapshot may actually refer to an aggregate.

Good point.

I also made a whole episode on this topic.

I'll discuss the topic in more depth.

You can take a look at it.

And with that we come to this topic, where there was already interest last time.

And I planned a little faster, so to speak.

And that's the story with the layers.

First of all, the hint is that this is actually a pattern from the original blue Domain Driven Design book.

So there is layering as a pattern in this blue Domain Driven Design book.

And that means that I have the UI, the logic and the persistence.

And such layers always have dependencies from top to bottom.

That means, I say the UI uses the logic, the logic uses the persistence.

And that's exactly the story with the layering.

For me, the prototypical model for a layering is actually something like this network stack, where I have a physical layer at the bottom, i.e.

Ethernet or Wi-Fi.

Then I have IP over it, then I have TCP over it and then some protocols like FTP or HTTP.

And that's exactly such a layering.

So HTTP uses TCP or UDP by now.

TCP and UDP use IP.

IP then uses what I'm using right now, Ethernet or Wi-Fi.

And there is only the dependency in this direction.

I mention this because I think this layering often makes sense from a technical perspective.

But here we are talking about how we structure expertise.

And now the question is to me, with network layering, for example, because I have this physical layer, I can now switch from Ethernet to Wi-Fi relatively trivially or from Wi-Fi to mobile communication.

This is exactly hidden above that.

So that means I can exchange this lower layer exactly and the rest of the system remains untouched.

Here I would argue that this is not really a good reason, because I will probably rarely exchange the persistence.

So the question is to me why this pattern is there after all.

And what Eric said to me is, well, I separate the logic and have them in exactly one place.

And that's how I build the system so that it's easy to understand.

And in fact, it's like that.

Domain Design doesn't say anything about the UI.

So what Domain Design says is, OK, we have services, we have aggregates, such things.

That we have a UI that uses it is somehow clear.

But we don't say how it should be structured.

There are also possibilities to structure something like that.

And with the persistence, well, there is a repository as a pattern.

But that doesn't say that much about how you want to implement it exactly.

We just saw this transaction script, for example.

There are definitely other possibilities.

And that means that the core of this pattern only says, we have separated the logic.

The logic is actually the area where Domain Design says a lot about it.

Entity, aggregates and so on.

These are all things that are somehow in this logic layer.

And we separate that from the persistence, so that I don't, when I think about the logic and look at what's going on there, somehow get annoyed by SQL statements that have nothing to do with it.

Or JPA stories that have nothing to do with it.

But I have that somewhere else.

And analogously, I also separated the UI from it.

And on this abstraction layer, or on this abstraction level, hexagonal architecture is actually a solution to the same problem.

In other words, Eric could have said in his book, we're not talking about layers, we're talking about hexagonal.

That he didn't do that is because Domain Driven Design, if I'm not mistaken, is a bit older than hexagonal architecture.

In other words, back then it was somehow this three-layer architecture with UI, logic and persistence that was typically done.

So what's different about hexagonal architecture now?

Clean Architecture is very similar, for example.

I say the business logic exports some ports.

So I have the business logic.

It now has a port here, for example, to send out notifications.

And then I have adapters that implement these ports.

So I have an email adapter, for example.

So that means I say here in the business logic, I have a notification interface.

And the email adapter can now implement it.

And here, for example, are some business events that I now output to the UI.

Here's an admin thing that I output to the admin UI.

And here's the persistence.

And I have a database adapter that implements this persistence.

So what I've achieved is that in all cases, the dependency from the outside, from the database adapter, for example, to persistence, it implements what the persistence would like to have here.

Or here from the admin UI to admin.

Or from the email adapter to notification.

And that's not the case with layering.

With layering, the logic uses the persistence.

So that means logic depends on persistence.

Everything depends on the logic here, including the implementation of the persistence of the database adapter.

For me, this is relatively similar to this dependency inversion principle, where I say if I use something, well, then I can also define the interface here somehow.

And then the dependency is exactly the other way around.

So the business logic uses the database adapter, but it's not software-dependent, but it gives it the interface that the database adapter has to implement.

So that means database adapter implements persistence port.

As a result, the dependency is from outside, from these adapters to the ports.

And that leads, for example, so first of all, I achieve the same goal as de-layering.

So what Eric says is, I would like to separate the logic from something else.

I can do that here too.

Maybe even a little bit better, because I don't have this dependency into persistence.

And I also have the advantage that I can test the stuff better, because the business logic core is free of any kind of technology.

So that means if I have the layering, then it is in the logic that I actually somehow depend on the persistence.

Maybe I have to catch some exceptions that the persistence throws.

Here it is so that the database adapter is dependent on the business logic.

It defines what to expect, so to speak, and what the interface should look like.

And then the database adapter will implement that.

So that means the persistence doesn't know anything about it.

The business logic doesn't know anything about what exactly is happening here.

And that leads to better testability, because I can now replace the database adapter and all other adapters with something in the test.

So I can now say to myself, there is something that behaves like a database, or I can have something that, for example, asks for the notifications, which would otherwise go out as e-mails.

That means I can test in isolation with the business logic core.

And I think that's also a significant advantage.

I just did an episode with Warren Vernon.

Warren also wrote the book Domain Driven Design Compact.

And actually I had expected, we're not talking about domain driven design, but he talked a lot about ports and adapters, or hexagonal architecture.

And one thing that I think was totally exciting was that Warren basically said, well, is it really that much more complicated to build a hexagonal architecture?

And that's actually a good point.

So layering says, I separated these three things.

And hexagonal architecture says, I isolated UI, logic and persistence.

And hexagonal architecture now says, I isolated these three things.

And the persistence depends on the logic.

So if I'm here at layering, it would be that the logic uses the persistence and is dependent on it.

Here it is exactly the other way around.

Here I say, the logic does not know the persistence, but on the contrary, the database adapter implements this interface that the core of logic provides.

In terms of the UI, it is identical anyway, because the UI uses the logic.

Here, from top to bottom, the dependencies, that's the same here.

So that means the UI comes now somehow and uses this port here.

That means the dependency file is the same.

So the only thing that actually changes is this other dependency file on the database adapter.

And relatively stupidly, I can achieve that by somehow defining these interfaces in the business logic.

And yes, I have to make sure that it is technology-independent.

But that's what it is.

So that means, actually, it's a point, if I separate that, then the big effort is no longer such a big difference in terms of effort between hexagonal architecture and layering.

And I thought that was a very exciting idea, because hexagonal architecture has a bit of a reputation for being complicated.

And I think that's exactly this input that's interesting to me.

And as I said, the alternative to that is something like a transaction script, where I don't do this layering, where I no longer isolate the business logic that much, simply because there is too little of it or none at all.

So I should maybe add one more thing.

If I am forced to build a system as a developer that has no business logic, that means that I don't generate a lot of value either, I would say.

And it may be that I actually build a system that doesn't really solve the business logic problem.

So the customer comes and says, I would like to see the following data.

Okay, is that business logic?

No, I just want to display the data.

But that's probably not what this person really wants.

What she really wants is, she wants to decide now, when I look at the customer, I can decide whether it's a good or a bad customer.

But then it's actually the case that there is a business logic behind it, which I can now try to implement.

So I can now say, hey, according to our policy, this is a good customer, because he ordered a lot of things and returned little.

And that means, if I build a system that only transports data from A to B or only displays data, this may be a misleading chance to build a system with more business logic.

That means, this topic with the transaction script is the right solution, if I have little logic.

But be careful, maybe it's just that the logic has been hidden from me, so to speak.

In summary, I tried to paint this again.

And to get an overview of all the things, from left to right, there are more and more details.

And that was something I said last time.

So the idea here is not that this is a waterfall, where I walk through once, but I work on different details.

And the rough granule that I have is Big Picture Event Storming.

I get an overview of the entire system, the events that run here.

And I can then decide about it, for example, or a next step would be to say, what is my core domain?

So what is it all about?

I can use strategic design as an alternative to team topologies.

I say which teams are responsible and who does what where.

That's something...

I don't know if it's more detailed.

So here I'm actually talking about the business logic of Big Picture Event Storming.

And here I say, for something like strategic design or team topologies or core domain, I actually say how I want to divide it on the level of teams.

And they then work on one or more built-in contexts.

And then there are these very specific techniques that we talked about, so tactical design, to actually implement a built-in context and to say how it is implemented.

Design level event storming, to understand what the requirements are on this level.

I can use something like event sourcing or CQRS, if I have the necessary prerequisites for it, in the sense that I generate an advantage if I store the events in the case of event sourcing, or in the case of CQRS, if I can actually separate the writing and the reading part from each other.

And then there are layers or hexagonal architecture.

I have now also put a question mark behind it.

With event sourcing and CQRS, I would somehow say, okay, I'll use that when it fits, so to speak.

With layers or hexagonal, I would say one of the two patterns I should somehow apply, because otherwise I would have mixed up the logic and the other things.

Jude Ruth writes, Jude Ruth writes, additionally, warns of the naming of ports and adapters instead of hexagonal architecture.

Good point, I don't remember that at all.

And in fact, this is perhaps also a point that is a bit unfortunate here.

So the hexagonal architecture is called hexagonal because the business logic core and the things around it, so to speak, are randomly painted as hexagons.

And it is actually the case that ports and adapters are the better term, because I think that expresses better what it is actually about, namely to expose these ports from the business logic core and then to have adapters around it, which somehow implement that accordingly.

Good.

Then I think we're actually ready.

A note, next week, as I said, there is this training round on the topic Domain-Driven Design Salutes Legacy.

That's on the afternoon of the 16th and 12th.

You are welcome to join.

I think it's also reasonably moderate and it's a good opportunity to talk about how to build Legacy with DDD.

The other thing is, next week, Ralf will talk to Lars Röwekamp about the topic Generative AI meets Software Architecture.

And that will be at 3 p.m.

So Friday at 3 p.m.

That's a little later than usual.

And maybe you want to switch on again.

Otherwise, thank you very much for your attention.

And thank you very much for the questions and for the comments.

And then I would say, I wish you a pleasant and nice weekend.

Until then.

Thank you very much.