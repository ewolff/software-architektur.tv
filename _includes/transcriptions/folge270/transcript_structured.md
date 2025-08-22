# Folge 270 - Open-Source-Komponenten richtig im Projekt oder Produkt verwenden mit Prof. Dirk Riehle Eberhard, super, vielen Dank, dass ich dabei sein darf.

Ja, genau, freut mich.

Du bist ja auch nicht das erste Mal dabei.

Wir hatten damals die Episode über Inner Source.

Genau, und das war eine spannende Sache.

Und ich hatte mir gedacht, dass wir jetzt noch mal sprechen über das Thema Open Source Komponenten richtig im Projekt oder Produkt verwenden.

Dirk, willst du erst mal zwei Worte über dich sagen, was du so machst, wer du bist?

Klar, sehr gern.

Also mein Name ist Dirk Riehle.

Ich bin Professor für Informatik an der FAU Erlangen Uni Erlangen.

Habe lange in der Wirtschaft gearbeitet.

Und jetzt bin ich Professor Lehre Software Engineering mit einem Fokus auf Open Source Software.

Betreibe das in der Forschung.

Mein persönliches Anliegen ist allerdings, über die Forschung hinaus Startups, Hightech Startups zu generieren.

Und ein Großteil meiner Zeit geht auch genau dahin, mit meinen Teams Produkte an den Markt zu bringen.

Jenseits des Forschungsprojekts natürlich.

Genau, super.

Ja, und das Thema sind ja Open Source Lizenzen.

Also was sind denn Open Source Lizenzen überhaupt?

Gute Frage.

Muss man, sollte man auch als erstes klären.

Naja, ## Definition von Open-Source-Lizenzen

Software ist halt erst mal ein Artefakt, Source Code halt.

Und du, man bekommt, du bekommst Rechte, Nutzungsrechte über eine Lizenz.

Da gibt es die kommerziellen, proprietären Lizenzen, aber eben auch eine Kategorie von Lizenz, also Vertrag zwischen Softwareentwickler und Nutzer der Software.

Und so ein Vertrag, eine Open Source Lizenz, dann ist eine Lizenz, ist genau dann eine Open Source Lizenz, wenn sie bestimmte Bedingungen erfüllt.

Die sind auf der Webseite der Open Source Initiative definiert, die auch der de facto Arbeiterentscheider darüber ist.

### Grundlegende Rechte

Und konkret heißt das, eine Open Source Software Lizenz gibt dem Empfänger das Recht, die Software kostenfrei zu nutzen, im Quelltext zu erhalten, modifizieren zu dürfen, auch modifiziert weiter, unmodifiziert und modifiziert weiterzugeben.

Es kommen auch meistens dann Verpflichtungen noch dazu.

Und während die rechte Zusprechung praktisch immer dieselbe ist, variiert es bei den Verpflichtungen sehr stark.

Also programmierter Code, Source Code, wird dann zu Open Source Software, wenn er mit einer Open Source Lizenz kommt.

Und eine Open Source Lizenz muss halt mindestens mal diese rechte Zusprechung enthalten, kostenfreie Nutzung und so weiter.

Und da gibt es ja jetzt insbesondere, glaube ich, oder was vielleicht auch später noch ein Thema sein wird, ist ja irgendwie diese GNU Public License, Copyleft.

Und im Zusammenhang damit steht, glaube ich, auch dieses Thema mit dem Derivative Work.

Magst du darüber noch was sagen?

### Lizenztypen

Ja, also Open Source Lizenzen, es gibt so 100 Lizenzen, die anerkannt wurden, als offizielle Open Source Lizenzen von der Open Source Initiative.

50 sind, also ein guter Teil ist auch in den Ruhestand versetzt worden.

50 sind vielleicht aktiv, so richtig viel genutzt sind 10 bis 20 maximal.

Die bekannteste Lizenz ist die MIT Lizenz und die fällt in die sogenannte Kategorie permissive Lizenz.

Heißt konkret, um zu deiner Frage zu kommen, kein Copyleft-Effekt.

Man klassifiziert also Open Source Lizenzen, diese 100 Stück, danach, ob sie einen Copyleft-Effekt beinhalten oder nicht.

Was ist das jetzt?

Der Copyleft-Effekt ist eine Klausel, am prominentesten, dadurch wurde sie bekannt gemacht, eben in der GNU Public License Version 2, die du angesprochen hast, also eine konkrete Lizenz, die das erste Mal eine Copyleft-Klausel beinhaltete.

Und diese Copyleft-Klausel ist eine Verpflichtung für den Empfänger von Open Source Code.

Und ich habe ja eingangs gesagt, man kriegt diese Rechte, das ist ganz toll.

Und dann muss man aber diese Verpflichtung erfüllen, um die Rechte auch tatsächlich zu bekommen.

Also du kriegst die Rechte nicht, wenn du nicht die Verpflichtung erfüllst.

Und die Copyleft-Klausel oder die Copyleft-Verpflichtung ist genauso eine Verpflichtung, die für viele Softwarehersteller dann besonders schwierig ist, weil sie nämlich verlangt, dass unter bestimmten Umständen der Empfänger von deinem Code, wo sich dein Open Source Code und deine Copyleft-Klausel drin verbirgt, das Recht hat, deinen Quelltext einzufordern.

Und wie funktioniert das?

Du hast einen Open Source Programmierer, also wir müssen jetzt über drei Parteien nachdenken, das ist ja nicht ganz trivial.

Es gibt einen Open Source Programmierer, der stellt seine Software unter der GNU Public License Version 2 zum Beispiel zur Verfügung.

Damit wird es eine Open Source Software mit einer Copyleft-Verpflichtung.

Ein Hersteller jetzt zum Beispiel nimmt diese und verbaut diese Komponente vom Open Source Programmierer in einem Produkt, neben vielen anderen Komponenten.

Nutzen darf man Copyleft-lizenzierten Code immer.

Aber was ja ein Hersteller macht, er gibt den Code in Form eines Produktes an eine dritte Partei weiter.

Und hier ist jetzt der Kicker, der Copyleft-Lizenz.

### Auswirkungen des Copyleft

Bei entsprechender Kopplung des Copyleft-lizenzierten Codes im Produkt, hat der Kunde, der Empfänger, die dritte Partei das Recht, vom Hersteller einzufordern, nicht nur den Quelltext der Copyleft-lizenzierten ursprünglichen Open Source Bibliothek, sondern auch den Quelltext des Programmcodes, den der Hersteller dazu geschrieben hat.

Der ja üblicherweise oder häufig, nicht immer, aber häufig als Proprietär gilt, als Kronjuwelen auf Basis dessen man sein Geschäft betreibt.

Du hast auch schon gleich angesprochen, dass es hier ein Konzept der abgeleiteten oder des Derivative Work gibt.

Da wird es jetzt sehr schnell spezifisch, weil man muss genau hinschauen, wann wird denn diese Copyleft-Klausel ausgelöst.

Sie wird nicht immer automatisch ausgelöst.

Also wenn man jetzt zum Beispiel an einen Kunden ein unter GPLV2, also unter einer Copyleft-lizenziertes Binärdatei ausliefert, dann hat der Kunde das Recht, den Quelltext einzufordern.

Wenn man jetzt das eigene Programm separat davon ausliefert, also nicht integriert als eine Binärdatei, sondern separat davon, zum Beispiel in einem Verzeichnis einfach als Binary daneben, dann sind sie nicht gekoppelt im Sinne eines Derivative Work.

Es wird sehr schnell sehr spezifisch.

