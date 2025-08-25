# Episode 258 - Wardley Maps Meets Software Architecture where we will discuss Wardley Maps, and I think we still stick to that plan.

It's just that we changed minor details, probably.

So we will have an interesting discussion, I believe, in the next hour about Worthly Maps and more than that.

And we are live from AirGermany's architecture, and I suggest that we start with an introduction.

So, Simon, do you want to go first and say a few words about yourself?

Hello.

So I'm Simon Wardley, a former CEO, startup founder, advisory board for different startups, worked in government, worked across industry, and during this accidental journey, because it was more accident than nothing else, I also developed a way of mapping out my competitive landscape, both from a technological, economic, social, and political standpoint.

And I thought it was useful for me, that it might be helpful for other people, but I had no real idea.

So I made it all Creative Commons, and other people have found it useful.

So that's what I do.

I show people how to map stuff.

Hi, everyone.

I'm Svetlana Plummer, and I am an agile coach at the company called GFK, or now recently as well, NAQ.

And my perspective is more of a continuous learning person.

So I specialize in learning and organizational learning.

So recently in the meetup, we were bringing in Wardley Mapping in the meetup.

So we were practicing this, and I discovered that.

And I'm more of a beginner with this technique and excited to bring it in and explore within our learning sessions.

So I'm pretty much hyped up, I would say.

Hi, everybody.

My name is Carola.

I'm from Hamburg, from the company Workplace Solutions WPS.

And my role is architect and managing director, and I did a lot of work on architecture reviews and how to find out at what state you are with your software architecture.

And Wardley Maps, I know them, I've seen them a lot, and I heard your speech this morning.

So I'm very curious to discuss this topic from the viewpoint of architecture.

Hello, my name is Markus Hatter.

I'm working for InnoQ.

I'm doing legacy system modernization.

And someone just said you poisoned some people with your thinking and Wordly Mapping.

I think I'm one of those people because I'm using that in the background for diverse consultancy projects.

And when it's the time, I take out some ideas, discuss it with my clients or with other developers to show them a path to the future, for example, or discuss what they should get rid of.

So that's what I'm doing with Wordly Mapping and software architecture in general.

So first question is, what are Wordly Maps even?

And why would we care about that?

Okay, so I'm going to explain the origin of them.

So I was running a company, a software company.

We had about 16 different lines of business.

We were growing.

We were making good profits.

One of the lines of business was online photo service.

We also provided almost CRM as a service to others.

This was back in 2004, 2005.

And one of the things I started to realize was I was creating strategy documents for the organization, saying where we should go, but that was based on copying others.

I really didn't understand the landscape that I was operating in.

I didn't even know there was such a thing as a landscape.

All I knew is I created these wonderful strategy documents copied from other people.

They were mostly gibberish.

We were making profit, though, but I had no idea what I was actually doing.

So I ended up in a bookshop in London, in Charing Cross, and I was talking to the bookseller, and she asked me had I ever read Sun Tzu's The Art of War, which I hadn't.

And she persuaded me to buy two different versions, and I'm grateful for this, very grateful, because it was in the reading of the second version, they're all translations, so they're all different, that I noticed there was this pattern Sun Tzu talked about, five factors that mattered in competition.

One, have a purpose, a moral imperative to do something.

Two, understand your landscape.

Three, understand your climatic patterns, so the weather, the heavens, how the landscape is changing.

Then you're into principles of organizational doctrine, and finally you're into the leadership and gameplay.

And this got me really fascinated by this idea of how you observe your landscape.

Now, I hadn't done an MBA.

I still haven't done an MBA, though I do teach on a number of MBA courses now.

So I sort of assumed that this understanding of your landscape is obviously what you learn at MBA places, and I didn't have that, so I struggled with how would I understand the space.

And so in the organization, I said, right, do we have any maps?

And people gave me loads of maps, business process maps, my maps, customer journey maps, just maps, left, right, and center.

And I started taking these maps and moving components on them and realized that it didn't change the map because none of them were actually maps.

They were all graphs.

They were node and connection diagrams.

And the difference between a map and a graph is that in a map, space has meaning.

So you can't simply move a node without changing the meaning of the map, and that's why they're good for understanding landscapes.

So I then said, right, you've got to create a map.

How?

It took me about nine months, 9,223 publications to develop a way of mapping the space.

And to make it, to simply describe it, you start with thinking about who are your users, and then you ask the question, what are their needs?

And then you ask the question of what components does that need?

So if I'm doing a tea shop, I may say the users are the business, the tea shop, and the public consumers.

Public consumers have a need for, say, a cup of tea.

And as a business, I have a need to sell cups of tea.

Great.

A cup of tea has needs.

It needs a cup.

It needs tea.

It needs hot water.

Hot water has needs.

It needs cold water.

It needs a kettle.

Kettle has needs.

It needs power.

Now, that gives me an anchor, as in the users, and a chain of needs, which we call a value chain unless we're crossing organizational boundaries, in which case we call it a supply chain.

