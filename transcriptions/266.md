# Folge 266 - Soll man LLMs für Software-Architektur nutzen? mit Ralf und Eberhard ## Einführung und Standpunkte

Und es soll um das Thema gehen, soll man LLMs für Software-Architektur nutzen?

Und genau dazu, also wir haben da, glaube ich, so sagen die Vorgespräche irgendwie kontroverse Meinungen zu.

Deswegen glaube ich, da wird das ein interessanter Stream und wir hatten uns überlegt, damit anzufangen, die Frage zu beantworten, wofür benutzen wir denn eigentlich so LLMs im alltäglichen Leben?

Um so irgendwie erstmal die Frage zu klären, wofür soll man oder kann man denn LLMs überhaupt benutzen?

Und Ralf, willst du dazu was sagen?

### Vorstellung der Diskutanten

Ich weiß nicht, ob du noch zwei Worte zu dir selber sagen willst.

Du bist ja sozusagen Corus, von daher sollte das ja eigentlich, soll das ja eigentlich bekannt sein.

Ja, also genau, ich spare die Zeit, stelle mich jetzt nicht vor, ich freue mich total auf diese Episode, weil, wie du sagst, ich glaube, wir haben zwei unterschiedliche Meinungen.

### Unterschiedliche Perspektiven

Du stellst die Frage, sollen wir LLMs für die Software-Architektur verwenden?

Ich stelle mir eher die Frage, wie verwenden wir LLMs für die Software-Architektur?

Dieses sollen oder nicht sollen, ich sehe gerade Michael Simons ist im Chat, das wird spannend.

Auf seine Kommentare bin ich gespannt, denn ich bin mit der Meinung, relativ weit vorne, dass ich denke, ja, wir werden in Zukunft Architektur und Software-Entwicklung mit LLMs machen und auch da sehr viel in die Hand der LLMs geben und ja, das ist so mein Eingangsstatement und du grinst schon, weil deine Meinung eine andere ist.

Du hast ja jetzt hier im Chat schon gesagt, von wegen hier, Software-Entwicklung wird sobald nicht von den Maschinen übernommen werden, wir sind ja jetzt bei der Architektur.

Was ist dein Eingangsstatement?

Genau, ich wollte erst mal, also für die, die sozusagen jetzt im Chat nicht zugucken, der Michael Simons hat gerade eine Popcorn-Tüte mit dem Emoticon losgeschickt und ich glaube, das war so der Punkt, also die Frage, ich habe irgendwo in der letzten Woche als sozusagen dieser Episode in meinem Hinterkopf schon existierte, darüber in so einem Brustgelesen von wegen, dass irgendwas im Sinne von, dass die Person halt davon genervt ist, wenn man da irgendwie sagt, also jetzt mal ethische Fragen beiseite, wofür können wir eigentlich LLMs nutzen?

Und tatsächlich ist das hier so ein bisschen eine Episode, die halt irgendwie in diese Richtung geht und ich möchte da kurz verweisen auf diese Episode mit dem Lukas Dom, vor einiger Zeit, wo wir, glaube ich, auch diese ethischen Fragen damit diskutiert haben, tatsächlich würde ich das ein bisschen ausblenden, wir wissen alle, dass das irgendwie dazu führt, dass wir halt hohen Energieverbrauch haben, wir wissen alle, dass es da irgendwie Menschen gibt, die ausgebeutet werden, wir wissen, dass es halt diese Schwierigkeiten gibt rund um das Copyright-Recht, wir wissen halt, dass der Aaron Schwarz für viel kleinere Copyright-Probleme letztendlich in die Situation gebracht worden ist, die er mit einem Selbstmord beendet hat im Vergleich zu dem, was halt jetzt irgendwie systematisch passiert, das ist nicht das Thema heute und ich wollte eigentlich erst mal die Frage stellen, wofür wir eigentlich LLMs benutzen und ich muss halt gestehen, also der Abstract für diese Episode kommt, glaube ich, von dem LLM, nicht?

Den hast du gebaut, Ralf, wenn ich es richtig sehe?

Ja, Claude hat den gebaut.

Genau so und also bei mir ist es halt auch so, dass halt alle Abstracts, die ich halt baue, durch ein LLM laufen, einmal um halt irgendwie Lesbarkeit zu verbessern oder halt auch irgendwie Dinge in dieser Richtung halt zu machen.

Ich habe einen Blog bei Heise und ich habe irgendwie diese Architekturkolumne beim Java-Magazin, die übersetzt halt ein LLM auf Englisch und das erscheint dann irgendwie bei mir im Blog und ich nutze halt auch zunehmend LLMs für Probleme, wo ich halt das Gefühl habe, dass eine Suchmaschine nicht so richtig gut einem helfen kann und vielleicht auch so als so einen kreativen Kickstart, also tatsächlich hat die halt gestern gesagt, gib mir mal ein paar alternative Titel für diesen Vortrag und da kam halt irgendwas bei raus.

Mein Mantra ist dabei, dass ich halt die Ergebnisse von dem LLM halt kontrollieren muss.

Das heißt also, ich editiere die irgendwie nochmal nach und schaue halt, was da irgendwie rauskommt und betrachte das nochmal kritisch und das ist es eigentlich so im Wesentlichen.

Genau, was hast du da noch was ergänzen wollen würdest?

Ja, ich unterstütze es ja, dass du sagst, man muss das Ergebnis nochmal kontrollieren, aber ich denke mir halt auch immer, wir haben ein bisschen eine falsche Sichtweise auf die Maschine, dass wir von der Maschine erwarten, dass sie was Perfektes abliefert, weil es ja eine Maschine ist, war in der Vergangenheit so, wir lassen sie eins plus eins rechnen und erwarten zwei und mittlerweile können wir die Maschine überreden, dass eins plus eins drei ist.

Aber so im normalen Alltag, wenn ich mit Kollegen arbeite, dann gucke ich auch nochmal über die Ergebnisse drüber.

Wenn mir jemand ein Abstract vorschlägt, gucke ich auch nochmal drüber und das ist so die andere Sichtweise, dass ich es akzeptiere, dass die Maschine in dem Fall, weil sie ein LLM ist, nicht perfekt ist.

Und das ist vielleicht gleich ein guter Hinweis, um nochmal abstrakt auf dieser Ebene was über Standpunkte zu sagen.

Also ja, das ist eben eine Maschine und sie ist nicht perfekt und der Vergleich mit den Menschen bietet sich da ja irgendwie an.

Und Menschen sind halt auch nicht perfekt, aber hier ist ein wichtiger Unterschied und das ist halt irgendwie, dass man sich nach LLMs dazu neigen, gerade LLMs dazu neigen, Ergebnisse zu produzieren, die so katastrophal daneben sind, dass sie halt einfach unakzeptabel sind.

Und wir hatten ja im Vorhinein darüber gesprochen, dass wir uns irgendwie zwei Beispiele raussuchen wollen würden.

Ich würde jetzt tatsächlich mal in das eine Beispiel sozusagen gleich reingreifen, während ich irgendwie schaue, dass wir die Chatnachrichten durchziehen.

Ich glaube, wir sollten das Szenario kurz diskutieren, bevor wir gleich nochmal in den Chat gucken.

Und zwar ist es so, dass der Dirk Mahler, der war ja auch mal im Stream, der hat dieses JQS System mitgebaut, was letztendlich halt so ein System ist, was so Eigenschaften, also Architekturmanagement betreibt und dann die Daten in Neo4j ablegt.

Und er hat jetzt so ein Ding, so einen Fall zusammengebastelt, kann man bedingt nachlesen, wo er mit dem LLM, nämlich mit Claude über dieses MCP, Model Context Protocol, dem Zugriff gegeben hat auf Daten, die in der Neo4j-Datenbank drin waren, die also JQS System erzeugt hat.

