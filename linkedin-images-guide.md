# LinkedIn-Profilbilder Anleitung

## Aktuelle Lösung
Momentan verwenden wir **UI-Avatars.com** für professionelle, farbkodierte Profilbilder:
- 🔵 **Blau**: Hauptmoderator (Eberhard)
- 🟢 **Grün**: Co-Moderatoren (Lisa, Ralf)  
- 🔴 **Rot**: Security-Experten (Christoph Iserlohn)
- 🟠 **Orange**: Frontend-Experten (Franziska, Joy, Lucas)
- 🟣 **Lila**: Allgemeine Gäste

## Echte LinkedIn-Bilder hinzufügen

### Option 1: Manuelle Extraktion (Empfohlen)
1. **LinkedIn-Profil öffnen** (z.B. linkedin.com/in/eberhard-wolff)
2. **Rechtsklick auf Profilbild** → "Bildadresse kopieren"
3. **URL in guests.yml ersetzen**:
   ```yaml
   - name: "Eberhard Wolff"
     image: "https://media.licdn.com/dms/image/C4D03AQG..."
   ```

### Option 2: LinkedIn Profile Badge
LinkedIn bietet öffentliche Profil-Badges:
```yaml
image: "https://www.linkedin.com/in/eberhard-wolff/picture/"
```
⚠️ **Hinweis**: Diese URLs sind nicht immer stabil.

### Option 3: Lokale Bilder
1. **Profilbilder downloaden** und in `/images/guests/` speichern
2. **Lokale Pfade verwenden**:
   ```yaml
   image: "/images/guests/eberhard-wolff.jpg"
   ```

## Prioritätenliste für echte Bilder

### Hauptmoderatoren (Höchste Priorität)
- [ ] Eberhard Wolff
- [ ] Lisa Schäfer  
- [ ] Ralf D. Müller

### Top-Gäste (Hohe Priorität)
- [ ] Lucas Dohmen (5 Episoden)
- [ ] Franziska Dessart (4 Episoden)
- [ ] Christoph Iserlohn (3 Episoden, Security)
- [ ] Marco Emrich (3 Episoden, Clean Code)
- [ ] Stefan Toth (3 Episoden, Architektur)

### Internationale Größen (Mittlere Priorität)
- [ ] Simon Brown (C4 Model)
- [ ] Grady Booch (Software-Legende)
- [ ] Kevlin Henney (Bekannter Speaker)
- [ ] Rebecca Parsons (ThoughtWorks)
- [ ] Alberto Brandolini (Event Storming)

## Automatisierung (Zukunft)
```javascript
// Beispiel für automatische LinkedIn-Bild-Extraktion
function updateLinkedInImage(name, linkedinUrl) {
  // Backend-Service oder Browser-Extension könnte
  // automatisch LinkedIn-Bilder extrahieren
  const profileId = linkedinUrl.match(/\/in\/([^\/]+)/)[1];
  return `https://your-image-proxy.com/linkedin/${profileId}.jpg`;
}
```

## CSS-Anpassungen
Die aktuellen Styles unterstützen beide Ansätze:
- **Generated Avatars**: Automatische Farbkodierung
- **Echte Bilder**: Professionelle Rundung und Schatten
- **Fallbacks**: Automatische Initials bei Ladeproblemen

## Bulk-Update Script
```bash
# Beispiel für Batch-Update mehrerer Bilder
./update-linkedin-images.sh \
  "Eberhard Wolff:https://real-image-url.jpg" \
  "Lisa Schäfer:https://real-image-url2.jpg"
```
