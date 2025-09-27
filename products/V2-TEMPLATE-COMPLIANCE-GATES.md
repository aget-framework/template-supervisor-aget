# V2 Template Compliance: Go/No-Go Gates & Tasks

## Mission Critical
Ensure aget-cli-agent-template creates self-contained, working AGET projects before v2.0-beta release.

## Gate Timeline Overview
```
Gate 1 (DONE) → Gate 1.5 (NEW) → Gate 2 → Gate 3 → Gate 4 → Gate 5
   ↓               ↓                ↓        ↓        ↓        ↓
v2.0-alpha    Template Fix    v2.0-beta    Skip    v2.0-rc   v2.0
```

---

# GATE 1.5: Template Self-Containment (BLOCKING)

## Gate Entry Criteria
- [ ] Gate 1 released (v2.0-alpha) ✅
- [ ] Template issues identified and documented ✅
- [ ] Working reference implementation exists (my-AGET-aget) ✅

## Phase A: Clean Template (2 hours)

### Tasks
```bash
# A.1: Audit for hardcoded paths
cd ../aget-cli-agent-template
grep -r "/Users/\|C:\\Users\\" . --exclude-dir=.git > path_audit.txt

# A.2: Clean each file
for file in .aget/cost_tracking_config.json .aget/claude_costs.jsonl .aget/v2-baseline.json; do
    # Remove user-specific paths
    sed -i '' 's|/Users/[^/]*/github/|./|g' $file
done

# A.3: Verify cleanup
grep -r "/Users/\|C:\\Users\\" . --exclude-dir=.git --exclude="*.md"
# Should return EMPTY
```

### Supporting Tasks
- [ ] A.1: Run path audit (15 min)
- [ ] A.2: Clean cost_tracking_config.json (15 min)
- [ ] A.3: Clean claude_costs.jsonl (15 min)
- [ ] A.4: Clean v2-baseline.json (15 min)
- [ ] A.5: Re-audit to verify (15 min)
- [ ] A.6: Commit with message "fix: Remove hardcoded paths (ARCH-001)" (15 min)

### Go/No-Go Decision A
**Command**: `grep -r "/Users/" . --exclude-dir=.git --exclude="*.md" | wc -l`
- **GO (proceed)**: Returns 0
- **NO-GO (stop)**: Returns >0 - paths still exist

---

## Phase B: Install Infrastructure (3 hours)

### Tasks
```bash
# B.1: Copy pattern installer from my-AGET-aget
cp ../my-AGET-aget/scripts/install_pattern.py scripts/

# B.2: Create dependencies manifest template
cat > .aget/dependencies.json << 'EOF'
{
  "schema_version": "1.0.0",
  "architecture": "self-contained",
  "upgrade_policy": "intentional",
  "failure_mode": "fail-fast",
  "required_patterns": [],
  "required_scripts": [
    {
      "name": "aget_session_protocol.py",
      "source": "local",
      "status": "installed"
    }
  ],
  "optional_patterns": []
}
EOF

# B.3: Create verification script
cat > scripts/verify_dependencies.py << 'EOF'
#!/usr/bin/env python3
"""Verify AGET is self-contained per ARCH-001."""
import json
import sys
from pathlib import Path

def verify():
    # Check dependencies exist
    if not Path(".aget/dependencies.json").exists():
        print("❌ Missing dependencies.json")
        return False

    # Check no external paths
    has_external = False
    for p in Path(".").rglob("*.py"):
        content = p.read_text()
        if "/Users/" in content or "C:\\Users\\" in content:
            print(f"❌ External path in {p}")
            has_external = True

    if has_external:
        return False

    print("✅ Self-contained verification passed")
    return True

if __name__ == "__main__":
    sys.exit(0 if verify() else 1)
EOF

chmod +x scripts/verify_dependencies.py
```

