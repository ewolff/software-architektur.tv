# Netflix ohne Bounded Contexts: Eine kritische Analyse der Unified Data Architecture

Netflix sorgte kürzlich mit einem Blogpost für Aufsehen, in dem das Unternehmen seinen Ansatz "Model once, represent everywhere" und die neue Unified Data Architecture (UDA) vorstellte. Auf den ersten Blick scheint dies im Widerspruch zu etablierten Architekturprinzipien wie Bounded Contexts und unabhängigen Microservices zu stehen. Eine genauere Analyse zeigt jedoch ein differenzierteres Bild.

## Die eigentliche Motivation

Der Blogpost nennt als Hauptprobleme inkonsistente Datenmodellierung, mangelnde Datenqualität und fehlende Verbindungen zwischen Systemen. Bei näherer Betrachtung wird jedoch deutlich, dass Netflix primär eine Analyseplattform aufbaut. Die UDA zielt darauf ab, Daten aus verschiedenen Quellen zu integrieren und für Business-Analysen zugänglich zu machen.

## Die technische Umsetzung

Die Unified Data Architecture basiert auf mehreren Komponenten:

- Primary Data Management (PDM) für Referenzdaten und Taxonomien
- Eine eigene Modellierungssprache (APPA) für Domänenmodelle
- Das Analyse-Tool Sphere für Business-User
- Unterstützung verschiedener Datenformate wie GraphQL, Avro und Apache Iceberg

Die Architektur ermöglicht es, Datenmodelle in verschiedene Repräsentationen zu übersetzen und Daten zwischen Systemen zu bewegen. Dabei nutzt Netflix Standards wie RDF und SHACL für die semantische Modellierung.

## Kein Widerspruch zu Bounded Contexts

Anders als zunächst vermutet, steht der Netflix-Ansatz nicht im fundamentalen Widerspruch zu Domain-Driven Design und Bounded Contexts:

1. Der Fokus liegt auf Content Engineering - möglicherweise ein einzelner Bounded Context
2. Es geht primär um Datenintegration für Analysezwecke, nicht um die Implementierung von Geschäftslogik
3. Das System erlaubt Erweiterungen und unterschiedliche Repräsentationen

## Kritische Bewertung

Einige Aspekte des Ansatzes sind kritisch zu sehen:

- Hoher technischer Aufwand für eine Infrastrukturlösung statt Fokus auf Geschäftslogik
- Keine klare Darstellung der konkreten Business-Probleme und des ROI
- Mögliche Unterschätzung der Komplexität eines universellen Datenmodells
- Alternative Ansätze wie Data Mesh werden nicht ausreichend diskutiert

## Fazit

Netflix baut keine Alternative zu Bounded Contexts, sondern eine Datenintegrationsplattform für Analysen. Der Ansatz ähnelt eher Patterns wie Published Language oder Data Products. Für die meisten Unternehmen wäre ein solcher Aufwand schwer zu rechtfertigen - etablierte Lösungen oder ein Data-Mesh-Ansatz könnten praktikabler sein.

Der Fall zeigt auch die Grenzen schriftlicher Kommunikation in der Softwarearchitektur: Viele wichtige Fragen zu Teamautonomie, Koordinationsaufwand und alternativen Lösungsansätzen bleiben unbeantwortet. Eine direkte Diskussion wäre hier aufschlussreicher gewesen.

Für Architekten bleibt die Lehre: Technische Lösungen für organisatorische Probleme sind selten nachhaltig. Der Fokus sollte auf der effizienten Umsetzung von Geschäftsanforderungen liegen, nicht auf dem Aufbau komplexer Infrastrukturen.