# Critical Template Fixes for V2 Release

## Priority: BLOCKER 🚨
**Must fix before v2.0 release or template will create broken AGETs**

## Problem Summary
aget-cli-agent-template violates ARCH-001 (self-contained architecture) and will create projects that fail on first use with path dependency errors.

## Critical Fixes Required

### 1. Remove Hardcoded Paths (BLOCKER)
**Files to fix**:
```
.aget/cost_tracking_config.json  # Has /Users/aget-framework paths
.aget/claude_costs.jsonl         # Has absolute paths in logs
.aget/v2-baseline.json          # Has user-specific paths
```
**Fix**: Replace with relative paths or environment variables

### 2. Add Self-Containment Infrastructure (BLOCKER)
**Files to add**:
```
scripts/install_pattern.py       # Pattern installer (copy from my-AGET-aget)
.aget/dependencies.json          # Dependency manifest template
docs/adr/ARCH-001-SELF-CONTAINED-PROJECTS.md  # Architecture decision
```

### 3. Include Essential Patterns (HIGH)
**Patterns to include or make installable**:
```
patterns/documentation/smart_reader.py  # Referenced but missing
patterns/meta/project_scanner.py       # For project scanning
```

### 4. Update Session Protocol (HIGH)
**Fix in** `scripts/aget_session_protocol.py`:
- Remove fallbacks to parent directories
- Add warning when patterns missing
- Reference ARCH-001 in comments

### 5. Template Initialization Script (MEDIUM)
**Create** `scripts/initialize_aget.py`:
```python
def initialize_new_aget():
    # 1. Remove user-specific paths
    # 2. Install default patterns
    # 3. Create dependencies.json
    # 4. Run verification
```

## Validation Checklist

Before v2.0 release, template must pass:
- [ ] No `/Users/` or `C:\Users\` in any file
- [ ] Dependencies.json exists and is valid
- [ ] install_pattern.py can run successfully
- [ ] New AGET from template works in isolation
- [ ] "wake up; read docs" uses 2-3 tools, not 8-10
- [ ] No references to parent directories
- [ ] All referenced patterns exist or can be installed

## Test Procedure

```bash
# Clone template to isolated location
cd /tmp
git clone <template-repo> test-aget
cd test-aget

# Remove any parent directories
rm -rf ../patterns ../scripts

# Test basic operations
claude  # or relevant CLI
> wake up; read docs  # Should work with 2-3 tools

# Verify self-contained
grep -r "/Users/" . --exclude-dir=.git  # Should return nothing
python3 scripts/install_pattern.py  # Should work
```

## Impact if Not Fixed

- **Every v2 user** will experience path errors
- **First impression** will be broken functionality
- **Trust damage** - promises reliability but delivers errors
- **Support burden** - Each user reports same issue
- **Adoption barrier** - Users abandon after first failure

## Recommended Approach

1. **Fix in my-AGET-aget first** (DONE ✅)
2. **Port fixes to template** (TODO)
3. **Test template in isolation** (TODO)
4. **Update v2 release checklist** (TODO)

## Files to Port from my-AGET-aget

These files embody the solution and should be adapted for template:
```
scripts/install_pattern.py
.aget/dependencies.json
docs/adr/ARCH-001-SELF-CONTAINED-PROJECTS.md
.aget/evolution/DEC-2025-09-27-self-contained-architecture.md
```

## Timeline

- **Must complete**: Before v2.0-beta (Gate 2)
- **Ideally complete**: Before v2.0-alpha tag
- **Latest acceptable**: Before any public announcement

---
*Created: 2025-09-27*
*Priority: RELEASE BLOCKER*
*Owner: aget-cli-agent-template maintainers*