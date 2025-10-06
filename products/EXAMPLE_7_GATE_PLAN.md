# Example 7-Gate Plan: Fleet Version Migration

**Context**: Complex, multi-agent coordination task
**Task**: Migrate 5 worker agents from v2.4.0 to v2.5.0 with validation framework
**Complexity**: High (40+ files across 5 repos, partially reversible, multi-agent impact)

---

## Gate Sizing Calculation (L104)

Using gate sizing heuristic from AGENTS.md:

- **Reversibility**: Partially reversible (manual recovery needed) = +1
- **Impact Scope**: Multi-agent (5 agents affected) = +2
- **Complexity**: High (40+ files, 5 repositories) = +2
- **Total**: 2-3 baseline + 5 = **7-8 gates** ✅

---

## Gate 0: Discovery & Readiness Assessment (45 min)

### Intent
Understand current fleet state and identify migration blockers before committing to execution.

### Objective
Complete audit of 5 agents and create migration readiness matrix.

### Actions

1. **Audit Current State**:
   ```bash
   for agent in agent1 agent2 agent3 agent4 agent5; do
     cd ~/github/$agent
     echo "=== $agent ==="
     jq -r '.aget_version' .aget/version.json
     git status --short | wc -l  # uncommitted changes?
     pytest tests/ -q 2>&1 | tail -3  # current test status
   done
   ```

2. **Identify Blockers**:
   - Agents with uncommitted changes
   - Agents with failing tests
   - Agents with outdated dependencies
   - Agents missing contract test structure

3. **Create Migration Matrix**:
   | Agent | Current Version | Test Status | Blockers | Ready? |
   |-------|----------------|-------------|----------|--------|
   | agent1 | 2.4.0 | ✅ Pass | None | ✅ |
   | agent2 | 2.4.0 | ❌ 2 failing | Fix tests first | ❌ |
   | agent3 | 2.4.0 | ✅ Pass | Uncommitted changes | ⚠️ |
   | agent4 | 2.3.0 | ✅ Pass | Need 2.3→2.4 first | ❌ |
   | agent5 | 2.4.0 | ✅ Pass | None | ✅ |

4. **Estimate Work**:
   - Ready agents (agent1, agent5): 2 × 25 min = 50 min
   - Needs prep (agent2, agent3, agent4): Address blockers first
   - Decision: Migrate ready agents first, or fix all blockers?

### Success Criteria
- [ ] All 5 agents audited
- [ ] Current versions documented
- [ ] Test status captured
- [ ] Blockers identified
- [ ] Migration matrix created
- [ ] Readiness decision made

### DECISION POINT
**Should we proceed with full fleet migration, or staged approach?**

- **GO (Full Fleet)**: All blockers resolved → Migrate all 5 together
- **GO (Staged)**: Some blockers remain → Migrate ready agents first (agent1, agent5)
- **NOGO**: Critical blockers → Fix blockers before starting migration

---

## Gate 1: Prepare Migration Artifacts (30 min)

### Intent
Create reusable migration artifacts to ensure consistency across all agents.

### Objective
Build migration toolkit that can be applied to each agent systematically.

### Actions

1. **Copy Contract Tests from Template**:
   ```bash
   # Create staging directory
   mkdir -p ~/migration-kit/v2.5.0/
   cd ~/github/template-worker-aget
   cp tests/test_wake_contract.py ~/migration-kit/v2.5.0/
   cp tests/test_identity_contract.py ~/migration-kit/v2.5.0/
   cp tests/README.md ~/migration-kit/v2.5.0/
   ```

2. **Create Version Update Script**:
   ```bash
   # Script to update version.json consistently
   cat > ~/migration-kit/v2.5.0/update_version.sh <<'EOF'
   #!/bin/bash
   # Usage: ./update_version.sh <agent-name>
   AGENT_NAME=$1
   jq '.aget_version = "2.5.0" | .migrated_to_v25 = "2025-10-06" | .validation_framework_enabled = true' \
     .aget/version.json > tmp.json
   mv tmp.json .aget/version.json
   echo "✅ Updated $AGENT_NAME to v2.5.0"
   EOF
   chmod +x ~/migration-kit/v2.5.0/update_version.sh
   ```

3. **Create Validation Checklist**:
   ```markdown
   # Agent Migration Checklist
   - [ ] Contract tests copied to tests/
   - [ ] version.json updated to v2.5.0
   - [ ] Identity fields added (agent_name, instance_type, domain)
   - [ ] Contract tests pass (7/7)
   - [ ] Existing tests still pass
   - [ ] Committed and pushed
   - [ ] Verified on GitHub
   ```

4. **Document Migration Steps**:
   - Write step-by-step guide for each agent
   - Include rollback procedures
   - Note common issues and fixes

