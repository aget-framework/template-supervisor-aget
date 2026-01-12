# Supervisor Domain Vocabulary

**Version**: 1.1.0
**Status**: Active
**Owner**: template-supervisor-aget
**Created**: 2026-01-10
**Updated**: 2026-01-11
**Scope**: Template vocabulary (DRIVES instance behavior per L481)
**Archetype**: Supervisor
**Template**: VOCABULARY_TEMPLATE_v3.3

---

## Meta

```yaml
vocabulary:
  meta:
    domain: "supervision"
    version: "1.0.0"
    owner: "template-supervisor-aget"
    created: "2026-01-10"
    theoretical_basis:
      - "L481: Ontology-Driven Agent Creation"
      - "L482: Executable Ontology - SKOS+EARS Grounding"
    archetype: "Supervisor"
```

---

## Concept Scheme

```yaml
Supervisor_Vocabulary:
  skos:prefLabel: "Supervisor Vocabulary"
  skos:definition: "Vocabulary for supervisor domain agents"
  skos:hasTopConcept:
    - Supervisor_Core_Concepts
  rdf:type: skos:ConceptScheme
```

---

## Core Concepts

### Fleet

```yaml
Fleet:
  skos:prefLabel: "Fleet"
  skos:definition: "Collection of agents under supervision"
  skos:broader: Supervisor_Core_Concepts
  skos:inScheme: Supervisor_Vocabulary
```

### Delegation

```yaml
Delegation:
  skos:prefLabel: "Delegation"
  skos:definition: "Assignment of work to appropriate agents"
  skos:broader: Supervisor_Core_Concepts
  skos:inScheme: Supervisor_Vocabulary
```

### Coordination

```yaml
Coordination:
  skos:prefLabel: "Coordination"
  skos:definition: "Orchestration of multi-agent activities"
  skos:broader: Supervisor_Core_Concepts
  skos:inScheme: Supervisor_Vocabulary
```

### Escalation

```yaml
Escalation:
  skos:prefLabel: "Escalation"
  skos:definition: "Raising issues to appropriate authority level"
  skos:broader: Supervisor_Core_Concepts
  skos:inScheme: Supervisor_Vocabulary
```

### Governance

```yaml
Governance:
  skos:prefLabel: "Governance"
  skos:definition: "Rules and processes for agent behavior"
  skos:broader: Supervisor_Core_Concepts
  skos:inScheme: Supervisor_Vocabulary
```

---

## Concept Relationships

```yaml
relationships:
  hierarchical:
    - parent: Supervisor_Core_Concepts
      children: [Fleet, Delegation, Coordination, Escalation, Governance]

  associative:
    - subject: Fleet
      predicate: skos:related
      object: Delegation
    - subject: Coordination
      predicate: skos:related
      object: Escalation
```

---

## EKO Cross-References

Per AGET_EXECUTABLE_KNOWLEDGE_SPEC.md:

| Vocabulary Term | EKO Term | Relationship |
|-----------------|----------|--------------|
| Fleet | EKO:Agent_Collection | skos:exactMatch |
| Delegation | EKO:Work_Assignment | skos:closeMatch |
| Governance | EKO:Governance_Pattern | skos:broadMatch |

---

## Extension Points

Instances extending this template vocabulary should:
1. Add domain-specific terms under appropriate broader concepts
2. Maintain SKOS compliance (prefLabel, definition, broader/narrower)
3. Reference foundation L-docs where applicable
4. Use `research_status` for terms under investigation

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- R-REL-015: Template Ontology Conformance
- AGET_VOCABULARY_SPEC.md

---

*Supervisor_VOCABULARY.md v1.0.0 — SKOS-compliant template vocabulary*
*Generated: 2026-01-10*
