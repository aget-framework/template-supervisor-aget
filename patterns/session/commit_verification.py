#!/usr/bin/env python3
"""
Commit Verification Pattern for AGET Sessions

CRITICAL REQUIREMENT: Never claim success without verification
"""

import subprocess
import sys
from enum import Enum
from typing import Optional, Tuple

class OutputLevel(Enum):
    CRITICAL = 0  # Cannot be silenced, exits non-zero
    ERROR = 1     # Operation failed
    WARNING = 2   # Needs attention
    SUCCESS = 3   # Verified success
    INFO = 4      # Status update
    DEBUG = 5     # Verbose details

def run_command(cmd: str) -> Tuple[bool, str, str]:
    """Run command and return (success, stdout, stderr)"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        return (result.returncode == 0, result.stdout, result.stderr)
    except subprocess.TimeoutExpired:
        return (False, "", "Command timed out after 30 seconds")
    except Exception as e:
        return (False, "", str(e))

def verify_commit() -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Verify that commit succeeded and return commit SHA
    Returns: (success, commit_sha, error_message)
    """
    # Check if there are uncommitted changes
    success, stdout, stderr = run_command("git status --porcelain")
    if not success:
        return (False, None, f"Cannot check git status: {stderr}")

    if stdout.strip():
        # There are uncommitted changes
        uncommitted = len(stdout.strip().split('\n'))
        return (False, None, f"{uncommitted} uncommitted changes remain")

    # Get the last commit SHA
    success, stdout, stderr = run_command("git rev-parse --short HEAD")
    if not success:
        return (False, None, f"Cannot get commit SHA: {stderr}")

    commit_sha = stdout.strip()

    # Verify commit exists
    success, stdout, stderr = run_command(f"git cat-file -t {commit_sha}")
    if not success or stdout.strip() != "commit":
        return (False, None, f"Commit {commit_sha} verification failed")

    return (True, commit_sha, None)

def safe_commit(message: str) -> bool:
    """
    Perform a safe commit with verification
    Returns True only if commit succeeded and was verified
    """
    print(f"{OutputLevel.INFO.name}: Committing changes...")

    # First, add all changes
    success, stdout, stderr = run_command("git add -A")
    if not success:
        print(f"🚨 {OutputLevel.CRITICAL.name}: Failed to stage changes")
        print(f"   Error: {stderr}")
        print(f"   Recovery: Run 'git add -A' manually and check for errors")
        return False

    # Check what we're about to commit
    success, stdout, stderr = run_command("git diff --staged --stat")
    if not success:
        print(f"⚠️ {OutputLevel.WARNING.name}: Cannot preview changes")
    elif not stdout.strip():
        print(f"{OutputLevel.INFO.name}: No changes to commit")
        return True
    else:
        # Show brief summary
        lines = stdout.strip().split('\n')
        if len(lines) > 10:
            print(f"{OutputLevel.INFO.name}: Staging {len(lines)-1} files...")
        else:
            print(f"{OutputLevel.INFO.name}: Changes to commit:")
            for line in lines[:-1]:  # Skip summary line
                print(f"   {line}")

    # Perform the commit
    # Use heredoc style to handle complex commit messages
    commit_cmd = f'''git commit -m "{message}"'''
    success, stdout, stderr = run_command(commit_cmd)

    if not success:
        print(f"🚨 {OutputLevel.CRITICAL.name}: Commit FAILED")
        print(f"   Error: {stderr or 'Unknown error'}")
        print(f"   Your work is NOT saved to git history")

        # Check for common issues
        if "nothing to commit" in stderr or "nothing to commit" in stdout:
            print(f"   Issue: No staged changes")
            print(f"   Note: Working directory may be clean")
            return True  # Not really a failure
        elif "Please tell me who you are" in stderr:
            print(f"   Issue: Git identity not configured")
            print(f"   Fix: Run 'git config user.email' and 'git config user.name'")
        elif "hook" in stderr.lower():
            print(f"   Issue: Git hook prevented commit")
            print(f"   Fix: Check .git/hooks/ or run with --no-verify")
        else:
            print(f"   Fix: Review error and run 'git commit' manually")

        # Show uncommitted changes count
        success2, stdout2, _ = run_command("git status --porcelain")
        if success2 and stdout2:
            count = len(stdout2.strip().split('\n'))
            print(f"   Uncommitted changes: {count} files")

        return False

    # Verify the commit succeeded
    verified, commit_sha, error = verify_commit()

    if not verified:
        print(f"🚨 {OutputLevel.CRITICAL.name}: Commit verification FAILED")
        print(f"   Error: {error}")
        print(f"   Your commit may not have been saved properly")
        return False

    # Success - commit verified
    print(f"✅ {OutputLevel.SUCCESS.name}: Commit successful")
    print(f"   Commit: {commit_sha}")
    print(f"   Message: {message[:50]}...")

    return True

def main():
    """Example usage"""
    import sys

    message = sys.argv[1] if len(sys.argv) > 1 else "chore: Save work"

    if safe_commit(message):
        print("✅ Work saved successfully")
        sys.exit(0)
    else:
        print("🚨 FAILED to save work - manual intervention required")
        sys.exit(1)

if __name__ == "__main__":
    main()