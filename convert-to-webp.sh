#!/bin/bash

# Script to convert markdown image syntax to WebP includes
# Usage: ./convert-to-webp.sh

echo "Starting WebP conversion for markdown files..."

# Find all markdown files with PNG references
files=$(find . \( -name "*.md" -o -name "*.markdown" \) -exec grep -l "\.png" {} \;)

total_files=0
converted_files=0

for file in $files; do
    total_files=$((total_files + 1))
    echo "Processing: $file"
    
    # Create backup
    cp "$file" "$file.backup"
    
    # Use sed to replace markdown image syntax with WebP include
    # Pattern: ![alt text](/assets/img/filename.png) 
    # Replace with: {% include webp-image.html img="filename.png" alt="alt text" %}
    sed 's/!\[\([^]]*\)\](\/assets\/img\/\([^)]*\.png\))/{% include webp-image.html img="\2" alt="\1" %}/g' "$file" > "$file.tmp"
    
    # Check if any changes were made
    if ! cmp -s "$file" "$file.tmp"; then
        mv "$file.tmp" "$file"
        converted_files=$((converted_files + 1))
        echo "  ✓ Converted PNG references in $file"
    else
        rm "$file.tmp"
        echo "  - No PNG image references found in $file"
    fi
done

echo ""
echo "Conversion complete!"
echo "Files processed: $total_files"
echo "Files converted: $converted_files"
echo ""
echo "Backup files created with .backup extension"
echo "Test your site and remove backups when satisfied: rm *.backup"