# AGET Agent Mission-Vision Pattern
*Discovered: 2025-09-26*

## Pattern Definition
Every AGET agent CAN have (optional but recommended):
1. **Vision** with concrete success measures
2. **Mission** with near/mid/long-term goals aligned to maximize the vision

**Importance Scaling**: The more important/critical the agent becomes, the less optional these become.

## Structure Template

### Vision
- **What success looks like** (the ideal end state)
- **Success measures** (how we know we're getting there)
- **Why this matters** (the value created)

### Mission
Temporal goals that approximate/maximize the vision:

#### Near-Term Goals (next 3 months)
- **Commitment Level**: [ASPIRATIONAL | PLANNED | COMMITTED]
- Concrete deliverables with dates
- Directly measurable outcomes

#### Mid-Term Goals (3-12 months)
- **Commitment Level**: [UNDEFINED | ASPIRATIONAL | DIRECTIONAL]
- Capability building milestones
- Progress indicators

#### Long-Term Goals (12+ months)
- **Commitment Level**: [DIRECTIONAL | VISIONARY]
- Strategic positioning
- Ecosystem effects

## Alignment Principle
Each mission tier should:
- **Approximate** the vision (get closer to it)
- **Maximize** the success measures (improve the metrics)
- **Build on** previous tiers (compound progress)

## Example Implementation

### For a Code Review Agent
**Vision**: Zero defects reach production through perfect automated review
**Success Measure**: Defect escape rate < 0.1%

**Mission**:
- **Near**: Review 100 PRs, catch 80% of issues
- **Mid**: Learn from misses, reach 95% catch rate
- **Long**: Become trusted as sole reviewer for certain changes

### For a Documentation Agent
**Vision**: Self-documenting codebases that explain themselves
**Success Measure**: New developer onboarding time < 1 day

**Mission**:
- **Near**: Generate accurate README for 10 projects
- **Mid**: Auto-update docs on every commit
- **Long**: Predictive documentation before code is written

## When to Implement

### Optional For:
- **Experimental agents** (just exploring)
- **Utility agents** (simple tools)
- **Personal agents** (single user)
- **Throwaway agents** (temporary needs)

### Recommended For:
- **Team agents** (multiple users)
- **Long-lived agents** (6+ months)
- **Public agents** (open source)

### Required For:
- **Production agents** (business critical)
- **Framework agents** (like aget-aget itself)
- **Revenue-generating agents**
- **Compliance-sensitive agents**

## Benefits
- **Clarity**: Everyone knows what the agent is trying to achieve
- **Progress Tracking**: Clear metrics show advancement
- **Commitment Transparency**: Explicit about what's promised vs hoped
- **Strategic Alignment**: All actions serve the vision

## Implementation Notes
- Store in `governance/MISSION.md` or `.aget/mission.json`
- Review quarterly, adjust commitment levels as needed
- Failed missions are learning opportunities, document why
- Vision can evolve but should be stable; missions iterate frequently

---
*Pattern Status: DISCOVERED (seen in practice, not yet standardized)*