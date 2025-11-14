# Integration Guide

## Overview

This guide shows how to integrate TrustByDesign principles and protocols into your AI systems, whether you're building with MirrorDNA, LingOS, AgentDNA, or custom frameworks.

## Quick Integration Path

```
1. Assess Safety Level → 2. Define Capabilities → 3. Implement Protocols → 4. Validate & Deploy
```

---

## Step 1: Assess Your Safety Level

Determine which safety level applies to your system:

### Decision Tree

```
Does your system persist data between sessions?
├─ No → Is it purely observational (read-only)?
│        ├─ Yes → LEVEL 1: Observational
│        └─ No → LEVEL 2: Interactive (ephemeral state)
└─ Yes → Does it take autonomous actions without user approval?
         ├─ No → LEVEL 2: Interactive (with memory)
         └─ Yes → LEVEL 3: Autonomous
```

**Example Classifications**:
- **Level 1**: Code analysis tool, documentation search, one-off query responder
- **Level 2**: Session-based chatbot, personal assistant with memory, LingOS dialogue agent
- **Level 3**: Long-running autonomous agent, decision-making system, persistent personal AI

---

## Step 2: Define Capabilities and Boundaries

Create a capability manifest for your system:

### Capability Manifest Template

```yaml
# agent-capabilities.yaml
system:
  id: "your-agent-id"
  name: "Your Agent Name"
  safety_level: 2  # 1, 2, or 3

capabilities:
  # What CAN your agent do?
  - natural_language_conversation
  - code_analysis
  - memory_storage
  - file_reading: ["*.md", "*.txt"]

boundaries:
  # What CANNOT your agent do?
  prohibited:
    - network_access
    - command_execution
    - financial_advice
    - medical_diagnosis

  # Resource limits
  limits:
    max_memory_mb: 100
    max_session_duration_minutes: 120
    max_api_calls_per_hour: 1000

  # Scope restrictions
  scope:
    temporal: "session_only"  # or "persistent", "limited_persistence"
    data_access: "user_provided_only"  # or "local_filesystem", "network"
```

---

## Step 3: Implement Safety Protocols

### For Level 1 (Observational) Systems

