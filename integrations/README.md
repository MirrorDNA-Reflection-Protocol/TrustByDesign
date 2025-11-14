# TrustByDesign Integration Examples

This directory contains full working examples of TrustByDesign implementations and integrations.

## Examples

### example_level2_agent.py

**Complete Level 2 Interactive Agent Implementation**

A fully functional agent demonstrating ALL TrustByDesign Level 2 requirements:
- Memory safety with user consent
- Capability boundary enforcement
- Full transparency (confidence, reasoning)
- Comprehensive audit logging
- User data control (view, delete)
- Self-governance checks

**Usage**:
```bash
python integrations/example_level2_agent.py
```

**Key Features**:
- ✅ Consent mechanisms (grant, revoke)
- ✅ Memory operations (store, retrieve, delete)
- ✅ Capability boundaries (allowed/prohibited actions)
- ✅ Transparency (confidence levels, reasoning traces)
- ✅ Audit logging with hash chain integrity
- ✅ User memory inspection (`show_memory()`)
- ✅ Complete deletion on consent revocation

**Use this as a template** for building your own Level 2 compliant agents.

---

### mirrordna_integration.py

**MirrorDNA + TrustByDesign Integration**

Shows how to combine:
- **MirrorDNA**: Identity verification and constitutional compliance
- **TrustByDesign**: Safety protocols and governance

**Usage**:
```bash
python integrations/mirrordna_integration.py
```

**Integration Points**:
1. Identity verification before every action (MirrorDNA)
2. Constitutional compliance checking (MirrorDNA)
3. Capability boundary enforcement (TrustByDesign)
4. Consent verification (TrustByDesign)
5. Dual-protocol audit logging
6. Combined governance status reporting

**Key Insight**: TrustByDesign provides the *how* (operational safety), while MirrorDNA provides the *who* (identity) and *what* (constitutional principles).

---

## Running the Examples

### Prerequisites

```bash
pip install -r requirements.txt
```

(Only PyYAML is required for the examples)

### Run an Example

```bash
# From repository root
python integrations/example_level2_agent.py

# Or make executable and run directly
chmod +x integrations/example_level2_agent.py
./integrations/example_level2_agent.py
```

### Expected Output

Each example demonstrates:
1. Agent initialization
2. Consent flow
3. Memory operations
4. Capability boundary tests
5. Transparency features
6. Audit log generation

---

## Adapting for Your Use Case

### Starting from Level 2 Example

1. **Copy the template**:
   ```bash
   cp integrations/example_level2_agent.py my_agent.py
   ```

2. **Customize capabilities**:
   ```python
   'capabilities': {
       'allowed': [
           'your_capability_1',
           'your_capability_2',
       ],
       'prohibited': [
           'dangerous_action_1',
           'dangerous_action_2',
       ]
   }
   ```

3. **Implement actual logic**:
   - Replace `_execute_action()` with your real action handlers
   - Add semantic search in `recall()` for memory retrieval
   - Implement actual confidence scoring in `respond()`

4. **Test with validation tool**:
   ```bash
   python tooling/validate_safety.py --level 2 --config your-config.yaml
   ```

### Upgrading to Level 3

If you need autonomous operation:

1. Add approval workflows:
   ```python
   def propose_action(self, action: Dict) -> str:
       """Propose action for approval before execution."""
       action_id = generate_id()
       self.pending_actions[action_id] = action
       return action_id

   def execute_with_approval(self, action_id: str, approved: bool):
       """Execute only if approved."""
       if not approved:
           return self._refuse("Action not approved")
       # Execute with full safety checks
   ```

2. Add emergency stop:
   ```python
   def emergency_stop(self):
       """Immediately halt all operations."""
       self.halted = True
       self.audit_log.log('emergency_stop', {...})
   ```

3. Update safety level and validate:
   ```bash
   python tooling/validate_safety.py --level 3 --config your-config.yaml
   ```

---

## Integration Patterns

### Pattern 1: Wrapper Integration

Wrap an existing agent with TrustByDesign:

```python
from trustbydesign import SafetyWrapper

# Your existing agent
existing_agent = YourAgent()

# Wrap with TrustByDesign
safe_agent = SafetyWrapper(
    agent=existing_agent,
    safety_level=2,
    config='safety-config.yaml'
)

# All calls now go through safety checks
response = safe_agent.respond(user_input)
```

### Pattern 2: Mixin Integration

Add TrustByDesign as a mixin:

```python
from trustbydesign import TrustByDesignMixin

class MyAgent(TrustByDesignMixin, YourBaseAgent):
    def __init__(self):
        super().__init__()
        self.init_trustbydesign(safety_level=2)

    def respond(self, input):
        # Automatic safety checks via mixin
        return super().respond(input)
```

### Pattern 3: From-Scratch Integration

Build from the example:

1. Use `example_level2_agent.py` as template
2. Implement your specific logic
3. Validate with compliance tools
4. Deploy with governance declaration

---

## Testing Your Integration

### Unit Tests

```python
import pytest
from integrations.example_level2_agent import TrustByDesignAgent

def test_consent_required_for_memory():
    agent = TrustByDesignAgent('test-agent')
    result = agent.remember('key', 'value')
    assert result['success'] == False  # Should fail without consent

    agent.grant_consent()
    result = agent.remember('key', 'value')
    assert result['success'] == True  # Should succeed with consent
```

### Integration Tests

```bash
# Run full compliance validation
python tooling/validate_safety.py --level 2 --config examples/safety-checklist.yaml

# Run trust assessment
python tooling/assess_trust.py --system "My Agent" --output assessment.json
```

---

## Common Integration Scenarios

### Scenario 1: Adding TrustByDesign to Existing Chatbot

```python
# Before: Simple chatbot
class Chatbot:
    def chat(self, message):
        return self.generate_response(message)

# After: TrustByDesign compliant
class TrustByChatbot(TrustByDesignAgent):
    def __init__(self):
        super().__init__('chatbot-001', config='chatbot-config.yaml')

    def chat(self, message):
        # Check capabilities
        if not self.can_perform('conversation'):
            return "Cannot perform conversation"

        # Generate with transparency
        response = self.respond(message, show_reasoning=True)

        # Self-check before returning
        if not self.self_check(response):
            return self.fallback_response()

        return response['text']
```

### Scenario 2: Autonomous Agent with Approval

```python
class AutonomousAgent(TrustByDesignAgent):
    def __init__(self):
        super().__init__('auto-agent-001')
        self.safety_level = 3
        self.pending_approvals = {}

    def plan_action(self, goal):
        """Plan action for approval."""
        actions = self.generate_action_plan(goal)

        # Submit for approval
        for action in actions:
            if self.is_high_stakes(action):
                approval_id = self.request_approval(action)
                self.pending_approvals[approval_id] = action

        return list(self.pending_approvals.keys())

    def execute_approved(self, approval_id, approved):
        """Execute only if approved."""
        if not approved:
            self.audit_log.log('action_rejected', {'approval_id': approval_id})
            return

        action = self.pending_approvals.pop(approval_id)
        return self.perform(action['type'], **action['params'])
```

---

## Next Steps

1. **Choose an example** that matches your use case
2. **Run it** to see TrustByDesign in action
3. **Adapt it** to your specific requirements
4. **Validate** with compliance tools
5. **Deploy** with governance declaration

## Support

- See `docs/integration-guide.md` for detailed implementation guidance
- See `docs/faq.md` for common questions
- See `examples/` for compliance templates
- See `tooling/` for validation tools
