# Customization Guide

## Quick Start (< 5 minutes)

```bash
# Run the setup wizard
./setup.sh

# Answer the prompts
# Review generated files
# Start using immediately
```

## What Gets Customized

### Automatic (via setup.sh)
- **AGENTS.md**: Your project name and description
- **README.md**: Your governance layer documentation
- **Evolution tracking**: Initial setup record
- **CLAUDE.md**: Symlink created automatically

### Manual Customization Points

#### 1. Patterns Directory
```bash
patterns/
├── documentation/    # Keep or modify
├── session/         # Keep or modify
└── your-patterns/   # Add your own
```

#### 2. Products Directory
Remove example products you don't need:
```bash
products/
├── (keep what's useful)
└── (remove what's not)
```

#### 3. Scripts
Modify scripts for your workflow:
- `scripts/session_protocol.py` - Adjust session management
- `scripts/install_pattern.py` - Pattern installation logic

## Customization Levels

### Level 1: Basic (5 minutes)
- Run `./setup.sh`
- Use as-is

### Level 2: Intermediate (30 minutes)
- Run `./setup.sh`
- Remove unnecessary products
- Add your first pattern
- Customize AGENTS.md rules

### Level 3: Advanced (2+ hours)
- All of above
- Modify scripts
- Create custom patterns
- Build your workflow automation

## Finding Customization Points

Look for these markers in files:
- `{{PLACEHOLDER}}` - Replace via setup.sh
- `# CUSTOMIZE:` - Manual customization suggested
- `TODO:` - Implementation needed

## Common Customizations

### Adding Your Philosophy
Edit AGENTS.md or README.md:
```markdown
## Philosophy
1. Your principle here
2. Your approach here
```

### Adding Custom Commands
Edit AGENTS.md:
```markdown
## Custom Commands
When user says "your trigger":
- Your action here
```

### Creating Your First Pattern
```bash
mkdir -p patterns/my-patterns
echo "# My Pattern" > patterns/my-patterns/first.md
```

## Validation

After customization, run:
```bash
./validate.sh  # Checks your setup
```

## Tips

1. **Start Simple**: Don't over-customize initially
2. **Evolve Gradually**: Add patterns as you discover them
3. **Document Changes**: Use .aget/evolution/
4. **Keep Templates**: Don't delete templates/ directory

## Reset to Template

If you need to start over:
```bash
git reset --hard
./setup.sh
```

---
*Customization is iterative - start simple, evolve as needed*