# Folge 242 - Generative AI Meets Software Architecture mit Ralf D. Müller


## Einführung und Themenänderung

Unfortunately, this has been temporarily prevented.

That's why Eberhard Wolff has joined us.

### Ursprünglicher Plan

We're going to change the subject a bit, because I was actually going to interview Lars as an expert on the topic of Gen AI meets architecture.

And...

One moment.

Sorry.

Sorry, I just got problems with my audio setup.

So, we're going to change the subject.

### Neuer Fokus

I'm not going to interview Lars as an expert, but I'm going to talk about my experience with Gen AI and software architecture.

And Eberhard Wolff will hopefully contribute his expert opinion.

We're going to start with an experiment I did.

I used the machine, an LLM, to create a complete project.

## Das AsciiDoc Linter Projekt

In a channel, a user complained that AsciiDoc still doesn't have a linter for several years.

I thought, this is a nice real-world problem to start a project with the AI.

### Projektbeschreibung

AsciiDoc is a system with which you can write documentation.

I don't think it's just architecture documentation, but in general, a linter is something that says, the stuff you enter is meaningful or less meaningful.

That was the missing feature.

AsciiDoc is one of the projects where you do a few things, and that's the background.

Exactly.

AsciiDoc is the markdown for technical documentation.

The linter is supposed to check if a few files have been saved, that no overlays are skipped.

### Motivation

I thought it would be a good real-world project to see if I could program it with the AI.

## Agentic Workflow

I have my own chatbot front-end, which has developed an agentic workflow.

That means it has function calls that it can call.

These function calls include, for example, that it can use the bash, that it can execute Python code.

I wrote a system prompt that depends on it.

Sorry, what is an agentic workflow?

I can fill an hour on this topic alone.

### Definition

An agentic workflow is a self-running, independently running workflow.

Most of the time you also talk about a workflow with agents.

### Funktionsweise

That means I don't just have one chat partner, one LLM, but I have several LLMs in different roles.

For me, it's not several LLMs in different roles, but one LLM.

If a tool calls, like Chatshub-T, Chatshub-T can call a Python interpreter or generate a picture.

After the call, the control goes back to the user.

That means it doesn't run independently.

Sometimes I also get Chatshub-T to the independent one.

I've made it so that the control flow stays with the LLM.

That has the interesting side effect that if the LLM executes code and it comes from the compiler, a syntax error or something, then the LLM says, wait a minute, I think I know what it's about, I'll write the code again, try it again.

If I want to work in architecture with the Gen AI, I have a plugin, a function call, which can render a plant UML diagram.

That means Chatshub-T itself generates plant UML code, shows the code, I don't see a diagram yet.

If I go to the croquis server, croquis.io, then it can render the diagram via a library, sometimes gives syntax errors back.

The LLM then reacts independently on it, corrects the code until the diagram comes from the croquis server and then it shows the diagram.

That's totally cool.

It can correct itself via this agentic workflow.

With this Linter, I thought, it's a simple architecture.

It's a program that somehow has to go over the ASCII doc source code and applies different rules.

Rules that check certain properties.

These rules are individual modules that an LLM can implement individually.

## Test-Driven Development mit AI

I assigned the model that it should work test-driven.

### Implementierung

That's how it first wrote tests, then wrote code, and the tests failed and it went into the iteration.

It actually created a complete project.

That's software development for now.

But at the end, when it implemented the first rules, I already taught it how to work with the Architecture Communication Canvas.

## Architektur-Dokumentation

It's a one-pager that describes an architecture.

I asked it to create this one-pager.

It did.

Then I looked for the stars and said, you know ARC42, the template for architecture documentation.

Please create a complete architecture documentation.

That's what it did.

The exciting thing is, we already had an episode about a similar approach where we tried to solve the ISAQB task.

But the model didn't know the full extent of my solution because I had a lot in mind.

I could ask a lot of questions, but a lot remained hidden for the model.

Here it has now made the architectural decisions and documented them.

This gave it the opportunity to document these decisions.

What did you say to this system?

If you tell it to build an ASCII documentation, you have to have a set of rules.

This set of rules says, this is what we want to check with this linter.

You said, for example, that there will not be a cross-hierarchy.

I assume you don't mean 1.1.1 equal to 1, but 1.1.1 and then 1.1.1.

Then you would have to say, this is a rule that makes sense for some reason and you would have to define what this rule looks like.

How did that all come about?

I left the model to the master himself.

Of course, I have given three rules in terms of language.

According to the motto, I don't even know what the other two were.

I then told the model to come up with further rules.

This knowledge of the world comes into play by the model.

It knows other lintels.

It knows, for example, the Markdown linter.

It has come up with rules.

Let me see.

There are three rules.

