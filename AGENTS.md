# Agent Configuration

@aget-version: 3.15.0

## Agent Compatibility
This configuration follows the AGENTS.md open-source standard for universal agent configuration.
Works with Claude Code, Codex CLI, Gemini CLI, and other CLI coding agents.
**Note**: CLAUDE.md is a symlink to this file for backward compatibility.

## Framework Positioning

**AGET is a "Configuration & Lifecycle Management System for CLI-Based Human-AI Collaborative Coding"**

AGET occupies a unique niche in the agent framework landscape:
- **Not** an autonomous agent runtime (LangChain, MetaGPT, AutoGPT)
- **Not** a production ALM platform (AgentOps, Salesforce ALM)
- **Instead**: Human-supervised fleet management with organizational memory and version progression

**Differentiators**:
- Universal CLI compatibility (works across Claude Code, Codex CLI, Gemini CLI)
- Contract testing and version compliance (v2.5.0+)
- Shared learning repository (.aget/evolution/)
- Lightweight, zero-infrastructure (markdown + git)
- Human-centric governance (gated releases, evidence-based planning)

## Project Context
template-supervisor-aget - Supervisor AGET template - v3.13.0

**Note**: Update this section when instantiating template:
- Change project name to your supervisor agent name
- Update version to reflect your agent's version
- Add specific context about your fleet/portfolios

## Architecture Context

### Supervisor Role

This template creates supervisor AGETs that:
1. **Direct Management**: Supervise multiple worker agents across portfolios
   - Assign work, review outputs, enforce standards
   - Authority to escalate issues and modify agent configuration
   - Track fleet versions and coordinate upgrades

2. **Coordination**: Framework R&D and cross-cutting orchestration
   - Pattern deployment across fleet
   - Multi-agent migration coordination
   - Shared knowledge base maintenance (.aget/evolution/)
   - Specification and standards development

### Recursive Supervision Model (L99)

**Core principle**: Every agent is a worker. Supervision is a capability, not a type.

Even supervisors are supervised:
```
Human (supervises) → Supervisor AGET (supervises) → Worker agents
```

This enables:
- Multi-level hierarchies (supervisors of supervisors)
- Clear accountability chains (every agent knows its supervisor)
- Fractal growth patterns (same structure at every level)
- Dynamic reorganization (promote worker → supervisor via config)

### Supervision Patterns (L099)

**Practical patterns for effective multi-agent supervision:**

1. **Process Enforcement**: Catch violations early, enforce gate discipline
   - Critique format: Quantitative rating (X/10) + specific violations + actionable path forward
   - Example: "Process 2/10: No gate plan (violation), 914 lines without preview (violation)"

2. **Incremental Oversight**: Match review cadence to delivery cadence
   - Review at version completions, not just final output
   - Provide go/no-go decisions at natural checkpoints

3. **Intervention Timing**: Know when to stop vs when to let proceed
   - Intervene: Process violations, scope creep, disproportionate time investment
   - Don't intervene: Agent following approved gates, reasonable estimates

4. **Teaching Through Critique**: Quality feedback drives behavior change
   - Specific violations with evidence
   - Explain why it matters (impact, not just rules)
   - Acknowledge improvement (2/10 → 9/10)

5. **Scope Management**: Help design experiments, estimate effort, recommend timing
   - Not just approve/reject, but shape proposals into actionable plans

6. **Meta-Oversight**: Supervise the supervision
   - "Did I intervene at the right times?"
   - "Was my critique actionable?"
   - "Did the agent improve?"

**Naming Convention**:
- `-AGET` suffix = Action-taking agent (can modify systems)
- `-aget` suffix = Information-only agent (read-only)
- All detection logic supports both cases

## Decision Authority (L330, L342)

| Decision Type | Supervisor Authority | Escalate To |
|----

### Governance Capabilities

| Attribute | Value |
|-----------|-------|
| Governance Intensity | Rigorous |
-----------|---------------------|-------------|
| L-docs, specs, documentation | Autonomous | — |
| Agent configuration changes | Autonomous | — |
| Fleet-wide pattern deployment | Propose + validate | Human principal |
| Breaking changes | Escalate | Human principal |
| Visibility / access changes | Escalate | Human principal |

**Key Principle**: Supervisor provides governance oversight for fleet. Human principal approves major decisions.

