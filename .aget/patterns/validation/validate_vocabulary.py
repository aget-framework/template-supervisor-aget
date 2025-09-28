#!/usr/bin/env python3
"""
Validate that code and documentation comply with controlled vocabulary.

This tool checks that an agent's implementation uses terms consistently
with its declared controlled vocabulary and business rules.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class VocabularyValidator:
    """Validates usage against controlled vocabulary."""

    def __init__(self, vocab_file: Path = None, rules_file: Path = None):
        """Initialize validator with vocabulary and rules files."""
        self.project_root = Path.cwd()
        self.vocab_file = vocab_file or self.project_root / "CONTROLLED_VOCABULARY.md"
        self.rules_file = rules_file or self.project_root / "BUSINESS_RULES.md"

        self.vocabulary = self._load_vocabulary()
        self.rules = self._load_rules()
        self.violations = []

    def _load_vocabulary(self) -> Dict:
        """Load controlled vocabulary from markdown file."""
        vocab = {
            'entities': {},
            'actions': {},
            'states': {},
            'distinctions': {},
            'deprecated': set()
        }

        if not self.vocab_file.exists():
            return vocab

        content = self.vocab_file.read_text()

        # Extract entities
        entity_pattern = r'#### Entity: (\w+).*?- \*\*Technical Term\*\*: (.*?)\n'
        for match in re.finditer(entity_pattern, content, re.DOTALL):
            entity = match.group(1)
            formal_name = match.group(2)
            vocab['entities'][entity] = formal_name

        # Extract actions
        action_pattern = r'#### Action: (\w+).*?- \*\*Technical Term\*\*: (.*?)\n'
        for match in re.finditer(action_pattern, content, re.DOTALL):
            action = match.group(1)
            formal_name = match.group(2)
            vocab['actions'][action] = formal_name

        # Extract states
        state_pattern = r'#### State: (\w+)'
        for match in re.finditer(state_pattern, content):
            state = match.group(1)
            vocab['states'][state] = state

        # Extract critical distinctions
        distinction_pattern = r'### (.*?) vs (.*?)\n'
        for match in re.finditer(distinction_pattern, content):
            term_a = match.group(1)
            term_b = match.group(2)
            vocab['distinctions'][(term_a, term_b)] = True

        # Extract deprecated terms
        deprecated_pattern = r'\| (.*?) \| .* \| (.*?) \|'
        deprecated_section = re.search(r'### Deprecated Terms.*?(?=##|\Z)', content, re.DOTALL)
        if deprecated_section:
            for match in re.finditer(deprecated_pattern, deprecated_section.group(0)):
                old_term = match.group(1)
                vocab['deprecated'].add(old_term)

        return vocab

    def _load_rules(self) -> Dict:
        """Load business rules from markdown file."""
        rules = {}

        if not self.rules_file.exists():
            return rules

        content = self.rules_file.read_text()

        # Extract rules with their IDs
        rule_pattern = r'### (BR-\d+): (.*?)\n\*\*Rule\*\*: (.*?)\n'
        for match in re.finditer(rule_pattern, content):
            rule_id = match.group(1)
            rule_name = match.group(2)
            rule_text = match.group(3)
            rules[rule_id] = {
                'name': rule_name,
                'text': rule_text
            }

        return rules

    def validate_file(self, file_path: Path) -> List[str]:
        """Validate a single file against vocabulary."""
        violations = []

        if not file_path.exists():
            return violations

        content = file_path.read_text()
        lines = content.split('\n')

        # Check for deprecated terms
        for term in self.vocabulary['deprecated']:
            for i, line in enumerate(lines, 1):
                if term in line:
                    violations.append(
                        f"{file_path}:{i} - Deprecated term '{term}' found"
                    )

        # Check for inconsistent casing of entities
        for entity, formal in self.vocabulary['entities'].items():
            # Look for incorrect casing
            wrong_patterns = [
                entity.lower(),  # all lowercase when should be capital
                entity.upper(),  # all uppercase
            ]
            for pattern in wrong_patterns:
                if pattern != formal and pattern in content.lower():
                    for i, line in enumerate(lines, 1):
                        if pattern in line.lower():
                            violations.append(
                                f"{file_path}:{i} - Incorrect casing: "
                                f"'{pattern}' should be '{formal}'"
                            )

        # Check naming conventions
        if file_path.suffix == '.py':
            violations.extend(self._validate_python_naming(file_path, lines))

        return violations

    def _validate_python_naming(self, file_path: Path, lines: List[str]) -> List[str]:
        """Validate Python naming conventions."""
        violations = []

        # Check function names match action vocabulary
        function_pattern = r'^def (\w+)\('
        for i, line in enumerate(lines, 1):
            match = re.match(function_pattern, line.strip())
            if match:
                func_name = match.group(1)
                # Check if it's an action and follows naming convention
                if '_' in func_name:
                    parts = func_name.split('_')
                    verb = parts[0]
                    # Check if verb is in our actions vocabulary
                    if verb not in ['get', 'set', 'is', 'has', 'do']:  # Common verbs
                        if verb not in [a.lower() for a in self.vocabulary['actions'].keys()]:
                            violations.append(
                                f"{file_path}:{i} - Function '{func_name}' uses "
                                f"unrecognized action verb '{verb}'"
                            )

        # Check class names match entity vocabulary
        class_pattern = r'^class (\w+)[\(:]'
        for i, line in enumerate(lines, 1):
            match = re.match(class_pattern, line.strip())
            if match:
                class_name = match.group(1)
                # Check if it matches an entity pattern
                if not class_name.startswith('_'):  # Skip private classes
                    found = False
                    for entity in self.vocabulary['entities'].keys():
                        if entity in class_name:
                            found = True
                            break
                    if not found and class_name not in ['Test', 'Base', 'Abstract']:
                        violations.append(
                            f"{file_path}:{i} - Class '{class_name}' doesn't match "
                            f"any known entity pattern"
                        )

        return violations

    def validate_project(self) -> Tuple[bool, List[str]]:
        """Validate entire project against vocabulary."""
        all_violations = []

        # Check Python files
        for py_file in self.project_root.glob('**/*.py'):
            if '.aget' not in str(py_file):  # Skip framework files
                violations = self.validate_file(py_file)
                all_violations.extend(violations)

        # Check Markdown documentation
        for md_file in self.project_root.glob('**/*.md'):
            if md_file != self.vocab_file and md_file != self.rules_file:
                violations = self.validate_file(md_file)
                all_violations.extend(violations)

        return len(all_violations) == 0, all_violations

    def generate_report(self) -> str:
        """Generate validation report."""
        is_valid, violations = self.validate_project()

        report = [
            "=" * 60,
            "VOCABULARY COMPLIANCE REPORT",
            "=" * 60,
            f"Timestamp: {datetime.now().isoformat()}",
            f"Project: {self.project_root.name}",
            f"Vocabulary File: {self.vocab_file.name if self.vocab_file.exists() else 'NOT FOUND'}",
            f"Rules File: {self.rules_file.name if self.rules_file.exists() else 'NOT FOUND'}",
            "",
        ]

        if is_valid:
            report.extend([
                "✅ VALIDATION PASSED",
                "",
                "No vocabulary violations found.",
            ])
        else:
            report.extend([
                "❌ VALIDATION FAILED",
                "",
                f"Found {len(violations)} violations:",
                "",
            ])

            # Group violations by file
            by_file = {}
            for violation in violations:
                file_part = violation.split(':')[0]
                if file_part not in by_file:
                    by_file[file_part] = []
                by_file[file_part].append(violation)

            for file_path, file_violations in by_file.items():
                report.append(f"\n{file_path}:")
                for violation in file_violations:
                    report.append(f"  - {violation}")

        report.extend([
            "",
            "=" * 60,
            "",
            "VOCABULARY STATISTICS",
            "-" * 40,
            f"Entities: {len(self.vocabulary['entities'])}",
            f"Actions: {len(self.vocabulary['actions'])}",
            f"States: {len(self.vocabulary['states'])}",
            f"Distinctions: {len(self.vocabulary['distinctions'])}",
            f"Deprecated Terms: {len(self.vocabulary['deprecated'])}",
            f"Business Rules: {len(self.rules)}",
            "",
            "=" * 60,
        ])

        return '\n'.join(report)

    def suggest_fixes(self, violations: List[str]) -> List[str]:
        """Suggest fixes for violations."""
        suggestions = []

        for violation in violations:
            if 'Deprecated term' in violation:
                # Extract the deprecated term
                term = re.search(r"term '(.*?)'", violation).group(1)
                suggestions.append(
                    f"Replace '{term}' with updated terminology "
                    f"(check CONTROLLED_VOCABULARY.md for replacement)"
                )
            elif 'Incorrect casing' in violation:
                # Extract the correction
                match = re.search(r"'(.*?)' should be '(.*?)'", violation)
                if match:
                    wrong = match.group(1)
                    right = match.group(2)
                    suggestions.append(f"Change '{wrong}' to '{right}'")
            elif 'unrecognized action verb' in violation:
                verb = re.search(r"verb '(.*?)'", violation).group(1)
                suggestions.append(
                    f"Either add '{verb}' to controlled vocabulary "
                    f"or use a recognized action verb"
                )

        return suggestions


def main():
    """Main entry point for vocabulary validation."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate project against controlled vocabulary'
    )
    parser.add_argument(
        '--vocab',
        type=Path,
        help='Path to controlled vocabulary file'
    )
    parser.add_argument(
        '--rules',
        type=Path,
        help='Path to business rules file'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Suggest fixes for violations'
    )
    parser.add_argument(
        '--ci',
        action='store_true',
        help='CI mode - exit with error code on violations'
    )

    args = parser.parse_args()

    # Initialize validator
    validator = VocabularyValidator(
        vocab_file=args.vocab,
        rules_file=args.rules
    )

    # Generate report
    report = validator.generate_report()
    print(report)

    # Check if validation passed
    is_valid, violations = validator.validate_project()

    # Suggest fixes if requested
    if args.fix and not is_valid:
        print("\nSUGGESTED FIXES:")
        print("-" * 40)
        suggestions = validator.suggest_fixes(violations)
        for suggestion in suggestions:
            print(f"• {suggestion}")

    # Exit with appropriate code for CI
    if args.ci and not is_valid:
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()