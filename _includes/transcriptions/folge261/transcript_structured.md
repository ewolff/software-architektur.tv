# Folge 261 - Modelle statt Bounded Contexts?

## Einführung und Ankündigung

Eine Alternative für fachliche Modularisierung Modellen und ob das halt sozusagen eine Alternative ist zu bauenden Kontexten.

Bevor ich da loslege, noch ein Hinweis.

Ich habe den Link auch schon in den Chat getan und packe das auch nochmal in die Shownotes.

### Architektur-Kickstart

Und zwar mache ich diesen Architektur-Kickstart, den mache ich einmal vom 20. bis 21.05. in München vor Ort und dann ab dem 29.06. auch in diesem Internet.

Und da gibt es vier Einheiten zu vier Themen, die ich halt irgendwie relevant finde.

Also tatsächlich das Thema Modularisierung, um das es hier gehen wird, Umgang mit Legacy-Systems, Strategic Domain-Driven Design, also welche Sachen ich integriere und Qualitätsziele.

Und das ist halt eben, wie der Name schon sagt, ein Kickstart, um mit Architektur loszulegen.

Sehr praktisch, sehr pragmatisch.

Man führt das also alles selber durch und ich würde mich da natürlich freuen, von euch Leute zu begrüßen.

Und ja genau, legen wir inhaltlich los.

Also eine von den offensichtlichen, also das ist in gewisser Weise eine Fortsetzung von der Episode, die ich halt gemacht habe vor einiger Zeit, wo es halt um diesen Begriff von dem Bauenden Kontexten ging.

Und da ist eigentlich die Aussage, dass irgendwie die Geschichte mit dem Bauenden Kontexten so ein bisschen problematisch ist.

## Problematik von Bounded Contexts

Und das wesentliche Problem, was ich dabei sehe, ist, dass es halt eigentlich drei Dinge sind, über die wir da reden, wenn wir über Bauenden Kontexte reden.

Das eine ist eben, dass ein Bauenden Kontext ein begrenzter Bereich ist für ein ubiquitous language.

### Ubiquitous Language

Ein ubiquitous language ist halt diese Sprache, die halt Domenexpertinnen sprechen, die auch sich im Kode niederschlägt.

Und wir haben da halt irgendwie dieses Problem, dass bestimmte Begriffe irgendwie mehr deutlich sind.

Und im Moment mein beliebtestes Beispiel ist halt, also erst mal ist es halt so, es gibt in unterschiedlichen Bauenden Kontexten unterschiedliche Begrifflichkeiten.

Also wenn ich halt über das Liefern rede, dann habe ich halt eine Lieferung, die habe ich halt offensichtlich da, da habe ich leider nicht, wo ich es hinschicken will.

Und wenn ich über eine Rechnung rede, dann habe ich halt irgendwie keine Lieferung oder das ist das andere, sie ist halt irgendwie anders definiert.

Und diese unterschiedliche Begrifflichkeit, wo eben dasselbe unterschiedlich definiert ist, das lässt sich ganz gut illustrieren an so einem Kunden eines Hotels.

### Beispiel Hotel-Kunde

Also wer ist der Kunde eines Hotels?

Naja und das hängt halt eben davon ab, wenn ich der Kunde, der sich eincheckt, der Gast, das ist halt irgendwie eine natürliche Person, die hat irgendwie da existiert.

Dann gibt es halt den Kunden, der die Rechnung zahlt oder der auf der Rechnung drauf steht.

Das ist in meinem Fall die SwagTap GmbH, das ist jemand anders und das kann auch nicht im Hotel einchecken, die GmbH kann nicht im Hotel einchecken.

Und dann gibt es halt als dritte Komponente noch den Kunden, der das tatsächlich bezahlt.

Und wenn ich jetzt mit meinem Kollegen zusammen im Hotel bin und ich bezahle für uns beide, dann bin ich die Person, die bezahlt.

Die SwagTap GmbH ist der Kunde, der die Rechnung bekommt und ich bin der Kunde, der eincheckt und mein Kollege ist halt der Kunde, der eincheckt.

Und das führt eben dazu, dass unterschiedliche Begrifflichkeiten, unterschiedliche Modern Contexts definiert sind.

Und das ist so eben ein Aspekt.

Und das führt eben dazu, dass unterschiedliche Begrifflichkeiten, unterschiedliche Bounded Contexts definiert sind.

Und das ist so eben ein Aspekt.

Also ein Bounded Context ist ein begrenzter Bereich, in dem eine ubiquitous Language gilt.

## Modelle statt Bounded Contexts

Dann ist das halt ein Bereich, in dem sozusagen ein Modell gültig sein soll.

Und das ist ja das, wo wir eigentlich drüber heute reden wollen und wo wir eigentlich hinwollen.

Und dann ist es eben so, dass in Domain-Driven Design tatsächlich eben ein Modern Context auch etwas ist, woran ein Team arbeitet.

Und also, wie soll ich sagen, in einem kleinen Projekt ist es nicht einsehbar, warum nicht mehrere wenig aufwendig gebaute Kontexte von einem Team oder vielleicht sogar von einem Entwickler hin irgendwie verantwortet werden.

Und ich würde halt auch behaupten, dass es notwendig sein kann, und darüber habe ich ja auch so eine Episode gemacht, nicht über diese Frage.

Genau, ein Beispiel aus der Praxis ist das, wo ich gesagt habe, was ist denn eigentlich, wenn drei Teams an einem modernen Kontext arbeiten.

Und es kann durchaus sein, dass das halt irgendwie Sinn macht, weil man halt irgendwie eine Deadline erreichen möchte und dafür halt irgendwie mehr Menschen auf einen modernen Kontext schickt.

Ich verlinke das auch nochmal in den Shownotes, genau, und da wird man das dann halt sozusagen finden.

So, das heißt also, wir haben dadurch erstmal das Problem, dass das Konzept meiner Ansicht nach schwieriger zu verstehen ist, weil das sind irgendwie drei Dinge, die man da halt irgendwie verstehen muss.

Also, es ist eben ein begrenzter Bereich, in dem ein übergültiges Language halt gilt, es ist ein begrenzter Bereich, in dem halt ein Modell gültig ist, und es ist irgendwie etwas, an dem ein Team arbeitet.

Und ich finde das halt schwierig, wenn wir, also dadurch wird, glaube ich, erstmal das Konzept schwieriger zu verstehen, nicht, weil ich habe irgendwie drei Aspekte, und das ist etwas, was auch ich merke, halt in Trainings, dass es halt irgendwie schwierig ist.

Und ich glaube auch mittlerweile, dass es halt eben nicht sinnvoll ist, das alles zu kombinieren.

Also nicht nur, weil der Begriff dann halt überladen ist, sondern weil halt die Frage, was macht eigentlich ein Team, unabhängig ist von der Frage, was umfasst ein Modell.

Und bis zu einem gewissen Maße würde ich irgendwie behaupten, dass es halt auch unabhängig davon, was halt eine ubiquite Language ist.

So, jetzt ist da halt, ich muss mal kurz schauen, Marc hat geschrieben, also erstmal, nicht danke für den Chat, der ist heute relativ aktiv, und Marc hat geschrieben, rückwärtsdenken, ausgehend von den Bedürfnissen und Interessen der Nutzer, ein Modul soll ein Interesse eines Dekoters widerspiegeln, das Interesse ist das Ziel, von dem aus rückwärts zu Anforderungen und Eingaben gebracht werden soll.

Glaube ich nicht, ich würde halt eher behaupten, dass halt ein Modell, nicht zum Beispiel das Einchecken in einem Hotel, das ist da, oder die Rechnung in einem Hotel, da gibt es verschiedene Stakeholder, ich interessiere mich dafür, ich will die richtige Rechnung haben, Financials von dem Hotelunternehmen interessiert sich dafür, weil die müssen halt mit der Rechnung richtig umgehen, ein Callcenter interessiert sich dafür, wenn ich mal wieder irgendwie anrufe und sage, dass halt die Rechnungsadresse nicht stimmt, das heißt also solche Sachen wie eine Rechnungslegung sind eben Dinge, die halt verschiedene Stakeholder interessieren.