**Note**: Customize this table for your fleet's governance model — adjust authority levels based on trust and operational maturity.

### Inherited Knowledge (L330)

Supervisor agents inherit institutional knowledge. Key foundations:

| Document | Key Insight |
|----------|-------------|
| L143 | AGET = "Configuration & Lifecycle Management for CLI-Based Human-AI Collaborative Coding" |
| L99 | "Every agent is a worker. Supervision is a capability, not a type." |
| ADR-001 | AGET = conversation layer only |
| ADR-005 | Gates = release points |
| ADR-008 | Advisory → Strict → Generator quality progression |

**Note**: Populate with your fleet's critical decisions and learnings as they accumulate.
See: `governance/MEMORY_VISION.md`

---

## Skill Routing

| Task | Skill | When to Use |
|------|-------|-------------|
| Start session | /aget-wake-up | Beginning of every session |
| End session | /aget-wind-down | End of every session |
| Research topic | /aget-study-topic | Before proposing changes |
| Record learning | /aget-record-lesson | After discovering reusable insight |
| Create project | /aget-create-project | Starting multi-gate work |
| Review project | /aget-review-project | Mid-flight assessment |
| File issue | /aget-file-issue | Reporting bugs or gaps |
| Enhance spec | /aget-enhance-spec | Improving specification maturity |
| Check health | /aget-check-health | Verifying agent structure |
| Check fleet | /aget-check-fleet | Fleet-wide health and version audit |
| Review agent | /aget-review-agent | Assessing subordinate agent quality |


## Governed Project Creation (STRUCTURAL — D71 Layer 1)

**MUST invoke** `/aget-create-project` when creating any `planning/PROJECT_PLAN_*.md` file. Direct creation via Write or Edit is **PROHIBITED** — the skill enforces spec conformance (CAP-PP-001 through CAP-PP-007), gate ordering (L617), and self-verification (Step 7.5 + Step 8) that manual creation bypasses.

**Enforcement**: Strict (ADR-008). If a PROJECT_PLAN exists without skill invocation evidence, flag as governance bypass in retrospective.

## Structural Skill Routing (D71)

Skills with STRUCTURAL enforcement level. When the trigger condition is met, the skill MUST be invoked.

| Skill | Trigger Condition | Prohibited Alternative | ADR-008 Level |
|-------|-------------------|----------------------|:-------------:|
| `/aget-create-project` | Creating `planning/PROJECT_PLAN_*.md` | Direct Write/Edit to planning/ | **Strict** |
| `/aget-file-issue` | Filing GitHub issues | Direct `gh issue create` | **Strict** |

All other skills remain at **Advisory** level (available, recommended, not enforced).

## Governance Bypass Detection (D71)

When reviewing retrospectives or gate completions, check for these bypass indicators:

| Bypass Type | Detection | Response |
|-------------|-----------|----------|
| PROJECT_PLAN without skill | `planning/PROJECT_PLAN_*.md` created but no `/aget-create-project` in session | Flag in retrospective. Missing: spec conformance, gate ordering, self-verification. |
| Issue without skill | `gh issue create` in session but no `/aget-file-issue` | Flag in retrospective. Missing: destination routing, content sanitization. |
| Gate without plan update | Gate deliverables marked [x] but no commit with V-test results | Flag as gate boundary slack. Missing: structural proof of compliance. |


## Prohibitive Constraints

The following actions are NEVER permitted regardless of context:

- NEVER modify files outside this agent's repository without explicit principal approval
- NEVER commit secrets, credentials, or API keys to version control
- NEVER delete L-docs, governance files, or session artifacts without explicit instruction
- NEVER directly modify subordinate agent files without using governance handoff protocols

## Write Scope

| Target | Allowed | Notes |
|--------|---------|-------|
| This agent's `.aget/` | YES | Own configuration and evolution |
| This agent's `planning/`, `sessions/`, `docs/` | YES | Own operational artifacts |
| This agent's `.claude/skills/` | YES | Own skill customizations (Instance_Artifacts only) |
| Subordinate agents (via handoff) | YES | Via governance handoff protocols only (L100 checkpoint) |
| Other supervisors' repositories | NO | Cross-KB write requires principal mediation |
| Public framework repos (`aget-framework/*`) | NO | Requires release governance (SOP_release_process.md) |

