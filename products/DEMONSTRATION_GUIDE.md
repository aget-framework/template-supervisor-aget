# Demonstration Guide: Supervisor AGET Capabilities

**Purpose**: Guide for demonstrating supervisor agent capabilities effectively
**Audience**: AGET users, potential adopters, architecture reviewers
**Version**: 1.0 (v2.5.0)
**Last Updated**: 2025-10-06

---

## Overview

This guide shows how to demonstrate supervisor agent capabilities in a way that highlights the unique value proposition of coordination agents in the AGET framework.

**Key Message**: Supervisors coordinate multiple agents, enforce process discipline, manage fleet lifecycle, and maintain organizational memory.

---

## Supervisor vs Worker: Core Differences

### Worker Agent
- **Focus**: Execute specific domain tasks (data analysis, GitHub operations, etc.)
- **Scope**: Single-agent workflow
- **Memory**: Own session history and evolution logs
- **Authority**: Task execution within domain

### Supervisor Agent
- **Focus**: Coordinate multiple agents, enforce standards, manage migrations
- **Scope**: Fleet-wide coordination
- **Memory**: Shared evolution repository (`.aget/evolution/`)
- **Authority**: Process enforcement, work assignment, cross-agent orchestration

**Visual Comparison**:
```
Worker:           Human → agent → task execution
Supervisor:       Human → supervisor → [agent1, agent2, ...agentN] → coordinated execution
```

---

## Demonstration Structure (30-45 minutes)

### Part 1: Framework Positioning (5 min)
**Show**: What AGET is and isn't

**Script**:
> "AGET is not an autonomous agent runtime like LangChain or AutoGPT.
> It's a configuration and lifecycle management system for CLI-based human-AI collaborative coding.
> Key differentiators:
> - Universal CLI compatibility (Claude Code, Cursor, Aider, Windsurf)
> - Contract testing and version compliance
> - Shared learning repository (organizational memory)
> - Human-centric governance (gated releases, evidence-based planning)
> - Lightweight, zero-infrastructure (markdown + git)"

**Evidence**: Show `AGENTS.md:11-30` (Framework Positioning section)

---

### Part 2: Fleet Registry & Architecture (5 min)
**Show**: How supervisors track multiple agents

**Demo Steps**:
1. Open `.aget/registry/agents.yaml`
2. Walk through agent entries:
   - Agent metadata (name, type, version, domain, status)
   - Portfolio grouping (data-portfolio, automation-portfolio)
   - Fleet statistics (version distribution, migration tracking)

**Script**:
> "Supervisors maintain a fleet registry showing:
> - Which agents are supervised (10 agents across 3 portfolios)
> - Current versions (tracking v2.4.0 → v2.5.0 migrations)
> - Status and capabilities
> - Migration progress"

**Evidence**: Show `.aget/registry/agents.yaml`

**Follow-up**: Explain Recursive Supervision Model (L99)
> "Every agent is a worker. Supervision is a capability, not a type.
> Even supervisors are supervised: Human → supervisor → worker agents
> This enables multi-level hierarchies and dynamic reorganization."

---

### Part 3: Process Enforcement (10 min)
**Show**: Substantial Change Protocol and gate sizing

**Demo Steps**:
1. Open `AGENTS.md` and show Substantial Change Protocol section
2. Explain gate structure:
   ```markdown
   ### Gate N: [Clear Objective]
   **Objective**: What this gate accomplishes
   **Actions**: Specific steps
   **DECISION POINT**: [Question] [GO/NOGO]
   ```

3. Show Gate Sizing Heuristic (L104):
   - Baseline: 2-3 gates
   - Add for: Reversibility (+0-2), Impact Scope (+0-2), Complexity (+0-2)

4. Open `products/EXAMPLE_3_GATE_PLAN.md`:
   - Internal docs update: +0+0+0 = **3 gates**
   - Walkthrough: Planning → Execution → Commit