But the problem is that's not enough for a map, and that's still a graph.

So what turns it into a map is a realization that all of these nodes, whether they're practices, data, knowledge, values, or physical activities, they're all forms of capital.

And the 9,223 publications was the text analysis that I did to discover that there were four common stages for how this capital evolves.

We start off with the genesis, novel, and new items, which these are just labels for stage one, two, three, and four.

We don't have to use, like, genesis.

Another label we can use is concept.

And then you get the emergence of custom-built examples, which we call emerging.

And then you get products or rental services, which we call converging.

And then finally you get commodities, utilities, and things we call universally accepted.

So if I just simply take my value chain and just go through each component and ask that question, how evolved is it, that generates a map.

Now the map itself I found useful for myself for identifying patterns of change, where things were going.

I used it very successfully in places like Canonical with Ubuntu.

I also used it within government.

We saved quite considerable sums of money by doing this stuff.

And I found it useful.

And I sort of hoped there were other people out there who hadn't done MBAs or hadn't learned the proper way of doing it who might also find it useful.

So I made it all creative commons.

And that's where it just started.

So, I mean, with the example that you also gave in your keynote this morning, you're basically saying that I think on the left-hand side, on the right-hand side there are the things that are commodity industrialized, right?

Yes, correct.

So in your example with the T that would be like the power that you can just get out of the power grid.

Well, if you think about a cup of tea, you'd think.

So with the worldly map, you have the anchors, the users, the chain of needs, and then you position things along that evolution access from Genesis custom-built product commodity.

The right-hand side is commodity.

The left-hand is much more Genesis.

And so if you think about a cup of tea, you would go, well, power is very much commodity.

Cold water, commodity.

Hot water, commodity.

A cup, commodity.

Tea, well, we buy that by the kilogram, so commodity.

So pretty much everything is sort of a commodity.

But, of course, in the tea shop, I want to differentiate with other tea shops.

So I might add sort of other experiences.

Maybe users want a comfy place to sit.

Well, they've all got a comfy place to sit.

Okay, maybe they want a barista.

Well, they've all got baristas.

Okay, we'll have parrots as our baristas.

That's something totally novel and new, which nobody else is doing.

It might not be a sensible idea.

But the point is that I express what I'm trying to do on the map, which also enables other people to challenge.

So one of the things I found in business, and I was guilty of this as well, is that in business we tell everybody that great leaders are great storytellers.

So when I have a story, if you challenge my story, unbeknownst to you, you are saying I'm not a great leader.

And so people get defensive.

One of the beauties about putting it on a map is I can say the map is wrong without saying the person is wrong, which sounds like a sneaky trick.

But to give you an example, I mapped out cultural systems.

And to create a generic map of culture, I took two groups in the U.K.

One were Brexiteers and one were Remainers.

And I put them in a room, and these groups would not talk to each other at all.

So if I said, who wants a cup of tea?

If the Brexiteers went, yes, the Remainers said, we're having coffee.

Anybody want a biscuit?

The Remainers went, yes.

The Brexiteers were like, no, cake.

It was like no agreement.

But we managed to have a discussion through the medium of a map.

So I often use this for quite difficult subjects where we have conflict in that space.

And also, I mean, with the example of the tea shop, it becomes quite obvious that you have to really think hard to differentiate yourself because all the stuff is commodities.

So it sort of shapes your thinking, I believe.

At least that's what I got from that example.

Well, hopefully it helps.

But I also, on the tea shop example when I'm speaking that I use, I also deliberately put kettle in custom built.

And so I don't tell anybody other than the fact they can see it on the map.

And people come up to me and say, your tea shop example, why have you got kettle in custom built?

And that's exactly the sort of response you want, is you want people asking questions about why we have things, why do we treat this thing in this way.

One thing I was noticing when you were speaking about it being easier to challenge a map than an idea of a person because that could be taken personally.

Yeah.

I was thinking that it's actually also the exercise when we create a map, we usually create it together.

Yeah.

So it's not just one person that's making it, that's maybe also making it easier then to talk about things from a distance.

So that's an incredibly valuable point.

I mean, generally when discussing things, I find that the ideas that I need are within the heads of multiple people.

So, for example, I took a group of doctors and clinicians and we mapped out the area of health care from multiple different perspectives.

Now, the answers that we needed weren't in just one person's head.

They were in many people's heads.

And so by using the map, we were able to bring all this stuff down and actually get a general consensus discussion about what mattered.

And we did the same with the cultural map with the Brexiteers and Remainers.

Even though they couldn't talk to each other, we came to a consensus on the map itself.

It is a way of getting consensus between multiple people in often difficult areas about a space or what we perceive to be the space.

So mapping with others is important.

I've never used worldly maps myself yet.

That's okay.

But I've looked at them a lot and I really love this idea of this x-axis with the genius stuff and the commodity and all that.

Yeah.

But the point where I'm always struggling is when I ask myself, well, you should do that with a customer.