### Success Criteria
- [ ] Contract tests copied to migration kit
- [ ] Version update script created and tested
- [ ] Validation checklist created
- [ ] Migration guide documented
- [ ] All artifacts in ~/migration-kit/v2.5.0/

### DECISION POINT
**Are migration artifacts complete and tested?**

- **GO**: Artifacts ready → Proceed to canary migration
- **NOGO**: Missing pieces → Complete toolkit first

---

## Gate 2: Canary Migration (First Agent) (25 min)

### Intent
Prove migration process on single agent before applying to fleet.

### Objective
Successfully migrate agent1 (or other ready agent) to v2.5.0, validate all tests pass.

### Actions

1. **Execute Migration** (agent1):
   ```bash
   cd ~/github/agent1

   # Backup current state
   git stash  # if any uncommitted changes

   # Copy contract tests
   cp ~/migration-kit/v2.5.0/test_*.py tests/
   cp ~/migration-kit/v2.5.0/README.md tests/

   # Update version
   ~/migration-kit/v2.5.0/update_version.sh agent1

   # Add identity fields
   jq '.agent_name = "agent1" | .instance_type = "aget" | .domain = "data-analysis"' \
     .aget/version.json > tmp.json
   mv tmp.json .aget/version.json
   ```

2. **Run Contract Tests**:
   ```bash
   pytest tests/test_wake_contract.py tests/test_identity_contract.py -v
   # Expected: 7/7 passing
   ```

3. **Run Existing Tests**:
   ```bash
   pytest tests/ -v
   # Expected: All existing tests still pass
   ```

4. **Commit**:
   ```bash
   git add tests/ .aget/version.json
   git commit -m "release: Migrate to v2.5.0 (validation framework)

   - Added contract tests (wake + identity)
   - Updated version.json to v2.5.0
   - Added identity fields

   Validation: 7/7 contract tests passing
   "
   git push
   ```

5. **Verify Deployment**:
   ```bash
   gh api repos/your-org/agent1/contents/.aget/version.json | \
     jq -r '.content' | base64 -d | jq -r '.aget_version'
   # Expected: 2.5.0
   ```

### Success Criteria
- [ ] agent1 migrated successfully
- [ ] Contract tests pass (7/7)
- [ ] Existing tests pass
- [ ] Committed and pushed
- [ ] Verified on GitHub
- [ ] No regressions observed

### DECISION POINT
**Was canary migration successful? Any issues discovered?**

- **GO**: Clean migration, all tests pass → Apply to fleet
- **NOGO**: Issues found → Fix migration process before fleet rollout

---

## Gate 3: Fleet Migration (Remaining 4 Agents) (100 min)

### Intent
Apply proven migration process to remaining ready agents.

### Objective
Migrate agent2, agent3, agent4, agent5 using validated process from Gate 2.

### Actions

**For each agent** (parallelizable if desired):

1. **Pre-flight Check**:
   - Verify agent is in ready state (from Gate 0 matrix)
   - Resolve any blockers identified earlier
   - Confirm tests passing on current version

2. **Execute Migration** (repeat Gate 2 steps):
   - Copy contract tests
   - Update version.json
   - Add identity fields
   - Run contract tests (expect 7/7)
   - Run existing tests (expect all pass)
   - Commit and push
   - Verify on GitHub

3. **Track Progress**:
   | Agent | Status | Contract Tests | Existing Tests | Deployed |
   |-------|--------|----------------|----------------|----------|
   | agent1 | ✅ Done (Gate 2) | 7/7 | ✅ | ✅ |
   | agent2 | 🔄 In Progress | - | - | - |
   | agent3 | ⏭️ Pending | - | - | - |
   | agent4 | ⏭️ Pending | - | - | - |
   | agent5 | ⏭️ Pending | - | - | - |

4. **Handle Issues**:
   - If any agent fails: Document issue, continue with others
   - Mark problematic agents for follow-up
   - Don't block entire fleet on single agent

### Success Criteria
- [ ] agent2 migrated ✅
- [ ] agent3 migrated ✅
- [ ] agent4 migrated ✅
- [ ] agent5 migrated ✅
- [ ] All contract tests passing (7/7 per agent)
- [ ] All existing tests passing
- [ ] All committed and pushed
- [ ] All verified on GitHub

### DECISION POINT
**Are all agents successfully migrated?**

- **GO (Complete)**: All 5 agents at v2.5.0 → Proceed to validation
- **GO (Partial)**: 4/5 or 3/5 migrated → Proceed with note of incomplete agents
- **NOGO**: <3 agents migrated → Investigate systemic issues

---

## Gate 4: Fleet-Wide Validation (30 min)

