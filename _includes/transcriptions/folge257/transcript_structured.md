# Folge 257 - Monolithen zu Microservices - Macht man das noch so? zu Microservices macht man das eigentlich noch so.

## Einführung und Ankündigungen

Und da wollen wir uns nochmal genau mit dem Thema beschäftigen.

Also macht man das eigentlich noch so, dass man halt heutzutage Microservices einsetzt, um halt vom Monolithen wegzukommen.

### Virtuelle Kaffeepausen

Ich packe nochmal kurz ein paar Hinweise in den Chat und habe außerdem nochmal den Hinweis, also wenn ihr dieses Thema oder andere Themen nochmal mit mir privat sozusagen besprechen wollt, es gibt die Möglichkeit, einen virtuellen Kaffee mit mir zu buchen, kostenlos, und eine Stunde mit mir irgendwie zu reden über irgendein Thema, beispielsweise über dieses Microservices-Thema.

Ansonsten kurzer Hinweis auf die nächste Woche.

### Kommende Events

Wir haben nächste Woche zwei Episoden.

Die eine ist am 3.4., das müsste der Donnerstag sein, wenn ich das richtig in Erinnerung habe.

Und da haben wir um 15 Uhr eine Episode zum Thema Wortly Maps mit Software-Architektur mit Simon Wortley, der die Wortly Maps erfunden hat, und Markus Harrer und mir.

Markus ist auch da ein großer Experte in diesem Bereich.

Und dann haben wir am Freitag um 14 Uhr, also eine Stunde später als sonst, Building Product Teams Beyond Organizational and Geographical Boundaries mit Anna Nath und Leja Bulovic.

Das beides live von der Agile-Architecture.

Gut, soviel zum Vorspann und zu den Themen, die uns dann demnächst erwarten.

Heute soll es ja um das Thema gehen, will man eigentlich noch Monolithen aufteilen in Richtung Microservices.

Ich habe ein Buch geschrieben über dieses Thema mit den Microservices, von daher ist das ein Thema, was mir ein bisschen naheliegt.

Führt erstmal zu der Frage, was sind denn eigentlich Monolithen?

## Arten von Monolithen

Ich würde behaupten, es gibt zwei unterschiedliche Arten von Monolithen, die wir unterscheiden können.

Das sind einmal die Architekturmonolithen und dann die Deployment Monolithen.

### Architekturmonolithen

Architekturmonolithen sind Dinge, die irgendwie untrennbar sind, keine guten Strukturen haben, keine gute Aufteilung.

### Deployment Monolithen

Und ein Deployment Monolith ist etwas, was wir nur als Ganzes deployen können, wo wir also nicht einzelne Sachen deployen können.

## Probleme mit Monolithen

Wenn man davon weg migrieren will, dann impliziert das so ein bisschen, dass die ein Problem haben.

Was zu der Frage führt, warum sollte das ein Problem sein?

### Deployment-Geschwindigkeit

Und bei einem Deployment Monolithen ist eben offensichtlich das Problem, dass ich ein langsames Deployment habe.

## Continuous Delivery

Und schnelles Deployment hat zahlreiche Vorteile.

Ich habe eine Episode gemacht über diese DevOps-Studie und am Ende ist es eben so, dass ich durch Deployen, wenn ich öfter deploye, in so einen kontinuierlichen Prozess reinkomme, wo ich Software in Produktion übergebe und dadurch herausfinde, wo jetzt auf dem Weg in Produktion und im Softwareentwicklungsprozess insgesamt meine Bottlenecks sind.

Also vielleicht sind meine Tests die Bottlenecks, vielleicht ist es so, dass ich Änderungen erst mal genehmigen muss, bevor sie tatsächlich umgesetzt werden.

Und das ist irgendwie mein Bottleneck.

Und wenn ich jetzt versuche, die Geschwindigkeit zu erhöhen im Deployment, dann eliminiere ich schrittweise Bottlenecks.

Und was diese DevOps-Studie zeigt, ist, dass am Ende halt dabei qualitativ hochwertige Software herauskommt und ein besserer Prozess, ein produktiverer Prozess.

Und tatsächlich, ich habe eben auch vor sehr langer Zeit ein Buch geschrieben über das Thema Continuous Delivery.

Tatsächlich ist es eben so, dass das ein bisschen die Motivation für mich war, dieses Buch überhaupt zu schreiben über Continuous Delivery, weil ich eben durch Continuous Delivery glaube ich viel besser mit Softwareentwicklung zurechtkomme, als wenn ich mit einer zitternden Hand am Sonntag vor dem Rechner sitze und sage, jetzt deploye ich das Zeug und ich muss es heute machen, weil niemand online ist.

Und wenn es morgen nicht funktioniert, habe ich am Montag ein großes Problem.

Sondern wenn ich das ständig mache, bin ich in einem besseren Prozess.

Der Mev, wenn ich das richtig ausspreche von Twitch, sagt gerade, die Unterscheidung zwischen Architekturmonolithen und Deploymentmonolithen finde ich interessant.

Ich komme aus einer Firmwareentwicklung, Embedded Software, Bare Metals oder Airtos, kein Embedded Linux.

Ich denke, hier hat man häufig Deploymentmonolithen.

Bei der Architektur bin ich unsicher, ist die Unterscheidung Microservices, Monolithen beziehungsweise diese Begriffe auf Firmware generell anwendbar?

Also ja, ein Architekturmonolith kann ich halt dann noch haben, also ein System, wo ich eben keine vernünftige Strukturierung habe.

Und du hast recht, das ist eben inhärent dann eben ein Deploymentmonolith, weil ich eben alles auf ein System deployen muss.

Und das weist schon ein bisschen darauf hin, dass sozusagen ein Deploymentmonolith nicht per se unbedingt etwas Schlechtes sein muss.

Also in gewisser Weise spiele ich da jetzt ein Trade-off.

Das heißt also, ich investiere möglicherweise die Zeit und den Aufwand, um das System in mehrere getrennte Deploymenteinheiten aufzuteilen.

Das ist also der Aufwand, den ich betreibe.

Und auf der anderen Seite habe ich dafür dann eben ein schnelleres und einfaches Deployment von getrennten Teilen.

Und das, was eben diese DevOps-Studie zeigt und was auch insgesamt das zeigt, ist, dass ich verschiedene Bereiche habe, wo ich halt Deployment optimieren kann.

Und diese Aufteilung Microservices ist nur eine.

Also interessanterweise ist es eben so, dass das Buch, was es dazu gibt, zu der DevOps-Studie, dieses Accelerate, in dem Architekturkapitel gar nicht sagt, wir sollten übrigens Microservices machen, sondern es sagt eigentlich, naja wir sollten halt irgendwie eine vernünftige Architektur bauen, die uns ermöglicht, möglichst unabhängig voneinander Änderungen durchzuführen.

Das ist bei einem Architekturmonolithen, also bei einem System, was ja keine vernünftige Struktur hat, wahrscheinlich nicht der Fall.

Bei einem Deploymentmonolithen kann es schon der Fall sein.

Ich habe dann aber eben immer noch das Problem, dass ich vielleicht irgendwie alles gemeinsam deployen muss.

Und das bedeutet halt, dass ein Deploymentmonolith für mich eine valide architekturelle Entscheidung ist.

Und das ist eben etwas, was man eben so machen kann.

Kommen wir zu dem Architekturmonolith.

Das bedeutet eben, dass dieser schlechte Ruf, den vielleicht Monolithen haben und er dazu führt, dass man sagt, naja wir wollen in Richtung von Microservices migrieren, dass der eben vielleicht gar nicht so richtig berechtigt ist.

Jetzt haben wir auf der anderen Seite den Architekturmonolithen.

Das ist also ein System, was halt irgendwie keine vernünftige architekturelle Struktur hat, also nicht gewachsene Strukturen, könnte man das auch nennen, wenn man es nett umschreiben möchte.

Ich habe vor einiger Zeit, ich verlinke das später auch nochmal in den Shownotes, eine Episode gemacht zum Thema Big Ball of Mud.