And you already said that a bit.

There are these nodes and they can be, from my point of view, if I look at it, computer, computation, energy, whatever, they could be whatever you want.

You said they could be a lot.

You just mentioned that in your explanation in the beginning that they could be any type.

How do you decide?

What would you write next to a node?

I'm sorry.

No, no, no.

It's a fantastic, fantastic question.

First of all, in defense, I'm going to say the geographical parties to mapping, so mapping of the territorial space, have had a few thousand years to get this right.

Yes, yes.

We've only been doing it 20.

Part of the problem is that people say to me, how do you create a map?

How do you know it's got the right bits within it?

Because I can map ethical values.

I can do data.

I can do technology, economic patterns.

I threw them all into a map.

So how do I know the map is right?

The first thing is to realize, we'll start with something very simple, the idea of competition.

So the idea of competition, comp and pater means with and to strive for.

So competition is the act of groups of people striving for something.

And we often do this in different ways.

We might do it by fighting others, that's conflict, laboring with others, collaboration, or helping others, cooperation.

So all of these are aspects of competition.

And when we are competing with each other, in the territorial space, it's easy to see we have a map of the landscape.

We often have our borders.

This is the bit we'll conflict with others.

We'll collaborate with that group over there and cooperate with them to conflict with them or whatever it happens to be.

Now, we don't just compete over a territorial landscape.

We compete over technological, economic, social, political landscapes.

But we don't map those spaces out.

So the point about doing this map is to look at those different environments.

So when I start, I start off with a blank piece of paper.

And I go, right, that's my first map.

It's a blank piece of paper.

And then I go, okay, well, let's think about some users, put them on, some user needs, put them on, put some components, put them on, and we're having a discussion as a group.

And I normally time box it by two hours.

And at the end of the two hours, I just simply ask, do we have a better map than we had beforehand?

Is it better than the blank piece of paper?

And if people agree, it's helping us to have better discussions.

We stop, go away, do something else, come back the next day.

And we say, right, we spend another two hours.

Just map it out a little bit more.

And so we keep mapping it out.

And we ask the same question at the end.

Is this better than the map we had the day before?

Well, if it is, we continue a little bit more.

And we only do it four or five times.

And the goal is to get to a map that we all agree is a useful vehicle for discussing the space that is helping us to have conversations.

And that's the goal.

Now, sometimes we achieve it.

Sometimes we don't.

Most of the time when doing the maps, what we find is we take, we throw components on there.

We might go into the weeds on something, really into the depth of something.

And then we go, well, that's far too deep.

We'll put that on another map because you can have high-level maps like atlases.

And each node can be a map itself.

So you can go really deep.

And we might go, oh, no, we'll throw that onto another map.

It's not really relevant.

We'll just call that one thing, like compute.

We don't need to know about CPU and networks and all the rest.

But we might go, oh, there's this really low-level component, which is actually really important for this high-level map.

So we'll bring it onto there.

So we'll mix and match until we get something that as a group we find is useful discussing what we're trying to do.

Now, what is the form, the structure?

Is there a guide to?

We've only been doing this 20 years.

I come back in about 400 years or 300 or 200, whatever it takes.

And, well, it's a learning process to understand how to do it, as far as I see, and that's absolutely fine.

And you can go more abstract or more in detail, whatever is needed in that proper situation.

Absolutely, totally agree.

That's a bit the point.

So is there also a nice migration plan for software architects who already have some diagrams?

Or can it just kind of transfer those to what the maps or doesn't it make sense because it's better to start from scratch because the value is in the communication or the likes?

So that's a really interesting question.

Again, you know, we'll often have pre-existing stuff, architectural diagrams, the income statement for a company.

If I'm mapping out a company, the income statement is usually really useful because it tells me, you know, I'm spending money over here and here.

If I dig into it, it tells me what components are really there because we're spending money on those components.

So I can extract that information.

If I'm mapping a nation state or mapping an industry, there'll often be things like, you know, policies being announced, which will tell me there are components that I might not have considered.

I did a lot of this when looking at China versus comparing to the U.S. back in 2014, 2015.

So there's often many different form informational sources.

One of the most interesting ones is understanding of the supply chain because that supply chain is cross boundary value chain.

So it's not just one organization, many, but we tend to be, we have poor information in that space.

In most industries, most industries, we know what we call one up, one down, who we sell to, who we buy from.

But we know little more than that, which is why we get all these problems when you have things like Brexit or COVID or whatever or Ukraine.

We have all these difficulties in the supply chain.

And there are examples like in Hungary, they actually graphed transaction level for VAT.

So VAT records and they created a graph and that told them that the entire economy was like dependent upon 100 key companies, about 75 percent.

Any one of them having a problem, there was big problems and they weren't aware of this stuff.

So other information sources are always, always useful and good.

But again, a lot of the information is in within people's heads.

And the other thing is a lot of the information sources aren't really information sources.

