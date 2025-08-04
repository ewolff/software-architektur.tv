# Gast-Profilbilder

## Bildrichtlinien

### Format & Größe
- **Format**: WebP bevorzugt, JPEG als Fallback
- **Abmessungen**: 300x300 Pixel (quadratisch)
- **Dateigröße**: Maximum 50KB pro Bild
- **Kompression**: Optimiert für Web (Qualität 80-85%)

### Dateinamen-Konvention
- Kleinbuchstaben mit Bindestrichen
- Format: `vorname-nachname.webp` oder `vorname-nachname.jpg`
- Beispiele:
  - `eberhard-wolff.webp`
  - `lisa-schaefer.webp`
  - `ralf-mueller.webp`

### Bildqualität
- **Auflösung**: Scharf und professionell
- **Hintergrund**: Neutral oder entfernt
- **Beleuchtung**: Gleichmäßig, ohne harte Schatten
- **Ausrichtung**: Zentriert, Kopf und Schultern sichtbar

### Platzhalter
- `placeholder.jpg`: Standard-Avatar für Gäste ohne Bild
- `placeholder-webp`: WebP-Version des Platzhalters

## Bildoptimierung

### Tools
- **Squoosh.app**: Online-Tool für WebP-Konvertierung
- **TinyPNG**: JPEG-Kompression
- **ImageOptim**: macOS Tool für verlustfreie Optimierung

### CLI Tools
```bash
# WebP Konvertierung mit cwebp
cwebp -q 85 input.jpg -o output.webp

# JPEG Optimierung mit jpegoptim
jpegoptim --size=50k input.jpg
```

## Rechtliche Hinweise

### Bildrechte
- Nur autorisierte Bilder verwenden
- Bei Zweifel: Gast um Erlaubnis fragen
- Alternative: Platzhalter oder Initialen-Avatar

### Datenschutz
- Bilder nur mit Einverständnis der Gäste
- Möglichkeit zur Entfernung auf Anfrage
- DSGVO-konform handeln

## Maintenance

### Neue Bilder hinzufügen
1. Bild nach Richtlinien optimieren
2. In `images/guests/` ablegen
3. Pfad in `_data/guests.yml` aktualisieren
4. Lokale Tests durchführen

### Bestehende Bilder aktualisieren
1. Altes Bild ersetzen (gleicher Dateiname)
2. Browser-Cache berücksichtigen
3. Build-Prozess prüfen