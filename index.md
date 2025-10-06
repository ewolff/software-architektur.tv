---
title: "Software-Architektur im Stream"
type: website
description: Live-Diskussion zu Software-Architektur im Stream
tagline: Live-Diskussion zu Software-Architektur
---

Einmal in der Woche diskutiert Eberhard Wolff, Lisa Schäfer oder Ralf
D. Müller
Software-Architektur im
Live-Stream auf YouTube, Twitch und manchmal LinkedIn - oft zusammen mit einem
Gast. Zuschauer können über den Chat und
das Formular unten mitdiskutieren oder Fragen
stellen. 
Die Aufnahme steht danach als Video und Podcast zur Verfügung.

## Nächste Folge: Freitag 2025-10-10 Barrierefreiheit in Web-Projekten – Von der Architektur bis zur Implementierung

<!-- { include youtube.html -->
<!--   youtube-video-id="HlR70AlCwpA" -->
<!--   image-url="/thumbnails/folge280.png" -->
<!-- %} -->

<!-- <section id="content-links"> -->
<!-- 	<a href="https://www.linkedin.com/events/7376204788746620929/">LinkedIn</a> -->
<!-- 	<a href="https://www.twitch.tv/ebrwolff">Twitch</a> -->
<!-- 	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a> -->
<!-- </section> -->

**Gäste:** Maximilian Franzke & Danny Koppenhagen

Barrierefreiheit ist kein "Nice-to-have" mehr, sondern wird spätestens durch
das Barrierefreiheitsstärkungsgesetz (BFSG) seit Mitte 2025 für viele digitale
Dienste zur Pflicht. Doch wie integriert man Accessibility erfolgreich in
moderne Web-Architekturen? Unsere Gäste Danny Koppenhagen und Maximilian Franzke
zeigen, wie sie barrierefreie Web-Anwendungen entwickeln – von der strategischen
Architekturentscheidung bis zur praktischen Umsetzung.

Was erwartet euch:
* **Architektur-Impact:** Wie beeinflusst Barrierefreiheit eure
  Frontend-Architektur und Design System-Entscheidungen?
* **Praktische Umsetzung:** Konkrete Patterns und Techniken für
  barrierefreie Web-Anwendungen
* **Tooling & Automatisierung:** Welche Tools helfen bei der
  kontinuierlichen Überprüfung von Accessibility-Standards?
* **Enterprise-Scale:** Herausforderungen bei der Umsetzung in großen
  Organisationen mit mehreren Teams
* **Performance vs. Accessibility:** Wie balanciert man
  High-Performance-Anforderungen mit Barrierefreiheit?
* **Rechtliche Aspekte:** Was bedeuten WCAG, EAA und BFSG konkret für
  Entwicklungsteams?

Danny und Maximilian bringen ihre Erfahrung aus der Entwicklung des 
DB UX Design Systems sowie der Arbeit im BIK BITV Prüfverbund und dem
Austausch auf europäischer Ebene mit und zeigen, wie man von Anfang an
"accessibility-first" denkt, statt Barrierefreiheit nachträglich
"draufzupacken". Dabei geht es nicht nur um technische Lösungen, sondern
auch um organisatorische Prozesse und die Frage: Wie macht man
Barrierefreiheit zu einem natürlichen Teil der Softwarearchitektur?

**Für wen ist das interessant:**

* Software-Architekt:innen, die Barrierefreiheit von Beginn an
  mitdenken wollen
* Frontend-Entwickler:innen, die praktische Umsetzungsstrategien suchen
* Teams, die vor der Herausforderung stehen, bestehende Anwendungen
  barrierefrei zu machen
* Alle, die verstehen wollen, wie sich rechtliche Anforderungen auf
  Architekturentscheidungen auswirken
  
*Nach diesem Stream werdet ihr Barrierefreiheit nicht mehr als
"Extra-Aufwand" sehen, sondern als integralen Bestandteil guter
Software-Architektur.*

<!-- https://claude.ai/public/artifacts/e3c372ae-47cd-4706-9316-61aafb0be64a -\->

<!-- [Zum Kalendar hinzufügen](stream.ics) -->

## Fragen, Diskussion und Anregungen

Fragen, Diskussion und Anregungen für die Episode oder den Stream gerne im Twitch-Chat oder
YouTube-Chat oder anonym hier:

Questions, discussion, and suggestions are welcome in the Twitch chat or the
YouTube chat or
anonymously here:

{%- include google-form.html
  form-url="https://docs.google.com/forms/d/e/1FAIpQLSf0xIZkNG_wRJ0IiobVcO3Z-q3dQMcwYTww0wgiWCupZCKM4A/viewform"
  image-url="/images/google-form.png"
  %}

## Neueste Folgen

<div class="image-grid">
{%- for post in site.posts limit:4 %}
{%- assign image-url=site.url | append: "/thumbnails-small/" | append: post.thumbnail %}
{%- include link-card.html
  url=post.url
  title=post.title
  image-url=image-url
  keep-size=true
  %}
{%- endfor %}
</div>

## Lizenz

Inhalte von Software-Architektur im Stream zu konsumieren ist
[unvereinbar mit einer Unterstützung der AfD](/2024/01/22/folge198.html).

[Creative Commons Attribution 4.0 Unported
License](http://creativecommons.org/licenses/by/4.0/)

Attributiert werden sollen:

* Für Videos Eberhard Wolff, Ralf D. Müller oder Lisa Maria Schäfer und die jeweiligen Interviewten
* Für Sketchnotes Lisa Maria Schäfer

<a rel="me" href="https://mastodon.social/@ewolff"></a>
