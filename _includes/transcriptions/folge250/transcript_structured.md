### Einführung und Überblick

Ja, hallo und herzlich willkommen zu Software-Architektur im Stream.

Eine neue Episode.

Ich hoffe, wir sind jetzt wirklich live, aber das sehe ich bestimmt gleich in den Kommentaren, wenn man etwas nicht hört oder nicht sieht.

Genau, heute machen Ralf und ich einen Stream.

Ralf möchte ganz viel programmieren und euch zeigen und ich darf dann immer schlaue Fragen stellen.

So ist jedenfalls die Grundidee, aber ich hoffe auch ganz, ganz, ganz stark auf eure schlauen Fragen aus dem Chat.

### Themenvorstellung

Die Folge heute heißt Spaß mit KI, Adjantic Workflows und Self-Verification.

Ralf, was hast du dir dabei nur gedacht?

Genau, was habe ich mir dabei gedacht?

### Motivation

Wir hatten in den vergangenen Folgen immer viel über mein System geredet, was das alles kann, wie es eigenständig arbeitet.

Und immer wieder kam die Frage, ja, was ist das eigentlich?

Was hast du da für ein System?

Und deswegen habe ich mir gedacht, ich zeige mal so ein bisschen was heute.

### Agentic Workflows vs. Adjantic Workflows

Und wichtig ist dabei, momentan geht durch Social Media viel der Hype um Agenten und Adjantic Workflow.

Und das finde ich total spannend, weil das sind für mich zwei total unterschiedliche Sachen mittlerweile.

### Definition und Unterschiede

Anfangs dachte ich, naja, Adjantic, das heißt, das ist ein Workflow mit Agenten.

Aber wenn man es genau nimmt, bedeutet Adjantic eben auch eigenständig, dass es ein eigenständiger Workflow ist.

Das eben meine KI etwas eigenständig macht.

Und das ist eben, das kann unterschiedlich erreicht werden.

Also wir kennen das ja, wenn wir mit Chatty und Co Mistral, Claude quatschen, dann ist es immer so ein Frage-Antwort-Spiel.

Weil lange Zeit konnten die Tools gar nicht mehr als eine Antwort geben.

### Function Calling in KI-Systemen

Und mittlerweile haben sie das sogenannte Function Call, also fast jedes Tool hat Function Calling implementiert.

Und angefangen hat es eigentlich so bei Chatty mit dem Bild generieren, dass man gesagt hat, generieren wir mal ein Bild.

Und dann kam das Bild.

Und das war wenig Adjantic, weil das war auch wieder Auftrag und Antwort.

Und ich weiß gar nicht, wie es da implementiert ist, ob das Bild direkt an den User zurückgegeben wird, oder ob das LLM das Bild erst sieht und dann dem User sagt, guck mal, hier ist das Bild.

Weil das ist der große Unterschied, wenn das Modell das Tool aufruft und selbst das Ergebnis des Aufrufs zurückbekommt, dann kann es nochmal drauf reagieren, dann kann es eigenständig arbeiten.

Und ich würde mal vorschlagen, ich teile mal meinen Bildschirm und dann kann ich was zeigen.

Sehr gerne.

Also Adjantic Workflow, nur damit ich es nochmal so richtig auf dem Schirm habe, das ist quasi nicht, wenn man dieses Frage-Antwort-Battle macht mit der KI, sondern wenn man wirklich einen Auftrag, also einen kleinen abgeschlossenen Auftrag ihr gibt und sie würde den komplett eigenständig abschließen, eventuell auch mit dem Wechsel von internen Anwendungen, also keine Ahnung, sowas wie, programmier mir mal einen Taschenrechner.

Und sie überlegt erst mal, was brauche ich alles, um einen Taschenrechner zu programmieren, und dann setzt sie das auch in Python um, oder ist das schon wieder ein Schritt zu weit gedacht?

Ja, doch.

Also genau das kann ich mal zeigen.

### Praktische Beispiele

Also ich versuche mal, ich habe das jetzt nicht einstudiert, das, was ich jetzt gerade ausprobieren will.

Du bist auf den Taschenrechner gekommen, probiere was mit dem Taschenrechner aus.

Wenn ich jetzt hier, ich habe hier Claude offen, und wenn ich Claude frage, was ist die Wurzel aus 1234?

Mal gucken, was er macht.

Lass mich das berechnen, sagt er.

Sagt Analyzing.

Er hat einfach Python genommen und das ausgerechnet, ne?

Ne, das ist Python, das sieht aus wie JavaScript.

Ich überlege gerade, das sieht aus wie JavaScript.

Da bin ich jetzt auch wieder etwas erstaunt, weil ich dachte, er hat nur den Python Code Interpreter drin.

Gut, da ist er einen Schritt weiter, als ich dachte.

Ja, der wusste, dass wir gerade sprechen und er kannte mich noch.

Deswegen hat er JavaScript genommen.

Genau.

Auf jeden Fall, das ist jetzt eben schon genau dieses eigenständige, dieser eigenständige Workflow, dass er hier jetzt gesagt hat, okay, ich habe hier ein Tool, das kann ich benutzen und ich programmiere die Aufgabe Wurzel aus 1234, kriege von dem Tool das Ergebnis zurück und hier sieht man sehr schön, dass er das Ergebnis nimmt und nicht einfach ausgibt, so wie meistens bei den Bildern, sondern er baut eine Antwort, genauso wie damals im Matheunterricht, wo es hieß, Textaufgabe, bitte auch eine Antwort formulieren.

Und ja, ungefähr 35,13 genauer und das ist eben genau das, was er zurückbekommen hat.

Also das heißt, hier haben wir schon eine Implementierung des Code Interpreters und die Tools sagen immer so schön, ja, sie analysieren das.

Also das ist der Code Interpreter, eine Implementierung, wo das LLM die Maschine erst mal ihr Tool benutzt, das Ergebnis bekommt, das Ergebnis sieht und dann mit dem Ergebnis weiterarbeitet.

Ich habe zwei Fragen.

Warum nimmst du jetzt eigentlich Claude?

Du hast doch sonst immer JGPT genommen.

Das ist eine sehr gute Frage.

Ich weiß nicht, wie ich es jetzt richtig ausdrücke.

Ich meine, man hat jetzt so verschiedene Maschinen und man kommt mit der einen Maschine besser zurecht als mit der anderen.

Ich habe mich mit Claude mehr angefreundet als mit JGPT mittlerweile.

Liegt auch daran, dass Claude tatsächlich diesen Agentic Workflow besser beherrscht als JGPT, beziehungsweise das Modell dahinter, hier haben wir Claude 3.5.0 Net, bei JGPT haben wir das GPT 4.0 und so.

Es tut sich etwas schwerer mit dem Agentic Workflow und der ist halt jetzt aus meiner Sicht total wichtig.

Und ich versuche mal hier ein bisschen mehr rauszuholen, weil was jetzt hier passiert, das ist ja auch noch ein bisschen langweilig.