Their beliefs or statements of belief about how we think operate, not necessarily how that thing operates.

So you've got to be willing to dig in and challenge when creating this stuff.

Does that make sense?

Also, we're interested in non-application or what maps outside of software development.

So you said you are using it maybe internal for training or you are getting started in this area.

So what do you want to do with what maps in your case?

We have a very interesting meetup community in Berlin, collaborative modeling.

And recently we brought in worldly mapping because we just get together.

We want to learn about something and we do it together.

So we brought them in.

We've done a couple of mapping.

And now I'm trying to see if we can get it somehow also in the company.

So we haven't been there yet, but we've done some learning experiences together.

And I believe it's a really nice way.

All of these things that we just talked about, for example, the collaborative nature, bringing out a different way to look into how our teams are working, how our delivery is going, for example.

Or are we meeting those user needs?

Do we know them, especially if we are on a team that's not really directly collaborating with any users?

For example, internal platform teams, they are oftentimes not so aware and really thinking about strategy.

Not only on a higher level, but also with the teams who are not so aware about why certain decisions are being made.

I feel like this could be very useful on different levels in the organization, not just above.

So in your keynote this morning, and also when we just met and had a discussion about what we want to discuss here, you made a very good point about how diagrams, in particular architecture diagrams, often just represent beliefs.

And what you also said is, or the question that I think you even asked is, why are we still using diagrams that are not generated from code?

So why are we?

Obviously, diagrams that are generated from code do represent the reality, because they are generated from the code.

So they are an abstraction over the code.

However, if someone actually draws an architecture diagram, it's usually just, I would say, a lie, because it doesn't represent reality.

So why do we keep doing that?

And what's the value?

Because at the end of the day, reality is about reality.

And if we have something that isn't based on reality, we can't have a sensible conversation, can we?

So the interesting thing about that statement is that statement applies just as much to maps as to other diagrams.

So if you think about all maps, even territorial maps are imperfect representations of a space.

So if you think about a map of Paris, if you wanted a perfect representation of Paris, it would have to be one-to-one scale, which means it would have to be the size of Paris.

And of course, as soon as you created it, it would be completely useless, because somebody will have moved something.

So you generally have to accept that all maps are imperfect representations of a space, but they are vehicles by which we can come to a common sense, common understanding, discussion of the space.

Now, to the question, ideally, the maps would be generated through the data within the system.

So, for example, we do have things like we do sales tax VAT in the UK.

And because we have that interaction between companies, if we tracked at a transaction level, we could at least graph all the different components going between one company and another.

We don't do that.

We don't collect that information.

Of course, we need to go further than that and ask the question about how evolved the components are to generate a map.

But you could see a lot of this stuff over time could be directly generated from a system, but it's not.

Now, let's get to software engineering.

When we talk about software engineering, we often have architectural diagrams, and they are no more than statements of belief, what we think is there.

If you generate the actual structure from the code itself, and this is something I do with the people at Think and using things like glamorous toolkit and multiple development.

So, you generate the system from the code itself.

You'll often find our architectural diagrams are missing components and often critical components.

And we have this problem with migrating systems.

And it's not because people are doing a bad job, but it's difficult to manually keep up with something in an environment that's mostly constantly changing.

So, the question is, is this a new problem?

No, it's an old problem.

The question is, why aren't we generating architectural diagrams from the code itself?

Because the code actually represents the source of decisions that we're making about a system.

That's where the real decisions are happening, not in the diagram.

So, why not generate it from there?

And the answer is we don't, generally.

And it doesn't mean that architectural diagrams aren't useful, but again, they're very imperfect representations.

And I think there is a general issue in software engineering, which is related to the tools that we have.

That is a slightly different topic.

But before we get into that topic, does anybody want to jump in and tell me why I'm completely wrong on architectural?

Not wrong, but I mean, I'm doing a lot of work where we look into the structure of the system with tools and to the source code.

And you could say we generate a diagram, but not all information for the view we are heading to, the architectural view that we want to see is in the code.

So, we need what is in the brain of the humans to get out the architecture.

We do it on the code, but we say, OK, this package tree here belongs together with that one.

And we put them in one architecture element, which is not visible in the code.

And we think, I mean, and then we have the architecture as it is in the code, but with some extra information because this information is not in the code.

And then we discuss with the architects the target, where they actually want to be.

And then we compare them and see, well, oh, this is like just little mistakes we have to clean up.

And then we see the real problem.

And then we could do some refactoring.

So, for me, this phrase diagrams, we should just generate them.

I understand, of course, and we are doing that, but not all information is in the code.

These are fantastic points.

The reason being is that there's a tool called Online Worldly Maps where I can write code to generate me a map.

And so, I do these exercises where we map out things like manufacturing or transportation or energy, entire industries.

And so, I have one particular map, which is about coherent city transport.

And it was built by all these city planners.

And in this map, when we're looking at the map, we're talking about objects, relationships and the context.

