# Error Visibility Crisis in AGET Sessions

## Discovery Date
2025-09-26

## The Problem
AGET sessions are drowning users in low-value messages while critical errors go unnoticed.

## Current Reality

### Signal-to-Noise Ratio: TERRIBLE
```
✓ Reading file...
✓ File read successfully
✓ Checking status...
✓ Status checked
✓ Preparing to commit...
✓ Running git add...
⎿ Error: Error              <-- CRITICAL ERROR BURIED
✓ Cleaning up...
✓ Session complete! 🎉
```

### What Users See
- Walls of checkmarks
- Verbose progress updates
- Happy emojis
- Success messages

### What Users Miss
- Critical failures
- Data loss warnings
- Security issues
- Actual problems

## Why This Happens

### 1. Everything Looks Equal
```
✓ Trivial success
✓ Critical success
⎿ Trivial failure
⎿ CRITICAL FAILURE   <-- No visual distinction
```

### 2. Success Theater
- Celebrating micro-achievements
- Verbose progress for simple operations
- Optimistic messaging despite failures

### 3. Error Message Poverty
- "Error: Error" - useless
- No error codes
- No recovery instructions
- No severity indicators

## The Impact

### Immediate
- Users lose work thinking it was saved
- Critical errors ignored
- False confidence in operations

### Long-term
- Trust erosion
- Learned helplessness ("just ignore the output")
- Real problems missed

## Solution: Output Hierarchy

### Visual Hierarchy
```
🚨 CRITICAL: Commit failed - work NOT saved
⚠️  WARNING: Credentials near expiration
✓  Success: Operation completed
→  Info: Processing file
·  Debug: Checking variable
```

### Severity Levels
1. **CRITICAL** - Data loss, security breach (UNMISSABLE)
2. **ERROR** - Operation failed (Red, clear)
3. **WARNING** - Attention needed (Yellow)
4. **SUCCESS** - Confirmed success (Green, brief)
5. **INFO** - Status update (Minimal)
6. **DEBUG** - Details (Hidden by default)

### Message Reform

#### Before (Bad)
```
✓ Preparing session...
✓ Initializing git...
✓ Checking status...
✓ Running git add...
✓ Adding files...
✓ Preparing commit...
⎿ Error: Error
✓ Finalizing...
✓ Complete! 🎉
```

#### After (Good)
```
Starting session...
🚨 CRITICAL: Git commit failed
   Problem: Commit message formatting error
   Impact: Your work is NOT saved
   Fix: Run 'git commit -m "message"' manually
   Files affected: 23 uncommitted changes
```

## Implementation Strategy

### Phase 1: Critical Errors First
- Make critical errors UNMISSABLE
- Add error details and recovery steps
- Remove false success messages

### Phase 2: Reduce Noise
- Remove trivial confirmations
- Batch related messages
- Default to quiet mode

### Phase 3: Smart Output
- Context-aware verbosity
- Collapsible debug info
- Error summaries at end

## Metrics for Success
- Zero missed critical errors
- 80% reduction in output lines
- 100% of errors include recovery steps
- User trust restored

## The New Rule

> **"If everything is important, nothing is important"**

Reserve emphasis for what matters. Make critical errors impossible to miss. Celebrate real achievements, not routine operations.

## Code Example

```python
class OutputLevel(Enum):
    CRITICAL = 0  # Cannot be silenced
    ERROR = 1     # Shows in quiet mode
    WARNING = 2   # Shows in normal mode
    SUCCESS = 3   # Shows in normal mode
    INFO = 4      # Shows in verbose mode
    DEBUG = 5     # Shows in debug mode

def output(level, message, details=None):
    if level == OutputLevel.CRITICAL:
        print(f"🚨 CRITICAL: {message}")
        if details:
            for key, value in details.items():
                print(f"   {key}: {value}")
        # Also log to file, send notification, etc.
    elif level <= current_verbosity:
        # Show based on verbosity setting
```

## Lesson
The most dangerous error is the one nobody sees. Make critical failures louder than success.

---
*Discovered: 2025-09-26*
*Priority: CRITICAL - User Trust & Data Safety*