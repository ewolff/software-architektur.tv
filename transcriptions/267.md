# Folge 267 - Architekturtheater mit Claude und Ralf 

## Einführung und Zielsetzung

Heute machen wir Architektur-Theater mit Claude und Ralf.

### Vorstellung des Konzepts

Ihr habt das letzte Mal die Folge hoffentlich verfolgt, wo wir über, ja, darüber gesprochen haben, ob man LLMs, Large Language Models für Architektur einsetzen kann.

Dabei kam die Meinung hoch, dass, naja, das ist ja alles nur Architektur-Theater.

Und deswegen habe ich mir gedacht, ja, dann machen wir diesen Freitag mal Architektur-Theater und gucken mal, wie gut das klappt.

### Setup und Tools

Vorneweg habe ich hier zwei Links für den Chat.

Ihr könnt mal reingucken.

Oh, die sind jetzt unter dem falschen Namen gepostet.

Ihr seht ja, ich bin's, Ralf, nicht Eberhard.

Eberhard ist heute nicht dabei.

Wir haben hier zwei Links.

Einmal auf GitHub, einmal auf das Repository, mit dem wir gleich arbeiten werden, auf dem Claude gleich arbeiten wird.

Da könnt ihr auch mal draufgehen.

Claude wird einen zweiten Branch aufmachen, auf dem Claude dann live arbeiten wird.

Und wir werden das dann irgendwann in den Main Branch reinmerchen.

Und der zweite Link ist ein besonderes Anliegen.

Das heißt, wir haben hier auf unserer Homepage eine kleine Umfrage, ja, aufgesetzt, wo wir euch bitten, mal uns ein bisschen Feedback zur Website zu geben, damit wir wissen, wie wir die Website verbessern können.

So, aber jetzt zu unserem speziellen Gast.

## Vorstellung von Claude

Ich weiß nicht, Claude, ihr kennt alle Chat GPT.

Ihr kennt hoffentlich auch Claude Sonnet, weil Claude Sonnet ist für ITler eigentlich das LLM, was eben sehr gut programmieren kann.

Mittlerweile, die LLMs, die liefern sich ja so ein Rennen.

Aber Claude ist da recht gut im Rennen.

### Claude Desktop Features

Und ich verwende jetzt hier für diese Session Claude Desktop.

Ist noch in der Beta, aber ist eben ein Chat Frontend, was ich runterladen kann, was ich lokal verwenden kann.

Warum verwende ich diese Version?

Weil ich hier ganz jede Menge MCP Tools konfigurieren kann und die dann benutzen kann.

Und ihr seht zum Beispiel jetzt hier.

### GitHub Integration

Hier gibt es ein GitHub Tool, was oder GitHub MCP, was 36 Function Calls mitbringt.

Und dadurch kann dann das System eben direkt auf auf GitHub arbeiten.

Ich habe zwei Accounts mittlerweile auf GitHub.

Ich glaube, sollte ich nicht so laut sagen.

Ich weiß gar nicht, wie, wie das gewünscht ist.

Ich finde es auf jeden Fall praktisch.

Ich habe einmal meinen Erde Müller Account.

Das ist mein alter Account.

Und dann habe ich ganz neu den Reif Müller kleines Wortspiel.

Ich habe hier das L gegen ein I unbemerkt ausgetauscht.

Das ist die KI.

Das ist die KI, die dann eben ja unabhängig auf die Repositories zugreifen kann.

Sie ist dadurch eingeschränkt auf ihre Repositories.

Sie kann auf meine nicht zugreifen.

Sie kann nur Pull Request stellen.

Es kann relativ wenig schiefgehen und ich kann eben sehen, was die KI genau macht.

Aber jetzt begrüßen wir doch erst mal Claude.

Hallo Claude.

Ich werde jetzt versuchen, vieles, was Claude ausgibt, auch noch mal verbal zu wiederholen, weil wir ja auch den Audio Stream haben.

Claude freut sich, dass ich da bin und erklärt mir, was Claude alles für mich tun kann.

Architektur, Dokumentation, ADRs, Architecture, Communication, Canvas.

Das sind alles Prompts, die ich ihm mitgegeben habe, damit er so ein bisschen weiß, wie ich am liebsten mit diesen Tools umgehe, mit dieser Art von Dokumentation.

Jetzt fragt er mich, was er für mich heute tun kann.

Und jetzt gehe ich einfach mal zurück auf das Repository und kopiere die URL und sage ihm, schau dir mal bitte dieses GitHub Repository an.

Mal gucken, was er macht.

Okay, er sagt, er schaut sich das Ganze an.

Er holt die Dokumentation.

Er benutzt jetzt ein spezielles MCP, was über gitmcp.io erstellt worden ist.

Das ist ein Service, mit dem man read-only auf alle möglichen Repositories zugreifen kann.

Jetzt guckt er sich das Projekt genauer an, indem er mal in den Code reinschaut.

Ich kann es leider nicht ausklappen.

Ich weiß nicht, ob das an dem Zoom-Level liegt.

Ja, ihr seht schon, er ist jetzt fleißig am Arbeiten.

Was ist in diesem Repository drin?

## Repository Setup

Ich habe als kleine Vorbereitung ein Requirements-Dokument erstellt und habe natürlich mit Claude das Ganze vorab besprochen.

So machen wir das meistens mit Gästen, dass wir vorher mal drüber sprechen, was wir vorhaben.

Und wir haben dieses Requirements-Dokument erstellt.

Und in diesen Requirements geht es darum, dass wir einen Wortly-Map-Editor bauen wollen, dass wir die Architektur dafür bauen wollen.

Also es geht jetzt eigentlich nur um die Architektur.

Wenn Claude dann noch Zeit hat und tatsächlich den Code als ersten Proof-of-Concept erstellen möchte, schauen wir mal.