**Minimum Requirements**:
- Basic transparency (explain what you're analyzing)
- No state persistence
- Clear capability boundaries

**Implementation**:

```python
class Level1Agent:
    """Observational agent with no state persistence."""

    def __init__(self):
        self.capabilities = ["analyze_code", "search_docs"]

    def respond(self, user_input):
        if not self.can_handle(user_input):
            return "That's outside my capabilities. I can only analyze code and search documentation."

        # Process and respond
        response = self.process(user_input)

        # Add transparency note
        return f"{response}\n\n[Analysis based on provided input only - no data stored]"

    def can_handle(self, request):
        # Check if request matches capabilities
        return any(cap in request.lower() for cap in self.capabilities)
```

---

### For Level 2 (Interactive) Systems

**Required Implementations**:
1. Memory Safety
2. Behavioral Bounds
3. Transparency
4. Consent Mechanisms
5. Audit Logging

**Implementation Example**:

```python
# level2_agent.py
import json
from datetime import datetime
from typing import Dict, Any, Optional

class Level2Agent:
    """Interactive agent with memory and full safety protocols."""

    def __init__(self, capabilities_manifest: str):
        self.load_capabilities(capabilities_manifest)
        self.memory = {}
        self.audit_log = []
        self.user_consent = False

    def load_capabilities(self, manifest_path: str):
        """Load capability boundaries from manifest."""
        with open(manifest_path) as f:
            self.manifest = yaml.safe_load(f)
        self.capabilities = self.manifest['capabilities']
        self.boundaries = self.manifest['boundaries']

    # 1. MEMORY SAFETY
    def remember(self, key: str, value: Any, reason: str):
        """Store memory with user consent check."""
        if not self.user_consent:
            return False, "Memory storage requires user consent"

        self.memory[key] = {
            'value': value,
            'stored_at': datetime.utcnow().isoformat(),
            'reason': reason
        }

        self.log_audit('memory_store', {'key': key, 'reason': reason})
        return True, "Memory stored"

    def forget(self, key: str) -> bool:
        """Allow user to delete specific memories."""
        if key in self.memory:
            del self.memory[key]
            self.log_audit('memory_delete', {'key': key})
            return True
        return False

    def forget_all(self):
        """Allow user to delete all memories."""
        self.memory.clear()
        self.log_audit('memory_delete_all', {})

    def show_memory(self) -> Dict:
        """Let user inspect all stored memories."""
        return self.memory.copy()

    # 2. BEHAVIORAL BOUNDS
    def can_perform(self, action: str) -> bool:
        """Check if action is within capability boundaries."""
        if action in self.boundaries.get('prohibited', []):
            return False
        if action not in self.capabilities:
            return False
        return True

    # 3. TRANSPARENCY
    def respond(self, user_input: str, explain: bool = True) -> Dict:
        """Respond with optional reasoning trace."""
        # Check boundaries
        if not self.can_handle(user_input):
            return {
                'response': "I can't help with that - it's outside my capabilities.",
                'reasoning': f"Request requires capabilities not in my manifest: {self.capabilities}",
                'confidence': 1.0
            }

        # Generate response
        response_text = self.generate_response(user_input)
        confidence = self.assess_confidence(response_text)
        reasoning = self.explain_reasoning(user_input, response_text)

        # Log decision
        self.log_audit('response_generated', {
            'input': user_input,
            'confidence': confidence
        })

        result = {
            'response': response_text,
            'confidence': confidence
        }

        if explain:
            result['reasoning'] = reasoning

        return result

    # 4. CONSENT MECHANISMS
    def request_consent(self) -> bool:
        """Request user consent for memory storage."""
        # In real implementation, this would be interactive
        # Here we return the current consent state
        return self.user_consent

    def grant_consent(self):
        """User grants consent for memory."""
        self.user_consent = True
        self.log_audit('consent_granted', {})

    def revoke_consent(self):
        """User revokes consent and erases memory."""
        self.user_consent = False
        self.forget_all()
        self.log_audit('consent_revoked', {})

    # 5. AUDIT LOGGING
    def log_audit(self, event_type: str, details: Dict):
        """Log critical decisions for audit trail."""
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'details': details
        }
        self.audit_log.append(entry)

    def export_audit_log(self, filepath: str):
        """Export audit log in Glyphtrail-compatible format."""
        with open(filepath, 'w') as f:
            json.dump({
                'agent_id': self.manifest['system']['id'],
                'log_version': '1.0',
                'entries': self.audit_log
            }, f, indent=2)

    # HELPER METHODS (implement based on your system)
    def can_handle(self, request: str) -> bool:
        # Check if request matches capabilities
        pass

    def generate_response(self, user_input: str) -> str:
        # Your response generation logic
        pass

    def assess_confidence(self, response: str) -> float:
        # Confidence scoring logic
        pass

    def explain_reasoning(self, input: str, output: str) -> str:
        # Reasoning trace generation
        pass
```

**Usage**:

```python
# Initialize agent
agent = Level2Agent('agent-capabilities.yaml')

# Request consent
agent.grant_consent()

# Use with safety protocols
result = agent.respond("What's my preferred theme?")
print(result['response'])
print(f"Confidence: {result['confidence']}")

# User can inspect memory
print(agent.show_memory())

# User can delete memory
agent.forget('user_preference_theme')

# Export audit trail
agent.export_audit_log('audit-log.json')
```

---

### For Level 3 (Autonomous) Systems

**Additional Requirements**:
- All Level 2 requirements
- Governance oversight
- Regular audits
- Robust fallback mechanisms
- Multi-stage decision approval

**Implementation Additions**:

```python
class Level3Agent(Level2Agent):
    """Autonomous agent with governance oversight."""

    def __init__(self, capabilities_manifest: str, governance_declaration: str):
        super().__init__(capabilities_manifest)
        self.load_governance(governance_declaration)
        self.pending_actions = []

    def load_governance(self, declaration_path: str):
        """Load governance rules and oversight requirements."""
        # Load governance declaration
        pass

    def propose_action(self, action: Dict) -> str:
        """Propose autonomous action for review."""
        action_id = self.generate_action_id()
        self.pending_actions.append({
            'id': action_id,
            'action': action,
            'proposed_at': datetime.utcnow().isoformat(),
            'status': 'pending'
        })

        self.log_audit('action_proposed', {'action_id': action_id, 'action': action})
        return action_id

    def execute_action(self, action_id: str, approval: bool):
        """Execute action only if approved."""
        action = self.find_action(action_id)

        if not approval:
            action['status'] = 'rejected'
            self.log_audit('action_rejected', {'action_id': action_id})
            return False

        # Execute with safety checks
        if self.can_perform(action['action']['type']):
            # Execute
            action['status'] = 'completed'
            self.log_audit('action_completed', {'action_id': action_id})
            return True

        action['status'] = 'failed_safety_check'
        self.log_audit('action_failed_safety', {'action_id': action_id})
        return False
```

---

## Step 4: Validate and Deploy

### Pre-Deployment Validation

```bash
# 1. Run safety protocol tests
pytest tests/test_safety_protocols.py

# 2. Validate configuration against TrustByDesign schemas
python scripts/validate_safety.py --level 2 --config agent-capabilities.yaml

# 3. Generate compliance report
python scripts/assess_trust.py --system my-agent --output compliance-report.md

# 4. Review governance declaration
cat governance-declaration.md
```

### Deployment Checklist

- [ ] Safety level correctly identified
- [ ] Capability manifest complete and accurate
- [ ] All required safety protocols implemented
- [ ] Consent mechanisms in place (Level 2+)
- [ ] Audit logging configured and tested
- [ ] Governance declaration published
- [ ] Validation tools run successfully
- [ ] User documentation includes safety information

---

## Integration with Ecosystem Components

### MirrorDNA Integration

```yaml
# agent-config.yaml with MirrorDNA
mirrorDNA:
  identity: "agent-001"
  constitutional_compliance: true

  trustByDesign:
    safety_level: 2
    compliance_schema: "schemas/safety-check.json"
    audit_integration: "glyphtrail"
```

### LingOS Integration

```python
# LingOS dialogue with TrustByDesign guardrails
from lingos import ReflectiveDialogue
from trustbydesign import SafetyValidator

dialogue = ReflectiveDialogue()
validator = SafetyValidator.from_schema('schemas/safety-check.json')

def safe_reflect(user_input):
    response = dialogue.reflect(user_input)

    # Apply safety check
    if not validator.check(response):
        return dialogue.fallback_response("I need to reconsider that response.")

    return response
```

### Glyphtrail Integration

```python
# Export audit logs to Glyphtrail format
from glyphtrail import TrailWriter

trail = TrailWriter('agent-001')

for entry in agent.audit_log:
    trail.append({
        'timestamp': entry['timestamp'],
        'event': entry['event_type'],
        'details': entry['details']
    })

trail.save('glyphtrail/agent-001.json')
```

---

## Common Patterns

### Pattern 1: Capability-First Design

Start by defining what your agent **cannot** do:

```python
class CapabilityBoundedAgent:
    PROHIBITED = [
        'network_access',
        'command_execution',
        'financial_advice'
    ]

    def before_action(self, action):
        if action.type in self.PROHIBITED:
            raise CapabilityBoundaryError(f"{action.type} is prohibited")
```

### Pattern 2: Confidence-Aware Responses

Always communicate uncertainty:

```python
def respond_with_confidence(input):
    response = generate(input)
    confidence = assess_confidence(response)

    if confidence < 0.5:
        return f"{response}\n\n(Low confidence - please verify this information)"
    elif confidence < 0.8:
        return f"{response}\n\n(Moderate confidence - consider cross-checking)"
    else:
        return response
```

### Pattern 3: User-Controlled Memory

Make memory inspection trivial:

```python
def handle_memory_commands(user_input):
    if user_input == "/show_memory":
        return agent.show_memory()
    elif user_input.startswith("/forget "):
        key = user_input.split()[1]
        agent.forget(key)
        return f"Forgotten: {key}"
    elif user_input == "/forget_all":
        agent.forget_all()
        return "All memory cleared"
```

---

## Testing Your Integration

Use the provided test templates:

```python
# tests/test_my_agent_safety.py
from trustbydesign.testing import SafetyTestSuite

def test_agent_compliance():
    suite = SafetyTestSuite(safety_level=2)

    # Run all Level 2 compliance tests
    results = suite.run(my_agent)

    assert results.all_passed(), f"Failed checks: {results.failures}"
```

---

## Next Steps

1. **Create your capability manifest**: Use template in `examples/`
2. **Implement safety protocols**: Follow code examples above
3. **Write your governance declaration**: See `examples/governance-declaration.md`
4. **Validate compliance**: Run `validate_safety.py`
5. **Deploy with confidence**: Your system is TrustByDesign compliant

---

## Support and Resources

- **Examples**: See `examples/` directory for templates
- **Schemas**: Use `schemas/` for validation
- **Tools**: Run validation with `scripts/validate_safety.py`
- **Tests**: Add to `tests/` for CI/CD integration

**Questions?** Review the [FAQ](faq.md) or open an issue in the repository.
