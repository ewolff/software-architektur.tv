# Folge 248 - Code Charta mit Richard Gross Hallo, ich bin Eberhard Wolff.

Freitags mache ich oder Lisa Moritz einen Live-Stream zum Thema Software-Architektur, oft zusammen mit Gästen.

Dieser Podcast ist das Audio des Streams.

Weitere Folgen, Sketchnotes und vieles mehr findet ihr unter software-architektur.tv.

## Einführung und Vorstellung

So, dann herzlich willkommen zu einer weiteren Episode von Software-Architektur im Stream, diesmal mit Richard.

Schön, dass es geklappt hat und schön, dass du da bist.

Ja, ich freue mich total.

Genau.

Und bevor wir sozusagen inhaltlich losgehen, so ein paar Announcements.

Also, wir sprechen heute über CodeCarter.

Das ist ein Werkzeug zum Thema Architekturmanagement.

Wir haben vor langer Zeit, also vor ein paar Jahren, irgendwie ganz viele Episoden gemacht zu anderen Werkzeugen in dem Bereich.

Ich verlinke die nochmal.

Und der andere Hinweis ist, es gibt eine Ankonferenz zu Software-Architektur und KI.

Das heißt, wir treffen uns und sprechen über das Thema Software-Architektur und eben den Einfluss von KI oder wie KI das unterstützen kann.

Da gibt es, das ist am 17.02., meine ich, und zwar von 14 bis 18 Uhr.

Und da gibt es eine Möglichkeit, sich zu registrieren.

Das ist ein Zoom-Meeting und den Link findet ihr entweder hier im Chat, wenn ihr live dabei seid, oder sonst in den Shownotes.

Genau, ist natürlich kostenlos und so weiter.

Das sozusagen als kleiner Werbevorspann.

Und jetzt nochmal herzlich willkommen, Richard.

Willst du kurz zwei Worte über dich sagen, was du so machst und was so dein Hintergrund ist?

Ja, gern.

Ich bin Richard Groß.

### Hintergrund von Richard Gross

Ich bin jetzt seit zwölf Jahren bei Maiba und Wolf als IT-Archäologe angestellt.

Das heißt, ich mag Legacy-Code.

Spezifisch, ich mag es, Legacy-Code wieder flott zu machen.

Deswegen durchsetze ich mich auch sehr für das Thema hexagonale Architekturen.

Die lassen sich sehr gut mit Legacy-Code kombinieren.

Hypermedia, Test-DSL und halt klar ausdrucksstarke Modellierung von Code.

Das gefällt mir auch am meisten.

Und ich glaube, das Wichtigste für diese Runde ist, ich habe halt lange Zeit das Open-Source-Projekt begleitet, namens CodeCarter.

Und das hilft halt auch Non-Techies, aber Techies gleichermaßen, ein Gefühl für die Qualität von Software zu geben.

Ich werde gleich noch eine Präsentation dazu geben, aber das ist, glaube ich, der Hauptgrund, warum ich hier bin.

Genau.

Und die erste Frage, die ich mir so stellen würde, oder die ich dir gerne stellen würde, ist, warum habt ihr denn mit CodeCarter angefangen?

### Motivation für CodeCarter

Ja, wir hatten 2014 angefangen, so Health-Checks, Software-Health-Checks zu machen.

Ich sehe gerade, der Daniel hat gesagt, sein Vorgesetzter hat mal gesagt, wir sind nicht als Archäologen angestellt.

Ja, das stimmt.

Archäologe ist kein Selbstzweck.

Aber es geht ja darum, wenn man Legacy-Code hat, dann ist es halt Software, die Mehrwert hat.

Ansonsten wäre sie ja irgendwie gelöscht worden.

Und ich sehe den Begriff des Archäologen so, dass wir uns halt damit beschäftigen, wie schaffen wir halt wieder, dass dieser Code Optionen hat.

Oder besser gesagt, dass das Business-Optionen hat.

Weil wenn wir Legacy-Code haben, dann ist halt immer das Problem, okay, irgendwie hat der Mehrwert, weil ansonsten wäre er gelöscht worden.

Aber gleichzeitig, da sollen auch wieder neue Features rein und da ist dann irgendwie so ein Innovationsstau entstanden.

Deswegen, ich finde Archäologen, die sind nicht da, weil sie es toll finden, in alten Code einzusteigen, sondern die sind da, weil sie es toll finden, Business wieder zu enablen und wieder Optionen zu schaffen, die vorher nicht da waren.

Genau, super.

Und ich habe mein Turmproblem auch behoben.

Also ProTip, YouTube-Studio nicht gleichzeitig aufhören mit streamen.

Hast du schon die Frage, haben wir schon diskutiert oder hast du schon gesagt, wie die Lizenz aussieht von dem Projekt und wie Maiba und Wolf da drin involviert ist?

Ich habe tatsächlich pausiert mit meiner Vorstellung und habe einfach gerade auf einen Kommentar im Chat geantwortet.

Ich spule es mal gleich vor.

## Projektdetails und Lizenzierung

Also wir hatten das Problem, wir machen diese Health-Checks und da kriegt man halt eine Million Zeilen Code und die Frage, okay, was ist überhaupt das Problem und wie komme ich da raus?

Und das wollen wir innerhalb von drei Wochen beantworten.

Und da hatten wir gute Tools und irgendwann haben wir gesagt, okay, es macht total Sinn, wenn wir unsere eigene schreiben, weil eines unserer Kernkompetenzen sind diese Health-Checks.

### Open Source und Lizenz

Und das haben wir dann online gestellt, 2017 glaube ich war es, unter einer BSD3-Lizenz.

Also sprich, jeder darf die nutzen.

Das Einzige, was BSD3 und MIT unterscheidet, ich bin kein Anwalt und habe das länger nicht mal angeguckt, aber in aller Kürze, BSD3 ist ohne Werbung.

Also ihr dürft dann halt nicht großartig damit werben.

Bei MIT wäre es feuerfrei.

Macht, was ihr wollt.

Am Ende des Tages ist es allerdings trotzdem komplett kostenlos.

Jeder darf das halt nutzen.

Gut, super.

Du wolltest eine Live-Demo machen und eine kurze Präsentation.

Dann würde ich sagen, ist das der nächste Schritt?

Genau, dann starte ich mal die Präse.

## Visualisierungskonzept

Wenn man halt so ein Millionen Zeilen oder 100.000, ist eigentlich egal, wenn man sehr viel Zeilencode vor sich hat.

Dann fühlt sich das für mich immer so auf.

Man hat ganz viel Code und man ist halt irgendwie dort gerade.

Und das ist halt auch der Scope, den man hat.

Man ist relativ klein, fokussiert auf dieser eine Datei.

Und dann irgendwann später kommt man halt an eine andere Stelle und stellt fest, okay, hier war ein Problem und das wusste ich gar nicht.

Und man sieht halt den Wald vor lauter Bäumen nicht, weil man halt immer sehr klein und nur an einer Stelle halt eben arbeitet.

Und mein Gefühl ist zumindest, wenn man dann halt Legacy-Code vor sich hat, dann bietet einem sowas wie Sonar bietet einem dann auch nicht so den perfekten Überblick, weil man dann halt viel zu viele Bugs, viel zu viele Issues und viel zu viele Smiles hat und man fragt sich eigentlich, okay, wo soll ich überhaupt anfangen?

Und ich glaube, das ist halt ein reines Problem der Perspektive.

Wenn man halt diesen Schritt zurückgehen könnte und man geht halt auf so einen Berg drauf und kann von da auf die Software draufgucken, dann kann man sich ein Bild machen, dann kann man halt diese Perspektive haben und auch um folgreich Probleme zu erkennen.

Und ich habe dieses Bild jetzt mit Dolly gezeichnet, aber die Idee oder die Metapher ist da schon drin.

### Stadtmetapher

Nämlich, dass wir halt jede Datei als so ein Gebäude, als so ein Hochhaus zeichnen.

Und das Schöne ist, wenn ich jede Datei in meiner Code-Basis als Gebäude mache, dann habe ich halt eine Grundfläche von so einem Gebäude, eine Höhe vom Gebäude und eine Farbe, also sprich drei Metriken.