Kommt sehr schnell auf Programmiersprachen drauf an, Linking, wie was gekoppelt wird, aber ein Derivative Work folgt, wenn der proprietäre Quelltext mit dem Copyleft-Quelltext so gekoppelt wird, dass es nicht so einfach über Standardwerkzeuge auseinandergenommen werden kann.

Dann ist der proprietäre Code auch unter der Copyleft-Lizenz zu lizenzieren, wenn man diese Copyleft-lizenzierten Code nutzt.

Um es vielleicht zusammenzufassen, aus Sicht der Open-Source-Programmierer, die Copyleft-Lizenzen einsetzen, das tun ja nicht alle, aber die, die das gerne möchten, meistens unter dem Begriff freie Software dann statt Open-Source, diese möchten, dass sich ihre Lizenz, die sie gewählt haben, zum Beispiel die GPF2, fortpflanzt.

Die Idee ist, dass man nicht einschränken kann als Mittelperson, als Hersteller in der Mitte, was die Lizenzen sind, wenn an die dritte Partei eine Kundenweite gegeben wird.

Copyleft-Lizenzierung ist also eine Strategie der Propagierung des Fortpflanzen einer bestimmten Lizenz, eben der Copyleft-Lizenz.

Und das hat verschiedene, das hat manchmal moralische Gründe, das hat manchmal auch geschäftsstrategische Gründe.

Das beste Argument heute ist aus meiner Sicht, dass sich Kunden helfen können sollen, wenn es zum Beispiel Fehler gibt in der Software, ohne auf den Hersteller zurückgreifen zu müssen.

Und da kann man dann manchmal fragen, wieso sollen sich doch an den Hersteller wenden, aber das ist ja nicht immer so einfach und manchmal hat man gar keinen Vertrag mehr mit dem Hersteller.

Es wird besonders stark oder nachvollziehbar moralisch, wenn man so möchte, mit dem Right to Repair.

Du kaufst eine Waschmaschine und willst sie jetzt reparieren, da gibt es die physischen Komponenten, naja, aber die hat ja auch Software und wenn du an die gar nicht rankommst, weil du den Quelltext nicht hast, also mit anderen Worten, es gibt hier einen moralischen Anspruch.

Aber man sollte auch sagen, vor über 10, 15 Jahren waren die Copyleft-Lizenzen in Form der GPLV2 die am häufigsten neu vergebene Lizenz und das ist längst nicht mehr der Fall.

Heute führt die MIT-Lizenz, eine Lizenz, die keine Copyleft-Klausel beinhaltet, ganz deutlich an und ich würde sagen, es gibt eine Menge von Entwicklern, Entwicklerinnen, die wollen halt Copyleft aus verschiedensten Gründen, aber die permissiven Lizenzen live and let live, sozusagen, haben sich schon durchgesetzt.

Gut, danke erstmal für die Erläuterung, sozusagen.

Und diese Lizenzen sind ja auch tatsächlich Gegenstand von Gerichtsverfahren, wenn ich es richtig sehe.

GPL ist eben, ich glaube, sogar in Deutschland, wenn ich es richtig sehe.

Genau, es gibt zwei Bedrohungsszenarien, wenn man so möchte, für Softwarehersteller, die Open-Source-Komponenten in Produkten verbauen.

Man sollte dazu sagen, jeder Hersteller heute macht das, wäre ja völlig verrückt, alles von Neu, von Basis, das geht gar nicht.

Man hat Schätzungen von 80 bis 99 Prozent an Codes, Binär-Codes in einer Software mit Open-Source-Code.

Der ist dann nicht wettbewerbsdifferenzierend, jeder kann ja diesen Open-Source-Code haben und nutzen und die Wettbewerbsdifferenzierung ist halt das, was man so oben drauf schreibt, ja.

Aber über den gesamten Abhängigkeitsgrafen, über den wir vielleicht noch reden sollten, hat man halt jede Menge Open-Source-Code und dadurch muss man sich halt an die Verpflichtungen für diesen Open-Source-Code anhalten.

Das sind erstmal die Open-Source-Lizenzen und wenn da jetzt zum Beispiel Copyleft-lizenzierter Code drinsteckt, aber der Hersteller bei der Weitergabe entweder gar nicht realisiert hat, dass sich der Copyleft-Effekt per Derivative Work auf die eigene Arbeit ausgeweitet hat oder es bewusst ignoriert und so weiter, kann es ihnen passieren, dass sie tatsächlich verklagt werden.

Das ist das erste Bedrohungsszenario.

Hier ist es so, dass in der Historie des Open-Source immer mal so Einzelpersonen geklagt haben, die verärgert waren.

Meistens ging es dann um den Linux-Körnerl, der in weiten Teilen halt unter der GPL v2 lizenziert ist.

Das hat sich jetzt professionalisiert.

Da gibt es die Software-Freedom-Conservancy.

Die sammelt Donations, Gelder ein, um Musterklagen durchzuführen.

Musterklagen, um halt durchzusetzen, dass zum Beispiel der Copyleft-Effekt doch auch korrekt bitteschön von Herstellern, die von Open-Source-Code profitieren, sparen Geld, Qualitätssoftware, dann auch eingehalten wird.

Das ist das eine Bedrohungsszenario.

Das sind sozusagen eigentlich nur noch die Software-Freedom-Conservancy mit dem Ziel, doch sich bitte an die Lizenzbedingungen zu halten und das ist ja auch nachvollziehbar und gut so.

Es gibt ein zweites Bedrohungsszenario und das sind die Copyright-Trolle.

Die Software-Freedom-Conservancy, das kann man moralisch voll nachvollziehen.

Es gibt einen Anspruch und sie setzen ihn durch von Einzelpersonen gegenüber großen Unternehmen.

Dann gibt es aber auch die Copyright-Trolle.

Das sind im Wesentlichen Abzocker, die dadurch, dass sie mal irgendwo beigetragen haben und dann aber feststellen, dass ihre Rechte verletzt wurden, versuchen im Prinzip die Unternehmen, die ihre Rechte verletzen, abzumahnen.

Da ist aber jetzt so gemerkt, vielleicht ein Wechsel in der Moralität des Ganzen.

Diese Copyright-Trolle haben einen bestimmten Operationsmodus.

Die gucken auf dem Web nach Firmware oder was auch immer, wo vielleicht Programmierarbeit von ihnen, von Anno dazu mal drinsteckt.

Meistens ist es der Linux-Körner, zu dem sie halt mal beigetragen haben.

25.000 Personen haben im Laufe des ganzen Lebens, Lebenszeit des Linux-Körners zum Körner beigetragen.

Das sind viele Leute und gibt da auch einige, die dann sozusagen vom Glauben abgefallen sind oder einfach sagen, ja, jetzt will ich Geld verdienen.

Die gucken nach Verletzungen, die mahnen die Unternehmen ab, wo sie Verletzungen stattfinden.

Gucken dann, schicken den ganz normalen Abmahn-Schreiben, wie man das so kennt von Impressum oder ich weiß nicht was.

Das war ja mal so eine Welle in Deutschland und fordern dann ein, zahlt mir 5.000 Euro für die Aufklärungsarbeit, die ich hier geleistet habe.

Ein Unternehmen, das jetzt nicht aufpasst, würde vielleicht dann sagen, okay, ärgerlich, 5.000 Euro, immer noch viel Geld, aber vom Tisch und gut ist.

Was aber dieser sogenannte Copyright-Troll dann einfordert, ist natürlich die, wie heißt es so schön im Deutschen, strafbewehrte Unterlassungserklärung.

