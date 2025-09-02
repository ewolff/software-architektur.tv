# Folge 275 - Keine Bounded Contexts bei Netflix: Irrweg oder Inspiration?

Netflix keine bauenden Kontexte mehr benutzt und da will ich mich bedanken halt einmal bei dem Nico Stotz, der beim Software-Architektur im Stream Slack das Thema mal aufgebracht hat und außerdem hatte ich eine Person, mit der ich gesprochen hatte nach meinem Talk beim VR Developers World Congress, die mich auch noch meine Einschätzung von diesem Paper halt gefragt hat und beide haben glaube ich da den Eindruck, dass dieses Paper einen Widerspruch erzeugt zu eben unabhängigen Microservices und sowas wie bauenden Kontexten, also unabhängiger Datenmodellierung und das ist so ein bisschen die Richtung, in die das Ganze halt geht und das ist insbesondere deswegen halt interessant, weil eben Netflix einer der Pioniere ist in diesem Bereich von den Microservices und natürlich an der Stelle, wo jetzt einer von den Pionieren sagt, das passt halt irgendwie nicht mehr, ist das halt etwas, was natürlich auf Interesse stößt.

Ich werde kurz sozusagen so ein bisschen so eine Motivation geben, also warum ist das mit dem bauenden Kontext ein Thema, warum ist das mit dem Modell ein Thema, was sind so Alternativen, wie orte man das halt insgesamt ein.

Dann werde ich den Blogpost von Netflix tatsächlich diskutieren und dann das Ganze noch mal bewerten und ich freue mich natürlich irgendwie auf eure Fragen und Kommentare, die ihr halt sehr gerne in dem Chat oder halt in dem Formular auf der Homepage hinterlasten könnt.

## Bounded Contexts und Modelle

Also legen wir los, was ist halt die Geschichte mit diesen bauenden Kontexten und den Modellen.

Also das ist etwas, was sich so ein bisschen durch die mittlerweile seit glaube ich einem Jahr durch den Stream zieht.

### Definition Bounded Context

Es gab halt einmal diese Episode, die gesagt hat, naja, bauenden Kontext bedeutet eben, hat eigentlich so drei Dinge, die das halt irgendwie repräsentiert.

Das ist halt zum einen so ein Modell, also irgendetwas, wo ich halt hingehe und ich sage, ich habe eine Funktionalität.

Also zum Beispiel irgendetwas, was halt sagt, wie kriege ich halt eine Bestellung zum Kunden geliefert, sowas in dem Dreh.

Dafür brauche ich ja ein Modell.

Das heißt, also ich muss jetzt wissen, welche logistischen Möglichkeiten habe ich, Sachen halt zum Kunden zu bekommen.

Ich muss wissen, welche Waren habe ich, wie kann ich die verschicken.

Sollen die versichert verschickt werden oder nicht?

Sind die teuer oder billig?

Wenn sie teuer sind, sollen sie versichert verschickt werden und so weiter und so weiter.

So und das ist irgendwie dieser Modellcharakter von den bauenden Kontexten.

Dann gibt es noch irgendwie diese Sprache.

Das heißt also, in unterschiedlichen bauenden Kontexten können Dinge unterschiedlich definiert sein.

Und mein Beispiel dafür, was ich in letzter Zeit öfter benutze, ist der Hotelkunde.

### Beispiel Hotelkunde

Also wer ist der Kunde eines Hotels?

Und ich würde behaupten, wenn ich über den Check-in spreche, dann ist das eine natürliche Person, so wie ich, Eberhard.

Und wenn ich über sowas wie die Rechnungslegung spreche, dann ist das vielleicht mein Arbeitgeber, nicht die SwagClub GmbH.

Und die kann definitiv niemals in einem Hotel einchecken, weil es ist eben keine natürliche Person.

Und dann habe ich halt irgendwie noch, wer auch immer das bezahlt.

Ich bezahle das vielleicht selber, bezahle vielleicht für meinen Kollegen mit und dann habe ich eben drei verschiedene Modelle.

Also ich habe den Check-in, da bin ich und mein Kollege sind dort der Kunde.

Dann gibt es die Bezahlung, da bin ich vielleicht die Person, die es bezahlt mit meiner Kreditkarte, auch für meinen Kollegen.

Und dann haben wir noch das Modell für die Rechnungslegung, wo wir sagen, die SwagClub GmbH ist der Kunde.

Das heißt also, abhängig davon, über welchen Kontext wir reden, über welches Modell wir reden, sind bestimmte Sachen unterschiedlich definiert.

Also Kunde kann eben unterschiedliche Dinge sein.

Und da ist nochmal auch noch wichtig, wir reden dort über Logik.

Also wir haben ein Modell, was es mir erlaubt, dass sich irgendjemand eincheckt oder dass jemand in eine Rechnung geschickt wird.

Das ist Logik.

Da ist Logik drin.

Vielleicht darf ich nicht einchecken, weil ich bin minderjährig oder was auch immer.

Und das ist eigentlich der Kern.

Wir wollen also Logik aufteilen in verschiedene Modelle.

Dafür brauchen wir unterschiedliche Daten.

Davon getrennt ist noch ein bisschen die Geschichte mit der Sprache.

Man kann eben manchmal beobachten, dass wenn Menschen über verschiedene Dinge reden, also in diesem Fall über den Kunden unterschiedliche Dinge meinen, der Kunde ist vielleicht die SwagClub GmbH, vielleicht ist es auch eine natürliche Person.

Das ist der andere Aspekt, dass sprachliche Definitionen unterschiedlich sind.

Die Modelle sind ein Aspekt.

Und dann ist der dritte Aspekt, diese Geschichte, dass sich Einbauender Kontext einem Team geben kann.

Also auch über Teams ist das letztendlich eine Aussage, dass ein Team bekommt, typischerweise Einbauender Kontext zu tun.

Und damit ist das eben auch dort relevant.

Also habe ich diese drei Ebenen Modelle, Sprache und Teams.

Und darüber hatte ich eben in dieser einen Episode gesprochen, wo es darum geht, was ist eigentlich Einbauender Kontext?

Und ich habe da noch eine Episode nachgeschoben, wo ich gesagt habe, eigentlich ist es mit den Modellen spannend und diese Modelle zu finden.

Das ist so ein bisschen die Kernerausforderung von Software Architektur.

Und ich habe versucht, ein paar Röstling anzugeben, wie man so etwas auf die Reihe bekommen kann.

Der Urs Enzler bei LinkedIn hatte vorher auch schon gesagt, dass eben Modelle für ihn sozusagen das Wichtigste sind bei dieser Aufteilung.

Das würde ich auch so sehen.

Aus einer Software Architektur Frage ist das eben tatsächlich das Wichtigste.

Und da kommen wir jetzt her.

Das heißt also, wir wollen heute diskutieren, ob Netflix tatsächlich nur ein Modell nutzt.

Und das ist eigentlich erstaunlich, weil es wäre erstaunlich, wenn das so wäre.

Weil wenn man an dem Hotelbeispiel sieht, mehrere kleine Modelle sind eigentlich das, worauf es typischerweise hinausläuft und was eben typischerweise sozusagen der sinnvolle Ansatz ist.

Weil wir jetzt in so eine Situation kommen, wo wir halt über potenziell ein Datenmodell reden, das halt sozusagen universell ist.

Da gibt es halt von dem leider verstorbenen Stefan Tilkoff diesen Blogpost, den ich auch nochmal verlinke, wo er über diese kanonischen Datenmodelle spricht.

Das ist so ein Thema aus SOA, was ein Architekturansatz ist, der so vor 20 Jahren ein relevanter Architekturansatz war.

