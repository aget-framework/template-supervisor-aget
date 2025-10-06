# Sessions Directory

This directory stores session notes from your supervisor agent's work sessions.

## Purpose

Session notes create a timeline of work completed, capturing:
- What was accomplished in each session
- Decisions made and rationale
- Blockers encountered
- Patterns discovered
- Time invested

## Format

Use Session Metadata Standard v1.0 (if available in `.aget/docs/`):

**Filename**: `SESSION_YYYY-MM-DD_description.md` or `SESSION_YYYY-MM-DD.md`

**Structure**:
```markdown
---
session_id: SESSION_YYYY-MM-DD_description
date: YYYY-MM-DD
time_start: "HH:MM"
time_end: "HH:MM"
duration_minutes: NN
aget_version: "X.Y.Z"
agent_name: "your-supervisor-aget"
session_type: tactical|strategic|exploratory
---

# Session: YYYY-MM-DD - Description

## Objectives
What were we trying to accomplish?

## Work Completed
- Task 1: Status/outcome
- Task 2: Status/outcome

## Decisions Made
Key decisions and rationale

## Blockers / Issues
Anything blocking progress

## Patterns Discovered
Insights worth capturing (may become evolution logs)

## Next Steps
What to work on next session
```

## Best Practices

**Timing**: Create during wind-down (end of session)

**Frequency**: One per session (not per commit)

**Location**: Always in `sessions/` directory (never in root)

**Granularity**: Capture enough detail for "future you" to understand what happened 6 months later

**Quantitative**: Include metrics when possible (files changed, time spent, tests passing)

## Template Usage

This directory is empty in the template. Your session notes will appear here as you work with your supervisor agent.

**First Session**: After your first work session, run wind-down protocol to create your first session note.

---

**Session notes are your work log. Document consistently, reference frequently.**
