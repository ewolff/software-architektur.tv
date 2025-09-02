# Episode 252 - Intro to Beyond Estimates with Woody Zuill 

Dieser Podcast ist das Audio des Streams.

Weitere Folgen, Sketchnotes und vieles mehr findet ihr unter software-architektur.tv.

Welcome everybody to another episode of Software-Architektur im Stream.

This time around with Woody.

Welcome to the show, Woody.

Really glad to have you here.

Thank you.

And this show is, well, it's not really sponsored, but it's sort of a promotion for the Agile Meets Architecture Conference, where Woody and me will both talk.

And there is a rebate code.

It's AMA-SAIS-10 for 10% off.

So feel free to use that code to get 10% off the conference.

And I think it's a really interesting conference in Berlin on the 3rd and 4th of April, I think.

And yeah, we will both be there.

So we are really looking forward to that.

First of all, Woody, can you say a few words about yourself, what you're doing, what your professional background is?

Sure.

So I think of myself as a software developer or software programmer.

But mostly for the last number of years, I've been helping people learn about mob programming, which I'm now calling software teaming, by doing workshops and speaking at conferences, mostly on the topic of teamwork, but also on other topics, including what we're covering today.

Yeah, and we actually had an episode about remote mob or oxymor programming not too long ago.

So we figured that we will rather do an episode about beyond budgeting, behind estimates, and no estimates this time around, which, as you said, will also be the subject of your talk at Agile Meets Architecture Conference.

So I will start the screen share because you have prepared a nice presentation for us.

And the stage is all yours.

Very good, thank you.

I appreciate that.

So, you know, I've been doing software development for 45 years or so.

And when I first got into it, I worked at a place where they didn't do estimates.

My very first full time work, they weren't doing estimates.

And it was right in line with the way I'd worked in another field, which is advertising graphics and signage in the years before that.

There are times when doing an estimate makes sense, but there's time when doing estimates don't make sense.

And so this is some of the thinking that I've prepared about this concept of estimates.

And I usually start my workshops and other things I do asking this question.

So since we're not really doing this in an interactive way, anybody listening to this, you might think for a moment, you know, what is an estimate?

Can you distill that down to one word you would use to describe or to mean the same thing as an estimate?

If your boss comes to you and said, I need your estimate, then what word could they use in place of that?

I need your estimate for this software.

What word could you use in place of estimate?

So think about that for a moment and then I'll move forward.

So the first response is a guess by Kurt Patterson from YouTube.

Very good.

So we're right at the beginning of this and already we have somebody saying yes.

So I don't think there's any real need for me to go on with this presentation because that's sort of the fundamental purpose of this is we need to understand what do we really mean by an estimate?

So let's go on.

I'll share some ideas.

We'll come back to that later.

I always give a few disclaimers with this.

The first thing is, you know, I'm not here to tell you what to do.

I'm just sharing some of the things I think about.

It doesn't make them truths.

It doesn't make them right.

It's just the way that I think about stuff.

So this is important to me that I make it very clear right at the beginning.

I'm not trying to convince you of anything.

I just want to read out the slide for the people in the podcast.

So it says, the value of another's experience is to give us hope, not to tell us how or whether to proceed by Peter Block.

That's right.

And I think that's really the way I've used reading books and listening to podcasts of other people.

It's like I assume they had special circumstances that I may not have.

But I think the hope that I get is that they were able to figure things out.

So maybe I can figure things out.

So that's sort of what that's about.

Okay, so I'm not trying to convince you of anything.

That's not my purpose here today.

Try to keep an open mind.

I really like the idea that having an open mind is about having a curiosity.

When I first got into software development and I had to write my own software, I never used estimates because I was writing software that I myself would use.

So whatever I could write, I would use it and then I would add to it and keep using it.

So I never had to think much about estimates.

But when I got to making estimates for or working for other people doing estimates, creating software, they always were asking for estimates.

And it got me thinking, well, why are we doing this?

But questioning ourselves and questioning the processes we follow is always worthwhile in my opinion.

Now, we're only doing a quick introduction.

This is the second part.

We just saw the first part.

I have something like I could probably go on to 50 or 60 parts.

So we're going to cover the first few parts today.

So I'm going to tell you a little bit about how this started for me, the lessons I learned.

And I noticed a pattern and I have a big question.

So in software development, and I really mean in software development, because prior to that, I found this thinking useful in the world that I just mentioned, advertising graphics and things like that.

So I want to talk about two organizations.

I worked at a place in early 1999.

I was already not a young guy.

And I think I was about 45 years old.

And this was before the days of Agile.

They were doing extreme programming or something like extreme programming.

They weren't specifically following this extreme programming model, but it was very similar.

And they did not use estimates.

As a matter of fact, it was a wonderful place to work.

And they got a lot of work done.

Then my second contract, which was just a few months later, because that one was a very short term thing.

They were trying to get some rush work out.

I went to work at this other place.

And here's what I learned there.

First of all, there were 200 software developers.

They had hired all of them.

And most of them were in their early 20s.

They were quite young.

And this was in the days before Agile, but they were doing iterations.

You might have heard of IID, which is iterative incremental development.

I think that's what that stands for.

Barry Behm or somebody like that came up with that.

But they were going to do iterations.

And at the end of every two weeks, they were going to do, or excuse me, end of every six weeks, they were going to do what we would now call a retrospective.

So at the end of the very first retrospective, this is what we saw.

They noticed that their estimates were off.

They noticed that the requirements weren't clear when they started and they kept changing.

Now this is six weeks worth of work.

How are we going to fix this problem?

Well, we need to get better at estimating.

We need to get better at understanding the requirements and we need to control the changes.

Now I was already, I would consider a rather mature business person.

I'd seen these problems in other kinds of work and I could see these things were closely related, but I kept my mouth shut because actually there was a lot of impostor syndrome for me at that time.

I was just changing my career into software development and I was worried that if I started saying too much, they're going to find out I don't know anything.

So I figured, well, let me see what I can learn.

So we set off at learning these things.

They gave us a few days of training, how to get better at these things.

And then it was time for the second iteration.

Well, during the retrospective for the second iteration, and now we're 12 weeks into the project, what problems do you think they had?

Well, these were the primary problems, the same ones.

How are we going to fix it?

Well, it was the same things.

Well, I could see this as a pattern.

Patterns show up all over the place and I'm always looking for them.

But in 1999, the whole software development industry was really paying attention to the patterns of software development that we were seeing.

So, yep, time to go off to the next requirement.

I mean, the next iteration and off we go.

We do the work at the end of the third iteration.

We had our lessons learned 18 weeks into it.

And of course, I don't even have to tell you.

Same problems, same way to solve it.

So I actually stood up in the meeting.

It was a meeting where we did a lot of the workshopping kind of things.

And I said, you know, don't you see there's a pattern here?

And they didn't.

But this is what I did.

I said, we do something and we do it over and over and we're expecting things to get better and they're not getting better.

That's a pattern.

What are we going to call this pattern?

Well, I called it the cycle of continuous, no improvements.

Now, in those days, everyone was looking at getting a cycle of continuous improvement.

So I thought this was a bit of a funny way to say it.

And yeah, and it actually kind of backfired on me to bring this up.

But they didn't fire me.

I kept working there.

But I could tell this was not making the managers happy.

That's all right.

I saw a problem and here's the problem.

I've seen this over and over again.

That was 25 plus years ago.

I've seen it over and over at many, many companies.

At first, I thought it was unique.