Und dort sagt er, ich kann jetzt versuchen, zum Beispiel eben den Kunden zu modellieren.

Einmal für alle.

Da sagt er, das ist halt schwierig.

Einmal deswegen aus diesen konzeptionellen Unterschiedlichkeiten, die er in unterschiedlichen Situationen haben kann für einen Kunden.

Beim Check-In ist es eben jemand anders als bei der Rechnungslegung.

Er macht noch den Punkt, dass es halt die Teamautonomie einschränkt, weil die Teams eben nicht unabhängig voneinander die Modellierung durchführen können.

Und er spricht auch noch darüber, das sind die beiden Punkte, die er sieht als Schwierigkeiten.

Und er gibt dann als Tipp zu sagen, dass man eben unabhängige Teile von verschiedenen Teams definieren lassen sollte, weil die dann eben jeweils unabhängig voneinander die Sachen für diese Art relevant sind, selber modellieren kann.

Ich kann, wenn, dann vielleicht nur Fragmente standardisieren, wo das sinnvoll ist.

Und ich sollte insbesondere nicht das zentrale Modell in die Teams runterpushen.

Und er sagt halt insbesondere auch noch, dass so ein zentrales Modell, dass man da sozusagen versuchen kann, Aufwand zu sparen, dass das eine mögliche Motivation ist und dass das eben auch kontraproduktiv ist.

Das heißt also, er sagt halt, diese Motivation mit dem Aufwand sparen, das wird man typischerweise nicht hinbekommen, weil eben dieses universelle Modell zu bauen schwierig oder kaum möglich ist.

Das heißt also, aus der Perspektive würden wir jetzt erwarten, wenn wir ein Datenmodell haben, was übergreifend ist, haben wir Einschränkungen von Autonomie, hohen Aufwand, Probleme, weil es konzeptionell schwierig ist und es sollte insgesamt schief gehen.

Ich bin da mit Stefan völlig einer Meinung und das ist halt auch einer der Gründe, weswegen das sich erst mal so ein bisschen komisch anhört.

So jetzt gibt es halt im Bereich Domain Driven Design durchaus Patterns, die ein bisschen in so eine Modellierung von einem gemeinsamen Modell gehen.

Also ein Beispiel ist die Published Language.

Published Language bedeutet, dass ich irgendwo einen wohl definierten, publizierten Datendarstellung habe und zwar ist das eine gemeinsame Sprache, mit der ich dann dafür sorgen kann, dass wir uns für die Kommunikation zwischen zwei Bauenden Kontexten auf irgendeine gemeinsame Sprache einigen und der ist halt getrennt von den internen Modellen.

Das heißt also, potenziell könnten wir jetzt sagen, wir bauen eine Schnittstelle.

Nehmen wir mein internes Modell?

Nein.

Nehmen wir dein internes Modell?

Nein.

Wir bauen also ein gemeinsames Modell.

Das wäre dann die Published Language und das könnten wir auch höher skalieren.

Das heißt, wir könnten jetzt auch sagen, wir bauen halt so eine Published Language, die für mehrere Parteien relevant ist.

Das heißt also, da hätte ich jetzt ein Datenmodell tatsächlich, also eine Daten und das wäre etwas, was sich halt mehrere teilen.

Ein Realist schreibt halt schon, brauchst halt ein anständiges und wirksames Ontology Management.

Also Ontology, tatsächlich läuft das halt bei Netflix ein bisschen in diese Richtung, dass ich also dort dann Begriffe definiere und versuche, die halt irgendwie hin und her zu mappen.

Das ist also etwas, was ich dann irgendwie brauche für diese Übersetzung.

Ein anderer Bereich, wo ich halt so ein, was für mich nicht ganz in so ein gemeinsames Datenmodell geht, aber schon irgendwie etwas ist, was man glaube ich da diskutieren muss, sind halt diese Data Products bzw.

Data Meshes, wo ich also jetzt sage, ich habe irgendwelche Informationen, also zum Beispiel Informationen aus dem Check-in von einem Hotel und ich sage jetzt, diese Information von dem Check-in, die biete ich jetzt an zur Analyse.

Also vielleicht ist es halt so, dass ich glaube, dass der exakte Check-in Zeitpunkt relevant ist oder das Geschlecht oder das Alter oder was weiß ich.

Dann baue ich halt irgendwie so einen Datenexport zusammen, mit dem ich halt dann diese Daten zur Analyse bereitstellen kann, sodass eben dann ein anderes Team oder irgendwelche Business Intelligence Leute halt diese Daten analysieren können.

Und das ist typischerweise dann eher so auf der Schnittstellen-Ebene.

Also vielleicht exportiere ich die Daten halt in einen S3-Bucket und dadurch vermeide ich eben, dass Leute jetzt hinter meinem Rücken in meiner Datenbank meine Daten auslesen, sondern ich ziehe das halt auf eine Schnittstellen-Ebene.

Sprich, wenn ich jetzt mein internes Datenmodell ändere, kann ich ja trotzdem das Datenmodell für den Export konstant halten.

Und gleichzeitig ist es halt so, dass die Leute, die halt die Daten analysieren, da die Möglichkeit haben, Dinge zu analysieren, an die ich vorher vielleicht noch nicht gedacht habe, weil sie eben diese Datenprodukte kombinieren können, sich halt anschauen können und dort dann eben entsprechend Möglichkeiten haben, das zu tun, was sie tun wollen, was vielleicht vorher gar nicht planbar ist.

Also wenn ich vorher sagen kann, okay, exakt diese Daten will ich analysieren, das ist ja einfach.

Das wird dann schwierig, wenn ich halt sage, ich weiß nicht so genau, welche Daten ich analysieren will.

Gib mir sozusagen alles und sowas könnte ich jetzt hier so ein bisschen umsetzen.

So, das also so ein bisschen zum Einschwingen.

Wir haben jetzt eigentlich folgende Aussagen.

Wir erwarten, dass wir typischerweise in Softwareentwicklung eine Vielzahl an Modellen haben werden.

Das ist vorteilhaft.

Wenn wir das nicht haben, werden wir hohe Aufwände haben, die Dinge zu koordinieren.

Wir werden Schwierigkeiten haben, vernünftige Datenmodelle zu erzeugen, den Kunden für das Hotel einmal zu modellieren, dass er eben alle drei Benutzungen irgendwie abdeckt.

Das ist schwierig.

Würde ich auch nicht wollen.

Das macht dann auch konzeptionell wenig Sinn.

Also ich hätte dort ein Problem.

Die Autonomie, die Konzepte, die halt nicht funktionieren.

Und ich kann aber durchaus für Kommunikation und für Datenanalyse dazu kommen, dass ich ein Datenmodell habe, das so eine Art globalen Standard möglicherweise darstellt.

Published Language und ein Dataproduct können in diese Richtung gehen.

Das ist so ein bisschen das, wo wir herkommen.

Der Netflix-Blog hat eben diesen schönen Titel.

Model once represent everywhere.

Also ich modelliere einmal und die Repräsentationen sind überall.

Er nennt die Unified Data Architecture dort als das Schlagwort.

## Netflix Blogpost Analyse

Netflix ist mittlerweile breit bekannt.

Es ist ein Online-Videodienst, wo ich also nicht Online-Videos gucken kann.

Die sind deswegen interessant, weil sie ein Microservices-Pionier waren.

Und zwar schon so lange, dass ich am Anfang, als ich über Netflix gesprochen habe, noch immer erwähnen musste, was das überhaupt ist, weil sie gar nicht in Deutschland präsent sind.

Mittlerweile ist es ja deutlich anders.

