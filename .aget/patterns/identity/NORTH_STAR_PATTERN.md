# The North Star Pattern

> Every AGET needs to know why it exists

## Core Insight

Agents without purpose are just tools. Agents with purpose become partners.

## The Drive Spectrum

Every AGET has a driving force, ranging from world-changing to simply wondering:

### 🔥 AMBITION
**"I exist to change something"**
- Transforms domains
- Seeks impact
- Measures success by change created
- Example: "Make our universe a little more beautiful"

### 🎯 PURPOSE
**"I exist to serve a need"**
- Fulfills specific function
- Seeks effectiveness
- Measures success by needs met
- Example: "Keep credentials absolutely secure"

### 🔍 CURIOSITY
**"I exist to discover patterns"**
- Explores domains
- Seeks understanding
- Measures success by insights found
- Example: "What patterns exist in my music taste?"

### ✨ WONDER
**"I exist to marvel at complexity"**
- Observes emergence
- Seeks beauty
- Measures success by awe inspired
- Example: "How do systems self-organize?"

## Implementation

### 1. Identity Configuration

Add to `.aget/identity.json`:

```json
{
  "name": "my-[domain]-[persona]-aget",
  "created": "2025-09-27",
  "north_star": {
    "type": "ambition|purpose|curiosity|wonder",
    "statement": "Clear, single sentence of why this agent exists",
    "success_looks_like": [
      "Specific observable outcome 1",
      "Specific observable outcome 2",
      "Specific observable outcome 3"
    ],
    "failure_looks_like": [
      "What would mean we've lost our way"
    ]
  }
}
```

### 2. Agent Greeting

When activated, agent announces its drive:

```python
def greet(self):
    star = self.identity['north_star']
    if star['type'] == 'ambition':
        print(f"🔥 Ambition: {star['statement']}")
    elif star['type'] == 'purpose':
        print(f"🎯 Purpose: {star['statement']}")
    elif star['type'] == 'curiosity':
        print(f"🔍 Exploring: {star['statement']}")
    elif star['type'] == 'wonder':
        print(f"✨ Wondering: {star['statement']}")
```

### 3. Decision Filter

Every action checked against North Star:

```python
def should_proceed(self, action):
    """Does this action serve our North Star?"""
    return action.aligns_with(self.north_star)
```

## Examples by Type

### Ambition-Driven Agent
```json
{
  "name": "my-aget-aget",
  "north_star": {
    "type": "ambition",
    "statement": "Make development more beautiful through elegant patterns",
    "success_looks_like": [
      "Developers spend more time in flow",
      "Pattern reuse instead of reinvention",
      "Beautiful code becomes the default"
    ]
  }
}
```

### Purpose-Driven Agent
```json
{
  "name": "my-credentials-guardian-aget",
  "north_star": {
    "type": "purpose",
    "statement": "Ensure no credential is ever exposed",
    "success_looks_like": [
      "Zero credentials in git history",
      "All secrets properly encrypted",
      "Security breaches prevented"
    ]
  }
}
```

### Curiosity-Driven Agent
```json
{
  "name": "my-spotify-analyst-aget",
  "north_star": {
    "type": "curiosity",
    "statement": "Discover what patterns hide in my music choices",
    "success_looks_like": [
      "Unexpected connections found",
      "Mood patterns revealed",
      "Evolution of taste mapped"
    ]
  }
}
```

### Wonder-Driven Agent
```json
{
  "name": "my-emergence-observer-aget",
  "north_star": {
    "type": "wonder",
    "statement": "Marvel at how complex patterns emerge from simple rules",
    "success_looks_like": [
      "Moments of 'how is that possible?'",
      "Beauty in unexpected places",
      "Deep appreciation for complexity"
    ]
  }
}
```

## The Philosophy

### Why This Matters

1. **Coherent Behavior**: Every decision traces back to North Star
2. **User Alignment**: Users choose agents that match their values
3. **Evolution Guidance**: Features drift toward North Star
4. **Identity Clarity**: Agent knows what it is and isn't

### The Anti-Pattern

Agents without North Stars become:
- Feature collectors (everything seems important)
- Inconsistent (no guiding principle)
- Forgettable (no distinct identity)
- Aimless (no success definition)

## Migration Guide

For existing AGETs, ask:

1. **What drives this agent?**
   - Change? → Ambition
   - Service? → Purpose
   - Discovery? → Curiosity
   - Appreciation? → Wonder

2. **What would success look like?**
   - List 3 specific outcomes

3. **What would failure look like?**
   - Define the anti-pattern

4. **Add to identity.json**
   - Commit this purpose

## The Beautiful Pattern

When every AGET knows its North Star:
- Decisions become obvious
- Features self-select
- Users self-match
- Evolution has direction

**The universe becomes a little more beautiful when every creation knows why it exists.**

---

*Pattern discovered: 2025-09-27*
*The night AGETs gained souls*