Das sollte aber eigentlich auch klar sein aus den vorherigen Episoden.

So, also einmal glaube ich halt, es ist nicht sinnvoll, das zu kombinieren, weil das drei unterschiedliche Dinge sind und ich halt diesen komplexen Begriff habe und dann ist ja eigentlich die zentrale Frage, die mich jetzt interessiert, also ebenso als Architekt oder Architekturberater, wie komme ich zu einer gruppengranularen Modularisierung meines Systems, zum Beispiel in beiden Kontexten und da gibt es Antworten, also zum Beispiel halt Eventstorming, aber eigentlich will ich halt diese Modelle haben, also ich will jetzt eigentlich ein Modell haben, was halt einen Teil der Logik implementiert und das ist der Aspekt, der zentral ist für mich aus einer Architekturperspektive in Bezug auf Bauenden Kontext.

Es gibt Ansätze, wie man solche Bauenden Kontexte finden kann, zum Beispiel Eventstorming, haben wir auch eine Episode darüber gemacht, das sollte eigentlich irgendwie auch klar sein, aber dieses Modell da irgendwie nochmal tiefer reinzugraben, das ist glaube ich irgendwie auch nochmal eine spannende Sache und ich habe gerade eben nochmal in das blaue Buch geguckt, also das Instrument und Design Buch von dem Eric Evans und es stellt sich halt heraus, dass halt der Begriff Modell als solcher gar nicht im Index steht.

Also nicht, wenn man hinten halt irgendwie sagt, okay, hinten im Index nachguckt, ob dieser Begriff irgendwie definiert ist und ob da was explizit zusteht, ich habe es da nicht gefunden und ich habe es mir jetzt irgendwie erspart, die 600 Seiten sozusagen nochmal durchzulesen, die da irgendwie drin sind und das halt irgendwie zu verstehen und das führt irgendwie zu der Frage, haben wir nicht eigentlich den falschen Fokus, also das, was uns jetzt Bauende Kontext sagt, ist, es gibt mehrere Modelle und das macht ja Sinn, aber was ist ein Modell, sagt es uns nicht, sondern das ist eben etwas anderes und nachdem ich halt irgendwie daran gescheitert bin, in dem Design Buch das irgendwie auf den ersten Blick zu finden, habe ich mir gedacht, ich gucke mal irgendwie in Wikipedia und in der deutschen Wikipedia steht, Modell ist ein Begriff, der sowohl im wissenschaftlichen Sprachgebrauch als auch in der Umgangssprache unterschiedliche Bedeutungen besitzt.

Die häufigste ist dabei ein analoger Realitätsausschnitt, also Analogie bedeutet, ich baue etwas, was so aussieht wie die Realität und dann stand da weiter in der Wissenschaft, definiert man ein Modell als eine vereinfachte Darstellung eines Originals, die spezifische Eigenschaften hervorhebt und für einen bestimmten Zweck verwendet wird.

Modelle dienen dazu, komplexe Sachverhalte zu erklären, zu analysieren oder vorherzusagen.

Nach Stachowiak besitzen Modelle drei grundlegende Merkmale.

Sie sind Abbilder eines Originals, abstrichen nur die relevanten Eigenschaften und erfüllen eine pragmatische Funktion, in dem sie auf einen bestimmten Gebrauchszweck ausgerichtet sind.

Das ist das, was wir mit Modellieren in der Softwareentwicklung eigentlich erreichen wollen.

Wir wollen irgendetwas haben, was auf die Realität Auswirkungen hat und damit irgendetwas aus der Realität modellieren, wobei ich dieses Nachempfinden schwierig finde, weil wenn ich zum Beispiel über einen Kredit rede und ich implementiere jetzt mit Logik für einen Kredit und ich sage in meiner Logik, das ist die Zahlung, das ist die Kreditrate, dann wird das halt die Realität.

Also es ist halt nicht nur so, dass wir dadurch die Realität modellieren, indem wir sie nachempfinden, sondern wir designen halt auch in gewisser Weise Realität.

Wir definieren eben, wie dieser Kredit tatsächlich aussieht und was ich halt daraus aus dieser Stachowiak-Definition ableite, ist halt, dass es halt relevante Eigenschaften gibt.

Also es ist irgendwie nicht vollständig und es ist irgendwie pragmatisch.

Also es ist irgendwie etwas, womit ich irgendwie mit umgehen möchte und was halt erreichen möchte.

Wir sind also zielgerichtet auf irgendetwas und wenn das halt relevant ist, dann bedeutet es, dass es in unterschiedlichen Bereichen unterschiedlich relevante Dinge geben kann und dann sind wir bei einem Kontext.

Das heißt, wenn man halt über Modelle redet, kommt man eigentlich dazu, dass es halt unterschiedliche Modelle geben muss, weil unterschiedliche Dinge in unterschiedlichen Bereichen relevant sind und das ist ja das, was der Spawn-Context-Pattern sagt.

Das ist also eigentlich gar nicht so überraschend und ich habe mir noch von dem Georg Box diese berühmte, oder George Box, diese berühmte Zitat aufgeschrieben.

Nicht alle Modelle sind falsch, aber einige sind nützlich.

Also wir wollen irgendetwas damit erreichen.

Ah, der Matthias Wohn hat geschrieben, Moment, das will ich eigentlich anzeigen, aus Erics DDD-Referenz, a system of abstractions that describes selected aspects of a domain and can be used to solve problems related to that domain.

Das ist also dort die Definition eines Modells.

Danke für den Hinweis, Matthias.

Das hatte ich dann sozusagen nicht auf der Rolle, obwohl ich ja die DDD-Referenz mit übersetzt habe, aber so ist es halt manchmal.

So, also welches Problem wollen wir denn jetzt lösen?

Wir wollen halt eine vernünftige fachliche Aufteilung bauen.

Dazu ist uns halt die Teamfrage, würde ich sagen, egal.

Ein Team kann für mehrere fachliche Dinge halt verantwortlich sein oder wir können eine Fachlichkeit halt auch mit mehreren Teams bearbeiten.

Das führt zu Reibungsverlust, aber tun können wir das halt irgendwie schon.

Das bedeutet halt, um jetzt eine vernünftige fachliche Aufteilung zu bekommen, hilft uns halt die Teamfrage nicht wirklich.

Das ist halt eher eine Auswirkung.

Also wir haben halt eine Granularität, wo wir eine Empfehlung geben können, ein Team sollte so eine Fachlichkeit eines Modells halt idealerweise umsetzen.

Aber ein Team dürfte durchaus mehrere Modelle umsetzen, da sehe ich kein Problem.

Und wenn die Reibungsverluste akzeptabel sind aus irgendwelchen Gründen, dann können eben auch mehrere Teams an einem Modell arbeiten.

Es hilft aber nicht, dass wir diese für diese fachliche Aufteilung, die wir ja eigentlich erreichen wollen, dass wir diesen Teamaspekt noch zusätzlich betrachten.

Das macht diese Frage nicht einfacher, wie wir eine vernünftige fachliche Aufteilung hinbekommen.

Hilft uns das mit der Ubiquitous Language?

Also vielleicht hilft uns das, weil den Kunden aus diesem Hotelbeispiel jetzt einheitlich zu implementieren.

Das ist irgendwie super schwierig.

Also ich müsste dann halt einen Kunden haben, der gleichzeitig in der SwagClub GmbH ist und der Eberhardt und der Kollege und der Eberhardt, der es halt bezahlt.

Also ich habe ja drei Dinge.

Ich habe den Kunden, der die Richtung bekommt, SwagClub GmbH.

Ich habe den Kunden, der sich eincheckt.

Das bin ich zum Beispiel.

Und der Kunde, der es bezahlt, das bin ich.

Und das jetzt irgendwie in ein Modell zu gießen, macht halt irgendwie nicht so wahnsinnig viel Sinn.

Das heißt, wir kommen jetzt dazu, dass unterschiedliche Ubiquitous Languages wahrscheinlich unterschiedliche Modelle implizieren.

