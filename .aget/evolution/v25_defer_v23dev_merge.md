# Decision: Defer v2.3-dev Merge Until Post-Migration

**Date**: 2025-10-06
**Context**: v2.5.0 Wave 1 complete, Wave 2-5 pending (19 agents)

## Features on v2.3-dev

- Session metadata system (schemas, validators, docs)
- Pattern versioning system (compatibility checks, bumping)
- 2,526 lines total
- Last commit: 2025-10-02

## Why Deferred

**Risk Assessment:**
- Zero test coverage for new features (2,526 untested lines)
- Features are enhancements, not core validation requirements
- Mid-migration timing risk (14 hours, 19 agents remaining)
- Clean merge possible later (no conflicts confirmed)

**Strategic Rationale:**
- Wave 2-5 uses proven v2.5.0 baseline (7 contract tests, zero unknowns)
- Reduces blast radius if issues emerge during migration
- Features are deployment tooling (coordinator → agent push), not agent validation
- Bitrot risk LOW (recent work, clean merge preview successful)

## Investigation Evidence

**Timeline Check:**
- v2.3-dev last commit: 2025-10-02 (2 days ago)
- v2.3-dev unique commits: 2
  - "Deploy session metadata system from coordinator (Gate A3)"
  - "Deploy pattern versioning system from coordinator (Gate A2)"

**Test Coverage:**
```bash
find tests/ -name "*session*" -o -name "*metadata*" -o -name "*version*"
# Result: No feature-specific tests found
pytest tests/ -v
# Result: 7/7 basic setup tests pass (no feature coverage)
```

**Merge Conflict Preview:**
```bash
git merge --no-commit --no-ff v2.3-dev
# Result: "Automatic merge went well; stopped before committing"
# No conflicts - safe to merge later
```

**Files Added by v2.3-dev:**
- `.aget/patterns/MIGRATION_TEMPLATE.md`
- `.aget/patterns/versions.yaml`
- `.aget/schemas/session_metadata_v1.0.json`
- `.aget/schemas/session_metadata_v1.0.yaml`
- `.aget/tools/bump_pattern.py`
- `.aget/tools/check_pattern_compatibility.py`
- `.aget/tools/generate_session_metadata.py`
- `.aget/tools/validate_session_metadata.py`
- `docs/PATTERN_VERSIONING.md`
- `docs/SESSION_METADATA_MIGRATION_GUIDE.md`

## Integration Plan

**When:** After Wave 2-5 complete (all agents at v2.5.0)

**Prerequisites:**
1. Add test coverage for session metadata tools
2. Add test coverage for pattern versioning tools
3. Clean up version references (v2.3-dev branch name vs v2.0.0 in version.json)
4. Verify "deployment script" dependencies exist

**Integration Steps:**
1. Merge v2.3-dev → main
2. Run full test suite (expect 7 contract + N feature tests)
3. Update version to v2.5.1 (enhancement release)
4. Deploy to coordinator first (test in production)
5. Then deploy to fleet if stable

**Target Timeline:** Within 2-4 weeks to minimize bitrot

**Tag for Retrieval:** `archive/v2.3-dev-session-metadata-and-versioning`

## Lessons Learned

**Process Gap Identified:**
- Features marked "Status: Active" in documentation without test coverage
- Production-ready claims require verification

**Future Gate:** Add "test coverage verification" checkpoint before marking features production-ready

**Version Management:** Branch names, version.json, and docs should align before merge

## Decision Authority

- Supervisor assessment: Defer (Path C recommended)
- Advisory concurrence: Defer (HIGH confidence)
- Rationale: Risk asymmetry (merge-now risks >> defer risks)

## Related Documents

- Investigation session: `sessions/SESSION_2025-10-06_v25_wave1_and_v23dev_investigation.md`
- v2.5 migration plan: `products/V2.5_COMPLETE_FLEET_MIGRATION_PLAN.md`
- Fleet registry: `workspace/v2.5_COMPLETE_FLEET_REGISTRY.md`
