# Episode 262 - Questions from Agile Meets Architecture And the reason is because I'm going to answer all the questions due to my talk, Architecture and Agility, a Shared Skillset from the Architecture Meets Agile Conference.

And as the original talk was in English, I figured that I would also do this question and answer in English.

I was very happy to see that there were actually quite a few questions, and the organizers of Agile Meets Architecture were so kind to forward them to me, so I had a chance to answer them.

And they were not just interesting, the questions, but there were also quite a few of them.

So that is why I figured that it could take a whole episode to answer all of them.

If you're interested in the original talk, basically the main hypothesis of the talk is that people who do architecture work more with people than technology.

So I mean, if you look at architecture and architects in general, you would assume that the people would rather work with architecture and technical things, but really they do work with people, and therefore they need to use the same skills like agile people, agile coaches, because also agility is not something that is about project management, but it's rather about people and how people work together.

So that's the main hypothesis of the talk.

Interestingly enough, the questions by themselves are often sort of self-contained, so you can follow the questions without listening to the talk.

If you want to get an impression of the talk, I will link the slides.

And also, Eduardo da Silva was very kind to summarize the talk in a posting on LinkedIn, so I will also provide a link to that posting.

Okay, so let's start with the first question.

So the first question is, which architectural principles or guardrails help embrace change and make agility blockers visible?

And so basically the question is around blockers to agility, and I would argue that the typical blockers to agility, that's what, you know, scrum masters or agile coaches are concerned with.

It's probably a people's problem, so I'm not sure how architecture or architectural principles would influence that, because that is about technical decisions, that is about making some fundamental technical decisions, and it's not about blockers on the level of how people interact with one another.

I think there is an interesting discussion, and we will also cover that probably during the next few questions that arose during my talk, or after my talk, and that is about decision making.

So if you have an architecture, it's decisions about technologies, it's about decisions about how you structure the systems, so there is a question around, okay, so who is going to make these decisions, and how is that going to work out?

And indeed, there is an architectural principle or guardrails that allow you to sort of codify this.

So there is the idea of macro and microarchitecture, so the microarchitecture are decisions that would be made to and would cover all of the systems.

So for example, one decision might be to say, okay, each team provides a Docker container, and that is a decision that is made on the overall level, on the level of all the teams that work together, and that is probably because it allows you to have a common foundation, a common runtime environment to run the system on.

So it might be Kubernetes or some other system that allows you to run Docker containers.

And then there are micro decisions, or microarchitecture decisions, those are the ones that the teams actually make.

And this division between decisions that the teams can make and the overall decisions are sort of a codified set of guardrails that allow the team to make decisions.

And this discussion, this whole thing might actually point at problems, because if there is too much microarchitecture, it means that the teams are limited in what they can actually decide, so then there is a problem.

Another problem that might happen is that the teams actually don't set up and don't use the power of decisions that they can make, because they are afraid to make those decisions, because it also means to take responsibility for these decisions.

And then you have another agile blocker.

So this division between macro and microarchitecture might make such agile blockers visible.

And there are also different approaches towards micro and microarchitecture.

So the one that I just mentioned is basically a set of rules that teams have to adhere to.

So there is a clear decision that says, okay, this is how we are making decisions here.

You have to provide these things.

It's a docker container that you need to provide, and that's a set of technical decisions.

You can also have other things like, okay, so you need to have a specific interface to the monitoring system.

That would be another technical guideline that is very clearly expressed.

There is a different approach to microarchitecture where you basically have a set of, well, let's say best practices maybe.

I'm not sure whether that's the right word.

So let's imagine that we have the project, and in the project, scalability is an issue.

So we provide a document, maybe a Wikipedia page, that has a chapter about scalability.

So that expresses that scalability is an issue.

Then we tell the people, well, okay, the scalability depends on the business plan, and here is the link to the business plan.

And then there are different ways of dealing with scalability.

So there might be scale up, there might be scale out, and there might also be graceful degradation where you switch off a service if the load is too high.

And you actually write down these patterns, and you explain these patterns to the reader, and you also give some information about people that can explain that pattern in more detail and also give you an idea about how that pattern could be implemented in your environment, in the environment of this concrete project.

And that's quite different, right?

So if you use this approach, it basically means, okay, here is a set of challenges, like scalability.

Here is a set of potential solutions, like scale up or graceful degradation, or whatever it is.

And then it's up to the team or to the architect of that team to decide what they actually want to do, and they have quite some flexibility.