Aber so wirklich nützlich ist das halt für die fachliche Analyse, weil wir in der fachlichen Analyse dann wissen, es wird nicht den Kunden geben und wir müssen uns irgendwie darauf einstellen, dass eine Entität wie Kunde in unterschiedlichen Kontexten was unterschiedliches ist.

Und es geht dabei eigentlich um die Daten, die halt relevant sind.

Der Name ist halt relevant.

Für die Meldung ist tatsächlich meine Privatadresse relevant.

Für die Rechnung ist die Rechnungsadresse relevant und so weiter.

Das heißt, wir können auch dadurch, dass wir sagen, das sind unterschiedliche Datenbeschreibungen, nicht unterschiedliche Begriffe.

Dadurch kommen wir zu einem ähnlichen Ding, zu einer ähnlichen Idee.

Und das bedeutet, dass diese Geschichte mit dem Bauenden Kontext unser Problem nicht löst.

Also es sagt zwar, wir brauchen mehrere Modelle.

Es sagt aber nicht so klar, was denn nun genau ein Modell ist.

Also Matthias hatte jetzt gerade eben die Definition aus der Referenz noch reingepackt.

Aber es ist halt insbesondere nicht klar, wie wir es finden.

Eventstorming als Ergänzung im Domain des Designs sagt das halt schon ein bisschen.

Tasklog schreibt jetzt, dass ein Modell ausführbarer Code ist.

Das ist vielleicht auch noch ein wichtiger Hinweis.

Eigentlich wollen wir eben am Ende ausführbaren Code haben.

Wir wollen nicht ein Modell haben im Sinne von, wir malen es hin oder so, sondern wir wollen eben ausführbaren Code haben.

Also wir brauchen jetzt eine Methode, um Fachlichkeit zu strukturieren.

Und das ist etwas, was mich schon länger beschäftigt und was ich eben für zentral halte und wo wir auch verschiedene Episoden im Stream schon hatten.

Und ich halte das deswegen für wichtig, weil wenn man jetzt einfach irgendjemandem sagt, strukturieren wir dein System, dann kommen halt irgendwelche Ergebnisse dabei raus.

Aber es ist nicht so, dass wir eine klare Heuristik haben, wie wir unser System aufteilen und wie wir Fachlichkeiten aufteilen.

Und das ist eigentlich schlecht, denn das müssten wir eigentlich haben.

Meistens haben wir, wenn man sagt, wie teilt man das System auf, kommt meistens eine technische Antwort.

Wir haben Schichten, wir haben eine hexagonale Architektur.

Und da kann ich jetzt sagen, wenn ich UI-Code habe, also eine bestimmte Art von technischem Code, dann ist der halt in meinem System an einer bestimmten Stelle verortet.

Das hilft mir aber nicht für die fachliche Aufteilung, denn die fachliche Aufteilung ist etwas anderes.

Das ist die Frage, wo habe ich jetzt die Logik, die sagt, ich kann etwas zustellen, etwas zuschicken oder was auch immer.

Und ich finde es da wichtig, nochmal auf diese Geschichte einzugehen mit dem Information-Hiding.

Was wir eigentlich haben wollen, ist, wir wollen etwas haben, eine fachliche Funktionalität, die z.B. sagt, ich checke jemanden im Hotel ein.

Und wie das genau passiert, sollte versteckt sein.

Es sollte eine Schnittstelle geben, die jetzt irgendwie dafür sorgt, dass da Informationen rein und raus fließen.

Analog, wenn ich jetzt sage, eine Bestellung soll verschickt werden, dann will ich sagen, hier ist die Bestellung, hier sind die Sachen und irgendwie wird das zugestellt.

Aber die Details sollen versteckt sein und sich unabhängig von der Schnittstelle ändern können.

Das heißt, solange die Schnittstelle stabil bleibt, kann man die Implementierung ändern, was dazu führt, dass wir eben stärkere Unabhängigkeit haben, weil eben andere sich nur auf die Schnittstelle verlassen.

Und ich kann jetzt eben unabhängig von dem, was andere Teams tun oder EntwicklerInnen tun, in der Implementierung etwas ändern, solange die Schnittstelle konstant bleibt.

Und das ist genau Information-Hiding.

Ich gebe nicht die Information raus, wie es intern implementiert ist.

Dadurch kann ich das ändern.

Oliver schreibt, was genau meinst du mit, wir müssen das eigentlich haben.

Andere Industrien haben das doch auch nicht.

Und ich glaube, damit beziehst du dich auf diese Geschichte mit dieser fachlichen Aufteilung, dass wir das seitdem nicht haben.

Unser Job ist es, in der Softwarearchitektur Fachlichkeiten zu strukturieren.

Und das ist das, was wir eigentlich tagtäglich, Oliver schreibt jetzt gerade ein konkretes Aufteilsvorgehen, also diese fachliche Aufteilung ist zentral, um zu einer frühen Softwarearchitektur zu kommen.

Wenn man das so unterschreibt, müsste es so sein, dass wir in einer Ausbildung sagen, das machen wir übrigens so.

Und wenn man jetzt jemandem sagt, teil mal das System fachlich auf, dann kriege ich einen hohen Anteil an Menschen, die sich darüber einig sind, wie sie das machen.

Und das basiert auf irgendeiner Heuristik, oder irgendetwas, was den Menschen beigebracht worden ist in einer Ausbildung.

Das wäre das Optimum.

Und das erlebe ich nicht.

Also ich mache ja Trainings in diesem Bereich.

Und offensichtlich kann ich halt Geld damit verdienen, zu versuchen Leuten das irgendwie beizubringen.

Was bedeutet das, eine Lücke?

Ich finde das schwierig mit den anderen Branchen.

Denn einmal ist es so, die anderen Branchen, ich arbeite da halt nicht.

Also ich bin Softwareentwickler, ich baue keine Brücken oder sowas.

Und ich würde behaupten, dass in anderen Branchen halt beigebracht wird, wie man systematisch Brücken baut.

Ich weiß nicht, ob das tatsächlich so ist, wie es dann gemacht wird.

Das ist halt auch möglicherweise ein Gap.

Also es wird ja Menschen durchaus beigebracht, wie man Software entwickelt.

Nur das ist irgendwie nicht das, was tatsächlich relevant ist.

Also diese fachliche Aufteilung wird denen offensichtlich nicht beigebracht.

Das kann halt möglicherweise bei Brückenbau ähnlich sein, dass denen irgendwie nicht beigebracht wird, was eigentlich relevant ist.

Ich muss auch gestehen, dass mir das sozusagen so ein bisschen egal ist.

Ich vergleiche mich ja nicht mit Brückenbauern.

Das ist nicht der Punkt.

Ich glaube, wir haben da eine Schwäche und etwas, was wir in unserer Branche einfach lösen müssen.

Also ich würde mir wünschen, dass wir dieses Thema mit der Aufteilung, dass das irgendwie klar ist und dass jeder weiß, wie man sowas macht.

Das ist halt der Punkt.

Ich habe jetzt gerade gesagt, diese Geschichte mit dem Information Hiding und das ist die grundlegende Idee, so wie es halt heutzutage zumindest definiert wird.

Ich möchte gerne wissen, wie viel Geld ich auf dem Konto habe.

Ich kriege entweder den abgespeicherten Kontostand zurück oder aber es wird irgendwie intern berechnet, aus den letzten Überweisungen, wie hoch mein Kontostand ist und beide Möglichkeiten, also direkt den Kontostand speichern und nur zurückgeben oder ihn ad hoc berechnen, kann ich hinter derselben Schnittstelle verstecken, sodass ich zwischen diesen beiden Implementierungen wechseln kann, ohne dass es andere beeinflusst.

Das ist da erstmal das Konzept.

Ich habe schon mal in der OO-Folge über Abstract Data Types gesprochen.

Ich habe das Gefühl, deswegen wollte ich das hier nochmal aufgreifen, dass das etwas ist, was mir bei diesem Denken über die Schnittstellen hilft.

Das ist tatsächlich etwas, was ich meiner Ansicht nach im Grundstudium gelernt habe, im ersten oder zweiten Semester.

