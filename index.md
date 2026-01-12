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

## Adventskalender 2025

[Hier](/adventskalender2025.html) geht es zum Adventskalender 2025 mit
dem Thema "Advice for Designing Good Software Architecture".

## Freitag, 2026-01-16 13:00 CET Spec-Driven-Development mit Simon Martinelli

Code-First war gestern – Requirements-Driven ist die Zukunft! Doch bedeutet das wirklich, dass wir zu detaillierten Wasserfall-Spezifikationen zurückkehren müssen? Mitnichten!

In dieser Episode spricht Ralf D. Müller mit Simon Martinelli über den AI Unified Process (AIUP), einen agilen und iterativen Entwicklungsansatz, der Requirements ins Zentrum stellt – nicht den Code. Simon zeigt, wie man mit AIUP moderne Software entwickelt, bei der Anforderungen, Spezifikationen, Code und Tests gemeinsam durch kurze Iterationen wachsen, während KI als Konsistenz-Engine dient.

Wir diskutieren die zentrale Frage: Brauchen wir perfekte, deterministische Spezifikationen für KI-Code-Generierung? Simon argumentiert, dass dies der falsche Ansatz ist. Stattdessen ermöglicht AIUP iterative Verbesserung: Requirements treiben die Entwicklung, Spezifikationen werden detaillierter, Tests schützen das Systemverhalten, während der generierte Code sich gemeinsam mit allem anderen weiterentwickelt.

<!--
## Links
- 
- [AI Unified Process (AIUP)](https://aiup.dev)
- [Simon Martinelli](https://martinelli.ch)
- [AIUP Marketplace auf GitHub](https://github.com/martinellich/aiup-marketplace)
- [Spec-Driven Development with AI – A New Approach and a Journey Into the Past](https://martinelli.ch/spec-driven-development-with-ai-a-new-approach-and-a-journey-into-the-past/)
-->

{%- include youtube.html
  youtube-video-id="_VkC-CCEptk"
  image-url="/thumbnails/folge298.png"
%}

<section id="content-links">
	<a href="https://www.linkedin.com/events/7416516817726332928/">LinkedIn</a>
	<a href="https://www.twitch.tv/ebrwolff">Twitch</a>
	<a href="https://www.youtube.com/@EberhardWolff">YouTube Channel</a>
</section>

<!-- https://claude.ai/public/artifacts/e3c372ae-47cd-4706-9316-61aafb0be64a -->

[In Kalendar eintragen](spec-driven-development-mit-simon-martinelli.ics)

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