Vielleicht klappt das auch.

So, jetzt hat er sich die Dokumentation gezogen.

Er sagt, super tolles Projekt.

Gibt die Projektziele, den Tech-Stack in den Requirements schon vorgegeben.

Wieder, was für Dokumentation da ist.

## Projektstruktur

Da ist ein Lehrer-Arch-42-Ordner drin.

Ja, jetzt hat er schon verstanden.

Besondere Highlights.

Live-Development-Experiment.

Denn da steht schon drin, dass wir jetzt hier was live machen.

Und jetzt sage ich ihm mal, schau mal bitte auf die Uhr.

Welchen Tag, welche Uhrzeit haben wir?

Und normalerweise hat das System ja eigentlich kein Kalender, keine Uhrzeit.

Ich hätte jetzt erwartet, dass er die BEV benutzt.

Irgendwie hat er anscheinend doch im System-Prompt zumindest das Datum mitbekommen.

Er sagt, er kann nicht die Uhrzeit sehen.

Benutze eines deiner Tools, um die Uhrzeit in Erfahrung zu bringen.

Die Eigenständigkeit von den Modellen ist immer etwas unterschiedlich.

Ah, jetzt versucht er auf das Web zuzugreifen.

Current Time Germany, auch nicht schlecht.

Und diese Eigenständigkeit bedeutet halt, oftmals findet er gleich das richtige Tool.

Manchmal vertut er sich aber.

Und jetzt bin ich mal am gucken, ob er vielleicht doch nicht die Bash hat.

Doch, er hat die Bash.

Jetzt sage ich ihm direkt, nutze doch bitte die Bash.

Bislang hat er das eigentlich immer gemacht, dass er gesagt hat, ach prima, ich kann ja über die Bash den Date-Befehl ausführen.

Und jetzt sagt er 11 Uhr 9 UTC, das heißt kurz nach 13 Uhr bei uns.

Ja, genau.

Er fragt jetzt schon, haben Sie vor, jetzt am Wortly-Map-Editor zu arbeiten oder eine Live-Session zu starten?

Genau richtig.

Du bist schon live im Stream in der Live-Session.

Ich teile dich über den Bildschirm.

So, er sagt ja prima, hallo an alle Zuschauer.

Er versteht also, dass er irgendwo im Live-Stream ist und sagt aktueller Status des Projekts.

Ja, Repository Setup ist komplett.

Anforderungen sind dokumentiert.

### Dokumentation

Doc-Toolchain ist integriert.

Warum habe ich das gemacht?

Ich habe Doc-Toolchain reingesetzt, damit Dokumentation gleich eben auch gerendert werden kann und er somit Diagramme rendern kann.

Ich sehe gerade, ihr bekommt einen 404 auf der Website.

Jetzt gucke ich nochmal gerade rüber, dass die auch, die ist nicht auf Private gestellt.

Ich nehme nochmal den Link und gebe ihn hier nochmal rein.

Schaut mal bitte, ob ihr draufkommt.

Und er fragt jetzt, was wir als nächstes tun können.

Die ARC42-Architekturdokumentation starten, Kapitel für Kapitel aufbauen, ADRs erstellen, Diagramme erstellen, MVP-Implementation planen.

So.

Er fragt mich jetzt, was wäre für euch als Zuschauer am interessantesten?

## Live-Entwicklung

Und dann sage ich ihm jetzt erst mal, ich habe das letzte Mal das Feedback bekommen, dass KI einem ja immer nach dem Mund redet.

Bitte tue das nicht, sondern antworte britisch.

Ich korrigiere mal den Tippfehler, normal ist das kein Problem.

Und dann sage ich, und jetzt lass uns mit der ARC42-Architektur starten.

So und er hat jetzt im Prompt, ach jetzt kommt er erstmal mit seiner Kritik rüber.

Das Projekt ist aktuell noch ziemlich oberflächlich, ja.

Und die Requirements haben vielleicht auch nicht die Qualität, die wir erwartet haben.

Also ein realistisches Projekt.

Probleme, die ich sehe, klare, keine klare Architekturvision, ja, die wollen wir ja jetzt erarbeiten.

Technologieentscheidungen nicht begründet.

Performanceanforderungen fehlen komplett.

Ja, ja, ja.

Okay, er fragt, bevor wir starten, müssen wir ehrlich sein.

Was ist das echte Problem, das wir lösen?

Gibt es nicht schon Wortlimap-Tools?

Was macht unseres besser?

Realistische Einschätzung, eine Stunde für einen funktionsfähigen Editor ist sehr optimistisch.

Okay, schauen wir mal.

Trotzdem wollen wir starten, ja.

Also er hat mich kritisiert, ist gut.

Er hat hier seine Risikoeinschätzung gegeben.

Damit können wir was anfangen.

Und er fängt jetzt an, dass er sagt, okay, wir brauchen Kapitel 1, Einführung und Ziele.

Ich habe ihm so ein bisschen mitgegeben, in welcher Reihenfolge ich an den ARC42-Kapiteln arbeite.

Natürlich müssen wir erst mal das Projekt definieren.

Und dann fragt er, was die Qualitätsziele sind.

Ob er das Template anlegen soll.

Okay, und die Zuschauer sollten sehen, Architektur ist nicht nur schöne Diagramme malen.

Ja, bitte lege das Template im dafür vorgesehenen Ordner an.

Danke für deine Kommentare.

Wir werden sehen, wie weit wir in einer Stunde kommen.

So, er hat jetzt das Master-Dokument angelegt.

Er weiß, wie ARC42 funktioniert.

ARC42 ist ja Open Source und das hat große Vorteile.

Denn dadurch ist es in den Trainingsdaten drin, in dem Merkmalsraum, in dem Weltwissen.

Und ja, er wird jetzt tatsächlich sehr, sehr kritisch, dass er eben jetzt fragt, wofür brauchen wir das?

