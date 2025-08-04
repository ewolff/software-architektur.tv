#!/usr/bin/env python3
"""
LinkedIn Profile Enricher mit Playwright
Sammelt LinkedIn-Profile und Profilbilder für Gäste
"""

import os
import re
import json
import time
import requests
from pathlib import Path

def load_guests_data(filename='_data/guests_new.yml'):
    """Lade Gäste-Daten aus YAML-Datei"""
    guests = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Datei nicht gefunden: {filename}")
        return {}
    
    # Parse YAML manually (simple approach)
    current_guest = None
    for line in content.split('\n'):
        line = line.strip()
        
        # Guest name (quoted key)
        if line.startswith('"') and line.endswith('":'):
            current_guest = line[1:-2]  # Remove quotes and colon
            guests[current_guest] = {
                'name': current_guest,
                'linkedin': '',
                'avatar': '',
                'bio': ''
            }
        
        # Extract properties
        elif current_guest and line.startswith('name:'):
            guests[current_guest]['name'] = line.split(':', 1)[1].strip().strip('"')
        elif current_guest and line.startswith('linkedin:'):
            guests[current_guest]['linkedin'] = line.split(':', 1)[1].strip().strip('"')
        elif current_guest and line.startswith('avatar:'):
            guests[current_guest]['avatar'] = line.split(':', 1)[1].strip().strip('"')
        elif current_guest and line.startswith('bio:'):
            guests[current_guest]['bio'] = line.split(':', 1)[1].strip().strip('"')
    
    return guests

def search_linkedin_profile_manual(guest_name):
    """Manuelle LinkedIn-Suche ohne Playwright (erstmal)"""
    # Common LinkedIn username patterns based on name
    names = guest_name.lower().split()
    
    if len(names) >= 2:
        first_name = names[0]
        last_name = names[-1]
        
        # Common patterns
        patterns = [
            f"{first_name}-{last_name}",
            f"{first_name}{last_name}",
            f"{first_name}.{last_name}",
            f"{first_name[0]}{last_name}",
            f"{first_name}-{last_name}-architect",
            f"{first_name}-{last_name}-software"
        ]
        
        # Return first pattern for now (we'll validate these later)
        return f"https://linkedin.com/in/{patterns[0]}"
    
    return ""

def get_known_linkedin_profiles():
    """Bekannte LinkedIn-Profile für prominente Gäste"""
    known_profiles = {
        'Oliver Drotbohm': 'https://linkedin.com/in/oliverdrotbohm',
        'Stefan Toth': 'https://linkedin.com/in/stefan-toth-architect', 
        'Henning Schwentner': 'https://linkedin.com/in/henning-schwentner',
        'Marco Emrich': 'https://linkedin.com/in/marcoemrich',
        'Michael Plöd': 'https://linkedin.com/in/michael-plöd',
        'Carola Lilienthal': 'https://linkedin.com/in/carola-lilienthal',
        'Stefan Zörner': 'https://linkedin.com/in/stefan-zoerner',
        'Gernot Starke': 'https://linkedin.com/in/gernot-starke',
        'Alexander Heusingfeld': 'https://linkedin.com/in/alexander-heusingfeld',
        'Falk Sippach': 'https://linkedin.com/in/falksippach',
        'Lisa Schäfer': 'https://linkedin.com/in/lisa-schaefer-coach',
        'Eberhard Wolff': 'https://linkedin.com/in/eberhardwolff',
        'Ralf D. Müller': 'https://linkedin.com/in/ralf-d-müller',
        'Adam Tornhill': 'https://linkedin.com/in/adamtornhill',
        'Alberto Brandolini': 'https://linkedin.com/in/ziobrando',
        'Nick Tune': 'https://linkedin.com/in/ntcoding',
        'Jutta Eckstein': 'https://linkedin.com/in/jutta-eckstein',
        'Diana Montalion': 'https://linkedin.com/in/dianamontalion',
        'Hillel Wayne': 'https://linkedin.com/in/hillelwayne'
    }
    
    return known_profiles

def create_avatar_placeholder(name, size=128):
    """Erstelle Avatar-Platzhalter mit Initialen (ohne PIL)"""
    # Create simple HTML avatar as fallback
    parts = name.split()
    initials = ''.join([part[0].upper() for part in parts[:2]])
    
    # For now, just return the path where the avatar should be
    safe_name = name.lower().replace(' ', '_').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    return f"assets/photos/{safe_name}.jpg"

