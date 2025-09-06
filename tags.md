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

{%- capture counts_with_tags_string %}
{%- for tag in site.tags %}
{{-tag[1] | size | prepend:"000000" | slice:-6,6 }}:{{-tag[0] }}
{%- unless forloop.last %},{%- endunless %}
{%- endfor %}
{%- endcapture %}

{%- assign counts_with_tags = counts_with_tags_string | split:"," | sort | reverse %}

{%- for count_with_tag in counts_with_tags %}
  {%- assign tag = count_with_tag | split:":" | last | strip %}
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

<script>
document.querySelectorAll('details.hover-details').forEach(details => {
  // Open when mouse enters the entire details
  details.addEventListener('mouseenter', () => {
    details.setAttribute('open', true);
  });

document.querySelectorAll('details').forEach(details => {
  const summary = details.querySelector('summary');

  summary.addEventListener('mouseenter', () => {
    details.setAttribute('open', true);
  });


</script>

