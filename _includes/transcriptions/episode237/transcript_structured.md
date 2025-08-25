# Folge 237 - Warum ist Software(-Architektur) eigentlich immer so schlecht?

And before I get started, I'll show you a few words in my own way.

There is a Spreadshirt-Shop for Software-Architektur im Stream.

I've shown it here before.

With T-shirts and backpacks and hoodies and everything you need for Software-Architektur im Stream.

I'll put it in the chat and put it in the links and link it on the website.

If you feel like wearing the logo of Lisa, that would be your chance.

Today's topic is the topic of software quality.

This is a complicated topic, you can talk about it for a long time.

In fact, I've been talking about it in the stream for a long time.

I will give a few opinions here and shorten the discussion in some places.

A motivation for the whole story is that I am a consultant.

That means I often see suboptimal software.

The crux of the consultant is that he sees things that need advice.

So that just like suboptimal software is a focus of activity for me.

The question is, what would have to change so that I would be unemployed or so that I would have to look for something new?

What I mean by quality in particular, I am very happy that there has already been a bit of feedback or questions that are going in a different direction.

I mean, especially systems that do not have a reasonable structure, where the business logic is scattered everywhere, is not structured reasonably.

So this is especially about maintenance.

Software quality, of course, also has other aspects.

Performance, reliability, security, many, many other things.

I want to save that a bit.

Quality-driven software development means that I bring these different qualities together.

But I want to take care of the durability and structure of the software in particular, because that also influences the costs of further development in essence and thus also represents the costs for adapting to new features.

Martin Egli at LinkedIn also wrote, what is a bad software architecture or how good does the software architecture have to be?

When is the software architecture good enough?

Barry O'Reilly speaks of criticality, is that the goal?

I can repeat again, that's exactly the right question.

We want to build software that works reasonably, especially in relation to the non-functional requirements.

But on the other hand, most of the things I see out there in the wild, especially in relation to the structuring, are significantly too bad.

And that's what I want to take care of in particular.

Hamburg wrote, is it perhaps due to a lack of quality assurance?

I don't mean, look, I have G-Unit Test, lack of quality assurance.

I'm not sure.

And that might also be in line with what I actually intended to say next.

That annoys a lot of people when developing.

That annoys especially technicians.

And it's actually embarrassing for some.

That was also a motivation for me to make this episode.

I come to MWI often enough, I go to MWI and do consulting.

And I'm shown a suboptimal architecture again.

No wonder.

Because otherwise I don't need any advice.

And it seems to be embarrassing for people.

Almost.

Which somehow means that quality awareness is there.

So they basically stand up and say, okay, we know that it's screwed up.

Sorry, we know.

Look, this is what it looks like for us.

Hamburg also wrote an interesting question.

Who can teach the report how to do it right?

Those who have already made a real mistake and paid a lot of money, made a big mistake, without wanting to intervene now.

I would say a mistake, and that is also a motivator for me, that you think you can achieve a very good quality across the entire system.

And Hamburg continues to ask, or those who have never made a big mistake and thus apparently know how to do it.

I'm not sure if there is, so to speak.

So there are these exception systems.

I would always come up with tech.

How do you say that in German?

The layout system, type setting system, what Donald Knuth built.

That really has to be extremely clean.

There are certainly a few examples that are extremely clean.

But most of the time the core quality is suboptimal.

And maybe that's also something positive.

Because if the things you did a few years ago are not embarrassing, you have somehow stopped.

So maybe that's even something positive.

And I had already said that it may be shortened.

Peter Sommerlath wrote on Mastodon about why the software quality is always so bad.

I ask myself after almost 30 years Posa 1 again and again.

Patterns of Software Architecture.

That's just a book.

And then he continued, plan a party next year at the Europlop.

And that fits, I think, to what he was just saying in Hamburg.

That would only help.

So not a book like the Posa book, which is certainly important.

It only helps if we don't know it better.

But I'm not sure if that's really the core of the problem.

My claim would be that in many cases the people who are sitting on the system know how to do it better.

But maybe that's also part of the solution.

I walk around here and do a lot about modernization.

These are somewhat blatant basics and hope that I can actually contribute to that it gets better.

Therefore, yes, maybe that's also part of the solution.

I wanted to talk about it here in public, because, as I said, that's a taboo topic.

And another excuse for the episode is I had the honor to hold the keynote at the XP Days in Stuttgart.

It was somehow about why agility is such a problem and why it didn't work out.

I said on a slide that striving for technical excellence, which is in the manifesto, is a problem in my opinion.

And that's in a way actually something where I ...

I got feedback on it.

There was someone at the booth, at least one or even two people, who said to me, who, I think, especially on the subject have hung up a bit.

And I'm somehow to me ...