Aber das werde ich ihm gleich nochmal erklären.

Er macht jetzt ein Create-or-Update-File.

Das heißt, er müsste das jetzt tatsächlich schon hier in Git angelegt haben.

Ich mache mal ein Refresh.

Ich sehe es noch nicht.

Ich frage ihn mal.

Also ich bremse ihn mal ein bisschen aus.

Zu deinen kritischen Fragen.

Du brauchst jetzt nicht überkritisch zu sein.

Ob wir das brauchen?

Es ist ein Demo-Projekt.

Denk dran, du hast selbst die Idee gehabt, den Bordley-Map-Editor zu nehmen.

Dadurch haben wir kein Alleinstellungsmerkmal.

Zumindest gehe ich davon aus.

Lass uns mit der Architektur beginnen.

Ah, jetzt sagt er ja.

Er war zu überkritisch und er korrigiert seine Haltung.

Ja, es ist ein Demo-Projekt.

Ja, es ist Livestream.

Wir wollen zeigen, wie Human-AI-Collaboration funktioniert.

Und wir sollten pragmatisch bleiben statt perfektionistisch.

Das ist doch prima.

Weiter mit der Architektur.

Jetzt bin ich etwas erstaunt.

## Architektur-Dokumentation

Er sagt jetzt Kapitel 2, Randbedingungen.

Das ist jetzt aus meiner Sicht ein guter Feedback-Loop.

Er macht Fehler.

Er sagt jetzt, ich habe eigentlich Kapitel 1 schon gebaut.

Und ich sehe auch hier in der Liste, er hat da was.

Aber er sollte ja mit mir zusammenarbeiten.

Und da hole ich ihn jetzt zurück.

Ich frage ihn, wow, er ist schon bei Kapitel 3.

Warum bist du schon bei Kapitel 3?

Wir wollten doch erst mal Kapitel 1 zusammen erarbeiten.

So, ich lasse ihn da jetzt gerade noch mal weiterlaufen, dass er Kapitel 3 fertig hat.

Er ist jetzt zurückgekommen.

Und das ist jetzt so ein Ding, da unterscheiden sich auch die Modelle.

Ich bin jetzt absichtlich auf Claude Sonnet 4 gegangen.

Und das ist verdammt eigenständig.

Ich habe ja auch noch 3.7 und 3.5 zur Verfügung.

Und die rennen nicht so vorne weg.

Das heißt, ich muss hier Claude 4 ein bisschen ausbremsen.

Und ich hoffe, dass er jetzt eben auch mein Feedback versteht.

Er sagt absolut recht, mein Fehler.

Und er sagt, er hat die Anweisung, dass er schrittweise vorgehen soll, nach jedem Kapitel meine Zustimmung einholen soll und mit mir zusammenarbeiten soll, nicht alleine alles durcharbeiten.

Das ist tatsächlich im Prompt vorgegeben, mit dem ich ihn vorbereitet habe.

Aber er nimmt sich halt die Freiheit raus, eigenständig zu entscheiden und zu sagen, ach komm, das haben wir ja alles in den Requirements.

Ich schreibe einfach das Kapitel 1 runter.

So.

Dann fragt er jetzt, ob die Qualitätsziele so okay sind.

Fehlen wichtige Stakeholder?

Ist die Aufgabenstellung richtig formuliert?

Was sollen wir ändern, bevor wir zu Kapitel 2 gehen?

Dann sage ich, stelle mir doch bitte erst mal Kapitel 1 vor.

Ich gebe dir dann Feedback.

Also im Idealfall hätte er erst mal gesagt, okay, was ist die Aufgabenstellung?

Dann hätte ich gesagt, ja, du hast das Requirements Dokument.

Da hast du wahrscheinlich schon einiges rausgelesen.

Er ist jetzt halt vorgeprescht und sagt, naja, ich habe hier das Requirements Dokument gesehen. haben wollte, wesentliche Features, visuelle Map-Erstellung mit Drag-and-Drop, Positionierung auf der Evolution-Value-Achse, Abhängigkeiten zwischen Komponenten, DrawIO, XML-Export, Browser-basiert mit Local Storage, Qualitätsziele, Top 3, Usability, Performance und Compatibilität.

Da würde ich jetzt gleich mal einhaken und sagen, die Qualitätsziele passen nicht zu unserer Session.

Das Wichtigste ist momentan, dass wir das als Demo innerhalb einer Stunde präsentieren können.

Mal gucken, was er daraus macht.

Also ihr seht, ich habe jetzt kein wirkliches Qualitätsziel definiert, sondern ich habe einfach mal so umgangssprachlich was gesagt.

Und er sagt jetzt, Qualitätsziel Demo-Fähigkeit, Szenario, Messbarkeit, funktionierender Prototyp, präsentierbar in einer Stunde Livestream.

Gut, das können wir jetzt messen.

22 Minuten sind schon vergangen.

Finde ich eigentlich ganz gut.

Verständlichkeit, Zuschauer können den Architekturansatz nachvollziehen.

Auch das finde ich jetzt ganz gut angepasst.

Lernwert, Demonstration von Human-AI-Collaboration in der Architektur.

Ja, ich glaube, da können wir einiges ableiten.

Es ist jetzt sicher nicht optimal, aber es ist hier auf diese Situation angepasst.

Die ursprünglichen Ziele, 10 Minuten Einarbeitung für Neuling, 100 Komponenten, die Performance, wenn 100 Komponenten auf dem Screen sind, sagt er, waren klassische Über-Engineering-Fallen für ein Demo-Projekt.

Interessant ist halt, dass auch wenn ich eben mit den ersten Qualitätszielen nicht übereingestimmt habe, es war etwas, wo ich darauf eingehen konnte.