5. Open `products/EXAMPLE_7_GATE_PLAN.md`:
   - Fleet migration: +1+2+2 = **7 gates**
   - Walkthrough: Discovery → Canary → Fleet → Validation → Monitoring

**Script**:
> "Supervisors enforce gate discipline to prevent:
> - Scope creep ('while we're at it...')
> - Premature implementation (no planning)
> - Process violations (skipping validation)
>
> The Gate Sizing Heuristic (L104) provides a formula:
> Simple internal changes → 3 gates (1 hour)
> Complex multi-agent work → 7 gates (5-7 hours)
>
> This is not bureaucracy. It's risk-proportionate governance."

**Evidence**: Show `AGENTS.md:85-166`, `products/EXAMPLE_3_GATE_PLAN.md`, `products/EXAMPLE_7_GATE_PLAN.md`

**Common Question**: "Isn't this over-engineering?"
**Answer**: "No. Gate count matches risk. Documentation update: 3 gates (1 hour). Fleet migration: 7 gates (5 hours). Over-gating would be 7 gates for docs."

---

### Part 4: Supervision Patterns (10 min)
**Show**: How supervisors manage and critique agents

**Demo Steps**:
1. Open `AGENTS.md` and navigate to "Supervision Patterns (L099)"
2. Walk through 6 patterns:
   - **Process Enforcement**: Catch violations early
   - **Incremental Oversight**: Review at natural checkpoints
   - **Intervention Timing**: Know when to stop vs proceed
   - **Teaching Through Critique**: Quality feedback drives behavior change
   - **Scope Management**: Shape proposals into actionable plans
   - **Meta-Oversight**: Supervise the supervision

3. Show critique format example:
   ```
   Process 2/10: No gate plan (violation), 914 lines without preview (violation)
   → Actionable: Create 3-5 gate plan, present for approval
   ```

**Script**:
> "Supervisors don't just approve/reject. They teach through critique:
> - Quantitative rating (X/10) with specific violations
> - Explain why it matters (impact, not just rules)
> - Provide actionable path forward
> - Acknowledge improvement (2/10 → 9/10)
>
> This drives behavior change across the fleet."

**Evidence**: Show `AGENTS.md:41-83`

**Common Question**: "How do you balance intervention vs autonomy?"
**Answer**: "Intervene on process violations, scope creep, disproportionate time investment. Don't intervene when agent follows approved gates with reasonable estimates."

---

### Part 5: Organizational Memory (5 min)
**Show**: Evolution logs and shared learning

**Demo Steps**:
1. Open `.aget/evolution/` directory
2. Show L-number format (L001, L002, L103, etc.)
3. Open `.aget/evolution/README.md` and explain:
   - L = Learning (pattern discovered)
   - D = Decision (architectural choice)
   - DISC = Discovery (system finding)

4. Show concurrent collision prevention:
   ```bash
   # During wind-down, detect duplicate L-numbers
   dupes=$(ls .aget/evolution/L*.md | sed 's/_.*//;s/.*\///' | sort | uniq -d)
   if [ -n "$dupes" ]; then
     echo "⚠️  Duplicate evolution logs detected: $dupes"
   fi
   ```

**Script**:
> "Supervisors maintain organizational memory through evolution logs:
> - L104: Gate sizing heuristic
> - L099: Multi-agent supervision patterns
> - L093: Repository deployment verification
> - L084: Evidence before implementation
>
> These learnings propagate across the fleet. Every agent benefits from collective experience.
>
> Concurrent collision prevention ensures sequence integrity when multiple agents run simultaneously."

**Evidence**: Show `.aget/evolution/README.md`, evolution log examples

**Common Question**: "How is this different from regular documentation?"
**Answer**: "Documentation describes what to do. Evolution logs explain why we do it that way, based on actual experience. They capture failure modes, false starts, and hard-won insights."

---

### Part 6: Contract Testing & Version Compliance (5 min)
**Show**: How v2.5.0 establishes validation framework

**Demo Steps**:
1. Navigate to `tests/` directory
2. Show contract test files:
   - `test_wake_contract.py` (4 tests)
   - `test_identity_contract.py` (3 tests)

3. Run contract tests:
   ```bash
   python3 -m pytest tests/ -v
   ```

4. Open `tests/README.md` and explain:
   - Wake protocol (4 tests): version.json read, AGENTS.md read, git status, pwd
   - Identity protocol (3 tests): agent_name, instance_type, domain

**Script**:
> "v2.5.0 introduced contract testing:
> - 7 tests per agent (wake: 4, identity: 3)
> - Validates framework compliance
> - Prevents version drift
> - Baseline requirement for new agents
>
> New Agent Creation Policy: All agents must be created at v2.5.0 or higher.
>
> Contract tests ensure every agent in the fleet follows the same standards."

**Evidence**: Show `tests/README.md`, run pytest, show `AGENTS.md:216-246` (New Agent Creation Policy)

**Common Question**: "What happens if tests fail?"
**Answer**: "Agent is not compliant with v2.5.0 standard. Fix configuration (version.json, AGENTS.md) before committing. Tests provide specific failure messages showing what to fix."

---

### Part 7: Issue Management & Fleet Coordination (5 min)
**Show**: How supervisors triage and route work

**Demo Steps**:
1. Open `AGENTS.md` and navigate to "Issue Management" section
2. Show issue lifecycle:
   ```
   FILED → ROUTED → ASSIGNED → ACKNOWLEDGED → IN_PROGRESS → CLOSED
   ```

3. Show routing rules:
   - Critical issues → Escalate to supervisor
   - Framework/cross-cutting → Supervisor
   - Agent-specific → That agent
   - Human-filed → Template maintainer

4. Show helper scripts:
   ```bash
   # Dashboard - all agent-filed issues
   python3 .aget/patterns/github/list_issues.py --dashboard

   # Create issue with auto-routing
   python3 .aget/patterns/github/create_issue.py \
     --title "Issue title" \
     --body "Description"
   # Automatically detects severity, routes, assigns owner
   ```

**Script**:
> "Supervisors coordinate issue management across the fleet:
> - Centralized triage (agents file to hub repo)
> - Auto-routing based on severity and type
> - Owner assignment with SLA expectations
> - Acknowledgment protocol (24h-2wks based on severity)
>
> This prevents:
> - Issues falling through cracks
> - Unclear ownership
> - Delayed response on critical issues
>
> Cross-agent visibility ensures fleet-wide awareness."

**Evidence**: Show `AGENTS.md:320-450`, `.aget/docs/ISSUE_ACTION_PROTOCOL_v1.0.md`

**Common Question**: "Why centralized triage instead of per-agent repos?"
**Answer**: "Cross-agent visibility, privacy control, and consistent routing logic. Supervisor sees full fleet status. Critical issues escalate automatically."

---

## Key Takeaways (Summary Slide)

### What Supervisors Do
1. **Coordinate**: Manage multiple agents across portfolios
2. **Enforce**: Substantial Change Protocol, gate discipline, process standards
3. **Teach**: Critique agent work, drive behavior change through feedback
4. **Maintain**: Organizational memory (evolution logs), fleet registry, issue triage
5. **Validate**: Contract testing, version compliance, deployment verification
6. **Scale**: Multi-level hierarchies (recursive supervision model)

### Why Supervisors Matter
- **Risk Management**: Gate sizing matches complexity (3 gates for docs, 7 for migrations)
- **Knowledge Propagation**: Evolution logs share learnings across fleet
- **Quality Assurance**: Process enforcement prevents scope creep and premature implementation
- **Fleet Coordination**: Centralized triage, auto-routing, SLA tracking
- **Version Governance**: Ensure fleet-wide compliance with framework standards

### AGET's Unique Niche
- Not autonomous (human-supervised)
- Not production ALM (lightweight, zero-infrastructure)
- Universal CLI compatibility (works across tools)
- Human-centric governance (gated releases, evidence-based planning)
- Organizational memory (shared learning repository)

---

## Common Objections & Responses

### "This looks like waterfall/bureaucracy"
**Response**:
> "Gate count is proportional to risk. Documentation update: 3 gates (1 hour). Fleet migration: 7 gates (5 hours). We're not adding process for its own sake—we're matching governance to impact. And gates are incremental with GO/NOGO decision points, not a monolithic plan."

**Evidence**: Show gate sizing heuristic (L104), compare 3-gate vs 7-gate examples

---

### "Why not just use autonomous agents?"
**Response**:
> "AGET is explicitly human-supervised. Every gate has a human GO/NOGO decision point. This prevents autonomous agents from:
> - Scope creep ('while we're at it...')
> - Premature commits without validation
> - Cross-agent conflicts
>
> Supervision provides accountability and control."

**Evidence**: Show gate structure with decision points, supervision patterns (L099)

---

### "How does this scale to 50+ agents?"
**Response**:
> "Recursive supervision model (L99). Supervisors can supervise supervisors:
> ```
> Human → coordinator → [portfolio-1-supervisor, portfolio-2-supervisor] → workers
> ```
>
> Multi-level hierarchies with clear accountability chains. Same structure at every level."

**Evidence**: Show `AGENTS.md:33-39` (Recursive Supervision Model)

---

### "What if agent disagrees with supervisor critique?"
**Response**:
> "Escalate to human. Supervisors provide:
> - Quantitative rating (X/10)
> - Specific violations with evidence
> - Actionable path forward
>
> If agent believes critique is incorrect, human reviews and decides. This is human-supervised coordination, not autonomous authority."

**Evidence**: Show critique format example, supervision patterns (L099)

---

### "Isn't this over-documented?"
**Response**:
> "Evolution logs capture organizational memory. Without them:
> - Same mistakes repeated across agents
> - No knowledge transfer (what works, what doesn't)
> - Context lost when agents change
>
> L104 (gate sizing) prevents over-gating. L084 (evidence before implementation) prevents over-engineering. L099 (supervision patterns) codifies effective coordination.
>
> These learnings cost hours of experimentation. Documentation preserves that investment."

**Evidence**: Show evolution log examples (L104, L099, L084)

---

### "How do I customize for my fleet?"
**Response**:
> "Template provides structure. Customize:
> 1. **Fleet registry**: Replace example agents with your actual agents
> 2. **AGENTS.md**: Add your domain-specific protocols
> 3. **Evolution logs**: Document your learnings (L-numbers)
> 4. **Issue routing**: Adjust routing rules for your team structure
> 5. **Portfolio grouping**: Organize agents by your architecture
>
> Keep the framework (gates, contracts, supervision patterns). Customize the content."

**Evidence**: Show `.aget/registry/agents.yaml` (example template), `CUSTOMIZATION_GUIDE.md`

---

## Preparation Checklist

Before demonstrating supervisor capabilities:

- [ ] Clone template: `git clone https://github.com/aget-framework/template-supervisor-aget`
- [ ] Run contract tests: `python3 -m pytest tests/ -v` (verify baseline)
- [ ] Review key files:
  - [ ] `AGENTS.md` (supervisor configuration)
  - [ ] `.aget/registry/agents.yaml` (fleet registry)
  - [ ] `products/EXAMPLE_3_GATE_PLAN.md` (simple)
  - [ ] `products/EXAMPLE_7_GATE_PLAN.md` (complex)
  - [ ] `.aget/evolution/README.md` (organizational memory)
  - [ ] `tests/README.md` (contract testing)
- [ ] Prepare demo environment:
  - [ ] Terminal window with template directory open
  - [ ] Editor with key files ready to display
  - [ ] Browser with GitHub issues page (if showing issue management)
- [ ] Identify audience level:
  - [ ] Technical: Deep dive into contract tests, evolution logs, gate sizing
  - [ ] Executive: Focus on risk management, organizational memory, quality assurance
  - [ ] Public: Framework positioning, supervisor vs worker, key capabilities

---

## Timing Variants

### 15-Minute Lightning Demo
- Framework positioning (2 min)
- Fleet registry (2 min)
- Gate sizing with 3-gate vs 7-gate examples (6 min)
- Supervision patterns (3 min)
- Organizational memory (2 min)

### 30-Minute Standard Demo
- Follow 7-part structure above (5 min each)
- Skip deep dives, hit key points

### 45-Minute Deep Dive
- Follow 7-part structure above (5-10 min each)
- Include: Live contract test run, evolution log creation example, issue routing demonstration
- Take questions throughout

### 2-Hour Workshop
- All 7 parts with hands-on exercises:
  - Create custom fleet registry
  - Write 3-gate plan for example task
  - Create evolution log entry (L-number)
  - Run contract tests on customized agent
  - File and route sample issue

---

## Resources for Demonstrators

### Quick Reference
- **Framework positioning**: `AGENTS.md:11-30`
- **Recursive supervision**: `AGENTS.md:33-39`, `.aget/evolution/L99_recursive_supervision_model.md`
- **Supervision patterns**: `AGENTS.md:41-83`, `.aget/evolution/L099_multi_agent_process_enforcement.md`
- **Gate sizing**: `AGENTS.md:111-166`, `.aget/evolution/L104_gate_sizing_heuristic.md`
- **Contract testing**: `tests/README.md`
- **Issue management**: `AGENTS.md:320-450`, `.aget/docs/ISSUE_ACTION_PROTOCOL_v1.0.md`

### Example Scripts
Located in `.aget/patterns/github/`:
- `list_issues.py --dashboard` - Issue dashboard
- `create_issue.py` - File issue with auto-routing
- `assign_issue.py` - Assign owner
- `update_issue.py` - Update issue state

### Supporting Documentation
- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - How to adapt template
- [Session Metadata Standard v1.0](.aget/docs/SESSION_METADATA_STANDARD_v1.0.md) - Session documentation format
- [Issue Action Protocol v1.0](.aget/docs/ISSUE_ACTION_PROTOCOL_v1.0.md) - Complete issue lifecycle

---

## Post-Demonstration Follow-Up

### Typical Questions After Demo

**"Can I try this with my fleet?"**
1. Clone template: `git clone https://github.com/aget-framework/template-supervisor-aget`
2. Update `.aget/registry/agents.yaml` with your agents
3. Customize `AGENTS.md` with your protocols
4. Run contract tests: `python3 -m pytest tests/ -v`
5. Create first evolution log documenting initial setup

**"What's the learning curve?"**
- **Basic usage** (gates, registry, issue tracking): 1-2 hours
- **Supervision patterns** (critique, intervention timing): 4-6 hours
- **Advanced features** (contract testing, custom specs, multi-level hierarchies): 8-12 hours
- **Mastery** (organizational memory, pattern propagation, fleet optimization): 20-40 hours

**"How do I contribute back?"**
- File issues: `https://github.com/aget-framework/template-supervisor-aget/issues`
- Evolution logs: Share learnings (L-numbers) via PR
- Pattern improvements: Submit pattern enhancements
- Documentation: Clarify unclear sections

**"Where is the community?"**
- GitHub: `https://github.com/aget-framework`
- Issues: Template-specific issues + centralized hub
- Evolution logs: Shared learning repository (public agents only)

---

## Success Metrics

Effective demonstration achieves:
- [ ] Audience understands supervisor vs worker distinction
- [ ] Gate sizing heuristic (L104) makes sense (not arbitrary)
- [ ] Process enforcement seen as risk management, not bureaucracy
- [ ] Organizational memory value is clear (evolution logs)
- [ ] Contract testing purpose is understood (prevent drift)
- [ ] Recursive supervision model is comprehensible
- [ ] Questions focus on "how to apply" not "why this exists"

---

**Template Version**: v2.5.0
**Demonstration Guide Version**: 1.0
**Maintained by**: template-supervisor-aget maintainers
**Last Updated**: 2025-10-06

---

*This guide demonstrates supervisor capabilities for education and adoption. For customization guidance, see [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md).*
