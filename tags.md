---
title: Folgen nach Tags
type: website
description: Folgen nach Tags
---

# Folgen nach Tags

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
  <ul>
  {% for search_tag in site.tags %}
	{% if search_tag[0] == tag %}
	  {% for post in search_tag[1] %}
		  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
	{% endif %}
  {% endfor %}
  </ul>
{% endfor %}
