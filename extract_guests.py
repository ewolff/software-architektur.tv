#!/usr/bin/env python3
"""
Guest Extraction Script for software-architektur.tv
Extracts all guests from episode markdown files and generates complete guests.yml
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
import frontmatter

def extract_guest_names_from_title(title):
    """Extract guest names from episode titles using patterns"""
    guests = []
    
    # Pattern 1: "mit [Name]" or "mit [Name] und [Name]"
    mit_pattern = r'mit\s+([^-\n]+?)(?:\s*-|$)'
    mit_matches = re.findall(mit_pattern, title, re.IGNORECASE)
    
    for match in mit_matches:
        # Split multiple guests connected by "und" or ","
        names = re.split(r'\s+und\s+|,\s*', match.strip())
        for name in names:
            name = name.strip()
            # Remove common non-name words
            if name and not re.match(r'^(dem|der|das|live|von|einer|einem)$', name, re.IGNORECASE):
                guests.append(name)
    
    # Pattern 2: Direct name patterns in titles
    # Handle special cases like "Prof. Dr. [Name]"
    title_clean = re.sub(r'Folge\s+\d+\s*-?\s*', '', title)
    
    # Look for academic titles
    academic_pattern = r'(Prof\.?\s+)?(Dr\.?\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
    academic_matches = re.findall(academic_pattern, title_clean)
    
    return guests

def parse_episode_file(filepath):
    """Parse a single episode markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Extract metadata
        title = post.metadata.get('title', '')
        date_str = filepath.stem.split('-', 3)[0:3]  # YYYY-MM-DD
        date = '-'.join(date_str) if len(date_str) == 3 else ''
        tags = post.metadata.get('tags', [])
        
        # Extract guest names
        guests = extract_guest_names_from_title(title)
        
        # Build episode URL
        episode_url = f"/{date.replace('-', '/')}/{filepath.stem.replace(date, '').lstrip('-')}.html"
        
        return {
            'title': title,
            'date': date,
            'url': episode_url,
            'tags': tags,
            'guests': guests,
            'content': post.content
        }
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def extract_all_guests():
    """Extract all guests from all episode files"""
    posts_dir = Path('_posts')
    guest_episodes = {}
    all_guests = defaultdict(list)
    
    # Find all episode files with guests
    for filepath in posts_dir.glob('*.md'):
        if 'template' in filepath.name:
            continue
            
        episode_data = parse_episode_file(filepath)
        if not episode_data or not episode_data['guests']:
            continue
            
        guest_episodes[filepath.stem] = episode_data
        
        # Group episodes by guest
        for guest_name in episode_data['guests']:
            # Clean up guest name
            guest_clean = clean_guest_name(guest_name)
            if guest_clean:
                all_guests[guest_clean].append(episode_data)
    
    return all_guests, guest_episodes

def clean_guest_name(name):
    """Clean and normalize guest names"""
    # Remove common prefixes/suffixes
    name = re.sub(r'^(mit\s+|von\s+|und\s+)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+(live|vom|von|der|dem|mit).*$', '', name, flags=re.IGNORECASE)
    
    # Remove extra whitespace
    name = ' '.join(name.split())
    
    # Skip if too short or looks like not a name
    if len(name) < 3 or name.lower() in ['live', 'dem', 'der', 'das', 'mit', 'und']:
        return None
        
    return name

def generate_linkedin_url(name):
    """Generate likely LinkedIn URL from name"""
    # Simple heuristic - convert to lowercase, replace spaces with dashes
    linkedin_name = name.lower().replace(' ', '-').replace('.', '').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    return f"https://www.linkedin.com/in/{linkedin_name}/"

def generate_expertise_tags(episodes):
    """Generate expertise tags from episode tags and titles"""
    all_tags = set()
    
    for episode in episodes:
        # Add episode tags
        all_tags.update(episode.get('tags', []))
        
        # Extract topics from titles
        title = episode['title'].lower()
        
        # Map common topics
        topic_mapping = {
            'microservices': ['Microservices'],
            'frontend': ['Frontend', 'Web Development'],
            'security': ['Security', 'Cybersecurity'],
            'domain': ['Domain-Driven Design', 'DDD'],
            'api': ['APIs', 'REST'],
            'cloud': ['Cloud', 'AWS'],
            'kubernetes': ['Kubernetes', 'Container'],
            'architecture': ['Software-Architektur'],
            'agile': ['Agile', 'Scrum'],
            'devops': ['DevOps'],
            'testing': ['Testing', 'Quality Assurance'],
            'performance': ['Performance'],
            'ai': ['Artificial Intelligence', 'AI', 'LLM'],
            'spring': ['Spring', 'Java']
        }
        
        for keyword, tags in topic_mapping.items():
            if keyword in title:
                all_tags.update(tags)
    
    return sorted(list(all_tags))

def generate_guests_yaml():
    """Generate complete guests.yml file"""
    print("🔍 Extracting all guests from episodes...")
    
    all_guests, guest_episodes = extract_all_guests()
    
    print(f"📊 Found {len(all_guests)} unique guests in {len(guest_episodes)} episodes")
    
    # Build YAML structure
    guests_data = {'guests': []}
    
    # Sort guests by number of appearances (descending)
    sorted_guests = sorted(all_guests.items(), key=lambda x: len(x[1]), reverse=True)
    
    for guest_name, episodes in sorted_guests:
        if len(episodes) == 0:
            continue
            
        # Build guest data
        guest_data = {
            'name': guest_name,
            'linkedin': generate_linkedin_url(guest_name),
            'image': f"/images/guests/{guest_name.lower().replace(' ', '-').replace('.', '')}.jpg",
            'bio': f"Experte für {', '.join(generate_expertise_tags(episodes)[:3])}",
            'tags': generate_expertise_tags(episodes),
            'episodes': []
        }
        
        # Add episodes
        for episode in sorted(episodes, key=lambda x: x['date']):
            guest_data['episodes'].append({
                'title': episode['title'],
                'url': episode['url'],
                'date': episode['date'],
                'role': 'guest'  # Default role
            })
        
        guests_data['guests'].append(guest_data)
    
    return guests_data

def main():
    """Main execution function"""
    print("🚀 Starting complete guest extraction...")
    
    try:
        guests_data = generate_guests_yaml()
        
        # Write to YAML file
        output_file = '_data/guests_complete.yml'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Software-Architektur.tv Gäste-Datenbank\n")
            f.write("# Vollständig automatisch extrahiert aus allen Episode-Posts\n\n")
            yaml.safe_dump(guests_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"✅ Complete guest database generated: {output_file}")
        print(f"📊 Total guests: {len(guests_data['guests'])}")
        
        # Print summary
        print("\n🎯 Top guests by appearances:")
        for guest in guests_data['guests'][:10]:
            print(f"   • {guest['name']}: {len(guest['episodes'])} episodes")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()