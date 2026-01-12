# Shell Integration

This directory contains shell integration examples for the Supervisor template.

## Overview

Shell integration enables:
- Profile-based CLI backend selection
- Environment setup for agent sessions
- Quick access to common operations
- Fleet management helpers (supervisor-specific)

## Files

| File | Purpose |
|------|---------|
| `supervisor_profile.zsh` | Example zsh profile for supervisor agents |

## Usage

### Option 1: Source directly
```bash
export AGET_AGENT_DIR="/path/to/my-agent"
source shell/supervisor_profile.zsh
```

### Option 2: View documentation paths
```bash
aget_info         # Display all paths
aget_docs spec    # Open specification
aget_fleet_status # View fleet registry (supervisor-specific)
```

## Customization

When instantiating this template:
1. Copy `supervisor_profile.zsh` to your instance
2. Update `AGET_AGENT_NAME` to your agent name
3. Configure `AGET_FLEET_REGISTRY` path
4. Add fleet-specific helper functions

## References

- AGET Shell Orchestration: `aget/shell/aget.zsh`
- Template Spec: `specs/Supervisor_SPEC.md`
- Template Vocab: `specs/Supervisor_VOCABULARY.md`
- Framework Spec: `aget/specs/AGET_TEMPLATE_SPEC.md` (CAP-TPL-014)

---

*Shell integration for template-supervisor-aget*
