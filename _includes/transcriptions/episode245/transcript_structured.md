# Folge 245 - KI in der Software-Entwicklung - Über- oder unterhypt?

## Einführung in KI in der Software-Entwicklung

Hallo und herzlich willkommen zu einer neuen Episode von Software-Architektur im Stream.
Heute seht ihr schon, dass eine ganze Bande an Leuten hier und wir besprechen das Thema KI in der Softwareentwicklung über oder unter Hyped.
Ich sage schon mal Hallo André, Hallo Stefan, Hallo Ralf und Hallo Eberhard.
Ihr fragt euch vielleicht, wie es überhaupt zu dieser Zusammenstellung kommt und zu dieser Episode.
Eberhard hatte einen Post bei Heise veröffentlicht.
Ich hoffe, ich erzähle es jetzt auch richtig rum.
Diesen Post hat er irgendwann ins Englische übersetzt.
Dann gab es dazu einen LinkedIn-Post und dieser LinkedIn-Post ist mit ganz vielen Kommentaren überhäuft worden.
Und Eberhard hat dann beschlossen, dass es hier diese Folge geben soll mit eben André, Stefan und Ralf.
Genau.
## Vorstellung der Gäste

Bevor wir so richtig ins Thema anfangen, würde ich sagen, dass ihr beiden André und Stefan euch einmal kurz vorstellt, wer ihr seid, was ihr so macht.
Stefan, leg doch mal los.
### Stefan's Einführung

Ja, Stefan.
Coder by heart, sage ich immer.
Ich habe vor 40 Jahren mir Programmieren beigebracht, weil ich Videospiele programmieren wollte.
Hab dann Videospiele programmiert.
Programmier seitdem.
Manchmal hauptberuflich, manchmal nebenberuflich.
War lange Jahre Engineering Manager, war CTO und bin seit ein paar Jahren CTO-Coach, hauptberuflich.
Sehr gut.
André, machst du weiter?
### André's Einführung

Na klar, gerne.
Erstmal danke für die Einladung.
Ich war auch schon mal hier.
Das ist schon ein paar Tage her, aber ich mache es noch mal kurz.
Also André macht das so ungefähr jetzt gute 20 Jahre.
Ich würde sagen, nicht Coder by heart, aber Techie by heart.
Mich interessieren vor allem disruptive Technologien und wie man das auch in die Organisation bringt.
Ich war viele Jahre lang quasi so Individual Contributor, also Software-Ingenieur und habe mich dann irgendwann für die Management-Seite entschieden.
Und mache das jetzt so die letzten 10, 15 Jahre für verschiedene Unternehmen, verschiedenen Rollen.
Und versuche dann halt eben die Technologien halt auch ins Operative zu kriegen.
Sehr gut.
Genau.
## Thema der Episode

Wir haben schon gesagt, KI in der Softwareentwicklung über- oder unterhyped ist quasi das Grundthema.
Und ihr alle vier hattet dazu eine These.
Und um es halbwegs fair zu machen, würde ich einfach mal alphabetisch nach Vornamen vorgehen und euch bitten zu sagen, was eure Grundthese zu diesem Statement über- oder unterhyped von KI ist.
André, fang doch gerne noch mal an.
### Andrés These: Underhyped

Ja, also meine These ist quasi underhyped.
Also wir haben noch nicht verstanden, was damit möglich ist.
Ich glaube, wir befinden uns mit einer wahnsinnigen Geschwindigkeit in der Entwicklung, wo das Ende einfach noch nicht abzusehen ist.
Und deswegen einfach zu sagen, es ist underhyped, glaube ich, ist quasi für den Moment, max. situativ betrachtet, richtig sein.
Ist, glaube ich, aber für das, was da kommen mag, glaube ich, falsch.
Oder zumindestens kann man das in Frage stellen.
### Herausforderungen der Implementierung

Ich würde eine Sache hinzufügen, es ist underhyped.
Aus meiner Sicht ist es aber auch kompliziert, es einzuführen.
Wenn ich ein bisschen aus meiner täglichen Arbeit berichte, dann ist es, wie sagt man so schön, Change ist toll, solange es nicht selbst einen betrifft.
Und dieser Change, den wir hier vor uns haben, der ist allumfassend.
## Zusammenarbeit zwischen Mensch und Maschine

Wir reden nicht davon, dass wir jetzt jeden Tag deployen wollen.
Wir reden nicht von automatisierten Tests, sondern wir reden davon, dass grundlegend die Art und Weise, wie wir Software entwickeln, sich verändert.
Und das sägt im Zweifelsfall auch an dem eigenen Stuhl.
Und sich da dann quasi damit auseinanderzusetzen, glaube ich, ist verdammt, verdammt schwer.
Das wäre so eine These, also quasi warum es schwer ist, das in Unternehmen zu etablieren, obwohl es eigentlich sehr powerful ist.
Lass mich da auch nochmal vielleicht auf die Mächtigkeit eingehen, weil das, was wir sehen, ist eine rasende Geschwindigkeit.
Also getrieben meiner Meinung nach im Endeffekt aus drei Dimensionen.
Das ist einmal die Hardware, die immer effizienter wird und auch von oben nach unten durchläuft.
Also das, was quasi zuletzt bloß irgendwo im Rechenzentrum möglich ist, ist dann demnächst irgendwo eine Edge möglich.
Also auf meinem Laptop.
Also ich kann ohne Probleme ein LLM auf meinem Laptop laufen lassen.
Das Zweite ist halt LLMs, die Größe und die Fähigkeiten, die diese LLMs haben.
Also angefangen Parameter auf der einen Seite, aber auch Kontext Windows.
Am Anfang konnte man halt irgendwie eine Klasse da reinladen und sagen oder ein File ergänzt das mal.
Jetzt kann ich mittlerweile eine ganze Source-Code-Basis da reinpumpen.
Also Global Gemini 1.5 Pro sind quasi 300.000 Token.
Können wir gleich nochmal nachgucken.
Kann ich gleich nochmal nachliefern.
Aber die Kontext-Windows sind mittlerweile so groß, dass halt einfach große Code-Basen da reinpassen.
Und das verändert halt einfach alles.
Also deswegen kann man halt quasi Stand heute sagen.
Heute ist es vielleicht noch nicht da, wo es halt ist.
Aber die Wahrscheinlichkeit, dass es sich rasend schnell entwickelt, ist halt einfach gegeben.
Und das sieht man unter anderem auch bei den ganzen Benchmarks.
Quasi gibt es immer wieder neue Benchmarks, weil die alten Benchmarks dann quasi gelöst wurden.
Und das kann man auch relativ leicht nachvollziehen, wenn man sich mal einfach so den, den ich ganz gern verfolge.
So SWE Bench.
Da gibt es so ein Leaderboard.
Und da sieht man auch, mit welcher Geschwindigkeit, also im Monatstakt quasi da immer ein neues Set an LLM und Tools quasi da in den ersten Platz belegt.
Genau.
Und das bringt mich letztendlich zur letzten These.
Ich glaube, wir haben noch nicht verstanden, wie man das bestmöglich nutzt.
Am Anfang gab es so ein bisschen die Idee davon, wir müssen jetzt alle Prompt-Engineer werden.
Ich glaube, da ist auch was dran.
Also quasi Shit in, Shit aus.
Wenn der Prompt nicht gut ist, dann kann das Ergebnis nicht gut sein oder es beeinflusst zumindest das Ergebnis.
Jetzt wird die Idee von Agents gerade durch die Welt getragen.
Und die einfache Frage ist, was ist das Nächste?
Was ist das Nächste, was quasi uns in der Softwareentwicklung vielleicht einfach alles verändert?
Gewisse Teile werden bleiben.
Da glaube ich wahrscheinlich auch eine andere These als das, was vielleicht Stefan Eberhard gleich sagen.
Aber ich glaube, wir haben noch nicht verstanden, wozu LLMs oder quasi Generated AI, weil da zählen ja nicht nur LLMs rein, quasi in der Lage sind.
Sehr gut.
Ich habe noch eine kurze Nachfrage, weil ich glaube, das ist auch noch ganz interessant.
Nutzt du schon KI in deiner täglichen Arbeit?
Ja.
Das ist, würde ich auch sagen, für mich gar nicht mehr wegzudenken.
Ist für mich tatsächlich ein Sparrings-Partner, viele Sachen einfach auch schnell zu erledigen.
Also im Sinne von auch so Boring-Arbeit halt einfach zu erledigen.
Und ich nutze auch verschiedene Sachen.
Das habe ich für mich mittlerweile gelernt.
Da gibt es nicht dieses One-Tool-to-rule-them-all, sondern kontextbezogen braucht man das eine und mal das andere.
Sehr cool.
Genau.
Ich wünsche mir gleich von euch allen das auch nochmal, wenn ihr die These gesagt habt, sagt gerne auch nochmal dabei, ob ihr schon KI in eurer täglichen Arbeit nutzt.
Ich glaube, das ist auch nochmal spannend für die Einschätzung eurer Thesen.
Eberhard ist der Nächste im Alphabet.
## Eberhards Sichtweise: Overhyped

