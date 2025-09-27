# aget validate - Command Specification
*Testable principles for X-aget repositories*

## Command Overview
```bash
aget validate [path] [--principle=<name>] [--fix] [--strict]
```

## Core Validation Principles

### 1. Independence Principle
```bash
aget validate --principle=independence

PASS: ✅ Repository is self-contained
FAIL: ❌ External dependencies found:
      - /Users/aget-framework/github/scripts/session_protocol.py (line 45)
      - ../../../shared/utils.py (line 23)
```

### 2. Security Principle
```bash
aget validate --principle=security

Checking:
- No credentials in code
- .gitignore properly configured
- Secrets in .aget/secrets/ only
- No sensitive data in logs
```

### 3. Structure Principle
```bash
aget validate --principle=structure

Required directories:
✅ .aget/
✅ scripts/
✅ docs/
❌ products/ (missing)
❌ workspace/ (missing)
```

### 4. Session Principle
```bash
aget validate --principle=sessions

✅ wake up protocol defined
✅ wind down protocol defined
✅ sign off protocol defined
✅ scripts/session_protocol.py exists
```

## Implementation Strategy

### Phase 1: Shell Script (Immediate)
```bash
#!/bin/bash
# products/aget_validate.sh

validate_independence() {
    echo "Checking independence..."

    # Check for external absolute paths
    if grep -r "/Users/" . --exclude-dir=.git | grep -v "^#"; then
        echo "❌ Found absolute paths"
        return 1
    fi

    # Check for parent escapes
    if grep -r "\.\./\.\." . --exclude-dir=.git; then
        echo "❌ Found parent directory escapes"
        return 1
    fi

    echo "✅ Repository is independent"
    return 0
}
```

### Phase 2: Python Implementation (Beta.2)
```python
# src/aget_validate.py

class PrincipleValidator:
    """Base class for testable principles"""

    def validate(self, repo_path: Path) -> ValidationResult:
        """Returns (passed: bool, violations: List[str], fixes: List[str])"""
        pass

class IndependenceValidator(PrincipleValidator):
    def validate(self, repo_path: Path):
        violations = []

        # Check for external paths
        for file in repo_path.rglob("*"):
            if file.is_file():
                content = file.read_text()
                if "/Users/" in content and str(repo_path) not in content:
                    violations.append(f"External path in {file}")

        return ValidationResult(
            passed=len(violations) == 0,
            violations=violations,
            fixes=["Replace absolute paths with relative ones"]
        )
```

## Testable Principles Framework

### Principle Definition Format
```yaml
principle:
  name: "Independence"
  description: "Repository must be self-contained"

  tests:
    - name: "No external paths"
      command: "grep -r '/Users/' . --exclude-dir=.git"
      expect: "no output"

    - name: "Scripts exist locally"
      command: "test -f scripts/session_protocol.py"
      expect: "exit 0"

  violations:
    critical:
      - "External absolute path"
      - "Missing required script"
    warning:
      - "Symlink to external file"

  fixes:
    auto:
      - "Copy external scripts locally"
      - "Update paths in configuration"
    manual:
      - "Review security implications"
```

### Validation Levels

| Level | Description | Example |
|-------|-------------|---------|
| CRITICAL | Breaks independence | External paths |
| ERROR | Violates principle | Missing structure |
| WARNING | Could cause issues | Large files |
| INFO | Best practice | Documentation gaps |

## Auto-Fix Capabilities

```bash
aget validate --fix

🔧 Auto-fixing violations...
✅ Copied session_protocol.py to scripts/
✅ Updated 3 paths in AGENTS.md
⚠️  Manual review needed for Makefile:45
```

## Integration Points

### 1. On Creation
```bash
aget create my-new-aget
Running validation...
✅ All principles passed
```

### 2. Pre-Commit Hook
```bash
# .git/hooks/pre-commit
aget validate --principle=security,independence
```

### 3. CI/CD Pipeline
```yaml
# .github/workflows/validate.yml
- name: Validate AGET principles
  run: aget validate --strict
```

## Success Metrics

- **Adoption**: Used by 80% of X-aget repos
- **Prevention**: 0 dependency violations in new repos
- **Fix Rate**: 90% of violations auto-fixable
- **Speed**: Full validation < 2 seconds

## Timeline

- **Now**: Document principle, create products/
- **Saturday**: Include validation checklist in release
- **Beta.2**: Ship basic `aget validate` command
- **v2.0**: Full auto-fix capabilities

---
*Specification Created: 2025-09-26*
*Target Release: v2.0.0-beta.2*