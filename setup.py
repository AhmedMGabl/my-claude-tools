#!/usr/bin/env python3
"""
Setup script for my-claude-tools development environment.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run a command and report status."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"  [OK] {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [FAIL] {description} failed")
        if e.stderr:
            print(f"  Error: {e.stderr}")
        return False


def main():
    """Set up development environment."""
    print("=" * 60)
    print("Setting up my-claude-tools development environment")
    print("=" * 60)

    # Check Python version
    print(f"\nPython version: {sys.version}")

    # Install development dependencies
    if Path("requirements.txt").exists():
        run_command(
            "pip install -r requirements.txt",
            "Installing dependencies"
        )

    # Check if Git is initialized
    if Path(".git").exists():
        print("\n[OK] Git repository initialized")

        # Set up pre-commit hook
        hook_dir = Path(".git/hooks")
        hook_dir.mkdir(exist_ok=True)

        pre_commit_hook = hook_dir / "pre-commit"
        pre_commit_content = """#!/bin/bash
# Pre-commit hook for my-claude-tools

echo "Running pre-commit checks..."

# Check Python syntax
python -m py_compile *.py 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Python syntax errors found!"
    exit 1
fi

echo "Pre-commit checks passed!"
"""
        pre_commit_hook.write_text(pre_commit_content)
        pre_commit_hook.chmod(0o755)
        print("  [OK] Pre-commit hook installed")

    # Verify scripts
    print("\nVerifying Python scripts...")
    scripts = ["create_skill_zips.py", "verify_skills.py", "package_skills.py"]
    for script in scripts:
        if Path(script).exists():
            result = subprocess.run(
                ["python", "-m", "py_compile", script],
                capture_output=True
            )
            if result.returncode == 0:
                print(f"  [OK] {script}")
            else:
                print(f"  [FAIL] {script}")

    print("\n" + "=" * 60)
    print("Development environment setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Review installed packages: pip list")
    print("  2. Test scripts: python package_skills.py")
    print("  3. Create new skills in the skills/ directory")
    print("\nHappy coding!")


if __name__ == "__main__":
    main()
