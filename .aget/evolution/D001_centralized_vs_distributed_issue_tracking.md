# D001: Centralized vs Distributed Issue Tracking

**Date**: 2025-10-06
**Status**: Accepted → Implemented
**Decision Makers**: Fleet coordinator (supervisor), informed by multi-agent operational experience

## Context

With 10+ agents operating across multiple repositories, we needed to choose an issue tracking strategy. Each agent could file issues in their own repository (distributed), or all agents could file to a central hub repository (centralized).

**Problem**: How do we track issues across a multi-agent fleet while maintaining:
- Cross-agent visibility (agents need to see related issues from other agents)
- Privacy control (not all agents/issues should be public)
- Routing efficiency (issues should reach the right owner quickly)
- Centralized triage (supervisor needs fleet-wide view)

## Options Considered

### Option A: Distributed (Each Agent → Own Repo)

**Description**: Each agent files issues in their own repository.
```
my-github-AGET → files issues in my-github-AGET repo
my-deployment-AGET → files issues in my-deployment-AGET repo
my-data-analyst-aget → files issues in my-data-analyst-aget repo
```

**Pros**:
- Natural ownership (issues live where the agent lives)
- Standard GitHub practice (issues in same repo as code)
- No cross-repo permissions needed
- Easy to find agent-specific issues

**Cons**:
- **No cross-agent visibility**: Agents can't see related issues from other agents
- **Fragmented triage**: Supervisor must query 10+ repositories
- **Difficult routing**: Framework issues unclear which repo to file in
- **Privacy complexity**: Public repos expose all issues, private repos hide everything
- **Duplicate detection**: No way to find if another agent already filed similar issue

### Option B: Centralized (All Agents → Hub Repo)

**Description**: All agents file issues to central hub repository (aget-framework/aget).
```
my-github-AGET → files issues in aget-framework/aget (with [my-github-AGET] prefix)
my-deployment-AGET → files issues in aget-framework/aget (with [my-deployment-AGET] prefix)
my-data-analyst-aget → files issues in aget-framework/aget (with [my-data-analyst-aget] prefix)
```

**Pros**:
- **Cross-agent visibility**: All agents see all agent-filed issues
- **Centralized triage**: Supervisor has single dashboard view
- **Easy routing**: Framework issues clear destination, agent issues use prefix
- **Privacy control**: Hub repo private → all agent issues private
- **Duplicate detection**: Search one repo, find related issues
- **Fleet metrics**: Total open issues, trends, severity distribution

**Cons**:
- Unconventional (issues not in same repo as code)
- Requires hub repo setup (additional infrastructure)
- Issue counts inflate hub repo (looks like hub has many issues)
- Permissions needed (agents must have write access to hub)

### Option C: Hybrid (Agent-Specific → Own Repo, Framework → Hub)

**Description**: Agent-specific issues in agent repos, framework/cross-cutting issues in hub.

**Pros**:
- Preserves natural ownership for agent issues
- Centralizes cross-cutting concerns

**Cons**:
- **Triage fragmentation**: Still querying multiple repos
- **No cross-agent visibility**: Agent-specific issues invisible to fleet
- **Routing ambiguity**: "Is this agent-specific or cross-cutting?" (gray area)
- **Duplicate detection**: Must search multiple repos
- **Complexity**: Two different workflows depending on issue type

## Decision

**Selected**: **Option B - Centralized (All Agents → Hub Repo)**

**Rationale**:

1. **Cross-agent visibility is critical**: Agents frequently encounter similar issues. Without visibility, we duplicate effort and fail to recognize patterns.

2. **Supervisor needs fleet-wide view**: Centralized triage is essential for coordination. Querying 10+ repos is operationally infeasible.

3. **Privacy control matters**: Hub repo (aget-framework/aget) is private, ensuring all agent-filed issues remain private. Public/private boundary is clear: human-filed → public repos, agent-filed → hub.

4. **Routing efficiency**: Clear destination for all issues. Auto-routing logic (severity → escalate, agent-specific → that agent) works from single location.

5. **Convention over confusion**: Single workflow (always file to hub) is clearer than hybrid rules ("Is this framework or agent-specific?").