Und jetzt kann ich auf diese drei Attribute und auf diese drei Attribute kann ich jeweils eine Metrik legen.

Dann wird meine Karte, je größer die Datei ist, desto mehr Platz nimmt sie auf der Karte ein.

Komplexität, also zyklomatische, wäre dann zum Beispiel die Höhe.

Könnte aber auch Nesting-Level sein, das bietet sich auch an.

Und dann halt eben Churn, also wie oft es verändert wird, wäre dann halt die Farbe.

Und das Coole ist dann, dass es dann halt wirklich so eine Stadtkarte ergibt, wo ich dann halt eine Datei habe oder pro Datei ein Gebäude.

Und dann wird mir auch diese Ordner angezeigt und je nachdem, wie tief die Ordnerverschachtelung ist, geht es halt immer höher und höher.

Und das gibt mir dann halt total so eine Perspektive von oben drauf.

Und irgendwie werden dann Probleme halt sehr angenehm und sehr klar und sehr offensichtlich.

Im Detail ist es dann so, man hat dann halt eben hier rote Gebäude und da muss man dann als Mensch nochmal reingucken.

Also diese roten Gebäude sind der Start deiner Unterhaltung, nicht das Ende von der Unterhaltung.

Und das Coole ist, diese Ansicht kann ich jetzt ja als Architekt, als Developer oder was auch immer nutzen, um halt Probleme zu identifizieren.

Aber ich kann halt auch mit dieser Ansicht kommunizieren mit meinem Stakeholder, mit meinem Peer.

Und ich kann sagen, guckt mal, ihr wollt, dass wir ein Feature hier rechts oben einbauen.

Wir haben da folgende Probleme, dann ist da vielleicht nicht nur ein Gebäude, sondern ganz viele, die rot sind.

Und dann ist das irgendwie sehr plastisch.

Und ich kann sogar noch viel plastischer sein.

Warum sind denn die Gebäude rot, wenn ich fragen darf?

Also das wäre, also das rote Gebäude symbolisiert hier, also die Größe, die Grundfläche ist hier Lines of Code.

Die Höhe ist die Zyklomatisch-Komplexität und die Farbe ist Churn.

Also sprich, es wird sehr oft geändert.

Okay, das heißt, also ich sehe jetzt hier drei, vier Gebäude, glaube ich, die halt unterschiedlich groß sind.

So groß sind die gar nicht im Vergleich zu den anderen, so mittlere Größe, würde ich sagen.

Und das da hinten ist das höchste, also das ist das, was am meisten geändert wird.

Ja, also die Höhe bedeutet, dass es komplex, also sehr komplex ist.

Es hat die meiste Komplexität.

Ja, stimmt.

Und bei der Farbe gibt es jetzt hier keine Abstufung.

Ich könnte so den Gradienten-Modus anmachen, dann wäre es ein bisschen, aber meistens reicht es einfach zu wissen, okay, das Ding ist rot, gelb oder grün halt.

Und wird deswegen, also das rote Gebäude wird halt häufig geändert.

Das heißt, hinten haben wir ein Gebäude mit hoher Komplexität und einer, ja, wie auch immer gearteten Größe, so mittelgroß.

Und das wäre jetzt etwas, wo man sagen könnte, okay, ist das ein Problem, weil eben das ein komplexes Gebäude ist, was halt häufig geändert wird oder ein komplexer Teil, der häufig geändert wird.

Genau.

Und ich hatte ja, vorhin hatte ich ja zum Beispiel so Sonar-Metriken angesprochen, die kann man jetzt zum Beispiel auch auf die Farbe oder auf die Höhe legen.

Und dann kann ich halt unterschiedliche Metriken miteinander korrelieren und dann kann ich sagen, okay, das Ding ist sehr komplex und hat auch sehr viel Codesmells, okay, da sollte ich vielleicht mal reingehen.

Oder es ist sehr komplex, hat sehr viel Codesmells und es wird an und an geändert, okay, das ist teuer.

Und wenn ich will, kann ich das halt auch, ja, 3D drucken.

Das klingt wie eine Spielerei, aber es ist tatsächlich überraschend gut, damit greifbar zu machen für Leute, wie ihre Software halt aussieht.

Und es ist ein Gimmick, das irgendwie sehr beliebt ist und ich kann das total nachvollziehen.

Genau, und du hattest, ich glaube, du hattest mir das gegeben, nicht?

Das ist irgendwie so ein 3D gedrucktes Demo-Gebäude-Ding, wo man halt irgendwie die, so ein paar kleine Dinge sozusagen sieht.

Genau.

Genau.

Sehr schön.

Und jetzt kann ich halt auch hingehen und zum Beispiel halt Sprintrends.

Sorry, da ist eine Frage im, also es sind zwei Bemerkungen.

Also einmal steht da, erinnert mich an Commercial Tool.

Toll, dass es eine Alternative gibt.

Das stimmt.

Es gibt, es gab auch mal früher, also es gibt dieses Commercial Tool, aber es gibt halt auch dieses Code Cities, nicht?

Ich glaube, das ist irgendwie noch älter.

Ja, also wir hatten mal eine Recherche gemacht, ich kann mich an die Details nicht erinnern.

Also das, also was 100% stimmt und das will ich auch gar nicht überspielen, ist, wir machen da in Anführungsstrichen nichts Neues.

Diese Stadtmetapher, dieses Code Cities oder Evo Street oder sowas, es gibt da wirklich sehr schöne Forschungspapiere dazu.

Mein Gefühl ist halt, die enden dann halt immer dort.

Also die gehen halt hin, machen eine coole Forschungsarbeit, bauen halt irgendwie ein Tool für einen Beispielfall und danach ist dann halt zu Ende und es wird nicht weiterentwickelt.

Ja, genau.

Ich hatte irgendwann mal eine Recherche gemacht.

Ich glaube, das Ding hieß wirklich Code Cities.

Also ich habe es nur mal irgendwie durch das Web geguckt und festgestellt, es gibt halt das Werkzeug, aber es ist irgendwie nicht besonders benutzbar und dann war es das halt irgendwie.

Und also positiv wäre jetzt die Aussage, das ist halt ein etabliertes Konzept, wo man nachweisen kann, dass es gut funktioniert.

Genau.

Und die andere, so dazu noch, weil sonst ist ja noch eine andere Frage.

Ja, also wenn ihr durch Zufall mal über Serene zum Beispiel gestolpert seid, das wäre so das gängige Tool, das auch so eine 3D-Visualisierung anbietet.

Ansonsten in Sonar und Independent und solchen Tools ist meistens halt so eine 2D-Tree-Map von oben.

Also da hat man dann keine Höhe drin.

Genau.

Serene ist genau das andere Werkzeug, was da einfährt.

Ich glaube, das sind wir auch das, was der MD42Martin da irgendwie anspricht.

Und dann hat der N2000 heißt es, glaube ich, noch gefragt, Schörn High meint, die Anzahl der Änderungen liegt über einem Threshold.

Ja.

Genau.

Gut.

Dann haben wir das, glaube ich, soweit geklärt.

Dann können wir, glaube ich, weitermachen mit deiner Präsentation.

Genau.

Ich bemühe mich aber, das schnell abzuschließen.

Kein Stress.

Damit wir schnell in die Live-Demo kommen.

Nur kurz hier noch, jetzt kann ich halt diese Karten, jeden Sprint, die zu zeigen macht keinen Sinn.

Das ist vielleicht beim Projekt, das sehr schnell wächst, gerade noch irgendwie spannend, aber meistens ist es eher so ein, ich mache das zu bestimmten Milestones.

Aber das Schöne ist, gerade halt bei, also nicht nur bei grünen Wieseprojekten, wo man halt so Milestones zeigt und sagt, daran haben wir gearbeitet, kann man das halt bei Legacy-Projekten machen und man kann halt sagen, okay, am Anfang sah das so aus.

Also hier ist jetzt die Farbe Kraut-Coverage und man sieht halt, wie es im Laufe der Zeit, wenn die Gebäude halt immer kleiner, schmaler, flacher und halt die Coverage wirklich signifikant.