### Supporting Tasks
- [ ] B.1: Copy install_pattern.py (30 min)
- [ ] B.2: Adapt for template context (30 min)
- [ ] B.3: Create dependencies.json template (30 min)
- [ ] B.4: Create verify_dependencies.py (45 min)
- [ ] B.5: Test installation mechanism (30 min)
- [ ] B.6: Document in README (15 min)

### Go/No-Go Decision B
**Commands**:
```bash
python3 scripts/install_pattern.py --help
python3 scripts/verify_dependencies.py
```
- **GO**: Both commands succeed
- **NO-GO**: Either command fails

---

## Phase C: Core Patterns (2 hours)

### Tasks
```bash
# C.1: Setup pattern directories
mkdir -p patterns/documentation
mkdir -p patterns/meta

# C.2: Option 1 - Copy patterns (self-contained)
cp /Users/aget-framework/github/patterns/documentation/smart_reader.py patterns/documentation/
cp /Users/aget-framework/github/patterns/meta/project_scanner.py patterns/meta/

# C.3: Option 2 - Document as installable
cat >> .aget/dependencies.json << 'EOF'
  "required_patterns": [
    {
      "name": "documentation/smart_reader.py",
      "source": "https://github.com/aget-framework/aget-patterns/documentation/smart_reader.py",
      "version": "1.0.0",
      "status": "not_installed"
    }
  ]
EOF

# C.4: Test pattern installation
python3 scripts/install_pattern.py
```

### Supporting Tasks
- [ ] C.1: Create pattern directory structure (15 min)
- [ ] C.2: Decide copy vs reference strategy (30 min)
- [ ] C.3: Implement chosen strategy (45 min)
- [ ] C.4: Test pattern availability (20 min)
- [ ] C.5: Update dependencies.json (10 min)

### Go/No-Go Decision C
**Command**: `ls patterns/documentation/smart_reader.py 2>/dev/null || echo "MISSING"`
- **GO**: File exists OR can be installed
- **NO-GO**: File missing AND cannot install

---

## Phase D: Session Protocol Update (1 hour)

### Tasks
```bash
# D.1: Remove parent fallbacks from session protocol
sed -i '' '/\/Users\/.*\/github\/patterns/d' scripts/aget_session_protocol.py

# D.2: Add fail-fast for missing patterns
# Edit wake_up() method to check local patterns only

# D.3: Add ARCH-001 reference
sed -i '' '1a\
# ARCH-001: Self-contained architecture - no external dependencies\
' scripts/aget_session_protocol.py
```

### Supporting Tasks
- [ ] D.1: Remove parent directory references (20 min)
- [ ] D.2: Add pattern existence checks (20 min)
- [ ] D.3: Add fail-fast behavior (10 min)
- [ ] D.4: Test wake protocol (10 min)

### Go/No-Go Decision D
**Test**:
```bash
cd /tmp && cp -r ../aget-cli-agent-template test-template
cd test-template
python3 scripts/aget_session_protocol.py wake
```
- **GO**: Wake works without parent directory
- **NO-GO**: Wake fails or references parent

---

## Phase E: Integration Test (2 hours)

### Tasks
```bash
# E.1: Create test script
cat > test_template_compliance.sh << 'EOF'
#!/bin/bash
set -e

# Test in isolation
TESTDIR=$(mktemp -d)
cp -r . $TESTDIR/test-aget
cd $TESTDIR/test-aget

# Remove parent to ensure isolation
rm -rf ../patterns ../scripts

# Test 1: Verify no external paths
echo "Test 1: Checking for external paths..."
if grep -r "/Users/" . --exclude-dir=.git --exclude="*.md" > /dev/null; then
    echo "❌ Found external paths"
    exit 1
fi

# Test 2: Wake protocol works
echo "Test 2: Testing wake protocol..."
python3 scripts/aget_session_protocol.py wake || exit 1

# Test 3: Pattern installation works
echo "Test 3: Testing pattern installation..."
python3 scripts/install_pattern.py || exit 1

echo "✅ All tests passed"
EOF

chmod +x test_template_compliance.sh
./test_template_compliance.sh
```

