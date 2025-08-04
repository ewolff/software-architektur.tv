#!/usr/bin/env python3

# List of additional prominent guests to add
new_guests = [
    {
        "name": "Johannes Link",
        "linkedin": "https://www.linkedin.com/in/johanneslink/",
        "bio": "Property-Based Testing Experte, jqwik Maintainer",
        "tags": ["Property-Based Testing", "jqwik", "Test-Driven Development", "Java", "Testing"],
        "episodes": [
            {"title": "Folge 147 - Property-based Testing mit Johannes Link", "date": "2023-01-13"}
        ]
    },
    {
        "name": "Jochen Mader", 
        "linkedin": "https://www.linkedin.com/in/jochen-mader/",
        "bio": "Supply Chain Security Experte",
        "tags": ["Supply Chain Security", "Security", "DevSecOps", "BED-Con"],
        "episodes": [
            {"title": "Folge 231 - Supply Chain Security mit Jochen Mader - live von der BED-Con", "date": "2024-09-06"}
        ]
    },
    {
        "name": "Michael Plöd",
        "linkedin": "https://www.linkedin.com/in/michael-plöd/", 
        "bio": "Domain-driven Design Experte, innoQ Principal Consultant",
        "tags": ["Domain-driven Design", "DDD", "Software Architecture", "Quality Storming"],
        "episodes": [
            {"title": "Folge 90 - Michael Plöd - Wie steigt man in Domain-driven Design ein?", "date": "2022-01-07"},
            {"title": "Folge 224 - Quality Storming mit Michael Plöd", "date": "2024-07-12"}
        ]
    },
    {
        "name": "Oliver Wehrens",
        "linkedin": "https://www.linkedin.com/in/oliverwehrens/",
        "bio": "Software-Architekt und Agile Coach",
        "tags": ["Software Architecture", "Agile", "Team Collaboration"],
        "episodes": [
            {"title": "Folge 141 - Architektur Reviews mit Oliver Wehrens", "date": "2022-11-04"}
        ]
    },
    {
        "name": "Alexander von Zitzewitz",
        "linkedin": "https://www.linkedin.com/in/zitzewitz/",
        "bio": "Sonargraph Creator, Architektur-Management Experte",
        "tags": ["Sonargraph", "Architektur-Management", "Static Analysis", "Dependency Analysis"],
        "episodes": [
            {"title": "Folge 60 - Alexander von Zitzewitz zu Architektur-Management mit Sonargraph", "date": "2021-05-28"}
        ]
    },
    {
        "name": "Dehla Sokenou",
        "linkedin": "https://www.linkedin.com/in/dehla-sokenou/",
        "bio": "Diversity & Inclusion Expertin, Microsoft Germany",
        "tags": ["Diversity", "Inclusion", "Leadership", "Microsoft", "Career Development"],
        "episodes": [
            {"title": "Folge 156 - Karriereentwicklung und Diversity mit Dehla Sokenou", "date": "2023-03-10"}
        ]
    },
    {
        "name": "Joseph Pelrine",
        "linkedin": "https://www.linkedin.com/in/josephpelrine/",
        "bio": "Agile Coach und Complexity Science Experte",
        "tags": ["Agile", "Complexity Science", "Team Dynamics", "MetaProgramming"],
        "episodes": [
            {"title": "Folge 158 - Agile MetaProgramming mit Joseph Pelrine", "date": "2023-03-24"}
        ]
    },
    {
        "name": "Falk Hoppe",
        "linkedin": "https://www.linkedin.com/in/falk-hoppe/",
        "bio": "Platform Engineering Experte",
        "tags": ["Platform Engineering", "DevOps", "Cloud Native", "Kubernetes"],
        "episodes": [
            {"title": "Folge 161 - Platform Engineering mit Falk Hoppe", "date": "2023-04-21"}
        ]
    },
    {
        "name": "Kim Nena Duggen",
        "linkedin": "https://www.linkedin.com/in/kim-nena-duggen/",
        "bio": "Software-Architektin und Public Speaker",
        "tags": ["Software Architecture", "Public Speaking", "Career Development"],
        "episodes": [
            {"title": "Folge 162 - Aus der Perspektive einer Architektin mit Kim Nena Duggen", "date": "2023-04-27"}
        ]
    },
    {
        "name": "Tobias Goeschel",
        "linkedin": "https://www.linkedin.com/in/tobias-goeschel/",
        "bio": "Principal Engineer, Technische Schulden Experte",
        "tags": ["Technical Debt", "Software Quality", "Refactoring", "Legacy Systems"],
        "episodes": [
            {"title": "Folge 163 - Technische Schulden mit Tobias Goeschel", "date": "2023-04-28"}
        ]
    }
]

# Read current guests.yml
with open('_data/guests.yml', 'r', encoding='utf-8') as f:
    content = f.read()

# Add new guests to the file
for guest in new_guests:
    episodes_str = "\n".join([
        f"      - title: \"{ep['title']}\"\n        url: \"/{ep['date'].replace('-', '/')}/\"\n        date: \"{ep['date']}\"\n        role: \"guest\""
        for ep in guest['episodes']
    ])
    
    guest_entry = f"""
  # {guest['name']} - {guest['bio']}
  - name: "{guest['name']}"
    linkedin: "{guest['linkedin']}"
    image: "/images/guests/{guest['name'].lower().replace(' ', '-').replace('.', '')}.jpg"
    bio: "{guest['bio']}"
    tags: {guest['tags']}
    episodes:
{episodes_str}
"""
    content += guest_entry

# Write updated file
with open('_data/guests.yml', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Added {len(new_guests)} new guests to guests.yml")
