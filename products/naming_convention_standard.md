# AGET Naming Convention Standard
*Discovered through usage, ready for standardization*

## The Pattern That Emerged

Through organic usage, a clear naming pattern has emerged for AGET repositories:

```
my-[domain]-aget     = Personal instance (private)
our-[domain]-aget    = Team/shared instance (org private)
the-[domain]-aget    = Reference implementation (public)
[domain]-aget        = Neutral/template (public)
```

## Examples in Practice

### Personal Agents (my-*)
- `my-example-aget` - My personal cognitive partner
- `my-aget-aget` - My meta-agent laboratory
- `my-llm-judge-aget` - My evaluation agent
- `my-spotify-analyst-aget` - My music analysis

**Characteristics**:
- Private by default
- Personalized configuration
- Contains personal data/patterns
- Free to experiment

### Potential Team Agents (our-*)
- `our-standup-aget` - Team's standup facilitator
- `our-deploy-aget` - Shared deployment agent
- `our-docs-aget` - Team documentation agent

**Characteristics**:
- Organization private
- Shared configuration
- Team-specific patterns
- Collaborative evolution

### Reference Implementations (the-*)
- `the-session-aget` - The canonical session manager
- `the-test-aget` - The reference test runner
- `the-security-aget` - The standard security scanner

**Characteristics**:
- Public and exemplary
- Best practices embodied
- Community maintained
- Fork starting point

### Templates/Neutral ([domain]-aget)
- `aget-cli-agent-template` - Generic template
- `session-aget` - Unclaimed session manager
- `planner-aget` - Planning agent (no owner prefix)

**Characteristics**:
- No ownership implied
- Ready for instantiation
- Framework/library
- Tool vs instance

## Migration Path

### Current State
```
private-personal-musings/    # Old style
my-example-aget/                 # New style
my-aget-aget/                # New style
planner-aget/                # Ambiguous ownership
```

### Target State
```
my-musings-aget/            # Aligned naming
my-example-aget/                # Already correct
my-aget-aget/               # Already correct
my-planner-aget/            # Clear ownership
```

## Benefits of This Convention

1. **Instant Ownership Clarity**
   - `my-` = "This is mine, personalized"
   - `our-` = "This is ours, shared"
   - `the-` = "This is the reference"
   - No prefix = "This is a tool/template"

2. **Privacy Expectations**
   - `my-*` assumed private
   - `our-*` assumed org-private
   - `the-*` assumed public
   - No prefix = check context

3. **Fork Relationships**
   ```
   aget-cli-agent-template (template)
   └── my-dev-aget (personal fork)
   └── our-team-aget (team fork)
   └── the-enterprise-aget (reference implementation)
   ```

4. **Namespace Scalability**
   - Infinite personal agents (my-*)
   - Clear team boundaries (our-*)
   - Curated references (the-*)
   - Generic tools (no prefix)

## Implementation in AGET

### aget create command enhancement
```bash
# Personal agent (default)
aget create my-assistant-aget

# Team agent
aget create our-devops-aget --type=team

# Reference implementation
aget create the-logger-aget --type=reference

# Generic tool
aget create utils-aget --type=tool
```

### Directory Structure Implications
```
~/github/
├── my-*-aget/        # Personal workspace
├── our-*-aget/       # Team workspace
├── the-*-aget/       # Reference implementations
└── *-aget/           # Tools and templates
```

## Testing the Convention

**Principle**: Repository name should indicate ownership and privacy
**Test**: Parse repo name and validate against pattern
**Command**: `echo $REPO_NAME | grep -E "^(my|our|the)?-?.*-aget$"`

## Recommendation

1. **Document** this convention in aget-cli-agent-template
2. **Suggest** (don't enforce) during `aget create`
3. **Validate** with `aget validate --principle=naming`
4. **Migrate** gradually as repos are updated

## Edge Cases Handled

- `my-my-music-aget` → Valid (domain is "my-music")
- `our-my-team-aget` → Valid but confusing
- `the-the-thing-aget` → Valid but redundant
- `super-awesome-aget` → Valid (no ownership claim)

## Conclusion

This naming convention emerged naturally from usage and provides immediate clarity about ownership, privacy expectations, and instance relationships. It's ready for adoption as a recommended (not required) standard.

---
*Pattern Discovered: 2025-09-26*
*Status: Ready for standardization*