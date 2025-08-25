# Netflix ohne Bounded Contexts: Eine kritische Analyse der Unified Data Architecture

Netflix hat kürzlich in einem Blogpost seine neue "Unified Data Architecture" (UDA) vorgestellt, die scheinbar im Widerspruch zu etablierten Konzepten wie Bounded Contexts und unabhängigen Microservices steht. Eine genauere Analyse zeigt jedoch, dass der vermeintliche Paradigmenwechsel differenzierter betrachtet werden muss.

## Die ursprüngliche Motivation

Netflix beschreibt als Hauptprobleme:
- Mehrfache und inkonsistente Modellierung gleicher Konzepte (z.B. Schauspieler, Filme) in verschiedenen Systemen
- Inkonsistente Terminologie
- Probleme mit Datenqualität und kaputten Referenzen 
- Mangelnde Verbindungen zwischen Systemen

Allerdings fehlt eine klare Darstellung der konkreten Business-Auswirkungen dieser technischen Herausforderungen.

## Die technische Lösung: Unified Data Architecture

Die UDA basiert auf mehreren Komponenten:

1. Ein zentrales Domänenmodell, das in verschiedene Repräsentationen gemappt wird:
- Apache Iceberg für Big Data Analysen
- GraphQL für Datencontainer
- Data Mesh für Datenprodukte

2. Primary Data Management (PDM):
- Verwaltet Referenzdaten und Taxonomien
- Bietet UI für Business-Anwender
- Nutzt W3C Standards für Wissensorganisation (SKOS)

3. Sphere:
- Self-Service Reporting Tool für Business-Experten
- Traversiert den Knowledge Graph
- Generiert SQL Queries

4. APPA:
- Eigene Sprache zur Domänenmodellierung
- Definiert Schlüsselattribute und Beziehungen
- Kann in verschiedene Formate (GraphQL, Avro, Java) übersetzt werden

## Kritische Einordnung

Der Blogpost erweckt zunächst den Eindruck eines radikalen Paradigmenwechsels weg von Bounded Contexts. Bei genauerer Betrachtung zeigen sich jedoch mehrere wichtige Aspekte:

1. Begrenzter Scope:
- Die UDA betrifft primär den Content Engineering Bereich
- Dieser existiert erst seit 2020
- Es handelt sich möglicherweise um einen einzelnen Bounded Context

2. Fokus auf Datenanalyse:
- Das eigentliche Ziel scheint eine integrierte Analyseplattform zu sein
- Es geht weniger um die Implementierung von Geschäftslogik
- Ähnelt eher dem Konzept von Data Mesh und Datenprodukten

3. Technische Komplexität:
- Erheblicher Entwicklungsaufwand für Infrastruktur
- Möglicherweise Overengineering statt Nutzung existierender Lösungen
- Starker Fokus auf technische statt geschäftliche Aspekte

## Fazit

Die Netflix UDA stellt keinen fundamentalen Widerspruch zu Domain-Driven Design und Bounded Contexts dar. Stattdessen handelt es sich um:

- Eine Datenintegrationsplattform für Analysezwecke
- Einen möglicherweise einzelnen Bounded Context (Content Engineering)
- Ein System, das Datenrepräsentation, nicht Geschäftslogik vereinheitlicht

Für die meisten Unternehmen wäre ein solcher Ansatz wahrscheinlich überdimensioniert. Alternative Ansätze wie Data Mesh oder der Einsatz existierender Integrationsplattformen könnten effizienter sein.

Der Fall zeigt auch die Grenzen schriftlicher Kommunikation in der Softwarearchitektur: Viele wichtige Fragen zu Teamautonomie, Koordinationsaufwand und den eigentlichen geschäftlichen Problemen bleiben unbeantwortet.