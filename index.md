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

<script src="/js/talkitover.js"></script>
<p>
<talk-it-over url="{{-site.url }}/episoden.txt"
              prompt="Lade {url}. Ich suche passende Folgen von Software-Architektur im Stream zu einem Thema."
              label="Let's talk it over"
              providers="claude,chatgpt,copy"><a href="/episoden.txt">Alle Folgen als Text für deine KI</a></talk-it-over>
</p>

## 2026-11-20 13:00 CET Produktivität mit KI: Das Harvard-Paper

Wie viel schneller werden Entwickler:innen durch den Einsatz von KI?
Viele Studien untersuchen vor allem, wie stark KI das Coding
beschleunigt. Doch schnellerer Code bedeutet nicht automatisch mehr
Produktivität. Entscheidend ist letztlich, ob tatsächlich mehr
sinnvolle Features entstehen und bei den Kunden ankommen.

Die [Harvard-Studie](https://fion.ac/jellyfish.pdf) hat Daten
von 720.542 Entwicklern aus 655 Firmen ausgewertet und dabei mehr als
nur die Coding-Leistung bewertet. In dieser Folge erläutert Eberhard
die Ergebnisse der Studie an und diskutieren sie. Was lässt sich aus
den Zahlen tatsächlich ableiten? Und was sagen sie über den
Produktivitätsgewinn durch KI in der Software-Entwicklung aus?

<!-- { include youtube.html  -->
<!--  youtube-video-id="VzrNTrjp_jc"  -->
<!--     image-url="/thumbnails/episode344.png" %}  -->

<!--  <section id="content-links"> -->
<!--  	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a> -->
<!--  	<a href="https://www.linkedin.com/events/7520417493513904128">LinkedIn</a> -->
<!--  	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>  -->
<!--  </section>  -->

<!-- [Event at treff.tech](https://treff.tech/events/3438863e-71a1-449e-a96a-50c2430628c4) -->


## Der Stream bei Konferenzen und Trainings

Wir werden von einigen Konferenzen und Trainings unterstützt und haben auch Rabatt-Codes:

* [Training "kollaborative Modellierung" bei Socreatory](https://www.socreatory.com/de/trainings/cosmo).
  * Code
[SASTV](https://pretix.eu/socreatory/cosmo--praesenz/redeem?voucher=SASTV&subevent=4983797) 20% auf den normalen Ticketpreis bis 2026-11-15 
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
