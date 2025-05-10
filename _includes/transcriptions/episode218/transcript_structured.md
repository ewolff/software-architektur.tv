# Episode 218 - Vaughn Vernon about Ports and Adapters and DDD 

Herzlich Willkommen zu einem weiteren Episode von Software-Architektur im Stream, diesmal mit Warren Vernon.

Warren, möchtest du ein paar Worte über dich selbst sagen?

Sehr wenige, ja.

Es ist schön, hier zu sein, Eberhard.

Es ist schön, dich jahrelang kennenzulernen.

Du hast mich eingeladen, an der Go-to-Berlin-Konferenz auf einem Track zu sprechen, den du hattest.

Ich erinnere mich nicht genau, was der Name des Tracks war.

Aber ich wurde darüber gesprochen, Ungewissheit zu modellieren, einen domain-geführten Mindset zu nutzen, einen domain-geführten Ansatz.

Und das war Spaß.

Eigentlich ist das einer der lustigsten Reden, die ich je gegeben habe, nur weil ich in der Diskussion und in meiner Präsentation drängte, dass man das auf YouTube noch sehen kann.

Ich modelliere seit langer Zeit, und ich schreibe immer noch Software.

Ich versuche, mein fünftes Buch zu schreiben.

Das ist jetzt eine Art Herausforderung, weil ich ein Serien-Editor meiner eigenen Signature-Serie für Pierce & Addison-Wesley bin.

Das ist in sich eine große Herausforderung.

Und ich glaube, das war es.

Ich möchte nur sagen, ich hatte jemanden letztens, eigentlich ein deutscher Individuum, der mir sagte, dass mein Antrag oder etwas als Software-Ökologen nicht sinnvoll war, und dass niemand darauf achte, dass ich mich so nenne.

Und ich achte nicht darauf, ob jemand darauf achte, dass ich mich so nenne.

Aber ich denke, es ist wichtig, weil, wenn man versteht, was ein Ökologen ist, ein Ökologen sich um das System und das Ökosystem kümmert.

Und obwohl es normalerweise um den Planeten geht, um die Erde, wie wir sie behandeln, usw.

Wir haben Software-Systeme.

Und ich bin ein Software-Ökologen, weil ich mich darum kümmere, wie wir mit Software umgehen und System-Denken nutzen, um das zu tun.

Also egal, ob du das verstehst oder ob du dich kümmerst.

Ich wollte nur sagen, das ist der Grund, warum ich mich als Software-Ökologen nenne.

Und ich denke, das ist ein sehr guter Weg, sich über Software zu denken, mit System-Denken sehr wichtig zu sein und viele Dinge in Bezug zu nehmen.

Ich wollte nur erwähnen, dass du selbst ein Autor bist, also hast du das berühmte Buch »Implementing Domain-Driven Design« geschrieben und auch »Domain-Driven Design Distilled«.

Es gibt eine deutsche Übersetzung, die heißt »Domain-Driven Design Kompakt«.

Ich empfehle dieses Buch, weil es eine tolle Einladung zu »Domain-Driven Design« ist.

Selbst die deutsche Übersetzung hat nur 130 Bücher oder so.

Es ist also etwas, das einfach zu lesen ist, es beinhaltet fast alle Informationen.

Ich bin sehr dankbar dafür, dass du dieses Buch geschrieben hast.

Ich finde, es ist ein großartiges Buch.

Kann ich etwas sagen?

Es ist faszinierend für mich, dass die englische Übersetzung ca.

160 Bücher ist.

Ich habe keine Ahnung, wie es in Deutschland nicht so ist, dass es mindestens 190 Bücher sind.

In meiner Erfahrung, wenn man von englischen zu deutschen User-Interfacen lokalisiert, muss man seine UI spezifisch für Deutschformatieren, weil man die Bezeichnungen in den kleineren Bereichen der englischen Übersetzung nie aufpassen kann.

Es wäre interessant, die echte Webseite zu kennen.

Ich habe es gerade auf Amazon aufgeschaut.

Es sind 158 Bücher.

Es wurde von Carola Lilienthal und Henning Spender übersetzt.

Wir hatten sie beide auch hier auf der Show.

Was ist das Nummer 40?

Vielleicht hat es mehr Addison-Wesley-Advertisements in der Front und in der Rückseite.

Es ist 166, also die englische Übersetzung ist 166.

Vielleicht ist es eine andere Fontgröße.

Vielleicht.

Aber ich möchte auch sagen, dass Carola und Henning vielleicht schon darüber gesprochen haben, dass sie ein neues Buch geschrieben haben, das zuerst auf Deutsch ist, aber jetzt unter meiner Signatur-Serie steht, die heißt Domain-Driven Transformation.

Ja, der, der darüber spricht, wie man mit Legitimität umgeht und wie man das transformiert.

Ja, das ist ihr neuestes Buch.

Entschuldigung, weil diese Gedanken organisch aufkommen oder sie büffeln sich.

Ich überprüfe gerade Susanna Kaisers Buch.

Und sie ist auch in Hamburg, wie Carola und Henning.

Und ihr Buch bezieht sich auf Domain-Driven Design, Weltmappings und Team-Topologien, was ziemlich ein Thema ist.

Und ich habe gerade ihr letztes Manuskript erhalten, ein Manuskript, in den Kapiteln.

Ich hatte es eigentlich schon seit einer Weile, aber ich hatte dieses Backlog von Buchreviews in meiner Serie zu machen.

Und ich beginne gerade jetzt.

Und sobald ich ihre Review erledige, meine Serie-Editor-Review, werde ich Carola und Hennings neues Buch auch überprüfen.

Ja, nur einen Sekunden.

Ja.

So, I actually have a copy.

Oh, yeah.

The German version.

Yeah.

Yeah.

And there was a comment on the chat, content-encoding-compressed-German.

So maybe… What does that mean?

I don't understand.

It probably means that that book has been written in compressed German.

Oh, yeah, yeah.

Who knows?

Okay, excellent.

So much for the signature series.

I will put a link to Carola's and Hennings' book in the show notes.

And the one by Susanne is not out there yet.

I keep hearing great things about what she's doing with regards to worldly mapping and these kinds of things.

So I'm definitely sure it's going to be a great book.