Und ich hatte mit Dirk nochmal gesprochen, weil ich das Thema gerne aufgreifen wollte.

Und er hat gesagt, ja, das ist natürlich kein Problem und das finde ich super.

Von daher auch vielen Dank dafür.

### Beispiel ActiveMQ/Artemis

Und da sollte dann so eine Art Architekturbewertung rauskommen.

So eine von den Fragen, die diese Architekturbewertung beantwortet hat, war die Frage, welche Technologien werden denn genutzt?

So, da hat er halt dieses System freudestrahlend gesagt, dieses System benutzen unter anderem ActiveMQ und Artemis.

ActiveMQ ist ein Apache-Projekt, ein Messaging-System und Artemis ist eine Art Nachfolger von ActiveMQ.

Also ich würde jetzt nicht sagen, dass das eine Projekt tut ist, aber es ist irgendwie so nicht das nächste Projekt, was hat versucht, die nächste Messaging-Infrastruktur zu bauen.

Und das ist also jetzt genau so ein, das was du halt einen Fehler nennst oder gerade eben Fehler genannt hast, das was halt Menschen im KI-Bereich der Halluzination nennen.

Und was ich, um es deutlicher zu machen, worüber wir eigentlich reden, eine Fake-Information nennen würde.

Dieses Ding hat eine Fake-Information halt erfunden.

Es ist halt irgendwie die Frage, was bedeutet denn das?

Und wenn ich jetzt so ein, ich oder ein Kollege von mir, so ein Review abgegeben hätte, wo er so drin steht, benutze übrigens ActiveMQ und Artemis, dann gäbe es aus meiner Sicht ein richtiges Problem.

Und also ich weiß nicht genau, was ich machen würde, aber es wäre auf jeden Fall so, dass ich halt im hohen Maße unzufrieden wäre.

Und ich würde erwarten, dass ein Kunde, der uns beauftragt hat, uns nicht wieder beauftragt, wenn wir das nicht irgendwie sehr gut erklären können.

Das hängt irgendwie damit zusammen, dass das halt auf einen ganz anderen Architektur hinweist, wenn ich ein Messaging-System benutze, als wenn ich es nicht benutze.

Das ist halt was anderes.

Und dann ist es halt immer noch so komisch, weil halt diese beide Technologien benutzt werden, also die sozusagen Active als eine und dann nennen wir auch sozusagen der Nachfolger.

Und ich glaube auch ehrlich gesagt nicht, dass mir in den Reviews, die ich gemacht habe, so ein Fehler jemals unterlaufen ist.

Denn ich habe die Angewohnheit, wenn ich es sozusagen fertig habe, nochmal alles durchzugehen und zu sagen, was ist das Faktum, habe ich tatsächlich einen Beleg dafür, stimmt das?

Und zwar genau aus dem Grund, weil wenn diese faktischen Dinge falsch sind, dann wird es halt irgendwie schwierig.

Also weil ich damit halt einfach Vertrauen zerstöre.

Und das führt jetzt zu der Frage, was kann ich jetzt mit diesem Ergebnis eigentlich anfangen?

Also der kippt mir halt irgendein Ergebnis vor die Füße und sagt also, mein System sieht ja mit folgendermaßen aus.

Ich würde behaupten, ich kann mit dem Ergebnis nichts anfangen, weil das Ergebnis enthält Fake-Informationen und ich weiß nicht wo.

Wenn ich weiß, wo die Fake-Informationen sind, dann kann ich das lieber selber schreiben.

Ich behaupte also deswegen, dass das eigentlich nutzlos ist.

Und jetzt kommt halt die nächste Frage und das war für mich diese Geschichte war ein Motivator, um mich damit nochmal auseinanderzusetzen, weil mich auch die Reaktion auf das LinkedIn-Post ein bisschen irritiert hat, weil da im Prinzip irgendwie die Frage aufkam, wie kommt denn der auf die Idee?

Warum ist da dieser Fehler drin?

Und das sind ja eben das, was man Halluzinationen nennt.

Und daraufhin habe ich jetzt irgendwie da nochmal nachgebohrt und habe irgendwie, es gibt so ein Survey.

Ich verlinke den auch nochmal.

Ich habe ihn ehrlich gesagt nicht gelesen.

So ein Survey ist eine wissenschaftliche Zusammenfassung von verschiedenen Themen, verschiedenen Papern und da steht halt meiner Ansicht nach drin, diese Halluzination kann man nicht lösen.

Man kann sie wenn dann nur mitigieren.

Es gibt intrinsische Halluzinationen, die also den Trainingsdaten widersprechen.

Das wäre ja genau so etwas.

Die Trainingsdaten sagen oder die Daten, auf die dieses System aufbaut, sagt kein Artemis, kein ActiveMQ.

Es wird dann aber trotzdem diese Information erzeugt.

Oder es gibt Halluzinationen über Dinge, die in den Trainingsdaten nicht vorkommen, wo man dann kreativ irgendwelche Lücken füllt.

Kreativ ist das falsche Wort, aber wo das LLM die Lücken füllt.

Und da steht halt irgendwo drin, das kriegen wir irgendwie gelöst.

Und in der Zeit kam halt irgendwie auch die Nachricht, auch das verlinke ich nochmal, dass eben JGPT und OpenAI mehr Halluzinationen produziert und sie wissen nicht, warum.

Und das bedeutet, das Problem ist halt schlimmer geworden an der Stelle und es ist offensichtlich so stark nicht lösbar, dass man noch nicht mal weiß, was die Ursache ist.

Und damit würde ich behaupten, ist das Problem, was wir da sehen, ein typisches Problem und das wird halt nicht weggehen.

Und damit sehe ich halt nicht, wie man halt jemals ernsthaft so etwas wie ein Review oder überhaupt eine Aussage über ein System von einem LLM generieren lassen kann.

Und jetzt entschuldige ich mich dafür, dass ich so lange monologisiert habe.

Und jetzt versuche ich mal deine Gedankengänge einzeln wieder aufzugreifen.

Du hast jetzt gesagt, dem Review kannst du nicht vertrauen.

Wenn dir jemand so ein Review vor die Nase legen würde, das wäre eine Katastrophe.

Jetzt frage ich dich, wie lange brauchst du für so ein Review?

Da ist von der Maschine innerhalb von drei Sekunden ein Review erzeugt worden.

Und wir sind von dieser Technologie erst mal jetzt gewöhnt, dass wir einfache Sachen in Nullkommanichts beantwortet kriegen.

Und wir sind mit den Ergebnissen zufrieden und deswegen gehen wir stärker in die Tiefe.

Aber ich glaube, diese Frage, wo das herkommt, warum man jetzt diese Technologien denkt, dass sie drin sind, obwohl sie nicht drin sind, das ist das eine.

Ich könnte mir vorstellen, ich glaube, das war jetzt hier aus einer Datenbank rausgezogen.

Aber wenn es jetzt aus Source Code rausgezogen wäre, wäre ich nicht erstaunt, wenn tatsächlich irgendwo ein Kommentar drin stehen würde.

Hallo, wir könnten hier ActiveMQ verwenden.

Und aufgrund der Mechanismen, wie die Systeme auf die Artefakte, den Code zugreifen, eben Rack, dass da nur Fragmente rausgezogen werden, könnte es sein, dass das System nicht unbedingt halluziniert hat, sondern getäuscht worden ist.

Aber worauf ich auch hinaus möchte, ist, wenn das System innerhalb von drei Sekunden eine Antwort liefert, dann hat das Einfluss gehabt.

