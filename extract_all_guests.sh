#!/bin/bash

# Extract all unique guest names from episode titles
echo "Extracting all guest names from episodes..."

# Find all episodes with "mit" (indicating guests)
grep -r "^title:.*mit " _posts/ | \
  # Extract the part after "mit "
  sed 's/.*mit \([^"]*\)".*/\1/' | \
  # Remove common patterns and clean up
  sed 's/ - .*$//' | \
  sed 's/ und .*$//' | \
  sed 's/ & .*$//' | \
  sed 's/,.*$//' | \
  # Remove trailing whitespace
  sed 's/ *$//' | \
  # Sort and remove duplicates
  sort -u | \
  # Filter out non-names (dates, numbers, etc.)
  grep -v '^[0-9]' | \
  grep -v '^$' | \
  # Remove single letter names
  grep -v '^.$' | \
  # Show results
  head -50

