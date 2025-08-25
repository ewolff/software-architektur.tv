# Architekturtheater mit KI: Live-Entwicklung einer Softwarearchitektur mit Claude

Diese Live-Session demonstriert, wie die Zusammenarbeit zwischen Mensch und KI bei der Entwicklung einer Softwarearchitektur aussehen kann. Als Beispielprojekt diente ein Wardley Map Editor - eine bewusst überschaubare Aufgabenstellung, die sich gut für die zur Verfügung stehende Zeit von einer Stunde eignete.

## Die Ausgangssituation

Das Projekt startete mit einem vorbereiteten GitHub-Repository, das bereits grundlegende Requirements und eine docToolchain-Integration enthielt. Als KI kam Claude zum Einsatz - speziell Claude Desktop in der Beta-Version, das durch MCP (Model Context Protocol) direkte Interaktionen mit GitHub ermöglichte.

## Der Architekturentwicklungsprozess

Die Architekturentwicklung folgte dem arc42-Template und begann mit den grundlegenden Kapiteln:

1. **Einführung und Ziele**: Hier wurden die initialen Qualitätsziele angepasst - weg von klassischen Zielen wie Performance, hin zu demo-spezifischen Zielen wie Präsentierbarkeit und Verständlichkeit.

2. **Randbedingungen**: Wichtige technische und organisatorische Rahmenbedingungen wurden definiert, wobei das enge Zeitbudget als zentrale Randbedingung identifiziert wurde.

3. **Kontextabgrenzung**: Claude erstellte sowohl fachliche als auch technische Kontextdiagramme im C4-Format, die die System- und Schnittstellengrenzen klar aufzeigten.

4. **Lösungsstrategie**: Hier wurden zentrale technische Entscheidungen getroffen und in Form von Architecture Decision Records (ADRs) dokumentiert.

## Besonderheiten der KI-Kollaboration

Mehrere interessante Aspekte der Mensch-KI-Zusammenarbeit wurden deutlich:

- **Eigenständigkeit vs. Kontrolle**: Claude zeigte teilweise viel Eigeninitiative und musste gelegentlich "gebremst" werden, um den kollaborativen Charakter zu wahren.

- **Kritische Reflexion**: Die KI hinterfragte Entscheidungen und Anforderungen konstruktiv, statt einfach "nach dem Mund zu reden".

- **Strukturierte Entscheidungsfindung**: Bei technischen Entscheidungen nutzte Claude systematische Ansätze wie Entscheidungsmatrizen und Sequential Thinking.

- **Dokumentationsqualität**: Die erstellte Dokumentation war durchweg professionell, mit aussagekräftigen Diagrammen und nachvollziehbaren Begründungen.

## Lessons Learned

Die Session zeigte mehrere wichtige Erkenntnisse:

1. KI kann als wertvoller Sparringspartner in der Architekturentwicklung dienen, der kontinuierlich zur Verfügung steht.

2. Die Qualität der Zusammenarbeit hängt stark von der Qualität der initial gegebenen Prompts und Anleitungen ab.

3. Nicht jede Limitation ist eine technische Schuld - bewusste Scope-Entscheidungen sind legitime architektonische Entscheidungen.

4. Die KI benötigt gelegentlich Korrekturen und Führung, liefert aber auch eigenständig wertvolle Perspektiven und Ideen.

## Fazit

Das "Architekturtheater" demonstriert, dass KI-Systeme wie Claude durchaus in der Lage sind, bei der Architekturentwicklung substantielle Unterstützung zu leisten. Dabei geht es weniger darum, den Menschen zu ersetzen, sondern vielmehr darum, einen kompetenten Kollaborationspartner zu haben, der den Architekturentwicklungsprozess bereichert.

Die erstellte Architektur mag nicht perfekt sein, aber sie bietet eine solide Grundlage für die weitere Entwicklung und demonstriert die Möglichkeiten der Mensch-KI-Zusammenarbeit in der Softwarearchitektur. Die nächsten Schritte wären die testgetriebene Implementierung des Systems - ein Prozess, der ebenfalls mit KI-Unterstützung durchgeführt werden könnte.

Die Session macht deutlich: KI in der Softwarearchitektur ist kein "Theater", sondern kann - richtig eingesetzt - ein wertvolles Werkzeug sein, das den Architekturentwicklungsprozess unterstützt und bereichert.
