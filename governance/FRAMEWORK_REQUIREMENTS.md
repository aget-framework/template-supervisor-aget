# AGET Framework Requirements

## Purpose
This document captures framework-level requirements discovered through real usage that should be incorporated into the public AGET template.

## Status
Requirements here are discovered through experience in aget-aget and graduate to aget-cli-agent-template when validated.

## Discovered Requirements

### 1. Repository Visibility Decision (2025-09-25)
**Source**: OpenAI_DeepResearch-aget accidentally public
**Status**: Validated, needs implementation in template

Before creating any AGET, explicitly decide visibility:
- **DEFAULT TO PRIVATE** for organizational/research projects
- Consider: Is this competitive/sensitive/proprietary?
- Public only if: Educational value AND no sensitive content

**Implementation Ideas**:
- Add `--visibility` flag with private default
- Require explicit `--public` flag for public repos
- Add confirmation prompt for public organizational repos

### 2. Repository Planning (2025-09-25)
**Source**: DeepResearch-aget creation session
**Status**: Validated, needs implementation in template

Before creating any AGET, the framework must prompt for:
1. **WHERE** - GitHub? GitLab? Bitbucket? Local only?
2. **VISIBILITY** - Public or private?
3. **ACCOUNT** - Personal or organization?
4. **NAME** - Exact repository name
5. **TIMING** - Create remote first or after scaffolding?

**Implementation Ideas**:
- Add interactive prompt during `aget create`
- Or add `--repo-url` flag to specify upfront
- Template should include repository setup instructions

### 2. User Prerequisites (2025-09-25)
**Source**: Implicit assumptions discovered during sessions
**Status**: Documented, needs template integration

Users must have:
- Git configured (user.name, user.email)
- GitHub CLI installed and authenticated (for GitHub repos)
- Python 3.8+ installed
- Basic command line proficiency

**Implementation Ideas**:
- Add prerequisite checker to AGET CLI
- Create `aget doctor` command to verify setup
- Include in getting started guide

## Process for New Requirements

When discovering new framework requirements:

1. **Capture** in this file immediately
2. **Document** the source (which session/agent discovered it)
3. **Validate** through usage
4. **Graduate** to template when proven
5. **Track** implementation status

## Tracking Implementation

| Requirement | Discovered | Validated | In Template | Priority | Notes |
|-------------|------------|-----------|-------------|----------|-------|
| Repository Visibility | 2025-09-25 | ✅ | ❌ | P1 | Default to private |
| Repository Planning | 2025-09-25 | ✅ | ❌ | P2 | Needs CLI enhancement |
| User Prerequisites | 2025-09-25 | ✅ | ❌ | P2 | Needs doctor command |
| Auto-Activation | 2025-09-26 | ✅ | ❌ | P1 | Critical for UX |
| Identity Config | 2025-09-26 | ✅ | ❌ | P1 | .aget/identity.json |
| Post-Migration Verify | 2025-09-26 | ✅ | ❌ | P1 | verify_migration.sh |
| Seed Evolution | 2025-09-26 | ✅ | ❌ | P2 | Initial data required |
| Credential Management | 2025-09-26 | ✅ | ❌ | P1 | Security critical |
| Secrets Manifest | 2025-09-26 | ✅ | ❌ | P2→P1 | .aget/secrets.yaml |

### 3. Auto-Activation During Migration (2025-09-26)
**Source**: RKB_infra-aget migration experience
**Status**: Critical gap discovered, needs urgent implementation

Migration creates AGENTS_ENHANCED.md but doesn't activate it, leading to:
- User confusion (migration "complete" but agent not working)
- Generic responses instead of agent personality
- Manual activation steps required

**Implementation Required**:
- Auto-replace AGENTS.md at migration end
- Create backup as AGENTS_ORIGINAL.md
- Verify activation succeeded
- Show agent greeting to confirm

### 4. Identity Configuration Standard (2025-09-26)
**Source**: InfraGuard had personality but no standard storage
**Status**: Pattern identified, needs standardization

Need `.aget/identity.json` for consistent personality:
```json
{
  "name": "AgentName",
  "greeting": "Custom greeting",
  "personality": ["traits"],
  "mission": "Clear mission statement"
}
```

### 5. Post-Migration Verification (2025-09-26)
**Source**: No way to verify InfraGuard migration success
**Status**: Critical gap, needs implementation

Need `verify_migration.sh` that checks:
- AGET structure exists
- Identity is active
- Evolution tracking works
- Agent responds with personality

### 6. Seed Evolution Data (2025-09-26)
**Source**: InfraGuard evolution directories empty
**Status**: Reduces value, needs fixing

Migration should seed with:
- Baseline state
- Known issues
- Initial discoveries
- Historical data if available

### 7. Standardized Credential Management (2025-09-26)
**Source**: RKB_analytics-aget GA4 key setup pattern
**Status**: Critical security pattern, needs standardization

All AGETs need consistent credential management:
- **Standard location**: `.aget/secrets/` directory
- **Permissions**: 600 for files, 700 for directory
- **Git safety**: Comprehensive .gitignore mandatory
- **Documentation**: README.md in secrets with setup instructions
- **Rotation**: 90-day default with reminders

**Implementation Required**:
```bash
# Standard structure in every AGET
.aget/secrets/
├── .gitignore      # Critical: ignore all secrets
├── README.md       # Document each credential
└── [credentials]   # Actual keys with 600 perms
```

**Security Requirements**:
- Never commit credentials (even encrypted)
- Use read-only permissions when possible
- Document rotation schedule
- Include incident response plan
- Test credentials after setup

### 8. Secrets Manifest Declaration (2025-09-26)
**Source**: RKB_analytics-aget credential setup friction
**Status**: Usability enhancement, optional in v2, standard in v3

Add `.aget/secrets.yaml` to declare credential requirements:
- **Declaration**: What secrets the agent needs
- **Validation**: Commands to verify secrets work
- **Guidance**: URLs and instructions for setup
- **Tracking**: Rotation schedules and status

**Implementation Phases**:
1. **v2 Nudge** (immediate): Optional YAML with validation script
2. **v2.1** (next release): Include in template
3. **v3.0** (future): Full CLI integration with `aget secrets` commands

**Benefits**:
- Users know requirements upfront
- Validation before runtime
- Setup guidance included
- Rotation tracking automated

**Example Structure**:
```yaml
required:
  - name: ga4_credentials
    type: service_account
    path: .aget/secrets/ga4_credentials.json
    permissions: "600"
    setup_url: "https://console.cloud.google.com"
    rotation_days: 90
```

## Future Discoveries Go Here

(This section will grow as we discover more requirements)

---
*This is a living document that bridges discovery in aget-aget to implementation in aget-cli-agent-template*