Also er berechnet das und gibt das Ergebnis zurück.

Das wäre meine nächste Frage gewesen, weil im Moment ist es noch nicht cooler als der Taschenrechner, den ich habe.

Genau.

Aber wenn ich jetzt als Entwickler mit der Maschine arbeiten will und programmieren will und ich sage, apropos jetzt, ich hatte den roten Faden etwas verloren, was hier eben auch wichtig ist, gerade bei dem Berechnen.

Wir sehen jetzt, dass man sagt ja immer, die Maschinen können halluzinieren.

Aber hier sehe ich jetzt, ich kann glaube ich irgendwo die Tool Usage auch ausschalten.

Mal gucken.

Ich schalte das ab.

Und wenn ich jetzt berechne.

Die Wurzel 1234.

Ja, jetzt geht er ganz anders vor, weil er hat nicht mehr das Tool.

Er gibt jetzt hier zwar vorher mit genauer Berechnung.

Da waren wir jetzt mit dem JavaScript schon näher dran.

Ja, ich weiß jetzt auch nicht.

Ich habe die Zahl nicht mehr im Kopf.

Können wir gleich mal gucken, ob das jetzt so genau ist.

Auf jeden Fall.

Hier muss er auf einmal Kopf rechnen.

Und umso komplexer die Aufgabe wird, umso eher macht er Fehler, kommt ins Halluzinieren rein und dieses Halluzinieren kann ich halt eben sehr gut unterdrücken, indem ich.

Eben ihm ein Tool mitgebe, das heißt, das ist schon mal ganz wichtig.

Falsche Antworten unterdrücke ich, indem ich ein Tool mitgebe, was der KI es ermöglicht.

Das war nicht das Richtige.

Ich habe es falsch kopiert.

Sorry, indem ich ein Tool mitgebe, dass die Maschine eben so eine Berechnung oder andere Sachen auch ein Nachschlagen über eine API eigenständig machen kann.

Und damit das korrekte Ergebnis kriegt.

Und damit ist das System dann eben auch gegründet, weil es eben tatsächlich die die wirkliche die Wahrheit aus dem Tool holt.

Und ich kann dann als User eben sehen.

Ah ja, hier hat er was berechnet und hat es ausgegeben.

Aber wenn ich jetzt eben als Entwickler sage, schreibe mir einen Merge Sort in Python und höre ihn aus.

Ich hätte nochmal so auch jetzt.

Das passt hier auch noch nicht.

Ich hatte jetzt gerade gedacht, ich sitze in der Schule.

Ist schon lange her, aber ich kann mich ja auch mal eine Schülerin reinversetzen und habe Wurzelrechnung und ich muss dann ja erklären, wie das passiert.

Ich könnte ihn aber wahrscheinlich jetzt auch fragen.

Kannst du mir die Quadratwurzel von 1234 geben und mir den Lösungsweg erklären?

Würde er dann automatisch trotzdem die Wurzel berechnen oder würde er sie dann kopfrechnerisch berechnen und mir das schlechtere Ergebnis geben?

Oder muss ich das in zwei Stufen machen, weil er mir sonst Quatsch gibt?

Tolle Frage.

Ich müsste es ausprobieren.

Bei meinen Experimenten benutzt er eigentlich immer die Tools, aber ich lasse mir auch meistens nicht erklären, wie ich die Wurzel ziehe.

Das wäre hier jetzt quasi die gleiche Geschichte.

Sagen wir, ich bin in der Ausbildung und habe gerade Sortieralgorithmen und möchte bei meinen Hausaufgaben schubbeln, aber muss noch erklären, wie denn überhaupt der Merge Sort funktioniert und wie er sich vielleicht zu einem Quick Sort unterscheidet und wie er schneller ist.

Würde ich das dann eher in mehreren Schritten machen?

Hier steht es sogar schon.

Beim Merge Sort war er gnädiger zu dir.

Da hat er schon erklärt, wie der Algorithmus funktioniert.

Genau, hier erklärt er.

Er ist sehr aufgeschlossen, sehr gesprächig und er sollte ja eigentlich nur den Merge Sort schreiben, aber er erklärt ihn auch.

Das ist eigentlich sehr nett von ihm.

Wir sind es immer noch so gewöhnt, dass wir eine Anweisung reingeben und gleich das perfekte Ergebnis erwarten.

Aber das macht wenig Sinn, weil wir haben den großen Kontext der Maschine und den sollten wir auch nutzen, sollten langsam Kontext aufbauen, mit der Maschine reden.

Das heißt, es macht auf jeden Fall Sinn, in mehreren Schritten vorzugehen.

Hier habe ich jetzt ein kleines Problem.

Wir haben hier den Canvas.

Das ist ziemlich cool.

Da habe ich den Code hier nebendran.

Ich sehe jetzt gerade nicht korrekt, ob er das ausgeführt hat.

Was aber jetzt hier schon mal spannend ist, ist, dass er hier Tests geschrieben hat und theoretisch müsste er mir eigentlich Höhen zeigen, dass er das ausgeführt hat.

Ich sehe es jetzt hier nicht.

Ich hatte gestern das ausprobiert und er hat es mir inline gezeigt.

Hier ist jetzt der Canvas aktiv.

Das ist dieses extra nebendran gestellt, der Source Code.

Das ist hier übrigens ganz nett.

Du siehst, ich habe hier ein Kästchen, was für den Source Code steht.

Ich klicke drauf, dann geht es auf.

Und wenn ich jetzt mehrere Versionen habe, also wenn ich mit der Maschine an dem Code arbeite, dann habe ich hier auch mehrere Versionen im Zugriff.

Witzig, dass er jetzt Peisen genommen hat.

Das hattest du gar nicht spezifiziert, oder?

Doch, habe ich ihm gesagt.

Ich dachte schon, jetzt hat er keine Lust mehr auf JavaScript.

Genau.

Ich schaue jetzt nochmal.

Nicht, dass ich mich getäuscht habe.

Ich habe hier, ich mache das nochmal so, dass ich das Analysis Tool auf jeden Fall drin habe.

Ich muss zugeben, ich komme bei der Vielfalt der Tools ziemlich durcheinander.

Du hast vorhin gesehen, das JavaScript hat er ausgeführt.

Ich bin mir gerade gar nicht so sicher, ob ich jetzt das Ganze mit Mistral gemacht hatte oder jetzt hier mit Claude, dass das ausführt, ob jetzt hier Claude Peisen überhaupt ausführen kann.

Es gibt eine Frage im Chat, die ich sehr spannend finde, die hätte ich auch gerne noch gestellt später.

Woher weiß ich, ob das Programm zur Wurzelrechnung korrekt ist, Tests dazu generieren lassen aller Specification by Example?

Ja, genau, genau.

Das geht in genau die Richtung.

Lass mich kurz hier was ausprobieren.

Ich stelle mir gerade vor, wie du so einen Abergriff hast und die Wurzelnachrechnung.

