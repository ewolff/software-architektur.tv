# Zusammenfassung: Ports and Adapters mit Vaughn Vernon

## Wichtigste Takeaways

- Ports und Adapters (auch bekannt als Hexagonale Architektur) ist ein einfaches aber mächtiges Architekturmuster
- Das Pattern besteht aus einem Inside (Ports) und Outside (Adapter) Bereich
- Adapter übersetzen externe Anfragen in ein Format, das die Ports verstehen
- Ein Port kann von mehreren Adaptern verwendet werden
- Das Pattern ermöglicht gute Testbarkeit durch einfache Isolation der Komponenten
- Es muss nicht zwingend mit Domain Driven Design kombiniert werden
- Simple Probleme können auch mit einfacheren Patterns wie Transaction Script gelöst werden

## Wichtige behandelte Fragen

- Was ist der Unterschied zwischen Ports und Adaptern?
- Warum wird das Pattern auch Hexagonale Architektur genannt?
- Wie unterscheidet sich das Pattern von klassischer Schichtenarchitektur?
- Welche Vorteile bietet das Pattern für Testbarkeit?
- Wann macht der Einsatz des Patterns Sinn und wann nicht?
- Wie kann das Pattern mit und ohne DDD eingesetzt werden?

## Glossar

- Port: Innere Schnittstelle der Anwendung, die von Adaptern verwendet wird
- Adapter: Übersetzer zwischen externen Systemen und internen Ports  
- Transaction Script: Einfaches Pattern für CRUD-Operationen ohne Domainlogik
- Dependency Inversion: Prinzip zur Entkopplung von Komponenten
- Domain Model: Reichhaltiges Modell mit Geschäftslogik im Gegensatz zu anemischen Modellen
- Repository: Pattern zur Persistierung von Domänenobjekten
- Anti-Corruption Layer: Übersetzer zwischen verschiedenen Bounded Contexts