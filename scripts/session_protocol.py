#!/usr/bin/env python3
"""
Universal Session Protocol Handler
Implements wake up, wind down, and sign off protocols for all repos
"""

import os
import sys
import subprocess
import json
import re
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Tuple, Any


class SessionProtocol:
    """Handles session management protocols across all repositories"""

    def __init__(self):
        self.cwd = Path.cwd()
        self.repo_name = self.cwd.name
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.date_compact = datetime.now().strftime('%Y%m%d_%H%M')
        self.session_file = self.cwd / '.session_state.json'

    def run_command(self, cmd: List[str], check: bool = False) -> Tuple[int, str, str]:
        """Run a shell command and return (returncode, stdout, stderr)"""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return 1, "", "Command timed out"
        except Exception as e:
            return 1, "", str(e)

    def read_claude_md(self) -> bool:
        """Read CLAUDE.md to load configuration"""
        claude_path = self.cwd / "CLAUDE.md"
        if not claude_path.exists():
            claude_path = self.cwd.parent / "CLAUDE.md"

        if claude_path.exists():
            with open(claude_path, 'r') as f:
                # Just read it to "load" configuration
                content = f.read()
            return True
        return False

    def get_recent_files(self) -> List[str]:
        """Get recently modified files"""
        returncode, stdout, stderr = self.run_command(['ls', '-lat'])
        if returncode == 0:
            lines = stdout.strip().split('\n')[:10]
            return lines
        return []

    def get_git_status(self) -> Dict[str, any]:
        """Get git repository status"""
        status = {
            'branch': 'unknown',
            'has_changes': False,
            'changes': [],
            'is_repo': False
        }

        # Check if git repo
        returncode, stdout, stderr = self.run_command(['git', 'rev-parse', '--git-dir'])
        if returncode != 0:
            return status

        status['is_repo'] = True

        # Get branch
        returncode, stdout, stderr = self.run_command(['git', 'branch', '--show-current'])
        if returncode == 0:
            status['branch'] = stdout.strip() or 'main'

        # Get changes
        returncode, stdout, stderr = self.run_command(['git', 'status', '--porcelain'])
        if returncode == 0 and stdout.strip():
            status['has_changes'] = True
            status['changes'] = stdout.strip().split('\n')

        return status

    def get_project_status(self) -> Optional[str]:
        """Get project-specific status (if Makefile has status target)"""
        if (self.cwd / 'Makefile').exists():
            returncode, stdout, stderr = self.run_command(['make', 'status'])
            if returncode == 0:
                return stdout.strip()
        return None

    def load_session_state(self) -> Optional[Dict[str, Any]]:
        """Load previous session state if it exists"""
        if self.session_file.exists():
            try:
                with open(self.session_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def save_session_state(self, action: str, extra_data: Optional[Dict] = None):
        """Save current session state"""
        git_status = self.get_git_status()

        state = {
            'timestamp': self.timestamp,
            'last_action': action,
            'working_directory': str(self.cwd),
            'git_branch': git_status.get('branch', 'unknown'),
            'uncommitted_files': git_status.get('changes', []),
            'has_uncommitted': git_status.get('has_changes', False)
        }

        # Add any extra data provided
        if extra_data:
            state.update(extra_data)

        # Load existing state to preserve history
        existing = self.load_session_state()
        if existing:
            state['previous_session'] = {
                'timestamp': existing.get('timestamp'),
                'last_action': existing.get('last_action'),
                'duration': self.calculate_duration(existing.get('timestamp'))
            }

        try:
            with open(self.session_file, 'w') as f:
                json.dump(state, f, indent=2)
        except Exception:
            pass  # Silently fail - session state is nice to have, not critical

    def analyze_git_changes(self) -> Dict[str, Any]:
        """Analyze git diff to understand what changed"""
        analysis = {
            'files_changed': [],
            'lines_added': 0,
            'lines_removed': 0,
            'file_types': {},
            'change_summary': ''
        }

        # Get list of changed files
        returncode, stdout, stderr = self.run_command(['git', 'diff', '--name-status', 'HEAD'])
        if returncode == 0 and stdout:
            for line in stdout.strip().split('\n'):
                if line:
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        status, filename = parts[0], parts[1]
                        analysis['files_changed'].append(filename)

                        # Track file types
                        ext = Path(filename).suffix
                        if ext:
                            analysis['file_types'][ext] = analysis['file_types'].get(ext, 0) + 1

        # Get detailed statistics
        returncode, stdout, stderr = self.run_command(['git', 'diff', '--stat', 'HEAD'])
        if returncode == 0 and stdout:
            # Parse the stat line (e.g., "3 files changed, 42 insertions(+), 5 deletions(-)")
            stat_match = re.search(r'(\d+) insertion.*(\d+) deletion', stdout)
            if stat_match:
                analysis['lines_added'] = int(stat_match.group(1))
                analysis['lines_removed'] = int(stat_match.group(2))

        # Generate change summary
        if analysis['files_changed']:
            primary_type = max(analysis['file_types'].items(), key=lambda x: x[1])[0] if analysis['file_types'] else ''
            analysis['change_summary'] = f"{len(analysis['files_changed'])} files ({primary_type})"

        return analysis

    def generate_smart_commit_message(self, analysis: Dict[str, Any]) -> str:
        """Generate intelligent commit message based on changes"""
        files = analysis['files_changed']
        file_types = analysis['file_types']

        # Determine commit type
        if not files:
            return "chore: Minor updates"

        # Check file patterns for commit type
        if all('test' in f.lower() for f in files):
            prefix = "test"
            desc = "Update tests"
        elif all('doc' in f.lower() or f.endswith('.md') for f in files):
            prefix = "docs"
            desc = "Update documentation"
        elif any(f.endswith('.py') and 'protocol' in f for f in files):
            prefix = "feat"
            desc = "Enhance session protocols"
        elif file_types.get('.py', 0) > file_types.get('.md', 0):
            prefix = "feat" if analysis['lines_added'] > analysis['lines_removed'] else "refactor"
            desc = "Update implementation"
        else:
            prefix = "chore"
            desc = "Update configuration"

        # Add details
        if len(files) == 1:
            desc = f"Update {Path(files[0]).name}"
        elif len(files) > 3:
            desc = f"Update {len(files)} files"

        # Add metrics if significant
        if analysis['lines_added'] > 50:
            desc += f" (+{analysis['lines_added']} lines)"

        return f"{prefix}: {desc}"

    def generate_ai_summary(self, analysis: Dict[str, Any], session_start: Optional[str] = None) -> str:
        """Generate AI summary of session work"""
        # For now, create rule-based summary
        # Later can integrate with OpenAI/Claude API

        summary_parts = []

        # Session duration
        if session_start:
            duration = self.calculate_duration(session_start)
            if duration:
                summary_parts.append(f"Session duration: {duration}")

        # Changes overview
        if analysis['files_changed']:
            summary_parts.append(f"Modified {len(analysis['files_changed'])} files")

            # File type breakdown
            if analysis['file_types']:
                types_str = ', '.join([f"{count} {ext}" for ext, count in analysis['file_types'].items()])
                summary_parts.append(f"File types: {types_str}")

            # Change metrics
            if analysis['lines_added'] or analysis['lines_removed']:
                summary_parts.append(f"Changes: +{analysis['lines_added']}/-{analysis['lines_removed']} lines")

        # Focus areas based on file patterns
        focus_areas = []
        for file in analysis['files_changed']:
            if 'test' in file.lower():
                focus_areas.append("testing")
            elif 'doc' in file.lower() or file.endswith('.md'):
                focus_areas.append("documentation")
            elif 'protocol' in file:
                focus_areas.append("session management")

        if focus_areas:
            unique_areas = list(set(focus_areas))
            summary_parts.append(f"Focus: {', '.join(unique_areas)}")

        return " | ".join(summary_parts) if summary_parts else "No significant changes"

    def call_llm_api(self, prompt: str) -> Optional[str]:
        """Call LLM API for advanced summaries (placeholder for future integration)"""
        # This is where we'd integrate with OpenAI/Claude
        # For now, return None to use rule-based summary

        # Future implementation:
        # api_key = os.environ.get('OPENAI_API_KEY')
        # if api_key:
        #     response = openai.ChatCompletion.create(
        #         model="gpt-4",
        #         messages=[{"role": "user", "content": prompt}]
        #     )
        #     return response.choices[0].message.content

        return None

    def calculate_duration(self, previous_timestamp: Optional[str]) -> Optional[str]:
        """Calculate duration from previous timestamp"""
        if not previous_timestamp:
            return None
        try:
            prev_time = datetime.strptime(previous_timestamp, '%Y-%m-%d %H:%M')
            current_time = datetime.strptime(self.timestamp, '%Y-%m-%d %H:%M')
            duration = current_time - prev_time

            # Format duration nicely
            if duration.days > 0:
                return f"{duration.days} days"
            elif duration.seconds > 3600:
                hours = duration.seconds // 3600
                return f"{hours} hours"
            else:
                minutes = duration.seconds // 60
                return f"{minutes} minutes"
        except Exception:
            return None

    def wake_up(self) -> int:
        """Execute wake up protocol"""
        # Load configuration silently
        claude_loaded = self.read_claude_md()

        # Load previous session state
        previous_state = self.load_session_state()

        # Get all status info
        git_status = self.get_git_status()
        project_status = self.get_project_status()

        # Compact output
        print(f"## Wake Up - {self.timestamp}")
        print(f"📍 {self.cwd}")

        if git_status['is_repo']:
            changes_str = f" ({len(git_status['changes'])} uncommitted)" if git_status['has_changes'] else " (clean)"
            print(f"🔄 {git_status['branch']} branch{changes_str}")

        # Debug output if in debug mode
        if os.environ.get('DEBUG_SESSION'):
            print(f"🔍 Debug: CLAUDE.md loaded={claude_loaded}, session_file={self.session_file.exists()}")
            if previous_state:
                print(f"🔍 Debug: Previous state found with action={previous_state.get('last_action')}")

        # Show previous session info if available
        if previous_state:
            prev_session = previous_state.get('previous_session', previous_state)
            if prev_session.get('duration'):
                action = prev_session.get('last_action', 'unknown')
                print(f"📎 Last session: {prev_session['duration']} ago (ended with {action})")

            # Show warnings if there were uncommitted changes or issues
            if previous_state.get('tests_failed'):
                print(f"⚠️  Tests were failing in last session")
            if previous_state.get('handoff_notes'):
                print(f"📝 Note: {previous_state['handoff_notes']}")

        if project_status:
            # Extract key metrics from project status
            for line in project_status.split('\n'):
                if 'Queue' in line or 'Pending' in line or 'Enhanced' in line or 'Failed' in line:
                    print(f"📊 {line.strip()}")
                    break

        # Save wake up state
        self.save_session_state('wake')

        # Documentation discovery (from AGET template enhancement)
        docs_dirs = []
        for root, dirs, _ in os.walk(".", topdown=True):
            # Limit depth to avoid deep traversal
            if root.count(os.sep) >= 2:
                dirs[:] = []  # Don't go deeper
                continue
            if 'docs' in dirs or 'documentation' in dirs:
                doc_dir = os.path.join(root, 'docs') if 'docs' in dirs else os.path.join(root, 'documentation')
                docs_dirs.append(doc_dir)
            # Skip hidden and system directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'venv']]

        if docs_dirs:
            print(f"📚 Documentation available in: {', '.join(docs_dirs[:5])}")
            # ARCH-001: Self-contained - use only local patterns
            if Path("patterns/documentation/smart_reader.py").exists():
                print(f"💡 Tip: Use 'python3 patterns/documentation/smart_reader.py <path>' to safely read any file/directory")
            else:
                print(f"⚠️  smart_reader.py not installed. Run: python3 scripts/install_pattern.py")

        # Efficiency tips based on common patterns
        print("💡 Efficiency tips:")
        print("   • For 'read docs': use smart_reader.py (if available) or Task tool")
        print("   • For bulk operations: use Task tool for >3 similar actions")
        print("   • Batch similar Read/Grep operations together")
        print("   • Check .aget/patterns/session/EFFICIENT_STARTS.md for patterns")

        print("✅ Ready for tasks.")
        return 0

    def wind_down(self) -> int:
        """Execute wind down protocol"""
        git_status = self.get_git_status()
        committed = False
        files_committed = []
        ai_summary = ""

        # Get session start time from state
        previous_state = self.load_session_state()
        session_start = None
        if previous_state and previous_state.get('last_action') == 'wake':
            session_start = previous_state.get('timestamp')

        # Analyze changes for smart commit and summary
        if git_status['is_repo'] and git_status['has_changes']:
            analysis = self.analyze_git_changes()

            # Generate AI summary
            ai_summary = self.generate_ai_summary(analysis, session_start)

            # Track what we're committing
            files_committed = analysis['files_changed'][:5]

            # Use smart commit message
            smart_commit_msg = self.generate_smart_commit_message(analysis)

            # Commit changes
            returncode, stdout, stderr = self.run_command(['git', 'add', '-A'])
            if returncode == 0:
                # Use smart commit message with session summary
                commit_msg = f"{smart_commit_msg}\n\nSession: {ai_summary}"
                returncode, stdout, stderr = self.run_command(
                    ['git', 'commit', '-m', commit_msg]
                )
                if returncode == 0:
                    committed = True

        # Create session notes
        session_file = self.cwd / f"SESSION_{datetime.now().strftime('%Y-%m-%d')}.md"
        notes_created = False
        if not session_file.exists():
            with open(session_file, 'w') as f:
                f.write(f"# Session Notes - {self.timestamp}\n\n")
                f.write("## Work Completed\n")
                f.write("- [Add session summary here]\n\n")
            notes_created = True

        # Run tests if available
        tests_passed = None
        if (self.cwd / 'tests').exists():
            returncode, stdout, stderr = self.run_command(
                ['python', '-m', 'pytest', 'tests/', '-q', '--tb=no']
            )
            tests_passed = (returncode == 0)

        # Save wind down state with extra info
        extra_data = {
            'tests_failed': tests_passed is False,
            'tests_run': tests_passed is not None,
            'files_committed': files_committed if committed else [],
            'session_notes_created': notes_created
        }
        self.save_session_state('wind-down', extra_data)

        # Compact output
        print(f"## Wind Down - {self.timestamp}")
        if committed:
            print("✓ Changes committed")
        if notes_created:
            print(f"✓ Session notes created")
        if tests_passed is not None:
            print("✓ Tests passed" if tests_passed else "⚠ Some tests failed")
        print("✅ Session preserved.")
        return 0

    def sign_off(self) -> int:
        """Execute sign off protocol"""
        git_status = self.get_git_status()
        committed = False
        pushed = False

        if git_status['is_repo']:
            if git_status['has_changes']:
                # Quick commit
                returncode, stdout, stderr = self.run_command(['git', 'add', '-A'])
                if returncode == 0:
                    commit_msg = f"chore: Quick sign off at {self.timestamp}"
                    returncode, stdout, stderr = self.run_command(['git', 'commit', '-m', commit_msg])
                    if returncode == 0:
                        committed = True

            # Push to remote
            returncode, stdout, stderr = self.run_command(['git', 'push'])
            if returncode == 0:
                pushed = True

        # Save sign off state
        extra_data = {
            'committed': committed,
            'pushed': pushed
        }
        self.save_session_state('sign-off', extra_data)

        # Compact output
        print(f"## Sign Off - {self.timestamp}")
        if committed:
            print("✓ Changes committed")
        if pushed:
            print("✓ Pushed to remote")
        elif git_status['is_repo']:
            print("⚠ Push failed (may be offline)")
        print("✅ Signed off.")
        return 0


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: session_protocol.py [wake|wind-down|sign-off|note]")
        sys.exit(1)

    command = sys.argv[1].lower()
    protocol = SessionProtocol()

    if command in ['wake', 'wake-up']:
        return protocol.wake_up()
    elif command in ['wind-down', 'wind']:
        return protocol.wind_down()
    elif command in ['sign-off', 'sign']:
        return protocol.sign_off()
    elif command == 'note':
        # Add a handoff note to the session state
        if len(sys.argv) < 3:
            print("Usage: session_protocol.py note 'Your note here'")
            return 1
        note = ' '.join(sys.argv[2:])
        protocol.save_session_state('note', {'handoff_notes': note})
        print(f"📝 Note saved: {note}")
        return 0
    elif command == 'status':
        # Show session state for debugging
        state = protocol.load_session_state()
        if state:
            print("📋 Current session state:")
            print(f"   Last action: {state.get('last_action', 'unknown')}")
            print(f"   Timestamp: {state.get('timestamp', 'unknown')}")
            print(f"   Branch: {state.get('git_branch', 'unknown')}")
            print(f"   Uncommitted: {state.get('has_uncommitted', False)}")
            if state.get('tests_failed'):
                print(f"   ⚠️  Tests failed: Yes")
            if state.get('handoff_notes'):
                print(f"   📝 Notes: {state.get('handoff_notes')}")
            if state.get('previous_session'):
                prev = state['previous_session']
                print(f"   Previous: {prev.get('last_action')} ({prev.get('duration')} ago)")
        else:
            print("📋 No session state found")
            print(f"   Looking for: {protocol.session_file}")
            print(f"   File exists: {protocol.session_file.exists()}")
        return 0
    else:
        print(f"Unknown command: {command}")
        print("Use: wake, wind-down, sign-off, note, or status")
        return 1


if __name__ == '__main__':
    sys.exit(main())