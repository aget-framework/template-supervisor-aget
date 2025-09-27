# AGET Security Standards

## Purpose
Define security best practices for all AGET agents, especially credential management and data protection.

## Core Principles

### 1. Defense in Depth
- Multiple layers of security
- Assume breach and limit damage
- Principle of least privilege

### 2. Secure by Default
- Restrictive permissions out of the box
- Credentials never in code
- Encryption for sensitive data

### 3. Transparency
- Document all security measures
- Track security decisions in evolution
- Clear incident response procedures

## Credential Management Standards

### Required Structure
```
.aget/
└── secrets/                  # Standard location for ALL credentials
    ├── .gitignore           # MUST ignore all credential files
    ├── README.md            # MUST document each credential
    └── [credential files]   # Actual keys/tokens
```

### Permission Requirements

#### Unix/Linux/Mac
```bash
chmod 700 .aget/secrets/     # Directory: owner-only access
chmod 600 .aget/secrets/*    # Files: owner read/write only
```

#### Windows (if applicable)
- Use NTFS permissions
- Remove all users except owner
- Deny access to SYSTEM for credentials

### Mandatory .gitignore
```gitignore
# CRITICAL: Never commit credentials
.aget/secrets/*
!.aget/secrets/.gitignore
!.aget/secrets/README.md
!.aget/secrets/*.example
!.aget/secrets/*.template
```

### Credential Types and Storage

| Type | Format | Location | Permissions | Rotation |
|------|---------|----------|-------------|----------|
| Service Account | JSON | `.aget/secrets/[service]_credentials.json` | 600 | 90 days |
| API Keys | .env file | `.aget/secrets/.env` | 600 | 30-90 days |
| SSH Keys | PEM | `.aget/secrets/[purpose]_key` | 600 | Annual |
| Database | JSON/env | `.aget/secrets/db_config.json` | 600 | 90 days |
| Tokens | Text | `.aget/secrets/[service]_token` | 600 | Per provider |

## Security Best Practices

### DO ✅
1. **Use .aget/secrets/ exclusively** for credentials
2. **Set 600 permissions** on all credential files
3. **Document** each credential's purpose and rotation
4. **Use read-only** permissions when possible
5. **Test credentials** after setup
6. **Rotate regularly** (90 days default)
7. **Create example files** showing structure
8. **Log security events** in evolution
9. **Use environment variables** for runtime secrets
10. **Implement key rotation** reminders

### DON'T ❌
1. **Never commit** actual credentials (even encrypted)
2. **Don't store** credentials elsewhere in repo
3. **Avoid broad** permissions (777, 755)
4. **Don't share** credentials between agents
5. **Never hardcode** secrets in code
6. **Don't use** personal credentials for agents
7. **Avoid plaintext** passwords
8. **Don't ignore** rotation schedules
9. **Never log** credential values
10. **Don't trust** user input with credentials

## Incident Response

### If Credentials Are Exposed

#### Immediate Actions (< 5 minutes)
1. **REVOKE** credential in provider console
2. **ALERT** team if production system
3. **DOCUMENT** in `.aget/evolution/incidents/`

#### Recovery Actions (< 1 hour)
1. **GENERATE** new credential
2. **UPDATE** in `.aget/secrets/`
3. **TEST** all systems still work
4. **AUDIT** logs for unauthorized use

#### Follow-up Actions (< 24 hours)
1. **REVIEW** how exposure happened
2. **UPDATE** patterns to prevent recurrence
3. **NOTIFY** affected users if needed
4. **REPORT** to governance if required

### Incident Documentation Template
```json
{
  "timestamp": "ISO-8601",
  "type": "credential_exposure",
  "severity": "high|medium|low",
  "credential_type": "api_key|service_account|etc",
  "exposure_vector": "git|logs|breach|etc",
  "impact": "description of potential damage",
  "response": {
    "revoked_at": "timestamp",
    "rotated_at": "timestamp",
    "systems_affected": [],
    "unauthorized_use": "none|detected|unknown"
  },
  "lessons_learned": [],
  "pattern_updates": []
}
```

