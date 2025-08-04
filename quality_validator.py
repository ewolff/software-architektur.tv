#!/usr/bin/env python3
"""
Quality Validator für Guest-Datenbank
Bereinigt falsche Einträge wie Konzepte, unvollständige Namen etc.
"""

import re
import os

def load_guests_data(file_path):
    """Lade Gast-Daten aus YAML-Datei"""
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
                guests[current_guest] = {}
            elif current_guest and line.startswith('  '):
                # Guest property
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    value = value.strip().strip('"')
                    guests[current_guest][key] = value
    
    return guests

def is_valid_person_name(name):
    """Prüft ob ein Name ein gültiger Personenname ist"""
    
    # Blacklist von bekannten falschen Einträgen
    false_entries = {
        'Technische Schulden', 'Big Ball', 'Bounded Context', 'Data Mesh',
        'Extreme Programming', 'Funktionale Programmierung', 'Lose Kopplung',
        'Wardley Maps', 'Ask Me', 'Autonome Teams', 'Code Aufr', 'Fighting Agile',
        'Fearless Change', 'DDD When Surrounded by Legacy Systems',
        'Menschen mit Michael Hunger', 'Warum Continuous', 'Statt Agilit',
        'Statt Microservices', 'Technischer Kontext'
    }
    
    if name in false_entries:
        return False, "Blacklisted concept/topic"
    
    # Unvollständige Namen
    incomplete_names = {
        'Als Architekt', 'Lisa Sch', 'Michael Pl', 'Bert Jan',
        'Code Aufr', 'Statt Agilit'
    }
    
    if name in incomplete_names:
        return False, "Incomplete name"
    
    # Zu kurze Namen (weniger als 2 Wörter)
    words = name.split()
    if len(words) < 2:
        return False, "Too few words for person name"
    
    # Namen die wie Konzepte aussehen
    concept_patterns = [
        r'^(Warum|Statt|Fighting|Fearless|Extreme)\s',
        r'(Programming|Schulden|Kopplung|Context|Maps|Teams)$',
        r'^(Data|Big)\s\w+$'
    ]
    
    for pattern in concept_patterns:
        if re.search(pattern, name, re.IGNORECASE):
            return False, f"Matches concept pattern: {pattern}"
    
    # Titel ohne vollständigen Namen
    if name.startswith(('Dr. ', 'Prof. ')) and len(words) < 3:
        return False, "Title without full name"
    
    return True, "Valid person name"

def validate_guests(guests):
    """Validiere alle Gäste und entferne falsche Einträge"""
    valid_guests = {}
    removed_guests = []
    
    for name, data in guests.items():
        is_valid, reason = is_valid_person_name(name)
        
        if is_valid:
            valid_guests[name] = data
        else:
            removed_guests.append((name, reason))
            print(f"❌ Entfernt: {name} - {reason}")
    
    return valid_guests, removed_guests

def save_cleaned_guests(guests, output_file):
    """Speichere bereinigte Gast-Daten"""
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("# Gäste von software-architektur.tv\n")
        file.write("# Bereinigt und validiert\n")
        file.write(f"# Generiert am: {os.popen('date').read().strip()}\n\n")
        
        # Sortiere Gäste alphabetisch
        for name in sorted(guests.keys()):
            data = guests[name]
            file.write(f'"{name}":\n')
            file.write(f'  name: "{name}"\n')
            
            # Schreibe alle anderen Eigenschaften
            for key, value in data.items():
                if key != 'name':  # name bereits geschrieben
                    file.write(f'  {key}: "{value}"\n')
            file.write('\n')

def main():
    print("🧹 Starte Quality-Validation...")
    
    # Lade angereicherte Gast-Daten
    input_file = "_data/guests_enriched.yml"
    output_file = "_data/guests_validated.yml"
    
    if not os.path.exists(input_file):
        print(f"❌ Datei nicht gefunden: {input_file}")
        return
    
    print(f"📁 Lade Gäste-Daten aus {input_file}...")
    guests = load_guests_data(input_file)
    print(f"✅ {len(guests)} Gäste geladen")
    
    print("\n🔍 Validiere Gast-Einträge...")
    valid_guests, removed_guests = validate_guests(guests)
    
    print(f"\n📊 VALIDIERUNGS-STATISTIKEN:")
    print("=" * 40)
    print(f"👥 Original-Gäste:     {len(guests)}")
    print(f"✅ Gültige Gäste:      {len(valid_guests)}")
    print(f"❌ Entfernte Einträge: {len(removed_guests)}")
    print(f"📈 Bereinigungsrate:   {len(removed_guests)/len(guests)*100:.1f}%")
    
    if removed_guests:
        print(f"\n🗑️  ENTFERNTE EINTRÄGE:")
        print("-" * 30)
        for name, reason in removed_guests:
            print(f"  - {name}: {reason}")
    
    print(f"\n💾 Speichere bereinigte Daten...")
    save_cleaned_guests(valid_guests, output_file)
    print(f"✅ Bereinigte Daten gespeichert: {output_file}")
    
    print(f"\n🎉 Quality-Validation abgeschlossen!")
    print(f"📄 Clean file: {output_file}")

if __name__ == "__main__":
    main()