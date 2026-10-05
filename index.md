---
title: "Software-Architektur im Stream"
type: website
description: Live-Diskussion zu Software-Architektur im Stream
tagline: Live-Diskussion zu Software-Architektur
---

Einmal in der Woche diskutiert Eberhard Wolff, Lisa Schäfer, Ralf D. Müller
oder Lucas Dohmen bei Software-Architektur im Live-Stream auf YouTube, Twitch
und manchmal LinkedIn - oft zusammen mit einem Gast. Zuschauer können über den
Chat und das Formular unten mitdiskutieren oder Fragen stellen. Die Aufnahme
steht danach als Video und Podcast zur Verfügung.

## 2026-10-06 9:15 CEST Der Architektur-Turing-Test

Wir stellen einen Menschen und eine KI vor dieselbe Architekturfrage
und bitten beide, ihre Empfehlung kurz und knackig zu formulieren: mit
Architekturentscheidung, Begründung, Diagramm und bei Bedarf einem
kurzen Code-Beispiel.

Diese beiden Entscheidungen legen wir euch vor, natürlich ohne zu
verraten, wer welche geschrieben hat. Dazu jeweils zwei Fragen:

- Welche Empfehlung stammt vom Menschen?
- Welche Empfehlung würdet ihr in eurem eigenen Projekt umsetzen?

Damit die ADRs greifbar bleiben, arbeiten wir an einem durchgehenden
Beispielprojekt, das mit jedem ADR weiter wächst.

Am Ende interessiert uns vor allem eins: Wie gut trifft die KI eine
Architekturentscheidung, wenn sie dieselben Fakten vor sich hat wie
wir?

Dies ist die [Keynote für die Software Architecture Info  Days](https://www.infodays.de/sa/programm/konferenzprogramm/details/keydi-1).

{% include youtube.html
 youtube-video-id="iiNWOeQaJIY"
   image-url="/thumbnails/folge340.png" %}

 <section id="content-links">
 	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
 	<a href="https://www.linkedin.com/events/7510745377298366465">LinkedIn</a>
 	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>
 </section>

[Termin bei treff.tech](https://treff.tech/events/64769ed1-a6e6-4c3a-9ddc-4928b04cac1e) 

## Der Stream bei Konferenzen und Trainings

Wir werden von einigen Konferenzen und Trainings unterstützt und haben auch Rabatt-Codes:

* [Training "kollaborative Modellierung" bei Socreatory](https://www.socreatory.com/de/trainings/cosmo).
  * Code
[SASTV](https://pretix.eu/socreatory/cosmo--praesenz/redeem?voucher=SASTV&subevent=4983797) 20% auf den normalen Ticketpreis bis 2026-11-01 
* [iSAQB Software Architecture Gathering
  2026](https://www.software-architecture-gathering.com/)
  * 2026-11-16 - 19, Berlin
  * Code: SATV_15 (15% Rabatt)
* [IT-Tage 2026](https://www.ittage.informatik-aktuell.de/index.html)
  * 2026-12-07 - 10, Frankfurt
  * Code: ITT26-SIS-352 (100 Euro Rabatt)

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