So that's another great thing.

In my opinion, she, well, at least for what I have received in terms of training in worldly mapping, she explains worldly mapping better than anyone else that I've encountered.

That doesn't possibly, you know, I mean, I say that with a bit of reservation in that I haven't attended a lot of different worldly mapping trainings, but Susanne has insights into those three topics to a degree that I think are, you know, it's highly respected her insight into those, yeah.

Yeah, absolutely.

Great.

So you said that what you really want to talk about today is ports and adapters.

Well, one of the things, one of the things, yeah.

Yeah, so that's what you brought up in the conversation that we just had before.

So, well, the stage is yours.

Go ahead and tell us about ports and adapters.

Okay.

So I think that the reason that I keep returning to this subject is that for one thing, medium, I subscribe to medium and, you know, with all due respect to the platform that they have, the content that they push to me is just not very high quality in my opinion.

Sometimes I get some really insightful, you know, views of things and I even saw one that potentially could be good about domain driven design, but by and large a lot of what they push to me as you're going to be interested in this ends up being kind of, you know, I feel embarrassed for the author is how I would put it.

And, but also I feel bad for the people who read it and think that they know what they're talking about.

And for some reason the title or the name hexagonal has stuck with the pattern, with the architecture pattern better than ports and adapters has.

And okay, maybe hexagonal is, I don't know, maybe a little bit cooler name or something.

And it was the original name.

So, and even the fact that now Alistair Coburn has just yesterday announced that his ports and adapters book is available on Amazon.

So you rush over there and buy it right now.

But what you're going to see is the big title is hexagonal, which now just to explain this, literally Alistair Coburn commented on a LinkedIn post that I had about the topic.

And he asked me, please don't call it hexagonal anymore.

It's ports and adapters.

So what I think he's done with the title, it's not like that he can't make up his mind.

I just think that recognizably people are going to see hexagonal and they're going to go, Oh, I know what that is.

Whereas if he said ports and adapters, most people might say what, so sort of officially, you know, we should call it ports and adapters.

And there are certain aspects of ports and adapters that we should respect.

And to understand that while, you know, I think a lot of people might say that they knew about ports and adapters before Alistair Coburn.

Well, I'm not going to argue that one way or the other, but I would say that Alistair Coburn is the one who codified the pattern first and therefore, you know, is due credit for that and that he understands it well.

So when someone says that, you know, throws hexagonal architecture under the bus, as this is very complex, this is, you know, whatever, you know, it's, it doesn't make any sense.

It's wrong.

It's, you don't need it.

And all these things, well, you may not need it under certain circumstances, but if you're working in a complex domain, it sure makes sense to me.

And I think it makes sense to a lot of people.

Yeah.

So can you tell us what ports and adapters or hexagonal, whatever you want to call it, or you might call it what that actually is?

Yes.

So what I want to do first is do a little, a simple little share screen here.

And I'll start out by showing the layers architecture.

And I think pretty much everybody knows about the layers architecture.

This I refer to the strict layers architecture.

There's also relaxed layers.

I'll explain the difference between the two, but they're basically layers.

So you would think of in a, in a very simple web application or a simple architecture for a web based application that you would have the user interface at the top, right?

This is where requests come in.

And when the user interface receives a request, it dispatches, you know, some translation of the incoming requests is something that the application services can understand.

And if you use a domain model in your architecture and not, and when I say domain model, I mean a rich domain model that has behavior.

I don't mean an anemic model or a data model, right?

Which some people call domain model, but it's really not.

So a rich domain model, then you would have another layer under application services.

And then you would have at the bottom, what is typically known as infrastructure or whatever.

You know, I think that Eric even used these layers in his blue book, I think early on, maybe pages, I don't know, 70, 80, somewhere in there.

I don't know why you might remember that he does show just a layers architecture.

And this is, I think similar to the names that, that he used.

Well, one of the problems with the layers architecture in general is that you often have interfaces that are declared in a domain model or even in higher layers, but need to be implemented in the infrastructure.

Technically speaking, they should not, at least in the domain model, there should not be like this technical kind of influence in the model.

And so if you are viewing layers architecture in the way that it should, as you can see there, this little label says that, okay, the IMPL class, right?

Not that even I would use the name IMPL, but everybody seems to understand that.

So the IMPL class of the interface that's in the domain model is pointing in the wrong direction.

It is dependent.

This makes the infrastructure dependent on the domain model, which is one level higher.

And I, I think I use this very same example or something like this in my red book, the, the implementing domain driven design book.

So this is not like I'm saying something earth shattering, but just to make, you know, the presentation clear.

I would like to repeat that.

And by the way, it could be a repository interface or it could be a technical implementation of a domain service.

And the reason for a technical, technical implementation of a domain service is because you probably want, to use it.

You may use a domain service as an anti-corruption layer.

So you want it to look like part of the model, but because it has some heavy lifting, it's going to be implemented, at least the technical parts of it are going to be implemented in the infrastructure.

Okay.

So I hope this makes sense as a setting.

The only difference between strict layers and relaxed layers is that with relaxed layers, any higher level layer can depend on any lower level layer.

Whereas in strict layers, any higher level layer must depend only on the layer directly below it.

And you can read about that in the POSA one book or patterns of software architecture.

Yeah.

Which is Frank Bush or Frank Bushman.

Yeah.

Bushman and I'm sorry, I forget the other authors, but I've met Frank.

So, yeah.

Okay.

So here we are.

And what do we do about this?

Well, okay.

In my red book, I explain that first of all, you can simply switch to the, to using the dependency inversion principle of solid.

Okay.

I'm not judging solid here or anything, but dependency inversion principle, I think is an important way of viewing architecture, which basically means that you take the infrastructure layer and you move it to the top.

And now the infrastructure layer can depend on interfaces that are, you know, declared below it, right.

Defined below the infrastructure.

And that is just the basics of dependency inversion principle.

Now, after you have that mindset, and let me show you just how super complex ports and adapters is, right.

This is the colossally complex ports and adapters architecture, AKA hexagonal.

And as you can see, it's really not colossally complex.

I think that what's happened is that hexagonal reports and adapters has been seen as a kind of catchall for various technologies, such as I was told actually that in a certain region or country in Europe, I won't name any names in English, but it's a Spania, you know, in a certain language and that they have sort of said, well, I won't even say ports and adapters because they only refer to it as hexagonal.

