# Evolution Tracking

This directory captures the supervisor agent's learnings, decisions, and discoveries throughout its lifecycle. Evolution logs create organizational memory and enable pattern sharing across the fleet.

## Evolution Log Format

**Naming Convention**: Use **L-numbers** (L001, L002, L003, etc.) for sequential evolution logs.

**Format**: `L{NNN}_{descriptive_title}.md`
- `L` prefix = Learning/evolution log
- `{NNN}` = Zero-padded sequence number (L001, L002, ... L099, L100)
- `{descriptive_title}` = Snake_case description

**Examples**:
```
L001_first_supervisor_lesson.md
L042_gate_execution_discipline.md
L099_multi_agent_process_enforcement.md
L104_gate_complexity_rightsizing.md
```

## Entry Types

### Learning Logs (L-prefix)
**Purpose**: Capture lessons learned, patterns discovered, process improvements

**When to Create**:
- After completing significant work (migration, release, major refactoring)
- When discovering a reusable pattern
- After making a mistake worth documenting
- When establishing a new protocol or practice

**Structure**:
```markdown
# L{NNN}: {Title}

**Date**: YYYY-MM-DD
**Context**: {What situation led to this learning}
**Status**: {Active/Deprecated/Superseded}

## Summary
One-paragraph overview of the learning

## Background
What was the situation or problem?

## The Learning
What did we discover or learn?

## Evidence
What data/examples support this learning?

## Application
How should this learning be applied going forward?

## References
Related evolution logs, commits, sessions
```

### Decision Logs (D-prefix)
**Purpose**: Document major architectural or strategic decisions with trade-off analysis

**Format**: `D{NNN}_{decision_title}.md`

**When to Create**:
- Before making irreversible architectural changes
- When choosing between competing approaches
- When establishing new policies or standards

**Structure**:
```markdown
# D{NNN}: {Decision Title}

**Date**: YYYY-MM-DD
**Status**: Proposed/Accepted/Implemented/Deprecated
**Decision Makers**: {Who was involved}

## Context
What decision needs to be made and why?

## Options Considered
1. Option A: {description} - Pros: ... Cons: ...
2. Option B: {description} - Pros: ... Cons: ...

## Decision
{What was chosen and why}

## Consequences
- Positive: {benefits}
- Negative: {trade-offs}
- Neutral: {other impacts}

## References
{Related logs, specs, issues}
```

### Discovery Logs (DISC-prefix)
**Purpose**: Document unexpected findings, patterns in the wild, emergent behaviors

**Format**: `DISC{NNN}_{discovery_title}.md`

**When to Create**:
- When observing unexpected system behavior
- When finding patterns across multiple agents
- When identifying gaps in frameworks or documentation

**Structure**:
```markdown
# DISC{NNN}: {Discovery Title}

**Date**: YYYY-MM-DD
**Discovered By**: {Agent or human}
**Context**: {Where/when this was observed}

## The Discovery
What was found or observed?

## Evidence
Specific examples, data, or observations

## Implications
What does this mean for the fleet/framework?

## Action Items
What should be done about this discovery?
```

## Concurrent Collision Prevention

**Problem**: Multiple agents creating evolution logs simultaneously can create duplicate L-numbers.

**Example Collision**:
```
Agent A reads evolution/ → Sees L099 as last → Creates L100_topic_a.md
Agent B reads evolution/ → Sees L099 as last → Creates L100_topic_b.md
                                              ↓
                                        COLLISION
```

**Detection** (Wind Down Protocol):
```bash
# Run during wind-down to detect duplicates
dupes=$(ls .aget/evolution/L*.md 2>/dev/null | sed 's/_.*//;s/.*\///' | sort | uniq -d)
if [ -n "$dupes" ]; then
  echo "⚠️  Duplicate evolution logs detected: $dupes"
  echo "Consolidate before committing"
fi
```

**Resolution**:
1. Review both files for unique content
2. Consolidate into single file with best content from both
3. Delete redundant file
4. Document resolution in consolidated file's header

**Prevention**:
- Check for duplicates before committing (automated in wind-down protocol)
- Single-agent sessions naturally avoid collision
- Multi-agent coordination requires explicit synchronization

**See**: AGENTS.md Wind Down Protocol for automated detection

## Sequence Management

**Getting Next L-number**:
```bash
# Find highest L-number
highest=$(ls .aget/evolution/L*.md 2>/dev/null | \
  sed 's/.*\/L\([0-9]*\)_.*/\1/' | \
  sort -n | tail -1)

# Increment
next=$((10#$highest + 1))

# Format with padding
printf "L%03d" $next  # Produces L001, L042, L100, etc.
```

**Manual Assignment**: Acceptable to manually assign numbers (e.g., skip L013 for superstition, reserve L100 for milestone)

## Migration and Historical Logs

When migrating from other formats:
- **Old format**: `2025-09-25-005618-482177-DISC.md`
- **New format**: `DISC001_timestamp_based_discovery.md`

**Don't renumber historical logs** - preserve git history. New logs use L-numbers, old logs remain as-is.

## Supervisor-Specific Usage

**Fleet Patterns**: Document patterns observed across multiple agents
```
L050_worker_agent_common_failure_modes.md
L065_cross_agent_communication_patterns.md
```

**Coordination Learnings**: Capture multi-agent orchestration lessons
```
L075_fleet_migration_coordination.md
L089_process_investment_roi.md
```

**Process Improvements**: Document supervision and review patterns
```
L099_multi_agent_process_enforcement.md
L104_gate_complexity_rightsizing.md
```

## Best Practices

**Timing**:
- Create during wind-down (end of session)
- Don't create mid-session unless critical
- Batch-create if multiple learnings in one session

**Length**:
- Aim for 100-500 lines (substantial but focused)
- If >500 lines, consider splitting into multiple logs
- Include enough context for future readers

**References**:
- Link to related evolution logs (L042, L099, etc.)
- Reference commits, issues, sessions
- Include specification versions if applicable

**Audience**:
- Write for future self (6 months later)
- Write for other supervisors
- Assume reader knows AGET basics but not your specific context

## Maintenance

**Periodic Review**:
- Quarterly: Review recent logs for patterns
- Identify logs that should become protocols (AGENTS.md)
- Mark deprecated logs (superseded by later learnings)

**Index** (optional):
- `index.json` can track metadata
- Not required for small sets (<100 logs)
- Useful for large fleets with hundreds of logs

## References

- **Wind Down Protocol**: AGENTS.md (includes duplicate detection)
- **L103**: Concurrent collision example and resolution
- **Session Metadata Standard**: `.aget/docs/SESSION_METADATA_STANDARD_v1.0.md`
- **PATTERN_INTEGRATION_GUIDE.md**: When learnings become patterns

---

**Evolution logs are organizational memory. Document generously, reference frequently, share widely.**

**Current Template**: Contains exemplar logs (L001, D001, DISC001) showing format - replace with your own learnings as you work.