Und wenn du jetzt so ein Review erstellst, dann würdest du auch erst mal so eine Liste an Technologien zusammenstellen, die du jetzt erst mal vielleicht die erste Liste im Kopf, die du dann verifizierst gegen Source Code, gegen Fakten und guckst, ob das so passt und würdest dich korrigieren.

Genau das ist das, wo wir, glaube ich, hin müssen, dass die Maschinen noch mal mehrere Iterationen bekommen.

Weil wenn ich zum Beispiel dann als nächstes frage, kannst du mir Belege für diese Technologien liefern?

Dann wird die Maschine mittlerweile, ich meine, die haben ja jetzt alle möglichen Tools an der Hand, Reasoning-Modelle können.

Was habe ich gelesen?

Einmal hat es irgendwie 70 Minuten nachgedacht, wie es irgendein Problem lösen soll.

Also sie können in Iterationen gehen, wenn ich ihnen Tools gebe, dass sie sich verifizieren können.

Dann können sie das auch allein machen und finden solche Fehler eben teilweise selbstständig, wenn wir ihnen mehr Zeit geben, mehr Ressourcen.

Und ich glaube, das ist eben mit so einem Punkt in die Richtung wir gehen müssen.

Und deswegen sage ich halt auch eher, wie können wir das erreichen, dass es weniger wird?

Meistens wird von Halluzinationen gesprochen.

Manche Leute sagen eher positiv, das ist ja auch Kreativität, wenn jetzt irgendwelche Lösungen gesucht werden.

Ich finde es spannend, wo tatsächlich die Grenzen sind, weil momentan ist es so, dass wenn man sagt, es geht nicht, dann kommt doch einer daher und findet einen Weg.

Und wir haben gerade so diese Phase, wo es viele Leute gibt, die sagen, Mensch, die Halluzinationen, da kann ich mich nicht darauf verlassen.

Aber auf der anderen Seite gibt es Leute, die sagen, guck mal, habe ich gerade mit der KI gemacht, beziehungsweise KI hat für mich gemacht.

Und diese Diskrepanz, das finde ich so spannend, weil ich eben auch noch nicht weiß, wo sind die Grenzen der KI, was kann sie, wo hängt sie sich auf, was geht gut, was geht schlecht.

Und da finde ich zum Beispiel jetzt so aufs Kleine bezogen, dass die KI schlecht mit Zeilennummern umgehen kann.

Wenn ich sie einen Diff generieren lasse, hat sie oft bei One Errors und der Code ist kaputt.

Und deswegen sieht man auch bei den ganzen Coding Assistants, dass sie komplett den Text runter generieren als Workaround.

Genau, also verschiedene Begründe dazu.

Die erste Sache ist, du sagst, das LLM ist schneller.

Ich halte das, um es platt zu sagen, für unerheblich, weil wenn das Ergebnis nicht nützlich ist, ist es egal, wie schnell ich es erstelle.

Und ich kann das Ergebnis nicht nutzen, weil das Ergebnis Fehler enthält.

Und das bedeutet, dass die Geschwindigkeit, mit der ich irgendetwas erstelle, tatsächlich meiner Ansicht nach nicht ernsthaft ein Thema sein soll.

Was ich auch spannend finde, ist, dass du im Prinzip in dieselbe Richtung läufst, wie eben der LinkedIn Post und insbesondere die Menschen, die das weiter kommentiert haben.

Nämlich versuchst du zu erklären, dass das ja irgendwie ein Versehen ist.

Nee, ist es eben nicht.

Es ist eben so, dass LLMs Halluzinationen haben, Fake-Informationen produzieren.

Und das ist inhärent.

Es gibt kein Indikator dafür, dass dieses Problem lösbar ist.

Weder in diesem wissenschaftlichen, in diesem Survey, noch ist es so, dass OpenAI als wahrgenommener Marktführer in diesem Bereich dieses Thema überhaupt so unter Kontrolle hat, dass es besser wird.

Und das bedeutet, das Thema ist halt tatsächlich nicht lösbar.

Ich weiß nicht, ob wir in den Chat reinkommen, weil ich bin etwas überfordert, weil ich muss zuhören.

Ich sehe jetzt hier gerade zufällig von dem Martin Axiomär.

Enthält jede LLM-Ausgabe einen Fehler?

Nein, aber das Problem ist halt, ich weiß ja nicht, welcher einen Fehler enthält.

Das heißt also, in diesem Fall kriege ich eine Aussage über dieses, was auch immer es ist, also eine Softwarearchitektur.

Und ich weiß nicht, ob sie richtig ist oder falsch.

Und das hängt eben damit zusammen.

Und das ist auch das, was ich in der Episode mit SKI Bullshit eigentlich diskutiert habe.

Da gibt es ja genau dieses Paper, was argumentiert, dass eine KI Bullshit produziert, im Sinne von, dass sie keine Rücksicht auf Wahrheit nimmt.

Und das ist nachvollziehbar, weil eben ein LLM kein Konzept von Wahrheit hat.

Und das führt eben dazu, dass sie natürlich Fehler produziert.

Und wenn ich jetzt anfange, in einen Dialog zu gehen, dann fängt sie an und produziert neue Dinge, die halt wahr oder falsch sind, weil sie ja einen Dialog führen möchte.

Und wenn ich dem Ding halt irgendwie sage, also das ist aber jetzt falsch, dann generiert sie halt eine neue Information, die mir halt irgendwie gefällt.

Die hat gesagt, ja, stimmt, ist falsch.

Aber das bedeutet nicht, dass da ein Lernen ist.

Es gibt kein Konzept von Wahrheit, sondern es bedeutet nur, dass ein Text generiert wird, der halt eine gute Fortsetzung dieses Dialoges ist.

Und ich verstehe auf der Ebene tatsächlich nicht, was der Nutzen ist.

Also ich kriege ein Stück Papier, also ein virtuelles Stück Papier, in dem jetzt irgendwie steht, dein System sieht folgendermaßen aus.

Da sind potenziell faktische Fehler drin.

Das weiß ich.

Und da sind wir ja noch nicht mal an der Stelle, dass ich es jetzt bewerte.

Also die Aussage, das System benutzt Ekta, Füm, Q und Atim ist, das ist ja eine triviale, faktische Aussage.

Die interessante Aussage ist, was mache ich denn jetzt mit dem Ding?

Was soll ich damit machen?

Wie werde ich es besser machen?

Was sind die Herausforderungen?

Und dafür muss ich halt irgendwie nicht einen Denkprozess haben.

Und der ist halt noch mal ganz was anderes.

Und das Ding scheitert ja schon auf dieser Ebene der faktischen Sachen, was ja irgendwie erklärlich ist, weil es ist eben ein Textgenerator.

Es ist nicht eine künstliche Intelligenz.

Es ist ein Textgenerator.

Das ist keine Intelligenz.

Es generiert halt einen Text.

Und der hört sich halt gut an.

Das ist das, was das Ding halt kann.

Ich finde es so spannend, weil mir ist die ganze Theorie, vieles der Theorie ist mir egal, weil ich arbeite damit und ich sehe Ergebnisse.

Und ja, ich vermeide verhält sich verdammt intelligent.

Du hast gesagt, es hat kein Begriff von was es war, was ist falsch, aber oder was ist richtig.

Dieses was ist richtig kriegt es zum Beispiel gerade in der IT, in der Softwareentwicklung hat es die Chance, wenn es Code produziert, den Code erstmal auszuführen, damit erkennt es, ob der Code syntaktisch korrekt ist, kann nochmal korrigieren und wenn Tests vorhanden sind, dann kann es tatsächlich auch kontrollieren, ob der Code was richtig macht.