Und ich würde sagen, das ist so ein bisschen synonym.

Und das was halt interessant ist, ist, dass Big Ball of Mud in dem Paper zum Big Ball of Mud steht, dass das angeblich die populärste Architektur ist, die wir sozusagen haben.

Und ich kann mir das tatsächlich vorstellen, weil schnell mal irgendwas zusammenwerfen und sagen, okay, ich baue mal da irgendwas.

Ich mache mir keine Gedanken über Strukturen.

Das ist eben etwas, was einfach ist und mich ja auch erst mal schnell zu irgendetwas bringt.

Aber dann hat irgendwann ein Problem, weil das System eben langfristig schwer verstehbar, schwer änderbar ist und so weiter.

Das heißt, in gewisser Weise ist das ein Unfall.

Aber auf der anderen Seite vielleicht auch nicht.

Ich glaube halt, dass so eine Vernachlässigung von Strukturen typischerweise ein Ergebnis davon ist, dass man reckless ist.

Also ich habe auch eine Episode gemacht zum Thema Technik-Adept und da kommt so ein bisschen eben diese Idee raus, dass man durch reckless, wo man also rücksichtslos schnell vorgeht, dass dann eben Technik-Adept entsteht.

Möglicherweise ohne, dass ich das überhaupt weiß, weil ich gar keine Zeit habe.

Ich glaube, das ist der Grund, weswegen wir irgendwie so viele Big Balls auf matt haben und so viele Architektur-Monolithen.

Und das wird irgendwie durch Microservices logischerweise auch nicht besser.

Jetzt gucke ich gerade, was der B.

Garon geschrieben hat bei Twitch.

Ich könnte mir vorstellen, auch bei sehr komplizierter Firmware könnte es Sinn machen, zum Beispiel die Architektur um einen Message-Bus zu gestalten.

Dann wäre ich vielleicht wirklich in einem verteilten System.

Message-Bus ist typischerweise etwas Verteiltes.

Lustigerweise ist es ja so, dass, wenn ich es richtig sehe, in Autos dieser Canvas existiert, der eben tatsächlich dafür sorgt, dass verschiedene Sachen miteinander kommunizieren.

Das ist also in gewisser Weise vielleicht eben so eine Art Microservices-Architektur.

Ich glaube auch dadurch inspiriert, aber nicht mein Fachgebiet, dass Zulieferer irgendwelche Sachen zuliefern.

Da habe ich dann vielleicht auch so einen Ansatz, dass ich verschiedene Teile getrennt deployen kann und verschiedene Maschinen habe, verschiedene Teile, die kontrolliert werden müssen im Auto und dass die mit dem Bus miteinander reden.

Das hatte ich mir jetzt noch aufgeschrieben, sozusagen als weiterer Begriff.

Also dieser berühmte Distributed Monolith.

Das ist das, was passiert, wenn ich ein Architekturmonolith oder etwas Ähnliches, also ein Big Ball of Mud, baue mit Microservices.

Dann habe ich eben ein System, wo ich am Ende eben keine vernünftige Struktur habe und ein verteiltes System.

Mark M. hatte vorher mich auf LinkedIn noch kontaktiert und hat eine Frage in diese Richtung gestellt.

Mein Hinweis wäre da eben, dass es letztendlich eben auch wie ein Big Ball of Mud so etwas passiert eben und eben genau an der Stelle, wo ich dann irgendwie reckless vorgehe und mir halt aus Druck keine Gedanken mache über Architektur oder es halt absichtlich vernachlässige und halt eine komische Architektur baue.

Was eben wiederum bedeutet, dass die architekturelle Struktur natürlich durch Microservices nicht besser wird und ich glaube diese Distributed Monolith können halt ein Ergebnis davon sein, dass man sich vielleicht von Microservices gewünscht oder geglaubt hat, dass die Architektur Probleme lösen und das tun sie halt nicht.

Also wenn ich keine vernünftige Struktur habe, wird es nicht dadurch besser, dass ich jetzt meine nicht vorhandene Struktur auch noch verteile, sondern dann habe ich halt immer noch ein schwieriges System.

Ich gucke gerade, was hat der TTY 0482 geschrieben.

Man kann ja absolut auch mit Microservices ein Deployment Monolith bauen und damit hohem Aufwand ein abgestimmtes Set an Ständen nach längerem Freeze nach Proc Deployen.

Da hat der Alexander Herold geschrieben, ja das habe ich auch schon erlebt.

Ich würde da von einem Distributed Monolith vielleicht sprechen.

Für mich ist halt das getrennte Deployment erstmal eine technische Eigenschaft und einen Docker Container kann ich eben getrennt von allen anderen Docker Containern aktualisieren.

Das wäre für mich dann was Microservices mäßiges.

Wenn ich aber nur ein Ding habe und nicht mehrere Docker Container, dann habe ich eben nach meinem Empfinden Deployment Monolithen.

Also das ist ein guter Punkt.

Ich kann eben sozusagen ein System aus Microservices haben, was mich trotzdem dazu zwingt, das gemeinsam zu deployen und dann habe ich eben auch den Sinn wieder oder habe ich eben diesen Vorteil nicht.

Es kann übrigens trotzdem sinnvoll sein, weil ja Microservices beispielsweise auch getrennte Skalierbarkeit anbieten und die habe ich dann eben immer noch.

Was sich dadurch halt schon mal so ein bisschen ergibt ist, eigentlich ist halt diese fachliche Architektur wichtiger.

Also ich muss mir halt die Frage stellen, ich habe irgendwelche Funktionalitäten.

Funktionalitäten in meinem System irgendwo verorten.

Quizfrage, wo tue ich das und welche Sachen sind zusammen irgendwo implementiert.

Also in einem Teil eines Deployment Monolithen oder in einem Microservice.

Wenn ich diese Frage nicht vernünftig beantworte, dann habe ich halt ein Architekturproblem oder wahrscheinlich ein Problem in Bezug auf langfristige Wartung und Weiterentwickelbarkeit und zwar unabhängig davon, ob ich Microservices benutze oder irgendetwas anderes.

Ich habe Montag auf dem Software Architecture Summit einen Workshop gehalten und da hat er mir genau diese Frage gestellt.

Also ist irgendwie eine technische Architektur wichtiger oder eine fachliche.

Ich hatte also unter technischer Architektur sowas wie Onion oder Schichten oder so was halt verstanden, wo ich ja auch jetzt sage, bestimmte technische Teile sind irgendwo verortet.

Nicht in der Schichtenarchitektur weiß ich, es gibt eine UI-Schicht.

Das heißt, die technischen UI-Sachen sind eben in der UI-Schicht.

Die Logik-Schicht enthält die Logik.

In der fachlichen Architektur ist die Frage, wo irgendwie Fachlichkeit verortet ist.

Da kam eben mit einer relativ großen Mehrheit heraus, dass die fachliche Architektur wichtiger ist.

Wir hatten da noch eine Diskussion, aber am Ende ist das eben etwas, was zumindest einer Mehrheit klar ist, was wiederum bedeutet, dass die Frage nach solchen technischen Dingen wie bauen wir jetzt Microservices oder Monolith eigentlich klar sekundär ist.

Deswegen ich eben nicht verstehe, warum da so ein großer Fokus eigentlich draufsitzt.

Ein Hinweis noch, also da war halt auch diese Frage zu sowas wie Data Streaming.

Da gibt es halt, das hat der Mark M. auch gefragt, da gibt es halt offensichtlich so eine Aussage im Sinne von, sollte man da Monolithen machen oder nicht.

Das erinnerte mich auch an eine Episode, die ich vor einiger Zeit gemacht habe.

Das ist die Episode zu diesem Paper, wo Amazon angeblich, so die Lesart der breiten Mehrheit, weggegangen ist von Microservices hin zu einem Diplom mit Monolithen.

Was da wirklich passiert ist, die haben ein System gebaut, um bei Amazon Prime Video die Qualität der Videostreams zu monitoren.

Das hatten sie erst mit Function as a Service gebaut.

