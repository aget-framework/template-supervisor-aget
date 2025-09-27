# Risk-Based Agent Naming Pattern

## The Critical Insight
Not all agents are equal in risk. Some just read data, others modify production systems. The name should signal the risk level!

## Risk Levels

### 🟢 Level 1: Read-Only (Safe)
**Pattern**: `my-[domain]-analytics-aget` or `my-[domain]-monitor-aget`

```bash
my-spotify-analytics-aget    # Only reads Spotify data
my-ga4-analytics-aget        # Only reads GA4 data
my-finance-monitor-aget      # Only tracks spending
my-health-tracker-aget       # Only logs health data
```

**Keywords**: analytics, monitor, tracker, watcher, observer, reader

### 🟡 Level 2: Local Actions (Medium Risk)
**Pattern**: `my-[domain]-manager-aget` or `my-[domain]-assistant-aget`

```bash
my-notes-manager-aget        # Creates/edits local notes
my-music-organizer-aget      # Reorganizes local files
my-code-assistant-aget       # Modifies local code
```

**Keywords**: manager, organizer, assistant, helper, builder

### 🔴 Level 3: Production Actions (High Risk)
**Pattern**: `my-[domain]-operator-aget` or `[domain]-publisher-aget`

```bash
RKB-content-publisher-aget   # Publishes to production wiki
infra-operator-aget          # Modifies infrastructure
database-migrator-aget       # Changes production data
deploy-controller-aget       # Deploys to production
```

**Keywords**: publisher, operator, controller, migrator, deployer

## The Safety Matrix

| Risk Level | Prefix | Action Words | Permissions | Undo-able? |
|------------|--------|--------------|-------------|------------|
| 🟢 Read-Only | my-*-analytics | monitor, track, watch | Read | N/A |
| 🟡 Local | my-*-manager | manage, organize, edit | Read/Write Local | Yes |
| 🔴 Production | *-publisher | publish, deploy, migrate | Read/Write Prod | Maybe |

## Naming Formula

```
[ownership]-[domain]-[risk-signal]-aget

where:
- ownership: my|team|corp|public
- domain: spotify|finance|content|infra
- risk-signal: analytics|manager|publisher
```

## Real Examples Renamed

### Current → Better
```bash
# Unclear risk:
my-spotify-aget → my-spotify-analytics-aget (clear: read-only)
RKB_content-aget → RKB-content-publisher-aget (clear: production writes!)
RKB_infra-aget → RKB-infra-monitor-aget (clear: read-only monitoring)

# Clear risk:
my-journal-aget → my-journal-manager-aget (clear: local writes)
team-code-aget → team-code-analyzer-aget (clear: read-only analysis)
```

## Team Naming Complexity

You're right about "team-" ambiguity. Solution:

### Public Teams
```bash
oss-team-[project]-aget     # Open source team
public-team-[project]-aget  # Explicitly public
community-[project]-aget    # Community project
```

### Private Teams
```bash
corp-team-[project]-aget    # Corporate team
internal-team-[project]-aget # Internal only
acme-team-[project]-aget    # Company-specific
```

### Personal Team Projects
```bash
my-team-[project]-aget       # Your team, your namespace
```

## The Decision Tree

```
Is it personal?
├─ Yes → my-*
└─ No → Is it public?
    ├─ Yes → public-* or oss-*
    └─ No → corp-* or internal-*

What's the risk level?
├─ Read-only → *-analytics-aget or *-monitor-aget
├─ Local writes → *-manager-aget or *-assistant-aget
└─ Production → *-publisher-aget or *-operator-aget
```

## Practical Benefits

### 1. Instant Risk Assessment
```bash
$ ls github/
my-spotify-analytics-aget/     # Safe to run anytime
my-notes-manager-aget/         # Check what it might modify
RKB-content-publisher-aget/    # CAREFUL - production impact!
```

### 2. Permission Alignment
```python
if "analytics" in agent_name or "monitor" in agent_name:
    permissions = "read-only"
elif "publisher" in agent_name or "operator" in agent_name:
    permissions = "read-write-production"
    require_confirmation = True
```

### 3. Accident Prevention
```bash
# Clear from name what's safe:
$ cd my-spotify-analytics-aget && ./run.sh  # Safe
$ cd RKB-content-publisher-aget && ./run.sh  # Wait, this publishes!
```

## Migration Examples

### Your Current Repos → Risk-Clear Names
```
my-aget-aget → my-aget-aget (governance, special case)
RKB_infrastructure → RKB-infra-monitor-aget
RKB_analytics-aget → RKB-analytics-monitor-aget
RKB_content-enhancement → RKB-content-publisher-aget
spotify-data-aget → my-spotify-analytics-aget
```

## The Meta Pattern

Even agent types follow risk hierarchy:
- **Analytics agents**: Always read-only
- **Manager agents**: Local modifications
- **Publisher agents**: Production changes
- **Operator agents**: System-level changes

## Guidelines

### DO ✅
- Include risk signal in name
- Use consistent risk keywords
- Align permissions with risk level
- Document risk level in README
- Add confirmation prompts for high-risk

### DON'T ❌
- Don't name high-risk agents innocuously
- Don't use "manager" for production changes
- Don't use "analytics" if it writes anything
- Don't mix risk levels in one agent

## The Ultimate Safety

```bash
# A new developer can immediately understand:
my-spotify-analytics-aget     # "I can run this safely"
my-notes-manager-aget         # "This modifies my local notes"
RKB-content-publisher-aget    # "This pushes to production!"
team-infra-operator-aget      # "This changes infrastructure!"
```

---
*Pattern identified: 2025-09-26*
*Insight: Agent names should scream their risk level*
*Safety improvement: CRITICAL*