But then it's a pattern I've seen literally every nine out of ten companies I've been at.

And I've been at a number of contracts where I visited companies.

They do something like this.

So let's talk about this just a little bit.

I want to talk about I used to call this no estimates.

I want to talk about what it is not and what it is or what it means to me.

Pretty straightforward.

So a few things that no estimates is not.

It doesn't mean it's a commandment like you shall not do estimates.

It's not a commandment.

I'm not telling people not to do estimates.

It's not a protest.

It's not me saying I refuse to do estimates.

And I would say be very cautious about this.

This isn't for the people doing the estimates.

This is for the people using estimates.

So this is really important to me.

Because if you're working at a company and they ask you to do estimates, don't tell them you're not going to do them anymore.

Because some guy you saw on the internet said that estimates are no good.

This is for those using the estimates that we might make.

As a software developer, I've often made estimates.

So I'm just warning you.

If somebody says you've got to do them, then do them.

Don't lose your job because of something I said.

I do know of several people who have lost their jobs for this reason.

So please be cautious.

So if the system you're working in requires that somebody use estimates, that means somebody has to do the estimates.

I don't believe they're useful.

I don't believe they're meaningful.

But I just want to make that point.

If that's the place you're working, then you got to live the life you're living.

I like this picture.

Those of you can see it.

It's a woman who's looking at the cat food box and her cat is eating cat food, but it's actually a tiger.

And I think she's trying to figure out did the cat food have too much protein or whatever and it turned her cat into a tiger.

But that's what we have.

We've let the tiger out of the box, as they say.

Initially, I used the term no estimates in a blog post where I was describing a software development effort where we had not used estimates.

I want to make that really clear.

We had not used estimates.

We had no estimates.

It's not a technique.

It's the opposite of a technique.

It's not doing something that we otherwise are doing.

There's nothing to do in the place of it, by the way.

I just want to make it clear.

I used this in 2012.

As far as I could tell, I was the first person in Twitter, you remember Twitter, using this hashtag.

I did a search.

I found only one person who used it earlier in all my searches.

They were talking about a related thing, but not related to this conversation.

To make the point, it's just a reference to a blog post where we had not used estimates.

It turned into a very controversial terminology.

No estimates.

People took it to mean we are refusing to do estimates.

But I use it as a placeholder for the conversation I want to have about the problems we have in our industry surrounding estimates.

I've already said it several times, but I'm going to say it again.

I don't think estimates themselves are useful, but I also think they are harmful.

It's not just wasteful to do something that isn't useful, but it's really a problem if we're doing something that's harmful.

I won't be able to get too much into that during today's short presentation, but that's what my conference talk is going to be about.

I think I'm doing a mini-workshop or something.

The big question that we need to ask ourselves is, if using estimates is harmful, what would we do?

You can do this as an Einstein-style mind experiment, a thought experiment.

Maybe you believe estimates are useful, but look at it from the opposite point of view and ask yourself, if estimates are harmful, what would we do?

Pretend they are harmful.

What would we do?

Now, we don't have time to do that as an exercise here, but after this talk, it might be useful to do that as a kind of an exercise.

We need to have a definition of what we mean by estimates.

Remember earlier I asked you, what is an estimate?

Give me one word.

I've done this exercise probably 100 times.

I used to collect the data for this.

I've stopped doing that now, but I can show it this way as one of these word clouds.

This is typically what I get.

If I have 50 people, usually about 50% of them, I have to have more than 10 or 15.

It's a kind of law of big numbers.

You have to get up into enough people to see the averages play out.

I'm going to show you this here.

This is typical right here.

About 50% said guess or something like a guess.

Here's guess, but another one here says a best guess.

Another says a prediction or an assumption or an outlook or a forecast.

Each of those were different, but in the conversation of the workshop, people said, yes, we can use those as guests.

You can see it's a guess about the time or the effort or the size or the work we're going to do so that we can make a plan or have a budget so we can do our work.

I'm going to use my pointer.

I don't know if you can see that, but here's a guess about the time, the effort, the complexity or whatever of something so we can make a plan or a budget.

Now, these things down in the corner, those are sort of the dysfunctions.

It's a deadline.

It's an expectation.

It's a promise.

It's a pledge.

It's a commitment.

No boss would ever come to you and say, could you give me your effort by the end of the day?

They wouldn't know what you're talking about.

If we used the word effort in place of the word estimate, it really doesn't replace the word estimate.

The estimate is about the effort.

I think if the boss were using the word guess, we would know, hey, I need your guess about the work we're doing by the end of the day.

That's probably the way we would use it.

OK, so I'm going to do an estimate.

Think of this for yourself.

I got this from Davo Pancho.

I really like this little exercise.

Three months from today, you have to write your name on a white index card with a blue fountain pen.

An index card is like a recipe card where you can write down a recipe.

OK, when I usually do this, somebody will say, well, that's going to take me a few seconds or a minute.

How long is it going to take you to do on that day?

Well, when I ask that question and they come up with this amount of time, it makes a lot of sense.

But if I change it slightly, right now, this very moment, you have to write your name on a white index card with a blue fountain pen.

Very rarely does anybody have a blue fountain pen.

Nowadays, we carry ballpoint pens or markers.

We don't use fountain pens like we used to.

So you'd have to go find a fountain pen.

And also, you might not have an index card and you might not know enough about the index card.

This is the difference of the kind of questioning we need to do when we're actually making an estimate.

One is, do I have all the things I need in place and what would it take me to do if I had everything in place?

But usually a big part of what we do in our work is putting everything into place.

So we're going to use this to help us make a definition.

Work time is the amount of time actually doing the work.

So if I needed to get a fountain pen, maybe I could send an email telling the, you know, our supply department to get me a fountain pen.

And then I just write the email.

And then when that fountain pen comes, I can do the work.

But that's not really the work is getting the fountain pen.

Now, when we're doing elapsed recycle time, that includes the amount of time that we're going to, that will pass between when I first started on the work and when it got done.

So that's what's more important.

Like if you go to get your car repaired and you go and you say, hey, I've got to get the brakes fixed.

How long will it take?

And they say, oh, about two hours.

And they say, oh, well, if I come back in two hours, I can get my car.

Well, no, we have to order your brake parts.

So I have to take your car, put it on the rack, take the wheels off, look at the brakes, see what parts we need, order the parts, then the parts delivery people will bring the parts to us, then we'll put them on your car.

You can come get it at the end of the day.

We're more interested in when will it be done, not how much work time will it take.

But often we're estimating the work time when really what's interesting is the cycle time.

So we have to be careful.

Lead time, there's different definitions, but that's the amount of time when the request is first made until it's delivered.

So there's three kinds of times we need to think about.

We won't go into any more detail on that.

I want to cover one other thing.

I only talk about a very specific use of estimates for a very specific purpose.

Otherwise, it gets too complicated.

And that purpose is estimating the amount of time or cost for doing software development.

Whenever we do anything more than that, it gets to be rather complicated.

So our working definition or the one that I like to use is an estimate is a guess of the amount of time, cost, effort, whatever, to create some software, to do a project, a product, a feature, a task or for whatever.

So this is the basic idea that I use.

This is about creating software.

So let's just look at a few of the things related to it.

When we ask for estimates, it's good to understand why do we use them?

What are we going to do with them?

And in software development, it's usually used to attempt to predict the future.

That means we want to know something about how long something will take.

When will it be done?

How much will it cost?

How much can we get entering this specific amount of time?

How big is this thing?

And so on.

