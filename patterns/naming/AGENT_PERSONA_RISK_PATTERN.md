# Agent Persona as Risk Signal Pattern

## The Insight
Agent personas naturally map to risk levels! The persona type immediately conveys capabilities and danger.

## Core Personas by Risk Level

### 🟢 Safe Personas (Read-Only)
```bash
my-spotify-ANALYST-aget         # Analyzes data
my-RKB-OBSERVER-aget           # Watches systems
my-costs-AUDITOR-aget          # Reviews spending
my-logs-DETECTIVE-aget         # Investigates issues
team-code-REVIEWER-aget        # Reviews code
my-health-TRACKER-aget         # Tracks metrics
```

**Personas**: ANALYST, OBSERVER, AUDITOR, DETECTIVE, REVIEWER, TRACKER, MONITOR, WATCHER

### 🟡 Medium Risk Personas (Local/Reversible)
```bash
my-notes-CURATOR-aget          # Organizes content
my-files-LIBRARIAN-aget        # Manages collections
my-music-ORGANIZER-aget        # Arranges files
my-git-ASSISTANT-aget          # Helps with tasks
my-email-COMPOSER-aget         # Drafts content
my-backup-KEEPER-aget          # Maintains backups
```

**Personas**: CURATOR, LIBRARIAN, ORGANIZER, ASSISTANT, COMPOSER, KEEPER, MANAGER

### 🔴 High Risk Personas (Production/Irreversible)
```bash
my-RKB_CONTENT-PUBLISHER-aget    # Publishes content
INFRA-OPERATOR-aget              # Operates systems
DATABASE-SURGEON-aget            # Precise modifications
PROD-DEPLOYER-aget               # Deploys code
AWS-CONTROLLER-aget              # Controls infrastructure
SYSTEM-EXECUTOR-aget             # Executes commands
```

**Personas**: PUBLISHER, OPERATOR, SURGEON, DEPLOYER, CONTROLLER, EXECUTOR, COMMANDER

## Extended Persona Mapping

### Information Gathering Personas (🟢 Safe)
```bash
RESEARCHER    # Deep investigation
ANALYST       # Data analysis
DETECTIVE     # Problem solving
SCHOLAR       # Knowledge gathering
OBSERVER      # System watching
AUDITOR       # Compliance checking
```

### Creative/Organizing Personas (🟡 Medium)
```bash
CURATOR       # Content curation
LIBRARIAN     # Information organization
COMPOSER      # Content creation (drafts)
DESIGNER      # Structure planning
ARCHITECT     # System design (plans only)
ORGANIZER     # File management
```

### Action-Taking Personas (🔴 Dangerous)
```bash
PUBLISHER     # Makes content public
OPERATOR      # Runs operations
SURGEON       # Precise, critical changes
CONTROLLER    # System control
EXECUTOR      # Command execution
DEPLOYER      # Production deployment
```

## Special Personas with Context

### The GUARDIAN Persona (Variable Risk)
```bash
my-RKB_INFRA-GUARDIAN-aget       # 🟢 Read-only monitoring (like InfraGuard)
my-DATABASE-GUARDIAN-aget        # 🟢 Watches for issues
my-SECURITY-GUARDIAN-aget        # 🟡 May quarantine threats
```
GUARDIAN = Protective watching, usually safe

### The DOCTOR Persona (Variable Risk)
```bash
my-system-DOCTOR-aget            # 🟡 Diagnoses issues
my-DATABASE-DOCTOR-aget          # 🔴 May perform surgery!
```
DOCTOR = Diagnosis + potential treatment

### The PILOT Persona (High Risk)
```bash
my-DEPLOYMENT-PILOT-aget         # 🔴 Guides deployments
my-MIGRATION-PILOT-aget          # 🔴 Navigates changes
```
PILOT = Active navigation/control

## Persona Personality Traits

### Safe Personas Think/Observe
- Analytical
- Observant
- Studious
- Investigative
- Careful

### Medium Personas Organize/Create
- Methodical
- Creative
- Helpful
- Organized
- Thoughtful

### Dangerous Personas Act/Change
- Decisive
- Bold
- Authoritative
- Powerful
- Irreversible

## Real Examples with Personas

### Current → Persona-Based
```bash
# Before
RKB_infrastructure → my-RKB_INFRA-GUARDIAN-aget
RKB_analytics → my-RKB-ANALYST-aget
RKB_content-enhancement → RKB_CONTENT-PUBLISHER-aget
spotify-aget → my-spotify-ANALYST-aget

# The persona immediately tells you what it does!
```

### InfraGuard Reconsidered
```bash
# Original
my-RKB_INFRA-monitor-aget

# With Persona
my-RKB_INFRA-GUARDIAN-aget    # Perfect! Guardian = protective watcher
```

## Persona Combination Rules

### Can Combine Related Personas
```bash
my-code-ANALYST_REVIEWER-aget    # Analyzes AND reviews
my-data-DETECTIVE_ANALYST-aget   # Investigates AND analyzes
```

### Cannot Combine Conflicting Risks
```bash
# BAD: Mixed risk levels
my-code-ANALYST_PUBLISHER-aget   # NO! Safe + Dangerous

# GOOD: Split into separate agents
my-code-ANALYST-aget            # Safe analysis
my-code-PUBLISHER-aget          # Dangerous publishing
```

## The Cognitive Load Test

Which tells you more?

### Generic Risk Words
```bash
my-RKB-monitor-aget           # What does it monitor?
my-RKB-manager-aget           # What does it manage?
my-RKB-operator-aget          # What operations?
```

### Specific Personas
```bash
my-RKB-GUARDIAN-aget          # Protective watcher
my-RKB-CURATOR-aget           # Content organizer
my-RKB-PUBLISHER-aget         # Content publisher
```

**Personas win!** They convey both risk AND purpose.

## Implementation Guidelines

### 1. Choose Primary Persona
What is the agent's main role?
- Watching? → OBSERVER/GUARDIAN
- Analyzing? → ANALYST/DETECTIVE
- Organizing? → CURATOR/LIBRARIAN
- Publishing? → PUBLISHER/DEPLOYER

### 2. Apply Risk-Based Casing
- Safe personas: lowercase or Title Case
- Dangerous personas: UPPERCASE

### 3. Let Persona Drive Behavior
```python
class AnalystAgent:
    """I analyze but never modify."""
    read_only = True

class PublisherAgent:
    """I publish content to production."""
    requires_confirmation = True
    danger_level = "HIGH"
```

## The Meta Pattern

Agent personas are like job titles:
- **ANALYST** = Data scientist (safe)
- **CURATOR** = Museum curator (organizing)
- **SURGEON** = Brain surgeon (precise, dangerous)
- **PUBLISHER** = Newspaper publisher (public impact)

The job title immediately conveys:
1. What they do
2. How careful to be around them
3. What authority they have

## Final Examples

```bash
# Your ecosystem with personas
my-spotify-ANALYST-aget           # Analyzes music data
my-aget-ARCHITECT-aget            # Designs patterns (my-aget-aget!)
my-notes-CURATOR-aget             # Organizes notes
my-RKB_CONTENT-PUBLISHER-aget     # Publishes content
my-RKB_INFRA-GUARDIAN-aget        # Watches infrastructure
my-finance-AUDITOR-aget           # Reviews spending
my-code-REVIEWER-aget             # Reviews pull requests
PRODUCTION-SURGEON-aget           # Critical operations
```

---
*Pattern created: 2025-09-26*
*Insight: Personas convey both purpose and risk*
*Benefit: Richer semantics than generic risk words*