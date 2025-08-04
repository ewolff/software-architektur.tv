# Guest-List Feature - Wartungsanleitung

## Überblick

Das Guest-List Feature bietet eine interaktive Übersicht aller Stream-Gäste mit Filterung, Sortierung und direkten Links zu ihren Profilen und Stream-Episoden.

## Dateien-Struktur

```
├── _data/
│   └── guests.yml              # Gast-Datenbank (YAML)
├── _layouts/
│   ├── default.html           # Standard Layout
│   └── guest-list.html        # Guest-List Template
├── _includes/
│   ├── head.html              # HTML Head mit CSS
│   ├── page-header.html       # Navigation (erweitert)
│   └── page-footer.html       # Footer
├── images/
│   └── guests/                # Profilbilder
│       └── README.md          # Bildrichtlinien
├── css/
│   └── custom1.css           # Erweiterte Styles
├── guests.md                 # Hauptseite
└── Guest-List/
    ├── requirements.md       # EARS Requirements
    ├── plan.md              # Implementierungsplan
    └── README.md            # Diese Datei
```

## Neue Gäste hinzufügen

### 1. Gast-Daten in YAML eintragen

Bearbeite `_data/guests.yml`:

```yaml
guests:
  - name: "Neuer Gast"
    linkedin: "https://www.linkedin.com/in/neuergast/"
    image: "/images/guests/neuer-gast.jpg"
    bio: "Kurze Beschreibung des Gastes"
    tags: ["Tag1", "Tag2", "Tag3"]
    episodes:
      - title: "Folge XXX: Episoden-Titel"
        url: "/YYYY/MM/DD/folgeXXX.html"
        date: "YYYY-MM-DD"
        role: "guest"
```

### 2. Profilbild hinzufügen

- Bild nach `images/guests/` kopieren
- Format: 300x300px, WebP oder JPEG
- Dateiname: `vorname-nachname.jpg`
- Siehe `images/guests/README.md` für Details

### 3. Jekyll neu bauen

```bash
bundle exec jekyll build
bundle exec jekyll serve --livereload
```

## Testing

### Lokales Testen

1. **Jekyll Server starten**:
   ```bash
   bundle exec jekyll serve --livereload
   ```

2. **Guest-List öffnen**: 
   - http://localhost:4000/guests.html

3. **Funktionen testen**:
   - ✅ Suchfunktion (Namen eingeben)
   - ✅ Tag-Filter (Dropdown auswählen)
   - ✅ Sortierung (Name, Auftritte, Letzte)
   - ✅ Episode-Links (klickbar)
   - ✅ LinkedIn-Links (öffnen in neuem Tab)
   - ✅ Mobile Ansicht (responsive)

### Browser-Tests

**Desktop**:
- ✅ Chrome (neueste Version)
- ✅ Firefox (neueste Version)  
- ✅ Safari (macOS)
- ✅ Edge (neueste Version)

**Mobile**:
- ✅ iOS Safari
- ✅ Chrome Mobile
- ✅ Samsung Internet

### Performance-Tests

**Tools**:
- Google PageSpeed Insights
- GTmetrix
- WebPageTest

**Ziele**:
- First Contentful Paint < 1.5s
- Largest Contentful Paint < 2.5s
- Lighthouse Score > 90

## Wartung

### Regelmäßige Aufgaben

1. **Gast-Daten aktualisieren**
   - Neue Episoden zu bestehenden Gästen hinzufügen
   - LinkedIn-Profile auf Aktualität prüfen
   - Veraltete Links korrigieren

2. **Bilder optimieren**
   - WebP-Format für bessere Performance
   - Bildgrößen auf 300x300px standardisieren
   - Kompression optimieren (< 50KB pro Bild)

3. **Tags vereinheitlichen**
   - Konsistente Schreibweise
   - Synonyme zusammenfassen
   - Neue Tags dokumentieren

### Troubleshooting

**Problem**: Gast wird nicht angezeigt
- ✅ YAML-Syntax prüfen (Einrückung, Anführungszeichen)
- ✅ Jekyll Build-Fehler überprüfen
- ✅ Browser-Cache leeren

**Problem**: Bild lädt nicht
- ✅ Dateipfad in YAML korrekt?
- ✅ Bild existiert in `images/guests/`?
- ✅ Dateiname korrekt (Groß-/Kleinschreibung)?

**Problem**: Filter funktioniert nicht
- ✅ JavaScript-Fehler in Browser-Konsole?
- ✅ CSS korrekt geladen?
- ✅ HTML-Struktur intakt?

## Deployment

### GitHub Pages

1. **Commit & Push**:
   ```bash
   git add .
   git commit -m "Add new guest: [Name]"
   git push origin main
   ```

2. **GitHub Pages Build**: 
   - Automatisch nach Push
   - Status unter Settings > Pages

### Manuelles Deployment

1. **Build**:
   ```bash
   bundle exec jekyll build --destination _site
   ```

2. **Upload**:
   - Inhalt von `_site/` auf Server kopieren

## SEO & Analytics

### Meta-Tags

Die Guest-List Seite enthält optimierte Meta-Tags:
- Title: "Gäste von Software-Architektur.tv"
- Description: SEO-optimierte Beschreibung
- Open Graph Tags für Social Media

### Structured Data

Für bessere SEO könnten Schema.org Person-Markups hinzugefügt werden:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Gast Name",
  "sameAs": "LinkedIn URL",
  "description": "Bio"
}
```

## Backup & Recovery

### Wichtige Dateien sichern

- `_data/guests.yml` (Hauptdatenbank)
- `images/guests/` (Profilbilder)
- `css/custom1.css` (Custom Styles)

### Git-Repository

Alle Änderungen werden automatisch in Git versioniert:
```bash
git log --oneline Guest-List/
```

## Weiterentwicklung

### Mögliche Erweiterungen

1. **Enhanced Features**:
   - Volltext-Suche in Episode-Beschreibungen
   - Gast-Favoriten mit LocalStorage
   - Social Media Integration (Twitter, GitHub)
   - RSS Feed für neue Gäste

2. **Performance Optimierungen**:
   - Lazy Loading für Bilder
   - Service Worker für Caching
   - CDN für statische Assets

3. **Analytics**:
   - Click-Tracking für LinkedIn-Links
   - Beliebte Gäste/Tags identifizieren
   - A/B Tests für UI-Verbesserungen

## Support

Bei Problemen oder Fragen:

1. **Logs prüfen**: Jekyll Build-Output
2. **Browser-Konsole**: JavaScript-Fehler
3. **GitHub Issues**: Feature-Requests und Bugs
4. **Community**: Software-Architektur.tv Slack

---

*Letzte Aktualisierung: 2025-08-04*  
*Version: 1.0*