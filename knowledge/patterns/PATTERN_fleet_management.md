# Pattern: Fleet Management

**Version**: 1.0.0
**Created**: 2026-02-27
**Author**: AGET Framework Team
**Category**: Supervision
**Evidence**: Production supervisor fleet operations (32-agent fleet, 4 portfolios)

---

## Context

Supervisor agents manage fleets of varying size and complexity. Effective fleet management requires balancing oversight depth with operational efficiency.

## Problem

How to maintain fleet health, version consistency, and knowledge quality across many agents without creating supervisory bottlenecks.

## Solution

### Tiered Oversight Model

| Tier | Frequency | Scope | Tools |
|------|-----------|-------|-------|
| **Continuous** | Every session | Version consistency, test status | `/aget-check-health` |
| **Periodic** | Weekly/monthly | Evolution activity, KB quality | `/aget-review-agent`, `/aget-check-sessions` |
| **Event-driven** | On release | Upgrade coordination, conformance | `/aget-broadcast-fleet` |

### Fleet Health Indicators

| Indicator | Healthy | Warning | Critical |
|-----------|---------|---------|----------|
| Contract tests | All passing | 1-2 warnings | Any failures |
| Version alignment | All on latest | 1 version behind | 2+ versions behind |
| Session activity | Regular sessions | >2 weeks idle | >1 month idle |
| L-doc capture | Growing | Stagnant | Decreasing |

### Portfolio-Aware Operations

- Group agents by portfolio for targeted operations
- Respect portfolio sensitivity boundaries in communications
- Track upgrade status per portfolio, not just fleet-wide

## Consequences

- **Positive**: Early detection of fleet drift, consistent quality
- **Negative**: Overhead of regular reviews (mitigated by automation)

## Related Patterns

- PATTERN_escalation_routing.md — When fleet issues exceed supervisor scope
- SOP_fleet_coordination.md — Operational procedures for fleet work

---

*PATTERN_fleet_management.md v1.0.0*
