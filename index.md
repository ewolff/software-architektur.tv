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

## 2026-06-18 14:45 KI macht Software vermeintlich billiger. Macht sie Projekte einfacher?

In dieser Paneldiskussion live vom [TechRiders Summits 2026](https://tech-riders.de/) beleuchten
CTOs und Tech Leads gemeinsam mit Eberhard Wolff, wie KI die Kosten-
und Komplexitätswahrnehmung in der Softwareentwicklung beeinflusst –
von dem Versprechen einer "billigen" Umsetzung bis zu den verborgenen
Risiken. Die Diskussion adressiert zentrale Fragen:

- "Billiger" vs. "einfacher": Was steckt hinter diesen Begriffen?
  "Einfacher" ist nicht gleichbedeutend mit schneller oder
  wartungsfreundlich – vielmehr entstehen neue Abhängigkeiten von
  Drittanbieter-APIs, die Wartung komplexer machen.
  
- Versteckte Kosten der KI: Die Illusion einer kostengünstigen
  KI-Lösung ignoriert oft unsichtbare Aufwände – etwa für
  Modell-Training, Monitoring, Compliance (z. B. DSGVO), QA und
  Lizenzabhängigkeit von Anbietern.
  
- Team & Kompetenzen: KI verändert die Rollen von Architekt:innen –
  weg von reiner Code-Optimierung hin zu KI-Management und ethischer
  Bewertung. Während Junior-Entwickler:innen vermeintlich durch
  KI-Assistenten profitieren, droht der Wissenstransfer zu erodieren,
  wenn KI "Black Boxes" für Entscheidungen nutzt. 
  
- Strategische Grenzen: Lohnt sich KI aus architekturhistorischer
  Sicht? Welche Prinzipien (z. B. Modularität, Observability) bleiben
  unverändert, um Systeme auch im KI-Zeitalter kontrollierbar und
  skalierbar zu halten?
  
Gäste aus dem Speaker Line-Up des TechRiders Summit:

- Sebastian Kleinschmager 

- Axel Schulz

Wer beim Tech Riders Summit dabei sein möchte: mit dem [Code
ARCH-TECHRIDER-2026](https://app.tech-riders.de/offers/1/book?v=ARCH-TECHRIDER-2026&pr=10)
ist es kostenlos für End-Benutzer und "Anwender:innen".

{% include youtube.html
  youtube-video-id="kAFfZNm9GH0"
  image-url="/thumbnails/folge316.png" %}

<section id="content-links">
	<a href="https://www.linkedin.com/events/7471188167782666240/">LinkedIn</a>
	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>
	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
</section>

[In Kalendar eintragen](fishbowl-lernen-llms-was-und-wie-wollen-wir-lernen.ics)

## 2026-06-19 13:00 CEST Zwischen KI-Hype und KI-Vampire - wie wir den Einsatz von KI im Alltag erleben

GenAI erledigt Tasks in atemberaubendem Tempo - und trotzdem sind wir abends erschöpft und leer. Steve Yegge nennt es den „AI Vampire": Wir bauen mehr denn je, aber FOMO, Dopamin-Loops beim Prompten, Review-Müdigkeit und die schleichende Erosion des eigenen Verständnisses („Cognitive Debt") saugen uns aus. Und manch einer fragt sich leise: Macht Coden eigentlich noch Spaß?

<a href="https://www.linkedin.com/in/martin-lippert-9a1909/">Martin Lippert</a> (Spring Tools Lead, Broadcom) und Ralf D. Müller sprechen offen darüber, was sie selbst erleben, wie sich ihre tägliche Arbeit verändert hat, und was der Einsatz von KI mit ihnen und ihrer Arbeit macht.

Eine Folge über den täglichen Einsatz von KI in der Softwareentwicklung - ohne Verteufelung, ohne Hype.

{% include youtube.html
youtube-video-id="mRX9TTvFf_k"
  image-url="/thumbnails/folge317.png" %}

<section id="content-links">
	<a href="https://www.linkedin.com/events/7472231202003853314/">LinkedIn</a>
	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>
	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
</section>

[In Kalendar eintragen](vampir.ics)

<!-- [Add to calendar](john-romeros-prinzipien-mit-tom-asel.ics) -->

<!-- https://claude.ai/public/artifacts/e3c372ae-47cd-4706-9316-61aafb0be64a -->

## Der Stream bei Konferenzen

Wir sind bei einigen Konferenzen präsent und haben auch Rabatt-Codes:

* [TechRiders Summit 2026](https://tech-riders.de/)
  * 2026-06-17 - 18, Köln
  * [Code ARCH-TECHRIDER-2026 - kostenlos für  End-Benutzer/ „Anwender:innen“](https://app.tech-riders.de/offers/1/book?v=ARCH-TECHRIDER-2026&pr=10)
* [iSAQB Software Architecture Gathering
  2026](https://www.software-architecture-gathering.com/),
  * 2026-11-16 - 19, Berlin
  *  * Code SATV_15  (15% Rabatt)
* [IT-Tage 2026](https://www.ittage.informatik-aktuell.de/index.html)
  * 2026-12-07 - 10, Frankfurt

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

[Weitere Folgen...](/chronologisch.html)

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

## Lizenz

Inhalte von Software-Architektur im Stream zu konsumieren ist
[unvereinbar mit einer Unterstützung der AfD](/2024/01/22/folge198.html).

[Creative Commons Attribution 4.0 Unported
License](http://creativecommons.org/licenses/by/4.0/)

Attributiert werden sollen:

* Für Videos Eberhard Wolff, Ralf D. Müller oder Lisa Maria Schäfer und die jeweiligen Interviewten
* Für Sketchnotes Lisa Maria Schäfer

<a rel="me" href="https://mastodon.social/@ewolff"></a>