Or the one, the people that I've come in contact with about this topic.

And they've conflated this very simple concept to mean that you have to support Kafka.

You have to support Docker.

You have to support Kubernetes.

You have to support streaming.

You have to support, you know, like just, it's become this kind of like catchall of like a technology bucket.

When in fact technology should be at the, if you will, just for one second, I just want to say the outside layer or the top layer.

If you were viewing this from the dependency inversion principle in a layers architecture, that is the difference that primarily ports and adapters introduces.

It says there's an outside and an inside.

And Alistair Coburn also asked that I not use the term layer when referring to the ports and adapters architecture.

You can go to the LinkedIn post where he comments on that.

I don't know.

It may have been six months ago now.

He actually thanked me in the midst of all the controversy and everybody's, you know, flame wars and everything going on about how, you know, nobody needs hexagonal architecture and so forth.

But he thanked me for writing such a clear post about the real meaning of the architecture pattern.

So this is it.

You have an outside.

So I'm not going to refer to errors from this point forward.

You have an outside and you have an inside.

On the outside are your adapters.

Okay.

Let's say that you have a browser on the left-hand side and this browser, a user using a browser, obviously makes a request to this service or application, whatever, however you'd like to refer to it.

But there's a way to handle that request.

So let's say that the browser uses rest of course, or some form of restful, right?

And it, so it makes this request say it's a post request.

So you're going to have a controller or what some people like now to refer to as endpoint, because somehow that, you know, is better than saying controller.

I don't know, but anyway, I'll just say controller or endpoint or even a message listener.

So there is some kind of adapter that is sitting there and it is receiving stimuli from the outside, right?

And this, by the way, on the left-hand side is known as the driver side.

And as you can see, if there's a user at a browser, they are driving the application to do something, right?

So you've got this, let's just think of controller.

We have a controller sitting there.

I think everybody sort of is familiar with MVC, although I think, you know, model view controller, although I think that's not a popular thing to say anymore, MVC, but anyway, we have a controller.

If you really need to call it an endpoint, call it an endpoint.

So request comes in.

We have a handler of that request and that is the adapter.

What is the job of the adapter?

It is to take that post request that is in HTTP format, right?

It's got a method, you know, it has like a version number, a method name, and a URL associated with it.

It may have some number of headers, probably will.

And for a post, it's going to most likely need some kind of a entity body, you know, that is the data that's being, you know, the formal application data that's being carried.

And that may be in the form of a JSON object or XML.

I hate to say the word XML, but whatever format you've chosen, it could be a proto buffer, right?

It could be whatever, but you've got this payload in that request.

Okay.

Are we going to give that, all of that to the application on the inside and say, here, deal with it?

No, we're going to adapt that.

We're going to adapt that request to something that is suitable for a well-designed interface on the inside.

And Alistair Coburn refers to this as the port.

And I would like to hear confess an error that I made in my red book.

I literally, when I read Alistair Coburn's post, the original post on hexagonal architecture, I thought that he was referring to the port as what was on the inside and that essentially the port was the incoming thing, the port that actually takes in a request or a notification or whatever it is.

And the adapter is used along with the port to adapt to the inside.

But in fact, I was wrong about that.

So, and later Alistair, you know, sort of maybe tongue in cheek helped me to understand that.

So, and now I have the proper, you know, perspective on that, but you'll see this error still in the red book.

Now, over this, I will say that it doesn't change anything about the presentation of the pattern.

I do present it properly.

It just changes where I point when I say port, right?

So before I pointed at the outside, and in fact, the port is on the inside.

And I think that a lot of people didn't really understand this well until he gave a presentation sometime after my book was published, maybe a year or two in Paris.

And there was a, you know, there, there's a video on YouTube that where he goes through this.

And so I didn't even know about the, this video for a number of years, but he there kind of clears up the, you know, the confusion, the confusion.

Okay.

So anyway, you've got this incoming request.

You translate the request payload and whatever headers influence might mean.

And you, and you understand, okay, this URL points to some resource that is represented on the inside by something.

And we're going to pass that.

We're going to call an application service and pass that translated or adapted information as.

Argumente, Parameter für den Applications-Service.

Und das kann in verschiedenen Art und Weise gemacht werden.

Man könnte es in ein Kommando-Objekt einbauen, ein Payload auf seiner eigenen Seite, und das übernehmen, oder es auf ein kleiner Bus oder nur ein internes Messaging-System einbauen, sodass man die Synchronität vielleicht auf der Port-Level hervorhebt.

Okay, jetzt hat der Port Kontrolle.

Was wird es tun?

Nun, sagen wir, dass es eine gewisse Persistenz-Daten hat.

Oh, es ist ein Post, also ist das etwas, das noch nicht existiert, im Database.

Und so, was wir tun werden, ist, dass wir eine neue Entität erstellen.

Und diese neue Entität hat ein paar Daten auf ihr.

Und in diesem Fall werden wir einfach einen Repository nutzen, um diese neue Entität dem Database anzunehmen.

Das ist ein anderer Adapter.

Also ist eine Repository-Implementation der Adapter.

Also, wenn wir kurz zurückkehren zur Infrastruktur, hier unten, das ist diese Implementation hier.

Und sagen wir einfach, dass die Interface, die hier definiert wird, in dem Domain-Modell, eine Repository-Interface ist.

Okay, also wenn der Port die Repository-Interface nutzt, die es ohne Zweifel hier hat, sagen wir, sie als Teil ihrer Konstruktion handelt, also benutzt man das Framework, das neu genannt wird.

Und wenn man, weißt du, die Applikations-Service erstellt, handelt man sie dem Repository an.

Wie macht man das?

Nun, man kann das tun, weil der Außenbereich diese Instanz hat.

Und es kann, wenn es den Port erstellt, welcher ein Singleton sein kann, handelt es sich um die Objektreferenz, was die Implementation der Interface ist, aber der Innenbereich weiß nur über die Interface, aber der Außenbereich weiß, oh, es ist eine Instanz dieser Implementation hier.

