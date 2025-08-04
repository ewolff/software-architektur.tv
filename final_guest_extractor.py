#!/usr/bin/env python3
"""
Final Guest Extractor für software-architektur.tv
Korrekte Episode-Referenzen aus Titeln extrahieren
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

def extract_episode_number(title, filename):
    """Extrahiert Episode-Nummer aus Titel oder Dateiname"""
    
    # Suche in Titel nach "Folge X" oder "Episode X"
    title_match = re.search(r'Folge\s+(\d+)', title, re.IGNORECASE)
    if title_match:
        return int(title_match.group(1))
    
    episode_match = re.search(r'Episode\s+(\d+)', title, re.IGNORECASE)
    if episode_match:
        return int(episode_match.group(1))
    
    # Suche im Dateinamen nach Nummer
    filename_match = re.search(r'folge(\d+)', filename, re.IGNORECASE)
    if filename_match:
        return int(filename_match.group(1))
    
    episode_filename_match = re.search(r'episode(\d+)', filename, re.IGNORECASE)
    if episode_filename_match:
        return int(episode_filename_match.group(1))
    
    # Fallback: Datum-basierte Schätzung (falls kein Pattern gefunden)
    date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', filename)
    if date_match:
        year, month, day = map(int, date_match.groups())
        # Sehr grobe Schätzung basierend auf Start der Serie
        if year >= 2020:
            days_since_start = (year - 2020) * 365 + month * 30 + day
            estimated_episode = max(1, days_since_start // 7)  # Etwa wöchentlich
            return estimated_episode
    
    return 0

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
                title = frontmatter.get('title', '')
                
                # Extrahiere Episode-Nummer
                episode_num = extract_episode_number(title, post_file.name)
                
                # Extract episode info
                episode = {
                    'file': post_file.name,
                    'title': title,
                    'subtitle': frontmatter.get('subtitle', ''),
                    'episode': episode_num,
                    'youtube': frontmatter.get('video', ''),  # video statt youtube
                    'date': frontmatter.get('date', ''),
                    'tags': frontmatter.get('tags', [])
                }
                episodes.append(episode)
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {post_file}: {e}")
    
    return episodes

def extract_guest_from_title(title):
    """Extrahiert Gastnamen aus Episode-Titel"""
    
    # Verschiedene Patterns für Gast-Erkennung
    patterns = [
        r'mit\s+([^-\n]+?)(?:\s*$|\s*-)',  # "mit [Name]" am Ende oder vor -
        r'Interview\s+mit\s+([^-\n]+?)(?:\s*$|\s*-)',
        r'Zu\s+Gast[:\s]+([^-\n]+?)(?:\s*$|\s*-)',
        r'Guest[:\s]+([^-\n]+?)(?:\s*$|\s*-)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, title, re.IGNORECASE)
        if match:
            guest_text = match.group(1).strip()
            
            # Bereinige den Text
            guest_text = re.sub(r'[^\w\säöüÄÖÜß\.\-]', '', guest_text)
            
            # Extrahiere Namen
            names = extract_person_names(guest_text)
            if names:
                return names[0]  # Erster gefundener Name
    
    return None

def extract_person_names(text):
    """Extrahiert Personennamen aus Text"""
    # Split in Wörter
    words = text.split()
    names = []
    
    i = 0
    while i < len(words):
        word = words[i].strip()
        
        if not word or len(word) < 2:
            i += 1
            continue
        
        # Suche nach Namen (Großbuchstabe am Anfang)
        if word[0].isupper() and word.isalpha():
            name_parts = [word]
            
            # Schaue nach weiteren Namen-Teilen
            j = i + 1
            while j < len(words) and j < i + 4:  # Max 4 Wörter
                next_word = words[j].strip()
                if (next_word and len(next_word) > 1 and 
                    next_word[0].isupper() and next_word.isalpha()):
                    name_parts.append(next_word)
                    j += 1
                else:
                    break
            
            # Validiere den Namen
            if len(name_parts) >= 2:  # Mindestens Vor- und Nachname
                full_name = ' '.join(name_parts)
                if is_valid_person_name(full_name):
                    names.append(full_name)
                    i = j
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    
    return names

def is_valid_person_name(name):
    """Validiert ob es sich um einen echten Personennamen handelt"""
    
    # Blacklist von Konzepten
    blacklist = {
        'Software', 'Architektur', 'Development', 'Programming', 'Engineering',
        'Management', 'Testing', 'Security', 'Performance', 'Design', 'Code',
        'System', 'Application', 'Service', 'Framework', 'Library', 'Tool',
        'Microservices', 'DevOps', 'Agile', 'Scrum', 'Kanban', 'Docker',
        'Technische', 'Schulden', 'Context', 'Protocol', 'Model'
    }
    
    # Prüfe auf Blacklist-Begriffe
    if any(blocked.lower() in name.lower() for blocked in blacklist):
        return False
    
    # Mindestens 2 Wörter
    words = name.split()
    if len(words) < 2:
        return False
    
    # Alle Wörter sollten vernünftig lang sein
    if any(len(word) < 2 for word in words):
        return False
    
    return True

def analyze_episodes_for_guests(episodes):
    """Analysiert Episoden und extrahiert Gäste"""
    
    guests_episodes = {}  # guest_name -> [episode_info]
    
    for episode in episodes:
        title = episode['title']
        
        # Extrahiere Gast aus Titel
        guest_name = extract_guest_from_title(title)
        
        if guest_name and is_valid_person_name(guest_name):
            if guest_name not in guests_episodes:
                guests_episodes[guest_name] = []
            
            episode_info = {
                'episode': episode.get('episode', 0),
                'title': episode['title'],
                'file': episode['file'],
                'youtube': episode.get('youtube', ''),
                'date': str(episode.get('date', ''))
            }
            guests_episodes[guest_name].append(episode_info)
    
    return guests_episodes

def save_guests_with_episodes(guests_episodes, output_file):
    """Speichert Gäste mit Episode-Referenzen"""
    
    # LinkedIn Profile für bekannte Gäste
    known_linkedin = {
        'Lisa Schäfer': 'https://linkedin.com/in/lisa-schaefer-coach',
        'Ralf D. Müller': 'https://linkedin.com/in/ralf-d-mueller',
        'Stefan Toth': 'https://linkedin.com/in/stefan-toth-architect',
        'Henning Schwentner': 'https://linkedin.com/in/henning-schwentner',
        'Marco Emrich': 'https://linkedin.com/in/marcoemrich',
        'Michael Plöd': 'https://linkedin.com/in/michael-ploed',
        'Gernot Starke': 'https://linkedin.com/in/gernot-starke',
        'Stefan Zörner': 'https://linkedin.com/in/stefan-zoerner',
        'Nick Tune': 'https://linkedin.com/in/ntcoding',
        'Eberhard Wolff': 'https://linkedin.com/in/eberhardwolff',
        'Jutta Eckstein': 'https://linkedin.com/in/jutta-eckstein',
        'Diana Montalion': 'https://linkedin.com/in/dianamontalion',
        'Hillel Wayne': 'https://linkedin.com/in/hillelwayne',
        'Falk Sippach': 'https://linkedin.com/in/falksippach',
        'Adam Tornhill': 'https://linkedin.com/in/adamtornhill',
        'Alberto Brandolini': 'https://linkedin.com/in/ziobrando',
        'Carola Lilienthal': 'https://linkedin.com/in/carola-lilienthal'
    }
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("# Gäste von software-architektur.tv\n")
        file.write("# Mit korrekten Episode-Referenzen\n")
        file.write(f"# Generiert am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Sortiere Gäste nach Anzahl der Episoden (absteigend)
        sorted_guests = sorted(guests_episodes.items(), key=lambda x: len(x[1]), reverse=True)
        
        for guest_name, episodes in sorted_guests:
            # Sortiere Episoden nach Nummer
            sorted_episodes = sorted(episodes, key=lambda x: x.get('episode', 0))
            
            file.write(f'"{guest_name}":\n')
            file.write(f'  name: "{guest_name}"\n')
            file.write(f'  episode_count: {len(episodes)}\n')
            
            # Avatar und LinkedIn
            safe_name = guest_name.lower().replace(' ', '_').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
            file.write(f'  avatar: "guests/{safe_name}.jpg"\n')
            
            # Bekannte LinkedIn-Profile oder generierte
            linkedin_url = known_linkedin.get(guest_name)
            if not linkedin_url:
                linkedin_name = guest_name.lower().replace(' ', '-').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
                linkedin_url = f"https://linkedin.com/in/{linkedin_name}"
            
            file.write(f'  linkedin: "{linkedin_url}"\n')
            file.write(f'  bio: "Gast der Software-Architektur.tv"\n')
            file.write('  episodes:\n')
            
            for episode in sorted_episodes:
                file.write(f'    - episode: {episode.get("episode", 0)}\n')
                file.write(f'      title: "{episode.get("title", "")}"\n')
                file.write(f'      file: "{episode.get("file", "")}"\n')
                file.write(f'      youtube: "{episode.get("youtube", "")}"\n')
                file.write(f'      date: "{episode.get("date", "")}"\n')
            
            file.write('\n')

def main():
    print("🚀 Starte Final Guest-Extraktion mit korrekten Episode-Referenzen...")
    
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
    
    print(f"\n📊 FINAL STATISTIK-REPORT")
    print("=" * 50)
    print(f"📺 Gesamt-Episoden:           {len(episodes)}")
    print(f"👥 Episoden mit Gästen:       {episodes_with_guests}")
    print(f"🧑‍💼 Einzigartige Gäste:         {total_guests}")
    print(f"🎭 Gesamt-Gastauftritte:      {total_episode_appearances}")
    print(f"📈 Abdeckung:                 {episodes_with_guests/len(episodes)*100:.1f}%")
    
    # Top Gäste mit korrekten Episode-Nummern
    print(f"\n🏆 TOP 10 GÄSTE (mit Episode-Nummern):")
    sorted_guests = sorted(guests_episodes.items(), key=lambda x: len(x[1]), reverse=True)
    for i, (guest, episodes) in enumerate(sorted_guests[:10], 1):
        episode_nums = [str(ep.get('episode', '?')) for ep in sorted(episodes, key=lambda x: x.get('episode', 0))]
        print(f"  {i:2d}. {guest:<30} ({len(episodes)} Episoden: {', '.join(episode_nums)})")
    
    # Speichere Daten
    output_file = "_data/guests_final.yml"
    print(f"\n💾 Speichere finale Datenbank...")
    save_guests_with_episodes(guests_episodes, output_file)
    print(f"✅ Finale Datenbank gespeichert: {output_file}")
    
    print(f"\n🎉 Final Guest-Extraktion abgeschlossen!")
    print(f"📄 Neue Datei: {output_file}")

if __name__ == "__main__":
    main()