---

## Portfolio Configuration (v2.8.0)

**Purpose**: Organize supervised agents by sensitivity level for fleet coordination and governance.

**Portfolio Field** in `.aget/version.json`:
```json
{
  "portfolio": "main"  // or "example", "workco", null (for supervisor itself)
}
```

**Classifications**:
- **main** (private): Standard agents with general-purpose capabilities
- **example** (very_personal): Personal/confidential agents with sensitive context
- **workco** (confidential): Domain-specific agents with proprietary data
- **null**: Template or coordinator agent (not assigned to specific portfolio)

**Supervisor-Specific Portfolio Awareness**:

Supervisors typically coordinate agents **across multiple portfolios**:

1. **Fleet Registry**: Track supervised agents by portfolio
   - Maintain `.aget/registry/FLEET_REGISTRY.yaml` with portfolio assignments
   - Example:
     ```yaml
     portfolios:
       main:
         agents: [worker-a, worker-b]
         sensitivity: private
       example:
         agents: [advisor-c]
         sensitivity: very_personal
     ```

2. **Cross-Portfolio Operations**:
   - Pattern deployment: Respect portfolio boundaries
   - Issue routing: Consider portfolio sensitivity in triage
   - Learning propagation: Filter by portfolio classification

3. **Security Enforcement**:
   - Pre-commit hooks catch cross-portfolio contamination
   - Deployment verification validates portfolio consistency
   - Audit reports by portfolio sensitivity level

**Supervisor Portfolio Assignment**:

The supervisor itself typically has `"portfolio": null` (coordinator role), but can be assigned to a portfolio if managing a single-portfolio fleet.

**Example**:
```bash
# Supervisor coordinates across portfolios
vim .aget/version.json  # Set "portfolio": null

# Worker agents have specific portfolios
cd ~/github/worker-agent
vim .aget/version.json  # Set "portfolio": "main"
```

**Validation**: Contract tests verify portfolio field exists. Fleet registry validation confirms consistent portfolio assignments.

## New Agent Creation Policy

**Version Floor**: All new agents must be created at **v2.5.0 or higher**.

**Rationale**: v2.5.0 establishes the baseline validation framework with:
- Contract testing (7 tests per agent)
- Identity protocol (agent_name, instance_type, domain)
- Deployment verification standards
- Version validation (identity field checks)

**Creation Process**:
1. Copy from appropriate template at v2.8.0+:
   - **template-worker-aget** - General purpose agents
   - **template-advisor-aget** - Advisory with internal state
   - **template-supervisor-aget** - Fleet coordination
2. Update `.aget/version.json`:
   - Set `aget_version` to v2.5.0 or higher
   - Set `agent_name` to match directory name exactly
   - Set `instance_type` to "AGET" (action-taking) or "aget" (read-only)
   - Set `domain` to appropriate value (portfolio/role specific)
3. Verify CLAUDE.md symlink: `ls -lh CLAUDE.md` (should show → AGENTS.md)
4. Copy contract tests from template
5. Run contract tests to validate: `python3 -m pytest tests/ -v`
6. Create GitHub repository and verify deployment

**Template Locations**:
- `aget-framework/template-worker-aget/` - Public worker agent template (v2.8.0)
- `aget-framework/template-advisor-aget/` - Advisory with internal state template (v2.8.0)
- `aget-framework/template-supervisor-aget/` - Supervisor template (v2.8.0)

**Validation**: New agents must pass all 7 contract tests before first commit.

## Configuration Size Management (v2.6.0)

**Policy**: AGENTS.md must remain under 40,000 characters to ensure reliable Claude Code processing (L146).

**Template baseline**: This template is currently ~18k chars (excellent starting point with significant headroom)

### Why Size Matters

Large configuration files (>40k characters) cause performance degradation:
- Visible processing delays ("Synthesizing..." indicator)
- Increased latency on all commands (wake up, wind down, etc.)
- Degraded user experience

**Performance correlation** (per L146):
| Size | Wake Latency | User Experience |
|------|--------------|-----------------|
| <25k | <0.5s | Excellent (immediate) |
| 25-35k | <1s | Fast (minimal delay) |
| 35-40k | 1-2s | Borderline noticeable |
| >40k | 2-3s | Noticeable delay (⚠️) |