So it's not a clear-cut set of rules that you have to adhere to.

It's rather sort of a general guideline, and that means that the team has much more responsibility, the architect has much more responsibility.

And again, that means you have a different maturity level.

I did an episode about this.

I will link to it.

However, it's in German, I'm afraid.

And this is what comes to mind, these different styles of micro-macro-architecture and micro-macro-architecture in general, which means if there are a lot of decisions made for the teams, they're probably not that agile.

They're not really autonomous.

And I would prefer to have the teams make the decisions, so to give them as much space for the micro-architecture as you can, and let them decide.

So maybe that's some advice that I would give them.

TTY0482 on YouTube had a comment.

So he or she says, there's actually some hard data about that from the state of DevOps report 2017, summarizing and accelerate.

I'm surprised the loosely coupled architecture and autonomous teams are beneficial.

That's a very good point.

I did an episode about the DevOps study that you referred to.

Again, this is in German, I'm afraid.

And I would like to second that.

So architecture is an enabler to give you that kind of autonomy.

And if you have a very strongly coupled architecture, it means that the teams have to coordinate a lot, and therefore they cannot really be independent, and they cannot really be agile.

And the Accelerate book makes an excellent point that this is really what we should be focusing on in architecture, that each team can make decisions by themselves.

And it's probably not so much about, you know, using Kubernetes or microservices.

It's rather about this autonomy that enables teams to be more productive.

And this is what we should aim for.

So that is why this is a very good comment.

And I would like to thank TTY0482 for that.

Okay.

Next question is, how can we balance frequent changes in an architecture with making progress?

I thought this was quite an interesting question, because first of all, in most of the situations that I'm in as a consultant, it's the other way around.

So a lot of time and effort is spent on, well, making progress.

And I assume that means implementing features.

And that this usually wins, I think, isn't really that surprising, because at the end of the day, this is what makes the system valuable, right?

So if there are more features, if there are better features, then the system is more valuable.

So sort of the hypothesis of the question that you can spend a lot of effort on the architecture and not so much effort on actually making progress, obviously, you can do that.

But it's something that I would argue only rarely happens.

So therefore, I'm not sure whether this is a real problem, so to say.

So spending lots of time to keep the architecture clean does not really seem like a typical problem.

I'm not saying there is no such project that has this kind of problem.

It's rather that I think this is not sort of the typical case that you would have.

The other thing is, so why would I invest in architecture?

And I would argue that you would invest in architecture to actually make progress.

So one of the reasons why you would invest in architecture is because of quality requirements.

So you're not meeting the performance, the security, whatever it is.

You're not meeting some expectation from customers or users.

So therefore, you have to use a different technology.

You have to tweak the system, change it so it actually fulfills those quality requirements.

And I would argue if you do that, you do make progress because it's something that is clearly visible to the user, and chances are that some complaint by users or stakeholders is even the reason why you are investing in that architecture or technology change.

And the other reason why you might want to invest in architecture is because your system is not really that changeable or maintainable.

In that case, you are enabling to make more progress, to change the system quicker.

So I think, in my opinion, architecture is a means to an end.

It's not something that you do just because you want to do it.

It's rather something that is aimed at making more progress.

Which leads to the question, so if you don't make progress, either because the system becomes more maintainable and therefore you can provide more features, or because the quality requirements are met, if you don't achieve that with some change to the architecture, why would you invest in architecture?

There are cases, I would like to call them a migration, where you change a system quite fundamentally.

Okay, so for example, you have some old mainframe COBOL system, and now for some reason you want to convert it to a more modern environment.

Let's say you want to convert it to a Java application that runs on Linux systems.

And if you do these kinds of fundamental changes, which you might consider, well, fundamental change to the architecture, my advice is to have a good business reason for doing so.

So reasons might be the old system is very expensive, the system is not changeable, these kinds of things.

And then, again, it's about making progress in the sense that you are, again, meeting some quality requirements, like cost efficiency, if you migrate it over because the old system is much too expensive to run, or maintainability if you migrate the system because it's much too hard to change.

So again, also in this case, if you have a fundamental shift in architecture, it's because you want to make progress.

And coming back to the original hypothesis that most of the time it's the progress, the features that dominate what, well, time and effort is spent on, nowadays it seems to me – and actually I've been part of one project that had such a story – where you start with a mainframe system, you migrate it over to some modern system, like Java, for example, and before you fully migrate the system, there is a new architecture that says, okay, we are going to use, I don't know, JavaScript, or we are going to use a new approach to Java, not the old application service, but now we are going for microservices and Kubernetes and Spring Boot, whatever it is.

