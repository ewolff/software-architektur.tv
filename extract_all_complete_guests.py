#!/usr/bin/env python3
import os
import re
from datetime import datetime

def extract_guest_from_title(title):
    """Extract guest name(s) from episode title"""
    # Remove quotes and title prefix
    title = title.replace('title: "', '').replace('"', '').strip()
    
    # Look for "mit" pattern
    mit_match = re.search(r'\bmit\s+([^-]+?)(?:\s*-|$)', title, re.IGNORECASE)
    if not mit_match:
        return []
    
    guest_part = mit_match.group(1).strip()
    
    # Handle multiple guests separated by various delimiters
    separators = [' und ', ' & ', ', ', ' with ', ' + ']
    guests = [guest_part]
    
    for sep in separators:
        new_guests = []
        for guest in guests:
            if sep in guest:
                new_guests.extend([g.strip() for g in guest.split(sep)])
            else:
                new_guests.append(guest)
        guests = new_guests
    
    # Clean up each guest name
    cleaned_guests = []
    for guest in guests:
        # Remove common suffixes and patterns
        guest = re.sub(r'\s*\([^)]*\)', '', guest)  # Remove parentheses
        guest = re.sub(r'\s*\[[^\]]*\]', '', guest)  # Remove brackets
        guest = re.sub(r'\s*-.*$', '', guest)  # Remove everything after dash
        guest = re.sub(r'\s*\d+/\d+$', '', guest)  # Remove part numbers like "1/2"
        guest = re.sub(r'\s*(live|Live).*$', '', guest)  # Remove "live" suffixes
        guest = guest.strip()
        
        # Skip if too short, contains numbers, or common non-names
        if (len(guest) > 2 and 
            not re.match(r'^\d', guest) and 
            guest not in ['live', 'Live', 'dem', 'der', 'die', 'das', 'ein', 'eine']):
            cleaned_guests.append(guest)
    
    return cleaned_guests

def extract_episode_date(filename):
    """Extract date from filename"""
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        return date_match.group(1)
    return None

def extract_episode_number(content):
    """Extract episode number from content"""
    episode_match = re.search(r'Folge\s+(\d+)', content, re.IGNORECASE)
    if episode_match:
        return episode_match.group(1)
    return None

# Process all episode files
all_guests = {}
episode_files = []

for filename in os.listdir('_posts'):
    if filename.endswith('.md'):
        episode_files.append(filename)

episode_files.sort()

print(f"Processing {len(episode_files)} episode files...")

for filename in episode_files:
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
        if 'mit ' not in title.lower():
            continue
            
        guests = extract_guest_from_title(title)
        if not guests:
            continue
            
        episode_date = extract_episode_date(filename)
        episode_number = extract_episode_number(title)
        
        print(f"File: {filename}")
        print(f"Title: {title}")
        print(f"Guests: {guests}")
        print(f"Date: {episode_date}")
        print(f"Episode: {episode_number}")
        print("---")
        
        # Add to all_guests dictionary
        for guest in guests:
            if guest not in all_guests:
                all_guests[guest] = {
                    'name': guest,
                    'episodes': []
                }
            
            all_guests[guest]['episodes'].append({
                'title': title,
                'date': episode_date,
                'episode_number': episode_number,
                'filename': filename
            })
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        continue

print(f"\n\nFOUND {len(all_guests)} UNIQUE GUESTS:")
for guest_name in sorted(all_guests.keys()):
    episode_count = len(all_guests[guest_name]['episodes'])
    print(f"  {guest_name} ({episode_count} episode{'s' if episode_count > 1 else ''})")

# Save to file for review
with open('all_extracted_guests.txt', 'w', encoding='utf-8') as f:
    f.write(f"COMPLETE GUEST EXTRACTION RESULTS\n")
    f.write(f"Found {len(all_guests)} unique guests\n\n")
    
    for guest_name in sorted(all_guests.keys()):
        guest_data = all_guests[guest_name]
        f.write(f"{guest_name}:\n")
        for episode in guest_data['episodes']:
            f.write(f"  - {episode['title']} ({episode['date']})\n")
        f.write(f"\n")

print(f"\nSaved complete results to all_extracted_guests.txt")
