#!/usr/bin/env python3
"""
Harvest Retros - Fleet Retrospective Mining

Parse retrospective sections from completed PROJECT_PLANs and optionally
session log YAML frontmatter. Outputs structured extraction with cross-plan
theme clustering for improvement candidate identification.

Implements: CAP-PP-006 (Stub Retrospective — harvest side)
See: PROJECT_PLAN_TEMPLATE.md Part 8 (4Ls retrospective sections)
Related: CAP-PP-006 (Stub Retrospective), ADR-008 (Advisory to Strict)

Scan scope:
    planning/PROJECT_PLAN_*.md
    planning/archive/**/PROJECT_PLAN_*.md
    sessions/SESSION_*.md (opt-in via --sessions)

Usage:
    python3 scripts/harvest_retros.py                    # Human-readable (plans only)
    python3 scripts/harvest_retros.py --json             # JSON output
    python3 scripts/harvest_retros.py --verbose          # Show parse details
    python3 scripts/harvest_retros.py --all              # Include incomplete plans
    python3 scripts/harvest_retros.py --sessions         # Also harvest session logs

Note on --sessions:
    Session harvesting extracts pain_points, learnings, and blockers from
    YAML frontmatter in session files. This requires wind_down.py or the
    wind-down skill to produce structured frontmatter. If your session files
    lack YAML frontmatter, --sessions will find 0 extractable sessions.

Exit codes:
    0: Success
    1: No plans found or parse failure
    2: Configuration error

Author: aget-framework (canonical template)
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def find_agent_root() -> Path:
    """Walk upward from CWD to find .aget/ directory marker."""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / ".aget").is_dir():
            return parent
    return current


def discover_plans(root: Path, include_archive: bool = True) -> List[Path]:
    """Find all PROJECT_PLAN files in planning/ and planning/archive/."""
    plans = []
    planning_dir = root / "planning"
    if not planning_dir.is_dir():
        return plans

    # Direct planning/ directory
    plans.extend(sorted(planning_dir.glob("PROJECT_PLAN_*.md")))

    # Archive subdirectories
    if include_archive:
        archive_dir = planning_dir / "archive"
        if archive_dir.is_dir():
            plans.extend(sorted(archive_dir.rglob("PROJECT_PLAN_*.md")))

    return plans


def extract_status(content: str) -> Optional[str]:
    """Extract plan status from header area.

    Looks for **Status**: <value> pattern in the first 80 lines,
    using first match only to avoid gate-level status overwrite.
    """
    lines = content.split("\n")[:80]
    for line in lines:
        match = re.search(r"\*\*Status\*\*:\s*(.+)", line)
        if match:
            return match.group(1).strip()
    return None


def is_completed(status: Optional[str]) -> bool:
    """Check if plan status indicates completion.

    Must match completion keywords at word boundaries or as the primary status.
    Avoids false positives like 'Active (G1 COMPLETE)' where the plan itself
    is not complete — only a gate is.
    """
    if not status:
        return False
    lower = status.lower()

    # Extract the primary status word (before any parenthetical detail)
    primary = re.split(r"\s*\(", lower)[0].strip()

    # Also handle patterns like "COMPLETE — details"
    primary = re.split(r"\s*[—–-]\s*", primary)[0].strip()
    primary = primary.lstrip("✅ ").strip()

    # Reject gate/phase-level completion (means a gate/phase is done, not the plan)
    if re.match(r"(gate|phase)\s+\d", primary):
        return False

    # Reject "Active" or "In Progress" even if later text says COMPLETE
    if any(word in primary for word in ["active", "in_progress", "in progress",
                                         "planning", "draft", "ready", "paused",
                                         "blocked"]):
        return False

    return any(word in primary for word in ["complete", "closed", "done", "subsumed", "superseded"])


def extract_plan_name(content: str, filepath: Path) -> str:
    """Extract human-readable plan name from content or filename."""
    # Try extracting from first H1 header
    for line in content.split("\n")[:10]:
        if line.startswith("# "):
            return line[2:].strip()
    # Fallback to filename
    name = filepath.stem
    name = re.sub(r"^PROJECT_PLAN_", "", name)
    name = re.sub(r"_v\d+\.\d+$", "", name)
    return name.replace("_", " ").title()


def extract_created_date(content: str) -> Optional[str]:
    """Extract creation date from plan metadata."""
    for line in content.split("\n")[:30]:
        match = re.search(r"\*\*Created\*\*:\s*(\d{4}-\d{2}-\d{2})", line)
        if match:
            return match.group(1)
    return None


def extract_retro_sections(content: str) -> Dict[str, List[str]]:
    """Extract retrospective sections from plan content.

    Handles 3 format variants:
    1. Markdown tables (| Item | Evidence |)
    2. Bullet lists (- **Bold**: description)
    3. Numbered prose (1. **Question** Answer...)

    Returns dict with keys: went_well, didnt_go_well, to_improve, action_items
    """
    sections = {
        "went_well": [],
        "didnt_go_well": [],
        "to_improve": [],
        "action_items": [],
    }

    lines = content.split("\n")

    # Section header patterns (case-insensitive)
    section_patterns = {
        "went_well": [
            r"^#{2,4}\s+What\s+Went\s+Well",
            r"^#{2,4}\s+What\s+worked\s+well",
        ],
        "didnt_go_well": [
            r"^#{2,4}\s+What\s+Didn.t\s+Go\s+Well",
            r"^#{2,4}\s+What\s+Could\s+Improve",
            r"^#{2,4}\s+What\s+didn.t\s+work",
        ],
        "to_improve": [
            r"^#{2,4}\s+What\s+To\s+Improve",
            r"^#{2,4}\s+Recommendations",
        ],
        "action_items": [
            r"^#{2,4}\s+Action\s+Items",
        ],
    }

    def find_section_ranges() -> List[Tuple[str, int, int]]:
        """Find (section_key, start_line, end_line) for each retro section."""
        ranges = []

        for i, line in enumerate(lines):
            for key, patterns in section_patterns.items():
                for pattern in patterns:
                    if re.match(pattern, line, re.IGNORECASE):
                        ranges.append((key, i))
                        break

        # Determine end of each section (next header of same or higher level)
        result = []
        for idx, (key, start) in enumerate(ranges):
            # Find the header level of this section
            header_match = re.match(r"^(#{1,4})\s+", lines[start])
            header_level = len(header_match.group(1)) if header_match else 3

            end = len(lines)
            for j in range(start + 1, len(lines)):
                hm = re.match(r"^(#{1,4})\s+", lines[j])
                if hm and len(hm.group(1)) <= header_level:
                    end = j
                    break
                # Also stop at horizontal rules (gate boundaries)
                if lines[j].strip() == "---" and j > start + 2:
                    end = j
                    break

            result.append((key, start + 1, end))

        return result

    def parse_section_content(section_lines: List[str]) -> List[str]:
        """Parse items from a section, handling tables, bullets, and prose."""
        items = []

        for line in section_lines:
            stripped = line.strip()

            # Skip empty lines, table headers, and separator rows
            if not stripped:
                continue
            if stripped.startswith("|") and ("---" in stripped or "Item" in stripped
                                             or "Improvement" in stripped
                                             or "Evidence" in stripped
                                             or "Impact" in stripped):
                continue
            # Skip placeholder rows
            if "To be populated" in stripped or "TBD" in stripped:
                continue
            if "{" in stripped and "}" in stripped:
                # Template placeholder like {Success 1}
                continue

            # Parse table rows
            if stripped.startswith("|"):
                cells = [c.strip() for c in stripped.split("|")[1:-1]]
                cells = [c for c in cells if c]
                if cells:
                    items.append(" | ".join(cells))
                continue

            # Parse bullet items
            if re.match(r"^[-*]\s+", stripped):
                item = re.sub(r"^[-*]\s+", "", stripped)
                # Handle checkbox items
                item = re.sub(r"^\[[ x]\]\s*", "", item)
                if item:
                    items.append(item)
                continue

            # Parse numbered items
            if re.match(r"^\d+\.\s+", stripped):
                item = re.sub(r"^\d+\.\s+", "", stripped)
                if item:
                    items.append(item)
                continue

        return items

    for key, start, end in find_section_ranges():
        section_content = lines[start:end]
        items = parse_section_content(section_content)
        # Only keep first occurrence of each section key (avoid duplicates from
        # plans that have retro sections in multiple gates)
        if not sections[key]:
            sections[key] = items
        else:
            sections[key].extend(items)

    return sections


def discover_sessions(root: Path) -> List[Path]:
    """Find all SESSION log files."""
    sessions_dir = root / "sessions"
    if not sessions_dir.is_dir():
        return []
    return sorted(sessions_dir.glob("SESSION_*.md"))


def extract_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter fields from a markdown file.

    Parses the --- delimited block at the top. Handles both scalar
    and list values without requiring the yaml library.
    """
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    result: Dict[str, Any] = {}
    current_key = None
    current_list: List[str] = []

    for line in match.group(1).split("\n"):
        # List continuation
        if line.startswith("  - ") and current_key:
            current_list.append(line.strip().lstrip("- ").strip().strip('"'))
            continue

        # Save accumulated list
        if current_key and current_list:
            result[current_key] = current_list
            current_list = []
            current_key = None

        # Key: value line
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"')
            if val.startswith("[") and val.endswith("]"):
                # Inline list: [a, b, c]
                items = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
                result[key] = items
            elif val:
                result[key] = val
            else:
                # Could be start of a list block
                current_key = key
                current_list = []

    # Final flush
    if current_key and current_list:
        result[current_key] = current_list

    return result


