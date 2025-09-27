# Gate Risk: Template Non-Compliance with ARCH-001

## Date: 2025-09-27
## Type: GATE-RISK
## Severity: RELEASE BLOCKER
## Gate Affected: Gate 2 (v2.0-beta)

## Risk Summary
The aget-cli-agent-template is not compliant with ARCH-001 (Self-Contained Architecture) and will generate broken AGET projects that fail on first use.

## Evidence
1. **Hardcoded paths**: `/Users/aget-framework/github/` in multiple files
2. **Missing patterns**: smart_reader.py referenced but not included
3. **No installation mechanism**: No install_pattern.py script
4. **No dependency tracking**: No dependencies.json manifest

## Business Impact
- **100% failure rate** for new AGET projects from template
- **First-run failure** damages trust immediately
- **Support burden** as every user hits same issue
- **Reputation risk** for v2.0 launch

## Technical Impact
- Sessions use 8-10 tools instead of 2-3 (70% inefficiency)
- Path errors when patterns not found
- Cannot operate in isolation
- Violates core architectural principles

## Mitigation Required

### Before Gate 2 (MUST HAVE)
1. Remove all hardcoded paths from template
2. Add install_pattern.py to template
3. Include dependencies.json template
4. Update aget_session_protocol.py to be self-contained

### Before Gate 3 (SHOULD HAVE)
1. Pre-install common patterns
2. Add initialization script
3. Create template test suite
4. Document self-containment in README

## Success Criteria
```bash
# Template must pass this test
git clone template /tmp/test-aget
cd /tmp/test-aget
# Delete parent directories to ensure isolation
claude
> wake up; read docs
# Should complete in 2-3 tools, not 8-10
```

## Recommendation
**BLOCK Gate 2** until template is compliant with ARCH-001.

The template is the foundation - if it's broken, every project built on it will be broken.

## Tracking
- Created fix list: products/TEMPLATE-V2-CRITICAL-FIXES.md
- Architecture decision: docs/adr/ARCH-001-SELF-CONTAINED-PROJECTS.md
- Implementation example: my-AGET-aget (this repo)

---
*Discovered during architecture compliance review*
*Resolution required before v2.0 public release*