# SOP: Agent Creation

**Version**: 1.0
**Status**: DRAFT
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Evidence Source**: G3.7 user journey validation (2026-02-27) + SOP_aget_create.md v2.2.0

---

## Purpose

Define the standard procedure for creating new agent instances using the supervisor's `/aget-create-aget` skill.

## Scope

Applies when a supervisor needs to create a new agent instance from a template.

## Prerequisites

- Supervisor agent operational with `/aget-create-aget` skill
- Access to AGET templates (`template-worker-aget`, `template-advisor-aget`, etc.)
- Core framework `scripts/instantiate_template.py` available
- Core framework `sops/SOP_aget_create.md` available for reference

---

## Procedure

### Step 1: Determine Agent Needs

| Decision | Options |
|----------|---------|
| Archetype | Worker, Advisor, Supervisor, Developer, Consultant, etc. |
| Instance type | AGET (action-taking) or aget (read-only) |
| Portfolio | Which portfolio will this agent belong to? |
| Domain | What domain expertise will this agent develop? |

### Step 2: Invoke Creation Skill

```bash
/aget-create-aget <archetype> <agent-name>
```

The skill guides through 9 SOP gates:
- **G0**: Prerequisites (template access, naming)
- **G1**: Ontology creation (HUMAN GATE — requires domain expertise)
- **G2**: Specification (EARS format)
- **G3**: Instance creation (`instantiate_template.py`)
- **G4**: Configuration (version.json, identity.json)
- **G5**: Validation (contract tests)
- **G6**: Knowledge seeding
- **G7**: Supervisor handoff (HUMAN GATE — update fleet registry)
- **G8**: Operational verification

### Step 3: Post-Creation Verification

- [ ] Contract tests pass in new agent
- [ ] Identity fields correct (agent_name, domain, instance_type)
- [ ] Portfolio assigned in version.json
- [ ] Fleet registry updated
- [ ] First session (wake-up) succeeds

---

## Template Selection Guide

| Archetype | Best For |
|-----------|----------|
| **Worker** | Task execution, code changes, routine operations |
| **Advisor** | Analysis, recommendations, research |
| **Supervisor** | Fleet coordination, oversight |
| **Developer** | Software development, testing |
| **Consultant** | Expert advisory, strategic guidance |

See: Core framework `docs/GETTING_STARTED.md` for full archetype guide.

---

## Anti-Patterns

| Anti-Pattern | Description | Consequence |
|--------------|-------------|-------------|
| Skip Ontology | Creating agent without domain vocabulary | Imprecise communication, scope drift |
| Copy-Paste Config | Not updating identity fields after template copy | Identity conflicts, test failures |
| Skip Validation | Not running contract tests after creation | Undetected configuration errors |

---

## Related Documents

- `/aget-create-aget` — Creation skill (SKILL.md)
- Core: `sops/SOP_aget_create.md` — Full 9-gate creation process
- Core: `scripts/instantiate_template.py` — Template instantiation script
- `SOP_fleet_coordination.md` — Post-creation fleet integration

---

*SOP: Agent Creation v1.0 (DRAFT)*
*Evidence: G3.7 user journey validation — end-to-end creation path verified*
*Lifecycle: DRAFT — promote to ACTIVE after 3+ successful agent creations using this workflow*
