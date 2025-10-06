# DISC001: Concurrent Evolution Log Collision

**Date**: 2025-10-04
**Context**: Two agents (my-supervisor-AGET and my-github-AGET) independently created L102 evolution logs simultaneously, causing L-number collision
**Status**: Resolved → Prevention implemented

## Summary

When multiple agents run concurrently and both create evolution logs, they can independently generate the same L-number (sequence collision). This causes:
- Duplicate L-numbers (L102 exists twice)
- Unclear sequence (which L102 is "correct"?)
- Consolidation required (manual merge)
- Documentation ambiguity (references to L102 → which one?)

**Root cause**: Distributed sequence generation without coordination.

**Prevention**: Add duplicate detection to wind-down protocol.

## Discovery Details

**Incident timeline**:

```
14:30 - Agent A (supervisor) creates L102_bridge_observations.md (finishes session at 14:45)
14:35 - Agent B (github) starts session, checks for next L-number
        Sees: L099, L100, L101 (L102 not yet pushed by Agent A)
        Generates: L102_template_transfer_lessons.md
14:50 - Agent B finishes session, discovers collision during commit
```

**Detection**:
```bash
$ ls .aget/evolution/L102*
L102_bridge_observations.md
L102_template_transfer_lessons.md

# Two files with same L-number!
```

**Collision pattern**:
1. Agent A: `ls .aget/evolution/` → sees L101 → creates L102 → working
2. Agent B: `ls .aget/evolution/` → sees L101 (A's L102 not committed) → creates L102 → working
3. Agent A: Commits L102 (pushes to remote)
4. Agent B: Commits L102 (discovers collision)

## Impact

**Immediate**:
- Two L102 files in `.aget/evolution/`
- Unclear which L102 to reference in documentation
- Git conflict when Agent B tries to push

**Longer-term**:
- Sequence integrity compromised (can't trust L-numbers are unique)
- References ambiguous ("See L102" → which one?)
- Consolidation work required (manual merge or renumber)

**Severity**: Medium (fixable but requires manual intervention)

## Resolution

**Action taken**: Consolidated duplicate L102 files

**Process**:
1. Reviewed both L102 files for content overlap
2. Merged unique content into single file
3. Renumbered second L102 → L103
4. Updated references in documentation
5. Committed consolidated result

**Time cost**: 15 minutes (detection + resolution)

## Prevention Strategy

**Implemented**: Duplicate detection in wind-down protocol

**Detection script** (added to AGENTS.md):
```bash
# During wind-down, detect duplicate L-numbers
dupes=$(ls .aget/evolution/L*.md 2>/dev/null | sed 's/_.*//;s/.*\///' | sort | uniq -d)
if [ -n "$dupes" ]; then
  echo "⚠️  Duplicate evolution logs detected: $dupes"
  echo "Consolidate before committing:"
  for d in $dupes; do
    ls .aget/evolution/${d}_*.md
  done
  exit 1
fi
```

**Integration point**: Wind-down protocol (before commit)

**Behavior**:
- If duplicates found → alert user, block commit
- User manually consolidates (merge or renumber)
- Re-run wind-down → passes if no duplicates

**Example output**:
```bash
$ ./scripts/wind_down.sh
⚠️  Duplicate evolution logs detected: L102
Consolidate before committing:
.aget/evolution/L102_bridge_observations.md
.aget/evolution/L102_template_transfer_lessons.md

# User consolidates files
$ ./scripts/wind_down.sh
✅ No duplicate evolution logs
✅ Session saved
✅ Committed successfully
```

## Alternative Solutions Considered

### Option A: Centralized Sequence Server
**Description**: HTTP service providing next L-number atomically
**Pros**: Prevents collisions at source
**Cons**: Infrastructure complexity, single point of failure, network dependency
**Rejected**: Too heavy for lightweight framework (zero-infrastructure principle)

### Option B: UUID-based Naming
**Description**: Use UUIDs instead of sequential L-numbers (e.g., L-a1b2c3d4)
**Pros**: No collisions possible
**Cons**: Unreadable, loses sequence information, breaks existing conventions
**Rejected**: Sequence information is valuable (L104 > L099 → newer)

### Option C: Agent-Prefixed Sequences
**Description**: Each agent has own sequence (SUP-L001, GH-L001, DATA-L001)
**Pros**: No collisions, clear ownership
**Cons**: Fragments evolution logs, loses shared numbering space, complicates references
**Rejected**: Evolution logs are fleet-wide knowledge, not agent-specific

### Option D: Git-Based Locking
**Description**: Lock .aget/evolution/ during L-number generation
**Pros**: Prevents collisions at source
**Cons**: Requires git operations during session, complex, error-prone
**Rejected**: Too complex for marginal benefit

### Option E: Duplicate Detection (Selected)
**Description**: Detect collisions during wind-down, alert user to consolidate
**Pros**: Simple, zero-infrastructure, catches issue before commit
**Cons**: Manual consolidation required (not automatic resolution)
**Selected**: Best trade-off between simplicity and effectiveness

## Lessons Learned

### System Design Insight
**Distributed sequence generation without coordination → collisions inevitable**

This is a classic distributed systems problem. Solutions:
1. **Prevent collisions** (centralized coordination) → Complex
2. **Detect collisions** (local validation) → Simple
3. **Tolerate collisions** (UUID/random IDs) → Loses sequence

We chose #2 (detect) because:
- Collisions are rare (requires concurrent sessions)
- Manual resolution is acceptable (15 min cost)
- Zero infrastructure preserved (no coordination server)

### Concurrent Agent Coordination
**Key principle**: Lightweight frameworks must accept occasional manual intervention rather than building complex coordination.

**When to coordinate**:
- Shared mutable state (L-number sequence)
- Concurrent writers (multiple agents)
- Sequence integrity matters (L-numbers must be unique)

**Coordination strategy**:
- **Optimistic**: Assume no collision, detect at wind-down
- **Fail safe**: Block commit if collision detected
- **Manual resolution**: User consolidates (framework doesn't guess)

### Prevention vs Detection Trade-off
**Prevention** (no collisions ever):
- Requires infrastructure (sequence server, locks, etc.)
- Complex error handling (network failures, timeouts)
- Single point of failure

**Detection** (catch collisions early):
- Simple validation script (10 lines bash)
- No infrastructure dependency
- Manual resolution acceptable (rare event)

**Decision**: Detection wins for lightweight frameworks where collisions are rare and manual intervention is acceptable.

## Verification

**Test collision detection**:
```bash
# Simulate collision
touch .aget/evolution/L999_test_a.md
touch .aget/evolution/L999_test_b.md

# Run detection
dupes=$(ls .aget/evolution/L*.md | sed 's/_.*//;s/.*\///' | sort | uniq -d)
echo $dupes  # Should output: L999

# Cleanup
rm .aget/evolution/L999_*.md
```

**Expected behavior**:
- Wind-down script detects L999 duplicate
- Blocks commit with error message
- Lists both L999 files
- User consolidates before continuing

## References

- Prevention: AGENTS.md:200-215 (Wind Down Protocol - duplicate detection)
- Evolution: `.aget/evolution/README.md:140-180` (Concurrent Collision Prevention)
- Related: L099_multi_agent_process_enforcement.md (supervision patterns)
- Incident: Session 2025-10-04 (bridge observations + template transfer collision)

---

**Status**: Resolved (prevention implemented in wind-down protocol)
**Last Reviewed**: 2025-10-06
**Monitoring**: Track collision frequency (expected: <1% of sessions)
