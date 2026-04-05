# Template: Supervisor Agent

> Coordinate agent fleets with broadcast, review, and escalation capabilities

**Version**: v3.12.0 | **Archetype**: Supervisor | **Skills**: 6 specialized + 15 universal

---

## Why Supervisor?

The Supervisor archetype enables **multi-agent coordination** at scale. Unlike single-agent workflows, supervisor agents manage:

- **Fleet communication** — Broadcast announcements, directives, and release handoffs
- **Agent oversight** — Review health, conformance, and activity across agents
- **Escalation paths** — Route issues that exceed individual agent scope

**For evaluators**: If you're managing multiple AI agents or need coordination across a portfolio, the Supervisor archetype provides fleet governance without building custom orchestration.

**Domain knowledge that compounds**: Supervisor agents build persistent understanding of your fleet — agent capabilities, common failure patterns, escalation paths, and coordination strategies. Unlike tools that start fresh each session, your agent accumulates fleet intelligence that makes each broadcast more targeted, each review more insightful, and each escalation better routed.

---

## Skills

Supervisor agents come with **6 archetype-specific skills** plus the universal AGET skills.

### Archetype Skills

| Skill | Description |
|-------|-------------|
| **aget-broadcast-fleet** | Send communications to fleet members. Supports announcements, directives, and release handoffs with delivery tracking. |
| **aget-check-fleet** | Lightweight fleet health verification — 3 checks per agent (accessibility, structural integrity, symlink validity). Use for day-1 orientation or pre-delegation verification. |
| **aget-review-agent** | Review a specific agent's health, conformance level (L0-L5), and recent activity. Produces assessment with recommendations. |
| **aget-review-handoff** | Structured delegation review — compare agent output against delegation criteria, produce accept/reject decision with rationale. |
| **aget-escalate-issue** | Escalate issues to higher authority when they exceed current scope. Creates structured escalation documentation. |
| **aget-create-aget** | Create a new agent instance using the ontology-driven workflow. Guides through 9 SOP gates with human checkpoints. |

### Universal Skills

All AGET agents include session management, knowledge capture, and health monitoring:

- `aget-wake-up` / `aget-wind-down` — Session lifecycle
- `aget-create-project` / `aget-review-project` — Project management
- `aget-record-lesson` / `aget-record-observation` — Learning capture
- `aget-check-health` / `aget-check-kb` / `aget-check-evolution` / `aget-check-sessions` — Health monitoring
- `aget-propose-skill` / `aget-create-skill` — Skill development
- `aget-save-state` / `aget-file-issue` — State and issue management
- `aget-study-topic` — Focused KB research on a topic

---

## Ontology

Supervisor agents use a **formal vocabulary** of 8 concepts organized into 3 clusters:

| Cluster | Concepts |
|---------|----------|
| **Fleet Coordination** | Fleet, Agent_Registry, Portfolio |
| **Communication** | Broadcast, Directive, Handoff |
| **Governance** | Escalation, Conformance_Level |

This vocabulary enables precise communication about multi-agent coordination.

See: [`ontology/ONTOLOGY_supervisor.yaml`](ontology/ONTOLOGY_supervisor.yaml)

---

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/aget-framework/template-supervisor-aget.git my-supervisor-agent
cd my-supervisor-agent

# 2. Configure identity
# Edit .aget/version.json:
#   "agent_name": "my-supervisor-agent"
#   "domain": "your-domain"

# 3. Verify setup
python3 -m pytest tests/ -v
# Expected: All tests passing
```

### Try the Skills

```bash
# In Claude Code CLI
/aget-broadcast-fleet    # Send fleet communication
/aget-review-agent       # Review specific agent health
/aget-escalate-issue     # Escalate beyond current scope
```

---

## What Makes Supervisor Different

| Aspect | Single Agent | Supervisor Agent |
|--------|--------------|------------------|
| **Scope** | Own work only | Fleet-wide visibility |
| **Communication** | Direct messages | Structured broadcasts |
| **Issue handling** | Local resolution | Escalation pathways |
| **Health monitoring** | Self-check | Fleet-wide assessment |
| **Domain memory** | Starts fresh each session | Accumulates fleet coordination expertise over time |

---

## .claude/ Directory

| Directory | Purpose | Owner |
|-----------|---------|-------|
| `.claude/skills/` | Slash command definitions | Framework + Agent |
| `.claude/agents/` | Subagent definitions | Agent |
| `.claude/rules/` | Path-scoped context rules | Agent |

Skills are provided by the template. Agents and rules directories are scaffolded for your customization.

---

## Framework Specification

| Attribute | Value |
|-----------|-------|
| **Framework** | [AGET v3.12.0](https://github.com/aget-framework/aget) |
| **Archetype** | Supervisor |
| **Skills** | 21 total (6 archetype + 15 universal) |
| **Ontology** | 8 concepts, 3 clusters |
| **License** | Apache 2.0 |

---

## Learn More

- **[AGET Framework](https://github.com/aget-framework/aget)** — Core framework documentation
- **[Archetype Guide](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — All 12 archetypes explained
- **[Getting Started](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — Full onboarding guide

---

## Related Archetypes

| Archetype | Best For |
|-----------|----------|
| **[Worker](https://github.com/aget-framework/template-worker-aget)** | Task execution (supervised by this archetype) |
| **[Executive](https://github.com/aget-framework/template-executive-aget)** | Strategic decision support |
| **[Operator](https://github.com/aget-framework/template-operator-aget)** | Operational incident handling |

---

**AGET Framework** | Apache 2.0 | [Issues](https://github.com/aget-framework/template-supervisor-aget/issues)
