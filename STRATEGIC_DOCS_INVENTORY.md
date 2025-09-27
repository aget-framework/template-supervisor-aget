# Strategic Documents Inventory & Migration Plan
*Created: 2025-09-25 | Phase 1: Document Identification*

## Purpose
This inventory identifies which documents belong in AGET-AGET (strategic governance) vs aget-cli-agent-template (public framework), establishing clear boundaries for future agents to understand the separation of concerns.

## Document Classification

### 🧠 BELONGS IN AGET-AGET (Strategic/Vision/Governance)

#### Currently in aget-cli-agent-template (needs migration):
1. **`docs/AGET_AGET_CHARTER.md`**
   - Content: Defines AGET-AGET's role as strategic brain
   - Why move: This is about AGET-AGET itself, not the framework
   - Target: `governance/CHARTER.md`

2. **`docs/AGET_COGNITIVE_SPECTRUM.md`**
   - Content: Five modalities vision (standalone→meta-governance)
   - Why move: Strategic vision document
   - Target: `vision/COGNITIVE_SPECTRUM.md`

3. **`AGET_AGET_NEXT_ACTIONS.md`**
   - Content: Strategic roadmap and governance decisions
   - Why move: Strategic planning belongs in governance repo
   - Target: `governance/NEXT_ACTIONS.md`
   - Note: File itself says "To be moved to AGET-AGET repository"

#### May need partial migration:
4. **`AGET_USE_CASES_AND_SPECS_PLAN.md`**
   - Strategic planning parts → AGET-AGET
   - Implementation specs → Stay in template

5. **`AGET_IMPACT_REFLECTION.md`**
   - Vision/philosophy → AGET-AGET
   - Technical learnings → Stay in template

### ✅ STAYS IN TEMPLATE (Implementation/Usage/Public)

1. **`CHARTER.md`** (Template's charter)
   - Content: Public framework identity and contribution criteria
   - Why stays: Defines the public framework's purpose

2. **`README.md`**
   - Content: How to use the framework
   - Why stays: Public-facing usage documentation

3. **`NEXT_ACTIONS.md`** (Template's next actions)
   - Content: Implementation tasks for framework
   - Why stays: Technical implementation roadmap

4. **`AGENTS.md` / `AGENTS_AGET.md`**
   - Content: Conversational protocols
   - Why stays: Core framework functionality

5. **Pattern Documentation** (`docs/patterns/*.md`)
   - Content: How to use patterns
   - Why stays: Public pattern library

6. **Technical ADRs**
   - Content: Implementation decisions
   - Why stays: Public technical decisions

## Migration Rationale

### Why This Separation Matters

**For Future Agents:**
When an agent is spawned from aget-cli-agent-template, it needs to understand:
- The template provides the **implementation** (how to work)
- AGET-AGET provides the **vision** (why we work this way)
- Strategic questions go to AGET-AGET
- Technical questions stay in template

**For Governance:**
- AGET-AGET can evolve vision without breaking public framework
- Template remains stable for forks
- Clear authority boundaries

**For Contributors:**
- Know where to propose changes (vision vs implementation)
- Understand which repo to fork for their needs
- Clear contribution paths

## Context for Future Agents

When you (future agent) encounter strategic questions:
1. Check if AGET-AGET has guidance in `vision/` or `governance/`
2. Strategic decisions flow: AGET-AGET → Template → Your Instance
3. You can diverge from vision but should document why
4. Your experiments might graduate back to AGET-AGET

## Migration Execution Plan

### Phase 1: Identify (COMPLETE) ✅
- Documents catalogued above
- Clear separation criteria established

### Phase 2: Create Structure ✅ COMPLETE
Created:
- `governance/` - Strategic governance documents
- `vision/` - Future vision and frameworks
- `sessions/` - Learning and discoveries

### Phase 3: Copy Documents ✅ COMPLETE
```bash
# Copy with git history preserved
cp ../aget-cli-agent-template/docs/AGET_AGET_CHARTER.md governance/CHARTER.md
cp ../aget-cli-agent-template/docs/AGET_COGNITIVE_SPECTRUM.md vision/COGNITIVE_SPECTRUM.md
cp ../aget-cli-agent-template/AGET_AGET_NEXT_ACTIONS.md governance/NEXT_ACTIONS.md
```

### Phase 4: Add Context Headers
Each migrated document gets a header:
```markdown
---
repository: aget-aget
type: strategic-governance
migrated-from: aget-cli-agent-template
migration-date: 2025-09-25
---

# [Original Title]

> This strategic document now lives in AGET-AGET as part of the governance layer.
> Public implementation details remain in [aget-cli-agent-template](link).
```

### Phase 5: Update Cross-References
- Template README points to AGET-AGET for vision
- AGET-AGET README explains its governance role
- Both repos get STRATEGIC_SYNC.md

## Success Criteria
- [x] All strategic docs identified
- [x] Clear classification rationale
- [x] Migration path defined
- [x] Future agent context provided
- [x] No broken references (bidirectional pointers working)

## For the Current Session
This inventory provides crucial context that future agents will need to understand the AGET ecosystem's structure. It should be preserved and updated as the migration proceeds.

---
*This document establishes the strategic separation between AGET-AGET (governance) and aget-cli-agent-template (implementation).*