Also, wir, weißt du, save oder was auch immer, die Entität an den Repository addieren, und der Repository macht all das Persistente, was wir brauchen, und setzt es in den Database ein.

Und was ich hier versuchen, zu sagen, ist, das ist das superkomplexe, niemand braucht, das, weißt du, Ports und Adapters-Architektur.

Das ist es, da drüben, das ist das ganze, wie wir es auf Englisch sagen, Kit and Caboodle.

Das ist es, okay?

Und ich werde dir das nächste zeigen, und ich weiß, ich glaube, Eberhard will etwas sagen.

Lass mich nur aufklären, wo ist mein kleines Pfeil?

Oh, vielleicht muss ich es tun.

Okay, lasst uns ein Domain-Modell zum Innenbereich einbauen.

Also, der Port ist immer noch auf dem Innenbereich, aber wir separen die Applikations-Service vom Domain-Modell, und jetzt ist die Applikations-Service nicht, sagen wir mal, ein Transaktions-Skript, was wir wahrscheinlich, sagen wir mal hier, dass, wenn wir nichts anderes sehen, als was hier ist, vielleicht haben wir eine Art Transaktions-Skript, oder es populiert ein anämisches Datamodell-Objekt und verhält es sich.

Aber hier haben wir eigentlich ein Domain-Modell, und trotzdem wird der Port mit Parametern zu einer Method-Invokation auf dem Port, der Applikations-Service, und der Port wird den Repository benutzen, und sagen wir mal, in diesem Fall, dass wir einen existenten Bestandteil im Database haben, so wird der Port zuerst den Bestandteil durch den Repository lesen, und es wird das Modell-Objekt zurückbekommen, das Bestandteil, und dann wird es das Modell-Objekt sagen, etwas zu tun, mit einem richen Behaupten, aber keine Bestandteile oder Attribute auf dem Objekt, individuell auf seinem eigenen, auf der Seite des Users, stattdessen sagt es, Modell, mach das, und dann nimmt das Modell sich um, was es auf seinem eigenen Bestandteil setzen muss, und dann benutzt der Port den Repository, um es zurückzulegen.

Wiederum, das ist die super-wichtige super-komplexe, verrückte, schwierige Ports und Adapter, oder hexagonale Architektur, das ist es, das ist es, okay, und ich weiß, dass du etwas sagen möchtest, Eberhard, also geht's weiter.

Ja, also, ich denke, dass der interessante Punkt, den du machst, ist, dass nach allem es nicht so anders ist, oder in Bezug auf Komplexität ist es nicht so anders von Teilen, aber es hat einige Vorteile, wie du gesagt hast, du hast jetzt eine gemeinsame Abstraktion für sowohl die UI-Stuffe wie die Infrastruktur-Stuffe, es wurde grundsätzlich eine in einer Art, und eine Sache, ich weiß nicht, ob du darauf zustimmst, aber ich denke, einer der größten Vorteile ist einfacher Teststabilität, weil du jetzt die Verbindungen zu etwas machen kannst, während des Tests.

Und das ist einer der wichtigsten Punkte, den ich denke, ist in der ursprünglichen Blog-Post.

Jetzt hat Alistair Coburn seine Blog-Seite oder seine, ich denke, es heißt alistair Coburn Coburn.com oder etwas und jedenfalls hat es einen neueren Blick und Gefühl zu dem, als der ältere ist.

Aber ich denke, der Inhalt der Blog-Post ist immer noch dasselbe.

Also, du kannst da hin und was du in einigen Kommentaren sehen wirst, und ich denke, dass Robert C.

Martin ein paar Kommentare und andere gemacht hat, aber ja, Teststabilität ist eine sehr wichtige Teile von diesem.

Du kannst jede einzelne Teile der Architektur den Außen- und Innen- und sogar separaten Teile des Innern, wie das Port oder Applications- Services und das Domain- Modell.

Du kannst all das in Isolation testen, richtig?

Und du kannst deine Mocks oder Fakes für den Port benutzen, um zu testen, dass es tatsächlich die Domain- Modelle mit einem In-Memory- Repositorium hält, aber jetzt machst du sicher, dass der Nutzen funktioniert korrekt, und dann, natürlich, wirst du einige Integration- Tests haben, die testen, dass die Repositorien gegen den Database funktionieren, und so weiter.

Also, ja, aber wiederum, es ist nur ein einfaches Modell, und wenn du möchtest, wenn Leute sagen, wir brauchen keine Domain- Modelle, okay, na, hier geht es, richtig?

Du brauchst keine Domain- Modelle, das ist in Ordnung, wenn du keine Domain- Modelle brauchst, vielleicht dein Transaktions- Skript oder ein In-Memory- Modell ist das Beste, um in irgendeinem Fall zu benutzen, das ist in Ordnung, aber das macht es noch einfacher, um diese Architektur zu benutzen.

Kannst du ein Transaktions- Skript erklären, weil ich nicht sicher bin, ob jeder das kennt, und ich denke, es ist sehr wichtig, dass es einfache Alternativen gibt, für einfache Probleme, also sind nicht alle Ports und Adapters, Layers oder Domain- gegebene Design, wenn du ein einfaches Problem hast, dann solltest du wahrscheinlich an einfachen Tools stecken, um das einfache Problem zu lösen.

Ja, also in Martin Fowler's Patterns of Enterprise Application Architecture, right, this classic book, that is now at least 20 years old, maybe more than 20 years old, and still, like, probably the best seller under its category is probably, like, if you look at Amazon, it's probably, if it's not number one, it's probably number two, it's probably number three, it's probably number four, it's probably number five, it's probably it's not number one, it's probably two or three or something, but it's often number one in its category, still, after so many years, well, he discusses three major patterns that I would say are application patterns that introduce some architecture specifics.

One of those was transaction script, or is transaction script.

And a transaction script is basically just kind of the way it sounds, you start a transaction in your application service method that could even be using an annotation, or if you're using .NET, an attribute, right, square bracket attribute that says, okay, when I enter this method, I have a, what is it, point cut that, you know, starts a transaction when I fall off the end of the of the method, right, or return from it, whatever you are returning, I'm going to commit that transaction.

And if the user, if there's a problem and the programmer, or the method throws an exception, then I'm going to roll back that, right?

