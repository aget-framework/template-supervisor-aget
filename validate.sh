#!/bin/bash

# my-AGET-template Validation Script
# Verifies your governance layer is properly configured

echo "════════════════════════════════════════════════════════"
echo "   my-AGET-template Validation"
echo "════════════════════════════════════════════════════════"
echo

ERRORS=0
WARNINGS=0

# Color codes
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check function
check() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $2"
    else
        echo -e "${RED}✗${NC} $2"
        ERRORS=$((ERRORS + 1))
    fi
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
    WARNINGS=$((WARNINGS + 1))
}

echo "Checking prerequisites..."
echo

# Check Python
python3 --version > /dev/null 2>&1
check $? "Python 3 installed"

# Check Git
git --version > /dev/null 2>&1
check $? "Git installed"

# Check shell
[ -n "$SHELL" ]
check $? "Shell environment available"

echo
echo "Checking required files..."
echo

# Check critical files
[ -f "AGENTS.md" ]
check $? "AGENTS.md exists"

[ -f "README.md" ]
check $? "README.md exists"

[ -f ".gitignore" ]
check $? ".gitignore exists"

[ -d ".aget" ]
check $? ".aget/ directory exists"

[ -d "patterns" ]
check $? "patterns/ directory exists"

[ -d "scripts" ]
check $? "scripts/ directory exists"

echo
echo "Checking scripts..."
echo

# Check script functionality
if [ -f "scripts/session_protocol.py" ]; then
    python3 scripts/session_protocol.py status > /dev/null 2>&1
    check $? "session_protocol.py works"
else
    check 1 "scripts/session_protocol.py exists"
fi

if [ -f "scripts/install_pattern.py" ]; then
    echo "import sys; sys.path.append('scripts'); import install_pattern" | python3 2>/dev/null
    check $? "install_pattern.py valid Python"
else
    check 1 "scripts/install_pattern.py exists"
fi

echo
echo "Checking patterns..."
echo

# Check patterns
if [ -f "patterns/documentation/smart_reader.py" ]; then
    python3 patterns/documentation/smart_reader.py README.md > /dev/null 2>&1
    check $? "smart_reader.py works"
else
    warn "patterns/documentation/smart_reader.py missing"
fi

echo
echo "Checking for placeholders..."
echo

# Check for uncustomized placeholders
if grep -r "{{" . --include="*.md" --include="AGENTS.md" 2>/dev/null | grep -v templates/ | grep -v ".git" > /dev/null; then
    warn "Uncustomized placeholders found (run ./setup.sh)"
    grep -r "{{" . --include="*.md" --include="AGENTS.md" 2>/dev/null | grep -v templates/ | grep -v ".git" | head -3
else
    echo -e "${GREEN}✓${NC} No uncustomized placeholders"
fi

echo
echo "Checking for personal data..."
echo

# Check for personal paths
if grep -r "/Users/aget-framework" . --include="*.py" --include="*.sh" --exclude-dir=".git" 2>/dev/null | grep -v "CLAUDE.md" > /dev/null; then
    warn "Personal paths found - consider making generic"
else
    echo -e "${GREEN}✓${NC} No hardcoded personal paths"
fi

echo
echo "Checking git status..."
echo

# Check git
if [ -d ".git" ]; then
    if git remote -v | grep -q origin; then
        echo -e "${GREEN}✓${NC} Git repository configured"
    else
        warn "No git remote configured"
    fi
else
    warn "Not a git repository"
fi

echo
echo "════════════════════════════════════════════════════════"
echo "Validation Complete"
echo "════════════════════════════════════════════════════════"
echo

if [ $ERRORS -eq 0 ]; then
    if [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ All checks passed!${NC}"
        echo "Your governance layer is ready to use."
    else
        echo -e "${GREEN}✅ Core functionality verified${NC}"
        echo -e "${YELLOW}$WARNINGS warnings found (non-critical)${NC}"
    fi
    exit 0
else
    echo -e "${RED}❌ $ERRORS errors found${NC}"
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}$WARNINGS warnings found${NC}"
    fi
    echo
    echo "Please fix errors before proceeding."
    exit 1
fi