# Folge 243 - Process Orchestration, BPMN und Workflows mit Bernd Rücker

Nächste Woche gibt es eine Episode von den IT-Tagen.

Das ist am Dienstag.

Und zwar abends.

Ich meine um 19 Uhr.

Da kann ich aber gleich nochmal nachgucken.

Und da sprechen wir darüber, wie denn eigentlich so IT in 2034 aussieht.

Genau.

Das dazu.

Heute geht es um ein ganz anderes Thema.

Heute geht es um dieses Thema rund um Process Orchestration und die verschiedenen Sachen, die es da so gibt.

Jetzt habe ich Bernd eingeladen.

Bernd, schön, dass du da bist und schön, dass du die Zeit gefunden hast.

Willst du kurz zwei Worte über dich sagen?

Zwei Worte?

Das sind wenige.

Ja, Johannes, danke, dass du mich eingeladen hast.

Freut mich, dass das Thema hier rauskommt.

Genau, mein Background ist, ich habe eigentlich ein Engineering Background.

Ich würde mal fast behaupten, wir haben uns vor bestimmt auch schon über zehn Jahren mit Spring mal kennengelernt.

So in dieser ganzen Java Enterprise Ecke.

Habe mich aber dann schon ganz, ganz früh diesem Thema Prozessautomatisierung im weitesten Sinne verschrieben und habe auch zu BPMN viel gemacht.

Alles Themen, wo wir gleich, glaube ich, nochmal ein bisschen einsteigen wollen.

Habe dann früh die Camunda gegründet, zusammen mit dem Jakob Freund, das eigentlich Beratungshaus rund um dieses Thema BPM, Prozessautomatisierung.

Und dann hat mich das Thema nie mehr losgelassen.

Wir haben selber als Camunda dann pivotiert, wie man so schön sagt, 2013 vom Beratungshaus zu einem Softwarehersteller.

Also wir hatten einfach ganz, ganz viel gesehen über die Trainings und die Workshops, die wir so gemacht haben, was bei den Kunden, bei den Unternehmen funktioniert hat in Richtung Prozessautomatisierung.

Oder vor allem auch, was nicht funktioniert hat, auch im Sinne von Software.

Damals war ja ganz viel sowas wie, keine Ahnung, IBM Process Server oder irgendwelche Software AG Sachen.

Und das hat alles nicht so wahnsinnig gut funktioniert.

Wir waren viel mit Open Source zum Beispiel dann unterwegs.

Da gab es aber auch einfach gewisse Probleme, sage ich mal.

Und dann haben wir irgendwann gesagt, hey, eigentlich wissen wir, wie das Produkt aussehen sollte, was man da bräuchte.

Und dann haben wir irgendwann quasi uns den Mut genommen und haben gesagt, okay, dann machen wir das.

Und seitdem sind wir seit 2013 einfach Softwarehersteller und wachsen ganz, ganz fröhlich vor uns hin.

Es sind jetzt gerade ungefähr 500 Leute und haben gerade diesen, wie ich gelernt habe, Zentaurin-Status erreicht, den man bei 100 Millionen Jahresumsatz bekommt.

Also wo man quasi schon bewiesen hat, dass die Software offensichtlich auch tatsächlich irgendwie hilfreich ist.

Genau, also von dem her in zwei Worten würde ich sagen, so Process Orchestration, das ist ein Wort für mich, Enthusiast.

Genau, super.

Vielen Dank und auch herzlichen Glückwunsch zu dem wirtschaftlichen Erfolg an der Stelle.

Damit ist eigentlich gar nicht, also das gibt halt diese Beziehung zu Camondon.

Vielleicht kurz ein Hinweis dazu, wie die Episode zustande gekommen ist.

Die ist halt dadurch zustande gekommen, dass ich einen Vortrag und einen Workshop gehalten habe.

Und irgendwie kamen da halt so Fragen rund um, wie passt denn eigentlich diese Geschichte Business Process Management zusammen so mit klassischer Architektur, Domain Driven Design, Baune Kontexte, Modularisierung.

Und das fand ich war halt eine gute Frage.

Und nachdem das halt irgendwie zweimal innerhalb von, ich weiß gar nicht, so 14 Tagen irgendwie aufgetaucht ist, habe ich gedacht, machen wir mal eine Episode und holen uns halt mal jemanden dazu, der es sozusagen so wirklich versteht.

Und genau, da bin ich dann auf dich, Bernd, gekommen.

Und das führt so ein bisschen gleich zu der ersten Frage.

Wie heißt denn jetzt dieser Bereich eigentlich?

Also Workflow Engine, Process Orchestration, BPMN, BPM.

Was ist der richtige Begriff oder wie ist diese Begriffsverwirrung so ein bisschen zu erklären?

Ja, also lass uns vielleicht versuchen, die Begriffsverwirrung zu untangeln, also auseinander zu holen.

Ich würde sogar behaupten, einiges sind synonyme Begriffe und werden auch teilweise einfach sehr unterschiedlich benutzt.

Also aus der Historie heraus benutze ich persönlich immer noch gerne den Begriff Workflow Engine, weil der ganz arg diese, das ist klar, ich habe eine Softwarekomponente, eine Engine, die macht dann auch irgendwas und die soll eben so in dem Fall Workflows, also letztendlich ja auch Prozesse, abarbeiten.

Das Problem dieses Begriff Workflow Engines ist dann ganz oft, dass er mit so menschlichen To-Do-Listen und Tasks eher, ich steuere Aufgaben zu Menschen, assoziiert wird und damit jetzt nicht unbedingt in so, ich sage mal, eher IT-nahen Themen wie, keine Ahnung, Microservices Orchestration oder ich baue jetzt eine Zahlungsplattform, dann denkt man meist nicht an Workflow Engine.

Aber das dahinterstehende Konzept ist ja einfach zu sagen, okay, ich baue ein Stück Software, dem kann ich eine Beschreibung meines Prozesses geben.

Das sind immer irgendwie Schritte, irgendwie Kästchen und Peile dazwischen, was passiert in welcher Reihenfolge und dann kann die Maschine das für mich steuern.

Und das ist eben dieses, Steuerung, dann sind wir eben bei Orchestrierung, deswegen eher dieser, ich sage mal, neuer Begriff der Prozessorchestrierung, Process Orchestration und dann gibt es eben auch einen Process Orchestration Engine, aber letztendlich meint es eigentlich was sehr, sehr Gleiches an der Stelle.

Und ich komme gleich, BPM und BPMN würde ich gleich mal noch machen, aber lass mich mal ein Beispiel machen.

Ich mache immer gerne Beispiele.

Und da würde ich gerne ein, zwei Dinge auch noch entwirren, die ganz oft in einen Topf geworfen werden.

Wir haben auch schon Prozessautomatisierung gesagt, mindestens ich habe es, glaube ich, in der Intro mal gesagt.

Unter Prozessautomatisierung verstehen jetzt auch ganz viele Leute verschiedene Dinge.

Ich gucke jetzt mal auf Geschäftsprozesse.

Ich mache ein Beispiel, Kontoeröffnungsprozess.

Also das ist jetzt einfach aus der Bankenwelt.

Ich will ein neues, keine Ahnung, Shiro-Konto aufmachen.

So, dann geht ja auf der Seite der Bank ein gewisser Prozess los.

Also ich gehe vielleicht auf die Webseite, tippe meine Daten ab, klicke auf den Button und dann geht dort ein Prozess los, sodass er sagt, im ersten Schritt muss vielleicht irgendwelche Prüfungen gemacht werden, Adressprüfungen, irgendwelche Scoring-Sachen, also hier so Schufa-Einträge.

Dann muss irgendwie heutzutage Know Your Customer oder Compliance-Check.

Dann gehen so Sachen los.

Dann muss die Bank vielleicht noch entscheiden, wollen sie das?

