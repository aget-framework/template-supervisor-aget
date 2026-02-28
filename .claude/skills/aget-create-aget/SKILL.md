# /aget-create-aget

Create a new AGET agent instance using the ontology-driven creation workflow.

## Purpose

Guide the supervisor through the 9-gate agent creation process defined in `SOP_aget_create.md`. This skill wraps existing infrastructure (`instantiate_template.py` + SOP gates) into a guided workflow, pausing at human-intensive gates.

**Key Principle (L481)**: Define what the agent IS before instantiating it.

## Input

`<template-type> <agent-name>` — Template archetype and target agent name.

Examples:
- `/aget-create-aget worker my-task-worker-AGET`
- `/aget-create-aget advisor risk-advisor-aget`
- `/aget-create-aget researcher domain-researcher-aget`

## Mode Detection

| Input Pattern | Mode | Behavior |
|---------------|------|----------|
| Empty or blank | **Interactive** | Prompt for template type and agent name |
| `<type> <name>` | **Explicit** | Proceed with specified template and name |
| `<name>` only | **Inference** | Prompt for template type, use provided name |

## Execution

### Step 1: Input Validation (SOP G0)

Parse input for template type and agent name.

**Validate**:
- Template type exists in `aget-framework/` (see Template Selection Guide below)
- Agent name follows convention: `-aget` (internal KB) or `-AGET` (external systems) per L480
- Target directory does not already exist

```bash
# Check template exists
ls /path/to/aget-framework/template-{type}-aget/

# Check agent doesn't exist
ls /path/to/target/{agent-name}/ 2>/dev/null && echo "EXISTS - confirm overwrite" || echo "OK"
```

If validation fails, report error and stop.

### Template Selection Guide

| Template | Archetype | Use Case |
|----------|-----------|----------|
| template-worker-aget | worker | Task execution |
| template-supervisor-aget | supervisor | Fleet coordination |
| template-developer-aget | developer | Code development |
| template-consultant-aget | consultant | Client advisory |
| template-advisor-aget | advisor | Risk and guidance |
| template-analyst-aget | analyst | Data analysis |
| template-architect-aget | architect | System design |
| template-researcher-aget | researcher | Research |
| template-operator-aget | operator | Operations |
| template-executive-aget | executive | Leadership |
| template-reviewer-aget | reviewer | Quality review |
| template-spec-engineer-aget | spec-engineer | Specification |

### Step 2: Ontology Creation (SOP G1) — HUMAN GATE

**PAUSE and guide the user** through ontology creation. This is the most important gate — vocabulary and specifications DRIVE agent creation.

Present to user:

> **Gate 1: Ontology Creation**
>
> Before creating the agent instance, define its conceptual framework:
>
> 1. **Domain Vocabulary** (SKOS format) — What concepts does this agent work with?
>    - Create: `planning/artifacts/{agent-name}/specs/{DOMAIN}_VOCABULARY.md`
>
> 2. **Domain Specification** (EARS format) — What requirements govern this agent?
>    - Create: `planning/artifacts/{agent-name}/specs/{DOMAIN}_SPEC.md`
>
> 3. **Research Methodology** — How does this agent conduct its work?
>    - Create: `planning/artifacts/{agent-name}/specs/RESEARCH_METHODOLOGY.md`
>
> See: `aget/sops/SOP_aget_create.md` Gate 1 for templates and V-tests.
>
> **Say "GO" when ontology artifacts are ready.**

Wait for user confirmation before proceeding.

### Step 3: Instance Creation (SOP G3)

Run the instantiation script:

```bash
python3 /path/to/aget-framework/aget/scripts/instantiate_template.py \
  --template template-{type}-aget \
  --name {agent-name}
```