Ich hatte nicht die leere Seite, ich konnte darauf eingehen und konnte ihn korrigieren.

Weitere Anpassungen für Kapitel 1, Fokus auf MVP, realistische Erwartungen, Stream-Kontext, Bildungsziel steht im Vordergrund.

Ja, überarbeite Kapitel 1 und pushe das Ganze dann schon mal.

Und ihr werdet jetzt sehen, dass ich jetzt nicht das Kapitel 1 perfekt mache.

Aber was ihr hier auch seht, ist der Canvas-Modus auf der rechten Seite, der mir eben zeigt, was arbeitet er an dem Dokument.

Wir haben jetzt hier schon die Version 3 von diesem Kapitel 1.

Ich kann da hin und her springen.

Ich sehe, was er hier schreibt.

Ich sehe es noch nicht als ASCII-Doc gerendert, aber ASCII-Doc ist ja so, dass man es lesen kann.

Die Placeholder, ich lasse sie mal drinnen.

Und nein, mit echten Wordly-Map-Nutzern außer mir habe ich nicht gesprochen.

Wir entwickeln ins Blaue hinein.

Hast du einen Link auf das gepushte File?

Er sagt, er hat das jetzt geupdatet.

Er hat das Ganze gepusht.

Jetzt frage ich ihn, wo ist denn hier bitte der Link?

Ich öffne den Link.

Und siehe da, er hat diesmal keinen Fork angelegt.

Er ist direkt in den Main-Branch reingegangen.

Ist für mich okay.

Ich habe ihm da keine Anweisungen gegeben gehabt.

Das ist auch der Vorteil.

Ich habe es jetzt hier als ASCII-Doc gerendert.

Ich gehe mal gerade in den System Scope und Kontext.

Da hat er nämlich vorhin schon ein Diagramm reingesetzt.

Ich wechsle mal auf den KI-User, weil dann sehe ich hier in den Settings auch die Pages.

Und kann euch die URL auf die Pages hier in den Chat reingeben.

Und jetzt kann ich hier auf ARC42 gehen und habe die Kontextabgrenzung und sehe das Diagramm gerendert.

Sehr gut, so wollte ich es haben.

So kann ich jetzt weiterarbeiten.

Er guckt sich die Zeit an, 11.24 Uhr.

Er fragt, ob er das im Browser öffnen soll.

Nein, das habe ich schon gemacht.

Lass uns mit Kapitel 2 weitermachen.

So, er sagt, okay, dann machen wir die Randbedingungen.

### ARC42 Struktur

Browser-Support, moderne Browser.

Ja, wir wollen nicht abwärtskompatibel sein.

Kleinzeit-Only, keine Server-Komponenten.

Moderne JavaScript-Features, DrawIO-Kompatibilität.

Entwicklungszeit, eine Stunde Livestream, ja.

Open Source, MIT-License, das passt für mich.

Worldly-Map-Constraints, das hätte ich jetzt hier erstmal draußen gelassen.

Ich lasse es hier mal drin.

Jetzt frage ich ihm, also er fragt, ob die Randbedingungen richtig sind.

Wir sollten ein paar Entscheidungen begründen.

Mal gucken, wie er das jetzt aufnimmt.

Er sagt, ja, Begründungen sind entscheidend.

Welche Entscheidungen wollen wir konkret begründen?

Er fragt hier die JavaScript statt Framework oder Canvas versus SVG für Rendering.

Kleinzeit-Only, Browser-Support, DrawIO-Export statt eigenem Format.

Ich sage jetzt mal, wir nehmen, oder ich sage ihm, die meisten Entscheidungen sind durch den kurzen Slots begründet.

Kein Backend zum Beispiel, weil wir nicht die Zeit haben, einen Server zu starten.

Er sagt, perfekt, das ist die wichtigste Begründung.

Zeit, Budget, eine Stunde, Livestream.

Lassen Sie mich Kapitel 2 überarbeiten.

Ob ich ihm sagen soll, dass er mich duzen kann?

So hatten wir das in den Requirements.

In den Requirements habe ich eigentlich noch keine Architekturentscheidung.

Aber so hatten wir das gesagt, dass wir es möglichst einfach haben wollen.

Er schreibt jetzt hier in die Randbedingungen von Begründungen rein.

Das heißt, er nutzt jetzt diese Randbedingungen für Begründungen.

Das ist okay, wenn wir keine Alternative haben.

Ansonsten würde ich es eigentlich als Architekturentscheidung aufnehmen.

Ich lasse das jetzt mal so und schaue mal, welche Architekturentscheidungen er nachher noch sieht.

Er fragt, sind noch ein paar Entscheidungen offen?

Die restlichen Entscheidungen sollten wir als ADRs zum gegebenen Zeitpunkt dokumentieren.

Bitte pushe deine Änderungen.

Er sagt absolut richtig, ADRs sind für die spezifischen technischen Entscheidungen der saubere Weg.

Er pusht jetzt das File.

Es sollte also gleich im Repository auftauchen.

Und ihr seht, das, was ich bislang irgendwie als Demo hatte, das hat sich auch so unter Zeitdruck entwickelt, dass ich oftmals gesagt habe, du denkst dir Qualitätskriterien aus.

Aber ich empfinde es als total nützlich, dass ich hier einen Sparings Partner habe, mit dem ich zusammenarbeiten kann und zusammen das Ganze entwickeln kann.

Kapitel 2 hat er gepusht.

Begründungen für alle Entscheidungen.

Eigentlich Randbedingungen.

Zeitbudget als zentraler Treiber.

Verweis auf zukünftige ADRs für technische Details.

Status nach 20 Minuten.

Kapitel 1, Kapitel 2 ist fertig.

Und er fragt, ob er jetzt mit Kapitel 3 weitermachen soll.

Ja, lass uns Kapitel 3 erarbeiten.

So, und diese drei Kapitel sind für mich essentiell.