Ja, genau.
Vielen Dank.
Eigentlich müsste ich ja jetzt sagen, dass es overhyped ist.
Ich habe gestern das nochmal korrigiert.
Ich glaube, es ist ein bisschen overhyped bei Investoren und bei Management, die jetzt anfangen und sagen, das wird uns grundsätzlich zu ganz neuen Dingen führen und Sachen fundamental ändern.
Gleichzeitig ist es so, dass ich das Gefühl habe, dass Entwickler so ein bisschen müde geworden sind und jetzt eher sagen, naja, das ist keine besonders spannende Entwicklung.
Ich glaube, da spielt auch die Enttäuschung von Blockchain eine Rolle und die Probleme, die da existieren.
Blockchain ist am Ende eine Technologie, die für eine extreme Nische ermöglicht, im Wesentlichen Spekulationen und das Bezahlen von Menschen, die in kriminellen Aktivitäten verwickelt sind.
Das ist mit KI ein ganz anderes Ding.
Also wenn man Chatshipping ausprobiert hat und die anderen KI-Tools, wird man feststellen, dass die eben deutlich mehr können und viel helfen.
Also wie André gerade eben sagte, das ist auch bei mir etwas, was in der täglichen Arbeit eine Rolle spielt.
Ich arbeite viel mit Texten, dafür ist es super.
Da stelle ich mir der Schrecken fest, dass es Menschen gibt, gerade Techniker, die es noch nicht mal ernsthaft ausprobiert haben und das ist schwierig.
Jetzt ist die Frage, warum glaube ich, dass es Overhyped ist.
Ich habe diesen Heiser-Artikel geschrieben, der im Wesentlichen die These aufstellt, eigentlich bedeutet Softwareentwicklung, dass wir viele Menschen koordinieren, um gemeinsam an einem Projekt zu arbeiten.
Dazu gehören nicht nur Techniker, sondern wir Entwickler und Architekten, sondern vor allem auch Stakeholder, Benutzer und wer auch immer dazugehört.
Das bedeutet, dass das Hauptproblem von Softwareentwicklung ist, Menschen zu koordinieren und sie gemeinsam an einem Projekt arbeiten zu lassen.
Das ist das, was ich seit sehr langer Zeit auch tatsächlich so erlebe.
Das heißt, ich sitze da und rede mit irgendwelchen Leuten, so wie jetzt, über irgendwelche Ideen, irgendwelche Themen, irgendwelche Sachen, die wir bauen wollen und das ist mein wesentlicher Lebensinhalt.
André hatte schon einen ganz guten Punkt gemacht.
Man muss ein bisschen aufpassen, weil es gibt eine gewisse Versuchung zu sagen, mich tangiert das nicht, ich bin sicher.
Ich weiß noch nicht, ob ich da ein Opfer bin, aber ich würde behaupten, diese Tätigkeit, die ich dort betreibe und so, wie ich Softwareentwicklung erlebe und so, wie ich auch die Hauptprobleme erlebe, die ist ein Thema, was KI für mich nicht offensichtlich erschlägt.
Ich glaube sofort, dass KI-Tools die Produktivität von Entwicklern und Technikern verbessern, also eben das Produzieren von Code.
Wir hatten ja vor 14 Tagen die Episode mit Ralf gemacht, wo er darüber berichtet hat, wie ChatGPT für ihn im Prinzip ein Feature implementiert hat.
Das bedeutet, die Entwicklung von Code wird sicher viel einfacher, viel schneller funktionieren.
Das sind aber Dinge, die gar nicht so einmalig sind.
Wir haben eine Tradition davon, Produktivität zu verbessern durch bestimmte technische Maßnahmen.
Hochsprachen haben wir deswegen implementiert.
Wir haben angefangen, Betriebssysteme zu implementieren.
Wir haben angefangen, Datenbanken zu implementieren.
Wir haben Mitarbeiter, die Cloud, wo halt Komponentenbibliotheken sind, die ich einfach benutzen kann.
Ich kann eben Machine Learning-Modelle aus der Cloud benutzen.
Ich kann auch irgendwelche anderen Dinge, halbfertige Dinge aus der Cloud benutzen als Komponenten.
Das sind alles Dinge, die dafür sorgen, dass sich die Produktivität von Entwicklern erheblich verbessert.
Es gibt diese traditionelle Meinung von Fred Brooks, der gesagt hat, nicht eine einzige Maßnahme wird die Produktivität in der Softwareentwicklung um eine Größenordnung verbessern, also um einen Faktor von 10.
Das belegt er nicht richtig.
Das ist eher eine Vermutung.
Jetzt ist die Frage, ob KI daran kratzt.
Aber selbst wenn, und das ist der letzte Blogartikel, den ich geschrieben habe, ist die Frage, was passiert denn dann?
Meine These wäre, wir werden mehr Software in noch mehr Bereichen sehen.
Dinge, die wir heute mit Software ledigen, haben wir früher ohne gemacht.
Mittlerweile haben wir alle diese lustigen Telefone.
Ich habe hier eine Uhr, die hat auch Software.
Das sind Dinge, die wir früher nicht gemacht haben.
Das ist dieser Rebound-Effekt.
Weil etwas effizienter wird, weil wir es einfacher hinbekommen, bedeutet das nicht, dass weniger davon passiert, sondern im Gegenteil, möglicherweise sogar mehr.
Wir haben effizientere Autos.
Ergebnis, es wird mehr Benzin verbraucht, weil mehr Leute Auto fahren und mehr Strecken fahren.
Das ist vielleicht bei Softwareentwicklung ähnlich.
Wir sind hier in der schwierigen Situation, dass wir versuchen, die Zukunft vorherzusagen.
Das heißt, ich kann jetzt irgendwelche Dinge behaupten.
Und ich würde behaupten, wir werden vielleicht eher einen Rebound-Effekt sehen.
Und wir werden die Hauptprobleme nicht lösen.
Kommunikation, Stakeholder.
Unser Hauptproblem ist zu sagen, was genau soll implementiert werden.
Unser Problem ist nicht in erster Linie den Code zu produzieren.
Und ich glaube, davon können wir alle ein Lied singen, die wir täglich im Meeting sitzen und genau versuchen, das herauszufinden.
Nutzt du in deiner täglichen Arbeit KI?
Ja, und insbesondere für Arbeiten mit Texten.
Also Abstracts zusammenbasteln, Zusammenfassungen bauen, solche Geschichten.
Und das funktioniert hervorragend.
Und als ich vor zwei Jahren das erste Mal JGPT genutzt habe, hätte ich vorher gesagt, sowas geht gar nicht.
Und von daher nicht.
Also dass es eine Revolution ist und eine Disruption.
Das ist, glaube ich, unzweifelhaft so.
Danke, Eberhard.
Dann Alphabet.
Ralf, glaube ich, PQRS.
Genau.
## Ralphs Perspektive: Grenzenlosigkeit von KI

Also wenn ich bei der Technologie irgendwie schon Grenzen sehen würde, dann würde ich sagen Overhyped.
Aber mein Standpunkt ist Underhyped, weil ich sehe halt momentan keine Grenzen.
Ich versuche, die Grenzen zu finden, und ich finde sie nicht.
Es ist auf jeden Fall klar, dass GenAI, die Art und Weise, wie wir Software entwickeln, werden fundamental verändert und dass diese Veränderung in vielen Bereichen schnell und zeitnah erfolgen wird.
Momentan sehe ich noch, dass die KI oft falsch, weil punktuell, unterstützend und gegen die Regeln der Softwareentwicklung eingesetzt wird.
Also wenn ich zum Beispiel Code habe und dann meinen Copilot bitte, mir den Test schreiben zu lassen, dann ist es nicht mehr Test-Driven Development, sondern Development-Driven Testing.
Und so sehe ich in manchen Bereichen, dass wir über die KI, weil wir sie punktuell einsetzen, Fehler machen.
Aber meine These ist, wenn GenAI richtig eingesetzt wird und wir nicht an irgendwelche Grenzen stoßen, dann wird die GenAI die Softwareentwicklung für uns in Zukunft übernehmen können.
Das heißt, wir fallen da meines Erachtens komplett raus.
Das ist dieses, was Eberhard ja auch schon gesagt hat.
Wir programmieren nicht mehr in Assembler, wir nutzen Hochsprachen.
In Zukunft werden wir aus meiner Sicht natürlich sprachlich unsere Requirements, unsere Anforderungen stellen und dann wird die Maschine das umsetzen.
Das Ganze geht in Richtung Low-Code, No-Code und das führt wahrscheinlich anfangs nur wieder zu weiteren Problemen, weil wenn wir mit diesem Low-Code, No-Code Ansatz an die Softwareentwicklung rangehen, dann werden wir auf komplexere Probleme stoßen, die wir dann mit dem Low-Code Wissen nicht umsetzen können, sondern wo wir dann eben wieder entsprechende Experten brauchen.
Und das heißt, dieses Expertentum wird auch noch länger bestehen bleiben.
Davon werden dann einige extrem profitieren, andere weniger.
### Monokulturen in der Technologie

