#!/usr/bin/env python3
"""
Multi-language code standards checker.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Dict


def run_command(cmd: List[str]) -> Dict[str, any]:
    """Run a command and return results."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'errors': result.stderr
        }
    except Exception as e:
        return {'success': False, 'errors': str(e)}


def check_python():
    """Check Python files with flake8."""
    if not list(Path('.').rglob('*.py')):
        return None

    print("🐍 Checking Python files...")
    result = run_command(['flake8', '.', '--count', '--statistics'])

    if result['success']:
        print("  ✅ All Python files passed")
    else:
        print("  ⚠️  Issues found:")
        print(result['output'] or result['errors'])

    return result


def check_javascript():
    """Check JavaScript files with ESLint."""
    if not Path('package.json').exists():
        return None

    print("📦 Checking JavaScript files...")
    result = run_command(['npx', 'eslint', '.'])

    if result['success']:
        print("  ✅ All JavaScript files passed")
    else:
        print("  ⚠️  Issues found:")
        print(result['output'] or result['errors'])

    return result


def check_typescript():
    """Check TypeScript files."""
    if not Path('tsconfig.json').exists():
        return None

    print("📘 Checking TypeScript files...")
    result = run_command(['npx', 'tsc', '--noEmit'])

    if result['success']:
        print("  ✅ All TypeScript files passed")
    else:
        print("  ⚠️  Issues found:")
        print(result['errors'])

    return result


def main():
    """Run all applicable standards checks."""
    print("🔍 Running code standards checks...\n")

    results = []
    results.append(check_python())
    results.append(check_javascript())
    results.append(check_typescript())

    # Filter out None results
    results = [r for r in results if r is not None]

    if not results:
        print("❌ No recognized project type found")
        return 1

    print("\n" + "=" * 50)
    all_passed = all(r['success'] for r in results)

    if all_passed:
        print("✅ All checks passed!")
        return 0
    else:
        print("⚠️  Some checks failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