Naja, also das Ding ist, sobald ich auf den Code Interpreter gehe, habe ich halt die Programmiersprache im Hintergrund.

Und ja, wir hatten auch in der Vergangenheit Bugs in Prozessoren und so.

Aber ich muss irgendwo dem System in irgendeinem Level vertrauen.

Und der Programmiersprache vertraue ich.

Und ich weiß, dass wenn er das Tool benutzt, dann führt er das Ganze aus.

Und ja, in der Tat Test Driven.

Das ist jetzt der nächste Schritt.

Weil wenn ich jetzt hier nur den den Source Code habe und sag für das aus, dann weiß er schon.

Okay, ich habe hier mal Beispiele.

Ich habe hier einfache Tests, weil irgendwie muss ich das Ganze ausführen.

Wenn er den Code ausführt, dann hat er schon so die erste Ebene eines Checks.

Das heißt, der Code muss syntaktisch korrekt sein, dass er ausgeführt werden kann.

Die Libraries, die referenziert werden, die müssen auf dem System vorhanden sein.

Das ist ein erster Check.

Ein zweiter Check ist, wenn ich eben sag, erstelle Tests für einen Merge Sort in Python, erstelle dann nochmal den Merge Sort und führe die Tests aus.

Aber.

So, dann habe ich nämlich die zweite Ebene.

Dann habe ich nämlich die Ebene.

Er erstellt jetzt ganz viele Tests mit seinem Knowhow.

Was könnten hier irgendwelche Grenzfälle sein?

Und ich hatte da schon ein bisschen was gesehen.

Ich lasse ihn das gerade mal hier runter schreiben.

Ach, jetzt macht er hier noch andere Test Cases.

Das ist natürlich spannend.

Und jetzt kann ich hier auf die Tests gehen.

Und okay, eine große Liste.

Oder hier kein Element, ein Element.

Negative Zahlen mit drin.

Genau.

Und jetzt habe ich hier eben auch Zugriff auf die verschiedenen Versionen des verschiedenen Codes, den er jetzt erstellt hat.

Und das wäre jetzt eigentlich die zweite Check Ebene.

Also wenn er den Code ausführt, dann muss er syntaktisch korrekt sein.

Die zweite Ebene ist dann, dass die Tests ausgeführt werden.

### Test-Driven Development

Das heißt, die Tests müssen eben grün sein.

Und da habe ich jetzt noch was vorbereitet.

Und jetzt gehe ich einfach mal auf mein eigenes System, weil ich habe hier das Gefühl, dass ich hier den Fehler gemacht habe.

Ich bin irgendwie über meine Quote oder so rüber, dass er nicht die Tests ausführt.

Während du da langsam hin wechselst.

Ach, du bist schon hingewechselt.

Während du da sehr schnell hingewechselt bist.

Aber ich sage, ich bin unerfahrener Entwickler, habe keine Ahnung vom Merge Sort, gibt dem das jetzt, gibt dem auch die Tests.

Wie kann ich denn sicher sein, dass der mich nicht volle Möhre veräppelt?

Weil ich meine, ich kann doch super schlechten Code schreiben, wenn ich die Tests nur so schreibe, dass die immer grün sind.

Weißt du, wie ich meine?

Ja, ja, absolut.

Und da kannst du dir tatsächlich nicht sicher sein.

Das ist tatsächlich ein kleines Problem.

So, jetzt sage ich hier meinem System, er soll diesen Merge Sort schreiben in Python und die Tests ausführen.

Und das ist jetzt spannend, weil das ist immer noch genau so ein System, wie die anderen Systeme, die man draußen hat.

Nur, dass ich hergegangen bin.

Ich habe meinem etwas mehr Tools mitgegeben.

Ja, also er kann Diagramme generieren.

Er hat einen Python Code Interpreter.

Er hat einen Browser.

Er hat einen Groovy Interpreter.

Das ist so das, was ich gesagt habe.

Ich möchte ja nicht nur Python mit ihm entwickeln, sondern ich bin in der Java-Welt unterwegs.

Ich will hier JShell benutzen können.

Irgendwann habe ich ihm auch eine Bash gegeben.

Seitdem ignoriert er die anderen Interpreter.

Und er hat so ein paar Anweisungen, aber einfach nur im System prompt Anweisungen, in denen ich ihm gesagt habe, wenn du Code entwickelst, dann mach das bitte gescheit.

Dann mach das Test-Driven.

Und dann wirf nochmal einen Blick über den Code, ob der tatsächlich gewissen Anforderungen entspricht.

Und du siehst, ich habe hier diesen einen Request reingeschickt.

Und mein Scrollbar, der ist ziemlich lang geworden.

Also er sagt, ich gehe Schritt für Schritt vor, erst erstelle ich Tests, dann implementiere ich den Merge Sort, anschließend führe ich die Tests aus und überprüfe die Implementierung und er macht hier erstmal ein Create Folder und bei dem Create Folder soll er auch eine Erklärung mitgeben, was für ein Folder das ist, das macht er, dann erstellt er die Testdatei, dann erstellt er sie tatsächlich als Datei, das ganze läuft in einem Docker-Container.

Ah, ok, deswegen hat er auch einen Ordner erstellt, ich war gerade noch so ein bisschen raus, wo man einen Ordner braucht.

Also manchmal macht er es mit Ordner, manchmal macht er es einfach so, weil er sagt, hey, das ist nur ein File, aber ich finde es mit dem Ordner eigentlich gar nicht schlecht.

Und er läuft im Docker drin und generiert es dann einfach in seinem Docker-Container.

Genau, und in den Docker-Container habe ich einen Folder von mir gemountet, sodass ich zusammen mit ihm an den Files arbeiten kann.

Das sieht jetzt hier alles etwas, ja, mit Escaped in Anführungszeichen aus, weil das eben hier tatsächlich der Tool-Aufruf ist und man genau sieht, was wird dem Tool übergeben.

Er hat also auch hier wieder Tests mit Sonderfällen erzeugt, er hat jetzt hier nicht diesen Sonderfall, ich habe eine ganz lange Liste erzeugt.

Jetzt erstellt er den eigentlichen Merge Sort Algorithmus.

Das passt, dann führt er die Tests aus.

Da benutzt er die Bash, er benutzt sehr gern die Bash, er weiß, wie er mit der Bash umgehen soll.

Das ist nicht bei jedem Tool so gegeben.

Ein Modell hatte ich, das mit der Bash sehr viel ausprobiert hat und mir dann meinen Folder gelöscht hat.

Muss man natürlich auch ein bisschen aufpassen.

Aber klar, gerade Claude ist sehr, sehr kreativ, wenn es darum geht, Tools einzusetzen und zum Ergebnis zu kommen.

Und diese Kreativität brauchen wir bei dem Agentic Worker.

Das ist jetzt Claude im Hintergrund.

Ich kann das umstellen, ich habe hier ein paar Modelle hinterlegt.

Aber das ist jetzt Claude.

Er führt die Tests aus, sagt okay, sieben Tests okay.

