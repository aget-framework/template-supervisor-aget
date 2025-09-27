# Discovery: Systemic Path Dependency Issue

## Date: 2025-09-27
## Type: DISC (Discovery)
## Severity: High

## Problem Statement
AGET projects inherit scripts and patterns from parent directories but use relative paths that break when directory context changes.

## 5-Why Root Cause Analysis

**Problem**: Referenced non-existent `smart_reader.py` causing session failures

1. **Why**: Wake protocol suggested `patterns/documentation/smart_reader.py` without verifying local existence
2. **Why**: `session_protocol.py` copied from parent where file exists
3. **Why**: AGET projects inherit patterns/scripts from parent repositories
4. **Why**: Parent has different structure that children don't inherit
5. **Root Cause**: No pattern synchronization mechanism - each project assumed self-contained but scripts use relative paths

## Scope of Issue

### Missing Scripts (Referenced but not present)
- ❌ `scripts/aget_housekeeping_protocol.py`
- ❌ `scripts/validate_patterns.py`
- ❌ `scripts/health_check.py`
- ⚠️  `scripts/aget_session_protocol.py` (exists in parent only)

### Missing Patterns (Referenced but not present)
- ❌ `patterns/bridge/extract_output.py`
- ⚠️  `patterns/meta/project_scanner.py` (parent only)
- ⚠️  `patterns/documentation/smart_reader.py` (parent only)

### Files With Issues
- **Documentation**: 15+ files reference non-existent scripts
- **Makefile**: References potentially missing scripts
- **Test plans**: Reference scripts that don't exist locally

## Impact Analysis

### Current Impact
- Session inefficiency (8-10 tools vs 2-3)
- Failed automation attempts
- Documentation-reality mismatch
- Broken test plans

### Potential Future Impact
- Migration failures when scripts don't exist
- Broken CI/CD pipelines
- Failed agent operations
- User confusion and frustration

## Solution Options

### Option 1: Absolute Paths (Quick Fix)
```python
# Use absolute paths to parent
python3 /Users/aget-framework/github/scripts/session_protocol.py
python3 /Users/aget-framework/github/patterns/documentation/smart_reader.py
```
**Pros**: Works immediately
**Cons**: Hardcoded paths, not portable

### Option 2: Dynamic Path Resolution (Better)
```python
# Check multiple locations
for base in [".", "..", "/Users/aget-framework/github"]:
    if Path(f"{base}/patterns/{pattern}").exists():
        use_this_path()
```
**Pros**: Flexible, handles both cases
**Cons**: More complex, slower

### Option 3: Pattern Synchronization (Best Long-term)
```bash
# Create symlinks or copy patterns
ln -s /Users/aget-framework/github/patterns .aget/parent-patterns
```
**Pros**: Clean separation, explicit dependencies
**Cons**: Requires setup step

### Option 4: Self-Contained Projects (Ideal)
```bash
# Each project has all needed files
aget install-patterns documentation session meta
```
**Pros**: True independence, portable
**Cons**: Duplication, maintenance burden

## Recommendations

### Immediate (Today)
1. Update session_protocol.py with dynamic path detection ✅
2. Document all cross-repository dependencies
3. Add warnings when scripts reference missing files

### Short-term (This Week)
1. Create `.aget/dependencies.json` listing external requirements
2. Add validation script to check all dependencies exist
3. Update documentation to reflect actual paths

### Long-term (This Month)
1. Implement pattern installer: `aget install-patterns`
2. Create pattern registry for sharing
3. Version patterns independently from projects

## Lessons Learned

1. **Assumption is dangerous**: Never assume file structure matches parent
2. **Relative paths break**: When context changes, relative paths fail
3. **Inheritance needs management**: Shared resources need explicit tracking
4. **Test in isolation**: Projects should be tested in clean environments
5. **Document dependencies**: External requirements must be explicit

## Action Items

- [x] Fix smart_reader.py references
- [ ] Audit all script references in documentation
- [ ] Create dependency manifest
- [ ] Implement path resolution helper
- [ ] Add CI test for missing dependencies

---
*Category: Infrastructure*
*Impact: High*
*Status: Partially Resolved*