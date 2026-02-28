# Traceability Matrix

**Version**: 1.0.0
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Template**: template-supervisor-aget

---

## Purpose

Bidirectional traceability between requirements, specifications, tests, and implementation artifacts. Enables verification that every requirement is tested and every test validates a requirement.

---

## Template Spec Compliance (CAP-TPL)

| Requirement | Description | Test | Status |
|-------------|-------------|------|--------|
| CAP-TPL-001 | .aget/ directory structure | test_directory_structure::test_core_directories_exist, test_aget_subdirectories_exist | PASS |
| CAP-TPL-002 | version.json with required fields | test_directory_structure::test_version_json_exists, test_identity_contract::test_identity_consistency, test_wake_contract::test_wake_protocol_reports_version | PASS |
| CAP-TPL-003 | identity.json with north_star | test_identity_contract::test_identity_no_conflation, test_identity_persistence | PASS |
| CAP-TPL-004 | AGENTS.md with session protocols | test_directory_structure::test_agents_md_exists, test_claude_md_symlink, test_configuration_size::test_agents_md_size_limit | PASS |
| CAP-TPL-005 | governance/ with charter + mission | test_directory_structure::test_core_directories_exist (implicit) | PASS |
| CAP-TPL-006 | specs/ with at least 1 spec | File existence (18 skill specs + Supervisor_SPEC.md) | PASS |
| CAP-TPL-007 | tests/ with passing contract tests | pytest (29 tests passing) | PASS |
| CAP-TPL-008 | .claude/skills/ with wake-up + wind-down | File existence (20 skills) | PASS |
| CAP-TPL-009 | sessions/ directory exists | File existence | PASS |
| CAP-TPL-010 | sops/ with at least 1 SOP | File existence | PASS |
| CAP-TPL-011 | ontology/ with SKOS-compliant vocabulary | File existence (ONTOLOGY_supervisor.yaml) | PASS |
| CAP-TPL-012 | README.md with version badge | File existence + content check | PASS |

**Score: 12/12 PASS**

---

## Supervisor Spec Compliance (CAP-SUP, INV)

| Requirement | Description | Test | Status |
|-------------|-------------|------|--------|
| CAP-SUP-001 | Fleet oversight | test_supervisor_role::test_supervisor_domain, test_portfolio_field | PASS |
| CAP-SUP-002 | Work distribution | test_supervisor_role::test_supervisor_coordination_directory | PASS |
| CAP-SUP-003 | Quality assurance | test_supervisor_role::test_supervisor_patterns_documented | PASS |
| INV-CORE-001 | Agent shall not act outside scope | Governance (AGENTS.md scope boundaries) | PASS |
| INV-CORE-002 | Session continuity protocols | test_wake_contract (4 tests) | PASS |
| INV-CORE-003 | Substantial change protocol | Governance (AGENTS.md documents protocol) | PASS |
| INV-SUP-001 | Shall not execute delegatable work | test_supervisor_role::test_supervisor_patterns_documented | PASS |
| INV-SUP-002 | Shall not bypass escalation | test_supervisor_role::test_supervisor_patterns_documented | PASS |

**Score: 8/8 PASS**

---

## Skill Spec Coverage

