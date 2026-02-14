# Fleet Conformance Assessment

**Version**: 1.0.0
**Created**: 2026-01-11
**Implements**: L518 (Conformance Assessment Rubric Pattern)
**Reference**: `aget/docs/CONFORMANCE_RUBRIC.md` (canonical source)

---

## Purpose

This document provides fleet-level conformance assessment guidance for supervisors. It references the canonical CONFORMANCE_RUBRIC.md and documents fleet-specific workflows.

---

## Quick Reference

### Individual Agent Assessment

```bash
# Assess single agent
python3 ~/github/aget-framework/aget/validation/validate_conformance.py /path/to/agent --verbose

# JSON output for automation
python3 ~/github/aget-framework/aget/validation/validate_conformance.py /path/to/agent --json
```

### Fleet Assessment

```bash
# Assess all agents in a directory
for agent in /path/to/agents/*/; do
  echo "=== $agent ==="
  python3 ~/github/aget-framework/aget/validation/validate_conformance.py "$agent" --json
done > fleet_conformance_report.json
```

---

## Conformance Levels

| Level | Score | Action |
|-------|-------|--------|
| L3 Exemplary | 85-100% | Reference implementation |
| L2 Compliant | 60-84% | Production ready |
| L1 Baseline | 40-59% | Scheduled remediation |
| L0 Non-Conformant | <40% | Immediate action required |

---

## Fleet Governance Workflow

### 1. Periodic Assessment (Recommended: Monthly)

1. Run conformance check on all managed agents
2. Aggregate results into fleet dashboard
3. Identify agents below L2 threshold
4. Create remediation tickets

### 2. Post-Upgrade Assessment

After any point upgrade:
1. Run conformance check per SOP_point_upgrade.md
2. Verify L2+ maintained
3. Document version-specific gaps

### 3. New Agent Onboarding

Per `aget/sops/SOP_aget_create.md` Gate 5:
1. Require L2+ before fleet registration
2. Document baseline score
3. Track improvement trajectory

---

## Remediation Patterns

See canonical rubric for full remediation guidance:
- **Location**: `aget/docs/CONFORMANCE_RUBRIC.md`
- **Patterns**: 5 documented (Identity, Learning, V-Tests, Capabilities, Scope)

---

## References

- Canonical Rubric: `aget/docs/CONFORMANCE_RUBRIC.md`
- Validator: `aget/validation/validate_conformance.py`
- Pattern: L518 (Conformance Assessment Rubric Pattern)
- Specs: AGET_5D_ARCHITECTURE_SPEC, AGET_TEMPLATE_SPEC, AGET_INSTANCE_SPEC

---

*FLEET_CONFORMANCE.md v1.0.0*
*"Measure twice, remediate once."*
