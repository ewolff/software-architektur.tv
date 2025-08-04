#!/usr/bin/env python3
import os
import re

def extract_guest_from_title(title):
    """Extract guest name(s) from episode title"""
    # Remove quotes
    title = title.strip('"')
    
    # Look for "mit" pattern - be more precise
    patterns = [
        r'\bmit\s+([A-ZÄÖÜ][a-zäöüß]+(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*)',  # Names
        r'\bmit\s+([A-Za-zÄÖÜäöüß]+(?:\s+[A-Za-zÄÖÜäöüß]+)+)',  # Multiple words
    ]
    
    guests = []
    for pattern in patterns:
        matches = re.findall(pattern, title)
        for match in matches:
            # Clean up the match
            guest = match.strip()
            
            # Split on common separators
            separators = [' und ', ' & ', ', ']
            guest_list = [guest]
            
            for sep in separators:
                new_list = []
                for g in guest_list:
                    if sep in g:
                        new_list.extend([x.strip() for x in g.split(sep)])
                    else:
                        new_list.append(g)
                guest_list = new_list
            
            for g in guest_list:
                # Remove suffixes
                g = re.sub(r'\s*-.*$', '', g)
                g = re.sub(r'\s*\(.*?\)', '', g)
                g = re.sub(r'\s*\d+/\d+$', '', g)
                g = re.sub(r'\s*(live|Live).*$', '', g)
                g = g.strip()
                
                # Validate - should be a proper name
                if (len(g) > 3 and 
                    not g.lower() in ['live', 'dem', 'der', 'die', 'das'] and
                    not re.match(r'^\d', g) and
                    ' ' in g):  # Names should have at least firstname lastname
                    guests.append(g)
    
    return guests

# Get all episode files with "mit"
print("Finding all episodes with guests...")
guest_episodes = []

for filename in sorted(os.listdir('_posts')):
    if filename.endswith('.md'):
        filepath = os.path.join('_posts', filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'^title:\s*"([^"]*)"', content, re.MULTILINE)
            if not title_match:
                continue
                
            title = title_match.group(1)
            
            # Check if this episode has guests
            if 'mit ' in title.lower():
                guest_episodes.append((filename, title))
                
        except Exception as e:
            continue

print(f"Found {len(guest_episodes)} episodes with 'mit' in title")

# Extract all guests
all_guests = {}

for filename, title in guest_episodes:
    print(f"\nProcessing: {title}")
    
    guests = extract_guest_from_title(title)
    print(f"Extracted guests: {guests}")
    
    # Add to collection
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    episode_date = date_match.group(1) if date_match else None
    
    episode_match = re.search(r'Folge\s+(\d+)', title)
    episode_num = episode_match.group(1) if episode_match else None
    
    for guest in guests:
        if guest not in all_guests:
            all_guests[guest] = []
        
        all_guests[guest].append({
            'title': title,
            'date': episode_date,
            'episode': episode_num,
            'filename': filename
        })

# Print results
print(f"\n\n=== EXTRACTED {len(all_guests)} UNIQUE GUESTS ===")
for guest_name in sorted(all_guests.keys()):
    episodes = all_guests[guest_name]
    print(f"\n{guest_name} ({len(episodes)} episode{'s' if len(episodes) > 1 else ''}):")
    for ep in episodes:
        print(f"  - {ep['title']} ({ep['date']})")

# Also manually parse some tricky cases
print("\n\n=== MANUAL REVIEW OF TRICKY CASES ===")
manual_cases = []
for filename, title in guest_episodes:
    guests = extract_guest_from_title(title)
    if not guests:
        manual_cases.append((filename, title))

if manual_cases:
    print(f"Found {len(manual_cases)} episodes that need manual review:")
    for filename, title in manual_cases[:10]:  # Show first 10
        print(f"  {title}")
    
    if len(manual_cases) > 10:
        print(f"  ... and {len(manual_cases) - 10} more")

