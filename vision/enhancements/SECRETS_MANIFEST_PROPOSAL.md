# Secrets Manifest Proposal
*Simple enhancement for AGET v2.1/v3.0*

## Overview
Add `.aget/secrets.yaml` that declares what credentials an agent needs, enabling validation and setup assistance.

## The File: `.aget/secrets.yaml`

```yaml
# Declares what secrets this agent needs
version: "1.0"
agent: RKB_analytics-aget

required:
  - name: ga4_credentials
    type: service_account
    format: json
    path: .aget/secrets/ga4_credentials.json
    permissions: "600"
    validate_command: "python3 -c 'import json; json.load(open(\".aget/secrets/ga4_credentials.json\"))'"
    test_command: "python3 scripts/test_ga4_connection.py"
    setup_url: "https://console.cloud.google.com/iam-admin/serviceaccounts"
    rotation_days: 90
    description: "Google Analytics Data API service account"

optional:
  - name: openai_key
    type: api_key
    format: env
    path: .aget/secrets/.env
    env_var: OPENAI_API_KEY
    validate_regex: "^sk-[a-zA-Z0-9]{48}$"
    description: "OpenAI API for enhanced analysis"

provides:  # For cross-agent sharing (future)
  - name: analytics_data
    type: api_endpoint
    description: "Processed analytics available to other agents"
```

## Simple v2 Implementation (Nudgeable Today)

### 1. Validation Script
```bash
#!/bin/bash
# scripts/validate_secrets.sh

echo "🔐 Checking required secrets..."

# Parse YAML (using python for portability)
python3 << 'EOF'
import yaml
import os
import sys
import subprocess

with open('.aget/secrets.yaml') as f:
    manifest = yaml.safe_load(f)

missing = []
invalid = []

for secret in manifest.get('required', []):
    path = secret['path']
    if not os.path.exists(path):
        missing.append(secret['name'])
    elif secret.get('validate_command'):
        result = subprocess.run(secret['validate_command'], shell=True, capture_output=True)
        if result.returncode != 0:
            invalid.append(secret['name'])

    # Check permissions
    if os.path.exists(path):
        perms = oct(os.stat(path).st_mode)[-3:]
        if perms != secret.get('permissions', '600'):
            print(f"⚠️  {secret['name']}: Wrong permissions {perms} (should be {secret.get('permissions')})")

if missing:
    print(f"❌ Missing required secrets: {', '.join(missing)}")
    for s in manifest['required']:
        if s['name'] in missing:
            print(f"   Setup: {s.get('setup_url', 'See documentation')}")
    sys.exit(1)

if invalid:
    print(f"❌ Invalid secrets: {', '.join(invalid)}")
    sys.exit(1)

print("✅ All required secrets present and valid")

# Check rotation
import datetime
for secret in manifest.get('required', []):
    if 'rotation_days' in secret and os.path.exists(secret['path']):
        age = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(secret['path']))
        if age.days > secret['rotation_days']:
            print(f"⚠️  {secret['name']} needs rotation (age: {age.days} days)")
EOF
```

### 2. Setup Helper
```bash
#!/bin/bash
# scripts/setup_secrets.sh

echo "🔐 Secret Setup Wizard"
echo "====================="

python3 << 'EOF'
import yaml
import os

with open('.aget/secrets.yaml') as f:
    manifest = yaml.safe_load(f)

print(f"\nThis agent ({manifest['agent']}) requires:\n")

for secret in manifest.get('required', []):
    print(f"📌 {secret['name']}")
    print(f"   Type: {secret['type']}")
    print(f"   Description: {secret['description']}")
    if not os.path.exists(secret['path']):
        print(f"   ❌ MISSING - Setup at: {secret.get('setup_url', 'see docs')}")
    else:
        print(f"   ✅ Present")
    print()

for secret in manifest.get('optional', []):
    print(f"📎 {secret['name']} (optional)")
    print(f"   Description: {secret['description']}")
    print()
EOF
```

### 3. Integration Points

#### In Wake Protocol
```python
# Add to wake protocol
def wake():
    # ... existing wake code ...

    # Check secrets
    result = subprocess.run(['bash', 'scripts/validate_secrets.sh'], capture_output=True)
    if result.returncode != 0:
        print("⚠️  Secret configuration incomplete. Run: make setup-secrets")
```

#### In Makefile
```makefile
# Secret management commands
.PHONY: check-secrets setup-secrets test-secrets

check-secrets:
	@bash scripts/validate_secrets.sh

setup-secrets:
	@bash scripts/setup_secrets.sh

test-secrets: check-secrets
	@echo "🧪 Testing secret connections..."
	@python3 scripts/test_all_connections.py

# Add to default wake
wake: check-secrets
	@python3 scripts/session_protocol.py wake
```

## Benefits

### For Users
1. **Clear Requirements**: Know exactly what credentials needed
2. **Validation**: Verify secrets are correct before running
3. **Setup Guidance**: Links to where to create credentials
4. **Rotation Reminders**: Know when to rotate

### For Developers
1. **Declaration**: Document credential needs in code
2. **Validation**: Test commands ensure credentials work
3. **Portability**: Others can set up the agent easily
4. **Security**: Enforces permission requirements

## Future v3 Enhancements

### Cross-Agent Secret Sharing
```yaml
# Agent A declares it provides analytics
provides:
  - name: analytics_api
    type: internal_api
    endpoint: "http://localhost:8080/analytics"

# Agent B declares it consumes analytics
consumes:
  - name: analytics_api
    from_agent: RKB_analytics-aget
    type: internal_api
```

### Secret Broker Service
```python
# .aget/broker.py
class SecretBroker:
    """Manages inter-agent secret sharing securely."""

    def request_access(self, secret_name, from_agent):
        """Request access to another agent's provided secrets."""
        # Validate permission
        # Create temporary token
        # Log access
        pass
```

### Automatic Setup
```bash
# aget CLI enhancement
aget secrets setup    # Interactive setup wizard
aget secrets validate # Check all secrets
aget secrets rotate   # Rotation helper
```

## Implementation Path

### Phase 1: Manual (Today)
- Create `.aget/secrets.yaml` manually
- Add validation script
- Document in README

### Phase 2: Template Support (v2.1)
- Add to aget-cli-agent-template
- Include in migration process
- Standard validation scripts

### Phase 3: CLI Integration (v3.0)
- `aget secrets` commands
- Automatic validation
- Cross-agent sharing
- Secret broker service

## Example for RKB_analytics-aget

Share this with RKB_analytics-aget:

```yaml
# .aget/secrets.yaml
version: "1.0"
agent: RKB_analytics-aget

required:
  - name: ga4_credentials
    type: service_account
    format: json
    path: .aget/secrets/ga4_credentials.json
    permissions: "600"
    description: "Google Analytics Data API service account"
    setup_instructions: |
      1. Go to https://console.cloud.google.com
      2. Create service account
      3. Download JSON key
      4. Move to .aget/secrets/ga4_credentials.json
      5. chmod 600 .aget/secrets/ga4_credentials.json
      6. Grant GA4 viewer access to service account email
    test_command: "python3 scripts/test_ga4.py"
    rotation_days: 90

status:
  last_validated: "2025-09-26"
  last_rotated: "2025-09-26"
  next_rotation: "2025-12-26"
```

Then add to Makefile:
```makefile
check-secrets:
	@echo "🔐 Validating secrets..."
	@test -f .aget/secrets/ga4_credentials.json || echo "❌ Missing GA4 credentials"
	@test -f .aget/secrets/ga4_credentials.json && echo "✅ GA4 credentials present"
```

---
*Simple today, powerful tomorrow*