So I let it happen again for me and I realized that there was actually something, I think, not so nice about this slide, to put it carefully.

Because actually I always try to discuss the typical problems that are out there with the customers I see are actually the problems.

To then say, the typical problems I see, I would solve them as follows.

And the typical problem out there is not technical excellence, exaggerated technical excellence, but rather suboptimal quality and lacking technical excellence.

And that's why it's a bit strange to say, hey, striving for technical excellence is a problem.

In fact, it's a bit more complicated and in a way I also stand behind this statement that striving for technical excellence is a problem.

But at the same time, the lack of technical excellence is also a problem.

And maybe, I did the episode back then with Hillel Wayne about whether we are actually engineers, i.e. whether we are more engineering, as well as other engineering disciplines.

Subjectively, I always have the feeling that engineering products that you see out there have such a high quality.

I buy a great racing bike, that looks great, works great and has a high perceived quality.

And how should I say, it's also aesthetically appealing.

Most of the software architectures that I see are not like that, but they have a lot of optimization potential.

At the same time, you have to say that the software and the architecture solve a lot of business problems.

And my computer, which is in front of me, is essentially reliable.

If it has a problem, then it's more of a hardware problem.

That means, it can't be that bad.

And Danny Steinbrecher, also from Mastodon, also wrote such a thing, because we use the wrong technologies.

That's why it's bad.

I'm very insecure.

I would say, you can write good or bad code in any technology and build things that are good or bad.

Or too few meetings.

I found that exciting.

We also identified communication in this episode of Java Forum Stuttgart as a problem.

Maybe that's still the problem.

In doubt, is it the regulatory issue or the lack of time?

And that's exactly the last point that Danny is addressing.

The lack of time is actually what I think, as I said, I shorten it a bit, is possibly responsible for that we have the problem that we have.

I wrote down time pressure.

I also wrote down wrong technical decisions, which are sometimes dropped on the management level.

So that I somehow say, okay, I use microservices, because that's how you do it today.

And that's something that's granular and management compatible.

And maybe also such things that you say, okay, I have a division of some tasks for some teams.

Also a management decision, but that's also an architecture decision, because these teams will then each work on a part of the system.

So overall, it's a bit like that.

So in the first instance, I would now that the black Peter, I think many people who come from the technical corner first, so to speak, to the management and would say, well, the management creates time pressure.

The management makes some granular technical decisions.

We do microservices, which are somehow difficult.

And he says, we have a team that takes care of the customer and then I have a customer component and we know the management of such data is perhaps a problem.

And that's just an architecture decision that is made indirectly, because a management decision in favor of the task area of a team is made.

And that means and in some places it actually leads to things that, how should I say, are somehow intuitive and sensible and logical, but then have devastating consequences.

So if I stand up and say, I can make sure that the team produces things faster, that's a sensible decision .

So I can generate some values faster, I can implement business logic and I didn't know why you shouldn't do that.

But precisely because of this time pressure that is created, it is potentially a problem.

And I actually believe that this is a basic problem.

There was also an interesting feedback at the booth of the XP Days.

The person reported, to be honest, I can't remember the name, that she had the experience that there are artificial deadlines.

So that was the deadlines, when you ask her, so there are no time-limited deadlines.

So we have to go to the first, the first or the first five somehow live.

But these are somehow artificial things.

You can't figure out why this deadline is valid.

And this person then took over the management job and then somehow actually started and questioned deadlines.

And then it broke down a bit.

In other words, it was somehow revealed that these deadlines are somehow artificial.

And I don't want to say whether this is true or not.

But I think it's credible.

So whether this is a general concept.

The statement, I think, is definitely credible.

And maybe it's just that deadlines are more of a proof of performance.

So under my management, with the team I have, we can get things in order incredibly quickly.

And then there is actually a time pressure that is not really necessary due to a deadline.

In the sense of, we really have to be online at this point, because otherwise we have any damage that arises through laws that we break.

Or because now actually someone in the market takes over the market position or whatever.

So that means this time pressure is perhaps often unrealistic.

And I think the other problem that somehow leads us to a problem, so to speak, is somehow the visibility of technical problems.

So if a racing wheel is somehow strange, then I can see it, because I can just see it.

I can perceive it visually.

And I can also see how it behaves, so to speak.

With code, at least with code quality, I can't see it directly when I look at it from the outside.

So with the racing wheel, the connecting rods are somehow shifted.

And I somehow have the wheel and the spokes and all these things.

And I can somehow see whether that somehow works reasonably and somehow looks reasonable, whether the things are somehow well shifted or not.

And with code, I just have to look into the editor and I don't see it from the outside.

And these other things are not really obvious.

So that's just because I give teams tasks that influence the architecture.

It's clear to us, that's Conway's Law, whether the management class is somehow not so secure.