## Compliance Requirements

### Logging
- Log access attempts (success and failure)
- Never log credential values
- Track rotation events
- Document security decisions

### Auditing
```python
# .aget/scripts/security_audit.py
def audit_secrets():
    """Monthly security audit of credentials."""
    checks = {
        "permissions": check_file_permissions(),
        "rotation": check_rotation_schedule(),
        "gitignore": verify_gitignore(),
        "documentation": check_readme_current()
    }
    return checks
```

### Monitoring
- Check for exposed credentials in commits
- Monitor file permission changes
- Alert on rotation schedule
- Track failed authentication attempts

## Implementation Checklist

### For New AGETs
- [ ] Create `.aget/secrets/` directory
- [ ] Set directory permissions to 700
- [ ] Add comprehensive `.gitignore`
- [ ] Create `README.md` template
- [ ] Add security audit script
- [ ] Document in capabilities.json

### For Existing AGETs
- [ ] Migrate credentials to `.aget/secrets/`
- [ ] Update file permissions
- [ ] Verify `.gitignore` coverage
- [ ] Document existing credentials
- [ ] Set up rotation schedule
- [ ] Add security monitoring

## Validation Tests

### Security Validation Script
```bash
#!/bin/bash
# validate_security.sh

echo "🔒 Validating AGET Security Standards..."

# Check directory exists and permissions
if [[ -d .aget/secrets ]]; then
    perms=$(stat -c %a .aget/secrets 2>/dev/null || stat -f %A .aget/secrets)
    if [[ "$perms" == "700" ]]; then
        echo "✅ Secrets directory permissions correct"
    else
        echo "❌ Secrets directory should be 700, found $perms"
    fi
fi

# Check gitignore
if grep -q ".aget/secrets/\*" .gitignore; then
    echo "✅ Secrets properly gitignored"
else
    echo "❌ Secrets not in .gitignore!"
fi

# Check for exposed credentials
if git ls-files | grep -E "(password|api_key|token|credential)" | grep -v example; then
    echo "⚠️ Possible credentials in git!"
fi

echo "🔒 Security validation complete"
```

## Evolution Tracking

### Security Decisions
Document all security decisions in evolution:
```json
// .aget/evolution/decisions/security_setup.json
{
  "decision": "Use .aget/secrets for all credentials",
  "rationale": "Centralized, gitignored, standard location",
  "alternatives_considered": ["env files", "encrypted storage"],
  "risk_assessment": "Low risk with proper permissions"
}
```

### Security Discoveries
Track security findings:
```json
// .aget/evolution/discoveries/security_improvement.json
{
  "discovery": "Need rotation reminders",
  "impact": "Credentials going stale",
  "solution": "Automated rotation checking",
  "implemented": "date"
}
```

## Standard Security Files

### .aget/secrets/README.md Template
```markdown
# Secrets Management

## ⚠️ SECURITY CRITICAL
Never commit files in this directory (except this README and examples).

## Active Credentials
| Service | File | Purpose | Rotation | Last Updated |
|---------|------|---------|----------|--------------|
| GA4 | ga4_credentials.json | Analytics read | 90 days | 2025-09-26 |

## Setup Instructions
[Specific instructions for each credential]

## Rotation Schedule
- [ ] GA4: Due 2025-12-26
- [ ] API Keys: Check monthly

## Emergency Contacts
- Security Lead: [contact]
- On-call: [contact]
```

### .aget/secrets/.gitignore
```gitignore
# Ignore everything
*
# Except these files
!.gitignore
!README.md
!*.example
!*.template
```

## Governance

### Authority
These standards are mandatory for all AGET agents. Exceptions require documented approval in governance.

### Updates
Security standards evolve based on:
- Incident lessons learned
- Industry best practices
- Regulatory requirements
- Community feedback

### Enforcement
- Automated validation in CI/CD
- Security audit scripts
- Regular reviews
- Incident response exercises

---
*Security Standards Version: 1.0.0*
*Effective Date: 2025-09-26*
*Next Review: 2025-12-26*
*Authority: AGET-AGET Governance*