Was mich noch beschäftigt ist, dass wir weltweit momentan nur ein paar wenige LLMs haben, die dominieren.
Wir haben zwar eine riesige Anzahl an irgendwelchen Sprachmodellen, aber die Dominanten sind sehr wenig.
Und wenn all diese wenigen dominanten LLMs für uns in Zukunft die Entscheidung treffen, welche Technologien wir verwenden, welchen Code-Stil wir verwenden, dann wird es technologisch zu Monokulturen kommen.
Wir haben es jetzt schon, Python ist die Sprache der KI, es wird immer mehr KI eingesetzt.
Deswegen haben wir immer mehr Python-Repositories und die Sprache gewinnt an Popularität.
Und andere fallen dann hinten runter, weil sie eben auch von den Maschinen nicht unterstützt werden.
Und das ist eine sehr interessante Entwicklung.
Es war jetzt auch gerade die Woche eine Entscheidung in einem großen Repository, dass man eine Dokumentation nicht für den Menschen lesbarer gestalten möchte, sondern bei dem Lesbaren für die Maschine bleiben möchte.
Und das wird sehr spannend.
Und dich braucht man gar nicht fragen, du nutzt KI in deiner täglichen Arbeit, oder?
Nein, ich habe die ganze Zeit schon nachgedacht.
Und ja, ich versuche KI zu verwenden, also Gen AI, wo es möglich ist.
Wenn ich aber die Coding-Tools verwende, dann habe ich eher das Gefühl, dass sie mich verwenden.
Sie sagen, bitte den Code jetzt rüber kopieren und jetzt mal die Tests ausführen, ob es noch läuft.
Und davon will ich wieder weg.
Und da bin ich eben mit meinem eigenen System auch entsprechend weg, weil dieses System selbst den Code modifizieren darf und selbst die Tests ausführen darf und deswegen entsprechend in die Iterationen reinkommt.
Und das ist so mein Traum, dass eben die Maschine nebenbei entwickelt.
Manchmal Rückfragen stellt, du soll ich links oder rechts gehen?
Und so soll es in Zukunft sein.
Aus meiner Sicht.
Sehr cool.
Danke, Ralf.
Und dann darfst du noch den grünen Abschluss mit deinen Thesen machen, Stefan.
Ja, immer, immer am Ende wie in der Schule.
## Stefans Beitrag: Generation von Tests

Bei mir ist aber egal, ob man das mit Vor- oder Nachnamen macht.
Okay, meine Thesen.
Also erstens, ich benutze in der täglichen Programmierung Cursor als IDE nach ungefähr 20 Jahren, über 20 Jahren JetBrains Produkten.
Und ich bin ziemlich fasziniert davon, wie Cursor mich unterstützt, bestimmte Sachen zu programmieren.
Das heißt, ich ändere in einer Datei etwas, gehe in eine andere Datei und Cursor macht Vorschläge, was ich hier ändern müsste, damit es zu dem anderen passt.
Also es grenzt bei mir schon ab und an an Magie, wo ich denke, wie kommt man da jetzt drauf?
Aber das hätte ich auch gemacht.
Und die Sachen erscheinen mir auch nicht als trivial.
Also ich bin da fasziniert und ich halte es teilweise für Magie im Sinne von hinreichend komplizierte Technologie, die man nicht versteht, stellt sich magisch dar.
Ich hatte zwei vorige Momente.
Das erste Mal im Moment eben vor 40 Jahren, wo ich zum ersten Mal programmiert habe, was eingetippt habe und da kam am Bildschirm irgendwas Buntes.
Das war auch ein magischer Moment.
Und ein magischer Moment war auch Anfang der 90er, als das Internet kam und ich die ersten IRC Bots programmiert habe, die dann im Chat irgendwelche Sachen gemacht haben und Leute in Amerika darauf geantwortet haben.
### Wichtige Fragen der Entwicklung

