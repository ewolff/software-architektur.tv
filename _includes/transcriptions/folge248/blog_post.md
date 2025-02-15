Hier ist ein Blog-Post basierend auf dem Podcast-Transcript:

# Code Charta: Architektur-Visualisierung als Stadt

Software-Architektur zu visualisieren ist eine große Herausforderung - besonders wenn es darum geht, den Zustand und die Qualität von Legacy-Code zu kommunizieren. Das Open-Source-Tool Code Charta bietet hier einen innovativen Ansatz: Es stellt Softwarearchitektur als dreidimensionale Stadt dar.

## Die Stadt-Metapher

Code Charta visualisiert jede Datei als Gebäude in einer virtuellen Stadt. Dabei werden drei zentrale Metriken auf verschiedene visuelle Eigenschaften abgebildet:

- Die Grundfläche entspricht der Größe der Datei (z.B. Lines of Code)
- Die Höhe repräsentiert die Komplexität (z.B. zyklomatische Komplexität) 
- Die Farbe zeigt weitere Metriken wie Änderungshäufigkeit oder Test-Coverage

Die Ordnerstruktur wird als Straßennetz dargestellt, wodurch die hierarchische Organisation des Codes sichtbar wird. Diese intuitive Metapher macht es auch für Nicht-Techniker einfacher, den Zustand einer Codebasis zu verstehen.

## Einsatzmöglichkeiten

Code Charta eignet sich besonders für:

- Identifikation von problematischen Code-Bereichen durch auffällige "Gebäude"
- Visualisierung von Verbesserungen durch Refactoring über Zeit
- Kommunikation von technischen Schulden ans Management
- Analyse von Abhängigkeiten und Struktur größerer Codebasen

Ein besonders nützliches Feature ist der Delta-Modus: Hier können zwei Versionen verglichen werden, um Veränderungen über die Zeit sichtbar zu machen. Grüne Gebäude zeigen positive Entwicklungen wie reduzierte Komplexität, rote weisen auf potenzielle Probleme hin.

## Technische Details

Code Charta besteht aus zwei Hauptkomponenten:

1. Analyse-Tools zum Extrahieren der Metriken
2. Visualisierungs-Frontend zur Darstellung

Die Analyse kann über verschiedene Wege erfolgen:
- Direkter Source-Code-Parser (aktuell für Java)
- Import aus SonarQube 
- CSV-Import für beliebige Metriken
- Git-Log-Analyse für Change-Metriken

Die Daten werden in einem JSON-Format (cc.json) zwischen Analyse und Visualisierung ausgetauscht. Die Visualisierung läuft komplett im Browser und speichert alle Daten lokal.

## Open Source und Erweiterbarkeit

Code Charta ist unter BSD3-Lizenz als Open Source verfügbar. Durch die flexible Architektur und das standardisierte Datenformat lässt sich das Tool leicht erweitern:

- Neue Parser für weitere Programmiersprachen
- Alternative Visualisierungen 
- Integration weiterer Metriken
- Anbindung anderer Analyse-Tools

Die Community ist eingeladen sich zu beteiligen - sei es durch Feature-Requests, Bug Reports oder direkte Code-Beiträge.

## Fazit

Code Charta bietet einen wertvollen Beitrag zur Visualisierung von Software-Architektur. Die Stadt-Metapher macht komplexe Metriken greifbar und unterstützt die Kommunikation zwischen technischen und nicht-technischen Stakeholdern. 

Besonders im Legacy-Kontext hilft das Tool dabei, den Überblick zu behalten und Verbesserungen sichtbar zu machen. Die Open-Source-Natur und flexible Architektur ermöglichen vielfältige Einsatzszenarien.

Das Web-Studio auf der Code Charta Homepage ermöglicht einen einfachen Einstieg ohne Installation. Wer das Tool ausprobieren möchte, kann dort direkt mit eigenen Daten experimentieren.

[Link to Code Charta on GitHub]