### Intent
Verify migration consistency across entire fleet.

### Objective
Confirm all agents report v2.5.0 and pass validation checks.

### Actions

1. **Version Check Across Fleet**:
   ```bash
   for agent in agent1 agent2 agent3 agent4 agent5; do
     echo "=== $agent ==="
     gh api repos/your-org/$agent/contents/.aget/version.json | \
       jq -r '.content' | base64 -d | jq -r '.aget_version'
   done
   # Expected: All show 2.5.0
   ```

2. **Contract Test Summary**:
   ```bash
   for agent in agent1 agent2 agent3 agent4 agent5; do
     cd ~/github/$agent
     echo "=== $agent ==="
     pytest tests/test_wake_contract.py tests/test_identity_contract.py -q
   done
   # Expected: All show 7 passed
   ```

3. **Registry Update**:
   ```yaml
   # Update .aget/registry/agents.yaml in supervisor
   agents:
     - name: agent1
       version: "2.5.0"  # Updated
       validation_framework_enabled: true  # Added
     - name: agent2
       version: "2.5.0"  # Updated
       validation_framework_enabled: true  # Added
     # ... etc

   fleet_stats:
     total_agents: 5
     version_distribution:
       "2.5.0": 5  # All migrated
       "2.4.0": 0  # None remaining
     last_updated: "2025-10-06"
   ```

4. **Create Migration Report**:
   ```markdown
   # Fleet Migration Report: v2.4.0 → v2.5.0

   **Date**: 2025-10-06
   **Scope**: 5 agents

   ## Results
   - ✅ agent1: Migrated, 7/7 tests passing
   - ✅ agent2: Migrated, 7/7 tests passing
   - ✅ agent3: Migrated, 7/7 tests passing
   - ✅ agent4: Migrated, 7/7 tests passing
   - ✅ agent5: Migrated, 7/7 tests passing

   ## Statistics
   - Time: 257 minutes (4.3 hours)
   - Success Rate: 100% (5/5)
   - Issues: 0 blocking, 2 minor (resolved)

   ## Lessons Learned
   - Canary approach validated migration process
   - Migration toolkit saved 50+ minutes
   - Contract tests caught 1 identity mismatch early
   ```

### Success Criteria
- [ ] All agents verified at v2.5.0
- [ ] Contract tests passing fleet-wide
- [ ] Registry updated with new versions
- [ ] Migration report created
- [ ] No version drift detected

### DECISION POINT
**Is fleet migration validated and complete?**

- **GO**: All validation checks pass → Proceed to documentation
- **NOGO**: Issues found → Investigate and resolve

---

## Gate 5: Update Documentation (20 min)

### Intent
Document migration completion and update fleet status.

### Objective
Update all documentation to reflect v2.5.0 fleet state.

### Actions

1. **Update Fleet Documentation**:
   - README.md: Update fleet version stats
   - CHANGELOG.md: Add v2.5.0 migration entry
   - docs/FLEET_STATUS.md: Mark migration complete

2. **Create Announcement**:
   ```markdown
   # Fleet Migration Complete: v2.5.0

   All 5 agents successfully migrated to v2.5.0 "Validation" release.

   **New Capabilities**:
   - Contract test framework (7 tests per agent)
   - Identity protocol validation
   - Version consistency checks

   **Agents Updated**:
   - agent1, agent2, agent3, agent4, agent5

   **Next Steps**:
   - Monitor for issues (1 week)
   - Plan v2.6 enhancements
   ```

3. **Update Runbooks**:
   - Add v2.5.0 troubleshooting section
   - Document contract test usage
   - Update migration guide for future versions

### Success Criteria
- [ ] Fleet documentation updated
- [ ] Migration announcement created
- [ ] Runbooks updated
- [ ] Status dashboards reflect v2.5.0

### DECISION POINT
**Is documentation updated and accurate?**

- **GO**: Docs reflect current state → Proceed to commit
- **NOGO**: Gaps remain → Complete documentation first

---

## Gate 6: Commit & Deploy Documentation (15 min)

### Intent
Commit all migration artifacts and documentation.

### Objective
Create permanent record of migration in supervisor repository.

### Actions

1. **Stage All Changes**:
   ```bash
   cd ~/github/supervisor-agent
   git add .aget/registry/agents.yaml
   git add docs/FLEET_STATUS.md
   git add CHANGELOG.md
   git add reports/MIGRATION_v2.5.0_REPORT.md
   ```

