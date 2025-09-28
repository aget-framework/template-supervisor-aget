# Pattern Integration Guide

## Overview
This guide documents how to integrate battle-tested patterns from the AGET hub into new agents.

## Integration Process

### 1. Source Patterns
Patterns come from `my-AGET-aget` (the v2.0 hub) which maintains production-ready patterns.

### 2. Pattern Categories

#### Essential (Priority 1)
Must have for v2.0 compliance:
- Session management (wake_up, wind_down)
- GitHub basics (create, list, update issues)
- Agent discovery (routing)

#### Enhanced (Priority 2)
Recommended for full functionality:
- Quality checks (release validation)
- Compliance validation (v2 checker)
- Documentation tools (smart reader)

#### Specialized (Priority 3)
Agent-specific patterns:
- Governance patterns
- Naming conventions
- Safety protocols

### 3. Integration Steps

```bash
# 1. Copy patterns from hub
cp -r ../my-AGET-aget/.aget/patterns/github .aget/patterns/
cp -r ../my-AGET-aget/.aget/patterns/quality .aget/patterns/
cp -r ../my-AGET-aget/.aget/patterns/validation .aget/patterns/

# 2. Update routing pattern
cp ../my-AGET-aget/.aget/patterns/routing/agent_discovery.py \
   .aget/patterns/routing/

# 3. Test patterns
python3 .aget/patterns/validation/v2_compliance_check.py
python3 .aget/patterns/session/wake_up.py
python3 .aget/patterns/github/list_issues.py --help

# 4. Verify self-containment
grep -r "from \.\." .aget/patterns/
```

### 4. Testing Checklist

- [ ] Compliance check passes (>90%)
- [ ] Session patterns execute
- [ ] GitHub patterns have CLI help
- [ ] Agent discovery finds agents
- [ ] No external dependencies

### 5. Common Issues

#### Pattern Not Found
- Check source has latest patterns
- Verify path corrections

#### Import Errors
- Ensure self-containment
- Check Python path

#### GitHub CLI Missing
- Install: `brew install gh`
- Authenticate: `gh auth login`

## Pattern Development

When creating new patterns:

1. **Start in hub**: Develop in my-AGET-aget first
2. **Test thoroughly**: Ensure production ready
3. **Document well**: Include help and examples
4. **Share back**: Copy to template once stable

## Maintenance

### Updating Patterns
```bash
# Pull latest from hub
cp -f ../my-AGET-aget/.aget/patterns/github/*.py \
     .aget/patterns/github/

# Test changes
python3 .aget/patterns/validation/v2_compliance_check.py
```

### Version Tracking
Keep patterns synchronized:
- Hub (my-AGET-aget): Development version
- Template (my-AGET-template): Stable reference
- Agents: Copy from template

---
*Pattern integration is key to v2.0 success. Use hub patterns for consistency.*