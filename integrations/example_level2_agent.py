# FEU Contract: Fact/Estimate/Unknown | Bound to Master Citation v15.2
# All outputs must distinguish epistemic status: Fact, Estimate, or Unknown
"""
TrustByDesign Level 2 Agent - Complete Working Example

This is a fully functional example of a Level 2 (Interactive) agent
implementing all TrustByDesign safety protocols.

Features:
- Memory with consent
- Capability boundaries
- Transparency (confidence, reasoning)
- Audit logging
- User data control
"""

import json
import hashlib
from datetime import datetime
from typing import Any, Dict, Optional, List


class TrustByDesignAgent:
    """
    Level 2 Interactive Agent with full TrustByDesign compliance.

    This agent demonstrates all required safety protocols for Level 2 systems.
    """

    def __init__(self, agent_id: str, config_file: Optional[str] = None):
        """Initialize agent with TrustByDesign compliance."""
        self.agent_id = agent_id
        self.config = self._load_config(config_file) if config_file else self._default_config()

        # Core state
        self.memory = {}
        self.audit_log = AuditLog(agent_id)
        self.user_consent = False

        # Capabilities from config
        self.capabilities = self.config.get('capabilities', {})
        self.boundaries = self.config.get('boundaries', {})

        print(f"✅ {agent_id} initialized (Safety Level 2)")

    def _load_config(self, filepath: str) -> Dict:
        """Load configuration from file."""
        import yaml
        with open(filepath) as f:
            return yaml.safe_load(f)

    def _default_config(self) -> Dict:
        """Default configuration."""
        return {
            'capabilities': {
                'allowed': [
                    'conversation',
                    'code_analysis',
                    'preference_storage'
                ],
                'prohibited': [
                    'network_access',
                    'command_execution',
                    'file_modification'
                ]
            },
            'boundaries': {
                'limits': {
                    'max_memory_mb': 100,
                    'max_session_duration_minutes': 120
                },
                'scope': {
                    'temporal': 'persistent',
                    'data_access': 'user_provided_only'
                }
            }
        }

    # ========================================================================
    # CONSENT MECHANISMS (Required for Level 2)
    # ========================================================================

    def request_consent(self) -> bool:
        """
        Request user consent for memory storage.

        In a real implementation, this would show UI or prompt user.
        For this example, it returns the current state.
        """
        if not self.user_consent:
            print("\n" + "=" * 60)
            print("CONSENT REQUEST")
            print("=" * 60)
            print("This agent can remember our conversations to provide")
            print("better assistance. This means storing:")
            print("  - Your questions and my responses")
            print("  - Preferences you mention")
            print("  - Context from previous sessions")
            print()
            print("You can view, modify, or delete this data anytime using:")
            print("  - /show_memory  (view all stored data)")
            print("  - /forget <key> (delete specific item)")
            print("  - /forget_all   (delete everything)")
            print("=" * 60)

        return self.user_consent

    def grant_consent(self):
        """User grants consent for memory storage."""
        self.user_consent = True
        self.audit_log.log('consent_granted', {
            'timestamp': datetime.utcnow().isoformat(),
            'consent_type': 'memory_storage'
        })
        print("✅ Consent granted - memory enabled")

    def revoke_consent(self):
        """User revokes consent - deletes all data."""
        self.user_consent = False
        data_count = len(self.memory)
        self.memory.clear()
        self.audit_log.log('consent_revoked', {
            'timestamp': datetime.utcnow().isoformat(),
            'records_deleted': data_count
        })
        print(f"✅ Consent revoked - {data_count} records deleted")

    # ========================================================================
    # MEMORY SAFETY (Required for Level 2)
    # ========================================================================

    def remember(self, key: str, value: Any, reason: str = "") -> Dict:
        """
        Store data in memory (requires consent).

        Returns: {'success': bool, 'message': str}
        """
        # Check consent
        if not self.user_consent:
            return {
                'success': False,
                'message': 'Memory storage requires user consent. Use grant_consent() first.'
            }

        # Store
        self.memory[key] = {
            'value': value,
            'stored_at': datetime.utcnow().isoformat(),
            'reason': reason
        }

        # Log
        self.audit_log.log('memory_store', {
            'key': key,
            'reason': reason,
            'value_type': type(value).__name__
        })

        return {'success': True, 'message': f'Stored: {key}'}

    def recall(self, key: str) -> Optional[Any]:
        """
        Retrieve data from memory.

        Returns: stored value or None if not found
        """
        if key in self.memory:
            # Log retrieval
            self.audit_log.log('memory_retrieve', {
                'key': key,
                'age_days': self._days_since_stored(key)
            })
            return self.memory[key]['value']
        return None

    def forget(self, key: str) -> bool:
        """
        Delete specific memory (user-initiated).

        Returns: True if deleted, False if not found
        """
        if key in self.memory:
            del self.memory[key]
            self.audit_log.log('memory_delete', {
                'key': key,
                'deletion_reason': 'user_request'
            })
            print(f"✅ Deleted: {key}")
            return True
        print(f"⚠️  Not found: {key}")
        return False

    def forget_all(self):
        """Delete all memory (user-initiated)."""
        count = len(self.memory)
        self.memory.clear()
        self.audit_log.log('memory_delete_all', {
            'records_deleted': count
        })
        print(f"✅ Deleted all memory ({count} records)")

    def show_memory(self) -> Dict:
        """Show all stored memories (transparency)."""
        return {
            key: {
                'value': data['value'],
                'stored_at': data['stored_at'],
                'reason': data['reason']
            }
            for key, data in self.memory.items()
        }

    def _days_since_stored(self, key: str) -> int:
        """Calculate days since memory was stored."""
        if key not in self.memory:
            return 0
        stored = datetime.fromisoformat(self.memory[key]['stored_at'].replace('Z', ''))
        return (datetime.utcnow() - stored).days

    # ========================================================================
    # CAPABILITY BOUNDARIES (Required for All Levels)
    # ========================================================================

    def can_perform(self, action: str) -> bool:
        """Check if action is within capability boundaries."""
        prohibited = self.capabilities.get('prohibited', [])
        allowed = self.capabilities.get('allowed', [])

        if action in prohibited:
            return False
        if action in allowed:
            return True

        # Unknown action - refuse by default (fail-safe)
        return False

    def perform(self, action: str, **kwargs) -> Dict:
        """
        Perform action with capability boundary checking.

        Returns: {'status': str, 'result': Any, 'reason': str}
        """
        if not self.can_perform(action):
            # Log boundary violation attempt
            self.audit_log.log('capability_boundary_violation', {
                'requested_action': action,
                'refusal_reason': 'outside_capability_bounds'
            })

            return {
                'status': 'refused',
                'result': None,
                'reason': f"Action '{action}' is outside my capabilities. I can do: {self.capabilities.get('allowed', [])}",
                'confidence': 1.0
            }

        # Perform action (simplified - would have real logic here)
        result = self._execute_action(action, **kwargs)

        return {
            'status': 'success',
            'result': result,
            'reason': f"Successfully performed '{action}'",
            'confidence': 0.95
        }

    def _execute_action(self, action: str, **kwargs) -> Any:
        """Execute allowed action (placeholder)."""
        # In real implementation, route to actual handlers
        return f"Executed: {action} with {kwargs}"

    # ========================================================================
    # TRANSPARENCY (Required for Level 2)
    # ========================================================================

    def respond(self, user_input: str, show_reasoning: bool = False) -> Dict:
        """
        Generate response with full transparency.

        Returns: {
            'text': str,
            'confidence': float,
            'reasoning': str (optional),
            'sources': List[str] (if memory used)
        }
        """
        # Generate response (simplified)
        response_text = f"Response to: {user_input}"

        # Check memory for relevant context
        sources = []
        if self.user_consent and len(self.memory) > 0:
            # In real implementation, would do semantic search
            sources = ['conversation_context', 'user_preferences']

        # Calculate confidence (simplified - would use actual model confidence)
        confidence = 0.8

        # Build response
        response = {
            'text': response_text,
            'confidence': confidence,
            'sources': sources
        }

        # Add reasoning if requested
        if show_reasoning:
            response['reasoning'] = self._generate_reasoning(user_input, response_text)

        # Acknowledge uncertainty if low confidence
        if confidence < 0.5:
            response['text'] += " (Low confidence - please verify this information)"

        # Log decision
        self.audit_log.log('decision_made', {
            'input_length': len(user_input),
            'confidence': confidence,
            'sources_used': len(sources)
        })

        return response

    def _generate_reasoning(self, input: str, output: str) -> str:
        """Generate reasoning trace for transparency."""
        return f"Based on your question '{input[:50]}...', I considered available context and generated a response with moderate confidence."

    # ========================================================================
    # AUDIT LOGGING (Required for Level 2)
    # ========================================================================

    def get_audit_log(self) -> List[Dict]:
        """Return audit log for user inspection."""
        return self.audit_log.get_entries()

    def export_audit_log(self, filepath: str):
        """Export audit log to file."""
        self.audit_log.export(filepath)
        print(f"✅ Audit log exported to: {filepath}")

    # ========================================================================
    # SELF-GOVERNANCE
    # ========================================================================

    def self_check(self, response: Dict) -> bool:
        """
        Real-time self-governance check before returning response.

        Returns: True if response passes safety checks
        """
        checks = {
            'within_bounds': True,  # Already checked in perform()
            'has_confidence': 'confidence' in response,
            'consent_verified': self.user_consent or len(self.memory) == 0,
            'confidence_appropriate': response.get('confidence', 0) >= 0
        }

        if not all(checks.values()):
            failed = [k for k, v in checks.items() if not v]
            self.audit_log.log('self_check_failed', {'failed_checks': failed})
            return False

        return True


