---
title: Gäste
layout: guests
description: Alle Gäste von software-architektur.tv mit ihren Episoden
permalink: /gaeste/
---

# Gäste von software-architektur.tv

Hier findest du alle Gäste, die bisher in den Episoden von software-architektur.tv zu Gast waren, sortiert nach der Anzahl ihrer Auftritte.

Seit dem Start des Formats wurden **{{ site.data.guests | size }} verschiedene Gäste** in insgesamt **{% assign total_episodes = 0 %}{% for guest_data in site.data.guests %}{% assign total_episodes = total_episodes | plus: guest_data[1].episode_count %}{% endfor %}{{ total_episodes }} Episoden mit Gästen** begrüßt.

---

## Alle Gäste

<div class="guests-search">
  <input type="text" id="guest-search" placeholder="Gast suchen..." class="search-input">
  <div class="filter-options">
    <label><input type="radio" name="sort" value="episodes" checked> Nach Episoden-Anzahl</label>
    <label><input type="radio" name="sort" value="name"> Nach Name</label>
    <label><input type="radio" name="sort" value="recent"> Nach letztem Auftritt</label>
  </div>
</div>

<div class="guests-grid" id="guests-grid">
  {% assign sorted_guests = site.data.guests | sort: 'episode_count' | reverse %}
  {% for guest_data in sorted_guests %}
    {% assign guest = guest_data[1] %}
    <div class="guest-card" data-name="{{ guest.name | downcase }}" data-episodes="{{ guest.episode_count }}">
      <div class="guest-avatar">
        <img src="/images/{{ guest.avatar }}" alt="{{ guest.name }}" 
             onerror="this.src='/images/guests/default-avatar.png'">
      </div>
      <div class="guest-info">
        <h3 class="guest-name">{{ guest.name }}</h3>
        <p class="guest-episodes">{{ guest.episode_count }} Episode{% if guest.episode_count != 1 %}n{% endif %}</p>
        {% if guest.bio and guest.bio != "" %}
          <p class="guest-bio">{{ guest.bio }}</p>
        {% endif %}
      </div>
      <div class="guest-episodes-list">
        <h4>Episoden:</h4>
        <ul>
          {% assign sorted_episodes = guest.episodes | sort: 'number' %}
          {% for episode in sorted_episodes %}
            <li>
              <a href="/{{ episode.date | date: "%Y/%m/%d" }}/folge{{ episode.number | prepend: '000' | slice: -3, 3 }}.html">
                Episode {{ episode.number }}: {{ episode.title | remove: guest.name | remove: "mit" | remove: "with" | strip }}
              </a>
              <span class="episode-date">({{ episode.date | date: "%d.%m.%Y" }})</span>
            </li>
          {% endfor %}
        </ul>
      </div>
    </div>
  {% endfor %}
</div>

<script>
// Suchfunktionalität
document.getElementById('guest-search').addEventListener('input', function(e) {
  const searchTerm = e.target.value.toLowerCase();
  const guestCards = document.querySelectorAll('.guest-card');
  
  guestCards.forEach(card => {
    const name = card.dataset.name;
    if (name.includes(searchTerm)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
});

// Sortierung
document.querySelectorAll('input[name="sort"]').forEach(radio => {
  radio.addEventListener('change', function() {
    const sortBy = this.value;
    const grid = document.getElementById('guests-grid');
    const cards = Array.from(grid.children);
    
    cards.sort((a, b) => {
      switch(sortBy) {
        case 'name':
          return a.dataset.name.localeCompare(b.dataset.name);
        case 'episodes':
          return parseInt(b.dataset.episodes) - parseInt(a.dataset.episodes);
        case 'recent':
          // TODO: Sort by most recent episode date
          return 0;
        default:
          return 0;
      }
    });
    
    cards.forEach(card => grid.appendChild(card));
  });
});
</script>