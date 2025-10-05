# my-aget-aget: Personal AGET Pattern Laboratory

> **Private Repository** - My space for AGET experimentation
>
> One person's approach to pattern extraction and framework contribution

## What This Is

**my-aget-aget** is MY personal pattern laboratory for the AGET framework. This is where I manually extract patterns from my agents, experiment with enhancements, and validate before contributing to the public template.

This is not THE official AGET governance - it's just MY personal experimentation space. Anyone can create their own `*-aget-aget` laboratory!

## Purpose

Not everything needs to be public. my-aget-aget is where I:
- Test wild ideas that might break things
- Build personal tools that may stay personal
- Explore patterns that might graduate to the public template
- Learn from failures without public exposure

## Current Status

### Today's Discoveries (2025-09-26)
- ✅ X-aget independence principle (each repo must be self-contained)
- ✅ Testable principles framework ("if you can't test it, it's not a principle")
- ✅ `aget validate` command specification
- ✅ Naming convention standard (`my-`, `our-`, `the-` prefixes)
- ✅ Fixed dangerous cross-repository dependencies
- ✅ 4 new products ready for template graduation

### Active Focus
- Pattern extraction from real AGET usage
- Testing patterns across multiple agents
- Documenting lessons in evolution/
- Preparing contributions to public template

### Innovation Pipeline
```
Experiment (workspace/)
    → Validate (tests/)
    → Extract (products/)
    → Maybe contribute to AGET (selective)
    → Or keep private (perfectly valid)
```

## Structure

```
my-aget-aget/
├── workspace/        # Wild experiments happen here
├── products/         # Proven patterns ready for graduation
├── patterns/         # Discovered patterns from real usage
├── governance/      # Personal strategy and decisions
├── vision/          # Future possibilities and frameworks
├── sessions/        # Session documentation and learnings
├── .aget/           # AGET structure (yes, even this is an AGET!)
│   └── evolution/   # Learning from experiments
└── tests/           # Validation and testing
```

## Philosophy

1. **Freedom to Fail**: Not everything needs to work
2. **Private by Default**: Share only what adds value
3. **Learn Everything**: Failed experiments teach most
4. **Quality Gates**: Only proven patterns graduate

## Relationship to AGET

- **[aget-cli-agent-template](https://github.com/aget-framework/aget)**: Public framework for everyone
- **my-aget-aget**: My personal pattern laboratory and innovation space
- Some experiments → Graduate to public template
- Some experiments → Remain private tools
- All experiments → Learning captured in evolution/

See [PUBLIC_FRAMEWORK_POINTER.md](PUBLIC_FRAMEWORK_POINTER.md) for details on the contribution flow.

## What Lives Here

Examples of things that might stay private:
- Personal workflow optimizations
- Domain-specific patterns (like music analysis)
- Experimental features too wild for public
- Failed attempts that taught us something

Examples of things that might graduate:
- Proven patterns that help everyone
- Bug fixes discovered through experimentation
- Performance optimizations
- Universal workflow improvements

## Getting Started

```bash
# This is a private space for experimentation
# Wake up to start exploring
# Build freely in workspace/
# Track learnings in evolution/
```

## Status

- **Created**: 2025-09-25
- **Nature**: Private innovation lab
- **Contribution**: Selective, not mandatory
- **Value**: Learning > Publishing
- **Version Floor**: v2.5.0 (minimum version for all new agents as of 2025-10-04)

## Version Policy

**v2.5.0 as Floor** (Effective 2025-10-04):

All new agents created from this template must be at **v2.5.0 or higher**. This baseline includes:
- Contract testing framework (7 tests per agent)
- Identity protocol (agent_name, instance_type, domain fields)
- Deployment verification standards (L93)
- Gate 2.5 validation (identity field checks)

When creating a new agent from this template:
1. Copy the entire template structure
2. Update `.aget/version.json` to v2.5.0 or higher
3. Set identity fields (agent_name = directory name, instance_type, domain)
4. Copy contract tests to new agent
5. Run tests to validate before first commit

**Rationale**: Fleet-wide migration to v2.5.0 completed 2025-10-04. All agents now baseline at this version to ensure consistent validation and deployment practices.

---

*my-aget-aget: My personal AGET laboratory where patterns are discovered through real usage*