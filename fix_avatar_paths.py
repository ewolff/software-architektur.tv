#!/usr/bin/env python3
"""
Korrigiert Avatar-Pfade in guests.yml auf SVG-Dateien
"""

import os
from pathlib import Path

def fix_avatar_paths():
    """Korrigiert Avatar-Pfade in guests.yml"""
    
    guests_file = "_data/guests.yml"
    if not os.path.exists(guests_file):
        print(f"❌ Datei nicht gefunden: {guests_file}")
        return
    
    # Lese Original-Datei
    with open(guests_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ersetze .jpg mit .svg in Avatar-Pfaden
    corrected_content = content.replace('guests/', 'guests/').replace('.jpg', '.svg')
    
    # Schreibe korrigierte Datei
    with open(guests_file, 'w', encoding='utf-8') as f:
        f.write(corrected_content)
    
    print("✅ Avatar-Pfade auf SVG korrigiert")

def main():
    print("🔧 Korrigiere Avatar-Pfade...")
    fix_avatar_paths()
    print("🎉 Korrektur abgeschlossen!")

if __name__ == "__main__":
    main()