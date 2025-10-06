# Customization Guide: Supervisor AGET

**Purpose**: Adapt template-supervisor-aget for your specific fleet and coordination needs
**Version**: 2.0 (v2.5.0 - supervisor-specific guidance added)
**Last Updated**: 2025-10-06

---

## Quick Start (< 5 minutes)

```bash
# Clone the template
git clone https://github.com/aget-framework/template-supervisor-aget my-supervisor-name

cd my-supervisor-name

# Update identity in .aget/version.json
# - agent_name: "my-supervisor-name" (match directory name)
# - instance_type: "AGET" (supervisors typically have write permissions)
# - domain: "coordination" or your domain

# Run contract tests to validate
python3 -m pytest tests/ -v
```

**Next**: Customize fleet registry (see Supervisor-Specific Customization below)

---

## Supervisor-Specific Customization

### 1. Fleet Registry (REQUIRED)

**File**: `.aget/registry/agents.yaml`

**Replace example agents with your actual fleet**:

```yaml
agents:
  - name: your-agent-name
    type: aget  # or AGET for action-taking
    version: "2.5.0"
    domain: your-domain  # e.g., github, data-analysis, deployment
    status: active  # or migration-pending, deprecated
    repository: https://github.com/your-org/your-agent-name
    managed_since: "2025-10-06"
    capabilities:
      - Specific capability 1
      - Specific capability 2
    notes: Brief description

  # Add all agents you supervise (aim for 5-15 per supervisor)
```

**Portfolio grouping**:
```yaml
portfolios:
  - name: your-portfolio-name
    description: Purpose of this portfolio
    agents:
      - agent-1
      - agent-2
    lead: agent-1  # Primary agent in portfolio
```

**Fleet statistics** (update manually or automate):
```yaml
fleet_stats:
  total_agents: 10
  active: 8
  migration_pending: 2
  version_distribution:
    "2.5.0": 8
    "2.4.0": 2
  last_updated: "2025-10-06"
```

**Why this matters**: Fleet registry is the source of truth for coordination. Supervisors reference this for:
- Version migration planning (which agents need upgrade)
- Work assignment (which agent has capability X)
- Issue routing (agent-specific problems route to that agent)
- Portfolio reorganization (move agents between portfolios)

---

### 2. Supervision Protocols (RECOMMENDED)

**File**: `AGENTS.md`

**Customize supervision patterns** for your team culture:

```markdown
## Supervision Patterns

### Our Team's Critique Standard
[Describe your team's feedback style]
- Quantitative rating: X/10
- Specific violations with evidence
- Actionable path forward

### Our Intervention Rules
[When do you intervene vs let agents proceed?]
- Intervene: [your criteria]
- Don't intervene: [your criteria]

### Our Quality Bar
[What quality level do you expect?]
- Code reviews: [standard]
- Documentation: [standard]
- Test coverage: [standard]
```

**Customize gate sizing** for your risk tolerance:

```markdown
## Gate Sizing for Our Team

**Our baseline**: [2-3 gates or different?]

**Our risk factors** (adjust weights):
- Reversibility: [+0-2 or different?]
- Impact Scope: [+0-2 or different?]
- Complexity: [+0-2 or different?]

**Examples from our work**:
- [Your simple task]: X gates
- [Your medium task]: Y gates
- [Your complex task]: Z gates
```

---

### 3. Issue Management (RECOMMENDED)

**File**: `AGENTS.md` (Issue Management section)

**Customize routing rules** for your team structure:

```markdown
## Issue Management

### Our Routing Rules
- **Critical issues** → [your escalation path]
- **Framework/cross-cutting** → [owner]
- **Agent-specific** → [routing logic]
- **Human-filed** → [owner]
- **Default** → [fallback owner]

### Our SLA Expectations
[Adjust based on your team's capacity]
- Critical: Acknowledge in [time], resolve in [time]
- High: Acknowledge in [time], resolve in [time]
- Medium: Acknowledge in [time], resolve in [time]
- Low: Acknowledge in [time], resolve in [time]
```

**Repository configuration**:

Update scripts in `.aget/patterns/github/` to point to your hub repository:
- `list_issues.py`: Change `DEFAULT_REPO = "aget-framework/aget"` to your hub repo
- `create_issue.py`: Change hub repo reference
- `assign_issue.py`: Update owner list to your agents

---

### 4. Portfolio Structure (OPTIONAL)

**File**: `.aget/registry/agents.yaml`

**Design portfolio grouping** that matches your architecture:

**Option A: By Domain**
```yaml
portfolios:
  - name: data-portfolio
    agents: [data-agent-1, data-agent-2, analytics-agent]
  - name: automation-portfolio
    agents: [github-agent, deployment-agent, monitoring-agent]
  - name: research-portfolio
    agents: [web-research-agent, document-analyzer-agent]
```

**Option B: By System/Product**
```yaml
portfolios:
  - name: product-x-portfolio
    agents: [x-frontend-agent, x-backend-agent, x-deployment-agent]
  - name: product-y-portfolio
    agents: [y-api-agent, y-data-agent, y-monitoring-agent]
```

**Option C: By Capability Level** (Salesforce-inspired)
```yaml
portfolios:
  - name: level-3-autonomous  # Highest capability
    agents: [agent-with-full-authority]
  - name: level-2-supervised
    agents: [agent-with-limited-authority]
  - name: level-1-readonly
    agents: [agent-with-no-write-access]
```

**Why this matters**: Portfolio structure affects:
- Work assignment (route work to portfolio, let lead assign)
- Migration coordination (migrate portfolio as unit)
- Access control (portfolio-level permissions)
- Reporting (portfolio-level metrics)

---

### 5. Evolution Log Setup (RECOMMENDED)

**Directory**: `.aget/evolution/`

**Create initial evolution logs** documenting setup:

```bash
# Example: Document your fleet's baseline
cat > .aget/evolution/L001_initial_fleet_baseline.md <<'EOF'
# L001: Initial Fleet Baseline

**Date**: 2025-10-06
**Context**: Setting up supervisor for [your organization]

## Decision
Starting with [N] agents across [M] portfolios:
- Portfolio A: [agents]
- Portfolio B: [agents]

## Rationale
[Why this structure?]

## Consequences
- [Expected benefit 1]
- [Expected challenge 1]

## Alternatives Considered
- [Alternative structure]: Rejected because [reason]
EOF
```

**Customize L-number sequence**:
- Template reserves L001-L199 for teaching examples
- **Your fleet starts at L200+** to avoid conflicts
- Document this in `.aget/evolution/README.md`

---

### 6. Multi-Level Hierarchies (ADVANCED)

**For fleets with >20 agents**: Consider recursive supervision

**File**: `.aget/registry/agents.yaml`

```yaml
agents:
  - name: portfolio-a-supervisor
    type: AGET
    version: "2.5.0"
    domain: coordination
    status: active
    repository: https://github.com/your-org/portfolio-a-supervisor
    managed_since: "2025-10-06"
    capabilities:
      - Supervise 10 agents in Portfolio A
    supervisor: top-level-coordinator  # This supervisor is also supervised!

  - name: portfolio-b-supervisor
    type: AGET
    version: "2.5.0"
    domain: coordination
    status: active
    repository: https://github.com/your-org/portfolio-b-supervisor
    managed_since: "2025-10-06"
    capabilities:
      - Supervise 12 agents in Portfolio B
    supervisor: top-level-coordinator
```

**Structure**:
```
Human
  └─ top-level-coordinator (you)
      ├─ portfolio-a-supervisor
      │   └─ [10 worker agents]
      └─ portfolio-b-supervisor
          └─ [12 worker agents]
```

**Recursive Supervision Model (L99)**: Every agent is a worker. Supervision is a capability, not a type.

---

## Standard Customization (All Agents)

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
├── EXAMPLE_3_GATE_PLAN.md    # Keep as reference or remove
├── EXAMPLE_7_GATE_PLAN.md    # Keep as reference or remove
├── DEMONSTRATION_GUIDE.md    # Keep as reference or remove
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