These are the kinds of things we want to know.

We have to ask ourselves, are these facts?

When someone says that will take two weeks, is that a fact or is it not?

If it was facts, we could just act on it.

These are not facts, but it is information.

The problem is, it's not very good information.

Matter of fact, I would say it's harmful information.

It misinforms us rather than informs us.

So what do we do with this information?

That's a very important thing to me, but we use it to help us make decisions.

This is another problem.

People often tell me this.

And then they also say, or to spark a conversation.

Well, if you're doing estimates to spark a conversation, I would say, why don't you just have the conversation and stop worrying about the estimates?

When you do something for its side effect, you really need to look into that and decide, is that the right thing to be doing?

Do something else.

If you're doing something only because of the side effects, you can probably find a better way to do it.

But why do we want to spark the conversation?

Usually because we have a decision to make about how much will we get done.

Things like this.

Should we do project A or project B?

Should we do this project at all?

Which project should we choose to do in the next fiscal year?

You can see that's highly problematic right there.

We're going to choose based on estimates, based on our guesses, what work we should do next year.

For one thing, that's a very lagging thing.

It's going to take a long time before we find out whether we made a good decision or not.

If we decided to do one thing over the other, all we're going to know is whether the one thing we chose turns out to be worth doing or not.

We didn't learn much from it.

How many people should we hire?

I've worked on projects where we estimated how long it would take so we could figure out how many people we should hire.

We're estimating how long it will take people that we haven't even met yet to do some work.

That's very problematic.

I don't think that makes any sense.

We want to make decisions about prioritizing.

What should we do first?

Scheduling things, planning things.

What do we want to bring into this sprint?

That's something you often hear about.

How much can we do in the next two weeks?

Again, we're basing all of this important stuff on very easily done guesses.

We're depending on these guesses.

What's wrong with that?

This is the point.

We're making these decisions based on guesses.

Should we do this?

What a lot of people will tell me is, it's the best we can do.

I don't think it's the best we can do.

Listen to this.

When they say this, estimates help us make decisions, I agree.

It helps you make a decision, but flipping a coin would help you make a decision.

Throwing a dart at the dartboard could help you make a decision.

We don't need help making decisions.

We need help making good decisions.

This is a very different thing.

Can we prove that our estimates helped us make a good decision?

I doubt that this is true, that we have a way to prove this.

What we often do when we're trying to prove it, we will have some mechanism in place.

Probably the worst mechanism we can have is, was this on time and on budget?

You could probably think for yourself, what would be a better way to measure the success of something?

It's not getting it done on time and on budget.

That doesn't make a lot of sense for software.

If we got it done on time and on budget and we released it to the world and nobody bought it or nobody liked it, or worse, everybody says this is the worst software I've ever used, what good is it that we got that done on time and on budget?

I think that's another problem.

Some of you will have seen this.

We only have a few minutes of this part left, then we'll have a conversation.

Back in 1994, and I saw this about the time it came out, these folks, the Standish Group, did this thing they called the chaos report.

They polled a lot of companies that were doing projects, many, they have a lot of data, and they came up with these kinds of figures.

Failed projects means they didn't even get delivered or they failed greatly in some form.

Challenged means they didn't get what they want done, it wasn't done the way they wanted it to, it was too expensive, and so on, and a success.

The percentages were something like this.

How long ago is that now?

30 years?

A long time ago, whatever.

I'm not a mathematician.

You guys can calculate how many years ago 1994 was, but you get the picture here.

They've done this again every few years.

The last one they did, I think, was in 2020, and it might be the last one they'll ever do.

The numbers did not change very much.

Failures was about the same, challenged a little bit less, success a little bit more.

Was hat sich verändert?

Zunächst einmal, das ist nicht genug Veränderung für mich, um viel Interesse darauf zu nehmen.

Aber sie haben einen ganzen Bericht über das gemacht.

Sie sagten, dass wir unsere Prozesse ziemlich viel verändert haben.

Wir versuchen, Dinge in kürzeren Iterationen zu machen.

Aber das ist nicht der Weg, den Erfolg eines Projekts zu messen.

Das erzählt uns nur den Erfolg unserer Fähigkeit, zu beurteilen.

Und ich glaube nicht, dass diese Beurteilungen uns informieren.

Ich werde nur noch ein bisschen mehr machen und dann geht es weiter.

Ich denke, wir wollen so sehr die Zukunft beurteilen, dass wir glauben, dass wir es schaffen können.

Und ich denke, wir verarschen uns.

Das ist eine Art Konfirmations-Bias, aber ich denke, es heißt Wünsch-Bias.

Wir wünschen uns etwas so sehr, dass wir finden, wie wir glauben, dass wir es schaffen können.

Und ich denke, das ist problematisch.

Und ich denke, wir versuchen, die falschen Dinge zu entscheiden.

Die meiste Zeit versuchen wir, zu entscheiden, wie lange es dauert, um ein bestimmtes Set von Arbeit zu erledigen.

Aber meiner Meinung nach ist dieses Set von Arbeit die falschen Dinge, die wir arbeiten müssen.

Es wird etwas anderes geben, das wir entdecken werden.

Weil wir versuchen, diese Arbeit zu machen, das wird uns wichtiger werden.

Also haben wir die falschen Dinge in der ersten Plenarsitzung beurteilt.

Ich denke, wir haben genug veröffentlicht.

Der nächste Teil geht um den Bereich Softwareentwicklung.

Und ich werde das mit einem Satz beenden.

Als ich das erste Mal mit dieser Sache begonnen habe, haben die Leute gesagt, Hey, aber wenn ich meine Küche remodellieren muss, will ich wissen, wie viel es kostet für diese Qualität von Applikationen und Arbeit.

Und wie lange es dauert.

Das ist mir wichtig.

Und das ist perfekt in Ordnung.

In manchen Bereichen brauchst du keine Zahlen.

In manchen Bereichen sind Zahlen nützlich.

Und in manchen Bereichen sind sie schädlich.

Du gehst nicht in den Grocery-Store und fragst den Klärer, wie viel ein Teig mit Brot kostet.

Sie werden nur auf die Tafeln zeigen, wo das Brot ist, und sagen, das Brot ist da, die Preise sind auf der Tafel.

Du kannst schauen, wie viel ein Teig mit Brot kostet.

Sie brauchen keine Zahlen.

Aber wir sind in einem Welt, wie manche Dinge, die ich früher machte, z.B.

Screenprinting, Signage, Schilder auf Gebäuden, oder ein Verkaufsprogramm.

Wir könnten Zahlen geben.

Aber in manchen Bereichen können wir keine Zahlen geben.

Sie sind sinnlos.

Und ich denke, der Domain, in dem das Software steht, wenn du an Kenevan-Domäne denkst, ist er in dem Domain, den wir komplex nennen.

Es ist der Raum der Entdeckung.

Und ich denke, das ist ein guter Ort, um zu beenden.

Ich habe dich gezwungen, zu denken, sind Zahlen für dich nützlich?

Ich werde dir ein bisschen darüber nachdenken, warum wir sie machen.

Und meine Meinungen darüber, nur ein bisschen.

Normalerweise, wenn ich am Ende ein ganzes Gespräch darüber mache, werde ich dir erzählen, wie ich gearbeitet habe.

Und das ist wirklich einfach, ohne Zahlen.

Lass uns gut damit umgehen, Dinge in kleinen Teilen zu vermitteln, sodass wir sie steuern und lernen können, anstatt alles nach vorne herauszufinden.

