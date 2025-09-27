# AGET-AGET-Template Proposal
*A template for contributors who want their own pattern laboratory*

## The Problem Solved
- `aget-cli-agent-template` is for creating agents (99% of users)
- Only ~1% want to contribute patterns back
- Those contributors need a private experimentation space
- Don't burden the main template with contributor-specific tooling

## The Solution: aget-aget-template

A separate template specifically for creating your own pattern laboratory.

## What It Would Contain

### Core Structure
```
aget-aget-template/
├── .aget/                     # Yes, even governance labs are AGETs!
│   ├── evolution/            # Track your governance decisions
│   └── patterns/             # Meta-patterns for pattern extraction
├── patterns/                 # Your discovered patterns
│   ├── migration/           # Migration patterns
│   ├── security/            # Security patterns
│   └── [categories]/        # Your pattern categories
├── governance/              # Your governance docs
│   ├── FRAMEWORK_REQUIREMENTS.md
│   ├── SECURITY_STANDARDS.md
│   └── NEXT_ACTIONS.md
├── vision/                  # Your vision for AGET
├── experiments/             # Sandbox for wild ideas
├── tools/                   # Pattern extraction tools
│   ├── extract_pattern.py
│   ├── validate_pattern.py
│   └── contribute_pattern.sh
├── AGENTS.md               # Your lab's agent configuration
├── README.md               # Explains this is YOUR lab
└── CONTRIBUTING_UPSTREAM.md # How to contribute to aget-cli-agent-template
```

### Key Features

#### 1. Pattern Extraction Tools
```python
# tools/extract_pattern.py
"""
Helps extract patterns from your agents:
- Scans agent repositories
- Identifies common patterns
- Formats for contribution
"""
```

#### 2. Contribution Workflow
```bash
# tools/contribute_pattern.sh
#!/bin/bash
# Validates pattern
# Creates PR to aget-cli-agent-template
# Tracks contribution status
```

#### 3. Meta-Evolution Tracking
Your aget-aget itself evolves! Track:
- Governance decisions
- Pattern extraction methods
- Contribution successes/failures

#### 4. Pre-configured Documentation
```markdown
# README.md
# My AGET Pattern Laboratory (my-aget-aget)

This is my personal space for:
- Extracting patterns from my agents
- Experimenting with AGET enhancements
- Pre-validating contributions
- Documenting my AGET journey

Based on aget-aget-template.
```

## Usage Flow

### For New Contributors
```bash
# 1. Create your lab
git clone https://github.com/[user]/aget-aget-template my-aget-aget
cd my-aget-aget

# 2. Personalize
./setup.sh --owner "YourName"

# 3. Start extracting patterns
./tools/scan_agents.py ../my-agents/

# 4. Contribute back
./tools/contribute_pattern.sh patterns/security/my_pattern.md
```

### For Existing aget-aget (yours)
You could:
1. Keep `aget-aget` as is (you're the original!)
2. Extract the template from your experience
3. Help others create their own

## The Ecosystem

```
aget-cli-agent-template (for making agents)
         ↑
    Patterns flow up
         ↑
[Multiple Personal Labs]
alice-aget-aget  bob-aget-aget  corp-aget-aget
         ↑
  Created from
         ↑
aget-aget-template (for making labs)
         ↑
  Extracted from
         ↑
aget-aget (the original - yours!)
```

## Benefits

### For Contributors
- Ready-made structure
- Pattern extraction tools
- Contribution workflow
- Learn from the template itself

### For Main Template
- Stays focused on agents
- Not cluttered with governance
- Cleaner for regular users

### For Ecosystem
- Standardized pattern format
- Quality contributions
- Distributed innovation
- Meta-learning (patterns about patterns)

## Implementation Steps

1. **Extract from your aget-aget**
   - Remove personal content
   - Keep structure and tools
   - Add setup script

2. **Create aget-aget-template repo**
   - Public repository
   - Clear documentation
   - Link from main template

3. **Document in main template**
   ```markdown
   ## For Contributors

   Want to contribute patterns? Create your pattern lab:
   → https://github.com/[user]/aget-aget-template

   This gives you tools for pattern extraction and validation.
   ```

4. **Your aget-aget becomes reference implementation**
   - The original lab
   - Shows what's possible
   - Inspires others

## Naming Convention

All pattern labs MUST end with `-aget`:
- `my-aget-aget` ✓
- `alice-aget-aget` ✓
- `corp-patterns-aget` ✓
- `research-lab-aget` ✓
- `aget-laboratory` ✗ (doesn't end with -aget)

## Success Metrics

- Number of labs created from template
- Quality of pattern contributions
- Reduced friction for new contributors
- Clear separation of concerns

## The Philosophy

**"Every gardener needs a greenhouse, but not every gardener needs to build one from scratch"**

- aget-cli-agent-template = Seeds for gardens (agents)
- aget-aget-template = Blueprint for greenhouses (labs)
- Individual aget-agets = Actual greenhouses where experimentation happens

---

*Proposal created: 2025-09-26*
*Status: Concept - needs validation*
*Next: Extract template from current aget-aget*