Quasi ein Contract, was überhaupt in der Architektur erarbeitet werden soll.

Und die Kontextabgrenzung.

Er soll jetzt hier ein C4-Kontext-Diagramm erstellen.

Er hat als Akteure den Map Creator, den User, DrawIO und den Webbrowser identifiziert.

Wir haben kein Login oder sowas.

Das passt also einigermaßen.

Kommunikation, User erstellt Maps, Editor exportiert XML.

Daraus entsteht ein DrawIO.

Ah, DrawIO kann das importieren.

Genau.

Technischer Kontext, Single Page Application, Local Storage, File System, Canvas.

Externe Schnittstellen, DrawIO, XML-Format, Local Storage, JSON-Format.

Meine Fragen an Sie.

Fehlen wichtige externe Systeme?

Das ist jetzt natürlich immer so ein Ding.

Man hat jetzt was Vorgefertigtes.

Das ist so 80, 90 Prozent.

Und man sagt dann ganz gerne.

Ach, ich habe jetzt keine Lust darüber nachzudenken.

Das mache ich jetzt hier auch aufgrund der Zeit.

Ich sage also 1.

Passt so die externen Systeme.

Die Kontextabgrenzung richtig.

Das müsste ich mir angucken.

Muss ich mir gleich ansehen, wenn du es gepusht hast, damit ich das Diagramm gerendert sehe.

Import-Funktionalität.

Nein, kein Import.

Und Local Storage sollte reichen.

Bitte anpassen und pushen.

So, er hat jetzt hier als technische Schnittstellen.

Oder gehen wir noch mal ein bisschen weiter hoch.

Er baut ein Kontext-Diagramm für den fachlichen Kontext.

Er hat die Kommunikationspartner Input-Output für den User-Mouse-Keyboard-Interaktion.

Also eigentlich ganz detailliert beschrieben.

Das sieht eigentlich ganz gut aus.

Und das ist jetzt so ein Punkt, man muss immer überlegen, mit was man vergleicht.

Vergleich mit der idealen, perfekten Architektur.

Der Vergleich mit dem, was ich sonst in Projekten vorfinde, was für mich gut genug ist.

Und gerade weil das jetzt hier so ein Spielzeit-Projekt ist, ist da für mich einiges gut genug.

Er sagt, das Kapitel ist angepasst und gepusht.

Wichtige Anpassungen.

Kein Import wurde entfernt.

Klare Abgrenzung, was das System nicht macht.

Local Storage Download Only.

Er hat jetzt aus dem Kontext gelernt, ich möchte einen Link haben.

Er hat mir den Link gegeben zu dem fertigen Dokument.

Dann gucke ich mal drauf.

Er hat mir jetzt den Link rein in das GitHub-Projekt gegeben, weil er jetzt den Link von dem Doctoolchain-Projekt anscheinend nicht kennt.

Ich könnte ihn darauf hinweisen.

Doctoolchain braucht jetzt noch einen Moment, um das Ganze zu bauen.

Da können wir dann gleich nochmal drauf gucken, ob das Diagramm so passt.

Er hat tatsächlich den fachlichen Kontext und den technischen Kontext, so wie es eigentlich sein soll, unterschiedlich dargestellt.

Mir gefallen eigentlich diese beiden Diagramme.

Sie geben einen einfachen Überblick.

Es ist natürlich jetzt ein super einfaches System, aber er hat zum Beispiel an sowas wie eine Legende gedacht.

Er hat jetzt nicht einfach nur PlantML genommen, sondern er hat es als C4-Diagramm gerendert.

Er hat auch an die externen Schnittstellen gedacht.

Er hat hier die Schnittstelle für den DrawIO-Export als XML ausgegeben.

Das finde ich eigentlich schon ziemlich cool.

Auch sein LocalStorage gibt ein Datenformat, ein Beispiel an.

Das finde ich klasse.

Ihr habt vielleicht in dem Repository gesehen, es gibt da noch eine weitere Datei.

Jetzt gehe ich nochmal rüber.

Wo haben wir es?

Unter Docs müsste es liegen.

Ein DrawIO-Implementation-Guide.

Das fand ich sehr spannend, weil als ich das Ganze vorbereitet habe und mal einen Testdurchlauf gemacht habe, hat er gesagt, das XML-Format sagt mir jetzt nichts, da müsste ich mal recherchieren.

Dann habe ich gesagt, ja, dann recherchiere doch mal.

Daraus ist dieser Format-Implementation-Guide entstanden, wo er über 512 Webseiten analysiert hat.

Dafür hat er 8 Minuten 20 Sekunden gebraucht, wo ich gesagt habe, die Zeit will ich euch jetzt hier nicht warten lassen.

Da hat er dann tatsächlich einiges herausgefunden, wie das hier mit der XML-Struktur von DrawIO funktioniert, wie er da Shapes anlegen kann und, und, und, und, und.

Das fand ich spannend und das habe ich jetzt, um Zeit zu sparen, ihm einfach hier reingelegt.

Jetzt gucke ich mal, jetzt erwarte ich eigentlich, wenn ich das neu lade, dass dann die Diagramme leicht angepasst sind.

Ihr habt es vielleicht besser im Kopf.

Ich denke, das ist jetzt die aktuelle Version.

Der Map-Creator, er ist blau, ich würde ihn eigentlich grau darstellen, weil ich habe den User nicht unter Kontrolle, eigentlich nur meinen Editor habe ich unter Kontrolle.

Das kann ich ihm jetzt natürlich nochmal mitgeben und er würde es entsprechend abändern.

So, und jetzt sagt er, sollen wir zu Kapitel 4 Lösungsstrategie?

Dort entscheiden wir die konkreten Technologien, Canvas versus SVG oder wollen Sie was anderes machen?

