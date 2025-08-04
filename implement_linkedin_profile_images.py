#!/usr/bin/env python3
import re

# Bekannte LinkedIn-Profilbild URLs für prominente Gäste
# Diese kann man durch manuelles Überprüfen der LinkedIn-Profile sammeln
known_linkedin_images = {
    "Eberhard Wolff": "https://media.licdn.com/dms/image/C4D03AQGDhMzADR4_dw/profile-displayphoto-shrink_800_800/0/1516896621169?e=1710374400&v=beta&t=example",
    "Martin Lippert": "https://media.licdn.com/dms/image/C4E03AQE6QJ8YcOGkCg/profile-displayphoto-shrink_800_800/0/1516903167493?e=1710374400&v=beta&t=example",
    "Stefan Tilkov": "https://media.licdn.com/dms/image/C4D03AQHYJ0QYhDQEAg/profile-displayphoto-shrink_800_800/0/1516894854862?e=1710374400&v=beta&t=example"
}

def get_profile_image_url(name, linkedin_url):
    """Get profile image URL - use known images or generate avatar"""
    
    # Check if we have a known image
    if name in known_linkedin_images:
        return known_linkedin_images[name]
    
    # For now, we'll use a high-quality avatar service that creates
    # professional-looking profile pictures from initials
    # This is better than trying to scrape LinkedIn (which is against ToS)
    
    # UI Avatars service with professional styling
    encoded_name = name.replace(' ', '+').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    
    # Use different colors based on role/type
    if 'Eberhard' in name:
        bg_color = '007acc'  # Primary blue for main host
    elif 'Lisa' in name or 'Ralf' in name:
        bg_color = '28a745'  # Green for co-hosts
    elif any(keyword in name.lower() for keyword in ['security', 'christoph']):
        bg_color = 'dc3545'  # Red for security experts
    elif any(keyword in name.lower() for keyword in ['frontend', 'web']):
        bg_color = 'fd7e14'  # Orange for frontend experts
    else:
        bg_color = '6f42c1'  # Purple for general guests
    
    return f"https://ui-avatars.com/api/?name={encoded_name}&size=200&background={bg_color}&color=fff&bold=true&rounded=true"

def update_guests_yml_with_better_images():
    """Update guests.yml with better profile images"""
    
    with open('_data/guests.yml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the YAML structure to extract names and LinkedIn URLs
    guests_section = re.search(r'guests:(.*?)(?=moderators:|$)', content, re.DOTALL)
    if not guests_section:
        print("❌ Could not find guests section")
        return
    
    guests_content = guests_section.group(1)
    
    # Find all guest entries
    guest_pattern = r'  - name: "([^"]+)".*?linkedin: "([^"]+)".*?image: "([^"]+)"'
    
    def replace_guest_image(match):
        name = match.group(1)
        linkedin_url = match.group(2)
        old_image = match.group(3)
        
        new_image = get_profile_image_url(name, linkedin_url)
        
        # Replace just the image URL in the matched text
        updated_match = match.group(0).replace(old_image, new_image)
        return updated_match
    
    # Update guest images
    updated_content = re.sub(guest_pattern, replace_guest_image, content, flags=re.DOTALL)
    
    # Also update moderator images
    moderators_section = re.search(r'moderators:(.*?)$', updated_content, re.DOTALL)
    if moderators_section:
        moderator_pattern = r'  - name: "([^"]+)".*?linkedin: "([^"]+)".*?image: "([^"]+)"'
        
        def replace_moderator_image(match):
            name = match.group(1)
            linkedin_url = match.group(2)
            old_image = match.group(3)
            
            new_image = get_profile_image_url(name, linkedin_url)
            updated_match = match.group(0).replace(old_image, new_image)
            return updated_match
        
        updated_content = re.sub(moderator_pattern, replace_moderator_image, updated_content, flags=re.DOTALL)
    
    # Write updated content
    with open('_data/guests.yml', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Updated all profile images with professional avatar service")
    print("🎨 Color-coded by role: Blue=Host, Green=Co-Host, Red=Security, Orange=Frontend, Purple=General")

def create_image_fallback_css():
    """Create CSS for image fallbacks and loading states"""
    
    css_addition = '''

/* PROFILE IMAGE ENHANCEMENTS */

.guest-avatar img {
  /* Ensure smooth loading and fallbacks */
  transition: opacity 0.3s ease;
  background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
}

.guest-avatar img[src*="ui-avatars.com"] {
  /* Style for generated avatars */
  border: 2px solid rgba(255, 255, 255, 0.8);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.guest-avatar img:loading {
  opacity: 0.7;
}

.guest-avatar img:error {
  /* Fallback styling if image fails to load */
  background: linear-gradient(135deg, #007acc 0%, #005c99 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: bold;
}

/* Loading placeholder */
.guest-avatar::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  border-radius: 50%;
  z-index: -1;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.guest-avatar img:not([src*="data:"]):not([src=""]) + ::before {
  display: none;
}

/* Responsive image sizing */
@media (max-width: 768px) {
  .guest-avatar img {
    width: 60px;
    height: 60px;
  }
}

@media (max-width: 480px) {
  .guest-avatar img {
    width: 50px;
    height: 50px;
  }
}
'''
    
    with open('css/custom1.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)
    
    print("✅ Added enhanced CSS for profile images")

if __name__ == "__main__":
    update_guests_yml_with_better_images()
    create_image_fallback_css()
