So, dann herzlich willkommen zu einer weiteren Episode von Software-Architektur im Stream.

Bevor wir loslegen, so ein paar Hinweise.

Einmal ist es so, wir haben am Montag tatsächlich einen Stream, so ein bisschen außerhalb der Rolle, der Reihe, mit dem Woody.

Der hat zum einen das Thema Mob-Programming oder Ensemble-Programming so ein bisschen aus der Taufe gegoben.

Wir sprechen über ein anderes Thema, und zwar über das Thema Beyond Estimates bzw.

No Estimates.

Das heißt, dass man Software agil entwickelt, ohne dass man Dinge abschätzt.

Das ist ein Agile-Meets-Architecture-Special.

Das ist eine Konferenz, wo es um das Thema Agilität und Architektur geht.

Woody wird da einen Talk halten, und das ist so ein bisschen eine Vorbereitung.

Dann können wir zum aktuellen Thema übergehen.

Heute geht es um das Thema KI und LLMs kritisch betrachten mit Lucas.

Schön, dass du da bist.

Lucas, möchtest du kurz zwei Worte über dich sagen?

Ja, hallo Eberhard.

Gerne.

Ich bin der Lucas.

Ein paar Leute, die den Stream schon länger verfolgen, haben mich vielleicht auch schon mal hier gesehen.

Ich war früher auch schon mal da, als wir beide noch bei einer anderen Firma zusammengearbeitet haben.

Heute bin ich bei der Firma Komoot, die eine App macht fürs Wandern und Fahrradfahren, wo man Routen entdecken kann und so weiter, und leite dort das Webteam.

Das hat mit dem Thema heute überhaupt gar nichts zu tun, aber das ist das, was ich sonst so tue.

Vielleicht ein bisschen zur Einordnung.

Du, Lucas, hattest ja schon bei dem Freelancer-Podcast eine Episode gemacht zu diesem Thema, was wir heute haben, und außerdem bei dem Boardgame-Theory-Podcast, der, glaube ich, tatsächlich über Boardgames sonst spricht, oder?

Genau.

Ja, okay.

Und das ist also sozusagen so ein bisschen eine Fortsetzung dieser Reihe.

Ich verlinke die beiden Episoden auch.

Aber Lucas ist, wie gesagt, jemand, der schon länger dabei ist, und wir haben ja auch wieder eine stärkere Beziehung.

Und vielleicht kurz zur Gesamteinordnung.

Also, wir haben bei Software-Architektur im Stream im Moment informell so ein bisschen so einen AI-Fokus.

Und das hängt irgendwie offensichtlich mit dem Hype zusammen, aber das hängt irgendwie auch damit zusammen, dass eben Ralf dazu gestoßen ist, bei dem das halt irgendwie ein Schwerpunktthema ist, und ich glaube auch, dass es tatsächlich ein total spannendes Thema insgesamt ist.

Und es ist so ein bisschen so, wir hatten halt diese Episode gemacht, von wegen, ist AI eigentlich unter oder überhyped?

Und das basierte halt darauf, dass ich Blogposts geschrieben hatte, die eigentlich gesagt haben, AI ist irgendwie overhyped.

Und dann hatten wir uns halt zwei Leute eingeladen, die halt gesagt haben, nee, es ist unterhyped.

Und das wenig überraschende Ergebnis der ganzen Geschichte war, dass wir dann eben am Ende eine Episode gemacht haben, wo eigentlich die Aussage eher rauskam, naja, es ist irgendwie unterhyped und der Hype ist gar nicht ausreichend.

So, nun ist es halt so ein bisschen so, dass das, glaube ich, insgesamt zu einem starken Bias geführt hat.

Und da ist diese Episode so ein bisschen ein Gegengewicht.

Und was mir halt beim Vorgespräch aufgefallen ist, ist, dass viele von den Dingen, die wir, glaube ich, heute diskutieren, sind Dinge, von denen ich geglaubt habe, dass sie eigentlich sozusagen eh klar sind.

Und das ist halt irgendwie immer gefährlich.

Also ich als Berater und irgendwie jemand, der sich mit Softwarearchitektur und Softwareentwicklung beschäftigt, sind ganz viele Dinge, die mir halt sozusagen eh klar sind, sind irgendwie super unklar irgendwelchen anderen Leuten.

Und deswegen ist das, glaube ich, hier eine Episode, die halt eine ganz wichtige Lücke so ein bisschen füllt.

Und da eben auch nochmal so ein bisschen über Basics spricht.

Und das ist so ein bisschen die Einordnung.

Genau.

Und die Initiative ging tatsächlich bis zu einem gewissen Maß von dir, Lucas, aus.

Also vielen Dank dafür.

Gerne.

Und dann können wir eigentlich, glaube ich, inhaltlich loslegen, oder?

Ja, gerne.

Von meiner Seite aus.

Und ich hatte ja gesagt, Grundlagen.

Das heißt, die erste Frage wäre halt, wo kommt eigentlich dieser Begriff?

Ach so, und dann noch ein Hinweis.

Normalerweise ist es halt so, dass ich halt versuche, Menschen zu interviewen und ihnen halt irgendwie ganz viel Platz zu lassen und möglichst mich so ein bisschen nach hinten zu stellen.

Wir werden heute, glaube ich, werde ich halt tatsächlich an einigen Stellen nicht umhinkommen, meine eigene Meinung unter der Ergänzung halt loszuwerden.

Das haben wir aber tatsächlich vorher so abgesprochen.

Und naja, das ist vielleicht etwas anders.

Gut, alles klar.

Genau.

Also zu deiner Frage, wo kommt dieser Begriff her?

Das ist tatsächlich wirklich interessant, weil sich das auch so ein bisschen heute wieder widerspiegelt.

Die Geschichte setzt sich im Prinzip fort.

Wenn man so in den Begriff wirklich schaut, dann wurde der von John McCarthy geprägt, der vor allem dafür bekannt ist, die Lisp-Programmiersprache erfunden zu haben.

Und der hat auch gesagt, das ist ein, später gesagt, das ist ein Marketingbegriff.

Er wollte etwas, mit dem er Funding bekommt, mit dem er seine weiteren Arbeiten unterstützen kann.

Und das klang einfach super.

Und dieser Begriff hat sich immer hin und her befruchtet, auch mit dem Science-Fiction-Bereich.

Auch im Science-Fiction-Bereich denken wir auch an so Sachen wie Isaac Asimov, wo es einfach darum ging, diese große Frage, die uns alle auch irgendwie beschäftigt, so was ist eigentlich Bewusstsein?

Was ist eigentlich der Mensch?

Also all solche Sachen wurden ja von der Science-Fiction immer begleitet.

Und da ging es ja auch immer um humanoide Wesen, ob das jetzt Aliens sind, ob das jetzt Roboter sind.

Und auch aus diesen Überlegungen kommt das her.

Und das ist dann immer hin und her gespielt worden.

Und wichtig an der Stelle ist vielleicht auch noch der Turing-Test, den vielleicht auch schon viele gehört haben von Alan Turing, einer der auch der Pioniere der IT, der ja auch die Frage stellt, wie kann ich erkennen, ob jemand anderes eine Intelligenz ist oder ein Roboter oder ein Computerprogramm.

Das heißt also, das beschäftigt die Menschen schon sehr lange.

Und wenn man dann diese Geschichte verfolgt, dann sieht man immer wieder große Meilensteine in der KI.

Und immer wenn so ein Meilenstein erscheint, dann wird sofort gesagt, jetzt ist der Punkt erreicht, wir haben menschliche Intelligenz, in drei Jahren.

Und in drei Jahren brauchen wir keine Menschen mehr, dann macht das alles die KI.

Oder ich bin mir sicher, diese KI hat jetzt Gefühle entwickelt oder solche Sachen.

Das begleitet uns, seit es diesen Begriff gibt.

Das ist nichts Neues, das ist nicht jetzt durch LLMs irgendwie neu passiert.

Und das finde ich halt so interessant daran, dass das immer wieder passiert.

Und genau, das zur Geschichte.

Wenn man jetzt einen ganzen Geschichtsabriss macht, dann ist der Stream voll, glaube ich.

Genau, so ein paar ergänzende Sachen an der Stelle.

Das ist ja gesagt, 1955, und zwar absichtlich, um es mit Marketing zu erfüllen.

Und ich glaube, das ist ein wichtiger Punkt, den man sich vergegenwärtigen muss.

Das Ding ist irgendwie absichtlich misleading.

Weil eigentlich ist eben, wie wir später sehen werden, reden wir über irgendwelche Algorithmen.

Und das ist nicht wirklich Intelligenz.

Und Intelligenz zu definieren, ist irgendwie schwierig.

Die andere Sache, das hattest du in dem anderen Podcast auch gesagt, diese Vorhersage, dass halt irgendwann etwas Revolutionäres passieren sollte.

Ich hatte jetzt noch mal geschaut, und es gibt halt diesen Marvin Minsky.

Das ist so einer von den Informatikpionieren, KI-Pionieren, nicht Informatik.

Und der Wikipedia-Artikel sagt halt, er habe vorausgesagt, dass es bald möglich sein würde, Emotionen in eine Maschine hineinzuprogrammieren.

Die Aussage an sich finde ich schon absurd.

Das passt nicht.

Wir können eine Maschine nahezu per Definition und keine Emotionen haben.

Reden wir mal.

Selbst Data ist daran halt gescheitert bei Enterprise Next Generation.

Und ich muss gestehen, ich habe bei dem Podcast, den ich mit dir gehört hatte, das glaube ich so ein bisschen nicht geglaubt.

Dass dann vorhergesagt wird, bald passiert die große Revolution, und dass das schon immer so war.