Und dann passieren gewisse Schritte in der Reihenfolge, mein Konto, wir haben vielleicht eine IBAN zu vergeben, wirklich das Konto in den richtigen System, Backend-System anzulegen und so weiter und so fort.

Und das ist ein Prozess, verschiedene Schritte abfolgen.

Um diesen Prozess zu automatisieren, brauche ich eigentlich so zwei Ingredients.

Das eine ist eben dieses Thema Orchestrierung, also wie sorge ich dafür, dass die richtigen Dinge in der richtigen Reihenfolge passieren?

Und das zweite ist auch ein Stück weit automatisieren der Aufgaben, die in diesem Prozess zu tun sind.

Also es könnte sein, dass da irgendwie ich soll einen Schufa-Score prüfen als Beispiel.

Hat man früher wahrscheinlich einfach irgendjemand per Hand irgendwo in ein System geguckt, macht man heute nicht mehr, ruft man einfach ein System auf, eine Schnittstelle.

Und so ist das auch zu sehen.

Jeder Schritt ist dann entweder ein Systemaufruf, API-Aufruf, was auch immer das ist.

Oder eben den Menschen aufrufen, also eine Aufgabe in die Liste zu legen oder auch, keine Ahnung, heutzutage ihn anzuslacken oder eine Teams-Message zu schicken.

Also wie genau dann die Maschine mit den Menschen in Kontakt tritt, sei immer dahingestellt.

Also von dem her Process Automation ist für mich immer Process Orchestration und Task Automation.

Und so kommt das dann alles auch so ein bisschen zusammen.

Lass mich noch einen Begriff erklären und dann gebe ich dir auch mal wieder kurz Zeit, da reinzuhaken.

Nämlich den BPMN hast du mal kurz erwähnt.

Das steht für Business Process Model and Notation.

Das ist ein ISO, also inzwischen ISO-Standard für diese Prozessbeschreibungssprache letztendlich.

Also wenn man so will, ein XML-Dialekt, in dem ich dann diese Prozesse aufmalen kann auf der einen Seite, also wirklich grafisch, aber eben unter der Haube auch wirklich eine Bedeutung dahinter steckt, was diese Kästchen jetzt sind und wie ich da jetzt Logik dahinter hänge und was die eigentlich zur Ausführungszeit so bedeuten.

Ob der Pfad jetzt nach oben oder nach unten geht, ob ich da was parallel mache.

Also da kann ich auch so Timeouts machen.

Also BPMN ist sehr, sehr mächtig darin, so typische Probleme auszudrücken, die ich eben in solchen Prozessen habe.

Und das kann ich direkt zu einer, also zumindest einer guten Orchestration Engine geben und sagen, hier ist mein Prozessmodell und dann kann ich mir das auf der einen Seite grafisch angucken, aber eben auch direkt ausführen.

Genau, super.

Was also bedeutet, dass wir, wenn man das zusammenfassen sollte, oder das wäre die Frage, hört sich das für mich so an wie, das ist so ein Ding, was irgendwie atomare Sachen koordiniert.

Passt das so weit?

Ja, aus Sicht des Prozesses atomar.

Also ich habe einzelne Schritte, die sind aus der Sicht des Prozesses atomar.

Da kann ja noch mal ganz viel drinstecken.

Ja, genau.

Also da könnte drinstecken, jetzt mach hier eine Prüfung und das ist vielleicht sogar ein komplett eigener Prozess, der drei Wochen dauert.

Aber eben eine Koordination und Integration, das ist so ein bisschen die Idee.

Und das führt dann eigentlich zu der nächsten Frage.

Also bedeutet das, dass man da jetzt keine Geschäftslogik drin haben sollte?

Also dass man sagt, das ist eben so eine Integrationsschicht oder bestimmte Teile sind ja vielleicht dann tatsächlich Geschäftslogik, weil ich mir auch in dieser Integration dann irgendwelche Entscheidungen treffen muss.

Also ist das gut oder schlecht, wenn da halt irgendwie Geschäftslogik drin ist?

Oder sollte da nur bestimmte Geschäftslogik drin sein?

Oder wie ist da die Idee?

Lass uns mal vielleicht versuchen, ich versuche mal noch was anderes so ein bisschen auseinander zu ziehen.

Und das ist so, also jetzt habe ich diese Maschine, diese Orchestration Engine.

Oder man nennt sie auch gerne Workflow Engine.

Meine Erfahrung ist, dass die Leute das im Kopf immer noch besser klarkriegen.

Jetzt habe ich diese Engine.

Und erst mal aus einer rein technischen Sicht, sie stellt mir so eine Capability quasi bereit.

Das geht hauptsächlich darum, ich habe ein grafisches Modell, das kann ich ausführen.

Und ich kann langlaufende Sachen unterstützen.

Und dieses Thema Long Running, nämlich weil ich ganz oft warten muss auf Fremdsysteme, die brauchen ein bisschen mir eine Antwort geben, auf die Menschen, der auch nicht jeden Millisekunden antwortet, auf irgendwelche Events, die halt erst in zwei Wochen sind oder keine Ahnung.

Also ich muss warten und daraus resultieren Anforderungen an Persistenz, an Operating, an Monitoring, so, so, so.

Aber das ist erst mal so diese technische Komponente.

Jetzt kann ich die natürlich für unterschiedliche Anwendungsszenarien irgendwie brauchen.

Das eine, du hast es gerade schon gesagt, sind integrationsnahe Sachen.

Also wir haben durchaus so Use Cases.

Ich würde es jetzt mal Integrationsprozesse nennen, wo es eigentlich darum geht.

Ich will ja, keine Ahnung, ich will irgendwas über AI, über irgend so ein AWS-AI-Service rausfinden.

Aber dafür brauche ich vielleicht zwei, drei, vier Schritte, die nacheinander folgen.

Muss die Daten kurz transformieren, damit ich sie richtig irgendwie dahin schicken kann.

Oder du kannst das ganz simpel machen.

Ich will eine GMS-Nachricht schicken und auf die Antwort warten.

Und wenn die nicht kommt, will ich noch was anderes machen.

Also es gibt manchmal so Anforderungen, wo ich sage, ich muss halt drei, vier, fünf, sechs Sachen machen, um eigentlich fachlich gesehen so eine technische Schnittstelle aufzurufen.

Das wäre für mich so ein Integrationsprozess.

Dafür kann ich natürlich BPMN benutzen.

Dafür benutzen auch Leute Camunda oder andere Frameworks.

Ist aber ein ganz anderer Anwendungsfall, als wenn ich tatsächlich so, was wir Ende-zu-Ende-Geschäftsprozesse nennen, anschaue.

Also was ich gerade meinte, Kontoeröffnung oder was weiß ich.

Du willst eine Versicherungspolizei, du willst einen Schaden abwickeln, du willst neue Mobilverträge auf deinem Handy haben, du willst umziehen.

Das sind so typische Prozesse, die wir da eben auch bei den Kunden sehen.

Und das ist ja eine ganz andere Flughöhe.

Also da habe ich dann so einen Schritt, der heißt dann eben, ich muss das in mein Kernsystem schneiden, in mein Kernbankensystem.

Und vielleicht ist das unter der Haube dann ein Integrationsprozess mit 20 Schritten, weil das halt irgendwie kompliziert ist.

Und auf beiden Systemen spielt Process Orchestration Prinzipiell eine Rolle.

Theoretisch sind natürlich die Anforderungen ein bisschen anders, auch an die Tools.

Du hast eigentlich gefragt nach Geschäftslogik.

Jetzt fange ich langsam an, zu deiner Frage zurückzukommen.

Wenn ich mir diese Integrationsprozesse angucke, dann ist das typischerweise eben genau eigentlich keine echte Geschäftslogik, weil ich sage, da muss ich halt irgendwelchen technischen Kram machen, der ganz oft mit Long Running, mit Langlaufen zu tun hat, was mir eben schwer macht, es in Java oder in Python zu programmieren.