Ein schönes Rechtsdeutsch, wohinter sich aber verbirgt, dass, wenn das Unternehmen das unterschreibt, bei einer zweiten Verletzung der Rechte des Open-Source-Programmierers nicht mehr die Aufklärungskosten für die Abmahnung anfallen, sondern dann eben strafbewehrte Unterlassungen eingefordert werden.

Und in dem Strafbewert verbirgt sich dann halt ein sehr viel höherer Betrag.

Da gibt es also Leute, die tatsächlich mit Anwälten, also Open-Source-Programmierer, die sich mit Anwälten zusammengetan haben, um dann im Endeffekt über diese Abmahn-Schreiben erstmal Unternehmen in die Falle zu locken und dann mit einer zweiten Verletzung, die sie natürlich schon vorbereitet hatten und in der Hinterhand haben, dann diese Unternehmen vor Gericht zu zerren oder erstmal zu verklagen.

Und das scheint ein lukratives Geschäft zu sein.

Das ist ein Geschäft, das im Dunklen geschieht.

Niemand redet gerne darüber, weder die, die verklagt werden, noch die, die so ihr Geld verdienen.

Aber es ist eine reale Gefahr, diese Copyright-Rolle.

Eine Sache gab es im Chat.

Davon habe ich heute erfahren, dass die WTFPL die beste Lizenz ist.

Ist das eine Aufforderung?

Also ich kenne die Lizenz, aber jetzt hole ich mal ein bisschen aus und erläuter mal ein bisschen.

Das ist natürlich ein Scherz, wie man am Smiley erkennt.

Das ist eine Lizenz, eine von mehreren, die erstellt wurde von einem leicht genervten, denke ich mal, Open-Source-Entwickler, weil hinter dem, was ich geschildert habe mit Copy Left Effect und alle Software soll frei sein oder auch nicht, da haben sich die Leute wirklich gefetzt und gestritten und muss jede Software frei sein und so weiter und so fort.

Da gibt es halt auch Open-Source-Programmierer.

Auf eine gewisse Art und Weise ist das dann auch eine entspannte Erleuchtung, möchte ich mal sagen, weil die da einfach gesagt haben, was soll ich denn meinen Nutzern hinterhersitzen, um sie über Copy Left Klausel zu zwingen, ihren Quelltext offenzulegen.

Macht doch mit meinem Quelltext, was ihr wollt.

Ein Mach doch, was ihr wollt ist keine Open-Source-Lizenz, aber dahinter steht schon die Idee.

Ich programmiere hier, ich habe Spaß, ich lege das offen, vielleicht kriege ich Beiträge, habe eine Community, habe noch mehr Spaß.

Die Software wird schneller, besser und so weiter.

Ja, die Vorteile einer aktiven Open-Source-Community ist mir doch egal, ob da jetzt jemand Geld verdient oder nicht, weil Open-Source-Software ist halt notgedrungen nicht wettbewerbsdifferenzierend, weil jeder kann sie unter der Open-Source-Lizenz nutzen.

Das heißt, dieser historische Kampf ist glücklicherweise etwas vorbei.

Dieses Software-Freedom-Conservancy, die sich halt die Copy-Left-Fahne hochhält, sagt sehr klar, es geht uns darum, dass die Bedingungen der Lizenzen eingehalten werden und trägt nicht mehr so vor sich her, alle Software soll doch bitteschön frei sein.

Das ist jetzt meine Meinung.

Ich finde es tatsächlich auch gut, dass man doch den Empfängern von Open-Source-Software einfach überlässt, ob sie beitragen wollen.

Das meinte ich mit erleuchtet.

Wenn man Software nutzt, fängt man irgendwann auch an, sich zu überlegen, okay, ich habe diese Abhängigkeit zu dieser Software, wie manage ich denn diese Abhängigkeit?

Erleuchtetere Software-EntwicklerInnen verstehen dann halt, dass sie diese Abhängigkeit managen müssen, vielleicht beitragen müssen und dann fließt auch gut zurück.

Eine Sache wollte ich noch kurz fragen.

Du hattest das ja vorhin schon gesagt, an einigen Stellen, dass Open-Source etwas mit Moral zu tun hat und vielleicht auch mit einer bestimmten gesellschaftlichen Haltung.

Tatsächlich ist es so, dass die CT im letzten Editorial aufgegriffen hat, dass der Musiker Moby Dinge lizenziert hat, Musikstücke, die er hat.

Auch hier ein kleines bisschen ausholen.

Also Open Source Lizenzen sind eine super rechtliche Innovation gewesen, inklusive Copy Left Effect und alles.

Das war so genial und höchst kreativ und innovativ.

Wir haben danach dann in den unterschiedlichsten Kontexten, zum Beispiel Wikipedia und Wikis und offene Daten, Variationen dieses Konzepts offenlegen, klare rechtliche Rahmenbedingungen schaffen und so weiter gesehen.

Und eine weitere Entwicklung von Open Source Software sind dann jetzt nicht offene Daten oder Wiki-Inhalte, sondern tatsächlich Software-Lizenzen.

Gibt da zwei Schlagrichtungen, Source Available und ethische Lizenzen.

Die ethischen Lizenzen, du hast jetzt Mobi, also Musiker angesprochen, das ist vielleicht keine Software, aber in der Software gibt es ethische Software-Lizenzen, die tatsächlich genau einen äquivalenten Anspruch haben, zu dem, was Mobi da gesagt hat.

Der Entwickler oder die Entwicklerin der Software möchte nicht unter einer Open Source Lizenz diese zur Verfügung stellen.

Essenziell in der Definition von Open Source Software, so ein bisschen, ein kleines bisschen noch komplizierter, als ich eingangs erläuterte, ist halt keine Diskriminierung nach Anwendungszweck, Anwender und Anwenderin und so weiter.

Man kann also nicht bei einer Open Source Lizenz sagen, nicht im Krieg zu verwenden oder nicht für Gentechnik zu verwenden.

Geht nicht, dann ist diese Lizenz, wo sowas drinstehen würde, keine Open Source Lizenz mehr.

Deswegen neuer Begriff, ethische Lizenzen.

Die gab es in der Softwarewelt jetzt auch schon seit 6, 7, 8, 9 Jahren.

Die Mobi-Geschichte war mir jetzt neu.

Ich würde verweisen auf Wikipedia.

Die das auf die harte Art und Weise haben lernen müssen, per Analogieschluss.

Dort gab es eine Diskussion, was denn die Wikipedia-Inhalte, wie diese denn bereitgestellt werden sollten.

Und man hat also dann überlegt, ob man nicht kommerzielle Nutzung nicht verbieten soll, also kommerzielle Nutzung nicht verbieten sollte.

Das geht über eine bestimmte Lizenz, das ist die Creative Commons mit der NC, Non-Commercial-Klausel, die auch gern mal verwendet wird.

Der klare Konsens im Wikipedia-Kontext, denke ich, ist bloß nicht, weil es einfach nicht definierbar ist, was denn nicht kommerziell bedeutet.

Und genauso würde ich bei Mobi vermuten oder bei den ethischen Lizenzen.

Es ist schlussendlich nicht definierbar, was genau damit gemeint ist.

Bevor es die ethischen Lizenzen gab, gab es zum Beispiel die JSON-Lizenz.

Das ist eine ganz tolle Lizenz, das ist im Prinzip die MIT-Lizenz, also sehr pflegeleicht in vielerlei Hinsicht.

Aber mitten in der JSON-Lizenz steht drin, diese Software darf nur für das Gute in der Welt verwendet werden und nicht für das Böse.

Man hat sich also dann jahrelang die Köpfe eingeschlagen, wie man das denn bewerten will.