Also ich sehe das in ähnlicher Art und Weise.
Mich hat zwischendrin relativ wenig technisch fasziniert.
Mich fasziniert es unglaublich.
Ich glaube aber, dass diese ganze Gen AI für die Softwareentwicklung im Sinne von Code Generierung letztlich nur eine Brückentechnologie ist, die kommt und geht.
Eine Auswirkung dieser Brückentechnologie wird sein, dass die Programmierer den reinen manuellen Anteil, also Codeschreiben immer schneller machen.
Und deswegen glaube ich, diese Zeiten immer kürzer werden und daraus resultiert, dass die Interaktionen mit Leuten mittelfristig vielleicht auch in Richtung Eberhard nochmal zunehmen, weil wenn ich immer schneller fertig bin mit dem, was ich machen soll oder will oder darf oder kann und dann wieder zurückkommen muss, darf, soll, muss, kann, um mit jemandem zu sprechen, dann werden diese Interaktionen erstmal zunehmen.
Also im Prinzip so ein bisschen anders law.
Das hatte ich mal von Andrej vor vielen, vielen Jahren.
Weiterer Punkt ist, ich glaube, wir betrachten die Software zu sehr als als gegeben und vergessen, dass Software ein Werkzeug ist, das Probleme lösen soll.
Also unter dem ganzen Stichwort Jobs to be done ist Software eben ein Ding, was Jobs löst.
Mit Software kann ich bestimmte Jobs lösen, meine Aufgaben lösen.
Aber vielleicht brauche ich eben, wenn AI weiter fortschritt, brauche ich gar keine Software mehr.
Also die Frage ist nicht, löst AI Softwareentwicklung ab, sondern löst AI Software ab im Sinne von Jobs to be done.
Und vielleicht sind wir alle ein bisschen zu sehr drauf verhaftet.
Softwareentwicklung muss bleiben.
Ich würde sagen, was sie schon immer gibt.
Das stimmt bei Softwareentwicklung nicht ganz.
Aber da ein bisschen weiter wegzugehen, halte ich für einen wichtigen Punkt.
Generell glaube ich, es ist aber weitere Zukunft, dass Software, dass einzelne Systeme weggehen und ich in der AI halt sagen werde, irgendwann mal, was sie machen soll.
Also speichere mal alle E-Mail-Adressen von allen Kunden oder aggregiere die oder sag mir, in welchen Ländern die sind, ohne dass ich ein CRM-System programmieren müsste.
Wie man es vielleicht heute machen würde oder ohne dass man ein CMS machen müsste oder etwas wie HubSpot programmieren.
Sondern alle diese Aufgaben kann letztlich eine AI generisch lösen, ohne dass dafür Code generiert werden muss.
Der erste Schritt in diese Richtung, glaube ich, werden Datensysteme sein.
Ich habe in der Vergangenheit auch mehrmals Firmen geholfen und CTOs geholfen, ihre Datensysteme zu modernisieren und Datateams aufzusetzen.
Da glaube ich aber, das werden die ersten sein, die wahrscheinlich massiv darunter zu leiden haben.
Das heißt, Datensysteme als erste Instanz etwas, wo ich kein spezielles System mehr habe, sondern eine generische Lösung auf einem Data Lake und dann sage ich, mach mal für Montagmorgen die KPI-Diagramme und dann kommen da fünf Slides raus und dann können wir uns die angucken.
Da brauche ich aber keinen Data-Analysten dazu und keinen SQL-Menschen und keinen Plumber, der die Sachen zusammensteckt.
Vielleicht der Plumber bleibt vielleicht, brauchen vielleicht immer, kann sein.
Das war es, meine Meinung.
Super.
Dann vielen, vielen Dank euch vier schon mal für eure Meinung.
Wir haben im Chat schon ziemlich viel Nachrichten bekommen, dass zum Beispiel Christian Beuthenmüller, der hat als allererstes mal geschrieben, Overhype zumindest bei LLMs, also das ist seine Meinung und nachher, ich glaube, als Ralf gesprochen hat, hat er das ungefähr geschrieben, wir haben jetzt schon Grenzen, Modelle sind nicht besser geworden seit GPT-4.
Sind sie das nicht?
Also ich bin da nicht so drin.
Kann mich da jemand aufschlauen?
Also ich glaube, wir sind mit den Modellen echt ganz weit vorne, also die können schon so verdammt viel, dass jeder einzelne Prozentpunkt, den wir irgendwie in den Benchmarks gewinnen, schon ein großer Schritt nach vorne ist.
Aber ich glaube auch nicht, dass wir die Modelle so stark verbessern müssen, sondern die Frontends und die Art und Weise, wie wir mit den Modellen arbeiten.
Die Modelle brauchen den Kontext, um Software zu entwickeln und nicht nur einen Ausschnitt aus dem Code und wir müssen lernen, wie wir diesen Kontext der Maschine geben.
Und da ist, glaube ich, dann eben eine gute Architekturarbeit wieder von Vorteil, wenn wir, also ich habe zum Beispiel mal die Maschine gefragt, hier das Arc 42 Template für Software Architektur Dokumentation.
Welche Bereiche aus diesem Template sind für dich interessant?
Welche weniger?
Und das war ganz super spannend, weil es eigentlich gesagt hat, fast alle Bereiche.
Mir ist hängen geblieben, dass die Maschine gesagt hat, das Glossar, das ist jetzt sowas, die Fachbegriffe kennt die Maschine.
Aber ansonsten ist es halt wichtig, diesen Kontext für die Softwareentwicklung der Maschine mitzugeben.
André, du hattest auch noch gesagt, dass du so Benchmarks beobachtest.
Ja, also ich würde widersprechen, dass die LLMs nicht besser werden.
Also ich glaube, sie werden in jeder Dimension aktuell noch immer besser.
Und nach LLMs gibt es dann die nächsten Modelle.
Und vielleicht ist doch das Transformer-Modell, auf dem das alles basiert, quasi nicht mehr dann quasi ausreichend.
Aber ich glaube, wir reiten gerade eine große Welle, gerade die Menge an LLMs und Updates.
Ich gebe dir recht, gibt nicht so viele große.
Tendenziell könnte man das auch als kritisch einstufen.
Aber wenn man sich anschaut, was wirklich die großen, die Tech, die Magnificent Seven, mein Gott, man sollte Wörter wählen, die man aussprechen kann.
Also die großen Tech-Companies quasi immer wieder deployen und zur Verfügung stellen.
Dann würde ich sagen, ist es signifikant, dass was man in diesem Benchmark sieht, vielleicht das als Einschub noch, das sind natürlich immer getunte Modelle und das ist sicherlich auch eine Ebene, also ich würde jetzt zum Beispiel nicht sagen, dass man in den ganz normalen Gemini 1 5 Pro halt einfach seinen Software-Repo reinschmeißen sollte und darauf dann quasi basierend entwickelt.
Also das, was man in diesen Benchmarks quasi sieht, sind eigentlich durch die Bank weg alles getunte Modelle, alles quasi auch mit entsprechendem Tooling versehen.
Da bin ich bei euch.
Das fehlt.
Aber vor dem Hintergrund, klar, jede Meinung akzeptiert.
Ich würde es anders sehen, einfach aus der puren Erfahrung.
Ich versuche wirklich alles auszuprobieren.
Ich muss Stefan ein bisschen beipflichten, wirkt ab und zu ein bisschen wie Magie, wenn man sieht, wie gewisse Tools halt quasi einem da auch Vorschläge machen.
Ich würde vielleicht kurz einwerfen, wenn ich eine Schwäche beim Thema LLM sehe, ist denn den Fokus auf LLM.
Ich bin mir nicht ganz sicher.
Das ist ein bisschen wie mit Elektroautos und mit Wasserstoffautos.
Wasserstoff ist vielleicht bestimmte Sachen besser, aber die Masse an Ladeinfrastruktur und so weiter ist ja klar, dass das Elektro besser ist, bequemer und andere Sachen hat.
Und die Frage ist, ob das mit LLM und anderen Modellen ähnlich ist.
Also gibt es bessere Modelle für bestimmte Sachen oder eigene Modelle?
Sollte ich eigene Modelle machen oder trainieren oder eben nicht?
Kann das alles LLM?
Da bin ich mir zum Beispiel noch nicht so sicher.
Ich habe einen sehr erfolgreichen Kunden, der im Sinne von Jobs to be done.
Früher Software entwickelt hat für Kunden und jetzt Probleme für Kunden löst, indem er eigene AIs trainiert, die dem Kunden bestimmte Arbeiten abnehmen.
Also er hat vorher sehr tolle Tools gebaut, wo der Kunde so SaaS mäßig Sachen machen kann.
Und jetzt nimmt er den Jobs ab und das macht er aber nicht mit LLM, sondern mit eigenen Modellen.
Und da bin ich nicht sicher, wo es dahin geht.
Super, genau, Poliboy hat auch noch kurz ergänzt, angeblich ist die Hardware Skalierbarkeit für LLMs fast erreicht, durch die noch Fortschritte gemacht werden können.
Das hat noch jemand geschrieben.
Und was ich wollte, Ralf hat sich entmutet.
Du willst dazu was sagen?
Ich wollte es nur eben bestätigen.
Also wir denken jetzt immer an Gen AI und die LLMs.
Und das ist natürlich ein großes Problem.
Das war eigentlich auch schon vorher ein Problem.
Also ich habe mal gesucht, wie man Barcodes am besten decoden kann und bin auf viele Blogposts gestoßen, wo ein neuronales Netz trainiert worden ist, um die Barcodes zu erkennen.
Das ist natürlich blöd.
Ja, und genauso könnte ich jetzt LLMs für solche Tätigkeiten nutzen.
Aber damit verschwende ich nur Energie.
Und wir benutzen jetzt vor allem die LLMs, weil sie eben schon da sind und weil sie uns die Programmierprobleme lösen.
Aber es sind so viele Leute an den Unis und in den Firmen damit beschäftigt, diese Large-Language-Models in Small-Language-Models umzuwandeln, damit sie eben, wie André vorhin auch sagte, on the edge laufen können und auf kleineren Devices, damit man diese Technologie jetzt in den Griff bekommt.
Und das ist weiterhin, deswegen finde ich diese Unterscheidung in Gen-AI und KI auch so wichtig.
Das ganz normale Machine Learning ist weiterhin sehr, sehr wichtig, weil wir damit schon vor Gen-AI sehr gut Probleme gelöst haben und das nicht außer Acht lassen sollten.
Also hier im Chat ist total viel, aber ich glaube, wenn ich jetzt hier alles vorlese, was gerade im Chat passiert, dann kommen wir nie zu dem nächsten Thema, was wir eigentlich besprechen würden und wollten, und zwar, was können wir denn überhaupt heute schon tun?
Also was bedeutet das heute für uns, das ganze Thema mit der KI?
Ihr hattet schon, als ich in den Call kam, alle fleißig diskutiert.
Von daher würde ich einfach mal die Frage in den Raum werfen.
Was bedeutet das heute für mich?
Was sollte ich heute schon tun?
Und Eberhard sah aus, als wollte er reden, ist den Kopf zur Seite gedreht und kurz den Mund aufgehoben.
Finde ich, ist eine spannende Frage.
Ich glaube, eine Sache ist, sich mit den Technologien vertraut zu machen und sie tatsächlich ernsthaft zu nutzen.
Und da ist halt etwas am Werden.
Und wie gesagt, einer der Gründe, warum ich glaube, dass es sinnvoll ist, diese Episode zu machen, ist, weil ich immer noch das Gefühl habe, dass viele Leute sich darauf nicht einlassen und da nahezu technologiefeindlich sind.
Und das ist irgendwie schwierig, nicht?
Also ich glaube halt, dass sich da einiges ändern wird.
Ich bin ehrlich gesagt nicht sicher, was die konkreten jetzigen Hinweise sind.
Ich glaube, also jetzt auch nach der Diskussion, die wir bis jetzt geführt haben, dass, also wie soll ich sagen, ich hatte bisher gedacht, dass man irgendwie sagt, naja, wir haben halt eine höhere Ebene von Abstraktion und sagen halt, implementiert das mal, was ja eben genau das ist, was Ralf gemacht hat mit diesem Linter für SGDoc.
Und dann haben wir eben tatsächlich eine höhere Ebene von Abstraktion.
Also dann ist es eben so, wie man einem Entwicklern sagt, implementiert das mal und die macht es dann halt.
Unter der Voraussetzung bedeutet das halt, dass wir uns noch stärker orientieren müssen an den Dingen, die ja dann wie wichtig sind, also mit Kundinnen zum Beispiel sprechen, verstehen, was fachlich tatsächlich der Fall ist, was exakt die Veranforderungen sind und von daraus sozusagen eine Lösung entwerfen.
Und das ist meiner Ansicht nach eben traditionell das schwierige Thema.
Und das wird, glaube ich, auch das schwierige Thema weiterhin bleiben.
Und darauf müssen wir uns noch stärker fokussieren.
Ich glaube, die andere Sache und daraus ergibt sich dann eben auch.
Das ist auch so etwas, was ich so ein bisschen aus der Diskussion mitgenommen habe.
Eigentlich ist Code ja ein Mechanismus, mit dem Menschen miteinander kommunizieren.
Also ich schreibe es halt einmal.
Es wird vielfach gelesen.
Es wird geändert.
Wir müssen jetzt irgendwie weg davon kommen.
Und das ist halt genau diese Sache, die Ralf auch angesprochen hat.
Das ist halt jetzt so weit, dass man sagt, okay, dieses Diagramm will ich aber maschinenkompatibel haben.
Also wir müssen halt irgendwie dafür sorgen, das wird vielleicht ersetzt in Richtung von Menschen und Maschinen kommunizieren über Code und über bestimmte andere Dinge.
Da haben wir übrigens meiner Ansicht nach in der Episode mit Ralf von Pfeder gemacht.
Wir hätten nämlich eigentlich sagen müssen, hey, hier sind Qualitätsszenarien.
Wir haben aber Qualitätsszenarien erstellen lassen.
Also da sind Dinge, die wir, glaube ich, da noch besser machen können.
Und ich fand auch den Hinweis interessant von Stefan, dass das halt so ein allgemein generisches Ding ist, was halt einfach ein Problem lösen kann.
Und das bedeutet, dass wir halt noch was anderes haben.
Also wir haben halt nicht eine höhere Ebene von Abstraktionen, sondern was anderes, wo wir anders Dinge ausdrücken können.
Und da muss man sich, glaube ich, auch mal Gedanken darüber machen, was das denn nun tatsächlich bedeutet für die Projekte.
Und nicht also diese Hinweise, die auch Stefan da gegeben hat, nicht, dass vielleicht so eine Datenanalyse in Hochsprache, also normaler deutscher Sprache oder englischer Sprache oder was auch immer, dass das halt vielleicht ein Zukunftsding ist, nicht?
Guter Punkt.
Und das wäre etwas, was wir im Moment nicht so einfach umsetzen können.
Ich habe vielleicht eine etwas schwammige Nachfrage.
Du hast ganz am Anfang gesagt, dass du, dass es Leute gibt, die sich gerade mit dem Thema nicht auseinandersetzen wollen und dass, dass sie sich quasi, dass sie dagegen sind, mehr oder weniger.
Ist es denn so schlimm, wenn ich mich jetzt heute noch nicht damit auseinandersetzen möchte, wenn ich quasi noch ein bisschen warte, bis der Hype etwas abgeebbt ist?
Also ich sehe noch nicht so ganz den, dieses, was daran schlimm ist, wenn ich mich jetzt heute noch nicht damit auseinandersetzen möchte.
Was wir noch nicht angesprochen haben, ist, wir haben einen massiven Energieverbrauch und das wird ein großes Problem werden.
Das ist jetzt schon ein großes Problem und das ist sicherlich ein Nachteil von AI und AI wie alle Technologien hat irgendwie Nachteile.
Ich glaube, das, wo ich ein bisschen Angst habe, ist, dass wenn man sich damit auseinandersetzt, dass man dann wirklich irgendwann obsolet wird.
Und ich bin da, glaube ich, nicht so wie Stefan, der ja sagt, nicht.
Also das ist halt das neue Ding, was mich hat total begeistert.
Aber ich warne, glaube ich, vor der Fehlwahrnehmung, dass das halt nur ein Hype ist.
Also nicht Shichibiti ausprobieren.
Ich habe es halt irgendwie eine Stunde ausprobiert, als es halt rauskam.
Und ich war nach einer Stunde überzeugt, dass das halt ziemlich krasse Sachen sind, die ich vorher nicht für möglich gehalten habe.
Und ich habe ein Problem.
Also wie soll ich sagen, wenn man jetzt irgendwie sagt Nein, es ist halt nur ein Hype, dann ist das halt meiner Ansicht nach objektiv einfach falsch.
Und das bedeutet, dass man sich möglicherweise in seiner Karriere und halt in dem, was man halt so tut, in Anführungsstrichen falsch verhält, also nicht Dinge halt irgendwie falsch einschätzt.
Und das finde ich halt einfach schwierig.
Also ich glaube halt nicht grundloser, grundloses Hype-Wissen ist halt ein Problem oder Grundloser, ein Hypes-Glauben ist halt ein echtes Problem.
Und da ist halt Blockchain für mich halt ein, da gab es halt Leute, die irgendwie an diesen Hype geglaubt haben.
Und das war eben grundlos.
Das andere, wo ich irgendwie mich mit der Technologie nicht ausreichend kritisch beschäftigt habe, war EGB am Anfang.
Ganz anderes Thema.
Und ich glaube, bei KI ist es umgekehrt.
Also gibt es ein bisschen diese umgekehrte Tendenz.
Für mich ist immer, ich würde noch, darf ich kurz, Stefan?
Immer.
Okay, ansonsten schlägt das Alphabet, also Vorname.
Was ich gerade mitbekomme oder was ich, was ich immer wieder höre, ist also gegen was das halt antritt, also der Vergleich.
Und für mich ist die Frage, also tritt das gegen, also tritt Gen-AI gegen Cloud an oder gegen Microservices oder tritt das gegen, ich mach jetzt mal das krasse Gegenteil, tritt das gegen Feuer und Elektrizität an?
Also quasi über, also wo ordnet sich das, das Thema halt ein?
Und das, ich glaube, wenn es sich eher quasi bei dem Cloud-Thema einordnet, dann würde ich sagen, okay, brauchst du dich im Zweifelsfall nicht beschäftigen.
Das wird auch wahrscheinlich noch in 100 Jahren quasi Data Center geben, die quasi anders funktionieren.
Gibt immer gewisse Use Cases, die vielleicht eben nicht in der Cloud laufen können oder wo man Infrastruktur nicht so weitestgehend automatisieren kann.
Wenn das allerdings gegen die andere Seite antritt, dann ist es schon ziemlich fundamental.
Und jetzt ist vielleicht Feuer und Elektrizität also sehr, sehr, sehr weit quasi auf der anderen Seite.
Aber man könnte auch sagen, es tritt quasi gegen die Dampfmaschine halt irgendwie an.
Und das ist vielleicht dann schon irgendwas, was wir alle auch dann wiederum nicht kennen, aber was vielleicht ein bisschen greifbarer ist.
Und da muss man schon sagen, da sind ganze Industrien weggefallen.
Und vor dem Hintergrund und das vermisse ich so ein bisschen.
Meine Frage, die Frage war ja so ein bisschen, also was müsste man heute schon tun?
Und das verstehe ich nicht, weil ich quasi eigentlich unsere Disziplin immer als sehr neugierig wahrnehme.
Quasi diese Offenheit gegenüber einer Sache.
Und was ich halt häufig wahrnehme, ist entweder so eine relativ theoretische Sache.
Habe ich irgendwas gelesen?
Aber ich habe es nie probiert.
Und eine der Sachen, die wir machen, um da mal ein konkretes Beispiel zu machen, wir haben einmal im Monat so einen Self-Education-Friday und eigentlich versuchen wir da, die Leute zu ermutigen, mal Sachen auszuprobieren.
Das heißt, es gibt verschiedene Themen, aber unter anderem halt auch Gen-AI, wo man mal sehen, guck mal, man kann halt auch einen LLM auf seinem Notebook laufen lassen, kann ja halt irgendwie deiner täglichen Arbeit halt irgendwie helfen.
Ich will jetzt nicht sagen spielerische Herangehensweise, aber ich habe unsere Disziplin eigentlich immer so verstanden, Neugier, Automating all the things und halt einfach Sachen auszuprobieren und natürlich quasi dieses ganz große Bild, was das Szenario, was Stefan gerade gezeichnet hat, also quasi vielleicht gibt es gar keine Software, das mag irgendwann mal kommen.
Und da kann man sich natürlich jetzt vortrefflich drüber streiten, weil man es noch nicht, weil es ist nicht around the corner wahrscheinlich.
Aber quasi was kann ich heute quasi einfacher machen?
Womit kann ich mein Leben leichter machen?
Wo kann ich halt irgendwie das wegautomatisieren oder auslagern, was mir vielleicht auch persönlich gar keinen Spaß macht?
Das vermisse ich.
Also für mich beginnt das tatsächlich individuell im Kopf.
Ich habe gerade kam im Chat ein Kommentar zu dem Dampfmaschinenvergleich und zwar schreibt Happy Tree, der Unterschied zu dem Dampfmaschinenvergleich ist, dass wenn das funktioniert, es keinen neuen Arbeitsbereich gibt.
Ich weiß nicht mehr, wer von euch es sagt, aber irgendjemand sagte schon vorhin, dass man die Beine von seinem eigenen Stühlchen abschneidet oder so.
Du warst das, genau.
Ich war beide, beide sogar, genau.
Nee, ich wollte bloß kurz was sagen.
Also ich, jetzt geht es ja um die Softwareentwicklung so ein bisschen weniger um allgemeine.
Aber für das Allgemeine glaube ich, dass da würde ich dem Kommentar aus dem Chat sehr, sehr zustimmen.
Wir haben durch Rationalisierung alle Leute aus dem Agrarsektor in den Industriesektor, der glücklicherweise durch die gleichen Bedingungen zur gleichen Zeit entstanden ist, verfrachtet.
Und dann haben wir alle Leute aus dem Industriesektor in den Dienstleistungssektor verfrachtet.
Wenn man sich heute eine Fabrik anguckt, dann ist die quasi komplett leer, kaufen ganz wenig Leute rum.
Und jetzt verlagern wir Leute aus dem Dienstleistungssektor irgendwo hin.
Aber leider ist halt, das war jetzt so der dritte Sektor.
Aber es ist unklar, wo die Leute hinverlagert werden.
Also das ist, glaube ich, der ganz große Unterschied zur Dampfmaschine.
Und da würde ich mich dem ein bisschen dem Kommentar anschließen.
Ich habe noch einen Punkt zu dem vorher zu dem Energiethema, was mir immer ein bisschen aufstößt, also jetzt hier nur allgemein.
Es wird sehr, sehr stark vermischt an Training und Inferenz.
Also das hat natürlich jetzt auch stark mit dem aktuell, wie wir arbeiten, zu tun, mit LLMs und mit dem quasi mit dem Batch arbeiten, also mit dem Trainieren und mit dem Benutzen und mit dem Trainieren und mit dem Benutzen.
Aber trotzdem, glaube ich, muss man schon auch immer ein bisschen unterscheiden, weil Ralf vorher, glaube ich, es gesagt hat oder Andreas gesagt mit dem Laptop.
Aber letztlich kann ich es auf meinem Handy haben.
Also die Energienutzung von LLMs nutzen und von LLMs trainieren ist potenziell auch nochmal eine andere.
Das wird auch bei Performance oft und bei Hardware Performance oft irgendwie alles in einen in einen Topf geworfen.
Für mich sind es aber aktuell durch den Batch Modus zwei fundamental unterschiedliche Operationsmodelle von von AIs mit unterschiedlicher Performance, unterschiedlichen Energieverbrauch und so weiter und so fort.
Vielleicht ein paar Gedanken, also weil du es gerade sagtest, André, von wegen, wo trägt das an?
Also wir haben das ja im Stream exerziert.
Das heißt, wir haben gesagt, liebes, liebes Chetchipi Team, mach doch mal die SAP Beispielaufgabe.
So, damit lassen wir es halt in mir antreten gegen Software Architekten, die sich halt zertifizieren lassen.
Und das Schlimme dabei ist, dass die Ergebnisse zumindest scheinbar gar nicht so schlicht sind.
Und das ist genau das, was wir jetzt vor 14 Tagen in dem in dem Stream nochmal gesehen haben.
Also wenn ich mir Qualitätsszenarien angucke, also was sind die Dinge, die dieses Verfahren leisten soll?
Da kommt halt eine ein über ein überzeugend klingender Text raus.
Und wenn mir jetzt jemand fünf Sachen vorgeben würde und halt sagen würde Okay, guck dir mal die die an und sag mir mal, welches davon irgendwie von Chetchipi ist, bin ich mir nicht sicher, ob ich es rausfinden könnte.
Und das ist enttäuschend, weil das, was da irgendwie rauskommt, ist halt aus den Fingern rausgesogen.
Also kommen halt Performance Ideen raus, die halt irgendwie vom Himmel fallen.
So und das ist eine nicht positive Aussage über unsere Branche.
Wir müssen da besser werden.
Wir müssen halt solche Dinge wie Qualitätsszenarien, Anforderungen, solche Sachen halt besser hinbekommen und deutlich unterscheidbar sein von irgendwelchen AIs, sonst haben wir ein Problem.
Und das ist und das ist aber das, was also nicht, weil du sagtest, wo tritt das an?
Also da draußen sind garantiert Leute, die genau das machen und die halt dann irgendwie genau dieses, die halt dann sagen Okay, reicht ja.
Also nicht haben wir ja.
Und ich bin mal gespannt, wie das sozusagen rausgeht.
Und wir müssen da irgendwie, glaube ich, qualifizierter werden und besser werden.
Und bezüglich der Produktivität.
Ich finde das auch ein schwieriges Thema, weil nicht vor langer Zeit war es so, da gibt es immer wieder solche Schilde.
Wir haben schon diskutiert, die Fabriken sind mittlerweile leer.
Trotzdem gibt es noch Facharbeiter, die Autos bauen oder solche Dinge tun.
Ich erinnere mich an die Zeit, wo ich Anfang der 2000er war, wo die Aussage war, wir machen Offshoring und Nearshoring und dann ist das Thema mit Softwareentwicklung in Deutschland tot.
Das ist einfach nicht so.
Wir sind eine der größten Branchen, auch in Deutschland, auch in diesem Hochlohnland, obwohl das von der Autoindustrie so dominiert ist.
Zitiert mich nicht, aber ich meine, wir sind auf Augenhöhe mit der Autoindustrie.
Es gibt halt Produktivitätszuwächse und die führen scheinbar dazu, dass – oder nicht, wenn man das sozusagen extrapoliert von man hat – wir in diesem Bereich nicht mehr arbeiten.
Ich habe nur das Gefühl, das ist nicht so.
Es ist immer noch so, dass du als Facharbeiter in einem Automobilwerk gutes Geld verdienen kannst und du kannst immer noch als Entwickler hin gutes Geld verdienen, obwohl du im direkten Wettbewerb stehst zu irgendwelchen Leuten, die Offshoring machen.
Ich bin nicht sicher, ob das das Ding ist, was unser gesamten Brancheit das Licht ausbläst.
Wäre überraschend, weil die anderen Ansätze haben es im Jahr auch nicht geschafft.
Das war jetzt ein langes Statement, wenn ich das mal so sagen darf.
Du hast da sehr viele Punkte angesprochen, gerade jetzt zum Beispiel, die KI kann innerhalb kurzer Zeit eine Architektur erstellen und wir brauchen relativ lange, um diese Architektur zu validieren.
Zeit ist ein teures Gut und das merke ich eben auch, wenn die KI mir Code generiert innerhalb von Sekunden und ich brauche Minuten zum Verifizieren.
Gerade wenn ich jetzt sowas wie den ASCII-Doc Linter so nebenbei erstellen lasse, die Zeit, das alles zu verifizieren, ist teuer, ist aufwendig.
Und sobald ich da einen gewissen Trust in die Maschine habe, werde ich das bleiben lassen.
Aber interessant ist eben auch bei der Arbeit mit der Maschine.
Das, was ich kontrollieren kann, das kann ich ganz gut mit der Maschine bearbeiten, weil sie erzeugt mir etwas.
Ich gucke drüber, sage Ja, passt, die Qualität stimmt.
Noch besser ist es, wenn die Maschine das selbst kontrollieren kann.
Und da sind wir halt mit der Softwareentwicklung in einer Situation, die einfach toll ist.
Dadurch, dass wir automatisierte Tests machen können, sind gerade diese Bereiche wie der ASCII-Doc Linter.
Ich habe ein einfaches Interface, ich kann Tests schreiben und die Maschine kann selbst gegen die Tests ausprobieren, ob ihre Software funktioniert, kann selbst iterieren.
Jetzt bin ich natürlich noch einen Schritt weiter gegangen und habe gesagt, Maschine, schreibt dir selbst die Tests.
Und da brauche ich dann wieder das Vertrauen oder ich brauche den Aufwand, um es zu überprüfen, was die Maschine da geschrieben hat.
Und das geht halt in den Bereich, der wirklich viel mit mit Trust in die Maschine zu tun hat und wo wir eben auch mit der Zeit sehen werden, wie sich das entwickelt.
Und auch weil die Maschine so schnell manche Sachen machen kann, Aufgaben, die wir nicht gerne machen, laufen wir teilweise Gefahr, sie falsch einzusetzen.
Also neue Features entwickeln, macht Spaß.
Die Tests dafür zu schreiben und die Dokumentation zu erstellen, macht keinen Spaß.
Also übergeben wir das der Maschine.
Wir schreiben erst den Code, erst die Features, sagen dann der Maschine, du dokumentiere das mal und schreib mir die Tests.
Also hatten wir ja vorhin schon Test-Driven geht anders, ist das erste Problem.
Mit der Dokumentation ist das zweite Problem, weil die Maschine sieht den Code, kann nur sagen, was der Code macht, also das was dokumentieren.
Warum ich das Ganze so aufgebaut habe, warum ich folgende Libraries benutzt habe, das kann sie in dem Moment nicht sagen.
Es sei denn, ich mache den Kontext wieder groß und dieses Warum, das ist teilweise eben in der Architektur, dass wir uns für Technologien entscheiden aufgrund der Qualitätskriterien.
Und das wird dann eben spannend, wenn wir das mit der Maschine machen.
Aber diese diese Vorgänge sind wieder zeitlich aufwendig und es wird längere Zeit dauern, bis wir eben verschiedene Experimente gemacht haben, wie wir mit den Maschinen arbeiten können.
Und dann eben diese Experimente auch entsprechend bewerten können, um zu sagen, das war der richtige Weg oder eben auch nicht.
Zum Thema Verifikation hat HappyTree gerade noch auf YouTube geschrieben, die Verifikation ist auch der Game Changer.
Bis wir das haben, wird zum Beispiel im Medizinbereich und so weiter auch nicht KI zum Einsatz kommen.
Aber das wird auf jeden Fall kommen, denkt er.
Und er hat gerade noch geschrieben, man muss sich ja nun mal angucken, was im Modellchecker-Bereich im RE, wahrscheinlich Requirements Engineering Bereich geht, wie viele der Requirements am Ende unvereinbar sind.
Hat er noch geschrieben.
Stefan, du hast, glaube ich, noch gar nichts gesagt jetzt hier zu der Frage.
Wie ungewöhnlich.
Also vielleicht noch mal ganz kurz zum Hintergrund.
Ich habe zwar in größeren Firmen auch ein bisschen gearbeitet, aber mein Hintergrund ist eigentlich so bis 50, 60 Entwicklern in meistens stark wachsenden Startups, wo ich entweder Cyber Engineering Manager war oder jetzt meine Kunden sind.
Das heißt, das sind wahrscheinlich auch so ein bisschen unterschiedliche Welten, vielleicht auch vom Programmier-Niveau, vom Herangehensniveau von anderen.
Da unterscheiden wir uns sicherlich in dem Hintergrund oder unterscheide ich mich vielleicht ein bisschen im Hintergrund von anderen Leuten hier.
Und da muss ich sagen, beim Thema Test und AI, immer wenn, da hatte ich mich auch mit jemandem vor kurzem drüber unterhalten.
Wir waren der Meinung, in dem Kontext, in dem wir uns bewegen, schreibt AI bessere Tests.
Also besser, weil mehr.
Also besser durch Quantität und besser durch Qualität.
Das heißt, da muss man natürlich immer noch mal gucken, was will man mit den Tests?
Will man mit den Tests Requirements abdecken?
Will man Regressionen vermeiden?
Also was ist denn vielleicht die Aufgabe?
Und dann ist auch innerhalb von dem Test, wo die AI manche Sachen besser kann und manche Sachen schlechter kann.
Aber irgendwie scheint die AI meine Code-Basis und andere Klassen mehr zu verstehen und durch Anbindung potenziell an größere LLMs die Welt besser zu verstehen und an Sachen zu denken, an die ich nicht denke.
Und von dem Hintergrund, wenn ich vielleicht nicht sehr stark, jetzt mal eben kein Medizinbereich, vielleicht auch kein Rüstungsbereich oder keine kritischen Bereiche, würde ich eher dazu gehen, dass die AI bessere Tests schreibt als der Durchschnittsentwickler und meistens bessere Tests schreibt als ich, vielleicht eben als Durchschnittsentwickler.
Durch den größeren Hintergrund an Wissen und an was kann denn eigentlich schief gehen?
Du hast da zwei interessante Punkte genannt.
Also zum einen, die AI schreibt halt schnell viele Tests.
Dadurch habe ich schnell eine hohe Testabdeckung.
Meistens kriegen die Entwickler aufgrund von Zeitdruck gar nicht die Möglichkeit, sich mal über die Tests groß Gedanken zu machen.
Zumindest ist das so meine Erfahrung.
Wir haben die Theorie, wie es laufen sollte und wir haben die Praxis.
Das andere, was du gesagt hast, ist, dass du das Gefühl hast, dass die AI dein Repository gut versteht und ein gutes Weltbild hat.
Da finde ich es interessant, dass es dazwischen noch etwas gibt, dass ich zum Beispiel mit der AI in einem Repository arbeite, welches zu einem größeren Projekt gehört.
Und das kennt die KI momentan meistens nicht, weil sie sich auf ein Repository konzentriert.
Das heißt, sie kennt gar nicht die Schnittstellen zu der anderen Software.
Oder wenn wir jetzt die Architektur Dokumentation in einem Wiki haben, kommt die KI nicht dran.
Wenn wir aber den DOCSIS Code Ansatz verwenden, dann kann es passieren, dass unsere Architektur oder andere Dokumentation im Repository liegt und die KI, die aufgreift, die Qualitätskriterien vielleicht findet und deswegen sagt, oh, dann nehme ich lieber die Library anstatt jener.
Oder Zugriff auf Bug Reports hat und Critical Incidents und Postmortems.
Und da fällt mir auch gerade wieder ein, ich habe gerade wieder was entwickeln lassen und die KI hat ja einen alten Stand von Libraries benutzt, weil sie eben ein Knowledge Cutoff von vor einem Jahr hat.
Und dann haben wir da auch wieder ein Problem.
Wie gehen wir mit neueren Versionen um?
Das sind alles Sachen, auf die sich heutige Entwickler einstellen müssen.
Wir brauchen Antworten auf diese Fragen.
Was aber by the way bedeutet, und das ist auch etwas, was mir auffällt, dass die Anforderungen an Menschen in diesem ganzen Bereich eigentlich eher steigen.
Das, was du jetzt zum Beispiel als Beispiel gesagt hast, ist, hat eine alte Library benutzt, suboptimale Idee, muss ich halt irgendwie korrigieren.
Das heißt, ich muss nicht das Problem lösen, sondern ich muss erkennen, dass das Problem nicht vernünftig gelöst ist und es noch besser lösen.
Und das ist halt anspruchsvoll, wobei man auch natürlich argumentieren kann, aber es funktioniert ja und dann ist ja gut.
### Zukünftige Anforderungen