Das vertieft diese Geschichte mit der Schnittstelle.

Ich muss dazu sagen, dass ich ein bisschen gelernt habe, dass das möglicherweise auch ein Konstrukt ist, was in Beweisen über Programme genutzt wird und in formalen Strukturen.

Das ist gar nicht das, was ich hier meine, sondern für mich ist der Denkansatz erstmal wichtig.

Der Denkansatz ist, dass ich von der Benutzung her über einen Datentyp nachdenke.

Ich kann außerdem an der Schnittstelle Vor- und Nachbedingungen haben.

Das führt dazu, dass ich da mit Beweisen einiges machen kann, weil ich nicht weiß, welche Dinge in der Außenbetrachtung über diesen Datentyp gelten.

Ich kann darüber versuchen, Beweise zu machen.

So nehme ich jedenfalls an.

Das prototypische Beispiel ist ein Stack.

Das ist ein Stapel, wo man Sachen drauflegt.

Das ist eine Datenstruktur.

Das heißt, ich habe Dinge, die auf diesem Stack liegen.

Ich kann oben immer Sachen drauf tun.

Dann lese ich sie von oben wieder ab.

Das heißt, ich lege den W42 oben drauf.

Ich lege den W23 oben drauf.

Dann sage ich, gib mir das Höchste.

Das ist 23.

Dann sage ich wieder, gib mir das Höchste.

Das ist jetzt 42, weil die 23 ausgelesen worden ist und so weiter.

Dann kann so ein Stack wachsen und wieder in sich zusammen sinken.

Das sind Dinge, die ich mit Vor- und Nachbedingungen kombinieren kann.

Das heißt, etwas vom Stack zu nehmen, als Vorbedingung, dass das Ding nicht leer ist.

Ich werde eine Schnittstelle haben, die sagt, nimm das oberste Element raus und gib es mir zurück.

Ich werde eine Operation haben, die sagt, pack irgendetwas auf den Stack obendrauf.

Ich werde eine Operation haben, die sagt, es ist leer.

Jetzt kann ich sagen, wenn du etwas auf den Stack gelegt hast, ist es anschließend nicht mehr leer.

Wenn du etwas von dem Stack runterlesen willst, dann sollte es vorher nicht leer sein.

Und so weiter und so weiter.

Darüber habe ich jetzt von draußen bestimmte Verhaltensweisen definiert.

Ich bin nicht sicher, ob das, was ich verbal besprochen habe, dass ich etwas obendrauf lege und dann runterholen kann.

Ob ich so etwas mit Vor- und Nachbedingungen formulieren würde.

Das kann man wahrscheinlich auch tun.

Aber ich habe da jetzt eine Denkweise von draußen und kann dort noch mehr Semantik und mehr Ideen reinbringen.

Und weswegen ich diese Denkweise interessant finde, ist, weil das ist völlig getrennt von der Implementierung.

Wenn ich so ein Stack habe, kann ich den z.B. implementieren mit einem Array, also einem Feld.

Da kann ich mit dem Index auf Datenelemente zugreifen.

Dann merke ich mir den letzten Index.

Und wenn ich etwas drauflege, dann erhöhe ich den Index um 1 und speichere in dem Array das Ding ab.

Wenn ich etwas runterlese, entnehme ich das von dem Index, den ich mir gemerkt habe, raus, gebe es zurück und erniedrige den Index um 1.

Das wäre jetzt meine eine Implementierung.

Eine andere Implementierung wäre eine Linked List, wo jedes Datum einen Link hat auf das nächste.

Da kann ich jetzt vorne an die Linked List das Neue ranhängen und das entsprechend zurückgeben, wenn jemand das haben möchte und dann aus dieser Linked List löschen.

Das heißt, ich habe mehrere Implementierungsmöglichkeiten, die davon versteckt sind, die aber tatsächlich dieselbe Schnittstelle und dieselbe Semantik durch Vor- und Nachbedingungen ausgedrückt haben.

Die unterscheiden sich in so etwas wie Laufzeitverhalten und Speicherkomplexität und solche Geschichten.

Da kann ich jetzt sagen, wenn ich eine Linked List habe, die kann ohne größere Probleme wachsen.

In einem Array habe ich das vorbelegt und kann mir überlegen, welche Implementierung ich haben will.

Das bedeutet, dass ich das Design durch eine Benutzung treiben lasse.

Diese Woche habe ich von Jason Gorman einen BlueSky-Post gelesen, der gesagt hat, Test Driven Development, wo ich erst einmal einen Test schreibe, macht eigentlich dasselbe.

Das heißt, ich definiere die Schnittstelle und überlege mir, wie sich die Schnittstelle aus.

Anhand dessen schreibe ich einen Test und dann implementiere ich das.

Das ist eine ähnliche Denkweise.

Warum das für mich wichtig ist, weil ich das Gefühl habe, dass ich häufig auf Denken treffe, was sagt, ich komme mir jetzt die Daten an, ein Kunde, also nicht im Hotel, ich habe offensichtlich Kunden, dann lasse mich die jetzt modellieren.

Und wenn man dann irgendwie unschuldig fragt, wo in diesem System kann ich mir jetzt ein Hotel einchecken, dann ist die Antwort, keine Ahnung.

Das ist nicht klar.

Dadurch kommt man auch nicht auf die Idee.

Das ist ja kein Datum, das ist eine Vorgehensweise.

Tatsächlich habe ich so etwas gehabt, wo ein System war, wo Verträge, Produkte und Kunden sind.

Und ein Kunde schließt einen Vertrag über ein Produkt ab.

Und dann ist für mich nicht klar, wo dieser Abschluss ist.

Also im Vertrag, im Produkt oder beim Kunden.

Das kann man alles irgendwie argumentieren.

Sondern es ist ein System zur Abschließung von Verträgen.

Da ist es unklar, wo die Verträge abgeschlossen werden sollen.

Ich glaube, das hilft ihr darüber, eher so nachzudenken im Sinne von Abstract Data Types und Schnittstellen und da irgendwie hinzugehen.

Das heißt, wir wollen eigentlich einen Teil modellieren, aber eben nur einen Teil.

Und dort glaube ich, ein wenig von der Schnittstelle kommen und da eben eine Realität modellieren.

Beim Hotel ist es so, dass wir die Realität modellieren, dass der E-Baht jetzt im Hotel ist und gerade reingekommen ist.

Und das bildet das System jetzt ab.

Bei einem Kredit implizieren wir eher die Realität, weil wenn wir in dem System den Kredit haben, dann wird das tatsächlich passieren, weil der nur dafür sorgt, dass sich irgendwelche Daten, nicht irgendwelche Bankkontostände ändern.

Das heißt, da ist die Realität der Bankkontostand, der eigentlich nur ein Datum ist.

Beim Hotel modellieren wir tatsächlich, der Kunde ist jetzt in dem Hotel drin.

Und das führt jetzt zu einer Geschichte, also zu Fragen, die man wissen muss oder die man entscheiden muss.

Und da ist gerade die Frage, die Denkrichtung kommt von der Schnittstelle zum Modell.

Ja, das wäre jetzt, glaube ich, zumindest etwas, was wichtig ist, weil wir wollen ja wissen, wo Funktionalitäten sind.

Also irgendwo wird halt dieses Ding sein mit Kunde checkt sich ein.

Irgendwo wird irgendwie das Ding sein, Kunde schließt einen Vertrag ab.

Wo packen wir das hin?

Wenn wir nirgendwo in den Schnittstellen sagen können, das ist da, dann haben wir offensichtlich einen Fail, weil wir gerade im Hotel modelliert haben, wo sich niemand einchecken kann.

Respektive in dem anderen Fall haben wir eben etwas, also nicht ein Finanzprodukt modelliert, das man nicht abschließen kann.

Das ist halt offensichtlich absurd.

Das heißt, diese Frage müssen wir beantworten.

Irgendwo muss das halt in der Schnittstelle drin sein.

So, und jetzt ist halt irgendwie die Frage, soll das Ding, was jetzt ein Hotelgast eincheckt, auch wissen, ob ein Hotelgast sich einchecken darf?