And as a result of looking at this map, we had this discussion about how the Internet is actually a transportation system.

More people use the Internet, it impacts other transportation systems and impacts roads and things like that.

And why that's interesting is if you're planning to reduce congestion, one of the ways is to get people online.

Now, we built all these wonderful digital twins of cities and we sort of ignored one of the most important transportation systems there are, which is the Internet, which was quite an amusing realization.

However, that particular map was produced by this code on Online Worldly Maps.

And when we're talking about the code, we're talking about the rules, the syntax, the style.

But when we talk about the map, it's the same thing but a different representation.

And it's generated from it.

We're talking about objects, relationship and the context itself.

So, very much the nature of our conversations changes depending upon the medium.

And I see this in engineering departments, which is why I made the comment that if you go into an engineering department, you always see whiteboards because there's two conversations going on.

One is on the screen, which is about the code.

And exactly the same problem, we're having a different conversation on the whiteboard.

There it's about the objects, relationships and context.

The interesting thing about the large language models and code training is we've trained them on the code, but we never captured the whiteboards that went with them.

So, we've missed out all that sort of important information.

So, I love the idea that there is additional information.

Of course, I'd want that to be captured.

That intent should be somehow captured with the code.

It'd be great if we could pull that, but we're not there.

Well, it depends.

I mean, if we use tools like ArcUnit, where you can put in architectural rules and get them checked, but you have to discover them before, of course, and you can put in the structure.

And it's like testing every time if the architecture is in place.

You could use that one as well and put it into the generation, but most of the people are not there yet.

So, this is why they need it on paper or on their board.

Sorry, I'm just jumping.

I wanted just to add because architects always look for the why, why it's something there.

And the code is just what I would say.

So, we see what is there.

Maybe we see how the code was created because we could look at the history of a piece of source code, for example.

We can see maybe the user story where someone said, hey, we need to implement a feature.

So, this is why this code exists.

But the why, why did we program it this way and that way?

I think that's some missing information that we couldn't get out of the code.

But I think we could add some information to pieces of code or pieces like a waddle map to tell people why the code is this way.

That could be a puzzle point.

So, there is a comment on YouTube by a person called Jude Root.

So, they say, then we need to define points of abstraction software that should represent the abstraction we need in a map.

On the other hand, the software is situated at very low level.

Not sure what to make of it.

I mean, you, Carola, just mentioned ArcUnit.

So, there are tools that actually allow us to define more cost-strained parts of the code that we would then map out or show in a diagram.

I believe you have something to add.

Yeah, that could be a way.

You could add some additional information to the code to bring in these kind of abstractions.

So, for example, if you have object-oriented programming languages like Java, you have packages.

And then you could say, hey, a package for me is a specific component of my software system.

Be it some functional module, be it some technical aspect like a repository that was data to database and so back.

You could enhance this kind of missing knowledge maybe in the code directly and then go to these kind of new abstractions.

But, you know, what I've seen everywhere is when people are working on some software and programming, their job is to add some functionality.

And their job is not to think about the architecture.

And they don't at that moment.

So, they just create another package because they need it and give it some name.

So, I think this discussion of the architecture on the board or with a tool or wherever, you know, this is, as you said, the information is in the heads of some people or in the head of the architect.

And you have to get a common understanding of your idea, of your goal, no?

You look at it differently.

I just want to go back to that point that you make about how software architecture diagrams often represent the belief unless they are generated.

And I thought that was really a powerful statement.

And the discussion that we're having right now and also what you just said seems to me like, okay, this is a weakness.

And we really want to have diagrams that express what is actually there.

Like we would generate them from the code and make a one-to-one mapping.

And I have to admit that I'm not so sure anymore.

Because you made a very good point at your first statement about how actually at least worldly maps are – you could even argue, I'm not sure whether you would agree, are just something to have some conversation going.

So it's probably about the process.

And that means if we have a process that leads to something that we draw and that is our belief, the process itself might be valuable and also there is something in there.

And that's sort of new to me because, I mean, I intentionally said that's a lie what that diagram represents.

I think belief, obviously, that's not a lie, right?

It might be a misconception.

It's belief.

Exactly.

And the point that I'm trying to make is it might be interesting to say, okay, this is the belief.

This is the process that we took to come to that belief.

Here is the reality and there is a difference between those two.

And does that help us about the process in coming to an architecture?

Interesting.

And that is why that resonated to me because originally I would have said, why don't you just generate the stuff?

It doesn't make any sense.

And now I'm not so sure anymore because it gives a perception of the humans of the system and that's quite interesting.

I think that is interesting.

First of all, architectural diagrams are statements of belief where they're hand-drawn.

We accept that.

If we want to understand the architecture that exists within a system, you have to derive it from the system itself, the code, the modules, how they're communicating with each other, which you can do.

And it's often a much messier, a much more complex diagram and complicated diagram.

And there can often be entire components which are missing from whatever architectural diagrams you have.

I mean, I have numerous times.

