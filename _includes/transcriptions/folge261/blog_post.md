# Modelle statt Bounded Contexts? Eine Alternative für fachliche Modularisierung

Die Modularisierung von Software-Systemen nach fachlichen Gesichtspunkten ist eine zentrale Herausforderung in der Software-Architektur. Während Bounded Contexts aus dem Domain-Driven Design (DDD) häufig als Lösung genannt werden, zeigen sich dabei einige Probleme. Dieser Artikel schlägt einen alternativen Ansatz vor, der sich auf Modelle statt Bounded Contexts fokussiert.

## Die Problematik mit Bounded Contexts

Bounded Contexts vereinen drei unterschiedliche Aspekte:

1. Ein begrenzter Bereich für eine Ubiquitous Language
2. Ein Bereich, in dem ein spezifisches Modell gilt  
3. Ein Verantwortungsbereich für ein Team

Diese Vermischung verschiedener Konzepte macht Bounded Contexts schwerer verständlich und anwendbar. Zudem sind die drei Aspekte nicht zwangsläufig miteinander gekoppelt - ein Team kann durchaus mehrere fachliche Bereiche verantworten oder mehrere Teams können an einem Bereich arbeiten.

## Der Modell-Ansatz

Stattdessen sollten wir uns auf Modelle als zentrale Strukturierungseinheit konzentrieren. Ein Modell ist nach Stachowiak:

- Ein Abbild eines Originals
- Eine Abstraktion, die nur relevante Eigenschaften enthält  
- Auf einen bestimmten Zweck ausgerichtet

Diese Definition impliziert bereits, dass unterschiedliche Zwecke unterschiedliche Modelle erfordern. Ein Beispiel: Der "Kunde" hat in verschiedenen Kontexten unterschiedliche relevante Eigenschaften:

- Für die Lieferung: Lieferadresse, Name
- Für die Rechnungsstellung: Rechnungsadresse, Steuernummer
- Für den Check-in im Hotel: Personalausweis, Zimmerpräferenzen

## Autonomie als Leitprinzip

Ein wichtiges Ziel bei der Modularisierung sollte ein hohes Maß an Autonomie sein. Autonome Module können unabhängig voneinander geändert und weiterentwickelt werden. Dies wird erreicht durch:

1. Information Hiding: Die interne Implementierung wird hinter Schnittstellen versteckt
2. Minimale Abhängigkeiten: Module sollten möglichst wenige Verbindungen untereinander haben
3. Fachliche Kohäsion: Zusammengehörige Funktionalität wird gebündelt

Statt also einen zentralen "Kunden-Bounded-Context" zu haben, der von vielen anderen Kontexten abhängt, ist es oft besser die kundenrelevanten Daten direkt in den jeweiligen fachlichen Modellen zu halten.

## Praktische Vorgehensweise

Um zu einer guten fachlichen Modularisierung zu kommen, hilft folgende Herangehensweise:

1. Identifizierung der wesentlichen fachlichen Operationen (z.B. "Bestellung aufgeben", "Rechnung erstellen")
2. Definition klarer Schnittstellen für diese Operationen
3. Analyse der benötigten Daten und Regeln für jede Operation
4. Gruppierung zusammengehöriger Operationen in kohärente Modelle
5. Überprüfung und Optimierung der Autonomie zwischen den Modellen

Techniken wie Event Storming können dabei helfen, die relevanten fachlichen Operationen und deren Zusammenhänge zu identifizieren.

## Fazit 

Der Fokus auf Modelle statt Bounded Contexts hat mehrere Vorteile:

- Klarere Konzentration auf die fachliche Strukturierung
- Vermeidung der Vermischung mit Team- und Sprachaspekten
- Bessere Orientierung an Autonomie und Information Hiding
- Pragmatischere Herangehensweise für Entwickler

Bounded Contexts bleiben als Konzept wertvoll, besonders im Hinblick auf die Ubiquitous Language. Für die praktische fachliche Modularisierung ist jedoch der Modell-Ansatz oftmals zielführender.

Die Herausforderung bleibt, gute Heuristiken für die Identifikation und Abgrenzung von Modellen zu entwickeln. Dies ist eine zentrale Aufgabe der Software-Architektur, die weitere Forschung und Erfahrungsaustausch erfordert.