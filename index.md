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

## Next Episode: Friday, 2026-04-10 13:00 CEST Anarchy: A Solution to Software Development Organizations? with Andrew Harmel-Law

“Patterns of Anarchy” is a collection of writings published
in 1966. Andrew came to it because a) Christopher Alexander quotes
from it in “A Pattern Language” and b) because as a consultant and
developer they are interested in different patterns of organizing.

What interested them most about this book was the section “Constructive
Anarchism: Alternative Communities and Programs”. This covers the how
of anarchist organisation.

They will share some of the most interesting insights from their
perspective as a student of socio-technical organisation
design. Sometimes they’ll add some commentary. And of course the
question is how it relates to software engineering.

<!-- { include youtube.html -->
<!--   youtube-video-id="LuiiPYfcRKg" -->
<!--   image-url="/thumbnails/folge308.png" -->
<!-- %} -->

<!-- <section id="content-links"> -->
<!-- 	<a href="https://www.linkedin.com/events/7444787032842969088/">LinkedIn</a> -->
<!-- 	<a href="https://www.twitch.tv/ebrwolff">Twitch</a> -->
<!-- 	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a> -->
<!-- </section> -->

<!-- [In Kalendar eintragen](stream.ics) -->

<!-- https://claude.ai/public/artifacts/e3c372ae-47cd-4706-9316-61aafb0be64a -->

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
