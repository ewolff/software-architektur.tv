# Domain-Driven Design in der Praxis - Von der Strategie zur Implementierung

Domain-Driven Design (DDD) ist ein mächtiger Ansatz zur Entwicklung komplexer Softwaresysteme. Diese Episode anhand eines durchgängigen Beispiels, wie die verschiedenen strategischen DDD-Werkzeuge ineinandergreifen und in der Praxis angewendet werden können.

## Event Storming als Ausgangspunkt

Event Storming ist eine kollaborative Methode, um ein gemeinsames Verständnis der Domäne zwischen Fachexpert:innen und Entwickler:innen aufzubauen. Die Technik ist bewusst niedrigschwellig gehalten: Auf orangefarbenen Post-Its werden domänenrelevante Ereignisse in der Vergangenheitsform notiert (z.B. "Bestellung wurde akzeptiert") und an einer Wand chronologisch angeordnet.

Der Prozess beginnt mit einer chaotischen Explorationsphase, in der möglichst viele Events gesammelt werden. Anschließend werden diese in eine zeitliche Abfolge gebracht. Dann werden sie in parallele Swimlanes gruppiert. Im nächsten Schritt werden besonders wichtige "Pivotal Events" mit fundamentale Zustandsübergänge im System identifiziert.

Die Stärken von Event Storming liegen in der einfachen Verständlichkeit für Domänenexpert:innen und der Möglichkeit zur parallelen Zusammenarbeit. Zusätzlich werden soziale Strukturen und Expertenwissen sichtbar. Die größte Herausforderung ist es, die richtigen Personen zusammenzubringen - sowohl Fachexpert:innen mit Vision als auch solche mit tiefem operativem Verständnis.

## Bounded Contexts identifizieren

Aus dem Event Storming lassen sich erste Kandidaten für Bounded Contexts ableiten. Diese ergeben sich typischerweise aus den Bereichen zwischen Pivotal Events und den Swimlanes. Im Beispiel eines E-Commerce-Systems könnten das sein:

- Bestellprozess (bis zur Bestellannahme)
- Rechnungsstellung  
- Auslieferung

Bounded Contexts sind abgegrenzte Bereiche, in denen ein konsistentes Domänenmodell gilt und eine Ubiquituous Language verwendet wird. Sie sollten idealerweise einem Team zugeordnet sein und enthalten zusammengehörige Fachlichkeit.

## Core Domain

Nicht alle Bounded Contexts sind gleich wichtig für den Geschäftserfolg. Die Core Domain umfasst den strategisch wichtigsten Bereich. Im E-Commerce-Beispiel könnte man zunächst den Bestellprozess vermuten, schließlich wird dort der Umsatz gemacht. Aber in Wirklichkeit ist die Core Domain abhängig von der Geschäftsstrategie. Wenn sich das Unternehmen beispielsweise durch besonders schnelle und zuverlässige Lieferung differenziert, ist der Auslieferungsprozess die Core Domain.

Die übrigen Contexts sind entweder:
- Generic Subdomains: Standardfunktionalität, die zugekauft werden kann
- Supporting Subdomains: Spezialfunktionalität zur Unterstützung der Core Domain

Diese Priorisierung hat weitreichende organisatorische Konsequenzen: Die Core Domain erhält die besten Ressourcen und hat Vorrang bei der Weiterentwicklung.

## Strategisches Design und Team-Topologien

Die Zusammenarbeit zwischen den Teams muss die strategische Priorisierung widerspiegeln. Entsprechend dem Customer/Supplier-Pattern agiert das Team der Core Domain als "Customer" gegenüber anderen Teams als "Supplier". Seine Anforderungen haben Priorität.

Moderne Team-Topologien bieten hier einen pragmatischeren Ansatz als die klassischen DDD-Muster:

- Stream-Aligned Teams verantworten von der Anforderungsanalyse bis zur Produktion eine Funktionalität.
- Platform Teams stellen eine Plattform als internes Produkt bereit.
- Enabling Teams unterstützen Stream-Aligned Teams beim Aufbau von Fähigkeiten.
- Complicated Subsystem Teams kümmern sich um komplexe Algorithmen.

Die größte Herausforderung liegt oft nicht in der technischen Umsetzung, sondern in organisatorischen Aspekten wie informellen Machtstrukturen oder toxischen Unternehmenskulturen. Diese müssen adressiert werden, damit die theoretischen Modelle in der Praxis funktionieren können.

Domain-Driven Design bietet wertvolle Werkzeuge für die Entwicklung komplexer Systeme. Der Schlüssel zum Erfolg liegt in der geschickten Kombination der verschiedenen Techniken und der Berücksichtigung des organisatorischen Kontexts. Die vorgestellten Ansätze helfen dabei, von der strategischen Analyse bis zur taktischen Implementierung eine durchgängige Lösung zu entwickeln.
