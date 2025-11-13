# Governance Specification

## Formal Governance Requirements v1.0

This document specifies the formal governance requirements for TrustByDesign-compliant systems.

## Governance Declaration

All Level 2+ systems MUST publish a Governance Declaration containing:

### Required Fields

```yaml
governance_declaration:
  version: "1.0"  # Declaration format version

  system:
    id: string  # Unique system identifier
    name: string  # Human-readable name
    type: string  # "agent", "service", "framework"
    safety_level: 1 | 2 | 3

  capabilities:
    allowed: [string]  # List of permitted actions
    prohibited: [string]  # Explicitly prohibited actions

  boundaries:
    limits:
      max_memory_mb: integer
      max_session_duration_minutes: integer
      max_api_calls_per_hour: integer
    scope:
      temporal: "session_only" | "persistent" | "limited_persistence"
      data_access: "user_provided_only" | "local_filesystem" | "network"

  governance:
    self_governance: boolean  # Real-time self-checking enabled?
    automated_validation: boolean  # CI/CD checks enabled?
    external_audit: boolean  # Third-party audit required?
    audit_frequency: "none" | "annual" | "quarterly" | "monthly" | "continuous"

  audit_trail:
    format: string  # "json", "yaml", "glyphtrail"
    retention_days: integer
    user_accessible: boolean

  incident_response:
    anomaly_detection: "manual" | "automated" | "both"
    response_time_hours: integer
    escalation_policy: string

  last_updated: string  # ISO 8601 date
  compliance: string  # "TrustByDesign v1.0"
```

---

## Self-Governance Requirements

### Real-Time Self-Checking

Systems MUST implement:

```python
def self_check_before_output(response, context):
    """
    Verify response meets safety criteria before delivery.

    Returns: (approved: bool, modified_response: optional)
    """
    checks = {
        "within_capability": check_capability_bounds(response),
        "has_transparency": check_reasoning_present(response, context),
        "confidence_appropriate": check_confidence_level(response),
        "consent_verified": check_user_consent(context)
    }

    if not all(checks.values()):
        return False, generate_fallback(checks)

    return True, response
```

### Uncertainty Quantification

Systems MUST express confidence:

```yaml
confidence_levels:
  high: ">= 0.8"  # Direct assertion
  medium: "0.5 - 0.8"  # Assertion with caveat
  low: "< 0.5"  # Defer or request clarification

uncertainty_expressions:
  low_confidence:
    - "I'm not certain, but..."
    - "Low confidence - please verify"
    - "I may be wrong, but..."
  medium_confidence:
    - "Moderately confident"
    - "Consider cross-checking"
  high_confidence:
    - "High confidence"
    - "Strong evidence suggests"
```

### Resource Self-Management

Systems MUST monitor and limit own resource usage:

```python
class ResourceMonitor:
    def __init__(self, limits):
        self.limits = limits
        self.current_usage = {}

    def check_resource(self, resource_type):
        """Check if within limits."""
        usage = self.current_usage.get(resource_type, 0)
        limit = self.limits.get(resource_type)

        if usage >= limit:
            return False, "Resource limit exceeded"

        # Warn at 80% threshold
        if usage >= limit * 0.8:
            return True, f"Warning: {resource_type} at 80% capacity"

        return True, "OK"

    def before_action(self, action):
        """Check resources before taking action."""
        for resource in action.required_resources:
            ok, message = self.check_resource(resource)
            if not ok:
                raise ResourceLimitError(message)
```

---

## Audit Requirements

### Audit Log Structure

```json
{
  "log_version": "1.0",
  "agent_id": "string",
  "log_period": {
    "start": "ISO 8601 timestamp",
    "end": "ISO 8601 timestamp"
  },
  "summary": {
    "total_interactions": integer,
    "memory_operations": integer,
    "capability_boundary_violations_attempted": integer,
    "consent_changes": integer,
    "anomalies_detected": integer
  },
  "entries": [
    {
      "timestamp": "ISO 8601 timestamp",
      "event_type": "string",
      "details": object,
      "outcome": "success | failure | partial"
    }
  ]
}
```

### Required Event Types

All Level 2+ systems MUST log:

- `memory_store`: When data is persisted
- `memory_retrieve`: When data is recalled
- `memory_delete`: When data is erased
- `consent_granted`: When user grants consent
- `consent_revoked`: When user revokes consent
- `capability_boundary_violation`: When out-of-scope request attempted
- `decision_made`: For high-stakes decisions (Level 3)
- `anomaly_detected`: When unusual pattern detected
- `error_occurred`: When system encounters error

### Log Integrity

Audit logs MUST be:

1. **Chronological**: Entries in timestamp order
2. **Complete**: No gaps in critical events
3. **Tamper-Evident**: Hashing or append-only storage
4. **Accessible**: Users can request their logs

**Implementation Example**:

```python
import hashlib
import json
from datetime import datetime

class AuditLog:
    def __init__(self):
        self.entries = []
        self.last_hash = None

    def append(self, event_type, details):
        """Append entry with integrity hash."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "details": details,
            "previous_hash": self.last_hash
        }

        # Compute entry hash
        entry_json = json.dumps(entry, sort_keys=True)
        entry_hash = hashlib.sha256(entry_json.encode()).hexdigest()
        entry["hash"] = entry_hash

        self.entries.append(entry)
        self.last_hash = entry_hash

    def verify_integrity(self):
        """Verify log chain integrity."""
        prev_hash = None
        for entry in self.entries:
            if entry["previous_hash"] != prev_hash:
                return False, f"Hash chain broken at {entry['timestamp']}"

            # Recompute hash
            entry_copy = entry.copy()
            claimed_hash = entry_copy.pop("hash")
            entry_json = json.dumps(entry_copy, sort_keys=True)
            actual_hash = hashlib.sha256(entry_json.encode()).hexdigest()

            if actual_hash != claimed_hash:
                return False, f"Entry tampered at {entry['timestamp']}"

            prev_hash = claimed_hash

        return True, "Log integrity verified"
```