Es ist ein sehr erfolgreiches Unternehmen unter dem Fortune 500 und ist eben dort aus diesem Grund interessant, weil es eben dieses Microservices und dieses unabhängige Zeug, unabhängige Teams, autonome Teams und so weiter, gepredigt hat.

Zumindest zu dem Zeitpunkt und weil hier jetzt zumindest wahrgenommen Widerspruch ist.

Was hier also letztendlich passiert ist sowas wie, ich habe mir aufgeschrieben, eine Änderung an der Architektur.

Ich bin mir gar nicht sicher, ob das stimmt.

Eigentlich ist es eine Architekturentscheidung.

Also wir haben eine Architekturentscheidung, die irgendwie sagt, wir wollen ein gemeinsames Datenmodell haben.

Und um das zu bewerten, ist es wichtig, erstmal herauszufinden, was sind eigentlich die Gründe.

Also wenn ich eine Architekturentscheidung treffe, dann sollte ich die halt irgendwie begründen.

Und ich sollte sie halt anhand der Begründung auch bewerten.

Also nur, weil ich mich jetzt irgendwie hinstelle oder sich jemand hinstellt und sagt, wir bestreiten die Autonomie der Teams, das sollten wir nicht machen.

Es kann ja Gründe geben, warum ich das doch machen möchte.

Und vielleicht ist in diesem spezifischen Fall die Autonomie der Teams gar nicht so schlimm, wird nicht so stark eingeschränkt.

Das heißt also, ich muss mir die Frage stellen, was ist denn eigentlich das Ziel?

Warum treffe ich diese Entscheidung?

Und anhand dieser Kriterien sollte ich es anschließend bewerten.

### Problembeschreibung

Das Paper fängt auch tatsächlich damit an und sagt halt, das Problem, das wir haben, ist, dass sowas wie ein Actor, also ein Schauspieler oder ein Movie, also ein Film mehrfach modelliert ist.

Und zwar in einer GraphQL-Gateway für die internen Anwendungen, im Asset Management, im Media Computing, wo also Sachen encoded werden.

Und die modellieren das leicht unterschiedlich, mit wenig Koordination oder gemeinsamen Verständnis.

Oft haben sie dieselben Konzepte, aber sie wissen es nicht.

Ich würde jetzt erstmal behaupten, das ist keine vernünftige Begründung, weil das ist sicher suboptimal.

Das wünscht man sich vielleicht anders, gerade wenn man so ingenieursmäßig vorgeht.

Aber bis jetzt habe ich noch nicht verstanden, was sozusagen für BenutzerInnen oder irgendwelche anderen Stakeholder konkrete Nachteile sind.

Es ist im Gegenteil so, wenn ich Sachen mehrfach modelliere, aus dem, was ich vorher gesagt habe, kann es eben sein, dass es einen guten Grund dafür gibt, nämlich höhere Autonomie und dass es in Wirklichkeit unterschiedliche Konzepte sind.

Das heißt also, auf dieser Ebene ist es jetzt erstmal so, dass ich noch nicht so richtig sehen kann, was eigentlich das Problem ist.

Also doppelte und inkonsistente Modelle sind glaube ich nicht das Problem.

Dann haben sie als weiteres Thema inkonsistente Terminologie dargestellt.

Das finde ich auch schwierig, denn wir haben es gerade eben bei dem Kunden von dem Hotel diskutiert.

Der Kunde des Hotels ist eben unterschiedlich, je nachdem in welchem Bauenden Kontext ich ihn betrachte.

Das erwarte ich halt.

Das heißt also, diese inkonsistente Terminologie ist nicht etwas, was ich einfach abschalten kann, wenn ich mich auf irgendwas einige.

Sondern es ist eben so, dass der Kunde, der eincheckt, was anderes ist als der Kunde, der hat die Rechnung bezahlt oder die Rechnung bekommt.

Das bedeutet, diese inkonsistente Terminologie ist ein Teil, eine Auszeichnung der Modellierung meines Systems.

Das ist also auch ein schwieriges Thema und dem könnte ich jetzt auch zum Beispiel begegnen, indem ich beispielsweise ein Glossar schreiben, indem ich sage, das ist halt der Begriff und so sind die Synonyme oder dieser Begriff in den verschiedenen Bauenden Kontexten hat unterschiedliche Bedeutungen.

Das ist nichts, wo ich jetzt erstmal unbedingt Architekturmaßnahmen brauche.

Zwei Punkte, die ich interessant finde und nachvollziehbar ist einmal Datenqualität.

Also, dass diese Sachen auseinanderlaufen und Referenzen manchmal kaputt sind.

Also, dass eben Systeme auf Daten in anderen Systemen verweisen, die halt nicht mehr dort sind.

Das kann ein Thema sein.

Es ist aber immer noch nicht so, dass ich halt jetzt, also idealerweise würde ich mir wünschen, dass man sagt, an genau dieser Stelle hat irgendein Benutzer, irgendein Stakeholder ein echtes Problem gehabt und das können wir jetzt irgendwie lösen.

Das ist halt nicht Datenqualität an sich.

Ist halt erst dann ein Problem, wenn daraus irgendwelche Dinge hervorgehen, die halt wirklich Benutzer oder Stakeholder vor irgendwelche Schwierigkeiten stellen.

Hier ist es für mich eher nachvollziehbar und das will ich vielleicht irgendwie abstellen.

Es fehlt halt vielleicht nur die Information, die sagt, genau an dieser Stelle ist das ein Problem.

Und dann haben sie halt irgendwie noch aufgeschrieben, dass es halt wenig Verbindungen über Systeme hinweg gibt.

Das könnte eventuell auch ein Thema sein.

Nicht, dass ich also irgendwie Schwierigkeiten habe, von einem System zu einem anderen zu kommen und dort irgendwie mehr Details zu finden.

Interessant ist hier, dass eben diese Themen, die ja eigentlich jetzt erst mal relevant sind, also sprich Autonomie, Aufwand und so weiter und so weiter, hier gar nicht diskutiert worden sind.

Also das heißt, es steht nirgendwo, ja und dafür nehmen wir halt irgendwie in Kauf, dass die Teams halt weniger autonom sind.

Das steht halt irgendwie nicht drin.

Und es ist für mich halt irgendwie auch schwer nachvollziehbar, wie gravierend diese Probleme sind.

Also sprich, ist da irgendwo etwas, wo wir jetzt einen Umsatzverlust haben oder irgendeinen, was ich nicht ansehe, Verlust oder so oder irgendwelche Schwierigkeiten in dieser Richtung, das steht da nicht drin.

Kann man aber auch irgendwie nicht erwarten, weil es ist ein Blogpost und der Blogpost wird ja jetzt nicht sagen, wir haben übrigens massive Schwierigkeiten.

Und weil wir diese massive Schwierigkeiten haben, haben wir folgende Entscheidungen getroffen.

Also es wird kein Mensch sozusagen öffentlich zuzugeben, logischerweise.

### Technische Lösung

## UDA (Unified Data Architecture)

So und die Lösung ist jetzt zu sagen, wir definieren also einmal ein Modell und verwenden es überall wieder.

Und das wollen wir machen mit mehr als Dokumentation, nicht nur als Dokumentation, sondern wir wollen tatsächlich Schemata generieren, Konsistenz erzwingen und so weiter.

Das erste Interessante ist, dass genau genommen diese Sache halt nur genutzt wird für Content Engineering.

Content Engineering ist ein Bereich, den Netflix seit 2020 hat, damit deutlich nach den Netflix Microservices.

Bedeutet das, dass wir nur ein Modell haben sollen?

Es könnte halt sein, dass wir halt ein bauenden Kontext haben mit einem Modell, nämlich Content Engineering und das halt aus diesem Grund dieses eine Modell sozusagen funktioniert und das bedeutet auch, dass sie vielleicht gar nicht so viel Legacy-Themen haben.