For example, in ASCII DOC, the top level of the header is reserved for the book title.

A book can no longer have a book title.

That's why you can only give this level once.

Then there are block rules.

He came up with two.

I have certain blocks, e.g. a table or a code block.

If I don't close them in the end, it doesn't work.

If I have a modular document, where the code block is at the end, everything is automatically closed.

But if I include this document in a larger document, then I get problems.

He also checks that.

He checks white spaces in certain situations.

He has white space rules.

He has images that have certain attributes.

That's what he came up with.

He has implemented it.

He has also added that we have a few rules in Petto that we want to implement in the future.

For example, broken links.

That made the model so independent.

That means, it intervened in our work as an architect and took over this work.

How did that come about?

Did you take a look at it yourself?

Did people say anything about it?

How is the community or the user feedback at this point?

So far, it hasn't been published very well.

That means, this is actually the first time we're talking about it.

I took a look at it.

I have to say, the result looks pretty good.

I am quite satisfied with it.

He used diagrams in the documentation.

That is understandable.

It contributes a lot.

The diagrams look good.

The results used to be worse.

I think some diagrams are exaggerated.

They are superfluous.

I would just delete them.

But he actually has the chance to create diagrams through this planned UML approach.

And now that I look over the documentation, there is a second effect.

Because in the ASCII doc, the diagrams are described textually as planned UML.

But in the rendering, they are described as diagrams, which we can capture visually.

My experience with the models is, that they still can't handle diagrams so well visually.

But if I put it back on this project and look at the documentation, it will see the source code of the diagram and can therefore understand it.

The other point is, if you develop the thing further, I saw in the chat, that the tension is getting bigger and bigger.

Marco Wessemann wrote, I am very curious about the ACC.

I don't know exactly what an ACC is.

Architecture Communication Canvas.

You mentioned it.

I'll put that in the chat now.

I haven't really looked at it yet.

But the feedback, of course, interests me too.

And that's why I'm putting it in here now.

I think one of the listeners of what we did before with the ASCII Advanced Server example task, and I wanted to correct myself, but I have such a memory, that we realized that the task was actually no longer in the window that the system was still looking at.

Nevertheless, I have the feeling that the documentation is somehow quite good.

So I think you have to be careful.

Because, how should I say, GPT and all these AI solutions are, in my opinion, optimized to give the impression that they produce something great by answering questions.

I don't answer a question with yes or no, but I say, here's a lot of information.

And you think, wow, there's a lot of information and that's definitely true.

I think I got a little carried away by it back then.

And I think that would be the hint now.

Or at least that's how I understand what you're saying, so that would be the next question.

How do you know that the code actually works as it should, or that the system does what it should?

On the one hand, it invented requirements, that is, a problem could be that things that a linter should actually do are not in there at all, although you say, well, there is a Markdown linter.

Markdown and ASCII docs are relatively similar, but how do you know that it makes sense now, what it does?

Requirements have actually been invented, right?

Yes, of course, requirements have been invented.

I could have invested more time and gone into dialogue with him.

I could have said, ask me questions about the answers.

But I wanted him to get started and I thought, that's not such a difficult problem now, you can find the requirements yourself.

We do that too, sometimes, that we make suggestions for requirements for such a project.

Just to make it short, I don't think it's that absurd to stand here and say, okay, there is a linter for Markdown, I need the same for ASCII doc, and that's why I'm ...

I didn't mean to disqualify it, but I have the feeling or I would have the assumption that it is actually possible for such an automated system to build something that actually makes sense, because it's just a copy.

That leads to the question of whether we as humans would not have built just a copy.

Yes, definitely.

I didn't expect any creativity from him, but I found it very exciting that he actually did that with the test drive, that he took a unit test framework.

Until just now, I wouldn't have known if he might have solved the tests by just saying, it sounds true.

Now I've just taken a look, no, he's actually doing something.

And I also saw in his dialogue how the tests were always wrong, he corrected them, he implemented a new feature, an old test was wrong, and then he improved it again.

So there really seems to be logic behind it.

He also said at a certain point, interestingly, that the simple tests are not enough for him now.

He also wants to do test coverage, has activated test coverage, has noticed, I think we're at 29 percent, and then asked in between, should I implement the next feature or increase the test coverage first?

I think it's super spooky what's going on there.

Maybe another question in that context.

So if I have a unit test, it says 2 and 2 is 5 and I have an implementation that already says 2 and 2 is 5, then it's consistent in itself, but objectively wrong.

How do you know that this system is doing what it should be doing?

So in the sense that it does something that is actually technically correct.

So 2 and 2 is 4.

If I say in the system, in the test and also in the implementation, then I have a 100 percent test coverage.