Er sagt mir jetzt schon 35 Minuten verbleibend, da liegt er etwas falsch, aber okay, wir haben ja jetzt auch viel Zeit verschwätzt.

Ja, bitte, Kapitel 4.

Die Lösungsstrategie.

Mal gucken, was er vorschlägt.

Und meine Vorgehensweise ist, dass ich mir eine Skizze für die Lösungsstrategie mache und dazu muss ich Entscheidungen treffen.

Und das sagt er auch, die wichtigsten Entscheidungen, die wir treffen müssen, Rendering-Technologie, Canvas oder SVG.

Datenmodell, die Wordlist, Map, Drucktur, Architektur, Pattern, MVC oder Component basiert oder einfache Event-Händler.

Okay, dann würde ich sagen, lass uns mit der Rendering-Technologie beginnen.

Was ist dein Vorschlag?

Er hat ja schon gesagt, Canvas oder SVG.

Ich lasse ihn das einfach nochmal wiederholen.

## Technische Entscheidungen

Er sagt, SVG wäre besser.

### Interaktion mit Claude

Er versucht es zu begründen.

Pro SVG einfach das Event-Handling, schnellere Implementation, weniger Code-for-Drag-and-Drop, Debugging, Skalierung, Koordinaten.

Dagegen spricht Performance-Limits und Rendering-Overhead bei Animationen.

Wo er sagt, das eine Performance ist für Demo irrelevant und der Rendering-Overhead bei Animationen, die wir nicht brauchen.

Okay, das passt.

Er sagt, SVG ist eindeutig die richtige Wahl für unser Zeitbudget.

Canvas würde bedeuten, manuelles Hit-Testing für Maus-Events, Redraw-Logik.

Erwarte ist, dass er mir, ah er geht jetzt in Sequential Thinking.

Klasse.

Das ist ein Tool, was ich ihm mitgegeben habe.

Ich kenne es erst seit dieser Woche, ein MCP und der ist spannend, weil der, ich kann es jetzt hier leider nicht wirklich anzeigen, das ist ein Tool, was ihn quasi eine Checkliste erstellen lässt und diese Checkliste kann baumförmig aufgebaut werden und damit überlegt er halt, was könnte der User jetzt gemeint haben, wie gegenüberstellen und solche Geschichten und jetzt hat er mir hier tatsächlich eine Entscheidungsmatrix abgeliefert und hat hier verschiedene Kriterien für die Entscheidung, die beiden Optionen gegenübergestellt und dann eben entsprechend bewertet.

Ich lasse das jetzt einfach mal so stehen, aber das ist jetzt ein guter Ansatz, wo ich eben in die einzelnen Punkte reingehen kann, gucken kann, sehe ich das ähnlich, mir vom Modell erklären lassen, warum bewertet das Modell dies und jenes in folgender Art und Weise und dann würde ich sagen, okay, das passt so für mich, bitte arbeite den ADR aus und pushe ihn.

So, ganz nett, er hat jetzt als Autoren mich und sich als AI Assistant genannt, sagt schon Status Final, hat das Datum eingesetzt, das ist ja auch alles ganz prima.

Er beschreibt das Problem, dass wir eine Rendering-Technologie brauchen.

Er zeigt das Ganze in einer Pue-Matrix an, die werden wir uns gleich noch mal auf GitHub ansehen.

Er begründet, warum Canvas nicht gewählt worden ist. Übrigens, er schreibt jetzt alles in Englisch, weil ich ihm das gesagt habe, dass ich meine Dokumentation gerne auf Englisch haben möchte und er beschreibt dann die Entscheidung, dass wir SVG benutzen und warum.

Positive Effekte, Risiken und technische Schulden.

Performance ist ein Risiko, wenn wir zu viel auf der Map haben.

Animationen können wir nicht so gut machen.

Technische Schulden, Future Scalability, okay und Advanced Graphics sehe ich jetzt nicht als technische Schulden an und das sage ich ihm jetzt auch.

Die technischen Schulden sehe ich nicht, da wir diese Dinge gar nicht implementieren wollten.

Also Advanced Graphics, wenn wir es gar nicht umsetzen wollen, dann brauchen wir es auch nicht als technische Schuld irgendwie festzuhalten.

Er sagt absolut richtig, Denkfehler von ihm.

Er redet mir wieder ein bisschen nach dem Mund, aber es passt ja, solange ich beim richtigen Ergebnis rauskomme.

Technische Schulden entstehen nur, wenn wir bewusst Abkürzungen nehmen, wenn wir Quick and Dirty implementieren, wir Features weglassen, die wir eigentlich brauchen.

Da hat er vollkommen recht.

Ja, bitte korrigieren.

Er sagt jetzt auch noch, das ist ein wichtiger Punkt für die Zuschauer.

Nicht jede Limitation ist eine Schuld.

Und dann sage ich ihm, bitte trage die Risiken und Schulden auch immer gleich in das Template ein.

Für mich sind die Entscheidungen eine sehr gute Quelle für Risiken und technische Schulden und deswegen, wenn ich diese Entscheidungen treffe, also ihr seht es, Lösungsstrategie, da merke ich, was brauche ich, was für Entscheidungen muss ich treffen und dann überlege ich mir, welche Risiken entstehen aus diesen Entscheidungen, die ich getroffen habe und trage das dann entsprechend in das Kapitel ein.

Er gibt hier gleich noch Implementation Notes ab, das heißt, wie die SVG Struktur für die Worldly Maps aussehen könnten, wie das Event Handling aussehen könnte.

Ja, ist vielleicht ganz nett.

Muss vielleicht nicht direkt an der Stelle sein, sondern vielleicht in einem anderen Dokument.

Ich finde es aber jetzt hier für so ein kleines Projekt ganz gut.

### ADR Dokumentation

So, er hat den ADR korrigiert.

Er hat das Ganze gepusht.