Das haben wir natürlich in anderen Bereichen weniger, aber wenn ich eben das System bitte Referenzen rauszusuchen, warum es eben ActiveMQ in diesem Projekt gefunden hat, dann ist meine Erfahrung, dass es sehr schnell sagt, da gibt es gar keine Referenzen, da habe ich mich wohl getäuscht und diesen Zyklus und weil du auch gesagt hast, die Geschwindigkeit spielt eigentlich keine Rolle.

Wir haben jetzt hier auf einmal verschiedene Möglichkeiten, was wir mit dieser Geschwindigkeit anfangen können, weil wir eben doch mehr Iterationen laufen lassen können in einer kürzeren Zeit.

Wir können auch teilweise, wenn wir jetzt von der Softwareentwicklung zum Beispiel reden, etwas nicht nur einmal entwickeln lassen, sondern hundertmal in ganz kurzer Zeit und wir nehmen das, was die Tests besteht.

Also verschiedene Sachen dazu.

Die eine Sache ist eigentlich das Thema Softwareentwicklung.

Das hätten wir vielleicht am Anfang klären sollen.

Es gibt ein anderes Thema, was mit dem Thema, was wir heute diskutieren, glaube ich, verwandt ist und das ist die Frage, sollten wir LLMs benutzen für Softwareentwicklung und das ist ein verwandtes, aber ein anderes Thema.

Ich befürchte, ich kann nur wiederholen, wenn ich dem System sage, den Dialog führe und auf dieses Thema hinweise, dann kommt da eine vernünftige Antwort raus.

Die sind ja darauf optimiert, Antworten zu geben, die sozusagen beliebt sind und dann kommt da halt irgendetwas bei raus, was irgendwie den Eindruck erweckt, dass da irgendeine Art Denkprozess ist.

Aber das ist halt nicht so.

Also diesen Denkprozess gibt es halt nicht.

Das ist ein Textgenerator und ich glaube, da gibt es einen anderen Effekt der Erklärung.

Der andere Effekt der Erklärung ist, dass LLMs offensichtlich sehr gut da drin sind, Dinge zu produzieren, die überzeugend sind.

Es gibt ein Paper, was ich tatsächlich überflogen habe, was damit etwas zu tun hat.

Das ist so ein bisschen, wie soll ich sagen, nicht exakt dasselbe, aber eben relevant.

Und zwar geht es da um Persuasiveness, also um die Überzeugungskraft von Menschen versus JGPT 4 an der Stelle.

Das Ergebnis ist, wenn man es in zwei Sätzen zusammenfassen wollen würde, dass JGPT 4 dazu in der Lage ist, Menschen eher zu überzeugen.

## Problematik der Halluzinationen

Das Test-Setting ist ein bisschen was anderes.

Da geht es um politische Dinge.

Man führt einen Dialog und anschließend wird gesagt, ich habe die Menschen überzeugt.

Das ist deswegen interessant, auch gesellschaftlich interessant, weil wenn ich das Ding dann noch fütter mit irgendwelchen Daten über die Person, die ich versuche zu überzeugen, dann wird es noch mal besser.

Wenn man sagt, das ist ein weißer 52-jähriger Mann aus Kaiserslautern, dann kann es irgendwie noch mal besser argumentieren.

Und das, glaube ich, ist ein Teil der Erklärung für diesen Effekt, den ich in dieser Diskussion spüre, aber auch in diesem LinkedIn-Posting.

Die Dinge sind gut darin zu überzeugen.

Deswegen halte ich sie eigentlich eher für eine Gefahr.

Das ist genau das Problem.

Die sind darauf optimiert, sich überzeugend darzustellen.

Wir haben ja damals diese Episode gemeinsam gemacht zu diesem ARC42 für den Linter.

Das passt auch zu dem, was ich am Eingang gesagt habe.

Ich muss die Ergebnisse kontrollieren.

Wenn man das sagt, bedeutet das, dass ich eigentlich die Latte durch die Benutzung einer LLM noch höher lege, weil ich jetzt nicht jemanden brauche, der es macht, sondern jemanden, der das, was erzeugt wird, überprüft.

Das ist ja im Prinzip das, was du sagst.

Du sagst, ich habe eine LLM, das sagt jetzt, wie Active Function und Artemis wird genutzt.

Das überprüfe ich jetzt.

Ich weise das System darauf hin.

Da ist übrigens ein Problem.

Ich verstehe das nicht.

Ich gucke da nochmal rein.

Damit geidest du in diesem Fall eine LLM.

Du könntest genauso gut eine Person geiden in so einem Prozess, wo man sich Gedanken macht über eine Architektur.

Das behaupte ich jetzt mal.

Es hat jemanden coachen in eine Richtung oder in diesem Fall eine LLM coachen.

Ich glaube, das ist noch anspruchsvoller, als es selber zu machen.

Das wäre mein Gefühl.

Also da hast du wahrscheinlich recht, dass es selber machen momentan teilweise schneller geht.

Ja, aber die Erfahrung, die ich dabei mache, wenn ich mit dem LLM zusammenarbeite, die mir die Möglichkeit gibt, das nächste Mal besser mit dem LLM zusammenzuarbeiten, um es besser zu nutzen, die ist für mich sehr wertvoll.

Deswegen mache ich das.

Und du hattest jetzt den ASCII-Doc Linter angesprochen.

Das ist alles.

Wir sind da noch auf einem Niveau, wo wir, ja, du sagst es, die Ergebnisse hören sich überzeugend an, weil das Modell sehr eloquent ist.

Aber es ist halt noch am Anfang.

Also bei dem ASCII-Doc Linter hatte ich halt einfach mal ausprobiert, kann das Modell denn überhaupt mit einer Architektur arbeiten?

Kann es aufgrund einer Architektur etwas umsetzen?

Und das hat es schon mal gezeigt, dass es das kann.

Wie gut jetzt die Qualität ist, das Inhaltliche, ist noch mal tatsächlich was anderes.

Aber da spielt auch mit rein, dass, na ja, wie es unterschiedliche Menschen gibt, gibt es eben auch unterschiedliche LLMs.

Und die entwickeln sich ja auch weiter.

Und momentan geht es, glaube ich, auch in eine falsche Richtung, dass sie zu viel machen, zu eigenständig werden.

Aber unter Umständen, anderes LLM da auf die Architekturkomponenten angesetzt, hätte ich vielleicht auch ein anderes Ergebnis bekommen, auch wenn das Problem der Halluzinationen in diesen Modellen drin ist und nicht beseitigt werden kann.

Du hast ja auch oftmals, also du hast das Paper genauestens studiert.

Für mich kommen diese Halluzinationen immer aus so weißen Flecken in der Wissenslandschaft des LLMs.

Ist nicht immer so, ich weiß.

Teilweise kann auch einfach nur ein blödes Unicode-Charakter dazu führen, dass ich in eine ganz andere Ecke laufe mit dem LLM.

Aber das mit den weißen Flecken ist schon mal ein Ding.

Und man versucht es ja auch dadurch zu beheben, dass man die Modelle grounded, indem man ihnen eine Suchmaschine mitgibt, Zugriff auf den Code gibt und solche Geschichten.

Und die Erfolge sind davon nicht wegzudiskutieren, behaupte ich.

Ja, also nochmal sozusagen.

Also das Erste, was du ja gesagt hast, ist, okay, man kann also eine Arc42-Dokumentation generieren lassen.

Stimmt, kann man.

Ist halt ein Textgenerator, der kann alles Mögliche generieren, auch eine Arc42-Dokumentation.

Und das Andere, also nur damit wir uns nicht missverstehen, in dem spezifischen Beispiel hat das System nicht einen weißen Fleck halluziniert, sondern es hat gesagt, kontrafaktisch, dass das System Artemis und ActiveMQ nutzt, auf Basis einer Neo4j-Datenbank.

