# X-AGET Independence Principle
*For graduation to aget-cli-agent-template*

## Core Principle
Every X-aget repository MUST be completely self-contained and portable.

## Definition
An X-aget is independent when it can be:
- Cloned to any location
- Run without parent dependencies
- Shared as a complete unit
- Understood in isolation

## Anti-Patterns (What We Just Fixed)
```bash
# BAD: External dependency
python3 /Users/aget-framework/github/scripts/session_protocol.py

# GOOD: Local reference
python3 scripts/session_protocol.py
```

## Testable Requirements
1. **No absolute paths outside repository**
   - Test: `grep -r "^[^#]*/Users/" . --exclude-dir=.git`
   - Expected: No results

2. **All referenced scripts exist locally**
   - Test: Parse AGENTS.md/CLAUDE.md for script references
   - Expected: All scripts found in local directories

3. **No parent directory references**
   - Test: `grep -r "\.\./\.\." . --exclude-dir=.git`
   - Expected: No climbing beyond repo root

4. **Self-contained execution**
   - Test: Clone to temp directory and run basic commands
   - Expected: All commands work

## Implementation: aget validate

```bash
# Proposed command
aget validate [path]

# Checks:
- [ ] No external absolute paths
- [ ] All imports/scripts exist locally
- [ ] Configuration files portable
- [ ] No parent directory escapes
- [ ] Can run session protocols
- [ ] Dependencies documented

# Output:
✅ Repository is independent
❌ Found 3 violations:
  - External script reference in AGENTS.md:56
  - Absolute path in Makefile:23
  - Parent directory escape in scripts/helper.py:12
```

## Principle: Testable Principles

**Key Insight**: Every architectural principle must have a test.

If you can't test it, it's not a principle - it's a wish.

### Framework for Testable Principles

1. **Principle Statement**: Clear, single responsibility
2. **Success Criteria**: Measurable outcomes
3. **Test Command**: Automated validation
4. **Failure Examples**: What violations look like
5. **Fix Patterns**: How to resolve violations

### Examples of Testable Principles

| Principle | Test Command | Pass/Fail |
|-----------|--------------|-----------|
| Independence | `aget validate` | Binary |
| Security | `aget security-scan` | Graded |
| Performance | `aget benchmark` | Threshold |
| Documentation | `aget docs-check` | Coverage % |

## Migration Path

### Phase 1: Document (Now)
- Capture principle in products/
- Create manual test checklist

### Phase 2: Implement (Saturday Release)
- Add to aget-cli-agent-template docs
- Create validation script

### Phase 3: Enforce (Future)
- Run on agent creation
- Pre-commit hooks
- CI/CD integration

## Lessons from Today's Fix

1. **Silent success is dangerous** - Dependencies worked until they didn't
2. **Templates propagate patterns** - Both good and bad
3. **Explicit validation prevents drift** - Can't manage what you don't measure
4. **Independence enables evolution** - Each repo can grow freely

## Recommendation

Add this to Saturday's release as a "safety pattern":
- Document the principle
- Provide manual checklist
- Promise `aget validate` in beta.2

This prevents future X-agets from suffering the same coupling issue.

---
*Discovery Date: 2025-09-26*
*Status: Ready for graduation to aget-cli-agent-template*