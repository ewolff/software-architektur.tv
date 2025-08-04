#!/usr/bin/env python3
import os
import re

def extract_guests_from_title(title):
    """Extract guest names from various title patterns"""
    guests = []
    
    # German pattern: "mit [Name]"
    german_match = re.search(r'\bmit\s+([^-]+?)(?:\s*-|$)', title, re.IGNORECASE)
    if german_match:
        guest_part = german_match.group(1).strip()
        guests.extend(parse_guest_names(guest_part))
    
    # English patterns: "with [Name]", "about ... with [Name]"
    english_match = re.search(r'\bwith\s+([^-]+?)(?:\s*-|$)', title, re.IGNORECASE)
    if english_match:
        guest_part = english_match.group(1).strip()
        guests.extend(parse_guest_names(guest_part))
    
    # Pattern: "Name - Topic" (common in English episodes)
    if not guests and ' - ' in title and not title.startswith('Folge'):
        # Look for pattern like "Episode 123 - Name - Topic" or "Name - Topic"
        parts = title.split(' - ')
        if len(parts) >= 2:
            # Try the first part after episode number
            name_part = parts[0] if not parts[0].startswith('Episode') else (parts[1] if len(parts) > 1 else '')
            if name_part:
                name_part = re.sub(r'^Episode\s+\d+\s*-?\s*', '', name_part).strip()
                if is_likely_person_name(name_part):
                    guests.append(name_part)
    
    return list(dict.fromkeys(guests))  # Remove duplicates

def parse_guest_names(guest_part):
    """Parse multiple guest names from a string"""
    # Handle separators
    separators = [' und ', ' and ', ' & ', ', ', ' with ']
    guest_list = [guest_part]
    
    for sep in separators:
        new_list = []
        for g in guest_list:
            if sep in g:
                new_list.extend([x.strip() for x in g.split(sep)])
            else:
                new_list.append(g)
        guest_list = new_list
    
    # Clean each name
    cleaned_guests = []
    for guest in guest_list:
        cleaned = clean_guest_name(guest)
        if cleaned and is_likely_person_name(cleaned):
            cleaned_guests.append(cleaned)
    
    return cleaned_guests

def clean_guest_name(name):
    """Clean and validate guest name"""
    # Remove common suffixes and patterns
    name = re.sub(r'\s*-.*$', '', name)
    name = re.sub(r'\s*\(.*?\)', '', name)
    name = re.sub(r'\s*\[.*?\]', '', name)
    name = re.sub(r'\s*\d+/\d+$', '', name)
    name = re.sub(r'\s*(live|Live).*$', '', name, re.IGNORECASE)
    name = re.sub(r'\s*(vom|von der|von)\s+.*$', '', name, re.IGNORECASE)
    name = name.strip()
    
    return name if len(name) > 2 else None

def is_likely_person_name(name):
    """Check if string looks like a person name"""
    if not name or len(name) < 3:
        return False
    
    # Skip obvious non-names
    non_names = {
        'live', 'special', 'oop', 'conference', 'gathering', 'technology', 'day',
        'code', 'domain', 'spring', 'java', 'api', 'http', 'dsl', 'ai', 'ki',
        'software', 'architecture', 'architektur', 'development', 'test', 'testing',
        'agile', 'scrum', 'devops', 'cloud', 'microservices', 'frontend', 'backend'
    }
    
    if name.lower() in non_names:
        return False
    
    # Should have at least one space (first + last name)
    if ' ' not in name:
        return False
    
    # Should have capital letters (proper names)
    if not re.search(r'[A-Z]', name):
        return False
    
    # Should not start with numbers
    if re.match(r'^\d', name):
        return False
    
    return True

def identify_moderators(title):
    """Identify moderators in episodes without clear guests"""
    moderators = []
    
    # Look for co-host patterns
    if 'Lisa Schäfer' in title and 'mit Lisa Schäfer' not in title.lower():
        moderators.append('Lisa Schäfer')
    
    if 'Ralf' in title and 'mit Ralf' not in title.lower() and 'Ralf D. Müller' not in title:
        moderators.append('Ralf D. Müller')
    
    # Eberhard is usually the default host when not mentioned
    if not moderators and not any(pattern in title.lower() for pattern in ['mit ', 'with ']):
        moderators.append('Eberhard Wolff')
    
    return moderators

