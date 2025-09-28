#!/usr/bin/env python3
"""
release_quality_check.py - Pre-release quality gate for AGET repositories

Ensures repositories maintain clean structure and follow best practices
before any release. Run this as part of CI/CD or pre-release checklist.

Usage:
    python3 release_quality_check.py           # Check current directory
    python3 release_quality_check.py --strict  # Fail on warnings
    python3 release_quality_check.py --fix     # Auto-fix issues where possible

Exit codes:
    0 - All checks passed
    1 - Critical issues found
    2 - Warnings found (in strict mode)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime

# Maximum files allowed in root for different repo types
MAX_ROOT_FILES = {
    'strict': 10,      # Ultra-clean
    'standard': 15,    # Normal project
    'relaxed': 20      # Complex project
}

# Essential files that SHOULD be in root
REQUIRED_ROOT_FILES = [
    'README.md',
    'LICENSE',
    'CHANGELOG.md'
]

# Files that CAN be in root
ALLOWED_ROOT_FILES = [
    'README.md',
    'LICENSE',
    'LICENSE.md',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'AUTHORS',
    'AUTHORS.md',
    'CITATION.cff',
    'AGENTS.md',
    'CLAUDE.md',
    'PREREQUISITES.md',
    'UPGRADING.md',
    'INSTALL.md',
    '.gitignore',
    '.gitattributes',
    'Makefile',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'requirements.txt',
    'package.json',
    'package-lock.json',
    'Cargo.toml',
    'Cargo.lock',
    'go.mod',
    'go.sum',
    'VERSION',
    'version.txt'
]

# Patterns that suggest files should be moved
SUSPICIOUS_PATTERNS = {
    'sessions': ['SESSION_*.md', 'CHECKPOINT_*.md'],
    'planning': ['*_PLAN.md', '*_STATUS.md', '*_REPORT.md', '*TODO*.md'],
    'archive': ['*_OLD.md', '*_BACKUP.md', '*_DEPRECATED.md'],
    'internal': ['*_INTERNAL.md', '*_PRIVATE.md', '*_NOTES.md']
}

# Best practices to check
BEST_PRACTICES = {
    'has_readme': 'README.md must exist and be non-empty',
    'has_license': 'LICENSE or LICENSE.md must exist',
    'has_gitignore': '.gitignore must exist',
    'has_changelog': 'CHANGELOG.md recommended for versioned projects',
    'has_contributing': 'CONTRIBUTING.md recommended for open source',
    'has_security': 'SECURITY.md recommended for public repos',
    'docs_organized': 'Documentation should be in docs/ directory',
    'tests_organized': 'Tests should be in tests/ or test/ directory',
    'clean_root': f'Root should have fewer than {MAX_ROOT_FILES["standard"]} files'
}

class ReleaseQualityChecker:
    def __init__(self, path: Path = None, mode: str = 'standard'):
        self.root = Path(path) if path else Path.cwd()
        self.mode = mode
        self.max_files = MAX_ROOT_FILES[mode]
        self.issues = {'critical': [], 'warning': [], 'info': []}
        self.stats = {}

    def check_all(self) -> Dict:
        """Run all quality checks"""
        print(f"🔍 Release Quality Check - {self.root.name}")
        print(f"Mode: {self.mode} (max {self.max_files} root files)")
        print("-" * 50)

        # Run checks
        self.check_root_cleanliness()
        self.check_required_files()
        self.check_suspicious_files()
        self.check_best_practices()
        self.check_documentation_structure()

        # Generate report
        return self.generate_report()

    def check_root_cleanliness(self) -> None:
        """Check if root directory is clean"""
        root_files = list(self.root.glob('*'))
        # Only count visible files (not starting with .)
        visible_files = [f for f in root_files if not f.name.startswith('.') and f.is_file()]
        md_files = list(self.root.glob('*.md'))

        self.stats['total_root_files'] = len(root_files)
        self.stats['visible_root_files'] = len(visible_files)
        self.stats['md_in_root'] = len(md_files)

        # Check total count
        if len(visible_files) > self.max_files:
            self.issues['critical'].append(
                f"Root has {len(visible_files)} visible files (max: {self.max_files})"
            )

        # Check for too many .md files
        if len(md_files) > 10:
            self.issues['warning'].append(
                f"Root has {len(md_files)} .md files (recommended: <10)"
            )

        # Check for files that shouldn't be in root
        for file in root_files:
            if file.is_file() and file.name not in ALLOWED_ROOT_FILES:
                # Check if it matches suspicious patterns
                for category, patterns in SUSPICIOUS_PATTERNS.items():
                    for pattern in patterns:
                        if self._matches_pattern(file.name, pattern):
                            self.issues['warning'].append(
                                f"{file.name} should be in {category}/ directory"
                            )
                            break

    def check_required_files(self) -> None:
        """Check for required files"""
        for required in REQUIRED_ROOT_FILES:
            path = self.root / required
            if not path.exists():
                self.issues['critical'].append(f"Missing required file: {required}")
            elif path.stat().st_size == 0:
                self.issues['warning'].append(f"{required} is empty")

    def check_suspicious_files(self) -> None:
        """Check for files that suggest poor organization"""
        suspicious_count = 0

        for file in self.root.glob('*.md'):
            for category, patterns in SUSPICIOUS_PATTERNS.items():
                for pattern in patterns:
                    if self._matches_pattern(file.name, pattern):
                        suspicious_count += 1

        if suspicious_count > 3:
            self.issues['warning'].append(
                f"Found {suspicious_count} files that should be organized into subdirectories"
            )

    def check_best_practices(self) -> None:
        """Check for best practice adherence"""

        # Check for README
        if not (self.root / 'README.md').exists():
            self.issues['critical'].append(BEST_PRACTICES['has_readme'])

        # Check for LICENSE
        if not ((self.root / 'LICENSE').exists() or (self.root / 'LICENSE.md').exists()):
            self.issues['critical'].append(BEST_PRACTICES['has_license'])

        # Check for .gitignore
        if not (self.root / '.gitignore').exists():
            self.issues['warning'].append(BEST_PRACTICES['has_gitignore'])

        # Check for CONTRIBUTING.md in open source repos
        if (self.root / '.github').exists() and not (self.root / 'CONTRIBUTING.md').exists():
            self.issues['info'].append(BEST_PRACTICES['has_contributing'])

    def check_documentation_structure(self) -> None:
        """Check if documentation is well organized"""
        docs_dir = self.root / 'docs'

        # Count docs in root vs organized
        root_docs = len(list(self.root.glob('*.md')))
        organized_docs = len(list(docs_dir.glob('**/*.md'))) if docs_dir.exists() else 0

        self.stats['root_docs'] = root_docs
        self.stats['organized_docs'] = organized_docs

        if root_docs > 10 and organized_docs < root_docs / 2:
            self.issues['warning'].append(
                f"Documentation poorly organized: {root_docs} in root, {organized_docs} in docs/"
            )

    def _matches_pattern(self, filename: str, pattern: str) -> bool:
        """Check if filename matches a glob pattern"""
        from fnmatch import fnmatch
        return fnmatch(filename, pattern)

    def generate_report(self) -> Dict:
        """Generate quality report"""
        total_issues = (
            len(self.issues['critical']) +
            len(self.issues['warning']) +
            len(self.issues['info'])
        )

        # Print report
        print("\n📊 Statistics:")
        print(f"  Total files in root: {self.stats.get('total_root_files', 0)}")
        print(f"  Visible files in root: {self.stats.get('visible_root_files', 0)}")
        print(f"  Markdown files in root: {self.stats.get('md_in_root', 0)}")
        print(f"  Organized docs: {self.stats.get('organized_docs', 0)}")

        print("\n🚨 Issues Found:")
        if self.issues['critical']:
            print("\n❌ CRITICAL:")
            for issue in self.issues['critical']:
                print(f"  - {issue}")

        if self.issues['warning']:
            print("\n⚠️  WARNING:")
            for issue in self.issues['warning']:
                print(f"  - {issue}")

        if self.issues['info']:
            print("\n💡 INFO:")
            for issue in self.issues['info']:
                print(f"  - {issue}")

        # Overall status
        if self.issues['critical']:
            status = 'FAILED'
            emoji = '❌'
        elif self.issues['warning']:
            status = 'PASSED WITH WARNINGS'
            emoji = '⚠️'
        else:
            status = 'PASSED'
            emoji = '✅'

        print(f"\n{emoji} Release Quality: {status}")

        # Recommendations
        if total_issues > 0:
            print("\n📋 Recommendations:")
            if self.stats.get('md_in_root', 0) > 10:
                print("  1. Run: python3 .aget/patterns/organization/organize_docs.py --execute")
            if 'Missing required file: README.md' in str(self.issues):
                print("  2. Create a comprehensive README.md")
            if 'Missing required file: LICENSE' in str(self.issues):
                print("  3. Add a LICENSE file")

        return {
            'status': status,
            'stats': self.stats,
            'issues': self.issues,
            'total_issues': total_issues
        }

    def auto_fix(self) -> None:
        """Attempt to auto-fix common issues"""
        print("\n🔧 Attempting auto-fixes...")

        # Create missing directories
        for dir_name in ['docs', 'tests', 'sessions', '.aget/checkpoints']:
            dir_path = self.root / dir_name
            if not dir_path.exists():
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"  ✓ Created {dir_name}/")

        # Run organize_docs if available
        organize_script = self.root / '.aget/patterns/organization/organize_docs.py'
        if organize_script.exists() and self.stats.get('md_in_root', 0) > 10:
            print("  ✓ Running organize_docs.py...")
            os.system(f"python3 {organize_script} --execute")


def main():
    parser = argparse.ArgumentParser(
        description='Pre-release quality check for repositories'
    )
    parser.add_argument(
        '--mode',
        choices=['strict', 'standard', 'relaxed'],
        default='standard',
        help='Checking mode (affects thresholds)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Fail on warnings as well as critical issues'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Attempt to auto-fix issues'
    )
    parser.add_argument(
        '--path',
        type=str,
        help='Repository path (default: current directory)'
    )

    args = parser.parse_args()

    # Run checks
    checker = ReleaseQualityChecker(args.path, args.mode)

    if args.fix:
        checker.auto_fix()

    report = checker.check_all()

    # Determine exit code
    if report['issues']['critical']:
        sys.exit(1)
    elif args.strict and report['issues']['warning']:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()