Er sagt, Scope Entscheidungen sind legitime Architekturentscheidungen und ich sage mal, ja, er soll die, kannst du bitte die anderen ADRs selbst entscheiden und dokumentieren.

So, jetzt darf er mal eigenständig arbeiten.

Ist ja ein Demo.

Ich gehe mal zurück.

Guck mal, was er jetzt hier schon angelegt hat.

Er hat hier den ADR angelegt.

Er hat hier das diesmal als Pew Matrix angelegt.

Das heißt, er hat hier eine der Entscheidungen als Baseline genommen.

Die bewertet er mit Null für jedes Kriterium und dann die Alternativen entsprechend Plus 1, Minus 1.

Dann geht es leichter, wenn man gegen eine Baseline geht, um zu entscheiden, ist es jetzt dieses Kriterium mit SVG besser oder schlechter umzusetzen.

So bewertet er dann SVG mit Plus 5.

Das ist ganz gut und das ist jetzt auch so ein Vorteil, dass wenn ich irgendwie später sage, ja, da gibt es ja noch eine weitere Alternative.

Vor 20 Jahren hätte ich gesagt ein Applet, ja, und dann kann ich das einfach hier daneben stellen, habe schon meine Kriterien und könnte es einfach nochmal bewerten.

So, er hat jetzt schon ADR 2 und ADR 3 hier dokumentiert.

Die Data Persistence Strategy und die Architecture Pattern Selection.

Ihr seht vielleicht, dass er hier in den Überschriften die Lösung vorweg nimmt.

Ich habe ihm gesagt, er soll erst mal sich die Problemstellung angucken, mit mir erarbeiten, dann kann er den Titel daraus generieren.

Ich fange nicht mit dem Titel an, ich fange mit der Problemstellung an und dann habe ich ihm gesagt, wenn wir eine Entscheidung getroffen haben, dann kannst du den Titel hintendran mit der Entscheidung ergänzen, weil wenn ich dann über die ADR Titel einfach drüber lese, dann erkenne ich schon, okay, was ist entschieden worden und kann, muss nicht in die Details reingehen, kann das einfach skippen.

So, das ist doch schon ganz prima.

## Projektabschluss

Jetzt sagt er Architektur Dokumentation komplett.

Wir haben die Ziele, wir haben die Randbedingungen, wir haben die Kontextabgrenzung, wir haben die Lösungsstrategie.

Sollten wir die ADRs nicht im ARC43 Template referenzieren und was ist mit den anderen Kapiteln?

Er sagt jetzt halt, naja, diese vier Kapitel reichen ihm eigentlich.

Er baut jetzt noch Kapitel 9, die Architekturentscheidungen auf, wo er die ADRs entsprechend inkludiert und sagt jetzt, ja, eigentlich, und das ist jetzt hier ein wirklicher Kritikpunkt, den ich habe, Kapitel 10.

Ich habe ihm eigentlich gesagt, er soll mit den Qualitätsanforderungen anfangen, denn ansonsten können wir keine Entscheidungen treffen.

Er hat jetzt wahrscheinlich gesagt, naja, wir haben ja die drei Hauptqualitätsanforderungen, das wäre eigentlich was gewesen, da hätte ich besser darauf achten müssen.

Kapitel 11 hat er auch nicht angelegt, obwohl er es eigentlich hätte tun sollen und die Bausteinsicht hat er jetzt auch rausgelassen.

Er fragt jetzt, soll er Kapitel 9 machen?

Ja, Kapitel 9 hast du doch eben erstellt.

Pushe es.

Kapitel 11 sollten wir die Risiken und technischen Schulden aus den ADRs gesammelt haben.

Ich sehe gerade hier die Frage, ob Claude kontinuierlich in das Git-Repo pusht.

Ja, Claude arbeitet direkt auf dem Git-Repo.

Claude hat eigentlich hier auch eine virtuelle Umgebung, in der er arbeiten könnte und dann später bei der Umsetzung testgetrieben arbeiten könnte.

Das macht er jetzt nicht.

Es ist Architekturdokumentation.

Er braucht sie nicht zu überprüfen.

Er geht direkt auf das Repository.

Ich gucke mal auf die Uhr.

Wir haben nur noch sieben Minuten und jetzt frage ich ihn mal, warum hast du Kapitel 10 übersprungen?

Okay, er sagt, wir haben eigentlich keine technischen Schulden.

Ist auch ehrlich, braucht man sich nichts aus den Fingern zu saugen.

Was sagt er auf meinen Hinweis auf die sieben Minuten?

Okay, er sagt nur noch sieben Minuten Zeit für Ultrafokus auf MVP, Strategie Anpassung, keine drei Phasen mehr.

Eine Phase, absolutes Minimum für Demo.

Wir werden das Demo jetzt rauslassen.

Ihr könnt es selbst ausprobieren, ob ihr mit Claude Code zum Beispiel diese Dokumentation reingeben könnt und tatsächlich Code rausbekommt.

Ich werde es im Nachgang auch nochmal machen und in das Repository reingeben, dass ihr euch dann ansehen könnt, was das Ergebnis ist.

Er sagt jetzt, guter Punkt, ich habe Kapitel 10 Qualitätsanforderungen übersprungen.

Das war ein Fehler.

Kapitel 10 ist wichtig, weil dort die Qualitätsziele aus Kapitel 1 detailliert ausgearbeitet werden sollten.

Er redet sich jetzt also nicht daraus, dass er doch eigentlich drei Qualitätskriterien hatte.

Er hat es jetzt erstellt.

Nicht mehr hier im Canvas, sondern direkt auf GitHub.

Er sagt an die Zuschauer, so geht systematische Architekturdokumentation von Zielen über Entscheidung bis zu messbaren Qualitätsanforderungen.

Da lobt er sich selbst.

