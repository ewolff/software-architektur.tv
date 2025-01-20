# GenAI und Software-Architektur: Ein Blick in die Zukunft

In der jüngsten Episode unseres Podcasts hatten wir die Ehre, Christian Weyer zu Gast zu haben, einen Experten für Generative AI (GenAI) und deren Anwendungen in der Software-Architektur. Der Blick auf GenAI ist fundamental für die Entwicklung moderner Softwarelösungen. In diesem Blogbeitrag wollen wir einige der wesentlichen Themen und Ideen zusammenfassen und vertiefen, die Christian in seiner Diskussion hervorgehoben hat.

## Die Revolution der Softwareentwicklung durch GenAI

Generative AI hat in den letzten Jahren zunehmend an Bedeutung gewonnen und ist ein Thema, das nicht nur Softwareentwickler, sondern auch Unternehmen und Endanwender gleichermaßen betrifft. Wie Christian betont, ist die Möglichkeit, menschliche Sprache als „First Class Citizen“ in Software-Architekturen zu integrieren, eine entscheidende Neuerung. Dies bedeutet, dass wir Softwarelösungen entwickeln können, die besser auf die Bedürfnisse der Benutzer abgestimmt sind, indem sie natürlicher Sprache als Eingabe verwenden.

Traditionell mussten Benutzer lernen, wie sie mit Maschinen kommunizieren. Sie mussten spezifische Anweisungen und Befehle verstehen und verwenden. Mit der Einführung von GenAI der Sprache als Benutzeroberfläche wird dieser Prozess jedoch revolutioniert. Anstatt Rücksicht auf technisches Fachwissen nehmen zu müssen, können Benutzer einfach ihre Absichten ausdrücken. Dies öffnet Türen für eine vollständig neue Benutzererfahrung.

### Von LLMs zu SLMs: Spannende Entwicklungen in der Sprachverarbeitung

Im Gespräch mit Christian wurde deutlich, dass die Unterscheidung zwischen großen Sprachmodellen (Large Language Models - LLMs) und kleineren Modellen (Small Language Models - SLMs) von erheblicher Bedeutung ist. Während LLMs aufgrund ihrer Größe und Komplexität oft in der Cloud gehostet werden, bieten SLMs die Möglichkeit, lokale und spezialisierte Lösungen zu entwickeln. Dies erlaubt eine bessere Kontrolle über Daten und Anwendungsfälle.

Christian erwähnte dabei auch das Konzept der „Mixture of Experts“ (MoE), eine Architektur, bei der mehrere spezialisierte Modelle zur Verarbeitung von Anfragen verwendet werden. Im Wesentlichen erfolgt die Verarbeitung in einem kleineren, effizienteren Modell, das in der Lage ist, qualitativ hochwertige Ergebnisse zu liefern, während es gleichzeitig die Rechenressourcen schont.

## Die Bedeutung von Intent-Analyse und Semantischem Routing

Ein wichtiges Konzept, das Christian und ich diskutiert haben, ist die Notwendigkeit der Intent-Analyse in Kombination mit semantischem Routing. Bei der Anwendung der GenAI-Technologie ist es unerlässlich, den spezifischen Wunsch oder die Anfrage eines Benutzers zu verstehen. An dieser Stelle kommen Embedding-Modelle ins Spiel. Diese Modelle helfen dabei, die Bedeutung und die Absicht hinter einer Anfrage präzise zu erfassen und sie der entsprechenden Verarbeitungsschicht zuzuordnen.

Ein praktisches Beispiel wäre die Nutzung eines Sprachinterfaces in einer Unternehmensanwendung: Wenn ein Benutzer fragt: „Wann hat Sebastian Zeit für einen Workshop?“, sollte das System in der Lage sein, den Kontext und die Absicht dieser Anfrage zu erkennen und entsprechend zu handeln. Die Semantik dieser Anfrage wird durch das Embedding-Modell in einen mathematischen Vektor umgewandelt, um das Routing zur passenden Logik oder Datenbank zu optimieren.

## Benutzeroberflächen der Zukunft

