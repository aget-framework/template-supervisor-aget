# Example 3-Gate Plan: Internal Documentation Update

**Context**: Simple, low-risk task for internal documentation
**Task**: Update agent onboarding documentation based on recent feedback
**Complexity**: Low (3-5 files, fully reversible, internal-only)

---

## Gate Sizing Calculation (L104)

Using gate sizing heuristic from AGENTS.md:

- **Reversibility**: Fully reversible (git) = +0
- **Impact Scope**: Internal-only = +0
- **Complexity**: Low (<5 files) = +0
- **Total**: 2-3 baseline + 0 = **3 gates** ✅

---

## Gate 0: Analysis & Planning (20 min)

### Intent
Understand current documentation state and identify gaps from user feedback.

### Objective
Create specific list of documentation updates needed.

### Actions

1. Review user feedback from last 3 onboarding sessions
2. Identify common pain points (missing sections, unclear instructions)
3. List specific files to update (expected: 3-5 markdown files)
4. Draft outline of changes for each file
5. Create update checklist

### Success Criteria
- [ ] User feedback reviewed (3 sessions)
- [ ] Pain points identified (list created)
- [ ] Files to update listed (3-5 files)
- [ ] Update outline drafted
- [ ] Estimated time per file calculated

### DECISION POINT
**Does the update plan address user pain points effectively?**

- **GO**: Plan is clear and comprehensive → Proceed to execution
- **NOGO**: Missing key issues → Revise plan

---

## Gate 1: Execute Documentation Updates (30 min)

### Intent
Apply planned updates to documentation files.

### Objective
Update 3-5 documentation files with clearer instructions and missing sections.

### Actions

1. Update docs/onboarding/GETTING_STARTED.md:
   - Add missing prerequisites section
   - Clarify installation steps
   - Add troubleshooting FAQ

2. Update docs/onboarding/FIRST_SESSION.md:
   - Add expected output examples
   - Include common errors and fixes
   - Link to related docs

3. Update docs/onboarding/CONFIGURATION.md:
   - Add configuration examples
   - Explain each setting
   - Add validation checks

4. Review changes for clarity and completeness

5. Test: Walk through docs as if new user

### Success Criteria
- [ ] All 3-5 files updated
- [ ] Missing sections added
- [ ] Unclear instructions clarified
- [ ] Examples included where helpful
- [ ] Walkthrough test passed

### DECISION POINT
**Do the updated docs address original pain points?**

- **GO**: Docs are clearer and more complete → Proceed to commit
- **NOGO**: Issues remain → Revise updates

---

## Gate 2: Commit & Verify (10 min)

### Intent
Commit changes and verify documentation improvements.

### Objective
Deploy updated documentation and confirm quality.

### Actions

1. Review git diff to confirm only doc files changed
2. Commit with descriptive message:
   ```bash
   git commit -m "docs: Improve onboarding documentation

   - Added prerequisites section to GETTING_STARTED.md
   - Added expected output examples to FIRST_SESSION.md
   - Added configuration examples to CONFIGURATION.md

   Addresses feedback from 3 recent onboarding sessions.
   Improves clarity for new users.
   "
   ```

3. Push to repository
4. Verify changes on GitHub (browse updated files)
5. Optional: Share with recent onboarding users for quick validation

### Success Criteria
- [ ] Git diff reviewed (only doc files)
- [ ] Commit created with clear message
- [ ] Pushed successfully
- [ ] Changes visible on GitHub
- [ ] Optional: User feedback collected

### DECISION POINT
**Are documentation improvements deployed and verified?**

- **GO**: Docs deployed successfully → Work complete ✅
- **NOGO**: Issues found → Fix before declaring done

---

## Summary

| Gate | Objective | Time | Risk |
|------|-----------|------|------|
| 0 | Analysis & Planning | 20 min | Low |
| 1 | Execute Updates | 30 min | Low |
| 2 | Commit & Verify | 10 min | Low |
| **Total** | **Documentation Update** | **60 min** | **Low** |

---

## Why 3 Gates?

**This is right-sized for:**
- Internal-only changes (no external users affected)
- Fully reversible (git history preserved)
- Low complexity (3-5 markdown files)
- Clear scope (specific pain points from feedback)

**Red flags that would indicate over-gating:**
- 7 gates for documentation updates
- Multiple verification gates for simple docs
- More time planning gates than executing work

**Simplification considered:**
- Could combine Gates 1+2 (execute + commit) into single gate
- Keeping separate because user validation (Gate 1 DECISION POINT) before committing is valuable
- 3 gates allows pause points: After planning, after execution, after deployment

---

**Pattern**: Simple, reversible, internal tasks → 2-3 gates
**Application**: Use this structure for documentation updates, internal refactoring, configuration changes
