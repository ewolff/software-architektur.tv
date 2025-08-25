# Domain-Driven Design in der Praxis: Ein vollständiger Leitfaden für taktisches Design

Domain-Driven Design (DDD) ist ein mächtiger Ansatz zur Entwicklung komplexer Softwaresysteme. Dieser Artikel konzentriert sich auf das taktische Design als wichtigen Baustein von DDD und zeigt anhand praktischer Beispiele, wie es effektiv eingesetzt werden kann.

## Die Grundlagen des taktischen Designs

Taktisches Design beschäftigt sich mit der objektorientierten Strukturierung auf Klassenebene. Es stellt verschiedene Patterns bereit, die helfen, Business-Logik optimal zu organisieren:

### Entities und Value Objects
- **Entities** haben eine eigene Identität (z.B. eine Person oder ein Produkt)
- **Value Objects** repräsentieren Werte ohne eigene Identität (z.B. Geldbeträge oder Längenmaße)
- Value Objects sind unveränderlich (immutable) und haben Wert-Semantik

### Aggregates und Domain Events  
- **Aggregates** fassen mehrere Entities und Value Objects zusammen
- Sie haben eine Aggregate Root, die Konsistenz sicherstellt
- **Domain Events** dokumentieren relevante fachliche Ereignisse
- Konsistenz wird innerhalb von Aggregates synchron gewährleistet, zwischen Aggregates asynchron

### Repositories und Factories
- **Repositories** kapseln den Datenbankzugriff und geben die Illusion einer In-Memory Collection
- Sie definieren fachlich sinnvolle Abfragen
- **Factories** erzeugen komplexe Value Objects oder Aggregates

### Services
- **Services** implementieren Business-Logik, die nicht in Entities/Aggregates passt
- Zum Beispiel für Operationen über mehrere Aggregates hinweg

## Praktisches Beispiel: E-Commerce System

Am Beispiel eines E-Commerce Systems mit Lieferkontext lässt sich die Anwendung demonstrieren:

```java
// Entity
class Package {
  private PackageId id;
  private List<Product> products;
}

// Value Object  
class Address {
  private String street;
  private String city;
}

// Aggregate
class Delivery {
  private Package package;
  private Address address;
  
  public void schedule() {
    // Implement delivery scheduling logic
  }
}

// Repository
interface DeliveryRepository {
  Delivery findByCustomer(CustomerId id);
  void save(Delivery delivery);
}

// Service
class DeliveryService {
  public void scheduleDelivery(CustomerId customer, Package package) {
    // Coordinate delivery scheduling across aggregates
  }
}
```

## Event Sourcing und CQRS

Diese Patterns können das taktische Design ergänzen:

### Event Sourcing
- Speichert nicht nur den aktuellen Zustand, sondern auch die Events die dazu führten
- Gut geeignet für Domänen wo die Historie wichtig ist (z.B. Bankkonto)
- Sollte eine interne Implementierungsentscheidung bleiben

### CQRS (Command Query Responsibility Segregation)
- Trennt Lese- und Schreibmodell
- Ermöglicht unabhängige Skalierung
- Sinnvoll bei unterschiedlichen Anforderungen an Lesen/Schreiben
- Muss nicht zwingend eingesetzt werden

## Architektur-Varianten

Für die Gesamtarchitektur bieten sich zwei Hauptansätze an:

### Klassische Schichtenarchitektur
- UI, Logik und Persistenz in getrennten Schichten
- Abhängigkeiten nur von oben nach unten
- Einfach zu verstehen aber weniger flexibel

### Hexagonale Architektur
- Business-Logik definiert Ports (Interfaces)
- Adapter implementieren die technischen Details
- Bessere Testbarkeit durch Isolation der Domänenlogik
- Nicht wesentlich komplexer als Schichtenarchitektur

## Fazit

Taktisches Design ist ein mächtiges Werkzeug für die Strukturierung komplexer Geschäftslogik. Die Patterns sollten jedoch nicht blind angewendet werden:

- Für einfache CRUD-Operationen sind Transaction Scripts oft ausreichend
- Event Sourcing und CQRS nur bei echtem Bedarf einsetzen
- Architektur (Schichten vs. Hexagonal) nach Projektkontext wählen
- Fokus auf die Abbildung der Fachlichkeit legen

Der Erfolg von DDD liegt nicht in der peniblen Befolgung aller Patterns, sondern in der geschickten Auswahl und Kombination der passenden Werkzeuge für den jeweiligen Anwendungsfall.