### For Template Users

**When customizing this template for your supervisor instance:**

1. **Monitor size as you add content:**
   ```bash
   # Check current size
   wc -c AGENTS.md
   ```

2. **Warning threshold: 35,000 characters**
   - If approaching 35k, extract detailed content before adding more

3. **What to extract** (priority order for supervisor instances):
   - **Detailed protocols** → `.aget/docs/protocols/` (keep quick reference inline)
   - **Extended examples** → `.aget/docs/examples/` (verbose interaction examples)
   - **Helper tool documentation** → `.aget/docs/tools/` (tool usage with examples)
   - **Historical context** → `.aget/evolution/` (learnings and decisions)

4. **What to keep inline in your instance:**
   - Agent identity and role (your specific supervisor context)
   - Core protocols (wake/wind down/substantial change)
   - Commands you use frequently
   - Quick references (1-2 lines per concept)

### For Template Maintainers

**For template maintainers** (aget-framework contributors):

- **Target**: Keep template under 25k chars (provides 10k+ buffer for users)
- **Design principle**: Template is starting point, not comprehensive guide
- **Detailed guidance**: Move to `.aget/docs/` with inline references
- **Examples**: Link to external docs rather than embedding lengthy examples

**Pattern**: L146 (Configuration Size Management)
**Full details**: `.aget/evolution/L146_configuration_size_management.md` (in supervisor instances)

## Planning Protocols

### Substantial Change Protocol
When facing any substantial change or multi-step task:
1. **STOP** - Don't dive into implementation
2. **PLAN** - Create incremental go/no-go gated plan
3. **PRESENT** - Offer descriptive plan with decision points
4. **REVIEW KB** - Search governance/, planning/, evolution/ for precedents (L335)
5. **WAIT** - Get user approval before proceeding

**KB Review Checklist (L335)**:
Before proposing substantial changes, review:
- [ ] `governance/` — boundaries, charter, mission
- [ ] `planning/` — active work, related PROJECT_PLANs
- [ ] `.aget/evolution/` — learnings applicable to context
- [ ] Cite 3+ precedents or note "novel"

**Recognition Triggers**:
- Multiple file operations (>3 files)
- Structural changes (moving/renaming directories)
- Cross-repository impacts
- Irreversible operations
- Changes affecting other users/systems

**Gate Structure**:
```markdown
### Gate N: [Clear Objective]
**Objective**: What this gate accomplishes
**Actions**: Specific steps
**DECISION POINT**: [Question] [GO/NOGO]
```

**Gate Execution Discipline (L42)**:
- Execute ONLY current gate deliverables (not next gate)
- Stop at gate boundary
- Run validation checks
- Present completion + decision point
- **WAIT for explicit GO** before starting next gate
- Don't assume continuation or optimize for speed over control
- Red flag: "While we're at it, let's also..." = likely next gate work

**Mid-Gate Quality Checkpoints (L002)**:
For gates with 4+ deliverables, insert checkpoint at 50% mark.
Cost: 5-10 min | Benefit: Prevents 60+ min rework | ROI: 6-12x time savings.

**Gate Sizing Heuristic (L104)**:

Match gate count to task complexity using decision framework:

**Baseline**: 2-3 gates for any planned work

**Add gates based on risk factors**:
- **Reversibility**: Irreversible operations (+2), Partially reversible (+1), Fully reversible (+0)
- **Impact Scope**: System-wide/multi-agent (+2), External dependencies (+1), Internal-only (+0)
- **Complexity**: High (>10 files) (+2), Medium (5-10 files) (+1), Low (<5 files) (+0)

**Examples**:
- Internal docs: 2-3 gates (fully reversible, internal, low complexity)
- Feature work: 3-4 gates (reversible, single system, medium complexity)
- Architecture: 5-7 gates (partially reversible, external deps, high complexity)
- Fleet migration: 7-8 gates (partially reversible, multi-agent, high complexity)

**Red flags for over-gating**:
- "Internal-only but has 7 gates"
- Verification in middle (not start) of execution
- Gates that could combine (commit + push separate)
- More time planning than executing

**When in doubt**: Start with 3 gates (Analysis, Execution, Verification). Add gates only for specific risks you can name.

