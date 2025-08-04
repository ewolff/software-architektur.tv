#!/usr/bin/env python3
"""
Enhanced Guest Extractor für software-architektur.tv
Erstellt Gäste-Datenbank mit Episode-Referenzen ohne PyYAML
"""

import os
import re
from datetime import datetime
from pathlib import Path

def parse_yaml_frontmatter(content):
    """Manuelles YAML-Parsing für Frontmatter"""
    if not content.startswith('---'):
        return {}
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}
    
    yaml_content = parts[1].strip()
    data = {}
    
    for line in yaml_content.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            
            # Handle numbers
            if value.isdigit():
                data[key] = int(value)
            elif value.lower() in ['true', 'false']:
                data[key] = value.lower() == 'true'
            else:
                data[key] = value
    
    return data

def load_episodes():
    """Lade alle Episoden aus den Post-Dateien"""
    episodes = []
    posts_dir = Path("_posts")
    
    for post_file in sorted(posts_dir.glob("*.md")):
        if post_file.name == "template.md":
            continue
            
        try:
            with open(post_file, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Parse YAML frontmatter
                frontmatter = parse_yaml_frontmatter(content)
                
                # Extract episode info
                episode = {
                    'file': post_file.name,
                    'title': frontmatter.get('title', ''),
                    'subtitle': frontmatter.get('subtitle', ''),
                    'episode': frontmatter.get('episode', 0),
                    'youtube': frontmatter.get('youtube', ''),
                    'date': frontmatter.get('date', ''),
                    'tags': frontmatter.get('tags', [])
                }
                episodes.append(episode)
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {post_file}: {e}")
    
    return episodes

def extract_names_from_text(text):
    """Extrahiert Personennamen aus Text"""
    # Bereinige Text
    text = re.sub(r'[^\w\säöüÄÖÜß\-\.]', ' ', text)
    
    # Suche nach Namen-Patterns
    words = text.split()
    names = []
    
    i = 0
    while i < len(words):
        word = words[i].strip()
        
        # Skip unwanted patterns
        if not word or len(word) < 2:
            i += 1
            continue
            
        # Look for name patterns (Capitalized words)
        if word[0].isupper() and len(word) > 1:
            name_parts = [word]
            
            # Check following words for compound names
            j = i + 1
            while j < len(words) and j < i + 4:  # Max 4 words for name
                next_word = words[j].strip()
                if (next_word and len(next_word) > 1 and 
                    (next_word[0].isupper() or next_word.lower() in ['von', 'van', 'de', 'da'])):
                    name_parts.append(next_word)
                    j += 1
                else:
                    break
            
            if len(name_parts) >= 2 or (len(name_parts) == 1 and len(name_parts[0]) > 3):
                full_name = ' '.join(name_parts)
                if is_likely_person_name(full_name):
                    names.append(full_name)
                    i = j
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    
    return list(set(names))

def is_likely_person_name(name):
    """Prüft ob ein String wahrscheinlich ein Personenname ist"""
    
    # Blacklist von bekannten falschen Begriffen
    blacklist = {
        'Software', 'Architektur', 'Development', 'Programming', 'Engineering',
        'Management', 'Testing', 'Security', 'Performance', 'Design', 'Code',
        'System', 'Application', 'Service', 'Framework', 'Library', 'Tool',
        'Microservices', 'DevOps', 'Agile', 'Scrum', 'Kanban', 'Docker',
        'Kubernetes', 'Cloud', 'AWS', 'Azure', 'Google', 'Tech', 'IT'
    }
    
    if any(word in name for word in blacklist):
        return False
    
    # Muss mindestens 2 Wörter haben oder sehr lang sein
    words = name.split()
    if len(words) < 2 and len(name) < 8:
        return False
    
    # Prüfe auf typische Namensmuster
    has_typical_name_pattern = any(
        word[0].isupper() and len(word) > 1 and word.isalpha()
        for word in words
    )
    
    return has_typical_name_pattern

def is_valid_guest_name(name):
    """Erweiterte Validierung für Gastnamen"""
    
    # Blacklist von Konzepten und falschen Einträgen
    blacklist = {
        'Technische Schulden', 'Big Ball', 'Bounded Context', 'Data Mesh',
        'Extreme Programming', 'Funktionale Programmierung', 'Lose Kopplung',
        'Wardley Maps', 'Ask Me', 'Autonome Teams', 'Fighting Agile',
        'Fearless Change', 'DDD When', 'Menschen mit', 'Warum Continuous',
        'Statt Agilit', 'Statt Microservices', 'Technischer Kontext',
        'The Architecture'
    }
    
    if any(blocked in name for blocked in blacklist):
        return False
    
    # Unvollständige Namen
    if name in ['Als Architekt', 'Lisa Sch', 'Michael Pl', 'Bert Jan', 'Code Aufr']:
        return False
    
    # Muss echte Personennamen-Struktur haben
    words = name.split()
    if len(words) < 2:
        return False
    
    # Alle Wörter sollten mit Großbuchstaben beginnen
    if not all(word[0].isupper() for word in words if len(word) > 1):
        return False
    
    return True

def analyze_episodes_for_guests(episodes):
    """Analysiert Episoden und extrahiert Gäste mit Episode-Referenzen"""
    
    guests_episodes = {}  # guest_name -> [episode_info]
    
    for episode in episodes:
        title = episode['title']
        subtitle = episode.get('subtitle', '')
        combined_text = f"{title} {subtitle}"
        
        # Pattern für Gast-Erkennung
        guest_indicators = [
            r'mit\s+([^-\n,]+?)(?:\s*[-,]|$)',
            r'Gast[:\s]+([^-\n,]+?)(?:\s*[-,]|$)',
            r'Interview\s+mit\s+([^-\n,]+?)(?:\s*[-,]|$)',
            r'zu\s+Gast[:\s]+([^-\n,]+?)(?:\s*[-,]|$)'
        ]
        
        found_guests = []
        
        for pattern in guest_indicators:
            matches = re.findall(pattern, combined_text, re.IGNORECASE)
            for match in matches:
                names = extract_names_from_text(match.strip())
                found_guests.extend(names)
        
        # Entferne Duplikate und validiere
        valid_guests = []
        for guest in set(found_guests):
            if is_valid_guest_name(guest):
                valid_guests.append(guest)
        
        # Speichere Episode-Gast-Referenzen
        for guest in valid_guests:
            if guest not in guests_episodes:
                guests_episodes[guest] = []
            
            episode_info = {
                'episode': episode.get('episode', 0),
                'title': episode['title'],
                'file': episode['file'],
                'youtube': episode.get('youtube', ''),
                'date': str(episode.get('date', ''))
            }
            guests_episodes[guest].append(episode_info)
    
    return guests_episodes

def save_guests_with_episodes(guests_episodes, output_file):
    """Speichert Gäste mit Episode-Referenzen als YAML"""
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("# Gäste von software-architektur.tv\n")
        file.write("# Mit Episode-Referenzen und Avatar-Links\n")
        file.write(f"# Generiert am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Sortiere Gäste nach Anzahl der Episoden (absteigend)
        sorted_guests = sorted(guests_episodes.items(), key=lambda x: len(x[1]), reverse=True)
        
        for guest_name, episodes in sorted_guests:
            # Sortiere Episoden nach Nummer
            sorted_episodes = sorted(episodes, key=lambda x: x.get('episode', 0))
            
            file.write(f'"{guest_name}":\n')
            file.write(f'  name: "{guest_name}"\n')
            file.write(f'  episode_count: {len(episodes)}\n')
            
            # Avatar und LinkedIn generieren
            safe_name = guest_name.lower().replace(' ', '_').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
            file.write(f'  avatar: "guests/{safe_name}.jpg"\n')
            
            linkedin_name = guest_name.lower().replace(' ', '-').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
            file.write(f'  linkedin: "https://linkedin.com/in/{linkedin_name}"\n')
            file.write(f'  bio: ""\n')
            file.write('  episodes:\n')
            
            for episode in sorted_episodes:
                file.write(f'    - episode: {episode.get("episode", 0)}\n')
                file.write(f'      title: "{episode.get("title", "")}"\n')
                file.write(f'      file: "{episode.get("file", "")}"\n')
                file.write(f'      youtube: "{episode.get("youtube", "")}"\n')
                file.write(f'      date: "{episode.get("date", "")}"\n')
            
            file.write('\n')

def main():
    print("🚀 Starte Enhanced Guest-Extraktion mit Episode-Referenzen...")
    
    # Lade alle Episoden
    print("📁 Lade alle Episoden...")
    episodes = load_episodes()
    print(f"✅ {len(episodes)} Episoden geladen")
    
    # Analysiere Gäste
    print("🔍 Analysiere Episoden für Gäste...")
    guests_episodes = analyze_episodes_for_guests(episodes)
    
    # Statistiken
    total_guests = len(guests_episodes)
    total_episode_appearances = sum(len(eps) for eps in guests_episodes.values())
    episodes_with_guests = len(set(ep['file'] for eps in guests_episodes.values() for ep in eps))
    
    print(f"\n📊 ENHANCED STATISTIK-REPORT")
    print("=" * 50)
    print(f"📺 Gesamt-Episoden:           {len(episodes)}")
    print(f"👥 Episoden mit Gästen:       {episodes_with_guests}")
    print(f"🧑‍💼 Einzigartige Gäste:         {total_guests}")
    print(f"🎭 Gesamt-Gastauftritte:      {total_episode_appearances}")
    print(f"📈 Abdeckung:                 {episodes_with_guests/len(episodes)*100:.1f}%")
    
    # Top Gäste
    print(f"\n🏆 TOP 10 GÄSTE (nach Episodenanzahl):")
    sorted_guests = sorted(guests_episodes.items(), key=lambda x: len(x[1]), reverse=True)
    for i, (guest, episodes) in enumerate(sorted_guests[:10], 1):
        episode_nums = [str(ep.get('episode', '?')) for ep in episodes]
        print(f"  {i:2d}. {guest:<30} ({len(episodes)} Episoden: {', '.join(episode_nums)})")
    
    # Speichere Daten
    output_file = "_data/guests_with_episodes.yml"
    print(f"\n💾 Speichere erweiterte Datenbank...")
    save_guests_with_episodes(guests_episodes, output_file)
    print(f"✅ Erweiterte Datenbank gespeichert: {output_file}")
    
    print(f"\n🎉 Enhanced Guest-Extraktion abgeschlossen!")
    print(f"📄 Neue Datei: {output_file}")

if __name__ == "__main__":
    main()