**Key insight**: We're not tracking issues about code in a repository. We're tracking work assignments for agents. The natural location is the coordinator's workspace, not each worker's workspace.

## Implementation Details

**Hub repository**: `aget-framework/aget` (private)
**Issue prefix format**: `[agent-name] Issue Title`
**Labels**:
- Severity: `critical`, `high`, `medium`, `low`
- Routing: `route:escalated`, `route:supervisor`, `route:agent`, `route:needs-triage`
- Ownership: `owner:my-github-AGET`, `owner:supervisor`, etc.
- State: `status:acknowledged`, `status:in-progress`, etc.

**Scripts**:
```bash
# File issue (auto-detection + routing)
python3 .aget/patterns/github/create_issue.py --title "Issue" --body "Description"

# Dashboard view
python3 .aget/patterns/github/list_issues.py --dashboard

# Assign owner
python3 .aget/patterns/github/assign_issue.py 123 --auto
```

**Documentation**:
- Issue Action Protocol v1.0 (`.aget/docs/ISSUE_ACTION_PROTOCOL_v1.0.md`)
- AGENTS.md Issue Management section

## Consequences

### Positive

1. **Fleet-wide coordination**: Supervisor sees all issues in single dashboard
2. **Cross-agent learning**: Agents discover related issues from other agents
3. **Routing automation**: Auto-detect severity, route, assign owner
4. **Duplicate prevention**: Search one repo to find similar issues
5. **Privacy by default**: Hub private → all agent issues private
6. **Metrics visibility**: Total open issues, severity distribution, SLA tracking

### Negative

1. **Hub issue inflation**: Hub repo shows many issues (looks busy)
2. **Unconventional practice**: Issues not in same repo as code (may confuse new contributors)
3. **Hub dependency**: If hub repo unavailable, all agents can't file issues

### Neutral

1. **Human-filed issues separate**: Humans still file to agent-specific repos (e.g., template-worker-aget issues)
2. **Two issue sources**: Must check both hub (agent-filed) and agent repos (human-filed) for complete view
3. **Permissions required**: Agents need write access to hub repo

## Mitigation Strategies

**For "hub issue inflation"**:
- Add README badge explaining centralized triage
- Use labels to distinguish agent-filed from hub-specific issues

**For "unconventional practice"**:
- Document rationale in AGENTS.md and D001
- Explain "work assignments for agents" mental model

**For "hub dependency"**:
- Fallback: File issues locally in agent repo, migrate to hub when available
- Monitor hub availability, alert if unreachable

**For "two issue sources"**:
- Helper script: `./scripts/review_all_issues.sh` (checks both hub and template repos)
- Dashboard shows: "Agent-filed: X issues (hub), Human-filed: Y issues (template)"

## Alternatives Rejected

**Why not distributed (Option A)**:
- Cross-agent visibility is non-negotiable
- Centralized triage saves hours per week
- Privacy control is simpler with single hub repo

**Why not hybrid (Option C)**:
- Routing ambiguity creates friction
- Still fragments triage (must query multiple repos)
- Complexity not justified by benefits

## Review Criteria

**This decision should be revisited if**:
1. Fleet grows beyond 20 agents (scalability concern)
2. Hub repo becomes public (privacy model changes)
3. Cross-repo issue linking improves significantly in GitHub (technical landscape change)
4. Supervisor role changes (no longer centralized triage)

**Metrics to monitor**:
- Time spent on triage (should decrease with centralization)
- Duplicate issues filed (should decrease with visibility)
- Agent satisfaction with issue workflow (survey quarterly)

## References

- Implementation: `.aget/patterns/github/` (create_issue.py, list_issues.py, assign_issue.py)
- Protocol: `.aget/docs/ISSUE_ACTION_PROTOCOL_v1.0.md`
- Configuration: `AGENTS.md:320-450` (Issue Management section)
- Related: L099_multi_agent_process_enforcement.md (supervision patterns)

---

**Status**: Implemented (2025-10-06)
**Last Reviewed**: 2025-10-06
**Next Review**: After 3 months of operation or when fleet reaches 20 agents