Deswegen will ich vielleicht irgendwie ein Framework on top.

Aber das sollte idealerweise natürlich nicht wirklich Geschäftslogik sein.

Wenn ich mir jetzt Geschäftsprozesse angucke, dann bestehen die ja ganz essentiell aus Geschäftslogik.

Das ist ja eigentlich die Geschäftslogik, dass ich sage, hey, ich nehme nur Kunden in meine Bank auf, wo ich halt vorher diese fünf Prüfungen gemacht habe.

Und vielleicht ist das ja sogar eine gesetzliche Anforderung.

Also das ist essentiell Geschäftslogik.

Und ich will genau, dass die in diesem Prozess landet.

Dafür mache ich ihn eigentlich.

Das ist ja einer der großen Vorteile.

Also Langlaufen spielt dort auch eine Rolle.

Aber das andere, was dann schnell auch eine Rolle spielt, ist eben dieses Thema Sichtbarkeit.

Ich kann das jetzt mit verschiedenen Stakeholdern besprechen.

Ich kann das bei Banken der internen Revision zeigen, wenn das denn sein muss.

Ich bekomme so Process Intelligence Tooling, wo ich sehe, welche Pfade werden oft durchlaufen.

Wo dauert das lange?

Unter welchen Datenkonstellationen geht das oft nicht weiter?

Oder was auch immer.

Also da kann man ganz, ganz tolle Sachen eigentlich machen.

Und das basiert immer auf diesen grafischen Modellen.

Also da habe ich, wenn man so will, ein bisschen andere, was in der Plattform bringt mir eigentlich wie viel.

Macht das noch Sinn gerade?

Ja, also wenn ich es sozusagen zusammenfassen würde, hört sich das so an wie, ich habe eben bestimmte Dinge, du hast eben gesagt Long-Running-Prozesse, die ich halt eben auch Persistenz halten kann.

Und das können Sachen sein, die andere Dinge integrieren oder eben die ich halt sozusagen selber dann für mich entwerfe.

Und davon abhänge ich, ob es jetzt sozusagen meine eigenen Prozesse sind oder nur Integration, will ich halt Geschäftslogik in dem Prozess drin haben oder eben auch nicht.

So habe ich das jetzt sozusagen für mich verstanden.

Ja.

Vielleicht darf ich noch eine Sache dann und top da öffentlich wichtig finde.

Du musst dann natürlich auch immer gucken, welche Granularität von Logik willst du eigentlich in diesen Prozess packen.

Und das ist dann auch unterschiedlich.

Also bei einem Integrationsprozess bin ich ja in einer tiefen Granularität.

Der sieht vielleicht ein bisschen aus wie ein grafisches Programmieren manchmal, aber jeder Schritt kann halt sozusagen stehen bleiben, Long-Running sein.

Und so ein Geschäftsprozess ist natürlich auf einer Abstraktionsebene, wo ich sage, jetzt mach das aus einer fachlichen Sicht.

Du hast es ja vorhin schon gesagt.

Was sind denn atomare Tasks sozusagen?

Also was will ich hier tun?

Ganz häufig dann ja sogar unabhängig von der Implementierung gedacht.

Also sozusagen abstrakt von der Technologie.

Also bis hin zu eigentlich ist das egal, ob diesen Task jetzt ein Mensch macht, der dann sich durch 15 Oberflächenmasken klickt oder ob das ein Systemaufruf ist oder ob das morgen ein AI-Agent ist, der das irgendwie übernimmt.

Sollte egal sein, solange diese Granularität eigentlich irgendwie passt.

Also da fange ich dann genau nicht an, jeden kleinen Kran sozusagen da rein zu modellieren, sondern Bilder eine Granularität finden, wo ich sage, okay, dieser Geschäftsprozess ist sauber, dann habe ich einen Task und der ist irgendwie implementiert.

Vielleicht ist das sogar nochmal ein Prozess in der Ebene drunter, weil das eben Sinn macht.

Vielleicht ist das auch einfach nur ein Service-Aufruf.

Vielleicht ist das aber auch Programmierung, dann eben doch ein bisschen Java-Code hintendran.

Also in dem Sinne, es ist einfach, wenn man so will, ein zusätzliches Werkzeug im Stack, was ja auch gar nichts ersetzen soll in dem Sinne, was einfach diese Prozessebene bildet.

Heißt das, ich kann jetzt mit sowas wie Kamonda beispielsweise BPMN benutzen und gleichzeitig das auch als Programmier-Framework benutzen?

Also habe ich beide Möglichkeiten?

Also du kannst das zusammenstecken.

Also der Weg, wie die Engine funktioniert, ist letztendlich einfach auch über API.

Also in dem Sinne kannst du das auch komplett headless fahren, wenn du das möchtest.

Du kannst ja dann auch Unit Tests schreiben.

Das wollte ich gerade sagen, im einfachsten Fall.

Das stimmt, glaube ich.

Ich weiß gar nicht, ob es der einfachste Fall ist.

Aber wenn ich jetzt aus einer Java-Entwicklerbrille denke und überhaupt keine Ahnung habe von Workflow-Engines und BPMN, dann kann ich mir schon auch so vorstellen, dass ich sage, naja, ich habe jetzt halt noch so ein grafisches Bild und an jedem Knoten, der ist einfach verknüpft mit einer Methode in meinem Java-Code.

Und wenn ich quasi die Prozessinstanz, sagt man, also wenn ich einen neuen Prozess antriggere, sage ich über API, hey, starte eine neue Prozessinstanz und nimm bitte die paar Daten mit.

Das ist typischerweise ganz wenig.

So eine kleine Map von Sachen.

Dann guckt die Workflow-Engine in dieses Prozessmodell.

Was muss ich machen, wenn ich den starte?

Ah, ich laufe mal hier lang und dann kommt dieser Knoten da.

Und was bedeutet dieser Knoten?

Ah, das heißt eigentlich, dass dieser Code da unten in Java aufgerufen wird.

Und dann stellt sie eben sicher, dass das passiert sozusagen.

Und zwischendrin könnte sie auch warten und persistieren und so.

Aber das heißt, ich kann das schon mit meiner Programmierung zusammenbauen.

Ich kann mir auch ganz normal Unit Tests dafür schreiben.

Also ich kann auch sagen, ich will gewisse Szenarien bauen, wo ich sage, wenn diese Kontoeröffnung mit genau diesen Daten da vorne reingesteckt losläuft, erwarte ich, dass sie dann, keine Ahnung, diese Prüfung dieser API aufruft mit diesen Parametern, die ich dann irgendwie so rausmocke und solche Geschichten.

Also das ist nicht zwangsläufig weit weg von der Programmierung.

Das ist, wenn man genau hinguckt, eigentlich mit der Grund, warum wir damals auch Camunda als Produkt gestartet haben, weil die Tools, die wir damals gesehen haben, also wie gesagt 2012, 2013, lange her, die konnten genau das nicht.

Da waren es dann ganz oft, okay, ich nehme jetzt hier dieses BPM Produkt und dann muss ich auch alles da drin machen.

Und dann war es echt hakelig, noch echte Software Engineering dazu zu packen und das zusammen zu kriegen.

Das war eigentlich immer so ein bisschen das Ding.

Das ist, also da ist jetzt gerade im Chat so ein bisschen eine Diskussion, die ich auch schon im Hinterkopf hatte.

Also was du ja sagst ist, okay, ich habe ja diese grafische Notation und es gibt ja jetzt insbesondere so diese Geschichten rund um kollaborative Modellierung, sowas wie Events Storming, wo man eigentlich versucht mit so Low-Tech-Produkten, also so Prostits, dafür zu sorgen, dass man halt diese wahrgenommenen Barrieren hat, reduziert und hat gesagt, okay, wenn du halt ein Prostit schreibst, kannst du halt Events Storming machen.

