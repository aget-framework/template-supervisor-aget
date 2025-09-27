# Cursor (Codex) Compatibility Test Protocol

## Test Environment
- Repository: cli-agent-template
- Python version: 3.8+
- Test date: ___________
- Cursor version: ___________

## Phase 1: Basic Recognition Tests

### Test 1.1: Configuration Recognition
- [ ] Open this repo in Cursor
- [ ] Check if Cursor reads `.cursorrules`
- [ ] Verify Cursor acknowledges the rules
- **Result**: _________

### Test 1.2: Simple Command
- [ ] Type: "wake up"
- [ ] Does Cursor recognize the command?
- [ ] Does it execute `python3 scripts/aget_session_protocol.py wake`?
- **Result**: _________

## Phase 2: Protocol Tests

### Test 2.1: Wake Protocol
**Input**: "wake up"
**Expected**:
- Reads AGENT.md
- Shows working directory
- Shows git status
- Reports "Ready for tasks."
**Actual**: _________

### Test 2.2: Wind Down Protocol
**Input**: "wind down"
**Expected**:
- Commits changes
- Creates session notes
- Reports "Session preserved."
**Actual**: _________

### Test 2.3: Sign Off Protocol
**Input**: "sign off"
**Expected**:
- Commits changes
- Pushes to remote
- Reports "Signed off."
**Actual**: _________

## Phase 3: Error Handling Tests

### Test 3.1: Command Variations
Try these variations and note which work:
- [ ] "Wake up" (capitalized)
- [ ] "please wake up"
- [ ] "wakeup" (no space)
- [ ] "can you wake up"

### Test 3.2: Direct Command Fallback
If natural language fails, try:
- [ ] "Execute: python3 scripts/aget_session_protocol.py wake"
- [ ] "Run the wake protocol"
- [ ] Copy-paste the exact command

## Phase 4: Advanced Features

### Test 4.1: Housekeeping Protocols
- [ ] "housekeeping"
- [ ] "documentation check"
- [ ] "sanity check"

### Test 4.2: Parameter Support
- [ ] "sign off --status"
- [ ] Does Cursor pass parameters correctly?

## Comparison Matrix

| Feature | Claude CLI | Cursor | Notes |
|---------|-----------|---------|-------|
| Reads AGENT.md | ✅ | ? | |
| Natural language triggers | ✅ | ? | |
| Python execution | ✅ | ? | |
| Git operations | ✅ | ? | |
| Session state persistence | ✅ | ? | |
| Parameter passing | ✅ | ? | |

## Key Differences Found
1. _________
2. _________
3. _________

## Recommendations
- If natural language fails: _________
- If Python execution fails: _________
- Configuration adjustments needed: _________