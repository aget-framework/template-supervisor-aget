# Saturday Release Plan: v2.0.0-beta.1 "Safety First"

**Target**: Saturday noon (2025-09-28 12:00)
**Theme**: Critical safety patterns that prevent data loss and security issues

## Release Gates (Must Pass to Ship)

### Gate 1: Data Safety ✅
**Intent**: Users never lose work due to silent failures

#### Tasks
- [ ] Integrate commit verification into session protocols
- [ ] Test verification with success case
- [ ] Test verification with failure case
- [ ] Ensure non-zero exit on failure
- [ ] Add commit SHA to success messages
- [ ] Document recovery instructions for failures

#### Acceptance Criteria
- Session protocols MUST exit non-zero when commits fail
- Error messages MUST include actionable recovery steps
- Success messages MUST show commit SHA as proof

---

### Gate 2: Error Visibility ✅
**Intent**: Critical errors are impossible to miss

#### Tasks
- [ ] Implement OutputLevel hierarchy (CRITICAL/ERROR/WARNING/SUCCESS/INFO/DEBUG)
- [ ] Create visual distinction for CRITICAL errors (🚨)
- [ ] Remove verbose success theater
- [ ] Batch related messages
- [ ] Test error visibility in real session

#### Acceptance Criteria
- CRITICAL errors must be visually unmissable
- Error-to-output ratio improved by 80%
- No success message without verification

---

### Gate 3: Security Standards ✅
**Intent**: Credentials are never exposed or committed

#### Tasks
- [ ] Create .aget/secrets/ template structure
- [ ] Add mandatory .gitignore for secrets
- [ ] Document secrets.yaml manifest format
- [ ] Create validation script for permissions
- [ ] Test with real credential scenarios

#### Acceptance Criteria
- .aget/secrets/ created with correct permissions (600)
- .gitignore prevents any secret commits
- Clear documentation for credential setup

---

### Gate 4: Safety Naming ✅
**Intent**: Agent names signal risk level at a glance

#### Tasks
- [ ] Document comprehensive naming convention
- [ ] Create validation function for names
- [ ] Add examples for each risk level
- [ ] Update agent creation to enforce convention
- [ ] Test name validation

#### Acceptance Criteria
- Naming convention documented with examples
- my- prefix for personal agents
- UPPERCASE for write operations
- Validation prevents unsafe names

---

### Gate 5: Template Integration ✅
**Intent**: Patterns work in actual aget-cli-agent-template

#### Tasks
- [ ] Port patterns to template repository
- [ ] Test migration with new patterns
- [ ] Verify backward compatibility
- [ ] Update template documentation
- [ ] Create migration guide for existing agents

#### Acceptance Criteria
- Clean integration into template
- Existing agents continue to work
- Migration path documented

---

## Timeline

### Friday Night (Now - Midnight)
**Focus**: Complete Gates 1-2 (Core Safety)
- [ ] Commit verification implementation
- [ ] Error hierarchy implementation
- [ ] Initial testing

### Saturday Morning (9 AM - 11:30 AM)
**Focus**: Complete Gates 3-5 (Integration)
- [ ] Security standards
- [ ] Naming convention
- [ ] Template integration
- [ ] Final testing

### Saturday Pre-Noon (11:30 AM - 12:00 PM)
**Focus**: Release
- [ ] Run all gate checks
- [ ] Create release notes
- [ ] Tag v2.0.0-beta.1
- [ ] Push to public repo
- [ ] Announce release

---

## Go/No-Go Decision Points

### 10:00 PM Tonight
- Gates 1-2 complete?
  - YES → Continue to Gate 3
  - NO → Reduce scope or delay

### 10:00 AM Saturday
- Gates 3-4 complete?
  - YES → Continue to Gate 5
  - NO → Ship with completed gates as beta.1, defer rest to beta.2

### 11:30 AM Saturday
- Gate 5 complete?
  - YES → Ship full beta.1
  - NO → Ship without template integration, manual instructions only

---

## Risk Mitigation

### If Running Late
1. **Minimum Viable Beta**: Gates 1-2 only (commit safety + error visibility)
2. **Document workarounds**: For any incomplete gates
3. **Set beta.2 date**: Commit to next weekend for remaining gates

### If Blocked
1. **Connection issues**: Work locally, defer push
2. **Test failures**: Document known issues in release notes
3. **Integration issues**: Ship patterns separately from template

---

## Success Metrics

### Immediate (Saturday)
- [ ] All 5 gates passed
- [ ] Zero known data loss scenarios
- [ ] Release published by noon

### Week 1 (Validation)
- [ ] No reports of silent failures
- [ ] Users notice improved error messages
- [ ] No security incidents

---

## Release Checklist

### Pre-Release (11:30 AM)
- [ ] All gates passed
- [ ] Tests green
- [ ] Documentation updated
- [ ] BREAKING_CHANGES.md complete
- [ ] Release notes drafted

### Release (12:00 PM)
- [ ] Version bumped to v2.0.0-beta.1
- [ ] Git tag created
- [ ] Pushed to GitHub
- [ ] Release notes published
- [ ] Announcement drafted

### Post-Release (12:30 PM)
- [ ] Monitor for immediate issues
- [ ] Document lessons learned
- [ ] Plan beta.2 scope

---

## The Commitment

**We will ship v2.0.0-beta.1 by Saturday noon with AT LEAST Gates 1-2 (critical safety), preferably all 5 gates.**

*Data safety cannot wait. Better to ship partial safety improvements than nothing.*

---

*Plan created: 2025-09-27 (Friday night)*
*Target: 2025-09-28 12:00 (Saturday noon)*