Das kann halt nicht so schwierig sein.

Und demgegenüber stehen halt solche formalen, also das ist ja offensichtlich informell nicht, also ein Prostit ist halt irgendwie was, was nicht Formales wäre.

Ein BPMN, sei es fair gesagt, ist halt ein ISO-Standard und hat irgendwie auch dann irgendwelchen Formalitäten entsprechen müssen.

Der Darth Kali hat jetzt gerade im Chat geschrieben, wir benutzen Camunda.

Der große Vorteil ist, dass die Fachexpertinnen mit den Entwicklern, die ja zusammenkommen, und da hat er jetzt Ralf Müller geschrieben, kommen die Fachexperten mit BPMN gut zurecht.

Ich habe die Erfahrung, dass die Decorator teilweise als zu technisch angesehen werden.

Und dann kommt halt irgendwie Darth Kali und sagt, wir entwickeln das gemeinsam, da funktioniert es sehr gut.

Also führt ja zu der Frage, wie ist denn dein Eindruck?

Also der Darth Kali sagt halt irgendwie, vielleicht ist das sogar das, was beide sagen, nur Menschen wie wir, also TechnikerInnen, können das wirklich verstehen.

Und für Fachexpertinnen ist das zu formal.

Also es steht da nicht ganz, aber das höre ich so ein bisschen raus.

Ist da eine Erwartungshaltung, dass Menschen, also normale Menschen, nicht TechnikerInnen, BPMN verstehen und das modellieren sollten?

Oder ist das tatsächlich etwas so für Leute wie uns, die ja mit so formalen Systemen Erfahrung haben?

Schade, wir können jetzt eine halbe Stunde lang erstmal rollen und was ein normaler Mensch ist definieren.

Aber das lassen wir mal.

Also ich würde eigentlich das ziemlich unterstützen, wie es da im Chat, glaube ich, passiert ist.

Also das eine ist, meine Erwartungshaltung wäre nicht, dass jetzt zum Beispiel Fachabteilungen direkt BPMN modellieren.

Das glaube ich auch nicht. that actually models these BPMNs.

Whether this is a business analyst, I have already seen that, if they are good, yes.

Sometimes this is a bit too formal for them, why then always PowerPoint is so much cooler, but it doesn't matter at first.

Then it might actually be someone on the IT side, in the development side.

But if there is someone who models these BPMNs, it is the second thing to understand these BPMNs, if I see them.

And that actually works quite well again in terms of breadth.

And not every specialist user has to understand every detail in the model, so to speak.

You also have to say that there is the big bonus point, that this model, this graphic model that I have, is not only created for a documentary that then doesn't work for anyone, but it is running software.

That means I can really look into it at any time, also again with the specialist user together and say, okay, you need this change now, let's see where actually.

And maybe you don't understand the model completely on your own, but still I have this basis on which I can simply communicate.

And the experience then also shows, when the maturity, when the maturity in the company increases, the more you work with it, the more it is understood.

And then my claim would simply not be that everyone has to understand 100% BPMN.

That's nonsense.

But there must be at least one or two people in the company who can really drive that a bit.

So we have larger customers who really use it broadly.

Very often such a central team, which simply supports the others, enables, supports a bit.

And then it actually works quite well.

And now, I think, there will be a lot more in the next few years when it comes to this whole topic of co-piloting.

So we can already co-pilot BPMN today, where I theoretically, I haven't tried that yet, that would be exciting, such an event storming.

So event storming even goes well together with BPMN in terms of the matter.

So event storming would be, so to speak, the creative technology to get somewhere.

BPMN would be more like, okay, and now I'm doing something out of it.

Which is still very good for the events that I've actually stormed, so to speak.

And you can already throw something like that to such a co-pilot today.

So if I have that as a table, then I'll throw it to him and he'll make me a BPMN model out of it.

That won't be cool right away, but I'll get into a wheel pretty quickly, so to speak.

And that's what it's all about at the end of the day.

Exactly.

So maybe briefly in the chat, you just wrote, this creates a good exchange of knowledge.

So through this, that developers and domain experts do something together.

We developers learn more about the technical process and the technical experts have more understanding of the technical needs.

So that sounds good so far.

And at Twitch, the Java Hippie said, I also had very good experiences with the readability of BPMN.

We have a very long account opening process.

Yes.

Exactly.

Based on the BPMN model, we can discuss it with the legal department of a bank.

Yes.

Good.

I think that's how we got this BPMN, graphical modeling and so on.

Or that would be the other question, which concerns me a bit.

Graphical notation, if it's formal, we sometimes have this problem that it's easier to just write things down as code.

And now you say, that's also an XML dialect, but programming in XML is not really nice.

Especially these UML stories are often like that, if you really write everything down formally, it becomes insanely complicated and confusing.

And you want a programming language.

Is that also a problem that exists in BPMN and this workflow area?

I don't actually see it as a problem.

If you're out in the woods, everything is possible.

I've also seen projects that also used BPMN in a granularity level, where I would say, that doesn't make sense.

It was graphically programmed, a sense of reason, because now we have the tool, now we use it too.

And then, of course, models come out, where you say, okay, that doesn't really help me.

Then I only have overhead and nothing won.

I would have preferred programming that.

But if I hit this granularity level correctly, you have to see that, especially at end-to-end business processes, if I look at them, the effort is rarely, so to speak, these, and let that be 50 knots, but to paint them up and wire them up is not the effort in the project.

The effort in the project is to understand which knots I have to have, in which order they actually take place, how the data flow is in between, why it actually knows back there, what happened in the front.

And how I can change that now.

That's where the actual effort happens.

And that's where this model just helps me so incredibly much, because then I can communicate with a lot of people that I couldn't look at code with.

You can discuss for a long time now, but can I use such a specialist?

There is also a bullet point list of statements here.

Then I write a nice DSL.

I don't think it works.

At the latest, if you have a loop in it, then you have such a timeout, then you have 15 other things.

So we have good experiences there.

I have no problem with that at all.

And then the next thing comes up, yes, but then we make such changes.

And how do I understand?

Then I have to do such diffing.

And do you want to do XML diffs now?

That's totally bananas.

So two points to that.

In practice, these XML diffs were never such a big problem, because you rarely change the entire process.

And not everyone has to push the box a millimeter further to the left, just because he thinks it's nicer.

So if you put a bit of radio discipline on the day, it works pretty well with XML.

The second thing is that the tools, just like ours, you can do graphic diffing.

So it doesn't fail anymore nowadays, so to speak.

And then you can do pretty cool things.

So two more things from the chat, so to speak.

Ralf Demüller wrote, I'm still waiting for a text-to-diagram library à la PlantUML for BPMN.

I don't know if you want to say anything about that.

I don't know the specific tool, but what I think will solve this is this copilot thing.

So that you just use the AI, it can create the model.

And that works pretty well.

And what I then throw in, I can check my own estimates, the AI does that amazingly well.

And then Grumio has a question, also on YouTube, which maybe distracts us a bit from the original plan.

But that doesn't have to be negative.

So he wrote, are there typical obstacles in the introduction of tools like Cramunda that should be avoided, especially with regard to if there is already a kind of self-development in the company?

Yes, there are always many.

So you have to, it depends, you have to look a little bit how the situation is exactly there.

But, I'll just say, obstacles in general in the introduction are very often what we have already discussed, understand granularity, understand what the tool actually does for me and then don't program graphically.

That's one thing.

Of course, if I already have my own self-built workflow engine in the house, we see that very often, so we often solve them.

Then you just have to look at the political situation more often.

What do we already have?

And who likes that?

Or who doesn't like that?

And how is it seen internally?

I usually see it super positive, because at least that means that this way of thinking is already understood in the company.

What is a workflow engine?

What does it bring me?

How can I do that?

