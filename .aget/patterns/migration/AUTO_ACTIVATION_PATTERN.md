# Auto-Activation Pattern for AGET Migrations

## Problem
Current AGET migrations create all components but leave them inactive, requiring manual steps to "turn on" the agent. This leads to confusion where migration is "complete" but the agent doesn't work as expected.

## Evidence
- **Case Study**: RKB_infrastructure → RKB_infra-aget (2025-09-26)
  - Created InfraGuard identity in AGENTS_ENHANCED.md
  - User had to manually copy to AGENTS.md
  - First wake-up showed generic response, not InfraGuard personality
  - Value delivery delayed until manual activation

## Solution Pattern

### 1. Migration Must Auto-Activate
```bash
# At end of migration, automatically:
cp AGENTS.md AGENTS_ORIGINAL.md
cp AGENTS_ENHANCED.md AGENTS.md
echo "✅ Agent identity activated!"
```

### 2. Include Verification Step
```bash
#!/bin/bash
# verify_migration.sh
echo "🔍 Verifying AGET migration..."
[[ -f .aget/version.json ]] && echo "✅ Version present"
[[ -f .aget/capabilities.json ]] && echo "✅ Capabilities defined"
[[ -d .aget/evolution ]] && echo "✅ Evolution tracking ready"
grep -q "$AGENT_NAME" AGENTS.md && echo "✅ Identity active"
```

### 3. Seed with Initial Data
```json
// .aget/evolution/seed/migration_baseline.json
{
  "timestamp": "migration_date",
  "baseline_state": "...",
  "initial_discoveries": ["..."],
  "known_issues": ["..."]
}
```

### 4. Create Identity Config
```json
// .aget/identity.json
{
  "name": "InfraGuard",
  "greeting": "InfraGuard on duty. Infrastructure secure.",
  "personality": ["vigilant", "analytical", "protective"],
  "catchphrases": {
    "wake": "🛡️ InfraGuard activating...",
    "success": "Infrastructure protected.",
    "warning": "Anomaly detected: "
  }
}
```

### 5. Add Personality Commands
```makefile
# Makefile additions
.PHONY: $(AGENT_NAME) wake-$(AGENT_NAME)

$(AGENT_NAME):
	@cat .aget/identity.json | jq -r '.greeting'
	@make status
```

## Implementation Checklist

### During Migration
- [ ] Create AGENTS_ENHANCED.md with full personality
- [ ] Generate .aget/identity.json
- [ ] Seed evolution directories with baseline data
- [ ] Add agent-specific Makefile targets

### At Migration End (Automatic)
- [ ] Backup original AGENTS.md
- [ ] Activate new identity
- [ ] Run verification script
- [ ] Display first-use commands
- [ ] Show success with agent greeting

### First User Experience
```bash
user: wake up
agent: 🛡️ InfraGuard on duty. Infrastructure secure.
       [Infrastructure status with personality]
```

NOT:
```bash
user: wake up
agent: ## Status Report [generic response]
```

## Success Metrics
1. Zero manual steps after migration script completes
2. First wake shows agent personality immediately
3. All AGET commands work without configuration
4. Evolution tracking starts from first session

## Anti-Patterns to Avoid
- ❌ Creating AGENTS_ENHANCED.md without activating it
- ❌ Empty evolution directories
- ❌ Missing identity configuration
- ❌ Generic wake-up responses
- ❌ Manual activation instructions in docs

## Template Updates Needed

### aget-cli-agent-template Should Include:
1. `scripts/activate_identity.sh`
2. `scripts/verify_migration.sh`
3. `.aget/identity.json.template`
4. Migration step: "Activation & Verification"
5. Auto-activation in migration script

## Lesson
**"A migration isn't complete until the agent wakes up with its personality active."**

The goal is zero friction: migrate → wake → personality visible → value delivered.

---
*Pattern extracted from: RKB_infra-aget migration experience*
*Date: 2025-09-26*
*Impact: High - affects all future AGET creations*