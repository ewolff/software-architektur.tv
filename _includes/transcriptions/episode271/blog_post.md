# Die Architektur des Todessterns - Eine Fallstudie mit arc42

Die Dokumentation komplexer Softwarearchitekturen ist eine große Herausforderung. Das vor 20 Jahren entwickelte arc42-Template bietet hier einen bewährten Rahmen. Eine besonders kreative Anwendung dieses Templates stammt von Juan G. Carmona, der damit die Architektur des Todessterns aus Star Wars dokumentiert hat.

## Die Entstehungsgeschichte

Als erfahrener Softwareingenieur suchte Carmona nach einer Möglichkeit, das arc42-Framework anschaulich zu vermitteln. Die Wahl fiel auf den Todesstern als größtes fiktives Projekt der Galaxie. Die Geschichte dahinter: Chefingenieur Galen Erso, der zum Bau des Todessterns gezwungen wurde, versteckte die entscheidende Schwachstelle geschickt in der offiziellen Architekturdokumentation - wohl wissend, dass die Führungsebene diese ohnehin nicht lesen würde.

## Die arc42-Dokumentation im Detail

Die Dokumentation folgt konsequent dem arc42-Template mit seinen 13 Abschnitten:

1. **Einführung und Ziele**: Definition der Stakeholder (vom Imperator bis zu den Sturmtruppen) sowie der Qualitätsziele wie galaxisweite Operationsfähigkeit und Wartbarkeit

2. **Randbedingungen**: Externe Faktoren wie politische und rechtliche Vorgaben sowie interne Beschränkungen

3. **Kontext und Scope**: Aufteilung in Business-Kontext (imperiales Kommando, Flottenmanagement etc.) und technischen Kontext (Waffensysteme, Sensoren etc.)

4. **Lösungsstrategie**: Modularer Aufbau mit getrennten Systemen für Waffen, Energieversorgung und Lebenserhaltung

5. **Bausteinsicht**: Beschreibung der Hauptkomponenten wie Superlaser, Reaktorkern und Kommandozentrale

6. **Laufzeitsicht**: Dynamische Abläufe wie die Planetenzerstörungssequenz

7. **Verteilungssicht**: DevOps-Aspekte wie Entwicklungs-, Test- und Produktionsumgebungen

## Architektonische Entscheidungen und Qualitätsanforderungen

Eine zentrale architektonische Entscheidung war die Wahl eines einzelnen zentralen Reaktors statt mehrerer kleiner Einheiten. Diese Entscheidung wurde mit effizienterer Energiekontrolle und vereinfachter Systemintegration begründet. Die damit verbundenen Risiken - insbesondere die Reaktor-Vulnerabilität als "Single Point of Failure" - wurden zwar dokumentiert, aber von der Führungsebene ignoriert.

## Lessons Learned

Der Fall des Todessterns zeigt eindrücklich, wie wichtig es ist, Architekturdokumentation nicht als lästige Pflicht, sondern als strategisches Werkzeug zu begreifen. Qualitätsanforderungen wie Ausfallsicherheit und Verteidigungsfähigkeit müssen von Anfang an die architektonischen Entscheidungen leiten.

Die Dokumentation mit arc42 ermöglicht es, sowohl das große Ganze im Blick zu behalten als auch gezielt in technische Details einzusteigen. Das Template ist dabei flexibel genug, um an die jeweiligen Projektbedürfnisse angepasst zu werden - sei es für eine kleine Android-App oder eben eine Kampfstation in Mondgröße.

## Fazit

Die Dokumentation des Todessterns mit arc42 ist mehr als nur ein unterhaltsames Experiment. Sie demonstriert den praktischen Nutzen strukturierter Architekturdokumentation und zeigt, wie wichtig es ist, technische, geschäftliche und operative Aspekte ganzheitlich zu betrachten. Auch wenn die meisten realen Projekte kleiner sind als der Todesstern - die Grundprinzipien guter Architekturdokumentation bleiben dieselben.

May the Documentation be with you!