Und vielleicht ist das auch ein Teil der Komponente.
Also wenn man sagt, ich will am Ende nur etwas haben, was funktioniert und mein konkretes Problem löst, vielleicht definiert durch Tests, dann kriege ich es halt.
Und das ist vielleicht intern gar nicht so wahnsinnig schön.
Du hattest noch einen Kommentar bekommen, der bezog sich eventuell nur auf deinen Kommentar, den du in YouTube geschrieben hast, aber er passt, glaube ich, generell noch ganz gut von Christian Beuthmüller.
Er hat nämlich geschrieben, KI generierter Code basiert auf GitHub und Stackoverflows wird nicht besser werden als der Durchschnitt.
Und ich finde, der Kommentar passt auch nochmal gut zu den generierten Tests, die Stefan erwähnt hat.
Ich bin nämlich immer noch, also in meinem Kopf bin ich immer noch bei diesen Tests, die besser sind als die menschgeschriebenen Tests.
Und ich frage mich, wie das dazu kommen kann, dass sie besser sind.
Also ich hänge da, glaube ich, im Kopf noch ein bisschen dran.
Genau, und was ich jetzt noch gerade kam, noch ein von Happy Tree auch sehr interessant, finde ich auch die Frage, was mit Problemen wie dem XZ-Exploit passieren wird in diesem Kontext.
Da habt ihr da eine Meinung zu?
Also Richtung Exploits, Security, KI?
Also da sind jetzt verschiedene Punkte.
Der eine Punkt ist halt, also weil du bei den Tests sozusagen noch hängst, ich glaube, also wie soll ich sagen, ich bin nicht sicher, ob mich das überrascht, weil das bedeutet, dass halt viele Dinge, die wir halt in unserer Branche machen, eben qualitativ nicht so gut sind.
Und das führt irgendwie dazu, dass halt eine AI über diese Hürde drüber springt und halt besser ist.
Und ich weiß nicht, ob mich das überrascht.
Ich frage mich nur, was das bedeutet.
Also wenn jetzt einer von diesen generierten Tests fehlschlägt, also sind die, kann man die gut verstehen?
Versteht ihr dann gut, wo jetzt das Problem liegt?
Also das sind ja auch nochmal Sachen, also ich schreibe ja auch einen Test, der mir nochmal sagt, okay, ich habe das Problem verstanden, ich weiß, was die Lösung sein soll.
Also das Schreiben des Tests hat ja einen positiven Effekt auf das Verständnis des Gesamtcodes.
Und wenn ich dann sehe, dieser Test schlägt fehl, weiß ich ja warum.
Und wenn ich mich jetzt so daran zurückerinnere, auch nur wenn ein anderer den Test geschrieben hat und genau dieser Test schlägt dann fehl, je nachdem, wie komplex oder unumständlich der geschrieben ist, hampel ich ja dann daran länger rum.
Und ich frage mich nur gerade, wie gut das noch so für die restliche Nachvollziehbarkeit der Problemlösung ist, wenn dann mal ein Test fehlschlägt, weil wir einen Change gemacht haben.
Stefan, du hättest dich gemeldet.
Das mit dem Fehlschlagen ist, denke ich, ja üblich jetzt schon ein Problem, wenn jemand einen anderen Test geschrieben hat und ich habe den nicht geschrieben.
Das passiert ja öfter mal in Firmen bei Integrationstests oder sowas und dann hält das auf, weil ich nicht verstehe.
Also ich glaube, das kann ich nachvollziehen.
Ich wollte aber zu dem, wie kann es besser sein, als ich einwerfen.
Es gab mal diese Blogposts, wo dort stand, 100 Mythen, die Entwickler über Adressen glauben oder über Namen glauben oder sowas.
Also das weiß ich nicht.
Und vor dem Hintergrund glaube ich schon, dass eine KI bessere Tests schreiben kann als der Entwickler.
Ich glaube, ich bin bei besser eher so ins Stocken geraten.
Nicht ob der Vielfältigkeit der Tests und gerade bei Validierung glaube ich sofort, dass Entwickler nicht anders denken, was wirklich validiert werden soll, sondern eher in Richtung der Lesbarkeit der Ergebnisse, eben weil die Dinge über Stack Overflow und GitHub gezogen werden und nicht alle EntwicklerInnen bisher groß auf Lesbarkeit von Dingen geachtet haben.
Also ich hatte gerade jetzt das Problem, dass die Tests, die die Maschine mir erzeugt hat, tatsächlich für mich nicht so schön lesbar waren.
Ich habe der Maschine dann gesagt, sie soll sie überarbeiten und bitte mit Behavior Driven Development arbeiten, dass ich eben sehe, gegeben das und das.
Wenn das passiert, dann erwarte ich Folgendes.
Und dadurch wurde es wieder lesbarer.
Also ich meine, das ist dann eben jetzt auch so eine Entwicklung, dass ich der Maschine Verhalten beibringe, dass ich ihr sage, wie ich Software entwickeln möchte.
Und das landet dann im System prompt und das nächste Mal macht sie es dann eben genauso, wie ich das brauche.
### Vertrauen in Maschinen