These are somehow people who have a different background.

And also such a technical decision.

So why is the microservice a problematic technical decision?

So maybe it's not like that at all.

And that somehow leads to the fact that these things are actually made out of there or they lead to that we have these massive problems.

That they don't lead to these problems at first glance.

And these problems are not visible at first.

So I can build a microservices system, even if microservices are not the sensible solution.

It's just much more complex and it ensures that more servers are involved in the data center.

And that somehow the response times are slower.

But I see the slowest response times.

And this topic fits around Technical Debt.

I actually have several episodes on this topic.

I can also link them for sure.

And there's just a lot of discussion that can be had about it.

I think now that the main reason for Technical Debt is that pressure is created on the team.

And then good practices collapse.

And that's why it's important, because this metaphor, if you understand it, so to speak, says something different.

Technical Debt says, I take an active debt to pay it off later.

What I would claim now is what actually happens, that I just start and say, how do I get the deadline done now?

Then I take some wild abbreviations and then I'm at the end of a system that does what is somehow required.

It's somehow hacked.

But I somehow compromised the quality of the system.

And that's not the case that I have now actively said to myself, here, here, here and here I go into a debt and I will pay it off at some point.

But simply because I worked consistently, quickly, abbreviated, I created these Technical Debt things.

And you can discuss it more in detail.

I have to shorten it here because I don't have that much time.

I actually talked about Technical Debt for hours and then the time pressure is actually the central problem for this poor quality.

Or analogously this decision, not team distribution or the use of any technologies, which then leads to the fact that it just doesn't fit and that you then come to a result.

But that's just the opposite of what I said in the keynote.

That would now mean that the problem that we have primarily in the industry is due to high time pressure, which is not really motivating.

And through other decisions, which are made at the form of management level, we get into a situation where what comes out in the end is suboptimal.

And unfortunately that is not obviously visible.

It's not like when the racing wheel is somehow produced and we see that it obviously can't work.

It's like code and that's why it's not visible.

And that's why we have a core problem there.

These things are not so obvious.

And there's this story with what I said at the beginning.

Would it help us now if we talk for an hour about Technical Debt and understand it in detail, so to speak?

I'm not sure, because the next time when the time pressure appears or some things are decided, I will probably go back to the same behavior and run into the same problem.

And now comes the point that came back a bit from this cinema.

So that means now that in principle the statement comes, management decides something.

We just stand there and say cool that there is a decision.

It somehow leads to chaos.

We may also know that it leads to chaos.

Now the question is, what is the reaction?

The reaction to which I have now referred in the cinema is we just do the maximum quality.

So that means if you have this idea in this case it comes from Manifest or not from Xtreme Programming, for example.

We want to turn up the code quality very high.

Software Craftsmanship also has this idea.

I want to be proud of what I build.

Craftsmanship is not oriented to craftsmanship and the ideas that are in craftsmanship.

I want to build good things in terms of craftsmanship.

That means I want to deliver high quality and that everywhere.

My claim is that this is also exaggerated and that is the same only with other signs.

That means we have two extremes in principle.

We have the extreme that says I don't care what quality comes out of it.

I don't understand this technology either.

We are now doing a microservices system under high pressure and so is the team distribution, which means that technicians have ultimately found themselves trapped in a system in which they cannot build a high-quality system in terms of craftsmanship.

And the reaction is to say no, no, no, we don't do that, but we turn the quality to the maximum.

On the one hand, we have the extreme position that says that quality doesn't matter, we don't do anything.

On the other hand, we have the opposite maximum position that says quality is the most important ever and we definitely have to deliver the best quality ever.

For me, the important point is the thing that I think is extremely central is this idea of the core domain, what Eric Evans introduced in Domain Design.

And what he says is we can't reach the maximum quality everywhere.

In these two maximum positions, the one position says quality doesn't matter.

Wow, that means that we end up in a system that is difficult to develop and that is the core domain. part of a system that can have maximum quality.

And now Eric Evans comes in and says, unfortunately, I don't think he said unfortunately, but it's the case that we can't achieve maximum quality everywhere.

That's why we need a core domain.

As I said before, it's an important point not to define what is meant by quality here.

I think I tried to say it at the beginning.

I mean quality in the sense of durability, code quality, I don't neglect these things, especially the other qualities in the sense of software quality, so all the elites, not scalability, security, and what else, like performance, such things, but I want to focus on code quality and durability in particular.

So if I say, as Eric says, and I have no doubt that this is true, because I would say it's obvious, I can't achieve maximum quality everywhere, then I need a trade-off.

And that means I have to make a compromise.

And that means that exactly these people who say we have to achieve maximum quality everywhere, they don't want to meet this trade-off.

And I think that kills it.