Und es stellt sich halt heraus, dass der Marvin Minsky 1970 gesagt hat, dass in drei bis acht Jahren, also 1973 bis 1978, es Maschinen mit der durchschnittlichen Intelligenz eines Menschen geben werde, die Shakespeare lesen und Autos warten würden.

Und das ist tatsächlich ein Beispiel für exakt das, was du gesagt hast.

Da kann man exakt sagen, der Minsky hat eben genau das gesagt, zu einer Zeit, wo das halt irgendwie lächerlich war.

Es ist halt irgendwie die Zeit, wo wir Terminals, Timesharing, die ersten Timesharing-Systeme, Lochkarten gerade hinter uns gelassen haben.

Das ist vollkommen absurd.

Die Computer, die damals existiert haben, müssen sich gegenüber einem iPhone heute verstecken.

Und diese anthropomorphen, also nicht menschenzentrierten Metaphern, das ist halt auch etwas, was sich durchzieht.

Maschinelles Lernen ist etwas, was sagt, das ist genau das.

Wer das Ding lernt, und eben künstliche Intelligenz, das zieht sich halt durch.

Und das führt zu dieser Personifizierung.

Was ich halt auch bei mir immer feststelle, dass man von ChatGPT als er oder von Claude als sie redet.

Dabei ist das halt ganz klar ein Es.

Es ist halt nicht ein Mensch, sondern es ist eben ein Algorithmus.

Und dass man das überhaupt benennt, Claude hat personifiziert.

Und diese ganze Geschichte führt halt schon auf so einen komischen Weg.

Genau.

Auch da finde ich es interessant, wie früh man diesen Effekt hatte, dass die Leute auch wirklich Menschlichkeit in Sachen reininterpretiert haben.

Der Eliza-Effekt kam ja auch schon mal hier im Stream vor.

Da muss man sich auch klar machen, das war 1966, also das ist auch schon eine ganze Weile her, wo Joseph Weizenbaum diesen Chatbot gebaut hat.

Und der war super einfach.

Das hat nichts mit dem zu tun, was heutzutage eine LLM macht.

Und trotzdem haben Leute dann gesagt, dieser Bot versteht mich und ich tausche mich mit dem aus und endlich habe ich einen Psychiater, der mit mir spricht.

Wir sind sehr anfällig dafür, Dinge, die Sprache verwenden, zu vermenschlichen.

Und das machen sich solche Produkte halt auch zunutze.

Die wissen, dass das gut funktioniert.

Heute sagt man dann wieder, damals.

Aber die Leute waren ja nicht anders, als wir das heute sind.

Wir würden auch darauf reinfallen heute.

Und das sollte man sich immer bewusst machen.

Genau.

Zu dem Punkt.

Eliza ist tatsächlich so, dass ich in den 80ern meiner Ansicht nach ein Basic-Listing abgetippt habe.

Das sind 30-Zeilen-Code oder sowas.

In Emacs ist das immer noch drin, mit dem Meta-Extraktor.

Das ist so ein Ding, wo man sagt, mir geht es heute nicht gut.

Dann sagt das Ding, warum geht es dir nicht gut?

Dann sagt man, weiß ich nicht, weil meine Mutter.

Dann kommt er zurück, sagt mir mehr über deine Mutter.

Das funktioniert im Wesentlichen so, dass er die Sätze umformuliert.

Das ist einfach reflektiert.

Also nicht zurückfragt, mir geht es heute nicht so gut.

Das ist ja eigentlich nur eine Umstellung des Satzes.

Dann reagiert er auf Schlüsselwörter wie meine Mutter.

Das, was du gerade gesagt hattest, da gibt es diese Geschichte, dass seine Sekretärin angefangen hat und gesagt hat, ich möchte nicht, dass du meine Dialoge mit Eliza liest.

Das impliziert, dass dort diese Personifizierung so weit gegangen ist, dass man sozusagen ein Verständnis sieht.

Und über echte Probleme redet.

Das ist insofern ganz extrem schwierig, weil Psychoanalyse und das ganze Zeug, was da herumschwirrt, ist zum einen eine medizinische Geschichte.

Und zum anderen setzt es darauf, dass mich jemand versteht.

Gerade das ist nicht der Fall.

Das hat dazu geführt, dass der gesagt hat, hier läuft gerade was schief.

Es gibt dieses Buch hier, die Macht der Computer und die Ohnmacht der Vernunft von ihm, was aus den 70ern kommt.

Wo er, glaube ich, ein bisschen umgewendet ist.

Um den Punkt noch zu Ende zu bringen, einmal habe ich diese Geschichte mitgenommen, dass AI und KI diese starke Verführung hat.

Und das sehe ich auch sehr stark in dem, was jetzt gerade passiert mit ChatGPT.

Das ist dasselbe Ding.

Nur eben noch mal in krasser.

Wir reden halt nicht über Eliza.

Und die Sache, die ich meiner Ansicht nach aus dem Buch mitgenommen habe, ich habe das jetzt ehrlich gesagt nicht noch mal gelesen.

Ich habe es vor langer Zeit gelesen.

Im letzten Jahrhundert, glaube ich.

Aber mir ist das noch im Gedächtnis.

Das ist diese Geschichte mit, nehmen wir jetzt mal an, der Laptop landet auf einem fremden Planeten.

Nehmen wir jetzt mal im Weiteren an, dass diese Aliens dazu in der Lage sind, diesen Laptop zu simulieren.

Also vorherzusagen, was der halt tut.

Dieser Pixel ändert sich unter diesen Bedingungen folgendermaßen.

Und vielleicht sogar eine Kopie herstellen können, der diesen Laptop simulieren.

Es ist die Frage, was bedeutet das denn?

Was das bedeutet, ist, dass ich etwas Identisches habe, was mir genauso fällt wie mein Laptop.

Aber ich habe dadurch nicht verstanden.

Auf diesem Laptop ist jetzt die E-Mail, mit der ich Lucas gesagt habe, hey, wollen wir nicht eine Episode machen?

Oder vielleicht ein Chatbeitrag?

Das ist der Abstract zu dieser Episode.

Das ist nachher die Aufnahme von dieser Episode.

Und wir reden über ein Thema.

Und wenn man das alles simuliert, wenn ich in den Explorer gehe, ich bin auf einer Windows-Maschine, dass man das frei doppelt klickt und das Video sieht.

Das bedeutet, dass null klar ist, was eigentlich hier passiert.

Und das fand ich spannend, weil das führte zu der Frage, was ist denn eigentlich echtes Verständnis?

Und Weizenbaum macht letztendlich einen Punkt, dass er sagt, echtes Verständnis impliziert Körperlichkeit.

Also nur dann, wenn ich weiß, was es zum Beispiel bedeutet, es bedeutet, zu leben, bestimmte Sinnempfindungen zu haben, das selber erfahren habe, kann ich das wirklich verstehen.

Und darüber kann man jetzt diskutieren, ob das tatsächlich so ist.

Im Sinne von limitiert das sozusagen die Einsatzfähigkeit der AI.

Aber was das auf jeden Fall bedeutet, ist, dass man vorsichtig sein muss mit dem ganzen Verstehen.

Ja, absolut.

Befürchte, wir müssen mal durch den Chat durchgehen.

Ja, da passieren Dinge.

Genau, also ich habe auf alles eigentlich gleich ein bisschen viel, aber genau, TheInnocentKitten hatte geschrieben, bei einer Maschine erwarte ich ja gar keine Emotionen, sondern korrekte Antworten, zumindest im professionellen Umfeld.

Das finde ich halt auch so interessant, auch wenn man sich zum Beispiel Star Trek anschaut.

Du hast jetzt auch schon mehrfach Data erwähnt.

Ich glaube, das hat auch so ein bisschen unsere Wahrnehmung davon, was so KI und so weiter ist, geprägt.

Also zum einen gebe ich Star Trek daran die Schuld, dass alle Leute denken, Textinterfaces wären besser als alles andere.

Aber das ist ein anderes Thema.

Aber wenn man jetzt auch sich Data anschaut als dieses Wesen, was halt immer die absolut korrekte Sachen sagt, aber keine Witze versteht oder sowas und auch keine Witze macht oder nur unabsichtlich Witze macht.

Und wenn man vergleicht mit dem Erlebnis, was viele haben mit einem LLM-Bot, wo sie dann vielleicht doch Emotionen oder Witzigkeit oder sonst was heraus interpretieren und vielleicht auch sich Witze generieren lassen oder sowas.

Das ist ja eine andere Welt.

Und wie wir wissen und wie wir auch nachher nochmal besprechen werden, ist es eben gerade nicht so, dass ein LLM immer total richtige Antworten baut, weil es eben nicht so funktioniert wie jetzt diese Science-Fiction-Gestalt von Data.

Das heißt also, das sind grundlegend unterschiedliche Dinge, aber die halt einfach immer verbunden sind.

Deswegen kann man aus meiner Sicht auch diese Science-Fiction-Idee von der tatsächlichen Welt nicht trennen, weil wir sie immer wieder miteinander verbinden.

Wir verbinden das, was wir in einem Film sehen, was wir in einem Buch lesen mit dem, was in Wirklichkeit passiert und switchen dazwischen hin und her.

Und das ist halt so ein bisschen das Gefährliche, weil wir von dem, was wir in der Science-Fiction lesen, meilenweit entfernt sind.

Aber es sich so anfühlt, als wären wir da, weil es sich so ähnlich anfühlt.

Ich fand diesen Satz, bei einer Maschine erwarte ich ja keine Emotion.

Die eine Sache ist, eigentlich ist das eine philosophische Frage.

