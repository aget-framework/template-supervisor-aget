# Persona Casing Clarification

## The Confusion
When should personas be UPPERCASE vs lowercase?

## Option 1: Risk-Based Casing (Original Thought)
```bash
# Safe = lowercase
my-spotify-analyst-aget        # Safe reading
my-notes-curator-aget          # Safe organizing

# Dangerous = UPPERCASE
my-RKB_CONTENT-PUBLISHER-aget  # Dangerous publishing
DATABASE-SURGEON-aget          # Dangerous operations
```

**Problem**: Conflates persona with risk. ANALYST could analyze then delete!

## Option 2: All Personas Uppercase (Consistency)
```bash
my-spotify-ANALYST-aget
my-notes-CURATOR-aget
my-RKB_CONTENT-PUBLISHER-aget
my-RKB_INFRA-GUARDIAN-aget
```

**Problem**: Loses risk signaling. Everything screams equally.

## Option 3: Domain Risk, Persona Normal (Recommended) ✅
```bash
# Safe domain = lowercase domain + lowercase persona
my-spotify-analyst-aget        # spotify is safe domain
my-notes-curator-aget          # notes are safe to manage

# DANGEROUS domain = UPPERCASE domain + lowercase persona
my-RKB_CONTENT-publisher-aget  # RKB_CONTENT is production!
my-DATABASE-surgeon-aget        # DATABASE is production!
my-AWS-operator-aget           # AWS is dangerous domain!

# The UPPERCASE DOMAIN warns you, persona just describes role
```

## The Logic

### What Makes Something Dangerous?
**THE DOMAIN, not the persona!**

- `RKB_CONTENT` = Production content (DANGEROUS)
- `DATABASE` = Production data (DANGEROUS)
- `AWS` = Infrastructure (DANGEROUS)
- `PROD` = Production anything (DANGEROUS)

vs

- `spotify` = Your personal data (safe)
- `notes` = Your personal notes (safe)
- `files` = Your local files (safe-ish)

### Personas Are Just Roles
```bash
# These are just job descriptions:
analyst     # Analyzes things
curator     # Organizes things
publisher   # Publishes things
guardian    # Guards things

# The DANGER comes from WHAT they operate on:
my-spotify-analyst-aget         # Analyzing spotify (safe)
my-PRODUCTION_LOGS-analyst-aget # Analyzing PRODUCTION (careful!)
```

## Clear Examples

### Safe Domains → All Lowercase
```bash
my-spotify-analyst-aget
my-notes-curator-aget
my-music-librarian-aget
my-email-composer-aget
team-code-reviewer-aget
```

### Dangerous Domains → UPPERCASE Domain
```bash
my-RKB_CONTENT-publisher-aget   # RKB is production
my-DATABASE-surgeon-aget         # DATABASE is critical
my-AWS_PROD-operator-aget        # AWS PROD is dangerous
COMPANY_BLOG-publisher-aget      # COMPANY BLOG is public
```

## Test Cases

### Scenario 1: Same Persona, Different Domains
```bash
my-notes-publisher-aget          # Publishing YOUR notes (safe-ish)
my-BLOG-publisher-aget           # Publishing to YOUR PUBLIC BLOG (danger!)
COMPANY_BLOG-publisher-aget      # Publishing to COMPANY BLOG (very danger!)

# Same persona (publisher), different risk based on domain
```

### Scenario 2: Same Domain, Different Personas
```bash
my-RKB_CONTENT-analyst-aget      # Analyzing production (read-only)
my-RKB_CONTENT-curator-aget      # Organizing production (hmm, risky)
my-RKB_CONTENT-publisher-aget    # Publishing to production (danger!)

# Same domain (RKB_CONTENT), but publisher still most dangerous
```

## The Final Rule

```
[ownership]-[DOMAIN]-[persona]-aget

Where:
- ownership: always lowercase (my, team, corp)
- DOMAIN: UPPERCASE if production/public/dangerous
- persona: always lowercase (describes role)
- aget: always lowercase
```

## Why This Works

1. **Visual Scan**: UPPERCASE domains jump out as dangerous
2. **Consistent**: Personas always lowercase
3. **Clear Signal**: Danger comes from domain, not role
4. **Sortable**: Dangerous domains group together

## Edge Cases Resolved

### What about GUARDIAN?
```bash
my-rbk-infra-guardian-aget      # If RKB infra was safe
my-RKB_INFRA-guardian-aget      # But RKB INFRA is production!
```

Guardian is lowercase (just a role), but RKB_INFRA is UPPERCASE (production system)

### What about mixed safety?
```bash
my-email-composer-aget           # Composes drafts (safe)
my-EMAIL-sender-aget             # SENDS emails (reputation risk!)
```

When email becomes dangerous (sending), uppercase the domain!

## Migration Examples

### Your Repos Clarified
```bash
# Current confusion
my-RKB_CONTENT-PUBLISHER-aget   # Why both uppercase?

# Clarified
my-RKB_CONTENT-publisher-aget   # DOMAIN dangerous, persona normal

# Full set
my-spotify-analyst-aget         # Safe domain, analyst persona
my-aget-architect-aget          # Safe domain, architect persona
my-RKB_INFRA-guardian-aget      # DANGER domain, guardian persona
my-RKB_CONTENT-publisher-aget   # DANGER domain, publisher persona
```

## The Cognitive Test

What's clearer?

### Option A: Everything Uppercase
```bash
my-RKB_CONTENT-PUBLISHER-aget
my-SPOTIFY-ANALYST-aget
```
Can't tell what's actually dangerous

### Option B: Domain-Based Danger
```bash
my-RKB_CONTENT-publisher-aget   # RKB_CONTENT is the danger
my-spotify-analyst-aget         # spotify is safe
```
Immediately see RKB_CONTENT is the risky part!

---
*Clarification: 2025-09-26*
*Rule: UPPERCASE domains for danger, lowercase personas always*
*Insight: Danger comes from WHERE, not WHO*