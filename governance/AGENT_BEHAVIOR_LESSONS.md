# Agent Behavior Lessons

## Purpose
Document instances where agent behavior was inappropriate, to inform better agent design patterns.

## Critical Behaviors to Avoid

### 1. Premature Action-Taking (2025-09-25)
**What Happened**:
- Saw `OpenAI_DeepResearch-aget` repository name
- Immediately assumed it was wrong (mixed separators)
- Started editing files to "fix" the problem
- Created todo items and began making changes

**What Should Have Happened**:
- Notice the potential inconsistency
- ASK: "I notice this uses both underscores and hyphens. Is this intentional?"
- WAIT for clarification
- THEN act based on understanding

**Root Cause**:
- Over-confidence in pattern recognition
- Assumption that inconsistency = error
- Action-bias (jumping to fix rather than understand)

**Lesson for Agent Design**:
```python
# BAD PATTERN
if looks_wrong():
    fix_it()  # NO!

# GOOD PATTERN
if looks_unusual():
    ask_for_clarification()
    wait_for_response()
    if actually_wrong():
        propose_fix()
        if approved():
            fix_it()
```

## Behavior Patterns to Encourage

### Verification Before Action
1. Identify potential issue
2. State observation
3. Ask for clarification
4. Wait for confirmation
5. Then act

### Context Awareness
- Understand that external constraints exist
- We work with what we're given
- Not everything that looks inconsistent is wrong

## Implementation Ideas

### For AGET Framework
- Add "verification_required" flag for certain operations
- Implement "ask_before_fixing" pattern
- Create "assumption_check" middleware

### For Agent Prompts
- "When you notice something unusual, ask before changing"
- "Distinguish between 'different' and 'wrong'"
- "Respect existing constraints and contexts"

## Tracking

| Date | Behavior | Impact | Lesson |
|------|----------|---------|---------|
| 2025-09-25 | Premature action on naming | Almost "fixed" correct naming | Ask first, act second |

---
*This document helps us design better agents that collaborate rather than assume*