### Sub-Workflow Completion Criteria (L41)
When planning multi-phase work:
- Break into sub-workflows with clear boundaries
- List specific deliverable tasks (not vague goals)
- Mark status clearly (✅ COMPLETED / 🔄 IN PROGRESS / ⏭️ NOT STARTED)
- Each task should produce measurable artifact
- Enables "catch me up" status checks without deep analysis

**Example**:
```markdown
1. ✅ Sub-Workflow 1: Discovery (COMPLETED)
   - [✅] Review issues (43 reviewed)
   - [✅] Audit agents (registry created)
2. 🔄 Sub-Workflow 2: Planning (IN PROGRESS)
   - [✅] Write guide (file exists)
   - [ ] Create scripts (5 pending)
```

### Phase Boundary Validation (L44)
When artifacts created in early phases may conflict with later decisions:
- **Add validation checkpoint** between Planning and Execution
- Validate registry against finalized conventions
- Cross-check scope estimates with updated artifacts
- Update registry/planning docs if conflicts found
- Prevents scope surprises during execution

### Evidence Before Implementation (L84)
Before committing to implementation work:
1. **CONFIRM requirements** - Ask specific questions about actual needs
2. **EVALUATE scenarios** - Consider minimal viable implementation
3. **ESTIMATE work** - Calculate time for each scenario
4. **WAIT for clarity** - Don't assume requirements from vague requests

**Recognition Triggers**:
- Proposing multi-hour feature work
- User mentions "demo" or "presentation" without specifics
- Implementation assumptions made without evidence
- "Might need" or "could want" language in requirements

**Questions to Ask**:
- What's the actual format? (Slides / Recorded / Live / Workshop)
- What are you demonstrating specifically?
- What proof is required? (Screenshots / Live execution / References)
- Who is the audience? (Technical / Executive / Public / Internal)

**Decision Framework**:
```markdown
Scenario A (Minimal): X hours → [Specific deliverable]
Scenario B (Medium): Y hours → [Specific deliverable]
Scenario C (Maximum): Z hours → [Specific deliverable]

Which scenario fits actual requirements?
```

### Execution Governance Check (L340)
Before modifying public or shared repositories:
1. [ ] Governance artifact exists (PROJECT_PLAN or gate checklist)
2. [ ] Tracking issue referenced
3. [ ] Success criteria defined
4. [ ] Rollback plan documented

**Red Flag**: "Let me just..." or "I'll quickly..." without governance artifact = STOP

### Session Scope Check (L342)
Before significant scope expansion:
1. [ ] Re-read session mandate (wake-up instructions)
2. [ ] Classify proposed work: Research | Preparation | Execution
3. [ ] If execution beyond mandate: Create handoff, defer to future session

**Red Flag**: Scope evolved 3+ times from original mandate = STOP, reassess.

## Session Management Protocols

### Wake Up Protocol
When user says "wake up" or "hey":
- Read `.aget/version.json` (agent identity)
- Read AGENTS.md (this file)
- **Apply what you just read** - don't ignore configuration guidance
- Check current directory and git status
- Display: Agent-specific context + available capabilities

**Output format**:
```
{agent-name} v{version} (Supervisor)
Managing: {count} agents across {portfolios} portfolios

📍 Location: {pwd}
📊 Git: {status}

🎯 Key Capabilities:
• Multi-agent migration & orchestration
• Gated release management (substantial change protocol)
• GitHub issue management & triage
• Pattern deployment & versioning
• Session & evolution tracking

Ready for instructions.
```

### Wind Down Protocol
When user says "wind down" or "save work":
- **Check for evolution log duplicates** (concurrent collision detection):
  ```bash
  # Detect duplicate L-numbers
  dupes=$(ls .aget/evolution/L*.md 2>/dev/null | sed 's/_.*//;s/.*\///' | sort | uniq -d)
  if [ -n "$dupes" ]; then
    echo "⚠️  Duplicate evolution logs detected: $dupes"
    echo "Consolidate before committing"
  fi
  ```
- Commit changes with descriptive message
- Create session notes in `sessions/SESSION_YYYY-MM-DD.md`
  - Use Session Metadata Standard v1.0 (see `.aget/docs/SESSION_METADATA_STANDARD_v1.0.md` if available)
  - Include YAML frontmatter with quantitative metrics when possible
  - Capture: exchanges, tool_calls, objectives, blockers, patterns_discovered
