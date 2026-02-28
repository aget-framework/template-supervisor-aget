# Pattern: Escalation Routing

**Version**: 1.0.0
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Category**: Governance
**Evidence**: Production escalation patterns (L520, SOP_escalation.md)

---

## Context

Supervisor agents receive issues and requests from multiple sources — fleet agents, human principals, external systems. Each requires different routing and handling.

## Problem

How to route escalations efficiently without bottlenecking the supervisor or losing context in handoffs.

## Solution

### Routing Decision Tree

```
Incoming Issue
  ├─ Critical? → Immediate supervisor attention
  ├─ Agent-specific? → Route to owning agent
  ├─ Cross-cutting? → Supervisor handles directly
  ├─ Framework-level? → Escalate to framework owner
  └─ Unclear? → Triage (add context, then re-route)
```

### Routing Rules

| Source | Severity | Route To |
|--------|----------|----------|
| Fleet agent | Critical | Supervisor (immediate) |
| Fleet agent | High/Medium | Supervisor (queue) |
| Fleet agent | Low | Agent self-resolves, supervisor notified |
| Human principal | Any | Supervisor (direct) |
| External | Any | Triage first, then route |

### Escalation Quality Checklist

Before escalating, the source should provide:
- [ ] Clear problem statement
- [ ] Impact assessment (who/what is affected)
- [ ] Options considered (if any)
- [ ] Recommended action (if any)
- [ ] Urgency justification

### Anti-Patterns

| Anti-Pattern | Detection | Resolution |
|--------------|-----------|------------|
| Escalation ping-pong | Issue bounced 3+ times | Assign clear owner, add context |
| Over-escalation | Routine decisions escalated | Clarify agent authority boundaries |
| Silent failure | Agent stuck but doesn't escalate | Regular session reviews catch this |

## Consequences

- **Positive**: Issues resolved by right party with right context
- **Negative**: Routing overhead (mitigated by clear rules)

## Related Patterns

- PATTERN_fleet_management.md — Fleet-wide oversight context
- SOP_escalation.md — Step-by-step escalation procedure
- Decision Authority table in AGENTS.md — Authority boundaries

---

*PATTERN_escalation_routing.md v1.0.0*
