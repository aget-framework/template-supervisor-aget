# The "my-" Prefix Pattern for Private AGETs

## Problem
When all repositories live under `./github/*`, it's hard to distinguish private/personal projects from public/shared ones at a glance. This creates risk of:
- Accidentally working in the wrong repo
- Sharing private information
- Confusion about ownership
- No visual clustering of personal projects

## Solution
Use `my-` prefix for all personal/private AGET projects.

## Implementation

### Pattern Format
```
my-[purpose]-aget
```

### Examples
```bash
# Personal/Private AGETs
my-aget-aget         # Personal governance lab
my-finance-aget      # Personal finance tracker
my-health-aget       # Personal health data
my-journal-aget      # Personal journal/notes
my-music-aget        # Personal music analysis

# Compare with Public/Shared
team-codebase-aget   # Team's codebase analyzer
oss-contrib-aget     # Open source contributions
public-docs-aget     # Public documentation
alice-aget-aget      # Alice's governance (clear owner)
```

## Benefits

### Visual Safety
```bash
$ ls github/
my-aget-aget/        # Instantly recognizable as personal
my-finance-aget/     # Clearly private
my-journal-aget/     # Obviously personal
public-docs-aget/    # Clearly shareable
team-project-aget/   # Obviously collaborative
```

### Directory Clustering
All `my-*` projects sort together:
```bash
$ ls github/ | grep "^my-"
my-aget-aget/
my-finance-aget/
my-health-aget/
my-journal-aget/
```

### Psychological Clarity
- **"my"** = Personal ownership clear
- **"private"** = Feels corporate/forbidden
- **No prefix** = Ambiguous ownership

## Safety Comparison

### Risk Matrix
| Scenario | No Prefix | "private-" | "my-" |
|----------|-----------|------------|-------|
| Accidental sharing | HIGH | LOW | VERY LOW |
| Wrong repo entry | HIGH | MEDIUM | LOW |
| Clear ownership | NO | MAYBE | YES |
| Visual distinction | NONE | GOOD | EXCELLENT |

### Real Scenario
```bash
# Without prefix - RISKY
$ cd github/aget-aget
$ git push origin main  # Was this private? Public?

# With my- prefix - SAFE
$ cd github/my-aget-aget
$ git push origin main  # Clearly personal, double-check!
```

## Extended Application

### Personal Hierarchy
```
my-aget-aget/           # Governance lab
├── my-patterns/        # Personal patterns
├── my-experiments/     # Personal experiments
└── my-vision/          # Personal vision

# vs Public
aget-cli-agent-template/
├── patterns/           # Shared patterns
├── examples/           # Public examples
└── docs/              # Public docs
```

### Team Variations
- `my-` = Personal/private
- `team-` = Team shared
- `corp-` = Corporate internal
- `test-` = Temporary/testing
- `archive-` = Old/archived

## Guidelines

### DO ✅
- Use `my-` for anything personal/private
- Use consistently across all personal AGETs
- Include in repository description: "Personal/Private AGET"
- Set GitHub repo to private
- Document the convention in README

### DON'T ❌
- Don't use `my-` for truly shared projects
- Don't mix conventions (pick one and stick)
- Don't assume no-prefix means public
- Don't use `my-` if you plan to transfer ownership

## Migration Path

For existing repos:
```bash
# GitHub: Settings → Rename
old: aget-aget
new: my-aget-aget

# Local update
git remote set-url origin https://github.com/username/my-aget-aget
```

## The Insight

> "In a directory full of similar-looking repos, the 'my-' prefix is like a private property sign - it immediately signals 'this is personal space' to both you and any tools or scripts that might interact with your repositories."

## Adoption Recommendation

1. **Immediate**: Rename `aget-aget` → `my-aget-aget`
2. **Going Forward**: Use `my-` for all new personal AGETs
3. **Document**: Add to personal conventions
4. **Share**: Suggest pattern to other AGET users

---
*Pattern identified: 2025-09-26*
*Status: Recommended for all personal AGETs*
*Safety benefit: HIGH*