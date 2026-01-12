#!/bin/zsh
# ============================================================
# Supervisor Agent Shell Profile
# ============================================================
# Template: template-supervisor-aget
# Version: 3.3.0
#
# DOCUMENTATION
# -------------
# Shell README:    ./shell/README.md
# Template Spec:   ./specs/Supervisor_SPEC.md
# Template Vocab:  ./specs/Supervisor_VOCABULARY.md
# Agent Config:    ./AGENTS.md
# Framework Spec:  aget/specs/AGET_TEMPLATE_SPEC.md (CAP-TPL-014)
#
# USAGE
# -----
# 1. Set AGET_AGENT_DIR to your agent root directory
# 2. Source this file: source shell/supervisor_profile.zsh
# 3. Use aget_* functions for common operations
#
# CUSTOMIZATION
# -------------
# When instantiating this template:
# 1. Update AGET_AGENT_NAME to your agent name
# 2. Add domain-specific helper functions
# 3. Configure fleet registry path
# ============================================================

# ============================================================
# CONFIGURATION - Update these when instantiating
# ============================================================
export AGET_AGENT_NAME="${AGET_AGENT_NAME:-template-supervisor-aget}"
export AGET_ARCHETYPE="supervisor"
export AGET_VERSION="3.3.0"

# Agent directory (set before sourcing, or defaults to script location)
export AGET_AGENT_DIR="${AGET_AGENT_DIR:-$(dirname $(dirname ${(%):-%x}))}"

# ============================================================
# PATHS - Derived from AGET_AGENT_DIR
# ============================================================
export AGET_SPEC="${AGET_AGENT_DIR}/specs/Supervisor_SPEC.md"
export AGET_VOCAB="${AGET_AGENT_DIR}/specs/Supervisor_VOCABULARY.md"
export AGET_CONFIG="${AGET_AGENT_DIR}/AGENTS.md"
export AGET_PLANNING="${AGET_AGENT_DIR}/planning"
export AGET_SESSIONS="${AGET_AGENT_DIR}/sessions"
export AGET_EVOLUTION="${AGET_AGENT_DIR}/.aget/evolution"

# Supervisor-specific: fleet registry
export AGET_FLEET_REGISTRY="${AGET_AGENT_DIR}/.aget/registry/FLEET_REGISTRY.yaml"

# ============================================================
# HELPER FUNCTIONS
# ============================================================

# Display agent info and documentation paths
aget_info() {
    cat <<EOF
Agent: ${AGET_AGENT_NAME}
Archetype: ${AGET_ARCHETYPE}
Version: ${AGET_VERSION}

Documentation:
  Config:     ${AGET_CONFIG}
  Spec:       ${AGET_SPEC}
  Vocabulary: ${AGET_VOCAB}

Directories:
  Root:       ${AGET_AGENT_DIR}
  Planning:   ${AGET_PLANNING}
  Sessions:   ${AGET_SESSIONS}
  Evolution:  ${AGET_EVOLUTION}

Supervisor-Specific:
  Fleet:      ${AGET_FLEET_REGISTRY}
EOF
}

# Quick session start
aget_session_start() {
    echo "Starting ${AGET_ARCHETYPE} session..."
    aget_info
    echo ""
    echo "Tip: Use 'wake up' in Claude Code to initialize session"
}

# Open documentation
aget_docs() {
    local doc="${1:-config}"
    case "${doc}" in
        config|agents) open "${AGET_CONFIG}" ;;
        spec)          open "${AGET_SPEC}" ;;
        vocab)         open "${AGET_VOCAB}" ;;
        readme)        open "${AGET_AGENT_DIR}/README.md" ;;
        fleet)         open "${AGET_FLEET_REGISTRY}" ;;
        *)             echo "Usage: aget_docs [config|spec|vocab|readme|fleet]" ;;
    esac
}

# Fleet status check (supervisor-specific)
aget_fleet_status() {
    echo "Fleet Status for ${AGET_AGENT_NAME}"
    echo "=================================="
    if [[ -f "${AGET_FLEET_REGISTRY}" ]]; then
        cat "${AGET_FLEET_REGISTRY}"
    else
        echo "No fleet registry found at ${AGET_FLEET_REGISTRY}"
    fi
}

# ============================================================
# PROFILE ACTIVATION
# ============================================================
echo "Profile loaded: ${AGET_AGENT_NAME} v${AGET_VERSION}"
echo "Type 'aget_info' for documentation paths"