Ich würde behaupten, dass diese Information dort hätte drinstehen müssen.

Aber vielleicht will mir da auch irgendjemand widersprechen.

Das bedeutet, es ist tatsächlich so, dass das eben etwas ist, was nicht so ist, wie die Datenbasis es sagt.

Und jetzt kann man eben sagen, naja, okay, das ist halt ein Versehen.

Nee, dafür gibt es einen Begriff, das sind intrinsische Halluzinationen.

Das sind genau die, das sind die, wo man sagt, Fakt ist das, das ist etwas, was auch in der Wissensbasis drinsteht, und es wird etwas anderes aber ausgegeben.

Und das ist genau da, also würde ich behaupten, ist das, was da passiert ist.

Aber unabhängig davon, das ist etwas, was passieren kann.

Und damit ist das Ergebnis halt tatsächlich wertlos.

Aber ich würde gerne, glaube ich, in eine andere Richtung gehen.

Ich auch.

Auf Basis von dem, was du vorhin gesagt hast.

Also du hast ja gesagt, das war mal ein Experiment mit dem ARC-42 und das für dieses SG-DOC-Linter zu bauen.

Und ich fand es irgendwie super, dass wir das damals durchdiskutiert haben und dass du das irgendwie gemacht hast.

Weil auf jeden Fall führt es ja dazu, dass wir da Wissen aufgebaut haben.

Wofür benutzt du denn jetzt tatsächlich LLMs in der alltäglichen Arbeit?

Also du machst ja, glaube ich, Softwarearchitektur, was ja irgendwie sehr viel heißen kann.

Wofür benutzt du LLMs dann in dem Bereich?

Also mein Lieblingseinsatzbereich sind tatsächlich Architekturentscheidungen.

Und das geht ja jetzt natürlich in so eine Richtung, wenn da was halluziniert wird, ist das ein Problem.

Aber da kommt dieser Language-Model voll zum Einsatz, weil ich mit dem Modell diskutiere über eine Entscheidung und ich mache es zum Beispiel per Spracheingabe.

Ich droppe einfach meine Gedanken in das Modell.

Das Modell formuliert mir dann eine saubere Problemstellung, wo ich sage, okay, so ist es gut verständlich, ordentlich formuliert.

Es kennt aus meinem System Prompt die Vorgehensweise, die ich erwarte, wie ich so eine Architekturentscheidung aufbaue.

Und es kennt auch ein Template, in dem die Architekturentscheidung zum Schluss dokumentiert werden soll.

Und somit sind das erstmal tatsächlich Texttransformationen.

Zusätzlich unterstützt es mich aber auch noch mit seinem Lösungsraum, dass wenn ich Optionen für eine Lösung suche, was für Alternativen gibt es, kann es mir helfen und nennt mir tatsächlich eben auch Optionen, die mir vorher nicht bekannt waren und die ich dann teilweise auch zum ersten Mal mir angucke und merke, oh, das Modell hat recht.

Es ist besser geeignet als das, was ich vorhatte.

Und das ist dann so ein Sparings-Partner, der aus meiner Sicht sehr wertvoll ist.

Aber ich laufe in die Gefahr, was du eben auch beschrieben hast, dass ich einfach nur vom LLM mir die Entscheidung runterschreiben lasse.

Noch eine schöne Bewertungsmatrix, die realistisch aussieht.

Und wenn ich da nicht reingehe und mir die Details angucke, dann laufe ich tatsächlich Gefahr, dass ich Entscheidungen aufgrund von Halluzinationen treffe.

Was ja letztendlich bedeutet, das ist ja so ein bisschen der Punkt, an dem ich zum dritten Mal hier vorbeikomme, dass am Ende man es eben kontrolliert und halt selber sozusagen am Hebel sitzt.

Und das, was du jetzt skizzierst, sind ja Dinge, wo ich sonst vielleicht nicht eine ausführliche Web-Recherche machen würde oder was weiß ich was, um Ideen zu bekommen.

Aber letztendlich das eben selber kritisch hinterfrage und da dann selber Ergebnisse produziere.

Und das halte ich persönlich tatsächlich für nachvollziehbar, weil dieser Grundsatz mit, ich muss mir das selber entscheiden und überlegen, halte ich für nachvollziehbar.

Der ist nicht verletzt so rum.

Und dass man dadurch die Möglichkeit hat, sich noch mal andere Dinge anzugucken oder Imput zu holen, ist, glaube ich, irgendwie nachvollziehbar.

Und ich weiß nicht, wie es bei dir jetzt gerade aussieht.

Ich bin mir, ehrlich gesagt, noch nicht ganz sicher, wie wir mit den ganzen Kommentaren umgeben wollen, weil das sind eben tatsächlich ein paar mehr.

Ich hatte schon überlegt, ob das sozusagen Material für eine weitere Episode ist.

Wir könnten hier jetzt eben tatsächlich so ein paar Sachen einstreuen.

Bei der Aljoscha Rittner hat zum Beispiel geschrieben, ich habe gelernt, dass jede Dokumentation, die nicht gelesen wird, sinnlose Zeitverbrennung ist.

Generell, ich große Texthörsen in Aktion 40-Framework wird das eher gelesen als auch ein psychologisch Nö, was er eben sagt nicht.

Also dieses Experiment mit dem SK-Linter ist vielleicht nicht das, wo man hin will.

Ich finde es spannend, weil wenn mein LLM auch Code generieren soll, dann braucht es eine Grundlage.

Und dann ist die Architektur wieder für das LLM, was sie dann hoffentlich liest.

Wenn ich die Architektur nur per Rack reingebe, dann wird sie es nicht lesen.

Aber hier habe ich auch gerade eben gelesen von Aljoscha, kontextfreie Entscheidungen.

Auch das ist eben die richtige Herausforderung, dass ich mit dem Kontext richtig arbeite.

Wenn ich Qualitätskriterien, Qualitätsszenarien schon spezifiziert habe, dann sollte natürlich das LLM im Kontext diese Entscheidungen haben, dass es eben auch mithelfen kann, die Architekturentscheidung eben nicht kontextfrei zu generieren.

Wollen wir das Thema mit der Softwareentwicklung, unterstützt durch LLMs, also tatsächlich Code-Generierung diskutieren, weil dann würde ich da sozusagen ausholen?

Ich glaube, ich weiß, ich drifte immer wieder ab, aber ich sehe die Architektur als die Grundlage der Softwareentwicklung.

Und deswegen war das jetzt aus meiner Sicht wichtig, wer liest das Ganze.

Und in Zukunft bin ich mir sicher, dass die Maschinen weiterhin eine Architektur brauchen und dann eben diese Architektur von den LLMs gelesen wird, aber auch von uns Menschen.

Okay, also dann würde ich sagen, steigen wir tatsächlich so ein bisschen in dieses Thema ein.

Erstmal, das, was du diskutierst, ist etwas anderes.

Was du diskutierst und darstellst und für mich auch glaubwürdig ist und total viel Sinn macht, ist ein Ansatz, der sagt, ich fange an, ich nutze das wie ein weiteres Werkzeug, so wie ich auch Stack Overflow oder das Internet benutze und letztendlich kondensiere ich dadurch so eine Architektur.

Wir hatten das vorhin im Vorgespräch noch mal diskutiert.

Also ich glaube, hat genau dieses, ich habe einen Prozess, bei dem ich mir über irgendwas klar werde, irgendwelche Entscheidungen treffe und dann schreibe ich das auf.

Das ist eigentlich das, worum es geht.