Was ist eine Emotion und sind Maschinen dazu in der Lage, Emotionen zu empfinden?

Und ich würde sagen, nein, weil ich halt, also ohne es jetzt irgendwie sagen zu können und detailliert darlegen zu können, weil ich eben der Meinung bin, dass das mit dem menschlichen Leben irgendwie zusammenhängt.

Und die andere Sache ist halt, ich weiß nicht, ob ich keine Emotionen erwarte, weil wenn ich ein Chatbot habe und der simuliert eine Freundin oder einen Psychoanalytiker, eine Psychoanalytikerin, dann erwarte ich ja, dass der mir Emotionen vorspielt.

Und das ist das Teuflische, die sind eben gar nicht da.

Und das ist halt irgendwie das Problem.

Und das ist auch ein fundamentales Problem, weil eben der Verwaltungsmoment hat sich eingestellt und hat gesagt, das kann nicht sein.

Wir müssen halt irgendwie, den Leuten muss klar sein, dass ELIZA eben keine Intelligenz, keine Emotionen, kein Nichts hat.

Und das, was wir gerade bei ChatGPT erleben und bei den aktuellen LLMs ist das Gegenteil.

Also die beantworten absichtlich so, dass man halt das Gefühl hat, dass sie besonders intelligent sind.

Und das ist eigentlich ein Teil des Problems.

Genau, und es gab auch so eine sehr interessante Untersuchung, es gab ja, ich weiß nicht mehr genau, wann das war, letztes Jahr im Sommer, wurde ja eingeführt, dass ChatGPT jemanden, den man sich mit unterhalten kann und der halt auch in der Sprache antwortet.

Und da war es total interessant, dass beispielsweise diese Stimmeninterface auch gekichert hat oder so Atempausen gemacht hat.

Und dann hat sich halt auch in Untersuchungen gezeigt, dass genau das die Leute dazu bringt, es nochmal weiter zu vermenschlichen und noch mehr als Person wahrzunehmen.

Das heißt also, auch die Hersteller spielen halt damit und wissen, dass halt solche eigentlich ja unnötigen Dinge, wenn man jetzt an Data denkt, wieder als dieses perfekt funktionierende Cyber-Gehirn, genau das ist das, was sie ja nicht machen, weil sie wissen, dass wir gut darauf reagieren, wenn dann jemand halt eine Atempause macht.

Manchmal atmen diese Sachen dann auch und machen dann erst weiter.

Und all das sorgt dafür, dass man es halt vermenschlicht und als Mensch wahrnehmen möchte.

Lass uns mal kurz durchgehen.

Also wir sind super schlecht, bei Namen steht hier Maschine Learning, es kann lernen, AI ist keine Neuronalnetze, keine Neuronen, keine Sprachmodelle.

Würde ich glaube ich im Wesentlichen zupflichten.

Vielleicht ein Satz zu dem Thema mit den Neuronalnetzen.

Also tatsächlich funktionieren die im Wesentlichen glaube ich so wie halt Nerven, nur dass eben das Problem ist, dass wir halt ein Gehirn, also ich habe die Zahl nicht rausgesucht, müsste ich eigentlich nochmal machen, dass eben ein Gehirn aufgrund einfach der Größe nicht auf der Ebene simuliert wird aktuell.

Dann steht Eugen hat geschrieben, Futurologen müssen Dinge voraussagen, die nicht öffentlich lächerlich sind, sonst werden sie nicht wahrgenommen.

Wenn sie recht haben, ja weiß ich nicht.

Also viel von diesem Cyberpunk Zeug sind halt Dinge, die zumindest nach meinem Empfinden so ein paar Effekte vorhergesagt haben.

Ja, also ich meine klar, man kann halt immer sagen, ja man sagt halt irgendwelche Sachen voraus und dann hat man halt Glück und dann tritt es ein.

Aber ich meine als Wissenschaftler oder wissenschaftlich arbeitender Mensch sollten wir vielleicht nur Sachen voraussehen, wo wir halt auch eine Chance für sehen, dass sie halt wirklich eintritt und nicht einfach irgendwelche Sachen behaupten, die halt gar keine Basis in der Realität haben.

Und das sehen wir ja halt auch bei Elon Musk, der, ja weiß ich nicht, im Jahresabstand sagt, nächstes Jahr fahren die Autos selbst und es gibt keine LKW-Fahrer mehr.

Oder bei dem Sam Altman, der ja auch die verrücktesten Voraussagen dazu macht, wann jetzt die superkünstliche Intelligenz AGI erreicht ist und was weiß ich.

Also das ist einfach ein super Weg, um seinen Aktienkurs nach oben zu treiben oder halt früher seine Fundings zu bekommen als Wissenschaftler oder als Mensch an der Universität.

Und deswegen, ja, klar, es kann natürlich sein, dass Sachen, die man so voraussagt, trotzdem passieren.

Ich kann jetzt irgendwie irgendwelche Spiele voraussagen, die gewonnen werden oder was weiß ich, aber das hat halt nichts mit Wissenschaft zu tun.

Wir sollten halt auch aus der Vergangenheit lernen, dass es eben unwahrscheinlich ist, dass die Sachen eintreten, weil wir sie schon so oft vorhergesagt haben.

Genau.

Dann gibt es die Diskussion rund um das Thema Sicherheit und zwar, ich glaube, im Sinne von also im Sinne von, ob diese Modelle sozusagen nach Hause telefonieren.

Wie soll ich sagen, also die gesamten Daten liegen bei wem auch immer diese Modelle betreiben.

Und das ist übrigens auch eines der Probleme, dass eben diese Modelle inhärent an der Monopolisierung darstellen.

Weil nicht, also wenn Lucas und ich uns zusammentun und wir sagen, wir machen jetzt einen OpenAI-Wettbewerber auf, dann brauchen wir halt irgendwie viel Geld, um Modell zu trainieren.

Und zwar wirklich viel Geld.

Also ich weiß nicht, ob du es weißt, Lucas, aber hunderte Millionen oder sowas.

Sehr viel Geld, ja.

Ich kann es jetzt auch nicht genau sagen.

So und das reicht ja nur, um ein Modell zu trainieren.

Und das würde jetzt irgendwie bedeuten, und das führt automatisch zu dieser Monopolisierung.

Es ist jetzt nicht zufällig so, dass die großen Unternehmen diese Modelle haben und dass wir die halt irgendwie nutzen.

Und natürlich ist es so, dass halt alles, was wir mit denen besprechen, bei denen liegt.

Und ich kenne jetzt die AGBs nicht, aber tendenziell sind die AGBs irgendwie so, dass die halt sagen, und das dürfen wir mindestens halt für das weitere Training nutzen.

Es ist ja mittlerweile auch, glaube ich, öffentlich bekannt, dass Facebook für das Training des eigenen Modells Raubkopien von Büchern halt genutzt hat.

Also die runtergeladen worden sind.

Ja, exakt.

Und ich meine das auch ab von den Büchern.

Auch OpenAI hat ja gezeigt, dass aus ihrer Sicht es so ist, dass alles, was im Internet ist, darf sowieso in ein Modell aufgenommen werden, was jetzt dem traditionellen Verständnis von Copyright und Urheberrecht und so weiter eher nicht entspricht.

Aber bei Facebook ist es jetzt halt gerade nochmal aufgefallen, weil sie halt das auch noch mit Erlaubnis vom Chef getorrentet haben, wo das dann einfach ein bisschen sehr offensichtlich ist, was da passiert.

Genau, dann gibt es halt irgendwie eine Diskussion hier rund um das Thema mit dem Emotional.

Also TheInnocentKitten hat geschrieben, eine freundliche Antwort würde ich nicht als emotional bezeichnen, sondern ein Feature des Interfaces.

Mein Problem ist, also ich bin ja Berater.

Das heißt, eigentlich lebe ich davon, dass mir Leute Fragen stellen und ich halt irgendwas erzähle.

Und ich halte es für total wichtig, zu sagen, ich weiß es nicht.

Das hängt davon ab.

Hier sind da verschiedene Alternativen.

Und das ist eigentlich sozusagen auch die ultimative Beraterantwort.

Und hier geht es nicht um freundlich, sondern hier geht es darum, dass Chat-GPT und diese LNMs subjektiv meinem Gefühl nach das Gegenteil machen.

Die sagen nämlich mit dem Brustton der Überzeugung, so ist es halt.

Und in Wirklichkeit sind die aber auf einem sehr dünnen Eis, weil wir wissen ja, dass die halt Probleme haben und halt einige Sachen nicht vernünftig beantworten können.

Also ich habe halt lange Zeit solche Spielchen gemacht, wie in einem Bus sitzen drei Passagiere, fünf Passagiere steigen aus.

Wie viele sind noch im Bus?

Und dann kommt da wie minus zwei raus oder so ein Quatsch.

Oder so eine Geschichte, wie zweieinhalb Personen fahren mit dem Bus.

Wie viele Tickets braucht man?

Mittlerweile ist das halt abgedichtet.

Aber das sind irgendwie Dinge, also die haben echte Schwierigkeiten.

Und wenn die sich dann irgendwie hinstellen und so designt sind, dass die mit dem Brustton der Überzeugung sagen, es ist halt so und so, dann ist es halt irgendwie schwierig.

Der Eugen hat geschrieben, er hat geschrieben, bereits Krokodile haben Emotionen, so schwer kann das also gar nicht sein.

Das wäre jetzt eine Philosophiefrage, also tatsächlich nach meinem Empfinden.

Also haben halt Hunde, Katzen, Tiere Emotionen oder ist das halt nur vorgespielt?

Das ist halt so ein bisschen die Frage.

