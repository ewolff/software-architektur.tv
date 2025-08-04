#!/bin/bash

echo "Extracting guest names from episode titles..."

# Extract episodes with guests (containing "mit ")
grep -h "^title:.*mit " _posts/*.md | \
  # Remove title: prefix and quotes
  sed 's/^title: *"//' | \
  sed 's/"$//' | \
  # Extract everything after "mit "
  sed 's/.* mit //' | \
  # Split on common separators and take first name
  sed 's/ und .*//' | \
  sed 's/ & .*//' | \
  sed 's/ - .*//' | \
  sed 's/ (.*//' | \
  sed 's/ \[.*//' | \
  # Clean up whitespace
  sed 's/^ *//' | \
  sed 's/ *$//' | \
  # Filter out non-names
  grep -v '^[0-9]' | \
  grep -v '^$' | \
  grep -v '^.$' | \
  grep -v '^..$' | \
  # Sort and remove duplicates
  sort -u

