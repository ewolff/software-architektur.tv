# Implementierungsplan: Guest-List Feature

## Überblick
Implementierung einer statischen Guest-List Seite für software-architektur.tv, die alle Stream-Gäste mit Profilen, LinkedIn-Links und Stream-Verlinkungen anzeigt.

## Phase 1: Datenstruktur erstellen

### 1.1 YAML-Datenfile erstellen (`_data/guests.yml`)
- **Ziel**: Zentrale Datenhaltung für alle Gast-Informationen
- **Struktur**:
  ```yaml
  guests:
    - name: "Max Mustermann"
      linkedin: "https://www.linkedin.com/in/maxmustermann"
      image: "/images/guests/max-mustermann.jpg"  
      tags: ["Microservices", "Kubernetes", "DevOps"]
      episodes:
        - title: "Folge 042: Microservices in der Praxis"
          url: "/2023/01/15/folge042.html"
          date: "2023-01-15"
  ```
- **Aufwand**: 2 Stunden
- **Abhängigkeiten**: Keine

### 1.2 Bildverzeichnis vorbereiten
- **Ziel**: Struktur für Gast-Profilbilder schaffen
- **Aufgaben**:
  - Verzeichnis `images/guests/` erstellen
  - Platzhalter-Bild für Tests (`placeholder.jpg`)
  - Bildrichtlinien definieren (Format, Größe)
- **Aufwand**: 1 Stunde
- **Abhängigkeiten**: Keine

## Phase 2: Jekyll Layout & Template

### 2.1 Guest-List Layout erstellen (`_layouts/guest-list.html`)
- **Ziel**: Wiederverwendbares Template für Guest-List Seiten
- **Features**:
  - Extends `default.html` Layout
  - CSS Grid für responsive Gast-Cards
  - Filter/Sort Controls
  - Liquid Template Logic für YAML-Daten
- **Aufwand**: 3 Stunden
- **Abhängigkeiten**: Phase 1.1 abgeschlossen

### 2.2 Guest-List Seite erstellen (`guests.md`)
- **Ziel**: Hauptseite für Guest-List mit korrektem Front Matter
- **Inhalte**:
  ```yaml
  ---
  title: Gäste von Software-Architektur im Stream
  layout: guest-list
  description: Alle Gäste des Software-Architektur Streams mit Profilen und Stream-Links
  ---
  ```
- **Aufwand**: 1 Stunde  
- **Abhängigkeiten**: Phase 2.1 abgeschlossen

## Phase 3: Styling & JavaScript

### 3.1 CSS Styling (erweitere `css/custom1.css`)
- **Ziel**: Ansprechendes, responsive Design für Guest-List
- **Features**:
  - Guest-Card Design (Bild, Name, Tags, Links)
  - Filter/Sort Control Styling
  - Mobile-first responsive Design
  - Tag-Pills Styling
  - Konsistent mit bestehender Cayman-Theme
- **CSS Klassen**:
  - `.guest-grid`, `.guest-card`, `.guest-avatar`
  - `.guest-tags`, `.tag-pill`
  - `.filter-controls`, `.sort-controls`
- **Aufwand**: 4 Stunden
- **Abhängigkeiten**: Phase 2 abgeschlossen

### 3.2 JavaScript Funktionalität (`js/guest-list.js`)
- **Ziel**: Interaktive Filter- und Sortier-Funktionen
- **Features**:
  - Textsuche nach Namen
  - Tag-basierte Filterung
  - Sortierung (alphabetisch, nach Anzahl Auftritte)
  - Lazy Loading für Bilder
  - URL-Parameter für geteilte Filter-States
- **Aufwand**: 4 Stunden
- **Abhängigkeiten**: Phase 3.1 abgeschlossen

## Phase 4: Navigation Integration

### 4.1 Header Navigation erweitern
- **Ziel**: Guest-List in Hauptnavigation integrieren
- **Datei**: `_includes/page-header.html`
- **Position**: Zwischen "Folgen" und "Podcast"
- **Code**:
  ```html
  <a href="/guests.html">Gäste</a>
  ```
- **Aufwand**: 1 Stunde
- **Abhängigkeiten**: Phase 2.2 abgeschlossen

## Phase 5: Testing & Optimierung

### 5.1 Performance Optimierung
- **Ziel**: Schnelle Ladezeiten und optimale User Experience
- **Aufgaben**:
  - Bildkomprimierung (WebP-Format, optimale Größen)
  - CSS/JS Minifizierung
  - Lazy Loading Implementation
  - Core Web Vitals Testing
- **Aufwand**: 2 Stunden
- **Abhängigkeiten**: Phase 3 abgeschlossen

### 5.2 Cross-Browser & Responsive Testing  
- **Ziel**: Kompatibilität auf allen Geräten sicherstellen
- **Test-Matrix**:
  - Desktop: Chrome, Firefox, Safari, Edge
  - Mobile: iOS Safari, Chrome Mobile, Samsung Internet
  - Tablets: iPad Safari, Android Chrome