**Known limitations** of `instantiate_template.py` (document, don't fix — aget/ repo scope):
- Does not handle `-aget` vs `-AGET` suffix distinction
- Does not deploy session scripts to `scripts/` (only `.aget/patterns/session/`)
- Does not copy specs from staging to instance `specs/`
- Does not create CLAUDE.md symlink
- Does not deploy archetype-specific skill specs

After script completes, perform manual steps:

```bash
# Copy specs from staging
cp planning/artifacts/{agent-name}/specs/* {agent-name}/specs/

# Create CLAUDE.md symlink (L487)
cd {agent-name} && ln -s AGENTS.md CLAUDE.md

# Deploy session scripts if not present
# (Check if scripts/wake_up.py exists; if not, copy from template)
```

### Step 4: Configuration (SOP G4)

Guide user through capability configuration:

> **Gate 4: Capability Configuration**
>
> Configure the agent's governance files:
> 1. Edit `governance/CHARTER.md` — What this agent IS and IS NOT
> 2. Edit `governance/MISSION.md` — Goals and success metrics
> 3. Edit `governance/SCOPE_BOUNDARIES.md` — Operational boundaries
>
> Update identity from spec:
> - `identity.json` north_star derived from spec success criteria
> - `version.json` references specs_version and vocabulary_ref

### Step 5: Validation (SOP G5)

Run structural validation:

```bash
# Contract tests
cd {agent-name} && python3 -m pytest tests/ -v

# Structural validation (if available)
python3 /path/to/aget-framework/aget/validation/validate_template_instance.py {agent-name}/

# Operational test: wake up
cd {agent-name} && python3 scripts/wake_up.py
```

Report results. If failures, guide remediation.

### Step 6: Initial Assignment (SOP G6)

> **Gate 6: Initial Assignment**
>
> Prepopulate the agent's knowledge base:
> 1. Create `knowledge/` directories matching vocabulary concepts
> 2. Create `planning/RESEARCH_BACKLOG.md` from vocabulary terms
> 3. Initialize `evolution/index.json`

### Step 7: Supervisor Handoff (SOP G7-G8) — HUMAN GATE

**PAUSE for supervisor handoff**:

> **Gate 7-8: Supervisor Handoff**
>
> The agent is ready for fleet registration:
>
> 1. Create handoff document at `{supervisor-path}/handoffs/HANDOFF_{agent-name}_{date}.md`
> 2. Supervisor reviews agent compliance
> 3. Upon ACK, agent is registered in fleet and marked active
>
> See: `aget/sops/SOP_aget_create.md` Gates 7-8 for handoff template.
>
> **Agent is NOT active until supervisor acknowledges (G8).**

### Step 8: Report

Output summary:

```
## Agent Created: {agent-name}

**Template**: template-{type}-aget
**Location**: {agent-path}
**Write Scope**: {-aget|-AGET}

**Status**:
- [x] G0: Pre-requisites validated
- [x] G1: Ontology created (user-guided)
- [x] G3: Instance created from template
- [x] G4: Capability configured
- [x] G5: Validation passed
- [x] G6: Initial assignment complete
- [ ] G7: Supervisor handoff (pending)
- [ ] G8: Fleet registration (pending supervisor ACK)

**Next Steps**:
1. Submit handoff document to supervisor
2. Address any remediation items from supervisor review
3. Begin first session with `/aget-wake-up`
```

## Constraints

These are INVIOLABLE:

1. **NEVER** create agent instance before ontology (G1) is complete
2. **NEVER** skip supervisor handoff (G7-G8) — agent is not active without ACK
3. **NEVER** modify the instantiation script (aget/ repo scope, not this agent's)
4. **NEVER** overwrite an existing agent directory without explicit confirmation
5. **DO** validate write scope (-aget vs -AGET) before proceeding (L480)
6. **DO** reference SOP_aget_create.md for detailed gate procedures
7. **DO** pause at human gates (G1 ontology, G7 handoff) and wait for user

## Rationale

Per AGET theoretical grounding:
- **Ontology-Driven Creation** (L481): Vocabulary and specs DRIVE agent creation
- **SKOS+EARS Grounding** (L482): Formal vocabulary + testable requirements
- **Fleet Registration** (L487): Agents are not active until supervisor acknowledges
- **Write Scope** (L480): Naming convention encodes authorization level

This skill implements the "ontology-driven agent creation" pattern by wrapping `SOP_aget_create.md` and `instantiate_template.py` into a guided workflow.

## Traceability

| Link | Reference |
|------|-----------|
| SOP | `aget/sops/SOP_aget_create.md` v2.2.0 |
| Script | `aget/scripts/instantiate_template.py` |
| Spec | `.aget/specs/skills/SKILL-019_aget-create-aget.yaml` |
| L-docs | L480, L481, L482, L487 |
| Tests | T-CA-001 through T-CA-003 (manual validation) |

---

*aget-create-aget v1.0.0*
*Category: Supervision*
*Based on SOP_aget_create.md v2.2.0 (Ontology-Driven Agent Creation)*
