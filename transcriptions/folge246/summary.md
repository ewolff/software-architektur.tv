# Folge 246 - GenAI und Software-Architektur mit Christian Weyer

## Zusammenfassung

In dieser Folge diskutieren Ralf Müller und Christian Weyer über die Rolle von Generative KI (GenAI) in der Software-Architektur. Christian Weyer, ein Experte auf diesem Gebiet, beleuchtet, wie Language Models (LMs) und ihre Nutzung die Entwicklung und das Design von Software-Anwendungen revolutionieren können.

### Entwicklungen bei Language Models

Christian erklärt den Unterschied zwischen Large Language Models (LLMs) und Small Language Models (SLMs), wobei LLMs oft in Cloud-Diensten gehostet werden, während SLMs lokal betrieben werden können. Die Effizienz und Anwendungsvielfalt von SLMs wird als Schlüssel hervorgehoben, um spezifische Anforderungen in der Softwareentwicklung zu erfüllen.

### Menschliche Sprache als Interface

Eine der zentralen Ideen des Gesprächs ist, dass menschliche Sprache als „First Class Citizen“ in Software-Architekturen integriert werden kann. Statt Benutzeroberflächen, die strikte Interaktionen erfordern, können Entwickler Systeme schaffen, die auf natürliche Sprache reagieren, was die Benutzerfreundlichkeit erheblich verbessert.

### Semantisches Routing und Guarding

Ein entscheidendes technisches Konzept, das angesprochen wird, ist das semantische Routing, welches ermöglicht, Anfragen basierend auf ihrem Inhalt an die richtigen Subsysteme oder Funktionen weiterzuleiten. Hierbei wird auch die Rolle von Embedding Models hervorgehoben, die helfen, Bedeutungen und Intentionen aus sprachlichen Eingaben zu extrahieren.

### Ethik und Sicherheit

Die Diskussion über die Grenzen und Risiken der GenAI-Nutzung wird ebenfalls angesprochen. Der Umgang mit potentiellen Missbrauchsfällen, wie etwa via „Prompt Injection“, erfordert zusätzliche Schutzmechanismen (Guardrails), um sicherzustellen, dass das System nur in den vorgesehenen Anwendungsbereichen operiert.

### Zukunft der Software-Architektur

Der Gastgeber fragt nach der Auswirkung der GenAI auf zukünftige Software-Architekturen. Christian ist der Ansicht, dass sich sowohl die Nutzeroberflächen als auch die zugrunde liegenden Systeme grundlegend verändern werden, um menschliche Sprache in den Mittelpunkt der Interaktion zu stellen.

## Key Takeaways

1. **Unterschied zwischen LLMs und SLMs**: LLMs sind große, oft cloudbasierte Modelle, während SLMs lokal gehostet werden können und spezifischere Anwendungen bedienen.
2. **Integration von Sprache als Interface**: Der Fortschritt in der menschlichen Sprachverarbeitung ermöglicht es, Software-Interaktionen natürlicher und benutzerfreundlicher zu gestalten.
3. **Semantisches Routing**: Dieser Mechanismus hilft, Anfragen basierend auf ihrem Inhalt an die zuständigen Module oder Datenbanken im Backend weiterzuleiten.
4. **Embedded Models für Sprachverständnis**: Diese Modelle sind entscheidend für das Verständnis von Nutzereingaben und die Transformation in strukturierte Daten.
5. **Sicherheitsvorkehrungen**: Guardrails sind notwendig, um die Nutzung von GenAI in einem kontrollierten Rahmen zu halten und Missbrauch vorzubeugen.
6. **Zukunft der Software-Architektur**: GenAI wird die Art und Weise, wie Software entwickelt und architektonisch gestaltet wird, fundamental verändern und die Rolle der Softwarearchitekten beeinflussen.

## Wichtige Fragen, die behandelt wurden

1. Was unterscheidet LLMs von SLMs und wann sollte welches Modell verwendet werden?
2. Wie kann menschliche Sprache effektiv in Software-Interaktionen integriert werden?
3. Was ist semantisches Routing und wie funktioniert es in der Praxis?
4. Welche Sicherheitsmaßnahmen sollten implementiert werden, um Missbrauch von GenAI zu verhindern?
5. Wie sieht die Zukunft der Software-Architektur im Kontext von GenAI aus?

## Glossar

- **Large Language Model (LLM)**: Ein großes KI-Modell zur Verarbeitung natürlicher Sprache, das auf riesigen Datenmengen trainiert wurde und typischerweise in der Cloud gehostet wird.
- **Small Language Model (SLM)**: Ein kleineres KI-Modell, das lokal gehostet werden kann und oft auf spezifische Anwendungsfälle zugeschnitten ist.
- **Semantic Routing**: Ein Verfahren, das Anfragen basierend auf deren Bedeutung an relevante Verarbeitungseinheiten weiterleitet.
- **Embedding Model**: Ein Modell, das Text in mathematische Vektoren umwandelt, um deren semantische Bedeutung zu erfassen und operationale Vergleiche zu ermöglichen.
- **Guardrails**: Mechanismen oder Richtlinien, die sicherstellen, dass KI-Modelle in den vorgesehenen Grenzen operieren und nicht für unerlaubte Zwecke missbraucht werden.
- **GenAI (Generative AI)**: Eine Form von KI, die in der Lage ist, neue Inhalte zu generieren, meist basierend auf Mustern und Informationen aus bestehenden Daten.