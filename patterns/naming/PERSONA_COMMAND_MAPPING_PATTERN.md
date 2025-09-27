# Persona-Based Command Mapping Pattern

## The Real Insight
Personas aren't about risk - they define what COMMANDS the agent understands!

## Persona → Command Mapping

### ANALYST Persona
```bash
my-spotify-ANALYST-aget

Available commands:
- analyze [dataset]
- compare [period1] [period2]
- trend [metric]
- report [format]
- visualize [data]
- correlate [var1] [var2]
- summarize [timeframe]
```

### CURATOR Persona
```bash
my-notes-CURATOR-aget

Available commands:
- organize [by-date|by-topic|by-priority]
- tag [items] [labels]
- archive [older-than]
- categorize [using-rules]
- deduplicate
- index [collection]
- showcase [selection]
```

### GUARDIAN Persona
```bash
my-RKB_INFRA-GUARDIAN-aget

Available commands:
- guard              # Start watching
- patrol [areas]     # Check specific areas
- alert [condition]  # Set up alerts
- report-threats     # Report issues found
- stand-watch       # Continuous monitoring
- sound-alarm       # Escalate critical issues
```

### PUBLISHER Persona
```bash
my-RKB_CONTENT-PUBLISHER-aget

Available commands:
- draft [content]
- preview [changes]
- validate [content]
- schedule [datetime]
- publish [target]
- retract [content]
- update [existing]
```

### DETECTIVE Persona
```bash
my-logs-DETECTIVE-aget

Available commands:
- investigate [issue]
- search-clues [pattern]
- reconstruct [timeline]
- interrogate [source]
- solve [case-id]
- gather-evidence
- build-case
```

### SURGEON Persona
```bash
DATABASE-SURGEON-aget

Available commands:
- diagnose [issue]
- plan-operation
- prep [target]
- incision [precise-location]
- operate [procedure]
- suture [changes]
- post-op-check
```

## The Command Personality Match

### LIBRARIAN Commands Are Library-Like
```bash
my-docs-LIBRARIAN-aget

- catalog [items]
- checkout [document]
- return [document]
- find [by-author|by-subject|by-title]
- reserve [item]
- renew [loan]
- inventory
```

### COMPOSER Commands Are Creative
```bash
my-email-COMPOSER-aget

- compose [draft]
- revise [version]
- harmonize [elements]
- arrange [structure]
- polish [draft]
- rehearse [sending]  # Practice run
- perform [send]     # Actually send
```

### PILOT Commands Are Navigation
```bash
my-DEPLOYMENT-PILOT-aget

- preflight-check
- taxi [to-runway]
- takeoff
- navigate [route]
- altitude [level]
- approach [destination]
- land
- postflight-check
```

## Mixed Personas = Combined Commands

### ANALYST-REVIEWER Persona
```bash
my-code-ANALYST_REVIEWER-aget

From ANALYST:
- analyze [codebase]
- trend [metrics]

From REVIEWER:
- review [pr]
- approve/reject
- comment [line]
```

## The Implementation Pattern

```python
class AnalystAgent:
    """I analyze data and provide insights."""

    def analyze(self, dataset):
        """Core analyst action"""

    def compare(self, a, b):
        """Analyst comparison"""

    def trend(self, metric):
        """Analyst trending"""

    # These commands make sense for an ANALYST

class GuardianAgent:
    """I protect and watch over systems."""

    def guard(self):
        """Core guardian action"""

    def patrol(self, areas):
        """Guardian patrol"""

    def alert(self, condition):
        """Guardian alerting"""

    # These commands make sense for a GUARDIAN
```

## Wake-Up Greetings Match Persona

### GUARDIAN Wake-Up
```
"Guardian reporting for duty. All systems secure."
Available: guard, patrol, alert, report-threats
```

### ANALYST Wake-Up
```
"Analyst ready. What shall I investigate today?"
Available: analyze, compare, trend, report
```

### CURATOR Wake-Up
```
"Curator at your service. Ready to organize."
Available: organize, tag, archive, showcase
```

## The Naming Formula Refined

```
[ownership]-[DOMAIN]-[PERSONA]-aget

Where PERSONA defines:
- Available commands
- Interaction style
- Expected workflows
- Mental model
```

## Real Examples

### Current Name → Persona-Command Name
```bash
# Before: Generic
my-spotify-aget
# What can I do with this?

# After: Clear Commands
my-spotify-ANALYST-aget
# Ah! I can: analyze, trend, compare, report

# Before: Vague
RKB_infrastructure
# Monitor? Modify? Deploy?

# After: Specific
my-RKB_INFRA-GUARDIAN-aget
# Ah! I can: guard, patrol, alert (but not modify!)
```

## The User Experience

```bash
$ cd my-spotify-ANALYST-aget
$ ./aget analyze last-month
# Works - ANALYST knows 'analyze'

$ ./aget publish
# Error: ANALYST persona doesn't have 'publish' command
# Did you mean 'report'?

$ cd my-RKB_CONTENT-PUBLISHER-aget
$ ./aget publish
# Works - PUBLISHER knows 'publish'
```

## Persona Discovery

```bash
$ ./aget help

CURATOR Commands:
  organize [by]     Organize your collection
  tag [items]       Tag items for later
  archive [old]     Archive old items
  showcase [best]   Showcase curated selection

CURATOR personality: Methodical, organized, thoughtful
```

## The Cognitive Model

When you see:
- `*-ANALYST-aget` → Think: data analysis commands
- `*-GUARDIAN-aget` → Think: protective watching commands
- `*-CURATOR-aget` → Think: organization commands
- `*-PUBLISHER-aget` → Think: publishing commands

The persona IS the command interface!

---
*Pattern created: 2025-09-26*
*Insight: Personas define command vocabulary*
*Benefit: Immediately know what commands make sense*