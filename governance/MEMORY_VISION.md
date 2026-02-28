# Memory Architecture Vision

**Version**: 1.0.0
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Status**: Active
**Reference**: L335 (Memory Architecture Principles)

---

## Purpose

The knowledge base is the collaboration substrate that enables persistent, structured, shareable memory across sessions, agents, and humans. This document establishes the principles governing how supervisor agents build and maintain institutional knowledge.

---

## Core Principles

### 1. Every Session Leaves the KB Better

Each interaction should contribute to the knowledge base — whether through L-docs, observations, pattern recognition, or session handoff artifacts. Knowledge capture is not optional overhead; it is the primary mechanism for compounding value.

### 2. Context Recovery in Under 2 Minutes

Session initialization (wake-up) should restore essential context within 2 minutes. This requires well-structured artifacts, not scattered notes. Design for discoverability: consistent naming, clear cross-references, searchable content.

### 3. Memory as Shared Human-AI Artifact

The knowledge base belongs to the human-AI collaboration, not to either party alone. It should be:
- **Readable** by humans without tooling
- **Parseable** by agents for automated processing
- **Versionable** via git for change tracking
- **Portable** across CLI tools (Claude Code, Codex CLI, Gemini CLI)

### 4. Knowledge Enables Decision Quality

The primary value of persistent memory is better human decisions. Agents accumulate domain expertise — fleet patterns, failure modes, escalation paths, coordination strategies — that makes each interaction more informed than the last.

---

## Knowledge Architecture

### Storage Locations

| Location | Purpose | Lifecycle |
|----------|---------|-----------|
| `.aget/evolution/` | Lessons learned (L-docs) | Permanent — grows over time |
| `sessions/` | Session handoff artifacts | Archival — reference for context |
| `governance/` | Boundaries, charter, mission | Stable — changes infrequently |
| `knowledge/patterns/` | Reusable domain patterns | Evolving — refined with experience |
| `sops/` | Standard operating procedures | Versioned — lifecycle states |
| `planning/` | Active and completed projects | Active → archived |
| `specs/` | Formal specifications | Versioned — follows semver |

### Discovery Patterns

| Pattern | Trigger | Behavior |
|---------|---------|----------|
| Step Back / Review KB | "step back. review kb." | Systematic search across 5 KB areas before proposing |
| Session Handoff | Wind-down protocol | Capture pending work, decisions, context for next session |
| Study Up | `/aget-study-up <topic>` | Focused search on specific topic across KB |
| Pre-Proposal KB Audit | Before substantial changes | Verify precedents, cite 3+ or note "novel" |

---

## Theoretical Foundations

| Theory | Key Insight | Application |
|--------|-------------|-------------|
| Extended Mind (Clark/Chalmers) | KB extends cognition beyond the agent | Treat artifacts as part of the thinking process |
| Transactive Memory (Wegner) | Shared "who knows what" system | Fleet registry + L-docs = distributed expertise |
| Stigmergy (Grasse) | Coordination via environment modification | Artifacts coordinate across sessions without direct communication |
| Distributed Cognition (Hutchins) | Cognition across artifacts and agents | Knowledge architecture supports multi-agent reasoning |

---

## For Template Users

When instantiating this template for your supervisor:

1. **Start capturing L-docs immediately** — even informal observations compound over time
2. **Use session files** — structured handoff prevents context loss
3. **Build your fleet registry** — know which agent knows what
4. **Review before proposing** — the KB Review Checklist (L335) prevents reinventing the wheel

---

*MEMORY_VISION.md v1.0.0*
*"The knowledge base is the collaboration substrate"*
