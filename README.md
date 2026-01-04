# My Claude Tools

Personal collection of Claude Code skills, plugins, and utility tools.

## Custom Skills

This repository includes 6 custom skills for various development tasks:

### Development Tools

- **[development-helper](./skills/development-helper/)** - Streamlines project setup, dependency management, testing, and deployment workflows
- **[file-batch-processor](./skills/file-batch-processor/)** - Automates batch file operations including renaming, format conversion, and organization
- **[api-wrapper](./skills/api-wrapper/)** - Simplifies REST API interactions with authentication, rate limiting, and error handling

### Documentation & Quality

- **[doc-generator](./skills/doc-generator/)** - Generates documentation from templates (README, API docs, user guides)
- **[code-standards-checker](./skills/code-standards-checker/)** - Automates code review for standards compliance and quality
- **[workflow-automation](./skills/workflow-automation/)** - Automates CI/CD pipelines, deployments, and scheduled tasks

## Utilities

- **CLAUDE.md** - Project instructions and guidelines for Claude Code
- **create_skill_zips.py** - Script to create zip archives of skills
- **verify_skills.py** - Script to verify skill structure and integrity
- **skill-zips/** - Directory containing packaged skill archives

## Tools

### create_skill_zips.py
Creates zip files for all skills in the repository.

```bash
python create_skill_zips.py
```

### verify_skills.py
Verifies all skill zip files for proper structure and content.

```bash
python verify_skills.py
```

## Requirements

- Python 3.13+
- Claude Code CLI

## Setup

1. Clone this repository
2. Run the scripts as needed
3. Use with Claude Code

## License

Personal use