Grün anstatt Rot.

Genau, also es wird grüner als Rot, sieht man ja auch noch als der dritte Parameter.

Genau.

So, wie kann man das nutzen?

Also erstens, frei, kostenlos, open source, das heißt auf GitHub verfügbar.

## Technische Implementierung

Was wir anbieten, ist eine Analyse-Plattform, so eine kleine.

Und wir machen das so, wir teilen CodeCarter in zwei Hälften.

### Analyse-Komponenten

Es gibt den Analyse-Teil auf der linken Seite und den Visualisierungsteil auf der rechten Seite.

Kommunizieren tun die beiden über so ein Dateiformat namens cc.json, also CodeCarter.json.

Und man braucht im Prinzip immer irgendwie jemand, der einen Code hat, braucht man irgendwie einen Code-Parser.

Da kommt der Datei raus, dann kann man auch einen zweiten Parser haben, der guckt sich jetzt zum Beispiel Git-Metrik an, zieht dort auch eine Datei raus.

Und die mergt man dann zusammen.

Und jetzt kann man halt Metrik miteinander eben korrelieren und vergleichen.

Man kann dann sagen, okay, wie hoch ist meine Churn, wie hoch ist meine Komplexität.

Und deswegen ist es immer irgendwie, vorne ist halt ein Parser für unterschiedliche Quellen und die kann ich dann zusammen mergen.

Muss ich nicht, aber man kann sie zusammen mergen.

Dann nimmt man die Datei und dann visualisiert man sie.

Also alles, was ich euch bisher gezeigt habe, war der Visualisierungsteil.

Jetzt gucken wir mal kurz auf die Analyse.

Was wir nämlich insgesamt anbieten, ist halt für rein Java, haben wir den Source-Code-Parser gebaut.

Der war immer gedacht, dass der mehr parsen soll.

Ich kann Ausblick machen, das kommt jetzt auch noch, aber für unsere Zwecke hat sich meistens angeboten, Sonar zu nutzen.

Das kann von Haus aus, kann Sonar, glaube ich, 28 Sprachen.

Dann gibt es noch Community-Plugins, die man noch reinladen kann oder halt eine kostenpflichtige Sonar-Version, dann kannst du noch mehr sparen.

Dann kannst du auch Kobol und solche Sachen.

Und wir bieten halt ein Tool an, den Sonar-Importer.

Der kann halt aus Sonar die Metriken extrahieren.

Also sprich, wenn ihr einen Sonar habt, könnt ihr Codecard einsetzen.

Wenn ihr keinen Sonar habt, könnt ihr entweder den Sonar-Importer einsetzen.

Wenn ihr keinen Sonar habt, könnt ihr entweder den Source-Code-Parser nehmen.

Ihr braucht halt noch ein bisschen Liebe auf unserer Seite, aber vielleicht ist ja jemand da, der einen Pull-Request stellen will und den aufpeppen möchte.

Wer weiß.

Ihr kriegt gleich auch den Git-Log-Parser.

Es gibt noch einen SVN-Parser, aber in de facto, glaube ich, braucht den niemand mehr.

Und es gibt halt den CSV-Importer.

Und der CSV-Importer ist insofern spannend, weil damit kann ich jetzt beliebige Sachen visualisieren.

Weil am Ende ist ja ein Gebäude einfach nur ein Dateipfad und ein paar Metriken.

Und jetzt kann ich zum Beispiel als Gebäude auch Testfälle haben und Ausführungszeit von Metriken.

Oder ich kann die Personen Deutschlands visualisieren.

Okay, das wäre jetzt datenschutzrechtlich schwierig, oder vielleicht die Züge von Deutschland.

Dadurch, dass es sehr generisch ist, was Codekarte macht.

Es gibt einfach ein Gebäude und das hat Metriken.

Dadurch kann ich halt auch mit dem CSV-Importer halt alles Mögliche irgendwie visualisieren.

Weil solange es eine CSV ist in dem richtigen Format, kann man die halt umwandeln in eine CC-JSON.

Das heißt, wenn aus irgendeinem Grund ihr keinen Sonar einsetzen dürft oder die Sprache, die ihr habt, nicht von Sonar unterstützt wird, kann man immer überlegen, ob man vielleicht seinen eigenen Importer baut, der entweder eine CSV ausspuckt oder halt selber direkt eine CC-JSON ausspuckt.

Und das macht es halt super flexibel.

Wir nennen das auch eine Pipes-and-Filters-Architektur.

Genau.

Also ich glaube, in dem Kontext gibt es jetzt verschiedene Sachen, die sich vielleicht als Fragen anbieten.

Sonst müsste es mich sozusagen stoppen.

Die eine Sache ist die Frage, die halt übers Formular vorher schon vorgestern, glaube ich, reingekommen ist und anonym ist.

Da hat ja die Person geschrieben, witzig, das Tool habe ich erst diese Woche entdeckt, konnte es aber noch nicht im Detail ansehen.

Und da steht Codekarte unterstützt bisher ja nur Java.

So wie ich es verstehe, heißt Unterstützung insbesondere, dass die Codekarte Shell die Ausgaben eines QA-Tools versteht und in CC.JSON übersetzen kann, beziehungsweise ein QA-Tool bereits CC.JSON erzeugt.

Habt ihr praktische Erfahrung, wie aufwendig es ist, Codekarte für andere Sprachen, in meinem Fall PHP, zu nutzen?

Die QA-Tools im PHP-Bereich haben ja häufig auch ein Ausgabeformat für die Nutzung in typischen Standard-QA-Tools.

Also dann wahrscheinlich Sonar nehme ich auch an, dass es mit dazu gehört.

Oder muss ich dann für Zigmetrigen eine entsprechende Konvertierung schreiben, mit der Codekarte umgehen kann?

Ja, also die Kurzform ist, wenn du PHP hast und Sonar, bist du fertig.

Sonar kann ja nicht nur Codemetriken erfassen, sondern die können ja auch zum Beispiel Coverage einlesen, wenn es in dem JUnit-Format ist zum Beispiel.

Gib mir mal eine Sekunde.

So, pusten, sehr schön.

Können auch pro Tipp immer etwas zu trinken dabei haben.

Ich war letztens in Vilnius auf der Bilsdorf, da hatte ich so einen Hustanfall drei Minuten lang.

Ich glaube mittlerweile, dass es so wie sich das Lampenfieber bei mir äußert.

Wer weiß.

Ich hatte mal den Effekt, dass mir tatsächlich die Stimme während der Präsentation weggeblieben ist.

Das ist noch ein Stück interessanter.

Aber ja.

Ja, das ist auch schön.

Genau.

Also die Frage, du hattest halt gesagt, PHP, Sonar, dann ist man halt im Prinzip fertig.

Das wäre also eine Alternative.

Noch was zu diesem PHP-Thema?

Also es gibt immer die Möglichkeit, sich einen eigenen Importer zu schreiben.

Das ist halt die Frage, wie präzise der sein muss.

Man kommt ziemlich weit mit einem stupiden Rack-Expressions-Ansatz.

Weil was ist Komplexität?

Komplexität ist eine Verzweigung im Kontrollschluss.

Also, Entschuldigung, mehr keine Komplexität.

Vielleicht grundsätzlich noch mal zwei Worte dazu, warum ich diese Episode spannend fand und warum ich das wichtig fand.

Ich glaube tatsächlich, dass diese Visualisierung in so Code-Cities eine ganz spannende Sache ist und zur Kommunikation total viele Vorteile hat.

Mir sind Fälle bewusst, wo das eben auch tatsächlich ein bisschen ins Management dazu geführt hat, dass Dinge transparent werden und es klar wird, wie Dinge sich ändern.

Ich finde die Metapher spannend.

Das ist ja so ein Bereich, in dem wir ganz viel machen müssen.

Wir haben immer dieses Problem mit dem Technical Debt und uns als technischen Menschen ist klar, da gibt es irgendwelche Probleme.

Das ist etwas, was wir transportieren müssen in andere Rollen hinein.

Das, was Richard vorhin gezeigt hatte, diese Geschichte mit nicht, ist eine Stadt.

