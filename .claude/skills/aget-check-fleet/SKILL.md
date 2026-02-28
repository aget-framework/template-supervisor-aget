---
name: aget-check-fleet
description: Lightweight fleet health verification — 3 checks per agent across all managed agents
archetype: supervisor
allowed-tools:
  - Bash
  - Read
  - Glob
  - Grep
---

# aget-check-fleet

Verify fleet health with 3 lightweight checks per agent: .aget/ accessibility, structural integrity (no orphaned/invalid patterns), and symlink validity. Produces per-agent and fleet-level summary.

## When to Use

- **Day-1 orientation**: First thing after setting up a new fleet — verify all agents are reachable and structurally sound
- **Pre-delegation**: Before assigning work to an agent, confirm it's healthy
- **Post-upgrade**: After fleet-wide version upgrade, verify nothing broke
- **Periodic health**: Weekly or session-start fleet verification

## Input

```
/aget-check-fleet                    # Check all agents in fleet registry
/aget-check-fleet agent-name-AGET    # Check single agent
/aget-check-fleet --summary          # Fleet-level summary only (skip per-agent detail)
```

## Instructions

When this skill is invoked:

1. **Load Fleet Registry**
   - Read `.aget/registry/agents.yaml` (or `FLEET_REGISTRY.yaml`)
   - Extract agent paths from registry entries
   - If no registry exists, report error: "No fleet registry found. Create .aget/registry/agents.yaml first."

2. **For Each Agent, Run 3 Checks**

   **Check 1: .aget/ Accessibility**
   - Verify agent directory exists at registered path
   - Verify `.aget/` subdirectory exists and is readable
   - Verify `.aget/version.json` exists and parses as valid JSON
   - FAIL if: directory missing, .aget/ missing, or version.json unparseable

   **Check 2: Structural Integrity**
   - Verify no orphaned files in `.aget/` root (files not in any known subdirectory)
   - Verify `governance/` exists if version >= 3.0.0 (use version-aware check)
   - Verify no empty required directories (`.aget/persona/`, `.aget/memory/`, etc. for v3.0+)
   - WARN if: orphaned files found or empty required directories

   **Check 3: Symlink Validity**
   - Find all symlinks within agent directory: `find <agent_path> -type l`
   - For each symlink, verify target exists: `test -e <symlink_target>`
   - FAIL if: any symlink points to non-existent target (broken symlink)
   - PASS if: no symlinks present (symlinks are optional)

3. **Generate Report**
   - Per-agent: 3 check results (PASS/WARN/FAIL) with messages
   - Fleet summary: total agents, healthy count, warning count, failed count
   - If any agent FAIL: list specific failures with remediation hints

## Output Format

```markdown
## Fleet Health Check

**Fleet**: [N] agents | **Healthy**: [N] | **Warnings**: [N] | **Failed**: [N]

| Agent | Accessible | Structure | Symlinks | Status |
|-------|-----------|-----------|----------|--------|
| agent-1-AGET | PASS | PASS | PASS | Healthy |
| agent-2-AGET | PASS | WARN | PASS | Warning |
| agent-3-AGET | FAIL | — | — | Failed |

### Issues

- **agent-2-AGET**: 2 orphaned files in .aget/ root (cleanup recommended)
- **agent-3-AGET**: Directory not found at registered path /path/to/agent
```

### JSON Output

```bash
python3 scripts/check_fleet.py --json    # If implementation script exists
```

```json
{
  "timestamp": "2026-02-27T10:00:00",
  "fleet_size": 3,
  "summary": {"healthy": 1, "warnings": 1, "failed": 1},
  "agents": [
    {
      "name": "agent-1-AGET",
      "path": "/path/to/agent-1-AGET",
      "checks": {
        "accessible": {"passed": true, "message": "v3.6.0"},
        "structure": {"passed": true, "message": "no issues"},
        "symlinks": {"passed": true, "message": "0 symlinks"}
      },
      "status": "healthy"
    }
  ]
}
```

## Implementation Guidance

For agents implementing this skill as a script (`scripts/check_fleet.py`):

### Fleet Registry Reading

```python
import yaml
from pathlib import Path

def load_fleet_registry(agent_path: Path) -> list:
    """Load agent entries from fleet registry."""
    for registry_name in ['agents.yaml', 'FLEET_REGISTRY.yaml']:
        registry = agent_path / '.aget' / 'registry' / registry_name
        if registry.exists():
            with open(registry) as f:
                data = yaml.safe_load(f)
            return data.get('agents', [])
    return []
```

### Check Logic Pattern

```python
def check_accessible(agent_path: Path) -> dict:
    """Check 1: .aget/ accessibility."""
    if not agent_path.is_dir():
        return {"passed": False, "message": f"Directory not found: {agent_path}"}
    aget_dir = agent_path / '.aget'
    if not aget_dir.is_dir():
        return {"passed": False, "message": ".aget/ directory missing"}
    version_file = aget_dir / 'version.json'
    if not version_file.exists():
        return {"passed": False, "message": "version.json missing"}
    try:
        import json
        with open(version_file) as f:
            data = json.load(f)
        return {"passed": True, "message": f"v{data.get('aget_version', 'unknown')}"}
    except json.JSONDecodeError:
        return {"passed": False, "message": "version.json invalid JSON"}

def check_symlinks(agent_path: Path) -> dict:
    """Check 3: Symlink validity."""
    broken = []
    for symlink in agent_path.rglob('*'):
        if symlink.is_symlink() and not symlink.resolve().exists():
            broken.append(str(symlink.relative_to(agent_path)))
    if broken:
        return {"passed": False, "message": f"{len(broken)} broken: {', '.join(broken[:3])}"}
    return {"passed": True, "message": "no broken symlinks"}
```

### Error States

| Error | Cause | Remediation |
|-------|-------|-------------|
| "No fleet registry found" | Missing agents.yaml | Create `.aget/registry/agents.yaml` with agent entries |
| "Directory not found" | Agent moved or deleted | Update registry path or remove entry |
| "version.json invalid" | Corrupted file | Re-run upgrade or restore from git |
| "Broken symlink" | Target deleted | Remove symlink or restore target |

## Constraints

- **C1**: Read-only operation — NEVER modify any agent during fleet check
- **C2**: Scope-bounded — only check agents listed in fleet registry (not arbitrary paths)
- **C3**: Fail-safe — if registry is unreadable, report error and exit (don't guess agent locations)
- **C4**: Lightweight — 3 checks per agent, no deep analysis (use /aget-review-agent for deep review)

## Relationship to Other Skills

| Skill | Scope | Depth | When |
|-------|-------|-------|------|
| **aget-check-fleet** (this) | All agents | Lightweight (3 checks) | Orientation, pre-delegation |
| aget-check-health | Self only | Deep (8 checks) | Session start, sanity check |
| aget-review-agent | Single agent | Full review | Periodic assessment |

## Traceability

| Link | Reference |
|------|-----------|
| Evidence | Supervisor 2 (#1 CRITICAL for new users), Supervisor 1 (fleet health context) |
| Spec | TBD (to be created with skill proposal SP-002) |
| Ontology | Fleet, Health_Check, Agent_Registry (ONTOLOGY_supervisor.yaml) |
| Pattern | PATTERN_fleet_management.md (tiered oversight model) |
| CAP | CAP-SUP-003 (Fleet Health Monitoring) |
