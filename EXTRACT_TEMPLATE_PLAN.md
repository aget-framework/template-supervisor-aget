# Plan: Extract aget-aget-template from my-aget-aget

## Purpose
Create a reusable template so other contributors can quickly set up their own pattern laboratories.

## What to Extract (Keep)

### Structure
```
aget-aget-template/
├── .aget/
│   ├── evolution/
│   │   ├── decisions/
│   │   ├── discoveries/
│   │   └── README.md
│   ├── version.json.template
│   └── capabilities.json.template
├── patterns/
│   ├── migration/
│   ├── security/
│   ├── governance/
│   └── README.md
├── governance/
│   ├── FRAMEWORK_REQUIREMENTS.md.template
│   ├── NEXT_ACTIONS.md.template
│   └── README.md
├── vision/
│   ├── enhancements/
│   └── README.md
├── workspace/
│   └── README.md
├── products/
│   └── README.md
├── sessions/
│   └── README.md
├── AGENTS.md.template
├── README.md.template
└── setup.sh
```

### Template Files to Create

#### setup.sh
```bash
#!/bin/bash
echo "Setting up your AGET Pattern Laboratory"
read -p "Enter your name/identifier: " OWNER
read -p "Enter your lab name (must end with -aget): " LAB_NAME

# Validate name ends with -aget
if [[ ! "$LAB_NAME" =~ -aget$ ]]; then
  echo "Lab name must end with '-aget'"
  exit 1
fi

# Personalize templates
sed -i "s/{{OWNER}}/$OWNER/g" README.md
sed -i "s/{{LAB_NAME}}/$LAB_NAME/g" README.md
mv README.md.template README.md

echo "✅ Your pattern laboratory '$LAB_NAME' is ready!"
echo "📝 Start documenting patterns in patterns/"
echo "🔬 Track experiments in workspace/"
echo "📊 Document governance in governance/"
```

#### README.md.template
```markdown
# {{LAB_NAME}}: {{OWNER}}'s AGET Pattern Laboratory

This is {{OWNER}}'s personal space for:
- Extracting patterns from AGET agents
- Experimenting with framework enhancements
- Pre-validating contributions
- Learning from failures privately

Based on aget-aget-template.

## Quick Start

1. Document patterns in `patterns/`
2. Track experiments in `workspace/`
3. Record decisions in `.aget/evolution/`
4. Contribute proven patterns to aget-cli-agent-template
```

## What to Remove (Personal Content)

### Remove Completely
- All current evolution entries (my discoveries)
- Specific patterns I've documented
- My governance decisions
- Session documents
- Personal workspace experiments

### Replace with Templates
- Governance documents → Template versions
- Patterns → Example structure only
- Evolution entries → Seed examples

## Seed Content to Include

### Example Pattern
```markdown
# patterns/example/EXAMPLE_PATTERN.md
# Example Pattern Structure

## Pattern Name
Brief description

## Problem
What problem does this solve?

## Solution
How to implement

## Example
Code/configuration example

## When to Use
Guidelines

## When Not to Use
Anti-patterns
```

### Example Evolution Entry
```json
{
  "timestamp": "{{DATE}}",
  "type": "discovery|decision|lesson",
  "title": "Your discovery here",
  "description": "What you learned",
  "impact": "How it affects AGET"
}
```

## The Extraction Process

1. **Copy Structure**
   ```bash
   cp -r aget-aget aget-aget-template
   cd aget-aget-template
   ```

2. **Clean Personal Content**
   ```bash
   rm -rf .aget/evolution/discoveries/*
   rm -rf .aget/evolution/decisions/*
   rm -rf patterns/*/*_PATTERN.md
   rm -rf sessions/*
   rm -rf workspace/*
   rm -rf products/*
   ```

3. **Add Templates**
   - Create .template versions of key files
   - Add setup.sh script
   - Add example patterns

4. **Document**
   - Clear README for the template
   - CONTRIBUTING guide
   - Examples of each pattern type

5. **Test**
   ```bash
   cd /tmp
   git clone aget-aget-template test-lab-aget
   cd test-lab-aget
   ./setup.sh
   # Verify personalization works
   ```

## Success Criteria

A new contributor can:
1. Clone the template
2. Run setup.sh
3. Have a functional pattern laboratory in < 5 minutes
4. Understand where to document patterns
5. Know how to contribute upstream

## Timeline

1. **Today**: Plan extraction (this document)
2. **Tomorrow**: Create aget-aget-template repo
3. **This week**: Test with hypothetical user
4. **Next week**: Announce in aget-cli-agent-template

## The Meta Beauty

We're using my-aget-aget to create aget-aget-template, which will help others create their-aget-aget to contribute patterns to aget-cli-agent-template.

It's patterns all the way down! 🐢

---

*Extraction planned: 2025-09-26*
*Target: Create aget-aget-template for contributors*