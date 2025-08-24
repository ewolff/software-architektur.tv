# KI-gestützte Softwareentwicklung: Von der Architektur zum Code mit Claude

Die Integration von KI in den Softwareentwicklungsprozess gewinnt zunehmend an Bedeutung. In diesem Artikel betrachten wir ein praktisches Experiment, bei dem die KI Claude Code eine Webanwendung auf Basis einer Architekturspezifikation implementiert.

## Das Spark Framework und Claude Code

Als Grundlage dient das Spark Framework - ein Prompt-Builder für die Arbeit mit Claude Code. Es definiert verschiedene Entwicklungsphasen:

- Research & Discovery
- Spezifikation
- Pseudocode
- Architektur 
- Implementierung
- Test-Driven Development
- System Integration
- Completion Phase

Der Entwicklungsprozess läuft dabei weitgehend autonom ab - Claude Code arbeitet die Phasen selbstständig durch und generiert den Code.

## Das praktische Experiment

In unserem Experiment sollte eine "Worldly Map" Webanwendung implementiert werden. Dafür wurde Claude Code mit einem spezifizierten Prompt und den Anforderungen gefüttert. 

Das Ergebnis war beeindruckend: Innerhalb weniger Minuten erstellte die KI eine funktionsfähige Web-Anwendung mit:

- Interaktiver SVG-Oberfläche
- Drag & Drop Funktionalität
- Live-Updates der Parameter
- Domain Specific Language (DSL) zur textuellen Diagramm-Erstellung

Interessanterweise implementierte Claude Code auch Features wie Verbindungen zwischen Elementen, die zunächst in der UI nicht sichtbar waren, aber über die DSL nutzbar sind.

## Herausforderungen und Limitierungen

Das Experiment zeigte aber auch einige Schwachstellen:

- Die Test-Driven Development Phase wurde weitgehend ignoriert
- Nicht alle Qualitätskriterien wurden erfüllt (z.B. Usability)
- Die Integration der Arc42 Architektur-Dokumentation war unvollständig
- Der autonome Modus führte teilweise zu unkontrollierten Aktionen

## Lessons Learned

Einige wichtige Erkenntnisse aus dem Experiment:

1. **Präzise Spezifikationen sind entscheidend**: Je klarer die Anforderungen formuliert sind, desto besser das Ergebnis.

2. **Phasenweises Vorgehen hilft**: Die definierten Entwicklungsphasen geben Struktur und ermöglichen Kontrolle.

3. **Multiple Implementierungen sind möglich**: Durch die sinkenden Kosten von KI-Systemen können mehrere Varianten generiert und verglichen werden.

4. **Review-Aufwand beachten**: KI-generierter Code kann zu umfangreichen Änderungen führen, die geprüft werden müssen.

## Ausblick

Die Integration von KI in den Entwicklungsprozess wird zunehmen. Dabei kristallisieren sich einige Trends heraus:

- KI-Systeme werden leistungsfähiger und kostengünstiger
- Die Spezifikation wird zum zentralen Steuerungsinstrument
- Parallele Implementierungen und automatische Bewertung werden Standard
- Der Fokus verschiebt sich von manueller Entwicklung zur KI-gesteuerten Generierung

## Fazit

Das Experiment zeigt das große Potenzial von KI in der Softwareentwicklung. Gleichzeitig wird deutlich, dass wir unsere Prozesse und Arbeitsweisen anpassen müssen. Die Schlüssel zum Erfolg sind präzise Spezifikationen und ein kontrollierter Entwicklungsprozess.

Die Zukunft liegt wahrscheinlich in einer hybriden Entwicklung, bei der KI-Systeme wie Claude Code als "agentische Entwickler" eng mit menschlichen Entwicklern zusammenarbeiten. Dafür müssen wir lernen, die Stärken beider Seiten optimal zu nutzen.