Da sind große Gebäude und die sind alle rot.

Die werden klein und dann wird es grün.

Das ist eine ganz hervorragende Möglichkeit, zu sagen, es wird tatsächlich besser.

Wir haben investiert und es wird besser.

Das kann man jedem klar anschaulich machen.

Das ist eine von diesen Geschichten, die scheinbar einfach sind, aber in Wirklichkeit wertvoll.

Man kann nicht sagen, das ist nur eine weitere Visualisierung, aber das ist gerade total wichtig, weil wir Dinge kommunizieren müssen.

Dafür ist das genau eine geeignete Sache.

Ich wäre mir auch nicht bewusst, dass es eine große Alternative ist.

Was ich heute gelernt habe, ist, dass es da offensichtlich auch Forschung zu gibt.

Das ist dann nochmal extra spannend.

Aber auf jeden Fall finde ich, es ist eine super Sache und es passt auch gut ergänzend zu den anderen Werkzeugen, die wir so haben, die wir uns bisher im Stream angeschaut haben.

Die da, glaube ich, gar nicht so stark auf Visualisierung an Wert liegen.

Vielen Dank fürs Übernehmen.

Sehr gerne.

Also, wenn ihr eine Codebasis vor euch habt, ich mache mal mit der Live-Demo weiter.

Was ihr braucht, ist typischerweise irgendeine Form von Node.

Warum?

Die Visualisierung ist zwar in Node, wir liefern allerdings den Analyse-Teil, der in Kotlin geschrieben ist, liefern wir in npm auf.

Das heißt, npm install globally-codecard-analysis.

Dann kriegt man etwas Schönes, was sich da schimpft, CodeCarter-Shell.

Und da sind jetzt diese ganzen Parser drin, die wir alle haben.

Ihr seht, noch ein paar mehr, als ich in der PowerPoint drin hatte, weil das sehr überfrachtig gewesen wäre.

Und wenn ich jetzt keinen Sonar habe und eh keinen Zugriff auf Code, dann kann ich jederzeit ganz simpel starten.

Ich kann so Tools wie Toki einsetzen.

Die zählen einfach die Lines of Code.

Dann kommt raus, Java hat jetzt 471 Java-Teile, 45.000 Lines.

Davon sind Code 31.000.

Also sprich, Kommentare sind der Rest oder leere Zeilen.

Und Toki kann das für liebevolle Sprachen.

Im Endeffekt ist es dann nur Lines of Code, aber das ist ja wenigstens ein Startpunkt.

Das heißt, eine Möglichkeit für diesen PHP-Fall wäre, genau dieses Werkzeug jetzt zu benutzen.

Genau.

Das ist natürlich nicht optimal, weil irgendwie ist das schön mit CodeCarter, dass ich mehr Metrik miteinander kombinieren kann.

Aber so ist es halt manchmal.

Manchmal hat man nicht das Perfekte.

Das Schöne ist, Toki hat auch einen JSON-Export.

Und dann kann ich das in so ein JSON-Format reinprügeln.

Und jetzt kann ich auf CodeCarter-Seite den Toki-Importer nehmen und das dann halt auch wieder in unser gzippedes-tc-json-Format reinpacken.

Das heißt, da sind die beiden Dateien.

Am Ende des Tages.

Damit kann man überstarten.

Das heißt, ich habe jetzt die Größe der einzelnen Teile und du hast diese JSON-Code-Coverage auch mit diesem Toki ermittelt.

Richtig?

Es ist leider wirklich nur Lines of Code.

Also JUnit ist unser Beispiel und das sind jetzt die Lines of Code.

Ich kann jetzt halt auch lokal SonarCube laden.

Es gibt die Community-Edition von SonarCube.

Kann man sich runterladen.

Die ist auch kostenlos.

Und dann kann man halt eine Analyse hier machen.

Man kann halt JUnit 4 da reinpacken.

Und entsprechend wäre das dann.

Gucken, wie heißt das Ding nochmal?

Also, ich gucke mal kurz in die Datei rein.

Das ist ja nicht viel.

Man braucht diesen Sonar-Scanner.

Man braucht einen lokal laufenden SonarCube.

Und dann kann ich da halt eben mit Sonar-Scannen lokal starten.

Wenn ich den will.

Muss ich nicht.

Aber wenn Sonar in meiner Umgebung nicht läuft, aus welchem Grunde, ich kann es immer lokal ausprobieren.

Einfach nur, um zu sagen, hey, guck mal, Business wäre es nicht total cool, wenn wir Sonar hätten.

Oder was weiß ich, Kodana gibt es ja auch.

Wenn ihr IntelliJ nutzt, kennt ihr vielleicht Kodana.

Das ist deren Analyse-Plattform.

Hat natürlich nochmal ganz andere Features, weil IntelliJ sind sehr gut, was Mieträgen betrifft und intelligente Lösungen.

Dann kann ich den Sonar-Scanner nutzen.

Dann landet das hier drin.

Irgendwelche Open Issues.

Null Coverage.

Das liegt aber daran, dass ich es nicht konfiguriert habe.

Wäre ein bisschen komisch, wenn ein JUnit-Tool keine Coverage hätte.

Und danach kann ich den Sonar-Import machen.

Ich verbinde mich auf meinen Local-Host.

Ich sage, welches Projekt ich ziehen will.

Ich gebe meinen User-Token mit.

Und am Ende habe ich dann aus Sonar alle Mieträgen rausgezogen.

Das könnte man jetzt mit PHP-Analog machen, nicht?

Das heißt, ich würde da mit einem PHP-Projekt genauso vorgehen.

Das ist eine Frage, die mir vorhin angekommen ist.

Du hast ja jetzt den Java-Parser nicht benutzt, oder?

Genau, ich habe den Java-Parser nicht benutzt.

Also der Source-Code-Parser.

Was würde der denn noch bringen?

Der macht die Einstiegshöhe halt geringer.

Ich muss keinen Sonar aufsetzen.

Wenn ich schon einen Sonar habe, dann ist es egal.

Was also bedeutet, dass die Aussage, die dieser Mensch ja getroffen hat, CodeCutter unterstützt bisher nur Java.

Das ist sozusagen die Halbwahrheit, weil eigentlich ist deine Demo ja basiert auf Sonar und diesem Tokey.

Was also bedeutet, dass es mit jeder anderen Programming-Sprache genauso funktionieren würde, die von Sonar unterstützt wird und von dem Tokey unterstützt wird?

Genau.

Es gibt so ein paar Sachen, die bei Sonar besonders sind.

Die Community Edition von Sonar kann, glaube ich, kein C++.

Es gibt ein Community-Plugin für C++, aber das ist dann halt nicht in der Community Edition drin, sondern das müsst ihr dann halt reinladen.

Ansonsten C++ ist, glaube ich, ein Premium-Feature.

Aber PHP ist, glaube ich, in dem Standard-28-Programmiersprachen-Kader drin.

Oder, glaube ich, ich habe gestern nachgeguckt, das war drin.

Wollen wir noch kurz...

Es sind ein paar Fragen aus dem Chat.

Ich weiß nicht, ob wir die jetzt klären wollen oder ob du erstmal mit deinem...

Ja, warum denn nicht?

Wir machen es doch jetzt.

Genau.

Der MD42Martin bei Twitch hat gefragt, gibt es zum CSFV-Import-Beispiele?

Wäre schön, eine Grafik auf drei Sternchen zu haben.

Ich würde vermuten, dass damit die Homepage gemeint ist.

Wir können ja mal kurz in die Docs reingucken.

Da ist der CSV-Exporter, da ist der CSV-Importer.

Ja, ich finde es ehrlich gesagt ein bisschen...

Also die Grafik, die ein CSV-Export auswirft, wird hier genauso aussehen wie alle anderen Grafiken auch.

Deswegen frage ich mich, was da zu erwarten ist, was irgendwie anders aussieht.

Das bedeutet ja nur, dass ich eine offene Schnittstelle habe über klassische Mechanismen, wie wir sie in der IT kennen.

Ich glaube, es ging dem Fragesteller darum zu sehen, wie würde denn so ein Import aussehen.