Bei der JSON-Lizenz hat sich dann die Community mehr oder weniger geeinigt, das ist ein Low-Up, also hat keine Bedeutung.

Es ist äquivalent, ob dieser Satz dann entsteht oder nicht.

Und ich denke, das kann einem bei den ganzen ethischen Lizenzen auch passieren.

Worauf dann aber die Antwort der Erfinder dieser ethischen Lizenzen war, mag sein, aber wir wollen, dass sich die Leute damit auseinandersetzen und dass auch eher eine Abschreckung stattfindet, wenn dann ein Unternehmen kommt, das sich gar nicht so sicher ist, ob man dann Ärger bekommt, dann ist es vielleicht auch gar nicht das richtige Unternehmen, das die Software nutzen sollte.

Mit anderen Worten, die Lizenzen an sich funktionieren nicht so richtig, es sei denn, man sagt, es geht um eine Abschreckungswirkung und das ist auch mein letzter Stand der Dinge in dieser Debatte.

In der Software ist diese Debatte jetzt schon ein paar Jahre alt.

Mobi, wie gesagt, kannte ich nicht.

Ja, war, glaube ich, auch brandneu.

Vielleicht noch ein Hinweis in eigener Sache, also das ganze Zeug, was heute im Stream ist, haben wir unter Creative Commons Attribution gestellt und tatsächlich haben wir es jetzt, ich habe es vor kurzem gerade gezogen, weil da irgendwie noch Share a Like stand und das hat unserem Ziel, glaube ich, nicht entsprochen, weil wir wollen, dass das Zeug weit verteilt wird und dann muss man das an der Stelle nicht unbedingt einschränken.

Also es ist überhaupt kein Problem, wenn man unsere Sachen benutzt und das steht irgendwie nicht so verhechtigt im Stream, das ist irgendwie fine und dann habe ich das Ganze in Abstimmung mit Ralf, Lisa und Martina einmal unter Attribution gestellt.

Ja, ich würde da gerne gerade was zu sagen, weil wir haben dazu übersprungen, was das Hauptproblem heute mit Open Source Lizenzen ist.

Das ist nämlich genau das, was du eben genannt hast, die Attribution Klausel.

Was ist das?

Wie gesagt, Open Source Lizenz gibt dir Rechte, aber dann auch Verpflichtungen.

Attribution ist eine der Verpflichtungen.

Was bedeutet Attribution?

Du musst halt sagen, dass du diese Komponente verwendest, wer sie programmiert hat und zwar in Form dessen, dass du das Copyright-Statement dieser Person weiterreichst.

Du musst nicht den Quelltext bereitstellen, es ist nur, von wem kommt das?

Moralisch Gift-Credit, ich nutze diese Komponente, aber du musst jetzt nicht irgendwie deinen Quelltext per Copyright-Klausel offenlegen, weil da ist keine Copyright-Klausel.

Das hat auch die MIT-Lizenz sehr populär gemacht, für das Copyright-Statement und auch den Lizenz-Text.

Klingt völlig harmlos.

Es sei denn, man schaut sich mal reale Software an.

Ich habe es schon erwähnt, der Linux-Körnel, 25.000 und plus Software-Entwickler, jeder Einzelne hat das Recht, ein Copyright-Statement da drin vergraben zu haben, in irgendeiner Datei.

Und jeder Einzelne, jeder Einzelne hat das Recht, dass, wenn man den Linux-Körnel auf irgendein Gerät packt und verkauft, dass dann dem Kunden dieses Copyright-Statement bereitgestellt wird.

Nur 25.000 Mal verteilt über den Quelltext im Zweifelsfall diese Copyright-Statements finden.

Dass die Attribution, die Lizenz-Texte, weitere Notizen usw.

Für den Linux-Körnel gibt es eine etwas allgemeinere Lösung, aber in einem Software-Produkt hat man ja einen großen Abhängigkeitsgraf mit vielen, vielen Komponenten, aus all denen fast alle Open-Source-Lizenzen haben als Verpflichtung doch give credit to who credit is due, eben die Attribution, das durchzuführen.

Und ich habe ein Training, in dem ich das alles vermittle, wie man das macht.

Es ist viel Arbeit.

Aber diese Arbeit muss man machen, sonst bekommt man nicht das Recht, dass einem über die Open-Source-Lizenz zugesprochen wird.

Kein Recht, ohne die Verpflichtung zu erfüllen.

Und während zwar nicht der eigene Quelltext in Anführungszeichen in Gefahr ist, wie bei der Copy-Left-Lizenz oder einer Copy-Left-Klausel, ist dabei die Gefahr da, dass man halt die Verpflichtung doch nicht erfüllt.

Und diese Copyright-Trolle, von denen ich vorhin sprach, die stellen sich auf Attribution ab, denen geht es fast immer nur um Attribution.

Ich habe hier programmiert, aber ich werde nicht erwähnt, man hat meine Rechte verletzt.

Punkto.

Ich habe unten auf der Webseite bei uns reingeschrieben, dass attributiert werden soll, also entweder ich, Ralf oder Lisa, und die jeweils Interviewten für die Videos und für die Sketch-Notes Lisa.

Von daher glaube ich, dass es manageable ist.

Wir haben da tatsächlich noch so ein ethisches Ding.

Da steht, Inhalte von Software-Artikel im Stream zu konsumieren, ist unfeinbar mit einer Unterstützung der AfD.

Ein ethischer Einsatz?

Genau genommen steht da ja, das ist ja nicht Teil der Lizenz, würde ich behaupten.

Das ist einfach nur so ein Hinweis.

Für mich ist das eher eine inhaltliche Geschichte.

Wir können nicht über Diversity in unserer Branche reden und gleichzeitig eine Partei unterstützen.

Das möchte ich korrigieren.

Es geht immer um die Intention des Software-Entwicklers, des Software-Entwicklerinnen oder euch, die Software-Architektur im Stream bereitstellen.

Wie gesagt, in meinem Training diskutiere ich das alles, aber der Punkt ist, du fängst mit einer offiziellen Lizenz an.

Das ist vielleicht auf GitHub, da steht dann MIT.

Es geht aber viele Schritte weiter.

Du musst in den Quelltext gucken, vielleicht steht da eine andere Lizenz drin.

Dann steht da vielleicht irgendwo FAQ und wir haben noch folgende Randbedingungen.

Die musst du eigentlich auch finden.

So wie du jetzt eine politische Aussage getroffen hast, die dem entspricht, was du möchtest.

Das muss man finden, sonst hat man nicht das Recht.

Es ist fürchterlich, wenn wir davon reden, dass du in einem Quelltext was finden musst.

Das ist viel Arbeit.

Das führt für mich zu der Frage, was bedeutet das für mich als Entwicklerin?

Wir haben gesprochen über die Gefahr mit den Copyright-Trollen.

Dann hast du gesprochen über die juristischen Dinge, dass ich die Rechte nicht bekomme.

Ich bin mir nicht sicher, ob das ein Problem von Entwicklerinnen ist.

Idealerweise hätte ich hoffentlich Menschen, die sich professionell darum kümmern.

Vielleicht bleibt es bei mir hängen.

Gibt es da noch weitere Themen?

Es ist erst mal korrekter Einsatz von Open Source und Produkten und Projekten.

Das ist erst mal ein Geschäftsproblem.

Wenn man die Lizenz ignoriert, das kann man heutzutage nicht mehr akzeptieren.

Das eskaliert zum Geschäftsführer.

Man ist nicht am Stand der Technik.

Wenn man ein Softwareprodukt vertreibt, das nicht Open Source-lizenzkonform ist.

Aber der Geschäftsführer wird es delegieren.

