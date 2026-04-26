# Changelog

All notable changes to AGET will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.15.0] - 2026-04-25

**Theme**: Aligned with framework v3.15.0 (Two-Level Model Coherence + Security Hardening)

### Changed

- Version bump: 3.14.0 → 3.15.0 (framework alignment)
- `AGENTS.md` `@aget-version` updated to 3.15.0

### Breaking

- **BC-001**: `.aget/version.json` old field names removed (e.g. `agent_name` → `aget_agent_name`). See `aget/docs/BREAKING_CHANGES_v3.15.md`.
- **BC-002**: `--fix` flag removed from `/aget-check-health` (SKILL-003). Use `/aget-enhance-health` instead.

---

## [3.14.0] - 2026-04-18

**Theme**: Aligned with framework v3.14.0 (v3.13 Loop Closure + Scope-Lock Discipline)

### Changed

- Version bump: 3.13.0 → 3.14.0 (framework alignment)
- `AGENTS.md` `@aget-version` updated to 3.14.0

### Notes

Per-template CHANGELOG entries for 3.12.0 and 3.13.0 were not individually maintained; template work in those cycles is captured in `aget-framework/aget/CHANGELOG.md`. Gap flagged for v3.14.x / v3.15 retrospective.

---

## [3.11.1] - 2026-04-04

### Changed

- Renamed `aget_housekeeping_protocol.py` → `health_check.py`
- Renamed `study_up.py` → `study_topic.py`
- Config key `skip_sanity` → `skip_health_check`

---
## [3.11.0] - 2026-03-28 - "Skill Conformance, Requirements & Hooks"

### Added

- **requirements/** directory scaffolded (L742 two-level model, #725)
- **.claude/hooks/** directory with README (ADR-008 Generator, #505)
- **governance_intensity** field in AGENTS.md (#732)

### Changed

- 17 skill SKILL.md files updated for L736 conformance (SICR, #678)
- "sanity check" → "health check" terminology (#658)
- RUBRIC.template.md v2.0 deployed

---

## [3.10.0] - 2026-03-21 - "Structural Enforcement"

### Added
- MUST-invoke directives for /aget-create-project and /aget-file-issue (D71)
- Gate Boundary Protocol: plan update + commit as structural proof of gate completion
- Skill Completion Signal pattern in /aget-create-project and /aget-enhance-spec
- SOP Phase -0.5: Content Sync governance (D69/GOV-040)
- SKILL_SPEC_TEMPLATE.yaml (#439)

### Changed
- Skill renames: aget-capture-observation → aget-record-observation, aget-capture-nugget → aget-record-nugget, aget-study-up → aget-study-topic (#480)
- `capture` verb retired from Learning family
- Gate Execution Discipline strengthened with MUST update + MUST commit

### Fixed
- Template hygiene: VERSION, classifier, SECURITY.md corrections (#574)

## [3.9.0] - 2026-03-15 - "Governance Enforcement"

### Added
- Gate 0: Spec Verification (MP-1) in project plan template
- Phase -1: Release Readiness governance in SOP

### Changed
- Version bump to v3.9.0 (5/5 artifact types)
- version_bump.py: extended to cover AGENTS.md, codemeta.json, CITATION.cff
- TEMPLATE_PROJECT_PLAN.md: mandatory Gate 0 added

### Fixed
- aget-enhance-spec: Phase 6 consistency (#418), phantom spec reference (#419)

 - 2026-03-08 - "Governance Maturation"

### Added
- AGENTS.md governance patterns: capability declarations, CLI feature adoption guidance
- `.claude/` scaffolding: settings.json, skills directory structure
- Skill: `aget-expand-ontology` v1.0.0 (optional, acquirable)
- Skill: `aget-enhance-spec` v1.1.0 (specification enhancement lifecycle)

### Changed
- Version bump to v3.8.0
- identity.json: `type` field added
- SOP headers: CAP-SOP-001 compliance
- Migration history entry added

### Notes
- See aget/CHANGELOG.md [3.8.0] for framework changes
- Part of Governance Maturation release (principle codification, deliverable conformance)

---

## [3.7.0] - 2026-03-05 - "Quality Reconciliation"

### Added
- AGENTS.md governance patterns backported (TEMPLATE_AGENTS_MD_SPEC v1.0.0)
- `.claude/` directory scaffolding for CLI feature adoption

### Changed
- Skill renames: `aget-studyup` → `aget-study-up`, `aget-healthcheck-*` → `aget-check-*`
- README positioning: evidence-based reframe, removed undemonstrated claims
- Version bump to v3.7.0
- Migration history entry added

### Notes
- See aget/CHANGELOG.md [3.7.0] for framework changes
- Part of Quality Reconciliation release (content integrity, SOP lifecycle, positioning reframe)

---

## [3.6.0] - 2026-02-21 - "Infrastructure Maturation"

### Added
- Universal skill: `aget-studyup` (focused KB research before implementation)
- Canonical script: `scripts/study_up.py`

### Changed
- Platform claims: "Claude Code, Codex CLI, Gemini CLI" (was "Claude Code, Cursor, Aider, Windsurf")
- Version bump to v3.6.0
- Migration history entry added

### Notes
- See aget/CHANGELOG.md [3.6.0] for framework changes
- Part of Infrastructure Maturation release (observability, content integrity, ontology)

---

## [3.5.0] - 2026-02-14 - "Archetype Customization"

### Added
- Archetype-specific skills: `aget-broadcast-fleet`, `aget-review-agent`, `aget-escalate-issue`
- Formal ontology: `ontology/ONTOLOGY_supervisor.yaml` (8 concepts, 3 clusters)
- Universal skill: `aget-file-issue` (14th universal)
- Evaluator-focused README narrative

### Changed
- SKILL_VOCABULARY.md v1.2.0 with SKOS reference
- README structure: "Why Supervisor?" value proposition

### Notes
- See aget/CHANGELOG.md [3.5.0] for framework changes
- Part of Archetype Customization release

---

## [3.4.0] - 2026-01-18 - "Session Skills Maturity"

### Added
- Session protocol enhancements (re-entrancy guard, calendar awareness)
- Template infrastructure: `sops/SOP_escalation.md`

### Changed
- Cross-CLI validation (Claude Code, Codex CLI, Gemini CLI)
- Governance formalization patterns

### Notes
- See aget/CHANGELOG.md [3.4.0] for framework changes

---

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