- **Accessibility Testing**: Screen Reader, Keyboard Navigation
- **Aufwand**: 2 Stunden
- **Abhängigkeiten**: Phase 5.1 abgeschlossen

## Phase 6: Dokumentation & Content

### 6.1 Dokumentation erstellen
- **Ziel**: Wartbarkeit und einfache Datenpflege sicherstellen
- **Dokumente**:
  - `Guest-List/README.md`: Anleitung für Admins
  - `Guest-List/CONTRIBUTING.md`: Beitrag-Guidelines
  - Bildrichtlinien und Templates
- **Aufwand**: 2 Stunden
- **Abhängigkeiten**: Implementierung abgeschlossen

### 6.2 Initial Content Migration
- **Ziel**: Erste echte Gast-Daten einpflegen
- **Aufgaben**:
  - 10-20 prominente Gäste aus Posts extrahieren
  - LinkedIn-Profile recherchieren und verlinken
  - Profilbilder sammeln und optimieren
  - Tags aus bestehenden Posts zuordnen
- **Aufwand**: 3 Stunden
- **Abhängigkeiten**: Phase 6.1 abgeschlossen

## Technische Spezifikationen

### Dateistruktur
```
├── _data/
│   └── guests.yml              # Zentrale Gast-Datenbank
├── _layouts/
│   └── guest-list.html         # Template für Guest-List Seiten
├── _includes/
│   └── page-header.html        # Navigation (erweitert)
├── images/
│   └── guests/                 # Gast-Profilbilder
│       ├── placeholder.jpg
│       └── [guest-images]
├── css/
│   └── custom1.css            # Erweiterte Styles
├── js/
│   └── guest-list.js          # Interactive Funktionalität
├── Guest-List/
│   ├── requirements.md        # EARS Requirements
│   ├── plan.md               # Dieser Plan
│   └── README.md             # Wartungsanleitung
└── guests.md                 # Hauptseite
```

### YAML Schema Definition
```yaml
# _data/guests.yml Schema
guests:
  - name: string (required)           # Display name
    linkedin: string (required)       # LinkedIn URL
    image: string (required)          # Relative path to image
    tags: array[string] (required)    # Topic tags from episodes  
    bio: string (optional)            # Short bio text
    episodes: array (required)        # Episodes participated in
      - title: string                 # Episode title
        url: string                   # Relative URL to episode
        date: string (YYYY-MM-DD)     # Episode date
        role: string (optional)       # guest|co-host|moderator
```

### Performance Ziele
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s  
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3.0s
- **Lighthouse Score**: > 90 (Performance, Accessibility, SEO)

### Browser Support Matrix
- **Desktop**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Mobile**: iOS Safari 14+, Chrome Mobile 90+, Samsung Internet 14+
- **Accessibility**: WCAG 2.1 AA compliant

## Risiken & Mitigationen

### Technische Risiken
1. **Performance bei vielen Gästen**
   - *Mitigation*: Pagination oder Virtualization ab 100+ Gästen
   
2. **Bildladezeiten**
   - *Mitigation*: Lazy Loading, WebP-Format, CDN

3. **Jekyll Build-Zeit**  
   - *Mitigation*: Liquid Template Optimierung, Conditional Includes

### Content Risiken
1. **Fehlende LinkedIn-Profile**
   - *Mitigation*: Fallback auf andere Profile (Twitter, Website)
   
2. **Copyright bei Profilbildern**
   - *Mitigation*: Nur autorisierte Bilder, Fallback-Avatare

## Erfolgskriterien

### Funktional
- ✅ Alle Gäste werden korrekt angezeigt
- ✅ Filter/Sort Funktionen arbeiten fehlerfrei  
- ✅ Navigation ist intuitiv und konsistent
- ✅ Mobile Experience ist optimal

### Performance  
- ✅ Ladezeit < 3 Sekunden auf 3G
- ✅ Lighthouse Score > 90
- ✅ Keine Layout Shifts während Laden

### Wartbarkeit
- ✅ Neue Gäste können in < 5 Minuten hinzugefügt werden
- ✅ Dokumentation ist vollständig und verständlich
- ✅ Code ist kommentiert und strukturiert

## Zeitschätzung

| Phase | Aufwand | Abhängigkeiten |
|-------|---------|----------------|
| 1. Datenstruktur | 3h | - |
| 2. Templates | 4h | Phase 1 |  
| 3. Styling/JS | 8h | Phase 2 |
| 4. Navigation | 1h | Phase 2 |
| 5. Testing | 4h | Phase 3 |
| 6. Dokumentation | 5h | Phase 5 |
| **Gesamt** | **25h** | - |

## Next Steps

1. ✅ Plan erstellen und genehmigen lassen
2. 🔄 Phase 1: YAML-Struktur implementieren  
3. ⏳ Phase 2: Templates entwickeln
4. ⏳ Phase 3: Styling und Interaktivität
5. ⏳ Phase 4-6: Integration, Testing, Content

*Letzte Aktualisierung: 2025-08-04*