---
name: doc-generator
description: This skill should be used when generating documentation such as README files, API docs, code comments, user guides, or technical specifications. It provides standardized templates and workflows for creating comprehensive documentation.
---

# Documentation Generator

Automates the creation of various types of documentation using standardized templates and best practices.

## Purpose

Streamlines documentation creation by providing templates, style guides, and automated generation workflows. Ensures consistency across documentation and reduces time spent on formatting and structure.

## When to Use

Use this skill when:
- Creating README files for projects
- Generating API documentation
- Writing user guides or tutorials
- Creating technical specifications
- Documenting code with comments
- Building knowledge base articles
- Producing changelog entries

## Usage Guide

### README Generation

To create a README file:

1. Gather project information (purpose, installation, usage)
2. Select appropriate template from `assets/templates/`
3. Fill in sections with project-specific content
4. Add badges and links

Example: "Generate a README for my Python package"

### API Documentation

To generate API docs:

1. Parse source code for API definitions
2. Extract function signatures and docstrings
3. Format according to style guide
4. Generate navigation and examples

Use `scripts/generate_api_docs.py` to automate API documentation.

### Code Comments

To document code:

1. Identify functions/classes needing documentation
2. Follow language-specific conventions (JSDoc, docstrings, etc.)
3. Include parameters, returns, and examples
4. Keep comments concise and up-to-date

Reference `references/comment-styles.md` for language-specific conventions.

### User Guides

To create user guides:

1. Outline user workflows and tasks
2. Use template from `assets/templates/user-guide.md`
3. Include screenshots and examples
4. Organize by user role or feature

### Changelog Management

To maintain changelogs:

1. Follow Keep a Changelog format
2. Categorize changes (Added, Changed, Fixed, etc.)
3. Include version numbers and dates
4. Link to relevant issues/PRs

Use `scripts/update_changelog.py` for automated changelog updates.

## Bundled Resources

### Scripts

- `scripts/generate_api_docs.py` - Generate API documentation from code
- `scripts/update_changelog.py` - Automated changelog management
- `scripts/generate_readme.py` - Interactive README generator
- `scripts/doc_validator.py` - Validate documentation completeness

### References

- `references/comment-styles.md` - Code comment conventions by language
- `references/markdown-guide.md` - Markdown formatting reference
- `references/doc-best-practices.md` - Documentation writing guidelines

### Assets

- `assets/templates/README.md` - README template with common sections
- `assets/templates/API.md` - API documentation template
- `assets/templates/user-guide.md` - User guide template
- `assets/templates/CHANGELOG.md` - Changelog template
- `assets/badges/` - Collection of status badges

## Best Practices

1. **Clarity** - Write for your audience's technical level
2. **Examples** - Include code examples for all features
3. **Structure** - Use consistent heading hierarchy
4. **Updates** - Keep documentation in sync with code
5. **Links** - Cross-reference related documentation
6. **Searchability** - Use clear, descriptive headings
