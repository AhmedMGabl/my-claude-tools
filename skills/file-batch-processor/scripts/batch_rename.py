#!/usr/bin/env python3
"""
Batch file renaming with pattern matching and preview mode.
"""

import re
import sys
from pathlib import Path
from datetime import datetime


def rename_files(directory=".", pattern="*", new_pattern=None, preview=True):
    """
    Rename files matching a pattern.

    Args:
        directory: Directory to search for files
        pattern: Glob pattern to match files
        new_pattern: New naming pattern (supports {n}, {date}, {ext})
        preview: If True, show changes without applying
    """
    path = Path(directory)
    files = sorted(path.glob(pattern))

    if not files:
        print(f"❌ No files found matching pattern: {pattern}")
        return

    print(f"🔍 Found {len(files)} files")
    print()

    changes = []
    for i, file in enumerate(files, 1):
        if new_pattern:
            # Support placeholders
            new_name = new_pattern
            new_name = new_name.replace("{n}", str(i).zfill(3))
            new_name = new_name.replace("{date}", datetime.now().strftime("%Y%m%d"))
            new_name = new_name.replace("{ext}", file.suffix)

            if not new_name.endswith(file.suffix):
                new_name += file.suffix

            new_path = file.parent / new_name
            changes.append((file, new_path))

    if preview:
        print("📋 Preview of changes:")
        for old, new in changes:
            print(f"  {old.name} → {new.name}")
        print()
        print("ℹ️  Run with preview=False to apply changes")
    else:
        print("✏️  Applying changes...")
        for old, new in changes:
            old.rename(new)
            print(f"  ✅ {old.name} → {new.name}")
        print()
        print(f"✅ Renamed {len(changes)} files")


if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
        new_pattern = sys.argv[2] if len(sys.argv) > 2 else None
        preview = "--apply" not in sys.argv

        rename_files(pattern=pattern, new_pattern=new_pattern, preview=preview)
    else:
        print("Usage: batch_rename.py <pattern> <new_pattern> [--apply]")
        print("Example: batch_rename.py '*.jpg' 'photo_{n}_{date}' --apply")
