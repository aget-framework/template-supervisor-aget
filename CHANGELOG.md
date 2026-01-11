# Changelog

All notable changes to AGET will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.3.0] - 2026-01-11 - "Framework Alignment"

### Changed
- Updated to AGET framework v3.3.0
- Aligned with Shell Integration + Executable Knowledge Ontology release

### Notes
- See aget/CHANGELOG.md for framework changes
- L517 remediation: Template_Abandonment closure

---


## [3.2.1] - 2026-01-04 - "Version Inventory Coherence"

### Fixed
- **Version Consistency**: AGENTS.md, manifest.yaml, version.json now all show v3.2.1
- Part of L444 remediation (version inventory coherence)

### Notes
- Patch release to fix version inconsistencies from v3.2.0
- See aget-framework/aget CHANGELOG [3.2.1] for details

---

## [3.2.0] - 2026-01-04 - "Specification Architecture"

### Added
- Version sync with aget core v3.2.0

### Changed
- Version references updated across all files

### Notes
- Part of AGET v3.2.0 "Specification Architecture" coordinated release
- See aget-framework/aget CHANGELOG for full framework changes:
  - 7 new specifications
  - Naming conventions expanded (4 → 10 categories)
  - 6 new validators
  - INDEX.md + REQUIREMENTS_MATRIX.md

---

## [3.1.0] - 2026-01-04 - "Session Protocol Enhancements"

### Added
- **Complete Session Lifecycle Scripts**:
  - `wake_up.py`: Session initialization (R-WAKE-001 to R-WAKE-007)
  - `aget_housekeeping_protocol.py`: Mid-session sanity checks (R-SANITY-001 to R-SANITY-007)
  - `wind_down.py`: Session close with sanity gate (R-WIND-001 to R-WIND-006)
- **Cross-CLI Automation**: All scripts support `--json` output for Claude Code, Codex, Cursor

### Changed
- Version references updated across all files (manifest.yaml, identity.json, AGENTS.md)
- Scripts implement L038 (Agent-Agnostic) and L021 (Verify-Before-Modify)
- Pattern versions: session 1.2.0, housekeeping 1.1.0

### Notes
- Part of AGET v3.1.0 coordinated release
- See aget-framework/aget CHANGELOG for full framework changes

---

## [3.0.0] - 2025-12-28 - "5D Composition Architecture"

### Added
- **5D Directory Structure**: Organized agent composition
  - `.aget/persona/` - Identity and behavioral characteristics
  - `.aget/memory/` - Session handoffs and persistent state
  - `.aget/reasoning/` - Decision frameworks and policies
  - `.aget/skills/` - Patterns, SOPs, and automation scripts
  - `.aget/context/` - Environmental and domain information
- **v3.0 Contract Tests**: Updated test suite with SKIP_TEMPLATE_V2 pattern

### Changed
- `template` field replaces `roles` array
- `instance_type` field: `template` for templates, `aget`/`AGET` for instances
- `archetype` field: high-level classification
- Manifest version: 3.0

### Migration
- See `docs/FLEET_MIGRATION_GUIDE.md` in aget-framework/aget

---

## [2.10.0] - 2025-12-13 - "Capability Composition Architecture"

### Added
- **Capability Composition Architecture compatibility**
  - Framework now supports `capabilities[]` array in version.json
  - Agents can compose multiple capabilities onto base templates
  - See L330 (Capability Composition Architecture) for details

- **Theoretical Grounding Protocol** (L332)
  - Specifications should include `theoretical_basis:` sections
  - Maps AGET concepts to established theory (BDI, Actor Model, Cybernetics)

### Changed
- Version bump for v2.10.0 framework alignment

### Coming in v2.11.0
- CAPABILITY_SPEC_v1.0.yaml (formal capability schema)
- TEMPLATE_MANIFEST_SPEC_v1.0.yaml (composition declaration)
- capability-domain-knowledge implementation
- capability-structured-outputs implementation

### Notes
- **No structural changes required** for v2.10.0 compatibility
- Templates remain valid bases for capability composition
- v2.10.0 = Architecture defined | v2.11.0 = Architecture implemented

## [2.8.0] - 2025-11-08 - "Planning & Infrastructure"