Most of the time, the situation is that this is liked, only that there is usually too little capacity to properly develop this workflow engine.

Then features are missing, or a bug here, or you can't do that.

Then it's usually a pretty nice situation to say, okay, then we come in with another tool, that can do that, and otherwise it will continue in a similar way.

Maybe that's always a bit selfish, but I'm allowed to do that here.

No, it drives me around so much.

I have two things.

On the one hand, we as Camunda come from the company lifecycle in between already a little bit on the market, and have quite a few customers who actually use it on a large scale.

So not just one process, but many processes.

That means I've been dealing with it a lot in recent years.

I also wrote a book about what I actually have to do to bring it into the enterprise, to bring it into the breadth, also to scale internally.

And I learned a lot.

And one of the learnings, and I found that totally interesting, was completely different.

I would say that was my trigger where I understood it.

We had an insurer that actually uses Camunda on a large scale, which also uses RPA on a large scale.

Something like Robotic Process Automation.

Probably not so many people know that here, but that's the idea.

We know that under Selenium and Test Automation, but the same tools are also used to control surfaces, very often if you don't have an interface, no decent one.

For task automation, a surface is controlled.

And the fact that this happens in the company not so much from a technical point of view, but from a management point of view, RPA has the following judgment, if you will.

RPA projects can immediately calculate such a return on investment.

Because they typically replace people who hack stupid data from A to B.

Then you can say, this RPA project cost me X, so I save so and so many people, they can do something else now, so I have a return Y and with that I have a cool project.

And that's what they do.

And then at some point this led to the perception that RPA is really cool, we save a lot of money and Kamuna costs a lot here.

Although core processes were automated there, and not even less.

So it was at a level where you say, okay, but if you turn off Kamuna tomorrow, the insurance won't work anymore.

And this perception, I think it's important, you've often experienced this value, so to speak, what the workflow engine does and why I do it, and what strategic value it has.

So what I said earlier, I now understand the right granularity of the tasks, leads to the fact that I can suddenly think about where I want to use AI at all, where I can use AI at all.

This is currently a huge discussion everywhere.

And then getting this topic of business agility done is massively important, but it's hard to put into numbers.

And IT has anyway, I think we all know that, we always have such a restraint in there.

But that's clear, it makes total sense, it's a nice architecture or something.

But to convince on the right level, I think it's extremely important.

And especially when you come out of an IT, you often see Camonga projects initiated, you see the technical advantages, you save effort in the project, so to speak, great.

But beyond that, to also look at this level, because otherwise I've just experienced over time that projects are cut off from the political big picture and not at all from a technical point of view.

So it's very similar to microservices, you have to somehow think a little bit about that.

Sorry, that was long, but that's just as important to me.

So just to write the architect community a little bit more into the book, to just look at that.

Yes, so I'm honestly fully with you.

So I'm of the opinion that we take more technical measures, we are almost obliged to prove that they somehow make business sense.

So once from what is now politically motivated, but also simply because if we can't justify it, that it somehow helps to make more money, then it might not be good measures.

And that's why these glasses help to set priorities again.

The book you mentioned, where you played on it, is probably this Enterprise Process Orchestration.

I'll link that again.

Oh, you already have it?

No, it's an early access.

I printed it myself, how you can do it nowadays.

But that's coming in Wiley.

That's in the process right now.

That should be in April.

Exactly.

So now comes the next topic and that's this story with orchestration and choreography.

And yes, you said it in the previous interview, there is no clear definition.

But you wrote books and there is obviously a definition in there.

Yes, exactly.

Practical Process Automation.

What is that anyway?

So what is choreography, what is orchestration?

Yes, let me pick up one sentence on the subject.

Because in fact, let me lie, I would say 2017, 2018, a lot was busy.

All this micro-services, event-driven, architecture hype and not everyone, came to me and said, then we need your access.

We're all doing choreography now, we're all doing event-driven, nothing is controlled centrally via such a BPM machine.

That's nonsense, then you're out somehow.

And then I thought a lot about it.

So once, so to speak, you can now of course put on the film hat and say, no, I think that's nonsense.

But I really wanted to understand it.

And then I dived relatively deep.

And the first thing you said, I found it totally interesting, if you google a bit, on the Internet, you can't find a clean definition for either choreography or orchestration.

And there you can find very contradictory things.

And also on the really much-quoted things.

So I think the most quoted thing was some Stack Overflow discussion, which put clean diagrams in there, which in my opinion are wrong or sometimes even contradict each other a bit.

Well, that's where it all fed in a bit.

That's why I tried to clear it up.

And I wrote a definition into the book that I think is correct for me.

I don't think she would claim that she is totally adapted on the Internet.

But I understand it.

For me, choreography is always when it's about an event-driven coupling.

Choreography is for me when I have components that simply react to events that have somehow thrown other components into the world.

And then, typically, that has characteristics, that is ultimately a communication between two components.

But the one that emits the event, doesn't know who wants to do what with this event and then processes this event.

Well, she knows that she wants to process the event, but in doubt not where it comes from.

And that's choreography for me.

Because I can now build systems that just throw events.

Hey, a customer wants a new account here.

Hey, I've checked a customer here.

Hey, I've created an account here and then other components can react to it and do something.

That was the idea for a while.

That's how we build systems now.

If we have low coupling with this argument, then I just decide in my microservice which events to react to.

Everything is chic.

I can change that quickly.

That was often the idea.

What is orchestration for me now?

I define orchestration when two components interact with each other via commands, not events.

Or if you read Sam Newman he finds commands too suggestive.

You have to do that now.

You can't refuse that.

But I call them commands.

I still find it easier.

And that means in this communication relationship it's just the other way around.

The sender knows over there, you do the test for me now.

Then send a request and wait for it to come back.

If you want, just prepare an API.

He doesn't even know who called him.

That's it for me.

Those are the two sides of the coin, if that makes sense.

That would be something where I have a few questions.

You briefly mentioned earlier that orchestration and choreography in terms of conceptualization for me at least it's about a central control or not.

Orchestration implies a central control that there is a thing that says this does this.

In the context of the account opening I would expect that there is an entity that says for example in such a workflow engine and then I have these individual atomic parts that are coordinated over it.

While in choreography I would have thought but that seems to be a different definition.

For example, this Schufa scoring that there is someone who continues something with it.

This one thing knows what the next step is and just like the Schufa score thing that has been called up by something else.

That means every step knows what the next steps are and I have it decentralized.

What you suggest as a definition doesn't seem to have much to do with it.

Or am I wrong?

No, it's not that far away.

Maybe the very last thing you said was maybe a little different.

This component knows what the next step is.

For me, event-driven, when I look at event and choreography when I create an event I don't know what the next step is.

That's just event-driven for me.

Because that's not my responsibility.

It's a lot about responsibility how I cut my components.

And when I create an event I shouldn't assume that something will happen.

Sorry, but what does that mean?

Choreography as I just tried to define it would mean that the Schufa step knows what the next step is.

Schufa-Componente steuert ja jetzt eine andere Komponente, was zu tun.

Okay, das heißt also für...

Warum sollte sie das tun?

Jetzt kann man sich überlegen, wie man sozusagen Orchestrierung implementiert.

Also man könnte theoretisch ja sagen, es gibt dieses Routing-Slip-Pattern als Beispiel, dieser, wie heißt es auf Deutsch, dieser Laufzettel, glaube ich.

Also ich könnte quasi so eine Message reinschreiben, wenn du fertig bist, schick das da weiter.

Dann wüsste diese Komponente, die jetzt das Schufa-Scoring macht, kann den Routing-Slip lesen und weiß, ah, da schicke ich es jetzt hin, ohne zu wissen, warum eigentlich.

Damit hätte ich quasi auch Orchestrierung gebaut, dezentraler.

Ich glaube nur nicht daran, dass das besser funktioniert.