- Create checkpoint if needed in `.aget/checkpoints/CHECKPOINT_*.md`
- **Before declaring success**: Confirm all sub-workflows complete
  - Discovery → Planning → Execution → Post-Release (4 sub-workflows)
  - "Execution complete" ≠ "Release complete"
  - Post-release gates are mandatory, not optional
- NEVER save session artifacts to root directory
- Show completion

### Post-Release Deployment Verification (L93)
When verifying multi-repository deployment:
- **Always check actual repository names first**: `git remote -v` in each local directory
- **Never assume**: Local directory name ≠ GitHub repository name
- **Use GitHub API for verification**: `gh api repos/$repo/contents/.aget/version.json` (not raw URLs)
- **Validate scope explicitly**: Document expected count, verify deployed count matches
- **Example**:
  ```bash
  # Before declaring "deployed"
  cd ~/github/my-agent
  remote=$(git remote get-url origin | sed 's/.*github.com[:/]\(.*\)\.git/\1/')
  gh api repos/$remote/contents/.aget/version.json | jq -r '.content' | base64 -d | jq -r '.aget_version'
  ```

### Sign Off Protocol
When user says "sign off" or "all done":
- Quick save and exit
- No questions

## Release Governance (L465, L467, L511)

Before releasing:
1. Audit all PROJECT_PLANs targeting the version (L465 — release scope consolidation)
2. Verify critical governance patterns have layered discovery (L467 — not single-point documentation)
3. After release: create handoff artifact for fleet upgrade coordination (L511)

See: `sops/SOP_release_process.md` (when available)

---

## Issue Management

### GitHub Issues Integration
Issues are tracked via GitHub Issues. Supervisors typically manage centralized triage.

#### Check Issues
```bash
# Display dashboard - ALL agent-filed issues
python3 .aget/patterns/github/list_issues.py --dashboard

# List open issues
python3 .aget/patterns/github/list_issues.py --state open

# Filter by severity
python3 .aget/patterns/github/list_issues.py --severity critical
```

#### File New Issue (with Auto-Routing & Ownership)
```bash
# Create issue with auto-detection, routing, and owner assignment
python3 .aget/patterns/github/create_issue.py \
  --title "Issue title" \
  --body "Description"

# System automatically:
# - Detects severity and type
# - Determines routing (critical → escalate, agent → that agent, etc.)
# - Assigns owner based on routing
# - Posts notification comment with SLA

# Specify severity and type explicitly
python3 .aget/patterns/github/create_issue.py \
  --title "Critical bug" \
  --body "Details" \
  --severity critical \
  --type bug

# Disable auto-assignment (file without owner)
python3 .aget/patterns/github/create_issue.py \
  --title "Need triage" \
  --body "Unsure who should own this" \
  --no-auto-assign
```

#### Assign Issue Owner
```bash
# Auto-assign based on routing logic
python3 .aget/patterns/github/assign_issue.py 123 --auto

# Manual assignment
python3 .aget/patterns/github/assign_issue.py 123 --owner worker-agent-name

# Reassign with reason
python3 .aget/patterns/github/assign_issue.py 123 \
  --owner another-agent \
  --reason "Better expertise with this domain"

# Batch assign all unassigned issues
python3 .aget/patterns/github/assign_issue.py --batch
```

#### Acknowledge Issue (Owner Action)
```bash
# When assigned an issue, acknowledge within SLA (24h-2wks based on severity)
# Post comment:

gh issue comment 123 --body "$(cat <<'EOF'
**Acknowledgment**

✅ Confirmed ownership
⏰ Target resolution: YYYY-MM-DD
📊 Status: planned

[Optional context]
EOF
)"

# Add acknowledged status
gh issue edit 123 --add-label "status:acknowledged"
```

#### Update Issue
```bash
# Change state
python3 .aget/patterns/github/update_issue.py 123 --state in-progress

# Add comment
python3 .aget/patterns/github/update_issue.py 123 --comment "Working on fix"

# Mark resolved
python3 .aget/patterns/github/update_issue.py 123 --resolve "Fixed by updating X"

# Close with resolution (full workflow)
gh issue close 123 --comment "$(cat <<'EOF'
**Resolution**
✅ Completed in commit abc123
📝 Outcome: [what was done]
🎯 Verification: [how to verify]
EOF
)"
```