I also have a lot of green tests, but in the end I have nonsense.

So how do I know that this is not the case?

That is actually a question that is difficult for me to answer at the moment.

I see it as, for me it is the situation as if I had never told a colleague, and he comes back and says, look, the following features are implemented, the checks are green and I would rely on it.

Now the next step would be to try out the finished Linter and then notice whether the colleague has cheated or not.

At the moment I don't see any signs that the system has cheated.

I see that the Linter is called up in the tests, checks how many findings he has found to these rules, and that actually seems to be good.

The reason why I ask is our experience together, where I had the feeling that Chachibitty impressed us a bit with a pretty text.

And to be honest, that is one of the lessons learned from our episode together.

For me, when it comes to architectural documentation, it plays a role that you have to be careful about how much you can get involved.

For me that is also a bit, if I should be cynical now, a consultant skill.

You can somehow convince him to do something that is actually nonsensical.

And that's why I ask.

The other point why I ask, I wrote this blog post some time ago on the topic that AI is overrated.

And I was looking for this scientific study.

I came across it at some point.

I didn't look at it excessively.

And then you said, okay, let's take two groups.

One group builds code with AI tool support and does it in the classic way, which typically means Stack Overflow for us.

And that should have been tasks like delete my file.

And then it turned out that the group that used Stack Overflow built the safer solution and believed that there was a less secure solution.

That means the group that used AI tools had a high confidence in their own code, which was unfortunately wrong.

In the sense that it was less secure.

And those were obviously tasks like deleting the file.

Security is the feature.

If I don't get it right, it makes no sense to delete the file.

That's cool.

This system gave me this Linter.

How do I know that what happens to me makes sense?

And that it actually works.

And that's something different than with a human colleague.

I would expect him to have a better understanding of the real world and somehow tried, but I don't know.

There are a lot in the chat, but otherwise your thoughts come to an end first.

I think that's more important.

I just lost him.

We had this experience that we had the feeling that he told a lot, but there is little content behind it.

If we talk purely about textual tasks, linguistic tasks, then you can hide us quite well.

But we have the advantage in IT that when it comes to code, we can verify the code.

Of course, if he writes the tests himself, then he can cheat again.

My experience is from small experiments that he doesn't cheat.

Well, something can happen to him.

But my experiments were again and again, I said, write me a merge source. and the sorting in the test was not alphabetic, but according to the length of the words.

Or I give him numbers and the sorting in my test is again not according to the numbers, but alphabetically according to the number of words.

He experiments around, sometimes he pretends that he says, well, it's just a test, that means I can actually return a result in my merge sort and that works.

Then you can say, well, I have more tests here.

He definitely tries it first with code.

And once I even had the case that I had a mistake in the test.

He tried it around and in the end said, well, you have a mistake in your test.

I can't sort that at all.

And I also have the feeling, and I'm not an expert enough, maybe we have someone in the chat.

We are still relatively old-fashioned with the world knowledge of last year with most models.

So little has changed.

But I have the feeling that the interface, that is, how the system learns to deal with question-answer pairs, that has improved over time.

We also see that with OpenAI, with the reasoning model, which takes longer to answer, but actually performs this chain of sort and that we have thus got better models with which we can solve these tasks better.

What is a chain of sort?

That is, most of the time we tell the model, do this and that.

Give me a detailed link for my lecture next week.

And then the model is bad.

But if I give him a chain of thought and maybe even iteratively develop it, that I tell him, first of all, make me a rough link.

If you have the rough link, give me the detailed link.

If you have that, maybe make me speech texts.

That is this chain of thought with which he can deal better.

And that's how the new models do it internally themselves, that they first think about what they have to do to create this solution.

In this case, first write tests or first think about rules, then write tests for it, then implement.

The chat is boiling over.

Yes, exactly, let's go through it.

So Teutoteut wrote, Ralf told so much, which in the end the AI realized.

And I'm very curious about the end result.

That is not yet released, so to speak.

I pasted the link in here, just before this.

Okay, good.

So that means that it is already available on this Internet.

And I find it exciting that the AI corrects itself to a compatible artifact, because I have to add it.

From my perspective, it is probably compatible, what comes out of it.

You say that it has not met the tests.

It is partly like that.

It depends on the language and on the task, how well it can do it.

For example, it finds a lot of examples in the web, so it has it in its training data.

Nevertheless, it sometimes has a syntax error that it does not think about that a name has to be put in quotation marks when space is included.

Then it corrects itself.

Other things, not so well-known languages or so, it has bigger problems.

Okay.

Then Jörg Möller wrote about the question, how do I know that there is no cross?

As I said, possibly as preemptively as if a person had written the solution.

I think it says there.

Peer reviews the code and even peer review agents over the generated code in the use of the written requirements.

