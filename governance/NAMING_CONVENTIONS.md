# AGET Naming Conventions

## Official Entity Space

The AGET ecosystem uses a clear, hierarchical naming convention that reflects the relationship between concept, implementation, governance, and instances.

### Core Entities

```
aget           → The concept/framework/philosophy
aget-template  → Public implementation (short for aget-cli-agent-template)
aget-aget      → Governance/strategic layer
X-aget         → Instance pattern (DeepResearch-aget, spotify-aget)
```

## Detailed Definitions

### `aget` - The Concept
- **What it is**: The philosophical framework and cognitive augmentation concept
- **Usage**: When discussing AGET as an idea, methodology, or approach
- **Examples**:
  - "AGET provides cognitive augmentation"
  - "The AGET philosophy enables AI collaboration"
  - "I'm using AGET methodology"

### `aget-template` - The Public Implementation
- **Full name**: aget-cli-agent-template
- **Short name**: aget-template (preferred in conversation)
- **What it is**: The canonical, stable, public implementation
- **Repository**: https://github.com/aget-framework/aget
- **Usage**: When referring to the source repository or public framework
- **Examples**:
  - "Fork aget-template to get started"
  - "The latest aget-template release includes..."
  - "Submit PRs to aget-template"

### `aget-aget` - The Governance Layer
- **What it is**: The strategic governance and experimental laboratory
- **Repository**: https://github.com/aget-framework/aget
- **Purpose**: Vision, strategy, experiments, pattern validation
- **Usage**: When discussing strategic decisions or experimental features
- **Examples**:
  - "That vision discussion belongs in aget-aget"
  - "Experimental patterns live in aget-aget first"
  - "Check aget-aget for strategic roadmap"

### `X-aget` - Instance Pattern
- **Pattern**: `[domain]-aget` or `[project]-aget`
- **What it is**: A specific AGET instance for a particular domain or project
- **IMPORTANT**: Preserve the original project name exactly as it exists
  - If the base project uses underscores, keep them
  - We append `-aget` but don't modify the base name
- **Examples**:
  - `OpenAI_DeepResearch-aget` - Research augmentation (base uses underscore)
  - `spotify-aget` - Music data analysis
  - `DatGen-aget` - Project governance
  - `kubernetes-aget` - Contributor workspace

## Usage Guidelines

### In Documentation
- **Formal contexts**: Use full names (aget-cli-agent-template)
- **Conversational**: Use short names (aget-template)
- **Concepts**: Just "AGET"

### In Code
```python
# Repository references
TEMPLATE_REPO = "aget-cli-agent-template"  # Full name for clarity
GOVERNANCE_REPO = "aget-aget"

# Instance naming
instance_name = f"{project_name}-aget"  # Always suffix pattern
```

### In Conversation
- "I forked **aget-template** for my project" ✅
- "The **AGET** philosophy transformed my workflow" ✅
- "Check **aget-aget** for experimental features" ✅
- "I created **spotify-aget** for music analysis" ✅

## Anti-patterns to Avoid
- ❌ "aget-cli-agent" (incomplete)
- ❌ "AGET-template" (wrong capitalization)
- ❌ "aget_aget" (use hyphens, not underscores)
- ❌ "aget-spotify" (instance name should end with -aget)

## The Hierarchy

```
        AGET (concept)
             |
    aget-aget (governance)
             |
    aget-template (implementation)
             |
    [Your Instance]-aget (customization)
```

## Decision Rationale

This naming convention:
1. **Clarifies relationships** between concept, implementation, and instances
2. **Reduces verbosity** while maintaining clarity
3. **Enables natural conversation** about the ecosystem
4. **Establishes clear patterns** for new instances

---

## Related Specifications

- **File Naming**: For file and artifact naming conventions, see [AGET_FILE_NAMING_CONVENTIONS.md](../../aget/specs/AGET_FILE_NAMING_CONVENTIONS.md)
- **Controlled Vocabulary**: For AGET terminology, see [AGET_CONTROLLED_VOCABULARY.md](../../aget/specs/AGET_CONTROLLED_VOCABULARY.md)

---
*Naming convention established: 2025-09-25*
*Updated: 2025-12-20 (added file naming reference)*
*This is an official governance decision from aget-aget*