So, so you don't even need to have a, you know, coded, you know, begin, you know, transaction.begin or session.begin, whatever it is, and session.commit or connection.commit, whatever it is.

But in essence, in between where the transaction begins and where the transaction ends, all that you're doing is, in essence, building SQL query that is going to be used to insert or update a record, a row in a database.

And, yeah, okay, maybe it's more than one row or whatever, but that doesn't matter.

It's just, right?

Let's just think in terms of this is a simple entity, and we're just going to pop it into the database using an insert, or we're going to update it using a SQL update expression, and boom, that is it.

So if you're using JDBC, you would use a JDBC connection in its simplest form.

If you are using .NET, you know, like C-Sharp, you're probably using ADO in this case, right?

I think that's the correct one to say, ADO, or something like that.

You could also use Hibernate or JPA, whatever you like to refer to it these days, and you could use oh, Entity Framework or whatever, but that's not really the initial idea of transaction script.

You are literally just using simple SQL expressions or statements to interact with the database directly.

That is transaction script.

And I find it interesting, I mean, because you wrote all the books about DDD, and that you mentioned that pattern, which is actually quite old, and, you know, is one of the tools that you sort of recommend for specific challenges.

So, yeah, I think that's great.

I agree totally.

And for what it's worth, most patterns are really old.

And there are patterns that are way older than Martin's patterns, but, you know, like that's the whole point of patterns, right?

You just keep using them in different ways.

And it's really sad that for some reason, the newer, I don't know if you want to refer to this as generation of software developers or engineers have kind of thrown out patterns as, yeah, another thing that isn't useful, too complex, don't make sense, whatever they've categorized those.

It's really sad, because what they're going to do is they're just going to learn after they make a bunch of mistakes that, oh, yeah, well, let me invent something that solves that.

And all of a sudden, they've got these patterns, probably that have different names and maybe not even called patterns, because of course they can't use patterns, but they have recipes or they have, you know, whatever it is that they're going to name those.

And probably by now already are, because this movement sort of started as I saw it, maybe three, four years ago.

Seems like around pandemic time, when everybody was going kind of crazy during the early days of the pandemic.

So maybe that was just part of the crazy that was going on.

But anyway, yep, pretty simple stuff.

Yeah.

So, shall we switch subjects?

Well, one more thing, and this is where, this is where, this is probably where people's mind, you know, says, is going to say, oh, that's complex.

Okay, what I'm going to do now is I'm just going to go from this really simple concept to just introducing more kinds of adapters.

Okay.

And because I'm going to introduce more kinds of adapters, does not mean that you need all of these adapters.

But with this particular diagram, this presentation that I will transition to next, oh, that's why I shouldn't use hexagonal.

That's why it, no, it's just, right, like, this is not born in one day.

It's not born in one hour, right?

This is just simply saying, okay, at the driver's side, I have a browser.

At the driver's side, I may have a mobile app too.

At the driver's side, I may have some kind of messaging mechanism, such as Kafka, but doesn't have to be Kafka.

Could be RabbitMQ, could be AWS, SNS, SQS, could be Azure Message Bus.

It could be, just keep listing other kinds of messaging mechanisms.

And it's delivering notifications to us.

And in this case, it happens to be domain events.

And we may just have another bounded context or some kind of service or whatever it happens to be making command requests directly to our bounded context.

And what I, so what I have here are four different kinds of adapters, right?

Because we have four different kinds of incoming driver stimuli, right?

Happening.

But notice, notice, and this is a real strength of the ports and adapters architecture.

We don't have four different ports or two times four different ports, right?

Which you could imagine, well, we need a different application service for browser users.

And we need a different application service for mobile users.

And we need a different application service for incoming domain events or other kinds of notifications.

And when some bounded context makes a request, we're going to need yet another kind of port for that.

And so we have two ports here, which really doubles, right?

Or quadruples.

So we have eight, now eight different ports.

No, that's the whole point of the adapter.

The adapter adapts to whatever the port says is available as a behavior, right?

An action of some kind in the application service layer.

And now the same domain model that is used to handle the browser is also used to handle the mobile, the Kafka, you know, the messaging, the gRPC or REST request incoming, right?

Using an open host service.

There it is.

And then on the outside, well, we have, we're using CQRS in this case.

So we have a projection adapter.

This projection adapter is projecting domain events and maybe even full states of entities as views into a query model or as CQRS people, for some reason, like to call it the read model that you query on.

I love that.

You have a Postgres repository adapter.

It doesn't have to have the word adapter on it.

It's just some kind of Postgres repository.

As you can see, because it is, you know, positioned in a higher outside area of the architecture, it can have a dependency on the interface declared in the domain model.

And the same with this anti-corruption layer implemented in gRPC in this case, right, is implements the domain service interface that's here.

And then we have other entities, which you can call aggregates if you like.

And in some cases, your domain service will not have a technical implementation.

It's just business logic that happens to do some work that then is going to be, but, you know, then an entity is going to be used to with rich behavior to do something about what the domain service did at a higher level.

Maybe this is the some kind of a policy or anyway, whatever it happens to be, the I don't know.

Forgot, I've just dropped the word, but anyway, sorry.

But yeah, so then we have these sort of equal kinds of implementations of adapters on the outside.

This is a Kafka adapter that is putting domain events on a Kafka topic, right, and so forth.

So, you know, it's just the same pattern over and over and over again.

So whatever you see here and whatever you see here is just repeated.

And you may or may not need this many different kinds of adapters on either side of this.

Actually, it's easier because there is one part that is, as you said, implemented by multiple or is implemented or used by multiple adapters.

Yes.

So therefore it makes a lot of sense and is conceptually at least easier.

And yeah, also the question again is what the alternative might be, right?

Yeah.

So what I would ask is, if you're, if you see, you know, whether you're watching it now or whether you see it later, please, like, help Eberhardt to distribute this globally, everywhere, pollute the entire planet with this beautiful ecosystem, right?

Right?

Ah, okay.

I'm an software ecologist.

This is starting to make sense now, right?

We have to clean up the planet of all this misconception about hexagonal architecture and ports and adapters and champion this.

It's simple.

Yeah, and try it.

And we need to try to actually really understand what the patterns are and what the sort of foundations of our crafts are.