Es geht nicht darum, ein Arc42-Template auszufüllen und ich habe auch gerade bei dieser Episode mehrfach oder bei dem Darüber-Nachdenken über diese Episode mehrfach mich erinnert gefühlt an diese Geschichte von dem Kevlin Henni mit dem Architekturtheater.

Ich weiß nicht, ob du das kennst, wo ihn jemand gefragt hat, kann man eigentlich zu viel Architektur machen und wo Kevlin gesagt hat, also die Frage sozusagen nicht verstanden hat und dann irgendwie rauskam, dass die Person einen sehr komplizierten, bürokratischen, krassen Prozess im Auge hatte oder halt erleidet.

Und wo Kevlin hat gesagt, naja, das ist ein Architekturtheater.

Also man tut so, als würde man Architektur machen, aber in Wirklichkeit ist es halt kontraproduktiv.

Und also nicht, weil ich halt, ich habe immer das Gefühl, das kennen wir eigentlich alle aus irgendwelchen Projekten, wo halt irgendwie nicht ganz viel Papier produziert wird und ganz viele Themen.

Und wenn man sich mal irgendwie hinsetzt und sagt, was sind denn jetzt eure wirklichen Schwierigkeiten, dann stellt man halt fest, die sind nicht aufgeschrieben.

Und eine Lösung für diese Schwierigkeiten ist halt auch nicht aufgeschrieben.

Und es gibt irgendwie keine Richtung, in die das halt irgendwie gehen soll.

Und das erinnert mich halt daran, nicht irgendwie so ein A42-Template auszufüllen.

Das ist halt ein Beispiel für Architekturtheater.

Dann habe ich zwar ein A42-Template, kann einen Haken hinterher machen, aber es bringt mir halt eigentlich nichts.

Eigentlich ist der Prozess, dass ich da hinkomme, die Fragen stelle und da halt irgendwie der Punkt.

Wenn wir über Softwareentwicklung mit AI-System reden, muss ich ja erst mal gestehen, dass ich mir sehr sicher bin, dass ich mit dem Ansatz, den du gerade für Architektur diskutiert hast, deutlich produktiver Software entwickeln kann als ohne.

Insbesondere deswegen, weil ich eigentlich nicht, ich sage manchmal, ich bin irgendwie PowerPoint-Architekt, ich mache nicht einen Code für Geld.

Ich rede halt darüber, ich gebe irgendwie Hinweise zur Architektur.

Entwicklung selber ist nicht zu meinem Kern.

Und da halt ein System zu haben, dem man sagt, ich generiere mal dieses oder jenes oder bastel das mal, ist irgendwie hilfreich.

Ich hinterfrage es dann, ich gucke es mir an und ich verstehe es halt und versuche dann damit zu arbeiten.

Und das ist, glaube ich, tatsächlich konstruktiv.

## LLMs in der Softwareentwicklung

Was wir relativ schlicht konstatieren müssen ist, meine Meinung, dass aus irgendwelchen Gründen wertneutral dieser durchschlagende Erfolg, den halt AI möglicherweise bei der direkten Produktivität von Code produzieren könnte, sich nicht einstellt.

Und das mache ich halt einmal daran fest, dass, also ich habe drei Beispiele jetzt irgendwie in den letzten, weiß ich nicht, 14 Tagen oder so, wo wir über diese Episode ein bisschen geredet haben, gesehen, die ja sozusagen öffentlich sind.

Das eine ist halt das Servo.

Das ist so ein Webbrowser-Rendering-Engine, in Rust geschrieben.

Servo hat einfach AI-Contributions komplett verboten.

Der Curl-Maintainer hat, da gibt es einen Artikel, der hat irgendwie den schönen Titel, Curl-Maintainer habe die Nase voll wegen KI-Bug-Reports.

Also der ist halt auch inzwischen mittlerweile irgendwie sehr genervt.

Und es gibt noch dieses sehr schöne auf GitHub, also ein Microsoft-Produkt in der .NET-Runtime, ein Microsoft-Produkt, ein Pull-Request, den Copilot, ein Microsoft-Produkt gemacht hat.

Und ich glaube, euch einen dem mal zu lesen.

Ich verlinke dem, wie gesagt, gerne, weil der einfach Unterhaltungswert hat.

Also nicht im Sinne von, du hast die Tests nicht durchlaufen lassen.

Die Tests sind übrigens rot.

Also das sind so die Ebenen, auf denen das halt irgendwie schief geht. dass es tatsächlich seinen Höhepunkt überschritten hat.

Also ich glaube, die Anzahl der beantworteten Stack-Overflow-Fragen ist sogar rückläufig.

Und das bedeutet, das ist ein neues Werkzeug, was in diese Kerbel reingeht.

Aber es wirkt überhaupt nicht so, als gäbe es da jetzt einen Produktivitätssprung.

Insbesondere ist es eben so, dass einige Projekte sagen, bleibt mir bloß weg mit dem Zeug.

Und das sind die Projekte, die wir öffentlich haben, die immer Open Source sind.

Wäre es tatsächlich so, dass das halt etwas ist, was halt massiv Vorteile bringt, müssten wir halt irgendwie jede Menge Contributions sehen.

Wir sehen aber das Gegenteil, also dass eben Projekte da Abstand vonnehmen.

Und vielleicht eine Sache noch, weil ich das irgendwie auch lustig fand.

Wir hatten ja den Stream mit dem Simon Wortley von der Arma.

Und da hat er erzählt von seinen Ausflügen in VibeCoding, wo er ein System gebaut hat und dann mit der AI gesagt hat, mach mal irgendwie mehr Tests.

Und dann hat die AI irgendwie mehr Tests gemacht.

Und dann hat er irgendwann das Durchbruch mit dem VibeCoding, also hat tatsächlich in den Code reingeguckt und hat festgestellt, das System hat Code geschrieben, der Testausgang produziert, aber keine Tests, nichts, was den Code tatsächlich ausführt.

Und da ist wieder so eine Geschichte, wo ich halt sagen würde, ein Mensch, der nicht weiß, wie man Tests schreibt, dem helfe ich dabei.

Ein Mensch, der kommt und sagt, ich weiß nicht, wie man Tests schreibt, dem helfe ich auch dabei.

Ein Mensch, der Code schreibt, der so tut, als seien ja Tests und keine Tests sind, dem schreibe ich eine Abmahnung.

Und zwar sofort, weil das ist ein Täuschungsversuch und das ist halt unakzeptabel, geht halt nicht.

Und diese Abmahnung habe ich ChatGPT geschrieben und benutze jetzt Claude so nett.

Ja, ich bin mir gar nicht sicher, welches Werkzeug er hat genutzt, also kann ich tatsächlich nicht sagen.

Es ist tatsächlich so, dass man von den Modellen viel verlangt, viel erwartet, aber sie doch sehr unterschiedlich sind in der Leistung.

Und das, was du erzählt hast, dass jetzt hier Open-Source-Projekte sagen, sie wollen nichts mehr von der KI haben, keine Pull-Requests und nichts.

Da muss ich mich ein bisschen schuldig erkennen.

Ich habe mein alter Ego aufgebaut bei GitHub.

Es gibt jetzt einen weiteren Account, dem ich mit Claude Anweisungen geben kann, wo ich sagen kann, du guck dir mal das Issue an und kommentier das mal.

Und ich hatte damit auch schon ganz gute Erfolge, dass Claude es richtig analysiert hat, gesagt hat, da liegt der Fehler.

Nochmal gefragt, soll ich ein Pull-Request stellen?

Und irgendwie hat es gepasst.

Ist natürlich noch besser, wenn der Pull-Request auch tatsächlich schon verifiziert wäre, dass eben ein Test geschrieben wäre und man die Tests ausgeführt hätte.

Soweit ist die KI in dem Fall noch nicht.

Aber die Ergebnisse sind so gut.

