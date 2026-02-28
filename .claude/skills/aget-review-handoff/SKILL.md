---
name: aget-review-handoff
description: Structured delegation review — compare agent output against delegation criteria, accept or reject with rationale
archetype: supervisor
allowed-tools:
  - Read
  - Glob
  - Grep
---

# aget-review-handoff

Review a delegated task's output against the original delegation criteria. Produces a structured accept/reject decision with rationale. Designed for formulaic, repeatable reviews — not deep analysis.

## When to Use

- **Post-delegation**: Agent reports task complete — review before accepting
- **Milestone check**: Mid-task checkpoint against delegation criteria
- **Handoff acceptance**: Agent transferring work to another agent — verify completeness
- **Session boundary**: Reviewing work done during a session before wind-down

## Input

```
/aget-review-handoff                           # Interactive: prompt for delegation + output
/aget-review-handoff <delegation-ref>          # Review specific delegation by reference
```

**Required context** (provided by user or read from artifacts):
1. **Delegation**: The original task assignment (what was asked, acceptance criteria, constraints)
2. **Output**: The agent's deliverables (files created, changes made, reports generated)

## Instructions

When this skill is invoked:

1. **Read Delegation**
   - Load the original delegation (from session file, issue, or user-provided context)
   - Extract: objective, acceptance criteria, constraints, expected deliverables
   - If delegation has no explicit criteria, note "implicit criteria — review may be subjective"

2. **Read Output**
   - Identify what the agent produced (files, commits, reports, session notes)
   - Map each deliverable to the delegation's expected outputs
   - Note any undelivered items or unexpected additions

3. **Compare Against Criteria**
   - For each acceptance criterion: PASS / PARTIAL / FAIL with evidence
   - For each constraint: RESPECTED / VIOLATED with evidence
   - For each expected deliverable: DELIVERED / MISSING / MODIFIED

4. **Score (Optional)**
   - **Process**: Did the agent follow the expected workflow? (X/10)
   - **Content**: Does the output meet quality standards? (X/10)
   - **Strategic**: Does the output advance the broader goal? (X/10)
   - Scoring is optional — criteria comparison (step 3) is sufficient for accept/reject

5. **Decision**
   - **ACCEPT**: All criteria met, no constraint violations
   - **ACCEPT WITH CONDITIONS**: Minor gaps, list conditions for full acceptance
   - **REJECT**: Criteria not met or constraints violated, provide specific rationale and remediation guidance

## Output Format

```markdown
## Handoff Review: [Delegation Reference]

**Agent**: [agent-name]
**Delegation Date**: [YYYY-MM-DD]
**Review Date**: [YYYY-MM-DD]

---

### Criteria Assessment

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | [criterion from delegation] | PASS | [what satisfies it] |
| 2 | [criterion from delegation] | PARTIAL | [what's missing] |
| 3 | [criterion from delegation] | FAIL | [why it fails] |

### Constraint Check

| Constraint | Status | Notes |
|------------|--------|-------|
| [constraint 1] | RESPECTED | — |
| [constraint 2] | VIOLATED | [how] |

### Deliverables

| Expected | Status | Location |
|----------|--------|----------|
| [deliverable 1] | DELIVERED | [path/ref] |
| [deliverable 2] | MISSING | — |

### Scoring (Optional)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Process | [X/10] | [workflow adherence] |
| Content | [X/10] | [quality assessment] |
| Strategic | [X/10] | [goal alignment] |

---

### Decision: [ACCEPT / ACCEPT WITH CONDITIONS / REJECT]

**Rationale**: [1-2 sentences explaining the decision]

**Conditions** (if ACCEPT WITH CONDITIONS):
1. [condition 1]
2. [condition 2]

**Remediation** (if REJECT):
1. [specific action to address failure]
2. [specific action to address failure]
```

## Implementation Guidance

### Criteria Extraction Pattern

When reading a delegation, extract criteria from these common patterns:

```python
# Delegation often appears in these formats:
CRITERIA_PATTERNS = [
    "acceptance criteria:",     # Explicit criteria section
    "success looks like:",      # Outcome-based
    "done when:",               # Completion-based
    "must:",                    # Imperative requirements
    "deliverables:",            # Output-based
    "V-test:",                  # Verification test (AGET convention)
]
```

### Decision Logic

```python
def decide(criteria_results: list, constraint_results: list) -> str:
    """Determine accept/reject from criteria and constraint results."""
    has_fail = any(c["status"] == "FAIL" for c in criteria_results)
    has_violation = any(c["status"] == "VIOLATED" for c in constraint_results)
    has_partial = any(c["status"] == "PARTIAL" for c in criteria_results)

    if has_fail or has_violation:
        return "REJECT"
    if has_partial:
        return "ACCEPT WITH CONDITIONS"
    return "ACCEPT"
```

### Implicit Criteria Handling

When delegation lacks explicit criteria (common in informal delegations):

| Signal | Inferred Criterion |
|--------|--------------------|
| "Fix the bug in X" | Bug no longer reproducible |
| "Update docs for Y" | Docs reflect current Y behavior |
| "Create Z" | Z exists and is functional |
| "Review A" | Review comments provided with rationale |

Flag implicit criteria in the review: "Note: criteria inferred from delegation wording — no explicit acceptance criteria provided."

## Constraints

- **C1**: Read-only — NEVER modify delegation artifacts or agent output during review
- **C2**: Evidence-based — every PASS/FAIL must cite specific evidence (file, line, commit)
- **C3**: Scope-bounded — only review against stated criteria, don't expand scope during review
- **C4**: Formulaic — follow the template structure; consistency across reviews matters more than prose quality

## Relationship to Other Skills

| Skill | Role | When |
|-------|------|------|
| **aget-review-handoff** (this) | Criteria-based accept/reject | Post-delegation, milestone, handoff |
| aget-review-agent | Full agent assessment | Periodic review |
| aget-review-project | PROJECT_PLAN progress | Mid-flight assessment |
| aget-broadcast-fleet | Communicate review result | After accept/reject decision |

## Traceability

| Link | Reference |
|------|-----------|
| Evidence | Supervisor 1 (3-dimensional scoring, formulaic), Supervisor 2 (criteria comparison, accept/reject) |
| Design | Criteria-based core (Sup 2) with optional scoring overlay (Sup 1) — reconciles both approaches |
| Spec | TBD (to be created with skill proposal) |
| Ontology | Delegation, Handoff, Work_Assignment (ONTOLOGY_supervisor.yaml) |
| Pattern | SOP_fleet_coordination.md (Output Review procedure) |
| CAP | CAP-SUP-001 (Work Delegation and Review) |
