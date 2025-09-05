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

# Nach Anzahl Folgen sortiert

{% capture counts_with_tags_string %}
{% for tag in site.tags %}
{{ tag[1] | size | prepend:"000000" | slice:-6,6 }}:{{ tag[0] }}
{% unless forloop.last %},{% endunless %}
{% endfor %}
{% endcapture %}

{% assign counts_with_tags = counts_with_tags_string | split:"," | sort | reverse %}

{% for count_with_tag in counts_with_tags %}
  {% assign tag = count_with_tag | split:":" | last | strip %}
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