Ausgezeichnet sagt er, alle Tests sind erfolgreich durchgelaufen.

Lassen Sie mich die Implementierung mit einem Diagramm visualisieren.

Das heißt, er benutzt jetzt sein Tool Generate Diagram.

Und hier geht er her und benutzt diesmal Mermaid, sonst nimmt er ganz gern Plant UML.

Das heißt, kommt ein bisschen auf die Tagesform drauf an.

Und anscheinend hat das geklappt.

Und er erklärt mir jetzt, was er gemacht hat und das, was du eben jetzt gesagt hast.

Ja, er hat jetzt also tatsächlich eine kleine Erklärung gebracht.

Man könnte das ihn jetzt noch bitten, das ausführlicher zu erklären und Wasser, wo er jetzt fehlgeschlagen ist.

Er hat zwar das Diagramm erzeugt, er zeigt es mir aber nicht an.

Ich sehe, dass das Tool es erzeugt hat, aber er hält es nicht für nötig, es mir anzuzeigen.

Jetzt gehe ich mal her und sage, zeige mir das Diagramm.

Wir haben eine Frage im Chat und ich glaube, dass da Sternchen reingerutscht sind, weil das bestimmt ein Link geworden ist.

Martin auf Twitch, wenn du möchtest, kannst du gleich korrigieren, was auch immer ich jetzt vorlese.

Hier steht, die Regeln im Settings-Dialog erinnern mich an Sternchen, Sternchen, Sternchen.

Eine modellunabhängige Regelsprache fände ich spannend.

Gibt es das schon?

Martin, wahrscheinlich sind Sternchen, Sternchen, Sternchen gerade irgendeine URL gewesen und deswegen wurde es rausgestrichen.

Kann das sein?

Und du Ralf, weißt du, ob es schon eine modellunabhängige Regelsprache gibt?

Ich kenne keine.

Ich gebe dem Modell natürlich sprachlich die Regeln vor und ich sehe auch, dass die Modelle sich da unterscheiden.

Ich sehe keine große Unterscheidung in der Wissensbasis, zumindest bei den ganz großen Modellen nicht.

Ich sehe aber eine Unterscheidung im Verhalten und das ist dann zum Beispiel das Instruction Following.

Wie gut folgen diese Modelle meinen Ausführungen?

Martin hat jetzt auch gesagt, dass es um cursor.com geht und da genau auf die Rules for AI in der Dokumentation hingewiesen wird.

Okay, die kann ich mir mal angucken.

Ich schicke dir direkt mal den Link, weil ich es jetzt hier so schön abgetippert habe gerade.

Okay, prima.

Also was ich hier vor allem jetzt mal zeigen wollte ist, ich scrolle nochmal hoch.

Ich habe hier eine kleine Anweisung gegeben.

Er soll mir hier ein Merge Sort bauen und dann ist er eigenständig losgelaufen und hat das alles hier gemacht und kommt irgendwann zurück.

Sagt Ich habe fertig, hat mir noch ein Diagramm gebaut, mit dem er das Ganze erklären will, den Algorithmus.

Auch da ist es teilweise unterschiedlich.

Hier hat er jetzt wirklich den Algorithmus erklärt.

Teilweise kommt er zurück mit einem Ergebnis, wo er tatsächlich ein Array in so einem Diagramm aufsplittet mit den Zahlen und das dann visualisiert.

Das ist ja cool.

Also gebe ich ja zu, vor allen Dingen für Ausbildung und Studium.

Aber ich sehe gerade nicht, wie das in einem praktischen Programmierer in den Alltag helfen kann, weil da würde ich ja einen Merge Sort wahrscheinlich nicht unbedingt.

Also mir ist es nicht sehr oft passiert, dass ich einen Sortieralgorithmus selber bauen musste in den Jahren, wo ich programmiert habe.

Kann man das auch sinnvoll in der Praxis anwenden?

Muss es denn immer sein?

Wir haben das Spaß genannt.

Ja, aber Ausbildung ist jetzt auch kein Spaß.

Also ich verbinde gerade Merge Sort einfach nur mit der Ausbildung und mit keinem Spaß.

Nee, passt ja, passt ja.

Ich versuche ein bisschen dahin zu kommen, zu zeigen, dass es irgendwo sinnvoll ist.

Ich starte eine neue Session.

Und sag jetzt nochmal, generiere mir einen Merge Sort in Python.

Und ich hoffe, dass er sich jetzt nochmal etwas anders verhält und vielleicht verhaspelt.

Passiert das auch manchmal?

Ja, ja.

Und das ist halt gerade das Wichtige.

Also wir wissen ja, wir sehen die Modelle meistens als nicht deterministisch an.

Es hängt vom Temperatur Parameter und anderen Parametern ab.

Sie können deterministisch sein, aber es hängt eben auch davon ab, wie ich meine Anfrage formuliere.

Und dementsprechend verhalten sie sich immer wieder anders.

Deswegen ist ja auch das Testing wichtig.

Also ich möchte Code haben, der sich deterministisch verhält.

Ich möchte aber die Kreativität der Maschine haben.

Und das zusammen, sie erzeugt Code, der ist dann deterministisch.

Das ist eigentlich prima.

### Code-Generierung und Testing

So, er hat wieder einen Folder angelegt.

Er macht wieder seinen Merge Sort.

Er sagt, er erstellt die Tests.

Prima.

Tests ausführen.

Prima.

Läuft.

So, und jetzt wird es spannend, weil ich ihm eigentlich gesagt habe, er soll nochmal einen detaillierten Blick auf den Code werfen.

Das ist im System prompt drin.

### Code-Qualität

Deswegen sagt er, er lässt jetzt nochmal einen Security Experten drüber gucken.

Und ich finde es total spannend, weil er benutzt sich selbst.

Er hat ein Tool, mit dem er nochmal ein LLM aufrufen kann.

Und dem sagt er jetzt, you are a security expert.

Specialized in Python Code Security.

Diesen System prompt hat er sich ausgedacht.

Das ist das Tool innerer Dialog.

Er gibt den Code mit.

Und bei so einem Merge Sort kommt da nicht viel raus.

Input Validation, aber naja.

Weil, this isn't a security issue per se.

Okay.

Dann aber auch nochmal Wartbarkeit.

Das gleiche.

Du bist ein Experte und guck mal drüber.

Und hier wird es spannend, weil er sagt, Mensch, dokumentiere doch bitte deinen Code.

Und slicing, was sagt er?

Unnecessary Memory Usage.

Kann man effizienter machen.

Okay.

Also I und J, das ist auch so ein Problem für ihn.

Manchmal sagt er ihm auch, du halte dich bitte an die Naming Conventions.

Und bitte keine Variablen wie I und J.

Weil das kann man nicht lesen.

Aber hier hat er halt gesagt, naja, I und J brauchst du nicht.

Du kannst ja direkt über die Listen iterieren.

Und da hat er also seine sich selbst aufgerufen als Experte.

Und das geht jetzt eigentlich in die Richtung Agents.

