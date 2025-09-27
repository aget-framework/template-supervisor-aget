# Decision: Pre-install welcomed flag

**Date**: 2025-09-26
**Type**: Design Decision
**Context**: RKB_analytics-aget first session experience

## Decision

Pre-create the `.aget/welcomed` flag during `aget init` to avoid runtime interruptions.

## Rationale

1. **No Bash Interruptions** - Avoid "touch .aget/welcomed" confirmation prompts
2. **Cleaner Flow** - Wake protocol doesn't need file creation logic
3. **Assumption** - Users who run `aget init` are ready to work
4. **Simplicity** - Less conditional logic in AGENTS.md

## Trade-offs

### What We Lose:
- First-time welcome message
- Onboarding guidance for new users
- Command suggestions on first encounter

### What We Gain:
- Uninterrupted workflow
- Simpler wake protocol
- No permission/confirmation issues
- Consistent experience every time

## Implementation

### For aget-template:
```python
# In aget/config/commands/init.py
def create_aget_structure(self, target):
    # Create .aget directories
    (target / ".aget").mkdir(exist_ok=True)
    (target / ".aget/evolution").mkdir(exist_ok=True)

    # Pre-create welcomed flag
    (target / ".aget/welcomed").touch()  # NEW
```

### For AGENTS.md template:
Remove the first-session welcome logic entirely. Users can discover capabilities through:
- Reading AGENTS.md directly
- Running "help" command
- Trying "demo" if curious
- Exploring src/ directory

## Alternative Considered

We considered showing welcome only on first wake, but this creates:
- Runtime file creation needs
- Bash confirmation interruptions
- Complex conditional logic
- Potential permission issues

## Decision Principle

**Simplicity over hand-holding** - Assume users are competent and can explore on their own. Documentation should be clear enough that explicit welcomes aren't needed.

## Impact on User Experience

- **Before**: Guided first experience with suggestions
- **After**: Direct to work, discover through exploration
- **Philosophy**: Professional tool, not tutorial

## Lesson for AGET

This reveals a design philosophy choice:
- **Option A**: Hand-holding, guided experience (welcome messages)
- **Option B**: Professional tool, self-discovery (pre-installed flags)

We choose **Option B** for AGET agents.

---

*This decision prioritizes workflow smoothness over first-time guidance.*