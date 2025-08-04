#!/usr/bin/env python3
import re
import os

def clean_guest_name(name):
    """Clean and validate guest name"""
    # Remove common suffixes
    name = re.sub(r'\s*-.*$', '', name)
    name = re.sub(r'\s*\(.*?\)', '', name)
    name = re.sub(r'\s*\[.*?\]', '', name)
    name = re.sub(r'\s*\d+/\d+$', '', name)
    name = re.sub(r'\s*(live|Live).*$', '', name, re.IGNORECASE)
    name = re.sub(r'\s*(vom|von der|von)\s+.*$', '', name, re.IGNORECASE)
    name = name.strip()
    
    # Skip if not a proper name
    if (len(name) < 3 or 
        re.match(r'^\d', name) or
        name.lower() in ['live', 'dem', 'der', 'die', 'das', 'ein', 'eine', 'vom', 'von']):
        return None
        
    return name

def extract_guests_from_title(title):
    """Extract all guest names from a title"""
    # Remove file prefix and quotes
    title = re.sub(r'^[^:]+:', '', title).strip(' "')
    
    print(f"Processing: {title}")
    
    # Look for pattern "mit [guest names]"
    mit_pattern = r'\bmit\s+([^-]+?)(?:\s*-|$)'
    match = re.search(mit_pattern, title, re.IGNORECASE)
    
    if not match:
        print(f"  No 'mit' pattern found")
        return []
    
    guest_part = match.group(1).strip()
    print(f"  Raw guest part: '{guest_part}'")
    
    # Split on common separators
    separators = [' und ', ' & ', ', ', ' with ']
    guests = [guest_part]
    
    for sep in separators:
        new_guests = []
        for guest in guests:
            if sep in guest:
                parts = [p.strip() for p in guest.split(sep)]
                new_guests.extend(parts)
            else:
                new_guests.append(guest)
        guests = new_guests
    
    # Clean each guest name
    cleaned_guests = []
    for guest in guests:
        cleaned = clean_guest_name(guest)
        if cleaned and cleaned not in cleaned_guests:
            cleaned_guests.append(cleaned)
    
    print(f"  Cleaned guests: {cleaned_guests}")
    return cleaned_guests

# Read all guest episode titles
all_guests = {}

with open('all_guest_titles.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Processing {len(lines)} guest episodes...\n")

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Extract filename for date
    filename_match = re.match(r'([^:]+):', line)
    if filename_match:
        filename = filename_match.group(1)
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
        episode_date = date_match.group(1) if date_match else None
    else:
        episode_date = None
    
    # Extract title
    title = re.sub(r'^[^:]+:', '', line).strip()
    title = title.strip(' "')
    
    # Extract episode number
    episode_match = re.search(r'Folge\s+(\d+)', title)
    episode_num = episode_match.group(1) if episode_match else None
    
    # Extract guests
    guests = extract_guests_from_title(line)
    
    # Add to collection
    for guest in guests:
        if guest not in all_guests:
            all_guests[guest] = []
        
        all_guests[guest].append({
            'title': title,
            'date': episode_date,
            'episode': episode_num,
            'filename': filename.split('/')[-1] if '/' in filename else filename
        })
    
    print()  # Empty line for readability

# Sort and display results
print(f"\n\n{'='*60}")
print(f"COMPLETE GUEST EXTRACTION RESULTS")
print(f"Found {len(all_guests)} unique guests from {len(lines)} episodes")
print(f"{'='*60}")

# Save detailed results
with open('complete_guest_list.txt', 'w', encoding='utf-8') as f:
    f.write(f"COMPLETE GUEST LIST - {len(all_guests)} UNIQUE GUESTS\n")
    f.write(f"Extracted from {len(lines)} episodes with guests\n\n")
    
    for guest_name in sorted(all_guests.keys()):
        episodes = all_guests[guest_name]
        f.write(f"{guest_name} ({len(episodes)} episode{'s' if len(episodes) > 1 else ''}):\n")
        
        for ep in episodes:
            f.write(f"  - Episode {ep['episode']}: {ep['title']} ({ep['date']})\n")
        f.write(f"\n")
    
    # Summary statistics
    f.write(f"\nSTATISTICS:\n")
    f.write(f"Total unique guests: {len(all_guests)}\n")
    f.write(f"Total guest episodes: {len(lines)}\n")
    
    # Count multiple appearances
    multiple_appearances = [(name, len(episodes)) for name, episodes in all_guests.items() if len(episodes) > 1]
    multiple_appearances.sort(key=lambda x: x[1], reverse=True)
    
    f.write(f"Guests with multiple appearances: {len(multiple_appearances)}\n")
    f.write(f"\nTop guests by episode count:\n")
    for name, count in multiple_appearances[:10]:
        f.write(f"  {name}: {count} episodes\n")

print(f"Detailed results saved to complete_guest_list.txt")

# Quick summary to console
print(f"\nTOP 20 GUESTS:")
guest_counts = [(name, len(episodes)) for name, episodes in all_guests.items()]
guest_counts.sort(key=lambda x: x[1], reverse=True)

for i, (name, count) in enumerate(guest_counts[:20]):
    print(f"{i+1:2d}. {name} ({count} episode{'s' if count > 1 else ''})")

print(f"\n... and {len(all_guests) - 20} more guests")