Bei größeren Unternehmen gibt es Open Source-Programme-Office.

Bei kleineren Unternehmen gibt es eine arme Person, die beauftragt wird, sich um Open Source zu kümmern.

Konsequenz ist, jemand muss sich kümmern.

Am Ende der Delegationskette kann es bei einem Entwickler oder einer Entwicklerin landen, die sich kümmern muss.

Das erhält viel Arbeit.

Wir können gerne diskutieren, was alles zu leisten ist.

Das ist die Software-Composition-Analysis.

Man muss sich ein umfangreiches Bild schaffen, was man alles verbaut, wenn man ein Produkt ausliefert.

Du bietest auch ein Training an.

Ich bin mir nicht sicher, ob wir da in die Tiefe gehen wollen.

Ich habe nicht mein Training beworben.

Aber Sensibilität für das, was Software-Composition-Analysis bedeutet, wäre hilfreich.

Dann spreche ich gerne aus.

Das Erste, was man verstehen muss, wenn man ein Software-Hersteller ist und 80 bis 99 % des Produkt-Codes sind zwar nicht wettbewerbsdifferenzierend, aber Open Source-Code, dann ist man für den zuständig.

Es ist immer wieder überraschend für mich, wie viele Unternehmen sagen, ich verbaue hier Open Source-Code, aber das haben andere programmiert und sind dann aus dem Open Source-Code erwachsen.

Das sind Lizenzbedingungen, das sind regulatorische Bedingungen dank Cyber Resilience Act usw.

Dafür, um denen zu begegnen, muss man erst mal genau verstehen, was man denn verbaut hat.

Entwickler und Entwicklerinnen mit einem sinnvollen Build-Tool Man weiß also, welche Bibliotheken man nutzt.

Das sind die First Level oder Direct Dependencies, direkten Abhängigkeiten.

Da hat man vielleicht mal hingeguckt, was die Lizenzen sind und wie man denen begegnet.

Dahinter ist der gesamte Abhängigkeitsgraf und den muss man auch verstehen.

Ich hoffe, bei dem einen oder anderen klingelt das jetzt, dass da ein ganzer Eisberg unter der Wasserlinie wartet, und um den muss man sich kümmern.

Da muss man sich alles anschauen, alle Lizenzen verstehen, sich an alle einzelnen Verpflichtungen halten.

Das führt für mich zu so einer Frage.

Vor ungefähr 14 Tagen gab es auf Mastodon einen Thread, der letztendlich gesagt hat, hier ist eine Bibliothek.

Diese Bibliothek hat erfahrungsgemäß schlechte Qualität.

Das hat offensichtlich dazu geführt, dass größere Qualitätsprobleme in Software-Systemen auftreten.

Jetzt ist das wieder passiert, wo jemand gesagt hat, dieser Entwicklerin, die dafür zuständig ist, sollte sich mal vernünftig verhalten und nicht qualitativ hochwertige Software bauen.

Dann kam zurück die Antwort, für mich auch nachvollziehbar, dass eine Abhängigkeit in einem Dependency-Grafen ein System zum Zusammenbruch bringt.

Dann hast du ein Problem, und du machst schlechtes Engineering.

Das, was du jetzt beschreibst, heißt nur, dass ich von meinem gesamten Dependency-Grafen alle Open-Source-Lizenzen verstehen muss.

Hier geht es noch einen Schritt weiter.

Ich versuche herauszufinden, welches Risiko ich habe.

Ich verstehe diese Aussage von dieser Person, die sagt, wenn eine kleine Random-Abhängigkeit ein System dazu bringt, dass es nicht mehr funktioniert, dann hast du ein Problem.

Aber was mache ich jetzt?

Hast du da einen konkreten Vorschlag?

Ich habe eher das Gefühl, die First-Level-Abhängigkeiten kann man noch relativ einfach auswechseln.

Bei Second- und Third-Level-Dependencies kann man natürlich auch dann die übergeordnete Abhängigkeit-Komponente klonen, fixen, versuchen, etwas zu ersetzen, aber das ist halt ausgesprochen mühsam.

Es stimmt, dass man über die Wahl seiner Abhängigkeiten eben von diesen auch abhängt.

Und was nicht gilt, ist, sich bei den Open-Source-EntwicklerInnen zu beschweren.

Man nutzt die Software, kriegt sie kostenfrei in den Lizenzen steht, dass die Entwickler keinerlei Verpflichtungen eingehen, keinerlei Garantien bereitstellen.

Und der schnellste Weg, sich öffentlich zu blamieren, ist, sich über Open-Source-Programmierer zu beschweren, die nicht schnell genug die Fehler beheben, weil die naheliegende Antwort ist, wenn das so hoch prior ist für dich, dann mach es doch selbst, dann hast du den Quell-Text.

Das ist richtig, man hängt davon ab.

Man muss potenziell sehr, sehr mühsam dann Lösungen finden oder eben im Endeffekt den Fehler selbst beheben.

Und das sollte man im Zweifelsfall auch machen und ist vielleicht ja auch gut, auf die Art und Weise, zum Open-Source beizutragen.

Was halt nicht geht, ist zu sagen, ist da irgendwie jemand anderes Code, den ich hier verwende, das geht nicht.

Ich muss die ganze Zeit auch an dieses Ex-KCD-Comic denken, wo nicht irgendwie dieses große Ding halt ist und das ist so ein kleiner Bestandteil und das ist halt ein Random-Open-Source-Projekt, nicht das große ist halt das Internet und nicht dieser kleine Bestandteil, das hat irgendwie eine Person und wenn der fehlt, bricht es halt zusammen.

Wir haben eine Menge an Kommentaren tatsächlich.

Also deine Erfahrung.

Gibt es derzeit eine zunehmende Verbreitung und Nutzung von SBOM-Dateien in Open-Source- und Closed-Source-Projekten beziehungsweise Produkten?

SBOM ist dieses Bill of Materials.

Wie ist da dein Gefühl?

Hat das eine Auswirkung?

Sehr gern.

Also ## Software Bill of Materials (SBOM)

SBOM steht für Software Bill of Materials, ist ein Inventar, ist im Prinzip dein Abhängigkeitsgraf als eine flache Liste.

Mit anderen Worten, du kriegst sozusagen eine Bestandsaufnahme aller Komponenten, die in einem Produkt verbaut sind.

Open-Source-Projekte bieten das üblicherweise nicht an.

Das wäre sehr hilfreich, aber ist halt zusätzliche Arbeit und wenn man keine Lust dazu hat, macht man es halt nicht.

### Bedeutung für Unternehmen

Für kommerzielle Produkthersteller ist es zunehmend zu einer Verpflichtung geworden.

Also kommerzielle Produkthersteller sollten es eigentlich anbieten.

Sollten, weil es unterschiedliche Quellen gibt, aus denen es gefordert wird.

Es ist also noch nicht so universal im Gesetz, dass man SBOM ausliefern muss, aber zum Beispiel die vorige US-Regierung hat per Cyber Security eingefordert, dass wenn man an ein US-Ministerium verkauft, die Software doch bitte schön mit SBOM kommt.

Also mit Inventar aller verbauten Komponenten.

Dahinter stecken jetzt nicht die Open-Source-Lizenzen, sondern Sicherheitsbedenken.

Wenn also ein US-Ministerium irgendeine Software in ihrem eigenen Rechenzentrum betreibt, möchte man doch sehr genau wissen, welche Open-Source-Komponenten da verbaut sind, für die vielleicht später im Betrieb Sicherheitslücken bekannt werden.

Soll heißen, smarte Nutzer, das ist der erste Schritt, überwachen die betriebene Software auf neu hin bekannt gewordene Sicherheitslücken.