Ich habe Cloud Desktop kann erst mal nicht auf mein File System zugreifen, kann nicht die Bash benutzen und kann aber programmieren.

Und ich habe es ausprobiert.

Ich habe Cloud Desktop gebeten, MCP zu schreiben, um aufs File System zuzugreifen.

Hat Claude gemacht.

Danach habe ich Cloud gestartet, habe den MCP gestartet und er konnte aufs File System drauf zugreifen.

Das nächste MCP, was er mir geschrieben hat, dass er die Bash nutzen kann, in einem Docker Container, konnte er schon selbst ins File System reinschreiben.

Ich habe Cloud gestartet und danach hatte Cloud weitere Fähigkeiten, dass es eben die Bash und somit Tests ausführen konnte.

Und das, finde ich, sind beeindruckende Schritte nach vorne, die eben über den einfachen Chat hinausgehen, wo die KI eben noch nicht überprüfen kann.

Ist das, was sie gemacht hat, irgendwie sinnvoll?

Funktioniert es?

Aber mit den richtigen Tools kann sie das.

Und diese Schritte, dass sie tatsächlich sich eigentlich fast selbst erweitert, das ist momentan krass.

Und weil du jetzt von negativen Beispielen gesprochen hast.

### Positive Beispiele

Es gibt auch viele positive Beispiele, wo Leute echt sagen Es funktioniert einfach.

Meine kleinen Tools, die ich so im Alltag brauche.

Ja, die die lasse ich mir generieren.

Wir haben die Transcription von diesen Folgen hier.

Ich weiß, es ist jetzt ein bisschen eingeschlafen.

Die letzten Folgen hatten keine Transcription mehr, weil ich die Automatisierung noch nicht drin habe.

Aber die eigentliche Transcription hat Cloud selbstständig erstellt mit Tests, mit eben dieser Ausführbarkeit und hat eben sehr, sehr viele Hürden bei der Entwicklung festgestellt.

Das festgestellt hat Okay, ich kann jetzt nicht einfach das komplette Audio File in die API reinschmeißen.

Ich muss es irgendwie klein bringen.

Wie bringe ich es klein, indem ich erstmal eine Spur entferne?

Dann ist es nur noch Mono.

Dann ist es immer noch zu groß.

Dann muss ich es cutten.

Ich suche jetzt Pausen und suche die so, dass ich es in drei Stücke ungefähr gleich große Stücke hacke.

Das ist jetzt natürlich ohne Architektur entwickelt worden, so wie ich es beschreibe.

Aber das könnte natürlich auch eine Vorab-Architektur gewesen sein, dass er sich überlegt, welche Technologien brauche ich, wie zum Beispiel FFmpeg, was er dann eben ad hoc entschieden hat, um das File kleiner zu schneiden.

Und das ist beeindruckend.

Was dann bedeutet, dass deine Ergebnisse differieren von dem, was andere da haben, was freien ist?

Wir haben dann letztendlich zwei unterschiedliche Wahrnehmungen oder Ausschnitte von dem, was daraus läuft.

Ich habe eigentlich alle wesentlichen Themen diskutiert, die mir so eingefallen sind.

Das ist vielleicht eine interessante Sache, die im Chat gerade hochgekommen ist.

Martin Axiomeyer hat geschrieben, wahrscheinlich könnte man diese Folge in zwölf bis zwölf Monaten wiederholen und dann sehen die Antworten vielleicht anders aus.

Ich behaupte mal, dass das für das Architektur-Thema nicht gelten wird.

Und wir sind mittlerweile ja tatsächlich, glaube ich, sogar schon länger an dem Thema dran.

Ich glaube, wir haben da ganz gute Fortschritte gemacht.

Wir haben am Anfang festgestellt, es kann Architekturaufgaben nicht lösen, sondern Lösungen erzeugen, wo man nochmal drüber gucken muss.

Das war das erste Experiment, dann später das Experiment mit dem Afgiedock-Linter, wo er nicht nur eine Architektur erzeugt hat, sondern eben im nachfolgenden Schritt umgesetzt hat.

Auch das hat irgendwo funktioniert und wir nähern uns dem Ganzen an.

Es sieht immer so aus, als wäre man echt nah dran, aber wir brauchen noch eine Weile, um es wirklich stabil zu machen.

Das ist meine Meinung.

Ich kann es aber auch verstehen, wenn man sagt, da fehlt das Menschliche.

Jetzt bist du bei mir gerade weg.

Chain-of-Sort-Prozesse macht ein LLM doch nun auch selbst und besser.

Chain-of-Sort ist dieses, dass ich dem Modell nicht nur einen Schuss gebe und dann muss das sitzen, sondern dass es eben auch ein bisschen iteriert und seinen Kontext nutzt.

Noch besser ist, wenn ich wirklich in die Iterationen reinkomme und über die Iterationen sich das Modell selbst die Lösungen angucken kann und verifizieren kann.

Und dann bin ich eben ganz weit vorne.

Und gerade in der Softwareentwicklung, was wir ja mit der Architektur bewirken wollen, das ist ja der Anfang der Softwareentwicklung, dann haben wir den Vorteil, dass wir das wirklich verifizieren können.

In anderen Disziplinen haben wir eben das nicht.

Wenn ich zum Beispiel eine Geschichte schreibe, dann kann ich nicht so einfach verifizieren, ob die beim Leser ankommt.

Und bei der Softwareentwicklung haben wir das.

Jetzt ist Eberhard Wolf ganz weg.

Ich gucke jetzt nochmal hier in die Kommentare rein.

Reasoning kumuliert massiv Fehler.

Ja, die Modelle schaffen es sich in Paint in a Corner, heißt es glaube ich im Englischen, dieses sich in eine Ecke verrennen, dass man nicht weiterkommt.

Und ich sage immer, ich versuche immer das Ganze mit, auch wenn es eine Maschine ist, mit dem menschlichen Verhalten zu vergleichen.

Und auch da verrennen wir uns teilweise in Lösungen.

Und das ist so diese Sache, wo ich eben versuche oder wo ich mir überlege, wie kommen wir daraus?

Wie können wir das, die Probleme, die wir sehen, vermeiden?

Hallo Eberhard, da bist du wieder.

Ja, sorry, Problem auf meiner Seite.

Ich wollte das nochmal aufgreifen mit diesem in sechs bis zwölf Monaten noch drauf gucken.

Und ich habe gerade nachgeguckt, also unsere Episode, die wir damals gemacht haben, ist datiert vom 15.12.2023, die ist also anderthalb Jahre alt.

Und ich würde behaupten, aber da würde mich deine Ansicht interessieren, ich würde so eine Episode nicht nochmal machen mit dieser Fragestellung, weil mir relativ klar ist, dass das Ergebnis, was dabei rauskommt, ein Text ist, der halt scheinbar diese Fragen beantwortet, aber der mir eigentlich nicht hilft.

Also vielleicht als Unterstützung.

Und das ist ja eigentlich das, was du auch sagst.

Also das ist das, was ich ausgelesen habe, aber vielleicht täusche ich mich da auch.

Du hast halt gesagt, ich habe sozusagen ein Ding, mit dem ich halt nochmal Ideen ventilieren kann, wo ich ein Feedback bekommen kann und so weiter und so weiter.

Das heißt also, das, was wir da gemacht haben, oder was du da ja im Wesentlichen gemacht hast, nämlich dem System einfach die Frage vorwerfen, ich weiß nicht, ob ich das nochmal machen würde.

Ich weiß nicht, wie du es siehst.

Also deswegen würde mich das genau mal interessieren.

Das ist ja vielleicht irgendwie genau die Antwort auf diese Frage, wie sieht es denn irgendwie in zwölf Monaten aus?