Ich denke, ich habe genug veröffentlicht.

Klingt das gut?

Vielen Dank.

Es gibt einen Kommentar oder eine Frage in der Chat, von MD42Martin auf Twitch.

Er sagt, dass Zahlen manchmal auch für Priorisierung genutzt werden, was auch problematisch ist.

Sollte es keine Geschäftswerte sein?

Würdest du dagegen?

Sollte es eher eine Geschäftswerte sein, auf die wir unsere Priorisierung basieren?

Ich denke, er hat einen sehr wichtigen Punkt eingebracht.

Und das ist, dass der Kosten von etwas irrelevant ist.

Was wichtig ist, ist der Wert.

Viele Leute sagen, sie wollen einen Wert für den Kosten entscheiden.

Ich würde diesen Warnsignal machen.

Bei Softwareentwicklung, wenn man nicht mehr als der Kosten von Softwareentwicklung produziert, sollte man nicht in Softwareentwicklung sein.

Wenn man schlechte Entscheidungen macht, was wir entwickeln werden, wird man es nicht gut machen.

Aber es gibt noch einen Hinweis.

Wertenteilung ist fast unmöglich.

Wertenteilung von Kosten ist etwas näher an etwas, was möglich ist.

Wertenteilung ist wirklich schwierig.

Um zu wissen, was etwas wirklich bringt, ist wirklich schwierig.

Deshalb liebe ich die kleinen Iterationen.

Wenn wir etwas machen können, wenn wir in die Hände der Nutzer kommen, wenn wir sehen, was sie benutzen, wenn wir zu dem Nächsten steuern.

Ich denke, das gibt uns viel mehr Wert, als wenn wir nur vor Ort entscheiden, dass wir diese große Sache machen, und später herausfinden, wie bei den Standish-Reporten, bei den Chaos-Reporten, dass die meisten Projekte verfehlt oder gezwungen wurden.

Ich hoffe, ich habe das beantwortet.

Hat das Sinn?

Ja, ich finde es interessant, dass du sagst, dass Wertenteilung von Geschäftsleistungen noch schwieriger ist, als Wertenteilung von Arbeit.

Ja.

Was du gesagt hast, ist, dass wenn man kurze Iterationen macht, dann wird es offensichtlich, was wertvoll ist, indem man es einfach herausstellt und sieht, ob es erfolgt oder nicht.

Ja, ich weiß nicht, ob offensichtlich das richtige Wort für mich ist, aber es gibt uns Informationen.

Zumindest ist es möglich, wirkliche Daten zu bekommen, oder wirkliche Informationen.

Die Bestimmungen sind nicht wirkliche Informationen.

Sie informieren uns nicht einmal.

Aber wenn ich etwas an den Kunden verliere, kann ich ein sehr spezifisches Beispiel dazu geben.

Ich hatte einen Kunden, nicht einen Kunden, aber jemanden, mit dem ich an einigen Dingen gearbeitet habe.

Sie hatten sehr gute Zahlen, wenn sie eine neue Version ihrer Application eröffnen, und ein Online-Kunde kann es downloaden, es auf der Maschine probieren.

Wenn sie das tun, bekommen sie einen gewissen Anteil und verwenden es.

Wir machen also etwas Neues, wir veröffentlichen es, die Leute downloaden es, sie probieren es auf der Maschine, und ein gewisses Anteil wird verwendet.

Das sind Anteile, die in ihrem Unternehmen festgestellt wurden.

Und einer Tage haben sie das Software geliefert, und sie konnten die Anteile anschauen, weil sie Rekorde davon haben.

Nicht nur die Leute, die es downloaden, sondern auch die Leute, die es installieren, weil sie die Notifikationen bekommen, und die Leute, die es probieren.

Als es zu dem Anteil kam, die Leute es probieren, sinken die Anteile signifikant, verglichen mit dem, was sie normalerweise sehen.

Das sagt uns etwas, und es ist so, dass die Installationsprozesse ein paar Fehler darin hatten.

Auf den meisten Maschinen würde es nicht richtig vollkommen.

Das ist also sehr echte Informationen, die wir bekommen können, die wir nicht vor der Zeit beurteilen können.

Also etwas in den Händen eines Nutzers zu bekommen, und das war ein sehr echter Beispiel, erzählt uns etwas echte Daten, und wir können auf echte Daten arbeiten.

Jetzt nochmal, es ist nicht perfekte Daten, aber es ist echt.

Es ist also so, es ist vielleicht so nah an perfekt, wie wir es in unserem Weltraum bekommen können.

Wenn du keine Analyse hast, und du, du weißt, ich habe es früher in Anleitungen gelegt, wenn jemand auf dieses hier klickt, in der Anleitung, und sie es benutzt, wie viele Male benutzt sie es?

Wenn sie es zweimal benutzt und nie wieder benutzt haben, naja, sie schauten es an, und sie mochten es nicht, oder es funktionierte nicht sehr gut für sie.

Ich will diese Art von Informationen.

Wenn sie eine neue Feature mochten, sie nutzten es mehr die nächste Woche, sie nutzten es noch mehr die nächste Woche, und es wurde ein Standard, das sie die ganze Zeit benutzt haben, das ist, und ich kann das Wert sehen.

Führt es sie dazu, mehr Geschäft zu bringen?

Natürlich, das wäre das, was wir wollen, aber du kannst sehen, es gibt Wege, um wirkliche Informationen zu bekommen, und es ist schwer, das zu bekommen, wenn wir an der Werte abwarten.

Ich hoffe, ich habe die Frage beantwortet.

Ja, ich mag die Antwort sehr.

Und es gibt noch ein Kommentar von Byteborg auf YouTube.

Er sagt, es ist der Raum der Entdeckung.

Das ist eine Ausdruck, die du benutzt hast.

Ja.

Ich liebe jede einzelne Worte davon.

Dann haben wir Kurt Petersen, und er sagt, wir lernen, und machen Entscheidungen, über das, was bekannt ist, wozu Dinge von Ken Schwarber in den frühen Tagen von Scrum kamen.

Er ist einer der Ursprüngler, oder ich glaube, er ist der Inventor von Scrum.

Ja.

Warum schaffen wir, dass die Leute die No-Estimates verweigern?

Weißt du, ich weiß es nicht.

Als ich zuerst No-Estimates benutzt habe, bevor ich Softwareentwicklung machte, und in meinem Business habe ich Kunden, die zu mir kamen, und, sagen wir, sie brauchen 100 dieser Art eines Zeichens mit diesen Farben, dieser Größe von Blättern.

Ich könnte das beurteilen, kein Problem.

Aber es gab Dinge, die ich nicht beurteilen konnte.

Ein Beispiel wäre, wenn sie zu mir kamen und gesagt haben, ich will ein neues Logo, und ich will, dass dieses Logo so aussieht, als ob ich seit 30 oder 40 Jahren in einem Geschäft war, sodass es wirklich ausreichend aussieht.

Nun, ich weiß nicht, was sie wollen.

Wir müssen einige Iterationen durchführen, um herauszufinden, was für Sie funktionieren wird.

Ich konnte also nicht wirklich ein No-Estimate dafür geben.

Was ich normalerweise sage, ist, ich kann Ihnen einige preliminäre Skizzen machen, und das kostet Ihnen so viel.

Dann können wir darüber sprechen, und Sie wählen die, die Sie mögen.

Dann können wir einige letzte Kompositionen machen, und ich kann Ihnen sagen, wie viele Iterationen es dauert.

