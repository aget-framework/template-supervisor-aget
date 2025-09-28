# Key Management Pattern for AGET Agents

## Overview
Most AGETs need to manage credentials securely (API keys, service accounts, tokens). This pattern establishes the standard approach.

## Evidence
- **RKB_analytics-aget**: GA4 service account key management (2025-09-26)
- **Pattern**: Download → Move to .aget/secrets → Secure permissions → Grant access

## Standard Structure

### 1. Secrets Directory
```
.aget/
└── secrets/           # All credentials live here
    ├── .gitignore     # CRITICAL: Ignore all secrets
    ├── README.md      # Instructions for each key
    └── [keys...]      # Actual credential files
```

### 2. Security Requirements

#### File Permissions (Unix/Mac)
```bash
# Set restrictive permissions on any credential file
chmod 600 .aget/secrets/credential.json  # Owner read/write only
chmod 700 .aget/secrets/                 # Directory owner-only access
```

#### .gitignore Entry (MANDATORY)
```gitignore
# AGET Secrets - NEVER COMMIT
.aget/secrets/*
!.aget/secrets/.gitignore
!.aget/secrets/README.md
!.aget/secrets/*.example
```

### 3. Key Storage Pattern

#### For Service Account Keys (Google, AWS, etc.)
```bash
# Standard naming: service_credentials.json
mv ~/Downloads/[downloaded-key].json .aget/secrets/ga4_credentials.json
chmod 600 .aget/secrets/ga4_credentials.json
```

#### For API Keys
```bash
# Store in environment file
cat > .aget/secrets/.env << 'EOF'
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
EOF
chmod 600 .aget/secrets/.env
```

#### For SSH Keys
```bash
# Store with standard names
cp ~/.ssh/id_rsa .aget/secrets/deploy_key
chmod 600 .aget/secrets/deploy_key
```

## Implementation Checklist

### During AGET Creation
- [ ] Create `.aget/secrets/` directory
- [ ] Add comprehensive `.gitignore`
- [ ] Create `README.md` with setup instructions
- [ ] Set directory permissions to 700

### When Adding Credentials
- [ ] Move credential to `.aget/secrets/`
- [ ] Set file permissions to 600
- [ ] Document in `README.md`
- [ ] Create `.example` file if appropriate
- [ ] Test credential works
- [ ] Set up rotation reminder

### Security Verification
```bash
# Verify permissions
ls -la .aget/secrets/

# Verify git ignoring
git status .aget/secrets/
# Should show: "nothing to commit"

# Test credential access
python3 -c "import json; json.load(open('.aget/secrets/credential.json'))"
```

## Example README.md for Secrets Directory

```markdown
# AGET Secrets Directory

## ⚠️ SECURITY WARNING
This directory contains sensitive credentials. NEVER commit these files to git.

## Current Credentials

### GA4 Analytics (ga4_credentials.json)
- **Purpose**: Read GA4 analytics data
- **Type**: Service Account JSON
- **Email**: rkb-analytics-agent@[project].iam.gserviceaccount.com
- **Permissions**: Viewer only
- **Rotation**: Every 90 days
- **Last Updated**: 2025-09-26

### Setup Instructions
1. Download service account key from Google Cloud Console
2. Move to this directory: `mv ~/Downloads/key.json .aget/secrets/ga4_credentials.json`
3. Secure permissions: `chmod 600 ga4_credentials.json`
4. Grant GA4 access to service account email

## Rotation Schedule
- [ ] GA4 key: Next rotation 2025-12-26
- [ ] API keys: Check monthly

## Emergency Procedures
If a key is compromised:
1. Revoke immediately in provider console
2. Generate new key
3. Update in this directory
4. Update all systems using the key
5. Document incident in .aget/evolution/incidents/
```

## Best Practices

### DO ✅
- Store all credentials in `.aget/secrets/`
- Use 600 permissions for files, 700 for directory
- Document each credential's purpose
- Set rotation reminders
- Use minimal permissions (viewer/read-only when possible)
- Create example files for structure

### DON'T ❌
- Store credentials anywhere else in the repo
- Commit actual credentials (even encrypted)
- Use broad permissions (777, 755)
- Share credentials between agents
- Hardcode credentials in code
- Store passwords in plain text

## Integration with AGET Framework

### Capabilities Declaration
```json
// .aget/capabilities.json
{
  "requires_credentials": true,
  "credential_types": ["service_account", "api_key"],
  "security_level": "high",
  "rotation_schedule": "90_days"
}
```

### Evolution Tracking
```json
// .aget/evolution/decisions/credential_setup.json
{
  "timestamp": "2025-09-26",
  "decision": "Store GA4 credentials in .aget/secrets",
  "security_measures": ["chmod 600", "gitignore", "viewer-only"],
  "rotation_schedule": "quarterly"
}
```

## Common Credential Types

### 1. Google Service Accounts
- Format: JSON file
- Location: `.aget/secrets/[service]_credentials.json`
- Permissions: 600
- Best practice: Viewer/read-only roles

### 2. API Keys
- Format: Environment variables
- Location: `.aget/secrets/.env`
- Permissions: 600
- Best practice: Scope to specific APIs

### 3. SSH Keys
- Format: PEM files
- Location: `.aget/secrets/[purpose]_key`
- Permissions: 600
- Best practice: Use deploy keys, not personal

### 4. Database Credentials
- Format: Connection strings
- Location: `.aget/secrets/db_config.json`
- Permissions: 600
- Best practice: Read-only users

## Rotation Pattern

### Automated Reminder
```python
# .aget/scripts/check_key_rotation.py
import json
from datetime import datetime, timedelta
from pathlib import Path

def check_rotation():
    secrets_dir = Path('.aget/secrets')
    for key_file in secrets_dir.glob('*.json'):
        # Check file age
        age = datetime.now() - datetime.fromtimestamp(key_file.stat().st_mtime)
        if age > timedelta(days=90):
            print(f"⚠️ ROTATE: {key_file.name} is {age.days} days old")
```

### Manual Rotation Process
1. Generate new credential in provider console
2. Download to secure location
3. Test new credential works
4. Replace old credential in `.aget/secrets/`
5. Update permissions: `chmod 600`
6. Verify systems still work
7. Revoke old credential
8. Update rotation date in README

## Testing Credentials

### Generic Test Script
```python
# .aget/scripts/test_credentials.py
def test_ga4_credentials():
    """Test GA4 service account access."""
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.oauth2 import service_account

    creds = service_account.Credentials.from_service_account_file(
        '.aget/secrets/ga4_credentials.json'
    )
    client = BetaAnalyticsDataClient(credentials=creds)
    # Test query here
    print("✅ GA4 credentials working")
```

## Security Incident Response

If credentials are exposed:
1. **Immediate**: Revoke in provider console
2. **Document**: Create `.aget/evolution/incidents/credential_exposure.json`
3. **Rotate**: Generate new credentials
4. **Audit**: Check logs for unauthorized use
5. **Learn**: Update patterns to prevent recurrence

---
*Pattern Version: 1.0.0*
*Last Updated: 2025-09-26*
*Status: Reference pattern for all AGET credential management*