Da gibt es verschiedene Algorithmen, die jetzt sagen, ob die Bilder okay sind oder nicht.

Die haben sie jeweils als Function as a Service implementiert und haben dann darum herum noch eine Logik, die diese Bilder rendert und bewertet.

Das haben sie gemacht, damit sie schnell Ergebnisse produzieren können.

Das hat offensichtlich auch funktioniert.

Dann haben sie in der Produktion gemerkt, dass diese Variante zum einen wahnsinnig langsam ist, weil sie ein Bild rendern, ablegen in S3 und dann holen sich die Algorithmen das von S3 runter.

S3 ist ein Object Store, wo ich größere Datenmengen ablegen kann und das sind teure Operationen.

Das heißt, es ist langsam und zum anderen auch teuer, weil ich viele Function as a Service Aufrufe habe.

Dann haben sie festgestellt, dass es cooler ist, alles wieder zusammen zu merken in einem System.

Ich glaube, dass man daraus einmal ableiten kann.

Es gibt bestimmte Fälle, wo diese sehr kommunikationslastigen Services vielleicht besser in einem Monolithen aufbewahrt sind, weil das etwas ist, wo nicht viele Microservices über so etwas wie S3 miteinander reden oder über Message Bus, wie wir gerade gesehen haben, sondern es sind lokale Methodenaufrufe und das deutlich schneller.

Wenn ich sage, guck mal, da ist das Bild im Speicher, nimm das und analysiere das, ist es natürlich unfassbar viel schneller, als wenn ich das von einem Storage runterhole.

Da gibt es auch die alte Riegel von dem Martin Fowler aus dem letzten Jahrhundert, von wegen Don't Distribute Your Objects, also verwende keine verteilten Objekte, keine verteilte Kommunikation.

Aber am Ende haben die in diesen beiden Phasen ihre Ziele erreicht.

In der ersten Phase haben sie schnell etwas auf die Reihe bekommen.

In der zweiten Phase haben sie die Produktionskosten gesenkt.

Das ist für mich eine evolutionäre Architekturweiterentwicklung.

Ich finde das völlig okay.

Ich glaube nicht, dass man daraus ableiten kann, dass die eine Architekturentscheidung am Anfang oder die spätere Architekturentscheidung falsch ist.

Die erste Architekturentscheidung war, dass wir schnell zu Ergebnissen kommen.

Das haben sie erreicht.

Die zweite Architekturentscheidung, da sind im Empfang schneller Service genutzt worden.

Die zweite Architekturentscheidung, von dem größeren System, war aufgrund von Kosten.

Damit haben sie ihr Ziel erreicht.

Ich glaube, das ist auch fein.

So viel zu Monolithen.

Auf der anderen Seite haben wir diese Microservices.

## Microservices

Die sind ein bisschen schwer zu definieren, weil es eben nicht die eine Definition gibt und auch von Anbeginn nicht.

Microservices waren von Anbeginn etwas, was unterschiedliche Menschen in unterschiedlichen Kontexten ausgenutzt haben.

Deswegen gab es auch leicht unterschiedliche Variationen davon.

### Verschiedene Ansätze

Netflix hatte da eine Pionierrolle.

Die haben starke, synchrone Microservices mit tiefen Aufruf-Hierarchien gebaut.

Der Jan Kocroft ist jemand, der sich dort gekümmert hat.

Am anderen Ende ist es so, wie der Fred George, der gesagt hat, wir haben asynchrone kommunizierende Services, die miteinander reden.

Das sind tatsächlich zwei gleichberechtigte Menschen, die gesagt haben, das ist aber ein ähnliches Konzept.

Das ist etwas, was wir jetzt Microservices nennen wollen.

## Fachliche vs. Technische Architektur

Das bedeutet, es sind synchrone oder asynchrone kleine Dinge, die ich deployen kann.

Ich brauche deswegen eine Infrastruktur, in die ich das deployen kann.

Heutzutage typischerweise Kubernetes.

Es wird dann so sein, dass ich mir wahrscheinlich eine Kommunikation als Standard überlegen muss, wie ich diese Microservices zusammenbekommen kann.

Dafür kann ich so etwas wie in der Programmiersprache freigeben.

Alexander hat gerade geschrieben, dass die Daten im Lokal sind.

Das ist ein wichtiger Punkt.

Hadoop und HBase sind Systeme im Bereich von MapReduce, wo man versucht, die Aufgabe auf verschiedene Rechner zu verteilen und dafür zu sorgen, dass das parallel auf mehr Rechner erledigt wird.

Das kann man gut auf Microservices übertragen.

Ich fand es erstaunlich, dass man versucht, Module aneinander zu koppeln, indem man erst drei Buckets nutzt.

Ich bin mittlerweile so aufgestellt, dass ich das nicht aus einer technischen Perspektive sehen wollen würde.

Ich würde das eher aus einer Modularisierungsperspektive sehen.

### Modularisierung

Ich würde mir wünschen, dass ich Module habe, die die Daten verstecken und die intern haben.

Mein Beispiel ist immer, dass ich etwas habe, das Konten verwaltet.

Jetzt will ich auf den Kontostand zugreifen.

Das sollte intern gespeichert sein.

Wenn ich von draußen die Anfrage bekomme, möchte ich den Kontostand haben, dann kommt von innen entweder der Kontostand direkt zurück, weil er direkt abgespeichert ist, oder ich berechne ihn aus den Transaktionen.

Das bedeutet, dass ich eine Logik habe, die mir sagt, was der Kontostand ist.

Die Daten sind versteckt.

Dann muss aber eine Funktionalität, die dort zu dem Konto gehört, bei dem Konto implementiert sein.

Das ist eine Modularisierungsfrage.

Das ist für mich, so wie ich das zumindest sehe, der richtigere, der wichtigere Ansatz, als wenn ich jetzt versuche zu sagen, die Daten sollen im Lokal sein.

Jetzt hat der Mev geschrieben bei Twitch, weil mir der Begriff Microservices nicht ganz klar ist.

Kann es Microservices auf einem einzelnen Node geben, bei dem die Module statisch gebaut und gelinkt werden?

Oder so spezifisch? schnell zu sowas wie Docker-Containern oder Functions as a Service oder vielleicht auch getrennte virtuelle Maschinen.

Also ich habe eben Dinger oder mindestens Betriebssystem-Prozesse und dadurch erreiche ich halt, dass ich die getrennt skalieren kann, dass sie halt auch, wenn es Schwierigkeiten gibt, wenn ich mir zum Beispiel ein Memory-Leak habe oder ein CPU-Problem mit der CPU-Auslastung, dann kann ich dort eben auf das Betriebssystem vertrauen.

Das Betriebssystem wird dafür sorgen, dass eben die Querschläger sozusagen beseitigt werden, während wenn ich ein Monolithen habe, dann sind das halt Module, die gemeinsam in so einem Prozess leben.

Das führt dazu, dass die eben nicht isoliert sind bezüglich CPU, nicht isoliert sind bezüglich Speicher und eben auch nicht isoliert sind bezüglich Deployment und das ist für mich sozusagen der wesentliche Unterschied.

Aber wie schon gesagt, das ist halt meine persönliche Aussage.

Der Begriff Microservices ist eben nicht so richtig, richtig gut fassbar und also bedankt sich halt gerade.

Ich glaube auch, dass der Bezug auf Prozesse hilfreich ist, sagt er oder sie.

Das glaube ich, ist mir auch tatsächlich ein Thema.

Warum würde ich jetzt ein System in Microservices aufteilen wollen?

Also ich habe dazu Vorteile.

Ich kann mein System in eine größere Unabhängigkeit letztendlich treiben, nicht durch diese Isolation und tatsächlich ist da vielleicht noch so ein Punkt, dass man halt, auch das ist so eine Folge, die ich immer mal gemacht habe, zu diesem Thema mit der Abhängigkeit.

Also es gibt eben unterschiedliche Arten von Abhängigkeiten.

Hier kann ich jetzt eben zum Beispiel dafür sorgen, dass ich eine Basistechnologie in einem Lokal für ein Microservice entscheide.