Also darf ich jetzt für meinen Kollegen, der nicht da ist, einchecken?

Weiß ich nicht, weil ich habe ja nicht seinen Personalausweis.

Ich weiß nicht genau, wo die Person wohnt.

Also wäre das jetzt etwas, was zu entscheiden wäre.

Der Eberhardt steht vor mir und sagt, ich möchte gerne schon mal meinen Kollegen einchecken.

Sage ich jetzt, nee, geht halt nicht, der muss halt nochmal kommen und seinen Personalausweis vorlegen, oder sage ich, alles klar, mache ich halt gerne.

So, da haben wir jetzt eine Vorbedingung.

Aus so einer ADT-Sicht wäre das jetzt so, dass ich sage, kann diese Person einchecken?

Das ist halt irgendwie eine Vorbedingung dafür, dass dann tatsächlich eingecheckt wird.

So, und aus so einer ADT-Sicht könnte man jetzt sagen, naja, das gehört halt irgendwie zusammen, weil ich will eigentlich ja die Vorbedingungen dort haben, wo ich auch die Implementierung habe.

Und wahrscheinlich hängt das halt irgendwie zusammen, aber vielleicht halt irgendwie auch nicht.

Also, weil dieses Modell, was jetzt entscheidet, darf der das tun, ist vielleicht so kompliziert und braucht halt andere Daten und andere Informationen.

Also, kenne ich die Personalausweisnummer?

Kenne ich diese Person?

Das sind alles eben Dinge, die nicht dafür relevant sind, dass ich dann tatsächlich einchecke, aber es ist vielleicht als Vorbedingung relevant.

Also, ich habe mir jetzt ein anderes Beispiel aufgeschrieben.

Sollte der Bestellprozess wissen, was eine Person bestellen darf?

Weiß ich nicht genau.

Das könnte halt vom Alter abhängen, von der Solvenz, die diese Person hat, irgendein Kundenrating, was halt irgendwie sagt, dass die Person halt häufig oder weniger häufig Sachen irgendwie zurückschickt.

Ist das etwas, was ein Modell, ein eigenes Modell rechtfertigt?

Möglicherweise schon.

So, und dann führt das eben dazu, dass ich irgendwie die Schnittstelle sozusagen durchbrechen muss und dann irgendwie sagen muss, okay, ich habe jetzt irgendwie ein Modell, was halt sagt, Bestellung wird tatsächlich gemacht.

Ich habe ein anderes Modell, was halt sagt, die Vorbedingungen sind erfüllt, weil diese beiden Modelle unterschiedliche Informationen benötigen.

Ich muss halt nicht mehr, wenn die Bestellung tatsächlich passiert, wissen, dass der Kunde irgendwie vorjährig ist.

Ich muss nicht mehr wissen, was das Kundenrating ist, sondern das mache ich dann halt einfach und kann das halt irgendwie erledigen.

Könnte also sein, dass ich irgendwie zwei Modelle brauche.

So, dann muss ich das halt irgendwie durchbrechen.

Das andere Beispiel ist halt die Geschichte, also was ich mir herausgelesen habe, ist irgendwie, er sollte das Bezahlen wissen, wofür bezahlt wird.

Und das hängt damit zusammen, dass ich halt über dieses Problem gestolpert bin vor einiger Zeit in einem Kontext, wo in meinen Augen es relativ offensichtlich war, dass halt ein Ding, was jetzt sagt, bitte bezahle 50 Euro Rate pro Monat, nicht wissen muss, ob das halt für einen Kredit, eine Versicherung oder was auch immer halt irgendwie ist.

Also aus meiner naiven Sicht scheint das irgendwie klar.

Und es ist ein Fehler, das halt anders zu modellieren, die halt in dem Fall tatsächlich offensichtlich zum Problem geführt hat.

Und wenn ich jetzt aber sage, ich bin halt in einem Supermarkt und ich bezahle mit einer Kreditkarte oder ich bestelle etwas online mit einer Kreditkarte, dann bin ich mir nicht so sicher, weil es gibt zum einen, glaube ich, also ich habe das jetzt nicht nachrecherchiert, hat so eine Geschichte, dass halt man Statistiken, dass man irgendwie Statistiken haben möchte über verschiedene Produkte, die halt gekauft werden.

Oder vielleicht ist es auch so, dass man halt von dem Kreditkartenhersteller eine Versicherung für bestimmte Produkte bekommt.

Und das würde jetzt eben wieder bedeuten, dass ich da nicht so ganz trivial auf der Schnittstelle eben das entscheiden kann.

Der Matthias fragt gerade oder sagt gerade, dass er ein bisschen lost ist.

Danke für den Hinweis.

Kannst du noch mal kurz sagen, wie sich ADT thematisch zu Baune Context verhält?

Also erst mal, ich diskutiere ja Modelle.

Und das ist ein Teil von diesen Baune Kontexten.

Und diese Abstract Data Types sind für mich nur eine Inspiration, noch mal tiefer über Schnittstellen zu reden.

Also wenn wir eine fachliche Aufteilung haben wollen in mehreren Modellen, dann haben wir irgendwelche Dinge, die halt Schnittstellen haben.

Und wir brauchen eigentlich jetzt nur eine Idee darüber, wo die Schnittstellenmethode ist mit ich bestelle jetzt irgendetwas, ich schließe dieses Produkt ab, ich bezahle irgendetwas, solche Geschichten.

Das heißt eigentlich ist diese fachliche Aufteilung eine Frage von wo, an welcher Schnittstelle, welches Modell habe ich diese Operation.

So was ich jetzt versuche mit den ADTs zu sagen ist, eine Schnittstelle kann eben mehr sein als nur eine Auflistung von Methoden.

Ich kann versuchen von draußen eine Semantik zu definieren, bei so etwas wie einem Stack.

Und das hilft vielleicht dabei, diese Systeme stärker zu strukturieren.

Also ich habe halt beim Stack die Vorbedingung, ist das Ding nicht leer, nur dann kann ich etwas rauslesen.

Ich habe für die Schnittstellen Operation, ich bestelle das jetzt die Vorbedingung, ich darf es tatsächlich bestellen, was vielleicht eine andere Operation an der Schnittstelle ist.

Und darüber kann ich jetzt versuchen, Dinge zu strukturieren.

Also bei einem ADT würde man sagen, die Vorbedingung und die Operation selber gehören offensichtlich zusammen.

Bei diesen Fachling-Modellen bin ich mir nicht so sicher, aber diese Kategorisierung überhaupt zu sagen, es gibt Vorbedingungen, es gibt irgendwie Operationen, die tatsächlich etwas ausführen, ich kann mir jetzt von draußen etwas über die Schnittstelle überlegen und ich bin dann unabhängig von der Implementierung, das hilft mir da.

Ich würde jetzt nicht sagen, dass diese Modelle, über die wir sprechen, ADTs sind, aber weil ich das im Studium gelernt habe und mir das geholfen hat, nochmal etwas über Schnittstellen zu verstehen, deswegen erzähle ich das hier.

Das ist ein nettes, abstraktes Modell.

Matthias hat geschrieben, er got it, Aufklang bewirkt Schnittstellen zwischen Modellen.

Daher, danke, da kommt das halt her.

Passlock hat geschrieben, ist eine Datenmarkentabelle auch schon ein Modell?

Nein, eine Datenmarkentabelle hat offensichtlich keine Operation.

Ich kann nicht sagen, die Datenmarkentabelle implementiert das Aufgeben einer Bestellung.

Das ist ein Datum, das ist intern, das ist ein Teil der Implementierung, das ist genau das, was ich versuche zu sagen.

Die Daten sind eine Folge davon.

Deswegen will ich auf Schnittstellen, ich konzentriere mich gerade nicht auf die Implementierung.

Ich glaube, und das ist der andere Aspekt, der mir irgendwann aufgekommen ist, ich glaube, es ist hilfreich, wenn man explizit sagt, wir wollen ein höheres Maß an Autonomie erreichen.

