## Titel: Domain-Driven Design - Ein vollständiges Beispiel 2/2

## Wichtige Keytakeaways:
- Taktisches DDD verwendet objektorientierte Konzepte wie Entities, Value Objects, Aggregates, Repositories, Factories und Services
- Event Sourcing ist eine Persistenzstrategie, bei der neben dem Zustand auch die Events gespeichert werden
- CQRS (Command Query Responsibility Separation) trennt Lese- und Schreibmodelle
- Hexagonale Architektur/Ports & Adapters ist eine Alternative zum klassischen Layering
- DDD sollte nur bei komplexer Geschäftslogik eingesetzt werden, für einfache CRUD-Operationen sind Transaction Scripts ausreichend

## Behandelte Kernfragen:
- Wie setze ich taktisches DDD praktisch um?
- Wann macht Event Sourcing Sinn?
- Was sind die Vor- und Nachteile von CQRS?
- Welche Architekturmuster eignen sich für DDD?
- Wie hängen Strategic Design und Tactical Design zusammen?

## Glossar wichtiger Begriffe:
- Entity: Objekt mit eindeutiger Identität
- Value Object: Unveränderliches Wertobjekt ohne eigene Identität
- Aggregate: Cluster zusammengehöriger Objekte mit definierter Grenze
- Repository: Abstrahiert Datenzugriff und gibt Illusion einer In-Memory Collection
- Event Sourcing: Speicherung von Zustandsänderungen als Event-Stream
- CQRS: Trennung von Lese- und Schreibmodell
- Transaction Script: Einfaches Muster für CRUD-Operationen ohne komplexe Domänenlogik
- Ports & Adapters: Architekturmuster zur Entkopplung von Geschäftslogik und technischen Details