Also seit 2020, gut, sind immerhin fünf Jahre, aber es ist ein relativ neues Thema und es ist halt auch deswegen ein neues Thema, weil eben Netflix noch nicht so lange, so jedenfalls meine Wahrnehmung selber, Content tatsächlich produziert.

Die haben ja früher halt nur Dinge vertrieben.

So und der Geschäftsprozess, der dort irgendwie abgebildet wird, ist halt sowas wie ein Pitch, wo man also sagt, das ist halt eine tolle Serie, dann halt eine Business Negotiation, wo man also darüber diskutiert, wie man die halt irgendwie produzieren kann, nehme ich an, dann Pre-Production, Production, Post- Production und schließlich Launch.

Das heißt also, wir nehmen nur dieses Thema aus dem gesamten Netflix-Universum raus.

Das heißt also, an der Stelle, wo das Ding live gegangen ist, ist da Schluss.

Was also bedeutet, dass wir wahrscheinlich, vielleicht nicht über ein unternehmenswertes Modell sprechen.

Ich bin mir auch nicht sicher, wie sehr wir über Legacy-Transformation sprechen, also ob wir darüber reden, dass wir alte Systeme modernisieren wollen.

Das wäre ja etwas, was sozusagen echten Umschwung wäre, oder nicht?

Wo man jetzt sagen würde, okay, wir haben halt Microservices gemacht, wir haben halt dezentral irgendwelche Sachen modelliert, das war eine blöde Idee, wir machen jetzt dieses zentrale Modell.

Das ist eigentlich nicht erkennbar, weil das eben ein relativ neuer oder anderer Bereich ist, als der den Netflix zumindest 2015 hatte.

Mir ist noch nicht ganz, also ich habe immer noch so ein Problem damit zu verstehen, was eigentlich genau das Problem ist, das gelöst werden soll.

Und ich kann es so ein bisschen spoilern.

Ich würde behaupten, dass das Problem, das eigentlich gelöst wird, ein ganz anderes ist.

Aber das sollten wir dann noch mal diskutieren.

So, jetzt ist halt die Frage, was macht dieses UDA-Ding?

Und ich muss mal kurz schauen.

Genau, das wollte ich zeigen.

Da kann man sich halt ein bisschen an der ersten Grafik orientieren, die die halt gebaut haben.

Und da ist es halt letztendlich so, dass man sagt, okay, wir haben ein Domainmodell in der Mitte, das mappen wir auf verschiedene Repräsentationen.

Da gibt es zum einen eine Repräsentation in Apache Iceberg, das ist so eine Big-Data-Lösung, wo man also offensichtlich Analyse mit betreiben kann, GraphQL-Repräsentation für irgendwelche Datencontainer.

Und unten haben wir dann halt auch eine Mapping-Richtung Data Mesh.

Das fand ich besonders interessant.

Also das heißt, eine Lösung, Data Mesh-Lösung für Datenprodukte ist eigentlich schon in Benutzung und ist eben eines der Mapping- Ziele.

Und man will jetzt mit diesem System Content-Domain-Modelle registrieren können und umsetzen können.

Und die halt entsprechend auch die Schemata übertragen können in Richtung von GraphQL Afro.

Afro ist dieses Format, was zum Beispiel im Apache Kafka-Kontext genutzt wird.

Was halt so rückwärtskompatible Möglichkeiten hat.

Also wo ich halt dann tatsächlich dafür sorgen kann, dass ich halt Daten in einem alten Format bekomme, obwohl sie in einem neuen Format vorliegen.

Also mit einem integrierten Converter.

Dann sowas wie SQL, was bei Iceberg bei sich eine Rolle spielt.

Sowas wie RDF.

Dazu kommen wir später nochmal.

Oder auch eine Java-Repräsentation.

Das ist halt das, was wir jetzt irgendwie bauen wollen.

Oder was die halt gebaut haben.

Dann wollen sie Daten transportieren vom GraphQL in Richtung zu dem Data Mesh zum Beispiel.

Dann, dass sie halt irgendwie die Möglichkeit haben, über Change Data Capture, also wenn irgendwie Daten geändert werden, das halt in die Iceberg-Datenprodukte reinzubekommen.

Solche Geschichten.

Und sie wollen dann eine Möglichkeit anbieten, um Domain-Konzepte zu finden und zu untersuchen durch Queries oder andere und Grafen.

Und auch programmatisch halt diesen Grafen sozusagen untersuchen.

So und damit ist eigentlich das Ziel, was sie jetzt da tatsächlich verfolgen, eine Daten-Integration.

Wo sie im Prinzip sagen, wir wollen halt Daten aus verschiedenen Bereichen vernetzen, in einen großen Datengrafen reinbekommen.

Diese ganzen Daten darüber eine gemeinsame Sicht anbieten und dafür sorgen, dass wir darüber halt arbeiten können.

Diese, was für mich da hinweist, dass das eigentliche Thema, das sie da haben, ein Datenanalyse-Thema ist.

Also sie wollen, glaube ich, irgendwie eine Oberfläche irgendwelchen Menschen anbieten, die ja Domain-Expertinnen sind und dafür sorgen, dass die dann einheitlich auf diese verschiedenen Datenquellen zugreifen können.

Und das ist die Richtung, in die sie halt erstmal, glaube ich, marschieren wollen.

Und das ist was anderes.

Also das Problem-Statement war ja nicht, wir haben ganz viele Datencontainer und wir können die Daten nicht analysieren, sondern die Aussage war, naja, unsere Datenqualität und diese Sachen sind halt ein bisschen schwierig.

Und damit ist das nach meinem Empfinden eben eigentlich ein Daten-Integrationsthema, ein Analyse-Thema und halt auch etwas, wo irgendwie diese Data-Products wieder eine Rolle spielen.

Und ohne jetzt sozusagen der endgültigen Diskussion vorgreifen zu wollen, bedeutet das, dass halt diese Aussage, dass wir einzelne Systeme, die getrennte Modelle haben, das steht da, glaube ich, gar nicht so im Kern dahinter, dass man jetzt davon eine Abkehr irgendwie haben wird.

Und genau, das heißt, sie wollen jetzt so einen Knowledge-Graphen bauen, wo sie eben diese ganzen Sachen gemeinsam miteinander vernetzen.

Dafür benutzen sie RDF, dieses Resource Description Framework.

Das ist etwas, was es bei B3 schon lange gibt, also beim B3C, so für dieses Semantic Webzeug, was ich glaube sogar schon in den 90ern ein Thema war, wo ich also so Aussagen formalisiert treffen kann über Ressourcen, Subjekte, Prädikate und Objekte und sowas.

Also das Beispiel, was wir im Text nennen, ist ECMI produziert Batterien.

Das heißt also, das Subjekt ist ECMI und das Prädikat ist produziert und das Objekt ist irgendwie Batterien.

Also grammatikalisch falsch, aber es stellt einen Zusammenhang hin hier zwischen Batterien und ECMI und zwar wie wir diesen Zusammenhang produzieren.

Und das ist jetzt eben etwas, also das ist das Wikipedia-Beispiel für RDF und das ist jetzt etwas, was ich natürlich nutzen kann, um irgendwie so Anthropologien und solche Sachen aufzubauen, wo ich Begriffe in Verbindung miteinander setze.

Und sie haben dann diese Shape Constraint Language, SHARCL heißt die, die jetzt irgendwie noch weiter auf diesen RDF-Grafen Constraints einführen kann.