So you have another third architecture option that you are actually investing in.

And in the scenarios that I see, all of these three architectures – so the original mainframe architecture, the first Java architecture, and the second Java architecture – exist in parallel because the new migration started before the old migration is fully executed.

And that again means – and now the question is, why is that?

And I would argue this is because you want to invest, again, in features and not in an architecture migration that probably doesn't make a lot of sense for some reason.

So maybe you got stuck because you can't clearly express what the value is, how this can be considered making progress.

And that is why you started yet another migration before finishing the first one.

So again, I would argue that in the projects that I see, at least, usually the balance between frequent changes in architecture and making progress, it's rather that it's towards making progress and there is too little investment in architecture, which slows down making progress because then you have a system that is very complex because there are so many different architectures, as I explained, or because the architecture is very complex and it's hard to maintain the system.

TTY0482 says, I like the approach of just enough architecture and treating it like any other part of Azure development with iterative incremental improvement.

And I would not just agree, but I would argue that this is the only way how you can actually make any kind of architecture or engineering, which is the idea that you have right now about the system, how you want to build the system, your current approach to architecture, it's just the current snapshot of your understanding and the consequences of your understanding.

And it might change because you might learn new facts about the domain, about how you do architecture, about techniques, about technologies.

And therefore, sort of by definition, the architecture will be implemented or will change and therefore it will be iterative incremental.

It's just that you can either realize that and say, okay, this is what's going to happen or you can try to ignore it.

But this is what usually happens.

And I did an episode with Hila and Wayne about engineering.

And it turns out that all engineering is like that.

So you have some plan, you try to implement it, and then you change plans.

And that is why you build prototypes, right?

Why there is a first iteration of something and then you build a prototype of a car, let's say a car.

And obviously, you would change that afterwards and build, well, the next prototype until finally you put it in production.

Even if it's in production, there might be tweaks and changes to the car or whatever you're producing.

TTY-04A2, again, I think in those scenarios, the problem is often all or nothing thinking.

A lot of people seem to think you need everything to be the same tech and patterns and concepts.

Yes, and that is why I spoke about this scenario where there are three architectures in parallel.

And I think it's actually something that is quite common.

And I'm not even sure whether it's a bad thing because it means that you invest in making progress and implementing features.

And that is, at the end of the day, what most of the value of the system comes from.

Okay, next question, another one that I found really interesting and made me do this episode.

So the question is, technology comes with certain underlying cultures and philosophies which influence the culture and habits of teams.

Will that not influence architecture?

And I think that's actually a great point because it means that a technology like Java, for example, it's not just a technology.

It's also sort of a placeholder for a specific culture which obviously will influence architecture.

And I'm not sure whether it's actually so clear for everyone.

So this is why I really like this question because I would argue that what this question sort of implies, that there is a culture that comes with a certain technology.

I would totally agree to that.

I was trying to think about an example, and I have to admit that I came up with… talk came up with lots of ideas that are still very relevant today.

And this is because of the, let's say, strong object-oriented culture that they have.

So examples are JUnit, the unit testing framework, is something that originates from, I think, SUnit in the small talk community.

So the whole unit testing is something that comes out of small talk, and the same is true for extreme programming.

If you look at Java, it is something that is used in the enterprise, quite often in the enterprise.

So therefore, there is a rather enterprise-y culture, building large backend systems, these kinds of things, and being conservative.

And this, again, translates into specific features of the technology.

So if you look at Spring, for example, Spring is a Java framework, and it aims to be very backwards compatible, so that if you have some code that is really old, you can still run it with the most recent version of Spring.

And the reason, and this is something that is quite common in enterprises.

So for example, if you have software for the IBM system 360, the mainframe from the 60s, you can basically still run it on modern-day mainframes.

So this backwards compatibility, and this being conservative, and these kinds of things, this is something that is typical about enterprises.

And therefore, I would argue that probably Java and Spring come with this kind of culture.

TTY0482 says, I think it can be both a bad and a good thing, depending on how one goes about it.

I've had projects where people tend to modernize the already modern parts and let the hard old parts not.

And I think this refers to changing the architecture and probably spending too much effort on it.