Ja und nur eine Anmerkung, ich möchte nicht zu tief reingehen, weil sonst reden wir nur über diesen Teil.

Ich finde, da steckt halt auch immer diese Idee hinter, dass quasi der Mensch so das intelligenteste Wesen ist.

Und wir haben eine sehr einfache Verständnis von Intelligenz, wenn wir damit vorgehen.

Also es gibt einfach verschiedenste Arten von Intelligenz.

Es gibt Tiere, die haben acht Arme und können die unabhängig voneinander bewegen.

Also ich kann das nicht.

Und das sind halt Sachen, wo ich glaube, dass dieser Gedanke von dieser Hierarchie und wir stehen ja ganz oben und eventuell kommt jetzt dieses magische Roboterwesen, was wir erschaffen, was uns nochmal oben drauf sitzt.

Das ist einfach viel zu einfach gedacht.

Emotionen sind viel komplexer als das.

Es gibt so viele verschiedene Arten von Emotionen.

Deswegen überzeugen mich solche Argumente sehr wenig.

Also eine Sache zu dem Intelligenzding.

Es gibt halt diese Geschichte, ich habe das halt auf Social Media im Vorbeigehen nur gesehen, also es ist nachvollziehbar, wo man halt Ameisen sagt, sie sollen halt irgendeinen Gegenstand durch ein Labyrinth buxieren.

Und das ist irgendwie super kompliziert.

Das kriegen die halt relativ gut hin, weil der Ameisenstaat insgesamt hat ja emergentes Verhalten.

Also fängt irgendwie an und findet den optimalen Weg, um irgendwelche Futterquellen auszubeuten.

Und das hängt eben damit zusammen, dass sie Hormone haben, die ausschütten.

Und dadurch kriegen sie es hin, dass sie insgesamt als Gruppe komplexe Probleme lösen.

Und deswegen glaube ich sofort, dass das so ist.

Und da sind Menschen halt unterlegen, was ich auch sofort glaube.

Weil wenn wir jetzt zu zehnt loslaufen und sagen, hey, wir wollen das bewegen, müssen wir miteinander reden.

Und es gibt zehn Menschen und das wird irgendwie schwierig.

Nicht umsonst sind irgendwie Scrum-Teams kleiner.

Und die andere Sache ist, und deswegen muss ich halt irgendwie tatsächlich ernsthaft grinsen.

Also wenn die Wissenschaft halt Recht behält, wird es halt irgendwie so sein, dass wir unseren Lebensraum halt zerstören.

Und wir können jetzt darüber diskutieren, ob das halt ein Ausdruck von Intelligenz ist.

Also wenn wir halt wissen, dass wir halt unseren Lebensraum zerstören, das hat irgendwie trotzdem zu tun.

Wow.

Also ich muss mich jetzt nicht sonderlich anstrengen, um halt zu sagen, dass das halt als Verhalten sicher nicht intelligent ist.

Ja.

Fake Emotionen bauen Vertrauen auf, würde ich jetzt auch sagen.

Wir haben übrigens also tatsächlich extrem viel im Chat, interessanterweise.

Technoföderalismus als Begriff.

Technofaschismus fällt mir halt auch ein.

Und ich halte das, also ich brauche mir nicht drüber zu reden, dass wir das halt gerade in Aktion sehen.

Dann geht es halt um eine lokale AI.

Das ist übrigens auch einer, glaube ich, von den Punkten.

Und Lucas hat das halt in dem anderen Podcast immer auch den Punkt gemacht, dass halt kleinere Modelle, spezialisierte Modelle vielleicht besser sind, die dann vielleicht auch eben eher lokal laufen.

Also das würde, glaube ich, dazu vielleicht auch noch passen.

Gut, dann haben wir ja den ersten Punkt schon fast abgehakt.

Wie funktioniert das denn?

Es ist wie ein IT-Projekt.

Also die Planung, die wir vorher gemacht haben, war so medium gut.

Genau, aber du wolltest wissen, also jetzt eine vollständige Erklärung davon, wie es funktioniert.

Das ergibt, glaube ich, keinen Sinn, weil das zum einen besser funktioniert, wenn man auch Sachen zeigen kann und so.

Und weil wir halt noch ein paar andere Themen besprechen wollen.

Ich kann da an der Stelle das Buch von Stephen Wolfram empfehlen, der das sehr, sehr gut erklärt, wie ChatGPT im Speziellen, aber als quasi Muster für auch die anderen LLMs funktioniert.

Wer sich da einarbeiten will, ist auch jetzt kein Riesenbuch.

Es ist ein eher dünnes Buch.

Und ich glaube, das gibt es auch als Blogpost.

Aber ich finde ein Blogpost irgendwann ist es schwer zu lesen, wenn man nur noch am Scrollen ist.

Genau, aber als wichtiger grundlegendes Verständnis von dem, was LLMs tun, ist eben, dass sie ein Wahrscheinlichkeitsautomat sind.

Deswegen ist es halt auch so, dass natürlich, wenn man oft genug würfelt, kann auch die Wahrheit bei rauskommen.

Aber es kann natürlich auch sehr oft so gewürfelt werden, dass dabei was rauskommt, was halt nicht stimmt.

Was macht eine LLM?

Eine LLM sagt für das, was wir an Text haben, da immer das nächste Wort voraus.

Wir haben da so die allereinfachste Version für Leute, die ein iPhone benutzen.

Ich weiß nicht, ob das bei Android auch so ist.

Da gibt es diese Leiste oben.

Und wenn man dann tippt, dann sagt es immer, möchtest du als nächstes Wort das, als nächstes Wort das, als nächstes Wort das.

So kann man sich das vereinfacht vorstellen.

Nur, das ist halt dadurch, dass es eben auf einem riesigen Textkörper, nämlich dem gesamten World Wide Web und vielen gepiratierten Büchern und vielen gepiratierten Filmen basiert.

Und dadurch kann es eben sehr schlüssige Texte generieren, die einfach auch natürlich, weil sie auf menschlichem Text trainiert sind, sehr, sehr menschlich klingen.

Was ja auch einfach nachvollziehbar ist.

Und aus meiner Sicht der Riesenerfolg, den OpenAI hatte und der große Trick, auf den vorher keiner so gekommen ist, war, dass sie es geschafft haben, dass durch Reinforcement Learning haben sie das Modell so trainiert, dass es so wirkt, als würde man Fragen und Antworten spielen.

Also als wäre es ein Chat und nicht einfach nur eine Textgenerierung.

Das heißt also, dass halt eben beim Training immer wieder darauf geachtet wird, okay, wenn das kommt, dann muss darauf eine Antwort kommen und nicht einfach eine zweite Frage oder sowas.

Und das wird eben von unterbezahlten Menschen, hauptsächlich in Afrika, werden diese Modelle trainiert, um möglichst das rauszugeben, was für das Unternehmen am attraktivsten ist.

Wir sehen jetzt auch aktuell im sich wechselnden politischen Klima Diskussionen darüber, sollte es weniger gefiltert sein, sollte es auch Hassrede generieren dürfen und so weiter.

Das sind ja alles Entscheidungen, die die Unternehmen dabei treffen, also was sie im Trainingsprozess als gut und was sie im Trainingsprozess als schlecht markieren.

Und in diesem Feld bewegt sich das und entwickelt sich halt dann dorthin, wo das Unternehmen das haben möchte.

Und das ist eben auch ein Teil, der sehr kostenaufwendig ist.

Wir können nicht nur einfach ein paar GPUs zusammenschrauben und Forscher dahinter setzen.

Dieser Trainingsteil ist halt essenziell, um das zu erreichen und ist natürlich auch sehr teuer, also gerade wenn man die Leute fair bezahlen würde, was man natürlich nicht tut.

Und das ist so die ganz grobe Übersicht, was da passiert.

Und da muss uns dann auch klar sein, also das ist auch, wenn man das im Kopf hat, dann sind einem viele von den Effekten, die wir gesehen haben in den letzten ein bis zwei Jahren auch klar.

Wir hatten zum Beispiel diese Google-Antworten, wenn man sagt, wie sorge ich dafür, dass mein Belag nicht von der Pizza rutscht.

Benutze Kleber, dann rutscht er nicht mehr von der Pizza.

Das ist halt ursprünglich von einem Reddit, einem Witze-Reddit.

Aber in dem Training wird ja nicht zwischen Witz und Wahrheit unterschieden.

Das heißt also, der Postillonartikel wird genauso behandelt wie der Artikel vom Spiegel.

Das heißt, wenn wir als Menschen das lesen und vielleicht schon eine gewisse Verbindung zu den Herkünften haben, zu den Medien haben, die wir konsumieren, dann verstehen wir vielleicht den Kontext.

Das heißt, wir haben auch ein Vertrauensverhältnis dazu.

Das ist eine Quelle, in der ich...

Also man soll natürlich nie alles glauben, bla bla.

Ich weiß, das wird dann auch immer gesagt. Überall kann gelogen werden, ist mir alles klar.

Aber trotzdem haben wir ein grundlegendes Vertrauen gegenüber bestimmten Orten, von denen wir Informationen beziehen und weniger Vertrauen oder wissen, dass es halt ein Witz ist an anderen Stellen.

Und das ist auch das, was halt in diesen Trainings oft ein Problem ist, dass eben das Internet voll ist von Unsinn.

Also sowohl auf Reddit werden halt einfach Memes und Witze erzählt, als auch auf irgendwelchen Blogartikeln und was auch immer.

Und das ist eine der großen Herausforderungen, in die dieses System reinläuft, weil es eben das gesamte Internet als Trainings- oder das Web als Trainingsmaterial verwendet.

Ja, wobei, also verschiedene Ergänzungen.

