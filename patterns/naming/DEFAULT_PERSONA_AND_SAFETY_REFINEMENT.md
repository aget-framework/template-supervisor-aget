# Default Persona and Safety Level Refinement

## Key Insights from Naming Decisions

### 1. Default Persona Pattern
**Not all agents need an explicit persona**

```bash
# Default persona (no explicit role)
my-example-aget             # Generic AGET agent
my-aget-aget            # Generic AGET agent
my-llm-judge-aget       # Generic AGET agent

# Explicit persona (specific role)
my-spotify-analyst-aget # Explicit ANALYST persona
```

**The Rule**: Only add persona when it clarifies the agent's specific role/commands. Otherwise, default AGET behavior applies.

### 2. Public vs Private Distinction
**The base project can be public while the agent is private**

```bash
llm-judge              # Public project (no my-, no -aget)
my-llm-judge-aget      # Private agent FOR the public project
```

This is brilliant because:
- The research/project is shareable
- Your personal agent/automation is private
- Clear separation of concerns

### 3. RKB Domain Safety Clarification
**RKB itself is NOT dangerous - only PUBLISHING to it is**

```bash
# RKB reading/analyzing is SAFE
my-rkb-analytics-aget    # Reading RKB data (safe)
my-rkb-analyst-aget      # Analyzing RKB data (safe)
my-rkb-monitor-aget      # Monitoring RKB (safe)

# RKB writing is DANGEROUS
my-RKB_CONTENT-publisher-aget  # Publishing to RKB (DANGEROUS!)
my-RKB_DATA-importer-aget      # Importing to RKB (DANGEROUS!)
```

**The Pattern**:
- Reading from X = lowercase domain
- Writing to X = UPPERCASE domain

## Refined Naming Rules

### Domain Casing Based on Operation
```bash
# Reading/analyzing = lowercase domain
my-rkb-analytics-aget      # Reads from RKB
my-database-analyst-aget   # Queries database
my-aws-monitor-aget        # Monitors AWS

# Writing/modifying = UPPERCASE domain
my-RKB_CONTENT-publisher-aget   # Writes to RKB
my-DATABASE-migrator-aget       # Modifies database
my-AWS-operator-aget            # Changes AWS
```

### When to Add Persona

#### Use Default (No Persona)
```bash
my-project-aget          # Generic agent
my-tool-aget            # Standard functionality
my-helper-aget          # Basic automation
```

#### Add Explicit Persona
```bash
my-data-analyst-aget     # Specific analysis commands
my-content-curator-aget  # Specific curation commands
my-infra-guardian-aget   # Specific monitoring commands
```

### The Public/Private Split

```bash
# Public projects (shareable research/code)
llm-judge               # Public LLM judge project
spotify-analysis        # Public Spotify analysis
rkb-tools              # Public RKB tools

# Private agents (your automation)
my-llm-judge-aget      # Your agent for LLM judging
my-spotify-analyst-aget # Your Spotify analyzer
my-rkb-analytics-aget  # Your RKB analyzer
```

## Updated Examples

### Your Final Repository Names
```bash
# Generic agents (no persona needed)
my-aget-aget            # Pattern laboratory
my-example-aget             # EXAMPLE agent
my-llm-judge-aget       # LLM judge agent

# Persona-specific agents
my-spotify-analyst-aget # Spotify analyzer
my-RKB_INFRA-guardian-aget  # Infra monitor (InfraGuard)

# Safe RKB agents (reading)
my-rkb-analytics-aget   # Analytics reader

# Dangerous RKB agents (writing)
my-RKB_CONTENT-publisher-aget  # Content publisher
```

## The Operation-Based Safety Matrix

| Operation | Domain Casing | Risk Level | Example |
|-----------|--------------|------------|---------|
| READ | lowercase | 🟢 Safe | my-rkb-analytics-aget |
| ANALYZE | lowercase | 🟢 Safe | my-database-analyst-aget |
| MONITOR | lowercase | 🟢 Safe | my-aws-monitor-aget |
| ORGANIZE | lowercase | 🟡 Medium | my-files-organizer-aget |
| WRITE | UPPERCASE | 🔴 High | my-DATABASE-writer-aget |
| PUBLISH | UPPERCASE | 🔴 High | my-RKB_CONTENT-publisher-aget |
| DELETE | UPPERCASE | 🔴 High | my-AWS-cleaner-aget |

## The Cognitive Test

Which naming better reflects reality?

### Option A: Domain always uppercase if "production"
```bash
my-RKB-analytics-aget    # Suggests RKB is dangerous
my-RKB-monitor-aget      # But these just read!
```

### Option B: Operation determines casing
```bash
my-rkb-analytics-aget    # Reading from RKB (safe)
my-RKB_CONTENT-publisher-aget  # Writing to RKB (dangerous!)
```

**Option B wins!** The operation determines the danger, not the system itself.

## Key Takeaways

1. **Default persona is fine** - Not every agent needs a specific role
2. **Public/private split makes sense** - Project vs agent separation
3. **Operation determines danger** - Reading is safe, writing is dangerous
4. **RKB isn't inherently dangerous** - Publishing to it is

---
*Pattern refined: 2025-09-26*
*Insight: Danger comes from operations, not systems*