Also ich habe einen, der benutzt Java, Springboot, einen anderen benutzt Python.

Ich kann jetzt grundsätzlich erstmal das überhaupt ermöglichen, während ich halt beim Diplomamonolithen da voraussichtlich limitiert bin.

Und selbst, wenn ich jetzt sage, wir bauen alle Java-Systeme oder wir bauen alle ein Springboot-System, ist es halt so, dass ich zum Beispiel ein Update auf eine neue Version von Springboot oder Java oder was auch immer in einem Microservice machen kann, was also das Risiko minimiert und dafür sorgt, dass ich eben das Update erstmal dort machen kann, wo es mir besonders viel hilft.

So und wir sind jetzt an so einer Stelle, also der tty0482 hat geschrieben, ich kann mir vorstellen, dass man durchaus Microservices in Frameworks bauen kann.

Da müssen eben einzelne Prozesse zur Laufzeit ausgetauscht werden können.

Bin nicht sicher, was du damit sozusagen meinst.

Also natürlich ist da irgendwo ein Kontinuum.

Also ich kann jetzt eben Prozesse haben, ich kann Docker-Container haben, die haben dann getrennte Filesysteme und so weiter.

Also ich kriege da halt immer mehr, wie soll ich sagen, so unterschiedliche Arten von Entkoppelung hin.

Also Firmware steht hier gerade.

Also das bedeutet, ich kann mir durchaus vorstellen, dass man Microservices in Firmware bauen kann.

Ja, vielleicht kann man das.

Dann wäre das halt irgendwie ein Ansatz, den man da vielleicht auch verwenden will.

Aber da ist wieder die Frage, brauche ich das und bringt mir das was?

Und nicht.

Das ist so ein bisschen das, was glaube ich insgesamt eine Herausforderung ist.

Nämlich die Frage, lohnt es sich Microservices zu verwenden?

Und das kann man jetzt an diesem Beispiel, was ich gerade hatte, illustrieren.

Also ich habe die Möglichkeit, Technologien freizugeben.

Das geht erst mal.

Das impliziert aber organisatorische Maßnahmen.

Das heißt, ich müsste jetzt mit den Teams sagen, ihr dürft das entscheiden.

Und das kann ich relativ schnell und einfach kontrollieren, indem ich sage, schön, dass wir Microservices machen.

Ihr müsst alle folgendes Framework benutzen in genau dieser Version und kann dadurch diesen Vorteil kassieren und den nicht umsetzbar bekommen.

Und am Ende ist das etwas, was mit sozialen Dingen zu tun hat, nach meinem Empfinden.

Also zum Beispiel mit so etwas wie Vertrauen.

Also wenn ich jetzt tatsächlich den Teams sage, ihr dürft machen, was ihr wollt.

Und ich glaube, dass die Entwickler ihre Spielkinder sind.

Dann kann ich mir sehr gut vorstellen, dass man sagt, das kann ich nicht tun, weil die arbeiten unverantwortlich und treffen Entscheidungen.

Und ich kriege am Ende einen Wildwuchs.

Ich kann jetzt argumentieren, warum es im Interesse eines Teams ist, dieselbe Technologie wie andere zu benutzen.

Nämlich einfach deswegen, weil es einfacher ist.

Wenn die anderen schon Java oder Microservices gebaut haben oder was auch immer es ist, .NET Core oder was auch immer.

Dann ist es für mich einfacher, dasselbe zu bauen, weil ich weiß ja schon, wie diese Dinge betrieben werden, wie die umgesetzt werden.

Und ich kann denen sagen, gib mir doch mal so ein Template.

Dann wäre mein verantwortungsvolles Verhalten, möglichst das zu nutzen.

Außer es gibt gute Gründe, die dagegen sprechen.

Weil ich diese Technologie vielleicht überhaupt gar nicht beherrsche.

Und dann ist es aber vielleicht gut, dass ich eine andere Technologie benutze.

Es ist eine verantwortliche Entscheidung.

Der andere Punkt, den ich schwierig finde, ist, wenn ich Menschen habe, die unverantwortlich handeln.

Wenn das tatsächlich der Fall ist, dann bin ich mir unsicher, ob ich das dadurch einfange, dass ich sie stärker kontrolliere.

Das ist jetzt aber ein Thema, das ich diskutieren muss.

Ich muss jetzt anfangen und sagen, diese Technologiefreiheit nutzen wir oder eben auch nicht.

Und by the way, ich finde es jetzt gar nicht ethisch verwerflich, wenn man sagt, das machen wir nicht, weil ich vertraue euch nicht.

Das ist dann eben so.

Und vielleicht gibt es dafür auch Gründe.

Es gibt ja durchaus Sachen, wo man sagen muss, dass EntwicklerInnen oder auch andere Menschen Vertrauen enttäuscht haben.

Und dann ist es vielleicht nachvollziehbar, warum man denen jetzt nicht mehr vertraut.

Das unabhängige Deployment ist für mich besonders, weil es da nicht so viele Alternativen gibt und weil das in Bezug auf diese Geschwindigkeit wichtig ist.

Wobei man auch eine gewisse Geschwindigkeit mit Monolithen hinbekommt.

Aber dann muss ich auch neben der Aufteilung von Microservices die Continuous Delivery Pipeline aufteilen und damit auch die Tests.

Dann müsste ich sagen, ich habe einzelne Microservices, die ich getrennt testen und deployen kann.

Denn sonst wird das Deployment eben nicht so schnell, weil ich alles gemeinsam monolithisch testen muss.

Und das ist wahrscheinlich deutlich aufwendiger und da gibt es größere Probleme in Bezug auf das Zeitbudget im Vergleich zu dem, dass ich die Sachen deploye.

Das Deployment wird wahrscheinlich nicht so lange dauern wie die ganzen Tests.

Das halte ich für unwahrscheinlich.

Was also bedeutet, dass ich vermutlich dann eben auch insbesondere in der Aufteilung der Tests investieren muss.

Julian Wirzbicki fragt, Geschwindigkeit mit der ich Veränderungen in Betrieb nehmen kann?

Genau, also der Durchlauf durch einen Prozess von ich habe ein Requirement bis es ist halt in Produktion oder zumindest in einer Staging Umgebung.

Eine Sache, die man zumindest am Anfang auch für Microservices so ein bisschen, also schreibt der Alexander, in dem Fall würde ich mir mal Doremetrigen anschauen.

Genau das ist das, was ich in dieser Episode rund um das Thema die DevOps-Studie, packe ich auch noch mal in die Show Notes, wie gesagt, zitiert habe.

Genau diese Doremetrigen und die sagen eben, dass genau diese Deployment-Geschwindigkeiten also von Requirement bis in Produktion ein wichtiger Optimierungspunkt sind.

Achso, eine weitere Eigenschaft, die wir an Microservices haben, die am Anfang glaube ich insbesondere so ein Thema war, ist die Ersetzbarkeit, also dass ich die wegwerfen kann und neu bauen kann.

Ich finde das ehrlich gesagt schwierig, weil ich dadurch glaube ich eher zu kleinen Microservices komme und zu vielen Microservices und ich verstehe auch nicht so richtig, wo der Wert ist.

Ich habe eher das Gefühl, dass das irgendwie dazu führt, dass man sagt, naja, also ich komme halt in so einen Bereich, wo ich halt ständig die Microservices neu schreibe und wegwerfe und ich wüsste nicht, warum ich das tun sollte.

Deswegen finde ich diese Ersetzbarkeit nicht so übermäßig wichtig.

Es ist natürlich ein Vorteil, weil ich eben nicht jetzt beispielsweise alles komplett neu bauen muss, wenn ich halt irgendwo eine neue Technologie haben will oder irgendwo jetzt nicht das Machine Learning Zeug mit Python schreiben will und das Rest so lassen will, wie ich halt habe.

TTY 0482 schreibt, wenn ich gute automatisierte Tests und sinnvolle modularen Pipelines habe, kann ich ja durchaus auch Monolithen schnell ändern und deployen.