Wobei ich sage, es ist eigentlich immer noch das gleiche System, was einfach nur sagt, ich habe jetzt den Code geschrieben.

Ich gucke nochmal drüber, bevor ich den ausliefe.

So wie wir Menschen das eigentlich auch machen.

Also niemand von uns würde jetzt irgendwie Code einmal runterschreiben und sagen, da, fertig.

Sondern man guckt nochmal drüber.

Es gab noch eine Frage im Chat, eine ganz kurze.

Sind der innere Dialog und das Reasoning, was man von GPT kennt, unterschiedliche Dinge oder das Gleiche?

Das sind unterschiedliche Dinge.

Bei dem Reasoning bin ich mir nicht ganz so sicher, wie das im Modell verankert ist.

Es gibt System Prompts, die Reasoning verursachen.

Dass man dem Modell sagt, du machst dir eben erstmal Gedanken und führe folgende Schritte aus.

Formuliere die Problemstellung nochmal klarer und überlege dir, welche Lösungen es geben könnte.

Wähle eine Lösung aus.

Implementiere die Lösung.

Das würde als System Prompt zu einem Reasoning führen.

Jetzt ist das Reasoning aber eben auch in den Modellen irgendwie verankert.

Und da bin ich mir nicht sicher, wie sie das machen.

Ob das tatsächlich ein vorgeschalteter Prompt ist oder wahrscheinlich eher ein antrainiertes Verhalten.

Was ist dann der Unterschied zum inneren Dialog?

Der innere Dialog ruft halt nochmal das LLM auf.

Und es ist jetzt eine andere Ebene.

Das ist jetzt hier quasi so ein Überprüfen und keine Schlussfolgerung.

Ja, ein Experte könnte das jetzt genau erklären.

Ja, ich bin jetzt vor allem der Anwender.

Und wenn man damit arbeitet, dann merkt man eben so die Unterschiede.

Vor allem hier habe ich auch die Sache.

Ihr seht ja hier immer die unterschiedlichen Kästchen.

Und das ist immer wieder ein Call.

Das heißt, die Session, dieses Frage-Antwort-Spiel, das macht er hier mit sich selbst.

Und dadurch benutze ich den Kontext und ich benutze auch den Ausgabe-Kontext.

Weil ich habe den Session-Kontext.

Das müssten hier, glaube ich, 128.000 Token sein.

Und ich habe einen Ausgabe-Kontext.

Den habe ich in meinem System auf 4.000 Token, 4.096 gesetzt.

Und dadurch, dass er mit sich selbst redet, kann er eben viel mehr Output erzeugen, weil er immer wieder neu diese 4.000 Token nutzen kann.

Das mit diesen Experten, das kann ich mir irgendwie in der Praxis schon besser vorstellen.

Wenn ich quasi einen Programm-Code-Schnipsel schreibe, den dann übergebe und sage, hier kannst du mir das mal analysieren in Hinsicht auf Security und Wartbarkeit.

Aber wie sicher kann ich mir sein, dass er mich da jetzt nicht veräppelt?

Also ich kann ja auch jeden Satz anfangen mit, ich bin ein Experte für Security.

Und dann halt irgendwas sagen.

Ich habe am Ende trotzdem keine Garantie, dass es stimmt und muss am Ende trotzdem nochmal recherchieren.

Wie sicher bist du dir, wenn du deinem Kollegen eine Aufgabe gibst und sagst, komm, du hast doch hier Ahnung von JavaScript, kannst du mir das hier schreiben?

Und er zurückkommt und sagt, guck mal, hier ist es.

Ist ähnlich.

Und so langsam baut man dann auch Vertrauen auf, beziehungsweise wir haben ja noch das Know-how, um eben auch mal drüber zu gucken.

Und das werden wir auch gleich sehen.

Also er geht jetzt hierher und erzeugt jetzt die verbesserte Version.

Weiß, wir arbeiten Test-Driven.

Das heißt.

Er.

Ah, er stellt nochmal Tests für die verbesserte Version.

Und führt die Tests aus.

Alles grün.

Prima.

Und jetzt fängt er an.

Er will es mir erklären.

Baut das Diagramm und jetzt wird spannend.

Also erst mal.

Du hast nach dem dem Sinn gefragt.

Macht es wirklich.

Also Merge Sort macht ja keiner selbst.

Aber hier haben wir es jetzt geschafft, dass die Maschine nicht einfach sagt.

Hier ist der Code.

Kopier du ihn rüber und für ihn aus.

Und ich bin auf einmal ja nur noch der Handlanger der Maschine, der eben immer den Code rüber kopiert, aktualisiert, sagt es läuft so nicht.

Und hier ist der neue Code.

Das heißt, die Maschine kann Test getrieben arbeiten.

Und das finde ich sehr, sehr wichtig, weil in vielen Demos sieht man die Maschine hat hier Code erzeugt.

Und und jetzt bitte ich die Maschine, Tests zu erzeugen.

Und das ist Fallschwung.

Also wir wollen ja Test und Development und nicht Development und Testing.

Und deswegen finde ich das jetzt so so wichtig, dass wenn ich der Maschine einen Auftrag gebe, sie Test driften arbeitet.

Und hier wollte sie jetzt ein Diagramm bauen.

Und es ist nicht so gut gelaufen.

Die Maschine braucht einen Feedback Loop und den kriegt sie hier, weil sie die Tools verwenden kann.

Sie benutzt wieder Mermaid und Mermaid ist ja eine JavaScript basierte Library.

Und ich hätte jetzt einfach diese Library in dieses Frontend reinsetzen können und diesen Code rendern können.

Dann hätte ich es gesehen und ich wäre zufrieden.

Ich habe es aber anders gemacht.

Dieses Generate Diagram Tool, das schickt den Code an Kroki Server und der Kroki Server.

Der liefert entweder ein Diagramm zurück oder eine Fehlermeldung.

Diese Fehlermeldung sieht die Maschine und sagt Oh, sorry.

Mermaid ist halt nicht.

Komme ich nicht mit klar.

Ja, ich probiere es jetzt mit Plant UML.

Und dann macht die Maschine das nochmal mit Plant UML.

Und jetzt hat sie ein anderes Problem gekriegt.

Aber sie wird kreativ.

Sie kriegt das Feedback, ob es geklappt hat oder nicht.

Und fängt dann an, notfalls, wenn es nicht klappt, andere Wege zu suchen.

Und diese anderen Wege, da wird sie wirklich kreativ, weil sie sucht verschiedene Fallback Ebenen.

Einmal hatte ich es, dass sie mir dann ein ASCII Art Diagramm zurückgeliefert hat.

Und bei einer anderen Aufgabe, wo sie mal eine Link Liste anschauen sollte und sie hat es nicht geschafft, sich nach außen zu connecten, hat sie mich auf einmal gebeten, du kannst du mal auf die Website gehen und dann mit Inspect gucken, wie der Link aussieht.

Das fand ich schon spooky.