Lass uns die ARK 42 Dokumentation finalisieren.

Wir verzichten auf den Code.

Ja, Michael, du hast recht.

Nur unter Druck entstehen Diamanten.

Auf Diamanten kann man keinen weiteren Druck ausüben.

Auch den Spruch gibt es.

Mal gucken, wie weit er jetzt noch kommt.

Ich gehe mal rüber.

Guck mal an, was er jetzt hier gemacht hat.

Ich gehe mal gleich hier in die Dokumentation.

Das ist ein bisschen nachlaufend immer wegen dem Rendering.

Er hat jetzt hier die ADRs nicht drauf geachtet.

Er hat sie einfach in den Folder gelegt.

Deswegen werden die hier noch mal unsauber dargestellt.

Obwohl sie jetzt hier in Kapitel 9 noch mal drin sein sollten.

Ja, hier sind die ADRs.

Sie sind jetzt aufgrund der Schriftgröße.

Ich kann es mal ein bisschen kleiner machen.

Ist ein bisschen besser formatiert.

Da habe ich die ADRs.

Prima.

Lösungsstrategie passt.

Aber jetzt wollte ich mal nach den Qualitätsanforderungen gucken.

Er hat einen Qualitätsbaum erstellt.

Wow, das ist doch mal was.

Verständlichkeit, Demofähigkeit, Lernwert.

Das finde ich nicht schlecht, dass er daran gedacht hat und eben auch seine Möglichkeiten nutzt, dass er weiß, er hat plant um zur Verfügung in Askidog.

Er kann hier den Qualitätsbaum als Mindmap aufbauen.

Super.

Hier Bewertungsszenarien.

Ihm ist es nicht geglückt, hier eine Liste richtig darzustellen.

Da hat er immer mal wieder Probleme mit der Askidog-Syntax.

Die Qualitätskriterien, man müsste sie wirklich noch mal mit ihm genauer durchgehen, damit das, was er sich jetzt ausgedacht hat, nicht einfach irgendwie Quatsch ist, sondern man es mit ihm zusammen erarbeitet hat.

Ihr merkt, er versucht, den Anweisungen zu folgen.

Er schafft es nicht immer.

Das heißt, man muss eben immer noch mal drüber gucken.

Aber eigentlich kriegt er auch in seinem Prompt dann so eine Anweisung mit.

Du hast die Qualitätsanforderungen und bei jeder Entscheidung guckt noch mal drüber, ob das eben entsprechend passt.

Risiken und technisch Schulden hat er auch aufgebaut.

Er hat es sogar mit den ADRs als Quelle verlinkt.

Er hat die Auswirkungen hier bewertet.

Niedrig, akzeptabel.

Das finde ich eigentlich prima.

Das sind alles Sachen, wo ich jetzt, wenn ich mehr Zeit hätte, mit ihm noch mal detailliert reingehen würde, um das mit ihm zu diskutieren.

Und ihr seht, ich habe hier einfach einen Sparings-Partner, mit dem ich zusammenarbeiten kann.

Jemand, der ständig zur Verfügung steht.

### Zusammenfassung

So, er sagt, die ARC42-Dokumentation ist vollständig.

Alle zwölf ARC42-Kapitel sind erstellt.

Vier ADRs, vollständige Integration der ADRs in das Template.

Risiken, technisch, Schulden, Qualitätsszenarien, Bausteinsicht.

Die hatte ich mir jetzt gar nicht angeguckt.

Die haben wir hier.

Ja, hat er was gebaut.

Ist eine Grundlage, auf der man sicherlich arbeiten kann.

Er hat jetzt hier das Whitebox-Gesamtsystem.

Danach geht er in die Ebene 1.

Da hätte er jetzt natürlich noch C4 nehmen können.

Wobei, das würde ich jetzt eigentlich sagen, das sind schon Klassen.

Da fehlt mir eine Ebene dazwischen, würde ich jetzt mal so spontan sagen.

Event-Händler hat er was.

Also ihr seht, da kann man noch darüber diskutieren.

Glossar hat er mittlerweile auch erstellt.

Das ist jetzt so ein Ding, das fand ich ganz interessant, weil wenn man Claude fragt, welches ist das unwichtigste Kapitel, dann sagt er, das Glossar, weil er kennt die technischen Begriffe.

Gernot Starke hat daraufhin gesagt, dann hat er das Glossar eigentlich falsch verstanden.

Da sollen nicht die üblichen technischen Begriffe rein, sondern da sollen die Fachbegriffe rein.

Also das, was der Leser eben noch nicht kennt.

Wir haben jetzt hier eine Architektur erstellt.

Wir haben daraus gelernt und wir können jetzt den Prompt für das LLM verbessern, dass wir ihm zum Beispiel Hinweise für das Glossar geben, was da reinkommen soll.

So, ich sehe, ich habe schon eine Minute überzogen.

Ich danke euch für eure Aufmerksamkeit.

Bitte denkt nochmal daran, auf unserer Website software-architektur.tv könnt ihr uns Feedback geben für unsere Website.

Und jetzt bin ich gespannt drauf.

Ich werde alle eure Kommentare lesen.

Ich werde sie alle kommentieren.

Ich freue mich drauf, vor allem britische Kommentare.

Lasst sie ruhig raus.

Ich will sie hören, weil ich habe ein bisschen die rosa-rote Brille auf.

Und ich werde als nächstes jetzt dann offline ihn bitten, das Ganze mit Cloud Code, nicht Cloud Desktop, das Ganze zu implementieren, Test-Driven und werde das in das gleiche Repository stellen, dass ihr dann nächste Woche mal reingucken könnt und mal ausprobieren könnt, was ist denn aus diesem Wordly Map Editor geworden.

Herzlichen Dank für eure Aufmerksamkeit.

Ich freue mich auf euer Feedback und schönes Wochenende.