Modulare Pipelines weiß ich nicht, weil nicht ein Deployment Monolith bedeutet, dass ich eben alles deployen muss und ich würde es wahrscheinlich dann auch noch mal alles durchtesten.

Deswegen weiß ich nicht, ob ich sowas halt umsetzen kann mit einem Deployment Monolith.

Also ich vermute mal, dass bedeutet, dass ich nur ein Teil teste und dann das gesamte deploye.

Kann man vielleicht machen.

Und ja, also mit diesem guten automatisierten Test komme ich halt auch relativ weit.

Und das ist ja genau das, was ich halt sage.

Und diese, wie soll ich sagen, die Geschwindigkeit, das was bei den Neurometrigen steht, das ist ja gerade der wesentliche Punkt bei den Neurometrigen.

Das hängt eben nicht von einem einzigen Schalter ab, sondern es ist etwas, wo ich mehrere Schalter einschalten kann.

Und irgendwann komme ich vielleicht dazu, dass eben mein Problem ist, dass das ein Deployment Monolith ist und dann muss ich es auflösen.

Aber bis dahin werde ich wahrscheinlich viele weitere Maßnahmen erreichen können.

Julian schreibt noch, aber habe ich dann nicht die Selberwerte in der Modularisierung, bloß bei den Tests, nicht beim eigentlichen Produkt?

Genau.

Und also das muss ich halt tun und mindestens in Richtung Microservices.

Und es ist ja eine Bedingung dafür, dass ich am Ende eben tatsächlich getrenntes Deployment habe.

Und das ist etwas, was gerade so bei Monolith zu Microservices durchaus etwas sein kann, was halt aufwendig ist und schwierig ist.

Oliver hat geschrieben, warum würdest du in einem Monolith nochmal alles durchtesten, gehst aber davon aus, dass es ein Microservices-System ausreicht, lediglich einzelne Services zu Integration testen?

Ja, guter Punkt.

Also einmal ist es halt so, das hängt damit zusammen, dass ich halt bei Microservices wirklich garantieren kann, dass eben nur der eine Microservice geändert wird und die anderen Sachen bleiben, so wie sie sind.

Bei einem Monolith wäre ich mir nicht ganz so sicher, aber ja.

Also wenn ich zum Beispiel einen JAR-File dazu packe, was vorher gebaut worden ist, dann kann ich das vielleicht irgendwie auch sozusagen zusichern.

Und ja, also Oliver schreibt halt gerade noch mit einem strukturierten Monolith, klar.

Ich habe dann noch, also da stand jetzt noch, achso, das für den Integrationstest, das ist auch noch ein guter Punkt.

Das ist ja ein Problem.

Das heißt also, wenn ich jetzt viele, wenn ich versuchen möchte, unabhängig zu deployen, will ich idealerweise keinen Integrationstest machen, weil die Integrationstests sind halt eigentlich ein Bottleneck.

Also weil ich dann verschiedene Sachen zusammenbringen muss und dort halt dann diese ganzen Sachen zusammen Integrationstesten muss.

Und wahrscheinlich muss man dann über alle Microservices sozusagen eine Serialität herstellen.

Also man muss dann irgendwie dafür sorgen, dass der eine Microservice in der neuen Version getestet wird, der geht in Produktion.

Dann wird der nächste Microservice in der neuen Version getestet im Integrationstest und der geht dann in Produktion und so weiter und so weiter.

Also ich kann nicht mehrere Microservices gleichzeitig ändern, weil ich im Integrationstest wahrscheinlich einen zurzeit nur als neue Version testen will, damit ich herausbekomme, wer jetzt verantwortlich ist.

Und dem kann ich entgegenwirken, indem ich konsumative Contract-Tests mache und dadurch teste ich die Systeme darauf, ob sie wechselseitig Contracts einhalten.

Und ich habe dann eben nicht so einen monolithischen Test, sondern ich teste das Zusammenspiel zwischen zwei Microservices, dadurch dass ich ein Contract habe und schaue, ob der andere Microservice den Contract einhält, von dem der Microservice glaubt, dass er eingehalten werden muss.

Und deswegen kann ich den Integrationstest dann letztendlich sozusagen dort einsparen.

Das könnte ich vielleicht bei Deployment-Monolithen auch machen.

Ich glaube, dass bei den Microservices noch hinzukommt, dass der Rückweg einfacher ist.

Ich muss nur ein Microservice zurückfallen lassen auf die alte Version, nicht an die Deployment-Monolithen.

Und das bedeutet, wenn es schief geht, habe ich vielleicht leichteres Spiel, da etwas zu machen.

Jetzt hat Oliver geschrieben, was hat er noch geschrieben?

Also Oliver hat geschrieben, er nimmt ein strukturierter Monolith.

Dann hat Julian geschrieben, das wäre ja dann der perfekte Monolith.

Auch nicht wahrscheinlich mit so einem Zwinker-Smiley.

Doch, ich kann Monolithen mit einer Struktur versehen und garantieren, dass die existiert.

Spring Modulist, woran viel der Zufall so spielt, Oliver arbeitet, ist ein Werkzeug dafür.

Oder wir haben auch ganz viele Episoden zum Thema Software-Architektur Management.

Ich würde unterschreiben, dass ein Monolith, der nicht mit solchen Werkzeugen versehen ist, tatsächlich dazu neigt, dass man Abhängigkeits-Chaos zwischen den Modulen hat.

Und das war ja auch einer der Gründe, weswegen man zumindest am Anfang gesagt hat, Microservices sind eine gute Idee, weil ich da diese stärkere Modularisierung habe.

Ich habe irgendwie Betriebssystem-Grenzen.

Und wenn ich jetzt sage, ich habe hier eine Klasse und ich führe eine Abhängigkeit zu einer anderen Klasse ein, das ist schnell gemacht und passiert dann vielleicht auch irgendwie als Unfall.

Aber wenn ich jetzt sage, ich habe hier ein Microservice und ich will den Microservice benutzen, das ist aufwendiger und deswegen mache ich mir da wahrscheinlich Gedanken, was dazu führt, dass die Modularisierung wahrscheinlich eher durchgehalten wird.

Ich finde das aber nicht ausreichend, um keine ausreichende Motivation um Microservices einzusetzen, weil das kann ich eben auch mit Architektur-Management oder Spring Modulist was ich halt mache.

Oliver hat auch geschrieben, Änderungen in einem Microservice heißt ja nicht, dass es keine Auswirkungen auf andere Microservices gibt.

Genau, aber dann kann ich halt versuchen, das zurückzurollen.

Das ist wahrscheinlich einfacher.

Kommt darauf an, ob man das äußere Verhalten ändert oder nicht, schreibt jetzt Julian.

Oliver schreibt ja schon, aber das sieht die Build-Pipeline der Änderung ja nicht an.

Hinweis dann von TTY 0482.

Dafür gibt es ja Packt und so, Blue Screen, Green Deployment, Asymmetric Monitoring und so.

Dann schreibt Oliver wieder korrekt, aber das ist alles zusätzlicher Aufwand.

Ja, also ich glaube, man kann das halt so ein bisschen zusammenfassen unter, nicht Microservices sind eine weitere Möglichkeit, um zum Beispiel solche Änderungen, solche Sachen halt irgendwie zu lösen, wie zu langsames Deployment.

Und ich kann nur noch mal sagen, also das Accelerate Buch, was ja eben sagt, wir wollen gerne schnelleres Deployment und hat diese Dora-Metring in den Mittelpunkt gestellt, sagt halt nicht in dem Architektur-Kapitel macht halt Microservices, sondern er sagt halt, schaut halt, dass ihr da Architektur habt, die halt möglichst Änderungen, unabhängige Änderungen ermöglicht.

Und er nicht, also sagt sogar explizit, dass halt die Diskussion über sowas wie Kubernetes, Microservices oder so, halt die falsche ist.

