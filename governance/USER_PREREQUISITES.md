# Prerequisites and Assumptions

## Overview
This document outlines what we assume users already know and have configured before working with AGET.

## Required Knowledge

### Git Fundamentals
Users should understand:
- Basic git operations (add, commit, push, pull)
- Branch management
- Remote repository concepts
- Git configuration (user.name, user.email)

### Repository Management
Users should know how to:
- Create repositories on GitHub/GitLab/Bitbucket
- Decide between public and private repositories
- Manage repository permissions
- Understand personal vs organization accounts
- Use repository naming conventions

**Lesson Learned**: The DeepResearch-aget creation revealed we must explicitly ask:
1. **WHERE** - GitHub? GitLab? Local only?
2. **VISIBILITY** - Public or private?
3. **ACCOUNT** - Personal or organization?
4. **NAME** - Exact repository name
5. **TIMING** - Create remote first or after scaffolding?

### Command Line Proficiency
- Navigation (cd, ls, pwd)
- File operations (cp, mv, rm, mkdir)
- Text editing (vim, nano, or preferred editor)
- Environment variables
- Shell basics (bash/zsh)

## Required Tools

### Essential
- **Git**: Version 2.x or higher
- **Python**: 3.8 or higher
- **Text Editor**: Any preferred editor

### Highly Recommended
- **GitHub CLI (`gh`)**: For repository creation and management
  - Install: `brew install gh` (macOS) or see [cli.github.com](https://cli.github.com)
  - Configure: `gh auth login`
  - Why: Enables seamless repository creation during AGET setup

### Optional but Helpful
- **Make**: For running Makefile commands
- **Docker**: For containerized development
- **VS Code/Cursor**: For integrated development

## Configuration Assumptions

### Git Configuration
We assume you have already:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### GitHub CLI Configuration
If using GitHub, we assume:
```bash
gh auth login  # Already authenticated
gh auth status # Shows active account
```

### SSH Keys (Optional)
For SSH-based git operations:
- SSH key generated and added to GitHub/GitLab
- SSH agent running with key loaded

## Platform Assumptions

### Operating System
- **Primary Support**: macOS, Linux
- **Secondary Support**: Windows with WSL2
- **Note**: Native Windows may require adaptations

### File System
- Case-sensitive file system awareness
- Understanding of hidden files (dotfiles)
- Ability to work with symbolic links

## Conceptual Prerequisites

### Agent Concepts
- Understanding of autonomous agents
- Cognitive enhancement principles
- Memory and evolution tracking concepts

### Software Patterns
- Model-View-Controller (MVC) basics
- Repository patterns
- Configuration management
- Testing fundamentals

## What We DON'T Assume

### Not Required
- Advanced Python programming (AGET handles complexity)
- Deep AI/ML knowledge (framework abstracts this)
- DevOps expertise (basic git is sufficient)

### We'll Guide You Through
- AGET-specific patterns
- Evolution tracking system
- Memory implementation
- Agent personality design

## Common Pitfalls

### Repository Confusion
**Problem**: Creating AGET in wrong repository or orphaning locally
**Solution**: Always establish repository location BEFORE creating AGET

### Missing GitHub CLI
**Problem**: Manual repository creation interrupts flow
**Solution**: Install and configure `gh` before starting

### Uncommitted Changes
**Problem**: Losing work due to git confusion
**Solution**: Use AGET session management (wake/wind-down/sign-off)

## Quick Prerequisite Check

Run this to verify your setup:
```bash
# Check git
git --version

# Check Python
python3 --version

# Check GitHub CLI (if using GitHub)
gh --version
gh auth status

# Check current directory is a git repo
git status

# Check remote configuration
git remote -v
```

If all commands work, you're ready for AGET!

## Getting Help

### If Prerequisites Missing
1. **Git**: [git-scm.com/book](https://git-scm.com/book)
2. **GitHub CLI**: [cli.github.com](https://cli.github.com)
3. **Python**: [python.org](https://python.org)

### If Concepts Unclear
- Review AGET documentation in aget-cli-agent-template
- Check case studies in sessions/
- Ask in GitHub issues

---
*Last Updated: 2025-09-25*
*Lesson from DeepResearch-aget creation incorporated*