And that's an interesting point again.

You just said there was this Stack Overflow experiment with security.

How secure is the code?

My frontend actually has a tool called inner dialogue.

It can call up an LLM itself.

It has to give a system prompt and then a task.

And if you tell it to look at the code from the perspective of a security expert and from the security of maintenance, then it actually goes into this inner dialogue.

And especially with maintenance, I find it fascinating.

You say, oh, with the variable names, let's stick to the standards.

Please put comments in the code.

And by the way, this one method should be modularized and split into two.

For me it seems now, I don't even know if I read that, but rather to the question, no.

For me, there seems to be a history of, how should I say, the task of controllability behind it.

So either I could actually review the code completely now, but then it would mean that I would go down to this level.

And what I found so exciting about your example and what you did with it, is that my principle says, well, solve the construction.

And then something comes out.

In fact, it's just like when I said to a team or a person, build it.

And I don't want to review stuff on that level.

But yes, you can of course have someone look at it again.

But that doesn't mean that it's more manageable in my opinion.

The result will only get better.

I still don't know what's going on in there.

Exactly, then Crazy P wrote to me.

Linter are meant to perform an automated check.

The Linter would be responsible for the check.

So we're talking about a Linter for ESCIDOC.

That's a documentation language.

And not about a Linter for the primary language itself.

So that's two different things.

Then he wrote on Twitch, DarthScady.

I think the tests should always be written by people.

So maybe not in code, but the technical content.

It may be that 2 plus 2 equals 5 is correct in a certain technical context.

I think we've already discussed that.

So that's just this story.

Then you would somehow intervene on this code level.

And the other thing is, I have to think of the episode we did about code retreats.

I can, and you said it yourself, I can make sure that the test is green.

And I can only implement this example that the test tests.

There is an exercise in this pair programming code review thing.

That you try to be as evil as possible.

And if someone wants me to implement addition, and 2 plus 2 is supposed to give 4, then I say my addition always gives 4 back.

And then the test is green and it doesn't do an addition.

Then comes the next case and he says 2 plus 3 is 5.

Then I look at the second addition factor.

At 2 I say the result is 4.

At 3 I say the result is 5.

I ignore the first factor.

I have two green tests again and so on.

And that's a fundamental problem of tests.

That the tests just give examples.

And the point of this exercise sounds a bit bizarre.

But the point of this exercise is to point out that if you want to write good tests, you have to do a lot.

You have to do so much that the other person is forced to implement the code.

And that can be quite time-consuming to do.

And I don't want that.

You address a topic that applies not only to tests, but also to documentation.

I was always skeptical about automatically generated tests.

I give the machine a function and tell it to write tests for it.

And it doesn't know what this function is supposed to do.

It only sees what it does.

That means if the machine tests exactly, it also tests the bugs.

It is similar with documentation.

I have always said that automatically generated documentation makes little sense.

Because when the machine sees the code, it can explain what the code does.

It cannot explain why this code has been implemented.

Why I took a merge sort and not a quick sort, for example.

This information is lost at the point where I just give the test or the code for the documentation of the machine.

Here we have the interesting point that the machine itself has made decisions that it can document.

The machine has decided for itself what this code is supposed to behave like.

And hopefully it was able to write behavior-based tests.

And that is an assumption of mine that still needs to be verified.

But that's what makes this experiment so interesting.

That the entire block has been given to the machine.

I think I'll say the same thing again.

I am always careful because it can lead to an illusion.

In other words, it seems like it makes sense, but in reality it doesn't.

You have the feeling that the machine is doing something.

Because the suspicion is that there is reasoning behind it.

You kindly gave me the architecture documentation earlier.

And in the architecture documentation, just to pick something out randomly, there are quality requirements.

This is the first performance scenario.

### Qualitätsanforderungen

The processing of a thousand-digit document should take less than one second.

This is a high priority.

Next, many files need to be processed.

If it should be 200 documents, it should be less than 10 seconds.

This is medium.

Then there is memory requirement.

If I process a large document, for example 10 megabytes, then I should use less than 100 megabytes of RAM.

Is that thing in Java?

No, that's in Python.

That's also high.

Then it says that the startup time of the Linter is less than 0.5 seconds.

That's medium.

I don't know how you see it.

But that sounds to me ...

One question would be, where the hell is that coming from?

And the other question is, does the software somehow comply with these conditions?

I would be surprised if there was a reasonable answer to that.

I think that processing a thousand-digit document takes one or two seconds.

I don't think it matters.

I don't know why it's high priority.

100 documents in less than 10 seconds.

I use SGDoc.

Have you seen a project where there are 100 SGDoc documents?

It can easily accumulate.

Especially if you have several modules that you document with ARC 42 to a large project.

