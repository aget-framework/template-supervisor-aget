# SOP: Release Process

**Version**: 1.0
**Status**: DRAFT
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Evidence Source**: Derived from production release governance patterns (L465, L467, L511)

---

## Purpose

Define the standard procedure for releasing new versions of supervisor-managed agents and templates.

## Scope

Applies to:
- Template version releases
- Agent instance version upgrades
- Fleet-wide version coordination

---

## Pre-Release Checklist

### Step 1: Scope Consolidation (L465)
- [ ] Audit all PROJECT_PLANs targeting this version
- [ ] Create consolidated plan if multiple exist
- [ ] Mark superseded plans with consolidation reference
- [ ] Confirm all planned items are complete or explicitly deferred

### Step 2: Quality Verification
- [ ] All contract tests pass (`python3 -m pytest tests/ -v`)
- [ ] Version numbers consistent across version.json, README.md
- [ ] No private information in public-facing content
- [ ] CHANGELOG.md updated with release notes

### Step 3: Governance Check
- [ ] Release within approved authority (see Decision Authority)
- [ ] Supervisor/principal approval obtained if required
- [ ] Release window respected (per team preferences)

---

## Release Procedure

### Step 1: Version Bump
```bash
# Update version.json
# Update README.md version badge and framework spec link
# Update CHANGELOG.md
```

### Step 2: Final Validation
```bash
python3 -m pytest tests/ -v
# Verify: all tests pass
```

### Step 3: Commit and Tag
```bash
git add -A
git commit -m "release: vX.Y.Z — [summary]"
git tag vX.Y.Z
git push origin main --tags
```

### Step 4: Post-Release

- [ ] Create release handoff artifact (L511): `handoffs/RELEASE_HANDOFF_vX.Y.Z.md`
- [ ] Notify supervisor of new version availability
- [ ] Run post-release validation
- [ ] File any discovered issues

---

## Fleet Upgrade Coordination

When releasing a version that affects fleet agents:

1. **Handoff**: Create release handoff with upgrade guide
2. **Pilot**: Select 1-2 agents for pilot upgrade
3. **Validate**: Verify contract tests pass on pilot agents
4. **Fleet**: Coordinate fleet-wide upgrade via `/aget-broadcast-fleet`
5. **Track**: Monitor upgrade completion across fleet

---

## Anti-Patterns

| Anti-Pattern | Description | Consequence |
|--------------|-------------|-------------|
| Premature Victory (L92) | Declaring "done" before post-release gates | Incomplete deployment |
| Scope Creep at Release | Adding features during release | Delayed release, untested changes |
| Silent Release | No handoff artifact or notification | Fleet agents miss upgrade |

---

## Related Documents

- `governance/CHARTER.md` — Release authority
- `SOP_fleet_coordination.md` — Fleet broadcast for releases
- `SOP_escalation.md` — When release issues exceed scope

---

*SOP: Release Process v1.0 (DRAFT)*
*Evidence: Production release governance patterns (L465, L467, L511)*
*Lifecycle: DRAFT — promote to ACTIVE after 2+ successful releases following this procedure*