Eine spannende Perspektive, die aus unserem Gespräch hervorging, ist der zukünftige Einfluss von GenAI auf Benutzeroberflächen. Anstatt mit grafischen Benutzeroberflächen (GUIs) zu interagieren, könnten Benutzer einfach mit der Software sprechen. Diese Entwicklung könnte die Notwendigkeit für komplexe UIs oder Menüs, die oft zur Verwirrung führen, überflüssig machen. Christian merkt an, dass es verrückt ist, dass Anwender durch Menüs navigieren müssen, um Funktionen zu finden, anstatt diese einfach durch gesprochene Sprache abzurufen.

Die Vorstellung, dass Benutzeroberflächen weniger mechanisch und mehr intuitiv gestaltet werden können, ist beflügelnd. Kunden könnten beispielsweise ihre Wünsche äußern, und die Software würde die erforderlichen Einstellungen automatisch vornehmen, ohne dass der Benutzer dafür die Programmiersprache oder spezifische Anforderungen kennen muss.

## Die Herausforderung von Weltwissen vs. Sprachverständnis

Ein kritischer Punkt in Christians Argumentation war die Unterscheidung zwischen Weltwissen und Sprachverständnis. GenAI-Modelle werden nicht einfach als eine Art Wissensdatenbank angesehen, sondern als Systeme, die in der Lage sind, Sprache zu verstehen und miteinander zu kommunizieren. Dies eröffnet neue Möglichkeiten, wie wir Software nicht nur verbessern, sondern revolutionieren können.

Christian ist der Meinung, dass die Leistungsfähigkeit von GenAI nicht darin besteht, als allwissender Assistent zu fungieren, sondern die Absicht und den Kontext der Anfrage korrekt zu erfassen und entsprechend zu reagieren. Dies schafft ein Kommunikationsniveau zwischen Mensch und Maschine, das viele Anwendungen vereinfachen und intelligenter machen könnte.

## Die Rolle von Guardrails

Bei der Entwicklung von GenAI-gestützten Lösungen ist es unerlässlich, Guardrails oder Schutzmechanismen zu implementieren, die unangemessene oder gefährliche Anfragen abfangen und verhindern. Dies wurde besonders wichtig, als wir erkannten, dass eine KI, die sich nicht an Regeln hält, potenziell schädlich sein kann.

Christian schlägt vor, dass diese Schutzmechanismen den Nutzern helfen sollten, klare Grenzen zu setzen, wie sie interagieren möchten. Die Herausforderung besteht darin, sicherzustellen, dass das System nur nach den gewünschten Vorgaben operiert, um Missbrauch zu verhindern und die Datensicherheit zu gewährleisten.

## Futuristische Perspektiven: Wie weit können wir gehen?

In den letzten Abschnitten unserer Diskussion sprach Christian über die Zukunft von Agenten in der Softwareentwicklung. Diese Agenten könnten in der Lage sein, Entscheidungen zu treffen und basierend auf den Anfragen von Benutzern zu agieren. Während wir uns gegenwärtig in einer Phase der Exploration und des Experimentierens mit GenAI-Systemen befinden, gibt es sicher Potenzial, um massive Veränderungen im Bereich der Softwarearchitektur und -entwicklung einzuleiten.

Die Kombination von GenAI mit Low-Code-Entwicklung eröffnet neue Möglichkeiten für die Automatisierung einfacher Anwendungsfälle, wodurch die Entwicklungsgeschwindigkeit und Effizienz erheblich gesteigert wird.

## Fazit

Die Diskussion mit Christian Weyer hat verdeutlicht, wie transformative GenAI für die Softwareentwicklung ist. Wir stehen am Anfang einer neuen Ära, in der menschliche Sprache und Künstliche Intelligenz Hand in Hand gehen können, um intelligente, intuitive Softwarelösungen zu schaffen. Indem wir Intent-Analyse, semantisches Routing und lokale Modelle integrieren, können wir die Art und Weise, wie wir Software gestalten und verwenden, revolutionieren.

Lasst uns weiterhin diese bahnbrechenden Ideen fördern und die zahlreichen Möglichkeiten, die uns die GenAI-Technologie bietet, erkunden. Wir werden in den kommenden Jahren sicherlich viele spannende Entwicklungen beobachten, die diese Disziplin vorantreiben. Seid gespannt, was die Zukunft für uns bereithält!