Wie viel kostet es?

Das wissen wir nicht voraus.

Also beginne ich, ohne No-Estimate in diesen Fällen zu arbeiten, und ich kann Ihnen sagen, wenn Sie ein einfaches No-Estimate wählen, ein einfaches Logo, nach unseren ersten primären Skizzen oder preliminären Skizzen, dann kostet es wahrscheinlich x Dollar.

Aber ich weiß nicht, wie viele Malzeiten es dauert.

Also, wenn Sie mit mir ein paar Stunden sitzen, wir machen die Grundlagen, und das kostet Ihnen so viel Geld.

Aber am Ende weiß ich es nicht.

Und ich hatte viele Kunden, die so gearbeitet haben.

Es gab drei Kunden, ich will hier einen klaren Punkt machen, drei Kunden, die mir wirklich gezeigt haben, wie wichtig das war.

Und das waren die Kunden, die in Notfällen waren.

Sie mussten vieles sehr schnell machen, und wenn wir die Zeit für die Estimaten verbracht hätten, hätten wir nicht genug Zeit für ihr Arbeiten, weil sie wirklich echte Zeitlinien hatten.

Zwei von ihnen waren für Sport-Evente.

In der Software gibt es Zeitlinien, aber sie sind immer ein bisschen weich.

Bei einem Sport-Event, wie zum Beispiel ein internationales Sport-Event, das telekommuniziert wird, passiert das am Tag, wenn es keinen Schneesturm gibt oder so.

Man kann also nicht eine Minute zu spät sein.

Sie waren also wirklich unter der Pistole, und sie mussten das Arbeiten fertig machen.

Und ich sagte ihnen, ihr könnt einfach unsere Zeit kaufen.

Ihr könnt einfach unsere Zeit kaufen, und nach drei Kunden, die das gemacht haben, drei relativ große Kunden, habe ich bemerkt, dass das die Leute sind, die mehr Interesse an Wert haben, als an Kosten.

Dass sie das gemacht haben, ist für sie wichtiger, als dass sie wissen, dass die Kosten nicht zu groß sein werden.

Es ist das gleiche in dieser Welt wie in der Software.

Wenn wir nicht viel Geld für unser Arbeiten verdienen können, sollten wir in diesem Business nicht sein.

Die Grenzen sind in manchen Businessen wirklich fest.

Wenn Sie ein kleines Fastfood-Restaurant besuchen, dann wissen Sie genau, dass jeder Penny zählt.

Aber wenn wir große Sport-Evente machen, dann würde die Menge, die sie mir bezahlen, nur ein kleines Teil ihres Budgets sein.

Das gleiche ist mit der Software.

Wenn wir uns über das Budget mit der Software kümmern, müssen wir darüber nachdenken, was wir falsch machen.

Die ursprüngliche Frage war, warum wir aufhören oder vermeiden zu investieren.

Ich habe eine Antwort gegeben, die ist, dass manchmal die Zeitlinien oder die Werte der Software nicht wirklich wichtig sind für den gesamten Prozess.

Das ist ein guter Punkt.

Was Sie gesagt haben, ist, wenn ich eine Zeitlinie habe und es wirklich eine harte Zeitlinie ist, habe ich keine Wahl.

Ich muss so schnell wie möglich gehen.

Das ist eine Fähigkeit.

Es geht schnell um kleine Schritte, damit wir so weit wie möglich auf so viele Dinge wie möglich gehen können.

Aber es gibt noch einen Punkt.

Das Problem mit Werten ist oft die Zeitlinie, die wir haben.

Wenn wir Entscheidungen machen, für welche Projekte wir eine sehr schlechte Entscheidung machen werden, müssen wir verschiedene Entscheidungen machen.

Aber ich glaube, es hat viel mit diesen Domänen zu tun, wie sie in dem Stacy-Modell oder Kenevan gesprochen haben.

Wenn wir in der komplexen Welt sind, helfen die Wertschätzungen nicht so viel.

Wenn wir in der komplizierten Welt, in der wir eigentlich sind, helfen sie nicht so viel.

Fakt ist, dass sie in der komplexen Welt nicht so viel helfen.

Und das ist das Problem mit Wertschätzung.

Dass die Wertschätzung nicht so gut funktioniert.

Und dass das nicht so gut funktioniert.

Und dass das Problem mit Wertschätzung nicht so gut funktioniert.

Und darum haben wir diese Worte hier gesprochen, um einfach die Kommunikation mit Wertschätzung zu ändern.

Und einmal möchte ich dich persönlich fragen, weil ich denke, dass eine der möglichen Erklärungen wäre, dass die Leute sicherer und sicherer sind, wenn sie diese Wertschätzung machen.

Und sie planen und es fühlt sich bequemer an.

Und es fühlt sich bequemer an.

Und ich denke, dass es eine psychologische Erklärung gibt.

Würdest du das verstehen?

Ja.

Ich denke, dass das Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass das Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl ist, dass wir in Kontrolle sind.

Und ich denke, dass es ein Gefühl Es wird immer noch eine Variabilität im System geben.

Egal, wo wir hinlegen, werden wir nicht das, was wir wollen, bekommen.

Wir müssen also vorsichtig sein, diese Metriken zu folgen.

Aber es wird immer noch mehr nutzbare Informationen kommen.

In meiner Meinung.

Eine wichtige Sache.

Ich denke, das ist ein sehr guter Punkt.

Wie du gesagt hast, sind Estimaten nur Gäste.

Sie sind keine echten Daten.

Es macht also wahrscheinlich Sinn, mehr in echte Daten und harte Daten zu investieren.

Ralf sagt, wir prädigen die Zukunft, indem wir sie formieren.

Das ist das, was Alan Kay gesagt hat.

Okay, ich gehe mit dem nach.

Wir sind in der Pflicht für etwas.

Und es hat zumindest einen Effekt auf das, was wir als Nächstes tun.

Für alles Gute.

Beitbarg sagt, man kann ein System so sanft und erfolgreich wie möglich erstellen.

Ab einem Punkt in der Zeit wird der ökonomische Himmel aufstehen, der Effizienz bedroht.

Ja.

Aber Effizienz ist problematisch.

Wir wollen Effizienz.

Effizienz ist sinnvoll in standardisierten Arbeiten.

Z.B.

Hier habe ich ein Earpod-Ding.

Wer diese Plastiknoten bis zu einem Millionstel formiert, wie viel das kostet und wie lange es dauert und all das.

In standardisierten Arbeiten kann Effizienz einen Sinn haben.

Es hat keinen Sinn in unserem Weltraum der Entdeckung, in unserem Weltraum der Innovation.

Und wenn das, was wir tun, nicht innovativ ist, wenn es kein Entdeckungsarbeit ist, dann ist es nicht risikosam genug, etwas wert zu sein.

Es gibt also viele Probleme, die wir beantworten müssen.

Ich habe keinen Weg, das zu stoppen.

Das ist in jeder Organisation so.

Effizienz und Produktivität sehen wichtiger aus, als die sinnvolleren Dinge der Innovation und der Entdeckung, was wir wirklich tun sollten.

Das ist sehr anders als alles, was wir jetzt kennen.

Wir werden die Zukunft entdecken, wenn wir dort sind.

Wir können die Entscheidung jetzt nicht treffen, was das wird.

Ich denke, dass fast alles, was wir hier diskutieren, eine Diskussion um die Wirtschaft ist, weil wir über Werte, Wertschätzungen und Kosten sprechen.