TTY 0482 sagt, ist richtig, aber Alternative ist grassierende Umgebung und massiver Testaufwand oder M21 Risiko, was aber vielleicht bei Microservices dann weniger ein Problem ist, weil da ist eben das Risiko durch ein Deployment erstmal prinzipiell geringer Ja, führt irgendwie zu der Frage und das ist so ein bisschen auch der Grund, weswegen ich mir gedacht habe, ich mache mal eine Episode darüber, ob wir halt doch wieder Monolithen machen wollen.

Und ich glaube, das ist eigentlich nur das, was ich jetzt die ganze Zeit schon gesagt habe.

Naja, nicht, es hängt irgendwie davon ab.

Ich finde halt, Microservices sind eine Möglichkeit und vielleicht ist es zum Teil ein bisschen sehr übertrieben.

Aber ich glaube, diese krassen Monolithen, die zumindest ich gesehen habe, will ich vielleicht auch nicht wieder haben.

Und es ist eben so, dass halt viele von diesen technischen Nachteilen jetzt klarer werden.

Kubernetes brauche ich vielleicht als Infrastruktur.

Das ist auch nicht so easy.

Ich brauche halt Observability.

Ich muss halt diese ganzen Betriebsaspekte mir angucken.

Und was in gewisser Weise lustig ist, also wir haben ja da einen Fortschritt bei den Werkzeugen.

Also als das Thema mit den Microservices losging, habe ich tatsächlich in einem Projekt gesessen, die halt irgendwie selber VMs gebaut haben und eine eigene Umgebung, in der sie viele VMs laufen lassen können.

Sehr ressourcenintensiv und auch schwer zu handhaben, ganz anders.

Und wir haben irgendwann dann darüber diskutiert, ob wir nicht Docker nutzen wollen würden, weil das halt viel leichtgewichtiger und einfacher ist.

Und das ist heute ja überhaupt kein Thema mehr.

Und trotzdem ist es halt eben so, dass diese technischen Nachteile mittlerweile dazu führen, dass vielleicht eher Monolithen gemacht werden.

Genau, also sprich, diese technischen Herausforderungen sind vielleicht mittlerweile etwas kleiner, als sie am Anfang waren.

Der Billy85 bei BlueSky hatte noch geschrieben, als Antwort auf meine Anfrage, wenn der Code an sich sauber ist, dann gibt es zum Beispiel nur eine Datenbank.

Deployments sind aufwendig und zeitintensiv und so weiter.

Wieder das Deployment-Thema haben wir diskutiert.

Das ist, glaube ich, ein valider Punkt.

Bei den Datenbanken würde ich halt argumentieren, also erstmal in der Theorie können mehrere Microservices auf eine Datenbank zugreifen, auf dieselbe Datenbank, dieselben Datenbank-Schemat haben.

Das ist nur eine relativ blöde Idee, weil die dann halt sehr stark abhängig voneinander sind, was im Umkehrschluss bedeutet, dass eben auch niemand einen davon abhält, verschiedene Module in einem Deployment-Modul mit verschiedenen Datenbank-Schematra zu versehen.

Und ich würde sogar sagen, dass das eigentlich eine gute Idee ist.

Denn wenn ich halt eine starke fachliche Unabhängigkeit habe durch sowas wie baune Kontexte oder andere vernünftige fachliche Module, dann wüsste ich nicht, warum die sich irgendwie auf der Datenbank wieder treffen sollten.

Und deswegen ist diese Entscheidung mit getrennten Datenbank-Schematra oder Datenbanken noch mal was anderes als die Entscheidung zu Gunsten oder gegen Microservices.

Ich muss mal schauen, was hier noch an Themen ist.

Also Martin hat geschrieben, bei Remote-Updates beim Kunden ist ein Microservice hinsichtlich Bandbreite und Reaktionsgeschwindigkeit im Vorteil.

Ja, genau.

Aber umgekehrt ist es halt auch wieder so, dass wenn man jetzt sozusagen Kundinnen dazu bringen möchte, Microservices-Systeme zu warten, das ist vielleicht auch nicht so gut und hat ein Problem, weil dann müsste man ja ein Kubernetes haben und so weiter.

TTY 0482 schreibt.

Also ich sehe es so, wenn man Microservices macht, sollte man es richtig machen.

Sonst hat man alle Nachteile ohne Vorteile.

Genau.

Aber das ist ja so ein bisschen das, was ich versuche zu sagen.

Also ich glaube, ich muss mir halt grundlegende architektonische Gedanken machen, insbesondere über die Fachlichkeit.

Und die sind allgemein nützlich.

Und mir ist halt irgendwie nicht klar, woher das halt irgendwie kommt, dass irgendwelche Menschen ja scheinbar gedacht haben, dass durch Microservices die Architekturprobleme gelöst werden.

Das ist halt irgendwie nicht so.

Kann man jetzt natürlich sagen, naja, wir sind ja schlauer als das.

Und mittlerweile wissen wir das halt.

Aber ich bin mir da sehr unsicher.

Also die typischen Aussagen über Architektur, die ich halt sehe oder viele von denen sind technische Fragestellungen, die sich eben nicht damit beschäftigen, wie ich die Funktionalität aufteile aus einer fachlichen User-Sicht, sondern die sich damit beschäftigen, wie ich halt technische Probleme löse.

Und das passt irgendwie nicht dazu, dass eben wenn man halt fragt, was ist irgendwie wichtiger, fachlich oder technisch, dass man dann als Antwort bekommt, naja, fachlich halt.

TTIP 0482 hat geschrieben, vielleicht doch wieder die gute alte SOA.

Ist was ähnliches, nicht Service-Oriented Architecture?

Meiner Ansicht nach auf einer anderen Ebene, eher so eine Enterprise-Ebene.

Und ja, nicht Microservices und SOA, also die Aufteilung in Services, haben was miteinander zu tun.

Nur ich glaube, das hat mindestens die Ebene halt da was machen.

Peter hat noch geschrieben, im Gedenken an Stefan Tilkoff.

Ich weiß nicht exakt, worauf sich das jetzt bezieht.

Und dann schrieb er noch, ich bin keinesfalls der Meinung, dass man immer Microservices einsetzen sollte und Monolithen immer schlecht sind.

Ich finde Monolithen prima und bin deswegen der Meinung, dass wir ganz viele davon haben sollten, genau, bauen sollten.

Das ist das, was Stefan gesagt hatte.

Genau, und das...

Ich würde jetzt argumentieren, dass das so ein bisschen widersprüchlich in sich ist.

Aber wir haben tatsächlich da, ich glaube, aus Versehen mal sehr ähnliche Präsentationen gehabt.

Im Sinne von, Microservices sind eben nicht klein, weil sie vielleicht eine Fachlichkeit umfassen sollten.

Und es sind halt auch keine Services, sondern es geht eigentlich um Deployment, meiner Ansicht nach zumindest.

Ich hatte leider mit dieser Präsentation von wegen, Microservices ist weder Micro noch Service.

Und ja, das ist etwas, wo er, glaube ich, fast sehr Ähnliches damals gemacht hat.

Es gibt ja auch durchaus modulbasierte Deploymentmöglichkeiten und es muss noch nicht mal OSGi sein.

Genau, das gibt es.

OSGi ist so ein Java-Ansatz, wo ich halt in Java mehrere Module unabhängig voneinander deployen kann.

Führt aber dazu, dass ich halt immer noch zum Beispiel Schwierigkeiten habe in meiner Memory League oder so.

Und ich bin eben immer noch eingeschränkt auf Technologien, die OSGi unterstützen.

Also im Java und ähnliche Technologien, die eben auf der JVM laufen.

Und das ist eben an der Stelle sozusagen das Thema.

So, dann hat Alexander geschrieben, ja, OSGi kann sowas, ist aber in der Praxis nicht so einfach.

Läuft nicht immer so, wie man das erwartet von OSGi.

Es hat seine Nische, aber es ist jetzt irgendwie nicht mehr der große Hype.

Also es gab eine Zeit, wo man geglaubt hat, dass Enterprise Java in Richtung von OSGi geht, das nicht passiert.

Sauwei hat geschrieben, doch, OSGi funktioniert.