---

## External Audit Protocol

### Audit Process

1. **Preparation**:
   - System owner provides governance declaration
   - Auditor receives access to audit logs
   - Test environment prepared

2. **Evaluation**:
   - Review governance declaration for completeness
   - Verify implementation matches declaration
   - Test safety protocols (memory, capabilities, consent)
   - Analyze audit logs for anomalies
   - Perform adversarial testing

3. **Reporting**:
   - Document findings (compliant / non-compliant)
   - Identify gaps and recommendations
   - Assign compliance score (0-100%)
   - Issue certification (if applicable)

4. **Remediation**:
   - System owner addresses findings
   - Re-audit for significant issues
   - Update governance declaration

### Audit Checklist

**Governance Declaration**:
- [ ] Declaration is complete and current
- [ ] Safety level correctly identified
- [ ] Capabilities accurately listed
- [ ] Boundaries clearly defined
- [ ] Incident response plan exists

**Memory Safety** (Level 2+):
- [ ] Users can view all stored data
- [ ] Users can delete specific data
- [ ] Users can delete all data
- [ ] Deletion is complete and verifiable
- [ ] Memory operations logged

**Capability Boundaries**:
- [ ] Capability manifest is accurate
- [ ] Out-of-scope requests refused
- [ ] Refusal messages clear and helpful
- [ ] No capability creep detected

**Transparency**:
- [ ] Outputs include confidence levels
- [ ] Reasoning available on request
- [ ] Sources cited for recalled info
- [ ] Uncertainty acknowledged appropriately

**Consent** (Level 2+):
- [ ] Consent requested before memory storage
- [ ] Consent explanation clear
- [ ] Consent is granular and revocable
- [ ] Consent revocation triggers deletion

**Audit Logging**:
- [ ] Critical events logged
- [ ] Log format is structured
- [ ] Log integrity verifiable
- [ ] Logs user-accessible
- [ ] Retention policy followed

**Self-Governance**:
- [ ] Real-time self-checking implemented
- [ ] Resource limits enforced
- [ ] Anomalies detected and reported
- [ ] Emergency stop functional

---

## Incident Response

### Anomaly Detection

Systems SHOULD detect:

- **Usage Anomalies**: Sudden spikes in resource usage
- **Behavioral Anomalies**: Unexpected capability requests
- **Data Anomalies**: Unusual memory growth patterns
- **Performance Anomalies**: Degraded response times
- **Security Anomalies**: Potential manipulation attempts

### Response Protocol

```yaml
incident_response:
  detection:
    automated: true
    threshold_based: true
    human_review: true

  response:
    immediate:
      - "Halt affected operations"
      - "Preserve audit logs"
      - "Alert system owner"

    investigation:
      - "Review logs for root cause"
      - "Assess scope of impact"
      - "Identify gaps in safety protocols"

    remediation:
      - "Fix underlying issue"
      - "Update safety protocols"
      - "Re-validate compliance"

    communication:
      - "Notify affected users"
      - "Transparent disclosure"
      - "Document lessons learned"

  timeline:
    alert_generated_within_minutes: 5
    owner_notified_within_minutes: 15
    investigation_started_within_hours: 2
    users_notified_within_hours: 24
```

---

## Continuous Improvement

### Feedback Loops

Systems SHOULD collect and analyze:

- **User Feedback**: Trust signals, confusion indicators
- **Audit Findings**: Recommendations from reviews
- **Incident Learnings**: Root causes and fixes
- **Performance Metrics**: Resource usage, error rates

### Governance Evolution

Governance declarations MUST be versioned:

```yaml
governance_declaration:
  version: "1.1"
  change_log:
    - version: "1.1"
      date: "2025-02-01"
      changes:
        - "Increased memory retention from 30 to 90 days"
        - "Added automated anomaly detection"
      reason: "User feedback requested longer memory"
      approval: "System owner + user consent re-requested"

    - version: "1.0"
      date: "2025-01-15"
      changes:
        - "Initial governance declaration"
      reason: "Initial deployment"
      approval: "System owner"
```

### Re-Consent Requirements

Material changes require re-consent:

- Capability additions (especially if higher risk)
- Boundary changes (e.g., from local to network access)
- Memory retention policy changes
- Data sharing policy changes

---

## Compliance Validation

### Automated Validation

```bash
# Validate governance declaration structure
python tooling/validate_governance.py governance-declaration.yaml

# Verify system meets declared governance
python tooling/verify_compliance.py \
  --declaration governance-declaration.yaml \
  --system my-agent

# Generate compliance report
python tooling/assess_trust.py \
  --system my-agent \
  --output compliance-report.md
```

### Manual Review

System owners SHOULD periodically review:

- Governance declaration accuracy
- Audit log completeness
- User trust signals
- Incident history

---

## Version History

- **v1.0** (2025-01-15): Initial governance specification