So if I live in a reality where I can't achieve maximum quality everywhere, but I try, then I will fail, and in the end the quality is somehow randomly distributed over the system.

That means I have parts where I managed to achieve the goal with my high efforts, and other parts where I just don't have it.

And that was actually the reason for me why I discussed this topic in the keynote, because I think this approach to say, hey, we want the highest quality everywhere, and we want technical excellence, that's over the top.

We have to make these compromises and we have to actively control it.

So, and probably this problem is, I try to achieve the highest quality everywhere, smaller is the problem.

I have time pressure and the system breaks down for me as a whole.

And that's why I think, as I said, that especially this time pressure and this history are an important topic.

A short excursion, because that's also important to me, so to speak.

We also made an episode about it.

I made this episode in retrospect of Xtreme Programming.

And the project that Xtreme Programming was, so to speak, was this C3 project at Chrysler.

There is this very nice book about what Xtreme Programming is a bit of a question.

And there is one of the statements that this C3 project failed in the end.

So first of all, it's about a payroll, so it's about Chrysler's payroll at the time.

That was Chrysler shortly before the merger with Daimler in the late 90s.

And this project was ultimately discontinued and never made a significant part of the payroll.

And one reason for this may well be that this high quality requirement, together with the constant refactoring, has led to the fact that the project is no longer particularly productive.

That would have to be researched again.

I've saved that now, so to speak.

But something like that could be an illustration for this high quality requirement really leading to problems.

And that means we can't put the quality at 100% everywhere, as Xtreme Programming is trying to do.

Even if we wanted to, and I don't think we want to, because it's simply unprofitable in some places.

So we have to build as much quality as is profitable in the essential places.

That's the only real possibility.

And now it's just starting, and we actually have to get both sides together.

So that means we need management on one side, which on the one hand says, we reduce the pressure, and on the other hand also somehow says, where exactly do we need this sustainability?

So actually, quality in terms of maintenance and crude quality is a matter of sustainability.

So I can develop software with high crude quality and good maintenance at a constant speed.

And that makes sense and helpful when I have to.

So if I'm building a piece of software for a business case, I don't know, Christmas is just around the corner, where I say, I want to be live on December 1st at Advent time.

On December 24th I'll throw it away.

Then it doesn't matter what quality this thing has, because I'll never have to wait any longer.

It's only a problem if the quality is already good, while I have it out there.

So if I have to make changes from December 1st to December 24th, and they are already incredibly difficult, then it may be good to deliver a high quality.

But after December 24th, the quality doesn't matter at all, because then I won't make any more changes, but I've thrown the code away.

And it could be that I have such a case.

I think in many cases it is also the problem that management doesn't believe that this is the case in this case.

But that's exactly the problem.

So from a management point of view, I have to get a credible statement that says, then we have to have it.

So not artificial time pressure.

That's something we want to develop sustainably.

That's something we definitely don't want to develop sustainably.

Or we don't know that exactly yet.

So that's one side that makes this requirement and makes it concrete.

These are ultimately business decisions that are behind it.

So that means I have to decide now.

Do I want features?

Do I want to have sustainability?

And then I have to get started somehow.

So the development has to communicate the quality problems on the other side, so that management understands it.

And that's one of the points that I find difficult.

And that's what I wanted to refer to.

Example.

So I have a team.

For certain reasons, this team goes past a technical infrastructure component, because it is not allowed to use it.

So there is an architecture rule that says, that this infrastructure component is not to be used in this case.

Okay.

I'm a software architect.

That means what I see mentally in front of my eye is, there's some kind of thing, there's a dependency file, it's not allowed to go to the technical component.

So I have a file that's too little, that's kind of weird.

Okay.

That's kind of unpleasant.

But not dependencies that shouldn't be there or something like that.

That's my daily bread.

So I'm actually shoulder sucking.

Later, I found out that this led to the additional effort of this team, and that's significant.

That makes it from, we have a problem somehow where some boxes and Freelite don't fit together, to a problem that has some impact, potentially on a deadline and on effort.

So that means, if I communicate this problem as a technician and say, we just spent so much effort and we have so much delay because of that, I have a different communication and a different basis than if I stand up and say, by the way, there is this dependency, we are not allowed to use this infrastructure component.

Why actually?

That's actually stupid and inconsistent.

The latter is just such an abstract quality thing, which somehow doesn't say, somehow it should look like the architecture might demand it.

The first thing is something that I can calculate in euros, so to speak.

So I can calculate in euros how long I have been busy with the developers and have been busy in excess, and I can calculate in euros what it costs me that somehow this software goes live too late.

And that's something we as technicians can work on, to improve this communication.

And that's also in my opinion, so that's something that I've noticed lately.

I see in technicians, subjectively in my field of experience lately, increasingly the problem that such things are tolerated.