Then that can happen.

But I think it's important here that the machine ...

Maybe I'm interpreting too much.

But such a Linter should run fast.

It shouldn't stop the image process.

Maybe I'm interpreting too much.

Yes, it's just random.

To be honest, I scrolled through it again and stumbled over it.

And I'm a bit ...

I always find it difficult with the quality scenarios.

And especially with the quality scenarios, I think it's important to find out the things that are actually really relevant.

And not some random things.

And this is an example for me of ...

I can imagine that humans would write the same way.

But I would ask humans, where does this come from?

Why is that?

And try to find out what it should be.

Because when I write down such a thing, I say that it is important.

Performance of the thing is important.

And especially there is a high priority.

And I don't think that's understandable.

So not exactly this question with the one second would be the question.

And the next question I ask is ...

Okay, how do you know that this thing needs a second?

Do you have a test?

Show me.

And it also says that the thing should start within less than 0.5 seconds.

Is that good?

I don't know.

What is the price?

Probably.

No idea.

And that's just what I mean.

## Kritische Betrachtung

I think you have to stay critical.

### Vertrauenswürdigkeit

I can also briefly write down the requirements.

And think about it.

And then you see, wow, quality scenarios.

Very, very nice.

But then there is exactly the danger that if you find out words, they have no content.

And I think that's something I want to warn against.

Absolutely.

But I also have to say, I'm amazed that he actually linked the quality scenarios again.

In performance, reliability, usability.

And then also built a quality tree.

But your feedback now.

I think that's great.

Because I would now include that in the system prompt.

That I always tell him when he creates quality scenarios, he should also justify why that is important or less important.

And then he provides a sound justification.

Yes, indeed.

But then I will be able to check it better.

And will be able to ask questions.

If I take more time, then I could also work with him much more interactively.

And also move him in the right direction.

Whether it really is that it's going so fast.

I could give him the task next to try to write tests for the quality scenarios.

Exactly.

Which then means that you actually need an architecture consultant.

Although no one does it themselves, but you need an architecture consultant.

And I think that's another point.

If you would suggest this to someone and say, okay, do you notice anything?

Or a kind of Turing test.

Can you tell the difference between what a human has built?

The Turing test is with this test where you say, I forgot how it works exactly.

You have a predefined conversation with a client about, I think, a certain topic.

Or you can choose freely.

You can decide whether it's a machine or a person you're talking to.

Something similar could be done here.

You could say, okay, cool, this architecture documentation, does it come from a human or a machine?

That's a different question than, is it good or bad?

And I'm not sure what the result is.

Because if I pull this out now, that can also have been written by another person.

I think that's our daily bread, that you say, okay, this is a quality scenario.

Explain to me why the hell there is this quality scenario.

Why is this important?

And then we all agree, maybe it's not that important at all.

Especially with performance, such demands have somehow fallen from the sky.

I don't think that's unusual at all.

And so, that's also something I took away from our last episode.

We can definitely get better as humans in this whole area.

I think that's clear to me too.

You address a topic here, I notice it again and again, if you actually use the A42 as a form, and then it falls down, oh, five quality criteria.

I don't have any at all right now, I'm sucking something out of my fingers.

Then you would actually behave like that in some cases.

And when you address the Turing test, it's fascinating.

I would now, for example, because of the graphics that have been created, the diagrams say, okay, with some diagrams, with the risk matrix, technical risks and technical debt, you notice that no one has visually looked over it and it doesn't make any sense at all.

That was certainly the machine.

With other things, I have to say, the Turing test, I started to say at some point, the machine doesn't pass the Turing test because it's too perfect.

As far as I know, the setting is like this, you have two chats and you have to say which one is the chat partner machine and which one is human.

And you quickly notice that the knowledge is very broad, very detailed and such things.

And the machine still passed the Turing test in an experiment.

And the system prompt was like the motto, well, answer like a 15-year-old teenager and also include spelling mistakes and such things to get rid of this perfectionism.

And that's how the machine, I think, in 51 percent or so of the cases, actually got the human status.

Which, in turn, means that it's just about, I'll say, so-called elements, like correct spelling or something and less about content, possibly.

Exactly, Marco Wesselmann wrote that the outcome should of course be subject to the review process, how it is designed, it is certainly company-dependent, acquisition against qualities and so on, was discussed, I think.

There are similar approaches with other text artifacts that arise via LLMs, and Jörg, I think, it's also about this review topic, and Jörg went on to write about this thing, that it's going to be reviewed.

But you can also let yourself be supported, if you want to, by embedding the agent role reviewer.

But I don't think that leads to it, so then you have a system that can produce nonsense in itself, no idea.

You run a few reviews the other way around, if you know that it arises through an LLM.