Ich kann dir gerade mal noch was vorlesen, weil der Florian Polster hat über seine Erfahrungen mit LLMs schon gesprochen.

Das ist ganz interessant.

Er schreibt, ich verwende LLMs erfolgreich beim professionellen Programmieren.

Voraussetzung ist, dass man der KI genug Kontext geben kann, damit sie ihre Aufgabe erfüllen kann.

Dann sagt er, schreibt mir, meine Tests für die Klasse in Datei X funktioniert.

Füge das neue Feature in den hunderttausend Lines of Code Monolithen ein.

Funktioniert nicht.

Also danke Florian fürs Teilen.

Ich finde es cool, dass es schon auch sinnvolle Verwendung gibt und nicht nur Merge Sort.

Und Ralf, eine Frage von Eberhard aus dem Off.

Das ist ja alles ganz schön, aber er würde gerne wissen, wie man das GPT-Chat zum Laufen bringt auf seinem eigenen Rechner.

Ja, guter Punkt.

Ich würde ganz gern noch eine Demo machen wollen.

Aber du musst uns versprechen, dass du es am Ende erklärst.

Ich glaube, sonst ist Eberhard traurig, wenn er das heute nicht mehr rausfindet.

Ja, da kommt noch ein Hinweis dazu.

Ich will ihn nochmal sortieren lassen.

Schreibe eine Sort-Methode in Python und führe sie mit folgendem Test aus.

Und jetzt habe ich eine besondere Sortierung.

Ich sage, wo sind meine Tasten da?

1, 2, 3, 4 soll sortiert werden zu 3, 1, 4, 5.

Ich denke mir bei diesen Experimenten immer so ein bisschen komische Sortierreihenfolgen aus.

Und hier habe ich mir gedacht, naja, ich nehme die Zahlwörter, sortiere sie alphabetisch und das soll meine Sortierreihenfolge sein.

Das kann ja mit nur einem Beispiel.

In der Schule hätte man mehrere bekommen.

Sorry, dass ich heute so oft Schule sage.

Ich weiß auch nicht.

Ja, das stimmt schon.

Aber du hattest vorhin gesagt, kann ich dem Ganzen jetzt vertrauen, dass er nicht einfach was Triviales macht?

Er könnte jetzt einfach eine Sort-Funktion nehmen und sagen return 3, 1, 4, 2.

Oder er sagt, das geht nur für Arrays mit genau vier Dingern und ich muss immer das dritte an die erste Stelle packen, das erste an die zweite, das vierte an die letzte.

Ja, guck mal, Custom Sort, Position Map.

Ja, also es geht genau in die Richtung und da schreibt er jetzt einen Test.

Aber ich sag mal so, also hättest du mir jetzt diese Aufgabe gegeben, ich hätte dir ja auch nur Quatsch gesagt.

Ich hätte ja auch nicht verstanden, was du überhaupt von mir willst.

Ich hätte ja auch mindestens ein paar Beispiele gebraucht oder halt die Beschreibung.

Ja, aber genau, die Maschine ist teilweise wirklich schlau und sagt, also ich habe es auch schon erlebt, dass sie gesagt hat, okay, wir vermischen jetzt einfach die Zahlen so und so nach dem und dem Schema.

Ich habe auch schon erlebt, dass sie tatsächlich diese Schemas erkannt hat, ganz unterschiedlich, wie das läuft.

Aber was jetzt hier spannend ist, ist tatsächlich die Tests, weil ja, dieser Sort-Algorithmus, der ist Murks.

Die Tests sind trotzdem grün, ja, weil er eben auch den Test dem Ganzen angepasst hat und da kann ja nichts rauskommen.

Und das ist dann eben auch das, wo man darauf achten sollte, dass, wenn ich die Tests hinterher schreibe, die Maschine guckt sich genau die Methode an, weiß, was die Methode macht und schreibt dementsprechend die Tests.

Deswegen müssen wir gerade mit der Maschine darauf achten, dass wir eben die Tests vorneweg schreiben lassen.

Schreibe ein paar mehr Tests und höre sie aus.

Aber auch dann weiß sie doch gerade immer noch nicht, was du überhaupt willst.

Genau, aber im Idealfall kommt sie jetzt dazu, dass sie eben weiß, das ist ein Sortier-Algorithmus, ich überprüfe das Verhalten.

Ich schreibe jetzt mehr Tests und merke, ja, irgendwie passt meine Implementierung nicht.

Okay, ich bin immer noch skeptisch.

Also sie könnte natürlich jetzt auch mehr Tests schreiben und merken, Implementierung passt, weil sie einfach den gleichen Quatsch nur in anderen Reihenfolgen macht.

Hat sie das gerade auch gemacht?

Das freut mich.

Das ist ja genau mein Gedankengang.

Ich wusste ja nicht mal, was du von mir wollen würdest.

Wieso sollte sie das dann wissen?

Aber die richtigere Reaktion wäre ja gewesen, auf Basis deiner Informationen kann ich nichts Sinnvolles programmieren.

Bitte gib mir mehr Informationen, oder?

Genau, und da ist die Maschine noch relativ schlecht, dass sie mir nicht so Rückfragen stellt.

Also ich kann ihr sagen, sie soll Rückfragen stellen, aber sie macht es nicht so gerne.

Also selbst, wenn ich es ihr vorgebe, und das ist jetzt hier ein typisches Beispiel, dass ich falsch an die Aufgabe rangegangen bin und die Maschine einfach Quatsch macht.

Aber was wir eben auch sehen, ist, dass der Feedback-Loop für die Maschine wichtig ist.

Ich glaube, wir hatten jetzt hier wieder, dass er ein Diagramm generiert und hier hat es geklappt.

### Feedback Loops in KI-Systemen

Aber dieser Feedback-Loop, dass die Maschine erkennt, ob sie etwas richtig gemacht hat oder falsch und sich eben nochmal korrigieren kann, ist ganz wichtig.

Und auch dieses weitere Tooling, weil als Architekten wollen wir halt tatsächlich mit Diagrammen arbeiten.

Und da ist dann dieser Ansatz, dass die Maschine textuellen Diagrammen beschreiben kann, uns aber visuell anzeigt.

Ideal, weil die Maschine damit das Diagramm erzeugen kann und umgekehrt, wenn solch ein Diagramm in der Dokumentation drin ist, sieht die Maschine das Diagramm wieder als Code und kann es viel leichter verstehen, als wenn ich es ihr als Grafik reingebe.

Und diese Feedback-Loops, an denen müssen wir halt wirklich arbeiten, dass wir die immer schön hinbekommen.

Wollte ich auch nochmal ein kurzes Beispiel machen, weil es ist gerade so ein bisschen, es gibt den Operator von OpenAI.

Wenn ich 200 Dollar im Monat zahle, dann habe ich einen Browser zur Verfügung, kann mit dem arbeiten.

Tolle Sache.

Es gibt auf Deep Learning AI ein 1-Stunden-Tutorial, was euch erklärt, wie man diese sogar Computer-Usage implementiert.