| Spec ID | Skill | Capabilities | Test Cases | Constraints | Status |
|---------|-------|-------------|------------|-------------|--------|
| SKILL-001 | aget-wake-up | R-WU-001..007 (7) | T-WU-001..004 (4) | C-WU-001..002 (2) | Specified |
| SKILL-002 | aget-wind-down | R-WD-001..007 (7) | T-WD-001..003 (3) | C-WD-001..002 (2) | Specified |
| SKILL-003 | aget-check-health | R-SC-001..007 (7) | T-SC-001..003 (3) | C-SC-001..002 (2) | Specified |
| SKILL-004 | aget-check-evolution | R-HE-001..007 (7) | T-HE-001..003 (3) | C-HE-001..002 (2) | Specified |
| SKILL-005 | aget-check-sessions | R-HS-001..007 (7) | T-HS-001..003 (3) | C-HS-001..002 (2) | Specified |
| SKILL-006 | aget-check-kb | R-HK-001..008 (8) | T-HK-001..003 (3) | C-HK-001..002 (2) | Specified |
| SKILL-007 | aget-record-lesson | R-RL-001..006 (6) | T-RL-001..003 (3) | C-RL-001..003 (3) | Specified |
| SKILL-008 | aget-capture-observation | R-CO-001..006 (6) | T-CO-001..003 (3) | C-CO-001..003 (3) | Specified |
| SKILL-009 | aget-propose-skill | R-PS-001..007 (7) | T-PS-001..003 (3) | C-PS-001..002 (2) | Specified |
| SKILL-010 | aget-review-project | R-RP-001..007 (7) | T-RP-001..003 (3) | C-RP-001..003 (3) | Specified |
| SKILL-011 | aget-create-project | R-CP-001..007 (7) | T-CP-001..003 (3) | C-CP-001..004 (4) | Specified |
| SKILL-012 | aget-create-skill | R-CS-001..006 (6) | T-CS-001..003 (3) | C-CS-001..002 (2) | Specified |
| SKILL-013 | aget-save-state | R-SS-001..007 (7) | T-SS-001..003 (3) | C-SS-001..003 (3) | Specified |
| SKILL-014 | aget-broadcast-fleet | R-BF-001..005 (5) | T-BF-001..003 (3) | C-BF-001..003 (3) | Specified |
| SKILL-015 | aget-escalate-issue | R-EI-001..005 (5) | T-EI-001..003 (3) | C-EI-001..003 (3) | Specified |
| SKILL-016 | aget-file-issue | R-FI-001..006 (6) | T-FI-001..003 (3) | C-FI-001..006 (6) | Specified |
| SKILL-017 | aget-review-agent | R-RA-001..005 (5) | T-RA-001..003 (3) | C-RA-001..003 (3) | Specified |
| SKILL-018 | aget-study-up | R-SU-001..006 (6) | T-SU-001..003 (3) | C-SU-001..003 (3) | Specified |

**Coverage: 18/18 skills specified (100%)**
**Total: 116 capabilities, 56 test cases, 48 constraints = 220 requirement artifacts**

---

## Contract Test → Spec Mapping

| Test File | Tests | Spec References |
|-----------|-------|-----------------|
| test_basic_setup.py | 7 | Infrastructure (no spec mapping) |
| test_configuration_size.py | 3 | CAP-TPL-004, L146 |
| test_directory_structure.py | 5 | CAP-TPL-001, CAP-TPL-002, CAP-TPL-004 |
| test_identity_contract.py | 3 | CAP-TPL-002, CAP-TPL-003 |
| test_portfolio_field.py | 3 | CAP-TPL-002, CAP-SUP-001 |
| test_supervisor_role.py | 4 | CAP-SUP-001, CAP-SUP-002, INV-SUP-001, INV-SUP-002, L99, L099 |
| test_wake_contract.py | 4 | R-WU-001, CAP-TPL-002, CAP-TPL-003 |

**Total: 29 contract tests, 22 with spec references (76%)**
**Unmapped: 7 infrastructure tests (test_basic_setup.py) — intentionally unmapped**

---

## Coverage Gaps

| Gap | Impact | Remediation |
|-----|--------|-------------|
| Skill spec test cases (T-*) are manual, not automated | V-tests require human execution | Future: automate subset per PROCO-2026-061 pattern |
| No automated test for CAP-TPL-005 (governance/) | Implicit via directory check | Low priority: stable structure |
| No automated test for CAP-TPL-008 (skills/) | Implicit via wake-up | Low priority: verified by wake-up count |

---

*TRACEABILITY_MATRIX.md v1.0.0*
*18 skill specs, 220 requirement artifacts, 29 contract tests*
*"Every requirement traced, every test grounded"*