Also nur, dass wir es sozusagen sauber bekommen, das heißt, das, was du jetzt bei Choreography sozusagen voraussetzt, ist, ich habe eine anonyme Menge an Dingen, die irgendwie reagieren, während du sagst, bei Orchestrierung weiß ich, mit wem ich spreche.

Das ist die Definition, die du jetzt mit Commands und Events sozusagen da siehst.

Ja genau, im Prinzip ist das so, ja.

Okay, so und dann sagst du halt, wenn ich ein Ding habe, also dieser Schufa-Schritt weiß, was die nächsten Schritte sind, dann ist das bei Orchestrierung aber dezentral.

Genau, ein anderer Weg, das hinzukriegen sozusagen.

Genau, und irgendwie scheinst du jetzt zu implizieren aus dem, was du gesagt hast, dass so eine dezentrale Orchestrierung irgendwie keinen Sinn macht oder deutliche Nachteile hat.

Also zwei Dinge.

Erstens, ich störe mich immer ein bisschen an diesem Wort zentral und dezentral, weil das, glaube ich, auch häufig ganz unterschiedlich verstanden wird.

Also, wenn Leute schon ein bisschen länger dabei sind und gerade mit BPM-System und ich sage zentral, dann denken die immer an, oh, wir haben hier diesen einen dicken BPM-Server im Unternehmen, der wird noch von diesem Team gemanagt und wenn ich da irgendwas mache, ist das ein Riesen-Bottleneck, das ist irgendwie alles blöd und so wollen wir das ja nicht.

Passt auch nicht mit Microservices zusammen.

Und das Team ist ja nicht so, also so sieht ja Technologie heute nicht mehr aus, sondern ich kann ja auch sagen, ich fahre allein schon die Orchestrierungslogik dezentral.

Also, ich hätte meinen einen zum Beispiel Kontoeröffnungsservice, wenn ich so denke, und dieser Kontoeröffnungsservice, der ownt quasi gewisse Geschäftslogik, wie das Konto zu öffnen ist da.

Daher der Name, ne?

Und da gibt es ja dann auch irgendwie einen Verantwortlichen und ein Team vielleicht, das das baut und weil eben dieser Kontoeröffnungsprozess davon profitieren kann, eine Orchestration Engine zu nehmen, werden sie das vermutlich, hoffentlich tun und sagen dann auf dem Weg anderen Services, die sie als Zulieferern brauchen, eben Bescheid.

Natürlich könnte ich jetzt sagen, nee, ich nehme keine Orchestration Engine, weil will ich nicht und könnte irgendwie einen Routing-Slip ausdenken und den rumreichen.

Das würde schon technisch funktionieren.

Ich kenne jetzt einfach zumindest keine out of the box, wie sagt man, Framework oder Vorgehen, wo ich das echt gesehen habe, dass das gut funktioniert.

Rein vom Pattern her würde das schon funktionieren.

Ich frage mich dann, welchen Vorteil ich da mit habe, weil dann hätte ich ja diese Komponente, wenn wir bei dem Beispiel bleiben, die meinen Schufa-Score macht, die muss ja auf einmal einen Routing-Slip verstehen und wissen, wie es weitergeht.

Versus in der anderen Variante habe ich halt meinen Kontoeröffnung-Service und der weiß, erst mal mache ich Schufa-Scoring und wenn das fertig ist, mache ich was anderes und dann muss ich Schufa-Scoring gar nicht anfassen.

Dann kann das sogar morgen ein SaaS-Dienst sein, wenn das geht.

Das ist mir völlig egal, hat überhaupt keinen Einfluss.

Also im Sinne der Kopplung sozusagen, stört es mich dann so darüber nachzudenken, dass man sagt, dieser Routing-Slip wäre jetzt bald dezentral weniger gekoppelt.

Aber man kann es tun.

Also das wäre für mich immer noch, aber trotzdem eine Orchestrierung, wäre eine andere Art, das zu implementieren.

Damit du aber implizit jetzt sagst, also eigentlich sagst, ich brauche sowieso einen Prozess als Gesamtprozess, eben die Kontoeröffnung und so die Aussage, ich habe eigentlich nur die Wahl, entweder das als Routing-Slip mitzuschicken oder ich muss es halt zentral koordinieren in einer Workflow-Engine, was du damit in Abrede stellst, ist, dass man den Prozess so modellieren kann, dass er eben nur aus den Einzelschritten besteht und die Gesamtsicht halt einfach dann sozusagen verschwindet.

Also nicht, dass ich halt sage, okay, ich bin halt Schufa, ich kenne den nächsten Schritt und ich weiß nicht, was sonst noch irgendwie passiert.

Muss ich auch nicht wissen, muss ich auch nicht einen Routing-Slip haben, sondern ich habe irgendwie nur mich und den nächsten Schritt und der Schritt, von dem ich irgendwie aufgerufen werde.

Also eben sozusagen inhärente Dezentralisierung, weil ich fachlich halt dieses Gesamtmodell nicht brauche, über den gesamten Kontoeröffnungsprozess.

Also ich würde das an sich, also zumindest den Anfang, den Satz, den du gesagt hast, fast unterschreiben.

Ich würde sagen, man will diesen Prozess halt haben und man braucht ihn nicht zwingend.

Ich kann das anders implementieren.

Ich glaube, man will ihn eigentlich haben.

Warum?

Weil ich bei solchen Ende-zu-Ende-Prozessen halt tatsächlich auch die Verantwortung zum Beispiel klar haben will, also auch rein organisatorisch, weil ich möchte da einen Owner haben.

Vielleicht ist unsere Brille ganz oft ein Process-Owner, aber du kannst das ja auch im Domain-Gem-Design.

Also du brauchst eine Ownership für diese Komponente.

Die hat eine gewisse Verantwortung.

Was muss sie denn eigentlich hinkriegen?

Und dann sage ich dir, du musst Kontoeröffnungen hinkriegen und die müssen übrigens morgen drei Tage schneller sein, weil die Competition ist auch drei Tage schneller.

Und die müssen irgendwie so und so eine Quote haben, die brauchen irgendwelche Absprungquoten.

Wo gehen die Leute eigentlich verloren?

Wie oft kann man nachfragen?

So etwas kommt ja auf diesen Owner zu.

Und um das quasi sauber auch ownen zu können, will ich an dieser Stelle diesen Gesamtprozess auch verstehen, will ich ihn auch modellieren, will ich ihn auch monitoren können, will ich ihn auch überwachen können, will ich auch eingreifen können, will ich auch im Operating sozusagen den wieder sehen, sag ich, hier laufen gerade 100 Prozesse wild.

Also die laufen da alle auf und dann sehe ich das und dann sehe ich auch, was ist vorher passiert, warum sind die Daten krude und hier sind nicht irgendwelche dead messages, die sich irgendwo auftunen und keiner weiß, wo die herkommen.

Also ich sage nicht, dass man das so bauen muss, aber ich glaube, man will es eigentlich so bauen, weil man genau diese Ownership dann auch machen kann sozusagen.

Und mein Punkt war dann immer, oder ist irgendwie noch der, das widerspricht sich dann überhaupt nicht mit so Domain Driven Design Modularisierung oder Microservices oder auch Entkopplung.

Wenn man das, glaube ich, einfach sauber schneidet und die Granularitäten auch sauber schneidet.

Und dann, ich lasse dich gleich wieder zu Wort kommen, eine Sache noch.

Ich fand das Beispiel schön, wenn wir beim Account Opening oder Kontoeröffnung bleiben, weil Sam Newman hatte das in einem Buch, habe ich auch länger mal mit ihm diskutiert, er hat da auch eventgetriebene Teile drin, sowas wie, sein Beispiel ist hier so ein Bonusprogramm, Loyalty Points Bank, da soll ich noch eingetragen werden, wenn ein Kunde neu aufgenommen wurde.

