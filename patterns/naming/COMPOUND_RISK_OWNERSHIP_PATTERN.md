# Compound Risk & Ownership Naming Pattern

## The Scenario
What if you have a PERSONAL agent that does DANGEROUS things?
- `my-` signals personal/private
- `UPPERCASE` signals danger
- How do they combine?

## The Options

### Option 1: Ownership First, Then Risk
```bash
my-RKB-CONTENT-PUBLISHER-aget    # "MY dangerous publisher"
my-DATABASE-MIGRATOR-aget        # "MY database migrator"
my-PROD-DEPLOYER-aget            # "MY production deployer"
```
**Reading**: "This is MY personal agent that does DANGEROUS things"

### Option 2: Risk Overrides Everything
```bash
RKB-CONTENT-PUBLISHER-aget       # Danger trumps ownership
DATABASE-MIGRATOR-aget           # Too dangerous to be "my"
PROD-DEPLOYER-aget               # Risk is primary signal
```
**Reading**: "This is DANGEROUS (ownership secondary)"

### Option 3: Compound Signal
```bash
MY-RKB-CONTENT-PUBLISHER-aget    # ALL CAPS when dangerous
MY-DATABASE-MIGRATOR-aget        # Full uppercase
my-spotify-analytics-aget        # Lowercase when safe
```
**Reading**: "EVERYTHING UPPERCASE = MAXIMUM DANGER"

## The Underscore vs Hyphen Debate

### Current Mixed Convention
```bash
RKB_infrastructure      # Underscore for multi-word domains
RKB_content-enhancement # Mixed (ugly!)
my-spotify-aget        # Hyphen for prefixes
```

### Proposed Clear Convention

#### Hyphens for Structure, Underscores for Names
```bash
# Structure: ownership-DOMAIN_NAME-RISK-aget
my-RKB_CONTENT-PUBLISHER-aget    # Clear segments
my-spotify-analytics-aget        # Simple domain, no underscore
team-ACME_PROD-OPERATOR-aget     # Team + company name + risk
```

#### Rule: Underscores Only Within Domain Names
```bash
# Domain names that are naturally multi-word:
RKB_CONTENT        # RKB Content system
RKB_ANALYTICS      # RKB Analytics system
GM_MUSIC           # GM Music collection
ACME_CORP          # ACME Corporation

# Then compose:
my-RKB_CONTENT-PUBLISHER-aget
my-GM_MUSIC-analytics-aget
team-ACME_CORP-monitor-aget
```

## Decision Tree for Complex Cases

```
Is it dangerous?
├─ YES → UPPERCASE the risk parts
│   └─ Is it personal?
│       ├─ YES → my-DOMAIN-RISK-aget
│       └─ NO → DOMAIN-RISK-aget
└─ NO → lowercase
    └─ Is it personal?
        ├─ YES → my-domain-analytics-aget
        └─ NO → domain-analytics-aget
```

## Real Examples

### Your Current Repos → Clear Convention
```bash
# Current (inconsistent)
RKB_infrastructure
RKB_content-enhancement
RKB_analytics-aget

# Proposed (clear)
my-RKB_INFRA-monitor-aget          # Personal, safe monitor
RKB_CONTENT-PUBLISHER-aget         # Shared, dangerous
my-RKB_ANALYTICS-explorer-aget     # Personal, safe analytics
```

### Edge Cases Resolved
```bash
# Personal but dangerous
my-BLOG-PUBLISHER-aget              # YOUR blog publisher (still dangerous!)
my-AWS-OPERATOR-aget                # YOUR AWS operator (very dangerous!)
my-EMAIL-SENDER-aget                # YOUR email sender (reputation risk!)

# Safe but shared
team-code-analytics-aget           # Team's safe analyzer
public-docs-monitor-aget           # Public safe monitor
```

## The Cognitive Load Test

Which is clearer?

### Option A: Mixed Case Confusion
```bash
my-Rkb-Content-Publisher-aget     # What's dangerous?
My-RKB_content_PUBLISHER-aget     # Chaos
my-rkb-content-publisher-AGET     # Wrong emphasis
```

### Option B: Clear Risk Signal
```bash
my-RKB_CONTENT-PUBLISHER-aget     # Personal + Dangerous + Clear
my-spotify-analytics-aget         # Personal + Safe + Clear
RKB_CONTENT-PUBLISHER-aget        # Shared + Dangerous + Clear
```

**Winner: Option B** - Consistent uppercase for danger

## The Final Convention

### Format
```
[ownership]-[DOMAIN_NAME]-[RISK_LEVEL]-aget

Where:
- ownership: my|team|corp (lowercase)
- DOMAIN_NAME: UPPERCASE if dangerous, lowercase if safe
- RISK_LEVEL: UPPERCASE if dangerous, lowercase if safe
- Underscores: Only within multi-word domain names
- Hyphens: Separate the segments
```

### Examples
```bash
# Safe agents (all lowercase except proper names)
my-spotify-analytics-aget
my-notes-manager-aget
team-code-analyzer-aget

# Dangerous agents (UPPERCASE the danger)
my-RKB_CONTENT-PUBLISHER-aget
my-DATABASE-MIGRATOR-aget
PRODUCTION-DEPLOY-OPERATOR-aget

# The uppercase SCREAMS: "STOP AND THINK!"
```

## Special Cases

### When You're Testing Production Tools
```bash
my-RKB_CONTENT-PUBLISHER-TEST-aget   # TEST suffix for safety
my-DATABASE-MIGRATOR-DRY-aget        # DRY run version
```

### When Transitioning Risk Levels
```bash
my-email-drafter-aget              # Safe: just drafts
my-EMAIL-SENDER-aget               # Dangerous: actually sends!
```

## The Rule of Thumb

> "If running it wrong could ruin your day, UPPERCASE THE DANGER"

Personal (`my-`) doesn't make it safe. It just means it's YOUR dangerous tool!

---
*Pattern created: 2025-09-26*
*Insight: Ownership and risk are orthogonal concerns*
*Convention: Uppercase always wins for danger signaling*