Und damit sie das können, müssen sie erstmal wissen, was da verbaut wurde.

Dass da irgendwo Lock4J oder sonstiges drinsteckt in der Software, die sie verwenden.

Das ist in den USA eine Richtlinie oder eine Anforderung für ein US-Ministerium geworden, wenn man in einer großen Lieferkette steckt.

Zum Beispiel die deutschen Automobilhersteller.

Also Automobilhersteller sind mit die Vertreiber von den größten Software-Komponenten-Systemen überhaupt.

Im Sinne von wird physisch ausgeliefert.

Das ist nämlich der Infotainment-Stack im Auto.

Die zentrale Konsole da.

Da läuft viel mehr Kode als auf meinem Laptop hier zum Beispiel.

Und weil das halt ein physisches Ausliefern ist, muss man sich halt an die Open-Source-Lizenzbedingungen halten.

Und deswegen wollten die Automobilhersteller schon lange, bevor jetzt irgendwelche Ministerien aufgewacht sind, wissen, was denn aus der Software-Lieferkette bei ihnen ankommt und im Endprodukt an Kunden ausgeliefert wird.

Also Bedrohungsszenario ist tatsächlich mal wieder Attribution.

Stell dir vor, du bist stolzer Mama, stolze Mama, stolzer Papa.

Willst deinen Kindern zeigen, guck mal, ich habe im Linux-Körnerl oder in folgender Bibliothek mitgearbeitet.

Die tut hier ihren Job bei uns.

Deswegen können wir gerade Musik hören.

Attribution verlangt, dass ich jetzt im Auto oder auf einfache Art und Weise irgendwo hinkomme, wo mir angezeigt wird.

Copyright-Zone.

Copyright bei Mama, Copyright bei Papa.

Er hat sich gerade gegenüber seinen Kindern geäußert.

Das ist schon sehr peinlich.

Ich habe das jetzt ein bisschen ausgemalt.

Aber es ist ja der rechtliche Anspruch eines Open-Source-Entwicklers und der Automobilhersteller, um beim Beispiel zu bleiben, haben halt schon lange auf diese Art und Weise in die Software-Lieferkette hineingehorcht, soweit, dass sie vorab wissen wollten, bevor überhaupt ausgeliefert wurde, wie denn die S-Bomb aussehen wird.

Das war bei den Automobilherstellern Lizenzen.

Sonst heute ist es primär Security.

Zu dem Thema gibt es jetzt verschiedene Nachfragen.

Es gibt eine kurze Nachfrage.

Du hast zu dieser Aussage im Infotainment läuft mehr Code als auf meinem Laptop.

Und das hat die Frage, ob du in dem Kontext das Betriebssystem ausgeklammert hast.

Also bei modernen Autos, ich habe leider kein sehr modernes Auto, aber bei modernen Autos, da laufen VMs, da laufen Container.

Du hattest das vorhin schon mal sozusagen im Vorbeigehen gesagt, dieser Cyber-Resilience-Act.

Also MH hat die Frage gestellt, wird die S-Bomb nicht mit dem Cyber-Resilience-Act der EU verpflichtend?

Und dann hat Sebastian Schubert geschrieben, S-Bomb muss laut CRA, also Cyber-Resilience-Act, erstellt, aber nicht unbedingt zur Verfügung gestellt werden.

Hört zu der Frage, also was ist dieses Cyber-Resilience-Act und wie sieht das da mit S-Bombs aus?

## Cyber Resilience Act

Genau, also der CRA, Cyber-Resilience-Act ist eine Gesetzgebung, die in die EU-Länder gespült wird, eben über die EU.

Es ist eine EU-Regelung zu Software Security und beinhaltet halt, klarzustellen, dass Software-Hersteller vollumfänglich für ihre Produkte haften, egal wie viel Open-Source-Code dabei ist, eben auch diesen Open-Source-Code.

Und dann gibt es halt verschiedene Verpflichtungen unterschiedlicher Art, dass man seine S-Bomb verstehen muss, in der Tat.

Ich würde es ja auch immer mit ausliefern, aber dass man dann halt auch zum Beispiel Kunden informiert, also gezwungen wird durch die Regularien, durch den Act, dass man Kunden informiert, wenn jetzt Sicherheitslücken bekannt geworden sind.

Könnte man meinen, dass, wenn man einen Lizenzvertrag mit einem Kunden hat, ist das so oder so der Fall.

### Verpflichtungen

Es gilt sogar über ausgelaufene Lizenzen hinaus.

Also man muss Nutzer, Kunden, die Software von einem erhalten haben, informieren über bekannt gewordene Sicherheitslücken.

Selbst wenn man schon lange aus dem Vertrag raus ist mit diesen.

Und das heißt halt, um das umsetzen zu können, dass man eigentlich kontinuierlich nachmitspeichern muss, was man genau an wen ausgeliefert hat, mit welcher S-Bomb, also mit welchen verbauten Komponenten.

Es ist einfacher, wenn man einen Webdienst betreibt, wo es genau die eine Version gibt, aber wenn man jetzt tatsächlich noch binär verteilt oder gar Projektgeschäft hat, wo jeder Kunde anders ist, das muss man alles tracken, um genau zu wissen, okay, das sind die verbauten Komponenten gewesen und da muss man monitoren.

Oh, hier ist eine Sicherheitslücke bekannt geworden für diese Bibliothek, die wir Anodat zumal verbaut haben und dann muss man die Personen, die Kunden darüber informieren.

Genau, also MS setzte nochmal nach zu diesen 100 Millionen Zeilen Code, also er oder sie schrieb Danke für die Ausführung 100 Millionen Zeilen Code und trotzdem funktioniert die Bluetooth Verbindung nicht stabil.

Ich finde die Kausalität ein bisschen umgekehrt.

Ich würde sagen, wenn wir 100 Millionen Zahlen Code haben, haben wir halt auch mehr Fehler und dann kommt vielleicht genau sowas raus.

Und genau Jude hatte gefragt, ich muss mal kurz schauen, also da war ja diese Frage von wegen, gibt es eine zunehmende Verbreitung von S-Bomb Lizenzen und er hatte halt dann die Frage gestellt, ob die Erstellung von S-Bombs über Lizenzen verpflichtend gemacht werden kann.

Das ist ein guter Hinweis.

Bin gar nicht auf die Idee gekommen.

Ich denke, man könnte eine Open Source Lizenz einführen, die verlangt, dass tatsächlich eine S-Bomb bei Verbreitung des Quelltexts, ich glaube die Open Source Initiative, es gibt also Mailing Listen, die de facto das diskutieren und Entscheidungen treffen.

Ich glaube, die würde sagen, das geht zu weit, weil man ja über die eigene Open Source Software hinausreicht.

Also wenn man jetzt eine Open Source Software hat und eine Verpflichtung, das ginge noch, weil die wäre nicht diskriminierend, einfach die Verpflichtung, verbaut man diese Open Source Komponente in einem Produkt, dann müsste dieses Produkt mit S-Bomb kommen.

Ich denke, das ist aber ein rein pragmatisches Argument, dass die Personen auf der License Review Liste argumentieren würden, das geht über die Open Source Komponente hinaus, weil man jetzt ja plötzlich Anforderungen hat, die irgendwie den Kontext sprengen.

Man könnte es versuchen.

Ich glaube, dass es nicht funktionieren würde.

Man muss sich auch fragen, würde ein Open Source Programmierer das sozusagen sich selbst mit auf die Nase binden?