Ich würde behaupten, das wollen wir, weil wenn ich autonome Modelle habe, dann kann ich mit der Änderung eines Modells dafür sorgen, dass ich eine Geschäftssache ändere.

Das könnte ein Team tun, dann habe ich auch autonomere Teams, die Funktionalitäten in einem Team umsetzen können.

Das heißt, wir wollen ein hohes Maß an Autonomie.

### Beispiel Bestellprozess

Wenn wir das jetzt als Ziel definieren, und ich sage jetzt beispielsweise, ich habe ein Modell für eine Bestellung, für einen Bestellprozess, und ich habe ein Modell für einen Kunden, dann ist die Frage, sind die autonom?

Und die Antwort ist, nö, sind sie nicht, weil der Bestellprozess wird dieses Kunden-Ding benötigen.

Und wenn ich jetzt sage, ich habe ein Produkt, dann werde ich sagen, der Bestellprozess benötigt ein Produkt.

Und das bedeutet, dass Produkt, Kunde und Bestellprozess drei Dinge sind, die miteinander in einer Beziehung stehen, und die sind nicht autonom, in dem Sinne, dass ich jetzt bei einer Änderung möglicherweise alle drei ändern muss.

Dann stellt sich die Frage, kann ich ein höheres Maß an Autonomie erreichen?

Ich würde behaupten, ja, indem ich einfach sage, den Kunden packe ich sozusagen mit in diesen Bestellprozess rein.

Offensichtlich könnte ich jetzt sagen, ich eliminiere diese Benutzbeziehung dadurch, dass ich sage, ich mache aus diesen beiden eins.

Jetzt könnte man natürlich sagen, naja, netter Versuch, das ist eigentlich irgendwie ein Taschenspielertrick, weil ich sage halt, statt dass ich drei getrennte Dinge habe, mache ich einfach eins, und das eine Ding ist dann eben autonom.

Aber das umfasst ja alles drei.

Das wäre dann ein Modell, das Produkt, Kunde und Bestellung hat.

Das ist ja gigantisch, und ich habe ja eigentlich nichts gewonnen.

Aber das ist ja eben das, wo wir jetzt feststellen können, dass für einen Bestellprozess oder für eine Lieferung andere Informationen über einen Kunden relevant sind, als eben für einen Rechnungsprozess.

Da muss ich wissen, wie groß ist das Produkt?

Wie schwer ist es?

Und ich muss wissen, wo der Kunde es hingeliefert hat.

Für den Rechnungsprozess muss ich halt wissen, wie teuer ist das Produkt?

Welchen Mehrwertsteuersatz muss ich dafür berechnen?

Und ich muss halt wissen, was die Rechnungsadresse des Kunden ist.

Das führt eben dazu, dass ich da eben gewinne an Autonomie, wenn ich sage, ich habe ein spezifisches Modell für Rechnungslegung oder Bestellung, das halt in diesem Modell für den Rechnungslegungsprozess drin ist.

Was ich damit versuche zu sagen ist, ich treffe häufig auf diese Geschichte mit, aber ich will ja jetzt irgendwo den Kunden modellieren.

Die Antwort ist jetzt, kannst du halt irgendwie tun.

Software ist soft und natürlich kannst du ein Modell für den Kunden haben.

Das ist auch ein Modell, wir haben ja darüber gesprochen, modelliert er nicht.

Das Produktchecker, das ist vielleicht der Eberhard selber in Kaiserslautern, sind also unterschiedliche Dinge.

Also es wird halt einmal sehr kompliziert und zum anderen ist es so, dass du die Autonomie einschränkst, weil es bedeutet eben, dass dieser Lieferprozess beispielsweise nicht ohne das Kundenmodell und ohne das Produktmodell auskommen kann.

Und wenn du das willst, aus irgendwelchen Gründen, ist es halt fein, du torpedierst Ich finde es halt immer gut, diesen Trade-Off halt explizit zu machen und vielleicht ist das sozusagen ein Einflussfaktor, den man da nutzen kann.

Und das passt eben auch zu diesem Thema mit dem Information Hiding.

Wir wollen weitestgehend verstecken, wie irgendetwas funktioniert.

Das heißt also, wir wollen nicht wissen, welche Information eines Kunden wir jetzt genau benötigen für den Lieferprozess, sondern das soll vielleicht versteckt sein.

Und damit sind wir wieder bei diesem Information Hiding, bei dem vom Anfang.

Wir suchen nur einen Teil, wo wir halt an der Schnittstelle hinschreiben können.

Ich möchte gerne, dass das jetzt zum Kunden geliefert wird.

Wie das detailliert dann im Hintergrund passiert, ist mir eigentlich egal.

Und wenn das Ding jetzt unbedingt das zentrale Kundenmodell nutzen will, meinetwegen, führt halt zu einer zusätzlichen Schnittstelle und führt dazu, dass ich ein kompliziertes Modell habe.

Kannst du halt tun, es hat einen Trade-Off.

So, das war also das, was ich da...

Und das habe ich jetzt die Hoffnung, hilft halt ein bisschen, besser über Fachlichkeiten nachzudenken.

Ich bin aber noch nicht ganz am Ende.

Also das ist offensichtlich keine fertige Heuristik, um halt Modelle zu finden und Systeme aufzuteilen.

Aber es zählt vielleicht sozusagen beim Denken.

Und ein weiteres Werkzeug, was man nutzen kann, ist Event-Storming.

Das Problem, was ich mit Event-Storming habe, ist, ich brauche etwas, wenn mir jemand eine fachliche Architektur vorlegt und sagt, hier ist irgendwie dieses Ding.

Das ist übrigens unser Ding, was irgendwie was über Kunden sagt.

Da muss ich eine Heuristik haben, die mir sagt, ist das eine gute oder eine schlechte Idee?

Und ich habe jetzt gesagt, das ist wahrscheinlich eine schlechte Idee, weil wahrscheinlich dadurch die Autonomie von den Dingern, die tatsächlich Funktionalitäten erbringen, wie zum Beispiel den Lieferprozess, das einschränkt.

Und da hilft eben sowas, sich zu überlegen.

Also sind das gute Modelle?

Dafür hilft, glaube ich, einmal diese Idee von den ADTs und diese Geschichte von Autonomie.

So, der Christoph bei Mastodon hatte mich noch hingewiesen auf Cell-Based-Architecture und das wollte, also das passt ein bisschen hier rein, weil Bonded-Context halt tatsächlich im blauen Buch von dem Eric als Illustration so eine Zelle hat.

Und eine Zelle definiert sich halt eben dadurch, dass es eine Zellwand gibt, die halt nicht das Interne der Zelle, also die biologische Zelle, das Interne der Zelle hat abgrenzt von dem Außen und hat eben kontrolliert, was rein und raus geht.

Sondern das ist, das passt also als Metapher und ist da sozusagen anerkannt auch.

Und das ist jetzt etwas, wo ich erst dachte, dass das eigentlich ganz gut zu dem passt, was wir irgendwie heute diskutieren.

Und das tut es in gewisser Weise auch.

Aber insgesamt bin ich da jetzt gar nicht so begeistert von.

Aber ich sollte es vielleicht nochmal kurz erklären.

## Cell-Based Architecture

Also die Idee ist halt, ich habe so ein System, das aus Zellen aufgebaut ist.

Die haben eigene Daten, eine eigene Logik und einen eigenen Zustand.

Das ist genau das, was ich mit diesen Modellen ja gerade fordere.

Ich will halt ein Ding haben, dem ich jetzt sage, ich liefere das Produkt aus und idealerweise ist die Logik, der Zustand und die Daten dafür da drin, sodass das halt irgendwie das autonom erbringen kann.

Das heißt, Autonomie ist irgendwie das Ziel.

Das passt also.

So, dann steht da halt irgendwie, ich will das unabhängig entwickeln.

Klar, also wir wollen eine fachliche Aufteilung, damit wir das unabhängig entwickeln können.

Und dann steht da etwas von unabhängigem Deployment und Skalierung.

### Kritik an Cell-Based Architecture

Und da sind wir jetzt wieder an der Stelle, was ich auch bei den Bauern und Kontexten kritisiere, dass wir plötzlich drei Ziele haben, die halt unterschiedliche Aspekte betrachten.