And I would agree, and this is why, and I discussed that in quite a few episodes, this is why I think you have to motivate the migration of some system, the investment in architecture with some kind of business benefit, because otherwise it might become pointless.

So I think taking into account the business benefit of some things that you do in the architecture is also a good filter to see whether the ideas that you have there are really worth it, or whether you should rather not work on them because they don't change a lot of things at the end of the day.

Okay, so yes, I would argue that technology comes with certain cultures and philosophies, and that will definitely influence architecture.

It's a specific style of thinking.

So Smalltalk is sort of, I would argue that people who work with Smalltalk have sort of the original, tried to build object-oriented systems like they were originally meant to be.

Java people probably want to build these enterprise-y, conservative systems, and so on and so on.

And there are exceptions from the rule, but I would argue that this is the case.

And I don't know, the question somehow seems to imply, or maybe that's my problem because I'm a consultant, so usually if someone asks me about something, it's because there is some problem.

And in this case, I sort of failed to see the problem, really, because it just means that there is a certain technology and that comes with a certain culture, and I'm not sure whether that's actually a bad thing.

If I look at some team, I would believe that the team, the people, is probably something that is sort of more constant than the technology, even though thinking about it, that might not be the case.

I think what I'm trying to say is, if I have a specific set of people, then they will tend to use some technology and a specific approach to solve problems.

And therefore, maybe the people, the culture, will determine the technology that you're using.

If that is the case, it means that technology decisions depend on people, and so does culture.

And that is something that I feel is often neglected in technology decisions because it seems that, you know, you can come up with the ideal, perfect technology for a specific problem.

But I'm not sure whether I would agree.

I would argue that you can build almost any system with any technology and be successful about it.

These days, the typical systems that I work on, they don't really have such huge problems in terms of what they need to achieve, like performance or these kinds of things.

They hardly push the envelope there.

So therefore, I'm not sure whether it's so very important to sort of use the right technology.

So maybe there is a takeaway there that says, okay, if you build some system, take into account what kind of people are building the system and take that into account if you decide about a specific technology.

And you probably shouldn't fight it.

So if you have people that feel strongly about, I don't know, Java or a specific front-end framework in the JavaScript universe, why would you make them use something different?

Does it really matter?

Does that really cause – does that really influence the success of the project as much?

Or should you rather listen to the people and try to do something that sort of makes them happy?

Let's see.

So supermain02 says, to my opinion, especially documentation is a vital part of architecture, and without, you don't have any.

Why is this so rarely a point in discussions about architecture?

Well, first of all, I would argue it's actually an important point about architecture because if you look at what we did at Software Architecture on Stream, we spent quite a few episodes about architecture documentation.

And I have to admit that they are – so it's something that I personally am not so interested in.

And the – so sort of to my surprise, the episodes about architecture documentation are quite popular.

So I think – I'm not sure whether I would agree that architecture documentation is something that is rarely a point.

Quite the opposite, it seems.

And it's – you know, you could come to the conclusion that it's a boring topic, but people seem to be interested in it.

So I don't think that there's such a huge problem.

However, even without documentation, there is an architecture, because the structure of the system, the technology decisions that you made, they are present in the system.

So therefore, there is an architecture, even if you don't document it.

And there might – there are other ways to sort of understand an architecture so, you know, you can talk to one another.

And I would argue that an architecture documentation only takes you so far.

So when I do a review, or I do a review together with my colleagues, usually I'm quite skeptic about the documentation.

So I assume that it has – that it sort of lies because it might be outdated.

So it's not that people, you know, actively lie to me.

It's just that they provide some documentation that is outdated.

Therefore, the information is incorrect.

And that is why I need to have direct conversations with the people who want me to do the review, because they actually know what is going on in the system.

And sometimes the documentation also fails to deliver important information.

So therefore, there are other ways to communicate that, right?

Documentation is just one way of communication.

It's just – it means that you write things down and other people read it.

But you can also do other things like, you know, I'm now talking to you.

Obviously, that's another way of communication.

And for good reason, we tend to, well, talk to one another, because the written documentation might be limited in bandwidth.

So therefore, I would argue that, yeah, just focusing on documentation doesn't probably cut it.

You know, and Supermain says, to my experience, architecture often fails to lack of communication, especially by documentation.

Yeah, absolutely.

That is also one of the reasons why I did the talk, because I think communication is something that also HR coaches care about.

It's a people business, and that clearly influences architecture.

