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

## Freitag, 2026-02-06 13:00 CET Soziotechnische Architektur Reviews mit Jonas Clusen und Hansjörg Gude


<!--
{ include youtube.html
  youtube-video-id="2WMQMzkZnaE"
  image-url="/thumbnails/folge300.png"
%}

<section id="content-links">
	<a href="https://www.linkedin.com/events/7421627789709115392/">LinkedIn</a>
	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>
	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
</section>

<!-- https://claude.ai/public/artifacts/e3c372ae-47cd-4706-9316-61aafb0be64a -->

<!-- [In Kalendar eintragen](agile-doku.ics)
-->

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

[Weitere Folgen...](/chronologisch.html)

## Lizenz

Inhalte von Software-Architektur im Stream zu konsumieren ist
[unvereinbar mit einer Unterstützung der AfD](/2024/01/22/folge198.html).

[Creative Commons Attribution 4.0 Unported
License](http://creativecommons.org/licenses/by/4.0/)

Attributiert werden sollen:

* Für Videos Eberhard Wolff, Ralf D. Müller oder Lisa Maria Schäfer und die jeweiligen Interviewten
* Für Sketchnotes Lisa Maria Schäfer

<a rel="me" href="https://mastodon.social/@ewolff"></a>
