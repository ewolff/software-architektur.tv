#!/usr/bin/env python3
import re

# Read the extracted guest list and clean it
real_guests = {}

# List of names that are clearly not person names - to filter out
non_person_names = {
    'Code', 'Dingen', 'Domain', 'DSL', 'HTTP Feeds', 'jQAssistant', 'Open', 
    'Single Page Frameworks', 'Sonargraph', 'Spring', 'Spring Native', 
    'Spring Boot', 'Spring Cloud', 'dem Technology', 'dem Faktor Mensch um?',
    'Liberating Structures für Architekt:innen mit Martin Günther',
    'Java', 'jMolecules mit O', 'Menschen mit Michael Hunger', 'KI'
}

with open('complete_guest_list.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse the guest entries
guest_entries = re.findall(r'([^:]+) \((\d+) episodes?\):(.*?)(?=\n[A-Z]|\n\nSTATISTICS|\Z)', content, re.DOTALL)

print(f"Found {len(guest_entries)} guest entries to process...")

for guest_name, episode_count, episodes_text in guest_entries:
    guest_name = guest_name.strip()
    
    # Skip non-person names
    if guest_name in non_person_names:
        print(f"Skipping non-person: {guest_name}")
        continue
    
    # Additional validation - should be a proper name format
    if (len(guest_name) < 3 or 
        not re.search(r'[A-Z]', guest_name) or  # Should have at least one capital letter
        guest_name.startswith('dem ') or
        guest_name.startswith('der ') or
        guest_name.endswith(' um?')):
        print(f"Skipping invalid name format: {guest_name}")
        continue
    
    # Parse episodes for this guest
    episode_matches = re.findall(r'- Episode (\d+): title: ([^(]+) \(([^)]+)\)', episodes_text)
    
    guest_episodes = []
    for ep_num, ep_title, ep_date in episode_matches:
        guest_episodes.append({
            'episode': ep_num,
            'title': ep_title.strip(),
            'date': ep_date,
            'url': f"/{ep_date.replace('-', '/')}/"
        })
    
    real_guests[guest_name] = guest_episodes
    print(f"Added: {guest_name} ({len(guest_episodes)} episodes)")

print(f"\nFinal count: {len(real_guests)} real person guests")

# Generate LinkedIn URLs (best effort based on common patterns)
def generate_linkedin_url(name):
    # Convert name to linkedin format: lowercase, replace spaces with dashes
    linkedin_name = name.lower()
    linkedin_name = re.sub(r'[^a-zA-Z0-9äöüß ]', '', linkedin_name)  # Remove special chars
    linkedin_name = linkedin_name.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    linkedin_name = linkedin_name.replace(' ', '-')
    linkedin_name = re.sub(r'^dr-?', '', linkedin_name)  # Remove Dr. prefix
    linkedin_name = re.sub(r'^prof-?', '', linkedin_name)  # Remove Prof. prefix
    return f"https://www.linkedin.com/in/{linkedin_name}/"

# Determine main expertise/tags based on episode titles
def extract_tags_from_episodes(episodes):
    all_titles = ' '.join([ep['title'] for ep in episodes])
    tags = []
    
    # Common technology/domain patterns
    if 'Security' in all_titles or 'OWASP' in all_titles or 'Zero Trust' in all_titles:
        tags.extend(['Security', 'OWASP', 'Cybersecurity'])
    if 'Domain-driven Design' in all_titles or 'DDD' in all_titles:
        tags.extend(['Domain-driven Design', 'DDD'])
    if 'Frontend' in all_titles or 'Web' in all_titles:
        tags.extend(['Frontend', 'Web Development'])
    if 'Spring' in all_titles:
        tags.extend(['Spring', 'Java'])
    if 'Architektur' in all_titles:
        tags.extend(['Software Architecture'])
    if 'Testing' in all_titles or 'Test' in all_titles:
        tags.extend(['Testing', 'Quality Assurance'])
    if 'Agile' in all_titles or 'Scrum' in all_titles:
        tags.extend(['Agile', 'Scrum'])
    if 'DevOps' in all_titles:
        tags.extend(['DevOps'])
    if 'Leadership' in all_titles or 'Team' in all_titles:
        tags.extend(['Leadership', 'Team Management'])
    if 'API' in all_titles:
        tags.extend(['API Design'])
    if 'Cloud' in all_titles:
        tags.extend(['Cloud Computing'])
    if 'KI' in all_titles or 'AI' in all_titles or 'ChatGPT' in all_titles:
        tags.extend(['AI', 'Machine Learning'])
    
    # Remove duplicates and limit to 5 tags
    tags = list(dict.fromkeys(tags))[:5]
    
    return tags if tags else ['Software Development']

# Create complete YAML content
yaml_content = """# Software-Architektur.tv Gäste-Datenbank
# VOLLSTÄNDIGE Liste aller 89+ Episoden-Gäste
# Extrahiert aus allen Episode-Titeln seit Beginn des Streams

guests:
"""

for guest_name in sorted(real_guests.keys()):
    episodes = real_guests[guest_name]
    linkedin_url = generate_linkedin_url(guest_name)
    tags = extract_tags_from_episodes(episodes)
    
    # Create a bio based on episode topics
    episode_topics = []
    for ep in episodes:
        if 'Security' in ep['title']:
            episode_topics.append('Security')
        elif 'Frontend' in ep['title']:
            episode_topics.append('Frontend')
        elif 'Domain' in ep['title']:
            episode_topics.append('Domain-driven Design')
        elif 'API' in ep['title']:
            episode_topics.append('API Design')
        elif 'Testing' in ep['title']:
            episode_topics.append('Testing')
        elif 'Agile' in ep['title']:
            episode_topics.append('Agile')
    
    unique_topics = list(dict.fromkeys(episode_topics))
    if unique_topics:
        bio = f"{', '.join(unique_topics)} Experte/Expertin"
    else:
        bio = "Software-Entwicklung und -Architektur"
    
    yaml_content += f"""
  # {guest_name} - {len(episodes)} Episode{'n' if len(episodes) > 1 else ''}
  - name: "{guest_name}"
    linkedin: "{linkedin_url}"
    image: "/images/guests/{guest_name.lower().replace(' ', '-').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')}.jpg"
    bio: "{bio}"
    tags: {tags}
    episodes:"""
    
    for ep in episodes:
        yaml_content += f"""
      - title: "{ep['title']}"
        url: "{ep['url']}"
        date: "{ep['date']}"
        role: "guest\""""

yaml_content += "\n"

# Write the complete guests.yml file
with open('_data/guests_complete.yml', 'w', encoding='utf-8') as f:
    f.write(yaml_content)

print(f"\nGenerated complete guests.yml with {len(real_guests)} guests")
print(f"File saved as _data/guests_complete.yml")

# Show summary
print(f"\nSUMMARY:")
print(f"Total guests: {len(real_guests)}")
multiple_episodes = [(name, len(episodes)) for name, episodes in real_guests.items() if len(episodes) > 1]
multiple_episodes.sort(key=lambda x: x[1], reverse=True)
print(f"Guests with multiple episodes: {len(multiple_episodes)}")

print(f"\nTop 10 most frequent guests:")
for i, (name, count) in enumerate(multiple_episodes[:10]):
    print(f"{i+1:2d}. {name}: {count} episodes")