Einwandfrei, es ist nur sehr komplex.

Weiß ich nicht.

Also tatsächlich habe ich halt, ich glaube, ich habe es schon mal gesagt, ich habe es schon mal gesagt, ich habe es schon mal gesagt, weiß ich nicht.

Also tatsächlich habe ich halt mal für Spring Source gearbeitet.

Da gab es dann den DM-Server.

Damit konnte man halt Enterprise Java-Anwendungen mit OSGi bauen.

Hat sich am Markt halt nicht durchgesetzt.

Und auch sehr deutlich nicht durchgesetzt.

Genau, was habe ich mir noch aufgeschrieben?

Ach so, und deswegen ist es halt für mich insgesamt so, und das ist auch vielleicht so ein bisschen der Grund, weswegen ich halt nicht sicher war, ob ich diese Episode machen wollte, weil das ja so ein bisschen irgendwie so Modeströmungen sind.

Machen wir Monolithen, machen wir Microservices.

Und ich glaube, das ist irgendwie etwas, was eben vom konkreten Fall abhängt.

Und man kann irgendwie sozusagen, beides hat halt seine Fälle.

Und diese Migration, also das, was ich bei Kunden beobachte, ist irgendwie etwas, was für mich unter diesem Thema Legacy-Modernisierung läuft.

## Legacy Migration

Das heißt, ich sage halt, ich habe halt ein Stück Software.

### Gründe für Migration

Dieses Stück Software hat halt irgendwie ein Problem.

Wir können halt Produkte nicht schnell genug launchen, weil unsere Software die nicht schnell genug abbilden kann.

So was.

Und das finde ich halt erst mal sehr schön, weil dadurch ist halt klar, ich habe einen fachlich wirtschaftlichen Grund.

Das ist deswegen auch allgemeiner, nicht Legacy-Modernisierung.

Ich möchte also weg von meiner aktuellen Software und will es halt irgendwie modern bekommen.

Und das sagt mir halt insgesamt dann mehr zu.

Und wenn ich jetzt irgendwie sage, ich möchte halt Produkte schneller launchen, und da stehen mir halt die Software im Wege, dann bin ich mir unsicher, ob Microservices meine Lösung sind.

Sondern da muss ich mir irgendwie Dinge angucken, die halt fachlich sind.

Und ich hatte die Episode mit meiner Kollegin Tanja Friedl auch gemacht.

Ich glaube, das reicht dann halt auch so in Produktmanagement rein, wo sie halt eben aktiv ist.

Weil das ja letztendlich bedeutet, dass sie halt das Produkt deutlich ändern muss.

Und zwar so, dass sie bei der Software fundamental etwas ändern muss.

Also warum ist es jetzt, ich habe ja immer einen konstanten Strom von irgendwelchen Änderungen, oder was auch immer.

Und jetzt ist ja irgendwie ein bisschen die Frage, warum sage ich jetzt plötzlich, so wie wir es jetzt irgendwie machen, mit diesem Strom an Änderungen, da kommen wir halt irgendwie nicht weiter.

Wir müssen halt irgendwie mal was anderes machen.

Und ich glaube, die Antwort ist halt, weil wir plötzlich etwas vor der Brust haben, oder so ist halt zumindest die Hoffnung, das eben deutlich aufwendiger, komplexer oder so ist, sodass ich mir irgendwie die Frage stelle, wie kann ich total etwas ändern?

Und das ist eben dann etwas, wo ich sozusagen ran muss.

So, TTY0482 hat geschrieben, alles Trade-offs wie immer.

Aber es gibt halt eine breite Auswahl an Möglichkeiten, aus denen man anhand der konkreten Anforderungen ausführen sollte.

Genau, und da ist irgendwie für mich genau diese Sache mit, ich sollte deswegen nicht von vornherein etwas ausschließen oder eben etwas sozusagen gleich gut machen.

Afril bei YouTube schreibt, ich empfinde die Erhöhung der Komplexität von Microservices als Potenzial für feingranulare Möglichkeiten der bedarfsgerechten und kleinteiligen Optimierung.

Für mich ergebe es in Konsequenz, dass Microservices da sinnvoll sein könnten, wo sich aus der Architektur Gedanken der Bedarf nach diesen Qualitäten als gewünscht herausstellen sollte. Ähm Ich bin nicht sicher, was mit dieser bedarfsgerechten und kleinteiligen Optimierung gemeint ist.

Software kann ich halt ändern.

Und ich kann auch ein Deployment-Moduliten ändern und ich kann halt auch bei einem Deployment-Moduliten ein kleines Modul ändern.

Wenn mir das sozusagen nicht ausreicht, um halt irgendetwas Kleines besser zu machen, dann vielleicht Microservices.

Aber ich wüsste nicht, wo das sozusagen zwingend dann zu einem Problem kommt. Ähm Ich hab noch, ich muss nochmal kurz gucken.

Achso, ähm Doch ein bisschen Zeit haben wir noch. Ähm Es gibt halt, also Es gibt halt auch Systeme mit zu vielen Microservices. Ähm Und da ist es eben so, dass man sich vielleicht überlegen müsste, ob man es konsolidieren müsste. Ähm Und da bin ich mir eben unsicher, ob ich sowas komplett zu einem Moduliten umbauen will.

Also wenn ich halt sage, ich hab ein Microservices-System und das ist irgendwie sehr groß und kompliziert, dann kann man ja die Frage stellen, will ich das vielleicht wieder zu einem Moduliten machen.

Ich bin mir nicht sicher, weil die Microservices-Umgebung habe ich dann ja schon.

Also diesen Overhead habe ich halt auf jeden Fall schon mal bezahlt.

Und ähm, ich würde halt auch behaupten, dass man die Sachen halt irgendwie konzeptionell zusammenfasst.

Also niemand kann halt hunderte oder tausende von Microservices verstehen, so wie ich ja auch nicht irgendwie hunderte oder tausende von Klassen verstehen kann, sondern ich werde halt diese Sachen halt irgendwie zusammenpacken.

Ich werde halt sagen, es gibt ein Package oder eben bei Microservices, es gibt eine Namenskonvention.

Ich habe eine Aufteilung nach Teams oder was auch immer.

Und mir ist allerdings auch nicht klar, warum diese kleinen Services dann entstehen.

Also wenn ich halt vernünftige fachliche Module habe, werde ich wahrscheinlich grob granulare Module haben und da halt eher zu einem Ergebnis kommen.

Und deswegen bin ich halt irgendwie unsicher.

Genau, TTY-0482 hat geschrieben, Sam Newman hat ja schon vor vielen Jahren in seinem Buch relativ klar aufgezeigt, warum man Microservices nutzen sollte.

Ich habe ja selber auch ein Buch darüber geschrieben.

Ich weiß nicht, ob ich das klar, also ob man das überhaupt klar aufzeigen kann.

Es ist halt wie ja richtig dargestellt ein Trade-off.

Und die zweite Sache ist ja auch, dass da zu viele Schrauben sind.

Also ein System, das tiefe, synchrone Aufrufe hat, wo ich also sage, ich zeige eine Webseite an, da habe ich halt irgendwie 5 Microservices, die direkt aufgerufen werden.

Diese 5 Microservices rufen wieder 20 Microservices auf.

Dann habe ich halt irgendwie nochmal Aufrufe und so weiter.

Ich verstehe nicht, warum ich so eine Architektur anstreben sollte.

Und die hat Nachteile, zum Beispiel im Zuge auf Resilience, weil wenn einer von diesen Services ausfällt, hat das möglicherweise deutliche Folgen, weil da irgendwie überall aufgerufen wird.

Da muss ich mich also damit beschäftigen, dass ich kompensiere.

Und ich habe halt auch ein Performance-Problem, weil ich halt so wahnsinnig viele Aufrufe habe.

Wenn ich eher das mache, was der Fred George sagt, wo ich irgendwie sage, okay, ich schicke halt Nachrichten hin und her, die sind halt asynchron und im Wesentlichen beantwortet ein Microservice Informationen aus dem, was er sozusagen hat, dann habe ich halt ein anderes System und das nenne ich halt auch Microservices, das hat aber einen anderen Trade-off.

