# my-AGET-template
*Template for creating AGET governance layers*

## What This Is
A snapshot template of a working AGET governance layer (my-AGET-aget). Use this to:
1. Create your own governance layer for managing multiple AGET agents
2. Restore my-AGET-aget to a known good state
3. Learn patterns for AGET ecosystem management

## Quick Start (For New Users)
```bash
# Clone this template
git clone https://github.com/aget-framework/my-AGET-template your-AGET-aget
cd your-AGET-aget

# Customize for your needs
# 1. Update AGENTS.md with your information
# 2. Remove example products you don't need
# 3. Start building your governance patterns

# Begin using
echo "wake up" # To start a session
```

## For my-AGET-aget Recovery
```bash
# If my-AGET-aget breaks, restore from this snapshot
cd /Users/aget-framework/github
cp -r my-AGET-template/* my-AGET-aget/
cp -r my-AGET-template/.aget my-AGET-aget/
```

## Structure Included
- **patterns/** - Working pattern library
- **scripts/** - Session management and utilities
- **products/** - Example governance products
- **.aget/** - Evolution tracking structure
- **docs/** - Documentation templates

## Relationship to AGET Ecosystem
- **aget-cli-agent-template**: Creates individual X-aget agents
- **my-AGET-template**: THIS - Template for governance layers
- **your-AGET-aget**: Your customized governance instance

## Version History
See VERSION.json for snapshot details.

---
*Private repository - Will be made public after validation*