Also da stehen dann halt die Metriken drin.

Und hier oben drüber stehen dann halt, naja, welche Metrik ist das denn eigentlich.

Okay, das heißt in der ersten Seite steht da drin, Path Name, Type, Airlock Functions.

Und dann hast du halt mit drunter stehen irgendeinen Namen von irgendetwas.

Und dann sagst du, stehen da halt irgendwie die Werte drin, Komma getrennt.

Und dann hat der nächste Datenpunkt mit dem entsprechenden Namen und den Werten und so weiter und so weiter.

Genau.

Also alles kein Hexenwerk oder so.

Das Wichtige des halben Mechanismus ist, diese ganzen Sachen sind jetzt halt beliebig.

Also da muss nicht Airlock stehen.

Da kann jetzt Metrik 5 sein oder MyMetric oder was auch immer.

Und deswegen kann ich dann halt auch unterschiedliche Sachen visualisieren.

Genau.

Und da ist dann so ein bisschen die nächste Frage von dem, die 42 Martin, der so fragt.

Habt ihr auch die Erlebung, damit auch ein Bildmonitor zu bauen?

Größe, Zeit, Anzahl, Changes.

Ja, ich weiß nicht, was er damit meint.

Größe, Zeit.

Ich glaube, er meint damit, dass man halt irgendwie das Wert trippelt.

Dass ich halt sage, ich habe die Größe einer Datei, die Zeit, die es halt braucht, um es zu bauen.

Und die Anzahl der Changes, die da drin sind.

Sowas halt irgendwie grafisch darzustellen.

Ich bin mir auch gerade nicht sicher, was man sozusagen aus denen daraus ermitteln kann.

Aber wie soll ich sagen?

Die Idee, dass man das halt nicht nur so klassisch Code Metering nimmt, kann ich mir schon vorstellen.

Ihr habt ja auch den Git-Import, der hat Änderungen importiert.

Genau, der importiert halt Anzahl der Autoren oder wie oft wurde es in letzter Zeit verändert, solche Geschichten.

Er hat gerade gesagt, auf eine Pipeline angewandt.

Also kann man, glaube ich, alles machen.

Ich glaube nur, ihr habt es halt in dem klassischen Modell noch nicht genutzt, nehme ich mal an.

Nö, aus meiner Sicht ist es halt übertrieben, da täglich reinzugucken.

Außer man will halt wirklich irgendeinen Fortschritt explizit überwachen, ist es jeden Tag reinzugucken viel zu viel.

Ich würde mal sagen, einmal pro Monat ist immer eine ganz gute Periode, bis man am Monatsanfang oder zum Sprint, zu jedem zweiten Sprint oder sowas.

Ja, also ich habe das Gefühl, ich weiß nicht, wie du es siehst, aber ich denke, das Werkzeug gibt es halt hier.

Also man kann ja beliebige Daten anzeigen, auch die Daten, die sozusagen von der Bildkomplexität her kommen.

Und ich finde die Idee gar nicht schlecht, zu sagen, es interessiert mich vielleicht nicht nur Architektur, sondern auch solche Sachen.

Denn gerade so etwas wie Bild ist ja durchaus eine wichtige Eigenschaft von Code.

Von daher finde ich eigentlich die Frage und die Idee, die da mitschwirbt, irgendwie ganz gut.

Ich habe das tatsächlich mal für Performance-Tests angewandt.

Dann hatte ich halt so einen Testlauf und der hat halt so und so viele Sachen abgefrühstückt.

Und dann wollte ich halt einen Delta haben.

Ich wollte halt wissen, okay, Performance-Test diese Woche sah so aus, letzte Woche sah der so aus.

Und dann konnte ich wirklich pro Testlauf gucken, okay, ist der besser, schlechter oder ist es grob im Mittel besser geworden.

Und das war halt, dafür fand ich es halt ganz spannend.

Weil wenn man halt irgendwie so 1000 Datenpunkte hat oder so und die halt gleichzeitig visualisieren und einen Delta haben will, dann bietet sich das halt einfach wirklich an.

Der Daniel C.

Oderbolz bei YouTube hat gefragt oder hat halt bemerkt, die Frage ist halt, ob sich Qualität auf drei Werte melden lässt. Ähm, nee.

Es ist immer eine Kombination.

Also, ich starte mal kurz Codekarte.

Genau, vielleicht kurz dazu sozusagen aus meiner Perspektive.

Ich habe diese Episode gemacht zum Thema, kann man eigentlich am mittleren Produktivität messen.

Und ich glaube, eine wichtige Aussage der Episode war halt, wenn ich irgendwas mit Metrigen mache, muss ich mir halt überlegen, was ich eigentlich untersuchen will.

Und das, was du jetzt irgendwie darstellst als prototypisches Beispiel, ist ja genau diese Geschichte mit, okay, ich will halt irgendwie herausfinden, ist mein Code änderbar?

Und diese Qualität kann ich ja anhand von Metrigen versuchen, dem halt irgendwie sozusagen hinterherzulaufen.

Und wir haben, glaube ich, gerade eben auch diskutiert, indirekt, dass es eben andere Qualitäten gibt.

Du hast ja zum Beispiel über Performance gesprochen.

Das ist ja eine andere Qualität, die man damit irgendwie auch visualisieren kann.

Das bedeutet, je nachdem, welche drei Werte ich wähle, kriege ich unterschiedliche Aussagen über unterschiedliche Qualitäten, wäre mein Gefühl.

Genau, also ich habe jetzt mal Codekarte gestartet, um das mal kurz zu zeigen.

Also man kann sich das lokal installieren, wenn man will.

Ist einfach lokal installiert, dann habe ich es immer und kann ich auch bestimmen, welcher Version es ist.

Ich kann aber genauso gut auch auf der Codekarte Homepage hingehen.

Und halt hier dieses Webstudio halt anklicken.

Wenn ich das Webstudio anklicke, ist 1.1 das Gleiche.

Da seid ihr halt darauf angewiesen, welche Version wir halt gerade online haben.

Kein funktionstechnischer Unterschied, aber inhaltlich.

Und da habe ich auch gleich ein Demo-Projekt, so scheint es nicht.

Genau, das hier ist Codekarte in Codekarte.

Ah cool.

In Codekarte sieht es sehr grün aus.

Ja, fast hätten wir es auch angelegt.

Also, ihr seht den Dateipfad immer hier oben, falls es euch interessiert.

Also wenn ich hier irgendwo drüberfahre, dann steht da oben jetzt Datamox, wo das ganze Ding drin liegt.

## Praktische Anwendung

So, die ursprüngliche Frage war ja, kann ich Qualität aus drei Werten heruntermappen?

Und ich behaupte nein.

### Metriken und Korrelation

Ich behaupte, was ich mit Codekarte mache, ist, ich nehme diese Metriken und die sind eine Indikation.

Und ich kombiniere mindestens drei miteinander.

Aber ich kann ja auch sagen, zum Beispiel dieser CodeMapMouseEventsService hier, der hat halt 390 Lines of Code, 92 McCabe-Komplexität und 14 CodeSmurfs.

Und jetzt ist halt für mich die spannende Frage, okay, wird der zum Beispiel oft geändert?

Oder, was weiß ich, wie viele Autoren habe ich?

Und dann, oder wobei, das hätte ich auch hier unten nachgucken können.

Welcher war das?

CodeMap, da.

Ich hätte ja auch hier unten auf, wo ist er? Äh.

Genau, wir sehen glaube ich gerade irgendwie 10, 20 Metriken oder so, die irgendwie diese Datei hat.

Genau.

Und jetzt habe ich halt dieses komplexe Gebäude hier gefunden mit einer hohen Anzahl an Authors.

Fragt mich jetzt nicht, warum der einfach jetzt gerade gar keine Authors anzeigt.

Hört mal die Seite neu.

So.

Jetzt wieder was an.

Ah, ich glaube, das ist ein Fehler in der Datei drin.

Moment.

Wir laden mal.

So.

So, jetzt kommt das da.

Die klicken wir jetzt mal weg.

Also, jetzt nochmal.

