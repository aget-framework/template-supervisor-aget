# SOP: Fleet Version Upgrade

**Version**: 1.0.0
**Created**: 2026-04-12
**Owner**: template-supervisor-aget
**Status**: ACTIVE
**Source**: Extracted from operational supervisor v1.4.0 (6 completed fleet upgrades)
**Spec Basis**: L466, L528, L570, L583, L622, L623, L624, L826

---

## Purpose

Canonical process for upgrading all fleet agents to a new AGET framework version. Consolidates improvements from 6 completed fleet upgrade cycles. Future upgrade plans should reference this SOP and document only **deviations**.

---

## Prerequisites

1. **RELEASE_HANDOFF exists**: Framework-AGET has published `RELEASE_HANDOFF_vX.Y.Z.md`
2. **DEPLOYMENT_SPEC available**: Authoritative target state (NOT the handoff — L570)
3. **PROJECT_PLAN created**: Per L528 — "a handoff triggers planning, not execution"
4. **Supervisor at current version**: Must be at N-1 before upgrading fleet

---

## Gate Structure (4 Gates)

### Gate 0: Spec Verification & Conflict Resolution

**Objective**: Read spec, reconcile against template and fleet, identify conflicts.
**Time**: 5-10 min

**Triad**: Invoke `/aget-release-audit-specs` — Spec Auditor verifies DEPLOYMENT_SPEC claims match template reality.

**Steps**:
1. Read DEPLOYMENT_SPEC
2. Read RELEASE_HANDOFF (note new skills, breaking changes)
3. Reconcile: For each spec claim, verify file exists in template and fleet
4. Classify divergences: ADOPT / SKIP / MERGE / ABSENT
5. Resolve skill conflicts:
   - Agent has organic version → KEEP (preserve organic)
   - Agent has unmodified template → OVERWRITE
   - Agent has customized template → MERGE (L629 diff-before-replace)
   - New skill → DEPLOY
6. **Full baseline reconciliation (L623)**: Compare template skills against agent — not just DEPLOYMENT_SPEC delta:
   ```bash
   comm -23 <(ls ~/github/aget-framework/template-worker-aget/.claude/skills/ | sort) <(ls .claude/skills/ | sort)
   ```
7. Document conflict resolution plan

**V-Tests**:
- [ ] DEPLOYMENT_SPEC read and referenced
- [ ] All divergences classified
- [ ] Baseline reconciliation: 0 missing template skills
- [ ] No implementation in this gate (read-only)

---

### Gate 1: Supervisor Self-Upgrade (Wave 0)

**Objective**: Upgrade supervisor first to catch issues before fleet.
**Time**: 15-35 min

**Canonical 8-Step Sequence** (per agent):

```python
import json, shutil
from pathlib import Path

# 1. Pre-check
data = json.load(open('.aget/version.json'))
print(f"Current: {data['aget_version']}")

# 2. Version bump
data['aget_version'] = 'X.Y.Z'
data['updated'] = 'YYYY-MM-DD'
data.setdefault('migration_history', []).append({...})
json.dump(data, open('.aget/version.json', 'w'), indent=2)

# 3. AGENTS.md version tag
# sed or Edit tool: @aget-version: X.Y.Z

# 4. Deploy skills per conflict resolution plan
# Use shutil.copy2() — NEVER shell cp (macOS cp -i alias blocks overwrites)
template = Path('~/github/aget-framework/template-worker-aget/.claude/skills')
for skill in new_skills:
    shutil.copy2(template / skill / 'SKILL.md', f'.claude/skills/{skill}/SKILL.md')

# 5. Validate
# 6. Commit (git add specific files, NOT -A)
# 7. Push
```

**Source Rule (L622)**: ALL skill files sourced from `template-worker-aget`, not from framework-AGET.

**Copy Method**: Python `shutil.copy2()` — never shell `cp` (L826 F1: macOS alias).

**V-Tests**:
- [ ] version.json at target
- [ ] AGENTS.md tag at target
- [ ] Consistency: version.json == AGENTS.md
- [ ] Skills deployed per plan
- [ ] **Runtime dependency scan (L624)**: All SKILL.md script refs exist or are `test -f` guarded
- [ ] **Baseline reconciliation (L623)**: `comm -23` returns empty
- [ ] wake_up.py reports target version

---

### Gate 2: Pilot Validation (Wave 1)

**Objective**: Confirm upgrade on 2-3 diverse agents before fleet rollout.
**Time**: 10-15 min

**Triad**: Invoke `/aget-release-critique` — Critic reviews pilot results. "What broke? What assumptions were wrong? What will fail at scale?"

**Pilot Selection (L583)**: Pick 3 agents across complexity:

| Slot | Criteria | Why |
|------|----------|-----|
| 1 | Simple (few organic extensions) | Baseline confidence |
| 2 | High-value (active, large KB) | Risk-weighted |
| 3 | Complex (many organic skills) | Merge conflict surface |

**Anti-Pattern**: Dormant agents as pilots — gives false confidence (L583).

Execute same 8-step sequence per pilot. After first pilot, run full V-tests before continuing.

**V-Tests** (per pilot):
- [ ] All Gate 1 V-tests pass
- [ ] No organic skill loss (compare before/after count)
- [ ] **Runtime dependency scan (L624)**: If broken refs found, STOP. Do not proceed to G3 until template is hotfixed.
- [ ] **Baseline reconciliation (L623)**: No missing template skills

---

### Gate 3: Fleet Rollout (Wave 2)

**Objective**: Upgrade all remaining agents, validate fleet-wide.
**Time**: 25-60 min

**Triad**: Invoke `/aget-release-build` — Builder executes with velocity tracking.

**Recommended**: Use a Python script (not manual per-agent). Reference implementation:

```python
import json, shutil
from pathlib import Path

# Read FLEET_STATE for agent paths
# For each agent: 8-step sequence
# Use shutil.copy2 for all file operations
# Track: upgraded/failed/skipped per agent
# V-test each batch before continuing
```

**Post-Rollout Validation**:
- [ ] All agents at target version
- [ ] Spot-check 2-3 random agents (V-tests)
- [ ] FLEET_STATE updated with new version + skill counts
- [ ] Commit + push all agents

---

## Lessons Encoded

| L-doc | Lesson | Where Applied |
|-------|--------|---------------|
| L622 | Source from template, not framework-AGET | Gate 1 Source Rule |
| L623 | Full baseline reconciliation, not delta | Gates 0-2 V-tests |
| L624 | Runtime dependency scan for SKILL.md | Gates 1-2 V-tests |
| L826 F1 | macOS cp -i alias | Copy Method (shutil) |
| L826 F2 | Improvised V-tests = permission friction | Single-script verify |
| L826 F3 | Multi-portfolio path resolution | FLEET_STATE paths |
| L583 | Pilot selection heuristic | Gate 2 selection |
| L570 | Handoff ≠ spec | Gate 0 prerequisite |

---

*SOP_fleet_upgrade.md v1.0.0 (template)*
*Extracted from operational supervisor v1.4.0*
*"A handoff triggers planning, not execution." (L528)*
