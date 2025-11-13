# TrustByDesign Validation Tooling

This directory contains validation and assessment tools for TrustByDesign compliance.

## Tools

### validate_safety.py

Validates a system configuration against TrustByDesign safety requirements.

**Usage**:
```bash
# Validate Level 2 system
python validate_safety.py --level 2 --config ../examples/safety-checklist.yaml

# Validate and save results
python validate_safety.py --level 2 --config my-config.yaml --output results.json
```

**Exit Codes**:
- `0`: All checks passed (compliant)
- `1`: Some checks failed (non-compliant)

---

### assess_trust.py

Interactive tool for generating comprehensive trust assessments.

**Usage**:
```bash
# Run interactive assessment
python assess_trust.py --system "My AI Agent"

# Save assessment results
python assess_trust.py --system "My Agent" --output assessment.json
```

---

## Requirements

These tools require Python 3.7+ and PyYAML:

```bash
pip install pyyaml
```

## Integration with CI/CD

Add to your CI pipeline:

```yaml
# .github/workflows/safety-check.yml
name: TrustByDesign Safety Check

on: [push, pull_request]

jobs:
  safety:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install pyyaml
      - name: Validate safety compliance
        run: |
          python tooling/validate_safety.py \
            --level 2 \
            --config config/agent-config.yaml
```

## Future Tools

Planned additions:
- `check_compliance.py`: Multi-system compliance checker
- `generate_report.py`: Automated report generation
- `audit_logs.py`: Audit log analyzer and verifier