Nothing is questioned, it is simply carried out bluntly and there is no feedback.

Yes, dear people, you don't have to be surprised if it looks weird.

So I'm a manager, I have no idea what software architecture is, someone comes to me and says, some dependencies are weird.

Okay, cool.

What should I do?

I don't really care and I don't really care either.

If someone comes to me and says, you just broke a deadline and you just spent money, that was just unnecessary.

That's a different topic.

We can change this type of communication and I actually believe that it is our duty.

So we cannot ask people who are in such a position as management, that they just stand there and say, I can do everything that has to do with technology.

These are two different fields.

We need communication and we need target-oriented communication, which means communication in relation to costs, deadlines, such things, because that's the world in which they move.

Right.

The function fulfilled, which I would like to have.

Or, in other words, if it's more expensive, I have to have some advantage.

So I have no problem with it, spending more money on a bioproduct, because it's a bioproduct, so it has a certain other quality.

But if I have two bioproducts that apparently have the same quality, I buy the cheaper one.

This is the economic world in which we somehow live.

And that means, if you can't reason why you're doing something, so what advantage that has, then it won't happen.

And to suggest to a customer that he wants to have his stuff fast and cheap, as I said, I would like to see how you go shopping at the supermarket.

So do I go there now and take the most expensive product?

No, I don't do that.

I only do it when the more expensive product has a clear advantage.

So we have to communicate that somehow.

And it can't be how to say it now, how should I say, if I were to say the word to this person, I would say, what does that mean?

Quality means software is getting slower and more expensive.

That's obviously absurd.

So that means I have to have a different kind of communication and I have to put other advantages in the room.

And that has to work, because the way technicians suffer under it, that somehow the quality is bad, will be reduced in numbers.

It's not like you sit there and say, wow, that's slow and frustrating, but it's efficient from an economic point of view, but it goes hand in hand.

The way we technicians are frustrated and need a lot of time is something that is also economically inefficient.

And that means that you would actually have to say, if it can't be fast and cheap enough for the customer, then we deliver good quality, because that's how we get cheap software.

And I can show you with which measures we can get this software cheaper.

And that means, but that there is actually a communication problem and it's not clear to me how to communicate that clearly, so to speak.

Hamburg has now...

Sorry, I was just looking...

I just wanted to make sure that I had, so to speak, finished the thought.

Sodi in Hamburg wrote, but how do you get people to pay threatening costs earlier if you can't estimate that exactly?

I'm not sure if I understand the question quite correctly.

I'll say something about it and there's always the possibility to ask questions.

The first thing I said is I don't think that the basic problem of quality is that you say, I have a decision and I'm taking the shortcut now and I know that this shortcut has the following advantages and disadvantages, but my claim is that in most cases it simply arises due to time pressure.

So that means, if I'm in the situation that I now say, I have two options and I objectively estimate them and think about the consequences actively, then in my opinion I'm already close to the result.

So that means I'm not, so I would claim if I think about the costs and the possible effects early on and make an active decision, the problem may already be solved.

And the other thing is estimating or estimating as a basis of decision is a day-to-day business.

We do that all the time.

Agile is estimating, that's exactly the basis.

And I think what's important about it is that it should only allow a decision.

So it's not like I deduce a deadline from it and now say, in exactly 10 months we've done this and that or in two weeks or so, but it's about saying I have these two alternatives.

This alternative is more complex than the other one, but has the advantage that we are able to modify the system easier in the long term.

While the other one has exactly the opposite.

It's short-term easy to realize, but in the long term it leads to difficulties.

And then I have to estimate which of the two with what I know at the moment is probably the better alternative.

But I don't need to say that one is 10 or the other is 5 days or 10 or 5 weeks, months, whatever.

But I just have to say that's probably the thing that is less complex in total.

Not just over the longer run time.

And that means I just have to get a rough, granular estimate.

What does that mean now?

That's a bit of a problem for me.

What I would actually like would be that we would discuss exactly this discussion.

That's why the question from Hamburg fits in very well.

That we would discuss it now.

We would say to the team listen up, we have two options now.

Either we do it this way or we do it this way.

Which is the better option?

And the management has to say we will probably never touch this piece of code again or on the 24th or 12th the thing is obsolete anyway and we throw it away.

It has to be credible or not.

Maybe the management should also say well, if we didn't deliver it on the 1st or 12th it doesn't make sense anyway because then the business case is gone.

So that definitely has to be there.

So we just have to get information about a hard deadline, about a soft deadline, about the trade-off, about the things that will change in the future and so on.

We would all have to get that.

And at the same time the technology would have to be willing and able to assess the stuff somehow, as Dean Hamburg says, and somehow also trust the management that what they say, so if they say there is this deadline or if they don't say we won't touch that again or throw it away, to actually believe that.

