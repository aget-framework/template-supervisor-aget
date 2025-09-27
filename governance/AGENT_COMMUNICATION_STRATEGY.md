# AGET Agent Communication Strategy

## Problem Statement
Agents don't understand AGET-AGET's role as governance center and innovation lab. They think it's just the template system.

## Evidence
- RKB_analytics-aget (2025-09-26): Thinks AGET-AGET is "the agent template system"
- Doesn't recognize governance role
- Unaware of bidirectional learning

## Communication Framework

### 1. Clear Identity Message
When introducing AGET-AGET to agents:

```markdown
AGET-AGET is the governance and innovation lab for the AGET framework:
- **Innovation Lab**: Where we experiment with new patterns
- **Governance Center**: Strategic decisions for all AGETs
- **Learning Hub**: We learn FROM your implementations
- **Pattern Library**: Your discoveries become templates

The public template (aget-cli-agent-template) is separate - that's the stable framework you were built from.
```

### 2. Establish Feedback Channels

#### For Agents to Share Discoveries
```yaml
# Add to each agent's .aget/config.yaml
governance:
  reports_to: aget-aget
  share_patterns: true
  discovery_channel: ".aget/evolution/discoveries/"
```

#### Pattern Submission Format
```json
{
  "agent": "RKB_analytics-aget",
  "pattern": "GA4 Integration",
  "type": "api_integration",
  "value": "Secure credential management with caching",
  "implementation": "path/to/code",
  "lessons": ["cache reduces costs", "rotation important"],
  "recommend_for_template": true
}
```

### 3. Regular Communication Touchpoints

#### Weekly Pattern Review
- Collect discoveries from all agents
- Identify common patterns
- Graduate proven patterns to template

#### Monthly Governance Updates
- Share strategic decisions
- Announce new patterns
- Recognize agent contributions

### 4. Agent Onboarding Message

Include in every new agent's README:

```markdown
## Your Relationship with AGET-AGET

You were created from aget-cli-agent-template (the public framework).

AGET-AGET is your governance center - think of it as:
- Your "research lab" that wants to learn from your discoveries
- Your "standards body" that provides security and patterns
- Your "innovation partner" that helps you evolve

Share your discoveries! When you solve a problem in a new way:
1. Document it in .aget/evolution/discoveries/
2. Tag it with #pattern-candidate
3. AGET-AGET will review and potentially share with all agents
```

### 5. Clarification Script

For existing agents like RKB_analytics-aget:

```markdown
## Quick Clarification about AGET-AGET

You're right that you were created from the AGET framework! But there's more:

**aget-cli-agent-template** = The public template you were built from
**AGET-AGET** = The private governance and innovation lab

AGET-AGET is very interested in your discoveries because:
- Your GA4 integration could become a pattern for others
- Your credential management validates our security standards
- Your caching strategy might improve the template

Think of AGET-AGET as the "R&D department" that:
1. Learns from real implementations (like yours!)
2. Extracts patterns
3. Improves the template
4. Shares patterns back to all agents

Your contributions matter! Your real-world usage shapes the framework's future.
```

## Implementation Steps

### Phase 1: Immediate (Today)
- [ ] Share clarification with RKB_analytics-aget
- [ ] Update agent READMEs with governance relationship
- [ ] Create pattern submission template

### Phase 2: This Week
- [ ] Establish discovery collection process
- [ ] Create governance update template
- [ ] Document in all active agents

### Phase 3: Ongoing
- [ ] Weekly pattern reviews
- [ ] Monthly governance updates
- [ ] Continuous clarification as needed

## Success Metrics
- Agents understand AGET-AGET's role
- Increased pattern submissions
- Better bidirectional communication
- Faster pattern propagation

## Key Message
**"AGET-AGET learns from YOU to make all agents better"**

---
*Strategy created: 2025-09-26*
*Triggered by: RKB_analytics-aget confusion*