Weil da können wir jetzt sagen, wie sah es vor 18 Monaten aus?

Du hast gerade das Ergebnis, was du erwartest, schon bewertet, dass du gesagt hast, dass es scheinbar ein richtiges Ergebnis ist.

Eigentlich müsste man neutraler rangehen.

## Entwicklung der LLM-Technologie

Und die LLMs haben sich extrem weiterentwickelt.

Und gerade von der Claude-Modellfamilie bin ich sehr beeindruckt, wie sie arbeiten können.

Und damals hatten wir noch Probleme, dass ChatGPT so Sachen hatte, dass ich habe mir halt einen Kaffee geholt, ich habe eine Pause gemacht und habe nicht gemerkt, dass die Dokumente für das System verschwunden waren, weil nach einer halben Stunde Session-Timeout sagt das System mir nichts, aber löscht einfach die Dokumente oder Zwischenergebnisse.

Mittlerweile können zum Beispiel auch die LLMs, wenn sie ein PDF analysieren, die Diagramme lesen und ich brauche sie da nicht mehr zu unterstützen.

Das heißt, wir sind jetzt an einem Punkt, wo man vielleicht sogar dieses Experiment viel einfacher machen kann, weil wir einfach die Beispielaufgabe hochladen und einem agentischen System sagen, du arbeite mal damit, ich gehe jetzt einen Kaffee trinken und in einer halben Stunde komme ich wieder und habe ein Ergebnis, ohne dass ich es unterstützen musste.

Und wie gut das Ergebnis ist, das würde ich jetzt noch nicht bewerten wollen, sondern offen lassen.

Ich befürchte, wenn das so ist, dann wäre für mich die Konsequenz, die so ein bisschen auf der Hand liegt, dass du einem LLM aus irgendwelchen Gründen die gesamte Verantwortung für seine Aufgabe ergeben würdest.

Da sind ja solche Sachen wie, was sind diese Aufgaben, finde Qualitätsszenarien oder sowas.

Das ist zum Beispiel etwas, was da drin steht.

Du würdest jetzt also diesem System sagen, schreib mal die Qualitätsszenarien.

Das ist ja ein artifizielles Beispiel, aber wäre das jetzt etwas, was du tatsächlich in einem echten Projekt machen würdest?

Unterstützend auf jeden Fall.

Allerdings war bei der Prüfung ein Interview, aus dem man die Qualitätskriterien herausgelesen hat.

Und das ist dann wieder die sprachliche Fähigkeit des Modells, das transformieren kann.

Von einer Beschreibung aus einem Interview rüber in die Qualitätskriterien.

Dass es sich da noch ein paar mehr ausdenkt, wo es sagt, das gehört dazu.

Okay, müssen wir gucken.

Gerade die neuen Modelle sind da leider sehr weit vorne, dass die sich sonst wie viel ausdenken.

Aber da fehlt mir eigentlich beim echten Projekt die Möglichkeit, dieses Interview direkt aufzunehmen, zu transkribieren und in die Maschine zu geben.

## Qualitätsszenarien und Architektur

Interessant, weil ich würde jetzt erstmal behaupten, das Erstellen der Architektur insgesamt ist ein Lernprozess.

Das Artefakt ist vielleicht gar nicht so relevant, sondern dass ich dazu komme, mir die Fragen zu stellen und mir zu überlegen, was die Antworten auf diese Fragen sind.

Das andere ist, für den SG-Doc Linter gibt es ja Qualitätsszenarien.

Wir laufen ein bisschen aus der Zeit.

Die sind nach meinem Empfinden tatsächlich dramatisch daneben.

Da muss eine bestimmte Testabdeckung sein.

Das ist kein Qualitätsszenario.

### Kritische Betrachtung

Ein Qualitätsszenario sagt, das System soll eine bestimmte qualitative Eigenschaft haben.

Zum Beispiel soll es wartbar sein.

Darüber muss ich etwas sagen.

Eine Testabdeckung ist der Versuch, Wartbarkeit hinzubekommen und noch nicht mal ein besonders guter, weil ich eine hohe Testabdeckung bekommen kann, ohne dass ich dabei tatsächlich ein wartbares System baue.

Da bin ich der Meinung, dass ein Textgenerator tatsächlich schwierig ist.

Was ich mir eigentlich wünschen würde, wäre ein Nicht-Textgenerator.

Also ein Ding, das sagt, die Qualitätsszenarien müsstest du dir schon selber überlegen müssen.

Das sind Anforderungen.

Wieso fragst du mich das?

Ich kann dir sagen, wie ich dadurch in den Prozess komme.

Eine Guidance wäre gut, aber das ist eben nicht das, was eine LLM will oder tut.

Eine LLM kriegt einen Text.

Und dann laufe ich zu einem Architekturtheater.

Dann habe ich Qualitätsszenarien, die nützen nichts und dann habe ich ein Problem.

Ich muss zugeben, bei dem ASCII-Doc Linter, aufgrund der Zeit hatte ich dem System einfach gesagt, überleg dir was, überleg dir was, was passt.

Und das ist Textgenerator.

Aber normalerweise drehe ich die Rollen um und sage dem Modell, stelle mir Fragen, bis du eben alles weißt, um dann weitergehen zu können.

Wenn ich jetzt so überlege, was ich an Architekturen oftmals in real life gesehen habe, dann neige ich dazu zu sagen, dass das, was ich aus dem LLM rausbekomme, von, ich würde mal sagen, überdurchschnittlich ist.

Und dein Anspruch ist ganz weit vorne.

Aber deswegen geht das bei dir, würde ich jetzt behaupten, nicht so einfach durch.

Aber was mich zum Beispiel erfreut ist, wenn ich mit Claude spreche und ich habe Claude die verschiedenen Kapitel von ARC42 bewerten lassen.

Und da kam raus, dass die höchste Bewertung kriegen die Qualitätskriterien, weil Claude sagt, wir wollen qualitätsgetriebene Architektur machen.

Und Claude weiß, dass es die Qualitätskriterien braucht, um dann Architekturentscheidungen zu treffen.

Und das ist diametral zu vielen Architekturen, die aufgrund von Konferenzen, Konferenzbeiträgen entstehen.

Was ist momentan aktuell?

Was sieht nach einem modernen Stil aus und nicht was passt zu den Qualitätskriterien?

Und da bin ich gespannt, wie sich das so entwickelt.

Wir laufen so ein bisschen über die Zeit raus, befürchte ich.

Ja.

Und ich muss mich entschuldigen, oder wir müssen uns entschuldigen, nein, ich muss mich entschuldigen dafür, dass wir nicht so wahnsinnig viel auf die Chatbeiträge eingegangen sind.

Gibt es noch irgendwas, was du loswerden willst?

Ich bin sehr froh, die Diskussion ist gut gelaufen.

Ich denke, wir haben hier zwei valide Standpunkte und ich bin gespannt, wie sich das entwickelt.

Und ich bin gespannt, was gleich in dem Chat drin steht, weil ich auch nicht nachgekommen bin, den zu lesen.

Vielen Dank für die Beiträge im Chat.

Sonst hätte ich dem nichts hinzuzufügen.

Dann würde ich sagen, vielen Dank an dich, Ralf, vielen Dank an die vielen ZuschauerInnen.

Nächste Woche ist das Thema noch offen.

Geht gerne auf die Webseite www.nichtsoftware-architektur.tv, führt dort den entsprechenden Fragebogen aus zur Nutzung der Webseite.

Das hilft uns, die halt irgendwie noch weiterzuentwickeln.

Und dann wünsche ich ein schönes Wochenende, würde ich sagen.

Und bis dahin.

Gleichfalls.

Bis dahin.

Ciao.