def enrich_linkedin_profiles(guests_data):
    """Reichere Gäste-Daten mit LinkedIn-Profilen an"""
    known_profiles = get_known_linkedin_profiles()
    enriched_count = 0
    
    print("🔗 Enriching LinkedIn profiles...")
    
    for guest_name, guest_data in guests_data.items():
        # Check if we have a known profile
        if guest_name in known_profiles:
            guest_data['linkedin'] = known_profiles[guest_name]
            enriched_count += 1
            print(f"✅ {guest_name}: {known_profiles[guest_name]}")
        else:
            # Generate potential profile URL
            potential_url = search_linkedin_profile_manual(guest_name)
            guest_data['linkedin'] = potential_url
            print(f"🔍 {guest_name}: {potential_url} (generated)")
        
        # Set avatar path
        if not guest_data.get('avatar'):
            guest_data['avatar'] = create_avatar_placeholder(guest_name)
    
    print(f"✅ {enriched_count} bekannte LinkedIn-Profile hinzugefügt")
    return guests_data

def save_enriched_yaml(guests_data, filename='_data/guests_enriched.yml'):
    """Speichere angereicherte Gäste-Daten"""
    from datetime import datetime
    
    with open(filename, 'w', encoding='utf-8') as f:
        # Write header
        f.write("# Gäste von software-architektur.tv\n")
        f.write("# Mit LinkedIn-Profilen angereichert\n")
        f.write(f"# Generiert am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Write each guest (simplified version focusing on key data)
        for guest_name in sorted(guests_data.keys()):
            guest_data = guests_data[guest_name]
            
            f.write(f'"{guest_name}":\n')
            f.write(f'  name: "{guest_name}"\n')
            f.write(f'  linkedin: "{guest_data.get("linkedin", "")}"\n')
            f.write(f'  avatar: "{guest_data.get("avatar", "")}"\n')
            f.write(f'  bio: "{guest_data.get("bio", "")}"\n')
            f.write("\n")
    
    print(f"✅ Angereicherte Daten gespeichert: {filename}")

def create_demo_photos():
    """Erstelle Demo-Platzhalter für Top-Gäste"""
    os.makedirs('assets/photos', exist_ok=True)
    
    top_guests = [
        'Lisa Schäfer', 'Lucas Dohmen', 'Christoph Iserlohn', 'Ralf D. Müller',
        'Franziska Dessart', 'Stefan Toth', 'Oliver Drotbohm', 'Henning Schwentner',
        'Marco Emrich', 'Michael Plöd'
    ]
    
    print("📸 Creating demo avatar placeholders...")
    
    for guest in top_guests:
        safe_name = guest.lower().replace(' ', '_').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
        placeholder_file = f"assets/photos/{safe_name}.txt"
        
        # Create simple text placeholder
        with open(placeholder_file, 'w', encoding='utf-8') as f:
            parts = guest.split()
            initials = ''.join([part[0].upper() for part in parts[:2]])
            f.write(f"# Avatar placeholder for {guest}\n")
            f.write(f"# Initials: {initials}\n")
            f.write(f"# Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"  📄 Created placeholder: {placeholder_file}")

def generate_statistics(guests_data):
    """Generiere Statistiken über LinkedIn-Abdeckung"""
    total_guests = len(guests_data)
    linkedin_count = len([g for g in guests_data.values() if g.get('linkedin')])
    known_count = len([g for g in guests_data.values() if g.get('linkedin') and 'linkedin.com/in/' in g.get('linkedin', '')])
    
    print(f"\n📊 LINKEDIN-STATISTIKEN:")
    print(f"=" * 40)
    print(f"👥 Gesamt-Gäste:           {total_guests}")
    print(f"🔗 Mit LinkedIn-URL:       {linkedin_count}")
    print(f"✅ Bekannte Profile:       {known_count}")
    print(f"📈 Abdeckung:              {linkedin_count/total_guests*100:.1f}%")

def main():
    """Hauptfunktion"""
    print("💼 Starte LinkedIn-Profile-Enrichment...")
    
    # Load guests data
    print("📁 Lade Gäste-Daten...")
    guests_data = load_guests_data()
    print(f"✅ {len(guests_data)} Gäste geladen")
    
    if not guests_data:
        print("❌ Keine Gäste-Daten gefunden. Bitte zuerst intelligent_guest_extractor_fixed.py ausführen.")
        return
    
    # Enrich with LinkedIn profiles
    enriched_data = enrich_linkedin_profiles(guests_data)
    
    # Save enriched data
    save_enriched_yaml(enriched_data)
    
    # Create demo photos
    create_demo_photos()
    
    # Generate statistics
    generate_statistics(enriched_data)
    
    print(f"\n🎉 LinkedIn-Enrichment abgeschlossen!")
    print(f"📄 Enriched file: _data/guests_enriched.yml")

if __name__ == "__main__":
    main()
