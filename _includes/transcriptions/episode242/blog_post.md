# Generative AI in der Softwarearchitektur - Ein Experiment mit einem AsciiDoc-Linter

Die Entwicklung von Software mithilfe von Künstlicher Intelligenz ist eines der spannendsten Themen unserer Zeit. In dieser Folge führen wir ein interessantes Experiment durch, bei dem ein KI-System nicht nur Code generiert, sondern auch architektonische Entscheidungen trifft und dokumentiert.

## Der Ausgangspunkt: Ein fehlender AsciiDoc-Linter

Der Anlass für das Experiment war ein fehlendes Feature: Seit Jahren gibt es keinen Linter für AsciiDoc, eine Markup-Sprache für technische Dokumentation. Ein Linter ist ein Werkzeug, das Code auf Konsistenz und Best Practices prüft. Diese Lücke bot eine ideale Gelegenheit, die Fähigkeiten von Generativer KI in einem realen Entwicklungsszenario zu testen.

## Der Entwicklungsprozess mit KI

Für das Experiment nutzten wir einen eigenen Chatbot-Frontend mit "agentischem Workflow". Das bedeutet, dass das KI-System selbstständig Funktionen wie Python-Code-Ausführung oder PlantUML-Diagramm-Generierung aufrufen kann. Der Entwicklungsprozess folgte dabei einem testgetriebenen Ansatz:

1. Das System schrieb zunächst Tests für die gewünschte Funktionalität.
2. Anschließend implementierte es den Code.
3. Bei Fehlern korrigierte es sich selbst.
4. Es führte auch Code Coverage Analysen durch.

Das System entwickelte dabei eigenständig sinnvolle Regeln für den Linter, zum Beispiel:
- Prüfung der korrekten Verwendung von Überschriftenebenen
- Validierung geschlossener Codeblöcke
- Konsistente Verwendung von Whitespaces
- Korrekte Attributierung von Bildern

## Architektur-Dokumentation durch KI

Besonders interessant war, dass das System nicht nur Code generierte, sondern auch eine vollständige Architekturdokumentation nach dem arc42-Template erstellte. Dies umfasste:
- Ein Architecture Communication Canvas als Überblick
- Qualitätsszenarien mit Priorisierungen
- Architekturentscheidungen mit Begründungen
- UML-Diagramme zur Visualisierung

## Chancen und Herausforderungen

Das Experiment zeigt sowohl die Potenziale als auch die Grenzen von KI in der Softwareentwicklung:

**Vorteile:**
- Schnelle Entwicklung funktionierender Code-Basis
- Konsistente und umfangreiche Dokumentation
- Selbstständige Fehlerkorrektur
- Fähigkeit zur Begründung von Entscheidungen

**Herausforderungen:**
- Verifikation der Korrektheit des generierten Codes
- Überprüfung der Sinnhaftigkeit von Qualitätsanforderungen
- Potenzielle "Scheinkompetenz" der KI
- Notwendigkeit menschlicher Überprüfung

## Lehren für die Zukunft

Das Experiment verdeutlicht, dass wir uns in einer Übergangsphase befinden. Ähnlich wie beim historischen Übergang von Assembler zu höheren Programmiersprachen, könnte KI eine neue Abstraktionsebene in der Softwareentwicklung einführen.

Für die praktische Anwendung ergeben sich folgende Empfehlungen:
- KI als Unterstützungswerkzeug nutzen, nicht als vollständigen Ersatz
- Kritische Überprüfung der generierten Ergebnisse
- Anpassung der Entwicklungsprozesse an KI-Unterstützung
- Klare Dokumentation der KI-Interaktionen

## Fazit

Während das Experiment zeigt, dass KI-Systeme bereits erstaunlich komplexe Entwicklungsaufgaben übernehmen können, bleiben menschliche Überprüfung und Steuerung unerlässlich. Die Zukunft liegt vermutlich in der intelligenten Kombination menschlicher und künstlicher Fähigkeiten, wobei die größte Herausforderung darin besteht, das richtige Maß an Vertrauen und Kontrolle zu finden.