Ja klar, wäre schön, wenn alle nach einem immer saubere S-Bomb zerstellen, gerade wenn man auch Produkthersteller ist, aber will man sich selbst auch verpflichten und ich glaube, es würde wahrscheinlich schlichtweg nicht angenommen werden.

Dann ist da noch eine Frage von Axel Hohwind, die ist schon etwas älter.

Wir werden ja mit diesem Thema rund um S-Bomb und verschiedene andere Sachen, das geht da ein bisschen in eine andere Richtung.

Und zwar schreibt er als Maintainer von Projekten unter ASL zu, das müsste die Apache Leistung sein oder MIT Lizenz auf GitHub, kann ich das Einverständnis zur Veröffentlichung unter der Lizenz voraussetzen?

Bei Apache muss ich ja zum Beispiel die ACLA unterschreiben und er meint halt ein Pull-Request.

Das heißt, wenn ich jetzt einen Pull-Request stellen würde, ich Eberhard an ein Projekt, was Apache-License oder MIT-License ist, so verstehe ich das, dann wird mein Zeug, was ich da reinschreibe, letztendlich unter dieser Lizenz stehen und da ist die Frage, ob man das voraussetzen kann oder ob man sich da nochmal absichern muss.

Lass mich das zurückspiegeln.

Ich bin mir nicht 100% sicher, ob ich die Frage verstanden habe, aber ich glaube schon.

Man entwickelt also eine Open-Source-Software und jetzt kommt ein Pull-Request oder Merge-Request und jemand möchte etwas beitragen.

Das Problem ist jetzt, man möchte, dass die beitragende Person natürlich der Lizenz zustimmt für das Open-Source-Projekt, das man da entwickelt.

Und naheliegend davon auszugehen, dass wenn jemand etwas beitragen möchte, da wo man beiträgt, es eine Lizenz gibt, dass diese Person implizit dann auch zustimmt, dass der Code-Beitrag, den diese beitragende Person leisten möchte, dann mit unter diese Lizenz fällt.

Das heißt, der Beitragende, die Beitragende macht eine Lizenzierung, Outgoing-License des eigenen Beitrags in das Projekt unter der Lizenz des Projekts.

Das ist historisch immer ein bisschen schwierig und ich bin kein Anwalt.

Verschiedene Open-Source-Foundations, um sich abzusichern, haben gesagt, das ist keineswegs so garantiert, wenn die Person das nicht explizit macht.

Also die beitragende Person muss explizit sagen, ja, ich lizenziere meinen Code unter der gewünschten Lizenz.

## Contributor Agreements

Ein Beispiel war das bei der Apache Software Foundation, die für unter Apache laufende Projekte tatsächlich ein sogenanntes Contributor Agreement einfordert.

Also ein Vertrag, unter dem man sagt, ja, ich lizenziere meine Beiträge unter der Apache Lizenz, Apache 2.0 Lizenz.

Das machen viele auf GitHub, wo man halt keine eigene Foundation, keine Non-Profit hat, indem sie per GitHub Workflow einfordern, dass da per Klick sozusagen bestätigt wird, ich stimme der Projektlizenz bei und mein Beitrag wird unter die Projektlizenz gestellt.

### Verschiedene Ansätze

Es gibt Projekte, die sagen, wir gehen davon aus, dass da nichts extra unterschrieben wird, sondern dass das positiv und alles ist.

Interessanterweise zum Beispiel der Linux Corner.

Der verlangt also keine, meines Wissens nach keine Contributor Agreement, man muss da nichts unterschreiben oder durchklicken.

Aber man hat eine etwas andere Variante, einen anderen Aspekt, nämlich dass man zusichern muss, und das ist fast wichtiger, dass der Beitrag auch wirklich von einem beigeleistet werden kann und nicht von woanders hier kopiert wurde.

Also der Linux Corner hat per sogenanntes Developer Certificate of Origin verlangt, er den Leuten ab, zu bestätigen, ich habe die Rechte, diesen Beitrag zu leisten, das ist mein Copyright oder ich bin Agent einer Partei, meinetwegen eines Unternehmens, dass diese Rechte besitzt.

Weil man ansonsten das Problem hat, dass Copyright, also Rechte am Projekt, an weitere Parteien abwandern und Copyright ist immer ein sogenanntes Ausschlussrecht, also ein Vetorecht für die Software zu nutzen.

Und was man nicht möchte, dass irgendeine Person durch ein paar Beiträge, die dann tief vergraben werden und von der Menge her ausreichend sein müssen, dass diese Person plötzlich sagen kann, nö, ihr dürft die Software nicht mehr nutzen, weil ich habe euch nie das Recht ausgesprochen, die zu nutzen, zahlt mich aus.

Die Saat von Erpressung möchte man vermeiden.

Was ja wiederum bedeutet, ein pragmatischer Schritt wäre das, was du genau gesagt hast, also eben zu sagen, okay, wenn ich halt irgendwie ein Pull-Request stelle, mache ich halt so eine Box und sage halt, das ist irgendwie fein, dass das genutzt wird.

Gibt Tools auf GitHub, die das möglich machen.

Wie gesagt, ob es wirklich notwendig ist, weiß ich nicht.

Ich möchte mich aber nicht aus dem Fenster lehnen und sagen, nein, das ist nicht wirklich notwendig, weil es offenkundig ist, dass man unter der Projektlizenz beiträgt.

Ja, ich glaube, das ist halt so das typische Thema bei den juristischen Sachen, dass man halt irgendwie das ganz Schwierige so definiert.

Dass man dann anwälte bezahlt.

Die haben das Risiko, aber dafür haben sie die Ausbildung und die Stundensätze.

Ja, und auch die sind da meistens vorsichtig, also die Personen sich auch meistens drumherum zu lavieren, habe ich das Gefühl.

Ich habe ein, glaube ich, ganz anderes Thema noch, sozusagen auch ein bisschen aus Eigeninteresse.

Eigeninteresse ist das falsche Wort, sondern eher sozusagen nicht.

Also wir bewegen uns ja jetzt irgendwie gerade in einer interessanten Zeit und da gibt es diese Themen rund um Digital Sovereignty und da gibt es ja auch jetzt mittlerweile in Deutschland Investitionen in Open Source.

Wie siehst du das?

Also ist sozusagen Open Source die Lösung für digitale Souveränität?

Also wenn wir uns jetzt einfach hinstellen und sagen, wir benutzen halt alle irgendwie nur noch Open Source Software, sind wir ja eigentlich fein draus, oder?

## Digitale Souveränität

Na ja, es ist nur nicht so richtig realistisch, oder?

Also ich denke schon, dass Open Source das Beste ist, was wir machen können, um digitale Souveränität zu erreichen.

Ich glaube nicht, dass wir sie wirklich erreichen können, aber sagen wir mal, in die Richtung zu arbeiten, um die Angriffsvektoren und plötzlich die Software abzustellen.

Das ist ja dann auch so ein bisschen das Bedrohungsszenario zu reduzieren.

Also ja, ich finde das sehr gut, wenn die kritische Software, also muss man dann priorisieren, in deutschen Rechenzentren unter deutscher Kontrolle betrieben wird.

Wenn die entwickelte und dann betriebene Software als Open Source Software bereitsteht, dann greift man halt weltweit auf Entwicklungsressourcen zurück und hat halt durch die Transparenz und so weiter weitere Vorteile.

Das halte ich auch für sehr gut.

### Herausforderungen

Die Realität von Software, so viele Abhängigkeiten, ich glaube nicht, dass digitale Souveränität so einfach herzustellen ist.

Aber es ist wichtig, zweifelsohne in diese Richtung zu arbeiten.

Genau.