Und das will ich doch jetzt nicht jedes Mal den Kundenservice anpacken, wenn ich mir irgendwie ein neues Programm ausdenke, wo ich diesen Kunden eben eintrage.

Und da zum Beispiel bin ich ja hundertprozentig dabei.

Also ich würde zum Beispiel in so einem Kunden-Onboarding-Prozess unterscheiden zwischen dieser Phase, für die ich als Komponente Kunden-Onboarding halt auch wirklich zuständig bin.

Und das sind typischerweise die Prüfungen, das sind dann auch wirklich die Anlage in den Kernsystemen und so ein, zwei Dinge.

Und dann bin ich auch fertig und dann darf ich gerne Events erzeugen und darf gerne sagen, hier wurde ein neuer Kunde angelegt.

Und dann können andere auch losgehen ohne meine Kontrolle, ohne dass ich davon weiß und was daraus machen.

Was so ein bisschen impliziert, dass Events grobgranularer sozusagen sind als Prozesse.

Also ein Prozess würde dann eben in diesem Ansatz am Ende vielleicht mal ein Event losschicken?

Muss nicht so sein.

Also typischerweise schicken, ich würde mal sagen, eine Handvoll Events schickt so einen Prozess schon.

Der kann ja auch zwischendurch so meilensteinmäßig, jetzt ist irgendwas passiert, so ein bisschen, was will ich halt die Umwelt auch wissen lassen.

Weil das ist so das andere Ding, was ich nämlich auch glaube, sobald ich ja Events erzeuge, die sind ja auch eine Schnittstelle, die schmeiße ich irgendwo hin und dann darf jemand darauf reagieren.

Und das habe ich ja eben genau nicht mehr unter Kontrolle.

Das heißt, aus einer Wartungsperspektive, wenn ich mir dieses System mal in zwei, drei, vier Jahren angucke und will dieses Event halt wegnehmen, verändern, was auch immer, da muss ich ja erst mal verstehen, was da eigentlich passiert.

Und das ist gar nicht so trivial.

Und deswegen will ich wahrscheinlich im ersten Schritt sparsam sein mit Events, die ich, das ist ja Public API, ist immer schlecht zu ändern.

Aber typischerweise habe ich schon so eine Handvoll, die ich dann eben auch ausfülle.

Was aber eigentlich bedeutet, dass du im Kern sagst, ich will diese fachliche Entität, diesen Prozess irgendwie haben, weil du sagst, es gibt jemanden, der dafür zuständig ist.

Und ich glaube, ein ganz wichtiger Punkt, den du nennst, ist sozusagen auch diese Transparenz.

Also dass man sagt, okay, was passiert denn innerhalb dieses Prozesses und dieses ganze Monitoring, was irgendwie noch mal eine andere Dimension ist.

Also das ist ja nicht Modellierung und Systementwurf, sondern tatsächlich sehen, was macht das System eigentlich.

Genau.

Aber auch auf einem grafischen Modell.

Das ist einfach sehr mächtig.

Genau.

Also, wie soll ich sagen, die Frage, und du hattest ja vorhin gesagt, und das war ja auch so ein bisschen so ein Auslöser für diese Episode, dass es halt sozusagen vollständig kompatibel mit Domain-Driven Design ist.

Da liegt jetzt so ein bisschen die Frage in der Luft, naja, aber also nicht Domain-Driven Design, da gibt es ja nur Kontexte, dann gibt es halt diese Kontexte, diese ganzen Geschichten rund um Strategic Design.

Dann gibt es irgendwie taktisches Design.

Und also meines Wissens nach gibt es halt kein Pattern, was halt sagt, der Business-Prozess.

Und es gibt auch, ich wüsste auch nicht, wo es sozusagen reingehören würde.

Also wir würden ja jetzt über eine Koordination innerhalb, als wenn es eine Koordination innerhalb eines Bonum-Kontext wäre, müsste es halt eben im taktischen Design sein.

Da gibt es sowas nicht.

Wenn es halt übergreifend wäre, hört sich ein bisschen danach an, als wäre es halt eher nicht so.

Also vielleicht ist das zu grob granular.

Da müsste es halt im Strategic Design sein.

Ist da irgendwie eine Lücke oder wie erklärst du dir das?

Oder nehme ich was falsch wahr?

Ich würde zwei Sachen dazu sagen wollen.

Also das eine, also eben auch das Domain-Driven Design kennt eigentlich dieses Process-Manager-Pattern.

Ich frage mich nicht, wo das genau verankert ist, da ich jetzt zu lange nicht mehr in die DDD-Bücher reingeguckt habe.

Aber der Process-Manager ist eigentlich was, was vielleicht nicht in dem DDD-Buch hier so von Eric Evans drinsteht.

Das weiß ich jetzt ehrlich gesagt nicht, aber in der Community dort auf jeden Fall viel diskutiert wird.

Aus einer reinen DDD-Brille, ja, das passiert eigentlich innerhalb eines Bonum-Kontext in einer Domäne.

Also wenn du dir diese hexagonale Architektur anguckst, wäre dann einfach quasi die Workflow Engine nochmal so eine Capability, die ich habe, so dass ich meine Domain-Logik innerhalb dieses Dings auch mit BPMN ausdrücken kann, anstatt mit anderem Code.

So würde ich sagen, passt das in DDD.

Und wenn ich dann quasi integrieren muss, weil ich eben andere Services brauche, dann ist es einfach, ja, ich rede halt mit anderen Kontexten.

Das kann ich ja tun, so oder so.

Zum Beispiel eben über Events, wie du sagtest.

Zum Beispiel, oder einfach über Request-Response, also Commands.

Warum nicht, geht ja auch.

Ja, ich überlege gerade, also damit haben wir eigentlich irgendwie, das Thema mit der zentralen und dezentralen Kontrolle diskutiert.

Das war, glaube ich, irgendwie sehr hilfreich.

Darf ich noch eine Sache sagen?

Ja, sehr gerne.

In der Praxis tatsächlich erlebe ich es aber echt selten, dass das auf dieser Ebene wirklich dann gelebt wird.

Also tatsächlich, weil du sagtest, oder es ist nochmal extra, passiert es außerhalb.

Also wir haben nicht wenige Kunden, die tatsächlich diesen Process Layer, als eigenen Process Layer sehen und etablieren.

Das kommt jetzt, würde ich sagen, nicht unbedingt aus einer Solution Architecture oder aus einer Architektenbrille raus.

Das kommt fast eher aus einer Business Architecture Brille raus.

Und da ist es einfach so ein plakativ schöner Layer.

Und dann sind Prozesse, gerade so Ende-zu-Ende-Geschäftsprozesse, schon so ein bisschen was Eigenes in dieser Welt.

Das funktioniert schon auch sehr gut.

Also ich will mich dem nicht wehren.

Meine Independence Brille ist immer so ein bisschen zu gucken, wo man so steht im Unternehmen, also auch so gedankenmäßig.

Und dann geht das meiner Ansicht nach sehr, sehr gut mit DDD zusammen.

Aber es geht tatsächlich auch gut als eigener Layer zusammen.

Also das halte ich beides für einen total gangbaren Weg, halt mit gewissen Unterschieden dann.

Ja, also fair.

Und ich meine, der Hinweis, dass sozusagen Geschäftsprozesse Geschäftsprozesse sind und dass die da draußen in der Realität existieren und dass es eine gute Idee ist, die als solcher zu modellieren, ist ja total nachvollziehbar.

Insbesondere, wie du gesagt hast, weil es eben etwas ist, wo ich Menschen habe, die dafür verantwortlich sind, die dann dieses Artefakt haben und eben auch sehen können, wie dieses Artefakt in der IT-Welt funktioniert und wie gut das funktioniert.

Und das ist, finde ich, total nachvollziehbar.

Und wie gesagt, das ist so etwas, was so ein bisschen vielleicht mindestens im blauen Buch nicht vorkommt.

