# Decision: Self-Contained AGET Architecture

## Date: 2025-09-27
## Type: DEC (Decision)
## Status: Accepted

## Context
Discovery of systemic path dependency issues where AGET projects reference parent resources using relative paths that break when structure differs.

## Decision
AGET projects will be **completely self-contained** with the following principles:

### 1. Self-Contained Islands
- Each AGET must have its own copy of ALL dependencies
- No runtime references to external/parent directories
- Changes in other AGETs must NOT impact this AGET
- Trade-off: Accept duplication for complete independence

### 2. Intentional Upgrades
- Updates must be explicitly requested and considered
- AGET itself can request updates: "I need pattern X updated"
- aget-AGET-aget (meta-agent) can manage updates across projects
- No automatic inheritance of parent changes
- Version pinning for all dependencies

### 3. Fail-Fast on Missing Dependencies
- Missing patterns/scripts must halt execution immediately
- No silent fallbacks or degraded modes for missing files
- Clear error messages identifying what's missing
- Rationale: Prevent damage from incomplete operations

## Implementation Plan

### Phase 1: Immediate (Today)
```bash
# Copy essential patterns from parent
cp /Users/aget-framework/github/patterns/documentation/smart_reader.py patterns/documentation/
cp /Users/aget-framework/github/patterns/meta/project_scanner.py patterns/meta/
```

### Phase 2: Pattern Installer (This Week)
```python
# scripts/install_pattern.py
def install_pattern(pattern_name, source_path):
    """Copy pattern from source, version it, update manifest"""
    # 1. Copy files
    # 2. Update dependencies.json
    # 3. Run verification
    # 4. Commit with version tag
```

### Phase 3: Upgrade Protocol (Next Week)
```bash
# AGET requests upgrade
aget request-upgrade smart_reader.py

# Manual upgrade with review
aget upgrade-pattern smart_reader.py --from=/path/to/source

# Bulk upgrade (careful!)
aget upgrade-all --dry-run
```

## Consequences

### Positive
- ✅ Complete independence - no external failures
- ✅ Predictable behavior - what you see is what runs
- ✅ Version control - every file tracked in git
- ✅ Portable - entire project can be moved/shared
- ✅ Testable - no hidden dependencies

### Negative
- ❌ Duplication - same patterns in multiple projects
- ❌ Maintenance burden - updates must be propagated
- ❌ Storage overhead - more disk space used
- ❌ Divergence risk - projects may drift apart

### Mitigations
1. **Pattern Registry**: Central catalog of available patterns
2. **Update Notifications**: AGET can check for updates
3. **Bulk Management**: aget-AGET-aget manages multiple projects
4. **Version Tracking**: Clear versioning in dependencies.json

## Validation Criteria
- [ ] No references to parent directories in code
- [ ] All patterns copied locally before use
- [ ] Dependencies.json lists all external sources
- [ ] Verification script catches missing files
- [ ] Project works in isolation (no parent needed)

## Alternative Considered
**Shared Library Model**: Reference parent patterns
- Rejected because: Violates independence principle
- Would save space but creates fragile dependencies

## References
- DISC-2025-09-27-path-dependency-issue.md
- User architectural guidance: self-contained, intentional, fail-fast

---
*Decision by: User + Claude (my-AGET-aget)*
*Impact: High - Fundamental architecture choice*
*Review date: 2025-10-27*