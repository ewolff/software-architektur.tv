---
title: Folgen chronologisch
type: website
description: Folgen chronologisch
---

{%- include filter.html
   placeholder="Episoden filtern"
   to-be-filtered="a.link-card"
   filter-subelement="p"
%}

<div class="image-grid">
{%- for post in site.posts %}
   {%- if post.title != "Folge149" %}
{%- assign image-url=site.url | append: "/thumbnails-small/" | append: post.thumbnail %}
{%- include link-card.html
  url=post.url
  title=post.title
  image-url=image-url
  keep-size=true
  %}

   {%- endif %}
{%- endfor %}
</div>