Und das ist jetzt etwas, wo ich mir nicht sicher bin, ob es für die Architekturdiskussion relevant ist, aber es ist halt etwas, wo wir jetzt Semantik von Daten sozusagen einfangen können.

Also ich hatte es vorhin schon gesagt, ein Realist hat es eben auch schon kurz gesagt, ich brauche halt irgendwie solche semantischen Dinge, um jetzt Anthropologien zu haben und um unser Mapping auf die Reihe zu bekommen.

### Komponenten

So, und sie haben jetzt verschiedene Bestandteile des Systems.

Da gibt es einmal das Primary Data Management, PDM.

Da gibt es halt diese Referenzdaten und diese Taxonomien drin.

Das heißt, da steht jetzt irgendwie drin, was halt semantisch wie der ROT modelliert ist.

Und das generiert eine UI für Businessanwender in.

So, und da ist wieder die Geschichte nicht, also wenn ich sozusagen nur das Problem anschaue, in dem Problem steht nichts von Analyse.

Hier ist aber eine Lösung, die hat offensichtlich auf Analyse abzielt.

Das heißt also, wahrscheinlich ist das Problem eher, ich will irgendwie die Daten analysieren und will halt irgendwelchen Business-Expertinnen die Möglichkeit geben, diese ganzen Daten anzuschauen.

Und das kann im Moment Afro und GraphQL, also eben nur zwei Plattformen.

Das heißt also, die sind halt auch noch in der Implementierung.

Dann haben sie als weiteres Produkt Sphere.

Das ist also nicht die Kugel.

Das ist ein System, mit dem Sie, mit dem Business-Expertinnen sich selbst Reports zusammenbauen können.

Und das katalogisiert uns als Business-Konzepte wie im Actor oder Movie sozusagen zueinander in Beziehung.

Traversiert dann halt diesen Knowledge-Graphen, der da ist.

Das heißt also, da habe ich jetzt irgendwie diese gesamte Oberfläche mit den verschiedenen Daten.

Da habe ich diesen Knowledge-Graphen, den kann ich jetzt über das Sphere benutzen, um hier halt irgendwelche Reports zu machen.

Und daraus generiert das System dann SQL Queries.

Und das ist halt wieder eine Geschichte, die halt irgendwie eher Datenanalyse bedeutet.

Wo dann für mich wieder die Frage ist, warum nicht Data Meshes und Datenprodukte dort haben.

Also warum brauche ich mir nicht ein System, wo ich halt diese ganzen Daten einfach rein exportiere und dann anschließend Reports drüber fahren lassen kann.

Keine Ahnung.

So, dann haben Sie eine eigene Sprache, um Domänen zu modellieren.

Die nennt sich APPA.

Da haben Sie Schlüsselattribute und die Beziehungen dazwischen, in Beziehung zu anderen Entitäten.

Die sind dann in Taxonomien organisiert.

Und da gibt es halt ein Beispiel.

Das ist das hier.

Mal kurz schauen, dass ich das richtig hinbekomme.

Genau, also da ist es halt so, dass wir jetzt sehen einen One-Piece-Charakter.

One-Piece ist irgendein Manga.

War mir vorher auch nicht bekannt.

Und da gibt es einen Devil Fruit.

Das ist also eine bestimmte Frucht, die so einen Charakter typischerweise hat oder den repräsentiert.

Und da habe ich halt diese Beziehung Devil Fruit dazwischen.

Und dann gibt es halt darunter noch den Devil Fruit Type.

Das ist, glaube ich, ein artifizielles Beispiel.

Wir werden nachher noch sehen, dass Netflix mit den echten Beispielen aus dem echten Leben eher vorsichtig ist.

Und so kann jetzt eine Modellierung aussehen.

### Datenintegration

Das bedeutet, ich habe dort jetzt eine Taxonomie und ein Datenmodell gebaut.

Das kann ich anschließend auch in eine Sprache übersetzen.

Ich erspare uns, da sind Listings drin, aber ich erspare uns, das im Listing sozusagen anzugucken.

Es geht darum, das konzeptionell zu verstehen.

Das kann ich dann transpellieren, also übersetzen in Richtung zu GraphQL, Afro, Iceberg oder Java.

Und das ist also letztendlich eine generelle universelle Datenrepräsentationssprache, die ich jetzt übersetzen kann auf diese verschiedenen Systeme.

Was ich dabei noch interessant finde, ist, dass dieses System die Möglichkeit bietet, diese Domainmodelle zu erweitern, was möglicherweise darauf hindeutet, dass sie eben sozusagen ein gemeinsames Ding definieren und dann einzelnen Teams oder einzelnen Bereichen die Möglichkeit geben, es zu erweitern.

Was ja wiederum bedeutet, es gibt nicht das eine übergreifende Modell, sondern eben einen gemeinsamen Kern, den man dann eben entsprechend erweitern kann.

Also auch da, das wäre jetzt auch so ein Hinweis, wir bauen nicht das eine Modell, sondern unterschiedliche Dinge, nur einen gemeinsamen Kern.

Und das Nächste, worüber sie dann noch diskutieren, ist das hier.

Das ist also so eine Data Container Representation für dieses Data Mesh.

Und hier sieht man jetzt also nicht dieser One Piece Charakter, also One Piece Devil Fruit is a Record, da gibt es irgendwie Namen und noch einen Namen und die sind irgendwie nicht nullable.

Also dort eben eine Datenbeschreibung, die man jetzt dann umgesetzt werden kann, in beispielsweise Afro, wie man hier sieht.

So und das kann ich jetzt eben tatsächlich visuell sozusagen mappen.

Das heißt also, ich kann jetzt im nächsten Schritt dann sagen, dass ich halt dort irgendwas übersetzen möchte von diesem UDA Properties auf irgendwelchen konkreten Data Assets und habe da die entsprechende Übersetzung.

Und hier ist eins der Features, dass die auch haben, dass man die Daten automatisch irgendwo anders hinbewegen kann.

Dass ich jetzt sage, okay, ich habe die Daten in GraphQL und ich schmeiße sie jetzt mal irgendwie in Iceberg, damit ich sie da halt dann analysieren kann mit meinem SQL, was vielleicht irgendwie performance mäßig besser ist.

So, was eben bedeutet, dass ich durch Transpellieren nicht nur diese verschiedenen Schema-Teile erzeugen kann, sondern dass ich eben auch die Daten hin und her kopieren kann.

Und das ist so die wesentliche Idee, die sie dort offensichtlich haben.

Beispiele, die sie dann nennen, wo dieses System sozusagen genutzt wird, ist halt einmal dieses Primary Data Management.

Da sprechen sie tatsächlich davon, dass sie eben ein kontrolliertes Vokabular umsetzen und zentral definieren.

Also was ist wo, wie erlaubt, mit welchen Werten?

Und zwar durch irgendwelche Business User In, also nicht durch Techniker In.

Und das nutzt auch ein W3C-Standard, nämlich S-Core Simple Knowledge Organization System, worüber jetzt einzelne Nutzer in ihr eigenes Modell mit ihrer eigenen Sprache sozusagen drunter benutzen können.

Und offensichtlich diesen S-Core Layer, keine Ahnung wie genau, aber von dem müssen sie noch nicht mal wissen, dass das existiert.

Was also auch wieder bedeutet, dass es vielleicht nicht das eine Modell ist, sondern eher so ein Übersetzungs-Ding.

Und dann haben sie schönerweise ein Screenshot zu diesem Sphere.

Da ist halt bedauerlicherweise alles mögliche irgendwie geschwärzt, sodass man im Prinzip nur Production hier sieht.

Das bedeutet, irgendwie kann man da Reports machen, aber was genau wie, das sagt uns Netflix hier halt irgendwie nicht.

