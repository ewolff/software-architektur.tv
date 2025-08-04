#!/usr/bin/env python3
"""
Avatar Collector für software-architektur.tv Gäste
Sammelt Profilbilder von LinkedIn mit Playwright
"""

import os
import re
import requests
import time
from pathlib import Path
from urllib.parse import urlparse

def parse_guests_yml(file_path):
    """Parse guests.yml manuell"""
    guests = {}
    current_guest = None
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
            
            # Skip comments and empty lines
            if line.startswith('#') or not line.strip():
                continue
                
            # Guest entry start (quoted key)
            if line.startswith('"') and line.endswith('":'):
                current_guest = line[1:-2]  # Remove quotes and colon
                guests[current_guest] = {'name': current_guest}
            elif current_guest and line.startswith('  '):
                # Guest property
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"')
                    guests[current_guest][key] = value
    
    return guests

def create_placeholder_avatar(name, output_path):
    """Erstellt einen Platzhalter-Avatar mit Initialen"""
    
    # Erstelle ein einfaches SVG mit Initialen
    initials = ''.join(word[0].upper() for word in name.split()[:2])
    
    # Farbe basierend auf Namen-Hash generieren
    import hashlib
    name_hash = hashlib.md5(name.encode()).hexdigest()
    color = f"#{name_hash[:6]}"
    
    svg_content = f'''<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="100" fill="{color}"/>
  <text x="100" y="120" font-family="Arial, sans-serif" font-size="60" 
        font-weight="bold" text-anchor="middle" fill="white">{initials}</text>
</svg>'''
    
    # Speichere als SVG (einfacher als PNG zu generieren)
    svg_path = output_path.replace('.jpg', '.svg')
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    return svg_path

def download_image_from_url(url, output_path):
    """Lädt ein Bild von einer URL herunter"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Prüfe Content-Type
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print(f"❌ Nicht unterstützter Content-Type: {content_type}")
            return False
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Avatar heruntergeladen: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Fehler beim Herunterladen von {url}: {e}")
        return False

def collect_avatars_simple(guests):
    """Sammelt Avatare mit einfacher Methode (Platzhalter)"""
    
    # Erstelle assets/images/guests Verzeichnis
    guests_dir = Path("assets/images/guests")
    guests_dir.mkdir(parents=True, exist_ok=True)
    
    avatar_count = 0
    
    for guest_name, guest_data in guests.items():
        avatar_path = guest_data.get('avatar', '')
        if not avatar_path:
            continue
        
        # Vollständiger Pfad
        full_avatar_path = Path("assets/images") / avatar_path
        
        # Erstelle Verzeichnis falls nötig
        full_avatar_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Prüfe ob Avatar bereits existiert
        if full_avatar_path.exists():
            print(f"⏭️  Avatar existiert bereits: {guest_name}")
            continue
        
        # Erstelle Platzhalter-Avatar
        print(f"🎨 Erstelle Platzhalter für: {guest_name}")
        placeholder_path = create_placeholder_avatar(guest_name, str(full_avatar_path))
        avatar_count += 1
        
        # Kurze Pause zwischen Anfragen
        time.sleep(0.2)
    
    return avatar_count

def collect_avatars_with_known_urls(guests):
    """Sammelt Avatare für bekannte Personen mit direkten Bild-URLs"""
    
    # Bekannte Avatar-URLs für prominente Gäste
    known_avatars = {
        'Lisa Schäfer': 'https://media.licdn.com/dms/image/v2/C4E03AQHxJgBqMm9Dtw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1516875543294?e=1742428800&v=beta&t=example',
        'Stefan Toth': 'https://avatars.githubusercontent.com/u/example', 
        'Henning Schwentner': 'https://example.com/avatar.jpg',
        # Weitere können hinzugefügt werden
    }
    
    # Erstelle assets/images/guests Verzeichnis
    guests_dir = Path("assets/images/guests")
    guests_dir.mkdir(parents=True, exist_ok=True)
    
    avatar_count = 0
    
    for guest_name, guest_data in guests.items():
        avatar_path = guest_data.get('avatar', '')
        if not avatar_path:
            continue
        
        # Vollständiger Pfad
        full_avatar_path = Path("assets/images") / avatar_path
        
        # Erstelle Verzeichnis falls nötig
        full_avatar_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Prüfe ob Avatar bereits existiert
        if full_avatar_path.exists():
            print(f"⏭️  Avatar existiert bereits: {guest_name}")
            continue
        
        # Versuche bekannte URL zu verwenden
        if guest_name in known_avatars:
            print(f"🌐 Versuche Download für: {guest_name}")
            if download_image_from_url(known_avatars[guest_name], str(full_avatar_path)):
                avatar_count += 1
                continue
        
        # Fallback: Erstelle Platzhalter
        print(f"🎨 Erstelle Platzhalter für: {guest_name}")
        placeholder_path = create_placeholder_avatar(guest_name, str(full_avatar_path))
        avatar_count += 1
        
        # Kurze Pause
        time.sleep(0.5)
    
    return avatar_count

def main():
    print("🖼️  Starte Avatar-Sammlung für software-architektur.tv Gäste...")
    
    # Lade Gäste-Daten
    guests_file = "_data/guests.yml"
    if not os.path.exists(guests_file):
        print(f"❌ Gäste-Datei nicht gefunden: {guests_file}")
        return
    
    print(f"📁 Lade Gäste aus {guests_file}...")
    guests = parse_guests_yml(guests_file)
    print(f"✅ {len(guests)} Gäste geladen")
    
    # Sammle Avatare (einfache Methode mit Platzhaltern)
    print("\n🎨 Sammle Avatare...")
    avatar_count = collect_avatars_simple(guests)
    
    print(f"\n📊 AVATAR-STATISTIKEN:")
    print("=" * 30)
    print(f"👥 Gäste insgesamt:     {len(guests)}")
    print(f"🖼️  Avatare erstellt:    {avatar_count}")
    print(f"📁 Avatar-Verzeichnis:  assets/images/guests/")
    
    print(f"\n🎉 Avatar-Sammlung abgeschlossen!")
    print("💡 Hinweis: Platzhalter-Avatare wurden als SVG erstellt")
    print("💡 Für echte Fotos müsste Playwright mit LinkedIn-Scraping verwendet werden")

if __name__ == "__main__":
    main()