We've had systems where there was strong belief that this is what it looked like.

And when you actually went to the point of the code and the interactions, there are entire systems that people had forgotten about, which were actually within the system.

So you have the reality and you have the sort of belief.

But I think there's this interesting connection between why do we make – the code is a record of the choices that we've made.

And some of that you can get with GitHub in terms of changes and repository.

But there's also missing information as well.

I think this always can be enhanced.

What was the intention, the purpose behind doing something?

Because it might have started with one purpose and ended up changing.

But we should – all of these things could be – I would like to see them recorded.

I think that's useful additions.

And I think that the process of creating the diagram, it's interesting to go through the – let's create an architectural diagram.

Okay, we accept it as a belief.

Why is it different from what we've got?

That's an interesting set of questions actually.

I was thinking as well, like, what if we actually just find both useful, just in different contexts?

Like, for example, when you are drawing something, you don't always let the experts do it.

Sometimes you have somebody that's new to the team, somebody that wants to understand.

So it's useful to just try to draw something first yourself.

Then maybe you have something in the code that can generate.

And then you can compare and see, okay, oh, my understanding was wrong or, ah, my understanding was right.

I do that very often with clients, you know, when they want to grow their team and they want to add some people.

We choose just a half day and look with a tool on their architecture and discuss their idea, how it should be and how it is.

And we map those things.

And the people, the new people, they learn so much.

You know, they understand, oh, you want it like this.

Oh, and in the code it is like this.

Oh, and yeah.

And you plan this.

Oh, yes.

And now I understand the structure.

It helps so much to find your way around.

So I say, okay, we're going to get into the AI stuff in that particular space as well.

I mean, if I look at groups like FENC and Tudor Gerber and the whole glamorous toolkit stuff, we'll often find examples.

Literally, if people, you know, they have an architectural diagram for how they think something works.

And when we dig into it, we will find missing systems.

And it's always an interesting conversation to follow the data lineage through a system and point out you've got these other third party systems.

And people are unaware because often these are big systems and it's taken time to build and all the rest of it.

And people have gone and people forget about things.

So I'm not knocking architectural diagrams, but I'm just recognizing their statements of belief.

And the truth is the system itself.

Now, the large language model AI stuff as well.

I'm seeing the code, I'm deciding, you know, I'm making the decisions, what's being included, etc.

And then there's the other side, which I call vibe wrangling.

I know it's called vibe coding, but it's a non-deterministic language.

I'm not really coding in the same way, I'm more wrangling the AI to generate me something I find useful.

But in that world, when it's really full-on conversational programming style, I am just communicating through prompts.

I never look at the code, so I hand over all the decision-making and the architectural choices to the system itself.

And for me, one of the big things about architecture, ultimately, well, it seems to, one of the things that is coming up is we have to decide or find a way of deciding contextually within a system, where do humans matter in terms of decision-making, and where are we willing just to hand it over to the machine, because it's going to happen, but it's a question of whether it's controlled or not.

I have to admit that I liked your point in the keynote about the tests that you had generated, that were entirely fake.

Like what was it?

They basically said, I don't know, it was just random output, right?

Because I do these experiments, which are pure conversational programming, I'm just within the world of prompts, and I was building this system, I thought it would be really good to have some testing in there as well.

So I asked the model to create me a testing engine, created a testing engine, great.

And I said, right, for every function, we'd go along, add a new test to the testing engine, and I asked it to give me a graphical output.

And so I'm building this system, and I'm looking at my graphical output, and I can run these tests, and it would go pass, pass, pass, and every now and then, there would be an error.

So I asked it to build me a log for the errors, so it did that, and I'd copy it and paste it, here's the error, can you fix it?

And the machine would go, fix the error, we've increased the version number to dot, dot, dot, and we'd carry on, carry on, building more and more tests.

And eventually, I was like, something is not quite right here.

And I couldn't get to the bottom of it.

And eventually, I broke my rule, I said, I'm going to have to look at the code.

So I went to look at the code.

And it hadn't built me a testing engine, it built me a simulation of a testing engine, so that every time I updated version numbers randomly, every now and then, it would fail a couple of tests.

And every new test it was adding wasn't testing the code, it was just the message that should be given and the frequency of failure rates for it to randomly appear.

So I've been hoodwinked into believing it had a testing engine, and it was just a simulation.

And you know, that is why, I mean, with this example in particular, I think it's a very good example, I don't see how you can give control to these systems.

I mean, it's just beyond me.

I don't see the perspective, because what this thing does is it produces fake code.

And it led you to believe that there are tests when in fact there are none.

So if you give control to this system, and you build software that actually matters, I don't see how you can do that, because it's just fake code.

And now you could argue, and that is something that, how shall I put it, that quite a lot of people do, that these are hallucinations and that they will be fixed.

First of all, I have to admit that I have a problem with the term hallucination, because hallucination is about senses, right?

So I can have the hallucination that there is someone in the room who isn't there, and that's just because I have, you know, my vision is not okay.

