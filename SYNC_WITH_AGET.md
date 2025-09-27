# Relationship Between aget-aget and AGET

This file clarifies what aget-aget commits to vs experiments with.

## Fundamental Standards (Committed To)

aget-aget accepts these as foundational - they define what AGET is:

### Core Identity
- **MISSION.md** - "Help software creators achieve their vision (with their linguistic AI collaborator)"
- **Core patterns** - wake, wind-down, sign-off (the heartbeat of AGET)
- **Philosophy** - Private exploration → selective public value

### Quality Baseline
- **Pattern structure** - Must have apply_pattern() function
- **Evolution tracking** - Decision/Discovery/Extraction format
- **Test coverage goals** - >80% for critical paths

These fundamentals are shared because aget-aget IS part of AGET.

## Experimental Standards (Free to Diverge)

aget-aget can experiment with anything, including:

### Documentation
- **DOCUMENTATION_STANDARDS.md** - Can try new formats here first
- Alternative naming conventions
- Different organizational structures

### Workflows
- New patterns beyond core three
- Alternative command structures
- Different tool integrations

### Quality Tools
- `experiment_001_pattern_validator.py` - Experimental until proven
- New testing approaches
- Alternative validation methods

## Graduation Process

When experiments prove valuable:
1. Test thoroughly in aget-aget (private)
2. Document learnings in evolution
3. Graduate to AGET (public)
4. Mark as fundamental if core to AGET identity

## Sync Process

When AGET updates a synchronized file:
1. Copy the update to aget-aget
2. Run any local tests
3. Commit with message: "sync: Update [file] from AGET"

When aget-aget improves a shared standard:
1. Test in aget-aget first
2. Graduate to AGET when proven
3. Mark as synchronized

## Current Sync Status

# Sync Status Report

## ❌ Fundamental Standards Issues
- Missing fundamental: patterns/session/wake.py - Core pattern - wake protocol
- Missing fundamental: patterns/session/wind_down.py - Core pattern - wind down protocol
- Missing fundamental: patterns/session/sign_off.py - Core pattern - sign off protocol

## ❌ Mission Alignment Issues
- Mission statement doesn't contain AGET's core mission

## ✅ Innovation Active
