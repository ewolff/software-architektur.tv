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

## Nächste Folge am Freitag 2026-09-25: Simple Cloud in der Praxis mit Lucas Dohmen & Dirk Breuer

Wie betreibt man eine Webanwendung in der Simple Cloud – also auf transparenter
Basis-Infrastruktur (VPS, Networking, Firewalls) ohne Cloud-Managed-Services?
Mit [Dirk Breuer](https://codelater.de) bespreche ich, wie unser Setup bei
fejo.dk, einem der führenden Portale, um Ferienhäuser in Dänemark zu buchen,
funktioniert und wie wir dabei auf Einfachheit gesetzt haben. Wir gehen das
Setup durch: von Terraform über Ansible zu Docker und Capistrano. Wir freuen
uns auf eure Fragen vorab auf
[Mastodon](https://podcasts.social/@maschinenraum) oder LinkedIn oder live bei
der Aufnahme.

<!-- {%- include youtube.html -->
<!--  youtube-video-id="5L1xBA2A6us" -->
<!--    image-url="/thumbnails/episode338.png" %} -->

 <section id="content-links">
 	<a href="https://www.linkedin.com/events/7507805199416270848">LinkedIn</a>
 	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>
 	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
 </section>

<!-- [Event at treff.tech](https://treff.tech/events/beb9c703-5ec7-4941-97dd-6082cc7de3d7) -->

## Der Stream bei Konferenzen und Trainings

Wir werden von einigen Konferenzen und Trainings unterstützt und haben auch Rabatt-Codes:

* [BEDcon](https://bed-con.org/2026/)
  * 2026-09-23 - 24, Berlin
  * [Code A-ARCH205 40€ Rabatt](https://pretix.eu/bedcon-berlin/2026/redeem?voucher=A-ARCH205)
* [Training "kollaborative Modellierung" bei Socreatory](https://www.socreatory.com/de/trainings/cosmo).
  * Code
[SASTV](https://pretix.eu/socreatory/cosmo--praesenz/redeem?voucher=SASTV&subevent=4978817) 20% auf den normalen Ticketpreis bis 2026-10-04 
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