And that would then lead to an open communication and then we would make some kind of decision.

And the problem with the matter is that I believe in the very, very most cases, or let me put it another way, I would say I wish I could, but I just can't do that in reality, mostly in the project, which leads to the fact that you can take other measures that somehow work.

So, for example, measures that you say from the 14-day sprint or 10-day sprint we'll take two days now and we'll invest them in improving the system.

And that's something that clearly says whether it's been kept or not.

We can look at it at the end and we can say from the 10-day sprint two days have actually been improved, flowed.

We can then put a checkmark and can say that it actually happened.

So it's easy.

And we can also protect this time, so to speak.

We just pretend that this team only has a capacity of eight days, not ten.

And these two days are actually for improving the quality.

So we can make sure that this time pressure is managed, so to speak, and is not too strong.

And we can somehow try to renovate this system.

The problem with the matter is that you also decouple this decision a little bit from what the management needs.

So what can come out in the worst case is that you say we're just doing this part of the system totally great and easy to maintain.

And then somehow someone comes and says here is a requirement and then you determine this requirement is somewhere else.

And what you just polished so nicely on code, that is never touched again.

But that would be or vice versa, or not.

We just build highly optimized code, nice code for things that are not used in perspective at all, and so on.

And for that, to avoid something like that, you would have to have this communication.

But it's difficult.

And what we also exclude by doing this is that we now maybe we can expand the budget.

Maybe it makes sense to invest more time in quality and less time in scraping new features.

But that would mean that we have to do something fundamentally different.

So we have to change the budget and we can only do that if someone says OK, at the moment, maybe somehow the quality is important. where someone said, okay, until the end of the year, I'll somehow keep this up, but then I'll just go.

And then he went to work with someone and then said, in the context of that, on that day, okay, I can't stand this anymore, I'm going now.

And it was because of these pains that are actually there in the maintenance, so to speak.

And that's just, how should I say, something that is quite impressive, isn't it?

And not in a positive way.

And not projects can come to this complete standstill where they are de facto no longer able to change anything at all.

And that can somehow lead to a very, very blatant, blatant problem.

At the same time, you have to say, and that's something I just said in this keynote from the XP Days, technical excellence, on the other hand, does not necessarily lead to a business advantage.

So you can also achieve a business advantage with other mechanisms.

You can exploit people, you can cheat the system.

There are also consultancies that hire new people from the university every year and don't invest in them permanently, but you expect that after two or three years, if they don't feel like it anymore, because they have to develop software under high pressure, then go somewhere else.

So that also works in our industry with this exploitation.

We are certainly privileged there.

It's a different level of exploitation than if someone works somewhere in the accord somewhere on the treadmill.

But we also have exploitation.

There are also companies that cheat the system.

The fossil industry is manipulated by the public hand and doesn't have to compete.

And that means they are somehow decoupled from the fact that they have to build technically excellent software or build something excellent there at all, but they have found other mechanisms to compete.

In other words, only software people believe that everything revolves around software, which means that competition is more diverse and software quality is just one factor that makes companies competitive.

Now comes another point that I think is totally important.

One point I wanted to make is that I think this communication is a problem and that is something that we can really improve.

And where I also find some things really difficult.

For example, I don't understand at all why people just bear without giving feedback that the systems they build are terrible and that they suffer pain every day.

I would wish and believe that you can give feedback.

And that's one of the points.

And that's not a management problem, but management decides according to best knowledge and conscience and doesn't get the right information or doesn't get sufficient information or doesn't communicate information in a way that would actually be necessary.

The other point is, and I also find it important to point out, that it is not only us as technicians who suffer from the fact that the quality of the system is somehow suboptimal, but management and business also suffer from it.

Actually, this perceived contrast doesn't make any sense at all.

And that's why I also find communication important.

And the background is simply this.

When I look at what I do, renovation of old systems, architecture renovation, things like that, that's a focus of my work.

And that's something, so not migration away from the monolith.

I want to make the system more manageable for me.

And these are projects that come from management.

Once because they are incredibly expensive.

So I say, I want to throw the system away and make a new one.

That's incredibly expensive.

That's not where a technician can stand up and say, I'm frustrated, I want to build it somehow better.

But it's something where euros are promised, so to speak, which means that the old system has been written off or is dead and I have to rebuild it completely, which means I have a massive investment.

And I don't think that people who think in terms of operations are happy when they say, we have a software that works in principle, we have to throw it away, because we can no longer operate it and no longer wait.

So that's also a problem.

And that's also something that sometimes happens, that such a management change, where it is said, okay, we have the old software landscape here and now we have someone who wants to go new, who may want to have progress in some way in the future.

And the person is now taking care of this system, actually somehow, so to speak, throw it away and make a new one.