Aber deswegen ist es ja eben gut, vielleicht darüber zu reden, dass es eine Ergänzung sein kann.

Damit ist halt auch so ein bisschen, habe ich das Gefühl, diese Frage beantwortet, die wir hier aufgeschrieben haben, von wegen, die Abfolge der Aktivitäten ändert sich doch nicht.

Das heißt also, ich muss vielleicht diesen Prozess, es ist sozusagen nicht so spannend, diesen Prozess hinzumalen, damit man ihn irgendwie ändern kann.

Du hast damit ja gesagt, es ist eine Transparenz, es ist ein Artefakt, was eher Anforderungen erfüllt und vielleicht ist die Änderbarkeit gar nicht der wichtigste Punkt.

Wobei, ja doch, nicht der einzige.

Natürlich ist Monitoring und Sichtbarkeit auch im Monitoring extrem wichtig.

Aber diese Änderbarkeit, also auch diese Diskussion habe ich halt sehr häufig.

Ich glaube, dass es nicht so ist, dass Prozesse, auch Geschäftsprozesse sind nicht mehr stabil.

Vielleicht ist es so am besten ausgedrückt.

Also wir haben so viel Veränderung heute, von einmal technischen Möglichkeiten, also AI vorneweg, aber auch was ich alles, an digitaler Transformation, an IT-Modernisierung.

Also man kann diverse Programme raussuchen, die alle Unternehmen gerade fahren, die alle darauf abzielen, eigentlich auch wirklich Geschäftsprozesse in ihren Grundfesten mal sauber zu rütteln.

Noch dazu kommen ja auch, dass Geschäftsmodelle gar nicht mehr so stabil sind.

Also selbst auch in etablierten Branchen schneidet sich das um.

Ich habe neue Zulieferer, baue mir da andere Sachen zusammen, Open Banking, weiß ich nicht was.

Also sprich, ich glaube nicht daran, dass Geschäftsprozesse so stabil sind, wie wir irgendwie das vor 10 oder 20 Jahren einfach, wie sie da wahrscheinlich auch waren, wo wir dann sagten, naja, aber der Prozess, der ist doch stabil, und wir machen immer noch das Gleiche.

Da glaube ich nicht mehr so dran.

Also von dem her finde ich das trotzdem wichtig, dieser Enderberg halt.

Ja, okay.

Also das ist ja eine Aussage über die Änderung der Fachlichkeit.

Man könnte jetzt noch eine Frage stellen, die ja damit sozusagen im Zusammenhang steht.

Also das Ziel von Softwarearchitekturmodellisierung ist ja eigentlich, irgendwie Änderungen zu begrenzen.

Und was du jetzt irgendwie sagst, ist, naja, wir müssen halt irgendwie auf dieser sehr eher grobgranularen Ebene dann tatsächlich irgendwie Änderungen vollziehen, eben auf dieser Business-Prozess-Ebene.

Ist das eine Niederlage von Modellisierung, sozusagen, nicht?

Nein, nein.

Aber wir müssen das ja anders ausdrücken.

Ziel von Softwarearchitektur ist ja eigentlich, die nötigen Änderungen zu minimieren, um die notwendigen fachlichen Änderungen zu ermöglichen.

Ich muss halt einfach fachliche Änderungen zulassen.

Und dann muss ich Änderungen im System machen.

Also das geht einfach nicht ohne.

Das wäre schön, vielleicht macht das irgendwann der Co-Pilot, aber da sind wir noch lange nicht.

Und das heißt, ich muss diese Änderungen ermöglichen und das zu wenig Aufwand.

Und da hilft eben, glaube ich, genau dieser Prozess, weil ich sage, wenn ich auf der Prozess-Ebene, klar, wenn ich meinen Datenband tausche, hilft mir das nichts.

Aber wenn ich auf der Prozess-Ebene Änderungen machen will, dann hilft mir das, dass ich das an dieser Stelle machen kann und dann eben auch nicht fünf Systeme angucken muss, die alle irgendwie mal diese Nachrichten in die Hand nehmen.

Ich kann vielleicht das auf dieser einen Stelle begrenzen.

Also immer wenn ich Prozessänderungen habe, wird es genau einfacher.

Das macht diese Architektur dann sozusagen.

Genau.

Also der Florian hat bei YouTube geschrieben, ich würde sagen, es gibt in Capital Letters ja den Geschäftsprozess, in der Regel frage ich sowieso um BPM, BPMN, hilft mir erstmal nur, diesen leicht zu modellieren und zu verstehen.

Ich glaube, das ist eine gute Zusammenfassung mit dem, was du gesagt hast.

Dann schreibt er weiter, bei BPM bekommt man meiner Meinung nach die Orchestration, das Treiben des Prozesses sowieso, sowie die Geschäftstransparenz zur Laufzeit und im Business Activity Monitoring praktisch geschenkt.

Das kommt ja auch zu dem, was du gesagt hast.

Und dann schreibt er weiter bei Choreography, z.B.

Event-Driven Architecture ohne Orchestrator muss die Steuerung und Prozesstransparenz anderweitig sichergestellt hergestellt werden.

Was, glaube ich, auch zu dem passt, was du gesagt hast.

Genau.

Dann passt das sozusagen soweit.

Wir sind so ein bisschen am Ende der Zeit.

Wie probiere ich es aus, wäre so die letzte Frage sozusagen.

Machen.

Okay.

Nein, also es gibt, genau, ich empfehle es immer einfach tatsächlich auch wirklich mal auszuprobieren, mal ein bisschen damit spielen.

Das ist ja wieder das Schöne als Techie, das macht ja dann auch ein bisschen Spaß.

Ihr könnt einfach bei uns, Commodore.com, dann könnt ihr das z.B. einfach runterladen und dann haben wir so Get Started Guides, je nachdem, wo ihr steht.

Wenn ihr programmieren wollt, gerne mit Spring.

Einfach mal ein bisschen was machen.

Also ihr solltet da in, ihr könnt auch SARS machen, wenn ihr gar nicht runterladen wollt, dann solltet ihr eigentlich in einer halben Stunde da was am Laufen haben und ein bisschen spielen.

Perfekt.

Dann würde ich sagen, haben wir es soweit?

Oder hast du noch Themen, die du sprechen wollen würdest?

Also viele, aber wir haben ja keine Zeit mehr.

Ja, genau.

Nein, ansonsten, wen noch was interessiert, auch immer gerne auf mich zukommen.

Also mich, tatsächlich interessieren mich die Themen alle im Herzen sehr, von dem her freue ich mich immer über gute Diskussionen.

Genau, ich packe deinen Link zu deinem Mastodon Account, deinem Blue Sky Account und zu deinem LinkedIn nochmal in die Notes, und da kann man dich dann ja auch ansprechen.

So ist es.

Genau, perfekt.

Dann würde ich sagen, vielen Dank.

Schönes Wochenende und wie gesagt, Dienstagabend um 19 Uhr, ich hätte es nochmal nachgeguckt, haben wir dann eben IT in 2034 und wir haben tatsächlich einen längeren Planungshorizont.

Das heißt, am 20. geht es dann mit Ralf, dem Stefan und André zum Thema und mit der Moderation von Lisa zum Thema, was denn nun eigentlich AI für uns bedeutet und was wir damit irgendwie so anfangen können, wenn wir da so einen netten Launchable haben.

Auslöser war, dass Stefan und André einen Kommentar losgeschickt hatten, wo sie dann gesagt haben, AI ist eigentlich underhyped und ich hatte ja gesagt, es sei overhyped und das werden wir jetzt endgültig ausdiskutieren.

Gut.

Dann, wie gesagt, vielen Dank.

Ja, danke, dass ich da sein durfte.

Bis dann.

Tschüss.

So und damit sind wir raus.

Lass mich kurz nochmal...