Es geht also nicht um den Wirtschafts-Typ.

Du könntest dich als Wirtschafts-Typ mit der Diskussion, die wir hier haben, bezeichnen.

Es ist eher so, dass jemand nicht wirklich versteht, worum es hier alles geht, und dann kommt er mit seltsamen Sachen.

Wenn du also einen richtigen Wirtschafts-Typ hast, würde ich sagen, es sollte mit dem, was du sagst, resonieren.

Es gibt ein Problem mit dem, wie Firmen entwickeln.

Wo wir anfangen, in den meisten Firmen, wenn sie klein sind, hat es viel mehr mit dem Verständnis von diesen Dingen.

Sie versuchen nur, Dinge zu bewegen.

Aber später wird es viel mehr bürokratisch, und dann starten die Probleme.

Ich arbeitete an einem Ort, wo ich sagte, so groß wie wir es jetzt haben, müssen wir Dinge in einer formelleren Art und Weise machen.

Ziemlich bald schreibst du Rechte für alles, und alles, was du tust, macht es immer schwerer und schwerer, sinnvolle Dinge in einer schnellen Art und Weise zu erzielen.

Ich habe das ein paar Mal gesehen.

Ich sage nicht, dass ich ein Experte bin.

Es ist eine Beobachtung, die ich gemacht habe.

Bitte, alle, erinnert euch, wo wir angefangen haben.

Ich sage euch keine Wahrheiten.

Ich sage euch nur die Dinge, die ich darüber denke.

Wenn ihr sie interessant findet, dann ist es wahrscheinlich eine Konversation, die ich mit euch haben möchte.

Das ist das Interessante an mir.

Ich fand es toll, dass du das am Anfang gesagt hast.

Es ist die richtige Auffassung zu diesen Dingen.

Es gibt viele Dinge im Chat, und ich weiß nicht, ob wir das alles durchführen können.

Wenn du ein paar davon machst, kann ich versuchen, sie sehr kurz zu machen, und dann sind wir fertig.

Ich habe etwas über Priorisierung gelernt.

Ich dachte, hier ist ein gutes Beispiel.

Das ist von Jojo Broker.

Er fragt, wie Woody mit Arbeitsplätzen umgeht, die auf Einstimmigkeitsstellungen stimmten.

Spielte er einfach mit, oder versuchte er, sein Arbeitsumfeld zu beeinflussen?

Anfangs würde ich die Einstimmigkeitsstellungen mit einem Disclaimer machen.

Ich würde einfach sagen, ja, ich werde diese Einstimmigkeitsstellungen machen, aber hier ist nicht genug Informationen, um mir eine nützliche Einstimmigkeitsstellung leisten zu können.

Als die Welt zum Thema kam, war es so, dass sie die Poker-Einstimmigkeitsstellungen mit den Karten benutzt haben.

Ich dachte, das macht keinen Sinn für mich.

Aber etwa 2006 oder 2007 habe ich an dem Ort angefangen, an dem ich arbeitete, und habe gesagt, ich werde keine Einstimmigkeitsstellungen mehr machen.

Ich werde einfach nur mein Arbeit machen, und ihr könnt mich anrufen, wenn ihr wollt.

Dann, 2009, weil es einen großen ökonomischen Unterschied gab, und ich von diesem Job abgelassen wurde, dachte ich, von jetzt an werde ich nur an Orten arbeiten, die sagen, nein, ihr müsst keine Einstimmigkeitsstellungen mehr machen.

Ich habe es also vorher klargemacht, wenn jemand mich anrufen wollte, und seit 2009, bin ich mir sicher, habe ich keine Einstimmigkeitsstellungen in Softwareentwicklung gemacht.

Ich arbeite weiterhin direkt in Softwareentwicklung bis 2015, und ich habe es nur seitdem sporadisch gemacht, weil ich meistens Training mache.

Aber zurück in mein eigenes Arbeiten, als ich meine Nachtjahre arbeite, nehme ich Arbeit, die mich interessiert.

Das war der Grund, warum ich mit dem Experiment begonnen habe.

Ich würde nie Einstimmigkeitsstellungen in diesem Arbeiten machen.

Ich habe also viele Kunden gefunden, bis zum Ende 2003 und vielleicht schon vorher, wo ich keine Einstimmigkeitsstellungen gemacht habe.

Ich habe es hart gearbeitet, keine Einstimmigkeitsstellungen zu machen.

Also, die Strategie, die du benutzt, ist, dass du sagst, okay, ich mache keine Einstimmigkeitsstellungen, und wenn du mich willst, werde ich den Job nicht nehmen.

Ja, genau.

Das ist eine Strategie, die nicht genügend ist, um richtige Begriffe zu haben, die sagen, das ist, wie ich das machen werde, und wenn du diese Begriffe nicht angehst, werde ich das nicht machen, weil ich nicht denke, dass wir einen gemeinsamen Grund haben, um etwas zusammen zu machen, weil es einfach so anders ist.

Ja.

Es gibt vielleicht keine Einstimmigkeitsstellungen für dich, es gibt vielleicht andere Dinge für andere Menschen.

Es gibt einen Weg, um das zu erreichen, und was ich gefunden habe, ist, wenn ich mich bereit mache, eine Arbeit anzunehmen, die verfehlt ist, die bereits verfehlt ist, dann sind die Leute nicht so interessiert in Einstimmigkeitsstellungen, sie sind nur interessiert, es zu stoppen, es zu verfehlen.

Also, wenn es eine Arbeit ist, die sie nicht erledigen können, weil es alles zerbrochen ist oder so, dann sind sie bereit, je schlimmer die Dinge sind, desto mehr sind sie bereit, ein paar Alternativen zu versuchen.

Aber ich habe keine einfache Antwort dafür.

Du findest deinen eigenen Weg.

Wenn du einen perfekten Weg findest, um das zu machen, würde ich es gerne hören.

Ja.

So, sollen wir die restlichen Kommentare wirklich kurz durchführen?

Wenn du die Zeit hast, ich habe genug Zeit, ich sitze in einem Hotelraum.

Also, es gibt nicht viel für mich zu tun.

Wir können definitiv einige Okay.

Und ich werde versuchen, kurz Antworten zu geben.

Also, Kurt Peterson hat gesagt, wenn du allgemein Einstimmigkeitsstellungen verlässt, empfiehlt dir das, dass du Zeitverlängerung oder ist Zeitverlängerung manchmal auch nicht so wichtig?

Ja, also Zeitverlängerung ist eine dieser Dinge, über die die Leute sprechen, aber ich denke, es ist auch ein bisschen unbedingt wichtig, weil wir kein Standardwerk machen.

Das ist kein Standardwerk.

Wenn es ein Standardwerk wäre, hätte Zeitverlängerung einen Sinn.

Wie lange dauert es, eine Geschichte durch unser System zu gehen?

Für mich macht es keinen Sinn.

Was wichtig ist, sind Dinge wie Queueing.

Wie lange dauert es, Zeitverlängerung zu machen?

Oder noch eine Sache wäre Aging.

Wie lange dauert es, dass etwas in unserem System bleibt?

Es ist nicht exakt Zeitverlängerung.

Wir können nur Zeitverlängerung betrachten.

Aber ich denke wirklich, dass ein Wertstreben-Map eine wichtige Sache ist.

Okay, also du sagst, wenn wir Zeitverlängerung reduzieren und Zeitverlängerungen reduzieren, werden wir Zeitverlängerung optimieren, obwohl wir unsere Zeitverlängerung nicht direkt messen.

