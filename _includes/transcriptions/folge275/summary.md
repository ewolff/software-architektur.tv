# Folge 275 - Keine Bounded Contexts bei Netflix: Irrweg oder Inspiration?

## Wichtige Keytakeaways
- Netflix baut eine Unified Data Architecture (UDA) für Content Engineering
- Der Fokus liegt auf Datenintegration und -analyse, nicht auf Geschäftslogik
- Es handelt sich nicht um eine vollständige Abkehr von Bounded Contexts
- Das System ermöglicht Datenanalyse über verschiedene Quellen hinweg
- Die Lösung erscheint stark technisch getrieben (Overengineering)

## Behandelte Kernfragen
- Warum baut Netflix ein zentrales Datenmodell?
- Steht dies im Widerspruch zu Bounded Contexts?
- Welche konkreten Geschäftsprobleme werden gelöst?
- Ist der gewählte Ansatz für andere Unternehmen sinnvoll?
- Wie verhält sich die Lösung zu Data Mesh und Data Products?

## Glossar wichtiger Begriffe
- UDA (Unified Data Architecture): Zentralisierte Datenarchitektur bei Netflix
- Apache Iceberg: Big-Data-Lösung für Datenanalyse
- RDF (Resource Description Framework): Framework zur Beschreibung von Ressourcen
- SHACL: Shape Constraint Language für RDF-Graphen
- Published Language: DDD-Pattern für gemeinsame Datenrepräsentation
- Data Mesh: Dezentraler Ansatz für Datenbereitstellung
- PDM (Primary Data Management): Netflix-System für Referenzdaten
- Sphere: Netflix-Tool für Business-Nutzer zum Erstellen von Reports
- APPA: Netflix-eigene Sprache zur Domänenmodellierung

## Fazit
Der Netflix-Ansatz scheint primär eine Datenintegrationslösung für Analysezwecke zu sein und steht nicht grundsätzlich im Widerspruch zu Bounded Contexts. Die Lösung erscheint sehr technisch getrieben und ist wahrscheinlich für die meisten Unternehmen nicht der richtige Weg.