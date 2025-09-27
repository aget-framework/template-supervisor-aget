# ARCH-001 Template Compliance Gate Plan

## Executive Summary
Template must be ARCH-001 compliant before Gate 2 (v2.0-beta) or users will create broken projects.

## Critical Path with Go/No-Go Gates

### Pre-Gate 1: Foundation Check ✅
**Status**: PASSED (Gate 1 already released as v2.0-alpha)
**Note**: Internal use only, template issues not critical yet

---

### GATE 1.5: ARCH-001 Implementation (NEW - URGENT)
**Timeline**: Before Gate 2 (BLOCKING)
**Owner**: aget-cli-agent-template

#### Tasks (8-12 hours total)

##### Phase A: Template Cleanup (2 hours)
- [ ] Remove all `/Users/` paths from `.aget/*.json` files
- [ ] Replace absolute paths with relative or env variables
- [ ] Clean cost_tracking_config.json, claude_costs.jsonl, v2-baseline.json
- **Go/No-Go**: `grep -r "/Users/" . --exclude-dir=.git` returns nothing

##### Phase B: Self-Containment Infrastructure (3 hours)
- [ ] Copy `scripts/install_pattern.py` from my-AGET-aget
- [ ] Create template `.aget/dependencies.json`
- [ ] Add `scripts/verify_dependencies.py`
- [ ] Copy ARCH-001 decision document
- **Go/No-Go**: `python3 scripts/install_pattern.py --help` works

##### Phase C: Essential Patterns (2 hours)
- [ ] Create `patterns/documentation/` directory
- [ ] Add smart_reader.py or reference to parent
- [ ] Document pattern sources in dependencies.json
- [ ] Test pattern installation process
- **Go/No-Go**: Dependencies can be installed successfully

##### Phase D: Update Session Protocol (1 hour)
- [ ] Modify aget_session_protocol.py to remove parent fallbacks
- [ ] Add fail-fast for missing patterns
- [ ] Reference ARCH-001 in comments
- [ ] Test wake protocol uses local patterns
- **Go/No-Go**: Wake protocol works with local patterns only

##### Phase E: Template Validation (2 hours)
- [ ] Create test script for new project creation
- [ ] Test in isolated environment (no parent dirs)
- [ ] Verify "wake up; read docs" uses 2-3 tools
- [ ] Document in testing/v2_release/TEMPLATE_TEST.md
- **Go/No-Go**: New project from template passes all tests

#### Gate 1.5 Exit Criteria (MUST PASS ALL)
- ✅ No hardcoded user paths in template
- ✅ install_pattern.py included and working
- ✅ dependencies.json present and valid
- ✅ Session uses local patterns (no parent fallback)
- ✅ New project creation test passes
- ✅ "wake up; read docs" uses ≤3 tools

**DECISION POINT**: If any criterion fails → BLOCK Gate 2

---

### Gate 2: Beta Release
**Current Date**: Planned for ~Day 35-40
**Dependency**: Gate 1.5 MUST pass first

#### Additional Template Tests (2 hours)
- [ ] Create new project in /tmp (isolated)
- [ ] Run full test suite on new project
- [ ] Test with 3 different templates (agent, tool, hybrid)
- [ ] Verify no regression from Gate 1.5

#### Go/No-Go Criteria
- ✅ Gate 1.5 passed (template self-contained)
- ✅ Migration tests pass (existing plan)
- ✅ No path dependency errors
- ✅ New projects work immediately

**DECISION**:
- **GO**: Release v2.0-beta to collaborators
- **NO-GO**: Fix template issues, retest

---

### Gate 3: Migration Gate
**Note**: No template changes needed, internal only

---

### Gate 4: Release Candidate
**Dependency**: Gates 1.5 and 2 passed

#### Template Stability Check (1 hour)
- [ ] Review beta feedback for template issues
- [ ] Verify ARCH-001 compliance maintained
- [ ] Check dependency versions still valid
- [ ] Update documentation if needed

#### Go/No-Go
- ✅ No template regression since Gate 2
- ✅ Beta users successfully created projects
- ✅ Documentation accurate

---

### Gate 5: Public Release (v2.0)
**Date**: October 7 target

#### Final Template Validation (1 hour)
- [ ] Full template test in clean environment
- [ ] Verify all patterns included or installable
- [ ] Check documentation completeness
- [ ] Tag release

#### Go/No-Go
- ✅ All previous gates passed
- ✅ Template creates working projects
- ✅ Documentation complete
- ✅ No known critical issues

---

## Risk Assessment

### HIGH RISK (Gate Blockers)
- **Template has hardcoded paths**: Blocks Gate 2
- **Missing install_pattern.py**: Blocks Gate 2
- **Session protocol has parent fallbacks**: Blocks Gate 2

### MEDIUM RISK (Quality Issues)
- Documentation references non-existent files
- Pattern versions not tracked
- No verification script

### LOW RISK (Nice to Have)
- Template includes all patterns pre-installed
- Automated testing in CI
- Pattern marketplace integration

## Rollback Plan

If Gate 1.5 fails:
1. Continue using my-AGET-aget as reference
2. Document manual workarounds
3. Delay Gate 2 by 1 week maximum
4. If still blocked, reduce Gate 2 scope

## Success Metrics

- **Gate 1.5**: 100% of tests pass
- **Gate 2**: <5% of beta users report path issues
- **Gate 4**: 0 template-related blockers
- **Gate 5**: New project creation works first try

## Timeline Impact

- **Current**: Gate 2 at risk
- **With Gate 1.5**: Adds 8-12 hours
- **Without Gate 1.5**: Gate 2 creates broken projects
- **Recommendation**: Execute Gate 1.5 immediately

## Decision Required

**Do we proceed with Gate 1.5 implementation?**

- [ ] **YES** - Block Gate 2 until template compliant (RECOMMENDED)
- [ ] **NO** - Accept broken template, document workarounds
- [ ] **DEFER** - Ship Gate 2 with warnings, fix in Gate 4

---
*Created: 2025-09-27*
*Priority: CRITICAL PATH*
*Blocks: Gate 2 (v2.0-beta)*