Die muss ich jetzt auch mal disablen.

Sorry.

Okay.

Boss Event Service, there we go.

Und jetzt haben wir auch wieder eine ordentliche Anzahl von Authors.

Also, ich glaube, es ist halt sinnvoll, wenn man halt irgendein Gebäude gefunden hat und sich halt fragt, okay, ist das jetzt schlimm, dass man halt Metriken miteinander korreliert.

Aus Sicht von so einer Komplexität war der jetzt halt irgendwie spannend, aber gleichzeitig hat der halt auch eine ganz solide Anzahl an Authors.

Der hat nämlich 20 Autoren.

Also, sprich, es gibt genug Leute, die sich darin auskennen.

Und das ist, glaube ich, halt das Wichtige, dass man halt nicht sagt, oh, ich habe zwei Metriken und die sagen, das ist schlimm, sondern ich korreliere mehrere davon.

Und am Ende mache ich dann sowas wie hier zum Beispiel doppelt draufklicken.

Und dann kann ich halt in dem Fall so einer Cloud, kann ich dann halt den Deep Dive machen.

Ich finde in Code Carter irgendwas und dann mache ich den Deep Dive, springe hier rein und sage mal, okay, ist hier wirklich irgendwas großartig Schlimmes?

Und dann scrolle ich halt so drüber und schaue mir diesen Code halt an.

Hier wäre vielleicht irgendwas, was man ordentlich refactoren könnte, weil das schon ein langes If-Statement ist.

Und dann dadurch finde ich halt Punkte, wo ich sagen kann, okay, da sollten wir nochmal hingehen oder das sollten wir überarbeiten.

Oder wir sagen halt, okay, warte mal, aufgrund der Metriken sah es irgendwie schlimm aus, aber in der Realität ist es gar nicht so schlimm.

Also ich glaube, es ist halt nur ein Ich-Finde-Startpunkt, um eine Diskussion zu haben.

Damit hast du, glaube ich, zwei wichtige Sachen gesagt.

Also die eine Sache ist eben Informationsreduktion.

Also wir haben ein großes Stück Software und da können wir eben nicht alles sehen.

Das hattest du ja auch gesagt, nicht?

Also 100.000 Zahlen vom Code.

Und das andere ist, glaube ich, auch total wichtig.

Du hast gesagt, wir haben eine Diskussion.

Das Ergebnis kann sein, das ist halt fein.

Und von daher passt es halt.

Da ist noch eine Frage, wo ich ehrlich gesagt, also die ist, glaube ich, einmal übers Formular gekommen, aber jetzt auch nochmal im Chat von dem Daniel C.

Uderbolz, wo ich auch ehrlich gesagt gespannt bin, wie es die Antwort ist.

Habt ihr dieses Tool auch schon genutzt, um Customizations an Standardsoftware zu ändern?

Die sehen zum Beispiel ServiceNow.

Also ServiceNow ist offensichtlich eine Standardsoftware.

Also man könnte es bestimmt dafür nutzen.

Ich nicht.

In was bitte?

Gott, in was macht man Customization ServiceNow?

Ist das rumiersprachenunabhängig?

Ich weiß es gar nicht.

Ich kann es dir, glaube ich, auch gerade nicht sagen.

Oder nutzen die ABAP?

Also würde bestimmt Sinn machen.

Im Regelfall analysiere ich halt Individualsoftware und nicht irgendwie Customizations oder so.

Ja, im Chat meinte...

Ja, JavaScript steht da.

Ja.

Und damit ist man ja im normalen Umfang.

Also JavaScript ist ja dann etwas ganz Normales.

Ich zeige nochmal kurz was.

Also wie ihr seht, es gibt halt viele Buttons.

Also ich kann immer meine Metriken auswählen.

Number of authors, 18 weeks oder sowas.

Ich kann immer hier anpassen, was sind die Ranges, die ich sehen will.

Dann habe ich auch hier so ein Histogramm und sehe halt, okay, der Großteil, der Number of authors, ist halt irgendwie relativ weit hier unten.

Und dann gibt es am Ende diesen Longtail mit Sachen, die halt schon so lange dabei sind, bis sie immer noch verändert werden.

Ist übrigens auch so eine spannende Frage, warum Sachen immer noch so viel...

Also warum Sachen überhaupt 60 Autoren bekommen haben.

Das könnten wir jetzt irgendwie...

Das können wir jetzt natürlich noch größer hinausstellen.

Mal gucken.

Das ist eigentlich eine spannende Sache, nicht?

Das bedeutet, es gibt irgendwie...

Eine niedrige Anzahl Authors kann schlecht sein, aber auch eine hohe Anzahl Authors kann irgendwie komisch sein.

Ja, okay, gut.

Ja, Datamox macht Sinn.

Datamox gewinnt immer, weil alle Mox da reingeschoben werden, egal was man tut.

Man sieht auch, das Ding ist super flach.

Einfach alle Mox da drin.

Aber keine Logik.

Das würde jetzt bedeuten, dieses Gebäude hat zwar eine große Grundfläche und ist irgendwie rot, aber wir ignorieren es halt und es ist halt fein.

Genau.

Vielleicht auch nicht.

Das ist ja schon eine relevante Frage.

Warum sollen denn alle Mox da drin sein?

Wie modelliert man da denn nicht die Übersichtlichkeit?

Weil das Ding hier ist jetzt...

Da oben seht ihr es.

Wenn ich jetzt drüber habere, hat das einfach mal 2.700 real lines of code.

Also real in dem Fall heißt ohne Kommentare und Leerzeilen.

Aber das wäre jetzt eigentlich die Frage.

Wie kommst du jetzt zu einer Entscheidung, ob du halt dieses Problem als Problem erkennst, was du tatsächlich fixen willst?

Was machst du denn jetzt?

Ja, da sind wir jetzt leider in dem It depends.

Ich glaube, dieses Datamox im explizit ist einfach nur eins.

Man muss das mal mit dem Team diskutieren.

Und dann entscheiden sie sich, hey, ne, hast recht, wir wollen das mal aufsplitten.

Oder sie entscheiden sich, ach ne, das ist eigentlich super, ich finde alle Sachen, die ich da drin brauche und dann habe ich nur eine Datei und so weiter.

Das kann man ja diskutieren.

Hier reden wir nicht viel von das Problem, das Problem, hier reden wir nicht viel von Komplexität.

Wenn es allerdings Sachen gibt, die halt komplex sind und die auch beim Deep Dive dann halt komplex sind und ich sehe, die werden auch oft geändert oder die haben nur einen Autor.

Das ist dann kein Diskussionsobjekt mehr.

Weil wenn es oft geändert wird und nur einen Autor hat, okay, dann habe ich dann Wissensziele.

Und wenn dieser Autor dann vielleicht auch noch das Team verlassen hat, es gibt ja den Lotto-Faktor, Lotto gewonnen oder Kind gekriegt oder sowas ist weg und das wird anderer und verändert und dann ist er nicht mehr da, dann ist das ja ein Business-Risiko.

Da muss ich, da kann ich ja nicht mehr darüber diskutieren, da kann ich nur noch über Prioritäten reden und sagen, okay, ist das jetzt das Allerwichtigste oder ist es das, was keine Ahnung, was bekannt dafür ist, dass es sehr viele Bugs verursacht.

Was hat, ich glaube da ist schon was Spannendes gesagt, also das hat gesagt, okay, es gibt halt irgendwie bestimmte Dinge, die diskutiert man halt nicht, weil die sind halt so und bei einem Autor ist es halt auch irgendwie so, dass es nicht viel Sinn macht, das zu diskutieren, weil es gibt nur eine Person, die das eigentlich diskutieren kann.

Und dann gibt es irgendwie diese Sachen, wie zum Beispiel mit diesem Mock, wo man eben diese Diskussion haben kann und ich weiß nicht, wie es dir geht, aber oder ich würde jetzt mal unterstellen, wenn jetzt irgendwie das Team sagt, naja, wir können halt damit leben, das sieht zwar komisch aus, aber was soll's, dann wäre das halt so.

