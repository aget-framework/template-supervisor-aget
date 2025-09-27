# Discovery Tracker

## Purpose
Track all discoveries, lessons, and insights from real AGET usage to inform framework improvements.

## Active Discoveries

### Week of 2025-09-25

#### Repository Planning Gap
- **When**: DeepResearch-aget creation
- **What**: No prompt for where agent will live
- **Impact**: Agent orphaned locally until manual fix
- **Status**: Captured in FRAMEWORK_REQUIREMENTS.md
- **Next**: Add to aget-cli-agent-template

#### Governance Pointer Success
- **When**: Fresh agent in aget-template
- **What**: Agent correctly found governance via pointer
- **Impact**: Validates separation strategy
- **Status**: Working as designed
- **Next**: Document pattern for reuse

#### Prerequisites Assumptions
- **When**: Multiple sessions
- **What**: We assume Git/GitHub CLI without stating
- **Impact**: User confusion if missing
- **Status**: Documented in USER_PREREQUISITES.md
- **Next**: Add prerequisite checker

#### Repository Visibility Default 🔴
- **When**: OpenAI_DeepResearch-aget creation
- **What**: Created as public when should be private
- **Impact**: Exposed research project structure
- **Silver Lining**: Became valuable educational resource
- **Lesson**: Consider visibility carefully, default to private for org projects
- **Status**: Documented, keeping public as case study
- **Next**: Add visibility decision to AGET creation flow

#### Premature Action-Taking Lesson 🔴
- **When**: Reviewing OpenAI_DeepResearch-aget name
- **What**: Agent immediately started making changes without asking
- **Impact**: Would have "fixed" something that wasn't broken
- **Behavior**: Jumped straight to editing files instead of asking for clarification
- **Lesson**: Base repo name (OpenAI_DeepResearch) is given, we append -aget
- **Meta-Lesson**: ASK FIRST before making changes based on assumptions
- **Status**: Self-corrected after user intervention
- **Next**: Add "pause and verify" pattern before acting on assumptions

## Discovery Categories

### 🔴 Critical Gaps
Things that break the experience:
1. Repository planning (FIXED)
2. Repository visibility defaults (DISCOVERED)

### 🟡 Friction Points
Things that slow users down:
1. Missing GitHub CLI (DOCUMENTED)
2. Unclear prerequisites (DOCUMENTED)

### 🟢 Validated Patterns
Things that work well:
1. Governance pointers
2. Evolution tracking
3. Session management

### 🔵 Enhancement Ideas
Things to explore:
1. `aget doctor` command
2. Interactive repository setup
3. Automated prerequisite checking

## How to Use This Tracker

When you discover something:
1. Add it here immediately with date/context
2. Categorize by severity
3. Link to detailed documentation
4. Track resolution status

## Resolution Flow

```
Discovery → Tracker → Requirements → Template → Validation
    ↑                                              ↓
    └──────────────── Feedback ←──────────────────┘
```

## Quick Links

- [Framework Requirements](FRAMEWORK_REQUIREMENTS.md) - Requirements ready for implementation
- [User Prerequisites](USER_PREREQUISITES.md) - What users need
- [Sessions](../sessions/) - Detailed discovery documentation

---
*Living document - Update whenever discoveries happen*