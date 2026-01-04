---
name: code-standards-checker
description: This skill should be used when reviewing code for adherence to coding standards, style guides, best practices, and team conventions. It provides automated checking and reporting of code quality issues.
---

# Code Standards Checker

Automates code review for style, standards, and best practices compliance.

## Purpose

Enforces consistent code quality and style across projects by automatically checking code against defined standards. Identifies violations early in development to maintain code quality and reduce review time.

## When to Use

Use this skill when:
- Reviewing pull requests for standards compliance
- Setting up pre-commit hooks
- Auditing existing codebases for quality
- Enforcing team coding conventions
- Checking for security vulnerabilities
- Validating code before deployment
- Generating code quality reports

## Usage Guide

### Standards Checking

To check code against standards:

1. Define standards and rules to check
2. Run appropriate linters and checkers
3. Review violations and severity
4. Fix issues or update standards

Use `scripts/check_standards.py` for comprehensive standards checking.

Example: "Check all Python files for PEP 8 compliance"

### Style Guide Enforcement

To enforce style guides:

1. Configure linters (ESLint, Flake8, etc.)
2. Set up auto-formatting (Prettier, Black)
3. Run checks in CI/CD pipeline
4. Generate reports

Reference `references/style-guides.md` for language-specific style guides.

### Security Scanning

To scan for security issues:

1. Run security linters (Bandit, ESLint security)
2. Check for known vulnerabilities
3. Validate dependencies
4. Review sensitive data exposure

Use `scripts/security_scan.py` for security-focused code review.

### Complexity Analysis

To analyze code complexity:

1. Calculate cyclomatic complexity
2. Identify code smells
3. Measure code metrics
4. Suggest refactoring targets

Use `scripts/complexity_analyzer.py` for complexity metrics.

### Custom Rules

To enforce custom team rules:

1. Define custom rules in `references/custom-rules.md`
2. Implement checkers in `scripts/custom_checker.py`
3. Integrate with existing tools
4. Document violations

## Bundled Resources

### Scripts

- `scripts/check_standards.py` - Multi-language standards checker
- `scripts/security_scan.py` - Security vulnerability scanner
- `scripts/complexity_analyzer.py` - Code complexity metrics
- `scripts/custom_checker.py` - Custom team rules checker
- `scripts/generate_report.py` - Quality report generator

### References

- `references/style-guides.md` - Style guides by language
- `references/custom-rules.md` - Team-specific coding rules
- `references/best-practices.md` - General best practices
- `references/security-patterns.md` - Security coding patterns

### Assets

- `assets/configs/` - Linter configuration files
- `assets/templates/` - Report templates

## Best Practices

1. **Automation** - Run checks automatically in CI/CD
2. **Consistency** - Apply same standards across all code
3. **Education** - Document why rules exist
4. **Flexibility** - Allow exceptions when justified
5. **Incremental** - Fix issues incrementally, not all at once
6. **Feedback** - Provide clear, actionable error messages