Und wenn ich jetzt zum Beispiel sage, ich gehe auf die Seite von Software-Architektur im Stream.

T.

Martin hat es auf YouTube gerade schön zusammengefasst.

LLMs sind und bleiben People-Pleaser.

Ja, das stimmt.

Aber wenn wir das wissen, können wir damit umgehen.

Hier finde ich es jetzt interessant, die Maschine nutzt das Weltwissen, dass sie weiß, Software-Architektur im Stream, kenne ich doch, dieses bekannte Format und die URL ist software-architektur.tv.

Geht auf diese Website drauf und ja, Browser.

Ich könnte ihn jetzt hier irgendwo klicken lassen, um zu sehen, was ist die nächste Folge oder was war die letzte Folge mit, keine Ahnung.

Das Spannende ist aber, er sieht diese Seite und ich kann wieder einen Feedback-Loop aufbauen, weil ich jetzt sagen kann, baue mir diese Seite in HTML nach.

Und früher war das ja so, dass die Bilderkennung, die hat halt auf dem Bild erkannt, ja Fahrrad, Hund, Auto.

Das wurde als Text reingegeben und ich konnte nicht fragen, was für ein Hund ist das?

Welche Farbe hat das Fahrrad?

Und das ist jetzt anders, weil dieses Bild in das Modell reingeht und das Modell kann sich das Bild angucken und dann baut es hier die HTML-Seite und ich kriege hier eine Vorschau.

Die Vorschau sieht es nicht direkt, aber das ist, finde ich, ziemlich nah dran.

Also das beeindruckt mich aber gerade nur mäßig prächtig, weil das hat ja quasi die komplette HTML-Seite als Code vorliegen und die dann copy-pasten das jetzt nicht so beeindruckend.

Nein, das hat sie jetzt tatsächlich nicht gemacht, weil ich ihr tatsächlich hier im Browser nicht die HTML-Seite gebe.

Da ist der Kontext schnell voll.

Also wir haben dieses Diagramm, wie groß sind die Webseiten geworden.

Wenn ich das in den Kontext reinwerfe, dann ist der Kontext sofort voll, kann ich nicht mehr mit arbeiten.

Deswegen kriegt sie hier tatsächlich nur das Bild und arbeitet aus dem Bild und ich könnte jetzt hier tatsächlich hergehen und ihm sagen, du speichert das mal ab als File, starte im Hintergrund einen Python-Web-Server und guck dir die Seite an.

Und dann fängt er an zu iterieren.

Dann sagt er, der Farbverlauf, den habe ich nicht so ganz hingekriegt.

Moment, ich probiere noch mal.

Und solche Geschichten.

Genau, dieser Streifen.

Und damit kriege ich dann wieder den Feedback-Loop hin.

Und der war bei meinen letzten Experimenten bei dem Visuellen so stark, dass er gearbeitet, gearbeitet, gearbeitet hat, bis der Kontext voll war.

Der erkennt dann auf so einem Screenshot, oh, da habe ich ein broken Image.

Da muss ich noch mal gucken.

Wie kann ich das fixen?

Und das ist zu weit rechts und und und und.

### Bedeutung für die Entwicklung

Das ist für die Softwareentwicklung, finde ich, echt ein starkes Tool, was was daraus entstehen kann.

Ja, so, Eberhard wollte wissen, wie kann ich das selbst machen?

Also.

Die eine Lösung ist, ich gehe in eins der Systeme und sagt dem System, schreibt mir mal so ein Chatshub-Clone in Python.

Dann werde ich 200 Zeilen Code kriegen und dann habe ich die Grundlage und dann gehe ich damit weiter vor.

So habe ich das gemacht.

Also, als ich damit angefangen habe, konnte ich noch kein Python.

Ich kann es immer noch nicht, weil ich vertraue der Maschine, die codiert für mich.

Was aber total cool ist, ist das Model-Kontext-Protokoll.

Und ich rufe das mal kurz auf.

Du musst uns gleich allen noch einen Gefallen tun mit Claude, aber erzähl das weiter.

Okay.

### Model-Kontext-Protokoll

Das ist von Entropiq, den Machern hinter Claude.

Die haben sich gedacht, ja, dieses Tool-Usage, dieses Function-Calling ist total cool.

Wie können wir das vereinheitlichen?

Und sie haben sich das Model-Kontext-Protokoll ausgedacht.

### Architektur

Das heißt, wenn wir jetzt mal hier in die Introduction gucken, dann haben wir hier einen Host und da läuft das Chat-Frontend.

Und wir haben dann verschiedene Model-Kontext-Protokoll-Server.

Das wäre zum Beispiel meine Python-Umgebung, die was ausführen kann.

Und dann kann der Chat hier vorne, hat die Connection rüber, erkennt, aha, ich kann hier was ausführen.

Ich mache das mal.

Ich führe das hier aus.

Ich kriege das Ergebnis zurück.

Ich habe hier ein standardisiertes Protokoll.

### Implementierung

Momentan läuft das nur lokal.

Das Protokoll ist nur lokal definiert.

Das heißt, ich brauche eine lokale Umgebung, in der ich das ausführen kann, in der ich das nutzen kann.

Und von Claude gibt es eine Desktop-Version und die kann das.

Da konfiguriere ich das System.

Ich habe hier zwei Tools liegen.

Hier sind zwei.

Das sind Demo-Tools, Add-Node und Search-Nodes.

Und guckt ihr die mal an, dann holt er sich die Beschreibung der Tools, gibt das in den System-Kontext, weiß dann, dass er was damit machen kann.

Und ja, ich könnte ihm jetzt hier sagen, benutze mal das, notiere dir mal Folgendes und er macht das.

Was hier wieder total cool ist, dieses Tutorial.

Wenn ich jetzt meine Tools, meinen Browser in diese Welt bringen will, Browser muss ich nicht mehr reinbringen, weil hier gibt es ganz viele Example-Servers und da gibt es z.B.

Google Drive, da gibt es GitGitHub, da gibt es Puppeteer, Browser Automation.

Habe ich hier schon alles vorgegeben.

Das heißt, ich kann das einfach hier an Claude Desktop dran flanschen, auch an andere Tools.

Zum Beispiel gibt es hier Example Clients, da gibt es Client als Plugin für Visual Studio Code.

Aber wenn ich eben eine neue Idee habe, z.B. den Croquiserver, dass ich Diagramme erzeugen kann, dann gehe ich hier ins Tutorial und die sagen, ja benutzt doch Claude z.B. als LLM.

Du gehst hier auf diesen Text.

Das ist die Dokumentation, die Claude braucht, um dir einen Server oder ein Client zu bauen.

Das gibst du rein in den Kontext und dann beschreibst du deinen Server und Claude wird dir diesen Server erstellen.

Das finde ich total cool, dieses Weitergedachte.

Ich habe jetzt nicht hier ein Tutorial, wo ich als Entwickler mir überlege, wie gehe ich damit um, sondern ich habe hier ein Tutorial für die Maschine und ich beschreibe nur noch der Maschine, was ich haben möchte.

