# GitHub Issues Label Schema
**Created**: 2025-09-27
**Purpose**: Standardized labels for AGET issue management

## Label Categories

### 1. Severity Labels (Red shades)
Indicates issue severity and impact

| Label | Color | Description | Priority |
|-------|-------|-------------|----------|
| `severity:critical` | #B60205 | Data loss, security, or system failure | P0 |
| `severity:high` | #D93F0B | Major functionality broken | P1 |
| `severity:medium` | #E99695 | Important but workaroundable | P2 |
| `severity:low` | #FBCA04 | Minor inconvenience | P3 |

### 2. Type Labels (Blue shades)
Categorizes the issue type

| Label | Color | Description |
|-------|-------|-------------|
| `type:bug` | #0E4C92 | Something broken |
| `type:feature` | #1E88E5 | New capability |
| `type:improvement` | #64B5F6 | Enhancement to existing |
| `type:discovery` | #90CAF9 | Finding or insight |
| `type:question` | #BBDEFB | Needs clarification |

### 3. State Labels (Yellow/Orange shades)
Tracks issue workflow state

| Label | Color | Description |
|-------|-------|-------------|
| `state:investigating` | #FFF176 | Being analyzed |
| `state:blocked` | #FFB74D | Waiting on dependency |
| `state:in-progress` | #FFD54F | Actively working |
| `state:needs-review` | #FFEE58 | Ready for review |
| `state:ready-to-close` | #FFF59D | Can be closed |

### 4. Agent Labels (Purple shades)
Identifies agent involvement

| Label | Color | Description |
|-------|-------|-------------|
| `from:agent` | #7B1FA2 | Filed by an agent |
| `from:my-AGET-aget` | #8E24AA | Filed by my-AGET-aget |
| `from:my-example-aget` | #9C27B0 | Filed by my-example-aget |
| `from:my-spotify-aget` | #AB47BC | Filed by spotify agent |
| `from:my-github-aget` | #BA68C8 | Filed by github agent |

### 5. Routing Labels (Green shades)
Indicates where issue should go

| Label | Color | Description |
|-------|-------|-------------|
| `route:needs-triage` | #2E7D32 | Needs routing decision |
| `route:my-AGET-template` | #388E3C | For template repo |
| `route:spotify` | #43A047 | For spotify project |
| `route:resolved` | #66BB6A | Routing complete |

### 6. Project Labels (Teal shades)
Associates with specific projects

| Label | Color | Description |
|-------|-------|-------------|
| `project:aget-framework` | #00695C | AGET framework issues |
| `project:spotify` | #00796B | Spotify project |
| `project:github-workspace` | #00897B | GitHub workspace |
| `project:internal` | #009688 | Internal tooling |

### 7. Special Labels (Various)
Special handling indicators

| Label | Color | Description |
|-------|-------|-------------|
| `good-first-issue` | #7057FF | Good for newcomers |
| `help-wanted` | #008672 | Needs assistance |
| `duplicate` | #CFD3D7 | Duplicate of another |
| `wontfix` | #FFFFFF | Will not be fixed |
| `data-loss-risk` | #B60205 | Can cause data loss |

## Label Creation Commands

```bash
# Create all labels at once
# Run from my-AGET-aget directory

# Severity labels
gh label create "severity:critical" --color "B60205" --description "Data loss, security, or system failure"
gh label create "severity:high" --color "D93F0B" --description "Major functionality broken"
gh label create "severity:medium" --color "E99695" --description "Important but workaroundable"
gh label create "severity:low" --color "FBCA04" --description "Minor inconvenience"

# Type labels
gh label create "type:bug" --color "0E4C92" --description "Something broken"
gh label create "type:feature" --color "1E88E5" --description "New capability"
gh label create "type:improvement" --color "64B5F6" --description "Enhancement to existing"
gh label create "type:discovery" --color "90CAF9" --description "Finding or insight"
gh label create "type:question" --color "BBDEFB" --description "Needs clarification"

# State labels
gh label create "state:investigating" --color "FFF176" --description "Being analyzed"
gh label create "state:blocked" --color "FFB74D" --description "Waiting on dependency"
gh label create "state:in-progress" --color "FFD54F" --description "Actively working"
gh label create "state:needs-review" --color "FFEE58" --description "Ready for review"
gh label create "state:ready-to-close" --color "FFF59D" --description "Can be closed"

# Agent labels
gh label create "from:agent" --color "7B1FA2" --description "Filed by an agent"
gh label create "from:my-AGET-aget" --color "8E24AA" --description "Filed by my-AGET-aget"
gh label create "from:my-example-aget" --color "9C27B0" --description "Filed by my-example-aget"
gh label create "from:my-spotify-aget" --color "AB47BC" --description "Filed by spotify agent"
gh label create "from:my-github-aget" --color "BA68C8" --description "Filed by github agent"

# Routing labels
gh label create "route:needs-triage" --color "2E7D32" --description "Needs routing decision"
gh label create "route:my-AGET-template" --color "388E3C" --description "For template repo"
gh label create "route:spotify" --color "43A047" --description "For spotify project"
gh label create "route:resolved" --color "66BB6A" --description "Routing complete"

# Project labels
gh label create "project:aget-framework" --color "00695C" --description "AGET framework issues"
gh label create "project:spotify" --color "00796B" --description "Spotify project"
gh label create "project:github-workspace" --color "00897B" --description "GitHub workspace"
gh label create "project:internal" --color "009688" --description "Internal tooling"

# Special labels
gh label create "good-first-issue" --color "7057FF" --description "Good for newcomers"
gh label create "help-wanted" --color "008672" --description "Needs assistance"
gh label create "duplicate" --color "CFD3D7" --description "Duplicate of another"
gh label create "wontfix" --color "FFFFFF" --description "Will not be fixed"
gh label create "data-loss-risk" --color "B60205" --description "Can cause data loss"
```

## Usage Guidelines

### When Filing Issues

1. **Always include**:
   - One severity label
   - One type label
   - `from:agent-name` if filed by agent

2. **Add if applicable**:
   - Project label for context
   - State label for workflow
   - Routing label if needs transfer

### Label Combinations

Valid examples:
- `severity:critical` + `type:bug` + `data-loss-risk`
- `severity:medium` + `type:improvement` + `project:spotify`
- `severity:high` + `type:discovery` + `from:my-example-aget`

### Priority Mapping

| Severity | Priority | Response Time |
|----------|----------|---------------|
| CRITICAL | P0 | Immediate |
| HIGH | P1 | Same day |
| MEDIUM | P2 | This week |
| LOW | P3 | Backlog |

## Maintenance

- Review label usage monthly
- Add new agent labels as needed
- Retire unused labels quarterly
- Keep total labels under 50