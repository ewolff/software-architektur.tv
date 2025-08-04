#!/bin/bash

echo "🚀 Extracting all guests from software-architektur.tv episodes..."

# Extract all episodes with "mit" in title
echo "📋 Found episodes with guests:"
grep -r "mit " _posts/*.md | grep title | wc -l

# Extract guest names and episode info
echo ""
echo "🎯 All guest episodes:"
grep -r "mit " _posts/*.md | grep title | sort | while IFS=: read -r file title_line; do
    # Extract episode date from filename
    filename=$(basename "$file")
    date=$(echo "$filename" | grep -o '^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}')
    
    # Extract episode number/name
    episode=$(echo "$filename" | sed 's/\.md$//')
    
    # Extract title
    title=$(echo "$title_line" | sed 's/title: //')
    
    # Extract guest name (everything after "mit")
    guest=$(echo "$title" | sed -n 's/.*mit \([^-]*\).*/\1/p' | sed 's/^ *//;s/ *$//')
    
    echo "📅 $date | 👤 $guest | 📺 $title"
done > /tmp/all_guests.txt

echo ""
echo "💾 Complete guest list saved to /tmp/all_guests.txt"
echo "📊 Total guest episodes found: $(wc -l < /tmp/all_guests.txt)"

# Show unique guests
echo ""
echo "🔍 Unique guests (needs manual cleanup):"
grep -r "mit " _posts/*.md | grep title | sed 's/.*mit \([^-]*\).*/\1/' | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -nr | head -20

echo ""
echo "✅ Use this data to build complete guests.yml manually or with additional processing"