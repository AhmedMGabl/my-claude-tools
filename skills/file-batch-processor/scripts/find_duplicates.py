#!/usr/bin/env python3
"""
Find duplicate files using hash comparison.
"""

import hashlib
from pathlib import Path
from collections import defaultdict


def hash_file(filepath):
    """Generate MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_duplicates(directory=".", recursive=True):
    """
    Find duplicate files in a directory.

    Args:
        directory: Directory to scan
        recursive: Whether to scan subdirectories
    """
    path = Path(directory)
    files = path.rglob("*") if recursive else path.glob("*")

    print("Scanning for duplicate files...")
    print()

    # Group files by size first (faster than hashing)
    by_size = defaultdict(list)
    file_count = 0
    for file in files:
        if file.is_file():
            by_size[file.stat().st_size].append(file)
            file_count += 1

    print(f"Scanned {file_count} files...")

    # Hash files with same size
    by_hash = defaultdict(list)
    for size, file_list in by_size.items():
        if len(file_list) > 1:
            for file in file_list:
                file_hash = hash_file(file)
                by_hash[file_hash].append(file)

    # Report duplicates
    duplicates = {h: files for h, files in by_hash.items() if len(files) > 1}

    if not duplicates:
        print("\n[OK] No duplicate files found")
        return

    total_wasted = sum(
        files[0].stat().st_size * (len(files) - 1)
        for files in duplicates.values()
    )
    wasted_mb = total_wasted / (1024 * 1024)

    print(f"\n[!] Found {len(duplicates)} sets of duplicate files")
    print(f"[!] Wasted space: {wasted_mb:.2f} MB\n")

    for file_hash, files in duplicates.items():
        size_mb = files[0].stat().st_size / (1024 * 1024)
        print(f"Duplicate set ({size_mb:.2f} MB each, {len(files)} copies):")
        for file in files:
            try:
                print(f"   - {file}")
            except UnicodeEncodeError:
                print(f"   - {str(file).encode('ascii', 'replace').decode('ascii')}")
        print()


if __name__ == "__main__":
    import sys
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    find_duplicates(directory)
