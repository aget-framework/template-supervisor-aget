# AGET Template Enhancement Proposals
## Based on RKB_analytics-aget Creation Experience

**Created**: 2025-09-26
**Source**: Lessons from first specialized agent creation
**Status**: Ready for extraction to aget-template

---

## Enhancement 1: Pre-installed Welcome Flag (REVISED)

### Problem
Runtime file creation (touch .aget/welcomed) causes bash confirmation interruptions.

### Solution
Pre-create welcomed flag during `aget init` to ensure smooth workflow.

### Design Decision
**Simplicity over hand-holding** - Professional tool, not tutorial.

### Implementation (for aget-template)

#### File: `aget-cli-agent-template/aget/config/commands/init.py`
```python
def create_aget_structure(self, target: Path):
    """Create .aget directory structure."""
    # Create directories
    (target / ".aget").mkdir(exist_ok=True)
    (target / ".aget/evolution").mkdir(exist_ok=True)
    (target / ".aget/checkpoints").mkdir(exist_ok=True)

    # Pre-create welcomed flag to avoid runtime interruptions
    (target / ".aget/welcomed").touch()  # NEW

    # Create version.json
    version_data = {
        "version": "1.0.0",
        "created": datetime.now().isoformat(),
        "template": self.template_name
    }
    # ...
```

#### File: `aget-cli-agent-template/templates/agent/AGENTS.md`
Simplified wake protocol without welcome check:

```markdown
### Wake Up Protocol
When user says "wake up" or "hey":
1. Show current directory and status
2. Check git status
3. Report readiness with agent type

### Quick Start
New to this agent? Try:
- "help" - See commands
- "demo" - Run demonstration
- "status" - View metrics
```

---

## Enhancement 2: Agent Type Awareness

### Problem
Generic "ready" message doesn't indicate agent specialization.

### Solution
Template should include agent_type variable throughout.

### Implementation (for aget-template)

```python
# In init.py, extend templates dict:
self.templates = {
    'agent': {
        'dirs': [...],
        'description': 'Full autonomous agent structure',
        'agent_type': 'general',  # NEW
        'primary_commands': ['status', 'help', 'explore'],  # NEW
    },
    'analytics': {  # NEW PERSONA
        'parent': 'agent',
        'agent_type': 'analytics',
        'primary_commands': ['status', 'insights', 'trends'],
        'voice': 'data-driven, visual, actionable'
    }
}
```

---

## Enhancement 3: Capability Discovery

### Problem
Users don't know what the agent can do without reading all files.

### Solution
Auto-generate capabilities list from src/ modules.

### Implementation (for aget-template)

```python
# New file: aget-cli-agent-template/aget/discovery.py
def discover_capabilities(src_path):
    """Scan src/ for Python modules and extract docstrings."""
    capabilities = []
    for py_file in Path(src_path).glob("*.py"):
        module_doc = extract_module_docstring(py_file)
        if module_doc:
            capabilities.append(f"- {py_file.stem}: {module_doc}")
    return capabilities

# In wake protocol:
if Path("src").exists():
    capabilities = discover_capabilities("src")
    print("Available modules:", capabilities)
```

---

## Enhancement 4: Demo Mode

### Problem
Users need to understand agent capabilities quickly.

### Solution
Add demo detection and execution.

### Implementation (for aget-template)

```python
# Add to AGENTS.md template:
demo_section = """## Demo Mode
When user says "demo" or "show me what you can do":
1. Check for src/*_demo.py or src/*_agent.py files
2. If found, run: python3 src/{main_module}.py
3. Show sample output
4. Explain what each part means
"""
```

---

## Enhancement 5: Data Source Clarity

### Problem
Agents confuse data sources with data subjects (e.g., "AWS Costs" as mission vs tool).

### Solution
Explicit data source section in template.

### Implementation (for aget-template)

```markdown
## Data Architecture
### Data Sources
- List external APIs or data sources
- Example: Google Analytics GA4, AWS Cost Explorer

### Data Subjects
- What the agent analyzes
- Example: Traffic patterns (325K bots/month), Infrastructure costs ($213/month)

### Data Storage
- data/ - Cached metrics and historical data
- workspace/ - Analysis experiments
- products/ - Reports and dashboards
```

---

## Where These Enhancements Should Live

### Phase 1: Prove in aget-aget (CURRENT)
- Location: `aget-aget/products/AGET_TEMPLATE_ENHANCEMENTS.md`
- Status: This document
- Purpose: Validate through real use

### Phase 2: Test in aget-aget
- Implement in next agent creation
- Refine based on experience
- Document what works

### Phase 3: Extract to aget-template
- Submit as PR to aget-cli-agent-template
- Location: `aget-cli-agent-template/aget/enhancements/`
- Include tests and documentation

---

## Immediate Actions for RKB_analytics-aget

Based on these enhancements, we should update:

1. **Add First Session Welcome** to AGENTS.md
2. **Clarify Data Sources vs Subjects**
3. **Add Demo Mode** section
4. **Create .aget/capabilities.json**
5. **Update wake protocol** with capability discovery

---

## Code to Add to aget-template

### Option 1: Minimal Change (Just Documentation)
- Update README.md with better examples
- Add FIRST_TIME_SETUP.md guide
- Include persona examples

### Option 2: Template Enhancement (Moderate)
- Extend init.py with persona support
- Add first-session detection
- Include capability discovery

### Option 3: Full Persona System (Comprehensive)
```bash
aget init --template agent --persona analytics
aget personas --list
aget personas --apply analytics
```

---

## Additional Enhancements

### Pre-Installation Pattern (NEW)
Based on welcomed flag success, we've identified a broader pattern for pre-installing files during init. See `PRE_INSTALLATION_PATTERN.md` for:
- Command history tracking
- Default checkpoint creation
- Performance baselines
- Decision criteria for what to pre-install

## Recommendation

Start with **Option 1** (documentation) for immediate value, then gradually implement **Option 2** features based on real usage patterns discovered in aget-aget.

The pattern is:
1. **Discover** need (in real agent creation)
2. **Implement** locally (in specific agent)
3. **Extract** pattern (to aget-aget/products/)
4. **Contribute** upstream (to aget-template)

This ensures we only add proven, valuable enhancements.