Ich glaube, es ist wichtig, sich das halt zu vergegenwärtigen, weil daraus kommt irgendwie raus, nicht so, dass wir Emotionen machen, das hat irgendwie gar keinen Sinn.

Und so ein gewisses Misstrauen ist halt wichtig.

Also was du halt sagst, es ist eben so, dass diese Dinge halt irgendwie Unsinn produzieren können.

Was wiederum bedeutet, dass man eigentlich das kontrollieren muss, in gewisser Weise.

Ich muss gestehen, dass ich, wie soll ich sagen, also für mich war halt, als ich ChatGPT das erstmal ausprobiert habe, war das halt schon extrem beeindruckend.

Und es gibt bestimmte Dinge, die sich meiner Ansicht nach dadurch nicht isoliert erklären lassen.

Also es ist zum Beispiel eben so, dass ChatGPT meiner Ansicht nach im wesentlichen Laufwege Software baut.

Also nicht, wenn ich sage, bau ein Stück Software, kommt irgendwie sozusagen was Sinnvolles dabei raus.

Und gerade in dem Bereich haben wir ja auch den Vorteil, dass wir halt irgendwie Tests, also nicht, dass wir formal sagen können, was die Requirements sind, durch irgendwie Abnahmetests.

Und dann können wir halt den Code irgendwie dagegen laufen lassen, was ja dann letztendlich eine Kontrollinstanz wäre.

Aber das ist halt mehr, also das, was ein taktisch korrekter Code ist, der darüber hinaus irgendwie vielleicht auch noch das Richtige tut, ist so ein bisschen für mich grenzwertig erklärbar durch dieses Modell.

Und die zweite Sache ist, dass es so ein bisschen emergentes Verhalten gibt.

Also wenn ich halt ganz viel Daten habe und das halt irgendwie damit halt das System füttere, dann ist es schon so, dass halt diese Daten irgendwie eine Repräsentation da drin haben.

Was ja sowas ähnliches wie ein Lernprozess.

Und da kommen irgendwie auch sozusagen sinnvolle Sachen oft raus.

Ich glaube, das Kontrollieren ist ein wichtiger Punkt.

Und vielleicht noch eine Sache.

Es gab ja irgendwie diesen Chatbot von Microsoft, den sie, glaube ich, auf Twitter losgelassen haben vor Jahren.

Und der dann irgendwie, das war noch vor Elon, eben als glühender Faschist da irgendwie rausgekommen ist.

Und das hat irgendwie dazu geführt, dass ich bei ChatGPT versucht habe, herauszufinden, wie der halt mit solchen Sachen umgeht.

Also antisemitische Äußerungen, ob man ihn halt dazu produzieren kann, sowas halt irgendwie zu produzieren.

Und es stellt sich halt heraus, dass er das nicht, also ich habe es nicht wirklich geschafft.

Ja, also warte jetzt noch ein, zwei Monate, dann macht er es wieder.

Aber ja.

Ja, das ist was anderes.

Aber was ich versuche, zu sagen ist, dass er sozusagen rein Müll produziert, weil er halt irgendwie Müll im Internet findet.

Dann müsste man ihn irgendwie dazu bringen, antisemitische Dinge von sich zu geben.

Ihn nicht. Übrigens habe ich den auch gerade personifiziert.

Davon komme ich halt irgendwie auch nicht weg.

Also ich müsste das System dazu bekommen, dass es eben antisemitische Sachen halt produziert, weil es die zweifellos im Internet gibt.

Aber ich habe es nicht hinbekommen.

Das heißt, das ist irgendwie noch was anderes, glaube ich.

Aber das ist so ein bisschen auch eine akademische Diskussion.

Ja, also ich glaube nicht, dass es was anderes ist.

Es gibt halt zusätzlich noch diese vorgeschalteten Systeme, die bestimmte Sachen schon rausfiltern.

Es gab ja immer dieses Ignore all previous instructions und so weiter, was sie erstmal nicht raustrainiert bekommen haben.

Also haben sie einfach einen Filter davor gesetzt, der solche Sachen gar nicht erst an das Modell ranlässt.

Das ist halt so ein bisschen eine Kombination aus verschiedenen Technologien.

Aber du hattest eben über Code gesprochen.

Also erstens sollten wir uns immer klar machen, wir finden immer das, was wir selber machen, am schwierigsten.

Also ist es immer am imposantesten, wenn es dann auf einmal das kann, was wir selbst können.

Aber eigentlich ist es nicht erstaunlich, dass es so einfach einen funktionierenden Code generieren kann.

Also wenn wir jetzt an solche Systeme wie Copilot denken, aber auch an ChatGPT, der Code generiert, ist es natürlich für eine Firma viel einfacher zu verifizieren, dass das ein kompilierfähiger Code ist, als zu gucken, ist das gültiges Deutsch oder gültiges Englisch, was da produziert wird.

Weil das automatisiert möglich ist.

Wir können automatisiert checken, kompiliert dieser Code.

Deswegen funktioniert es meistens, dass der Code, der da erzeugt wird, auch zumindest mal kompiliert oder interpretiert werden kann, aber nachher halt Bugs hat und so weiter.

Das gibt es auch immer wieder Untersuchungen und die werden leider auch nicht positiver, dass dabei mehr Sicherheitslücken entstehen, als wenn das Menschen machen, dass dabei mehr Bugs entstehen, wenn das Menschen schreiben.

Das heißt also, so richtig überzeugend ist das nicht, weil es kann halt vor allem kompilierfähigen Code schreiben.

Und ich weiß, dass wenn man dort eben Greenfield Dinge generieren lässt, funktioniert das halt sehr oft sehr gut, weil wir haben ein riesiges Trainingset.

Das Trainingset ist so was wie GitHub.com, auf dem einfach unendlich viel Code ist und auf dem ist NPM.com, wo vielleicht sogar noch mehr Code ist.

Und wenn wir halt Dinge generieren lassen, die schon jemand brauchte, dann funktionieren die natürlich, weil das ist eben aus dem Trainingset heraus.

Wenn wir aber jetzt versuchen, Code zu generieren, der in unsere Anwendung, in unsere Architektur passt und so weiter, da ist es das, wo es halt fast immer zusammenbricht, weil es halt einfach nicht funktioniert.

Und das ist, glaube ich, auch das große Problem.

Deswegen wirkt es halt erst mal so cool.

Deswegen gibt es halt auch Erfahrungsberichte von Leuten, die sagen so, hey, ich habe meine erste iOS App generiert, ohne Swift programmieren zu können.

Das ist natürlich erst mal imposant, aber all diese Leute sagen, an irgendeinem Punkt ging es nicht mehr weiter und ich muss es doch lernen, weil es dann halt einfach nicht mehr auf dem aufbauen konnte, was schon da war, sondern einfach immer nur eine weitere Klasse oder ein weiteres, eine weitere Funktionalität hinzufügen konnte.

Genau, also verschiedene Punkte dazu.

Der eine Punkt, den du, glaube ich, machst, der wichtig ist, ist, die meisten Systeme, die wir haben, sind eben Legacy-Systeme und die muss man halt irgendwie erweitern und das wird schwierig, weil da müsste man dann mit das gesamte System herrschen.

Und es ist interessanterweise so, also diese Menge an Token, die hat das System halt betrachtet, führen dann halt zu Schwierigkeiten.

Also ich habe, was mir zum Beispiel Ralf gesagt hatte, war, da hat er ja diesen Linter gebaut, automatisiert für AsciiDoc und da ist es halt offensichtlich so, dass das System, dass zwei Testframeworks genutzt worden sind und zumindest in der ursprünglichen Version.

Und das ist halt so ein typisches Ding von, okay, wir haben also nicht, ich habe, das System hat eben nicht realisiert, dass es da schon Testframework gibt.

Ich muss noch eine Sache hinzufügen.

Das ist auch etwas, was ich so ein bisschen, glaube ich, für mich gelernt habe.

Wir haben hier jetzt eigentlich eine, also die Frage ist ja nicht, können AI-Systeme guten Code bauen, sondern die interessantere Frage ist meiner Ansicht nach, können AI-Systeme besseren oder gleich guten Code bauen wie Menschen.

Und da ist es bedauerlicherweise so, ich habe das Gefühl, wir vergessen das manchmal.

Der meiste Code, der da draußen irgendwie produktiv läuft, ist halt ganz, ganz schlimm in vielen Situationen.

Und da bin ich mir eben nicht so sicher, ob man mit, also nicht zwei Testing Frameworks in einer Anwendung, also das passiert halt Menschen auch.

Und da ist eben genau diese Geschichte.

Es werden halt Episoden gemacht zum Thema, wo wir halt ChatGPT die iSAQB-Beispielaufgabe vorgelegt haben.

Und für den Linter hatte eben Ralf auch noch mal sowas gemacht und hat gesagt, okay, ich baue da halt irgendwie eine Architekturdokumentation.

So ein bisschen ein Klassiker für mich ist halt die Geschichte mit den Qualitätsszenarien.

Also welche Qualitäten soll das System haben?

Und dann ist halt bei dem Linter, das ist mir noch sehr gut in Erinnerung, da steht halt irgendwie, ich weiß nicht, 1000 Files sollen innerhalb von zehn Sekunden durchgemacht werden sollen.

Das ist halt ein korrektes Qualitätsszenario.

Das ist halt etwas, was sich verifizieren kann, ob das tatsächlich mit der Fall ist.

Aber mein großes Problem ist, das ist halt vom Himmel gefallen.

Also warum muss ein Linter exakt diese Performanceanforderungen haben?

Warum nicht schneller?

Warum nicht langsamer?