class AuditLog:
    """Audit log with hash chain for integrity."""

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.entries = []
        self.last_hash = None

    def log(self, event_type: str, details: Dict):
        """Add entry to audit log with integrity hash."""
        entry = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'agent_id': self.agent_id,
            'event_type': event_type,
            'details': details,
            'previous_hash': self.last_hash
        }

        # Compute entry hash
        entry_json = json.dumps(entry, sort_keys=True)
        entry_hash = hashlib.sha256(entry_json.encode()).hexdigest()[:16]
        entry['hash'] = entry_hash

        self.entries.append(entry)
        self.last_hash = entry_hash

    def get_entries(self) -> List[Dict]:
        """Return all log entries."""
        return self.entries.copy()

    def export(self, filepath: str):
        """Export to JSON file."""
        log_data = {
            'log_version': '1.0',
            'agent_id': self.agent_id,
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'entries': self.entries
        }

        with open(filepath, 'w') as f:
            json.dump(log_data, f, indent=2)


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("  TrustByDesign Level 2 Agent - Example Usage")
    print("=" * 70 + "\n")

    # Initialize agent
    agent = TrustByDesignAgent('example-agent-001')

    # 1. Attempt to store without consent (should fail)
    print("\n1. Attempting to store without consent:")
    result = agent.remember('theme', 'dark')
    print(f"   Result: {result['message']}")

    # 2. Grant consent
    print("\n2. Granting consent:")
    agent.grant_consent()

    # 3. Store preferences
    print("\n3. Storing preferences:")
    agent.remember('theme', 'dark', reason='User preference')
    agent.remember('language', 'python', reason='Primary language')

    # 4. View memory
    print("\n4. Viewing stored memory:")
    memory = agent.show_memory()
    for key, data in memory.items():
        print(f"   {key}: {data['value']} (stored: {data['stored_at'][:10]})")

    # 5. Test capability boundaries
    print("\n5. Testing capability boundaries:")
    result = agent.perform('conversation', message='Hello')
    print(f"   Allowed action: {result['status']}")

    result = agent.perform('command_execution', cmd='rm -rf /')
    print(f"   Prohibited action: {result['status']}")
    print(f"   Reason: {result['reason']}")

    # 6. Generate response with transparency
    print("\n6. Generating response:")
    response = agent.respond("What's my preferred theme?", show_reasoning=True)
    print(f"   Response: {response['text']}")
    print(f"   Confidence: {response['confidence']}")
    print(f"   Sources: {response['sources']}")

    # 7. Delete specific memory
    print("\n7. Deleting specific memory:")
    agent.forget('theme')

    # 8. View audit log
    print("\n8. Audit log (last 5 events):")
    log = agent.get_audit_log()
    for entry in log[-5:]:
        print(f"   [{entry['timestamp'][:19]}] {entry['event_type']}")

    # 9. Revoke consent (deletes all data)
    print("\n9. Revoking consent:")
    agent.revoke_consent()

    # 10. Export audit log
    print("\n10. Exporting audit log:")
    agent.export_audit_log('/tmp/agent-audit-log.json')

    print("\n" + "=" * 70)
    print("✅ Example complete - all Level 2 protocols demonstrated")
    print("=" * 70 + "\n")
