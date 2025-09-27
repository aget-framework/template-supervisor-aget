# Efficient Session Patterns

## Common Requests → Optimal Patterns

### Documentation Reading
- **Request**: `wake up; read docs`
- **Efficient Option 1**: `python3 patterns/documentation/smart_reader.py docs/` (local)
- **Efficient Option 2**: `Task: "Read and summarize all documentation in docs/"`
- **Saves**: 7-9 tool calls
- **Note**: Per ARCH-001, use local patterns only

### Project Scanning
- **Request**: `wake up; check all projects`
- **Efficient**: `Task: "Scan all subdirectories for AGET projects"`
- **Saves**: 10-15 tool calls

### Multiple File Reads
- **Request**: Reading 3+ related files
- **Efficient**: `Task: "Read and summarize [list of files]"`
- **Saves**: N-1 tool calls (where N = number of files)

### Status Checks
- **Request**: `project status` across directories
- **Efficient**: `python3 patterns/meta/project_scanner.py`
- **Saves**: Manual directory traversal

### Bulk Operations
- **Request**: Any repetitive operation on multiple items
- **Efficient**: Single Task tool with clear description
- **Saves**: Proportional to item count

## Anti-Patterns to Avoid

❌ Sequential Read() calls for related documentation
❌ Individual Bash() calls for similar commands
❌ TodoWrite() for trivial sequential reads
❌ Multiple Glob() when one pattern would work

## Quick Decision Tree

```
Number of similar operations needed?
├─ 1-2: Direct execution OK
├─ 3-5: Consider batching
└─ 5+: Always use Task or bulk pattern
```

## Validation Checklist
- [ ] Did I check for existing bulk patterns first?
- [ ] Am I about to do >3 similar operations?
- [ ] Did the wake message suggest a pattern?
- [ ] Could Task tool do this more efficiently?

---
*Created: 2025-09-27*
*Purpose: Reduce tool usage by 60-80% for common operations*