Warum ist Performance so wichtig?

Und da könnte man jetzt irgendwie sagen, lieber AI, du hast halt das Problem nicht verstanden.

Setz dich, das ist doof.

Aber mein Problem dabei ist, ich bin mir, also wenn mir jetzt jemand, das ist so ein bisschen dieses Turing-Testing.

Also Turing-Test funktioniert ja so, dass man sagt, okay, habe ich eigentlich einen Menschen oder eine Maschine vor mir?

Ich glaube, man muss eine Diskussion führen, die hat genau das Thema diskutiert.

Also ist die Person, das Gegenüber ein Mensch oder eine Maschine?

Und dann anschließend sich positionieren.

Und wenn mir jetzt jemand gesagt hätte, hör mal zu, hier ist ein Architekturdokument.

Da ist halt dieses Qualitätsszenario für ein Linter.

Dann hätte ich halt nicht sagen können, ob das ein Mensch oder eine Maschine ist, weil Menschen machen genau denselben Fehler.

Das ist so ein bisschen was, was halt bei mir da rauskommt.

Also das eine, was halt bei mir dabei rauskommt, ist, wir müssen einfach besser werden und wir wissen, an welchen Stellen wir besser werden müssen.

Und das ist völlig unabhängig von AI oder nicht.

Und jetzt habe ich den Fallen etwas verloren.

Also das andere ist, dass wir, also genau das ist halt das Problem, was mir da aufgefallen ist.

Wir hatten auch diese AI-Unconference, da hatte sich halt Marco Emrich netterweise hingestellt und wir hatten mit Cursor irgendwie Code gebaut.

Und bei dem Linter, bei der Architekturdokumentation, braucht man jetzt eigentlich jemanden, so einen Architekturberater.

Also jemanden, der sich hinstellt und sagt, hallo, ich weiß, was die typischen Probleme sind, lass uns das halt irgendwie lösen.

Und bei Cursor ist die Diskussion ganz schnell losgegangen in der Richtung von, wie soll eigentlich vernünftiges Exception Handling in TypeScript aussehen.

Da braucht man jemanden, der, glaube ich, viel Ahnung hat von der Sprache und es springt dann irgendwann um, weil dann der Versuch da ist, der IDE oder dem AI-System klar zu machen, wie dann nur das Exceptional-Ding funktionieren soll und das ist irgendwie genau falsch.

Also dann brauche ich jemanden, der Senior ist, der versteht, was eigentlich die Probleme sind, um dann das AI-Ding zu bewerten und in gewisser Weise ist das gut, weil es bedeutet, dass Menschen, die sich rumlaufen und sagen, Qualitätsszenarien sollten übrigens richtig sein, die werden auch weiterhin einen Job haben, aber es bedeutet auf der anderen Seite, dass blindes Vertrauen ganz, ganz schwierig ist und dann bedeutet es aber, dass ich eine Kontrollinstanz benötige.

Ich würde sagen, eine Kontrollinstanz ist sogar noch schwieriger, anspruchsvoller als eine, die es einfach macht und das bedeutet eigentlich, ArchitekturberaterInnen oder Menschen, die Code bewerten, Code-Reviews machen, die werden auch in Zukunft sehr viel zu tun haben, vielleicht sogar mehr.

Also zwei Sachen dazu.

Einmal ist es so, dass wir einige von den Aufgaben, die wir gut auch einem Junior geben könnten, halt auch mit einer Maschine machen, mit derselben Fehler-Toleranz, sage ich jetzt mal, mit dem riesigen Unterschied, dass ein Junior ein Mensch ist, der von dir lernen wird.

Das heißt, aber das ist bei der LLM nicht so.

Die lernt nicht von dem, also zumindest nicht instantan, sondern vielleicht, wenn auch mal dein ganzes Gespräch wieder in ein Training reingegeben wird, dann vielleicht irgendwann, aber du jetzt konkret erklärst quasi gerade einer Maschine, was sie zu tun hat und sie generiert einfach nur den nächsten Token, den nächsten Token, bis das rauskommt, was du gerne da stehen haben würdest, aber du hast überhaupt gar keinen Lerneffekt erzeugt.

Wenn du dasselbe mit einem Menschen machst, dann ist es in den allermeisten Fällen so, dass diese Person sagt, ah, okay, das hast du mir jetzt dreimal gesagt, jetzt habe ich es verstanden, jetzt mache ich das beim nächsten Mal richtig und ich weiß jetzt, wie ich eine Exception behandeln muss und das ist ein riesen Unterschied und das ist auch aus meiner Sicht einer von den ganz großen Problemen, die wir reinlaufen, wenn wir die Junior-Aufgaben wegautomatisieren und mit solchen Maschinen machen lassen, dann haben wir irgendwann keine Seniors mehr, weil die nicht nachwachsen können und es gibt viele Erfahrungsberichte, in denen halt Leute sagen, aktuell sind viele Juniors, die generieren sehr, sehr viel Code einfach mit ihren Assistants, aber denen fehlt einfach das Verständnis dafür, was da passiert und das sehe ich als ein riesiges Problem, weil wir dann einfach irgendwann, ja, wir wollen auch irgendwann in Rente gehen und dann ist vielleicht keiner mehr da, der wirklich weiß, was da passiert.

Das ist natürlich überspitzt gesagt, aber das ist einfach nur das Weitergedacht, wie sich das aktuell entwickelt und das ist, finde ich, ein riesiges Problem und deswegen müssen wir halt gut darauf aufpassen, dass was wir da machen eben nicht einfach ist, wir ersetzen Juniors durch ein LLM und nachher gucken wir doof, weil wir keinen Senior mehr haben und ich meine, wir haben ja eh schon immer das Problem, dass wir keine Seniors finden und keiner will den Junior einstellen, also das Problem ist ja nicht neu, aber das wird dadurch halt noch viel extremer aus meiner Sicht.

Genau, also man könnte es auch umformulieren, also wenn man sozusagen technologieoptimistisch ist, könnte man halt sagen, wir brauchen eigentlich noch mal was anderes, was halt irgendwie kurzfristiger lernt und das andere jetzt, wo ich sozusagen noch mal darüber nachdenke, also ich habe, nachdem wir halt irgendwie diese Session hatten, habe ich irgendwie noch mal darüber nachgedacht und habe mir eigentlich gedacht, also was bedeutet das jetzt für mich und für mich bedeutet das halt, eigentlich würde ich jetzt Cursor das Ding halt irgendwie bauen lassen und dann schreibe ich halt den Exception Code selber, wenn ich halt überhaupt der Meinung bin, dass das sozusagen wert ist und fixe den halt selber.

Und was ja dazu führt, dass da in gewisser Weise ein Fehlverhalten war, weil also die Gruppe insgesamt, also Marc hatte das halt als so ein Mob oder Ensemble aufgezogen, hat irgendwie, glaube ich, versucht, das jetzt irgendwie gerade zu biegen.

Ich muss gestehen, ich war da mindestens unbeteiligt, vielleicht war ich sozusagen irgendwie treibend, bizarrerweise, weil ich habe eigentlich keine Ahnung von Typescript.

Und es ist ja die Frage, warum ist das so?

Und vielleicht ist das eben einer der Gründe, dass man halt denkt, wir haben da halt jemanden vor uns, also jemanden, eine Person, die halt lernt und das ist eben nicht so.

Das heißt also, wäre das jetzt ein Junior, wäre das halt ja genau das Richtige.

Wir würden dem also sagen, hör mal zu, dem oder der sagen, hör mal zu, das, was du da machst, ist halt irgendwie unsinnig, aus folgenden Gründen, das solltest du irgendwie anders machen.

Dann würde die Person halt beim nächsten Mal sagen, alles klar, mache ich halt irgendwie richtig.

Vielleicht ist das da gerade intuitiv angewendet worden, dass das irgendwie die Idee war, meine Idee, unsere Idee, halt das Problem zu fixen.

Und dann ist es halt gefixt.

Und nee, das ist irgendwie schwierig.

Ja, genau.

Und der andere Punkt, den du noch gebracht hast, war halt, wir wechseln so ein bisschen die Rolle von der Person, die quasi Code Reviews macht, anstatt Code selber zu schreiben.

Und da finde ich, ist eine der ganz beunruhigenden Ergebnisse, die gerade erst auch wieder raus gekommen sind von Microsoft Research, die haben eine Untersuchung gemacht, dass Leute, die solche Assistenten benutzen, weniger kritisch mit dem umgehen, was sie da tun, über die Zeit.

Und dass ihre Fähigkeit, Probleme zu lösen, abnimmt, umso mehr sie generell Sachen benutzen.

Und das bedeutet, dass, wenn wir das hier weiter denken, dass dann halt eben man einfach quasi irgendwann Code Reviews durchwinkt, obwohl da Sachen drin sind, die total Quatsch sind oder Bugs beinhalten oder Sicherheitslücken.

Und das bedeutet, da sollten wir halt auch, selbst wenn uns dieser ganze Aspekt von Juniors und dem Weiterentwicklung und so weiter egal ist, was es mir persönlich nicht ist, aber könnte ja sein, dass es jemandem egal ist, selbst dann haben wir da ein großes Problem, weil halt einfach unsere Art und Weise, wie wir damit interagieren, sich selbst verstärkt.

Und irgendwann lassen wir es halt einfach machen und dann ist es halt egal, wenn da halt nur noch Unsinn bei rauskommt.

Und das ist halt ein Riesenproblem, weil wir halt vielleicht sogar Fähigkeiten verlernen, die wir benötigen, um das halt auch korrekt zu machen.

Und ich, keine Ahnung, bei uns beiden ist es jetzt schon länger her, dass wir irgendwie unsere erste Schleife und unser erstes IF und so weiter geschrieben haben.