Wir sind so ein bisschen, also wir haben noch gute fünf, sechs Minuten.

Ich weiß nicht, ob aus deiner Sicht noch Themen sind, die du gerne ansprechen wollen würdest, die wir jetzt noch nicht angesprochen haben, die für dich persönlich wichtig sind.

Ja, vielleicht nochmal das Thema, dass man den Open Source Code in den eigenen Produkten nicht ignorieren darf und dass aber vielen, das ist immer wieder überraschend, nicht klar ist, wie viel Code das ist und wie viel Arbeit es bedeutet, das aufzuarbeiten.

Man hat dann immer keine Lust dazu, aber diese Aufarbeitung mithilfe von SCAR Tools, heißt die Kategorie, also Software Composition Analysis Tools, verlangt halt, dass man sich wirklich jede Bibliothek im Prinzip anschaut, alle Copyright Statements rausholt, alle Lizenztexte rausholt.

Das ist dann eine Best Practice, so steht es in den Lizenzen nicht drin, aber als Rechtsvermerke bereitstellt und so weiter und so fort.

Und das muss man halt machen, um rechtskonform mit den Lizenzen auszuliefern.

Gleichzeitig über den CRA und so weiter weiß man, dass der erste Schritt, nämlich überhaupt zu verstehen, was da verbaut wurde, auch wichtig ist, um Sicherheitslücken zu verstehen, zu monitoren und so weiter.

Und diese Art von Arbeit kann einen tage-, wochenlang beschäftigt halten.

Man muss die gesamte Software durchgucken.

Es gibt ein marktführendes Werkzeug hier, das scannt all deinen Source Code, dann kriegst du 10.000 Findings, 10.000 Mal blinkt da ganz wild was rot, hier doch bitte dieses Copyright Statement in deine Rechtsvermerke kopieren.

Da hat kein Entwickler, keine Entwicklerin Lust, das zuzumachen, müssen sie aber.

Und dann ist die Frage, wer macht das?

Ich habe gute Studierende, die das machen, also ein bisschen günstiger, als deine Entwickler selbst drauf abzustellen.

Aber es ist unendlich viel Arbeit.

Und was soll man sagen?

Entweder man verzichtet drauf und viele Entwickler, ähnlich wie die WTFPL License, sagen ja mir doch egal, aber es braucht halt nur wieder Copyright Rolle, die einen verklagen.

Es reicht ja die eine Person, Handvoll, kleine Menge an Personen, die auf die Art und Weise ihre Brötchen verdienen wollen.

Ich glaube, ich will auch noch eine Sache loswerden, die mir sozusagen wichtig ist.

Und du hattest ja gesagt, es ist vielleicht das Ziel von Open Source Entwicklern, Source Code zu bekommen von anderen Menschen.

Ich habe ja nun irgendwie diese Historie mit dem Spring Framework.

Also ich war eben bei Spring Source und habe mich halt dort gekümmert, eben um Spring.

Und eine Erfahrung, die ich halt irgendwie gemacht habe, war, ich stehe halt irgendwo an einem Messestand.

Es kommt irgendjemand und sagt, ich habe übrigens folgendes Problem mit dem Framework.

Okay, cool.

Und irgendwann habe ich halt angefangen und habe halt als erste Frage gestellt, nicht so wie, have you tried turning it off and on again?

Da habe ich die Frage gestellt, hast du mal einen Jira eingestellt?

Also damals hatte Spring noch irgendwie Jira als Backtracking-Tool.

Und die typische Antwort war nein.

Und ich will halt noch mal eine Lanze dafür brechen, Open Source Contribution bedeutet nicht nur Source Code, sondern das mehr.

Und solche Sachen wie eben beispielsweise, ich stelle halt NeShu ein.

Ich glaube, das Letzte, was ich bei GitHub irgendwie als Pull-Request eingestellt habe, war ein Rechtschreibfehler, den ich halt irgendwie gefixt habe.

Da war ein Zeichen zu viel.

Und das ist irgendwie Kleingram und nicht gut.

Aber ich glaube, dass das halt trotzdem auch wertvoll ist.

Und da zu partizipieren, ist halt, glaube ich, eine gute Idee.

Und das hilft irgendwie allen.

Also wenn ich ein Problem habe, muss man nicht warten, bis man die Menschen, die hinter dem Ding stehen, dass man die privat tatsächlich ansprechen kann.

Sondern ich würde halt ein NeShu einstellen.

Und meine Erfahrung ist halt, dass in den allermeisten Fällen, selbst wenn das Sachen sind, wo die Antwort ist, hey, schön, aber du hast es nicht verstanden.

Hier ist das Feature schon oder nicht.

In Wirklichkeit funktioniert es halt so.

Und dann reagieren die Leute halt irgendwie nett und offen.

Und daher wäre das halt immer ein Hinweis.

Also ich möchte sagen, wir haben uns heute primär über die rechtlichen Rahmenbedingungen des Einsatzes von Open-Source-Software unterhalten.

Wie man Communities baut, wie Open-Source nachhaltig geworden ist.

Ein großes, tiefes Thema. Überhaupt nicht besprochen haben wir das tatsächlich dank Open-Source-Foundations und zunehmend klaren Verständnis.

Was heißt es, wettbewerbsdifferenzierenden Code versus nicht-wettbewerbsdifferenzierenden Code zu schreiben?

Open-Source nachhaltig geworden ist.

Ich kenne den Ex-KCD auch, der arme Entwickler in Nebraska, der halt diese eine wesentliche Stütze entwickelt.

Das stimmt schon.

Aber die Realität ist, ökonomisch wichtiger Open-Source-Software wird fast immer in Foundations unter klarer Regelung von Copyright, Markenrechten.

Trademarks sind super wichtig.

Gehandhabt, damit ein faires, klares Spielfeld entsteht.

Wie man dann den Open-Source nutzen kann.

Wie man beitragen kann.

Und in allen Fällen die eigene Investition, die ja stattfindet durch die Einführung dieser Abhängigkeit.

Wie die eigene Investition auch sichergestellt ist.

Das ist ganz essentiell für langlebigen Community-Open-Source, dass man solche rechtlichen Regelungen zum Beispiel über Open-Source-Foundations hat.

Genau, und an der Stelle können wir auch nochmal kurz erwähnen, dass wir die Folge 32 hatten.

Mittlerweile sind es seit fünf Jahren, wo du über In-House gesprochen hast.

Also, dass man eben diese Open-Source-Konzepte auch in einer Firma umsetzt.

Und dann halt dort eine bessere Kollaboration zwischen verschiedenen Teams umsetzt.

Was ja bedeutet, dass man eben von Open-Source auch da gute Sachen lernen kann.

Gut, ich glaube wir haben es soweit.

Wir sind so ein bisschen am Ende der Zeit.

Ich schaue nochmal, ob ich irgendwas übersehen habe, irgendwo an Fragen.

Aber ansonsten haben wir es soweit.

Vielen Dank für die Zeit.

Vielen Dank für die vielen Antworten auf die vielen Fragen.

Auch vielen Dank für die Diskussion und die Fragen im Chat.

Wir haben in der nächsten Woche eine Episode, die Ralf macht.

Und diese Episode dreht sich um das Thema The Architecture of the Death Star, 20 Years of Architecture and What We Can Learn.

Da haben wir einen Gast, das wird Johann G.

Carmona sein.

Genau, und da geht es also offensichtlich um die Architektur des Todessterns.

Ich bin selber mal gespannt.

Ich glaube, es wird ganz spannend.

Vielen Dank und schönes Wochenende, würde ich sagen.

Herzlichen Dank dir, dass ich dabei sein durfte, mal wieder.