Der MD42 Martin hat noch geschrieben, ist es sinnvoll, solches Insider-Wissen, also ich nehme an, dieser Lottofaktor von eins, dass eben nur eine Person da irgendwie das Bescheid weiß und wenn die halt irgendwie da ein Problem, wenn die halt das unternehmen will, deshalb hat man halt ein Problem.

Ist es sinnvoll, sowas als Kommentar am Datamocks zu hinterlassen?

Geht das überhaupt?

Also, dass das Ding nur einen Autor hat?

Ach so!

Also, dass man jetzt sagt, dass man jetzt irgendwie was sagt und halt sagt, hey, netter Versuch, ist aber eigentlich egal, wir haben uns halt irgendwie darüber unterhalten und es ist halt fein.

Ja, also in Code, also Moment, distanziert zwischen Code und Codekarte.

Sorry, er hat gerade geschrieben, nein, ich meinte, dass alle Mocks in Datamocks sind, also dass man jetzt irgendwie hinschreibt irgendwie, okay, Datamocks ist das Ding, da sind alle Mocks drin, das ist der Grund, warum das irgendwie so komisch aussieht.

Es sieht ja tatsächlich komisch aus.

Ich glaube, es ist das Gebäude mit offensichtlich der größten Grundfläche.

Es ist rot und es ist relativ niedrig und das sticht wirklich hervor.

Ob es sinnvoll ist, ich mach's mir mal einfach und sag, das ist halt eine Teamdiskussion.

Also, ich...

Thema Onboarding, Thema Perprogramm, wie kriegt man diese Information am besten vermittelt?

Keine Ahnung.

Das ist halt so unglaublich teamvariabel, dass ich darauf keine Antwort geben kann.

Ja, was aber auch wiederum bedeutet, also wir hatten ja vorhin dieses Ding, diese sehr schöne Grafik, wo du eben gesagt hast, okay, die City wird halt hübscher, also kleinere Gebäude, weniger rot.

Und da muss man jetzt an einigen Stellen, also, wie soll ich sagen, wenn man einfach reflektiert jetzt sagt, und das ist das Ziel, müsste man ja jetzt bei dem Datamox irgendwie sagen, das müssen wir jetzt irgendwie klein hauen.

Und das macht vielleicht nicht so viel Sinn, also das hat er gesagt, es ist denkbar, dass das Team damit leben kann, dann würde man eben damit leben.

Ja, und dann kann es sein, dass das Team auch entscheidet, okay, wir machen jetzt einen Kommentar hin.

Was aber dann nicht in dem Werkzeug wäre, glaube ich, oder?

Was ist in dem Werkzeug?

Was wir machen können in dem Werkzeug, ist natürlich, wir können sagen, okay, entweder flatten oder exclude.

Also flatten ist, ich mache es mal flach.

Dann hat es auch keine Farbe mehr.

Es ist einfach platt gedrückt.

Ich kann das mal ein bisschen exemplarisch mit diesem Großen hier machen und sagen, okay, platt.

Wenn ich allerdings sage, okay, das ist aber trotzdem eine große Grundfläche, ich hätte das gerne jetzt exclude, dann kann ich es auch rausschmeißen.

Und wie ihr seht, hat sich die Stadt geändert und das Ding ist halt weg.

Genau, das ist so ein bisschen der Nachteil von so einer TreeMap.

Der Algorithmus sagt, der ist nicht refactoring-stabil.

Weswegen wir auch einen anderen anbieten, der ist aber ein bisschen experimenteller.

Und der sieht dann halt wirklich aus wie eine Stadt.

Also wir hatten vorher komplett die Fläche sozusagen nur unterteilt.

Das war so ein großes Quadrat.

Hier sehen wir tatsächlich Straßen mit Gebäuden dran, also wie eine richtige Stadt, die eben nicht mehr eine quadratische Grundfläche hat, die irgendwie aufgeteilt ist, sondern das ist eben eine richtige Stadt.

Genau.

Und der große Vorteil ist, wenn ich jetzt hier irgendwas großartig flatter oder halt gleich exclude, also die grundsätzliche Struktur bleibt halt da.

Die ist refactoring-stabil.

Ich sehe jetzt halt die Größen nicht mehr so wirklich optimal.

Vorher war halt etwas, das sehr groß war, war halt auch physisch zentriert an einem Ort sehr groß und jetzt ist es halt so spread out.

Es ist manchmal eine praktische Darstellungsform, weil wenn man viel refactoring gemacht hat, dann macht es mehr Sinn, diese Grafik zu zeigen.

Sie ist aber, wie ihr hier unten seht, also warum ist diese Straße so lang?

Und das ist halt ein Algorithmus-Thema, weil die Bounding-Box von der Straße, die hier abgeht, halt so groß ist.

Und dann ist diese Straße auch so lang.

Woher kommen denn die Straßen jetzt?

Also die Gebäude sind immer noch die drei Meter.

Also das sind Ordner.

Ah, okay.

Also das ist dann tatsächlich die Source-Kunststruktur.

Genau.

Also du siehst hier hier oben wieder den Dateipfad.

Da siehst du Root, App.

Und von App geht jetzt Code-Charta und dann geht da von State dann da von UI.

Und noch eine Frage.

Du sagtest refactoring stabil.

Damit meinst du, wenn ich Gebäude entferne, sieht der Rest immer noch genauso aus wie vorher?

Richtig?

Das meintest du?

Also das ist nicht Refactoring im Code, sondern wenn ich halt hier diese Grafik ändere, weil ich halt irgendwelche Gebäude ausschließen möchte.

Ja, also ich meine auch, also es ist natürlich, wenn ich jetzt irgendwie ein Gebäude komplett aufsplitte.

Also wirklich Refactoring.

Und das Ding wird jetzt zu zwei, drei kleinen.

Dann bleiben die halt entweder hier oder vielleicht ein bisschen weiter drüben.

Aber die bleiben grob an derselben Stelle.

Bei der selben Straße sein, bei der selben Ordnerstruktur irgendwo sein werden, in der Nähe.

Genau.

Also es ist schon auch auf Refactoring, auf das Code-Refactoring bezogen.

Es ist halt nur jetzt gerade für mich schwierig, Refactoring darzustellen.

Ja, klar.

Das ist experimentell, sagtest du?

Ja, das ist experimentell, weil ich die Darstellung vorne noch nicht so gut finde.

Ich haue jetzt gerade unseren PO ein bisschen auf den Mützen.

Ich bin ja nicht mehr der PO.

Da sage ich das nur ganz kurz und danach halte ich die Klappe, damit er nicht sauer wird auf mich.

Vor allem, weil ich ihn dazu gebracht habe, es einzubauen.

Es ist halt, also da muss man auch ein bisschen Gehirnschmalz reinstecken, wie man diese Bounding-Boxes macht, damit diese Straßen halt ein bisschen hübscher aussehen.

Also es ist einfach ein ästhetisches Erfinden bei mir, wo ich sage, das könnte schicker aussehen.

Genau, das ist jetzt eine relativ lange Straße, an deren Ende irgendwie so drei Gebäude sind.

Und das ist halt weird, weil die anderen Straßen sehen halt so aus wie Manhattan, nicht?

Ein bisschen.

Genau.

Also das passiert halt gerade bei dem Root, aber im Regelfall bietet es sich nicht her.

Es ist halt auf jeden Fall nutzbar und nicht irgendwie instabil oder so, sondern du sagst, dass man da irgendwie noch das noch hübscher machen kann.

Genau, genau.

So und eine Sache wollte ich noch, bevor uns die Zeit wegläuft.

Ich habe viel darüber geredet, es gibt halt auch einen Delta-Modus.

Und den finde ich halt sehr angenehm, wenn man halt zum Beispiel ein Review hat und halt einfach explizit nur ein Refactoring vorzustellen hat.

Und wie macht man dieses Refactoring für Non-Business-User halt eben plastisch?

Naja, so.

Man kann halt sagen, okay, wir haben jetzt zum Beispiel hier also da links oben habt ihr es gesehen, wir haben Komplexität abgebaut.

Also sprich, alles was grün ist, ist in dem Fall eher irgendwie positiv.

Denn grünes Dach hier heißt, ich habe Komplexität abgebaut.