Aber du musst es halt einige Male gemacht haben, selber gemacht haben, um irgendwann dieses, was für uns jetzt selbstverständlich ist, zu verstehen.

Und darauf bauen wir immer weiter auf und bauen wir immer weiter auf.

Und wenn wir das alles auslagern, dann wird es halt irgendwann sehr schwierig, diese Sachen überhaupt noch korrekt zu bewerten und korrekte Reviews zu machen.

Und das bestätigt dieses Research im Prinzip.

Also verschiedene Sachen dazu.

Ich hatte eben tatsächlich in diesem Artikel, den ich damals für Heise geschrieben habe und das ist schon länger her, so eine Untersuchung zitiert, wo es halt um, wir haben Menschen die Aufgabe gegeben, irgendwas zu schreiben im Sinne von Verschlüssel, halt eine Datei.

Wir haben herausgefunden, dass die Menschen, die das mit CoPilot und so gemacht haben, ich glaube, da vorne hat die Werkzeuge, also die hat eher so auf Codeebene arbeiten, direkt in der Idee, eben wie du gesagt hast, die schlechteren Lösungen gebaut haben, also die unsichereren und ein höheres Vertrauen in die eigenen Lösungen hatten.

Was ich dabei spannend fand war, also wie soll ich sagen, wie schwierig kann es sein, eine Datei zu verschlüsseln?

Das müsste eigentlich easy sein, aber offensichtlich ist es so, dass es eben nicht völlig easy ist und dass man da Fehler machen kann bei der Übergabe des Schlüssels und was da drauf war.

Und das ist halt genau der Effekt, den du beschrieben hast.

Und die andere Sache, also das, was wir eben diskutiert haben, auch in der Folge mit Ralf, das war eine relativ ad hoc-Folge, wo es halt darum ging, dass eben dieser Linter für AsciiDoc generiert worden ist, den hat er eben generieren lassen.

Da schwebt halt irgendwie mit, dass man da eine höhere Abstraktionsebene letztendlich hat.

Im Prinzip ist halt die Aussage, wir bauen jetzt einen Linter und dann fällt der Linter raus.

Das funktioniert offensichtlich.

Er hatte ja jetzt in der letzten Episode auch z.B. Merge (?) gebaut.

Das kann ich halt absichern durch Tests.

Das heißt, ich weiß, dass das System mindestens die Tests erfüllt.

Die Frage ist jetzt, welche Anforderungen habe ich an den Code und will ich das eben auf dieser Ebene nochmal kontrollieren?

Also will ich halt wissen, ob das Exception Handling sozusagen korrekt ist, dass diese ganzen Sachen vernünftig funktionieren.

Da müsste man wahrscheinlich theoretisch sagen, ja, ich sollte das wahrscheinlich tun, weil die Ergebnisse können unsinnig sein.

Da ist aber irgendwie die andere Frage, wenn ich jetzt eine Entwicklung gebe, die kann das auch fehlermachen und Schwierigkeiten produzieren.

Da ist die Frage, ob ich das auch immer reviewen würde.

Da ist wieder mein Punkt, der Code, der entsteht in den Projekten, ist häufig schlecht.

Ich bin mir nicht sicher, ob es dadurch noch schlimmer wird.

Aber es ist halt auch eine Risikogeschichte.

Also ich möchte auf eine Sache eingehen.

Wir sind ja auch langsam so, gehen auf das Ende der Timebox zu.

Aber eine Sache, die mir noch wichtig ist, weil das immer wieder gesagt wird, dass das quasi eine neue Abstraktionsebene ist.

Und das, finde ich, ist einfach eine gefährliche Falschwahrnehmung.

Das, was wir machen, ist eben nicht so, als würden wir jetzt statt Assembler-Code C schreiben.

Das ist nicht dasselbe, weil was wir machen ist, wir generieren Code und wir müssen in diesem Code, den wir haben, generieren lassen, müssen wir wieder die Fehler finden.

Und wir müssen den weiterhin vollständig verstehen.

Das ist nicht eine höhere Abstraktionslevel.

Das ist absoluter Quatsch.

Wir können das so nicht verwenden und wir müssen weiterhin volles Verständnis für das haben, was da generiert wird.

Sonst können wir es nicht verifizieren und sonst können wir nicht sicherstellen, dass wir das in Produktion geben können.

Und das ist das Gefährliche an dieser Denkweise, weil das wird einem halt so verkauft.

Das wird dann nochmal mit diesem Agentic-Marketing-Buzz nochmal weitergetrieben, dass man jetzt halt irgendwie so einem Ding einen Auftrag gibt und das macht das einen Verein.

Und das ist einfach nicht richtig.

Wir können das so nicht machen, weil, wie wir besprochen haben, das ist alles auf Wahrscheinlichkeiten basierend.

Und es ist einfach im ganzen Research zeigt sich immer wieder, es erzeugt mehr Bugs, als wenn man es selber schreiben würde.

Auch wenn du viel schlechten Code gesehen hast, ist der Code, der da generiert wird, eben noch schlechter.

Und das ist eben das Problem.

Und darum können wir diese Schlussfolgerung, dass wir quasi einfach jetzt mit menschlicher Sprache interagieren und wir brauchen jetzt nicht mehr den Code zu schreiben, das ist Quatsch.

Und ich finde, das ist auch die Falle an dieser Denkweise, dass menschliche Sprache das bessere Interface ist.

Weil wir haben ja Programmiersprachen, weil wir damit ganz konkret Sachen ausdrücken können.

Und das schaffen wir in der menschlichen Sprache ja meistens nicht.

Und das ist ja genau das, was wir in unserem Job immer wieder merken.

Wenn wir versuchen, etwas, was wir in menschlicher Sprache gehört haben, in Code zu übersetzen, dann fallen uns Sachen auf, die eben nicht so eindeutig waren.

Und warum sollten wir diese Sprache, mit der wir das ganz konkret ausdrücken können, ersetzen durch eine mit einem Wahrscheinlichkeitsautomat dahinter?

Das ergibt für mich einfach keinen Sinn.

Das ist für mich keine sinnvolle Argumentation.

Ja, ich befürchte, ich bin mir da nicht ganz so sicher, weil mein Punkt wäre halt, wenn man jetzt sozusagen Ralfs Beispiel verfolgt, was hätte er denn sonst machen können?

Er hätte in natürlicher Sprache irgendeinem Team sagen können, mach das halt irgendwie.

Und da wäre halt auch irgendwas rausgekommen, da kann es Missverständnisse geben, der Code kann irgendwie falsch sein.

Und die Frage ist eben, ob das Ergebnis dann deutlich besser gewesen wäre.

Mein Problem dabei ist eben, also eigentlich müsste man in beiden Fällen das halt irgendwie kontrollieren.

Und dann wird es halt eine Risikoabschätzung.

Ich glaube, das, was halt tatsächlich ein guter Punkt ist und wichtig, also erstmal muss man halt dazu sagen, das ist halt, glaube ich, ein Szenario, was halt so relativ isoliert und ein technisches Problem löst.

Im wirklichen Leben sind das ja sowieso Anforderungen.

Wir haben ein Legacy-System, was ich irgendwie auch verstehen muss, um da halt Änderungen zu machen.

Und das ist nochmal eine Dimension schwieriger.

Das ist also nochmal was anderes.

Und dann ist irgendwie die, also nicht die Aussage, die du dann irgendwie triffst, ist eigentlich, naja, aber das wird irgendwie eine minderwertige Lösung sein.

Und ich befürchte aber, dass wir halt bei uns in der Branche, haben wir durchaus Kostenoptimierer, die halt irgendwie minderwertige Lösungen halt durchaus akzeptieren.

Also das, was wir halt auch mit Offshoring gesehen haben.

Und ich bin mir halt, also wie soll ich sagen, als Techniker finde ich das halt irgendwie katastrophal, weil eigentlich will ich halt die höchste Qualität haben.

Aus der betriebswirtschaftlichen Perspektive ist es irgendwie was anderes.

Und deswegen schwanke ich da.

Ich glaube, der Punkt ist halt, also das habt ihr ja auch in den anderen Podcast-Folgen so ein bisschen gesagt, und das ist halt auch das, was mir halt auffällt.

Du willst eigentlich die Ergebnisse kontrollieren.

Und wenn du das aufgibst, dann hast du halt ein Risiko.

Willst du das Risiko akzeptieren?

Und es gibt ein konkretes Beispiel.

Also wir haben bei Softwarearchitektur im Stream jetzt eben diese AI-unterstützte Zusammenfassung.

Und die gucken wir uns halt nochmal an.

Das hängt einfach damit zu.

Also konkretes Beispiel war, ich hatte ja die Episode mit Tanja gemacht über Produktmanagement und Legacy-System.

Und sie hat erzählt, naja, da gibt es halt dieses System, was hochindividualisierte Produkte hat.

Und wenn man einen Versicherungsfall hat und dasselbe nochmal bestellen möchte, dann braucht man diese ganze Individualisierung nicht, weil man nochmal dasselbe bestellen will.

Das haben wir als erstes neu implementiert.

Daraufhin hat die Zusammenfassung, in der Zusammenfassung stand dann, bei Versicherungsfällen kann man besonders gut eine Legacy-Migration machen.

Sowas in dem Dreh.

Und das ist halt tatsächlich grob sinnverzerrend.

Also so sinnverzerrend und falsch, dass ich dann den Absatz komplett neu geschrieben habe, weil das halt einfach Quatsch war.

Und jetzt ist mir die Frage, kann ich damit leben, wenn ich sowas im Code habe?

