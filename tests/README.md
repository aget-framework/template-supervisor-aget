# Contract Tests

## Purpose

Contract tests validate agent compliance with AGET framework standards. These tests ensure your supervisor agent correctly implements core protocols (identity, wake behavior) required for fleet coordination.

**Why Contract Tests**:
- Prevent version drift (version.json consistency)
- Validate identity protocol (agent_name, instance_type, domain)
- Ensure wake protocol reports correct information
- Catch configuration errors before deployment

## Tests Included

### Wake Protocol Contract Tests (4 tests)
**File**: `test_wake_contract.py`

1. **`test_wake_protocol_reports_agent_name`**
   - Validates agent reports its identity correctly
   - Ensures agent_name matches directory name

2. **`test_wake_protocol_reports_version`**
   - Validates version format (X.Y.Z semantic versioning)
   - Ensures version is reported consistently

3. **`test_wake_protocol_reports_capabilities`**
   - Validates capability structure (dict or list formats supported)
   - Ensures supervisor capabilities are documented

4. **`test_wake_protocol_reports_domain`**
   - Validates domain specification exists
   - Ensures supervisor role/domain is clear

### Identity Contract Tests (3 tests)
**File**: `test_identity_contract.py`

1. **`test_identity_consistency_version_json_vs_manifest`**
   - Prevents version drift (L28 pattern)
   - Validates version.json == agent_manifest.yaml (if manifest exists)
   - **Critical**: Catches the most common migration error

2. **`test_identity_no_conflation_with_directory_name`**
   - Validates identity = location principle
   - Ensures agent_name matches directory name exactly
   - Prevents identity confusion across fleet

3. **`test_identity_persistence_across_invocations`**
   - Separates identity from operational state
   - Ensures agent_name, instance_type, domain are stable
   - Validates identity fields exist and are non-empty

## Running Tests

### Run All Contract Tests
```bash
cd ~/github/your-supervisor-aget
python3 -m pytest tests/test_wake_contract.py tests/test_identity_contract.py -v
```

### Run Specific Test File
```bash
# Wake protocol tests only
python3 -m pytest tests/test_wake_contract.py -v

# Identity tests only
python3 -m pytest tests/test_identity_contract.py -v
```

### Run Single Test
```bash
python3 -m pytest tests/test_identity_contract.py::test_identity_consistency_version_json_vs_manifest -v
```

## Expected Output

### All Tests Passing (7/7)
```
tests/test_identity_contract.py::test_identity_consistency_version_json_vs_manifest PASSED
tests/test_identity_contract.py::test_identity_no_conflation_with_directory_name PASSED
tests/test_identity_contract.py::test_identity_persistence_across_invocations PASSED
tests/test_wake_contract.py::test_wake_protocol_reports_agent_name PASSED
tests/test_wake_contract.py::test_wake_protocol_reports_version PASSED
tests/test_wake_contract.py::test_wake_protocol_reports_capabilities PASSED
tests/test_wake_contract.py::test_wake_protocol_reports_domain PASSED

========================== 7 passed in 0.15s ===========================
```

### Common Failures and Fixes

**Version Drift (test_identity_consistency_version_json_vs_manifest fails)**:
```
AssertionError: Version mismatch: version.json shows 2.5.0, agent_manifest.yaml shows 2.4.0
```
**Fix**: Update both files to same version atomically (see Version Promotion Protocol in AGENTS.md)

**Identity Mismatch (test_identity_no_conflation_with_directory_name fails)**:
```
AssertionError: agent_name 'old-name' does not match directory 'new-name'
```
**Fix**: Update agent_name in .aget/version.json to match directory name

**Missing Identity Fields (test_identity_persistence_across_invocations fails)**:
```
KeyError: 'agent_name' not found in version.json
```
**Fix**: Add identity fields to .aget/version.json:
```json
{
  "aget_version": "2.5.0",
  "agent_name": "your-supervisor-aget",
  "instance_type": "AGET",
  "domain": "your-coordination-domain"
}
```

## Template Adaptation

When instantiating this template:

1. **Update .aget/version.json**:
   ```json
   {
     "aget_version": "2.5.0",
     "agent_name": "your-supervisor-name-AGET",
     "instance_type": "AGET",
     "domain": "your-coordination-domain",
     "created": "2025-MM-DD",
     "template": "supervisor",
     "tier": "coordinator"
   }
   ```

2. **Run tests immediately**:
   ```bash
   python3 -m pytest tests/ -v
   ```

3. **Expected**: 7/7 tests pass (if template instantiation correct)

4. **If tests fail**: Fix before first commit (contract tests are version gate)

## Integration with CI/CD

Contract tests run fast (<0.2s) and should be part of:
- Pre-commit hooks (validate before each commit)
- CI/CD pipeline (validate on every push)
- Version promotion workflow (validate before version bump)

**Example pre-commit hook**:
```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 -m pytest tests/test_wake_contract.py tests/test_identity_contract.py -q
if [ $? -ne 0 ]; then
  echo "❌ Contract tests failed. Fix before committing."
  exit 1
fi
```

## Contract vs Application Tests

**Contract Tests** (this README):
- Validate framework compliance
- Test identity, version, wake protocol
- Same across all agents (universal)
- Fast (<0.2s), no external dependencies
- **Must pass** for v2.5.0+ compliance

**Application Tests** (separate):
- Validate your supervisor's specific functionality
- Test fleet management, issue routing, etc.
- Specific to your supervisor
- May be slower, may have dependencies
- Recommended but not required

Both types are valuable. Contract tests ensure framework compatibility, application tests ensure your logic works correctly.

## Version Compliance

**v2.5.0 Requirement**: All agents must pass 7 contract tests

**Migration from v2.4.0 or earlier**:
1. Add contract test files from template
2. Add identity fields to version.json
3. Run tests and fix failures
4. Commit tests with version promotion

**Template users**: Tests included by default, should pass out of the box

## References

- **Version Promotion Protocol**: AGENTS.md (prevents version drift)
- **Identity Protocol**: .aget/version.json structure
- **Evolution Log L28**: Version drift detection pattern
- **Gate 2.5 Validation**: Identity field requirements

---

**Status**: Contract tests are mandatory for v2.5.0+ compliance
**Execution Time**: <0.2s per agent
**Coverage**: 7 tests (wake: 4, identity: 3)
**Pass Rate Target**: 100% (7/7 tests passing)
