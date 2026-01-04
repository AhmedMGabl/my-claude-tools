#!/usr/bin/env python3
"""
Dependency checker for multiple package managers.
Analyzes and reports dependency status across npm, pip, go mod, etc.
"""

import json
import subprocess
import sys
from pathlib import Path


def check_npm_deps():
    """Check npm dependencies for outdated packages."""
    if not Path("package.json").exists():
        return None

    try:
        result = subprocess.run(
            ["npm", "outdated", "--json"],
            capture_output=True,
            text=True
        )
        if result.stdout:
            return json.loads(result.stdout)
        return {}
    except Exception as e:
        return {"error": str(e)}


def check_pip_deps():
    """Check pip dependencies for outdated packages."""
    if not Path("requirements.txt").exists():
        return None

    try:
        result = subprocess.run(
            ["pip", "list", "--outdated", "--format=json"],
            capture_output=True,
            text=True
        )
        if result.stdout:
            return json.loads(result.stdout)
        return []
    except Exception as e:
        return {"error": str(e)}


def main():
    """Run dependency checks for all detected package managers."""
    print("🔍 Checking dependencies...\n")

    # Check npm
    npm_deps = check_npm_deps()
    if npm_deps is not None:
        print("📦 NPM Dependencies:")
        if isinstance(npm_deps, dict) and "error" in npm_deps:
            print(f"  ❌ Error: {npm_deps['error']}")
        elif npm_deps:
            for pkg, info in npm_deps.items():
                print(f"  ⚠️  {pkg}: {info.get('current')} → {info.get('latest')}")
        else:
            print("  ✅ All packages up to date")
        print()

    # Check pip
    pip_deps = check_pip_deps()
    if pip_deps is not None:
        print("🐍 Python Dependencies:")
        if isinstance(pip_deps, dict) and "error" in pip_deps:
            print(f"  ❌ Error: {pip_deps['error']}")
        elif pip_deps:
            for pkg in pip_deps:
                print(f"  ⚠️  {pkg['name']}: {pkg['version']} → {pkg['latest_version']}")
        else:
            print("  ✅ All packages up to date")
        print()


if __name__ == "__main__":
    main()