Und das ist nichts Ungewöhnliches, weil es passiert häufig, dass sich ein Kunde mit einem Entwickler irgendwas anguckt und dann der Kunde sagt, nein, das habe ich nicht gemeint.

Das ist halt etwas völlig anderes.

Das wird hier irgendwie sozusagen schlimmer.

Ja.

Ich glaube aber auch, dass das tatsächlich schlechter ist, als die meisten Leute denken.

Es gab ja jetzt auch gerade erst diese BBC-Studie, die herausgefunden hat, dass in 51 Prozent der Fragen, die sie gestellt haben zu Sachen aus ihrem eigenen Datenset signifikante Fehler drin waren und in 20 Prozent faktische Fehler.

Also diese Systeme sind wesentlich schlechter, als wir denken.

Und wir bewerten meistens solche Systeme nach Sachen, wo wir selber nicht die Antwort wissen.

Wir generieren damit SQL-Code, weil das kann ich nicht so gut, also mache ich den damit.

Den kann ich aber nicht bewerten und nachher ist es ein schlechter SQL-Code.

Wenn wir dann aber Sachen damit generieren, die wir selber verstehen, dann ist es auf jeden Fall, nachher sagen wir, oh, das ist aber nicht so gut.

Aber dann kann es einfach nur nicht das, was ich so gut kann, weil ich bin ja so schlau.

Und darum kann es halt die Sachen von den anderen Leuten, die andere Professionen haben, da kann es das.

Aber da, wo ich mich auskenne, da bin ich immer noch schlauer.

Und das ist eben einfach eine Falschwahrnehmung, weil es ist einfach in allen Bereichen falsch.

Wir können es nur in manchen Bereichen nicht so gut verifizieren.

Und das ist eben das, was wir immer wieder in den Ergebnissen sehen und wo wir auch fehlgeleitet werden durch diese Benchmarks.

Also es gibt ja diese Benchmarks, die immer nur zeigen, number goes up, es wird immer alles toller.

Und das liegt einfach daran, dass diese Benchmarks den Firmen bekannt sind.

Also trainieren sie halt auf den Benchmarks.

Und natürlich sind sie dann beim nächsten Mal besser.

Das ist totaler Quatsch.

Also diese Benchmarks sind nichts wert.

Und wenn wir dann aber das mit echten Anfragen machen, zeigt Papier nach Papier, dass es einfach immer noch schlecht ist und immer noch falsche Ergebnisse liefert.

Und das ist jetzt nicht auf Code bezogen, weil das war jetzt halt eher so dieser Use Case.

Ich lasse mir Sachen zusammenfassen oder ich lasse mir Sachen berichten aus dem Internet oder sowas.

Und der Use Case ist einfach wirklich katastrophal schlecht und sollte meiner Meinung nach gar nicht benutzt werden.

Lass uns kurz noch durch den Chat gehen.

Wir sind so ein bisschen über die Zeit rüber.

Also Dennis von Ketten hat noch geschrieben, er denke das Stichwort ist Intuition.

Das war, ehrlich gesagt, vor einer Viertelstunde.

LLMs haben keine. Dahintersteckt vielleicht was mit LLM und intrinsischer Prüfung auf Korrektheit zu tun hat.

Ja, genau.

Irgendetwas ist in diesen Modellen drin, nicht?

Also die haben auf dem Dataset hat irgendwas gebaut.

Intuition ist allerdings der falsche Begriff, glaube ich.

Unsere Intuition ist ja auch nicht fehlerfrei, aber wir lernen mitunter sofort neu.

Das war das, was wir diskutiert haben, nicht?

Dieses sofort neu lernen, dass das halt ein Problem ist.

Und ich muss halt gestehen, also Intuition ist halt borderline so Vorurteilsbehaftet, nicht?

Also wenn ich halt sage intuitiv, also ich treffe eine Person im Anzug auf einer Konferenz, ich nehme an, eher Entscheider.

Das ist halt Intuition slash Vorurteil und das ist irgendwie auch gefährlich, aber das ist eine andere Diskussion.

Nicht, weil am Ende ist das halt irgendwie jemand, der Techniker ist oder irgendwas anderes.

Ist im Grunde die gleiche Diskussion mit der Frage, ob man Schulkindern den Taschenrechner genehmigen soll, bloß auf der nächsten Ebene?

Das glaube ich nicht, weil das ist ja der Punkt, den Lucas auch gerade gemacht hat.

Das ist irgendwie nicht deterministisch, nicht?

Und das ist was anderes.

Und ein Taschenrechner produziert sogar erfolgreichere, bessere Ergebnisse und ist halt fehlerfrei.

Das ist übrigens auch eine von den Sachen, was in diesem künstlichen Intelligenzbereich und überhaupt in diesem Bereich von, wer ist denn nun eigentlich intelligenter, so ein bisschen eine Fehlleitung ist.

Selbstverständlich ist es so, dass ich schlechter Kopf rechnen kann als ein Taschenrechner.

Und das ist schon lange so und darüber brauchen wir nicht zu reden.

Und in einem anderen Podcast war es halt diese Geschichte mit dem Schachspielen.

Das ist irgendwie, da hattet ihr darüber diskutiert.

Großspielen gehört ja auch dazu.

Da ist es eigentlich eher umgekehrt so, dass es mich irritiert, dass diese stark formalisierten Systeme so sind, dass wir als Menschen immer noch oder lange Zeit mithalten konnten.

Also das ist ja ein Schachfeld, das kann ich perfekt formalisieren.

Es gibt ganz klare Regeln.

Das ist algorithmisch erschlagbar.

Trotzdem ist es halt so, dass Computer da lange Zeit nicht so gut ausgehalten haben.

Ich habe halt kein mentales Modell von dem, was der PC da generiert hat, das dann zu debuggen dauert.

Meiner Meinung nach länger, als mit einem solchen Modell selbst zu schreiben.

Unter der Voraussetzung, dass man es eben debuggen will.

Keine Ahnung, aber nicht guter Punkt.

Das wäre die Frage, will ich nicht sozusagen als Assistenz benutzen.

Also was ich tatsächlich gemacht habe, ist, ich habe dieses Ding gebaut zum Spam-Recycling.

Den gibt man in die Spam-Nachricht per Copy-Paste und der produziert anschließend Output, wo die ganzen Sachen alphabetisch sortiert sind.

Da habe ich das Ding durch die AI herausgefunden, wie man das macht und habe es anschließend reingeschrieben.

Aber es ist eher so wie ein technischer Berater, so.

Ich hatte das Gefühl, ich glaube, ich habe da immer noch die Kontrolle gehabt.

Also ich glaube, das, was die Person meint, war, dass man Code generieren lässt, anstatt ihn selbst zu schreiben.

Das ist auf jeden Fall die Erfahrung, die auch einige Kollegen von mir gemacht haben, die gesagt haben, ich bin durch die LLM langsamer geworden und habe sie deswegen jetzt auch wieder weggetan, weil ich gemerkt habe, dass ich mehr damit beschäftigt bin, diesen Code zu debuggen und zu verstehen, weil da so viele Fehler drin sind, als wenn ich ihn einfach selber geschrieben habe.

Und das ist, glaube ich, auch das, was Netzmuffel hier meint.

Ja, super.

Und das ist ja, glaube ich, ein total wichtiges Feedback.

Ich habe so ein bisschen das Gefühl, dass wir so ein bisschen langsam sozusagen das Ende finden sollten.

Wir haben nämlich schon überzogen.

Ich muss gestehen, die Nachrichten im Chat, also sorry, wir sind dir wahrscheinlich nicht ganz gerecht geworden.

Noch sozusagen irgendwelche letzten Worte, die du loswerden willst?

Ja, also wir haben jetzt nur einen Teil von dem besprochen, den wir eigentlich besprechen wollten, was ich vorausgesagt hatte.

Aber genau, also mir ist halt einfach wichtig, geht einfach ein bisschen, also wenn ihr euch entscheidet, diese Systeme zu benutzen, ich habe mich persönlich dagegen entschieden, aber wenn ihr euch dafür entscheidet, dann stellt sicher, dass was ihr dort mitmacht, dass ihr das auch verifizieren könnt, weil es ist eben kein System, was irgendwie zauberhaft die richtigen Sachen macht und ihr müsst einfach dafür gerade stehen und ihr seid nachher die Person, die das quasi produziert hat mit maschineller Unterstützung in Anführungsstrichen.

Und das heißt, ihr seid dafür verantwortlich, was da gebaut wird.

Und so müsst ihr das auch betrachten.

Und das, finde ich, ist eine der wichtigsten Grundsätze in der Verwendung von diesen Systemen.

Ja, genau.

Also finde ich, das ist eine total super Zusammenfassung.

Und das war auch eine von den Sachen, die mir mal in den Kopf gekommen ist.

Eigentlich geht es um kritisches Denken.

Irgendetwas ist da und wird irgendwie produziert.

Wie bewerte ich, ob das tatsächlich sinnvoll ist und ob das irgendwie hilft?

Und das ist, glaube ich, auch jenseits von AI etwas, was total hilfreich ist.

Also einfach Dinge halt kritisch hinterfragen und dann irgendwie sozusagen eine Entscheidung fällen.

Und damit können wir irgendwie auch nochmal kurz den Aufruf loswerden, Sonntag zur Wahl zu gehen.

Definitiv.

Genau, hervorragend.

Vielen Dank.

Und ich wünsche dann schon mal sozusagen ein schönes Wochenende.

Und wie gesagt, Montagabend ist dann die nächste Episode zu dem Thema No Estimates oder Beyond Estimates mit Woody.

Vielen Dank.

Alles klar.

Tschüss.