Und als Ausgangsperspektive oder als weitere Perspektive sagen sie dann, naja, also es kann mehr Projections geben, also wir werden mehr Datenformate unterstützen, um da mehr Möglichkeiten zu haben.

Zum Beispiel auch sowas wie Protobuf, binäre, eher effiziente Protokoll oder sowas wie gRPC als weitere Kommunikationsmöglichkeit.

Wir werden den Logistik-Graphen materialisieren.

Also ich denke mal, dass der dann nicht nur das konkrete Datenstrukturen vorstellt und weitere Probleme in Bezug auf die Suche über diesen Graphen lösen.

So, soweit Schnelldurchlauf sozusagen für dieses Paper.

## Bewertung und Kritik

Jetzt ist halt die Frage und damit komme ich sozusagen zu dem dritten Teil.

Also was bedeutet das jetzt für uns und was ist eigentlich so das Ergebnis und wie bewerten wir das?

Also zurück zu dem Problem.

Wenn wir halt tatsächlich diese Lösung bauen, um Datenqualität zu erhöhen, also das Kapanzene aufzulösen, kaputte Referenzen aufzulösen und diese Verbindung zwischen den Systemen halt irgendwie hinzubekommen, dann kann ich mir nicht vorstellen, dass der Aufwand, den man dafür treibt, in einem vernünftigen Verhältnis zu den Nutzen steht.

Das heißt also, ich würde behaupten, dieses Problem, was wir ursprünglich genannt haben, ist nicht das Problem.

Ich glaube, dass Sie eigentlich eine Analyseplattform bauen wollen und insbesondere Sphere läuft ja auch in diese Richtung.

Also ich mache welche Reports, mache solche Geschichten.

Dann haben wir aber eigentlich was anderes gebaut.

Wir haben ein System gebaut, mit dem wir Datenanalyse betreiben können.

Hier wieder die Beziehung Richtung Data Meshes, Data Products, wo ich also irgendwelche Daten, die ich in dem System habe, so darstellen kann, dass ich sie anschließend analysieren kann.

Ich habe jetzt hier eigentlich ein Architekturansatz.

Ich habe verschiedene natürliche Datenrepräsentationen, GraphQL, Afro, whatever.

Ich versuche, das zu vereinheitlichen, mit einer Plattform und einer gemeinsamen Sicht darauf anzubieten.

Das ist etwas anderes, als wenn ich jetzt jedem Team sagen würde, die Daten, die du hast, da sind Menschen, die sich vielleicht für diese Daten interessieren.

Stell denen die doch zur Verfügung und mach das irgendwie.

Was der Data Mesh bzw.

Data Product Ansatz wäre, so wie ich ihn verstehe.

Das heißt, ich habe hier eine Integrationsplattform, die versucht, das alles unter einen Hut zu bekommen.

In dem anderen Fall hätte ich einen Marktplatz von Daten.

Mir gefällt dieser Marktplatz von Daten besser, weil ich dadurch Teams im Prinzip die Freiheit gebe, die Daten eigenständig in irgendeinem vernünftigen Format zu exportieren und jedem Team übertrage, das irgendwie zu machen.

Ich habe auch das Gefühl, dass das wahrscheinlich technisch weniger aufwendig ist.

Aber wie dem auch sei.

Man kann jetzt wahrscheinlich eine Architekturdiskussion führen und schauen, welche Vorteile das andere System hat.

Ich finde es ehrlich gesagt ein bisschen schwierig, das so ad hoc zu sehen, was da die Vorteile wären.

Und er könnte dann diese Ansage auch normal hinterfragen.

Ja genau, also der Marco Wesselmann schreibt, was das eigentlich der Karl Schmolke gerade geschrieben hat, ich auch nicht und noch sehe ich auch noch kein wirtschaftlich rechtfertigbares zugrundeliegendes Problem.

Was hat er weiter geschrieben?

Den wirklichen Grund beziehungsweise Ziel, wo sie darauf hinaus steuern, werden sie nicht öffentlich kundtun.

Naja, also nichts zu sagen, wir bauen halt eben eine Datenplattform und Daten zu analysieren, finde ich, können sie halt schon sagen.

Aber das ist der nächste Punkt, den ich sozusagen diskutieren wollen würde.

### Technische Komplexität

Ich habe mir hier aufgeschrieben, overengineering.

Also was das bedeutet ist, dass wir halt jetzt einen massiven Aufwand betreiben, um eine Infrastruktur zu schaffen mit in der Menge Zeug, das nicht Netflix spezifisch ist, in dem Sinne, dass es jetzt speziell abgestimmt ist auf Filme.

Das ist im Prinzip ein Datenanalyse Problem mit verschiedenen Datenquellen und das ist halt kein Netflix Problem, sondern das ist was anderes.

Das führt natürlich dazu, dass es jetzt ganz viele spannende Engineering Probleme gibt.

Also man kann sich vorstellen, dass da Sachen sind, die Techniker gerne lösen wollen, wobei ich eigentlich lieber Geschäftslogik bauen würde, aber sei es drum nicht.

Also es gibt eben Leute, die gerne technisch komplizierte Sachen lösen und das ist hier sicher ein schönes Spielfeld dafür.

Und das ganze Paper ist halt voll mit ganz viel Technik.

Ich habe es ja erzählt, es gibt APA und es gibt Sphere und es gibt PDM und was weiß ich und das ist ganz viel in dieser Richtung, aber wenig über konkrete Probleme.

Genau, Kaschmolka hat auch noch mal geschrieben, was ist eigentlich der geschäftliche Zweck?

Genau, das fehlt halt so ein bisschen und das ist ein bisschen etwas, was Netflix hat auch bei dem Microservices Zeug bereits gemacht hat.

Die haben eben auch eine eigene Microservices Stack gebaut mit einer Menge an Open Source Projekten und dabei zum Beispiel auch diese Resilience Lösung gebaut, das Hystrix, was ja mittlerweile eingestellt worden ist und das ist glaube ich da im Prinzip dasselbe.

Also wir investieren viel Aufwand, um eine Infrastruktur zu schaffen für irgendein Problem und also bei dem Microservices Stack kann man noch diskutieren, ob es keinen am Markt gab.

Hier ist halt mein Gefühl, also zumindest eine oberflächliche Recherche ergibt halt, dass es halt Integrationsplattformen gibt, die sowas wie eine Ontologie und so etwas unterstützen.

Das bedeutet für mich, Kunden, die ich typischerweise berate, dem würde ich halt nicht dazu raten, dieses zu tun, weil das massiver, tinscher Aufwand ist und es ist nicht so klar, was der Vorteil ist und ich würde mich fragen, ob ich nichts kaufen kann.

Ich investiere da irgendwie in Infrastruktur, nicht in meine spezifische Geschäftslogik und das ist halt selten eine gute Idee.

Cashmoney hat nochmal geschrieben, das werden sie erst auflösen, wenn sie damit erfolgreich waren.

Mitbewerbervorteil, ja sicher werden sie wahrscheinlich nicht darüber öffentlich reden, aber es ist trotzdem irgendwie komisch, dass sie dort so wenig, also ich kann ja auch abstrakt über Geschäftsprobleme reden, also dass ich sage, ich will Sachen analysieren und das tun sie halt wenig bis gar nichts.

Ich habe das Gefühl, dass diese starke technische Motivation, dieses Over-Engineering und die Ablehnung von Kaufsoftware, dass das bei diesem Blogartikel irgendwie durchschreitet.

Es ist ja auch nicht so, dass sie schreiben, hey und das ist übrigens so, dass es da zwar Lösungen am Markt gibt, aber die passen auf uns nicht, weil folgende Gründe, sondern es steht einfach da, wir haben es dann irgendwie gelöst.