2. **Commit with Comprehensive Message**:
   ```bash
   git commit -m "release: Complete v2.5.0 fleet migration

   Migrated 5 agents from v2.4.0 to v2.5.0 (validation framework)

   Agents updated:
   - agent1: ✅ 7/7 contract tests passing
   - agent2: ✅ 7/7 contract tests passing
   - agent3: ✅ 7/7 contract tests passing
   - agent4: ✅ 7/7 contract tests passing
   - agent5: ✅ 7/7 contract tests passing

   Statistics:
   - Duration: 4.3 hours
   - Success rate: 100% (5/5)
   - Contract tests: 35/35 passing (7 per agent)

   Updated:
   - Fleet registry (.aget/registry/agents.yaml)
   - Fleet status docs
   - Changelog
   - Migration report

   All agents validated on GitHub with API checks.
   "
   ```

3. **Push**:
   ```bash
   git push origin main
   ```

4. **Tag Release**:
   ```bash
   git tag -a v2.5.0-fleet-migration -m "Completed v2.5.0 migration for 5-agent fleet"
   git push --tags
   ```

### Success Criteria
- [ ] All changes committed
- [ ] Pushed to GitHub
- [ ] Tag created
- [ ] Supervisor repository up to date

### DECISION POINT
**Are all artifacts committed and deployed?**

- **GO**: Repository updated → Proceed to post-migration monitoring
- **NOGO**: Issues with commit/push → Fix before proceeding

---

## Gate 7: Post-Migration Monitoring (30 min + ongoing)

### Intent
Ensure migration stability and catch any issues early.

### Objective
Monitor fleet for 1 week post-migration, address any issues promptly.

### Actions

1. **Immediate Health Check** (Day 0 - today):
   ```bash
   # Run contract tests across fleet
   for agent in agent1 agent2 agent3 agent4 agent5; do
     cd ~/github/$agent
     pytest tests/test_wake_contract.py tests/test_identity_contract.py -v
   done
   # Expected: All 7/7 passing
   ```

2. **Day 1 Check** (tomorrow):
   - Verify agents still operational
   - Check for any user-reported issues
   - Review contract test status

3. **Day 3 Check**:
   - Spot-check 2-3 agents (contract tests)
   - Review any issue tracker for migration-related bugs
   - Confirm no version drift

4. **Week 1 Review** (Day 7):
   - Full fleet health check (all 5 agents)
   - Assess migration success
   - Document any issues and resolutions
   - Declare migration complete or identify follow-up work

5. **Issue Response Plan**:
   - **Critical**: Immediate response, consider rollback
   - **High**: Fix within 24 hours
   - **Medium**: Fix within week
   - **Low**: Add to backlog

### Success Criteria
- [ ] Day 0 health check: All pass
- [ ] Day 1 check: No issues reported
- [ ] Day 3 check: Spot checks pass
- [ ] Week 1 review: Fleet stable
- [ ] Issues tracked and addressed
- [ ] Migration declared complete

### DECISION POINT
**Is migration stable after 1 week of monitoring?**

- **GO**: No issues, fleet stable → Migration complete ✅
- **NOGO**: Issues found → Address and extend monitoring

---

## Summary

| Gate | Objective | Time | Agents | Risk |
|------|-----------|------|--------|------|
| 0 | Discovery & Assessment | 45 min | 5 | Low |
| 1 | Prepare Artifacts | 30 min | - | Low |
| 2 | Canary Migration | 25 min | 1 | Medium |
| 3 | Fleet Migration | 100 min | 4 | Medium |
| 4 | Fleet Validation | 30 min | 5 | Low |
| 5 | Update Documentation | 20 min | - | Low |
| 6 | Commit & Deploy | 15 min | - | Low |
| 7 | Post-Migration Monitoring | 30 min + 7 days | 5 | Medium |
| **Total** | **Complete Fleet Migration** | **~5 hours + monitoring** | **5 agents** | **Medium** |

---

## Why 7 Gates?

**This is right-sized for:**
- Multi-agent coordination (5 agents affected)
- Partially reversible (manual recovery possible but costly)
- High complexity (40+ files across 5 repositories)
- External impact (agents used by systems/users)
- Version consistency critical (contract testing required)

**Gate breakdown rationale**:
- **Gates 0-1**: Planning and preparation (prevent rushing)
- **Gate 2**: Canary validation (prove process before fleet)
- **Gate 3**: Fleet execution (bulk of work, parallelizable)
- **Gates 4-5**: Validation and documentation (ensure quality)
- **Gates 6-7**: Deployment and monitoring (ensure stability)

**What makes this different from 3-gate plan:**
- Canary gate (Gate 2) - Not needed for single-agent work
- Fleet validation gate (Gate 4) - Unique to multi-agent coordination
- Post-migration monitoring (Gate 7) - Risk mitigation for external impact

---

**Pattern**: Complex, multi-agent, partially reversible tasks → 7-8 gates
**Application**: Use this structure for fleet migrations, breaking changes, multi-system refactoring
