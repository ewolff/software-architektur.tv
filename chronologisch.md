---
title: Folgen chronologisch
type: website
description: Folgen chronologisch
---

<input type="text"
  id="filterInput"
  placeholder="Episodes filtern"
  style="margin-bottom: 1rem; padding: 0.5rem; width: 100%;"
  />
  
<script>
  const filterInput = document.getElementById("filterInput");

  filterInput.addEventListener("input", () => {
    const filterText = filterInput.value.toLowerCase();

    document.querySelectorAll("a.link-card").forEach(card => {
      const p = card.querySelector("p");
      const text = p ? p.textContent.toLowerCase() : "";

      if (text.includes(filterText)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  });
</script>

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