def harvest_session(filepath: Path, verbose: bool = False) -> Optional[Dict[str, Any]]:
    """Harvest improvement-relevant data from a session log.

    Extracts from YAML frontmatter:
    - pain_points (direct improvement candidates)
    - learnings (lessons learned)
    - blockers (blocked items — may surface patterns)
    """
    try:
        content = filepath.read_text(encoding="utf-8")
    except (IOError, UnicodeDecodeError) as e:
        if verbose:
            print(f"  SKIP session {filepath.name}: {e}", file=sys.stderr)
        return None

    fm = extract_yaml_frontmatter(content)
    if not fm:
        return None

    date = fm.get("date", None)
    name = filepath.stem.replace("SESSION_", "").replace("_", " ")

    # Extract improvement-relevant fields
    pain_points = fm.get("pain_points", [])
    learnings = fm.get("learnings", [])
    blockers = fm.get("blockers", [])

    # Normalize: ensure all are lists of strings
    if isinstance(pain_points, str):
        pain_points = [pain_points]
    if isinstance(learnings, str):
        learnings = [learnings]
    if isinstance(blockers, str):
        blockers = [blockers]

    # Filter out empty/placeholder entries
    pain_points = [p for p in pain_points if p and p not in ("None", "none", "N/A")]
    learnings = [l for l in learnings if l and l not in ("None", "none", "N/A")]
    blockers = [b for b in blockers if b and b not in ("None", "none", "N/A")]

    total = len(pain_points) + len(learnings) + len(blockers)
    if total == 0:
        return None  # Nothing extractable

    return {
        "file": str(filepath),
        "name": f"Session: {name}",
        "source_type": "session",
        "date": date,
        "sections": {
            "pain_points": pain_points,
            "learnings": learnings,
            "blockers": blockers,
        },
        "item_counts": {
            "pain_points": len(pain_points),
            "learnings": len(learnings),
            "blockers": len(blockers),
        },
        "total_items": total,
    }


