# TrustByDesign Governance Layer — Quick Start

This guide shows you how to use the TrustByDesign governance layer in 5 minutes.

## What You Can Do

1. **Generate compliance checklists** automatically
2. **Create governance declarations** interactively
3. **Use audit trail templates** for logging
4. **Run working code examples** to learn
5. **Validate compliance** automatically

---

## 1. Generate a Compliance Checklist (30 seconds)

```bash
# Generate a Level 2 checklist for your chatbot
python tooling/generate_compliance_checklist.py \
  --level 2 \
  --type agent \
  --name "My Chatbot" \
  --output my-checklist.yaml

# Output: my-checklist.yaml with all requirements filled in
```

**What you get**: A complete compliance checklist with:
- Pre-filled capability boundaries
- All required safety checks
- Guidance notes for your level
- Test result templates

---

## 2. Create a Governance Declaration (2 minutes)

```bash
# Interactive builder - answers questions, creates declaration
python tooling/generate_governance.py --output my-governance.yaml
```

**Questions you'll answer**:
- System name and ID
- Safety level (it helps you choose!)
- Capabilities and boundaries
- Governance preferences
- Audit configuration

**What you get**: Complete governance declaration ready to use.

---

## 3. Use a Pre-Made Template (10 seconds)

```bash
# Copy the right template for your level
cp templates/compliance/level2-chatbot.yaml my-agent-config.yaml

# Edit to match your system
nano my-agent-config.yaml  # or your favorite editor

# Validate when done
python tooling/validate_safety.py --level 2 --config my-agent-config.yaml
```

**Available templates**:
- `level1-observational.yaml` — Read-only systems
- `level2-chatbot.yaml` — Interactive agents
- `level3-autonomous-agent.yaml` — Autonomous systems

---

## 4. Run a Working Example (1 minute)

```bash
# See a complete Level 2 agent in action
python integrations/example_level2_agent.py
```

**What it demonstrates**:
1. Consent flow (grant/revoke)
2. Memory operations (store/retrieve/delete)
3. Capability boundaries (allow/refuse)
4. Transparency (confidence, reasoning)
5. Audit logging (complete trail)

**Output**: Full example showing all protocols working together.

---

## 5. Validate Your Implementation (30 seconds)

```bash
# Check compliance
python tooling/validate_safety.py \
  --level 2 \
  --config my-agent-config.yaml

# Get trust assessment
python tooling/assess_trust.py \
  --system "My Agent" \
  --output trust-report.json
```

**What you get**:
- Pass/fail for each safety check
- Compliance score (0-100%)
- List of gaps to fix
- Trust assessment across 6 dimensions

---

## 6. Use Audit Trail Templates (Copy & Paste)

For daily operations:
```bash
# Start with basic audit log template
cp templates/audit-trails/basic-audit-log.json audit-logs/$(date +%Y-%m-%d).json
```

For Glyphtrail integration:
```bash
# Use Glyphtrail-compatible format
cp templates/audit-trails/glyphtrail-compatible.json audit-logs/session-$(date +%s).json
```

For monthly reporting:
```bash
# Monthly summary template
cp templates/audit-trails/monthly-summary.json reports/$(date +%Y-%m).json
```

---

## 7. Integrate Into Your Code (Copy Example)

```bash
# Copy the working example as your starting point
cp integrations/example_level2_agent.py my_agent.py

# Customize it:
# 1. Update capabilities in _default_config()
# 2. Implement your actual logic in _execute_action()
# 3. Add your response generation in respond()

# Test it works
python my_agent.py

# Validate compliance
python tooling/validate_safety.py --level 2 --config my-agent-config.yaml
```

---

## Common Workflows

### Workflow 1: New Chatbot from Scratch

```bash
# 1. Generate checklist
python tooling/generate_compliance_checklist.py -l 2 -t agent -n "ChatBot" -o chatbot-checklist.yaml

# 2. Copy working example
cp integrations/example_level2_agent.py chatbot.py

# 3. Customize capabilities in chatbot.py

# 4. Validate
python tooling/validate_safety.py --level 2 --config chatbot-checklist.yaml

# 5. Run
python chatbot.py
```

### Workflow 2: Add TrustByDesign to Existing Agent

```bash
# 1. Generate governance declaration
python tooling/generate_governance.py --output governance.yaml

# 2. Use Level 2 example as reference
cat integrations/example_level2_agent.py

# 3. Add to your code:
#    - Consent mechanisms
#    - Memory safety (delete capability)
#    - Audit logging
#    - Capability boundaries

# 4. Validate
python tooling/validate_safety.py --level 2 --config governance.yaml
```

### Workflow 3: MirrorDNA Integration

```bash
# 1. Review integration example
python integrations/mirrordna_integration.py

# 2. Copy pattern:
#    - MirrorDNA identity verification
#    - Constitutional compliance check
#    - TrustByDesign safety protocols
#    - Dual audit logging

# 3. Adapt to your MirrorDNA setup
```

---

## File Locations

**Templates**:
- `templates/compliance/` — 3 compliance templates (Levels 1, 2, 3)
- `templates/audit-trails/` — 3 audit log formats + README

**Examples**:
- `integrations/example_level2_agent.py` — Full Level 2 implementation
- `integrations/mirrordna_integration.py` — MirrorDNA + TrustByDesign

**Tools**:
- `tooling/generate_governance.py` — Interactive declaration builder
- `tooling/generate_compliance_checklist.py` — Auto-generate checklists
- `tooling/validate_safety.py` — Validate compliance
- `tooling/assess_trust.py` — Trust assessment

**Docs**:
- `docs/integration-guide.md` — Full implementation guide
- `docs/governance-model.md` — Governance deep-dive
- `integrations/README.md` — Integration patterns

---

## Next Steps

### If You're Building Something New
1. Use `generate_compliance_checklist.py` to create your checklist
2. Copy `example_level2_agent.py` as your template
3. Customize capabilities and logic
4. Validate with `validate_safety.py`

### If You Have an Existing System
1. Run `generate_governance.py` to understand requirements
2. Review your system against `docs/safety-protocols.md`
3. Add missing protocols (start with memory safety)
4. Use `validate_safety.py` to track progress

### If You're Auditing
1. Request the system's governance declaration
2. Run `validate_safety.py` on their config
3. Run `assess_trust.py` for trust dimensions
4. Review audit logs (use templates as reference)

---

## Support

- **Documentation**: See `docs/` for comprehensive guides
- **Examples**: See `integrations/` for working code
- **Templates**: See `templates/` for ready-to-use formats
- **FAQ**: See `docs/faq.md` for common questions

---

**Time from zero to compliant agent: ~10 minutes** ⏱️

**All tools tested and working** ✅

**Ready for production use** 🚀