And I couldn't agree more.

And so there is one comment on YouTube by Ein Realist, and he said, frameworks and libraries encapsulate patterns nowadays, and devs might not recognize that they use one.

Let's say that, read that again.

The first part, at least.

Frameworks and libraries encapsulate patterns nowadays.

And therefore, developers might not even recognize that they are using a specific pattern.

Because it's just, you know, it's the way that framework does it.

Well, and I have to say something.

At the original DDD summit that Eric held in Portland, Maine, back in 2011, the very first one, there were, I think, there were three total, 2012 and 2013.

I actually said something that got Eric's attention, you know, because usually things I would say, Eric would just sort of like look at me strangely, and we'll talk about his genius later.

But anyway, I made the statement because the topic came up on hexagonal architecture, which I think maybe at the time had already, I don't know if it had already been renamed to ports and adapters, but I said something like, probably most, every team or project uses hexagonal architecture, but they don't know it, right?

And Eric said, can you say that again?

It's burned into my brain because I actually said something that Eric thought was at least interesting, if not useful.

So, yeah.

So what is your take?

So is that really something that you see out there that people are using a framework and therefore they are using some pattern that they don't even recognize?

I mean, with ports and adapters, I wouldn't know, I'm not sure whether there is a framework that has that problem.

Well, okay.

So use dependency injection, right, if you will, and that's taken all kinds of forms.

But in essence, okay, how do you get, how do you make this port have a reference to a repository, for example?

How do you do that?

Well, you call its constructor.

In the outside, you have something that is sort of bootstrapping the inside for operations.

First of all, it bootstraps itself, the outside that, you know, instances of various adapters have to be instantiated.

And then you call a constructor.

And if you happen to use an annotation to call the port constructor with the repository implementation instance, boom, it gets injected, right, via the constructor.

I really just dislike the whole, you know, I just don't like when we use a constructor and when I even call the word, you know, I use the new keyword and I say something equals new, something with parameters, that that is now become known as dependency injection, because I pass parameters to a constructor.

That's only happened because of inversion of control containers.

And I think, and I just think it's kind of sad because again, it's just semantic diffusion.

You're just using a constructor.

So, but anyway, yeah, if you need to think about it in that way, because it makes sense to you, okay, but that's what you do.

Use, okay, dependency injection.

And it could be that you're actually using Spring or, oh, whatever, what is it, structure map or whatever the new thing is on .NET that does that, which I don't really use those anymore, because again, like my friend and sort of colleague, Niklas Hedman in Sweden says, the most underutilized framework on earth is public static void main.

And I love it because it's so true.

I mean, really, most of these things are just so simple.

Like, I don't know why anyone really needs those kinds of annotations, but yeah, they do seem to.

Okay.

So, if I understand correctly, what you're saying is that to build up that relation between ports and adapters, you could use dependency injection, which actually means that, you know, you would call a constructor.

So there is not even the need for a framework.

But the original question was, frameworks and libraries encapsulate patterns so that people wouldn't understand the patterns and wouldn't recognize that they are there.

So, if you do it the way that you...

Sorry, go ahead.

Well, I wouldn't say that Spring encapsulates the ports and adapters architecture.

I would say that it enables it in ways that Programmers don't have to think about that they're doing it.

They may not even realize it.

Like I said back in 2011, most people are using hexagonal architecture and they don't know that they're using it.

Okay, so what you're saying is, if I do sensible software development or software architecture, then I will probably end up with a structure that is essentially hexagonal architecture.

Something like that.

It might really truly be more like layers and things just get injected and maybe some don't mind that somehow or another the domain model has or the application service has something injected from a lower level layer.

You know, like technically you shouldn't do that or you're really not using the layers architecture, but whatever.

That could easily happen.

So I wouldn't necessarily say that it is with the adapters just because you're using dependency injection, but it's very likely that it could be.

Yeah, even though you could.

Sorry.

I'm Wassertrinken.

I get to throw out my very minimal German every now and then.

Your German is not that bad after all, I would say.

So what you're saying, I mean, you could also do layering using dependency injection and I've done that.

So I guess the answer to the question is that these kinds of patterns are probably not hidden by frameworks.

And I think the other stance that you give concerning frameworks is that to implement any pattern like domain-driven design or so there is not really a need for a framework.

Is that what you say?

I mean, I think there are some frameworks that claim that they do support DDD.

So at least.

So do you think that or CQS or whatever, like event sourcing.

So what do you think, is that something that makes sense or is it rather something that you think doesn't really make a lot of sense and doesn't really add a lot of value?

Well, I think, okay, so maybe the question actually meant, for example, that Spring provides, I think, some kind of abstract base class or something for the repository, right, a repository.

I think so.

But the problem with that is I think that the interface that is provided takes a very crud approach.

So it's going to be like create.

So this means that your repository actually creates the entity a la JPA, right, that's going to be inserted into the database using JPA instead of the domain model creating that entity and then giving that entity to the repository.

So just be careful that just because something is named repository doesn't mean that it follows a driven design approach of repository.

Now that said, okay, I talk about repository because it's part of the tactical patterns within DDD, but you don't have to use the repository pattern to use domain-driven design.

You certainly could use other patterns.

I used a pattern that I called, oh, it was just object store because I just like thinking of an object database.

And, you know, abstractly the object store was an object database, but underneath you were just using a relational database like everybody did 15 years ago.

But, you know, and Udi Dahan doesn't, or I don't know if he still doesn't, but he at one point didn't like the repository pattern, and he would use, I think he would just use like, I don't even remember, but in other words, he didn't necessarily use the repository pattern.

At least, again, this was probably 10, 12 years ago, so maybe he does something differently now.

But you don't have to use the repository pattern.

But if you are using a repository pattern, I would suggest that you look into using a domain-driven tactical pattern view of a repository rather than a CRUD, what is it, data access object or whatever.

I don't even remember the terminology exactly, but where, in essence, the repository has business logic in it.

Right.

Okay.

That makes some sense.

So Einrede, who asked the question, or gave the comment concerning frameworks and averages, said a few minutes ago, Vaughn described it better, so that was good.

There is one other question by Udi L., or comment, and he said, what I'm missing on that diagram, so the one that we are seeing right now, are the application services.

They're right here.