That's not what these models do.

They don't have any senses.

It's different.

It's fake.

It's fake stuff that is generated.

And I don't claim to be an expert on AI, but I mean, this is what these things do, right?

They generate stuff that seems plausible, and they are even optimized for creating stuff that seems so plausible that you fell for it, at least for some time.

So I don't know.

I mean, it's a tough problem, because there are things that I can certainly do, I myself can certainly do just with an AI, and they are very helpful.

So I could certainly try to change a JavaScript program, even though I'm not really familiar with JavaScript.

So that is something that I would only really do if I had an AI, and that is something that I would dare to do with these kinds of supports.

I mean, I could learn JavaScript for that sake, but, you know, it doesn't make any sense.

But on the same side, I'm really afraid of these kinds of things, because it's just a problem.

And it's not like this is the only time this happened.

It's something that happens quite frequently.

So we had some episodes on the stream where the systems were asked to create some kind of architecture documentation, and it was just hallucinated.

It was not for real.

It was just some requirements that it spelled out.

And I don't know, I'm pretty...

And we had this other thing that was an unconference, and we had cursor, and we had the system generate some stuff in TypeScript, and we ended up trying to make it do proper exception handling.

I mean, in retrospect, I would say we sort of misused the system, because we should have just fixed the exception handling.

But still, it means I have to deal with exception handling in TypeScript.

So I'm not sure.

And in particular, I think the question that is really interesting is, what am I supposed to do right now?

Like, you know, what am I going to do now in software development differently?

And I think that's a really tough question.

So it is a tough question.

I think from an architectural point of view, it is the question of where do you value humans in terms of in the decision making.

So if I'm building a prototype of something, it's something which I'm going to throw away.

It could be TypeScript, it could be local storage.

So there's no authentication, nothing along those lines.

There's no keys to anything.

I'm quite happy to vibe my way to a prototype, knowing that the code behind it can be all sort of, because I can show it, I can demonstrate it, I can put the game online.

It's relatively safe.

Now, if I'm taking any large, complicated system with many components, I mean, some of the components on the map are outsourced.

Others I might do vibing there.

Others, I'm going to want to see what the code is.

I'm going to want somebody with experience of the space to make that assessment.

I can't just, and that is a judgment call.

That's an architectural call.

And I agree.

And I think that's also something that is very valuable also about watermaps, to make this clear distinction.

At the same time, that is also something that crossed my mind when I was listening to your keynote.

In a way, what we see there is something that allows us to write code faster.

And if we work on that abstraction level, where we would just do the prompts, we don't intend to understand the code.

Now, most of the work that I do, and I believe it might be the same for, well, quite a few people here in this room, is our clients that lost control of their code because they don't understand it anymore.

And they are looking for some kind of solution, which usually means somehow make the code understandable, change it in a way, even rewrite it.

That means that they're basically saying, okay, we're going to throw it all away and we're going to do it anew, which is not such a good idea.

You should do it in iterations, but that's as desperate as they are.

Now, we introduced a technology that allows us to generate more code quicker.

I think, in a way, that's a good thing because it means that I'm not going to be out of a job for the foreseeable future, but for the industry as a whole and also for my customers, I'm not sure whether it really solves their problem.

So now we get into another question of software engineering because there's one question which is about when the system builds the code for me, it's making the decisions.

So I'm just accepting the fact that it's making the decisions.

When it builds the code and I assess that code, I'm into software engineering because I'm no longer just relying on it.

I'm actually looking at the system itself.

But now we're going to another area of software engineering because when we think about the process of – if I go back to the physical world and I love making soups, so in my kitchen I have a kitchen blender and I make soups with my kitchen blender.

Now, if I wanted to build a deep shaft mine, I would not attempt to do so with a kitchen blender.

I would use a different tool for building a deep shaft mine.

And that's what we do in engineering.

We build tools for the problem.

And the interesting thing about software is though the tools and the applications are all symbolic instructions, we don't seem to build tools for our problem.

We seem to try and use standardized tools and exact them to our problem.

There is one exception to this and that's in the testing area.

And there's an industry, the gaming industry, which is a bit different.

So in testing area, test a very, very small tools, input, output, and a flag.

And what we do is we build the test to the problem.

So we have a problem.

We build the tool.

In this case, it's a test to the problem.

And we might write code before or after, depends on if we're using test-driven development.

But all these little micro tools are contextual.

No one turns up with a hundred thousand Acme test suite, please buy this, because you'd be looking at them thinking, what's the point of that?

My tool, my test have to be to my software problem, my context.

But we don't do that with other tools within software engineering.

The exception being the gaming industry, which spends all its time building tools and then uses the tools to build the game.

In most engineering spaces, we don't build tools for the problem.

We try to use basically a set of pre-existing tools defined for somebody else's problem.

And this leads us into a painful world of rather than being able to visualize the environment, building the tool to visualize the problem, help us increase our understanding.