Wenn ich jetzt Coverage vergleichen würde, würde ich halt eher sagen, okay, dort, wo ich Coverage abgebaut habe, ist es rot.

Und dann kann ich ihm halt auch sagen.

Hier sind jetzt aber viele rote Gebäude.

Ja, genau.

Bei manchen Sachen ist das okay.

Hier ist ein komplett neues Gebäude entstanden seit dem letzten Mal.

Also ich vergleiche hier gerade Mai 24.

Das Delta hat nicht nur das Refactoring, sondern hat eben auch das Ongoing Business.

Und wenn man jetzt das rein Refactoring hätte, könnte man tatsächlich das Ergebnis das rein Refactoring dazu zeigen.

Genau.

Oder, keine Ahnung, hier.

Da ist jetzt schon die Frage, okay, der Filepanel hatte vorher 36 Complexity.

Jetzt hat er 49.

Okay, gut.

Also schon ordentlich mehr.

Musste das sein?

Nein, hätte man da nicht was anderes machen können.

Dann kann man diese Diskussion halt führen.

Dann kann man sagen, oh, ja, da sind wir vielleicht noch nicht ganz fertig mit dem Refactoring.

Genau.

Es gibt noch eine Frage aus dem Chat von Teertrude, der schreibt oder fragt, kann man auch Monoreprister mit analysieren?

Ja.

Den Drilldown vom Projekt eben starten, sprich ein Gebäude, ein Projekt.

Ein Gebäude, ein Projekt.

Ach so.

Also ich glaube, er meint damit, ich habe irgendwie so ein Ding, wo viele Projekte sind und dann fange ich halt an und sage, ein Gebäude ist ein Projekt.

Ja, also ich meine, natürlich tierfrei.

Genau, dann kannst du keinen Drilldown machen.

Also ich kann ja nicht sagen, dieses Gebäude ist ja dieses Projekt und dann kann ich halt irgendwie in das Gebäude reingehen und das irgendwie noch detailliert anschauen.

Sondern du müsstest ja verschiedene Beziehungen haben.

Was du natürlich machen kannst, ist, du kannst halt ...

Wenn du jetzt zum Beispiel zwei Projekte hast, JUnit4 und CodeCarter.

Das sind deine Projekte im Monorepo jetzt beispielsweise.

Dann habe ich hier JUnit4 und dort habe ich CodeCarter.

Das heißt, ich kann mehrere jetzt gemeinsam anzeigen.

Genau.

Das ist im Endeffekt auch das, was ihr seht, wenn wir jetzt hier die Seite komplett neu laden, dann zeigen wir standardmäßig CodeCarter.

Das ist CodeCarter Visualization und Analysis an.

Und dann siehst du halt auf der linken Seite, die Analyse ist halt deutlich kleiner als hier die Visualisierung.

Das liegt auch ein bisschen an Kotlin, aber ehrlicherweise ist die Visualisierung auch da, wo mehr von unserer Zeit reinfließt.

Was ja nachvollziehbar ist, weil es ist im Wesentlichen ein Visualisierungstool.

Irgendwas, was du den Zuschauern mitgeben soll, willst du irgendwas?

Also gar nicht.

Man kann es ausprobieren, man kann auf die Homepage gehen und das da sozusagen live verwenden.

Das läuft im Wesentlichen im Browser, von daher ist es halt auch nicht besonders aufwendig.

Man muss nicht irgendwie groß was installieren.

Also der Travelling-IT-Konsultant hat noch gefragt, das heißt dann aber, dass man für jedes Projekt im Monorepo eine eigene Analyse fahren muss, oder?

Und das ist dann so, glaube ich.

Das Problem ist ja jetzt an dieser Frage, was heißt Monorepo?

Ich habe ein JavaScript-Projekt, das ist dann aufgeteilt in mehrere einzelne sowas wie NX oder so.

Das ist aufgeteilt in mehrere kleine Projekte und insgesamt ist es ein Projekt.

Und das kann man dann auch als eines analysieren.

Wenn im Monorepo allerdings irgendwie ein Frontend, ein Backend ist und die sind in unterschiedlichen Programmiersprachen, dann kommt es halt ein bisschen darauf an, ob man jetzt Sonar nutzt und das eben sagt, ich will das in separate Sachen in Sonar pumpen oder ich will es in ein oder andere Sachen reinpumpen.

Von daher die Antwort auf deine Frage ist it depends.

Also auf deine Projektsetup, wie du es selber in Sonar gerne vorfinden möchtest, ob du überhaupt Sonar hast.

Und wie es da umgesetzt ist.

Eine ganz wichtige Sache.

Es steht hier irgendwo so da.

## Datenschutz und Deployment

Also Codekarte als Visualisierung und als Analyse, entweder das läuft komplett bei euch oder ihr nutzt dieses Webstudio.

### Lokale Datenspeicherung

So oder so, das nutzt nur eure Local Storage.

Also ich kann das auch technisch belegen.

Es ist in GitHub Pages gehostet.

Also sprich, da ist kein Backend oder so.

Also die Daten bleiben bei euch.

Fertig.

Okay, das heißt, ich kann online eben auch meine eigenen Sachen analysieren, sagst du, weil die Daten irgendwie bei mir bleiben.

Genau.

Also wenn ihr aus irgendeinem Grund sagt, hey, das Risiko ist mir zu hoch, dass ihr da irgendwelchen Bullshit macht, naja, also ich meine, ihr könnt auch die Codekarte Visualisierung halt lokal starten.

Braucht ihr nicht, aber könnt ihr natürlich machen.

Okay, das heißt also eigentlich sagst du, ich muss nicht unbedingt also mindestens die Visualisierung muss ich eben nicht bei mir selber betreiben.

Was Irgendwas, was du noch den ZuschauerInnen irgendwie mitgeben möchtest?

Ja, ich würde mich super darüber freuen, wenn ihr uns da so ein Sternchen geben würdet.

Bei GitHub?

Ja, bei GitHub.

Ich würde mich generell auch super darüber freuen, Feedback zu kriegen.

LinkedIn oder Blue Sky oder was auch immer.

Einfach anschreiben.

Wir requesten natürlich gerne Issues.

Also wenn ihr sagt, da ist ein Bug drin oder wenn ihr sagt, da fehlt ein Feature, also nur zu.

Wir finden das super.

Also wir finden es nicht super, dass wir Bugs haben, aber wir finden es super, wenn wir Feedback kriegen.

Genau, und das würde ich gerne noch unterstreichen.

Das ist auch so eine, wie soll ich sagen, so eine Misskonzeption, die hat ja mit da draußen existiert.

Also beteiligen an Open-Source-Projekten bedeutet eben nicht unbedingt selber Code schreiben, sondern irgendwie Feedback geben, Issues einstellen und Bugs man und so weiter.

Das ist, glaube ich, irgendwie auch ich habe das halt gemerkt, als ich noch mich intensiv mit dem Spring Framework beschäftigt habe.

Da kamen dann irgendwelche technischen Fragen und dann bin ich dazu übergegangen zu sagen, also nicht, und das sah dann auch aus wie ein Bug oder irgendwas ist irgendwie unklar.

Und dann bin ich dann dazu übergegangen zu sagen, hast du ein Issue eingestellt?

Also sehr nett, wenn jemand mit mir redet, aber besser ist es halt noch, wenn es irgendwo ein Bug-Checker steht und da steht eben die Möglichkeit offen.

Gut.

Dann würde ich sagen, haben wir es soweit?

Vielen Dank auf jeden Fall, dass du da warst.

Ich finde es total spannend und ich glaube, das ist ein total cooles Tool für Visualisierung.

Und genau, dann sehen wir uns nächste Woche wieder.

Mal schauen, was wir nächste Woche im Stream machen.

Noch ist das nicht so ganz klar.

Und genau, ich würde sagen schönes Wochenende und bis dahin.

Achso, und wie gesagt, wenn ihr zu der Konferenz, zu der Ankunft von uns kommen wollt, zu dem Thema Software, Integration und KI, sehr gerne.

Freuen wir uns natürlich.

Bis dahin.

Ciao.