And that is sort of the original reason why I did the talk that we are discussing the questions about now.

TTY0482 says, I think a lot of time it's the old cargo cart problem, applying methods wrong without understanding the ideas behind them, like OP, DDD, Agile, DevOps.

Yes, absolutely.

That's why I'm doing the stream.

And that's sort of a sad story that oftentimes people are not able to look, well, further and try to really understand what's going on and then stick to these buzzwords without really understanding what they should be doing.

TTY0482 also says, I'm not sure about the value of a lot of architecture documentation.

I feel like if you have implemented a clear, understandable architecture, most staff will stick to it, which sort of means that the documentation is a way to make developers actually use the documentation.

I'm not, sorry, the architecture.

I'm not sure whether I agree.

We had quite a few episodes about architecture management tools, and these actually do enforce architecture.

So, they enforce a specific split of the system into different parts.

I will also link to that.

And then, well, it gives you some feedback about whether what you did in your code is what the architecture wants you to do.

And if you fail to do that, if you do something that violates the architecture, you can have a discussion about that.

And that is what I would be doing and maybe not just, you know, write it down somewhere where nobody would read it.

Another comment by TTY0482.

Thanks for the comments and the discussions.

Document quality, RDRs interfaces, maybe give a high-level overview to the rest of the implementation tools, in my opinion, exactly.

So, you need to focus on what is actually important and spell that out, and other things might be not so important.

What else is there?

Oh, right, that's the next question.

How can I encourage the team to value the architecture when not everyone wants to be involved?

I thought there is an underlying assumption here in the question, which is if people are not involved in the architecture, they are not valuing the architecture, and I'm not sure whether that's actually true.

So, I don't see why everyone should be involved.

To me, it's fine if they value the architecture, if they execute the architecture, and if they provide some feedback, but if they don't really design it themselves.

I mean, there are people who do want to code and solve, like, hands-on problems, and there are other people like myself who rather want to talk about architecture and get a better understanding about these things, and both roles and both approaches are valuable and important to get a system done.

So, if there is some developer who says, okay, I don't really want to discuss this in detail, that's just not what I'm interested in, I think that's totally fine, and you can actually accept it.

Rather the opposite, if everyone wants to be involved, and if everyone has some opinion, then you will have endless discussions, and that's also not really healthy.

So, you should, in my opinion, try to explain architecture to people, you should try to get some feedback.

You might want to write it down, as we discussed with the documentation, you might want to make the decisions happen, but as I said, I'm totally fine if just a subset of all the people on the team actually work on the architecture, and I don't see where the whole problem would be.

I would be scared, or there is a problem if people actually fight the architecture without providing feedback, if there is no compromise, if they can't live with some solution that everyone agrees on, but then you're basically down to a problem around communication and team dynamics, and that brings me back to the original point of the talk, even, which is that if you have some people who work together in a team, and you want to be successful in making them work together, it is actually a prerequisite to also make the architecture happen, and this might be an example, right?

So, if there are people who really don't want to work with the architecture, not provide a productive feedback, this is when it's really about people, and this is also when the typical skills of agile coaches and scrum masters would be very valuable.

Happy Tree says, architecture is a mental model.

Maybe if it does not fit in the people's head working on the project, either does not fit.

You could adapt an architecture that solves the problem and fits in their head, which, again, is a people and communication problem because it means it's too complex, and the architecture is too complex for them to understand and fit in their heads, and it's not a problem of them not being involved.

It's rather that whoever came up with the architecture probably did not such a great job because it's too complex, and then you should sort of scale it down.

So, next question, is dictatorship necessary in certain architectural decisions given that teams split into camps, e.g.

React versus Vue, and facts don't convince the other side?

So, okay, TTY04A2, I agree, which is why I find it so valuable to make sure people understand or have the opportunity to what you are trying to do with the whole system and architectural decisions in particular.

I think that's a good point and sums up the last point.

So, what about dictatorship in this concrete example?

The example is that there seem to be two camps, and one says React is the way to go, the other one says Vue is the way to go, and now someone has to make a decision.

And I'm not sure that that's dictatorship because at the end of the day, you actually listen to those people.

They have just different opinions, and now it's up to you to moderate some kind of decision, or for that matter, it might be something that some scrum master might do or some agile coach might do.

I would argue that dictatorship would rather be, okay, we are going to use Angular because this is what I want, period.

But that's different, right?

Because then you enforce your decision and you don't really listen to whatever they say.

