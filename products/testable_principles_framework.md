# Testable Principles Framework
*Every principle must have a test*

## Core Insight
"If you can't test it, it's not a principle - it's a wish."

## Framework Definition

### What Makes a Principle Testable?

1. **Binary Outcome**: Pass or Fail (with optional gradations)
2. **Automated Check**: Can be run without human judgment
3. **Reproducible**: Same input → same output
4. **Fast Feedback**: Results in seconds, not minutes
5. **Actionable Results**: Clear what to fix when it fails

### Anatomy of a Testable Principle

```yaml
Principle:
  statement: "What must be true"
  rationale: "Why it matters"
  test_command: "How to verify"
  success_criteria: "What passing looks like"
  failure_examples: "What violations look like"
  fix_patterns: "How to resolve violations"
```

## Examples of Well-Defined Testable Principles

### 1. Independence Principle
**Statement**: X-aget repositories must be self-contained
**Test**: No paths outside repository boundary
**Command**: `grep -r "^[^#]*\(/Users/\|/home/\)" . --exclude-dir=.git`
**Pass**: No output
**Fail**: List of files with external paths

### 2. Commit Safety Principle
**Statement**: Every commit must be verified before proceeding
**Test**: Git operations return SHA on success
**Command**: `git rev-parse HEAD`
**Pass**: Returns 40-char SHA
**Fail**: Error or empty output

### 3. Error Visibility Principle
**Statement**: Critical errors must be unmissable
**Test**: CRITICAL errors display even in quiet mode
**Command**: `./script --quiet 2>&1 | grep "CRITICAL"`
**Pass**: Critical errors visible
**Fail**: Silent failure

### 4. Documentation Coverage Principle
**Statement**: Public functions must have docstrings
**Test**: Parse and check documentation
**Command**: `python -m pydoc -w . && grep -c "No documentation" *.html`
**Pass**: Count = 0
**Fail**: Count > 0

## Anti-Patterns: Non-Testable "Principles"

### ❌ "Code should be elegant"
- Not measurable
- Subjective judgment
- No binary outcome

### ❌ "Follow best practices"
- Too vague
- Which practices?
- How to verify?

### ❌ "Maintain high quality"
- Quality of what?
- By what measure?
- What's the threshold?

## Converting Wishes to Principles

### Wish → Principle Transformation

**Wish**: "Code should be maintainable"
**Principle**: "Functions must be <50 lines with cyclomatic complexity <10"
**Test**: `radon cc . -s -n B` (flags functions over threshold)

**Wish**: "Project should be well-documented"
**Principle**: "README must contain: purpose, setup, usage, examples"
**Test**: `grep -c "## Purpose\|## Setup\|## Usage\|## Examples" README.md` = 4

**Wish**: "Security should be a priority"
**Principle**: "No secrets in code, all credentials in .aget/secrets/"
**Test**: `grep -r "api_key\|password\|token" . --exclude-dir=.aget/secrets`

## Implementation in AGET

### Level 1: Manual Checklist
```markdown
## Release Checklist
- [ ] Run: `grep -r "/Users/" .` (expect: no results)
- [ ] Run: `pytest tests/` (expect: all pass)
- [ ] Run: `git status` (expect: clean)
```

### Level 2: Shell Script
```bash
#!/bin/bash
# validate_principles.sh

principles_passed=0
principles_failed=0

# Test each principle
test_independence && ((principles_passed++)) || ((principles_failed++))
test_security && ((principles_passed++)) || ((principles_failed++))
test_structure && ((principles_passed++)) || ((principles_failed++))

echo "✅ Passed: $principles_passed"
echo "❌ Failed: $principles_failed"
```

### Level 3: Integrated Tool
```bash
aget validate --all-principles

Testing 12 principles...
✅ Independence
✅ Security
✅ Structure
❌ Documentation (coverage: 67%, required: 80%)
✅ Performance
✅ Error Handling
...
Overall: 11/12 passed
```

## Principle Lifecycle

1. **Discovery**: Pattern emerges from usage
2. **Definition**: Convert to testable statement
3. **Validation**: Create automated test
4. **Integration**: Add to `aget validate`
5. **Evolution**: Refine based on violations

## Meta-Principle: Principles About Principles

**The Testability Principle**: Every principle must be testable
**Test**: Check if principle has test command
**Command**: `grep -c "test_command:" principles.yaml`
**Pass**: Count equals number of principles

## Benefits of Testable Principles

1. **Objective Enforcement**: No arguments about compliance
2. **Automated Validation**: CI/CD can enforce
3. **Clear Communication**: Everyone understands requirements
4. **Continuous Improvement**: Measure adoption and impact
5. **Reduced Drift**: Catch violations early

## Gradual Adoption Strategy

### Phase 1: Document (Now)
- Write principles as testable statements
- Create manual test commands

### Phase 2: Automate (Beta.1)
- Script the test commands
- Add to release process

### Phase 3: Integrate (Beta.2)
- Build into `aget validate`
- Add to CI/CD

### Phase 4: Enforce (v2.0)
- Block commits on violations
- Auto-fix where possible

## Conclusion

Testable principles transform architectural guidelines from philosophical statements into engineering constraints. They make quality measurable, enforceable, and improvable.

**Remember**: If you can't write a test for it, it's not ready to be a principle.

---
*Framework Created: 2025-09-26*
*Status: Ready for adoption in aget-cli-agent-template*