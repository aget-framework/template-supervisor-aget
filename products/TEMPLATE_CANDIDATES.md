# Template Candidates for aget-cli-agent-template

## Overview
Patterns and conventions discovered through real usage in my-aget-aget that should graduate to the public template.

---

## 1. Comprehensive Naming Convention 🏆

### Pattern Name
`AGET Safe Naming Convention`

### Description
A complete naming system that signals ownership, risk, and purpose through name structure.

### Components

#### Formula
```
[ownership]-[domain]-[persona]-aget
```

#### Rules
1. **Ownership prefix** (`my-`, `team-`, `corp-`)
   - `my-` = personal/private
   - `team-` = team shared
   - `corp-` = corporate
   - No prefix = public/uncertain

2. **Domain casing** (operation-based)
   - lowercase = read-only operations
   - UPPERCASE = write/modify operations

3. **Persona** (optional, defines commands)
   - analyst, curator, guardian, publisher, etc.
   - Only add when it clarifies role

4. **Suffix** (always `-aget`)

### Examples
```bash
# Safe personal agents
my-spotify-analyst-aget
my-notes-curator-aget
my-rkb-analytics-aget

# Dangerous personal agents
my-RKB_CONTENT-publisher-aget
my-DATABASE-migrator-aget

# Generic agents (no persona)
my-llm-judge-aget
my-aget-aget
```

### Template Integration
- Add to `docs/NAMING_CONVENTIONS.md`
- Include in agent creation wizard
- Validate in CI/CD

---

## 2. Persona-Based Command Mapping 🎭

### Pattern Name
`Persona Command Vocabularies`

### Description
Each persona has a specific set of commands that make semantic sense.

### Standard Personas

#### ANALYST
```python
commands = ["analyze", "compare", "trend", "report", "visualize"]
```

#### CURATOR
```python
commands = ["organize", "tag", "archive", "categorize", "showcase"]
```

#### GUARDIAN
```python
commands = ["guard", "patrol", "alert", "report-threats", "stand-watch"]
```

#### PUBLISHER
```python
commands = ["draft", "preview", "validate", "publish", "schedule"]
```

### Template Integration
- Create `patterns/personas/` directory
- Include persona templates
- Generate help text from persona

---

## 3. Security Patterns Suite 🔒

### Pattern Name
`Secure Credential Management`

### Components

#### A. Standard Secrets Directory
```bash
.aget/secrets/
├── .gitignore      # Mandatory
├── README.md       # Setup instructions
└── [credentials]   # 600 permissions
```

#### B. Secrets Manifest (secrets.yaml)
```yaml
required:
  - name: api_key
    type: token
    path: .aget/secrets/key
    permissions: "600"
    rotation_days: 90
```

#### C. Validation Script
```bash
scripts/validate_secrets.sh
```

### Template Integration
- Auto-create structure
- Include validation tools
- Add to .gitignore templates

---

## 4. Migration Patterns 🔄

### Pattern Name
`Auto-Activation Migration`

### Description
Migrations must auto-activate the agent identity, not leave it for manual steps.

### Required Components
1. Auto-replace AGENTS.md
2. Create verification script
3. Seed evolution data
4. Test identity activation

### Template Integration
- Update migration scripts
- Add verification step
- Include in documentation

---

## 5. Risk-Based Friction Patterns ⚠️

### Pattern Name
`Production Safety Friction`

### Description
High-risk agents require intentional friction to prevent accidents.

### Implementation
```bash
# Typed confirmation
$ ./run.sh
⚠️ HIGH RISK: Type 'publish-to-production-2025-09-26': _

# Segregated directory
PRODUCTION-AGENTS/
└── CONTENT-PUBLISHER-aget/
```

### Template Integration
- Add friction templates
- Include safety checks
- Document in security guide

---

## 6. Evolution Tracking Standards 📈

### Pattern Name
`Structured Evolution Tracking`

### Description
Standardized format for tracking decisions, discoveries, and lessons.

### Structure
```
.aget/evolution/
├── decisions/      # Strategic choices
├── discoveries/    # Patterns found
├── incidents/      # Issues and responses
└── optimizations/  # Improvements
```

### Template Integration
- Include in default structure
- Provide entry templates
- Add evolution commands

---

## 7. Two-Agent Collaboration Pattern 🤝

### Pattern Name
`Governance-Implementation Split`

### Description
Separate thinking (governance) from doing (implementation) with two specialized agents.

### Roles
- **my-aget-aget**: Strategy, patterns, governance
- **aget-template**: Implementation, building, testing

### Template Integration
- Document pattern
- Provide collaboration examples
- Include in advanced docs

---

## 8. Default Persona Pattern 🎯

### Pattern Name
`Optional Persona Specification`

### Description
Not all agents need explicit personas. Default AGET behavior is valid.

### Examples
```bash
my-project-aget         # Generic, no persona needed
my-tool-analyst-aget    # Specific analyst persona
```

### Template Integration
- Make persona optional in wizard
- Document when to use
- Provide decision tree

---

## Priority for Template

### High Priority (Security & Safety)
1. Naming Convention (prevents confusion)
2. Security Patterns (prevents breaches)
3. Risk Friction (prevents accidents)

### Medium Priority (Usability)
4. Persona Commands (improves UX)
5. Auto-Activation (reduces friction)
6. Default Persona (simplifies)

### Lower Priority (Advanced)
7. Evolution Tracking (power users)
8. Two-Agent Pattern (advanced users)

---

## Implementation Plan

### Phase 1: Documentation
- Add all patterns to docs/
- Create examples
- Update README

### Phase 2: Tooling
- Add to creation wizard
- Include validation scripts
- Update templates

### Phase 3: Enforcement
- Add CI/CD checks
- Create linting rules
- Provide migration tools

---

## Success Metrics
- Reduced naming confusion
- Fewer security incidents
- Faster agent creation
- Better pattern adoption

---

*Candidates identified: 2025-09-26*
*Source: my-aget-aget real-world usage*
*Status: Ready for graduation to template*