So actually, sorry, inside, the big word inside, if you look here, application layer, the ports are the application services.

Okay, I see.

In this case.

And in a case like this, the application service is the only thing there, in essence, and it is maybe using transaction script.

Okay.

And he continues and said, but especially these are often a point of confusion within my dev team.

But then I think we answered that question.

Read my red book.

Please just remember that I point in the wrong place for port at that time, but I still have application service right there.

But, yeah, this is what you need to know.

And Astrid Zawadzki on Twitch said, so sort of translated my comment to you, because she said, not that bad.

It's a German high praise, and I agree.

I'm actually from northern Germany, and that's even more than a high praise if you come from that part of the country.

So I was trying to say that your German is very good, actually.

So that was what I wanted to say.

Danke.

I'm afraid we are even a little bit over time already.

Oh.

Well, I wanted to talk about – well, it's up to you, but you have Abendessen maybe or something.

So what did you want to talk about?

I wanted to talk about AI.

We had that little discussion before this stream, and I just wanted to say a few things about AI.

Or maybe you'd like to reserve that for a later conversation with a certain special genius.

Yeah, I mean, we can totally spend like five or ten minutes on that.

Okay.

So if there's anything that you want to say about it, I think that makes a lot of sense.

Okay.

So actually I don't have initially, you know, at least the way I'm going to start out this, I don't have a lot of complementary things about the current state of AI.

What I will say is that, for example, chat GPT is very good at some things, right?

And I think the conversation that we had prior to this stream – Sorry, can you stop the screen share?

I think that would be a good idea.

Oh, yeah, yeah, yeah.

Yeah, sorry about that.

Yeah, so let me see here.

Yeah, so I think you said it very well that chat GPT seems to be designed to impress humans, right?

I mean, that to me was like a striking statement because, yeah, it really impresses humans, except for the humans who are trying to do something complex with it and they find out later that it was a complete hallucination and complete nonsense, but was plausibly remarkably amazing, right?

It's just like you read this outcome.

For example, okay, I need some marketing material for my website.

I type up something, you know, I type up a paragraph and we need something very striking and maybe we need it to have a corporate sound or maybe we want to have a hip sound or maybe, you know, whatever flavor to it.

And we go to chat GPT and we say, okay, give me three different renditions of this paragraph in corporate speak, right, whatever you say to it.

You're prompt.

And it returns, you know, like some really good answers to that paragraph.

And it's like, okay, now you just choose the one that you like best or maybe you ask for a few more, whatever.

I don't like too many options.

Just give me the three best that you have.

Okay, that's impressive.

Or go to chat GPT and ask it what domain driven design is.

I think you'll be impressed that it understands at least, you know, the high level definition of domain driven design relatively good, relatively well.

But I go to chat GPT and I say, okay, I, you know, and my thought process is I've been searching for, and this is for the current book that I'm working on, which is implementing strategic monoliths and microservices, a follow on book for strategic monoliths and microservices that was published in 2021.

I'm looking for an example of calculating risk and calculating rate for automobile insurance, right?

I need to model this in an accurate way.

And so I scour the internet and I find here, and there, you know, like some things, but I really don't find a suitable, simple algorithm, not even simple, right?

I mean, simple in that I can read it, understand it.

I don't find any, I really don't find anything useful.

And by the way, if anybody finds anything really, truly useful, that's understandable, contact me and let me know.

So I finally say, and I had sort of sworn to myself, I will not use chat GPT until, you know, whatever.

And I said, okay, I give up.

I'm going to ask chat GPT.

So I start out with one simple prompt, you know, provide an algorithm that calculates risk and rate for auto insurance.

Boom.

And I'm reading this and I go, wow, this is amazing, right?

But the first question that I asked myself is, how can it possibly know that?

If Google can't show me that over like months and months of trying to find every different angle to search for this.

And I can't find it.

Google can't find it because Google can't find it.

And yet chat GPT knows, right?

GPT three, maybe or four at the time.

I don't remember.

Knows it.

And I say, well, okay, I'm going to say that, you know, they have a, you know, some kind of access into a defunct insurance company, something or another, right?

Whatever.

And they know this because they've gotten the information.

And then I prompt, you know, another prompt and then another prompt.

And it just keeps impressing me.

It's just like, so plausibly, not only believable, but amazing.

Right.

And I, and I'm like, wow, I hit this gold mine.

I say, you know what I'm going to do is I'm going to now contact an author in my signature series, Joe Emison, because he is co-founder and CTO of an insurance company.

And in fact, they have some really cool, you know, it's called branch insurance.

Um, uh, you can find it online.

I'm sure.

And I brag about Joe and his insurance company a lot because they're doing really cool things.

I won't explain it now, but I go, I, I forward this information to Joe and I say, look at what I found through chat GBT.

And I don't think it took him 30 minutes to reply.

And he said, throw out that trash.

And I'm, I'm using trash as, you know, a fill in the, well, a replacement for what he really said.

And he said, that's not, that has nothing to do with anything.

It was just, you know, in the nicest terms possible, it was just a complete hallucination.

Right.

And, but it was impressive.

And that to me is the danger of AI right now is we think that it can help you do things that it really probably is not safe to conclude that it can't.

Help you with.

And you may not know that because you don't already know the answers and you don't know anyone who does know the answers.

And I just want to say that in the United States, there are at least two lawyers who submitted cases to trials, right to the judge and use chat GBT.

And the cases that they submitted were complete.

They did not exist.

There was no history.

And I heard that one of the lawyers at least got disbarred.

I don't know if that's true, but I do know in my own searches, I found that they both had to actually face trial themselves before, you know, like the, the, the legal bar board, whatever that's called the legal board.

And, and, and I think they were at least fined heavily for it.

So be careful, right?

You could be dealing with financial thing, you know, like I was with insurance, even if it's just for a book, try to make sure it's accurate.

Or you might be dealing with someone's life, right?

Be very careful with this stuff.

Yeah.

And I would like to second that, however, and there was a comment on the chat.

So I'm realistic as such.

Narrative AI just remixes the learning set and mimics intelligence to someone who does not know how models work.

Function of the training set is the ceiling of what the model can respond to.

And continues to say there is not the intuition that is required to make an intelligent.

