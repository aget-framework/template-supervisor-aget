# Workspace Directory

Your supervisor agent's private workspace for exploration, experiments, and work-in-progress artifacts.

## Purpose

The workspace is where your supervisor agent:
- Experiments with new patterns before formalizing
- Creates draft plans and analyses
- Generates temporary working documents
- Tests ideas before promoting to `products/`

**Key Distinction**:
- `workspace/` = Private, exploratory, temporary
- `products/` = Public, finalized, maintained
- `docs/` = Official documentation, stable

## Typical Contents

**Exploration**:
```
workspace/experiment_001_new_pattern.py
workspace/draft_fleet_analysis.md
workspace/coordination_hypothesis.md
```

**Work in Progress**:
```
workspace/DRAFT_migration_plan.md
workspace/INCOMPLETE_specification.yaml
workspace/WIP_enhancement_design.md
```

**Temporary Analyses**:
```
workspace/agent_comparison_matrix.md
workspace/performance_benchmarks.csv
workspace/issue_triage_notes.md
```

## Lifecycle

1. **Create**: Ideas start in workspace
2. **Iterate**: Refine through experimentation
3. **Graduate**: Move successful patterns to:
   - `products/` → Maintained deliverables
   - `docs/` → Official documentation
   - `.aget/patterns/` → Reusable patterns
   - `.aget/evolution/` → Lessons learned

4. **Archive**: Unsuccessful experiments can be deleted or documented in evolution logs

## Best Practices

**Naming**:
- Use descriptive names
- Prefix experiments: `experiment_NNN_description`
- Prefix drafts: `DRAFT_`, `WIP_`, `INCOMPLETE_`

**Lifecycle Management**:
- Regularly review and clean workspace
- Don't let experiments accumulate indefinitely
- Document learnings from failed experiments

**Not for**:
- Final deliverables (use `products/`)
- Official documentation (use `docs/`)
- Session notes (use `sessions/`)
- Evolution logs (use `.aget/evolution/`)

## Supervisor-Specific Usage

**Fleet Analysis**:
```
workspace/fleet_health_assessment.md
workspace/version_distribution_analysis.md
```

**Coordination Experiments**:
```
workspace/parallel_migration_prototype.py
workspace/cross_agent_communication_test.md
```

**Planning Iterations**:
```
workspace/DRAFT_v2.6_migration_strategy.md
workspace/issue_routing_rules_v3.yaml
```

## Template Usage

This directory is empty in the template. Your workspace files will appear here as you explore and experiment with your supervisor agent.

---

**Workspace is for exploration. Create freely, iterate quickly, graduate or archive decisively.**