### Motivation hinterfragen

Warum veröffentlichen sie das ganze?

Das hatte ich mir noch aufgeschrieben.

Das ist ja auch so eine Frage.

Wollen die uns irgendwas mitteilen?

Ist das irgendwie eine Motivation?

Sie schreiben, dass sie sich mit anderen Leuten vernetzen wollen, die Ähnliches bauen und ich glaube insgesamt ist das ein Versuch, um Engineers zu gewinnen, die gute Engineers sind, weswegen das vielleicht auch eine technische Diskussion ist.

Solche Blogs macht man jedenfalls nicht, um mehr Zuschauer zu gewinnen, sondern ich glaube, dass es letztendlich Personalmarketing ist, wenn es einen Grund gibt.

Jetzt ist die Frage, ist es denn nun tatsächlich so ein Widerspruch zu dieser Idee, mehrere Modelle zu haben?

Ich glaube, das ist kein solcher Widerspruch.

Der erste Punkt ist, vielleicht ist das, worüber wir reden, tatsächlich nur einbauende Kontexte.

Es ist Content Engineering und Content Engineering nicht von dem Pitch bis es zum Launch geht.

Da kann es sehr gut sein, dass ein Modell und eine Art, Daten zu repräsentieren, ausreichend ist.

Vielleicht ist das eine Erklärung, um diese beiden Sachen miteinander zu vereinbaren.

Das Ziel ist nicht, Aufwand zu sparen.

Stefan hat in seinem Artikel damals geschrieben, wenn ich es einmal modelliere, dann habe ich es einmal modelliert, kann es wiederverwenden, das ist einfacher.

Das ist nicht das, was Sie schreiben, das schreiben Sie ganz deutlich nicht, sondern es geht eben um Analyse.

Es gibt Möglichkeiten, das allgemeine Modell zu erweitern.

Das hatte ich bei AppA genannt, bei dieser Sprache, mit der man diese Schemata definieren kann.

Ich hatte auch gesagt, dass dieses S-Kurs in dem PDM sogar ermöglicht, dass Teams ihre eigene Sprache nutzen, ohne jetzt mit dem PDM in Kontakt zu sein.

Das kann bedeuten, dass es tatsächlich mehrere Modelle gibt, aber das steht nur am Rande da.

Jetzt hat Karl Schmeuke geschrieben, in einem möglichen Grund den Ansatz vom Sparen zu challengen.

Dafür ist es zu spät.

Die sind sehr lange in diese Richtung marschiert, haben offensichtlich ganz viele Systeme gebaut.

Das ist weit über eine Idee hinweg.

Ich glaube, dass man das nicht mehr ernsthaft ohne Gesichtsverlust kassieren kann.

Dann hat Tobias Böschel geschrieben, das kann eigentlich nur KI getrieben sein.

Singuläre Datenhaltung über die gesamte Geschäftsdomäne bedeutet Verfügbarkeit für allwissende Agenten.

Das könnte auch sein.

Da muss man vielleicht auch hinzufügen, dass vom Business-Usern tatsächlich die Sprache ist.

In dem gesamten Artikel erinnere ich zumindest nicht, dass AI oder KI angesprochen worden ist.

Aber Tobias, du hast recht.

Das ist etwas, was in so eine Motivation gehen könnte.

Ich habe diese Daten bestimmt und die sollen durch AI analysiert werden.

Ich hatte es am Anfang gesagt, so etwas wie eine Published Language oder Datenprodukte sind okay und sinnvoll.

Datenprodukte sind sicherlich eine ganz hervorragende Ergänzung zu so etwas wie Domain-Driven Design.

Das kann durchaus sein, dass wir gerade so einen Fall hier eigentlich sehen.

Vielleicht ist das eben genau so etwas, was konzeptionell einer Published Language oder solchen Datenprodukten aus dem Data Mesh ähnelt und dann dafür sorgt, dass man sagt, hier gibt es eine Repräsentation, die ich nach außen entgebe für die Analyse.

Ich habe eine interne Repräsentation.

Das sind zwei getrennte Sachen.

Diese interne Repräsentation ist für mich speziell und die nach draußen ist eine, die ich für die Analyse anbiete.

Dann hätte ich da eben auch keinen Widerspruch.

Der Daniel Pützinger hatte bei LinkedIn noch gesagt, im Domain-Driven Design gibt es ja ein paar Patterns, die er zumindest in diesem Text wiederfindet.

Er nannte da zum Beispiel Shared Kernel.

Shared Kernel ist etwas, wo ich ihm sage, zwei unterschiedliche Modelle haben einen gemeinsamen Kern.

Das ist das, was Shared Kernel sagt.

Ich sehe hier kein Shared Kernel, weil Shared Kernel Modelle sind für mich Logik.

Wir teilen hier keine Logik, sondern wir reden hier nur über den Austausch von Daten.

Sonst könnte das sein, dass man sowas per einen gemeinsamen Datenkern definiert.

Dann schrieb er noch sowas wie ein Open-Host-Service.

Das könnte das sein.

Open-Host-Service ist nach meinem Empfinden eine Schnittstelle, die viele andere Teams konsumieren.

Was auch wiederum bedeutet, Zugriff auf Logik.

Das sehe ich hier auch nicht.

Das ist meiner Ansicht nach ein Datenformat, keine Schnittstelle.

Es ist auch ein Datenformat, das sozusagen aufgepoppt wird.

Man sagt allen, bitte konvertiere deine Daten in dieses Datenformat oder ziehe dieses Datenformat vielleicht sogar in deine Systeme mit rein.

Dann hat er noch genannt als Pattern Conformist.

Conformist ist ein Pattern, wo jemand ein Modell vorgibt und die anderen müssen das nutzen und haben kein Mitspracherecht, also kein Veto-Recht oder keine Möglichkeit, das weiterzuentwickeln.

Zum Beispiel, weil es vielleicht ein Legacy-System ist und das Legacy-System nicht anpassbar ist, sodass man mit dem leben muss, was dort ist.

Es wäre eine ähnliche Geschichte.

Es ist für mich eher eine Sache, die etwas mit Logik zu tun hat.

Conformist hat eher etwas mit Logik zu tun.

Es hat insbesondere eine bilaterale Beziehung, wo ich also zwei Teams habe, die miteinander reden.

Das sehe ich hier auch nicht.

Insgesamt ist es halt eher etwas, was für mich in die Datenintegration geht.

Es ist tatsächlich so, dass in den gesamten Blogposts, in meiner Erinnerung, keine Funktionalitäten besprochen werden.

Es wird nirgendwo gesagt, auch nicht bei diesem One-Piece-Beispiel, was man jetzt eigentlich mit diesen Daten anfangen will, sondern es wird nur gesagt, die Daten sind da und ich kann sie mir angucken und analysieren.

Das ist meiner Ansicht nach nicht das, was DDD-Modelle, die speziell darauf ausgerichtet sind, komplexe Logik zu implementieren, wo das hingeht.

Mutex.ab bei den Heise-Foren hat dann noch geschrieben, das könnte ich auch mit Datenbanken und Datenbank-Links umsetzen.

Eine gemeinsame Sicht mit Views und darüber kriege ich das hin.

Ja, aber hier kann ich mit mehr Heterogenität umgehen.

Ich habe sowas wie GraphQL, was ja nicht eine Datenrepräsentation ist, sondern da ist es so, dass ich über HTTP REST stelle und mich Daten zur Verfügung stelle.

Dann habe ich sowas wie dieses Apache Iceberg.

Dann habe ich halt Dataproducts aus dem Data Mesh und die können andere Persistenztechnologien benutzen.

