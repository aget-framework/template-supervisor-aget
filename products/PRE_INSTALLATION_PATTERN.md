# Pre-Installation Pattern for AGET Templates
## Future Enhancement Proposal

**Status**: For Future Consideration
**Created**: 2025-09-26
**Source**: RKB_analytics-aget creation experience
**Priority**: Medium

---

## Pattern Definition

Pre-create files and structures during `aget init` to avoid runtime creation issues and enable immediate functionality.

## Proven Example

### Welcomed Flag (IMPLEMENTED)
- **File**: `.aget/welcomed`
- **Purpose**: Avoid runtime bash confirmations
- **Result**: ✅ Smoother workflow

## Proposed Extensions

### 1. Command History (PROPOSED)
```python
# In aget/config/commands/init.py
def create_command_history(self, target: Path):
    """Pre-create command history for usage analytics."""
    history_file = target / ".aget/command_history.jsonl"

    # Seed with init event
    init_event = {
        "timestamp": datetime.now().isoformat(),
        "command": "init",
        "template": self.template_name,
        "version": __version__
    }

    with open(history_file, 'w') as f:
        f.write(json.dumps(init_event) + "\n")
```

**Benefits**:
- Usage analytics from day 1
- No runtime permission issues
- Self-analysis capabilities

### 2. Default Checkpoint (PROPOSED)
```python
def create_default_checkpoint(self, target: Path):
    """Create revertible default state."""
    checkpoint = {
        "id": "default",
        "created": datetime.now().isoformat(),
        "description": "Clean installation state",
        "protected": True,  # Cannot be deleted
        "manifest": self.generate_file_manifest(target)
    }

    checkpoint_file = target / ".aget/checkpoints/default.json"
    checkpoint_file.write_text(json.dumps(checkpoint, indent=2))
```

**Benefits**:
- Safety net for experimentation
- Encourages bold changes
- Known-good recovery point

### 3. Performance Baselines (PROPOSED)
```python
def create_performance_baselines(self, target: Path, template: str):
    """Create template-specific performance baselines."""
    baselines = {
        "analytics": {
            "response_times_ms": {
                "status": {"p50": 100, "p95": 500},
                "insights": {"p50": 2000, "p95": 5000}
            },
            "thresholds": {
                "slow_response_ms": 5000,
                "high_memory_mb": 512
            }
        },
        "agent": {
            "response_times_ms": {
                "default": {"p50": 200, "p95": 1000}
            }
        }
    }

    if template in baselines:
        baseline_file = target / ".aget/metrics/baseline.json"
        baseline_file.parent.mkdir(parents=True, exist_ok=True)
        baseline_file.write_text(
            json.dumps(baselines[template], indent=2)
        )
```

**Benefits**:
- Anomaly detection from first run
- Template-appropriate defaults
- No learning period needed

---

## Decision Criteria

Pre-install when ALL of these are true:
1. ✓ Runtime creation causes issues (permissions/interruptions)
2. ✓ Empty state provides no value
3. ✓ All users benefit from having it
4. ✓ File size is small (<10KB)
5. ✓ Doesn't constrain user choices

Do NOT pre-install when:
1. ✗ User-specific configuration needed
2. ✗ Large files or data
3. ✗ May become stale quickly
4. ✗ Optional features

---

## Implementation Plan

### Phase 1: Test Locally
- Implement in next agent creation
- Measure actual benefits
- Gather usage data

### Phase 2: Refine
- Keep what proves valuable
- Remove what doesn't help
- Document patterns

### Phase 3: Contribute
- Submit PR to aget-template
- Include tests
- Document in README

---

## Philosophy Alignment

This pattern embodies:
- **Simplicity over hand-holding**: Remove runtime complexity
- **Professional tool mindset**: Assume competent users
- **Enable, don't constrain**: Provide capabilities, not restrictions

---

## Code Template

```python
class InitCommand(BaseCommand):
    def __init__(self):
        super().__init__()

        # Define pre-installations by template
        self.pre_installations = {
            'all': [
                self.create_welcomed_flag,
                self.create_command_history
            ],
            'agent': [
                self.create_default_checkpoint
            ],
            'analytics': [
                self.create_performance_baselines
            ]
        }

    def execute(self, template='agent', **kwargs):
        # Regular init...

        # Apply pre-installations
        for installer in self.pre_installations.get('all', []):
            installer(target)

        for installer in self.pre_installations.get(template, []):
            installer(target)
```

---

## Future Considerations

Other candidates for pre-installation:
- `.aget/cache/` directory
- `.aget/logs/` directory with .gitignore
- `.aget/config.defaults.json`
- `.aget/README.md` with .aget structure explanation

---

## Success Metrics

Pre-installation is successful if:
1. Zero runtime file creation errors
2. Features work immediately after init
3. No user confusion about missing files
4. Reduced support questions
5. Faster time-to-value

---

*This pattern is ready for testing in the next agent creation session.*