It was just discussed.

Okay.

Where was the link posted?

The link is not in this chat.

I posted it again.

Okay, all right.

My opinion is that the biggest problem is that AI code cannot classify in a larger context, especially indirect dependencies are usually not recognized, also semantically often problematic, writes Malicieux on YouTube.

Exactly.

That's actually an interesting problem, where I sometimes thought, we write code for people, the machine may need other code.

Especially in Java, if we have an interface definition, an implementation, then the usage and the documentation, then we have four documents, or maybe much more, in which the model actually has to look.

Such a copilot, GitHub copilot, I've always had problems with that.

He always took only three documents maximum.

And then the context is not enough.

In my own experiments, I can use the full context, 128,000 tokens, that's already a booklet, what I can use.

And also the copilot and other systems go beyond that you now have the complete repository in a vector database.

That means, I think, we solved this problem quite well.

Yes.

And I think that leads to such an interesting story.

That was also what I thought, when you told me that the architecture documentation was just such a flash of thought.

What is that supposed to be?

Because I feel as a human being, that's something about human communication.

And I'm not sure if that's actually what you want.

Actually, the discussion is now turning around.

These are the essential properties of the software.

And I want to explain this to someone else.

And this is actually about interpersonal communication.

What we are discussing here now is something different, I think.

It's kind of like, can you tell me what properties this software actually has?

And can I somehow verify the result?

And is it comprehensible to me what happened to me?

Maybe I need a different kind of documentation and a different kind of representation for that.

I thought it was kind of absurd that a machine creates a document that is actually intended for human communication.

So if I write an architecture documentation so that you can take over the system later and you understand what I've been thinking about, fine.

But is that something that plays a role in humans now?

Probably, because this Linter, as you just said, will somehow continue to be developed by some AI system, right?

I would assume that now.

That would be my goal, that I ask the AI system to develop it further, yes.

But you address an interesting point.

There are different factors where we have to think about how to go on.

With the AI that we can no longer understand how it influences our work.

You are now saying that the architecture documentation was created for us humans.

Yes, we created it for us humans because we as humans created the architecture.

But it is important that this architecture documentation contains information that the machine also needs, in my opinion.

If we make quality-driven architecture, then the decisions we make for the software are based on the quality criteria.

And the machine can only make the decision if it knows the quality criteria.

Especially if I now go into something special.

If I say, well, this is a Linter and you already know how a Linter works, okay.

But if I now, I don't know, have the Linter for huge projects or something, then I have a different quality criterion that the machine has to know, I claim.

Yes, what I would actually like, to bring it down specifically to this performance thing, as I said, it just randomly pulled out.

What I would actually like now would be that the system tells me, okay, listen to me, performance, I don't know, I didn't look at it, it's not tested either, it's just the way it is.

And I mean, try it out, whether it's fast enough or not.

And that would actually be the information I need.

Because then I would know that it's a blind spot and that's not a guaranteed thing.

What I get is illusion.

So that's what I usually get from architecture documentation.

Any random statements that have nothing to do with reality.

So the system basically says, a Linter could just have to be fast.

That's why I wrote down how fast it could be.

It has nothing to do with the current implementation, but it looks like quality scenarios.

So I'm exaggerating now and I can add that this would be something that a human architect might have delivered, so to speak.

But that's not what it would do to me.

For me it would be more helpful, I don't know what you think, if the system would now say, I didn't look at it, period.

This solution is there, it's just an open topic.

And that's exactly what I might not get out of it.

But that would be helpful, or something like, my decisions in favor of something are based on this.

So not that I get trust, that it is more comprehensible than what the system does at all and so on.

And instead I actually get a document full of, that's probably too mean, because I didn't read it through, but I actually get a document full of fog candles.

Yes, but exactly this consideration that you are now making.

I would take you to the next point.

We already had that he should justify why he chose this quality criterion.

Yes, that will be a false justification for the time being.

But now you say, you want to know whether this is really verified or not.

That means he could write in whether it has been verified by a test.

Preferably whether the test is green or red.

Or what are the challenges of the system at the moment, or an open point or something like that, maybe, I don't know.

So that would actually be the next question, we would now imply that the system is able to draw the logical conclusion.

That can't be, can it?

I don't know.

I don't know.

So it gives the impression that it can draw the logical conclusion.

And it surprises me again and again.

I once asked how I can tell whether it is an LLM or a human.

I said, well, an LLM doesn't have a world view.

It doesn't know what the world looks like.

That means it can't use this knowledge.

I then asked, if I lock an elephant and a squirrel in a matchbox, how heavy is the matchbox?

I expected two tons of oil to come out of it.

He said, well, the elephant doesn't fit in, you won't be able to catch a squirrel, that's a joke, right?