And you might even have some reason like, okay, Angular is better for reason XYZ, but it's not trying to convince them.

It's rather that you'd say, okay, this is the decision, this is what I'm going to push through.

So, we are talking about a different case.

I wouldn't call that dictatorship.

I wouldn't call it Everytower either.

So, Everytower is where people make some decisions that do not matter and are probably not executed.

So, in the scenario that we have, such an Everytower decision might be use Spring because that clearly doesn't solve the problem at all because it's about a JavaScript framework and Spring is a Java framework.

So, first of all, you are disconnected from what is going on there.

So, in this case, it's a decision about some JavaScript framework.

And second of all, you make some decision, in this case, use Spring, which doesn't really solve the problem and it's just entirely pointless.

And this would, of course, be a social problem.

So, I would argue this is not dictatorship, it's not Everytower.

It's rather that you have a problem because there are two camps and they are unable to convince the other side.

And it might even be sort of a religious war, right?

I mean, we all know these war like VI versus Emacs and it starts to become, well, religious and not based on fact at one point.

And maybe that's also something that happens here.

Question is, is it really necessary that all agree?

Is it possible to have two teams that use these two technologies, even though you have different technologies then, but at least people would use what they prefer?

You could make some decision, like some random decision.

And I think at the end of the day, this is a communication issue and I'm not sure how I would behave in this situation because there are quite a few influencing factors, right?

It's about team dynamics, I would argue, and I would try to understand the team dynamics and then work from there.

And I have to admit that one thing that I always wanted to do, but I haven't done yet, is to just flip a coin and, you know, say, okay, React or Vue, we flip a coin, we go with whatever the coin says and that's it.

And I would be interested in doing that because I would be interested in the reaction from the team and maybe, you know, having such a decision made in this way will encourage people or will motivate people to actually make a decision that is not just based on flipping a coin.

There is another thing that I would like to talk about here, and that is – and we discussed that already with the feedback concerning the the decisions.

Why do you want to do that?

Because it's more efficient.

Because they know more facts, they are more sort of, well, sort of in the trenches, so they know what's going on there.

And it doesn't make a lot of sense to enforce a decision on them.

Which means that it's just a loss of efficiency if you step in and say, okay, we are going to do this.

There might be some team dynamics behind that because people might be frustrated that they are not listened to.

This is also one of the factors.

But there is certainly not an ethical problem around that.

So if you have a dictatorship as a – I mean, it's originally a political concept.

And I mean, it even – as far as I remember, it originates from the Roman Empire where dictatorship is actually an option that you could have, I think, in case of a war.

I have to admit that I didn't research that.

So it's not something that was originally negative these days.

It's clearly negative.

But that is because a political system is quite different from a project and covers different topics, right?

So at the end of the day, what the project does or tries to achieve is to build some software successfully while the society that we live in and how we make decisions in society is something that influences all of us and our quality of life, our freedom and all these kinds.

So what I'm trying to say is you can go back to dictatorship and just make the decisions yourself.

It's just inefficient and therefore probably not such a bad idea – sorry, probably not such a good idea.

But it might also be a result of the role that is assigned to you.

So if you are the architect which means that you are responsible for the technical success of the project, then if the team makes some decision that you think is just stupid or if the team doesn't come to some conclusion, then you will probably step in and say, okay, I'm going to make that decision because at the end of the day, it's me and my career that is on the line.

So I would rather make the decision than have an endless discussion and make the team successful.

But this is a problem that is concerned with your role and the role that has been assigned to you.

So let's see.

MD42Martin on Twitch said, sometimes a central decision is needed, for example, when the team does not see the benefits of trunk-based delivery when they never work with that.

I'm not sure whether the advantage of trunk-based development is worth it pushing that through.

And I'm not saying it's not.

It's rather that there are projects out there that use feature branches and they are successful.

So I'm not sure whether – and I think that is something that I also said during the talk.

So there are basically two things here.

So one thing is, should we use trunk-based development or feature branches?

And we can have a discussion about the efficiency and which one is better.

Trunk-based development has some advantages, and you can talk about that.

But the question is, do I want to push through that decision?

And then I would frustrate people.

It also means that I wasn't able to explain the advantage to them.

I wasn't able to make them realize the benefit of, in this case, trunk-based development.

And therefore, there are two things.

So one thing is, how much more efficient is trunk-based development?

And the other question is, how are we making decisions?

