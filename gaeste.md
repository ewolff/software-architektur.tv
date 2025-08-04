---
layout: guests
title: Gäste der Software-Architektur.tv
description: Alle Gäste der Software-Architektur.tv mit ihren LinkedIn-Profilen und Episoden-Referenzen
permalink: /gaeste/
---

# Gäste der Software-Architektur.tv

Hier finden Sie alle Gäste, die bisher in der Software-Architektur.tv zu Gast waren, mit direkten Links zu ihren Episoden.

<div class="guests-search">
  <input type="text" id="searchInput" placeholder="Gäste durchsuchen..." />
</div>

<div class="guests-stats">
  <p><strong>{{ site.data.guests_final | size }} Gäste</strong> in <strong>{{ site.data.guests_final | map: 'episode_count' | sum }} Episoden</strong></p>
</div>

<div class="guests-grid">
  {% assign sorted_guests = site.data.guests_final | sort: 'episode_count' | reverse %}
  {% for guest_data in sorted_guests %}
    {% assign guest = guest_data[1] %}
    {% assign guest_name = guest_data[0] %}
    
    <div class="guest-card" data-name="{{ guest_name | downcase }}">
      <div class="guest-header">
        <div class="guest-avatar">
          <img src="/assets/images/{{ guest.avatar }}" 
               alt="{{ guest_name }}" 
               onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
          <div class="avatar-placeholder">{{ guest_name | slice: 0, 2 | upcase }}</div>
        </div>
        <div class="guest-info">
          <h3>{{ guest_name }}</h3>
          <p class="episode-count">{{ guest.episode_count }} Episode{% if guest.episode_count != 1 %}n{% endif %}</p>
          {% if guest.linkedin %}
          <a href="{{ guest.linkedin }}" target="_blank" class="linkedin-link">
            LinkedIn →
          </a>
          {% endif %}
        </div>
      </div>
      
      <div class="guest-episodes">
        <h4>Episoden:</h4>
        <ul>
          {% for episode in guest.episodes %}
          <li>
            <a href="/{{ episode.file | replace: '.md', '/' }}">
              Folge {{ episode.episode }}: {{ episode.title | truncate: 60 }}
            </a>
            {% if episode.youtube %}
            <a href="https://youtube.com/watch?v={{ episode.youtube }}" target="_blank" class="youtube-link">
              📺
            </a>
            {% endif %}
          </li>
          {% endfor %}
        </ul>
      </div>
    </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('searchInput');
  const guestCards = document.querySelectorAll('.guest-card');

  searchInput.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    
    guestCards.forEach(card => {
      const guestName = card.dataset.name;
      const isVisible = guestName.includes(searchTerm);
      card.style.display = isVisible ? 'block' : 'none';
    });
  });
});
</script>