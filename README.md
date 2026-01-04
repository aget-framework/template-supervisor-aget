# template-supervisor-aget: Supervisor AGET Template

> **aget-framework Organization** - Private until supervisor patterns stabilize
>
> Base template for creating supervisor AGETs with fleet coordination capabilities

## What This Is

**template-supervisor-aget** is the official supervisor template for the AGET framework. This template provides the foundation for creating supervisor AGETs that coordinate multiple worker agents across portfolios.

This template extends the worker agent template with additional capabilities for fleet management, multi-agent orchestration, and release coordination.

## Purpose

This template is designed for creating supervisor AGETs that:
- Coordinate multiple worker agents across portfolios
- Manage fleet-wide version migrations and upgrades
- Orchestrate multi-agent releases with gated execution
- Track patterns and learnings across agent fleet
- Provide centralized issue management and triage

## Current Status

**Version**: v3.1.0 "5D Composition Architecture"
**Privacy**: Private until supervisor patterns validated
**Organization**: aget-framework
**Publication Plan**: Will be made public when supervisor coordination patterns stabilize

### Key Capabilities
- ✅ Fleet coordination and management
- ✅ Gated release management (substantial change protocol)
- ✅ Multi-agent version migration orchestration
- ✅ Pattern deployment and versioning
- ✅ Session and evolution tracking
- ✅ GitHub issue management with auto-routing
- ✅ Portfolio-based agent organization

---

## Specification