And if you just say, okay, we are going to do trunk-based development, period, because it's obviously the better way, it means that it might be the better way, but it also means that you limit the autonomy of the teams.

And then the question becomes whether that's actually worth it.

So MD42 said, let me see, when other teams in some org do no trunk-based delivery and clearly see the advantage.

And then, I mean, they could talk to one another, right, and you could try to convince them.

TTY0482 says, that's an interesting idea.

We have weighted the pros and cons, and neither came out on top, so we tossed a coin.

Would that make both sides happier, or would it just make people argue harder?

That's actually what I'm trying to say, right?

So because it's so, well, it's such a stupid way you could argue to make a decision, maybe it motivates people to actually come to some conclusion and agree on something.

What else is there?

TTY0482 says, I think sometimes you need to improve incrementally there as well.

Forcing a team to use trunk-based when they are far away from it probably won't work.

First get them to make small working commits.

Make small steps, let the team learn, adapt, and like the new methods, then take the next step.

And then you're back to, well, what I originally said, you're basically trying to facilitate learning in the team, which is something that an HR coach would also do.

TTY0482 says also, how do you prove claims like this?

Well, we already discussed the DevOps study, and I have to admit that I'm not entirely sure about the empiric evidence in this specific case.

But basically what the DevOps study and also the Accelerate book says is, if you deploy more frequently, you get lots of benefits like, well, more productivity.

So people actually can spend more time on your features.

You also get less burnout.

And they also say that if you increase the number of deployments, you have to get rid of specific blockers.

So there will always be a blocker to get even faster, right?

And blockers might be automation concerning deployment, automation concerning testing, and eventually you might reach the point where integrating a feature branch slows you down.

And then you might, well, need to go to trunk-based development to even be quicker.

And that might be a reason why trunk-based is sort of superior.

But I actually wrote a blog article, I have to dig it out, that argues, well, trunk-based development is probably the better way to work.

But there are projects out there that use feature branches, and those are quite successful too.

So chances are that this is not the most important optimization that you have at the moment.

And by the way, even if you come up with some empiric evidence, I'm not sure whether it would convince people.

And also, actually, your case with the people that you have, it might be that the empiric evidence is not – there is always sort of a distribution, right?

It's not like every team is the same.

Every project is different.

And if you have some empiric evidence, it means that you have mean values, and your project might be, or your team might be on the edges of the distribution.

And then having empiric evidence only helps you so much.

So our next question, what does agile architecting means for the quality attributes and the decision related to these?

If we consider security as agile architecting needed, and I thought this is interesting because it sort of means that there is some choice.

And I would argue that in reality, things do change.

So we might not know that the system needs to be secure in a specific sense of the word, and you cannot know everything in advance.

So what do you do now?

Sticking to security, if we use a signal as an example, so signal is secure in the sense that it is end-to-end encrypted.

So data is confidential, right?

So it's hard to wiretap into a conversation.

But as we all probably know, there seems to be a weak protection against adding people to some chat that you didn't intend to add.

So what happened in the States was that the person who added that journalist to that chat, the mobile number of that journalist was mistakenly added to his address book as the telephone number of some person that should have been in the chat.

And the reason was because that person that should have been in the chat forwarded an email from that journalist.

He got an email that was forwarded that was originally from the person that should be added to the chat, but had the telephone number of the journalist because it was a forwarded email in the footer.

It said this is the telephone number, and this was the telephone number of the journalist, even though the email was from the person that should have been added to the chat.

So then the telephone book said, oh, great, there is a telephone number that's surely from the person that this email came from, and then this telephone number was used when that person was added to the chat.

So there is a problem there.

And it turned out that there are other problems, too.

So, for example, messages can be auto-deleted in Signal, and that's a security feature in a way.

But it is actually also a problem because the communication needs to be archived.

So even though in a sense Signal is secure, it's not secure because information is deleted, which made it insecure for the means that the U.S. government needed it for or used it for, but which obviously improves security for people like me who don't want to have some person wiretap on the communication.

So what I'm trying to say is these things, so what is security?

It's a complex issue, and you might learn that in the specific environment that you're in, a seemingly secure system like Signal is actually not secure because you're missing some points, like messages must not be auto-deleted because, you know, the integration of the address book might be a problem, and so on and so on.

So I would argue that you will learn about the domain, you will learn about the quality attributes, so therefore you need to adjust the architecture.

So it's not a choice, and it's something that you have to change the architecture and how you deal with quality attributes.