Even if it's just a pretense.

This behavior is awesome.

But that's a bit of a problem, isn't it?

So exactly this story, that it can light candles very well and can say, it looks like that, but in reality it's just not like that.

Let's briefly, somehow, exactly, this is a very interesting discussion, let's get away from the things that were in the chat.

Marco Wessemann wrote, the interpretation of which tests and which forms are necessary, is, in my opinion, something that is currently only visible through AI.

Through a lot of code you are quickly deleted.

I take deleted and hidden.

That's exactly the point.

And that's where it starts again with controllability.

And Martin Axiomeyer wrote, if you write architectural documentation in LED, for example, GitHub Copilot, suggestions for the presentation of the time are not always correct.

And what you want, but sometimes with insufficient information.

Exactly.

I don't know what your attitude is.

I would suggest that the topic of GitHub Copilot, I don't really know exactly.

That would be the question of whether this is one of these AI tools that has been studied in this cited study.

But actually, the idea is code completion.

And being smart about what has already been used on the Internet, I don't think that's desirable.

We're talking about something else here.

In principle, we're talking about how a developer is emulated in a team.

That's what happens there.

Maybe not a team, but someone who says, I write the code and I do everything.

The documentation, the whole thing.

That's what a cross-functional technician has come up with.

However, this reference to GitHub Copilot, there's something else that comes through.

I think we will change the way we develop.

Anyone who has already found the source code of my project, will find a lot of metafiles.

That's why I asked the model, whenever a file is created, to write down what this file does.

Because that way it can get an overview quickly.

It has a list files command.

It gives the complete tree with the description of the file, so that the context is not filled in great.

Otherwise, if the context is missing, then the LLM has to guess because of the file name.

We know, in this and that file was this and that.

In this folder is this and that.

That helps.

Also with GitHub Copilot, when I first write a comment, what the function should do, then the auto-completion is much better.

I have already noticed from some developers, that they start to put a header in every file for the AI, in which there is a system prompt.

What should be in this file?

What not?

How should it be in there?

And so I think we will adapt the way we program the AI, while the AI or the manufacturers try to adapt the AI to our programming.

Yes, although I would say that the idea, that you say, I have such a strange thing, and I don't know exactly what's going on in there, but I'll describe it abstractly.

That's just modularization.

And if we get AI technicians to modularize things, by writing down what the thing should do, and that it is recognizable from the outside and not implicitly clear in the depths of the code, I don't think that's rejectable.

That was nice to say.

Absolutely.

But it's interesting to take advantage of the effort.

We talked about the design of the code and the review.

And now think about it, if the machine, it gets faster and faster, if it implements the code, the state that we have now, with what are the eight rules or so, in one hour.

So, then I want to have a review.

And how long does the person need to review this code?

I can put the machine back on it and say, do you want to do a review?

And then I build up trust somewhere.

Just like when I have a development team and I don't know at the beginning how good they are, what they can do.

And through the first results, I build up trust.

And now I'm curious which trust I can build into the machine.

And if I build up trust through the automated review, I say, actually, that's okay.

Then I run the risk that the human review will fail.

Yes, and ...

You said it yourself, I don't know when, we are in a special role that we develop software and software runs on essentially deterministic machines.

Even if it doesn't look like it sometimes.

That means we can now somehow say, okay, this piece of software does this and that is somehow objectively in an automated, from an AI, also accessible environment, so to speak, verifiable.

Which is something different than if we would say, let's build a bike.

A bike is something where I can't do these cycles.

I don't get any feedback.

And then theoretically something weird can come out.

Okay, I could still simulate that.

I think we're much closer to that.

And I'm not sure, that's a thought that's been in my head all the time, that exists in me.

We had this step back then from assembler and machine language to co-languages, where, as I said, not where this story happened.

In the old days, it was actually the case that you wrote individual zeros and ones into the memory.

So 40 or something, 50s.

Then there was somehow, you have to somehow the commands by hand, so to speak, then actually think about which ones are zeros and ones.

Then you had these assembler mnemonics to say, these machine commands, I have something there, which is more human-like, so to speak.

Then you could automatically convert these assembler mnemonics into a binary code.

And then we started to build co-languages.

And they are on a higher level of abstraction.

That means, I don't say in the extreme case, just do these things and then it might run parallel or sequentially or whatever.

There are also different execution options, especially in functional programming languages.

But otherwise, we now have more complex constructs that correspond to four machine language commands.

And we are here, maybe at a similar point, where you say, okay, I'll describe what I want to have.

Then somehow the thing comes out in the next lower language.

Just like a compiler makes assembler, we now have a thing where you say, okay, let's build a linter.

Then a linter comes out.

And you still have to specify what it does.

