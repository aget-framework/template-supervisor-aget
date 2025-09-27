# Decision: AGET Naming Convention Standardization

**Type**: Decision (DEC)
**Date**: 2025-09-25
**Status**: Accepted

## Decision

Establish official naming conventions for the AGET ecosystem:
- `aget` → The concept/framework/philosophy
- `aget-template` → Public implementation (short for aget-cli-agent-template)
- `aget-aget` → Governance/strategic layer
- `X-aget` → Instance pattern (DeepResearch-aget, spotify-aget)

## Context

During governance structure establishment, recognized the need for clear, consistent naming that:
1. Reduces verbosity (aget-template vs aget-cli-agent-template)
2. Clarifies entity relationships
3. Enables natural conversation
4. Establishes instance patterns

## Rationale

The naming reflects a beautiful ambiguity where "AGET" simultaneously represents:
- The philosophical framework
- The implementation template
- The cognitive agent experience
- Specific instance deployments

This multi-faceted identity is intentional and valuable.

## Consequences

### Positive
- Clearer communication in documentation
- Natural conversational flow
- Obvious instance naming pattern
- Reduced typing/verbosity

### Neutral
- Need to update documentation for consistency
- May need clarification for newcomers initially

### Implications
- All future instances should follow X-aget pattern
- Documentation should use short names conversationally
- Formal references can retain full names

## Implementation

Created `governance/NAMING_CONVENTIONS.md` documenting:
- Official entity definitions
- Usage guidelines
- Code examples
- Anti-patterns to avoid

## References
- governance/NAMING_CONVENTIONS.md
- Original discussion in aget-aget session 2025-09-25