def assess_retro_quality(sections: Dict[str, List[str]]) -> str:
    """Assess quality of retrospective: filled, partial, empty, or placeholder."""
    total_items = sum(len(v) for v in sections.values())
    filled_sections = sum(1 for v in sections.values() if v)

    if total_items == 0:
        return "empty"
    if filled_sections >= 3 and total_items >= 6:
        return "filled"
    if filled_sections >= 1:
        return "partial"
    return "empty"


def harvest_plan(filepath: Path, verbose: bool = False) -> Optional[Dict[str, Any]]:
    """Harvest retrospective data from a single plan."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except (IOError, UnicodeDecodeError) as e:
        if verbose:
            print(f"  SKIP {filepath.name}: {e}", file=sys.stderr)
        return None

    status = extract_status(content)
    name = extract_plan_name(content, filepath)
    created = extract_created_date(content)
    sections = extract_retro_sections(content)
    quality = assess_retro_quality(sections)

    return {
        "file": str(filepath),
        "name": name,
        "status": status or "Unknown",
        "created": created,
        "quality": quality,
        "sections": sections,
        "item_counts": {k: len(v) for k, v in sections.items()},
        "total_items": sum(len(v) for v in sections.values()),
    }


def extract_themes(
    results: List[Dict[str, Any]],
    session_results: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, List[Dict[str, Any]]]:
    """Extract cross-source themes from plans and sessions.

    Groups items by keyword similarity for basic theme clustering.
    Theme keywords are extensible — add domain-specific keywords as needed.
    """
    # Collect all improvement-oriented items with source attribution
    improvement_items = []

    # From plans: didnt_go_well + to_improve
    for r in results:
        if r["quality"] == "empty":
            continue
        for item in r["sections"].get("didnt_go_well", []):
            improvement_items.append({
                "item": item,
                "source": r["name"],
                "section": "didnt_go_well",
                "created": r["created"],
            })
        for item in r["sections"].get("to_improve", []):
            improvement_items.append({
                "item": item,
                "source": r["name"],
                "section": "to_improve",
                "created": r["created"],
            })

    # From sessions: pain_points + blockers
    for s in (session_results or []):
        for item in s["sections"].get("pain_points", []):
            improvement_items.append({
                "item": item,
                "source": s["name"],
                "section": "pain_point",
                "created": s["date"],
            })
        for item in s["sections"].get("blockers", []):
            improvement_items.append({
                "item": item,
                "source": s["name"],
                "section": "blocker",
                "created": s["date"],
            })

    # Basic keyword-based theme clustering
    # Extensible: add domain-specific keywords as your fleet's patterns emerge
    theme_keywords = {
        "gate_discipline": ["gate", "boundary", "discipline", "skip", "premature"],
        "specification": ["spec", "specification", "EARS", "requirement", "CAP-"],
        "automation": ["automat", "script", "manual", "tooling"],
        "estimation": ["estimate", "budget", "time", "duration", "velocity", "overestimate"],
        "scope": ["scope", "creep", "defer", "out-of-scope"],
        "verification": ["verif", "test", "V-test", "validation", "check"],
        "documentation": ["doc", "document", "readme", "guide"],
        "fleet_coordination": ["fleet", "deploy", "propagat", "rollout", "migration"],
        "template": ["template", "baseline", "standard", "drift"],
        "communication": ["handoff", "checkpoint", "L100", "coordinate"],
    }

    themes = {theme: [] for theme in theme_keywords}
    themes["uncategorized"] = []

    for entry in improvement_items:
        item_lower = entry["item"].lower()
        matched = False
        for theme, keywords in theme_keywords.items():
            if any(kw.lower() in item_lower for kw in keywords):
                themes[theme].append(entry)
                matched = True
                break  # First match wins
        if not matched:
            themes["uncategorized"].append(entry)

    # Remove empty themes
    return {k: v for k, v in themes.items() if v}


def format_human(
    results: List[Dict[str, Any]],
    themes: Dict[str, List[Dict[str, Any]]],
    session_results: Optional[List[Dict[str, Any]]] = None,
) -> str:
    """Format results as human-readable markdown."""
    out = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    session_results = session_results or []

    # Header
    out.append("=" * 60)
    out.append(f"HARVEST RETROS — {timestamp}")
    out.append("=" * 60)
    out.append("")

    # Summary stats
    total = len(results)
    filled = sum(1 for r in results if r["quality"] == "filled")
    partial = sum(1 for r in results if r["quality"] == "partial")
    empty = sum(1 for r in results if r["quality"] == "empty")
    plan_items = sum(r["total_items"] for r in results)
    session_items = sum(s["total_items"] for s in session_results)
    total_items = plan_items + session_items

    out.append(f"**Plans scanned**: {total}")
    out.append(f"**Retro quality**: {filled} filled, {partial} partial, {empty} empty")
    if session_results:
        out.append(f"**Sessions scanned**: {len(session_results)} (with extractable content)")
    out.append(f"**Total items extracted**: {total_items}" + (
        f" ({plan_items} from plans, {session_items} from sessions)" if session_results else ""))
    out.append("")

    # Quality breakdown
    if empty > 0:
        out.append(f"### Empty Retros ({empty} plans — closure checklist gap)")
        out.append("")
        for r in results:
            if r["quality"] == "empty":
                out.append(f"  - {r['name']} ({r['status']})")
        out.append("")

    # Per-plan extraction (filled + partial only)
    out.append("### Per-Plan Extraction")
    out.append("")
    for r in sorted(results, key=lambda x: x["created"] or "0000", reverse=True):
        if r["quality"] == "empty":
            continue

        out.append(f"#### {r['name']}")
        out.append(f"*Status: {r['status']} | Created: {r['created'] or 'Unknown'} | Quality: {r['quality']}*")
        out.append("")

        for section_key, section_label in [
            ("went_well", "Went Well"),
            ("didnt_go_well", "Didn't Go Well"),
            ("to_improve", "To Improve"),
            ("action_items", "Action Items"),
        ]:
            items = r["sections"][section_key]
            if items:
                out.append(f"  **{section_label}** ({len(items)}):")
                for item in items:
                    # Truncate long items for readability
                    display = item[:200] + "..." if len(item) > 200 else item
                    out.append(f"    - {display}")
                out.append("")

    # Session extraction
    if session_results:
        out.append("### Session Extraction")
        out.append("")
        for s in sorted(session_results, key=lambda x: x["date"] or "0000", reverse=True):
            out.append(f"#### {s['name']}")
            out.append(f"*Date: {s['date'] or 'Unknown'}*")
            out.append("")
            for section_key, section_label in [
                ("pain_points", "Pain Points"),
                ("learnings", "Learnings"),
                ("blockers", "Blockers"),
            ]:
                items = s["sections"][section_key]
                if items:
                    out.append(f"  **{section_label}** ({len(items)}):")
                    for item in items:
                        display = item[:200] + "..." if len(item) > 200 else item
                        out.append(f"    - {display}")
                    out.append("")

    # Theme analysis
    if themes:
        out.append("### Cross-Plan Themes (Improvement Candidates)")
        out.append("")
        # Sort themes by item count descending
        for theme, items in sorted(themes.items(), key=lambda x: len(x[1]), reverse=True):
            label = theme.replace("_", " ").title()
            out.append(f"  **{label}** ({len(items)} items):")
            for entry in items:
                source = entry["source"]
                display = entry["item"][:150] + "..." if len(entry["item"]) > 150 else entry["item"]
                out.append(f"    - [{source}] {display}")
            out.append("")

    out.append("=" * 60)
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Harvest retrospective sections from completed PROJECT_PLANs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 scripts/harvest_retros.py              # Human output (plans only)\n"
            "  python3 scripts/harvest_retros.py --json        # JSON output\n"
            "  python3 scripts/harvest_retros.py --sessions    # Include session logs\n"
            "  python3 scripts/harvest_retros.py --all         # Include incomplete plans\n"
            "  python3 scripts/harvest_retros.py --verbose     # Parse details\n"
        ),
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show parse details")
    parser.add_argument("--all", action="store_true", help="Include non-complete plans")
    parser.add_argument("--sessions", action="store_true",
                        help="Also harvest session log YAML frontmatter (requires structured frontmatter)")
    parser.add_argument("--dir", type=Path, default=None, help="Agent root directory")
    args = parser.parse_args()

    root = args.dir or find_agent_root()
    if not (root / ".aget").is_dir():
        print(f"Error: {root} does not contain .aget/ directory", file=sys.stderr)
        return 2

    # Discover plans
    plans = discover_plans(root)
    if not plans:
        print("No PROJECT_PLAN files found.", file=sys.stderr)
        return 1

    if args.verbose:
        print(f"Found {len(plans)} PROJECT_PLAN files", file=sys.stderr)

    # Harvest each plan
    results = []
    for plan_path in plans:
        result = harvest_plan(plan_path, verbose=args.verbose)
        if result is None:
            continue

        # Filter by completion status unless --all
        if not args.all and not is_completed(result["status"]):
            if args.verbose:
                print(f"  SKIP {plan_path.name}: status={result['status']}", file=sys.stderr)
            continue

        results.append(result)

    if args.verbose:
        print(f"Harvested {len(results)} plans", file=sys.stderr)

    # Harvest sessions (opt-in)
    session_results = []
    if args.sessions:
        sessions = discover_sessions(root)
        if args.verbose:
            print(f"Found {len(sessions)} session files", file=sys.stderr)
        for session_path in sessions:
            result = harvest_session(session_path, verbose=args.verbose)
            if result is not None:
                session_results.append(result)
        if args.verbose:
            print(f"Harvested {len(session_results)} sessions with content", file=sys.stderr)

    if not results and not session_results:
        print("No completed plans or sessions found.", file=sys.stderr)
        return 1

    # Extract themes (plans + sessions combined)
    themes = extract_themes(results, session_results)

    # Output
    plan_items = sum(r["total_items"] for r in results)
    session_items_total = sum(s["total_items"] for s in session_results)

    if args.json:
        output = {
            "timestamp": datetime.now().isoformat(),
            "plans_scanned": len(results),
            "sessions_scanned": len(session_results),
            "quality_summary": {
                "filled": sum(1 for r in results if r["quality"] == "filled"),
                "partial": sum(1 for r in results if r["quality"] == "partial"),
                "empty": sum(1 for r in results if r["quality"] == "empty"),
            },
            "total_items": plan_items + session_items_total,
            "plan_items": plan_items,
            "session_items": session_items_total,
            "plans": results,
            "sessions": session_results,
            "themes": {k: v for k, v in themes.items()},
        }
        print(json.dumps(output, indent=2, default=str))
    else:
        print(format_human(results, themes, session_results))

    return 0


if __name__ == "__main__":
    sys.exit(main())
