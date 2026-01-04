---
name: development-helper
description: This skill should be used when setting up development environments, managing project dependencies, or running common development commands. It provides standardized workflows for project initialization, dependency management, testing, and deployment.
---

# Development Helper

Streamlines common development workflows including project setup, dependency management, testing, and deployment tasks.

## Purpose

Automates repetitive development tasks and enforces consistent project setup procedures. Reduces context switching and manual command execution for common operations like environment setup, dependency updates, testing workflows, and deployment procedures.

## When to Use

Use this skill when:
- Initializing new projects with standard tooling
- Managing dependencies across multiple package managers
- Running test suites with consistent configuration
- Setting up development environments
- Executing deployment workflows
- Performing project health checks

## Usage Guide

### Project Initialization

To initialize a new project:

1. Determine project type (Node.js, Python, Go, etc.)
2. Use the appropriate initialization script from `scripts/`
3. Apply standard configuration templates from `assets/`

Example: "Set up a new Node.js project with TypeScript"

### Dependency Management

To manage dependencies:

1. Check current dependency status
2. Update outdated packages
3. Verify compatibility
4. Run security audits

Use `scripts/check_deps.py` to analyze and report dependency status across multiple package managers.

### Testing Workflows

To run tests:

1. Execute test suite with proper environment variables
2. Generate coverage reports
3. Validate test results

Reference `references/test-standards.md` for testing best practices and coverage requirements.

### Development Environment

To set up development environment:

1. Install required tools and dependencies
2. Configure environment variables
3. Set up pre-commit hooks
4. Validate setup

Use `scripts/setup_env.sh` to automate environment configuration.

### Health Checks

To perform project health checks:

1. Validate configuration files
2. Check for outdated dependencies
3. Run linters and formatters
4. Verify build process

Use `scripts/health_check.py` for comprehensive project validation.

## Bundled Resources

### Scripts

- `scripts/setup_env.sh` - Automated development environment setup
- `scripts/check_deps.py` - Multi-language dependency analyzer
- `scripts/health_check.py` - Project health and validation checker
- `scripts/init_project.py` - Interactive project initialization

### References

- `references/test-standards.md` - Testing standards and coverage requirements
- `references/env-vars.md` - Common environment variable configurations
- `references/git-workflow.md` - Git branching and commit conventions

### Assets

- `assets/templates/` - Project template files (.gitignore, .editorconfig, etc.)
- `assets/configs/` - Standard configuration files (tsconfig.json, pytest.ini, etc.)

## Best Practices

1. **Consistency** - Always use standardized scripts and templates
2. **Documentation** - Update references when adding new workflows
3. **Validation** - Run health checks before committing changes
4. **Automation** - Prefer scripts over manual command sequences
5. **Portability** - Ensure scripts work across different operating systems