Ja, weil die eigentliche Messung von Zeitverlängerung, und es gibt wahrscheinlich Leute, die mir sagen, woran ich falsch bin, aber ich habe diese Dinge seit Jahren studiert.

Und ich glaube, dass Zeitverlängerung für uns keinen Sinn macht.

Verstehen, was es ist, macht Sinn.

Aber ein weiterer sehr wichtiger Punkt, verstehen, was Inventar ist, und wie wir Inventar in unserem Unternehmen messen.

Und konzeptuell, Inventar ist alles, was wir gearbeitet haben, was nicht in den Händen der Nutzer ist.

Ich denke, die Definition von Mary Poppendick ist etwas wie das.

Wenn wir herausfinden, wie wir unser Inventar messen können, wie viel haben wir, was wir gearbeitet haben, wie viele Stunden haben wir gearbeitet, was noch niemand benutzt hat, dann ist es wert, das zu wissen.

Wir wollen das so wenig wie möglich reduzieren.

Und das selbe mit dem Queuen, so wenig Queuen wie möglich.

Das sind für mich bedeutende Dinge.

Vielleicht in ein paar Jahren denke ich mir, das ist nicht eine gute Sache.

Aber jetzt denke ich, das ist eine gute Sache.

Und du hast eigentlich nur eine Referenz zur LEAN-Softwareentwicklung gegeben, und auch, das ist alles um LEAN-Produktion und das Toyota-Produktionssystem und solche Dinge.

Also das ist, wo das wirklich herkommt.

Und es gibt wahrscheinlich eine ganze Geschichte, wie das auch missverstanden wurde in der deutschen Autokarrenindustrie und so weiter.

Ja, aber lasst uns klar sein, es ist wahrscheinlich missverstanden in der japanischen Autokarrenindustrie auch.

Oh, okay.

Es ist nicht so, dass sie das perfekte Wissen haben.

Sie kamen mit einigen Ideen vor, die wir wahrscheinlich in der westlichen Welt missbrauchten.

Aber das bedeutet nicht, dass all das Wissen, das sie hatten, perfekt war.

Du kannst nicht Kopie und Paste Wissen von einem Ort zu einem anderen.

Du kannst nicht Kopie und Paste Techniken auf jeden Fall sinnvoll machen.

Also müssen wir vorsichtig sein.

Diese Dinge sind da, genau wie mein erstes Bild.

Diese Dinge sind da, um uns ein Verständnis zu geben, vielleicht können wir eine Aktion machen und ein Ergebnis erzielen.

Es ist nicht so, dass das, was sie getan haben, das, was wir tun sollten.

Was sie an einem höheren Niveau getan haben.

Lasst uns immer überprüfen, was wir tun, und davon lernen.

Das ist nützlich.

Ja, wie eine Art Inspiration.

Ja.

Pierre Gauche auf YouTube hat gesagt, ein Projekt, das nah an unserem Team liegt, liegt an der Verschlechterung.

Der Beitragsfaktor ist das hohe Niveau der Prestige.

Einige Individuen haben eine bestimmte Technologie gewonnen, obwohl sie Kritik hatten.

Und jetzt können sie nicht ihre Fehler vermitteln und Kursen verändern.

Das würde bedeuten, dass sie die Phase verlieren.

Ja.

Das ist so weit weg von keinem Wert, aber ja, ich sehe das immer.

Ja.

Das bedeutet, dass der erste Grund, warum Dinge nicht funktionieren, ist auf dem sozialen Niveau und solchen Dingen.

Das ist ein guter Punkt.

Das könnte es sehr gut sein.

Ich würde es vielleicht so sagen.

Es gibt wahrscheinlich keine rationalen Gründe für viele der Dinge, die wir tun.

Ich glaube, Ben Franklin hat gesagt, dass ein rationaler Mensch eine großartige Sache ist, weil wir jede Entscheidung rationalisieren können.

Ja, das ist ein guter Punkt.

Und das ist eigentlich ein sehr guter Punkt, weil, was du sagst, ist, dass das wahrscheinlich effizienter ist, oder ich habe gesehen, dass das effizienter ist, oder es eine bessere Art des Arbeiten ist.

Aber jetzt ist der Punkt, auch wenn es wirklich so ist, dass es nicht bedeutet, dass andere Menschen es adaptieren können, weil die Menschen irrational sind.

Und ich denke, das ist ein sehr guter Punkt.

Es gibt keinen einfachen Weg durch das.

Genau.

Also, Beitbock hat gesagt, ich denke, dass Wirtschaftler oft eher durch ein dynamisches System aufgehoben werden.

Sie fordern Planungs- und Stabilität und ein Volatilsystem, vielmehr einen steilen Wachstum und ein limitiertes System.

Ich denke, wir haben das beschlossen, weil, was du gesagt hast, und ich denke, das war ein sehr guter Punkt, dass wir als Menschen suchen nach Sicherheit und eine Art Kontrolle.

Und das ist wirklich etwas, was ich aus diesem Episode entfernt habe.

Ja, es gibt nichts Einfaches über das auch.

Wenn wir wirklich die menschliche Natur verstanden hätten, dann hätten wir diese Gespräche nicht geführt, oder?

Alles wäre perfekt.

Und das ist es nicht.

Es ist, was es ist.

Ja, wir sollten alle Psychologie studieren.

Richtig.

Yang Yin Kim hat gesagt, es ist das Gleiche mit Beratungen.

Ich weiß nicht, was er oder sie sagen.

Ich kann das beantworten.

Ich bin zu vielen Orten, wo sie etwas sagen, wie Unsere Beratungen sind nicht sehr nützlich.

Wir müssen besser bei Beratungen sein.

Was ich denke, die echte Sache ist, unsere Beratungen sind nicht sehr nützlich.

Lass uns herausfinden, warum wir denken, dass wir Beratungen brauchen und einen besseren Weg finden, was wir brauchen.

Es ist eine sehr ähnliche Sache.

Beratungen sind ein Symptom.

Sie sind nicht das Problem.

Beratungen sind ein Symptom.

Sie sind nicht das Problem.

Das ist ein starkes Statement.

Ja, das ist ein guter Punkt.

Kat Petersen hat gesagt, aber das ist lange her, also es hat nichts zu tun mit dem, was du gerade gesagt hast.

Ich stimme total zu, Woody.

Wir halten an die wahrgenommene Sicherheit von Beratungen und Kontrolle.

Wir setzen oft Begrenzungen auf das, was wir können oder nicht können, und das fixiert unsere Denkweise in einem potenziell schädlichen Weg.

Ich denke, das ist ein guter Punkt in Bezug auf die Diskussion, die wir hatten.

Ein guter Beitrag auf Steuern gegen Kontrollen.

Kontrollen im ökonomischen Sinne.

Ich denke, das war bei den Mercedes.

Ich wollte sagen, dass wenn man einen Tank hat, dann ist Steuern vielleicht nicht so wichtig, aber das ist eine andere Diskussion.

Ich bin kein militärischer Mensch, aber ich habe ein paar Videos über militärische Taktiken gesehen, und ich würde sagen, dass ein hoffnungsvoller Anti-Tank-Maschinen wahrscheinlich ein guter Weg gegen einen Tank sein könnte, der nicht sehr gut steuert.

Aber was weiß ich?

Wenn ich ein Gorilla war, im Gorilla-Kampf, denke ich definitiv, dass es keine Wertschätzung gibt.

