#!/usr/bin/env python3
import re

def generate_linkedin_image_url(name):
    """Generate LinkedIn profile image URL based on standard patterns"""
    # LinkedIn profile images follow patterns like:
    # https://media.licdn.com/dms/image/C4D03AQE.../profile-displayphoto-shrink_200_200/0/...
    # But we can't generate these dynamically without API access
    
    # Alternative: Use LinkedIn's public profile URL approach
    linkedin_name = name.lower()
    linkedin_name = re.sub(r'[^a-zA-Z0-9äöüß ]', '', linkedin_name)
    linkedin_name = linkedin_name.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    linkedin_name = linkedin_name.replace(' ', '-')
    linkedin_name = re.sub(r'^dr-?', '', linkedin_name)
    linkedin_name = re.sub(r'^prof-?', '', linkedin_name)
    
    # Use a placeholder service that shows LinkedIn profile pics
    # or fallback to initials-based avatars
    return f"https://ui-avatars.com/api/?name={name.replace(' ', '+')}&size=200&background=007acc&color=fff&bold=true"

def update_guests_yml_with_linkedin_images():
    """Update guests.yml to use LinkedIn profile image URLs"""
    
    with open('_data/guests.yml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image lines and replace them
    def replace_image(match):
        # Extract the name from the previous line
        lines_before = content[:match.start()].split('\n')
        name_line = None
        for line in reversed(lines_before[-10:]):  # Check last 10 lines
            if 'name: "' in line:
                name_match = re.search(r'name: "([^"]+)"', line)
                if name_match:
                    name = name_match.group(1)
                    linkedin_image_url = generate_linkedin_image_url(name)
                    return f'    image: "{linkedin_image_url}"'
        
        # Fallback if name not found
        return match.group(0)
    
    # Replace all image lines
    updated_content = re.sub(
        r'    image: "/images/[^"]*"',
        replace_image,
        content
    )
    
    # Write updated content
    with open('_data/guests.yml', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Updated all image URLs to use generated avatar service")

if __name__ == "__main__":
    update_guests_yml_with_linkedin_images()