# Analyze all episodes
all_guests = {}
all_moderators = {}
episode_count = 0

print("Analyzing all 272 episodes for guests and moderators...")

for filename in sorted(os.listdir('_posts')):
    if filename.endswith('.md'):
        filepath = os.path.join('_posts', filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'^title:\s*"?([^"\n]*)"?', content, re.MULTILINE)
            if not title_match:
                continue
                
            title = title_match.group(1).strip('"')
            
            # Extract date and episode number
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
            episode_date = date_match.group(1) if date_match else None
            
            episode_match = re.search(r'(Folge|Episode)\s+(\d+)', title)
            episode_num = episode_match.group(2) if episode_match else None
            
            episode_count += 1
            
            # Extract guests
            guests = extract_guests_from_title(title)
            
            if guests:
                print(f"Episode {episode_num}: {title}")
                print(f"  -> Guests: {guests}")
                
                for guest in guests:
                    if guest not in all_guests:
                        all_guests[guest] = []
                    
                    all_guests[guest].append({
                        'episode': episode_num,
                        'title': title,
                        'date': episode_date,
                        'filename': filename
                    })
            else:
                # No clear guests - identify moderators
                moderators = identify_moderators(title)
                for mod in moderators:
                    if mod not in all_moderators:
                        all_moderators[mod] = []
                    
                    all_moderators[mod].append({
                        'episode': episode_num,
                        'title': title,
                        'date': episode_date,
                        'filename': filename
                    })
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"\n📊 COMPLETE ANALYSIS RESULTS:")
print(f"Total episodes processed: {episode_count}")
print(f"Unique guests found: {len(all_guests)}")
print(f"Moderators identified: {len(all_moderators)}")

# Show top guests
guest_counts = [(name, len(episodes)) for name, episodes in all_guests.items()]
guest_counts.sort(key=lambda x: x[1], reverse=True)

print(f"\n🏆 TOP 20 GUESTS:")
for i, (name, count) in enumerate(guest_counts[:20]):
    print(f"{i+1:2d}. {name}: {count} episodes")

# Show moderator statistics  
print(f"\n🎙️ MODERATOR STATISTICS:")
for mod, episodes in all_moderators.items():
    print(f"{mod}: {len(episodes)} episodes")

# Save complete results
with open('complete_guests_and_moderators.txt', 'w', encoding='utf-8') as f:
    f.write(f"COMPLETE GUESTS AND MODERATORS ANALYSIS\n")
    f.write(f"=====================================\n\n")
    f.write(f"Total episodes: {episode_count}\n")
    f.write(f"Unique guests: {len(all_guests)}\n")
    f.write(f"Moderators: {len(all_moderators)}\n\n")
    
    f.write(f"ALL GUESTS:\n")
    f.write(f"===========\n\n")
    for guest_name in sorted(all_guests.keys()):
        episodes = all_guests[guest_name]
        f.write(f"{guest_name} ({len(episodes)} episodes):\n")
        for ep in episodes:
            f.write(f"  - Episode {ep['episode']}: {ep['title']} ({ep['date']})\n")
        f.write(f"\n")
    
    f.write(f"MODERATORS:\n")
    f.write(f"===========\n\n")
    for mod_name in sorted(all_moderators.keys()):
        episodes = all_moderators[mod_name][:10]  # Limit Eberhard's list
        f.write(f"{mod_name} ({len(all_moderators[mod_name])} episodes - showing first 10):\n")
        for ep in episodes:
            f.write(f"  - Episode {ep['episode']}: {ep['title']} ({ep['date']})\n")
        if len(all_moderators[mod_name]) > 10:
            f.write(f"  ... and {len(all_moderators[mod_name]) - 10} more episodes\n")
        f.write(f"\n")

print(f"\nComplete analysis saved to complete_guests_and_moderators.txt")

