# AGET v2.0 Reference Manifest

## Official Template Version
**Version**: 2.0.0
**Status**: Production Ready
**Compliance**: 96% (24/25 checks passing)
**Last Updated**: 2025-09-28

## Required Directory Structure

```
.aget/                      # Framework metadata and configuration
├── patterns/               # ALL patterns must be here (not in root)
│   ├── session/           # Session management patterns
│   ├── github/            # GitHub integration patterns
│   ├── routing/           # Agent discovery and coordination
│   ├── quality/           # Quality and release checks
│   ├── validation/        # Compliance and validation tools
│   └── documentation/     # Documentation utilities
├── evolution/             # Decision and discovery tracking
├── checkpoints/           # Agent state snapshots
├── migrations/            # Migration artifacts
└── version.json          # Version and metadata

sessions/                  # Session notes (NOT SESSION_NOTES/)
workspace/                 # Agent's private workspace
products/                  # Public products maintained
data/                      # Persistent data storage
docs/                      # Documentation
tests/                     # Test suite
src/                       # Agent source code
```

## Required Core Patterns

### Session Management (Priority 1)
- ✅ `session/wake_up.py` - Initialize session, show status
- ✅ `session/wind_down.py` - Save work with commits
- ✅ `session/wind_down_safe.py` - Quick exit without commits
- ✅ `session/commit_verification.py` - Verify commit safety

### GitHub Integration (Priority 1)
- ✅ `github/create_issue.py` - Create issues with severity/type detection
- ✅ `github/list_issues.py` - List and dashboard view
- ✅ `github/update_issue.py` - Update issues and labels
- ✅ `github/setup_labels.py` - Configure label schema
- ✅ `github/migrate_issues.py` - Migrate issues between repos
- ✅ `github/label_schema.md` - Label documentation

### Agent Coordination (Priority 1)
- ✅ `routing/agent_discovery.py` - Discover agents and capabilities

### Quality Assurance (Priority 2)
- ✅ `quality/release_quality_check.py` - Pre-release validation
- ✅ `validation/v2_compliance_check.py` - v2.0 compliance verification
- ✅ `validation/validate_vocabulary.py` - Vocabulary consistency

### Documentation (Priority 2)
- ✅ `documentation/smart_reader.py` - Efficient document reading

### Template Patterns (Priority 3)
- ✅ Various patterns for governance, naming, safety, security

## Required Protocols in CLAUDE.md

1. **Session Management Protocols**
   - Wake up protocol (respond to "wake up" or "hey")
   - Wind down protocol (save work on "wind down")
   - Sign off protocol (quick exit on "sign off")

2. **Substantial Change Protocol**
   - Use go/no-go gated approach for major changes
   - Present plan before implementation
   - Wait for approval at each gate

3. **GitHub Issues Integration**
   - Hub repository: `aget-framework/aget`
   - Use agent prefix in issue titles
   - Apply severity and type labels

4. **Efficiency Rules**
   - Use Task tool for >3 similar operations
   - Batch operations when possible
   - Use local patterns (self-contained per ARCH-001)

5. **Directory Documentation**
   - Clear explanation of v2.0 structure
   - Pattern location: `.aget/patterns/`
   - Vocabulary notes (workspace vs products)

## Version Requirements

### version.json Structure
```json
{
  "aget_version": "2.0.0",
  "created": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "template": "agent",
  "tier": "basic|standard|advanced",
  "migration_from": "previous_version"
}
```

## Compliance Criteria

Run `python3 .aget/patterns/validation/v2_compliance_check.py` to verify:

### Must Pass (Critical)
- [x] Version 2.0.0 in version.json
- [x] All patterns in `.aget/patterns/`
- [x] No root `patterns/` directory
- [x] Essential directories exist
- [x] Core patterns installed
- [x] CLAUDE.md has required protocols

### Should Pass (Important)
- [x] GitHub CLI available
- [x] Self-contained patterns (ARCH-001)
- [x] 10+ patterns installed
- [x] Session patterns functional

### Nice to Have
- [x] 15+ patterns for full functionality
- [x] Quality checks passing
- [x] Agent discovery working

## Migration Path

For agents migrating to v2.0:

1. **From v1.x or no version**
   - Full migration required
   - Move patterns to `.aget/patterns/`
   - Update CLAUDE.md

2. **From v2.0.0-alpha**
   - Pattern relocation needed
   - Protocol updates in CLAUDE.md
   - Version update to 2.0.0

3. **From v2.0.0-beta**
   - Minor adjustments only
   - Verify compliance

## Pattern Development Guidelines

When creating new patterns:

1. **Location**: Always in `.aget/patterns/category/`
2. **Self-contained**: No external dependencies (ARCH-001)
3. **Documentation**: Include docstrings and help
4. **Testing**: Provide test examples
5. **CLI**: Include command-line interface when applicable

## Template Usage

This template serves as:
- **Reference Implementation**: The official v2.0 structure
- **Migration Target**: What agents should achieve
- **Pattern Library**: Battle-tested patterns ready to use
- **Compliance Standard**: Use compliance checker to verify

To create a new agent from this template:
```bash
# Copy template
cp -r my-AGET-template my-new-agent

# Customize CLAUDE.md
# Update agent-specific sections

# Verify compliance
python3 .aget/patterns/validation/v2_compliance_check.py
```

## Support and Resources

- **Hub Repository**: `aget-framework/aget`
- **Migration Guide**: `.aget/migrations/v2.0-migration-request.md`
- **Gotchas**: `.aget/evolution/migration-v2.0-gotchas.md`
- **Compliance**: `.aget/patterns/validation/v2_compliance_check.py`

---

*This is the official AGET v2.0 template manifest. All v2.0 agents should comply with these specifications.*