We have to constantly rely on reading code.

And a vast majority of what we do in software engineering is reading code to try to understand the system.

And a vast, if you ask my software engineers, they say 50, 60% of their time is reading code.

If you ask software engineers, how often have you thought about the process of reading code and why we need to do it, it's non-existent.

People just don't think about this problem.

So I think software engineering has to change, not just because of the use of LLMs, but the practice by which we go about it.

I think architecture is about decisions, and we need to think closely about that.

Sorry, I'm chatting far too much.

Apologies.

Well, no, no.

I mean, concerning reading code, I basically couldn't agree more.

And we actually had an episode with Ferdinand Hermanns about how to read complex code.

So there are people who actually do work on that, and she's even in academia, so there is proper research and there is code reading clubs that's, I think, an idea of hers, which, I mean, as you said, we spend, or software engineers spend a lot of time reading code, so they should definitely, well, work on that.

There was this point that you made that the whole industry will have to change in a certain way.

So this was, for me, very interesting in your talk today.

When you were talking about the different stages, genesis until commodity, you were saying that, of course, in management paradigms, we would use different paradigms for each stage.

Different labels, yeah.

Agility would be the first one, then you have, like, lean, then you have whatever until the end.

So then you showed that diagram when you're saying, okay, now we can use chatGPT and tools like that for the genesis part.

So what about our management paradigms?

What about our way that we organize in a company?

How would that change when we do a change like that?

Oh, gosh, those are all really big, hefty questions, aren't they?

So there's a number of dangers, interesting points, particularly with large language models.

They change the tools that we're using.

So we're changing from things like more defined tools to things like co-pilots and chat.

They change the language that we're using.

We change the medium which we're using, and all of those basically control how we reason about the world.

So one of the dangers of these systems is they create new theocracies, new belief systems.

So when thinking about using them, if I take an example, government policy, if you start thinking about using these and helping define what government policy is, you've got to be acutely aware of whatever the system has been trained with.

And unfortunately, we don't know because the training data is not open.

And the second thing we have to be aware of is there are specific biases created by the training data.

A classic one is if you look at social benefit and financial benefit for investment, most of these systems are trained on market data and have a bias towards financial benefit rather than social benefit.

And that creates a problem if you're government because government, you need citizens to vote for you and you need a market to trade in.

And citizens are members of society and they also need a market to sell goods in.

And the market needs trade, which needs property law, which is based upon exclusion.

And citizens also want opportunity, which is based upon inclusion.

And inclusion and exclusion are both values of society.

So your role of government, amongst many things, is balancing this conflict between inclusion and exclusion within your system.

And if you start creating policy with something which is trained almost all on exclusion, you end up heading towards a much more excluded environment.

And that can be very destabilizing for a system.

So I'm not saying they're bad, you've just got to be consciously aware.

And so if I look at when I took groups of doctors and surgeons and we mapped our healthcare, if you look at it from a financial benefit, and this is where the AI is also aligned, the things you would invest in are preventive medicine, personalized medicine, and things like AI in healthcare.

But if you look at it from a societal benefit, the things you would invest in are health outcomes based upon patient reported outcome measures rather than clean ROs, sharing of medical data, and then you are into basic medicine diagnosis.

So the things which benefit society are not the things which the market values.

Some industries, they're more aligned.

Many industries, they're totally polar.

And that's the danger with these systems.

So they're good, but you've got to think very carefully about them.

We don't teach enough critical thinking, full stop, anywhere.

And I think that's actually a very good point, and also you made the point that for open training data for AIs in your keynotes, I think that's also very important.

We are running a little bit out of time.

Carol already had to leave for her next assignment.

So is there anything that we still need to cover?

I mean, obviously there is lots of stuff that we could talk about, but for this stream, is there any final remarks, anything that you feel we should have said, you should have said, Markus?

I just was reminded this morning from a quote from Eric Evans, the inventor of domain-driven design, who once said, not all of a large system will be well-designed.

And the trick is to find out which parts benefit from great design.

I think for software architects, it's getting more and more important to get this kind of business view on software systems, to see where can we apply just large baggage models, they run on their own, where do we have a human in the loop, and so on.

So it's very interesting, and I think what the mapping can help us here, at least to not be completely blind when we are trying to use our new AI companions for coding.

So that's what I wanted to say at the end.

Thanks a lot for jumping in and for this great conversation.

I enjoyed it a lot.

So we are, and I hope you did too.

So we will do another episode.

Oh, and thanks a lot for Martina for dealing with the technical side of things.

We couldn't have done it without her.

And thanks for AgileMeetsArchitecture for giving us the opportunity and supporting us so very much.

So tomorrow at 1400 hours CEST, so that's an hour later than usual, we will have the next stream.

It's also going to be from here, so it's going to be live about building product teams beyond organizational and geographical boundaries with Ananad and Leila Bulovic.

So I'm looking forward to that one.

Thanks a lot, and hope to see you again, and have a great day.

Thanks.