Having said that, I would argue that, as you said, I mean, for specific things like modifying text, it's very useful and it does things that I never thought would be possible.

So I'm still impressed.

But I think being careful is a good point and in particular because it really seems to be optimized.

I have the impression that there was some kind of, what do you want to call it, like user tests or so, where people would judge the responses by GPT and it was optimized for being, for giving the impression that it knows stuff.

And for example, it prints, I mean, if I just ask it about DDD and actually the answer isn't that bad, but it's also quite long.

So one of the things that it does is it just provides lots and lots of stuff.

It doesn't provide like one sentence.

It provides lots of stuff because that convinces you that it's more useful.

And we had that episode where we would have GPT try to create an architecture.

And eventually we found out that the original requirement and document wasn't really taken into account for coming up with the answers to our questions.

Because there is just so much stuff that it can have in mind.

Still, the answers were nice to read and seemed like they are not that bad.

Oh, it's pleasant.

It's, you know, like when you read it, you just, you wish it was true.

You just wish it was true.

Exactly.

So, and therefore, I think being, and we, that episode was probably educational because it showed how easy it is to be deceived.

Yeah, excuse me.

I don't know.

Yeah.

And I will add, because we also talked about this before the stream, that Eric Evans gave the keynote at ExploreDDD in Denver in the US a few months ago.

And his keynote was entitled basically LLMs and DDD, right?

And just a few things that Eric mentioned is that he's using, he is now in whatever work he's doing, he's about full time on this LLMs with DDD.

So he's, you know, R&D, I think mostly a lot of R.

And he's using ChatGBT and he's using Minstrel.

So Minstrel.ai.

He suggests using RAG.

I'm not going to try to remember what that means, but I do know that it's a simple way of, you know, it's a lot lower cost way of solving problems using intelligent models, but without breaking the bank, right?

Or breaking the global ecosystem with power.

And he's also looking, I don't know, I don't know if this was his note or not, but I've also heard that Claude from Anthropic is actually way better.

So I'm just, I think that was my own note, maybe from a conversation that I had at ExploreDDD.

So Eric's got a very interesting viewpoint on this.

He's not, he's not at all betting on it, as it were, that AI is going to solve problems with DDD, but he's intensely interested in knowing whether it will and what the strengths and weaknesses are right now.

And so he's putting a lot into this and he's challenged the DDD, you know, overall community, so to speak, that to look into this and say, yeah, I'd like to explore this too.

And maybe by the next ExploreDDD in Denver, whenever Paul Rayner is going to hold that, maybe we'll have some more answers by then.

And some of the answers may be really, you know, promising and some of the, or some of the answers might be discouraging.

We don't know yet, but if you have a chance to do some exploration in that area, it would be good to, to know about it.

And what did I want to say?

I guess I'll just stop there.

I think that was a good inspiration to, you know, do some work there and try to figure out what you can do with AI.

So I think that's perfect.

Oh, I know what it was.

I'm sorry.

I know what it was.

The ExploreDDD keynote by Eric is on YouTube, so you can find it.

So just look for ExploreDDD 2024.

I think you're going to provide the link maybe or something.

Yeah.

I wrote down quite a few things that I need to find on the web to put the links in, in the show notes that was among that.

So Renato Ivancic, I do apologize if I mispronounced that name, said on the chat, in my everyday life, I found it helpful when GPT-Copilot predicted configuration properties in an application configuration file, or when it autocompletes part of sentences when I write readme files.

But those are understandable, right?

I mean, how many configuration files of various kinds are there on GitHub?

And that's just, you know, like.

Yeah, but I mean, what it really does is it provides code that actually runs, I mean, and solves the problem.

So, and I tried that on multiple occasions.

So I'm actually pretty sure that for, you know, doing on the code level, it's probably a very useful tool.

And I'm actually somewhat surprised because, you know, theoretical computer science tells us that there is no way that you can predict any non-trivial property of a program, but still we do, we seem to have something that allows us to say, okay, please implement this, please do that.

And then it actually spits out some code.

So I'm actually impressed.

And the answer to that only because there was something in the training set, it can intuitively give you a solution to some novel problem.

In worst case, the configuration, what does it say?

The configuration looks valid, but it is not, which is basically, I guess, the point that you just made, right?

That it is convincing, but you must not switch off your own brain and think for yourself, which is generally speaking a great idea, I think.

But when you face that situation, what's happening?

Oh, you mean I should have just done the research myself in the beginning, right?

In other words, if it gives you an answer and you don't know if it's correct, you may be going down a rabbit trail, you know, chasing the wild goose, so to speak.

And, and you, you know, you could have just, well, maybe it helps you, gives you incentive to do more research.

I don't know, but, or a framework for the research anyway.

Yep.

There is that.

I need to dig it out.

There is a study where developers were given exercises to write a specific code for some stuff.

And it turned out that the code they wrote, if they were supported by AI tools, was less secure, but the people had more confidence in the code.

And it was code that was clearly meant to solve some security problem, like, you know, encrypt a file.

And obviously, if you don't do it right, then you're sort of missing the point.

And I found that quite interesting.

And I think, as you said, the point is that the other people would probably use Stack Overflow and try to figure out what it actually says there and try to understand that, while the other ones are probably just, you know, relying on security and thinking, well, this will probably be correct.

And then you end up with that situation.

That's somewhat worrisome, of course.

Okay.

Thanks a lot.

Thanks a lot for being here.

Thanks a lot for all the knowledge and answering all the questions.

I hope you have a great day.

And as I said, oh, no, I didn't say that.

So we have another episode on Friday in German, I'm afraid.

And that will be with Oliver Trudbohm about technical domain-driven design using JMolecules.

So I'm looking forward to seeing you there.

Will it be in English?

No, I'm afraid it's going to be in German.

Sorry about that.

But there are Germans, there are auto-generated English subtitles for the YouTube videos.

I'm just not sure whether they are good or bad.

Yeah.

Okay.

Very good.

Well, thank you for inviting me, Eberhard.

And we saw each other at the Como Camp a little more than a year ago, right, in Vienna.

And that was really cool seeing you.

And thank you for inviting me and try to be in touch.

Yeah.

Thanks a lot.

And talk to you soon.

Okay.

Bye.