And that just means that from this perspective, maintenance is actually important, because these are expensive projects that often do not achieve their goals and with that they suffer from their own decision.

And there is a little bit, I think there is also the way in which you operate management or how you want to work.

If I say I'm a company owner, then I want to have a sustainable business model, which is somehow sustainable.

If I have something that is measured in quarters, then in a way my incentive for sustainable development is much lower.

There are listed companies that publish quarter numbers and pursue a long-term strategy.

But you have to be able to afford that.

If you have to deliver quarter numbers, then there is the urge to generate short-term benefits.

And then you can't invest in this sustainability.

So we're actually talking about this.

Do I want to implement software sustainably in the long term or in the short term?

That's actually a business question.

And that also shows up in other places.

So there are companies, for example, a large operator of rail infrastructure in Europe would come to my mind, where you have to say somehow, they are now there and have to make sure that they somehow have to renew their entire rail network.

And that's something where not software, but something else simply has to be completely renovated.

But there are also difficulties and surprising difficulties.

So why am I doing this massive investment?

Because I'm under pressure because I want to launch new products.

Okay, which products do you want to launch?

Sometimes there is no answer.

Or it's not clear to me what this goal is.

I want to launch new products.

Maybe you can name specific ones, how that now fits together with the basic renovation of the software.

So there is also an optimization, which then somehow leads to the fact that you have to think about it.

Okay, if we now say we want to launch a new product, some new financial product, some, what do I know, a cyber insurance.

I can't think of anything right now.

And then we should answer the question in the context of software renovation, how can I actually launch this cyber insurance?

So it probably won't help me if I modernize my life insurance stuff somehow.

And you could now say, okay, cool, you're telling obvious things right now.

Yes, but I'm afraid that in many situations this is exactly the question.

So what is it that should actually happen on the market?

How does that fit with the renovation?

Often it doesn't fit together.

And I think that has this story again with, we want to develop a technically good system.

And that's supposed to be good from the start, but it's not coordinated with what's actually happening on the market.

Christian Trutz writes, I love this pain on the developer and management side.

But often the problem is that technicians and management talk to each other.

Thank you.

That's what I'm actually trying to say.

And in particular, my feedback is that we have to work on to improve our communication, because we can't expect the communication of the management to get better.

Actually, there shouldn't be this ditch.

But if there is, we can work on our side, but less on the other side.

And that means that my recommendation would be to try to move into this world or actually take someone and see what this person sees as a topic and how they typically speak and act.

We also made an episode on corporate politics with Michael Ahrens, who is a defined non-technician.

And I think you can see something about how you can communicate there.

One thought I wanted to throw in, I often have this bit of a death blow example.

Let's say I'm a start-up.

I now have a million euros.

I can survive a year with the million euros.

And now I'm starting to build a software for my business case.

And now I'm done after a year.

One scenario.

I have a dirty, terrible software, which solves the business problem.

And I have customers because of that.

That's great.

Because then I can get more money.

Or maybe I even have sales and profit and can somehow finance my further development with this money, which then possibly means that I have to throw this software away and re-implement it.

That's, by the way, if you look at it in me, what many of the big companies have actually done.

The first iteration of the Amazon software, for example, is just like that.

And the alternative would be, or the other scenario would be, that I have a software down there, which is maintainable, clean code quality, and can be developed in the long term.

But unfortunately I don't have people who use the software.

And because of that, I don't have the opportunity to make money.

Then I have a failure.

Then I'm actually dead.

That means, the software quality in terms of maintenance is of no use to me.

I just need other software quality.

I just need software quality in terms of user-friendliness and these things that are related to it.

And there is actually a sustainable development, a lot of room for error.

And that's a bit of a top-notch example.

But that's actually a typical pattern.

Many of the successful start-ups that I know have exactly this topic, that they say, we have such a terrible old monolith, we have to get rid of it somehow.

And it's just kind of terrible and unmanageable.

And that's probably exactly what's left of it.

And those are the companies that have survived it and now say, this terrible monolith has to go.

The other companies that haven't survived it probably have terrible monoliths that don't interest anyone anymore today because they're just dead software because there are no more of these companies.

And I'm not sure what that means for established companies.

So if I'm an insurance company, do I have the same thing that I say now, I want to build something and I want to open this business case and I have to do that first?

I don't know.

And then there's this question again about the time pressure.

So is the time pressure real or is it unreal?

Can you work sustainably at all?

So if the statement is now also with established companies, there is exactly this topic.

I worked on a system that had the basic assumption that orders can somehow be made to a warehouse overnight.

And that's obviously not the case today.

So if I order something online somewhere today, then maybe I want it to be there tomorrow.

That means if the warehouse starts to commission it tomorrow, that's stupid.

