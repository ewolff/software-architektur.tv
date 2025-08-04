#!/usr/bin/env python3
"""
Intelligente Gäste-Extraktion mit verbesserter Pattern-Erkennung
Analysiert alle Episode-Titel und extrahiert echte Gäste-Namen
"""

import os
import re
import json
import time
from datetime import datetime
from pathlib import Path

def load_all_episodes():
    """Lade alle Episoden aus _posts Verzeichnis"""
    episodes = []
    posts_dir = Path('_posts')
    
    if not posts_dir.exists():
        print("❌ _posts Verzeichnis nicht gefunden!")
        return []
    
    for md_file in posts_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                
                # Parse title
                title_match = re.search(r'title:\s*(.+)', frontmatter)
                title = title_match.group(1).strip().strip('"\'') if title_match else ""
                
                # Parse description  
                desc_match = re.search(r'description:\s*(.+)', frontmatter)
                description = desc_match.group(1).strip().strip('"\'') if desc_match else ""
                
                # Parse video ID
                video_match = re.search(r'video:\s*(\w+)', frontmatter)
                video_id = video_match.group(1) if video_match else ""
                
                # Extract episode number from filename or title
                episode_num = extract_episode_number(md_file.name, title)
                
                # Extract date from filename
                date_match = re.search(r'(\d{4}-\d{2}-\d{2})', md_file.name)
                episode_date = date_match.group(1) if date_match else ""
                
                episodes.append({
                    'filename': md_file.name,
                    'episode_number': episode_num,
                    'title': title,
                    'description': description,
                    'video_id': video_id,
                    'date': episode_date
                })
                
        except Exception as e:
            print(f"⚠️  Fehler beim Laden von {md_file.name}: {e}")
            continue
    
    # Sort by episode number
    episodes.sort(key=lambda x: int(x['episode_number']) if x['episode_number'].isdigit() else 0)
    return episodes

def extract_episode_number(filename, title):
    """Extrahiere Episode-Nummer aus Filename oder Titel"""
    # Try filename first
    filename_match = re.search(r'folge(\d+)|episode(\d+)', filename, re.IGNORECASE)
    if filename_match:
        return filename_match.group(1) or filename_match.group(2)
    
    # Try title
    title_matches = re.findall(r'(?:Folge|Episode)\s*(\d+)', title, re.IGNORECASE)
    if title_matches:
        return title_matches[0]
    
    # Fallback to filename number
    number_match = re.search(r'(\d+)', filename)
    return number_match.group(1) if number_match else "0"

def analyze_guest_patterns(episodes):
    """Analysiere Gast-Patterns in Episoden mit verbesserter Logik"""
    guest_patterns = {}
    
    for episode in episodes:
        title = episode['title']
        
        # Look for guest indicators
        guests = []
        
        # Pattern 1: "mit [Name(n)]"
        mit_matches = re.findall(r'mit\s+([^-\n]+?)(?:\s*-|$)', title, re.IGNORECASE)
        for match in mit_matches:
            names = extract_names_from_text(match.strip())
            guests.extend(names)
        
        # Pattern 2: "with [Name(n)]" 
        with_matches = re.findall(r'with\s+([^-\n]+?)(?:\s*-|$)', title, re.IGNORECASE)
        for match in with_matches:
            names = extract_names_from_text(match.strip())
            guests.extend(names)
        
        # Pattern 3: Name nach Folge-Nummer (z.B. "Folge 91 - Sven Johann")
        if not guests:
            name_after_number = re.search(r'(?:Folge|Episode)\s*\d+\s*-\s*([A-Z][a-z]+(?:\s+[A-Z]\.?)?\s+[A-Z][a-z]+)', title)
            if name_after_number:
                potential_name = name_after_number.group(1).strip()
                if is_likely_person_name(potential_name):
                    guests.append(potential_name)
        
        # Clean and validate guests
        clean_guests = []
        for guest in guests:
            clean_guest = clean_guest_name(guest)
            if clean_guest and is_valid_guest_name(clean_guest):
                clean_guests.append(clean_guest)
        
        if clean_guests:
            episode['detected_guests'] = clean_guests
            for guest in clean_guests:
                if guest not in guest_patterns:
                    guest_patterns[guest] = []
                guest_patterns[guest].append(episode)
    
    return guest_patterns