Of course, the idea is not to ignore quality attributes and make no decision at all.

The idea is to face reality and revise decisions if needed.

Just like all engineering does, this is why we build prototypes, this is why we test prototypes, and if we realize that we did something stupid, we will build the next prototype until all problems are ironed out, we can actually put the product to market or our software in production.

Let's see, there are quite a few comments.

I think the idea is if you are not using trunk-based, you're not really continuously integrating, integrating, and then need to integrate at some point.

Also, it makes people communicate in commits, absolutely, and this is also what it says in my blog post.

And tty0482 also added, and I guess it forces you to make small working commits.

If you break the trunk, it's a lot more obvious than if you break feature launch, exactly.

Okay, yeah, still time for some more questions.

What do you do when management, that's MD42Martin from Twitch, what do you do when management does never prioritize quality attributes?

Select a few yourself.

Well, how shall I put it?

It means that you will not reach those quality attributes and then your system will probably not be fit for what it should be used for, and then you have a problem.

And in my opinion, in the ideal world, this is something that a product owner should actually decide about.

And in the real world, it should be something that you should be able to talk to management about.

So, you know, we learned that we must not auto-lead messages because there are some requirements about that.

So, we must make sure that the messages are archived and cannot be deleted.

Otherwise, we probably won't go into production because this is just what compliance says.

So, do you want me to do that or do you want the product not to work?

And then it's a decision that management hopefully will make the right decision because it clearly says that you have to have that quality attribute.

And if you can't make that case, chances are that you somehow... that your thinking is not that clear or maybe the quality attribute is, in fact, not really required.

So, again, there is this idea about, you know, if you can't communicate it to management, chances are that what you're trying to do doesn't make a lot of sense, right?

It's like rubber duck debugging where you explain what you're doing to some rubber duck, and then you realize the problem.

And this is maybe the same for architecture.

And B442 says, thank you.

You're very welcome.

TTY04A2 says, I have been considering and experimenting with integrating quality requirements and security in particular into cooperative modeling systems because really both are domain issues.

Absolutely.

And we had... there are ways to do that.

And let me think because I plan to do...

Yeah.

So, I did an episode about quality storming with Michael Pluth.

And this is... quality storming is a way to collaboratively work on quality requirements.

So, that is something that you can take a look at or listen to.

Yeah.

TTY04A2 says, of course, first you have to convince people to do a collaborative modeling.

Absolutely.

But, you know, maybe these are two different points, right?

Quality.

You can come up with sensible quality attributes without doing that collaboratively, I would argue.

We are a little bit over time.

I was thinking whether I still want to... and I'm afraid that I still didn't answer all the questions, and chances are that I won't do another episode about this.

So, let me see whether there is anything...

Yeah, I think there is another one that is quite different from the ones that we discussed so far.

So, that is why it might be interesting to answer it.

So, question is, how do you deal with buyer's built decisions with engineering teams?

Isn't there a bias for the team?

Yes, absolutely.

Engineers build software, so obviously they will try to think about how to build software, and they will probably not evaluate commercial off-the-shelf products.

So, you need different people, and I think people...

I mean, so the task is to figure out whether we can buy something for this specific domain.

This is something that requires domain knowledge, I would argue.

So, you have to understand the domain in your company.

You have to understand standard software, the domain features that they provide, and then you have to come up with some kind of difference between the two and make a decision.

And this is something that different people could do, domain experts, as I said, and there are even agencies that are specialized or companies that are consultancies that are specialized in figuring out which standard product might fit for a specific domain.

And therefore, this decision is something that someone else should make, or you have to have, you know, different people working on it.

And, I mean, I work for spec labs, so we have different people on the payroll, not just software architects, and I would go to these people to figure out whether something should be bought or built.

I think that makes more sense.

Yeah, so I think we are basically done.

TTY said, thank you.

Great, thanks a lot for all your questions and feedback.

I have to admit that 1st of May is a bank holiday here in Germany, and I was somewhat afraid that people would take today off and, you know, I would be here by myself, and that was clearly not the case.

So, thanks a lot for all the discussions and the questions.

Next week, there won't be a stream next week because I'm going to be at Jack's Conference, and I'm going to do a workshop on Friday.

There will be a stream in the week after next week.

Not sure about the topic yet, but we'll keep you posted, so please take a look at the website.

Thanks a lot.

Have a great weekend, and talk to you soon, or see you soon, and all the best.