Wenn ich ein General bin, der eine Armee leitet, die extrem gut finanziert ist, denke ich, dass Wertschätzungen eine tolle Sache sind.

Aber ich denke, wie Napoleon, einige von Ihnen haben von ihm gehört, er war ein General in Frankreich für eine Weile, er hatte das Sagen, dass es eigentlich war, lasst uns engagieren und sehen, wenn gefragt wird, was der Plan für diese Kampf ist.

Der Plan ist, wir engagieren uns mit dem Feind, und dann beginnen wir, Entscheidungen zu machen.

Bis dahin, sind alle Betten aus.

Engagieren und sehen.

Ich kenne einen ähnlichen Satz von Eisenhower, der sagte, dass kein Plan überlebt, der erste Kontakt mit dem Feind.

Ja, so etwas wie das.

Ich denke, er sagte, Pläne sind wertlos, aber die Planung ist gut.

Und ich gehe damit ein, lasst uns das nicht überdrehen.

Was er darüber spricht, ist, dass wir Pläne haben müssen, damit wir mit Wissen reagieren können, wenn wir die Entscheidungen treffen müssen.

Aber wenn wir die Entscheidungen zuvor treffen, sind wir in Problemen.

Wir müssen gut sein, unsere Anleitung zu schützen.

Wir müssen gut sein, unsere Leute trainieren, sie schnell zu bewegen.

Es gibt viel, was wir tun können.

Aber wenn es um die Kämpfe geht, ja, alle Betten sind aus, wie sie sagen.

Nils sagte, das ist der wichtigste Punkt, im Gegensatz zu vielen Geschäftspunkten.

Softwareentwicklung ist nicht eine Reihe von messbaren Schritten.

Oft führt eine Veränderung zu einer weiteren Veränderung, die zu einer weiteren Veränderung führt, und so weiter.

Das ist also eine exponentielle Explosion, was sinnvoll ist.

Um das zu beantworten, kann die Variabilität zu breiten Schwungen in den Ergebnissen führen.

Wenn wir nur eine kleine Variabilität hatten, aber die Variabilität sich selbst entwickelt, ist es wie ein Pendulum, das viele kleinere Pendulen an sich hat.

Wenn alle Pendulen in die gleiche Richtung gehen, gibt es einen wilden Schwung.

Wenn alle Pendel sich gegenseitig verändern, gibt es nicht viel.

Das ist die Art der Sache.

Wir wissen es nicht.

Wir können ein System aus der Kontrolle bekommen.

Es ist nur so, dass wir dieses Episode hatten, mit, wie heißt er, über, ob wir Ingenieure sind, Softwareingenieure, ob wir wirklich Ingenieure sind, mit, ich werde es nachlesen, und er sagte, dass wir Ingenieure sind, und wir, alle Ingenieure, arbeiten in Iterationen.

Also, ich weiß nicht, ob Produktdesign in anderen, ich meine, andere Arten von Produktdesign nicht vergleichbar ist mit dem, was wir tun.

Also, weil grundsätzlich dieses Statement sagt, dass wir anders sind, Softwareentwicklung ist anders, und ich weiß nicht, weil Produktingenieure Ingenieure sind anders, aber Ingenieure, jede Art von Ingenieure, ist wahrscheinlich ähnlich, und der Episode, den wir hatten, war mit Hidalg Wain, und die Technik, die er nutzte, war, er interviewte Menschen, die als Ingenieure arbeiteten, in anderen Bereichen, wie mechanische Ingenieure, elektrische Ingenieure, diese Arten von Dingen, und dann als Softwareingenieure arbeiteten, und er fragte sie, ob wir Ingenieure machen, und der Konsens scheint, dass wir Ingenieure machen, genau wie alle anderen.

Ich verstehe das ein bisschen.

Ich habe einmal einen Film gesehen, in dem Menschen große Projekte vor hunderten Jahren ingeniert haben.

Sie nutzten Theorien, die sie noch nicht mit der Mathe zu beweisen hatten.

Diese wurden auf Wissen gebaut, die sie nur von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache von der Tatsache beiégetragen sind.

Es war normal, dass wir ganz viele in der Zeit waren.

Ich glaube, wir sind noch in den ersten Stufen.

Und wir werden nie da sein.

Dinge ändern sich jedes paar Jahre.

Und jetzt ändern sich Dinge wieder.

Ich glaube, wir sind nicht in einem stabilen Zustand.

Aber fast kein wissenschaftlicher Bereich ist in einem stabilen Zustand.

Wenn wir da sind, ist es alte Sachen, die wir in die Vergangenheit geflüchtet haben.

Ja, das ist wahrscheinlich ein weiterer Episode.

Ja, ja, definitiv.

Wir brauchen eine Rundtabelle für diesen.

Ja.

So, Byteboxer, bitte nehmen Sie die Definition eines echten Wirtschaftspersonen zu Ihrem Lieblings-HR-Departement und stellen sie in Job-Office.

Das würde die Welt für besser ändern.

Also, ja, Entschuldigung über das.

Aber lernt die Business School nicht alles über Zahlen, Auswertungen usw.?

Erzählen wir den Geschäftsleuten, dass sie falsch sind?

Das ist ein sehr gute Frage.

I haven't been to Business School.

I haven't been to Business School.

I haven't either.

I have worked with a lot of people that in the US they have the MBA, which is a program where you get a degree in business.

There are different concerns here.

There's a concern at the level of the creation of the software or whatever it is we're doing, but there are concerns of the business themselves.

I'm doing them in this direction.

These are different concerns.

Their concerns at the business level are not about the same things that we're concerned with at the level of creating software.

I think we need to bridge that.

We need to make it where there's a better understanding in both directions.

If a top-level people in the company, they're more interested in how the rest of the industry perceives them, so the buyout that they're working on having happen, happens.

Well, that has nothing to do with how effective we are in creating our software.

What's important is that our software is perceived as being meaningful.

Whether it actually is or not may not be a concern.

They're working in a different area than we are.

I don't think there's any easy way to say, oh, we have to get them to understand this or they have to get us to understand this.

There's a whole lot more to this than I'm ready to think about.

I think you made a very good point.

It should be understanding in both directions.

There should be a bridge between these two professions.

It may be coming closer.

Yeah, so that's the point.

And the point that I originally wanted to make is the discussion that you have is basically what you're basically saying is, is it worth estimating the effort?

Shouldn't we focus on value?

And these terms and this idea to me is an economics idea and it should be something that economic people should be able to relate to.

And we even had the discussion about how this is really manufacturing, which is, again, an economics thing.

So at the core, it is an economics discussion that we have.

So I don't see why people with an economic background shouldn't be able to follow it or agree.

So the overall arching idea is that if we get good at generating value, that's more important than estimating value.

If we get good at generating value, it's better than being good at estimating cost.

So what is important to get good at?

It's not the things that we're trying to do when we're doing estimates.

Exactly.

And that should be something that isn't specific to us, but it's rather an economics thing.

Yeah.

These are things to think about, and I just want to make sure that conversation is happening.

Let's have this conversation.

And we definitely started that.

So thanks a lot for your time, of course.

And let me say again that I'm looking forward to your talk at Archer Meets Architecture.

Yeah, that's just April 3rd and 4th in Berlin.

So see you there.

Really looking forward to see you in real life.

Yes, me too.

Looking forward to your talk, and have a great evening.

I'm actually not sure what the next episode will be, but there will be one, and it's going to be next week.

So I'm looking forward to that as well.

So see you, and have a great evening.