Das spricht so ein bisschen für die These, dass man quasi prompt Engineering auf jeden Fall besser werden soll.
Wer hat das vorhin gesagt?
Shit in, shit out.
Das ist ja mit fast allem eh so.
Also wenn ich schlechte Requirements habe, dann kriege ich ja auch eine schlechte, eine unpassende Software.
Das ist ja nicht nur bei KI.
Ja, wir brauchen halt vor allem Mechanismen, wie wir die KI uns unseren Bedürfnissen anpassen können.
Und André hatte vorhin dieses Feintuning genannt.
Also zumindest André, du sagtest, dass die ganzen Modelle in den Benchmarks getunt sind.
Und ja, ist das dieses Feintuning, was man in den in der Dokumentation liest?
Oder meinst du, das sind quasi auf spezialisierte, mit spezialisierten Trainingsdaten gefütterte Modelle?
Sowohl also sowohl das als halt auch die Gewichtung, die die Modelle halt irgendwie nützlich bringen.
Also im Zweifelsfall ist ja aus so einem Large-Language-Modell nur ein Bruchteil der Informationen halt irrelevant und die werden einfach höher gewichtet.
Das ist eine Sache.
Da muss ich auch fairerweise zugeben, stehe ich jetzt nicht im Detail drin.
Man sieht bloß diesen Trend, dass es eben nicht ein JGPT 4.0 Mini ist, was da halt irgendwie antritt, sondern das sind alles quasi.
Ich würde fast sogar soweit gehen, zu sagen, das sind alles Forschungsmodelle oder Forschungsansätze, wo halt wirklich sehr genau getweakt wird.
Wie kann man jetzt diese Cases halt irgendwie lösen?
Im Chat kam gerade noch ein spannendes Statement.
Das möchte ich jetzt noch eben loswerden, obwohl wir schon überziehen.
Christian Beuthmüller hat geschrieben, meine aktuelle Erfahrung ist Senior Developer werden schneller und Junior eher das Gegenteil.
Habt ihr die Erfahrung auch gemacht in eurem beruflichen Kontext?
Ich habe ja mit 100 geantwortet, also insofern ja.
Ich glaube, es ist ein großes Problem oder nicht ein großes Problem, aber es ist ein Problem, was ich auch sehe.
Es ist halt quasi, dass halt einfach du der Sache blind folgst und das nicht quasi einhornen kannst.
Die Frage ist halt – das hatte ich auch geschrieben – so what?
Das fügt ja trotzdem jetzt keinen Weg dran vorbei.
Man sollte sich trotzdem mit dem Thema auseinandersetzen.
Das ist für mich immer so eine Frage nach eines bewussten Handelns.
So würde ich es wahrscheinlich einordnen.
Ich muss mir dessen bewusst sein oder ich muss den Leuten bewusst machen, den Kollegen bewusst machen, dass es da etwas gibt.
Aber dass man halt auch quasi mit einem gewissen – wie soll ich sagen – einfach nicht blind einsetzt.
Ich glaube auch, dass der Christian hat darauf geantwortet und würde ich auch zustimmen.
Man muss trotzdem die Grundlagen halt irgendwie beherrschen.
Solange wir in einem Szenario sind, wo wir auch eher das in einem Co-Pilot oder auch irgendwann mal in einem Pilotenmodus haben, muss man trotzdem verstehen, was da passiert.
Ich glaube spannend wird dann erst quasi so dieses Szenario, was Stefan ganz am Anfang aufgemacht hat, quasi Software verschwingelt.
Und da gibt es noch ein paar Episoden vorher.
Das Thema mit den Grundlagen ist aus meiner Sicht ganz wichtig, weil wenn ich die Grundlagen verstanden habe, dann kann ich GenAI sehr gut verwenden, um mir neue Sachen beizubringen.
Also ich habe jetzt Python verwendet, weil ich sage, GenAI kann am besten Python.
Und deswegen habe ich in meinem Zeitprojekt eben Python verwendet, obwohl ich überhaupt keine Ahnung davon hatte.
Aber ich habe mir einiges erklären lassen.
Die Maschine weiß, dass ich eigentlich aus der Java-Welt komme und erklärt mir dann, wie eben Vererbung oder Klassen oder Entkapselierung eben in Python funktionieren.
Und wow, es hilft mir.
Aber die Grundlagen muss ich wissen.
Lustiger Kommentar im Chat von HappyTree.
KI macht dumme dümmer und schlau schlauer wie das Fernsehen.
Deswegen musste ich lachen.
Wir haben schon leicht überzogen.
Hat noch jemand von euch ein Schlusswort, was er noch loswerden möchte?
Also Eberhard sehen wir jetzt nicht, ob er reden möchte, aber ich glaube, wir würden ihn hören, wenn er es wollte.
Stefan hatte länger nichts gesagt.
Möchtest du noch was loswerden, was dir auf der Zunge brennt?
Ja, ich würde noch zwei Sachen kurz loswerden.
Das eine ist die Diskussion um Taschenrechner ab der ersten Klasse.
Das ist so die gleiche Diskussion.
Und das andere ist Punkt, den ich loswerden will.
Alle Engineering Manager, deren Entwickler heute nicht State of the Art AI und Gen AI benutzen, würde ich gleich am Montag irgendwie alle einladen, Pizza kaufen und zeigen, was geht.
Also das wäre schon mein dringender Appell.
Ich hoffe, Montag sind nicht so viele Menschen im Büro.
Vielleicht lieber nächstes Jahr.
Am ersten Montag an dem Leute wieder überhaupt im Büro.
Ich weiß ja nicht, ob jemand ins Büro geht oder so.
## Schlussfolgerungen und Ausblick

