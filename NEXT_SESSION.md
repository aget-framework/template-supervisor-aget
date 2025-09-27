# Next Session Checklist

## October 7, 2025 (v2.0 Release Day)
- [ ] Push v2.0 commits to GitHub
- [ ] Tag v2.0.0 release
- [ ] Create GitHub release with changelog
- [ ] Announce v2.0 availability

## October 8-14 (Transition Week)
- [ ] Copy fundamental patterns to aget-aget
  ```bash
  cp -r ../aget-cli-agent-template/patterns/session patterns/
  cp ../aget-cli-agent-template/scripts/aget_*.py scripts/
  ```
- [ ] Test wake/wind-down works in aget-aget
- [ ] Create dev branch for v2.1
- [ ] Start first v2.1 experiment

## October 15+ (New Workflow)
- [ ] Morning: `cd aget-aget && wake up`
- [ ] Work in workspace/ for experiments
- [ ] Graduate proven features to AGET
- [ ] Keep aget-cli-agent-template for releases only

## Key Commands to Remember

### In aget-aget (development)
```bash
# Start day
wake up

# Run experiments
python3 workspace/experiment_*.py

# Track decisions
aget evolution --type decision "..."

# Check sync status
python3 workspace/sync_checker.py
```

### Graduation Process
```bash
# When feature is ready in aget-aget
cp workspace/feature.py ../aget-cli-agent-template/patterns/

# In AGET
cd ../aget-cli-agent-template
git add . && git commit -m "feat: Graduate feature from aget-aget"
```

## Success Metrics
- [ ] v2.0 released successfully
- [ ] First commit in aget-aget as primary (Oct 15)
- [ ] First graduated feature (Nov 1)
- [ ] v2.1 with 5+ features (Dec 1)

---
*Checklist created: September 25, 2025*
*The transition begins October 7, 2025*