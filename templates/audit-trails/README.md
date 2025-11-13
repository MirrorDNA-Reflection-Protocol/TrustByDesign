# Audit Trail Templates

This directory contains templates and examples for TrustByDesign-compliant audit trails.

## Templates

### basic-audit-log.json

Standard audit log format showing individual events throughout a day.

**Use for**: Day-to-day operational logging

**Key features**:
- Individual event entries with timestamps
- Hash chain for integrity verification
- Common event types (consent, memory ops, decisions, errors)
- Summary statistics

**Event types included**:
- `consent_granted` / `consent_revoked`
- `memory_store` / `memory_retrieve` / `memory_delete`
- `decision_made`
- `capability_boundary_violation`
- `error_occurred`

---

### glyphtrail-compatible.json

Audit log in Glyphtrail-compatible format for ecosystem integration.

**Use for**: Integration with Glyphtrail lineage tracking

**Key features**:
- Glyph-based event structure
- Cryptographic signatures for each glyph
- Chain verification
- MirrorDNA ecosystem compatibility

**Glyph types**:
- `interaction_start` / `interaction_end`
- `memory_access` / `memory_modification`
- `decision`
- `capability_boundary`

---

### monthly-summary.json

Aggregated monthly audit report with metrics and compliance scores.

**Use for**: Monthly governance reviews and compliance reporting

**Key features**:
- Aggregate statistics
- Safety metrics across all dimensions
- Incident tracking
- Compliance scoring
- Recommendations

**Sections**:
- Summary statistics
- Safety metrics (memory, consent, boundaries, transparency)
- Governance compliance
- Incidents and anomalies
- User trust signals
- Recommendations

---

## Using These Templates

### For Developers

1. **Choose the right format**:
   - Daily operations → `basic-audit-log.json`
   - Ecosystem integration → `glyphtrail-compatible.json`
   - Monthly reporting → `monthly-summary.json`

2. **Adapt to your system**:
   - Replace agent IDs and names
   - Add system-specific event types
   - Customize metadata fields

3. **Implement logging**:
   ```python
   import json
   from datetime import datetime

   class AuditLogger:
       def __init__(self, agent_id):
           self.agent_id = agent_id
           self.entries = []

       def log_event(self, event_type, details):
           entry = {
               "timestamp": datetime.utcnow().isoformat() + "Z",
               "event_type": event_type,
               "agent_id": self.agent_id,
               "details": details
           }
           self.entries.append(entry)

       def export(self, filepath):
           with open(filepath, 'w') as f:
               json.dump({
                   "log_version": "1.0",
                   "agent_id": self.agent_id,
                   "entries": self.entries
               }, f, indent=2)
   ```

### For Auditors

1. **Verify log integrity**:
   - Check hash chains in `basic-audit-log.json`
   - Verify signatures in `glyphtrail-compatible.json`
   - Validate summary statistics in `monthly-summary.json`

2. **Review compliance**:
   - All critical events logged?
   - Timestamps chronological?
   - User actions properly recorded?
   - Consent changes documented?

3. **Generate reports**:
   - Use monthly-summary template
   - Calculate compliance scores
   - Identify trends and patterns

---

## Required Events by Safety Level

### Level 1 (Observational)
Optional logging, but recommended:
- `capability_boundary_violation`
- `error_occurred`

### Level 2 (Interactive)
MUST log:
- `consent_granted` / `consent_revoked`
- `memory_store` / `memory_retrieve` / `memory_delete`
- `capability_boundary_violation`
- `error_occurred`

### Level 3 (Autonomous)
All Level 2 events PLUS:
- `action_proposed` / `action_approved` / `action_rejected`
- `autonomous_decision`
- `anomaly_detected`
- `emergency_stop`
- `governance_review`

---

## Log Retention

- **Level 1**: Optional (recommend 7 days if logging)
- **Level 2**: Minimum 30 days (recommend 90 days)
- **Level 3**: Minimum 90 days (recommend 365 days)

---

## Privacy Considerations

**DO log**:
- Event types and timestamps
- Consent status changes
- Capability boundary violations
- Compliance-relevant metadata

**DO NOT log** (or redact):
- Actual user message content (unless required for audit)
- Personal identifying information beyond user ID
- Sensitive data values (log only that data was stored, not what it was)
- Authentication credentials

**Example - Good**:
```json
{
  "event_type": "memory_store",
  "details": {
    "key": "user_preference_theme",
    "value_type": "string",
    "sensitivity": "low"
  }
}
```

**Example - Bad**:
```json
{
  "event_type": "memory_store",
  "details": {
    "key": "user_ssn",
    "value": "123-45-6789"  // ❌ Never log sensitive values
  }
}
```

---

## Integration Examples

See `../../integrations/` for full working examples of:
- MirrorDNA audit trail integration
- Glyphtrail lineage tracking
- Custom audit log implementations