Okay, aber dein Tool selber ist nicht Open Source und Eberhardt kann sich das einfach installieren?

Das Tool ist momentan nicht Open Source.

Das ist zu schlecht.

Da sind zu viele Bugs drin.

Ich habe mal die Maschine gefragt.

Ich habe ihr den Source Code gegeben, hier mit dem Container und ich habe da so einen Sandbox User, dass er die Bash nutzen darf und ich habe die Maschine gefragt, ist das eigentlich sicher genug mit dem Sandbox User im Container.

Die Maschine hat gesagt, es ist eigentlich nicht so sicher, da sollte es einen anderen Weg gehen und hat mir auch tatsächlich zwei, drei Vorschläge gemacht, welche Libraries ich da nutzen kann.

Ich habe gerade noch so einen anderen Gedankengang, aber ich glaube, ich kann es mir auch selber beantworten.

Könnte das hilfreich sein in Zukunft, wenn immer mehr COBOL Programmierer vom Markt gehen, aber immer mehr Bestandssoftware in COBOL noch verfügbar ist und gewartet werden möchte?

Kann die Maschine dabei vielleicht helfen?

Meine Antwort wäre, es ist wahrscheinlich schwierig, weil die COBOL Dokumentation im Internet ist auch eher mäßig prächtig.

Genau, aber ich glaube, wenn ich ihm jetzt einen Code Interpreter für COBOL mitgeben könnte und er dann eben nachträglich seine eigenen Tests schreiben kann, basierend auf dem Code, den er sieht, kann er sagen, Mist, ich habe keine Tests für diesen Code.

Deswegen schreibe ich mir jetzt erst meine Tests, überprüfe die Tests, dass sie auch grün sind, dass sie das Verhalten dieses Codes tatsächlich verifizieren und ich dann eben in eine andere sprachliche Welt rübergehe mit diesen Tests und ihn dann, ja, den Code rüberziehen lassen.

Ich glaube, da gibt es Möglichkeiten, wenn wir eben diese Feedback Loops implementieren.

Und spannend wird es halt wirklich, wenn man anfängt, immer darüber nachzudenken, wie kann ich ihm die richtigen Tools für diese Feedback Loops geben?

Martin wünscht sich auf Twitch MCP für die DocToolChain.

Also hast du schon eine Idee, was du am Wochenende basteln kannst?

Die DocToolChain, da gibt es auch noch ein spannendes Problem, weil die LLMs haben irgendwie die alte Dokumentation von der DocToolChain aufgegriffen.

Das heißt, ich werde jetzt wahrscheinlich erstmal so einen Ansatz wie hier fahren, dass man die Dokumentation als extra, als Kontext dem Modell mitgeben kann.

Und ja, ich meine, also ich habe einen System Prompt in meinem System, dass das Modell, wenn es Dokumentation erzeugt, bitte immer AsciiDoc erzeugt, was eben in Richtung DocToolChain geht.

Es kann mir die Diagramme erzeugen, es kann mir AsciiDoc mit Diagrammen erzeugen und genau in diese Richtung geht es, dass ich jetzt meine Architekturarbeit mit der Maschine machen kann, unterstützt.

Und da wollte ich eigentlich hin, genau.

Und jetzt musst du noch eine Sache mit Claude bitte beantworten, weil ich komme aus dem Schmunzeln hier gerade nicht mehr raus.

Kannst du Claude mal bitte fragen, welches Pronomen Claude präferieren würde?

Da gab es eine sehr amüsante Diskussion.

Also Diskussion ist oft zu viel gesagt hier im Chat.

Jetzt müssen wir alle gespannt sein und dann kann ich dir noch die Highlights aus dem Chat gleich einmal vorlesen.

Und Eberhard betont heute ist Folge 250.

Er kann sich also mit allem identifizieren.

Okay, das war jetzt eine traurige Antwort.

Ja, ich finde es immer schwierig.

Es kommt immer diese Frage.

Ich sage meistens gern die Maschine oder der Roboter.

Ich fand das ziemlich lustig.

Wo war das jetzt?

Ich muss das mal gerade finden.

Eberhard hat geschrieben, dass es schwierig ist, wenn man eher sie sagt, wenn man dann leicht das personifiziert und dann vielleicht nicht mehr so skeptisch dem Ganzen gegenübersteht.

Und Ingo Eichhorst hat da einfach mein heute Lieblingskommentar.

Florian hat geschrieben, Eberhard, ich würde es nicht zerdenken.

Zu meinem Hamster sage ich auch, sie, er und erwarte keine menschlichen Qualitäten.

Und in meinem Kopf ist jetzt einfach die KI ein kleiner Hamster und ich finde das Bild einfach großartig.

Genau und bevor ich es vergesse, weil ich habe es am Anfang vergessen, liebe Leute da draußen.

Am Montag, das ist der, ich muss spicken, 17.

Februar ist die KI und Software Architektur Unkonferenz.

Wir werden in einem Open Space Format von 14 bis 18 Uhr alle möglichen Themen rund um KI mit euch zusammen diskutieren.

Ihr könnt euch dafür anmelden und zwar könnt ihr auf LinkedIn euch zu dem Event anmelden.

Damit habt ihr es aber noch nicht geschafft, weil das ist ein Zoom Event und ihr müsstet euch auch einmal bei Zoom registrieren, dass ihr dann auch wirklich dabei seid.

Das Ganze wird nicht aufgezeichnet, weil es sich um eine Unkonferenz handelt und wir einfach gucken, was passiert.

Weil das, was passiert, ist genau das Richtige, ganz nach dem Motto einer Unkonferenz.

Genau, Ralf, ich klaue dir jetzt dein Screen nochmal, dass wir jetzt nur noch so zu sehen sind, weil es ist schon ganz, ganz kurz vor Ende und möchtest du noch irgendein spannendes finales Abschlusswort an alle richten?

Dann nutze ich die Zeit doch nochmal ganz kurz, weil jetzt haben wir nur über den Sort-Algorithmus gesprochen.

Es gibt ein Projekt, den ASCII-Doc Linter in dem Doc-Tool-Chain-Space.

Den hat die KI komplett selbst entwickelt, Test-Driven mit Architektur-Dokumentation, Manual, Readme, Test-Results, Test-Coverage.

Also es geht auch größer und jetzt ist die Frage, wie groß geht es?

Ich glaube, das ist die Zukunft und Feedback ist jederzeit gerne willkommen.

Danke für die Aufmerksamkeit.

Danke, dass ihr dabei wart.

Danke, Ralf, dass du das heute gemacht hast und war auf jeden Fall lustig und spannend anzusehen.

Ich habe mich über die Kommentare auch gefreut, die so reinkamen und ich freue mich schon, euch alle am Montag bei der Unkonferenz wiederzusehen.

Genau, dann würde ich mal sagen, vielen Dank und bis bald.

Tschüss.

Ciao.