### Added
- **Planning Framework v1.0**:
  - Decision tree for choosing planning approach
  - 5 templates: Enhancement, Gate, Project, Checkpoint, Critique
  - Integration with L274 (OKR), L275 (Multi-Gate), L42 (Gate Discipline)

- **Enhancement Filing Protocol**:
  - Systematic protocol for filing framework improvements
  - 5-section structure (Problem, Context, Solution, Benefits, Estimate)
  - Generalizability criterion (3+ agents benefit)

- **GitHub Tooling Improvements**:
  - Interactive issue filing (`make issue`)
  - Type taxonomy error handling
  - --learning flag for automatic learning document creation

### Changed
- Feature 10: Framework artifact consolidation to .aget/docs/releases/
- Naming conventions: Prefix meanings (private-/public-/my-) formalized

### Documentation
- Planning Guide v1.0 (comprehensive planning decision support)
- Enhancement Filing Protocol v1.0
- Naming Prefix Convention v1.0
- Planning Protocol Examples (14 examples)
- Fleet coordination patterns (supervisor-specific)

### Compatibility
- Fully backward compatible with v2.7
- New planning templates optional (existing approaches still work)

## [2.7.0] - 2025-10-13 - "Portfolio Governance"

### Added
- **Portfolio Governance System**:
  - `.aget/portfolios/` directory for fleet portfolio manifests
  - Portfolio-aware supervision across organizational boundaries
  - Classification enforcement (very_personal, confidential, private, public)
  - Cross-portfolio coordination protocols

- **Organizational Memory Patterns**:
  - Fleet-wide learning discovery framework
  - Standardized session metadata (v1.0) for coordination
  - Cross-agent knowledge sharing and pattern deployment

- **Learning Discovery Framework**:
  - Systematic learning capture from multi-agent operations
  - Learning reference validation for fleet deployments
  - Pattern deployment tracking and versioning

### Changed
- Enhanced wake protocol with fleet portfolio awareness
- Updated identity protocol to include portfolio coordinator status
- Improved multi-agent session coordination

### Documentation
- Portfolio manifests guide for supervisors
- Learning document standard (v1.0) for fleet coordination
- Session metadata standard for supervisor operations

### Compatibility
- Backward compatible with v2.6
- New portfolio field optional for non-fleet supervisors
- Existing supervisor agents work without portfolio assignment

## [2.6.0] - 2025-10-11 - "Configuration Management"

### Added
- **Configuration Size Management**:
  - 40,000 character limit for AGENTS.md (L146)
  - Size monitoring for complex supervisor configurations
  - Content extraction strategies for fleet coordination configs

- **Framework Positioning**:
  - Clarified supervisor role in AGET ecosystem
  - Updated positioning documentation
  - Landscape analysis for multi-agent coordination

- **Contract Test Validation**:
  - Enhanced contract test suite for supervisor agents
  - Fleet coordination validation
  - Multi-agent operation compliance testing

### Documentation
- Configuration size management for supervisors
- Framework positioning analysis
- Supervisor-specific best practices

### Compatibility
- Fully backward compatible with v2.5
- No breaking changes to supervisor contracts

## [2.5.0] - 2025-10-06 - "Validation"

### Added
- **Supervisor Template Creation**:
  - Initial supervisor template for fleet coordination
  - Multi-agent orchestration capabilities
  - Fleet management protocols

- **Contract Testing Framework**:
  - Core contract tests for supervisor identity
  - Automated validation of supervisor configuration
  - Fleet coordination validation

- **Identity Protocol**:
  - Standardized agent_name field (must match directory)
  - Instance type: "AGET" (supervisors are action-taking)
  - Domain field for coordination specialization
  - Recursive supervision model support (L99)

- **Validation Framework**:
  - Version compliance checking
  - Configuration consistency validation
  - Deployment verification standards (L93)
  - Fleet state verification

### Documentation
- Supervisor template creation guide
- Contract test documentation
- Identity protocol standards for supervisors
- Multi-agent coordination patterns

### Compatibility
- New template (no backward compatibility concerns)
- v2.5.0 established as supervisor version floor
- All new supervisor agents must pass contract tests

---

*Supervisor template tracks versions from v2.5.0 onwards (template creation release)*
*For earlier framework history, see worker template CHANGELOG*
