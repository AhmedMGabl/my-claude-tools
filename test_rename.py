#!/usr/bin/env python3
"""
Test batch rename on user's photos with preview.
"""

import sys
sys.path.insert(0, 'skills/file-batch-processor/scripts')

from batch_rename import rename_files

# Test renaming JPG files in the photos directory
photo_dir = r"C:\Users\eng20\Downloads\🤝Orders - EG August"

print("=" * 70)
print("BATCH RENAME PREVIEW - Orders Photos")
print("=" * 70)
print()

# Preview renaming JPG files to organized pattern
print("Example 1: Rename JPG files to 'order_###.jpg'")
print("-" * 70)
rename_files(
    directory=photo_dir,
    pattern="*.jpg",
    new_pattern="order_{n}.jpg",
    preview=True
)

print("\n" + "=" * 70)
print("Example 2: Rename with date (today)")
print("-" * 70)
rename_files(
    directory=photo_dir,
    pattern="*.jpg",
    new_pattern="photo_{date}_{n}.jpg",
    preview=True
)

print("\n" + "=" * 70)
print("To apply changes, modify the script and set preview=False")
print("=" * 70)
