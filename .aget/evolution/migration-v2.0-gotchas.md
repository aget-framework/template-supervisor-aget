# AGET v2.0 Migration Gotchas

## Migration Date
2025-09-28

## Starting State
- Version: 2.0.0-alpha
- Patterns: Split between root `patterns/` and `.aget/patterns/`
- Missing: Core v2.0 patterns

## Path Corrections Needed

### Pattern Location Change
**Issue**: Patterns were in both root `patterns/` and `.aget/patterns/`
**Resolution**: Consolidated all patterns to `.aget/patterns/`
**Impact**: Any scripts or references to `patterns/` need updating to `.aget/patterns/`

### Documentation References
**Issue**: CLAUDE.md referenced `patterns/documentation/smart_reader.py`
**Resolution**: Updated to `.aget/patterns/documentation/smart_reader.py`
**Impact**: Documentation and protocol references updated

## Pattern Conflicts Resolved

### Session Patterns
**Issue**: Had `commit_verification.py` but missing core session patterns
**Resolution**: Installed `wake_up.py`, `wind_down.py`, `wind_down_safe.py`
**Preserved**: Original `commit_verification.py` kept alongside new patterns

### EFFICIENT_STARTS.md
**Issue**: Already existed in `.aget/patterns/session/`
**Resolution**: Preserved during migration, no conflicts

## Custom Protocol Preservations

### Existing Customizations Maintained
- All 17 original pattern files preserved
- Custom `commit_verification.py` retained
- Existing session efficiency documentation kept
- Directory structure for existing patterns maintained

## Performance Impacts

### Positive
- Cleaner structure with all patterns in one location
- Faster pattern discovery (single directory tree)
- Self-contained architecture (ARCH-001 compliant)

### Neutral
- No performance degradation observed
- Pattern execution unchanged

## Migration Surprises

### Reference Template Structure
**Surprise**: Reference template had patterns in BOTH `patterns/` and `.aget/patterns/organization/`
**Learning**: v2.0 allows for gradual migration, but target is `.aget/patterns/` only

### GitHub Patterns
**Surprise**: No GitHub patterns in reference template's expected locations
**Resolution**: Created standard GitHub patterns based on v2.0 spec

### Session Pattern Naming
**Surprise**: Reference had `wake.py` instead of `wake_up.py`
**Resolution**: Renamed to match v2.0 specification during installation

## Rollback Information

Backup created at: `.aget/checkpoints/pre-v2-migration/`
Contains:
- Original patterns directory
- Original version.json
- Original CLAUDE.md

## Post-Migration Verification

All checks passed:
- ✓ Directory structure compliant
- ✓ Core patterns installed
- ✓ Self-contained (no external dependencies)
- ✓ Version updated to 2.0.0
- ✓ CLAUDE.md protocols updated

## Recommendations

1. Test all session protocols before production use
2. Verify GitHub integration with test issue
3. Update any automation scripts to use `.aget/patterns/` path
4. Consider removing backup after verification period

---
*Migration completed successfully from 2.0.0-alpha to 2.0.0*