# Pre-Installation Proposals
## Three Things to Pre-Create During `aget init`

**Analysis Date**: 2025-09-26
**Context**: Following "welcomed" flag success

---

## Proposal 1: Command History Cache (.aget/command_history.jsonl)

### What It Is
Pre-create an empty JSON Lines file for tracking command usage patterns.

### Why Pre-Install
- **Runtime Issue**: First command execution needs to append to history
- **Permission Issues**: Runtime creation might fail in read-only environments
- **Analytics Ready**: Agents can analyze their own usage from day 1

### Implementation
```python
# During aget init
(target / ".aget/command_history.jsonl").touch()
# Pre-seed with init event
with open(target / ".aget/command_history.jsonl", 'w') as f:
    f.write(json.dumps({
        "timestamp": datetime.now().isoformat(),
        "command": "init",
        "template": template_name
    }) + "\n")
```

### Trade-offs
- ✅ No runtime file creation needed
- ✅ Usage analytics from start
- ❌ File grows over time (needs rotation strategy)
- ❌ Privacy concern (tracks all commands)

---

## Proposal 2: Default State Checkpoint (.aget/checkpoints/default.json)

### What It Is
Pre-create a "clean state" checkpoint that agents can always revert to.

### Why Pre-Install
- **Safety Net**: Always have known-good state to restore
- **Confidence**: Users more willing to experiment knowing they can reset
- **Consistency**: All agents start from same baseline

### Implementation
```python
# During aget init
default_checkpoint = {
    "created": datetime.now().isoformat(),
    "template": template_name,
    "type": "default",
    "description": "Clean installation state",
    "files": {
        "AGENTS.md": hashlib.md5(agents_content).hexdigest(),
        ".gitignore": hashlib.md5(gitignore_content).hexdigest()
    },
    "can_delete": False  # Protect default checkpoint
}
Path(target / ".aget/checkpoints/default.json").write_text(
    json.dumps(default_checkpoint, indent=2)
)
```

### Trade-offs
- ✅ Instant recovery option
- ✅ Encourages experimentation
- ✅ Version control for agent state
- ❌ Duplicates git's role somewhat
- ❌ Users might over-rely on resets

---

## Proposal 3: Performance Baselines (.aget/metrics/baseline.json)

### What It Is
Pre-populate performance baselines based on template type.

### Why Pre-Install
- **Immediate Comparisons**: Can detect anomalies from first run
- **No Cold Start**: Don't need to "learn" what's normal
- **Template-Specific**: Analytics agents get different baselines than content agents

### Implementation
```python
# During aget init for analytics template
baseline = {
    "response_times": {
        "status": {"p50": 100, "p95": 500, "p99": 1000},  # ms
        "insights": {"p50": 2000, "p95": 5000, "p99": 10000},
        "demo": {"p50": 500, "p95": 1000, "p99": 2000}
    },
    "data_volumes": {
        "daily_traffic": {"min": 5000, "typical": 10000, "max": 20000},
        "cost_data": {"min": 100, "typical": 200, "max": 300}
    },
    "thresholds": {
        "slow_response": 5000,  # ms
        "high_cost": 250,       # $/month
        "low_traffic": 1000     # visits/day
    }
}
Path(target / ".aget/metrics/baseline.json").write_text(
    json.dumps(baseline, indent=2)
)
```

### Trade-offs
- ✅ Instant performance monitoring
- ✅ Anomaly detection from day 1
- ✅ Template-appropriate defaults
- ❌ May not match actual environment
- ❌ Needs calibration over time

---

## Bonus Proposals (Considered but Not Recommended)

### 4. Pre-Generated Demo Data (.aget/demo/)
- **Why Not**: Takes space, may become stale
- **Better**: Generate on first "demo" command

### 5. Template README in .aget/README.md
- **Why Not**: Duplicates main README
- **Better**: Link to main docs

### 6. Pre-configured .aget/config.yaml
- **Why Not**: Hardcoded configs are inflexible
- **Better**: Generate from environment on first run

---

## Recommendation Priority

### 1. **Command History** (HIGH VALUE)
- Enables self-analysis
- No runtime issues
- Useful for evolution tracking

### 2. **Default Checkpoint** (MEDIUM VALUE)
- Safety net for experimentation
- One-time creation
- Encourages bold changes

### 3. **Performance Baselines** (CONTEXT-DEPENDENT)
- Great for analytics/monitoring agents
- Less useful for content agents
- Needs template awareness

---

## Philosophy Check

These proposals align with "Simplicity over hand-holding" because:
1. **Remove runtime complexity** - No dynamic file creation
2. **Enable immediate value** - Features work from start
3. **Assume competent users** - Provide tools, not tutorials
4. **Professional defaults** - Sensible starting points

---

## Implementation Strategy

### Phase 1: Add to aget-template init.py
```python
def create_aget_structure(self, target: Path, template: str):
    # Existing
    (target / ".aget").mkdir(exist_ok=True)
    (target / ".aget/welcomed").touch()

    # NEW: Based on template type
    if template in ['agent', 'analytics']:
        self.create_command_history(target)
        self.create_default_checkpoint(target)

    if template == 'analytics':
        self.create_performance_baselines(target)
```

### Phase 2: Test with Next Agent Creation
- Create another specialized agent
- Verify pre-installations help
- Adjust based on experience

### Phase 3: Extract Pattern
- Document which pre-installations proved valuable
- Contribute back to aget-template
- Share learnings

---

## The Meta-Learning

Pre-installation is valuable when:
1. **Runtime creation causes issues** (permissions, interruptions)
2. **Empty state is useless** (needs seed data to function)
3. **Template type implies needs** (analytics → baselines)
4. **Feature requires history** (can't retroactively create)

The key: **Pre-install enables, not constrains**