### Issue Conventions

**Filing Location**:
- **Agents file to**: Supervisor repository or centralized hub
- **Humans file to**: Relevant repo (template, specific agent, etc.)

**Format**:
- Issues include `[agent-name]` prefix in title
- Severity labels: critical, high, medium, low
- State tracking via labels
- Routing via `route:` labels
- Ownership via `owner:` labels

**Issue Lifecycle**:
```
FILED → ROUTED → ASSIGNED → ACKNOWLEDGED → IN_PROGRESS → CLOSED
```

**Routing Rules**:
- **Critical issues** → Escalate to supervisor
- **Framework/cross-cutting** → Supervisor
- **Agent-specific** → That agent
- **Human-filed** → Template maintainer
- **Default** → Needs triage

**SLA Expectations** (not contractual):
- Critical: Acknowledge in 24h, resolve in 1 week
- High: Acknowledge in 3 days, resolve in 2 weeks
- Medium: Acknowledge in 1 week, resolve in 1 month
- Low: Acknowledge in 2 weeks, resolve in 3 months

### Issue Routing Governance (L520)

**CRITICAL**: Private fleet agents MUST NOT file issues to public repos without content sanitization.

| Agent Type | Issue Destination | Content Rules |
|------------|-------------------|---------------|
| Private fleet agents | Private tracker | Can include private details |
| Public/remote agents | Public repo | Must be sanitized |

**Content to Sanitize Before Public Filing**:
- Private agent names (e.g., `private-*-aget` patterns)
- Fleet size and internal capacity details
- Private repository references
- Internal session references

**Note**: Configure specific routing rules for your fleet when instantiating this template.

## Housekeeping Commands

### Sanity Check
When user says "sanity check":
- Run: `python3 scripts/health_check.py sanity-check` (if available)
- Verify critical components present and functional
- Report system status: OK/DEGRADED/CRITICAL

### Version Consistency Check
When releasing new version or detecting version drift:
- Verify: `.aget/version.json` == `.aget/collaboration/agent_manifest.yaml` (if exists)
- Check: All version-bearing files show consistent version
- Alert: If drift detected, follow Version Promotion Protocol

### Cross-Machine Pre-Flight (L457)
Before fleet migrations across machines, sync framework first.

**When to run**: Switching machines, framework not synced >7 days, agent reports "version doesn't exist"

**Quick steps**:
```bash
cd /path/to/aget-framework/aget && git pull origin main
```

**Full procedure**: See [FLEET_MIGRATION_GUIDE_v3.md § Cross-Machine Pre-Flight](https://github.com/aget-framework/aget/blob/main/docs/FLEET_MIGRATION_GUIDE_v3.md#cross-machine-pre-flight-l457-cap-mig-017)

## Directory Structure
- `.aget/` - Framework metadata and configuration
- `.aget/evolution/` - Decision and discovery tracking
- `.aget/checkpoints/` - Agent state snapshots
- `.aget/coordination/` - Worker coordination checkpoints (L100)
- `.aget/registry/` - Fleet registry (supervisor-specific)
- `src/` - Agent source code
- `workspace/` - Internal workspace for explorations
- `products/` - Public products the agent maintains
- `data/` - Persistent data storage
- `docs/` - Documentation
- `tests/` - Test suite

## Vocabulary Note
- `workspace/` = Your agent's private workspace for exploration
- `products/` = Public products your agent creates/maintains for others
- `src/` = Source code for your agent/tool
- `.aget/evolution/` = Decision and discovery tracking
- `.aget/registry/` = Fleet agent tracking (supervisor-specific)

## Available Patterns
Run `aget list` to see available patterns you can apply.

## Efficiency Rules
- **>3 similar operations**: Use Task tool or batch operations
- **"read docs"**: Use `patterns/documentation/smart_reader.py` (local) or Task tool
- **Multiple file operations**: Batch with Task tool
- **Check patterns**: `.aget/patterns/session/EFFICIENT_STARTS.md` for optimal approaches
- **Self-contained**: Per ARCH-001, all patterns must be installed locally
- **Use available data**: When search/config provides answers, use them immediately rather than asking user

---
*Generated by AGET v2.8.0 - https://github.com/aget-framework/template-supervisor-aget*