And that's just a higher level of abstraction, analogous to these higher programming languages.

I'm not sure if the analogy is correct, but if it is, it should be, then that would mean that this loss of control is to a certain extent, so to speak, fine.

Because, I don't look at the bytecode of a Java compiler.

You don't look at the bytecode of a C, so you don't look at the assembler code of a C compiler.

Or not in Python.

On these levels, you typically don't work anymore.

And maybe that would be something where we would get to.

The problem here is that these things are not obviously deterministic.

They are deterministic, because they run on software, on computers, of course.

But it's something else to have a compiler that is really deterministic and trivial deterministic.

Here we're talking about things that are a bit more complicated and different.

Exactly.

So the question would be, do I still want to understand these tests at all?

Do I want to do that at all?

Actually, I want to get to the point where I don't want to do that anymore.

I actually want to eliminate this distrust.

But that's just another visionary story.

At the end of the day, just briefly to this question, do I still want to understand the tests?

Do I still want to understand the code?

Is the result enough for me?

I say, we also have a problem when the cognitive performance of the machines gets better than our human cognitive performance.

And the machine generates code that is so complex that we can no longer look over it.

That's also very exciting.

And that's also something where we will need solutions in the future.

But that's blatant future music, isn't it?

And I would like to remind you again, the story that you can now look at through this paper, at least, is that if I, so stupidly put, if I give a developer support, it gets worse with her.

And that's just, so I just actually read a post-it note this morning on Mastodon, in the sense of where a person who obviously worked at the university has exactly these things with, okay, explain to me how you solved this task.

And then somehow he comes back, I don't know, you have to ask Cecil Petit.

And that's just, so trivially, difficult, isn't it?

Because that just means that I'm just delivered to the thing.

And she had at least one example, who also somehow posted that, where, as she said, a false statement came in a big way.

And then somehow she said, okay, that can't be like that.

And then somehow came back, yes, yes, here, look, there is the screenshot.

And that's just really, what impressed me so much is there is this book, the power of the computer and the power of reason by Weizenbaum, that's from the 70s.

And it describes this story of Eliza, he somehow built Eliza, this psychotic emulation, whatever you want to call it.

Actually, that's something that's relatively trivial, that somehow, so to speak, throws back questions, doesn't it?

Do you have problems with your family?

And then he comes back, somehow tell me more about your family or about your mother.

And that's a relatively simple algorithm.

I've been doing it in the 80s, 102 basic things, somehow tapping off what that does somehow.

And what he observed was that his secretary at some point started talking to this thing and said, please don't look at what I'm talking about with the thing.

That means that this secretary obviously took this system for granted and trusted things that are private.

That's exactly the problem.

What fascinates me is that 50 years ago it was exactly the same problem as we have now.

You start and say, I'm doing something with an AI system, something comes back and you take it for granted, so to speak.

But it is very questionable whether it actually builds reasonable solutions in all respects.

But that's just the way it is.

I would still ask a final question.

What is your tip?

What would be something that could be done differently today or where you would see where you can now use these things productively?

Would you recommend other people, like Dinter, to build on Chitchipiti or on the AI system?

No.

## Zukunftsausblick

We have systems like GitHub Copilot, which support and enhance our skills.

That's pretty good.

That works pretty well.

### Entwicklungspotential

What I've done now is an experiment that shows what could be in the future.

I think it's very important that we deal with it to think about how future reviews will run, for example.

How will we develop in the future?

What of the documentation is important in the future?

What is less important?

Because the machine can explain it from the code.

I think that's it.

Martin Axelmeyer wrote that an LLM does not have to be 100% error-free to be helpful.

For example, self-reflection.

Maybe you can also say that you have to be able to live with it, that this is not the case.

Maybe that's what has been going on through the hours.

This reference to this mistrust, which you may have to have.

Good.

Then I would say ...

Thank you very much.

It was fun.

I also found it super exciting.

The episode with Lars will lead to a suitable ...

Will you ... catch up at a suitable time.

That is still somehow open.

I'll look briefly into the plan ..

At six twelve we actually have Next week Process Orchestration BPMN and workflows with Bernd Rücker.

Then we are live at the IT days on December 10th.

This is Friday, Dec.

12th is a Tuesday, if I remember correctly.

It's about this question IT2034.

There we will pick up the things from the IT days.

And we still have on December 20th this KI under or overhyped with Stefan Schmidt, Andre Neubauer and us both and Lisa in moderation.

Oh, and today the trailer for the Advents calendar went live.

Where we will actually have a book tip every day in December.

So that's the next thing that happens.

You can also watch.

Exactly, then I would say thank you again.

Have a nice weekend and see you there.

Exactly, have a nice weekend.

Bye.