| Attribute | Value |
|-----------|-------|
| **Governed By** | [AGET_TEMPLATE_SPEC v3.1](https://github.com/aget-framework/aget/blob/main/specs/AGET_TEMPLATE_SPEC.md) |
| **Foundation** | [WORKER_TEMPLATE_SPEC v1.0](https://github.com/aget-framework/aget/blob/main/specs/WORKER_TEMPLATE_SPEC_v1.0.yaml) |
| **Archetype** | Supervisor |
| **Manifest Version** | 3.0 |
| **Contract Tests** | 29 tests |

### Key Capabilities

| ID | Capability | Pattern |
|----|------------|---------|
| CAP-001 | Wake Protocol | event-driven |
| CAP-009 | Wind Down Protocol | event-driven |
| CAP-031 | Portfolio Coordination | optional |
| CAP-SUP | Fleet Management | ubiquitous |

Validate compliance: `pytest tests/ -v`

See: [Full specification](https://github.com/aget-framework/aget/tree/main/specs)

---

### Template Structure
```
template-supervisor-aget/
├── workspace/        # Internal workspace for explorations
├── products/         # Public products the supervisor maintains
├── .aget/            # Framework metadata and configuration
│   ├── evolution/    # Decision and discovery tracking
│   ├── checkpoints/  # Supervisor state snapshots
│   ├── patterns/     # Coordination patterns
│   └── registry/     # Agent fleet registry
└── tests/            # Contract tests and validation
```

## Template Philosophy

1. **Coordination Over Execution**: Supervisors orchestrate, workers execute
2. **Gate Discipline**: Every substantial change requires GO/NOGO checkpoints
3. **Fleet Visibility**: Centralized tracking of agent versions and status
4. **Pattern Evolution**: Continuous learning captured in evolution logs
5. **Explicit Decisions**: Document trade-offs and rationale

## Relationship to Worker Template

- **[template-worker-aget](https://github.com/aget-framework/template-worker-aget)**: Base template for worker agents
- **template-supervisor-aget**: Extends worker template with coordination capabilities
- **Inheritance**: Supervisor includes all worker protocols (wake, wind down, etc.)
- **Additional**: Fleet registry, multi-agent orchestration, release management

## Supervisor-Specific Capabilities

What makes this different from worker template:

**Fleet Management**:
- Agent registry with capability discovery
- Version tracking across portfolios
- Migration orchestration with gated execution
- Compliance monitoring and reporting

**Coordination Patterns**:
- Multi-agent release coordination
- Issue triage and routing
- Pattern deployment across fleet
- Centralized GitHub issue management

**Decision Tracking**:
- Evolution logs for major decisions
- Checkpoint system for supervisor state
- Session metadata with quantitative metrics
- Post-release deployment verification

## Getting Started

```bash
# Clone this template to create your own supervisor
git clone https://github.com/aget-framework/template-supervisor-aget.git my-supervisor-name-AGET

# Update identity in .aget/version.json
# - agent_name: "my-supervisor-name-AGET"
# - instance_type: "AGET" (supervisors are action-taking)
# - domain: your coordination domain

# Initialize your fleet registry
# Copy contract tests and validate

# Wake up and start coordinating
claude code
wake up
```

## Creation Details

- **Created**: 2025-09-25 (as my-AGET-template)
- **Transferred**: 2025-10-05 (to aget-framework org, renamed to template-supervisor-aget)
- **Nature**: Official supervisor template for aget-framework
- **Privacy**: Private until supervisor patterns stabilize (working towards public release)
- **Version Floor**: v2.5.0 (minimum version for all new agents as of 2025-10-04)

## Version Policy

**v2.5.0 as Floor** (Effective 2025-10-04):

All new agents created from this template must be at **v2.5.0 or higher**. This baseline includes:
- Contract testing framework (7 tests per agent)
- Identity protocol (agent_name, instance_type, domain fields)
- Deployment verification standards (L93)
- Gate 2.5 validation (identity field checks)

When creating a new agent from this template:
1. Copy the entire template structure
2. Update `.aget/version.json` to v2.5.0 or higher
3. Set identity fields (agent_name = directory name, instance_type, domain)
4. Copy contract tests to new agent
5. Run tests to validate before first commit

**Rationale**: Fleet-wide migration to v2.5.0 completed 2025-10-04. All agents now baseline at this version to ensure consistent validation and deployment practices.

## Documentation

Key documentation for supervisor coordination:
- `AGENTS.md` - Full agent configuration (symlinked to CLAUDE.md for backward compatibility)
- `CUSTOMIZATION_GUIDE.md` - How to adapt template for your fleet
- `PREREQUISITES.md` - System requirements and setup
- `products/DEMONSTRATION_GUIDE.md` - How to demonstrate supervisor capabilities
- `products/EXAMPLE_3_GATE_PLAN.md` - Simple 3-gate plan example
- `products/EXAMPLE_7_GATE_PLAN.md` - Complex 7-gate fleet migration example
- `.aget/evolution/` - Evolution logs with examples (L001, D001, DISC001)
- `.aget/registry/agents.yaml` - Fleet registry template
- `sessions/EXAMPLE_SESSION.md` - Session documentation example
- `tests/README.md` - Contract testing guide

## License

**AGET Framework (This Template)**: Apache License 2.0

This template and all framework code (`.aget/` structure, patterns, protocols) are licensed under the Apache License 2.0. This ensures:

- **Patent protection** for all adopters
- **Freedom to fork**, modify, and redistribute
- **Enterprise-safe** licensing for production use

See [LICENSE](LICENSE) for full terms.

**Your Agent Instance**: Your Choice

When you create an agent from this template, **you choose the license** for your specific instance:

- Keep it Apache 2.0 (recommended for public/shared agents)
- Make it private (all rights reserved)
- Choose MIT, GPL, or any other license

**The framework is open commons. What you build with it is yours.**

### Why Apache 2.0?

AGET is production infrastructure for agent configuration and lifecycle management. Apache 2.0 provides:

1. **Patent Grant**: Contributors can't patent their contributions and sue adopters
2. **Patent Retaliation**: If someone sues for patent infringement, they lose their license
3. **Ecosystem Immunity**: The standard stays free even as it becomes valuable
4. **Enterprise Adoption**: Legal teams approve Apache 2.0 more readily than other licenses

This follows the precedent of Kubernetes, Android, Swift, and other infrastructure projects.

### Upgrading Existing Agents

If you created an agent from an earlier MIT-licensed template, no action is required. Your agent remains valid under MIT (grandfathered).

To upgrade to Apache 2.0 for patent protection benefits, see the upgrade guide in the [AGET Framework documentation](https://github.com/aget-framework).

---

## Support

For questions about using this template:
- **Issues**: File to aget-framework/template-supervisor-aget when public
- **Current**: Private template, direct communication with maintainers

---

*template-supervisor-aget: Official supervisor template for AGET framework - extends worker template with fleet coordination capabilities*