### Supporting Tasks
- [ ] E.1: Create isolation test (30 min)
- [ ] E.2: Test new project creation (30 min)
- [ ] E.3: Test "wake up; read docs" efficiency (20 min)
- [ ] E.4: Document results (20 min)
- [ ] E.5: Create test report (20 min)

### Go/No-Go Decision E
**Test**: `./test_template_compliance.sh`
- **GO**: All tests pass
- **NO-GO**: Any test fails

---

# GATE 1.5 EXIT: Final Go/No-Go

## Exit Criteria Checklist
- [ ] Phase A: No hardcoded paths (**GO/NO-GO**)
- [ ] Phase B: Installation infrastructure works (**GO/NO-GO**)
- [ ] Phase C: Patterns available locally (**GO/NO-GO**)
- [ ] Phase D: Session protocol self-contained (**GO/NO-GO**)
- [ ] Phase E: Integration tests pass (**GO/NO-GO**)

## Final Efficiency Test
```bash
# Create new project and test efficiency
cd /tmp
git clone ../aget-cli-agent-template new-project
cd new-project
time (
    echo "wake up; read docs" | claude
    # Count tool uses in output
)
```

### Final Gate Decision
- **GO TO GATE 2**:
  - All phases passed
  - Tool count ≤3
  - No external dependencies

- **NO-GO (BLOCK GATE 2)**:
  - Any phase failed
  - Tool count >3
  - External dependencies found

## Rollback Plan
If Gate 1.5 fails after 2 attempts:
1. Document known issues in KNOWN_ISSUES.md
2. Add warning to installer
3. Provide manual fix instructions
4. Schedule Gate 1.6 for fixes
5. Proceed to limited Gate 2 with warnings

---

# GATE 2: Beta Release

## Entry Criteria
- [ ] Gate 1.5 passed (template self-contained)
- [ ] Migration tests ready (existing plan)

## Additional Template Validation (1 hour)

### Tasks
- [ ] Create 3 test projects (agent, tool, hybrid)
- [ ] Each must pass "wake up; read docs" with ≤3 tools
- [ ] No external path references
- [ ] All can install patterns

### Go/No-Go Decision
- **GO**: All test projects work
- **NO-GO**: Any project fails

---

# GATE 3: (Skip - Migration Only)

---

# GATE 4: Release Candidate

## Entry Criteria
- [ ] Gate 2 beta feedback collected
- [ ] No template regression

## Template Stability Check (30 min)

### Tasks
- [ ] Review beta issues for template problems
- [ ] Verify ARCH-001 still compliant
- [ ] Update any broken pattern references

### Go/No-Go Decision
- **GO**: No new template issues
- **NO-GO**: Template regression found

---

# GATE 5: Public Release

## Entry Criteria
- [ ] All previous gates passed
- [ ] RC feedback addressed

## Final Template Certification (30 min)

### Tasks
- [ ] Run full compliance test suite
- [ ] Create 10 test projects rapidly
- [ ] Verify all work first-try

### Go/No-Go Decision
- **GO**: 100% success rate
- **NO-GO**: Any failure

## Release Command
```bash
git tag -a v2.0 -m "Release v2.0 - Self-contained AGET template"
git push origin v2.0
```

---

## Summary Metrics

| Gate | Hours | Risk if Skipped | Impact |
|------|-------|----------------|--------|
| 1.5  | 8-12  | 100% failure rate | CRITICAL |
| 2    | 1     | Beta user frustration | HIGH |
| 4    | 0.5   | RC quality issues | MEDIUM |
| 5    | 0.5   | Public launch problems | HIGH |

**Total Investment**: 10-14 hours
**Risk Mitigation**: Prevents 100% failure rate for new projects
**ROI**: Every new AGET project works first-try

---
*Decision Required: Proceed with Gate 1.5 implementation?*
*Recommended: YES - Block Gate 2 until complete*