# SOP: Fleet Coordination

**Version**: 1.0
**Status**: DRAFT
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Evidence Source**: Derived from production supervisor coordination patterns (32-agent fleet)

---

## Purpose

Define standard procedures for coordinating work across a fleet of supervised agents.

## Scope

Applies when a supervisor agent needs to:
- Assign work to fleet agents
- Review agent outputs
- Broadcast fleet-wide communications
- Coordinate cross-agent dependencies

## Prerequisites

- Fleet registry maintained (`.aget/registry/FLEET_REGISTRY.yaml`)
- Agent portfolio assignments current
- Communication channels established (GitHub issues, broadcasts)

---

## Procedure 1: Work Assignment

### Step 1: Identify Work Item
1. Review incoming request or PROJECT_PLAN gate
2. Classify: agent-specific vs. cross-cutting vs. fleet-wide
3. Determine required capabilities

### Step 2: Select Agent
| Criteria | Check |
|----------|-------|
| Domain expertise | Agent's `identity.json` domain matches |
| Current workload | No active in-progress PROJECT_PLANs |
| Authority level | Agent has sufficient authority for the work |
| Portfolio scope | Work falls within agent's portfolio |

### Step 3: Assign
1. Create issue or PROJECT_PLAN item referencing the agent
2. Include: context, deliverables, success criteria, deadline
3. Use `/aget-broadcast-fleet` for fleet-wide assignments

### Step 4: Track
- Monitor agent session files for progress
- Review at gate boundaries
- Intervene if blocked (see Escalation SOP)

---

## Procedure 2: Output Review

### Step 1: Receive Output
- Agent completes gate or deliverable
- Review artifacts against success criteria

### Step 2: Evaluate
| Dimension | Check |
|-----------|-------|
| Completeness | All deliverables present |
| Quality | Meets spec requirements |
| Process | Gate discipline followed |
| Documentation | L-docs captured, session filed |

### Step 3: Provide Feedback
- Quantitative rating + specific observations + actionable next steps
- Example: "Process 8/10: Gate discipline followed, minor: checkpoint missing at 50% mark"

---

## Procedure 3: Fleet Broadcast

### When to Broadcast
| Type | Trigger | Example |
|------|---------|---------|
| Announcement | New version, policy change | "AGET v3.7.0 released" |
| Directive | Required action by agents | "Upgrade to v3.7.0 by [date]" |
| Handoff | Release-to-fleet coordination | Release handoff artifact |

### How to Broadcast
1. Use `/aget-broadcast-fleet` skill
2. Include: type, urgency, action required, deadline
3. Track delivery confirmation

---

## Anti-Patterns

| Anti-Pattern | Description | Consequence |
|--------------|-------------|-------------|
| Micromanagement | Reviewing every minor action | Agent bottleneck, trust erosion |
| Silent Delegation | Assigning without context | Misaligned output, rework |
| Broadcast Fatigue | Too many fleet communications | Important messages ignored |

---

## Related Documents

- `/aget-broadcast-fleet` — Fleet communication skill
- `/aget-review-agent` — Agent review skill
- `SOP_escalation.md` — When coordination becomes escalation
- `governance/CHARTER.md` — Supervisor authority boundaries

---

*SOP: Fleet Coordination v1.0 (DRAFT)*
*Evidence: Production supervisor fleet coordination patterns*
*Lifecycle: DRAFT — validate through operational use before promoting to ACTIVE*