Also unabhängige Entwicklung impliziert nicht unbedingt unabhängiges Deployment.

Wir können uns zusammensetzen an einem großen, modularen, monolithen Arbeiten, nicht Modulist.

Oliver hat da ja irgendwie was zusammengebaut, mit dem man das halt irgendwie tun kann.

Können wir relativ unabhängig entwickeln.

Wir können es aber nur als Ganzes deployen.

Ist das eine blöde Idee?

Nein, weil es kann eben sein, dass ich nicht dieses modulare Deployment benötige und ich benötige vielleicht auch keine modulare Skalierung.

Und da ist wieder dasselbe Problem wie bei den Bauern und Kontexten.

Also warum sage ich halt, dass ich Zellen haben will, die ich unabhängig deployen und skalieren und entwickeln will?

Es kann, ich suche etwas, wie ich ein System fachlich aufteilen kann.

Und dafür ist die unabhängige Entwicklung relevant.

Und dann will ich eben entscheiden, anhand von irgendwelchen Maßstäben, ob ich die Sachen unabhängig deployen will oder nicht.

Vielleicht will ich unterschiedliche Teile auf unterschiedlichen Systemen deployen, weil das eine hat ganz viele GPUs und ich habe da Sachen, die von GPUs profitieren können.

Und ich habe andere Sachen, die von GPUs nicht profitieren können.

Das wird aber etwas anderes sein als die fachliche Aufteilung.

Es könnte zum Beispiel sein, dass das, was auf der GPUs Tour ein Berechnungskern ist, was eben GPUs ausnutzt.

So und das hat nichts mit einer Fachlichkeit zu tun.

Das ist sicherlich keine Zelle.

Trotzdem will ich das unabhängig deployen auf Rechtern, die GPUs haben und die anderen Sachen auf anderen Rechtern.

Ich verstehe wirklich nicht, warum man das kombinieren möchte.

Und dann ist die Aussage, eine Zelle ist ein Bauern und Kontext.

Da wird also eigentlich jetzt der Bauern und Kontext nur in der Definition oder im Sinne von Modell genutzt.

Intern können dann solche Zellen Legacy Komponenten haben oder Microservices oder was anderes, was halt eine technische Aussage ist.

Und ich finde das eben, wie gesagt, schwierig, weil es eben Technik, Organisationen und Modelle mischt.

Und es ist so ein bisschen schlimmer als Bauern und Kontexte, weil die immerhin damit nichts zur Technik sagen, nicht also Bauern und Kontext könnte oder das Modell eines Bauern und Kontextes kann eben in einem Microservices implementiert sein oder hat in einem Deployment Monolithen als ein Teil des Deployment Monolithen.

Das geht beides so und das fokussiert jetzt eben plötzlich an irgendeiner Stelle auf solche Qualitäts Attribute wie Skalierbarkeit.

Und das finde ich halt nicht so wichtig.

Insgesamt wirkt das so ein bisschen wie Microservices richtig gemacht.

In dem Sinne, dass man halt eigentlich eben bei Microservices genau das idealerweise anstrebt.

Also eben sagt, ich will halt unheimlich viel Fertigkeit haben.

Ich will das halt irgendwie auf Teams verteilen.

Ich will es unheimlich deployen.

Ich bin mittlerweile und wie soll ich sagen.

Das kann man ja durchaus argumentieren.

Also ich sage jetzt, ich habe ein Team, das macht den Bestellprozess.

Der Bestellprozess baut diesen einen Microservice.

Der wird unheimlich deployt und dann hätte ich eben das, was sozusagen Cell-Based sagt.

Ich finde das halt deswegen schwierig, weil man sich eigentlich die Frage stellen muss, muss ich das unabhängig deployen?

Will ich nicht Monolithen?

Wieso schließe ich ein Monolithen aus?

Dafür kann es Gründe geben.

Nur das ist eine andere Entscheidung.

Das ist nicht die Entscheidung.

Das ist halt eine Fachlichkeit.

Und ich kann durchaus eben ein Team auf mehr Fachlichkeiten arbeiten lassen und ich kann auch durchaus mehrere Teams an diesem Bestellprozess arbeiten lassen.

Es führt nun potenziell zu Reibungsverlusten und sowas wie Cell-Based gibt halt ein sehr einfaches Schema vor, ähnlich wie bauende Kontexte, was halt sagt, du baust halt einfach eine Zelle.

Diese Zelle ist eben so, dass sie ein Team ist, eine Fachlichkeit umfasst und so weiter.

Das Einzige, was ich halt bei dem Modell tatsächlich ganz spannend finde, ist irgendwie zu sagen, ich habe Legacy-Komponenten und neuere Komponenten, die halt dort potenziell zu so einer Zelle passen.

Was eben bedeutet, dass ich dort nicht sage, das ist nur ein Microservice, sondern das könnte auch durchaus irgendetwas sein, wo noch Sachen in einem Altsystem drin stecken oder so was.

Und das ist auch etwas, das kann durchaus helfen, weil eine Fachleitfunktionalität kann eben durchaus in einem Legacy-System und dann eben später in einem monolithen neuen System umgesetzt werden.

Ich glaube, das war so das, was ich erst mal im Wesentlichen sagen wollte.

Ich weiß nicht, ob von eurer Seite noch Fragen sind.

Ich hatte halt, genau, Mark hatte sich schon verabschiedet.

Taskwork hat geschrieben, bei Events Domain oder DDD denke ich nicht zuerst an allgemeine Datentypen.

Ne, das tue ich halt nicht, sondern da habe ich halt eben Events und versuche daneben durch Swimlanes, also Sachen, die ja Parallel sind und Pivotal Events, also Events, wo sich was fundamental ändert, das halt zu unterteilen.

Das sind irgendwie Kandidaten, die man häufig mit einem getrennten Datenmodell umsetzen kann.

Matthias hat gesagt, ich glaube, das Diplom in Orthogonal dazu ist, hat an sich nichts damit zu tun, nur ist ein guter fachlicher Stint.

Natürlich für Sebastian ist Diplom in Förderlich.

Und das würde ich eben, also wie soll ich sagen, in dieser, ich sage jetzt mal etwas naiven Welt, die halt Cell-based darstellt, ist das so nicht, da sage ich halt, ich habe ein Team, das halt etwas Fachliches getrennt deployed, was ich jetzt gerade versuche zu sagen ist, das ist aber nicht immer so, also es hält mich niemand davon, also wenn ich jetzt sage, ich habe so ein Ding, was eine generelle Datenanalyse auf Basis von GPUs macht und verschiedene fachliche Module machen eine Datenanalyse für verschiedene Dinge auf diesem einen Ding, was eben mit GPU-Unterstützung so eine Analyse anbietet, dann habe ich ein technisches Ding, das ich separat deploye auf so einem GPU-Ding, was von diesen verschiedenen fachlichen Komponenten, die eben dort ihre Berechnungen auslagern, genutzt wird.

Dann hat dieses separate Deployment nichts mit der Fachlichkeit zu tun, sondern es ist eine technische Geschichte.

