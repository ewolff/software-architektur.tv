# Die Evolution von Architektur durch Team Topologies

Software-Architektur und Teamorganisation werden oft als separate Themen betrachtet. Doch Team Topologies zeigt, dass beide eng miteinander verwoben sind und sich gegenseitig beeinflussen. Dieser Episode beleuchtet, auf welche Weise Team Topologies eine natürliche Evolution der Software-Architektur darstellt.

## Die Rolle der Kommunikation

Kommunikation ist sowohl essentiell als auch problematisch in der Softwareentwicklung. Einerseits ist sie die Basis für erfolgreiche Projekte - ohne vernünftige Kommunikation lassen sich Anforderungen nicht klären und Probleme nicht lösen. Andererseits kann zu viel Kommunikation den Fortschritt behindern, wenn Entwickler permanent in Meetings sitzen statt Code zu schreiben.

Die Herausforderung besteht darin, das richtige Maß an Kommunikation zu finden. Dokumentation ist wichtig, aber aufwendig zu erstellen und kann schnell veralten. Direkte Kommunikation ist oft effektiver, muss aber dosiert eingesetzt werden.

## Software-Architektur als Kommunikationsoptimierer

Eine zentrale Aufgabe der Software-Architektur ist es, den Bedarf für Kommunikation zu reduzieren - nicht durch Einschränkung der Kommunikation, sondern durch geschickte Strukturierung des Systems. David Parnas beschrieb dies bereits 1971 in seinem wegweisenden Paper "Information Distribution Aspects of Design Methodology".

Das Konzept des Information Hiding ist dabei fundamental: Module sollten so gestaltet sein, dass sie möglichst wenig Informationen nach außen preisgeben. Dies ermöglicht Änderungen am Modul, ohne dass andere Module davon betroffen sind. Ein klassisches Beispiel ist eine Bankkonto-Klasse, die intern entweder den Kontostand direkt speichern kann oder aus den Transkationen berechnen kann. Solange die öffentliche Schnittstelle beispielsweise zur Abfrage des Kontostands stabil bleibt, können die Implementierungen beliebig ausgetauscht werden.

## Team Topologies als evolutionärer Schritt

Team Topologies erweitert diesen Ansatz, indem es verschiedene Teamtypen und deren Interaktionsmuster definiert:

- Stream-aligned Teams: Verantworten einen Änderungsstrom von der Anforderung bis zur Produktion
- Enabling Teams: Unterstützen Stream-aligned Teams mit ihrer Expertise
- Platform Teams: Stellen eine Plattform als internes Produkt bereit
- Complicated Subsystem Teams: Kümmern sich um komplexe Komponenten, die beispielsweise komplizierte Algorithmen implementieren

Diese Teams interagieren über definierte Muster:
- Collaboration: Enge Zusammenarbeit, eine Person wird an ein anderes Team vorübergehend ausgeliehen
- X-as-a-Service: Nutzung definierter Benutzer-Schnittstellen oder APIs
- Facilitating: Unterstützung und Beratung

## Neue Perspektiven auf Systemgrenzen

Team Topologies erweitert die klassische domänenorientierte Aufteilung um weitere "Fracture Planes" wie:
- Standorte der Teams
- Regulatorische Anforderungen  
- Änderungshäufigkeit
- Risikoprofile
- Technologie-Stacks

Dies ermöglicht eine flexiblere Organisation, die besser zur Realität vieler Unternehmen passt. Die strikte Zuordnung "eine Domäne = ein Team" ist oft nicht praktikabel oder sinnvoll.

## Cognitive Load als zentrales Konzept

Ein wichtiger Beitrag von Team Topologies ist das Konzept des Cognitive Load: Teams sollten nicht mit zu vielen verschiedenen Aufgaben überlastet werden. Enabling Teams und Platform Teams helfen dabei, den Cognitive Load der Stream-aligned Teams zu reduzieren.

## Fazit

Software-Entwicklung ist ein soziotechnisches System - technische und organisatorische Aspekte lassen sich nicht trennen. Team Topologies bietet einen pragmatischen Rahmen, um beide Dimensionen zu berücksichtigen und die Evolution von Architektur und Organisation gemeinsam zu gestalten.

Dabei ist wichtig zu verstehen, dass es keine universellen Lösungen gibt. Die konkrete Ausgestaltung muss immer im Kontext der Organisation, der Menschen und der technischen Anforderungen erfolgen. Team Topologies liefert dafür wertvolle Patterns und Konzepte, die aber flexibel angewendet werden müssen.

Die Evolution von Software-Architektur durch Team Topologies zeigt: Erfolgreiche Systeme entstehen durch das Zusammenspiel von technischer Exzellenz und effektiver Teamorganisation. Nur wer beide Aspekte berücksichtigt, kann nachhaltig erfolgreiche Software entwickeln.
