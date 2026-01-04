#!/usr/bin/env python3
"""
Package custom skills into distributable zip files.
"""

import zipfile
from pathlib import Path
import shutil


def validate_skill(skill_path):
    """Validate that a skill has required components."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False, "Missing SKILL.md"

    # Check for YAML frontmatter
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False, "SKILL.md missing YAML frontmatter"

    # Check for name and description in frontmatter
    if 'name:' not in content[:500] or 'description:' not in content[:500]:
        return False, "SKILL.md missing name or description in frontmatter"

    return True, "OK"


def package_skill(skill_path, output_dir):
    """Package a skill into a zip file."""
    skill_name = skill_path.name
    zip_path = output_dir / f"{skill_name}.zip"

    # Validate skill first
    valid, message = validate_skill(skill_path)
    if not valid:
        return False, message

    # Create zip file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in skill_path.rglob('*'):
            if file.is_file():
                arcname = file.relative_to(skill_path.parent)
                zipf.write(file, arcname)

    # Get file count
    file_count = len(list(skill_path.rglob('*')))

    return True, f"OK ({file_count} files)"


def main():
    """Package all custom skills."""
    skills_dir = Path("skills")
    output_dir = Path("packaged-skills")

    if not skills_dir.exists():
        print("ERROR: skills/ directory not found")
        return 1

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    print("Packaging custom skills...\n")

    skills = sorted([d for d in skills_dir.iterdir() if d.is_dir()])

    if not skills:
        print("ERROR: No skills found in skills/ directory")
        return 1

    results = []
    for skill_path in skills:
        skill_name = skill_path.name
        success, message = package_skill(skill_path, output_dir)

        status = "[OK]" if success else "[FAIL]"
        print(f"{status} {skill_name:30s} {message}")
        results.append(success)

    print()
    success_count = sum(results)
    total_count = len(results)

    if success_count == total_count:
        print(f"SUCCESS: Packaged {success_count}/{total_count} skills!")
        print(f"Output directory: {output_dir.absolute()}")
        return 0
    else:
        print(f"WARNING: Packaged {success_count}/{total_count} skills")
        print(f"ERROR: {total_count - success_count} skills failed validation")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
