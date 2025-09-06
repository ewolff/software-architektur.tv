---
title: Folgen nach Tags
type: website
description: Folgen nach Tags
---

<section id="content-links">
	<a href="/tags.html">Nach Anzahl Folgen sortiert</a>
	&nbsp;	&nbsp;
	<a href="/tags-alphabetisch.html">alphabetisch sortiert</a>
</section>

# Alphabetisch sortiert

{%- capture tags %}
{%- for tag in site.tags %}
{{-tag[0] }}
{%- unless forloop.last %},{%- endunless %}
{%- endfor %}
{%- endcapture %}

{%- assign tags_sorted = tags | split:"," | sort %}

{%- for unstripped_tag in tags_sorted %}
  {%- assign tag = unstripped_tag | strip %}
  <details>
  <summary>
  {%- assign count = site.tags[tag] | size %}
  <h3 id="{{-tag }}">{{-tag }}  ({{count}}) <a href="#{{-tag }}">#</a></h3>
  </summary>
<div class="image-grid">
{%- for search_tag in site.tags %}
	{%- if search_tag[0] == tag %}
	  {%- for post in search_tag[1] %}
{%- assign image-url=site.url | append: "/thumbnails/" | append: post.thumbnail %}
{%- include link-card.html
  url=post.url
  title=post.title
  image-url=image-url
  keep-size=true
  %}
      {%- endfor %}
	{%- endif %}
  {%- endfor %}
</div>
  </details>
{%- endfor %}