Und das ist da halt sozusagen der Punkt.

Dann hat tty0482 geschrieben, aktuell sind ja Team Topologies in aller Munde, die ja da auch recht relevant sind.

Ich habe ein Buch geschrieben, Quatsch, ich habe ein kurzes Erklärungsvideo gemacht zu dem Thema Team Topologies, das verlinke ich dann auch nochmal.

Ich muss gestehen, also ja, es gibt halt irgendwie sozusagen eine Beziehung zwischen solchen architekturellen Entscheidungen und technischen Entscheidungen wie Microservices.

Ich bin nicht sicher, ob das eine das andere sehr stark bedingt.

Also ich würde sagen, eher nein.

Aber wir haben es ja bereits diskutiert.

Woher kommt diese Idee von Microservices?

Warum ist das etwas, was die Leute halt gerne wollen, weil sie dadurch eine stärkere Unabhängigkeit hinbekommen?

Und da ist eben für mich insbesondere die Unabhängigkeit bei der Technologie und die Möglichkeit, autonome Technologieentscheidungen zu fällen, ein Beispiel dafür, dass man diese technischen Voraussetzungen möglicherweise kassiert, wenn man auf sozialer Ebene sagt, die benutzen dann halt irgendwie alle verschiedenen Tausenden von Programmiersprachen und das will ich halt irgendwie nicht.

Das bedeutet, es gibt eben eine starke Komponente, wenn ich also sage, ich möchte diese Unabhängigkeit haben.

Das kann ich durch Microservices nur ermöglichen, aber ich kann es eben durch organisatorische Maßnahmen entsprechend konterkarieren und das ist auch etwas, was würde ich jetzt mal behaupten, nicht etwas ist, was Team Topologies im Sinne dieser Teamarten und der Kollaboration vermeidet, sondern das ist etwas, wo einfach Menschen vernünftig miteinander umgehen müssen und das ist halt auf einer anderen Ebene.

MightyCore1 schreibt Synchron, genau das macht Google unter der Raube, wenn man eine Suche infrage stellt, das scheint aber auch gut zu funktionieren.

Via Protobuf, ja, also ich meine Netflix funktioniert halt auch.

Ich halte es dennoch für ein Versehen, also das was, oder es ist etwas, wo ich gerne verstehen würde, warum man es anstreben sollte.

Ich würde versuchen anzustreben, dass ein Modul eine fachliche Verantwortung hat und diese fachliche Verantwortung idealerweise ohne andere Module halt hinbekommt und dadurch würde ich erwarten, gibt es wenig synchrone Aufrufe, was halt wiederum impliziert, dass ich eben entsprechend grobgranulare Module habe, das heißt, ich würde das aber höher priorisieren als Ersetzbarkeit.

Ersetzbarkeit wird eben besser, wenn ich kleinere Module habe und zwar eben deswegen, weil ich halt glaube, dass diese Ersetzbarkeit nicht so wichtig ist.

Wenn ich jetzt sage, ich will kleine Module haben, also nicht 102 Microservices, dann komme ich wahrscheinlich eher zu Systemen, die viel miteinander reden müssen und dann habe ich eben ein anderes Problem.

Das ist etwas, was ich tun kann, aber ich würde es halt vermeiden, aber das ist mein Stil.

Der nxnc schreibt, ich erlebe es immer wieder, dass Systeme mit zu vielen Microservices am Networking scheitern.

Ist das per se ein Problem von Microservices oder eine vier Konfiguration schlecht geschnitten?

Ja, also deswegen finde ich ja diese fachliche Aufteilung halt relevant.

Wenn ich ein Modul habe, das für eine fachliche Sache verantwortlich ist und das halt ohne Rückgriff auf andere Module erreichen kann, dann werde ich nicht beim System landen, wo ich verteilte Aufrufe halt habe, viel Kommunikation über das Netzwerk, weil beim System so ist, dass typischerweise ein Microservice eine Fachlichkeit erschlägt.

Alleine autonom.

Und wenn ich das habe, dann habe ich auch noch andere Vorteile, weil nämlich zum Beispiel bei einer fachlichen Änderung wahrscheinlich nur ein Microservice beeinflusst ist.

Deswegen ist das für mich das höchste Ziel und die wichtigste Sache.

Das ist eine fachliche Architekturfrage.

Das ist auch der Grund, warum ich eben dann angefangen habe, mich mit Domain-Driven Design und diesen Sachen noch stärker herumzuschlagen, weil das eben Dinge sind, die uns dort eine Antwort geben.

Und das ist halt der Grund, warum nicht, also die Frage ist ja hier von nxnc, ist das ein Problem von Microservices?

Nein.

Ich kann halt Microservices bauen, die nicht viel miteinander reden.

Ist das eine Fehlkonfiguration?

Nein.

Weil der Grund wahrscheinlich eben dafür ein schlechter Schnitt ist.

Und damit ist es halt irgendwie ein schlechter Schnitt, wobei ich das halt mit dem Schneiden so ein bisschen schwierig finde.

Es ist halt eine fachliche Aufteilung, eine fachliche Architektur.

Und ich finde es halt immer so, also meine Behauptung wäre halt, wenn ich etwas fachlich vernünftig hinbekomme, dann ist ein Ergebnis zum Beispiel weniger Kommunikation.

Aber ich würde mich jetzt nicht hinstellen und versuchen, darauf direkt zu optimieren, sondern ich würde halt sagen, ich möchte es fachlich gut eingefangen haben, dann werde ich eben ein System haben, was halt vielleicht eben auch nicht so viel Kommunikation hat.

Natürlich ist es so, wenn ich jetzt irgendwie ein System habe, wo die Module vier miteinander kommunizieren und das sind irgendwie Methodenaufrufe.

Da komme ich vielleicht damit noch durch die Tür, weil ich eben diese vielen Aufrufe akzeptieren kann, weil die eben schnell sind.

Bei Microservices schlägt das dann eben tatsächlich direkt zu.

Also Fazit.

Monolith und Microservices haben beide glaube ich ihre Berechtigung, aber es gibt Situationen, wo ich halt irgendwie mal in die Architektur rankommen muss.

Das ist das, was ich eine Legacy-Migration nenne, wo ich also jetzt irgendwie sage, okay, das, was ich halt vorher gemacht habe, trägt halt nicht mehr und ich muss irgendwas ändern.

Und das ist aber etwas, wo ich mich jetzt nicht nur auf Microservices sozusagen einschränken lassen wollen würde.

Hinweise noch.

Also ich hatte es gesagt, wenn ihr dieses Thema mit mir nochmal diskutieren wollt, auf euer Thema runtergebrochen, gibt es halt die Möglichkeit, einen virtuellen Kaffee mit mir zu buchen.

Ich packe da auch nochmal den Link in den Chat.

Diesmal ohne den Typo und sonst gibt es den halt auch in den Shownotes.

Wie gesagt, nächste Woche sind die beiden Episoden einmal zum Thema WortliMaps mit Herrn Wortli himself und dem Markus Harra am Donnerstag und dann am Freitag Building Product Teams Beyond Organisational and Geographical Boundaries mit Anna Nath und Leja Vulovic.

Vielen Dank für die Aufmerksamkeit.

Hat mich gefreut, dass so viele Menschen hier waren und dass es auch so viele Fragen und Kommentare gibt.

Das ist der Grund, weswegen ich halt dieses Format immer ganz schön finde.

Schönes Wochenende und vielleicht sehen wir uns bei einem der Folge-Streams oder vielleicht eben nächste Woche bei der Architecture.

Da haben wir übrigens auch, packe ich auch nochmal in den Chat, beziehungsweise in die Shownotes, da haben wir auch einen Rabattcode, das was für mich jetzt noch kurzfristig sozusagen dazukommen will.

So der Architecture.

Da freue ich mich.

Gut, dann würde ich sagen, ja, bis dahin, schönes Wochenende und vielen Dank soweit.