Das kann man natürlich sagen, nicht lieber Eberhard, du ziehst halt irgendwie Dinge sozusagen an den Haaren herbei, aber das, also erst mal so etwas begegnen mir ja tatsächlich in der Praxis und das andere ist auch, wie soll ich sagen, ich, wieso muss ich drei Dinge, die halt unterschiedlich sind, Deployment, Fachlichkeit oder eben Teamverantwortung, wieso muss ich das zwangsläufig bei einem Kamm scheren und also insbesondere, also nicht bei dem Deployment ist das, was du sagst, Matthias, glaube ich, noch am ehesten als Vereinfachung nachvollziehbar, bei den Teams halte ich das mittlerweile für relativ absurd, weil wenn ich sage Teams müssen an einem bauenden Kontext arbeiten, dann sage ich, es gibt keine technischen Infrastruktur, Teams, die hat eine technische Komponente bauen, das gibt es nun wirklich, nicht, also es gibt nun wirklich Leute, die halt irgendwie rumlaufen und sagen, ich kümmere mich halt um das Technik, solche Infrastrukturgeschichten wie Kubernetes oder so, nicht so was, was ein Plattformteam macht in Team Topologies oder auch irgendwelche anderen technischen Infrastruktur-Teams als eigene Libraries und die haben, sind natürlich validerweise da und natürlich müssen die dann auch mit Teams interagieren, die hat Fachlichkeiten bauen und das muss sich irgendwie abdecken und da jetzt irgendwie zu sagen, ein Team definiert sich halt durch einen bauenden Kontext, nee, also da gibt es andere Teams und die sind halt auch wertvoll und das ist eben dann tatsächlich irgendwie ein Fehlschluss, nicht, und deswegen würde ich halt dafür plädieren, diese drei Aspekte, also Deployment-technisch, Teams irgendwie so organisatorisch und eben diese Modelle, über die ich spreche, das halt zu trennen und das ist ja der Grund, weswegen ich halt sage, diese Geschichte mit den bauenden Kontexten finde ich halt schwierig und vielleicht sollten wir uns auf Modelle fokussieren, weil ich glaube, das ist das zentrale Thema.

Jetzt muss ich mal zu dem was Matthias noch geschrieben hat.

Was denkst du zu dem hier?

Ein Kontext ist ein Bereich, in dem sich verschiedene Menschen über die Bedeutung eines Begriffs einig sind.

Wenn sie es nicht sind, wird das Modell mehrdeutig.

Ja, also ich glaube auch, dass bauenden Kontext eigentlich in erster Linie hilfreich ist in Bezug auf ubiquitous language.

Ich bin mir gerade nicht sicher, ob das tatsächlich auch im blauen Buch so in den Mittelpunkt gestellt wird.

Sprich, diese Idee, dass eben Kunden in unterschiedlichen bauenden Kontexten eine unterschiedliche Bedeutung haben, das ist glaube ich eine sehr mächtige Idee und das führt dazu, dass ich diese Modelle eigentlich idealerweise trennen sollte.

Aber Software ist Soft.

Ich kann versuchen, das generelle universelle Modell für einen Kunden zu entwerfen.

Es wird nur irgendwie super schwierig.

Ich finde es schwierig zu sagen, ich baue ein Modell, das solche Mehrdeutigkeiten akzeptiert.

Also wenn ich in einem Modell den Kunden habe und das sind unterschiedliche Sachen, das ist echt weird.

Warum eigentlich?

Ich weiß nicht.

Wenn ich eine krasse Kunde habe, ist sie nicht mehr eindeutig.

Deswegen ist es schon so, dass diese bauenden Kontexte mit der ubiquitous language, dieser Aspekt der Idee ein guter Indikator dafür ist, dass ich Sachen getrennt umsetzen will mit getrennten Modellen.

Ich bin mir noch nicht sicher, ob das hilfreich ist.

Wenn ich aus einer technischen Sicht komme und sage, wo will ich welche Funktionalität in den Schnittstellen haben?

Dann stelle ich fest, ich habe einen Lieferprozess und dann stelle ich fest, ich habe einen Rechnungslieferungsprozess und dann fange ich an, die Implementierung zu bauen.

Dann stelle ich in der Implementierung fest, der Kunde, den ich jetzt gerade versuche zu implementieren, für die Rechnungslegung brauche ich eine Rechnungsadresse.

Bei der Lieferung stelle ich fest, ich brauche eine Lieferadresse.

Dann grabe ich weiter und stelle fest, das sind potenziell unterschiedliche Kunden.

Rechnung geht auf Swagglab GmbH, Lieferung für den Laptop geht zu Eberhardt.

Dann komme ich zu einem ähnlichen Ergebnis, ohne dass ich sage, ich habe ubiquitous language und diese getrennten Bedeutungen von irgendwelchen Begriffen.

Mein Motivator oder mein Punkt, den ich versuche, mit dieser Episode zu machen ist, wir brauchen als TechnikerInnen eine Möglichkeit, Systeme fachlich aufzuteilen.

Dafür liegt vielleicht dieser Denkprozess, den ich jetzt gerade beschrieben habe, als der Denkprozess, den ich eher beim Business-Analytiker sehen würde, der feststellt, der Kunde ist tatsächlich etwas unterschiedliches durch Analyse.

Wenn ich Daten nehme, um versuchen, eine Implementierung zu bekommen, komme ich zu einem ähnlichen Ergebnis wie der Business Process Engineer oder der Business Analyst.

Nur liegt mir das vielleicht näher in meinen Überlegungen.

Das ist das, was ich versuche zu sagen.

Ist diese Geschichte mit der ubiquitous language tatsächlich hilfreich?

Weiß ich nicht genau.

Matthias schreibt genau, deswegen ein Modell immer in einen Kontext packen.

Aber das impliziert ja schon die Definition eines Modells.

Modelle sind Abbilder eines Originals, abstrahieren nur die relevanten Eigenschaften und erfüllen eine pragmatische Funktion.

Das heißt, ein Modell für eine andere pragmatische Funktion kann ein anderes Modell sein und kann andere relevante Eigenschaften haben.

Das heißt, in dem Begriff Modell ist schon Baune Kontext angelegt.

Matthias schreibt, lass uns eindeutige Modelle machen.

Dann brauchen wir den Baune Kontext eigentlich nicht, weil wir ihn implizit schon haben.

Es wäre mal interessant, in einer Welt zu leben, wo wir nicht mehr über Baune Kontext reden, sondern über Modelle.

Und dann im Sinne von Dinge, die wir als Software implementieren, als Abbildung von Realität.

Ich würde das deswegen für gut halten, weil es dann klar ist, dass wir nur über diesen Aspekt von Baune Kontext reden und die anderen Aspekte, nämlich die Geschichte mit der ubiquitous language und mit den Teams, dass die sekundär sind.

Ich glaube, dass dann Dinge einfach zu verstehen sind.

Ich bin in Diskussionen gewesen, die ungefähr so waren, dass sie gesagt haben, okay, das sieht aus wie eine vernünftige fachliche Aufteilung.

Aber was ist denn jetzt mit der ubiquitous language?

Die Diskussion will ich eigentlich nicht führen, weil wenn ich eine vernünftige fachliche Aufteilung habe, ist die Geschichte mit der ubiquitous language für mich relativ egal.

Ich will ja nur eine vernünftige fachliche Aufteilung.

Es ist tatsächlich so, dass da Verständnisprobleme sind, die sagen, warum haben wir jetzt hier zwar eine vernünftige fachliche Aufteilung, aber das mit der ubiquitous language ist nicht so klar.

Respektive, warum haben wir hier irgendetwas, was ein fachliches Ding ist.

Aber dieses Team macht mehrere fachliche Dinge.

Da würde ich gerne rauskommen, würde gerne spezifisch nur über fachliche Architektur mit fachlichen Modellen, die in verschiedenen Modulen implementiert sind, diskutieren.

Davon getrennt ist ja auch die Frage nach technischen Modulen.

Eine hexagonale Architektur sagt uns ja, wie wir technische Module oder Bereiche wie Persistenz herauslösen können aus unserer Anwendung.

Das ist etwas, was noch mal getrennt ist von diesen fachlichen Modellen, über die ich hier spreche.

Ich glaube, dann habe ich es tatsächlich soweit erledigt.

Dann würde ich sagen, vielen Dank für die Aufmerksamkeit.

Schönes Wochenende.

Nächste Woche wird es einen Stream geben.

Ich bin noch nicht sicher, zu welchem Thema.

Ein Thema, was bei mir noch auf dem Stack liegt, ist bei der Agile Meets Architecture.

Da gab es eine sehr schöne Fragerunde und offensichtlich gab es eine Vielzahl an Fragen, die ich nicht beantwortet habe.

Das macht noch mal Sinn, daraus vielleicht eine Episode zu machen.

Das wäre so etwas, was ich planen würde.

Ich schaue auf die Webseite, da steht halt drauf, was im März nächstes kommt.

Dann würde ich sagen, vielen Dank, schönes Wochenende und bis dahin.