def extract_names_from_text(text):
    """Extrahiere Namen aus Text-Snippet mit verbesserter Logik"""
    # Split by "und", "and", ","
    separators = r'\s+und\s+|\s+and\s+|,\s*'
    parts = re.split(separators, text, flags=re.IGNORECASE)
    
    names = []
    for part in parts:
        clean_name = clean_guest_name(part)
        if clean_name and is_likely_person_name(clean_name):
            names.append(clean_name)
    
    return names

def clean_guest_name(name):
    """Bereinige Gast-Namen"""
    if not name:
        return ""
    
    # Remove common prefixes/suffixes
    name = re.sub(r'^(der|die|das|einem|einer|den|dem)\s+', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+(live|von|aus|bei|zur|zum|über|für|auf|vom)\s+.*$', '', name, flags=re.IGNORECASE)
    
    # Remove location/conference indicators
    name = re.sub(r'\s*\([^)]*\)\s*', ' ', name)  # Remove parentheses
    name = re.sub(r'\s*(OOP|Special|Live|Conference|Day).*$', '', name, flags=re.IGNORECASE)
    
    # Clean up whitespace and punctuation
    name = re.sub(r'[""„"()]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name

def is_likely_person_name(name):
    """Prüfe ob Text wahrscheinlich ein Personenname ist"""
    if not name or len(name) < 3:
        return False
    
    # Check for obvious non-names (case insensitive)
    non_names = [
        'live', 'teil', 'folge', 'episode', 'special', 'panel', 'discussion',
        'review', 'update', 'news', 'technology', 'software', 'architektur',
        'domain', 'driven', 'design', 'patterns', 'spring', 'java', 'python',
        'conference', 'gathering', 'day', 'oop', 'bed-con', 'innoq'
    ]
    
    name_lower = name.lower()
    for non_name in non_names:
        if non_name in name_lower:
            return False
    
    # Should have at least 2 parts (first + last name)
    parts = name.split()
    if len(parts) < 2:
        return False
    
    # Check if it looks like a person name structure
    # First part should start with capital
    if not parts[0][0].isupper():
        return False
    
    # Last part should also start with capital (last name)
    if not parts[-1][0].isupper():
        return False
    
    return True

def is_valid_guest_name(name):
    """Validiere ob Name ein echter Gast ist"""
    if not name or len(name) < 4:
        return False
    
    # Filter out obvious false positives (more comprehensive)
    false_positives = [
        'Live', 'Special', 'Panel', 'Teil', 'Technology', 'Day', 'Conference',
        'Software Architektur', 'Domain Driven', 'Design Patterns', 'Best Practices',
        'Open Source', 'Cloud Native', 'Spring Boot', 'Single Page', 'HTTP Feeds',
        'Structure', 'Domain', 'Strategic', 'Uncertainty', 'Native', 'Getting Started',
        'Cross-funktionale Teams', 'Crew Ressource', 'Quality Storming', 'Code Charta',
        'Green Software', 'Supply Chain', 'Learning Systems', 'Team Topologie'
    ]
    
    for fp in false_positives:
        if fp.lower() in name.lower():
            return False
    
    # Should contain at least one space (first + last name)
    if ' ' not in name:
        return False
    
    # Should not be too long (probably a topic then)
    if len(name) > 40:
        return False
    
    # Should not contain too many common German words
    german_words = ['mit', 'und', 'der', 'die', 'das', 'für', 'von', 'zu', 'bei']
    name_words = name.lower().split()
    german_count = sum(1 for word in name_words if word in german_words)
    if german_count > len(name_words) // 2:  # More than half are German articles
        return False
    
    return True

def build_guest_database(guest_patterns):
    """Baue strukturierte Gäste-Datenbank auf"""
    guests_db = {}
    
    for guest_name, episodes in guest_patterns.items():
        # Count episodes
        episode_count = len(episodes)
        
        # Get latest episode date
        latest_date = max(ep['date'] for ep in episodes if ep['date'])
        
        # Build episode list
        episode_list = []
        for ep in episodes:
            # Clean title by removing guest name to avoid redundancy
            clean_title = ep['title']
            for guest in ep.get('detected_guests', []):
                clean_title = clean_title.replace(f'mit {guest}', '').replace(f'with {guest}', '')
            clean_title = re.sub(r'\s+', ' ', clean_title).strip()
            clean_title = clean_title.rstrip('-').strip()
            
            episode_entry = {
                'number': int(ep['episode_number']) if ep['episode_number'].isdigit() else 0,
                'title': clean_title,
                'date': ep['date'],
                'video': ep['video_id'],
                'description': ep['description'][:200] + '...' if len(ep['description']) > 200 else ep['description']
            }
            episode_list.append(episode_entry)
        
        # Sort episodes by number (newest first)
        episode_list.sort(key=lambda x: x['number'], reverse=True)
        
        guests_db[guest_name] = {
            'name': guest_name,
            'episode_count': episode_count,
            'bio': "",  # TODO: Bio hinzufügen
            'avatar': f"guests/{guest_name.lower().replace(' ', '_').replace('.', '')}.jpg",
            'linkedin': "",  # TODO: LinkedIn hinzufügen
            'episodes': episode_list
        }
    
    return guests_db

def save_guests_yaml_manual(guests_db, filename='_data/guests_new.yml'):
    """Speichere Gäste-Datenbank als YAML ohne PyYAML"""
    # Create _data directory if it doesn't exist
    os.makedirs('_data', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        # Write header
        f.write("# Gäste von software-architektur.tv\n")
        f.write("# Automatisch generiert mit intelligenter Extraktion\n")
        f.write(f"# Generiert am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Write each guest
        for guest_name in sorted(guests_db.keys()):
            guest_data = guests_db[guest_name]
            
            # Guest name as key
            f.write(f'"{guest_name}":\n')
            f.write(f'  name: "{guest_name}"\n')
            f.write(f'  episode_count: {guest_data["episode_count"]}\n')
            f.write(f'  bio: "{guest_data["bio"]}"\n')
            f.write(f'  avatar: "{guest_data["avatar"]}"\n')
            f.write(f'  linkedin: "{guest_data.get("linkedin", "")}"\n')
            f.write("  episodes:\n")
            
            # Write episodes
            for episode in guest_data["episodes"]:
                f.write(f"    - number: {episode['number']}\n")
                f.write(f'      title: "{episode["title"]}"\n')
                f.write(f'      date: "{episode["date"]}"\n')
                f.write(f'      video: "{episode["video"]}"\n')
                f.write(f'      description: "{episode["description"]}"\n')
            
            f.write("\n")
    
    print(f"✅ Gäste-Datenbank gespeichert: {filename}")

def generate_stats_report(guests_db, episodes):
    """Generiere Statistik-Report"""
    total_episodes = len(episodes)
    episodes_with_guests = len([ep for ep in episodes if 'detected_guests' in ep])
    total_guests = len(guests_db)
    
    # Top guests by episode count
    top_guests = sorted(guests_db.items(), key=lambda x: x[1]['episode_count'], reverse=True)[:15]
    
    print(f"\n📊 STATISTIK-REPORT")
    print(f"=" * 50)
    print(f"📺 Gesamt-Episoden:           {total_episodes}")
    print(f"👥 Episoden mit Gästen:       {episodes_with_guests}")
    print(f"🧑‍💼 Einzigartige Gäste:         {total_guests}")
    print(f"📈 Abdeckung:                 {episodes_with_guests/total_episodes*100:.1f}%")
    
    print(f"\n🏆 TOP 15 GÄSTE:")
    for i, (name, data) in enumerate(top_guests, 1):
        print(f"  {i:2d}. {name:<30} ({data['episode_count']} Episode{'n' if data['episode_count'] > 1 else ''})")

def main():
    """Hauptfunktion"""
    print("🚀 Starte intelligente Gäste-Extraktion...")
    
    # Load all episodes
    print("📁 Lade alle Episoden...")
    episodes = load_all_episodes()
    print(f"✅ {len(episodes)} Episoden geladen")
    
    # Analyze guest patterns
    print("🔍 Analysiere Gast-Patterns...")
    guest_patterns = analyze_guest_patterns(episodes)
    print(f"✅ {len(guest_patterns)} Gäste identifiziert")
    
    # Build database
    print("🏗️  Baue Gäste-Datenbank auf...")
    guests_db = build_guest_database(guest_patterns)
    
    # Save to YAML
    print("💾 Speichere Datenbank...")
    save_guests_yaml_manual(guests_db)
    
    # Generate report
    generate_stats_report(guests_db, episodes)
    
    print(f"\n🎉 Extraktion abgeschlossen!")
    print(f"📄 Neue Datei: _data/guests_new.yml")

if __name__ == "__main__":
    main()
