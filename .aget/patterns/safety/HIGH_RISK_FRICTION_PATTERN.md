# High-Risk Agent Friction Pattern

## The Principle
Just as `my-` adds cognitive friction for privacy, high-risk agents need operational friction for safety.

## Naming Friction

### 🔴 Option 1: UPPERCASE Danger Signal
```bash
RKB-CONTENT-PUBLISHER-aget    # SCREAMS danger
INFRA-OPERATOR-aget           # Can't miss this
DATABASE-MIGRATOR-aget        # Obviously serious

# vs safe agents
my-spotify-analytics-aget     # lowercase = safe
my-notes-manager-aget         # normal case = normal risk
```

### 🔴 Option 2: Explicit PROD Marker
```bash
RKB-content-PROD-publisher-aget
infra-PROD-operator-aget
database-PROD-migrator-aget

# Makes target environment unmistakable
```

### 🔴 Option 3: Warning Prefix
```bash
DANGER-rkb-content-publisher-aget
PROD-infra-operator-aget
LIVE-database-migrator-aget
```

## Operational Friction

### 1. Required Confirmation File
High-risk agents require `.confirm-production` file to run:

```bash
# In the agent directory
$ cat .confirm-production
I understand this agent modifies PRODUCTION.
Last confirmed: 2025-09-26 by GM
Target: RKB Production Wiki
Impact: Public content changes

# Agent checks:
if not os.path.exists('.confirm-production'):
    print("⛔ PRODUCTION AGENT - Create .confirm-production to proceed")
    sys.exit(1)
```

### 2. Two-Step Execution
```bash
# Instead of direct execution
$ ./run.sh  # FAILS

# Require explicit unlock
$ ./unlock-production.sh  # Creates 5-minute window
$ ./run.sh  # Now works

# After 5 minutes, auto-locks again
```

### 3. Typed Confirmation
```bash
$ ./run.sh
⚠️  HIGH RISK: This publishes to PRODUCTION RKB
⚠️  Type 'publish-to-production' to continue: _

# Must type exact phrase, not just 'y' or 'yes'
```

### 4. Environment Variable Gate
```bash
# High-risk agents check for explicit permission
if os.environ.get('ALLOW_PRODUCTION_CHANGES') != 'TRUE':
    print("Set ALLOW_PRODUCTION_CHANGES=TRUE to run production agents")
    sys.exit(1)

# User must:
$ export ALLOW_PRODUCTION_CHANGES=TRUE
$ ./run.sh
```

### 5. Time-Based Friction
```python
# Prevent accidental 3am disasters
from datetime import datetime

hour = datetime.now().hour
if hour < 6 or hour > 22:  # Outside 6am-10pm
    response = input("⚠️ Running production agent outside business hours. Type 'override': ")
    if response != 'override':
        sys.exit(1)
```

## Directory Structure Friction

### Separate Dangerous Agents
```bash
github/
├── my-agents/           # Safe personal agents
│   ├── my-spotify-analytics-aget/
│   └── my-notes-manager-aget/
└── PRODUCTION-AGENTS/   # Segregated danger zone
    ├── RKB-CONTENT-PUBLISHER-aget/
    └── INFRA-OPERATOR-aget/
```

The uppercase directory name adds visual friction.

## Configuration Friction

### Required Production Config
```yaml
# .aget/production.yaml (required for high-risk agents)
production:
  confirmed: true
  last_review: "2025-09-26"
  reviewer: "GM"
  targets:
    - "RKB Production Wiki"
    - "Live Infrastructure"
  require_confirmation: true
  confirmation_phrase: "modify-production-{date}"

# Agent won't run without this file
```

## Medium Risk Clarification

You're right that MEDIUM is less clear. Perhaps:

### 🟡 Medium = Reversible Personal Changes
```bash
my-files-organizer-aget     # Moves YOUR files (but reversible)
my-git-committer-aget       # Commits to YOUR repos
my-email-drafter-aget       # Drafts but doesn't send
my-backup-manager-aget      # Manages YOUR backups
```

**Key**: Changes YOUR stuff but has undo/recovery path

## The Friction Stack

### Recommended Combination for HIGH RISK:

1. **Name**: `PROD-[domain]-publisher-aget` or `[DOMAIN]-PUBLISHER-aget`
2. **Location**: Separate `PRODUCTION-AGENTS/` directory
3. **Execution**: Typed confirmation phrase
4. **Config**: Required production.yaml
5. **Optional**: Time-based restrictions

Example:
```bash
$ cd PRODUCTION-AGENTS/RKB-CONTENT-PUBLISHER-aget
$ ./run.sh

⛔ PRODUCTION AGENT DETECTED
⚠️  This will modify: RKB Production Wiki
⚠️  Last accident: Never (keep it that way!)
⚠️  Type 'publish-to-rkb-prod-2025-09-26' to continue: _
```

## The Psychology

Just like `my-` makes you think "this is private", these frictions make you think:
- "This is serious"
- "I better double-check"
- "Am I sure I want to do this?"
- "Is this the right time?"

## Success Metrics

- Zero accidental production modifications
- Increased confidence when running safe agents
- Clear separation of risk levels
- Reduced 3am disasters

## Implementation Priority

### Essential (Minimum Viable Friction)
- Naming convention with risk signal
- Typed confirmation for execution

### Recommended
- Separate directory for high-risk
- Production config file

### Optional (Extra Safety)
- Time restrictions
- Two-step unlock
- Environment variables

---
*Pattern created: 2025-09-26*
*Purpose: Prevent production disasters through intentional friction*
*Inspiration: "my-" prefix friction for privacy*