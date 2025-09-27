# my-example-aget Incremental Update Plan
**Version**: 2.0.0
**Date**: 2025-09-27
**Approach**: Zero-Risk Incremental

## Philosophy: Add, Don't Replace
Every step adds capability without breaking anything. EXAMPLE continues to work exactly as it does today, with new AGET features appearing alongside.

## Step 0: Version Marker Only (5 minutes) ✅
**Zero Risk** - Just add metadata
**COMPLETED**: 2025-09-27 02:21

```bash
# Add version.json to existing .aget directory
.aget/version.json
```

Content:
```json
{
  "aget_version": "2.0.0-alpha",
  "created": "2025-09-27",
  "mode": "compatibility",
  "legacy_preserved": true,
  "example_version": "1.0.0"
}
```

**Test**: Everything still works exactly the same
**Rollback**: Delete one file

---

## Step 1: Parallel Session Protocol (30 minutes) ✅
**Add alongside existing** - Don't touch current scripts
**COMPLETED**: 2025-09-27 02:25

Create `patterns/session/wake.py` that:
1. Calls existing `make wake`
2. Adds AGET tracking
3. Falls back gracefully

**Test**: Both `make wake` and `aget wake` work
**Rollback**: Delete patterns/ directory

---

## Step 2: Evolution Tracking (20 minutes) ✅
**Pure addition** - New capability, no changes
**COMPLETED**: 2025-09-27 02:28

Create `.aget/evolution/` for:
- Decision tracking (DEC-001.md)
- Discovery logging (DISC-001.md)
- Pattern extraction (EXT-001.md)

Start with:
```markdown
# DEC-001: AGET Integration Approach
Date: 2025-09-27
Decision: Incremental addition, preserve all legacy
Rationale: EXAMPLE is mission-critical
```

**Test**: Current workflows unchanged
**Rollback**: Delete evolution/ directory

---

## Step 3: Backup Enhancement (45 minutes)
**Augment existing** - Make current better

Add to existing backup strategy:
1. `.aget/checkpoints/` for state saves
2. Automated verification after backup
3. Keep all current backup methods

```python
# Wrapper around existing backup
def enhanced_backup():
    run_existing_backup()  # Current method
    create_checkpoint()    # New AGET feature
    verify_recovery()      # New safety check
```

**Test**: Old backups work, new ones are better
**Rollback**: Remove checkpoint directory

---

## Step 4: Beauty Metrics Pattern (1 hour)
**Formalize existing feature** - Make it reusable

Extract beauty tracking into AGET pattern:
1. Keep `journal_enhanced.sh beauty-add` working
2. Add `patterns/beauty/tracker.py`
3. Both call same underlying data store

**Test**: Both old and new commands work
**Rollback**: Delete pattern file

---

## Step 5: Smart Reader (15 minutes)
**Fix without breaking** - Add safety

Add EISDIR prevention:
```python
# patterns/documentation/smart_reader.py
# Prevents "Is a directory" errors
# Falls back to native read if needed
# NOTE: Exists at /Users/aget-framework/github/patterns/documentation/smart_reader.py
```

**Test**: Reading files still works
**Rollback**: Remove reference or copy locally

---

## Step 6: Documentation Bridge (30 minutes)
**Compatibility layer** - Support both worlds

1. Keep CLAUDE.md as-is
2. Add AGET.md with extended info
3. Create symlink strategy:
   - CLAUDE.md → AGET.md (future)
   - For now, both files coexist

**Test**: Both files work independently
**Rollback**: Delete AGET.md

---

## Step 7: Testing Framework (1 hour)
**Quality assurance** - Protect what exists

Add tests for EVERYTHING:
```python
# tests/test_legacy.py
def test_musing_capture():
    assert journal_enhanced("muse", "test")

def test_wake_protocol():
    assert make("wake") == 0
```

**Test**: All legacy features pass
**Rollback**: Delete tests/

---

## Step 8: Graduate Patterns (2 hours)
**Share learnings** - Optional contribution

If successful, consider:
1. Extract EXAMPLE patterns to my-aget-aget
2. Generalize for template contribution
3. Keep EXAMPLE-specific parts private

**Test**: EXAMPLE unchanged, patterns extracted
**Rollback**: Not applicable (separate repo)

---

## Validation Gates (Lightweight)

### After Each Step:
1. Can you still capture musings? ✅/❌
2. Does wake/wind-down work? ✅/❌
3. Are commits/pushes working? ✅/❌
4. Is beauty tracking intact? ✅/❌

### Daily Use Test:
- Use EXAMPLE normally for 24 hours
- If ANY friction, pause and fix
- Only proceed when seamless

## Why This Works

1. **Nothing breaks** - Every addition is optional
2. **Instant rollback** - Delete new, keep old
3. **Gradual adoption** - Use new features when ready
4. **Preserve personality** - EXAMPLE remains EXAMPLE
5. **Learn safely** - Each step teaches next

## Timeline (Relaxed)

- **Week 1**: Steps 0-3 (Foundation)
- **Week 2**: Steps 4-6 (Features)
- **Week 3**: Step 7 (Testing)
- **Week 4**: Step 8 (Graduation)

Or do one step per day when you have 30 minutes.

## First Action (Right Now)

```bash
cd /Users/aget-framework/github/my-example-aget
echo '{
  "aget_version": "2.0.0-alpha",
  "created": "2025-09-27",
  "mode": "compatibility",
  "legacy_preserved": true,
  "example_version": "1.0.0"
}' > .aget/version.json
git add .aget/version.json
git commit -m "feat: Add AGET version marker (Step 0)"
```

Then test that everything still works.

---

*Incremental = Safe = Successful*