They should do that now, ideally somehow immediately.

And then the question is to me, when do I rebuild the system?

So that means I rebuild it from batch processing to something else.

So more batches that run, not just one per night, but that run in the hour.

Maybe also something that works event-based, that I say, okay, now an order comes in and then somehow someone in the warehouse starts running and somehow gets it.

No idea.

And then the question is, can I anticipate that beforehand?

So can I anticipate beforehand that this decision benefit of a batch is a decision that I want to review in perspective at some point?

I would say probably not.

And that's also something that's not so, how should I say, unlikely, or is now such an outlier.

So with transfer we have the same topic.

They just came over the night earlier and were just the next day.

Now they come on weekdays.

So that means the transfer system has to be modified accordingly.

And this whole topic, also monoliths and modules, is also a topic for management employees.

So there too, somehow, this availability is now a topic.

Maybe one more hint.

I promise myself a lot of this idea that we discussed in the Tidy First episode with Ken Beck.

Because he found a good model to illustrate this problem.

So he says, there are two possibilities.

I can now invest money for things that immediately bring money.

Or I can somehow buy options.

So I can now, for example, buy an option that says, next year you will get oil, steel or something delivered.

And that's just valuable, because I can now enter a planning.

So I can say for next year, okay, I want to build racing wheels.

I want to build them out of steel pipes.

So I'm buying an option that someone will deliver steel pipes to me.

And that way I can start now and say, if you want to buy my Tron racing wheels in the summer shop next year, they will cost so and so much.

And I have secured that somehow, because I have someone who can deliver steel pipes for a certain price.

And then I have exactly this option to buy them there.

And the nice thing is, if the market price is lower at that time, then I can even get them cheaper.

But I can manage my risk.

And I have the same in software development.

I can now tell the developer, just sit down and build a feature.

Then I earn money right away.

Or I say, just sit down and invest in it, that I can earn more money in a year, because then I have a system part that can be changed well.

I think this is helpful as an explanatory model.

I think it's better than the explanatory model for TechnicAdapt.

But I'm not sure if it helps, because this topic of sustainability is generally difficult for us.

So a sustainable business model, where I'm not short-term, how should I say, greedy, that's a general problem.

And maybe I don't have to be that either.

So maybe I don't have to be sustainable either.

Maybe in business, something short-term is often a good idea.

So what does that mean?

Time pressure is, I think, one of the important excuses for what we are observing here.

I should somehow meet this deviation, time pressure against the option to improve the system.

I think this Ken Beck model is good there.

I don't know if it works in practice, what leads to it.

I think this leads to the possibility to keep systems high quality in practice.

These are budgets.

But for the budgets, I have to limit the quality drive of the developers, so to speak.

Namely, I say, this is the time you have to improve your quality.

And that means this maximum quality goal, what developers have in many places and what I criticized in the keynote, is somehow difficult.

Pure time pressure from management is difficult.

I would actually like a communication about it.

And I think that's a really difficult topic.

I think it's very difficult to achieve that.

And there is again this topic of communication, which we have done a lot about communication in the last episodes, how to do it concretely.

I think that's actually the tool that is decisive there.

Which in turn means, also compared to what came up in the questions at the beginning and also in the preface, I don't think so much that the problem is that we don't know how to build high-quality software.

I think the problem is, we don't get there, so to speak.

And of course, you can also make an appointment again.

You can say, well, we have certain measures, certain architectural patterns.

Maybe they are not generally known.

Fundamentals of modularization are, for example, something where I myself have the feeling that they are not generally known, but they should be.

I still believe that actually this other topic of communication, this trade-off, that this is the decisive point.

Well, I'll check again if I missed any topics somewhere, any questions that are still there.

That doesn't seem to be the case.

Then we actually have, so I'll point out again to the Spreadshirt shop, which you can see here, where you can buy a lot of great things.

Oh, we don't earn anything from it.

That wasn't the idea.

In other words, they are cost covers, or if we actually earn something there, we can somehow make it available for a good purpose.

The next episode is on the 7th.

So that's actually Friday of the week with Diana Montaljon, together with Lisa, who then talks about system thinking.

We already had her on the stream.

It was very exciting.

Maybe you'll tune in again.

That will be in English.

Then I would say thank you very much.

Today on Wednesday, because of the holidays tomorrow and the day after tomorrow.

We won't see each other next week, because Lisa is taking over.

But maybe at another time.

Thank you very much.

Oh, no, that's not true.

That's more complicated.

So on the 8th, on Friday, Kusima Lau will be there to talk about coaching with Lisa.

And the appointment is on Thursday, on the 7th.

Lisa will also do that with Diana.

Then I would say thank you very much.

Have a nice weekend.

Have a nice holiday.

See you then.

And thank you for the questions, for the input.