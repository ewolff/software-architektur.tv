# Warum ist Software(-Architektur) eigentlich immer so schlecht?

Software-Qualität ist ein komplexes und vielschichtiges Thema, das die IT-Branche seit Jahren beschäftigt. Als Berater sehe ich häufig suboptimale Software-Systeme, die unter mangelnder Wartbarkeit, unstrukturierter Business-Logik und technischen Schulden leiden. Doch woher kommt diese systematische Qualitätsproblematik und was können wir dagegen tun?

## Die Kernprobleme

Ein zentrales Problem ist der permanente Zeitdruck in Software-Projekten. Dieser führt dazu, dass gute Entwicklungspraktiken vernachlässigt werden und technische Schulden entstehen - nicht als bewusste Entscheidung, sondern als ungewollte Nebenwirkung. Häufig sind die gesetzten Deadlines dabei künstlich und dienen primär als Performance-Nachweis des Managements.

Ein weiteres Problem ist die mangelnde Sichtbarkeit von technischer Qualität. Während Mängel bei physischen Produkten offensichtlich sind, bleiben Probleme im Code oft lange verborgen. Dies erschwert die Kommunikation zwischen Technikern und Management erheblich.

Auch technische Entscheidungen auf Management-Ebene, wie der Einsatz von Microservices oder bestimmte Team-Strukturen, können negative Auswirkungen auf die Architektur haben. Diese werden oft ohne tieferes technisches Verständnis getroffen.

## Der Qualitäts-Trade-off 

Eine wichtige Erkenntnis ist: Maximale Qualität überall anzustreben ist weder realistisch noch sinnvoll. Eric Evans' Konzept der Core Domain aus dem Domain-Driven Design zeigt, dass wir Kompromisse eingehen und uns auf die wichtigsten Bereiche fokussieren müssen.

Qualität bedeutet dabei vor allem Wartbarkeit und nachhaltige Entwicklungsgeschwindigkeit. Diese ist besonders wichtig für langlebige Systeme - bei kurzfristigen Projekten können andere Prioritäten sinnvoll sein.

## Bessere Kommunikation als Schlüssel

Um die Situation zu verbessern, braucht es vor allem eine bessere Kommunikation zwischen Technikern und Management:

- Technische Probleme müssen in Business-Auswirkungen übersetzt werden (z.B. höhere Kosten, verpasste Deadlines)
- Das Management muss klar kommunizieren, welche Systeme nachhaltig entwickelt werden sollen
- Gemeinsam müssen realistische Trade-offs gefunden werden zwischen schneller Feature-Entwicklung und technischer Qualität

Eine Möglichkeit ist die Reservierung fester Budget-Anteile für Qualitätsverbesserungen. Dies ermöglicht kontrollierte Verbesserungen, auch wenn die perfekte Abstimmung mit Business-Prioritäten schwierig bleibt.

## Fazit

Die systematischen Qualitätsprobleme in der Software-Entwicklung haben viele Ursachen. Neben dem allgegenwärtigen Zeitdruck sind es vor allem Kommunikationsprobleme zwischen Technik und Business. 

Der Schlüssel zur Verbesserung liegt nicht primär in besseren technischen Praktiken, sondern in:

- Realistischeren Erwartungen an Qualität
- Besserer Kommunikation der Auswirkungen technischer Schulden
- Bewussteren Trade-off-Entscheidungen
- Reservierten Budgets für Qualitätsverbesserungen

Nur wenn beide Seiten - Techniker und Management - die Perspektive des anderen verstehen und gemeinsam nach praktikablen Lösungen suchen, können wir die Qualität unserer Software-Systeme nachhaltig verbessern.