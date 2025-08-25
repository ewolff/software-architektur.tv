# Folge 275 - Keine Bounded Contexts bei Netflix: Irrweg oder Inspiration?

## Wichtige Keytakeaways
- Netflix hat eine neue Unified Data Architecture (UDA) eingeführt, die ein zentrales Datenmodell für Content Engineering implementiert.
- Der Fokus liegt auf Datenanalyse und Integration, nicht auf der Ablösung von Bounded Contexts.
- Das System dient primär der Datenanalyse durch Business-User, nicht der Implementierung von Geschäftslogik.
- Die Lösung erscheint stark technisch getrieben und könnte als Overengineering betrachtet werden.
- Es handelt sich nicht um einen generellen Widerspruch zu DDD und Bounded Contexts.

## Behandelte Kernfragen
- Wie funktioniert das neue Datenmodell bei Netflix?
- Steht der Ansatz im Widerspruch zu Bounded Contexts?
- Was sind die eigentlichen Beweggründe für die Architekturentscheidung?
- Warum wurde eine Eigenentwicklung statt einer Kauflösung gewählt?
- Wie ist der Ansatz architektonisch zu bewerten?

## Glossar wichtiger Begriffe
- UDA (Unified Data Architecture): Netflix neue zentrale Datenarchitektur
- Bounded Context: DDD-Konzept für abgegrenzte fachliche Kontexte mit eigenem Modell
- Published Language: Gemeinsame Sprache für die Kommunikation zwischen Bounded Contexts
- Data Mesh: Dezentraler Ansatz für Datenarchitektur mit unabhängigen Datenprodukten
- RDF (Resource Description Framework): Framework zur Beschreibung von Ressourcen
- SHACL (Shapes Constraint Language): Sprache zur Definition von Constraints für RDF
- Upper: Netflix' eigene Sprache zur Domänenmodellierung
