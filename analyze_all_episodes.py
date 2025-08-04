#!/usr/bin/env python3
import os
import re

def extract_episode_info(filepath):
    """Extract episode information from file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^title:\s*"?([^"\n]*)"?', content, re.MULTILINE)
    title = title_match.group(1).strip('"') if title_match else "Unknown"
    
    # Extract date from filename
    filename = os.path.basename(filepath)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    date = date_match.group(1) if date_match else "Unknown"
    
    # Extract episode number
    episode_match = re.search(r'Folge\s+(\d+)', title)
    episode_num = int(episode_match.group(1)) if episode_match else 0
    
    return {
        'filename': filename,
        'title': title,
        'date': date,
        'episode_num': episode_num,
        'has_guest': 'mit ' in title.lower()
    }

# Analyze all episodes
all_episodes = []
guest_episodes = []
non_guest_episodes = []

print("Analyzing all episodes...")

for filename in os.listdir('_posts'):
    if filename.endswith('.md'):
        filepath = os.path.join('_posts', filename)
        
        try:
            episode_info = extract_episode_info(filepath)
            all_episodes.append(episode_info)
            
            if episode_info['has_guest']:
                guest_episodes.append(episode_info)
            else:
                non_guest_episodes.append(episode_info)
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Sort by episode number
all_episodes.sort(key=lambda x: x['episode_num'])
guest_episodes.sort(key=lambda x: x['episode_num'])
non_guest_episodes.sort(key=lambda x: x['episode_num'])

print(f"\n📊 EPISODE STATISTICS:")
print(f"Total episodes: {len(all_episodes)}")
print(f"Episodes with guests ('mit'): {len(guest_episodes)}")  
print(f"Episodes without 'mit': {len(non_guest_episodes)}")

# Analyze non-guest episodes for moderators/hosts
moderators = {}

print(f"\n🎙️ ANALYZING NON-GUEST EPISODES:")
print("Looking for moderators in episode titles...")

for episode in non_guest_episodes[:20]:  # Show first 20
    title = episode['title']
    
    # Look for moderator patterns
    moderator_mentions = []
    
    # Common moderator patterns
    if 'Eberhard' in title:
        moderator_mentions.append('Eberhard Wolff')
    if 'Lisa' in title and 'mit Lisa' not in title.lower():
        moderator_mentions.append('Lisa Schäfer')
    if 'Ralf' in title and 'mit Ralf' not in title.lower():
        moderator_mentions.append('Ralf D. Müller')
    
    # Special patterns for multi-host episodes
    if ' und ' in title and 'mit' not in title.lower():
        # This might be a multi-host episode
        moderator_mentions.append('Multi-Host')
    
    print(f"Episode {episode['episode_num']:3d}: {title}")
    if moderator_mentions:
        print(f"     -> Detected: {', '.join(moderator_mentions)}")
    else:
        print(f"     -> Solo/Standard episode")
    
    # Count moderators
    for mod in moderator_mentions:
        if mod not in moderators:
            moderators[mod] = []
        moderators[mod].append(episode)

print(f"\n... (showing first 20 of {len(non_guest_episodes)} non-guest episodes)")

# Show moderator statistics
print(f"\n🎭 MODERATOR STATISTICS (from sample):")
for mod, episodes in moderators.items():
    print(f"{mod}: {len(episodes)} episodes")

# Look for specific patterns in all non-guest episodes
eberhard_solo = []
multi_host = []
special_episodes = []

for episode in non_guest_episodes:
    title = episode['title']
    
    if ('Eberhard' not in title and 'Lisa' not in title and 'Ralf' not in title and 
        'und' not in title and 'Special' not in title):
        eberhard_solo.append(episode)
    elif 'und' in title or 'Special' in title:
        special_episodes.append(episode)

print(f"\n📈 DETAILED BREAKDOWN:")
print(f"Likely Eberhard solo episodes: {len(eberhard_solo)}")
print(f"Special/Multi-host episodes: {len(special_episodes)}")
print(f"Other episodes: {len(non_guest_episodes) - len(eberhard_solo) - len(special_episodes)}")

# Save detailed analysis
with open('all_episodes_analysis.txt', 'w', encoding='utf-8') as f:
    f.write(f"COMPLETE EPISODE ANALYSIS\n")
    f.write(f"========================\n\n")
    f.write(f"Total episodes: {len(all_episodes)}\n")
    f.write(f"Episodes with guests: {len(guest_episodes)}\n")
    f.write(f"Episodes without guests: {len(non_guest_episodes)}\n\n")
    
    f.write(f"NON-GUEST EPISODES:\n")
    f.write(f"==================\n\n")
    
    for episode in non_guest_episodes:
        f.write(f"Episode {episode['episode_num']:3d} ({episode['date']}): {episode['title']}\n")

print(f"\nDetailed analysis saved to all_episodes_analysis.txt")

