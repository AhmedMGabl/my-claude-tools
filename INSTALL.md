# Installing and Using Custom Skills

## Installation Methods

### Method 1: Install from Packaged Zip Files

1. **Locate the packaged skills:**
   ```
   packaged-skills/
   ├── api-wrapper.zip
   ├── code-standards-checker.zip
   ├── development-helper.zip
   ├── doc-generator.zip
   ├── file-batch-processor.zip
   └── workflow-automation.zip
   ```

2. **Install via Claude Code CLI:**
   ```bash
   # Install a single skill
   claude skills add packaged-skills/development-helper.zip

   # Or install all skills at once
   claude skills add packaged-skills/*.zip
   ```

3. **Verify installation:**
   ```bash
   claude skills list
   ```

### Method 2: Install from Source Directory

If you prefer to work directly with the source:

```bash
# Install from source directory
claude skills add skills/development-helper/

# Or install all
claude skills add skills/*/
```

## Using Skills

### Automatic Triggering

Skills automatically activate when Claude detects relevant tasks based on the skill's description:

**Examples:**

- **development-helper** triggers when you say:
  - "Set up a new Node.js project"
  - "Check my dependencies for updates"
  - "Run the test suite"

- **file-batch-processor** triggers when you say:
  - "Rename all JPG files with today's date"
  - "Convert all PNG files to WebP"
  - "Find duplicate files in this directory"

- **api-wrapper** triggers when you say:
  - "Call the GitHub API to get my repos"
  - "Make a POST request to this endpoint"
  - "Integrate with the Stripe API"

- **doc-generator** triggers when you say:
  - "Generate a README for this project"
  - "Create API documentation"
  - "Update the changelog"

- **code-standards-checker** triggers when you say:
  - "Check my code for style violations"
  - "Run linting on all Python files"
  - "Review this code for standards compliance"

- **workflow-automation** triggers when you say:
  - "Set up GitHub Actions for testing"
  - "Create a deployment workflow"
  - "Automate my release process"

### Manual Skill Invocation

You can also explicitly invoke skills using slash commands:

```bash
# List available skills
/skills

# Use a specific skill
/skill development-helper

# Or reference in your message
"Use the development-helper skill to set up my project"
```

## Skill Management

### List Installed Skills
```bash
claude skills list
```

### Remove a Skill
```bash
claude skills remove development-helper
```

### Update a Skill
```bash
# Remove old version
claude skills remove development-helper

# Install new version
claude skills add packaged-skills/development-helper.zip
```

### View Skill Details
```bash
claude skills info development-helper
```

## Examples of Using Your Custom Skills

### Example 1: Setting Up a New Project
```
You: "Set up a new Python project with testing and linting"

Claude: *Activates development-helper skill*
- Creates project structure
- Sets up virtual environment
- Installs dependencies
- Configures pre-commit hooks
- Runs health check
```

### Example 2: Batch File Operations
```
You: "Rename all my photos from the trip to include the date"

Claude: *Activates file-batch-processor skill*
- Uses batch_rename.py script
- Shows preview of changes
- Applies renaming pattern
```

### Example 3: API Integration
```
You: "Help me integrate with the GitHub API"

Claude: *Activates api-wrapper skill*
- Uses api_client.py as template
- Configures authentication
- Implements rate limiting
- Adds error handling
```

### Example 4: Code Review
```
You: "Review my code for standards compliance"

Claude: *Activates code-standards-checker skill*
- Runs check_standards.py
- Reports violations
- Suggests fixes
```

## Tips for Effective Skill Usage

1. **Be Specific:** The more specific your request, the better Claude can activate the right skill
2. **Natural Language:** Just describe what you want to do - skills activate automatically
3. **Combine Skills:** Claude can use multiple skills together for complex tasks
4. **Script Access:** Skills provide scripts that Claude can execute directly
5. **Templates:** Skills with templates give Claude ready-to-use boilerplate

## Troubleshooting

### Skill Not Activating?

If a skill doesn't activate automatically:
- Try being more specific in your request
- Explicitly mention the skill type (e.g., "use file batch processing")
- Invoke it manually with `/skill <skill-name>`

### Check Installation:
```bash
# Verify skill is installed
claude skills list | grep development-helper

# Reinstall if needed
claude skills add packaged-skills/development-helper.zip --force
```

### View Skill Logs:
```bash
# Check Claude Code logs for skill loading issues
claude logs
```

## Sharing Skills

To share your skills with others:

1. **Share the zip file:**
   ```bash
   # Send them the packaged zip
   packaged-skills/development-helper.zip
   ```

2. **They install it:**
   ```bash
   claude skills add development-helper.zip
   ```

3. **Or share via GitHub:**
   - Direct them to: https://github.com/AhmedMGabl/my-claude-tools
   - They can download and install from there

## Next Steps

- ✅ Install the skills you want to use
- ✅ Try them out with real tasks
- ✅ Customize scripts for your needs
- ✅ Create more skills as needed
- ✅ Share your skills with your team