Dann würde ich sagen, wir haben jetzt hier eine Stunde spannende KI-Diskussion gehabt.
Ich bin immer noch fasziniert, dass es im Chat auch die ganze Zeit so gut abging und dass ihr Ralf und André auch noch nebenbei im Chat dabei wart.
Respekt, dass ihr zwei Diskussionen verfolgt habt oder sogar drei.
Ich bin sehr dankbar, dass ich heute dabei sein durfte und das moderieren durfte.
Ich weiß, dass Ralf gleich noch ankündigen will, womit es weitergeht im nächsten Jahr.
Erstmal aber danke, André, dass du da warst und danke, Stefan, dass du dabei warst.
Danke euch allen im Chat, dass ihr dabei wart.
Ralf, wie startet Software Architektur im Stream im neuen Jahr?
Ja, wir werden den als ersten Gast den Christian Weiher haben und da wird es wieder um KI in der Software Architektur gehen.
Das wird am 9.1. sein.
Mit der Uhrzeit sind wir noch ein bisschen am Gucken, was da am besten passt, aber es wird auf jeden Fall spannend.
Schaltet wieder ein.
Genau.
Ich packe den Chat auf jeden Fall nochmal zum Download in dieses Internet, also auf diese Webseite, die wir haben, dass man das nachlesen kann.
Super, gute Idee.
Ja, dann danke euch allen, danke euch ZuschauerInnen und schöne Feiertage, erholsame Feiertage und einen guten Rutsch ins neue Jahr.
Genau, guten Rutsch.