Das heißt, ich habe hier tatsächlich eine flexiblere Möglichkeit und ich muss auch gestehen, solche Systeme, die versuchen, sich über die Datenbank zu integrieren, das ist eine von den Sachen, wo ich in meiner Beratungspraxis zu oft gesehen habe, dass das dazu führt, dass man ein großes kompliziertes Modell hat, was de facto dann eben von vielen Systemen genutzt wird und schwer änderbar ist.

Davon würde ich generell eher Abstand nehmen.

Ich halte Integration über die Datenbank, über sowas wie Datenbankviews und so weiter eher für schwierig.

Auch da kann man im Einzelfall wahrscheinlich diskutieren, aber ich würde davon eher Abstand nehmen, weil ich Angst davor hätte, dass man dann am Ende bei einem großen komplizierten Datenbankmodell rauskommt, das irgendwie schwerwertig ist.

Was mich noch insbesondere gewundert hat, ist, ich hatte es vor allem bei Stefans Artikel nochmal gesagt, es gibt also jetzt ein paar, also warum legen wir, ich, so viel Wert darauf, dass wir getrennte Modelle haben und Systeme aufteilen mehrere Modelle.

Einmal deswegen, weil wir sonst in konzeptionelle Schwierigkeiten kommen.

Ein Kunde, der eincheckt, ist eben nicht der Kunde, der die Rechnung bekommt.

Und dann, weil diese umfangreichen großen zentralen Modelle super schwierig zu ändern sind.

Es passiert zu häufig, dass man sagt, ich habe hier eine große Datenbank, da ist ein großes kompliziertes Modell drin.

Dann habe ich lauter Systeme drumherum und dann versuche ich, die Systeme aufzuteilen.

Aber das klappt nicht, weil ich diese Datenbank im Kern habe.

Die Datenbank kann ich nicht aufteilen, weil niemand weiß, welche Daten welches System nutzt.

Und dann habe ich letztendlich ein ganz schwieriges Problem, jemals dieses System aufzuteilen.

Und zu diesem Thema, dass ein gemeinsames Modell auf der Datenebene zu einer starken Kopplung und zu einer Schwierigkeit führt, das System vernünftig zu modularisieren, findet man halt auch nichts in dem Blogbeitrag.

Und das ist so ein bisschen die Meta-Ebene.

So ein Papier zu schreiben und zu lesen ist eine Form von Kommunikation.

Die haben gesagt, wir schreiben einen Blogbeitrag und wir sitzen jetzt hier nicht und reden drüber, sondern ich habe den Blogbeitrag gelesen, glaube ihn irgendwie verstanden zu haben.

Und das ist eine indirekte Art von Kommunikation.

Ich habe nie mit diesen Menschen direkt gesprochen.

Und das führt dazu, dass es jetzt so eine Menge an Fragen gibt, die man jetzt stellen müsste.

Also was ist denn nun wirklich das Problem?

Ist es eigentlich ein Integrationsproblem?

Dann wäre für mich die Frage, was ist mit der Autonomie der Teams?

Wie stark ist die Modellierung tatsächlich unabhängig?

Habt ihr da Schwierigkeiten?

Habt ihr einen hohen Koordinationsaufwand?

Lauft ihr an so ein Problem, dass ihr ein großes Datenmodell habt, was niemand mehr versteht und auseinandernehmen kann?

Das wäre so etwas, wo man sich wahrscheinlich mal fünf, zehn Minuten oder vielleicht eine halbe Stunde zusammensetzen könnte und dann deutlich mehr wüsste.

Ich finde das nochmal wichtig, weil es mir zu häufig passiert, dass Leute sagen, hey, neue Menschen sollen bei uns irgendwas machen und da sind Schwierigkeiten und deswegen brauchen wir mehr Dokumentation.

Das hilft halt irgendwie nicht.

Das sieht man hier relativ gut.

Also man sieht irgendwie nicht, das ist gut geschrieben, das ist verständlich.

Trotzdem ist es so, dass da ein massiver Informationsverlust ist, weil wir eben nicht miteinander direkt gesprochen haben.

Da wäre jetzt für mich auch die Frage, was Sie sagen würden zu diesen verschiedenen kleinen Modellen, die wir ja eigentlich predigen.

Ich bin mir nicht sicher, ob Sie sagen würden, das ist ein Fehlansatz.

Das weiß ich nicht, weil Sie auf einer anderen Ebene sind bei dieser Datenanalyse in erster Linie.

Mich würde interessieren, warum Ihr Datamash, was Sie haben, nicht ausreichend ist.

Das wäre da so der Punkt.

Mich erinnert das auch ein bisschen zu diesem Paper, was ich vor einiger Zeit mal diskutiert habe.

Ich packe den Link dazu auch nochmal in die Shownotes, wo in der öffentlichen Wahrnehmung stecken übrig geblieben ist.

Amazon macht jetzt Monolithen statt Microservices und das stand halt in dem Paper einfach nicht drin.

Ich glaube, das ist hier was Ähnliches.

Es steht hier nicht drin, Bau einen Kontext und mehrere Modelle sind eine blöde Idee, sondern es steht irgendwie was anderes drin.

Ich glaube, es steht was drin in der Datenanalyse.

Lass uns nochmal durch die Fragen gehen.

Also Asmir Abdi hat gefragt, geht Netflix zu der Daten-Centric-Architecture?

Nein, glaube ich nicht.

Ich glaube, die bauen einfach eine Daten-Integration da am Ende.

Und man sieht es unten, softverbinden-architektur.tv findest du die Episode dann auch nochmal komplett und kannst sie nachhören oder dir angucken.

Karl Schmolka hat geschrieben, mögliche Gründe.

In der Vergangenheit haben sie viele autonome Teams dem Part, wenn dann immer nachrängig behandelt.

Darüber steht dann nichts drin und das ist halt tatsächlich komplette Mutmaßung, dass irgendwie eine zu große Autonomie dort zu einem Problem geführt hätte.

Und selbst wenn, dann kann ich halt Makroarchitektur-Regeln definieren, die halt sagen nicht, also Bau halt ein Datenprodukt, bietet das an und macht das vernünftig.

Was steht hier noch?

Karl Schmolka schrieb, der Aufruf, doch bitte Daten zu bedienen und zu befüllen, wurde nicht ausreichend und zufriedenstellend bedient.

Also zwingt man jetzt die Entwicklungsteams.

Also wie gesagt, es ist eine komplette Mutmaßung.

Und selbst wenn dem so wäre, fände ich, ist das ein Antipattern, weil das ist ein soziales Problem.

Die Teams machen nicht das, was sie eigentlich tun sollten und was sinnvoll wäre.

Und ich baue dann halt eine technische Lösung dafür, halte ich nicht für eine gute Idee.

Kann man machen, schrieb halt dazu.

Ich warte noch eine Sekunde, ob noch weitere Teams sind.

Sonst wäre das sozusagen meine kurze Zusammenfassung dazu.

Und vielen Dank nochmal für den Hinweis auf das Paper.

Nächste Woche wird es aller Voraussicht nach keine Episode geben.

Das hängt damit zusammen, dass ich so ein bisschen Zeitschwierigkeiten da gerade habe.

Die übernächste Woche ist was geplant.

Und zwar am 5.9. kommt dann das Thema Webperformance mit Lukas Domen und Lisa.

Das wird also auf jeden Fall die nächste Episode sein.

Vielleicht gibt es vorher nochmal was.

Aber da könnt ihr dann auf die Webseite gucken.

Vielen Dank für die vielen Fragen.

Vielen Dank für die Inspiration, für die Diskussion.

Und ich wünsche dann schon mal ein schönes Wochenende und bis dahin.