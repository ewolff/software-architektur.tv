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

## 2026-10-23 16:00 CEST Ralf mit Alexander von Zitzewitz: Wie relevant ist eine saubere Software-Architektur im Zeitalter der KI?

Moderne LLM's generieren oder überarbeiten ganze Applikationen in Rekordzeit. Die Frage ist, wie sich Architektur und Struktur auf die Qualität und die Wartbarkeit der Ergebnisse auswirkt. Spielt eine saubere Struktur noch eine Rolle? Was passiert, wenn die KI ein Problem nicht beheben kann?

<a href="https://www.linkedin.com/in/azitzewitz/">Alexander von Zitzewitz</a>

{% include youtube.html 
 youtube-video-id="fxOSHPLuL_I" 
    image-url="/thumbnails/folge342.png" %} 

 <section id="content-links">
 	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
 	<a href="https://www.linkedin.com/events/7518626878572912640">LinkedIn</a>
 	<a href="https://www.twitch.tv/ebrwolff">Twitch</a> 
 </section> 

[Termin bei treff.tech](https://treff.tech/events/11001c60-50f2-4269-9a0f-56473233b568)  

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
