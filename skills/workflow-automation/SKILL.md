---
name: workflow-automation
description: This skill should be used when automating repetitive workflows, creating task pipelines, setting up CI/CD processes, or orchestrating multi-step operations. It provides templates and scripts for common automation scenarios.
---

# Workflow Automation

Automates repetitive tasks and multi-step workflows with configurable pipelines and scripts.

## Purpose

Eliminates manual, repetitive work by automating common workflows. Provides templates for CI/CD pipelines, task automation, and orchestration of complex multi-step processes.

## When to Use

Use this skill when:
- Setting up CI/CD pipelines
- Automating deployment processes
- Creating scheduled tasks and cron jobs
- Orchestrating multi-step workflows
- Building release automation
- Setting up backup and sync processes
- Creating custom automation scripts

## Usage Guide

### CI/CD Pipeline Setup

To set up continuous integration:

1. Choose platform (GitHub Actions, GitLab CI, etc.)
2. Select workflow template from `assets/workflows/`
3. Customize steps and triggers
4. Test pipeline with sample changes

Example: "Set up GitHub Actions for Node.js testing"

### Deployment Automation

To automate deployments:

1. Define deployment steps
2. Set up environment configuration
3. Implement rollback procedures
4. Add deployment notifications

Use `scripts/deploy.py` for standardized deployment workflows.

### Scheduled Tasks

To create scheduled automation:

1. Define task schedule (cron syntax)
2. Write task script
3. Set up error handling and logging
4. Configure notifications for failures

Reference `references/cron-syntax.md` for scheduling patterns.

### Release Management

To automate releases:

1. Version bump automation
2. Changelog generation
3. Tag creation
4. Package publishing

Use `scripts/release.py` for release workflow automation.

### Backup Automation

To set up backups:

1. Define what to backup
2. Set backup schedule
3. Configure retention policy
4. Test restore procedures

Use `scripts/backup.sh` for automated backup workflows.

### Workflow Orchestration

To orchestrate complex workflows:

1. Break down into discrete steps
2. Define dependencies between steps
3. Implement error handling
4. Add progress tracking

Use `scripts/workflow_engine.py` for workflow orchestration.

## Bundled Resources

### Scripts

- `scripts/deploy.py` - Deployment automation script
- `scripts/release.py` - Release workflow automation
- `scripts/backup.sh` - Backup automation
- `scripts/workflow_engine.py` - Workflow orchestration engine
- `scripts/notification.py` - Notification helper

### References

- `references/cron-syntax.md` - Cron scheduling reference
- `references/ci-cd-patterns.md` - Common CI/CD patterns
- `references/deployment-strategies.md` - Deployment best practices
- `references/error-handling.md` - Error handling in automation

### Assets

- `assets/workflows/github-actions/` - GitHub Actions templates
- `assets/workflows/gitlab-ci/` - GitLab CI templates
- `assets/workflows/jenkins/` - Jenkins pipeline templates
- `assets/scripts/` - Reusable workflow scripts

## Best Practices

1. **Idempotency** - Workflows should be safe to run multiple times
2. **Error Handling** - Always handle and log errors
3. **Notifications** - Alert on failures, not just successes
4. **Testing** - Test workflows in non-production first
5. **Documentation** - Document what each workflow does
6. **Rollback** - Always have a rollback plan
7. **Monitoring** - Track workflow execution and success rates
