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

{% capture tags %}
{% for tag in site.tags %}
{{ tag[0] }}
{% unless forloop.last %},{% endunless %}
{% endfor %}
{% endcapture %}

{% assign tags_sorted = tags | split:"," | sort %}

{% for unstripped_tag in tags_sorted %}
  {% assign tag = unstripped_tag | strip %}
  <h3 id="{{ tag }}">{{ tag }} <a href="#{{ tag }}">#</a></h3>
  <details>
  <summary>Folgen ...</summary>
<div class="image-grid">
{% for search_tag in site.tags %}
	{% if search_tag[0] == tag %}
	  {% for post in search_tag[1] %}
<a href="{{ post.url }}">
<img src="{{ site.url }}/thumbnails/{{ post.thumbnail }}" alt="{{ post.title }}"
		loading="lazy">
		<p>{{ post.title }}</p>
</a>
      {% endfor %}
	{% endif %}
  {% endfor %}
</div>
  </details>
{% endfor %}
